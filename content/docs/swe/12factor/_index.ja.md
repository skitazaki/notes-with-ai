+++
date = '2025-12-04T22:29:49+09:00'
title = 'Twelve-Factor App'
+++

**Twelve-Factor** は、クラウドネイティブな SaaS
アプリを構築するための簡潔で言語に依存しないマニフェストです。単一のコードベースをバージョン管理システムで管理し、設定とコードを明確に分離し、ステートレスなプロセス、バックエンドサービスをアタッチされたリソースとして扱い、ログをイベントストリームとして扱うなど、様々な原則をまとめています。

本稿では、Twelve-Factor の項目に触れ、 **Go** と **Python** でこれらを実装する方法を説明します。
具体的なライブラリと実装パターンおよびコード例、クラウドプロバイダーの公開資料へのポインタを含みます。

## Twelve-Factorの短いガイド

公式 Twelve-Factor サイト: [12factor.net][1ja]

1. **Codebase（コードベース）** —
   アプリごとのリポジトリで複数のデプロイを実現。バージョン管理システム（git）を使用。ベストプラクティス：インフラ/運用スクリプトを同じリポジトリ内、または隣接するインフラリポジトリに保持し、クリアなビルド/リリースドキュメントを作成します。

2. **Dependencies（依存関係）** — 明示的に宣言し隔離（ロックファイル、ベンダリング）。言語ネイティブなパッケージ管理と
   CI を使用してビルドを再現します。

3. **Config（設定）** — 設定を環境変数に格納（秘密/設定をコードに埋め込まない）。ベストプラクティス：`DATABASE_URL`、API
   キー、フィーチャーフラグを環境変数またはシークレットとして扱い、`.env` はリポジトリにコミットしません。

4. **Backing services（バックエンドサービス）** —
   DB、キャッシュ、メッセージブローカーをアタッチされたリソースとして扱う（設定がそれらを指す）。接続 URL
   を使用し、コード変更なしにサービスをスワップできるようにします。

5. **Build, release, run（ビルド、リリース、実行）** — ビルド（アーティファクト）、リリース（アーティファクト +
   設定の結合）、実行（プロセスの実行）のステージを分離し、CI/CD で自動化します。

6. **Processes（プロセス）** — 1 つ以上のステートレスプロセスとして実行し、状態はバックエンドサービスに永続化します。

7. **Port binding（ポートバインディング）** — ポートバインディングを通じてサービスをエクスポート（HTTP サーバーは
   `$PORT` にバインド）。アプリを自己完結型にします。

8. **Concurrency（並行性）** —
   複数のプロセスタイプを実行してスケール。プロセスは水平スケーリングのためのファーストクラスです。

9. **Disposability（廃棄容易性）** — 高速起動とグレースフルシャットダウン（SIGTERM ハンドリング、K8s
   での準備完了/存続確認プローブ）。

10. **Dev/prod parity（開発/本番一致）** — 開発、ステージング、本番環境を類似させる：データ、時間、メンバー、依存関係。

11. **Logs（ログ）** — ログをイベントストリームとして扱う。キャプチャ/集約を実行環境に委任（例：構造化ログ →
    stdout/stderr → アグリゲータ）。

12. **Admin processes（管理プロセス）** —
    一度きりの管理/メンテナンスタスク（マイグレーション、REPL）をアプリと同じ環境で実行。

Twelve-Factor は概念レベルで意図的にシンプルかつ規範的です。
多くのチームはベースラインとして採用し、サービスメッシュ、シークレットマネージャー、テレメトリー/オブザーバビリティ、プラットフォーム固有パターン（Kubernetes、サーバーレスなど）を伴い拡張します。

Twelve-Factor は Heroku の経験から生まれ、今も正規の指針です。 2024/2025年に Heroku
からオープンソース化され、コミュニティによって進化できるようになりました。正規サイトでリストと根拠を確認してください。([Heroku ブログ][15] -
2024年11月12日)

<!-- deno-fmt-ignore-start -->

{{< callout type="warning" >}}
**Twelve-Factor がぴったり合わない場合は？** — 状態の多いアプリ（豊富なクライアント状態、低遅延のオンデバイスロジック）、一部のレガシーモノリス、特定のエッジ/IoT アプリは個別の調整が必要な場合があります。また Twelve-Factor は一部のパターン（サービスメッシュ、サイドカー、複雑なメッシュネットワーク）に先行しているため、状況に応じて調整してください。
{{< /callout >}}

