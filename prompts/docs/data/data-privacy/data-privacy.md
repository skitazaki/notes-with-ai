---
type: prompt
path: /docs/data/privacy
---

# Prompt — Generate a Documentation Article for "Data Privacy"

You are an expert in data management, data governance, privacy engineering, information security, and technical documentation.

Write a comprehensive documentation section for **Notes with AI**, a documentation website for data professionals, architects, platform engineers, governance teams, and technical leaders.

The writing should be educational rather than academic, practical rather than legal, and vendor-neutral.

The article should explain concepts from first principles before introducing implementation guidance.

Assume readers understand data platforms but are not privacy specialists.

---

## Writing Style

- Clear and authoritative
- Practical and implementation-oriented
- Neutral and vendor-neutral
- Use diagrams where appropriate (described in Mermaid)
- Explain _why_ before _how_
- Include examples throughout
- Avoid legal advice
- Prefer internationally applicable concepts over country-specific regulations
- Explain terminology before using abbreviations
- Separate theory from implementation
- Use tables wherever comparisons improve understanding

---

# Document Structure

Because the article is large, generate multiple Markdown pages.

Each page should be able to stand alone while linking naturally to the others.

Suggested hierarchy:

```
Data Privacy

├── Overview
├── Why Privacy Matters
├── Privacy Fundamentals
├── Personal Data and PII
├── Privacy Harms (Daniel J. Solove)
├── Confidential Data Classification
├── Data Anonymization
├── Privacy Engineering
├── Protecting Sensitive Data
├── Privacy Governance
├── Architecture Patterns
├── Best Practices
└── References
```

Each page should contain

- Executive Summary
- Main concepts
- Practical examples
- Key Takeaways
- Related Pages

---

# Topics to Cover

## 1. Introduction

Explain

- What Data Privacy is
- Why privacy differs from security
- Relationship between
  - Data Privacy
  - Information Security
  - Data Governance
  - Data Quality
  - Compliance
  - AI Governance

Include a conceptual diagram showing the overlap between these disciplines.

---

## 2. Why Data Privacy Matters

Discuss

- Customer trust
- Regulatory compliance
- Ethical data use
- Responsible AI
- Digital transformation
- Data sharing
- Cross-border data movement

Explain that privacy is not merely compliance but a design principle.

---

## 3. Fundamentals of Data Privacy

Explain foundational principles including

- Purpose limitation
- Data minimization
- Transparency
- Lawful processing
- Accountability
- Individual rights
- Consent
- Storage limitation
- Accuracy
- Security safeguards
- Privacy by Design
- Privacy by Default

Compare common principles appearing across major privacy frameworks without focusing on one regulation.

---

## 4. Personal Information and PII

Explain the differences between

- Personal Information
- Personal Data
- Personally Identifiable Information (PII)
- Sensitive Personal Information
- Special Category Data
- Confidential Information

Describe

Direct identifiers

Examples

- Name
- Passport
- Email

Indirect identifiers

Examples

- ZIP code
- Date of birth
- Device identifiers
- IP addresses
- Browser fingerprints

Quasi-identifiers

Explain re-identification risk.

Provide a comparison table.

---

## 5. Daniel J. Solove's Theory of Privacy

Provide a detailed explanation of Daniel J. Solove's taxonomy of privacy.

Explain why privacy cannot be reduced to secrecy.

Describe the four categories:

### Information Collection

- Surveillance
- Interrogation

### Information Processing

- Aggregation
- Identification
- Insecurity
- Secondary Use
- Exclusion

### Information Dissemination

- Breach of Confidentiality
- Disclosure
- Exposure
- Increased Accessibility
- Blackmail
- Appropriation
- Distortion

### Invasion

- Intrusion
- Decisional Interference

For every category

Describe

- definition
- examples
- enterprise examples
- AI examples
- mitigation strategies

Include a taxonomy diagram.

Explain how Solove's framework complements regulatory approaches by focusing on privacy harms.

---

## 6. Confidential Data Classification

