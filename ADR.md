# Architecture Decision Record: Lang-Check

## ADR-001: Use Multilingual Sentence Embeddings for Cross-Lingual Similarity

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

We need to compare an English ideal sentence against Wikipedia lead sections written in 90+ different languages. The comparison must be:
- **Semantic** (meaning-based), not lexical (word-matching) — because the same concept is expressed with different vocabulary in different languages
- **Cross-lingual** — the comparison must work across different scripts (Latin, Cyrillic, Arabic, Devanagari, Chinese, etc.)
- **Fast** — scoring 90+ language editions should complete in under a minute
- **Reproducible** — the same input should produce the same scores every time

### Options Considered

1. **Multilingual sentence embeddings (chosen)** — Pre-trained models like `distiluse-base-multilingual-cased-v2` map sentences from 50+ languages into a shared vector space. Cosine similarity in this space measures cross-lingual semantic similarity.

2. **Machine translation + monolingual embeddings** — Translate each language's lead to English (via Google Translate API or similar), then compare using a standard English sentence transformer. This would add API costs, latency, and translation errors.

3. **Character n-gram overlap** — Compute Jaccard similarity of character trigrams between the ideal sentence and each lead. Works across scripts but captures only surface form, not meaning. Two sentences that say the same thing in different words would score low.

4. **Dictionary-based keyword matching** — Extract key terms from the ideal sentence ("Wikimedia movement", "annual conference", "community", "volunteers") and check their presence in each lead via a Wiktionary-translated keyword list. Fragile, incomplete coverage.

### Decision

Use **Option 1**: `sentence-transformers` with the `distiluse-base-multilingual-cased-v2` model.

### Rationale

- **Single model, zero translation APIs** — No external dependencies or costs beyond the model download
- **51 languages in training data** — Covers the vast majority of Wikipedia language editions with >100,000 articles
- **512-dimensional embeddings** — Compact enough for fast computation (~100 sentence pairs in milliseconds)
- **0.5 GB model size** — Reasonable for a developer workstation
- **Deterministic** — Same text always produces the same embedding

### Consequences

**Positive:**
- Simple pipeline: one model, one similarity computation
- No rate limits or API keys needed (unlike translation APIs)
- Fast: ~2 seconds for 90 leads after model loading
- Easy to swap to a different model later (LaBSE, E5, etc.)

**Negative:**
- Model has weak coverage for South Asian Brahmic scripts (Kannada, Telugu, Tamil, Malayalam, Assamese, Bengali, Punjabi, Khmer) — these score near zero despite having reasonable lead text
- Model was trained in 2020; newer models (LaBSE, 2022; E5, 2023) may perform better
- ~1.3 GB total disk usage (PyTorch + model weights)

---

## ADR-002: Dual-Metric Scoring (Best-Sentence + Lead-Section)

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

A Wikipedia lead section typically contains 1–5 sentences. The ideal sentence captures a specific claim or framing. We need to decide how to compare the ideal against a multi-sentence lead.

### Options Considered

1. **Best-sentence match only** — Compare the ideal sentence against each individual sentence in the lead. Take the maximum similarity. This captures whether the claim exists *anywhere* in the lead, ignoring structure.

2. **Lead-section match only** — Concatenate the first N sentences of the lead into a single block and compare against the ideal. This rewards leads that are topically aligned overall but may dilute a single correct sentence with lower-relevance context.

3. **Combined scoring (chosen)** — Weighted average of both approaches: 70% best-sentence + 30% lead-section.

### Decision

Use **Option 3**: `combined_score = 0.7 × best_sentence_sim + 0.3 × lead_section_sim`

### Rationale

- **Best-sentence (70%)** addresses the primary question: "Does this language's lead contain the right information?" A lead that hides the key fact in its third sentence should still score well — the information is there.
- **Lead-section (30%)** provides a structural bonus: a lead that consistently echoes the ideal across multiple sentences should score higher than one that only has one good sentence.
- The weighting favors information presence over structure, which aligns with the tool's purpose (identifying content gaps, not prose quality).

