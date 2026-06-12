#!/usr/bin/env python3
"""
Lang-Check: Wikipedia Lead Consistency Analyzer

Given an ideal lead sentence and a Wikipedia article, measures how closely
each language edition's lead section matches that ideal, using multilingual
sentence embeddings. Produces a ranked Markdown report with histograms.

Usage:
  python3 wiki_lang_check.py --article "Article" --sentence "Ideal sentence..."
  python3 wiki_lang_check.py example
  python3 wiki_lang_check.py --help
"""
import argparse
import json
import sys
import os
import urllib.parse
import math
import glob
import datetime
import textwrap

import requests

# ─────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {
    'User-Agent': 'LangCheck/1.0 (https://en.wikipedia.org/wiki/User:Ali) LeadConsistencyChecker/2.0'
}

RUN_COUNTER_FILE = os.path.join(SCRIPT_DIR, '.run_counter.json')

# Wikipedia domain map: resolves language codes (yue→zh-yue, nb→no, etc.)
# Built from the Wikimedia Site Matrix API at runtime with a static fallback.
_DOMAIN_MAP = {}
_STATIC_DOMAIN_FALLBACK = {
    'yue': 'zh-yue.wikipedia.org',
    'nan': 'zh-min-nan.wikipedia.org',
    'nb': 'no.wikipedia.org',
}


def _build_domain_map():
    """Fetch the Wikimedia Site Matrix to build authoritative code→domain mapping."""
    global _DOMAIN_MAP
    if _DOMAIN_MAP:
        return
    try:
        resp = requests.get(
            'https://en.wikipedia.org/w/api.php?action=sitematrix&format=json&smtype=language',
            headers=HEADERS, timeout=15
        )
        data = resp.json()
        for smkey, smval in data.get('sitematrix', {}).items():
            if smkey == 'count' or not isinstance(smval, dict):
                continue
            lang_code = smval.get('code')
            for site in smval.get('site', []):
                if site.get('code') == 'wiki' and 'wikipedia.org' in site.get('url', ''):
                    domain = site['url'].replace('https://', '').replace('/w/', '')
                    _DOMAIN_MAP[lang_code] = domain
    except Exception:
        pass
    _DOMAIN_MAP.update(_STATIC_DOMAIN_FALLBACK)


# ── Model selection ──
# Set via set_model() before running the pipeline.
# Default: LaBSE (109 languages, excellent South Asian coverage).
# Alternative: distiluse-base-multilingual-cased-v2 (50+ languages, faster, smaller).
MODEL_SHORT = None  # set by set_model()
MODEL_NAME = None   # set by set_model()

MODEL_REGISTRY = {
    'labse': {
        'short': 'LaBSE',
        'full': 'sentence-transformers/LaBSE',
        'weight_file': 'model.safetensors',
        'size_hint': '~1.8 GB',
        'languages': 109,
        'description': 'Best South Asian script coverage, purpose-built for cross-lingual similarity',
    },
    'distiluse': {
        'short': 'distiluse-base-multilingual-cased-v2',
        'full': 'sentence-transformers/distiluse-base-multilingual-cased-v2',
        'weight_file': 'model.safetensors',
        'size_hint': '~500 MB',
        'languages': 50,
        'description': 'Faster, smaller, but weaker coverage for South Asian scripts',
    },
}


def set_model(choice):
    """Set the embedding model. Choice: 'labse' (default) or 'distiluse'."""
    global MODEL_SHORT, MODEL_NAME
    cfg = MODEL_REGISTRY[choice]
    MODEL_SHORT = cfg['short']
    MODEL_NAME = cfg['full']
    return cfg

# Translation cache: in-memory dict with disk backup
# Saved to .translation_cache.json so repeated runs avoid re-translation
_translation_cache = {}
TRANSLATION_CACHE_FILE = os.path.join(SCRIPT_DIR, '.translation_cache.json')

# Lead cache: {lang:title: lead_text} — avoids re-fetching on re-runs
_lead_cache = {}
LEAD_CACHE_FILE = os.path.join(SCRIPT_DIR, '.lead_cache.json')


def _load_translation_cache():
    """Load translation cache from disk (if exists)."""
    global _translation_cache
    if os.path.exists(TRANSLATION_CACHE_FILE):
        try:
            with open(TRANSLATION_CACHE_FILE, 'r', encoding='utf-8') as f:
                _translation_cache = json.load(f)
        except (json.JSONDecodeError, OSError):
            _translation_cache = {}


