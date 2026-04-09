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
| `maturity` | How developed the category is: `established`, `developing`, or `provisional` |
| `lifecycle_stages` | Where in the AI lifecycle this risk manifests: `pre-processing`, `in-processing`, `post-processing` |
| `mappings` | External equivalences (see Alignment section below) |

---

## Category classification

Each risk category is classified along two independent dimensions: **inclusion** (whether it is part of every audit) and **maturity** (how developed the category's definitions and methods are).

### Inclusion: required vs. audit-dependent

**Required** — Assessed in every Eticas audit regardless of system type or engagement scope. These categories represent risks that are relevant to any AI system.

**Audit-dependent** — Assessed based on the engagement scope, system type, and regulatory context. Their exclusion from a specific audit is a scoping decision that should be documented and justified.

### Maturity: how developed the category is

**Established** — Stable definition, well-developed subcategories, proven assessment methods, and strong mappings to external frameworks. Changes to established categories are made carefully.

**Developing** — The definition is solid, but subcategories and assessment methods are being refined through use in audits. External mappings may be partial.

**Provisional** — Recognised as important, but definitions may change, subcategories are incomplete, and assessment methods are not yet proven. Findings referencing provisional categories should note the provisional status.

### Current classification

| Category | Inclusion | Maturity |
|----------|-----------|----------|
| Bias & Fairness | required | established |
| Privacy & Confidentiality | required | established |
| Reliability | required | established |
| Governance | required | established |
| Security & Misuse | required | established |
| Transparency & Explainability | required | established |
| Environmental Impact | audit-dependent | established |
| Responsibility & Redress | audit-dependent | developing |
| Autonomy & Human Agency | audit-dependent | provisional |
| Agentic Risks | audit-dependent | provisional |
| Manipulation & Misinformation | audit-dependent | provisional |

Both dimensions can change independently. An audit-dependent category can be promoted to required as practice evolves. A provisional category becomes developing and then established as definitions stabilise and assessment methods are tested. These are team decisions documented in the changelog.

---

## Risk categories

### Required categories

These categories are assessed in every Eticas audit.

#### 1. Bias & Fairness
`https://taxonomy.eticas.ai/risk/bias-fairness`

The risk that an AI system produces outcomes that systematically advantage or disadvantage individuals or groups based on protected or sensitive attributes, leading to unequal treatment, reduced accuracy, or unjust impacts. This includes biases introduced through data, model design, or deployment context, and covers both measurable disparities and perceived unfairness in decision-making.

**Subcategories:**
- **Dataset bias and under/over-representation** — Training or evaluation data that does not adequately represent all relevant population groups
- **Proxy discrimination** — Discrimination through correlated features that serve as proxies for protected attributes
- **Intersectional unfairness** — Compounded disadvantage affecting individuals at the intersection of multiple protected characteristics
- **Accessibility barriers** — System design that excludes or disadvantages people with disabilities
- **Geographic, cultural, or language skew** — Systematic performance differences across geographies, cultures, or languages
- **Feedback loops reinforcing inequality** — System outputs that, when fed back into the system or its context, amplify existing biases
- **Quality of service disparities** — Inconsistent service quality across demographic groups
- **Stereotyping and demeaning content** — Outputs that reinforce, erase, or demean demographic groups
- **Harmful content and toxicity** — Offensive or harmful outputs that damage user well-being
- **Sentiment fairness across groups** — Unequal emotional tone in outputs across groups
- **Performance equity across populations** — Higher error rates for specific groups

#### 2. Privacy & Confidentiality
`https://taxonomy.eticas.ai/risk/privacy-confidentiality`

The risk that an AI system collects, processes, or infers personal information in ways that infringe on individuals' rights to control their data (privacy), or that sensitive information is exposed, accessed, or shared without authorization (confidentiality). This includes risks from data leakage, re-identification, unauthorized use, or insufficient safeguards.

**Subcategories:**
- **Unlawful collection or processing of personal data**
- **Re-identification of anonymised data**
- **Function creep** — Repurposing data beyond original intent
- **Biometric surveillance** — Mass biometric data collection and processing
- **Emotion inference or sensitive attribute profiling**
- **Weak data retention/erasure and access controls**
- **PII leakage** — Personal data present in training data leaking through model outputs
- **Membership inference risk** — Ability to determine whether specific individuals were in training data

#### 3. Reliability
`https://taxonomy.eticas.ai/risk/reliability`

The risk that an AI system produces false, fabricated, or misleading outputs (hallucinations), spreads inaccurate or deceptive information (misinformation), or delivers inconsistent results across similar inputs and contexts. Such failures undermine trust, reduce system dependability, and can lead to harmful or misguided decisions.

**Subcategories:**
- **Hallucination and fabricated outputs** — Generation of false or misleading information that appears credible
- **Output inconsistency** — Inconsistent results across similar inputs and contexts
- **Output drift over time** — Degradation of output quality or accuracy as conditions change
- **Out-of-distribution robustness** — Unpredictable behaviour when exposed to unfamiliar data
- **Failure and remediation gaps** — Lack of remediation plans for predictable or unknown failures
- **Monitoring and evaluation gaps** — Lack of monitoring rendering datasets obsolete and outputs unreliable

#### 4. Governance
`https://taxonomy.eticas.ai/risk/governance`

The risk that an AI system lacks adequate structures, policies, or accountability mechanisms to oversee its design, deployment, and use. Weak governance can lead to unclear responsibilities, poor documentation, limited auditability, and failure to align with legal, ethical, or organizational standards.

**Subcategories:**
- **Unclear responsibilities and accountability gaps** — Missing or ambiguous role assignments
- **Poor documentation** — Incomplete or outdated system documentation
- **Limited auditability** — Insufficient logging, versioning, or traceability for external review
- **Regulatory non-compliance** — Failure to align with applicable legal or ethical standards
- **Lack of change management** — Absence of controlled processes for system modifications
- **Oversight of adverse impacts** — Missing processes for identifying and escalating harmful outcomes
- **Fitness for purpose** — System not validated against the problem it is intended to solve
- **Data governance** — Inadequate labelling, tagging, approval, or appropriateness assessment of data
- **Human oversight and control** — Lack of defined intervention points or override capabilities
- **Decision traceability** — Inability to trace decisions back to specific inputs and processes
- **Critical input/output logging** — Failure to log inputs and outputs systematically
- **Responsible actor attribution** — Unclear attribution of responsibility across developers, deployers, and reviewers
- **Task success** — Low or uneven task success across subpopulations or input types

#### 5. Security & Misuse
`https://taxonomy.eticas.ai/risk/security-misuse`

The risk that an AI system is exposed to vulnerabilities, attacks, or misuse that compromise its integrity, availability, or confidentiality. This includes adversarial inputs, model inversion, data poisoning, prompt injection, and unauthorized access, which can lead to manipulation of outputs, data breaches, or system failure.

**Subcategories:**
- **Adversarial attacks** — Evasion, poisoning, and extraction attacks
- **Prompt injection** (LLM) — Malicious inputs that subvert system intent
- **Jailbreaking** (LLM) — Bypass of safety controls to trigger prohibited behaviours
- **Unauthorized access** — Exploitation of access control weaknesses
- **Supply-chain vulnerabilities** — Risks from third-party components, data sources, or model providers
- **Incident response gaps** — Insufficient detection, logging, or response capabilities
- **Misuse beyond intended purpose** — Use of the system for purposes it was not designed for

### Audit-dependent categories (established)

These categories are assessed where relevant to the audit scope.

#### 6. Environmental Impact
`https://taxonomy.eticas.ai/risk/environmental-impact`

The risk that an AI system's development, deployment, or use causes negative environmental effects, such as excessive energy or water consumption, carbon emissions, or unsustainable use of hardware and resources. This includes hidden impacts across the system's lifecycle, from model training to long-term operation.

**Subcategories:**
- **Inference-time energy consumption** — High energy use during deployment
- **Training resource consumption** — Significant carbon emissions from model training
- **Hardware efficiency** — Poor hardware utilisation increasing costs and environmental impact

#### 7. Transparency & Explainability
`https://taxonomy.eticas.ai/risk/transparency-explainability`

The risk that stakeholders cannot understand how an AI system works, what it does, or why it produces specific outputs. Lack of transparency undermines informed consent, impedes oversight, and erodes trust.

**Subcategories:**
- **AI system explainability** — Stakeholders misinterpret or misunderstand system purpose or outputs
- **Communication to stakeholders** — Stakeholders not aware of system limitations or settings
- **Disclosure of AI interaction** — Users interacting with AI under the assumption it is human
- **Model card completeness** — Incomplete documentation of model purpose, performance, or limitations
- **Prompt transparency** (LLM) — Inconsistent outputs to semantically similar inputs reducing trust
- **Self-consistency and stability** — Service degradation for specific user groups or contexts

#### 8. Responsibility & Redress
`https://taxonomy.eticas.ai/risk/responsibility-redress`

The risk that individuals affected by AI-driven decisions have no effective means to understand, challenge, or seek remedy for those decisions. This includes absence of appeal mechanisms, unclear remediation procedures, and failure to communicate with affected parties.

**Subcategories:**
- **Absence of appeal mechanisms**
- **Unclear remediation procedures**
- **Ineffective communication with affected parties**

### Audit-dependent categories (provisional)

These categories are recognised as important but definitions and assessment methods are still under development.

#### 9. Autonomy & Human Agency
`https://taxonomy.eticas.ai/risk/autonomy`

The risk that an AI system undermines individuals' ability to make free, informed decisions, whether through over-reliance, automation bias, manipulative design, or erosion of human agency.

#### 10. Agentic Risks
`https://taxonomy.eticas.ai/risk/agentic-risks`

The risk that AI systems operating with a degree of autonomy — planning, executing multi-step actions, using tools, or coordinating with other AI agents — introduce failure modes not present in single-inference systems. This includes cascading errors across agent chains, unintended emergent behaviour, and loss of meaningful human control over compound actions.

#### 11. Manipulation & Misinformation
`https://taxonomy.eticas.ai/risk/manipulation-misinformation`

The risk that AI systems are used — intentionally or through design flaws — to deceive, manipulate, or mislead individuals or populations. This includes generation of disinformation at scale, deepfakes, subliminal manipulation, and pollution of the information ecosystem.

---

## Alignment with external frameworks

The taxonomy is formally linked to the following external frameworks using SKOS mapping properties (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`).

### Primary alignment targets

These frameworks provide concept-level URIs or structured identifiers suitable for formal linking.

#### W3C Data Privacy Vocabulary (DPV) — AI Extension
- **URL:** https://w3c.github.io/dpv/2.3/ai/
- **Repository:** https://github.com/w3c/dpv
- **Format:** RDF (Turtle, JSON-LD, RDF/XML)
- **Why:** The most comprehensive standards-based vocabulary for AI risks. Provides SKOS concepts for bias types, security attacks, AI lifecycle stages, and risk assessment processes. Includes extensions encoding the EU AI Act and GDPR in RDF. Maintained by a W3C community group with overlapping membership from the AIRO/VAIR ontology teams.
- **Coverage:** Strong across all Eticas categories except Agentic Risks and Environmental Impact.

#### MIT AI Risk Repository
- **URL:** https://airisk.mit.edu
- **Paper:** Slattery et al., *Patterns* (Cell Press), March 2026
- **Format:** Google Sheets / CSV (CC BY 4.0)
- **Why:** The largest systematic database of AI risks (1,725 entries from 74 source frameworks), organised into 7 domains and 24 subdomains. Provides the richest catalogue for mapping individual risk types.
- **Coverage:** Strong across all Eticas categories. Added multi-agent risks (Subdomain 7.6) in April 2025.

#### NIST AI 600-1 — Generative AI Risk Profile
- **URL:** https://doi.org/10.6028/NIST.AI.600-1
- **Format:** PDF
- **Why:** Defines 12 risk categories specific to generative AI, each mapped to NIST AI RMF trustworthiness characteristics. The most widely referenced US government framework for GenAI risk.
- **Coverage:** Strong for LLM-specific risks. Gaps: Agentic Risks, Transparency (addressed only through trustworthiness characteristics, not as a standalone risk).

### Secondary alignment targets

These provide authoritative definitions and regulatory context but lack concept-level URIs.

#### NIST AI RMF (AI 100-1)
- **URL:** https://www.nist.gov/itl/ai-risk-management-framework
- **Why:** Defines 7 Trustworthy AI characteristics and 4 core functions (Govern, Map, Measure, Manage) with 66 subcategories. Extensive crosswalk ecosystem to ISO 42001, EU AI Act, OECD, and others.

#### OECD AI Principles and Classification Framework
- **URL:** https://oecd.ai
- **Why:** Normative foundation adopted by 47 countries. The EU AI Act adopts OECD definitions verbatim. Five principles map to Eticas categories. The incident taxonomy provides structured harm classification.

#### ISO/IEC 42001 and ISO/IEC 23894
- **Why:** Certification-grade AI management system and risk management standards. The AIRO ontology provides a semantic bridge to ISO concepts. Paid standards — Eticas links to concepts by reference rather than reproducing content.

#### EU AI Act (via W3C DPV EU AI Act Extension)
- **URL:** https://w3c.github.io/dpv/legal/eu/aiact/
- **Why:** The DPV extension encodes the Act's risk tiers, roles, assessment types, and sector classifications in RDF, providing the machine-readable layer the EU has not published directly.

### Specialist references

#### AIRO — AI Risk Ontology
- **URL:** https://w3id.org/airo | https://github.com/DelaramGlp/airo
- **Why:** OWL 2 ontology modelling AI systems, domains, purposes, capabilities, and associated risks. Grounded in ISO 31000/23894. Designed to answer EU AI Act Annex III classification questions.

#### VAIR — Vocabulary of AI Risks
- **URL:** https://w3id.org/vair | https://github.com/DelaramGlp/vair
- **Why:** SKOS instantiation of AIRO with populated hierarchies across 21 facets.

#### AIR 2024 Taxonomy (Zeng et al.)
- **Paper:** arXiv:2406.17864
- **Why:** Most granular academic classification: 4 levels, 314 specific risk types. Powers the AIR-Bench safety benchmark (ICLR 2025).

---

## Category-level mapping table

| Eticas Category | MIT Domain | NIST AI 600-1 | NIST Trustworthy Characteristic | OECD Principle | W3C DPV |
|---|---|---|---|---|---|
| Bias & Fairness | 1. Discrimination & Toxicity | #6 Harmful Bias & Homogenization | Fair with Harmful Bias Managed | Fairness | `ai:AIBias` hierarchy |
| Privacy & Confidentiality | 2.1 Compromise of Privacy | #4 Data Privacy | Privacy-Enhanced | Privacy | `dpv:PersonalDataHandling` |
| Reliability | 7.3 Lack of Capability/Robustness | #2 Confabulation | Valid & Reliable | Robustness | `ai:Reliability` |
| Governance | 6.5 Governance Failure | #12 Value Chain Integration | Accountable & Transparent | Accountability | `dpv:GovernanceProcedures` |
| Security & Misuse | 2.2 + Domain 4 | #9 Information Security | Secure & Resilient | Security & Safety | `ai:SecurityAttack` hierarchy |
| Environmental Impact | 6.6 Environmental Harm | #5 Environmental Impacts | Safe | Sustainable Development | — |
| Transparency & Explainability | 7.4 Lack of Transparency | — | Explainable & Interpretable | Transparency | `ai:Transparency` |
| Responsibility & Redress | — | — | Accountable & Transparent | Accountability | `dpv:RightToRemedy` |
| Autonomy | 5.2 Loss of Agency | #7 Human-AI Configuration | — | — | `ai:HumanOversight` |
| Agentic Risks | 7.6 Multi-agent Risks | — | — | — | — |
| Manipulation & Misinformation | Domain 3 | #8 Information Integrity | — | Information Integrity (2024) | `ai:Misinformation` |

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