<!-- deno-fmt-ignore-end -->

## Go での考え方

Go アプリはコンパイル済みバイナリをアーティファクトとして配布して動かします。これは Twelve-Factor の **ビルド → リリース
→ 実行** モデルにうまく適合します。検討すべきギャップは、_環境変数を型付き Go 設定にきちんとマップする方法_
および起動/シャットダウンを安全に保つ方法です。

### 一般的なライブラリ

Go コミュニティの多くの例では、Twelve-Factor に沿って `envconfig` または `viper`
でアプリを構築する手順を説明しています。設定の注入パターンとローカル開発用の `godotenv`
を使用する方法を示すチュートリアルとブログ投稿もあります。([blog.gopheracademy.com][7])

- **`os` / `os.Getenv`** — 標準的な低レベルの読み取り。小さなアプリには適しています。
- **`kelseyhightower/envconfig`** — 環境変数を型付き Go
  構造体にマップするための構造体タグ駆動型マッピング。小さくて慣用的です。([GitHub][3])
- **`spf13/viper`** —
  柔軟な設定ライブラリ：環境変数、ファイル（JSON/TOML/YAML）、リモートソース（Consul）をサポートし、Cobra CLI
  と統合。複数のソースが必要なアプリに最適。([GitHub][4])
- **`joho/godotenv`** — ローカル開発用の `.env` ファイルローダー（本番環境では .env
  を使用しないでください。プラットフォームのシークレット/設定マップを使用）。開発者のオンボーディングに便利。([GitHub][5])
- **`spf13/cobra`** — CLI を手早く実装できるため管理プロセスや使い捨てコマンドに役立ちます。([GitHub][6])

### 実装パターン（Go）

- **設定の単一ソース** — 型付き `Config`
  構造体を構築します。起動時に環境から設定し、コンポーネントに渡します（グローバル可変状態を回避）。
- **単一の接続 URL を使用** — 可能な場合、複数の DB フィールドではなく、例えば `DATABASE_URL` を使用。
- **グレースフルシャットダウン** — `context.Context` を使用し、`SIGTERM`/`SIGINT`
  シグナルを受け取ったらリクエストを完了させる（タイムアウト付き）。
- **Twelve-Factor開発の便利さ** — ローカル開発でのみ `godotenv` を使用します。CI と本番は CI
  シークレットマネージャーとプラットフォーム設定マップから環境を取得します。
- **ログ** - 標準出力 (stdout) に構造化ログを書き出します（例：`log/slog`、zerolog、logrus
  など）。プラットフォームが収集できるようにします。

例えば、**Viper** は `config.yaml` を読み込み、`AutomaticEnv()` で環境変数の上書きを許可し、**Cobra**
を使用してフラグを結合できます。設定情報を多層的に管理したりフィーチャートグルが必要な場合は、重厚的にはなりますが強力です。

### 例：`envconfig` を使用した Go 設定

