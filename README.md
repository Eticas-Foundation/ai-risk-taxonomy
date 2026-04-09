# Eticas AI Risk Taxonomy

A unified, machine-readable AI risk taxonomy for use across [Eticas](https://eticas.ai) audit methodologies, assessment frameworks, and reporting outputs.

**Namespace:** `https://taxonomy.eticas.ai/risk/`  
**Version:** 0.1.0  
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## What this is

This repository contains Eticas' canonical definitions of AI risk categories and subcategories, formally linked to major international frameworks including the NIST AI RMF, EU AI Act, MIT AI Risk Repository, OECD AI Principles, ISO/IEC 42001, and the W3C Data Privacy Vocabulary.

Each concept has a stable URI (e.g., `https://taxonomy.eticas.ai/risk/bias-fairness`), a definition, alternative labels, lifecycle stage applicability, and cross-references to equivalent concepts in external frameworks.

## Risk categories

### Required (assessed in every audit)
- [Bias & Fairness](risk/bias-fairness.md)
- [Privacy & Confidentiality](risk/privacy-confidentiality.md)
- [Reliability](risk/reliability.md)
- [Governance](risk/governance.md)
- [Security & Misuse](risk/security-misuse.md)
- [Transparency & Explainability](risk/transparency-explainability.md)

### Audit-dependent
- [Environmental Impact](risk/environmental-impact.md) — established
- [Responsibility & Redress](risk/responsibility-redress.md) — developing
- [Autonomy & Human Agency](risk/autonomy.md) — provisional
- [Agentic Risks](risk/agentic-risks.md) — provisional
- [Manipulation & Misinformation](risk/manipulation-misinformation.md) — provisional

## Outputs

| Format | Path | Description |
|--------|------|-------------|
| YAML source | [`src/taxonomy.yaml`](src/taxonomy.yaml) | Human-editable source of truth |
| SKOS Turtle | [`dist/taxonomy.ttl`](dist/taxonomy.ttl) | Machine-readable RDF |
| SKOS JSON-LD | [`dist/taxonomy.jsonld`](dist/taxonomy.jsonld) | Machine-readable linked data |
| Browsable site | [`risk/`](risk/) | Markdown pages (served as HTML via GitHub Pages) |

## How to contribute

1. Edit `src/taxonomy.yaml`
2. Run the build: `pip install -r build/requirements.txt && python build/convert.py && python build/validate.py && python build/generate_pages.py`
3. Open a pull request

CI validates all changes automatically. See [`docs/implementation.md`](docs/implementation.md) for architecture details.

## How to cite

```
Eticas. (2026). Eticas AI Risk Taxonomy (Version 0.1.0).
https://taxonomy.eticas.ai/risk/
```
