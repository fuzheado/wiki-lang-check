# Lang-Check: Wikipedia Lead Consistency Analyzer

**Measure how consistently a Wikipedia article's lead sentence is translated across all language editions.**

Given an ideal lead sentence (in English) and a Wikipedia article title, Lang-Check fetches the lead section from every language edition where the article exists, computes semantic similarity between your ideal sentence and each language's lead text using multilingual sentence embeddings, and produces a ranked report with distribution histograms.

## Why This Exists

Wikipedia articles in different languages are independently written by local communities. They are *not* translations of each other. This means the lead sentence — the article's most important summary — can diverge significantly across languages. Some key facts might be present in 80% of language editions, others in only 20%. Lang-Check makes this divergence measurable.

Use cases:
- **Consistency auditing** — Check whether a specific phrasing (e.g., "organized by the community of contributors") is faithfully reflected across language editions
- **Translation quality assessment** — Measure semantic fidelity of lead sections without needing human translators
- **Content gap analysis** — Identify language editions where the lead omits key facts present in the ideal sentence
- **Bias detection** — Surface systematic framing differences (e.g., "Foundation conference" vs. "community-organized conference")

## How It Works

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌──────────────┐
│ 1. Discover  │────▶│ 2. Fetch Leads   │────▶│ 3. Score Leads   │────▶│ 4. Report    │
│ Languages    │     │ (parallel HTTP)  │     │ (multilingual    │     │ (Markdown)   │
│ via Action   │     │ 12 concurrent    │     │  embeddings)     │     │              │
│ API          │     │ workers          │     │                  │     │              │
└──────────────┘     └──────────────────┘     └──────────────────┘     └──────────────┘
```

1. **Discover** — Query the Wikimedia Action API for all interlanguage links of a given article title
2. **Fetch** — Download each language edition's lead section via the REST API (`/page/summary`), using 12 concurrent HTTP workers
3. **Score** — Encode the ideal sentence and each lead with `distiluse-base-multilingual-cased-v2`, then compute a **dual-metric score**:
   - *Best-sentence match (70% weight)* — maximum cosine similarity between the ideal sentence and any single sentence in the lead
   - *Lead-section match (30% weight)* — cosine similarity between the ideal and the combined first 3 sentences
4. **Translate** — Each language's best-matching sentence is automatically translated into English via Google Translate (free, no API key) so you can see what the lead actually says
5. **Report** — Generate a Markdown report with an ASCII histogram, a ranked table with English translations for every language, and detailed top/bottom comparisons

## Setup

```bash
# Clone or navigate to the project
cd /Users/alih/Documents/ai/lang-check

# Create virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install sentence-transformers requests numpy
```

> **Note:** `sentence-transformers` pulls in PyTorch (~800MB on first install). The model weights (`distiluse-base-multilingual-cased-v2`) download on first run (~500MB).

## Usage

### Quick start

```bash
source venv/bin/activate

# Run the built-in Wikimania example:
python3 wiki_lang_check.py example

# Or run with your own article and ideal sentence:
python3 wiki_lang_check.py --article "Article" --sentence "Your ideal lead sentence here."

# Show usage info:
python3 wiki_lang_check.py --help
```

The `example` mode is a quick way to see how the tool works without specifying arguments.

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--article TEXT` | Yes (or `example`) | Wikipedia article title (e.g., `"Wikimania"`) |
| `--sentence TEXT` | Yes (or `example`) | Ideal lead sentence to compare against |
| `--help` | No | Show detailed usage message |
| `example` | No (subcommand) | Run the built-in Wikimania example |

### Output files

Each run produces **two files** with names that never collide:

```
<Article>_runNNN_results.json    # Structured scoring data
<Article>_runNNN_report.md       # Full Markdown report
```

Examples:
- `Wikimania_run001_results.json`
- `Wikimania_run001_report.md`
- `Wikimania_run002_results.json`  (use the counter)

The run counter persists in `.run_counter` and auto-increments each invocation.

## Files

```
lang-check/
├── wiki_lang_check.py          # Main CLI: discover → fetch → score → report
├── score_and_report.py         # Standalone scorer (expects batch_results_*.json)
├── CHANGELOG.md                # Feature progress & planned work
├── PRD.md                      # Product requirements
├── ADR.md                      # Architecture Decision Record
├── README.md                   # This file
├── .run_counter                # Persistent run sequence number
├── venv/                       # Python virtual environment
├── all_langs.json              # Language list cache
├── examples/                   # Example output files
│   ├── Wikimania_example_report.md
│   └── Wikimania_example_results.json
├── Wikimania_run*              # Actual run output (numbered)
└── *.py                        # Other helper scripts
```

## Scoring Methodology

The combined score uses two complementary metrics:

- **Best-sentence match (70%)** — Why 70%? We want to know if the ideal concept exists *anywhere* in the lead. A lead might have four sentences where the first three describe logistics and the fourth captures the key idea. Best-sentence match finds that needle.
- **Lead-section match (30%)** — Added because a lead that consistently echoes the ideal across multiple sentences should score higher than one that only has one good sentence. This rewards overall topical alignment.

