---
type: blog
path: /blog/coding-agent-architecture
description: Future standalone blog brief for exploring concrete model, endpoint, runtime, and integration choices in coding-agent architectures.
---

# Future Blog Brief — Coding-Agent Architecture Choices

## Status

Keep this brief as a candidate for a future standalone blog article. The examples below were intentionally removed from the evergreen [Coding Agents documentation page](/docs/swe/ai-as-software-engineering-tool/coding-agents/) when that page was refocused on durable concepts. They are retained here as research leads, not as verified current recommendations. Do not draft or publish the article until its scope and timing are confirmed.

## Working angle

Explain how teams assemble a coding-agent system from several independent choices: interaction surface, model family, endpoint, access pattern, tool integrations, and execution location. Use concrete provider and platform examples to show that model families and endpoints are not one-to-one, and that running a model locally is a separate decision from running repository tools locally.

The article should be useful to enterprise architects, platform engineers, and engineering leaders comparing deployment and integration topologies. It should help readers ask which system performs each job, where it runs, which network paths it needs, and what authority it receives.

## Research leads to preserve

### Access patterns

- **Cloud-managed access:** investigate examples such as GitHub Copilot and direct model APIs, including OpenAI, Anthropic, and Gemini APIs, as well as Azure OpenAI. Compare operational simplicity and elastic capacity with provider policy, region, quota, network-path, and data-boundary constraints.
- **Self-managed cloud inference:** investigate teams operating inference on AWS, Azure, or Google Cloud. Explain the control this can provide alongside responsibility for operations, observability, security hardening, capacity, and cost.
- **Local model execution:** investigate models running on developer workstations or internal infrastructure. Cover privacy or offline use cases together with hardware, model-size, throughput, and maintenance constraints.

Treat these as access patterns, not maturity stages. Do not assume that a coding agent's repository tools run in the same place as its model.

### Model families and endpoints are not one-to-one

Research and verify examples of a model family being available through more than one endpoint or platform:

- OpenAI-family models through OpenAI endpoints, Azure OpenAI, and GitHub Copilot.
- Anthropic models through Anthropic APIs and cloud-hosted offerings such as Claude on Amazon Bedrock; verify the current naming, availability, and relationship of Claude Platform on AWS before using it as an example.
- Google models through Gemini API and Gemini Enterprise Agent Platform.
- Microsoft model families through Microsoft Foundry.

The point is the topology, not a vendor catalog: show that the selected model family, endpoint, and access pattern are separate dimensions, and that compatibility and availability depend on the service and region.

### Gateways and hybrid routing

- Investigate Databricks Unity Gateway and Snowflake Cortex AI as platform-mediated ways to access and govern models. Verify current product names, capabilities, supported model providers, and regional availability against official documentation.
- Investigate ngrok as an example of a routing and security layer connecting cloud and local model endpoints in a hybrid setup. Verify the exact current capabilities and avoid implying it is itself a model host or an agent runtime.

Explain where a gateway or routing layer sits in the request path, what policies it can enforce, and how it differs from both the coding agent and the repository execution environment.

### Open-weight and open-source model options

Preserve Llama, Mistral, and Qwen as examples to investigate for cloud or local deployment. Discuss evaluation quality, guardrails, update cadence, hardware fit, and operational ownership. Verify current model licensing and deployment terms before making comparative claims; do not treat “open-weight” and “open-source” as interchangeable labels.

## Suggested article structure

1. **Start with the topology:** distinguish the human-facing surface, agent orchestrator, model interaction, repository tools, external engineering systems, and people reviewing the work.
2. **Separate the choices:** explain surface, model family, endpoint, access pattern, and execution location as related but independent decisions.
3. **Trace one task:** follow an issue from context retrieval through a local or remote repository workspace, validation, and pull-request handoff.
4. **Compare deployment patterns:** use cloud-managed, self-managed cloud, local, and hybrid examples without presenting them as a ranking.
5. **Explain boundaries:** cover local filesystem and Git access, command execution, network egress, credentials, hosted repository operations, and CI runner isolation.
6. **Offer a decision framework:** help readers select a topology based on task risk, latency, data boundaries, hardware, integration needs, operational capacity, and review requirements.

## Evidence and editorial constraints

- Verify all product names, model availability, endpoints, regions, and capabilities using current official documentation before publication. Product details are time-sensitive.
- Prefer vendor documentation for service-specific claims and clearly separate verified facts from architectural interpretation.
- Present provider and platform names as examples, not endorsements or an exhaustive market map.
- Do not imply every coding agent supports every model, endpoint, system integration, or access pattern.
- Keep the distinction clear between **where inference runs** and **where repository tools execute**. A local model can use a remote workspace; a hosted model can control tools running on a developer workstation.
- Distinguish local repository state from a hosted repository service, and distinguish a CI service from the runner that executes its jobs.
- Explain that local execution does not automatically grant unrestricted filesystem or network access, and remote execution is not automatically isolated or trusted.
- Keep the article focused on architecture choices and their consequences; leave evergreen definitions and general task-boundary guidance on the documentation page.