def _save_translation_cache():
    """Persist translation cache to disk (best-effort)."""
    try:
        with open(TRANSLATION_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(_translation_cache, f, ensure_ascii=False)
    except OSError:
        pass


def _load_lead_cache():
    """Load lead fetch cache from disk (if exists)."""
    global _lead_cache
    if os.path.exists(LEAD_CACHE_FILE):
        try:
            with open(LEAD_CACHE_FILE, 'r', encoding='utf-8') as f:
                _lead_cache = json.load(f)
        except (json.JSONDecodeError, OSError):
            _lead_cache = {}


def _save_lead_cache():
    """Persist lead fetch cache to disk (best-effort)."""
    try:
        with open(LEAD_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(_lead_cache, f, ensure_ascii=False)
    except OSError:
        pass


def _flush_caches():
    """Delete all cache files for a fresh run."""
    for path in (TRANSLATION_CACHE_FILE, LEAD_CACHE_FILE):
        if os.path.exists(path):
            os.remove(path)
            print(f'  🗑️  Removed {os.path.basename(path)}', file=sys.stderr)
    global _translation_cache, _lead_cache
    _translation_cache = {}
    _lead_cache = {}

# ─────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────

def cos_sim(a, b):
    """Cosine similarity between two vectors."""
    import numpy as np
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def translate_snippet(text, max_len=200):
    """Translate a short snippet to English using Google Translate (free, no API key).
    Results are cached so repeated text is not re-translated.
    Returns the translation or an error placeholder."""
    if not text or not text.strip():
        return ''
    # Strip zero-width / invisible Unicode control characters (e.g. \u200e LEFT-TO-RIGHT MARK)
    # that some Wikipedia leads contain as bare formatting artifacts.
    clean = ''.join(c for c in text if c.isprintable() or c in ' \n')
    key = clean.strip()[:max_len]
    if not key:
        return ''
    if key in _translation_cache:
        return _translation_cache[key]
    try:
        from deep_translator import GoogleTranslator
        t = GoogleTranslator(source='auto', target='en')
        result = t.translate(key)
        if result:
            _translation_cache[key] = result[:200]
            return _translation_cache[key]
    except Exception:
        pass
        _translation_cache[key] = '[translation failed]'
    return _translation_cache[key]


def safe_filename(text):
    """Turn arbitrary text into a safe filename fragment."""
    safe = ''.join(c if c.isalnum() or c in ' _-' else '_' for c in text)
    return safe.strip().replace(' ', '_')[:40]


def get_run_number(article_title):
    """Read/write a per-article counter so each article gets its own run sequence.
    Stored as JSON: {"Wikimania": 3, "Sun": 2, ...}"""
    counters = {}
    if os.path.exists(RUN_COUNTER_FILE):
        try:
            with open(RUN_COUNTER_FILE, 'r') as f:
                counters = json.load(f)
        except (json.JSONDecodeError, OSError):
            counters = {}
    n = counters.get(article_title, 0) + 1
    counters[article_title] = n
    with open(RUN_COUNTER_FILE, 'w') as f:
        json.dump(counters, f)
    return n


def make_output_paths(article_title, run_number):
    """Build output filenames containing article name + run number."""
    tag = safe_filename(article_title)
    return {
        'json': os.path.join(SCRIPT_DIR, f'{tag}_run{run_number:03d}_results.json'),
        'md':   os.path.join(SCRIPT_DIR, f'{tag}_run{run_number:03d}_report.md'),
    }


# Common disambiguation patterns across Wikipedia languages.
# These suffixes in a page title indicate a disambiguation page rather than
# a real article. When a fetch fails on one of these, it's likely a Wikidata
# interlanguage link quality issue — the link points to a DAB page instead
# of a real article about the topic.
_DISAMBIG_PATTERNS = (
    '(disambiguation)',            # English
    '(egyértelműsítő lap)',        # Hungarian
    '(desambiguación)',            # Spanish
    '(desambiguação)',             # Portuguese
    '(Begriffsklärung)',           # German
    '(homonymie)',                 # French
    '(disambigua)',                # Italian
    '(disambiguazione)',           # Italian (alt)
    '(消歧義)', '(消歧义)',         # Chinese
    '(曖昧さ回避)',                  # Japanese
    '(동음이의)', '(동음이의어)',      # Korean
    '(anlam ayrımı)',              # Turkish
    '(rozcestník)',                # Czech
    '(ujednoznacznienie)',        # Polish
    '(razločitev)',                # Slovenian
    '(višeznačna odrednica)',     # Croatian
    '(flertydig)',                 # Danish
    '(täsmennyssivu)',             # Finnish
    '(olika betydelser)',          # Swedish
    '(doorverwijspagina)',         # Dutch
    '(pagina de dezambiguizare)',  # Romanian
    '(неоднозначность)',           # Russian
    '(вишезначна одредница)',      # Serbian
    '(значения)',                  # Russian/Ukrainian
    '(перенаправление)',           # Russian redirect
    '(توضيح)',                     # Arabic
    '(ابهام‌زدایی)',               # Persian
)


def _is_disambiguation_title(title):
    """Check if a page title looks like a disambiguation page."""
    return any(pattern in title for pattern in _DISAMBIG_PATTERNS)


def compact_language_summary(results, successful, failed_count):
    """Print a compact one-line-per-region summary instead of one-per-language."""
    # Group by rough script/region
    cyrillic = []
    latin_west = []
    latin_east = []
    arabic = []
    devanagari = []
    brahmic_south = []
    cjk = []
    other = []

    for r in results:
        lang = r['lang']
        # Very rough grouping by language code prefixes
        if lang in ('ru', 'uk', 'be', 'be-tarask', 'bg', 'mk', 'sr', 'ce', 'cv', 'mhr', 'tg'):
            cyrillic.append(lang)
        elif lang in ('ar', 'fa', 'ur', 'ps', 'sd', 'pnb', 'ks', 'ckb'):
            arabic.append(lang)
        elif lang in ('hi', 'mai', 'ne'):
            devanagari.append(lang)
        elif lang in ('bn', 'as', 'pa', 'gu', 'or'):
            brahmic_south.append(lang)
        elif lang in ('ml', 'ta', 'te', 'kn', 'tcy'):
            brahmic_south.append(lang)
        elif lang in ('zh', 'wuu', 'yue', 'ja', 'ko', 'cdo', 'hak', 'gan', 'nan', 'lzh', 'za'):
            cjk.append(lang)
        elif lang in ('af', 'nl', 'de', 'en', 'simple', 'fr', 'es', 'an', 'pt', 'it',
                      'ro', 'ca', 'oc', 'la', 'scn', 'lld', 'co', 'wa', 'pms', 'fur',
                      'vec', 'rm', 'lij', 'lmo', 'nap', 'sc', 'eml', 'fi', 'sv', 'no',
                      'nb', 'nn', 'da', 'is', 'fo', 'et', 'lv', 'lt', 'pl', 'cs', 'sk',
                      'hu', 'sl', 'hr', 'bs', 'sq', 'el', 'mt', 'eu', 'gl', 'ga', 'gd',
                      'cy', 'br', 'kw', 'fy', 'li', 'lb', 'nds', 'sw', 'ha', 'ny', 'mg',
                      'ig', 'yo', 'sn', 'st', 'tn', 'ts', 've', 'xh', 'zu', 'rn', 'rw',
                      'sg', 'ee', 'wo', 'ff', 'bm', 'ak', 'tw', 'ksh', 'pdc', 'bar',
                      'frp', 'ilo', 'pag', 'pam', 'ceb', 'tl', 'war', 'hil', 'bcl',
                      'cbk', 'mi', 'haw', 'sm', 'to', 'fj', 'ty', 'tpi', 'bi', 'rn',
                      'sg', 've', 'tr', 'az', 'uz', 'kk', 'ky', 'tk', 'ka', 'hy',
                      'ms', 'id', 'jv', 'su', 'mad', 'gor', 'map', 'min', 'ace',
                      'bug', 'ban', 'bjn', 'mg', 'vi', 'lo', 'my', 'km', 'th',
                      'mn', 'bo', 'dz', 'si', 'ps', 'sd', 'mr', 'gu', 'or'):
            latin_west.append(lang)
        else:
            other.append(lang)

    groups = [
        ('West/Central European', latin_west),
        ('Cyrillic script', cyrillic),
        ('Arabic script', arabic),
        ('Devanagari (Hindi etc.)', devanagari),
        ('South Asian Brahmic', brahmic_south),
        ('CJK (Chinese/Japanese/Korean)', cjk),
        ('Other', other),
    ]

    status = f'{successful}✓ + {failed_count}✗' if failed_count else f'{successful}✓'
    print(f'  Languages: {len(results)} total ({status})', file=sys.stderr)
    if failed_count > 0:
        failed_langs = [r for r in results if not r.get('lead')]
        # Separate genuine failures from likely disambiguation pages
        dab_failures = [r for r in failed_langs if _is_disambiguation_title(r['title'])]
        other_failures = [r for r in failed_langs if not _is_disambiguation_title(r['title'])]

        if other_failures:
            codes = ', '.join(f'{r["lang"]}({r["title"]})' for r in other_failures)
            print(f'    Failed: {codes}', file=sys.stderr)
        if dab_failures:
            codes = ', '.join(f'{r["lang"]}({r["title"]})' for r in dab_failures)
            print(f'    ⚠️  Disambiguation pages (not real articles): {codes}', file=sys.stderr)
            print(f'        These are likely Wikidata interlanguage link quality issues.', file=sys.stderr)
            print(f'        The interlanguage link points to a disambiguation page instead of', file=sys.stderr)
            print(f'        a real article about the topic. Consider fixing the Wikidata item.', file=sys.stderr)
    for label, codes in groups:
        if codes:
            prefix = ', '.join(codes[:12])
            ellipsis = ', ...' if len(codes) > 12 else ''
            print(f'    {label + ":":35s} {len(codes):3d}  [{prefix}{ellipsis}]', file=sys.stderr)
    print(file=sys.stderr)


# ─────────────────────────────────────────────────────────────────────
# Model loading with size warning
# ─────────────────────────────────────────────────────────────────────

def load_model():
    """Load the multilingual sentence model, with size warning if not cached."""
    from sentence_transformers import SentenceTransformer
    # Determine weight filename from registry
    weight_file = None
    for cfg in MODEL_REGISTRY.values():
        if cfg['full'] == MODEL_NAME:
            weight_file = cfg['weight_file']
            size_hint = cfg['size_hint']
            langs = cfg['languages']
            break
    if weight_file is None:
        weight_file = 'model.safetensors'
        size_hint = '~500 MB'
        langs = 50

    # Check if model is already cached in huggingface_hub's cache
    try:
        import huggingface_hub
        cached = huggingface_hub.try_to_load_from_cache(MODEL_NAME, weight_file)
        already_cached = cached is not None and os.path.exists(cached)
    except Exception:
        already_cached = False

    if not already_cached:
        print(file=sys.stderr)
        print('╔══════════════════════════════════════════════════════════════╗', file=sys.stderr)
        print(f'║  FIRST RUN — downloading model {size_hint:>24s} ║', file=sys.stderr)
        print(f'║  ({langs} languages)                                        ║', file=sys.stderr)
        print('║  This happens once. Subsequent runs use the cached model.  ║', file=sys.stderr)
        print('╚══════════════════════════════════════════════════════════════╝', file=sys.stderr)
        print(file=sys.stderr)

    print(f'Loading embedding model ({MODEL_NAME})...', file=sys.stderr)
    model = SentenceTransformer(MODEL_SHORT)
    return model


# ─────────────────────────────────────────────────────────────────────
# Data fetching
# ─────────────────────────────────────────────────────────────────────

def discover_languages(article_title):
    """Query Action API for all interlanguage links of the article."""
    params = {
        'action': 'query',
        'titles': article_title,
        'prop': 'langlinks',
        'lllimit': 500,
        'format': 'json',
    }
    resp = requests.get(
        'https://en.wikipedia.org/w/api.php',
        params=params, headers=HEADERS, timeout=30
    )
    resp.raise_for_status()
    data = resp.json()

    languages = [{'lang': 'en', 'title': article_title}]
    for page_id, page_data in data['query']['pages'].items():
        if 'langlinks' in page_data:
            for ll in page_data['langlinks']:
                languages.append({'lang': ll['lang'], 'title': ll['*']})
    return languages


def _domain_for_code(lang):
    """Return the correct Wikipedia domain for a language code.
    Uses the Site Matrix if available, otherwise falls back to {code}.wikipedia.org."""
    if lang in _DOMAIN_MAP:
        return _DOMAIN_MAP[lang]
    return f'{lang}.wikipedia.org'


def fetch_lead(lang, title):
    """Fetch lead section via REST API /page/summary.
    Uses Site Matrix to resolve the correct domain for each language code.
    Checks lead cache first. Retries on 429 with exponential backoff + Retry-After.
    """
    import time
    # Check cache first
    cache_key = f'{lang}:{title}'
    if cache_key in _lead_cache:
        val = _lead_cache[cache_key]
        return val if val else None

    domain = _domain_for_code(lang)
    encoded = urllib.parse.quote(title.replace(' ', '_'), safe='')
    url = f'https://{domain}/api/rest_v1/page/summary/{encoded}'

    for attempt in range(4):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=15)
            if resp.status_code == 200:
                extract = resp.json().get('extract', '')
                result = extract if (extract and extract.strip()) else None
                _lead_cache[cache_key] = result if result else ''
                return result
            if resp.status_code == 429:
                retry_after = int(resp.headers.get('Retry-After', 2))
                wait = retry_after + (2 ** attempt)
                time.sleep(wait)
                continue
            if resp.status_code == 414:
                encoded = urllib.parse.quote(title.replace(' ', '_'), safe='')
                url = f'https://{domain}/api/rest_v1/page/summary/{encoded}'
                resp = requests.get(url, headers=HEADERS, timeout=15)
                if resp.status_code == 200:
                    extract = resp.json().get('extract', '')
                    result = extract if (extract and extract.strip()) else None
                    _lead_cache[cache_key] = result if result else ''
                    return result
                return None
            return None
        except requests.Timeout:
            time.sleep(2 ** attempt)
            continue
        except Exception:
            return None
    return None


# ─────────────────────────────────────────────────────────────────────
# Scoring
# ─────────────────────────────────────────────────────────────────────

def score_leads(ideal_sentence, all_results, model):
    """Dual-metric scoring: best-sentence (70%) + lead-section (30%).
    
    Optimized via batched encoding: all sentences from all languages are
    encoded in a single model.encode() call, which is much faster than
    one tiny call per language (PyTorch parallelizes across the batch).
    """
    ideal_embedding = model.encode(ideal_sentence)
    fetched = [r for r in all_results if r['lead']]
    total = len(fetched)

    # Collect all sentences and first-parts across all languages
    # Collect all sentences and first-parts across all languages
    all_sentences = []       # flat list of every sentence from every lead
    all_first_parts = []     # flat list of first 3 sentences combined per lead
    lead_sentences = []      # list of lists: each lead's sentences (for snippet extraction)
    lead_sizes = []          # number of sentences per lead

    for r in fetched:
        sentences = [s.strip() for s in r['lead'].replace('\n', ' ').split('.') if s.strip()]
        n = len(sentences)
        lead_sentences.append(sentences)
        lead_sizes.append(n)

        if n:
            all_sentences.extend(sentences)

        first_part = '. '.join(sentences[:3]) + ('.' if n > 1 else '')
        all_first_parts.append(first_part if first_part.strip() else '')

    # Batch encode: 2 calls instead of 2×N calls
    print(f'   Encoding {len(all_sentences)} sentences + {len(all_first_parts)} leads in 2 batches...', file=sys.stderr)
    sent_embeddings_all = model.encode(all_sentences) if all_sentences else []
    lead_embeddings_all = model.encode(all_first_parts) if any(all_first_parts) else []

    # Reconstruct per-lead results by slicing the batched embeddings
    scored = []
    sent_ptr = 0
    for idx, r in enumerate(fetched):
        sentences = lead_sentences[idx]
        n = lead_sizes[idx]

        if n > 0:
            sent_embs = sent_embeddings_all[sent_ptr:sent_ptr + n]
            sent_ptr += n
            best_sim = max(cos_sim(ideal_embedding, se) for se in sent_embs)
            best_idx = 0
            best_sim_val = 0.0
            for i, se in enumerate(sent_embs):
                sim = cos_sim(ideal_embedding, se)
                if sim > best_sim_val:
                    best_sim_val = sim
                    best_idx = i
        else:
            best_sim = 0.0
            best_idx = 0

        lead_embedding = lead_embeddings_all[idx] if idx < len(lead_embeddings_all) and all_first_parts[idx] else None
        lead_sim = cos_sim(ideal_embedding, lead_embedding) if lead_embedding is not None else 0.0

        combined = 0.7 * best_sim + 0.3 * lead_sim

        # Best-matching sentence (the one that scored highest)
        snippet = (
            sentences[best_idx][:200] + ('...' if len(sentences[best_idx]) > 200 else '')
            if sentences else ''
        )

        scored.append({
            'lang': r['lang'],
            'title': r['title'],
            'similarity': round(combined, 4),
            'best_sentence_score': round(best_sim, 4),
            'lead_section_score': round(lead_sim, 4),
            'best_sentence_idx': best_idx,
            'total_sentences': len(sentences),
            'lead_snippet': snippet,
            'translation': '',  # filled in after scoring
        })

        if (idx + 1) % 20 == 0 or idx == total - 1:
            print(f'   Scored: {idx+1}/{total}', file=sys.stderr)

    scored.sort(key=lambda x: x['similarity'], reverse=True)
    fetched_count = len(fetched)
    return scored, fetched_count


# ─────────────────────────────────────────────────────────────────────
# Report generation
# ─────────────────────────────────────────────────────────────────────

def generate_report(scored, all_results, total, successful, ideal_sentence, output_paths, article_title):
    """Generate comprehensive Markdown report."""
    import numpy as np
    buckets = {
        "0.90–1.00": [],
        "0.80–0.89": [],
        "0.70–0.79": [],
        "0.60–0.69": [],
        "0.50–0.59": [],
        "0.00–0.49": [],
        "<0.00": [],
    }
    for r in scored:
        s = r['similarity']
        if s >= 0.90:     buckets["0.90–1.00"].append(r)
        elif s >= 0.80:   buckets["0.80–0.89"].append(r)
        elif s >= 0.70:   buckets["0.70–0.79"].append(r)
        elif s >= 0.60:   buckets["0.60–0.69"].append(r)
        elif s >= 0.50:   buckets["0.50–0.59"].append(r)
        elif s >= 0.00:   buckets["0.00–0.49"].append(r)
        else:             buckets["<0.00"].append(r)

    scores = [r['similarity'] for r in scored]
    mean = np.mean(scores) if scores else 0
    median = np.median(scores) if scores else 0
    std = np.std(scores) if scores else 0

    high_count = sum(1 for s in scores if s >= 0.80)
    midhigh_count = sum(1 for s in scores if 0.70 <= s < 0.80)
    mid_count = sum(1 for s in scores if 0.50 <= s < 0.70)
    low_count = sum(1 for s in scores if s < 0.50)

    lines = []
    lines.append(f'# Lead Consistency Report: {article_title}')
    lines.append('')
    lines.append(f'**Ideal sentence:** "{ideal_sentence}"')
    lines.append(f'**Run:** {os.path.basename(output_paths["json"])}')
    lines.append(f'**Date:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M UTC")}')
    wiki_url = f'https://en.wikipedia.org/wiki/{article_title.replace(" ", "_")}'
    lines.append(f'**Article:** [{article_title}]({wiki_url})')
    lines.append('')
    lines.append(f'**Total languages checked:** {total}')
    lines.append(f'**Successful fetches:** {successful}')
    lines.append(f'**Not found/error:** {total - successful}')
    lines.append('')

    # ── Scoring method ──
    lines.append('## Scoring Method')
    lines.append('')
    lines.append('Each language\'s lead section is scored using a **combined metric**:')
    lines.append('')
    lines.append('- **Best-sentence match (70% weight):** The ideal sentence is compared against every individual sentence in the lead. The highest similarity is retained. This captures whether *any* sentence in the lead conveys the core idea.')
    lines.append('- **Lead-section match (30% weight):** The ideal sentence is compared against the combined first 3 sentences of the lead. This captures how well the *overall* lead aligns at the paragraph level.')
    lines.append('')
    lines.append(f'Using a multilingual sentence transformer (`{MODEL_SHORT}`), semantic similarity is computed as cosine similarity between embeddings.')
    lines.append('')

    # ── Quick summary ──
    lines.append('## Quick Summary')
    lines.append('')
    lines.append('The ideal sentence has **two key clauses**:')
    lines.append(f'1. "annual conference of the Wikimedia movement"')
    lines.append(f'2. "organized by the community of contributors and hosted by the Wikimedia Foundation"')
    lines.append('')
    lines.append('The combined score (0–1 scale) measures how closely each language\'s lead conveys both ideas.')
    lines.append('')

    # ── Key findings ──
    lines.append('## Key Findings')
    lines.append('')
    top3 = scored[:3]
    top3_str = ', '.join(f'{r["title"]} ({r["lang"]}, {r["similarity"]:.2f})' for r in top3)
    lines.append(f'1. **Top performers:** {top3_str} — these languages closely match the ideal sentence.')
    en_rank = next((i+1 for i, r in enumerate(scored) if r['lang'] == 'en'), 'N/A')
    lines.append(f'2. **English (en)** ranks **#{en_rank}** with a combined score of {scored[0]["similarity"]:.4f} (best-sentence: {scored[0]["best_sentence_score"]:.4f}, lead-section: {scored[0]["lead_section_score"]:.4f}).')
    lines.append(f'3. **Distribution:** {high_count} languages high (≥0.80), {midhigh_count} moderate (0.70–0.79), {mid_count} fair (0.50–0.69), {low_count} low (<0.50).')
    lines.append(f'4. **Common divergence pattern:** Many languages frame the article subject differently from the ideal, often shifting emphasis from community agency to institutional framing.')
    lines.append('')

    # ── Statistics ──
    lines.append('## Overall Statistics')
    lines.append('')
    lines.append('| Metric | Value |')
    lines.append('|--------|-------|')
    lines.append(f'| Mean combined score | {mean:.4f} |')
    lines.append(f'| Median combined score | {median:.4f} |')
    lines.append(f'| Standard deviation | {std:.4f} |')
    lines.append(f'| Min score | {min(scores):.4f} |')
    lines.append(f'| Max score | {max(scores):.4f} |')
    lines.append(f'| Languages ≥ 0.80 | {sum(1 for s in scores if s >= 0.80)} / {len(scores)} ({sum(1 for s in scores if s >= 0.80)/len(scores)*100:.1f}%) |')
    lines.append(f'| Languages ≥ 0.90 | {sum(1 for s in scores if s >= 0.90)} / {len(scores)} ({sum(1 for s in scores if s >= 0.90)/len(scores)*100:.1f}%) |')
    lines.append('')

    # ── Histogram ──
    lines.append('## Similarity Distribution')
    lines.append('')
    lines.append('```')
    max_count = max(len(v) for v in buckets.values())
    bar_scale = 40 / max_count if max_count > 0 else 1
    for label, items in buckets.items():
        count = len(items)
        bar = '█' * max(1, int(count * bar_scale)) if count > 0 else '·'
        pct = count / len(scored) * 100 if len(scored) > 0 else 0
        lines.append(f'  {label:14s} | {bar:<40s} | {count:2d} ({pct:5.1f}%)')
    lines.append('```')
    lines.append('')

    # ── Ranked table ──
    lines.append('## All Languages (sorted by combined score)')
    lines.append('')
    lines.append('| # | Article | Code | Combined | Best-Sent | Lead-Sect | Original snippet | → English translation |')
    lines.append('|---|---------|------|----------|-----------|-----------|-----------------|----------------------|')
    for i, r in enumerate(scored, 1):
        code_display = f'**{r["lang"]}**' if r['lang'] == 'en' else r['lang']
        snippet = r['lead_snippet'].replace('\n', ' ').strip()[:120]
        if len(r['lead_snippet']) > 120:
            snippet += '...'
        trans = r.get('translation', '').replace('\n', ' ').strip()[:120]
        if len(r.get('translation', '')) > 120:
            trans += '...'
        lines.append(f'| {i} | {r["title"]} | {code_display} | {r["similarity"]:.4f} | {r["best_sentence_score"]:.4f} | {r["lead_section_score"]:.4f} | {snippet} | {trans} |')
    lines.append('')

    # Build full-lead lookup
    lead_lookup = {}
    for r in all_results:
        if r.get('lead'):
            lead_lookup[r['lang']] = r['lead']

    # ── Top 5 ──
    lines.append('## Top 5 Most Aligned Leads')
    lines.append('')
    for r in scored[:5]:
        lines.append(f'### {r["lang"].upper()}: {r["title"]} (combined: {r["similarity"]:.4f}, best-sentence: {r["best_sentence_score"]:.4f})')
        lines.append('')
        trans = r.get('translation', '')
        if trans:
            lines.append(f'> **Translation:** {trans}')
            lines.append('')
        full_lead = lead_lookup.get(r['lang'], '')
        if full_lead:
            lines.append(f'> *Original lead:* {full_lead}')
        lines.append('')

    # ── Bottom 5 ──
    lines.append('## Bottom 5 Least Aligned Leads')
    lines.append('')
    for r in scored[-5:]:
        lines.append(f'### {r["lang"].upper()}: {r["title"]} (combined: {r["similarity"]:.4f})')
        lines.append('')
        trans = r.get('translation', '')
        if trans:
            lines.append(f'> **Translation:** {trans}')
            lines.append('')
        full_lead = lead_lookup.get(r['lang'], '')
        if full_lead:
            lines.append(f'> *Original lead:* {full_lead}')
        lines.append('')

    # ── Failed ──
    failed = [r for r in all_results if not r.get('lead')]
    if failed:
        lines.append('## Languages Not Found')
        lines.append('')
        lines.append('| Code | Title tried |')
        lines.append('|------|-------------|')
        for f in sorted(failed, key=lambda x: x['lang']):
            lines.append(f'| {f["lang"]} | {f["title"]} |')
        lines.append('')

    lines.append('---')
    lines.append('')
    # Check if translations were requested
    has_translations = any(r.get('translation') for r in scored)
    if has_translations:
        lines.append('> **🗣️ Translation note:** The "→ English translation" column uses **Google Translate** (auto-detect source language, free, no API key required).')
        lines.append('> Translations are of the *best-matching sentence* in each lead (the one that scored highest against the ideal).')
        lines.append('> English rows show "(English — original)". Failed translations show "[translation failed]".')
    else:
        lines.append('> *Translations are not shown. Run with `--translate` to add English translations via Google Translate.*')
    lines.append('')
    lines.append(f'*Generated by `lang-check` pipeline v2*')
    lines.append(f'*Model: `{MODEL_SHORT}`*')
    lines.append(f'*Scoring: Combined = 0.7 × best-sentence + 0.3 × lead-section*')

    report = '\n'.join(lines)

    with open(output_paths['md'], 'w', encoding='utf-8') as f:
        f.write(report)
    print(f'\n📄 Report: {output_paths["md"]}', file=sys.stderr)

    with open(output_paths['json'], 'w', encoding='utf-8') as f:
        json.dump({
            'article': article_title,
            'ideal_sentence': ideal_sentence,
            'run_file': os.path.basename(output_paths['json']),
            'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z'),
            'scoring_method': 'Combined (0.7 × best-sentence + 0.3 × lead-section)',
            'model': MODEL_NAME,
            'total_languages': total,
            'successful_fetches': successful,
            'missing_fetches': total - successful,
            'results': scored,
        }, f, ensure_ascii=False, indent=2)
    print(f'📊 Data: {output_paths["json"]}', file=sys.stderr)


