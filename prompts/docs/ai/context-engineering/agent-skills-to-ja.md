---
type: docs
path: /docs/ai/context-engineering/agent-skills
---

# Agent Skills ページの日本語版作成

あなたは AI エージェント技術の専門家であり、一般公開される技術ドキュメントのプロフェッショナルです。

翻訳対象は次の英語ページです。

`content/docs/ai/context-engineering/agent-skills/_index.md`

日本語版を次のパスに保存してください。

`content/docs/ai/context-engineering/agent-skills/_index.ja.md`

要件:

- 元ページの構造、見出し、表、コード例、リンク、主要メタデータを保持する
- 日本語として自然で、ソフトウェアアーキテクトや経験豊富な開発者が読みやすい文章にする
- Agent Skills、Agent Plugins、Model Context Protocol（MCP）など、仕様上の固有名称は英語表記を維持する
- `SKILL.md`、`plugin.json`、`mcp.json`、`scripts/`、`references/`、`assets/` などのファイル名やパスを変更しない
- 「skill」は仕様上の概念を指す場合は「スキル」とし、初出では Agent Skill と明示する
- progressive disclosure は「段階的開示」と訳す
- discovery、activation、execution は、それぞれ「発見」「有効化」「実行」と訳す
- interoperability は「相互運用性」と訳す
- trust、permission、execution safety は文脈に応じて「信頼」「権限」「実行の安全性」と訳し、同一概念では表記を統一する
- 誇張や宣伝的な表現を避け、仕様の標準化範囲とクライアント固有の動作を区別する
- Agent Plugins 1.0.0 が英語版で Working Draft と記載されている場合、その状態と確認日を保持する
- 日本語化済み画像 `progressive-disclosure.ja.webp` と `agent-skills-architecture.ja.webp` を参照する
- 画像の代替テキストも自然な日本語に翻訳する
- 英語版に存在しないリンクや製品サポート情報を追加しない

公開前に `pnpm format`、`pnpm lint`、`pnpm build` を実行し、日本語ルートで表示を確認してください。
