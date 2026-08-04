---
type: prompt
path: /docs/data/privacy
---

# 日本語の翻訳版の作成

あなたはデジタルテクノロジーの専門家であり、ドキュメント作成のプロフェッショナルです。
一般公開可能な品質で正確性を損なわずに分かりやすく、日本語として自然な文書を作成してください。

翻訳対象のファイルは以下のパスにあります。

`content/docs/data/privacy/_index.md`

日本語版のファイルは `_index.ja.md` として同じフォルダに保存してください。
元の文書構造とメタデータ（日付、タイトル、重み付け、`prev` など）を保持してください。

翻訳にあたっては以下の方針に従ってください。

- 文末はですます調で統一してください。
- 各セクションの見出しは日本語を基本としつつ、必要な略語（AI / PII / SQL など）は残して構いません。
- タイトルは自然な日本語を優先し、`Data Privacy` は原則として **データプライバシー** と訳してください。
- 本文中で英語の専門用語を残す場合は、初出で日本語のあとにカッコ書きで補足してください。
- 英語の語と日本語を隣接させる場合は、不自然な詰まりを避けるため半角スペースを入れてください。たとえば `AI ガバナンス`、`PII の定義` のようにしてください。
- 既存のコードブロック、Mermaid 図、リンク先パスの構造は基本的に維持してください。
- 画像の Markdown は維持しつつ、代替テキストは日本語に翻訳してください。
- 画像ファイルについては、日本語版として用意されている画像が同じフォルダにある場合、`.ja.webp` などの日本語向けファイル名へリンク先を調整して構いません。
- テーブル構造、箇条書き、カード shortcode、番号付き手順、JSON、SQL、YAML のコード例は保持してください。
- ベンダー寄りの言い換えや意訳は避け、概念の境界が曖昧にならないようにしてください。

文量は原文と同程度を目安としてください。
英語の直訳調にはせず、公開ドキュメントとして自然で読みやすい日本語にしてください。

このページはデータプライバシーのハブページです。単なる定義紹介にせず、以下の点を明確に保ってください。

- プライバシーは法令遵守だけではなく、責任あるデータ利用のための設計とガバナンスの実践であること
- セキュリティ、データガバナンス、データ品質、コンプライアンス、AI ガバナンスとの違いと関係が明確に区別されていること
- プライバシー原則が抽象論で終わらず、データ収集、利用、共有、保持、削除の判断にどうつながるかが分かること
- ハブページとして、後続の詳細ページへ自然につながるように可読性と案内性を維持すること

用語の翻訳は以下の規則を優先してください。

- Data Privacy -> データプライバシー
- privacy -> プライバシー
- responsible data use -> 責任あるデータ利用
- cross-cutting concern -> 横断的関心事
- data ecosystem -> データエコシステム
- dataset -> データセット
- data lifecycle -> データライフサイクル
- data governance -> データガバナンス
- data quality -> データ品質
- compliance -> コンプライアンス
- information security -> 情報セキュリティ
- confidentiality -> 機密性
- AI governance -> AI ガバナンス
- decision lens -> 意思決定の視点
- Purpose Limitation -> 目的の明確化
- Data Minimization -> データ最小化
- Transparency -> 透明性
- Accountability -> 説明責任
- Individual Participation -> 本人の関与
- Retention Limitation -> 保持期間の制限
- Privacy by Design and by Default -> プライバシー・バイ・デザイン／デフォルト
- lawful processing -> 適法な処理
- consent -> 同意
- data classification -> データ分類
- access management -> アクセス管理
- least privilege -> 最小権限
- segregation of duties -> 職務の分離
- de-identification -> 非識別化
- pseudonymization -> 仮名化
- anonymization -> 匿名化
- aggregation -> 集計
- generalization -> 一般化
- re-identification -> 再識別
- lifecycle management -> ライフサイクル管理
- archived -> アーカイブ済み
- data owner -> データオーナー
- steward -> スチュワード
- derived outputs -> 派生アウトプット
- trustworthy data systems -> 信頼できるデータシステム

画像と図版については、以下の方針を守ってください。

- `data-privacy.webp` と `data-privacy-core-principles.webp` の画像参照は維持してください。
- 代替テキストは日本語として自然に翻訳してください。
- 同じフォルダに日本語版画像が存在する場合に限り、`.ja.webp` などへ差し替えて構いません。

カードセクションについては、以下の方針を守ってください。

- Hugo の `cards` shortcode とリンク先パスは維持してください。
- 各カードの `title` と `subtitle` は日本語に翻訳してください。
- `TBD` は必要に応じて `（予定）` など自然な日本語に置き換えて構いません。

特に次の点では訳し分けに注意してください。

- `privacy` と `confidentiality` を混同しないでください。
- `appropriate use` は文脈に応じて「適切な利用」または「適切な使用」とし、単なる「許可された利用」に狭めないでください。
- `controls` は文脈に応じて「管理策」「統制」「コントロール」を使い分け、機械的に一語へ固定しないでください。
- `evidence` は文脈に応じて「証跡」または「根拠」とし、監査可能性が伝わるようにしてください。

訳文では、概念説明としての正確さを優先してください。
特に、プライバシーとセキュリティの違い、原則と運用管理策のつながり、ハブページとしての導線が曖昧にならないよう注意してください。
