+++
date = '2025-12-04T22:29:49+09:00'
title = 'Twelve-Factor App'
+++

**Twelve-Factor** is a concise, language-agnostic manifesto for building cloud-native SaaS apps, which are single
codebase tracked in VCS, clear separation of config from code, stateless processes, backing services as attached
resources, logs as event streams, etc.

Below I’ll give a compact refresher of the twelve factors, then dive deep into how teams typically implement them in
**Go** and **Python** — including concrete libraries, idiomatic patterns, short code examples, and short case-study
pointers.

## The Twelve Factors in short guide

Official Twelve-Factor site: [12factor.net][1]

1. **Codebase** — One repo per app, many deploys. Use VCS (git). Best practice: keep infra/ops scripts in the same repo
   or an adjacent infra repo with clear build/release docs.

2. **Dependencies** — Explicitly declare & isolate (lock files, vendoring). Use language-native package management + CI
   to reproduce builds.

3. **Config** — Store _config_ in environment variables (don’t bake secrets/config into code). Best practice: treat
   `DATABASE_URL`, API keys, feature flags as env vars or secrets; never commit `.env` to VCS.

4. **Backing services** — Treat DBs, caches, message brokers as attached resources (config points to them). Use
   connection URLs and allow swapping services without code change.

5. **Build, release, run** — Separate build (artifact) from release (combine artifact + config) from run (execute
   processes). Automate with CI/CD.

6. **Processes** — Execute as one or more stateless processes; persist state in backing services.

7. **Port binding** — Export services by binding to a port (HTTP servers bind to `$PORT`), making the app
   self-contained.

8. **Concurrency** — Scale by running multiple process types; processes are first-class for horizontal scaling.

9. **Disposability** — Fast startup and graceful shutdown (SIGTERM handling, readiness/liveness probes in K8s).

10. **Dev/prod parity** — Keep dev, staging, prod similar: data, time, personnel, and dependencies.

11. **Logs** — Treat logs as event streams; delegate capture/aggregation to the execution environment (e.g., structured
    logs → stdout/stderr → aggregator).

12. **Admin processes** — Run one-off admin/maintenance tasks in the same environment as the app (migrations, REPLs).

Twelve-Factor is intentionally simple and prescriptive at a conceptual level; many teams adopt it as a baseline and
extend with service meshes, secrets managers, telemetry/observability, and platform-specific patterns (Kubernetes,
serverless, etc.).

Twelve-Factor was created from Heroku’s experience and remains the canonical guidance. In 2024/2025 the Twelve-Factor
project was open-sourced by Heroku to let the community evolve it. Use the canonical site for the authoritative list and
rationale. ([Heroku blog][15] on November 12, 2024)

<!-- deno-fmt-ignore-start -->
{{< callout type="warning" >}}
**When is Twelve-Factor not a perfect fit?** — State-heavy apps (rich client state, low-latency on-device logic), some
  legacy monoliths, and certain edge/IoT apps may need adaptations. Also Twelve-Factor predates some patterns (service
  meshes, sidecars, complex mesh networking), so treat it as a _baseline_ and adapt.
{{< /callout >}}
<!-- deno-fmt-ignore-end -->

## Core idea in Go

Go apps are often compiled binaries distributed as artifacts — this fits the Twelve-Factor **build → release → run**
model well. The most common gap to fill is _how to map environment variables to typed Go config_ cleanly and how to keep
startup/shutdown safe.

### Common libraries

Many community examples document building 12-factor Go apps with `envconfig` or `viper`; there are tutorials & blog
posts showing patterns for config injection and using `godotenv` for local dev. ([blog.gopheracademy.com][7])

- **`os` / `os.Getenv`** — standard low-level reads; fine for tiny apps.
- **`kelseyhightower/envconfig`** — struct-tag driven mapping of env vars into typed Go structs; small and idiomatic.
  ([GitHub][3])
- **`spf13/viper`** — flexible config library: supports env vars, files (JSON/TOML/YAML), remote sources (Consul), and
  integrates with Cobra CLI. Good for apps needing layered sources. ([GitHub][4])
