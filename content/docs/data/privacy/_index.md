---
date: "2026-07-30T00:00:00+09:00"
title: "Data Privacy"
weight: 4
prev: "/docs/data"
---

Data privacy is the discipline of deciding when and how information about people may be collected, used, shared, retained, and deleted. It makes the effects of data processing on individuals visible, so that organizations can create value from data without treating people merely as sources of information.

Privacy is a cross-cutting concern in a data ecosystem. A dataset can move from an application into a platform, be combined with other records, used for analytics or AI, shared with a partner, and retained for years. Each stage can change what the data reveals and who is affected by it. Privacy provides the principles and controls for reasoning about those changes.

Privacy is therefore more than a compliance obligation. It is a condition for trustworthy data use. When people, customers, employees, and partners can understand how their information is handled, organizations can make better decisions about what to collect, which uses are justified, and which safeguards are needed.

## Privacy as a Cross-Cutting Concern

Privacy is closely connected to other data disciplines, but it is not interchangeable with them. Security helps protect data from unauthorized access, alteration, or loss. Privacy asks whether information about people should be processed for a particular purpose at all, and under what conditions. Strong security is necessary for privacy, but it cannot make an unjustified or unexpected use of personal data appropriate.

Data governance creates the policies, ownership, and decision processes that make privacy operational across a data estate. Data quality ensures that information is accurate and fit for purpose; it also matters to privacy because incorrect data can lead to harmful decisions about people. Compliance translates applicable legal, contractual, and industry obligations into requirements, while privacy provides the broader design discipline that should inform systems before a specific requirement is tested.

| Discipline           | Primary concern                                                 | Relationship to privacy                                                                       |
| -------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Data privacy         | Responsible processing of information about people              | Defines appropriate purposes, expectations, and protections throughout the lifecycle          |
| Information security | Protection against unauthorized access, alteration, and loss    | Supplies safeguards that privacy depends on, but does not determine appropriate use           |
| Data governance      | Accountability, policies, ownership, and decision rights        | Provides the operating model for applying privacy consistently                                |
| Data quality         | Accuracy, completeness, consistency, and fitness for use        | Reduces the risk of decisions or actions based on misleading personal information             |
| Compliance           | Meeting applicable legal, contractual, and industry obligations | Turns relevant obligations into verifiable requirements and evidence                          |
| AI governance        | Responsible development, deployment, and oversight of AI        | Extends privacy concerns to training data, inference, automated decisions, and feedback loops |

The same distinction is important when privacy is discussed alongside confidentiality. Confidentiality limits disclosure to authorized parties. Privacy also considers collection, analysis, inference, secondary use, and retention. A confidential record can still be used in a way that is unexpected, excessive, or harmful.

## Core Privacy Principles

Privacy principles are useful as decision lenses. They are not a substitute for context, risk assessment, or applicable obligations, but they help teams ask the right questions before data becomes difficult to change or withdraw.

### Purpose Limitation

Collect and use data for clear, specific, and legitimate purposes. A team that collects an email address to send a service notification should not assume that the same address is available for unrelated profiling or outreach. Purpose gives data use a boundary that can be communicated, governed, and reviewed.

### Data Minimization

Use the least amount of information needed for the purpose. Minimization concerns both the fields collected and the precision, duration, and audience of processing. For example, a newsletter subscription needs an email address to deliver messages; it does not need a date of birth, home address, or a copy of an identity document unless a separate, specific purpose requires those details.

### Transparency

People should be able to understand, in meaningful terms, what information is processed, why it is processed, and how it may affect them. Transparency is not only a notice or policy document. Clear data descriptions, understandable product behavior, and visible boundaries around automated decisions all support it.

### Accountability

Organizations need identifiable owners for data uses and evidence that privacy decisions have been made and reviewed. Accountability turns principles into a repeatable practice: someone owns the purpose, the data flow is understood, controls are maintained, and exceptions can be examined.

### Individual Participation

People have an interest in knowing about, influencing, and correcting the processing of information about them. Consent is one important mechanism for expressing a person's informed choice when it is appropriate to the context; it should be understandable, specific to the choice being made, and possible to withdraw. The exact mechanisms vary by context, but the underlying principle prevents data systems from treating individuals as passive subjects of opaque records.

### Retention Limitation

Data should not persist indefinitely merely because storage is inexpensive. Retention should reflect the purpose, operational need, and applicable obligations. Clear lifecycle states—active, archived, and deleted—make it less likely that historical data is reused without scrutiny.