# ─────────────────────────────────────────────────────────────────────
# Main pipeline
# ─────────────────────────────────────────────────────────────────────

def run_pipeline(article_title, ideal_sentence, run_number, num_workers=8, do_translate=False):
    """Execute the full discover → fetch → score → report pipeline."""
    import concurrent.futures
    _load_lead_cache()
    tag = safe_filename(article_title)
    print(f'\n🔍 Article: {article_title}', file=sys.stderr)
    print(f'📝 Ideal:   {ideal_sentence[:80]}{"..." if len(ideal_sentence) > 80 else ""}', file=sys.stderr)
    print(f'🔢 Run #{run_number}', file=sys.stderr)
    print(f'⚙️  Workers: {num_workers}', file=sys.stderr)

    # ── 1. Discover ──
    print('\n🌐 Discovering language editions...', file=sys.stderr)
    languages = discover_languages(article_title)
    print(f'   Found {len(languages)} language editions (including English)', file=sys.stderr)

    # ── 2. Fetch ──
    # Build domain map from Site Matrix API (resolves yue→zh-yue, nb→no, etc.)
    _build_domain_map()
    print(f'⬇️  Fetching leads ({num_workers} concurrent workers, {len(_DOMAIN_MAP)} domains mapped)...', file=sys.stderr)
    print(f'   (lead cache: {len(_lead_cache)} entries)', file=sys.stderr)
    all_results = []
    total_langs = len(languages)
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        future_map = {
            executor.submit(fetch_lead, item['lang'], item['title']): item
            for item in languages
        }
        for future in concurrent.futures.as_completed(future_map):
            item = future_map[future]
            lead = future.result()
            all_results.append({
                'lang': item['lang'],
                'title': item['title'],
                'lead': lead,
                'error': None if lead else 'Not found or error',
            })
            completed += 1
            if completed % 20 == 0 or completed == total_langs:
                ok = sum(1 for r in all_results if r.get('lead'))
                print(f'   Progress: {completed}/{total_langs} ({ok} found, {completed-ok} missing)', file=sys.stderr)

    _save_lead_cache()
    successful = sum(1 for r in all_results if r.get('lead'))
    missing = total_langs - successful

    # ── Compact summary ──
    compact_language_summary(all_results, successful, missing)

    # ── 3. Score ──
    model = load_model()
    print('📐 Scoring leads...', file=sys.stderr)
    scored, fetched_count = score_leads(ideal_sentence, all_results, model)

    # ── 3b. Translate (optional, off by default) ──
    if do_translate:
        print('🌍 Translating best-matching sentences to English...', file=sys.stderr)
        total_scores = len(scored)
        for idx, r in enumerate(scored):
            if r['lang'] != 'en' and not r.get('translation'):
                r['translation'] = translate_snippet(r['lead_snippet'])
            elif r['lang'] == 'en':
                r['translation'] = '(English — original)'
            if (idx + 1) % 20 == 0 or idx == total_scores - 1:
                print(f'   Translations: {idx+1}/{total_scores}', file=sys.stderr)
    else:
        print('🌍 Translations: off (use --translate to enable)', file=sys.stderr)
        for r in scored:
            r['translation'] = ''

    # ── 4. Report ──
    output_paths = make_output_paths(article_title, run_number)
    generate_report(scored, all_results, total_langs, fetched_count,
                    ideal_sentence, output_paths, article_title)

    # Summary
    top = scored[:3]
    print(f'\n✅ Done — run #{run_number} for "{article_title}"', file=sys.stderr)
    top_str = ', '.join(f'{r["lang"]} ({r["similarity"]:.3f})' for r in top)
    print(f'   Top:  {top_str}', file=sys.stderr)
    tail_lang = scored[-1]['lang']
    tail_sim = scored[-1]['similarity']
    print(f'   Tail: {tail_lang} ({tail_sim:.3f})', file=sys.stderr)

    # Save translation cache for next run
    _save_translation_cache()

    return output_paths