- **`joho/godotenv`** — `.env` file loader for local development (don’t use .env in production; use platform
  secrets/config maps). Useful for onboarding developers. ([GitHub][5])
- **`spf13/cobra`** — CLI scaffolding (helps for admin processes / one-off commands). ([GitHub][6])

### Practical patterns (Go)

- **Single source of truth for config** — Build a typed `Config` struct; populate it from env once at startup and pass
  it to components (avoid global mutable state).
- **Use a single connection URL** — e.g. `DATABASE_URL` rather than multiple DB fields when possible.
- **Graceful shutdown** — use `context.Context`, listen for `SIGTERM`/`SIGINT`, and allow ongoing requests to finish
  (with timeouts).
- **12-factor dev convenience** — use `godotenv` for dev only; CI and production ingest env from CI secrets managers and
  platform config maps.
- **Logs** - write structured logs to stdout (e.g., `log/slog`, zerolog, or logrus) so platform can collect them.

For example, **Viper** can read a `config.yaml`, allow env overrides via `AutomaticEnv()`, and bind flags using
**Cobra**. It’s heavier but powerful when you need multiple sources of layered config or feature toggles.

### Example: Go config using `envconfig`

```go
// config.go
package config

import "github.com/kelseyhightower/envconfig"

type Config struct {
    Port        int    `envconfig:"PORT" default:"8080"`
    DatabaseURL string `envconfig:"DATABASE_URL" required:"true"`
    LogLevel    string `envconfig:"LOG_LEVEL" default:"info"`
}

func Load() (*Config, error) {
    var c Config
    if err := envconfig.Process("", &c); err != nil {
        return nil, err
    }
    return &c, nil
}
```

`main.go` loads `config.Load()` once and passes `*Config` to the server. This approach is compact, explicit, and fits
the Twelve-Factor config principle.

## Core idea in Python

Python teams often use frameworks (Django, Flask, FastAPI). The 12-factor principle “config in env” maps to multiple
popular libs that make reading/parsing env vars, validating types, and supporting `.env` files simple.

### Key Python libraries

- **`python-dotenv`** — load `.env` into environment for local dev (don’t commit `.env`). Straightforward helper.
  ([PyPI][8])
- **`pydantic` / `pydantic-settings` (BaseSettings)** — type-safe settings classes that load from env (and `.env`), with
  validation and defaults — excellent for FastAPI/modern codebases. Pydantic explicitly mentions compatibility with
  12-factor patterns. ([Pydantic][9])
- **`dynaconf`** — layered configuration system inspired by the Twelve-Factor guide; supports multiple formats and
  environment layering, plus secrets/remote backends. Good when you need more flexibility than simple env mapping.
  ([dynaconf.com][10])
- **`environs`**, **`python-decouple`**, **`django-environ`** — lightweight helpers for env parsing and Django
  integration. ([PyPI][11], [django-environ.readthedocs.io][13])

Framework-specific integrations: `django-environ` for Django, `pydantic` for FastAPI, `dynaconf` for projects that need
multi-format support. These are widely used across the community. See library docs for usage and patterns.

### Practical patterns (Python)

- **Settings class** — define a `Settings` (Pydantic BaseSettings) object and instantiate it at startup. This
  centralizes defaults, docs, and validation.
- **Use single-value connection strings** — e.g. `DATABASE_URL` parsed by `sqlalchemy`/`dj-dburl` to avoid many
  scattered env keys.
- **Local dev** — use `python-dotenv` or `pydantic`’s built-in `.env` support to load dev env. CI/prod must pull secrets
  from a vault, not a committed file.
- **Logs** — use structured logging to stdout/stderr; have centralized aggregators (ELK, SaaS).

**Dynaconf** supports `[default]`, `[development]`, `[production]` layers and will read env vars to override values —
good for apps that want a single library to offer both file and env layering.

### Example: Pydantic `BaseSettings`

```python
# settings.py
from pydantic import BaseSettings, AnyUrl

class Settings(BaseSettings):
    database_url: AnyUrl
    port: int = 8000
    log_level: str = "info"

    class Config:
        env_file = ".env"  # convenience for dev only

settings = Settings()
```

