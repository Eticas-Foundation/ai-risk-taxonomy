# Eticas AI Risk Taxonomy

**Version:** 0.1.0-draft  
**Namespace:** `https://taxonomy.eticas.ai/risk/`  
**License:** CC BY 4.0  
**Maintained by:** [Eticas](https://eticas.ai)

## About this taxonomy

This is Eticas' unified AI risk taxonomy — a structured, machine-readable vocabulary of risk categories used across all of Eticas' audit methodologies, assessment frameworks, and reporting outputs.

Each concept in the taxonomy has a stable URI, a canonical definition, and formal links to equivalent or related concepts in major international frameworks. The taxonomy is published as a SKOS (Simple Knowledge Organization System) vocabulary, making it interoperable with knowledge graphs, linked data systems, and semantic web tools.

The taxonomy is designed to be:

- **Authoritative** — the single source of truth for risk category definitions across Eticas
- **Interoperable** — formally linked to NIST, EU AI Act, MIT AI Risk Repository, OECD, ISO, and W3C DPV vocabularies
- **Extensible** — new categories and subcategories can be added without breaking existing references
- **Human-readable and machine-readable** — source files are editable YAML; build outputs include browsable HTML, SKOS Turtle, and JSON-LD

## Taxonomy structure

The taxonomy is organised in three levels: **risk categories** (top level), **subcategories** (specific risk types), and **indicators** (observable manifestations, linked to assessment checks in Eticas methodologies).

Each concept carries the following metadata:

| Field | Description |
|-------|-------------|
| `id` | Stable identifier (e.g., `bias-fairness`, `privacy-pii-leakage`) |
| `uri` | Persistent URI under `https://taxonomy.eticas.ai/risk/` |
| `prefLabel` | Canonical English label |
| `altLabel` | Alternative labels / synonyms used in Eticas documents |
| `definition` | Prose definition |
| `scope` | Applicability: `ADM`, `LLM`, or `ALL` |
| `inclusion` | Whether this category is part of every audit: `required` or `audit-dependent` |
| `maturity` | How developed the category is: `established`, `developing`, `provisional`, or `proposed` |
| `perspective` | Which client concern the category addresses: `rights & ethics`, `technical soundness`, `governance & compliance`, or `operational viability` |
| `lifecycle_stages` | Where in the AI lifecycle this risk manifests: `pre-processing`, `in-processing`, `post-processing` |
| `mappings` | External equivalences (see Alignment section below) |

---

## Category classification

Each risk category is classified along three independent dimensions: **inclusion** (whether it is part of every audit), **maturity** (how developed the category is), and **perspective** (which client concern it addresses).

### Inclusion: required vs. audit-dependent

**Required** — Assessed in every Eticas audit regardless of system type or engagement scope. These categories represent risks that are relevant to any AI system.

**Audit-dependent** — Assessed based on the engagement scope, system type, and regulatory context. Their exclusion from a specific audit is a scoping decision that should be documented and justified.

### Maturity: how developed the category is

**Established** — Stable definition, well-developed subcategories, proven assessment methods, and strong mappings to external frameworks. Changes to established categories are made carefully.

**Developing** — The definition is solid, but subcategories and assessment methods are being refined through use in audits. External mappings may be partial.

**Provisional** — Recognised as important, but definitions may change, subcategories are incomplete, and assessment methods are not yet proven. Findings referencing provisional categories should note the provisional status.

**Proposed** — Suggested but not yet validated by the team. Included in the taxonomy to show how the category would integrate. Definitions, subcategories, and scope are subject to discussion.

### Perspective: which client concern the category addresses

**Rights & ethics** — Does the system respect people's rights and treat them fairly?

**Technical soundness** — Does the system work correctly and safely?

**Governance & compliance** — Is the system properly managed and legally compliant?

**Operational viability** — Will the system actually deliver value in context?

### Current classification

| Category | Inclusion | Maturity | Perspective |
|----------|-----------|----------|-------------|
| Bias & Fairness | required | established | rights & ethics |
| Privacy & Confidentiality | required | established | rights & ethics |
| Reliability | required | established | technical soundness |
| Governance | required | established | governance & compliance |
| Security & Misuse | required | established | technical soundness |
| Transparency & Explainability | required | established | governance & compliance |
| Environmental Impact | audit-dependent | established | technical soundness |
| Responsibility & Redress | audit-dependent | developing | rights & ethics |
| Autonomy & Human Agency | audit-dependent | provisional | rights & ethics |
| Agentic Risks | audit-dependent | provisional | technical soundness |
| Manipulation & Misinformation | audit-dependent | provisional | rights & ethics |
| Resilience | audit-dependent | proposed | operational viability |
| Integration Readiness | audit-dependent | proposed | operational viability |

All three dimensions can change independently. An audit-dependent category can be promoted to required as practice evolves. A proposed category becomes provisional once validated by the team, then developing and established as methods mature. These are team decisions documented in the changelog.

---

## Risk categories

Each category links to a detailed page with subcategories, definitions, and mappings to external frameworks. Browse all categories at the [taxonomy site](https://eticas-foundation.github.io/ai-risk-taxonomy/risk/).

**[Bias & Fairness](risk/bias-fairness.md)** — The risk that an AI system produces outcomes that systematically advantage or disadvantage individuals or groups based on protected or sensitive attributes, leading to unequal treatment, reduced accuracy, or unjust impacts. *(12 subcategories)*

**[Privacy & Confidentiality](risk/privacy-confidentiality.md)** — The risk that an AI system collects, processes, or infers personal information in ways that infringe on individuals' rights to control their data (privacy), or that sensitive information is exposed, accessed, or shared without authorization (confidentiality). *(8 subcategories)*

**[Reliability](risk/reliability.md)** — The risk that an AI system produces false, fabricated, or misleading outputs (hallucinations), spreads inaccurate or deceptive information (misinformation), or delivers inconsistent results across similar inputs and contexts. *(6 subcategories)*

**[Governance](risk/governance.md)** — The risk that an AI system lacks adequate structures, policies, or accountability mechanisms to oversee its design, deployment, and use. *(13 subcategories)*

**[Security & Misuse](risk/security-misuse.md)** — The risk that an AI system is exposed to vulnerabilities, attacks, or misuse that compromise its integrity, availability, or confidentiality. *(7 subcategories)*

**[Environmental Impact](risk/environmental-impact.md)** — The risk that an AI system's development, deployment, or use causes negative environmental effects, such as excessive energy or water consumption, carbon emissions, or unsustainable use of hardware and resources. *(3 subcategories)*

**[Transparency & Explainability](risk/transparency-explainability.md)** — The risk that stakeholders cannot understand how an AI system works, what it does, or why it produces specific outputs. *(5 subcategories)*

**[Responsibility & Redress](risk/responsibility-redress.md)** — The risk that individuals affected by AI-driven decisions have no effective means to understand, challenge, or seek remedy for those decisions. *(3 subcategories)*

**[Autonomy & Human Agency](risk/autonomy.md)** — The risk that an AI system undermines individuals' ability to make free, informed decisions, whether through over-reliance, automation bias, manipulative design, or erosion of human agency. *(no subcategories yet)*

**[Agentic Risks](risk/agentic-risks.md)** — The risk that AI systems operating with a degree of autonomy — planning, executing multi-step actions, using tools, or coordinating with other AI agents — introduce failure modes not present in single-inference systems. *(no subcategories yet)*

**[Manipulation & Misinformation](risk/manipulation-misinformation.md)** — The risk that AI systems are used — intentionally or through design flaws — to deceive, manipulate, or mislead individuals or populations. *(no subcategories yet)*

**[Resilience](risk/resilience.md)** — The risk that an AI system cannot absorb disruption, degrade gracefully, or recover when faced with adverse events, attacks, infrastructure failures, or environmental changes. *(5 subcategories)*

**[Integration Readiness](risk/integration-readiness.md)** — The risk that an AI system fails to deliver value not because of model performance issues but because it does not fit the organisational, technical, or human context into which it is deployed. *(5 subcategories)*

---

## Alignment with external frameworks

The taxonomy is formally linked to major international frameworks using SKOS mapping properties (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`). Each category page lists its specific mappings to the MIT AI Risk Repository, NIST AI RMF, NIST AI 600-1, OECD AI Principles, W3C DPV, ISO 42001, and the EU AI Act.

For a detailed analysis of how each Eticas category aligns with, diverges from, and extends these frameworks — including coverage gaps and areas where Eticas addresses risks that existing frameworks miss — see **[External framework alignment](docs/external-framework-alignment.md)**.

---

## Versioning and governance

The taxonomy follows [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0): Breaking changes — categories removed or fundamentally redefined
- **Minor** (0.X.0): New categories or subcategories added; inclusion or maturity changes; new external mappings
- **Patch** (0.0.X): Definition refinements, typo fixes, additional alternative labels

Changes are proposed via GitHub Issues, discussed with the team, and merged via pull requests. Every release is tagged and produces a timestamped snapshot of all output formats (Turtle, JSON-LD, HTML).

---

## How to cite

```
Eticas. (2026). Eticas AI Risk Taxonomy (Version 0.1.0).
https://taxonomy.eticas.ai/risk/
```

---

*This taxonomy is maintained by Eticas and published under CC BY 4.0. Contributions and alignment suggestions are welcome via GitHub Issues.*