### Consequences

**Positive:**
- Robust to lead structure variations — some languages front-load key facts, others bury them
- Provides sub-scores that help diagnose *why* a language scored low (missing information vs. different framing)
- Easy to explain and tune

**Negative:**
- Adds complexity to the scoring logic (sentence splitting, two-pass encoding)
- The 70/30 split is empirically chosen, not scientifically validated

---

## ADR-003: REST API `/page/summary` for Lead Fetching

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

We need to extract the lead section (first paragraph) of a Wikipedia article in any language edition. The Wikimedia ecosystem offers multiple APIs for this.

### Options Considered

1. **REST API `/page/summary` (chosen)** — Returns a structured JSON with an `extract` field containing the lead paragraph as plain text. No parsing required. Available on `{lang}.wikipedia.org/api/rest_v1/page/summary/{title}`.

2. **Action API `action=parse&section=0`** — Returns the first section (lead) as wikitext or HTML. Requires parsing to extract plain text. More flexible but more complex.

3. **Action API `prop=extracts&exintro`** — Returns a plain-text or limited-HTML extract of the introduction. Similar to REST API but with more parameter options. Requires two API calls (one for langlinks, one for extracts).

### Decision

Use **Option 1**: REST API `/page/summary` for lead fetching.

### Rationale

- **Returns clean text** — No wikitext parsing needed. The `extract` field is human-readable plain text or simple HTML.
- **Built-in redirect resolution** — If the article title redirects, the API returns the canonical page content.
- **Thumbnail + description** — The response includes page description and thumbnail, useful for future enhancements.
- **One API call per language** — Simple parallelization with `concurrent.futures.ThreadPoolExecutor`.

### Consequences

**Positive:**
- Simple, clean data extraction
- Fast: typical response in 200–500ms per language
- Handles most edge cases (redirects, missing pages)

**Negative:**
- For some languages (e.g., tcy with `{{Infobox recurring event}}` as the only content), the extract may be empty even though the page exists
- The summary endpoint may truncate very long leads (capped at ~500 characters in some implementations)
- Fallback needed for languages where the REST API returns 404 but the article exists under a different title

---

## ADR-004: Concurrent HTTP Workers for Lead Fetching

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

With 94 language editions to fetch, sequential HTTP requests would take ~2 minutes (at 200ms/request). Parallel fetching is necessary for acceptable performance.

### Options Considered

1. **`concurrent.futures.ThreadPoolExecutor` (chosen)** — Python's concurrent HTTP with a thread pool. 12 workers.

2. **`asyncio` + `aiohttp`** — Async HTTP for maximum throughput. More efficient but requires different code patterns and an extra dependency.

3. **Subprocess parallelism** — Spawn separate processes for each batch. Heavy and unnecessary for I/O-bound work.

### Decision

Use **Option 1**: `ThreadPoolExecutor` with 12 workers.

### Rationale

- **I/O bound** — HTTP requests spend most of their time waiting for the network, not using the CPU. Threads are ideal for this.
- **Zero additional dependencies** — `concurrent.futures` is in the Python standard library.
- **12 workers** — A balance between speed and Wikimedia's rate limits. With 200ms average response time, 12 workers sustain ~60 requests/second, which is within acceptable limits for short bursts.

### Consequences

**Positive:**
- Fetching 94 languages completes in ~10 seconds
- Simple error handling (each future can independently fail)
- Easy to adjust worker count

**Negative:**
- Python's GIL means CPU-bound work wouldn't benefit, but HTTP I/O is fine
- No built-in rate limiting — could trigger 429s on very fast networks. Mitigated by keeping worker count moderate and respecting Retry-After headers
- Thread overhead for 12 workers is negligible but wouldn't scale to hundreds

---

## ADR-005: Markdown for Reports (Not HTML or PDF)

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

