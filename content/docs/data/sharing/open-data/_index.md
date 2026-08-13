---
date: "2026-08-13T00:00:00+09:00"
title: "Open Data"
weight: 5
prev: "/docs/data/sharing/data-spaces"
next: "/docs/data/sharing"
---

Open data is data that anyone is free to access, use, modify, and share, subject at most to conditions that preserve provenance and openness. It is a publication and reuse model within the broader [Data Sharing](/docs/data/sharing/) landscape.

Open data is not merely data that can be viewed without payment. Durable openness depends on legal permission, practical accessibility, machine-readable formats, adequate documentation, and governance that protects rights and legitimate restrictions.

## What Makes Data Open

The [Open Definition 2.1](https://opendefinition.org/od/2.1/en/) describes open knowledge as material anyone may access, use, modify, and share. This requires more than a public URL.

| Dimension         | Requirement                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Legal             | An open license or public-domain status permits reuse and redistribution                                    |
| Technical         | Data is available in machine-readable, non-discriminatory formats                                           |
| Access            | Users can obtain it without unnecessary registration or negotiation                                         |
| Metadata          | Scope, provenance, units, schema, quality, and update behavior are understandable                           |
| Operational       | Publication is reliable, versioned, and maintained over time                                                |
| Rights and safety | Privacy, confidentiality, security, intellectual property, and community harms are addressed before release |

“Publicly accessible” and “openly licensed” are not synonyms. A dashboard may be publicly visible while prohibiting extraction or reuse. A downloadable file may lack any license, leaving users unable to determine what they may legally do with it.

## Open by Default, With Purpose

The [Open Data Charter](https://opendatacharter.org/principles/) describes six principles: open by default; timely and comprehensive; accessible and usable; comparable and interoperable; used for improved governance and citizen engagement; and used for inclusive development and innovation.

Open by default is a policy presumption, not an instruction to publish every dataset. Legitimate reasons for restriction include personal privacy, confidentiality, security, protected cultural or community knowledge, contractual duties, intellectual property, and risks created by combination with other datasets.

Publication should also be purposeful. Producers should understand intended public outcomes, likely users, excluded or affected communities, and the resources required to keep data accurate and usable.

## Open Data Architecture

An open-data service normally includes:

- a publishing workflow with classification and disclosure review
- stable dataset identifiers and version information
- an open license attached to the dataset and distributions
- a catalog with searchable metadata
- downloadable distributions in open, documented formats
- APIs or bulk access where they improve use without discriminating among consumers
- provenance, quality, temporal and geographic coverage, and update schedules
- change notices, archives, corrections, and deprecation procedures
- usage feedback and impact measurement that do not require tracking every user

[DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) distinguishes a conceptual dataset from its distributions and data services. This is useful for publishing one dataset through CSV, JSON, an API, or other representations while keeping a shared identity and metadata record.

## Licensing and Attribution

An open license should clearly allow access, use, modification, and redistribution. Some licenses require attribution or require derivatives to remain open. Restrictions that discriminate by user, field of endeavor, or commercial purpose generally prevent data from meeting the Open Definition.

License compatibility matters when combining datasets. Attribution requirements should be practical at scale, and the publisher should have authority to apply the license. Publishing third-party content under an incompatible open license does not create legitimate openness.

## Privacy and Responsible Release

Open publication is difficult to reverse. Once copied and redistributed, access controls and revocation cannot reliably recall the data. Disclosure review must therefore occur before release.

Removing names is often insufficient. Rare attributes, locations, timestamps, and linkage with other public data can re-identify people or expose sensitive groups. [Data Privacy](/docs/data/privacy/) provides decision principles such as purpose limitation, minimization, transparency, and retention. Aggregation, generalization, synthetic data, delayed release, or non-open controlled access may be more appropriate when privacy risk remains material.

Openness can also affect communities even when records are not personal data. Publishers should consider security, environmental sensitivity, indigenous data governance, discrimination, and asymmetric benefits between organizations able to exploit the data and communities represented within it.

## Quality, Usability, and Maintenance

Open data creates value only when users can interpret and depend on it. Publication should include definitions, units, codes, identifiers, collection methods, limitations, known gaps, update cadence, and contact or feedback paths.

Stable identifiers and version history let users cite and reproduce results. Machine-readable schemas and standard vocabularies improve comparison. Bulk download protects users from API dependency, while APIs can support selective and current access. Neither interface compensates for unclear meaning or abandoned maintenance.

## Value and Measurement

Open data can support transparency, accountability, research, public services, civic participation, education, and commercial innovation. These benefits may be indirect and distributed across society.

Useful measures include dataset freshness, availability, documentation completeness, reuse in research or services, issue resolution, user diversity, and demonstrated public outcomes. Download counts alone do not reveal whether the data was understood, useful, or equitably accessible.

## Common Failure Modes

- Publishing data without an explicit open license
- Providing only a human-facing dashboard or proprietary format
- Treating anonymization as removal of direct identifiers
- Releasing many low-value datasets while neglecting high-demand data
- Omitting definitions, provenance, limitations, and update commitments
- Breaking URLs or schemas without versioning and notice
- Measuring success only through portal inventory and downloads
- Assuming openness is always safer or more valuable than controlled sharing

## Summary

Open data is governed sharing for broad, non-discriminatory reuse. It combines legal permission, technical accessibility, metadata, quality, maintenance, and responsible disclosure.

The durable goal is not maximum publication. It is to make appropriate data genuinely reusable while protecting people, communities, security, and rights that openness cannot restore once information has been released.
