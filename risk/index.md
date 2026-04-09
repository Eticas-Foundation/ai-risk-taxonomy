---
layout: default
title: "Eticas AI Risk Taxonomy"
---

# Eticas AI Risk Taxonomy

Version 0.1.0

A unified AI risk taxonomy for use across Eticas audit methodologies, assessment frameworks, and reporting outputs.

## Required categories

Assessed in every Eticas audit.

### [Bias & Fairness](bias-fairness) <span class="badge badge-established">established</span>

The risk that an AI system produces outcomes that systematically advantage or disadvantage individuals or groups based on protected or sensitive attributes, leading to unequal treatment, reduced accuracy, or unjust impacts.

- [Dataset bias and under/over-representation](dataset-bias)
- [Proxy discrimination through correlated features](proxy-discrimination)
- [Intersectional unfairness](intersectional-unfairness)
- [Accessibility barriers](accessibility-barriers)
- [Geographic, cultural, or language skew](geographic-cultural-language-skew)
- [Feedback loops reinforcing inequality](feedback-loops)
- [Quality of service disparity across groups](quality-of-service-disparity)
- [Unequal allocation of opportunity](allocation-of-opportunity)
- [Stereotyping and demeaning content](stereotyping-demeaning-content)
- [Harmful content and toxicity](harmful-content-toxicity)
- [Sentiment fairness across groups](sentiment-fairness)
- [Performance equity across populations](performance-equity)

### [Privacy & Confidentiality](privacy-confidentiality) <span class="badge badge-established">established</span>

The risk that an AI system collects, processes, or infers personal information in ways that infringe on individuals' rights to control their data (privacy), or that sensitive information is exposed, accessed, or shared without authorization (confidentiality).

- [Unlawful collection or processing of personal data](unlawful-data-processing)
- [Re-identification of anonymised data](re-identification)
- [Function creep](function-creep)
- [Biometric surveillance](biometric-surveillance)
- [Emotion inference or sensitive attribute profiling](emotion-inference-profiling)
- [Weak data retention, erasure, and access controls](weak-data-controls)
- [PII leakage through model outputs](pii-leakage)
- [Membership inference risk](membership-inference)

### [Reliability](reliability) <span class="badge badge-established">established</span>

The risk that an AI system produces false, fabricated, or misleading outputs (hallucinations), spreads inaccurate or deceptive information (misinformation), or delivers inconsistent results across similar inputs and contexts.

- [Hallucination and fabricated outputs](hallucination)
- [Output inconsistency](output-inconsistency)
- [Output drift over time](output-drift)
- [Out-of-distribution robustness](out-of-distribution-robustness)
- [Failure and remediation gaps](failure-remediation-gaps)
- [Monitoring and evaluation gaps](monitoring-evaluation-gaps)

### [Governance](governance) <span class="badge badge-established">established</span>

The risk that an AI system lacks adequate structures, policies, or accountability mechanisms to oversee its design, deployment, and use.

- [Unclear responsibilities and accountability gaps](unclear-responsibilities)
- [Poor documentation](poor-documentation)
- [Limited auditability](limited-auditability)
- [Regulatory non-compliance](regulatory-non-compliance)
- [Lack of change management](lack-of-change-management)
- [Oversight of significant adverse impacts](oversight-of-adverse-impacts)
- [Fitness for purpose](fitness-for-purpose)
- [Data governance](data-governance)
- [Human oversight and control](human-oversight-control)
- [Decision traceability](decision-traceability)
- [Critical input/output logging](input-output-logging)
- [Responsible actor attribution](responsible-actor-attribution)
- [Task success](task-success)

### [Security & Misuse](security-misuse) <span class="badge badge-established">established</span>

The risk that an AI system is exposed to vulnerabilities, attacks, or misuse that compromise its integrity, availability, or confidentiality.

- [Adversarial attacks](adversarial-attacks)
- [Prompt injection](prompt-injection)
- [Jailbreaking](jailbreaking)
- [Unauthorized access](unauthorized-access)
- [Supply-chain vulnerabilities](supply-chain-vulnerabilities)
- [Incident response gaps](incident-response-gaps)
- [Misuse beyond intended purpose](misuse-beyond-intended-purpose)

### [Transparency & Explainability](transparency-explainability) <span class="badge badge-established">established</span>

The risk that stakeholders cannot understand how an AI system works, what it does, or why it produces specific outputs.

- [AI system explainability](system-explainability)
- [Communication to stakeholders](stakeholder-communication)
- [Disclosure of AI interaction](ai-interaction-disclosure)
- [Model card completeness](model-card-completeness)
- [Prompt transparency](prompt-transparency)

## Audit-dependent categories

Assessed based on engagement scope and system type.

### [Environmental Impact](environmental-impact) <span class="badge badge-established">established</span>

The risk that an AI system's development, deployment, or use causes negative environmental effects, such as excessive energy or water consumption, carbon emissions, or unsustainable use of hardware and resources.

- [Inference-time energy consumption](inference-energy-consumption)
- [Training resource consumption](training-resource-consumption)
- [Hardware efficiency](hardware-efficiency)

### [Responsibility & Redress](responsibility-redress) <span class="badge badge-developing">developing</span>

The risk that individuals affected by AI-driven decisions have no effective means to understand, challenge, or seek remedy for those decisions.

- [Absence of appeal mechanisms](absence-of-appeal)
- [Unclear remediation procedures](unclear-remediation)
- [Ineffective communication with affected parties](ineffective-communication)

### [Autonomy & Human Agency](autonomy) <span class="badge badge-provisional">provisional</span>

The risk that an AI system undermines individuals' ability to make free, informed decisions, whether through over-reliance, automation bias, manipulative design, or erosion of human agency..

### [Agentic Risks](agentic-risks) <span class="badge badge-provisional">provisional</span>

The risk that AI systems operating with a degree of autonomy — planning, executing multi-step actions, using tools, or coordinating with other AI agents — introduce failure modes not present in single-inference systems.

### [Manipulation & Misinformation](manipulation-misinformation) <span class="badge badge-provisional">provisional</span>

The risk that AI systems are used — intentionally or through design flaws — to deceive, manipulate, or mislead individuals or populations.