The pipeline needs to output a readable report with tables, histograms, and rich text formatting for sharing via the pi agent, GitHub, or chat applications.

### Options Considered

1. **Markdown (chosen)** — Plain text with lightweight formatting. Readable in terminals, rendered beautifully on GitHub, supported by the pi agent's context.

2. **HTML** — Full visual control (styled tables, bar charts, color). Requires a browser to view properly; not ideal for agent-to-agent communication.

3. **PDF (via LaTeX)** — Professional formatting. High complexity and dependency overhead.

4. **Rich terminal output** — Using libraries like `rich` or `textual`. Great for interactive use but not portable.

### Decision

Use **Option 1**: Pure Markdown with ASCII histograms.

### Rationale

- **Universally readable** — Renders in any Markdown viewer (GitHub, VS Code, terminal `cat`, the pi agent)
- **ASCII histogram** — A block-character bar chart works in any viewer without images or JavaScript
- **GitHub-flavored tables** — Easy to parse and read
- **Zero dependencies** — Report generation is string concatenation

### Consequences

**Positive:**
- Reports can be viewed anywhere without special tools
- Easy to include in pi agent context for continuation
- Simple to extend with additional sections

**Negative:**
- ASCII histograms are less visually refined than SVG/HTML charts
- No interactive filtering or sorting
- Long tables (90+ rows) are cumbersome to scroll through in some viewers

---

## ADR-006: Single Script Architecture (Not Modular Package)

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

The pipeline has four distinct phases (discovery, fetch, score, report). Should these be separated into modules/classes or kept in a single file?

### Options Considered

1. **Single script (chosen)** — All phases in one Python file (`wiki_lang_check.py`), with functions for each phase.

2. **Modular package** — Separate files: `discovery.py`, `fetcher.py`, `scorer.py`, `reporter.py`, with a `main.py` orchestrator.

3. **Piped CLI tools** — `lang-discover | lang-fetch | lang-score | lang-render` as separate CLI commands.

### Decision

Use **Option 1**: Single script with functional decomposition.

### Rationale

- **Prototype velocity** — One file is easier to develop, debug, and run
- **Minimal friction** — No package setup, no `__init__.py`, no import path issues
- **Easy to run** — `python3 wiki_lang_check.py` — no installation, just edit and run
- **All state in one place** — No cross-module state management needed

### Consequences

**Positive:**
- Fast iteration and experimentation
- Easy for non-Python-experts to understand and modify
- Single file deployment (copy + venv setup)

**Negative:**
- Not reusable as a library
- Hard to test individual phases in isolation
- Would need refactoring if the tool grows beyond a single pipeline
- The file is ~300 lines, which is manageable but approaching the threshold for splitting

---

## ADR-008: Google Translate via deep-translator for In-Report Translations

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

The report table shows each language's original lead snippet and a numeric similarity score. Without a translation into English, the user cannot tell *what* the snippet actually says — they only know whether the embedding model thinks it's similar to the ideal. This makes the report much less useful for non-European languages or scripts the user cannot read.

We need an automated translation step that:
- Runs for every non-English language (up to ~90 per run)
- Produces readable English text
- Requires no API keys or paid accounts
- Adds at most 30–60 seconds to total runtime

### Options Considered

1. **Google Translate via `deep-translator` (chosen)** — A lightweight Python library wrapping Google Translate's free web interface. Auto-detects source language. No API key required. ~30 seconds for 90 translations.

2. **Local translation model (e.g., `Helsinki-NLP/opus-mt`)** — Would need one model per language pair (~50 models). Impractical download size and runtime.

3. **LibreTranslate self-hosted** — Would need a Docker container running LibreTranslate. Adds operational complexity.

4. **No translation** — User must manually look up each language. Defeats the purpose of a comprehensive report.

### Decision

Use **Option 1**: Google Translate via the `deep-translator` Python library.

### Rationale