```go {filename="config.go"}
package config

import "github.com/kelseyhightower/envconfig"

type Config struct {
    Port        string `envconfig:"PORT" default:"8080"`
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

`main.go` は `config.Load()` を一度読み込み、`*Config`
をサーバーに渡します。このアプローチはコンパクトかつ明示的で、Twelve-Factor の設定原則に適合します。

## Python での考え方

Python チームはフレームワーク（Django、Flask、FastAPI）を使用するケースが多々あります。Twelve-Factor
の原則「設定を環境変数に格納する」は人気のあるライブラリとも相性が良く、環境変数の読み取りと解析、型の検証、 `.env`
ファイルのサポートをシンプルにしてくれます。

### 主要な Python ライブラリ

- **`python-dotenv`** — ローカル開発では `.env` を環境変数に読み込みます（`.env`
  はコミットしません）。直感的なヘルパーです。([PyPI][8])
- **`pydantic` / `pydantic-settings` (BaseSettings)** — 型安全な設定クラスは環境変数および `.env`
  ファイルから検証とデフォルト付きで情報を読み込みます。FastAPI などモダンなコードベースに最適です。Pydantic は
  チームはフレームワーク（Django、Flask、FastAPI）を使用するケースが多々あります。Twelve-Factor
  パターンとの互換性を明示的に言及しています。([Pydantic][9])
- **`dynaconf`** — Twelve-Factor
  ガイドに触発されたレイヤー化された設定システム。複数の形式と環境のレイヤリング、シークレット/リモートバックエンドをサポート。シンプルな環境マッピング以上の柔軟性が必要な場合に最適。([dynaconf.com][10])
- **`environs`**, **`python-decouple`**, **`django-environ`** — 環境変数の解析と Django
  統合のための軽量ヘルパーです。([PyPI][11], [django-environ.readthedocs.io][13])

フレームワーク固有の統合：Django 用の `django-environ`、FastAPI 用の
`pydantic`、マルチフォーマットサポートが必要なプロジェクト用の
`dynaconf`。これらはコミュニティ全体で広く使用されています。使用例とパターンについてはライブラリドキュメントを参照してください。

### 実装パターン（Python）

- **設定クラス** — `Settings`（Pydantic
  BaseSettings）オブジェクトを定義し、起動時にインスタンス化。これにより、デフォルト値、ドキュメント、検証を一元化します。
- **単一値の接続文字列を使用** — 例：`DATABASE_URL` は `sqlalchemy`/`dj-dburl`
  で解析され、複数の環境変数のキーが散在することを避けます。
- **ローカル開発** — `python-dotenv` または `pydantic` の組み込み `.env`
  サポートを使用してローカル開発環境で環境変数を読み込みます。CIや本番環境は機密情報管理システムからシークレットを取得します。コミットされたファイルではありません。
- **ログ** — stdout/stderr への構造化ログを使用します。一元的なアグリゲータ（ELK、SaaS）を設定します。

**Dynaconf** は `[default]`、`[development]`、`[production]`
レイヤーをサポートし、値をオーバーライドするために環境変数を読み込みます。ファイルと環境の両方のレイヤリングを提供する単一のライブラリが必要なアプリに最適です。

### 例：Pydantic `BaseSettings`

```python {filename="settings.py"}
from pydantic import BaseSettings, AnyUrl

class Settings(BaseSettings):
    database_url: AnyUrl
    port: int = 8000
    log_level: str = "info"

    class Config:
        env_file = ".env"  # ローカル開発の便利さのみ