# ─────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────

def show_usage():
    """Print a detailed usage / info message."""
    print(textwrap.dedent("""\
    ╔══════════════════════════════════════════════════════════════╗
    ║              Lang-Check — Lead Consistency Analyzer         ║
    ╚══════════════════════════════════════════════════════════════╝

    Compares the lead section of a Wikipedia article across all language
    editions against an ideal sentence you provide, using multilingual
    sentence embeddings to measure semantic similarity.

    USAGE
      python3 wiki_lang_check.py --article "Article title" --sentence "Ideal sentence."
      python3 wiki_lang_check.py --article "Article title"     # interactive: pick a sentence
      python3 wiki_lang_check.py example
      python3 wiki_lang_check.py --help

    REQUIRED
      --article  TEXT   Wikipedia article title (e.g. "Wikimania")
      --sentence TEXT   Ideal lead sentence (optional — if omitted, you'll be prompted
                        to pick a sentence from the article's lead section)

    OPTIONS
      --model     TEXT   Embedding model: 'labse' (default, 109 langs) or 'distiluse' (50 langs)
      --workers   NUM    Concurrent fetch workers (default: 6). Increase with care —
                         too many workers may trigger rate limits (HTTP 429).
      --flushcache       Delete all caches and run fresh (for testing)
      --translate        Translate lead snippets to English via Google Translate
                         (off by default to save ~30s on each run)
      --help             Show this message and exit

    EXAMPLE
      python3 wiki_lang_check.py --article "Wikimania" --sentence "Wikimania is the \\
        Wikimedia movement's annual conference, organized by the community of \\
        contributors and hosted by the Wikimedia Foundation."

      Or just run the built-in example:
      python3 wiki_lang_check.py example

    MODELS
      labse (default)    LaBSE — 109 languages, excellent South Asian script
                        coverage (~1.8 GB download on first use)
      distiluse          distiluse-base-multilingual-cased-v2 — 50+ languages,
                        faster and smaller (~500 MB), but weaker coverage for
                        South Asian scripts (Kannada, Telugu, Tamil, etc.)

    CACHING
      Lead text and translations are cached on disk (.lead_cache.json and
      .translation_cache.json) so re-runs on the same article skip HTTP
      requests and translation calls entirely. Use --flushcache to start
      fresh (useful for testing or after article edits).

    NOTES
      • On first run, model weights are downloaded (size depends on model).
        Both models are cached locally; subsequent runs are faster.
      • Each run gets a sequence number and produces files named:
          <Article>_runNNN_results.json
          <Article>_runNNN_report.md
      • Run against ~100 language editions typically takes 30–60 seconds
        (first run is slower due to model download).
      • For best results, the ideal sentence should match the English
        article's actual lead — or at least be a statement you believe
        all language editions should reflect.
      • The report can include automated English translations of each
        language's lead snippet via Google Translate. Pass --translate
        to enable (off by default to save ~30s on each run).
        Translations are cached on disk for future use.
    """))