- **Zero configuration** — `pip install deep-translator` and it works. No API keys, no accounts.
- **Auto language detection** — We don't need to tell it which language each snippet is in.
- **Caching** — Translations are cached in-memory so re-runs skip translation.
- **Graceful degradation** — If translation fails (network, rate limit), the report shows `[translation failed]` and continues.
- **Lightweight** — The library is ~2 MB, no heavy dependencies.

### Consequences

**Positive:**
- Users can now read what any language's lead actually says, regardless of script
- Dramatically improves the utility of the report: score + translation gives both *how closely* and *what*
- Makes South Asian script languages decipherable (e.g., Malayalam: "global gathering of users working on wiki initiatives")

**Negative:**
- ~30–60 seconds added to total runtime for 90 translations
- Google rate limits may cause failures on very large runs (mitigated by caching + retries)
- Machine translation quality varies; low-resource languages may produce garbled output
- Depends on an external service (Google Translate web interface)

---

## ADR-009: Model Registry Pattern (LaBSE as Default, --model Flag)

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

Initially the tool used a single hardcoded model (`distiluse-base-multilingual-cased-v2`, 50+ languages). Testing revealed poor coverage for South Asian Brahmic scripts (Kannada, Telugu, Tamil, Malayalam — all scoring near zero regardless of content quality). LaBSE (109 languages) was identified as a better fit, but we wanted to keep distilUSE available as a faster, lighter fallback.

### Options Considered

1. **Model registry with CLI flag (chosen)** — A `MODEL_REGISTRY` dict mapping short names to model metadata (short name, full HuggingFace path, weight file, size hint, language count). A `set_model()` function configures globals from the registry. CLI flag `--model labse|distiluse`.

2. **Two separate scripts** — One for each model. Code duplication, maintenance burden.

3. **Environment variable** — `MODEL=distiluse python3 wiki_lang_check.py ...`. Less discoverable than a CLI flag.

### Decision

Use **Option 1**: Model registry with `--model` CLI flag. LaBSE is the default because it covers all our target languages.

### Rationale

- **Single code path** — All models use the same pipeline; only the embedding changes
- **Discoverable** — `--help` shows available models
- **Extensible** — Adding a third model is one entry in `MODEL_REGISTRY` dict
- **Lightweight dispatch** — The registry holds strings, not loaded models; no memory cost for unused models

### Consequences

**Positive:**
- LaBSE fixed South Asian scores from ~-0.02 to ~0.70–0.83
- Users can fall back to distilUSE for speed or smaller downloads
- Adding a new model is a 4-line dict entry

**Negative:**
- Slightly more complex CLI (one more flag to document)
- Users must know which model to choose

---

## ADR-010: Disk Cache for Lead Fetching

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

Each run fetches the lead section of the same article from 100–300+ Wikipedia language editions via HTTP. If a user re-runs the tool on the same article (e.g., with a different ideal sentence or a different model), every language is re-fetched. This is wasteful and risks hitting rate limits.

### Options Considered

1. **Disk cache with JSON file (chosen)** — `.lead_cache.json` stores `{lang:title: lead_text}`. Checked before HTTP; written after success. Loaded at pipeline start, saved after fetch completes.

2. **In-memory cache only** — Wouldn't survive between runs. Only prevents duplicate fetches within a single run (which we already do via `all_results`).

3. **SQLite database** — More structured but adds a dependency. Overkill for a simple key-value store of ~300 entries.

4. **No caching** — Every run is a full re-fetch. Unnecessary HTTP traffic and slower re-runs.

### Decision

Use **Option 1**: JSON file on disk.

### Rationale

- **Simple** — No extra dependencies, no schema to maintain
- **Cross-session** — Cache persists between runs, even days apart
- **Small** — ~100 KB for 300 languages, trivial I/O cost
- **Transparent** — Easy to inspect and debug (`cat .lead_cache.json | jq`)

### Consequences