### Privacy by Design and by Default

Privacy should shape a system while it is being designed, rather than being added only after data flows are established. Defaults matter as much as features: a workflow that exposes data broadly unless someone opts out creates a different privacy posture from one that starts with restricted access and deliberate expansion.

Together, these principles guide ordinary platform decisions. Before collecting an attribute, a team can ask what purpose requires it. Before granting access, it can ask whether the recipient needs the information in identifiable form. Before reusing a dataset, it can test whether the new use remains within the original context and expectations. Before retaining a record, it can ask when it should cease to be useful.

## From Principles to Operational Controls

No single technology or policy provides privacy. Effective privacy emerges from several controls that work together across the data lifecycle.

**Data classification** makes the sensitivity and handling needs of data visible. It distinguishes data that can be shared freely from data that requires restricted access or stronger safeguards. Classification also helps teams recognize that identifiability can arise from combinations of attributes, not only obvious identifiers such as names or account numbers.

**Purpose and use controls** connect datasets to the reasons they were collected and the conditions under which they may be used. They reduce the risk that convenient data is repurposed without a deliberate decision. Metadata, data contracts, and clear documentation can help preserve this context as datasets move between teams and systems.

**Access management** ensures that only appropriate people, services, and workloads can obtain sensitive information. Least-privilege access, segregation of duties, and reviewable authorization decisions limit unnecessary exposure, but access control should be informed by the intended use rather than treated as a complete privacy solution.

**De-identification** can reduce the risk that data is linked back to a person. Techniques such as pseudonymization, aggregation, generalization, and anonymization have different properties and limitations. Their suitability depends on the data, the context, the recipients, and the realistic possibility of re-identification.

**Lifecycle management** applies retention, archival, and deletion decisions consistently. It prevents obsolete copies, forgotten extracts, and retired systems from becoming ungoverned stores of personal information. Lifecycle controls also need to account for downstream datasets, backups, and derived outputs.

**Governance and evidence** establish who makes privacy decisions, how exceptions are handled, and how controls can be demonstrated over time. Data owners, stewards, privacy specialists, security teams, and platform teams have different responsibilities, but their decisions should connect through shared policies, metadata, and review processes.

These capabilities reinforce one another. Classification informs access controls. Purpose information informs reuse and retention decisions. Governance connects technical safeguards with accountable ownership. Together, they make responsible data use easier to sustain as systems, teams, and uses evolve.

## Recommended Reading Flow

This section is organized as a documentation library rather than one long article. Start here for the shared concepts, then choose a deeper topic based on the question you need to answer.

{{< cards >}}
{{< card link="privacy-fundamentals/" title="Privacy Fundamentals (TBD)" icon="book-open" subtitle="Core principles, terminology, and decision lenses" >}}
{{< card link="personal-data-and-pii/" title="Personal Data and PII (TBD)" icon="identification" subtitle="Identifiers, sensitive data, and re-identification risk" >}}
{{< card link="privacy-harms/" title="Privacy Harms (TBD)" icon="exclamation" subtitle="How collection, use, disclosure, and interference can affect people" >}}
{{< card link="data-classification/" title="Data Classification (TBD)" icon="tag" subtitle="Classifying data according to sensitivity and handling needs" >}}
{{< card link="de-identification/" title="De-identification (TBD)" icon="eye-off" subtitle="Reducing identifiability through anonymization, pseudonymization, and related techniques" >}}
{{< card link="privacy-engineering/" title="Privacy Engineering (TBD)" icon="cog" subtitle="Embedding privacy requirements into systems and data flows" >}}
{{< card link="sensitive-data-protection/" title="Sensitive Data Protection (TBD)" icon="lock-closed" subtitle="Safeguards for data that requires stronger handling controls" >}}
{{< card link="privacy-governance/" title="Privacy Governance (TBD)" icon="scale" subtitle="Accountability, policies, roles, and evidence across the lifecycle" >}}
{{< /cards >}}

## Summary

Data privacy is a continuous design and governance discipline. It helps organizations decide what information about people they need, why they need it, how long they should keep it, and which safeguards and accountability mechanisms make its use responsible.

When privacy is embedded in data collection, platform design, access decisions, reuse, and lifecycle management, it creates a foundation for trustworthy data systems. That foundation enables organizations to use data with greater clarity, resilience, and respect for the people represented in it.