The weighting was chosen empirically: best-sentence gets the majority weight because the primary question is "does this language's lead contain the right information?" while lead-section provides a gentle bonus for well-structured leads.

## Translations

Each language's **best-matching sentence** (the one that scored highest against the ideal) is automatically translated to English using **Google Translate** (via the `deep-translator` library, free, no API key required).

Translations appear in the report's ranked table as a `→ English translation` column, and in the detailed top/bottom sections. This lets you see — without knowing the language — whether the lead actually says what you expect.

Results are cached, so re-running the same article uses cached translations and skips re-translation.

### Caveats
- Translations are of the *single best-matching sentence only*, not the entire lead
- Machine translation quality varies by language pair; it's best for European languages and weaker for low-resource languages
- If translation fails (network error, rate limit), the report shows `[translation failed]`

### Model: `distiluse-base-multilingual-cased-v2`

- 512-dimensional multilingual embeddings
- Trained on 50+ languages (distilled from Universal Sentence Encoder multilingual)
- Supports: Arabic, Chinese, Dutch, English, French, German, Greek, Hebrew, Hindi, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Thai, Turkish, Vietnamese, and many more
- **Known limitation:** Weak coverage for South Asian Brahmic scripts (Kannada, Telugu, Tamil, Malayalam, Bengali, Assamese, Punjabi, Khmer). Languages in these scripts that have semantically correct lead text may score near zero due to model underrepresentation.

## Example Results (Wikimania)

From the initial run across 94 language editions. The "translation" column is a live Google Translate result of the best-matching sentence in each lead:

| Lang | Score | Translation (Google Translate) |
|------|-------|-------------------------------|
| 🇬🇧 en | **0.91** | *(English — original)* |
| 🇪🇸 es | **0.88** | "annual conference of the Wikimedia movement, organized by volunteers and sponsored by the WMF" |
| 🇦🇷 an | **0.85** | "annual conference of the Wikimedia movement, organized by volunteers and sponsored by the WMF" |
| 🇬🇷 el | **0.83** | "annual conference of the Wikimedia movement, organized by volunteers and hosted by the WMF" |
| 🇳🇱 nl | **0.77** | "annual conference for users of wiki projects created by the WMF" |
| 🇩🇪 de | **0.69** | "international conference organized annually by the WMF at different locations" |
| 🇫🇷 fr | **0.69** | "main conference organized by the Wikimedia foundation from 2005" |
| 🇨🇳 zh | **0.56** | "academic conference hosted by the WMF" |
| 🏴 ckb | **0.64** | "annual conference of the Wikimedia movement organized by volunteers and hosted by the WMF" — *content is near-perfect but Arabic script scores low due to model bias* |

**Key finding:** Most language editions frame Wikimania as *"a conference **of** the Wikimedia Foundation"* rather than *"a conference **of the Wikimedia movement** organized **by the community**."* This is a systematic framing divergence.

## Status: Initial Prototype

This is a **first-version proof of concept**. The approach — cross-lingual lead comparison via sentence embeddings + Google Translate — has been tested on one article (Wikimania) with promising results, but more runs on diverse articles are needed to validate:

- Whether the embedding model's similarity scores correlate reliably with human judgment across different scripts and language families
- Whether Google Translate handles the varied lead structures (infobox-heavy, stub articles, multi-paragraph leads) without breaking
- Whether the 70/30 scoring weight split is optimal, or whether it should be tuned per language family
- How the tool behaves with articles that have very different interlanguage link patterns (e.g., local-interest topics with fewer translations)

**Use the results as directional guidance, not definitive truth.** Manual spot-checking of specific language editions is still recommended before making editorial decisions based on this tool's output.

## Limitations

1. **Model coverage gap** — South Asian Brahmic scripts (Telugu, Kannada, Malayalam, Tamil, Assamese, Bengali, Punjabi, Khmer) score artificially low regardless of semantic content quality
2. **Lead ≠ first paragraph** — The REST API `summary` endpoint returns the lead paragraph. For some articles this may be shorter or longer than the true lead section
3. **One ideal sentence** — The tool compares against a single English sentence. A multi-sentence ideal or multi-language ideal could improve coverage
4. **No translation quality baseline** — We measure semantic similarity, not correctness. A high score means "similar framing," which could come from a faithful translation or from a superficial match

## Related Skills

This project uses the following skills from the [Wikipedia AI Skills](https://github.com/alih/Wikipedia-AI-Skills) repository:

- [wikimedia-api-access](https://github.com/alih/Wikipedia-AI-Skills/blob/main/.claude/skills/wikimedia-api-access/SKILL.md) — API access patterns and rate limiting
- [wikimedia-api-strategy](https://github.com/alih/Wikipedia-AI-Skills/blob/main/.claude/skills/wikimedia-api-strategy/SKILL.md) — Choosing between REST, Action, SPARQL