**Positive:**
- Re-runs on the same article skip all HTTP — near-instant fetch phase
- Reduced rate-limit risk on subsequent runs (only new/changed articles need fetching)
- `--flushcache` gives users control to force a fresh fetch when article content changes

**Negative:**
- Stale data if the Wikipedia article is edited between runs — user must remember `--flushcache`
- ~300 KB write per run (negligible)

---

## ADR-011: Rate-Limit Handling with Exponential Backoff

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

The Wikimedia REST API enforces rate limits via HTTP 429 responses. With 8–12 concurrent workers and 300+ language editions, the tool triggers these limits after ~100 requests. The old `fetch_lead()` treated any non-200 as a failure, causing ~150 false "missing" languages for the Sun article.

### Options Considered

1. **Retry with exponential backoff + Retry-After (chosen)** — On 429, read the `Retry-After` header, add exponential backoff (`2^attempt` seconds), sleep, and retry up to 3 times. Also retries on `requests.Timeout`. Handles 414 (URI too long) with re-encoded URL.

2. **Fixed delay between all requests** — Add `time.sleep(0.2)` between every request regardless of rate limit. Slower for small articles, wastes time when not rate-limited.

3. **Reduce concurrency to 1** — Serial requests. Too slow for 300+ languages (~2 minutes).

4. **Ignore rate limits** — The old behavior. Lost ~50% of languages on large articles.

### Decision

Use **Option 1**: Retry with exponential backoff + `Retry-After` header respect. Combined with reducing default workers from 12 to 6.

### Rationale

- **Respects server signals** — `Retry-After` tells us exactly how long to wait
- **Minimal overhead on success** — No artificial delays when requests are fast
- **Self-healing** — After a 429, the backoff naturally paces subsequent requests
- **Combined with worker reduction** — Fewer workers = fewer concurrent 429s, so retries are rare

### Consequences

**Positive:**
- Sun article: 103/312 found → 296/312 found
- 414 errors now handled with re-encoded URLs
- Timeouts retried rather than failing silently

**Negative:**
- 429 retries add latency (a few extra seconds per batch)
- 16 languages still fail (mostly genuine 404s for redirected domains like `gsw.wikipedia.org`)

---

## ADR-007: Weighted Scoring over Raw Cosine Similarity

**Status:** Accepted  
**Date:** 2026-06-12  
**Deciders:** Ali  

### Context

Raw cosine similarity between sentence embeddings can produce misleading results for short, factual sentences. The ideal sentence contains two clauses ("annual conference of the movement" + "organized by the community and hosted by the Foundation"). A language that only captures one clause might still score moderately.

### Options Considered

1. **Raw cosine similarity** — Simple, transparent, but can mask partial matches.

2. **Weighted best-sentence + lead-section (chosen)** — As described in ADR-002.

3. **Decomposed clause matching** — Split the ideal sentence into atomic claims, score each claim independently, and report per-clause agreement. This would be the most informative but requires:
   - Clause boundary detection (not trivial cross-lingually)
   - A separate embedding for each clause (3× the compute)

### Decision

Use **Option 2**: Weighted dual-metric scoring with decomposed clause tracking as a future enhancement.

### Rationale

- The two metrics naturally capture clause-level matching: best-sentence match picks up either clause if present anywhere, lead-section match rewards full-structure alignment
- 70/30 weighting was validated by examining the Wikimania results: Spanish (0.88) captures both clauses; Dutch (0.77) captures only the first clause; the difference reflects the missing community-organizing framing

### Consequences

**Positive:**
- Good diagnostic separation between "has the right info" and "structures the lead well"
- No complex NLP pipeline needed for clause decomposition

**Negative:**
- 70/30 is an empirical weighting, not theoretically derived
- Doesn't tell you *which* clause is missing in low-scoring languages — you'd need to inspect the lead snippet manually
- Future versions could add explicit clause decomposition for per-clause reporting
