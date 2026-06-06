---
type: docs
path: /docs/data/management/data-quality-dimensions/
---

# データ鮮度の明確化

対象ファイル:

`content/docs/data/management/data-quality-dimensions/_index.ja.md`

日本語版記事において「データ鮮度」は紛らわしい用語です。
「実行時拡張」セクションの最後に、本文とは異なるデザインの注記を追加してください。
Hugo の `callout` ショートコードを使い、補足説明であることが視覚的に分かる形で表現してください。

追記内容のイメージ

> 適時性（Timeliness）は、データが利用目的に対して十分なタイミングで利用可能であることを表す品質観点である。
> 一方、更新鮮度（Freshness）は、データが最後に更新されてからの経過時間を表す運用メトリクスであり、適時性を評価するための代表的な測定手段の一つである。

可能であれば、注記内では単独の「鮮度」ではなく「更新鮮度（Freshness）」という表現を優先してください。

本文のその他の場所で「鮮度」の意味が紛らわしい場合は記載を明確にしてください。
特に、品質観点としての Timeliness と、運用メトリクスとしての Freshness が混線しないように用語を整理してください。

# 日本語でのデータ鮮度の整理

日本語の「鮮度」は下記の概念を含むため誤解が起きやすい用語です。

- データが新しい
- 更新が速い
- 遅延が少ない
- リアルタイムである

Data Quality の文脈では **Timeliness（適時性）** と **Freshness（鮮度）** が混同されがちですが、本来は別の概念です。
データ品質のコア観点としては Timeliness を採用し、Freshness はメトリクスやシグナルとして扱います。
単独の「鮮度」という日本語が広すぎる場合は、運用メトリクスとしての意味を示すために **更新鮮度** という語を使ってください。

類似する用語には以下のものがあります。

| 英語        | 日本語   |
| ----------- | -------- |
| Timeliness  | 適時性   |
| Freshness   | 更新鮮度 |
| Latency     | 遅延     |
| Currentness | 最新性   |
| Realtime    | 即時性   |

# Timeliness と Freshness

## Timelinessとは何か

DAMAやISOでいう Timeliness は
「データが利用目的に対して十分なタイミングで利用可能であること」です。

「新しいこと」ではなく「間に合うこと」が重要です。

**例1** - 売上レポート

- 毎日朝6時更新
- 利用者は9時に見る

→ 品質良好

**例2** - IoT監視

- 5秒以内に更新必要
- 30秒遅延

→ 品質不良

つまり Timeliness は「利用目的との関係」です。

## Freshnessとは何か

Observability製品で使われる Freshness は
「最後に更新されてからどれくらい時間が経過したか」を意味します。

日本語では、ここでいう Freshness を単に「鮮度」と書くと
Timeliness や低遅延性の意味まで含んで読まれやすいため、必要に応じて「更新鮮度」と明記してください。

例えば以下の計算式です。

```
now() - max(event_time)
```

**例**

- 現在時刻 = 12:00
- 最新レコード = 11:58

→ Freshness = 2分

これは「品質観点」ではなく「観測値」です。
つまり Metric あるいは Signal です。

Freshness は Timeliness を測るための代表的なメトリクスです。

## なぜ混乱するのか

dbtやSodaなどは Freshness を品質観点として扱います。

観点として以下の項目が出現します。

- Freshness
- Volume
- Schema
- Distribution

しかしこれは品質理論ではなく運用理論です。

# レイヤーモデルで整理すると

**Core Dimension**

- 適時性（Timeliness）

**Runtime Metrics**

- 更新鮮度（Freshness）
- 遅延（Latency）

**Runtime Signals**

- 鮮度低下 (Freshness Degradation)

**SLA**

- 95%のデータは15分以内に配信される

# 反映時の指示

- 「実行時拡張」セクション末尾の注記は、通常本文に埋め込まず `callout` で独立表示にすること
- 記事中で Freshness を指す箇所は、文脈が曖昧なら「更新鮮度（Freshness）」に言い換えること
- Timeliness を説明する箇所では、「新しいこと」より「利用目的に対して間に合うこと」が中心概念だと分かるように保つこと
- Latency、Realtime、Currentness と混同しそうな日本語表現があれば補足して解消すること
