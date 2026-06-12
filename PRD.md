# Product Requirements Document: Lang-Check

**Version:** 1.0  
**Status:** Draft  
**Author:** Ali  
**Date:** 2026-06-12  

## 1. Executive Summary

Lang-Check is a tool that measures how consistently a Wikipedia article's lead sentence is translated or reflected across all language editions of that article. Given an "ideal" lead sentence (typically from the English article or a canonical formulation), the tool fetches the lead sections of the same article in every available language edition, computes semantic similarity between the ideal and each language's lead using multilingual sentence embeddings, and generates a ranked report with distribution statistics and visual histograms.

The tool is designed for Wikipedia editors, translation quality auditors, and Wikimedia researchers who need to:
- Verify that key factual claims in a lead are faithfully represented across languages
- Identify language editions that have diverged significantly from the consensus lead
- Measure systematic framing differences (e.g., institutional vs. community-centric language)
- Track lead consistency over time as articles evolve

## 2. Problem Statement

Wikipedia articles in different language editions are independently written by their respective communities. While the English article may have a carefully crafted lead sentence that reflects community consensus (e.g., "Wikimania is the Wikimedia movement's annual conference, organized by the community of contributors and hosted by the Wikimedia Foundation"), other language editions may frame the same subject differently (e.g., "Wikimania is the main conference organized by the Wikimedia Foundation").

Currently there is no automated way to:
- Measure how much divergence exists across language editions for a given claim or framing
- Quantify the degree of semantic alignment between an ideal sentence and a foreign-language lead
- Produce a ranked, evidence-based report that editors can use to identify and fix problematic leads

## 3. User Personas

### 3.1. Wikipedia Editor / Patroller
- **Goal:** Ensure that the lead sections of non-English articles faithfully represent the key facts agreed upon by the broader Wikimedia community
- **Use case:** Run Lang-Check on an article, identify the bottom 20% of languages, and either fix the leads or flag them for discussion
- **Technical level:** Comfortable running a Python script

### 3.2. Translation Quality Researcher
- **Goal:** Study how information degrades or transforms as it travels across language boundaries on Wikipedia
- **Use case:** Run Lang-Check on multiple articles, aggregate results to find systematic patterns (e.g., "Asian languages systematically omit community-organizing language")
- **Technical level:** Comfortable with JSON output and data analysis

### 3.3. Wikimedia Foundation / Movement Strategist
- **Goal:** Understand whether campaign-driven messaging (e.g., "Knowledge as a Service", "Wikimedia is a movement, not just a website") is being reflected in article leads across languages
- **Use case:** Commission Lang-Check analyses for key articles before and after editing campaigns
- **Technical level:** Can read a Markdown report

## 4. Functional Requirements

### 4.1. Core Pipeline

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| F-01 | Discover all language editions of a given Wikipedia article via the Action API | P0 | |
| F-02 | Fetch lead sections (first paragraph / summary) for each language edition via the REST API | P0 | Must handle 404 (article missing), network errors, and redirects |
| F-03 | Accept a user-provided ideal sentence in English | P0 | |
| F-04 | Score each language's lead against the ideal using multilingual sentence embeddings | P0 | |
| F-05 | Support concurrent HTTP requests for fetching leads | P1 | 12 concurrent workers |
| F-06 | Output structured JSON with per-language scores, including sub-scores | P0 | |

### 4.2. Scoring System

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| S-01 | Compute cosine similarity between ideal embedding and each individual lead sentence | P0 | |
| S-02 | Compute cosine similarity between ideal embedding and the combined first 3 lead sentences | P0 | |
| S-03 | Produce a combined score from both metrics with configurable weighting | P0 | Default: 70% best-sentence, 30% lead-section |
| S-04 | Report both sub-scores alongside the combined score | P1 | |
| S-05 | Report which sentence in the lead produced the best match | P2 | |
| S-06 | Report the total number of sentences in each lead | P2 | |
| S-07 | Translate each lead's best-matching sentence to English | P1 | Using Google Translate (free, no API key). Cache results to avoid re-translation |

