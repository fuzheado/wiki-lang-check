# Lang-Check: Progress & Feature Log

Tracking implemented features, in-progress work, and planned enhancements.

---

## ✅ Implemented

| Feature | Version | Notes |
|---------|---------|-------|
| CLI with `--help`, `--article`, `--sentence` | 2.0 | No-args shows rich usage message |
| `example` subcommand | 2.0 | Runs the built-in Wikimania example |
| Model download warning | 2.0 | Shows ~500 MB banner on first model load; tqdm progress bars from SentenceTransformer |
| Compact language summary | 2.0 | Groups 90+ languages by script/region instead of one-per-line |
| Run-safe output filenames | 2.0 | `<Article>_runNNN_results.json` and `_report.md` via persistent counter |
| Dual-metric scoring | 1.0 | 70% best-sentence + 30% lead-section |
| Multilingual embedding model | 1.0 | `distiluse-base-multilingual-cased-v2` |
| Concurrent HTTP fetch (12 workers) | 1.0 | `ThreadPoolExecutor` |
| Markdown report with histogram | 1.0 | ASCII bar chart, ranked table, top/bottom 5 |
| Parallel subagent pipeline | 1.0 | 10 batches × 8 worker agents for lead fetching |
| **Machine translation in reports** | **2.0** | Each lead's best-matching sentence auto-translated to English via Google Translate (`deep-translator`, free, no API key). Shown in report table + top/bottom details |
| **Lazy imports for fast startup** | **2.0** | Heavy libraries (torch, sentence-transformers, numpy) now imported on-demand only. No-args / `--help` startup dropped from ~5s to ~0.13s |
| **LaBSE as default model** | **2.0** | Default model changed to LaBSE (109 languages, excellent South Asian coverage). Old distilUSE available via `--model distiluse`. South Asian language scores improved from ~-0.02 to ~0.70-0.83 |

---

## 🚧 In Progress / Recently Changed

*Nothing currently in progress.*

---

## 🔮 Planned Features

### P1: Non-English base language

Allow `--lang fr` or `--lang ar` so the ideal sentence can be in French, Arabic, etc., and the pipeline compares against all language editions from that base.

**Why:** An editor working on French Wikipedia should be able to check consistency starting from the French article's lead.

**Status:** Not started.

### P2: Better article discovery & error handling

- **Redirect detection:** When an article title redirects in a particular language edition, detect and report it (e.g., `nb.wikipedia.org` → `no.wikipedia.org`)
- **Language code resolution:** Some Wikipedia language codes differ from Wikimedia's standard codes (e.g., `yue` may resolve to `zh-yue`, `nb` redirects to `no`). Implement a lookup table or fallback chain.
- **Page-not-found fallback:** When the REST API returns 404 but the Action API knows the page exists, try the Action API as a fallback.

**Why:** 4 of 94 languages returned no data on the initial Wikimania run due to these issues. Better error handling would recover most of them.

**Status:** Not started.

### P3: Per-clause scoring

Instead of a single combined score, decompose the ideal sentence into atomic claims (e.g., "annual conference", "of the Wikimedia movement", "organized by community", "hosted by WMF") and score each clause independently.

**Why:** Would tell users *which specific claim* is missing in each language edition, not just a single similarity number.

**Status:** Not started. Requires clause-boundary detection (NLP).

### P4: Longitudinal tracking

Cache previous run results and show score deltas (↑ / ↓) in the report.

**Why:** Useful for tracking whether editing campaigns are improving lead consistency.

**Status:** Not started.

---

## 💡 Feature Requests (Unprioritized)

- **Model upgrade:** Replace `distiluse-base-multilingual-cased-v2` with `LaBSE` or `intfloat/multilingual-e5-large` for better South Asian script coverage
- **Web UI (Toolforge):** Deploy as a Toolforge tool with a simple HTML form
- **CSV export:** Add `--csv` flag for spreadsheet-friendly output
- **Batch mode:** Accept a file with multiple article/sentence pairs and run sequentially
- **Contrast scoring:** Compare two different ideal sentences to measure framing shifts (e.g., "community conference" vs "Foundation conference")
- **Temporal analysis:** Re-fetch the same article after N days and compare scores
- **`--quiet` mode:** Suppress progress output, print only final report path
- **`--top N` / `--bottom M`:** Limit the report to only top/bottom performers
- **Docker image:** One-command setup without Python/venv