Explain enterprise information classification.

Describe categories such as

- Public
- Internal
- Confidential
- Restricted
- Highly Restricted

Explain classification based on

- Business impact
- Privacy impact
- Regulatory obligations
- Financial risk
- Reputation

Describe ownership responsibilities.

Include a responsibility matrix.

---

## 7. Data Anonymization

Explain the differences between

- Anonymous data
- Pseudonymized data
- De-identified data
- Masked data
- Tokenized data
- Encrypted data

Explain techniques including

- Suppression
- Generalization
- Perturbation
- Randomization
- Noise injection
- Hashing
- Tokenization
- Differential Privacy
- Synthetic Data

Describe

- strengths
- weaknesses
- re-identification risks
- appropriate use cases

Include comparison tables.

---

## 8. Privacy Engineering

Explain engineering approaches including

- Privacy by Design
- Privacy by Default
- Data lifecycle protection
- Least privilege
- Encryption
- Access control
- Data masking
- Consent management
- Audit logging
- Data retention
- Secure deletion

Include architectural diagrams.

---

## 9. Managing Confidential Data

Describe practical enterprise guidance.

Include

Data discovery

Classification

Cataloging

Metadata

Access management

Data contracts

Retention

Deletion

Data sharing

Data lineage

Monitoring

Incident response

Secrets management

Key management

AI training datasets

LLM prompt privacy

Data residency

Cross-border transfer

Provide examples from enterprise data platforms.

---

## 10. Privacy Governance

Explain

Roles

- Data Owner
- Data Steward
- Privacy Officer
- Security Team
- Legal
- Platform Team
- Domain Team

Describe governance processes.

Include RACI examples.

---

## 11. Architecture Patterns

Describe architectures supporting privacy.

Include

- Data Lake
- Data Warehouse
- Lakehouse
- Data Mesh
- MDM
- Data Catalog
- AI Platform

Explain

where privacy controls should exist.

Include layered architecture diagrams.

---

## 12. AI and Data Privacy

Discuss

- LLM data leakage
- Prompt privacy
- Retrieval-Augmented Generation (RAG)
- Embedding privacy
- AI agents
- Training data
- Model inversion attacks
- Membership inference
- Synthetic data for AI
- Privacy-preserving machine learning
- Federated learning

Explain emerging privacy risks.

---

## 13. Best Practices

Provide practical recommendations.

Examples include

- Classify before collecting
- Collect only necessary data
- Separate identifiers
- Encrypt sensitive data
- Monitor access continuously
- Minimize copies
- Define retention schedules
- Automate deletion
- Test anonymization
- Document data flows
- Perform privacy impact assessments
- Build privacy into architecture reviews

---

## 14. Common Misconceptions

Include a table correcting myths such as

- Encryption alone ensures privacy.
- Anonymous data can never be re-identified.
- Privacy equals security.
- Compliance guarantees privacy.
- Consent solves every privacy problem.

---

## 15. Glossary

Define all important terminology.

---

## 16. References

Recommend authoritative references including works by:

- Daniel J. Solove
- Helen Nissenbaum
- OECD Privacy Guidelines
- ISO/IEC 27701
- ISO/IEC 29100
- NIST Privacy Framework
- ENISA privacy engineering guidance

---

# Visuals

Throughout the article, include Mermaid diagrams for:

- Privacy ecosystem
- Data lifecycle
- Solove taxonomy
- Confidential data classification
- Data anonymization decision tree
- Privacy architecture layers
- Enterprise governance model
- Privacy engineering workflow

---

# Writing Requirements

- Approximately 25,000–35,000 words across all pages.
- Use Markdown with Hugo-compatible headings.
- Use relative links for cross-references between pages.
- Include callout blocks for **Note**, **Best Practice**, **Warning**, and **Example**.
- End each page with:
  - Summary
  - Related pages
  - Further reading

The final result should read like a professional technical documentation set for enterprise architects, data engineers, governance specialists, and AI platform teams, balancing conceptual foundations with actionable implementation guidance.