### 4.3. Reporting

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| R-01 | Generate a Markdown report with an ASCII histogram of score distribution | P0 | |
| R-02 | Include a ranked table of all language editions with scores, lead snippets, **and English translations** | P0 | Each best-matching sentence translated via Google Translate |
| R-03 | Show the top 5 and bottom 5 leads in full with translation analysis | P1 | |
| R-04 | Show overall statistics (mean, median, std, min, max) | P1 | |
| R-05 | List languages that could not be fetched | P1 | |
| R-06 | Report the number and percentage of languages in each score bucket | P1 | |

### 4.4. Edge Cases & Error Handling

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| E-01 | Handle 404 (article doesn't exist in that language) gracefully | P0 | Mark as "not found" and continue |
| E-02 | Handle 429 (rate limiting) with Retry-After header | P0 | |
| E-03 | Handle network timeouts (15s timeout per request) | P1 | |
| E-04 | Handle redirects (e.g., nb → no.wikipedia.org) | P1 | Use fallback logic for known redirects |
| E-05 | Handle leads that return only infobox/meta content (e.g., `{{Infobox recurring event}}`) | P2 | Flag for human review |
| E-06 | Report model coverage gaps for specific script families | P2 | |

## 5. Non-Functional Requirements

| ID | Requirement | Target | Notes |
|----|-------------|--------|-------|
| N-01 | Time to run all languages | < 3 minutes for ~100 languages | Includes model loading time |
| N-02 | Memory usage | < 4 GB | Model weights ~500 MB |
| N-03 | HTTP rate limiting | ≤ 2 requests/second sustained | With bursting |
| N-04 | Model download size | < 1 GB (first run only) | |
| N-05 | Reproducibility | Deterministic for same input | Results should be stable across runs |
| N-06 | Language coverage | At least 50 languages with reasonable accuracy | |

## 6. User Stories

### US-01: First-run analysis
> "As an editor, I want to run Lang-Check on the 'Wikimania' article with my ideal sentence, so I can see which language editions need their leads updated."

**Acceptance criteria:**
- Pipeline runs from setup to report in < 3 minutes
- Report shows all 94 language editions sorted by score
- Top divergences are highlighted with the actual lead text

### US-02: Cross-article comparison
> "As a researcher, I want to run Lang-Check on 5 different articles and compare their consistency patterns."

**Acceptance criteria:**
- Pipeline script can be re-run with different parameters without code changes
- Output JSON can be aggregated across runs
- Consistent scoring methodology across runs

### US-03: Fix prioritization
> "As a patroller, I want to know which language editions are most in need of lead section improvements."

**Acceptance criteria:**
- Report clearly shows bottom-ranked languages
- Lead text for low-scoring languages is shown for human review
- Sub-scores (best-sentence vs. lead-section) help diagnose the problem

### US-04: Longitudinal tracking
> "As a project manager, I want to track lead consistency over time after an editing campaign."

**Acceptance criteria:**
- Scored results JSON is timestamped and comparable
- Score changes can be computed between reports

## 7. Technical Architecture

### 7.1. System Components

```
┌──────────────────────────────────────────────────────────┐
│                     Pipeline Driver                       │
│  (wiki_lang_check.py)                                      │
│                                                           │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────┐ │
│  │ Discovery  │─▶│ Fetch      │─▶│ Scoring Engine     │ │
│  │ (Action    │  │ (REST API  │  │ (sentence-         │ │
│  │  API)      │  │  x12 Par.) │  │  transformers)     │ │
│  └────────────┘  └────────────┘  └────────┬───────────┘ │
│                                           ▼             │
│                                 ┌────────────────────┐  │
│                                 │ Report Generator   │  │
│                                 │ (Markdown + JSON)  │  │
│                                 └────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### 7.2. Data Flow

1. **Input:** Article title (e.g., "Wikimania") + ideal sentence
2. **Discovery:** `GET https://en.wikipedia.org/w/api.php?action=query&titles=Wikimania&prop=langlinks&lllimit=500`
3. **Fetch:** `GET https://{lang}.wikipedia.org/api/rest_v1/page/summary/{title}` (parallel, 12 workers)
4. **Score:** `model.encode(ideal) → model.encode(lead) → cosine_similarity()`
5. **Output:** `scored_results.json` + `report.md`

### 7.3. Dependencies

- **Python 3.10+**
- `sentence-transformers` (model: `distiluse-base-multilingual-cased-v2`)
- `requests` (HTTP client)
- `numpy` (vector operations)
- `concurrent.futures` (parallel HTTP, stdlib)

## 8. Scoring Model Requirements

### 8.1. Model Selection

| Criteria | Requirement |
|----------|-------------|
| Multilingual | At least 50 languages supported |
| Embedding size | Not critical (512d is fine) |
| Inference speed | < 1 second for 100 sentences |
| Download size | < 1 GB |
| License | MIT, Apache 2.0, or CC-BY-SA compatible |

### 8.2. Known Gaps

The current model (`distiluse-base-multilingual-cased-v2`) has weak coverage for:
- South Asian Brahmic scripts (Kannada, Telugu, Tamil, Malayalam, Assamese, Bengali, Punjabi)
- Khmer (Cambodian)

These languages may score near zero even when their lead text is semantically correct. This is documented as a known limitation.

**Future options for better coverage:**
- `sentence-transformers/LaBSE` — Better coverage for South Asian languages, but larger model
- `intfloat/multilingual-e5-large` — Strong cross-lingual performance, but ~2 GB

## 9. Output Specifications

### 9.1. JSON Output (`scored_results.json`)

```json
{
  "ideal_sentence": "...",
  "scoring_method": "Combined (0.7 × best-sentence-match + 0.3 × lead-section-match)",
  "total_languages": 94,
  "successful_fetches": 90,
  "missing_fetches": 4,
  "results": [
    {
      "lang": "en",
      "title": "Wikimania",
      "similarity": 0.9147,
      "best_sentence_score": 0.9846,
      "lead_section_score": 0.7515,
      "best_sentence_idx": 0,
      "total_sentences": 2,
      "lead_snippet": "Wikimania is the Wikimedia movement's annual conference..."
    }
  ]
}
```

### 9.2. Markdown Report (`report.md`)

Required sections:
1. Title and ideal sentence
2. Scoring method explanation
3. Quick summary and key findings
4. Overall statistics table
5. ASCII histogram of score distribution
6. Complete ranked table of all languages
7. Top 5 most aligned leads (full text)
8. Bottom 5 least aligned leads (full text)
9. Languages not found

## 10. Constraints & Limitations

1. **Not a translation quality tool** — Measures semantic similarity, not translation correctness
2. **English-centric ideal** — The ideal sentence is always in English. A multi-language ideal would capture more nuance
3. **Single snapshot** — The tool analyzes the current state of articles. It does not track changes over time
4. **REST API dependency** — The `/page/summary` endpoint returns the first paragraph, which may not always match the full lead section (especially for articles with infoboxes before the lead text)
5. **Model coverage asymmetry** — Roman-script and Cyrillic-script languages score more reliably than Brahmic-script languages

## 11. Future Versions

### v2.0 (Planned)
- **Multi-ideal scoring:** Accept ideal sentences in multiple languages for cross-lingual comparison
- **Temporal analysis:** Compare scores over time by caching historical results
- **Wikipedia-side integration:** Toolforge tool with a simple web UI

### v2.1 (Nice-to-have)
- **LaBSE or E5 model** for better South Asian script coverage
- **Export to CSV / spreadsheet** for easy filtering
- **Batch mode:** Analyze multiple articles from a list
- **Contrast scoring:** Compare two different ideal sentences to measure framing shifts

## 12. Glossary

| Term | Definition |
|------|------------|
| Lead section | The introductory paragraph(s) of a Wikipedia article, before the table of contents |
| Language edition | One of the ~330 independent Wikipedia projects (en.wikipedia.org, de.wikipedia.org, etc.) |
| Interlanguage link | A link from an article in one language to the same topic in another language |
| Semantic similarity | A measure of how close two pieces of text are in meaning, computed via embedding cosine similarity |
| Embedding | A dense vector representation of text in a high-dimensional semantic space |
| Cosine similarity | The cosine of the angle between two vectors, ranging from -1 (opposite) to 1 (identical) |