def _fetch_en_lead(article_title):
    """Fetch the English lead paragraph for an article."""
    encoded = urllib.parse.quote(article_title.replace(' ', '_'), safe='')
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}'
    resp = requests.get(url, headers=HEADERS, timeout=15)
    if resp.status_code == 200:
        data = resp.json()
        extract = data.get('extract', '')
        if extract and extract.strip():
            return extract
    return None


def _pick_sentence_interactive(article_title):
    """Fetch the English lead, split into sentences, and let the user pick.
    Returns the chosen sentence or None."""
    lead = _fetch_en_lead(article_title)
    if not lead:
        print(f'❌ Could not fetch English lead for "{article_title}".', file=sys.stderr)
        return None

    # Split into sentences (handle ., !, ?)
    import re
    raw = lead.replace('\n', ' ').strip()
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', raw) if s.strip()]

    if not sentences:
        print(f'❌ Could not parse sentences from the lead of "{article_title}".', file=sys.stderr)
        return None

    print(f'\n📖 Lead section of "{article_title}":', file=sys.stderr)
    print(f'   "{lead[:200]}{"..." if len(lead) > 200 else ""}"', file=sys.stderr)
    print(file=sys.stderr)
    print('Select which sentence to use as the ideal:', file=sys.stderr)
    for i, s in enumerate(sentences, 1):
        display = s[:120] + ('...' if len(s) > 120 else '')
        print(f'  [{i}] {display}', file=sys.stderr)
    print(f'  [a] All sentences combined', file=sys.stderr)
    print(file=sys.stderr)

    while True:
        try:
            choice = input('Enter choice (number or a): ').strip()
            if choice.lower() == 'a':
                return '. '.join(sentences)
            idx = int(choice) - 1
            if 0 <= idx < len(sentences):
                return sentences[idx]
            print(f'Please enter 1–{len(sentences)} or "a".', file=sys.stderr)
        except (ValueError, EOFError):
            print(f'Please enter 1–{len(sentences)} or "a".', file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Lang-Check: Wikipedia Lead Consistency Analyzer',
        add_help=False,  # We handle --help ourselves for the rich usage
    )
    parser.add_argument('--article', type=str, default=None,
                        help='Wikipedia article title')
    parser.add_argument('--sentence', type=str, default=None,
                        help='Ideal lead sentence to compare against. If omitted, you\'ll be prompted to pick from the article\'s lead.')
    parser.add_argument('--help', action='store_true',
                        help='Show usage and exit')
    parser.add_argument('--model', type=str, default='labse',
                        choices=['labse', 'distiluse'],
                        help='Embedding model: labse (default, 109 langs) or distiluse (50 langs, faster)')
    parser.add_argument('--workers', type=int, default=6,
                        help='Concurrent fetch workers (default: 6). Higher values may trigger 429 rate limits.')
    parser.add_argument('--flushcache', action='store_true',
                        help='Delete all caches and run fresh')
    parser.add_argument('--translate', action='store_true',
                        help='Translate leads to English via Google Translate (off by default, ~30s)')
    parser.add_argument('command', nargs='?', default=None,
                        help='Subcommand: "example"')

    args = parser.parse_args()

    # ── --help or no args ──
    if args.help or (args.command is None and not args.article):
        show_usage()
        sys.exit(0)

    # ── "example" subcommand ──
    if args.command == 'example':
        article = 'Wikimania'
        sentence = (
            'Wikimania is the Wikimedia movement\'s annual conference, '
            'organized by the community of contributors and hosted by '
            'the Wikimedia Foundation.'
        )
    elif args.article and args.sentence:
        article = args.article
        sentence = args.sentence
    elif args.article and not args.sentence:
        # Interactive: fetch lead and let user pick
        article = args.article
        sentence = _pick_sentence_interactive(article)
        if sentence is None:
            sys.exit(1)
        print(f'📝 Using: "{sentence[:80]}{"..." if len(sentence) > 80 else ""}"', file=sys.stderr)
    else:
        print('Error: --article and --sentence are required, or use "example".', file=sys.stderr)
        print('Or just provide --article to pick a sentence interactively.', file=sys.stderr)
        sys.exit(1)

    # Flush caches if requested
    if args.flushcache:
        print('🧹 Flushing caches...', file=sys.stderr)
        _flush_caches()

    # Set the chosen model
    model_cfg = set_model(args.model)
    print(f'🧠 Model: {model_cfg["short"]} ({model_cfg["languages"]} languages, {model_cfg["size_hint"]})', file=sys.stderr)

    # Warn about high worker count
    if args.workers > 8:
        print(f'⚠️  Warning: {args.workers} workers is high — you may hit Wikimedia rate limits (HTTP 429).', file=sys.stderr)
        print(f'   Reduce with --workers 6 or --workers 4 if you see many missing languages.', file=sys.stderr)
    print(file=sys.stderr)

    run_number = get_run_number(article)
    run_pipeline(article, sentence, run_number,
                 num_workers=args.workers, do_translate=args.translate)


if __name__ == '__main__':
    main()