settings = Settings()
```

`settings.database_url` は起動時に検証されます。本番では、`.env`
は無視されます。プラットフォームからの環境変数がオーバーライドするためです。Pydantic
はこのパターンを明示的にサポートしています。

## モダンな適応

1. **シークレット管理** — Twelve-Factor
   は「環境変数」と言いますが、本番環境でのベストプラクティスは機密情報をシークレットマネージャー（AWS Secrets
   Manager、HashiCorp
   Vault、プラットフォームシークレット）に配置し、実行時に環境に注入するか、ファイルとしてマウントします。原則は同じです：_コード外の設定_。
2. **Kubernetes** — Twelve-Factor モデルを K8s プリミティブにマップします：設定用の ConfigMaps/Secrets、プロセス用の
   Deployments、処理可能性用の準備完了/存続確認プローブ。
3. **`.env` ファイル** — コミュニティの合意：ローカル開発の便利さに `.env` を使用しますが、本番シークレットとしては
   `.env` を **扱わない** でください。`python-dotenv` と `godotenv`
   などのライブラリはこの開発ユースケースを明示的にサポートしています。
4. **構造化ログとテレメトリー** — Twelve-Factor の「ログをイベントストリームとして」は構造化 JSON を stdout
   に発行し、プラットフォームに集約/処理を依存することと一致します。
5. **検証 + スキーマ** — 型付き設定（Go
   構造体、Pydantic）を使用します。設定の問題は本番実行時ではなく起動時に表示されます。

## 📚 主要クラウドプロバイダーが公開するガイド

主要クラウドプロバイダー（アマゾン ウェブ サービス、Microsoft Azure、Google Cloud）は **ガイドドキュメント /
リファレンスガイド** を公開しています。特に Twelve-Factor /
クラウドネイティブアプリの実装を支援するもの（または類似）を強調しています。各ガイドの提供内容と重要な理由を説明します。

### アマゾン ウェブ サービス (AWS)

**"AWS アーキテクチャで学ぶ The Twelve Factors App 本格入門"** ([AWS builders.flash][21])

- **何について：** Twelve-Factor の各項目を説明し、_なぜ重要か_、_AWSで実装する方法_ を示す日本語の記事です。
- **なぜ有用：** AWS コンテキストで説明し（ビルド → デプロイ → ランタイム）、AWS サービス（ECS/Fargate, ECR,
  CodeBuild/CodePipeline, CloudWatch）にマップします。AWS での Twelve-Factorの実装に最適です。

**"Amazon ECS と AWS Fargate を利用した Twelve-Factor Apps の開発"** ([AWS ブログ][22ja])

- **何について：** ECS/Fargate
  上のコンテナ、バックエンドサービス、CI/CD、ログ管理を使用したサンプルソリューションを説明するチュートリアルスタイルの
  AWS ブログ投稿です。Twelve-Factorスタイルのアーキテクチャが AWS コンテナワークロードにどのように対応するかを示します。
- **なぜ有用：** アプリケーションをコンテナ化し、AWS 上で Twelve-Factor
  の原則に従う「リファレンスアーキテクチャ」が必要な場合に有用です。

### Microsoft Azure

**"Cloud-native architecture & 12-Factor App guidance"** ([Microsoft Learn][23])

- **何について：** Azure ドキュメントページでは、クラウドネイティブアーキテクチャは Twelve-Factor
  をクラウドネイティブアプリの「確実な基盤」として明示的に参照しています。
  クラウドネイティブデザイン（ステートレスプロセス、弾性性、設定分離など）が Azure
  インフラにどのように対応するかを説明しています。
- **なぜ有用：** 特に Azure Kubernetes
  Service（AKS）、コンテナサービス、またはサーバーレスを使用する場合に、Twelve-Factor の考え方を Azure
  アーキテクチャパターンと一致させるのに役立ちます。

**Azure App Configuration ドキュメント / ガイド** ([Microsoft Learn][24])

- **何について：** Azure App Configuration サービスは Twelve-Factor の「Config」原則を実装するツールとして提示されます。
  設定をコードから外部化し、マイクロサービス/コンテナベースのデプロイメントで特に動的設定管理を有効にします。
- **なぜ有用：** Azure 上でコンテナ化または分散アプリを実行するチーム、外部設定管理が必要、設定をコード外に保つ必要 —
  マイクロサービスまたはマルチ環境デプロイメント特に有用です。

### Google Cloud

**スケーラブルで復元性の高いアプリのためのパターン / "Application development" セクション**
([Google Cloud Documentation][25ja])

- **何について：** Google Cloud
  ドキュメント内の一般的なランディングエリア。アプリケーション開発（コンピュート、ホスティング、コンテナ、データ、オブザーバビリティなど）についてのリソースを集約します
  — Google Cloud 上でクラウドネイティブアプリを設計するための良い出発点です。
- **なぜ有用：**
  クラウドネイティブの構成要素（コンピュート、ストレージ、マネージドサービス）を探索するのに役立ちます。これらは
  Twelve-Factorのアイデア（バックエンドサービス、ステートレスコンテナ、設定外部化など）と一致します。

**"From the Twelve to Sixteen-Factor App"** ([Google Cloud][26])

- **何について：** AI 時代では元の Twelve-Factor モデルを拡張すべきだと主張する最近（2025）の Google Cloud
  ブログ投稿です。 AI アプリを含む最新のユースケースのための Twelve-Factor の思考の現代的な進化を提供します。
- **なぜ有用：** アプリケーションが AI/ML ワークロードに関わる場合に有用です。従来の CRUD
  またはサービスバックアップアプリを超えた最新のユースケースのための Twelve-Factor を適応/強化する方法を示します。

### 互いに補完する関係

- AWS ガイドは非常に具体的です。Twelve-Factor の各原則を特定の AWS サービス（ECS/Fargate、ECR、CloudWatch、CodeBuild
  など）にマップします。AWS 上で Twelve-Factorを採用する際に車輪を再発明せずに実装しやすくします。
- Azure のクラウドネイティブアーキテクチャガイダンス + App Configuration
  サービスは、より管理された/設定駆動型のアプローチを提供します。特にコンテナ化またはマイクロサービスベースのアプリに最適です。Azure
  エコシステム（AKS、Functions など）を既に使用している場合に最適です。
- Google Cloud のドキュメントはより一般的ですが（アプリケーション開発センター）、コミュニティと公式の Twelve-Factor
  の思考の進化があります。「Sixteen-Factor」投稿は AI/ML ワークロードに特に興味深く、 Twelve-Factor
  は廃止されていないが、最新のアプリパターンのために適応が必要であることを示唆しています。
- 3
  つのプロバイダー全体で繰り返されるパターンがあります：設定外部化、コンテナ化（ステートレスプロセス）、マネージドクラウドサービスとしてのバックエンドサービスは
  Twelve-Factor が提唱するものものです。これらのドキュメントは Twelve-Factor
  の原則をプロバイダー固有のベストプラクティスに根付かせるのに役立ちます。

## アプリケーションの例

ここでは、Twelve-Factor のパターンに従ったサンプルアプリを示します。以下の内容が含まれます。

- Go 製 Web アプリ（$PORT にバインドし、環境変数を読み取り、PostgreSQL や Redis といったバックエンドサービスに接続）
- PostgreSQL（メインDB）
- Redis（キャッシュ）
- pgAdmin（データベース管理 UI）
- Prometheus + Grafana（オブザーバビリティ）
- Alloy + Loki（ログ集約 ― 任意だが一般的）
- クリーンな分離のためのネットワークとボリューム

これらは Docker Compose を使って構築できます。 Compose の `secrets` セクションで参照される **POSTGRES_PASSWORD** と
**PGADMIN_DEFAULT_PASSWORD** を含む `.env` ファイルが必要です。

<!-- deno-fmt-ignore-start -->

{{< filetree/container >}}
{{< filetree/folder name="project-root/" >}}
{{< filetree/file name="docker-compose.yml" >}}
{{< filetree/file name=".env" >}}
{{< filetree/folder name="webapp/" >}}
{{< filetree/file name="Dockerfile" >}}
{{< filetree/file name="main.go" >}}
{{< filetree/file name="go.mod" >}}
{{< filetree/file name="go.sum" >}}
{{< /filetree/folder >}}
{{< filetree/folder name="observability/" state="closed" >}}
{{< filetree/file name="grafana-datasources.yaml" >}}
{{< filetree/file name="prometheus.yml" >}}
{{< filetree/file name="loki-local-config.yaml" >}}
{{< filetree/file name="alloy-local-config.alloy" >}}
{{< /filetree/folder >}}
{{< /filetree/folder >}}
{{< /filetree/container >}}

<!-- deno-fmt-ignore-end -->

`docker-compose.yml` を例示します。 最上段の要素で [`configs`][30] と [`secrets`][31]
を使い、開発環境から導入しやすくします。

<!-- deno-fmt-ignore-start -->

{{< codefile fname="docker-compose.yml" language="yaml" >}}

<!-- deno-fmt-ignore-end -->

サンプルの Go アプリでは、オブザーバビリティのための "/healthz"、"/readyz"、"/metrics"
といった基本的なハンドラーを定義しています。

<!-- deno-fmt-ignore-start -->

{{< codefile fname="webapp/main.go" language="go" >}}

<!-- deno-fmt-ignore-end -->

- `GET /healthz` はプロセスが生存している限り常に 200 を返します。
- `GET /readyz` は DB 接続（DB.PingContext）と Redis
  接続（Redis.Ping）を確認します。依存サービスが準備できていない場合は 503 を返します。
- Prometheus が "/metrics" エンドポイントをスクレイプします。

Liveness と Readiness については [Kubernetes のドキュメント][32] を参照してください。 Prometheus
では、ターゲットからメトリクスを取得する HTTP パスを示す **metrics_path** のデフォルト値は "/metrics" です。
([Prometheus][33])

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
[25]: https://docs.cloud.google.com/architecture/scalable-and-resilient-apps?hl=en "Patterns for scalable and resilient apps  |  Cloud Architecture Center  |  Google Cloud Documentation"
[25ja]: https://docs.cloud.google.com/architecture/scalable-and-resilient-apps?hl=ja "スケーラブルで復元性の高いアプリのためのパターン  |  Cloud Architecture Center  |  Google Cloud Documentation"
[26]: https://cloud.google.com/transform/from-the-twelve-to-sixteen-factor-app "Rethinking the Twelve-Factor App framework for AI"
[30]: https://docs.docker.com/reference/compose-file/configs/ "Configs | Docker Docs"
[31]: https://docs.docker.com/reference/compose-file/secrets/ "Secrets | Docker Docs"
[32]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ "Configure Liveness, Readiness and Startup Probes | Kubernetes"
[33]: https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "Configuration | Prometheus"