`settings.database_url` is validated at startup; in production, the `.env` will be ignored because env vars from the
platform will override. Pydantic explicitly supports this pattern.

## Modern adaptations

1. **Secrets management** — Twelve-Factor says “env vars” but production practices usually place secrets in a secret
   manager (AWS Secrets Manager, HashiCorp Vault, platform secrets) and inject them into env at runtime or mount them as
   files. The principle is the same: _config external to code_.
2. **Kubernetes** — map the Twelve-Factor model onto K8s primitives: ConfigMaps/Secrets for config, Deployments for
   processes, readiness/liveness probes for disposability.
3. **`.env` files** — community consensus: use `.env` for local development convenience, but do **not** treat `.env` as
   production secrets. Libraries like `python-dotenv` and `godotenv` explicitly support this dev use.
4. **Structured logs & telemetry** — Twelve-Factor’s “logs as event streams” aligns with emitting structured JSON to
   stdout and relying on a platform for aggregation/processing.
5. **Validation + schema** — Use typed settings (Go structs, Pydantic) so config problems show up at startup rather than
   in production.

## 📚 Key Cloud-Provider Guides

Here is a curated list of **guide documents / reference guides** for 12-Factor / Cloud-Native Apps from major cloud
providers (Amazon Web Services, Microsoft Azure, Google Cloud) — particularly those that help teams implement
cloud-native / 12-Factor (or similar) applications. I highlight what each guide offers and why it matters.

### Amazon Web Services

**“AWS アーキテクチャで学ぶ The Twelve Factors App 本格入門”** ([AWS builders.flash][21])

- **What it’s about**: A Japanese-language AWS article that goes through each of the 12 factors, explains _why_ they
  matter, and shows _how_ to implement them on AWS (ECS/Fargate, ECR, CodeBuild/CodePipeline, CloudWatch, etc.)
- **Why it’s useful**: Great for implementing 12-Factor on AWS — walks through each factor in AWS context (build →
  deploy → runtime) and maps them to AWS services (ECR, ECS/Fargate, CloudWatch).

**“Developing Twelve-Factor Apps using Amazon ECS and AWS Fargate”** ([AWS Blogs][22])

- **What it’s about**: A tutorial-style AWS blog post describing a sample solution using containers on ECS/Fargate, with
  backing services, CI/CD, and log management — showing how 12-Factor–style architecture maps into AWS container
  workloads.
- **Why it’s useful**: Useful if you’re containerizing applications and want a “reference architecture” that follows
  12-Factor principles on AWS.

### Microsoft Azure

**“Cloud-native architecture & 12-Factor App guidance”** ([Microsoft Learn][23])

- **What it’s about**: The Azure documentation page on cloud-native architecture explicitly references 12-Factor as a
  “solid foundation” for cloud-native apps. It describes how cloud-native designs (stateless processes, elasticity,
  configuration separation, etc.) map onto Azure infrastructure.

- **Why it’s useful**: Helpful to align 12-Factor thinking with Azure’s architecture patterns, especially if using Azure
  Kubernetes Service (AKS), container services, or serverless.

**Azure App Configuration docs / guide** ([Microsoft Learn][24])

- **What it’s about**: The Azure App Configuration service is presented as a tool to implement the 12-Factor “Config”
  principle: externalizing configuration from code, enabling dynamic configuration management especially in
  microservices / container-based deployments.
- **Why it’s useful**: Practical for teams running containerized or distributed apps on Azure, need external config
  management, want to keep config out of code — especially useful for microservices or multi-environment deployments.

### Google Cloud

**Google Cloud Architecture Center / “Application development” section** ([Google Cloud Documentation][25])

- **What it’s about**: A general landing area in Google Cloud docs that gathers resources on application development
  (compute, hosting, containers, data, observability, etc.) — good starting point for designing cloud-native apps on
  Google Cloud.
- **Why it’s useful**: Helps explore cloud-native building blocks (compute, storage, managed services) that align with
  12-Factor ideas (backing services, stateless containers, config externalization, etc.).

**“From the Twelve to Sixteen-Factor App”** ([Google Cloud][26])

- **What it’s about**: A recent (2025) Google Cloud blog post arguing that in the AI era the original 12-Factor model
  should be extended — offering a modern evolution of 12-Factor thinking that includes considerations for AI apps.
