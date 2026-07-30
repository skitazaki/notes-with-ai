---
type: docs
path: /docs/data/privacy
---

Write a concise documentation hub page (roughly 1,200–1,500 words) titled:
"Data Privacy"

You are a senior privacy engineer, data governance practitioner, and technical writer. Create the overview page for the Data Privacy section of a vendor-neutral technical documentation site.

Audience:

- Technology leaders, data architects, platform engineers, data governance practitioners, and senior engineers
- Readers understand data platforms but are not necessarily privacy specialists

Purpose:

- Define data privacy and explain why it is a cross-cutting concern in the data lifecycle
- Give readers a durable conceptual model before they navigate to more focused privacy topics
- Clarify the relationship between privacy, security, governance, compliance, and responsible AI
- Act as the navigation hub for the Data Privacy documentation library

Scope:

- Treat privacy as the responsible processing of information about people, including the risks created by collection, use, sharing, retention, and inference
- Explain why privacy is broader than confidentiality and why privacy and security are related but distinct disciplines
- Introduce privacy principles: purpose limitation, data minimization, transparency, accountability, individual participation, retention limitation, and privacy by design
- Explain at a high level how data classification, lifecycle controls, access controls, de-identification, governance, and privacy engineering support those principles
- Describe the library as a set of complementary documents rather than attempting to teach every topic in one page

Do not make this page a regulatory guide, legal interpretation, implementation manual, threat catalog, or exhaustive taxonomy of personal data.

Tone and style:

- Neutral, explanatory, precise, and practical
- Concept-first and evergreen; explain why before how
- Use plain language, defining terms before abbreviations such as PII
- Use brief enterprise or data-platform examples only where they make a concept concrete
- Avoid hype, vendor references, legal advice, jurisdiction-specific requirements, and future predictions

Required structure:

1. **Opening overview**
   - Define data privacy in two or three paragraphs.
   - Establish that privacy enables trustworthy use of data; it is not only a compliance obligation.
   - Explain that privacy applies across collection, storage, use, sharing, and deletion.

2. **Privacy as a cross-cutting concern**
   - Explain the relationship and boundaries among data privacy, information security, data governance, compliance, data quality, and AI governance.
   - Include a compact comparison table with columns for discipline, primary concern, and its relationship to privacy.
   - Make clear that security safeguards data, while privacy governs whether and how information about people should be processed.

3. **Core privacy principles**
   - Present the principles as durable decision lenses, not as a checklist for a particular law.
   - Briefly explain purpose limitation, minimization, transparency, accountability, individual participation, retention limitation, and privacy by design/default.
   - Connect the principles to ordinary data-platform decisions such as collecting an attribute, granting access, reusing a dataset, or retaining a record.

4. **From principles to operational controls**
   - Introduce, without deep implementation detail, the controls and practices that make privacy operational: data classification, purpose and use controls, access management, de-identification, lifecycle management, governance, and evidence/auditability.
   - Emphasize that no single control provides privacy on its own.

5. **Recommended reading flow**
   - State explicitly that this section is a documentation library rather than a single long article.
   - Add a Hugo `cards` block that links to the planned child pages below. Use relative links and concise, descriptive subtitles.

   ```md
   {{< cards >}}
   {{< card link="privacy-fundamentals/" title="Privacy Fundamentals" icon="book-open" subtitle="Core principles, terminology, and decision lenses" >}}
   {{< card link="personal-data-and-pii/" title="Personal Data and PII" icon="identification" subtitle="Identifiers, sensitive data, and re-identification risk" >}}
   {{< card link="privacy-harms/" title="Privacy Harms" icon="exclamation" subtitle="How collection, use, disclosure, and interference can affect people" >}}
   {{< card link="data-classification/" title="Data Classification" icon="tag" subtitle="Classifying data according to sensitivity and handling needs" >}}
   {{< card link="de-identification/" title="De-identification" icon="eye-off" subtitle="Reducing identifiability through anonymization, pseudonymization, and related techniques" >}}
   {{< card link="privacy-engineering/" title="Privacy Engineering" icon="cog" subtitle="Embedding privacy requirements into systems and data flows" >}}
   {{< card link="sensitive-data-protection/" title="Sensitive Data Protection" icon="lock-closed" subtitle="Safeguards for data that requires stronger handling controls" >}}
   {{< card link="privacy-governance/" title="Privacy Governance" icon="scale" subtitle="Accountability, policies, roles, and evidence across the lifecycle" >}}
   {{< /cards >}}
   ```

6. **Summary**
   - Reinforce that effective privacy is a continuous design and governance discipline that enables responsible data use.

Constraints:

- Produce one hub page only; do not generate the child pages.
- Do not include step-by-step implementation instructions, product selections, or configuration examples.
- Do not provide legal advice, claim universal legal requirements, or center the article on named regulations.
- Do not reproduce Daniel J. Solove's privacy-harm taxonomy here; reserve its detailed treatment for the Privacy Harms child page.
- Do not add an executive summary, key-takeaway section, reference list, or Mermaid diagram. The opening, conceptual sections, and navigation cards should carry the page.