- **Why it’s useful**: Useful if your application involves AI / ML workloads — shows how to adapt 12-Factor (or enhance
  it) for modern use-cases beyond traditional CRUD or service-backed apps.

### How They Complement Each Other

- The AWS guides are very concrete — they map each 12-Factor principle to specific AWS services (ECS/Fargate, ECR,
  CloudWatch, CodeBuild, etc.), making it easier to adopt 12-Factor on AWS without reinventing the wheel.
- Azure’s cloud-native architecture guidance + App Configuration service offers a more managed/config-driven approach,
  especially for containerized or microservice-based apps; good if you’re already using Azure ecosystem (AKS, Functions,
  etc.).
- On Google Cloud, the documentation is more general (Application Development center), but there are community and
  official evolutions of 12-Factor thinking. The “Sixteen-Factor” post is especially interesting for AI/ML workloads —
  suggesting 12-Factor isn’t obsolete but needs adaptation for modern app patterns.
- Across all three providers, there’s a recurring pattern: configuration externalization, containerization (stateless
  processes), backing services as managed cloud services — exactly what 12-Factor advocates. These docs help ground
  12-Factor theory into provider-specific best practices.

[1]: https://12factor.net/ "The Twelve-Factor App"
[1ja]: https://12factor.net/ja/ "The Twelve-Factor App"
[2]: https://12factor.net/config "Store config in the environment"
[3]: https://github.com/kelseyhightower/envconfig "kelseyhightower/envconfig: Golang library for managing ... | GitHub"
[4]: https://github.com/spf13/viper "spf13/viper: Go configuration with fangs | GitHub"
[5]: https://github.com/joho/godotenv "joho/godotenv: A Go port of Ruby's dotenv library (Loads ... | GitHub"
[6]: https://github.com/spf13/cobra "spf13/cobra: A Commander for modern Go CLI interactions | GitHub"
[7]: https://blog.gopheracademy.com/advent-2013/day-03-building-a-twelve-factor-app-in-go/ "Go Advent Day 3 - Building a Twelve Factor App in Go"
[8]: https://pypi.org/project/python-dotenv/ "python-dotenv | PyPI"
[9]: https://docs.pydantic.dev/latest/api/pydantic_settings/ "Pydantic Settings - Pydantic Validation"
[10]: https://dynaconf.com/ "Dynaconf"
[11]: https://pypi.org/project/environs/ "environs | PyPI"
[13]: https://django-environ.readthedocs.io/ "django-environ"
[15]: https://www.heroku.com/blog/heroku-open-sources-twelve-factor-app-definition/ "Heroku Open Sources the Twelve-Factor App Definition"
[21]: https://aws.amazon.com/jp/builders-flash/202208/introductions-twelve-factors-app/ "AWS アーキテクチャで学ぶ The Twelve Factors App 本格入門 | AWS builders.flash"
[22]: https://aws.amazon.com/blogs/containers/developing-twelve-factor-apps-using-amazon-ecs-and-aws-fargate/ "Developing Twelve-Factor Apps using Amazon ECS and AWS Fargate | AWS Blogs"
[22ja]: https://aws.amazon.com/jp/blogs/news/developing-twelve-factor-apps-using-amazon-ecs-and-aws-fargate/ "Amazon ECS と AWS Fargate を利用した Twelve-Factor Apps の開発 | AWS ブログ"
[23]: https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/definition "What is Cloud Native? - .NET"
[24]: https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview "What is Azure App Configuration?"
[25]: https://docs.cloud.google.com/architecture/scalable-and-resilient-apps?hl=en "Patterns for scalable and resilient apps  |  Cloud Architecture Center  |  Google Cloud Documentation"
[25ja]: https://docs.cloud.google.com/architecture/scalable-and-resilient-apps?hl=ja "スケーラブルで復元性の高いアプリのためのパターン  |  Cloud Architecture Center  |  Google Cloud Documentation"
[26]: https://cloud.google.com/transform/from-the-twelve-to-sixteen-factor-app "Rethinking the Twelve-Factor App framework for AI"
