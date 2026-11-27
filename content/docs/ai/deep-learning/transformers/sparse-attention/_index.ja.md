---
date: "2026-11-27T20:43:00+09:00"
title: "Sparse Attention"
weight: 1
prev: "/docs/ai/deep-learning/transformers"
next: "/docs/ai/deep-learning/transformers"
---

Sparse Attention（疎なアテンション）は、Attention で計算するトークン間の組み合わせを減らす手法群です。すべての Query がすべての Key を参照する代わりに、パターンや選択機構によって参照先を限定します。目的は、必要な情報経路を保ちながら長い文脈の処理を効率化することです。

Sparse Attention は単一のアルゴリズムではありません。どの接続を残すか、どのように選ぶか、選択したパターンをハードウェア上でどう実行するかによって、さまざまな設計があります。

## Attention の計算コスト

系列長を N、Head の次元を d とすると、標準的な Dense Attention のスコア計算と Value の集約は、おおむね O(N²d) の計算量になります。Attention 行列には N² 個の要素があり、系列長に対して二次的に増加します。

長い入力を一度に処理する Prefill では、このコストが特に大きくなります。逐次生成時には KV Cache によって過去の Key と Value の射影を再計算せずに済みますが、長い Cache を読み出して Attention を行うコストは残ります。Sparse Attention は、Attention が参照する接続そのものを制限します。

## Dense Attention と Sparse Attention

- **Dense Attention**：許可された Query-Key の組み合わせをすべて計算します。
- **Sparse Attention**：許可された組み合わせの一部だけを計算します。
- **効率化された Dense Attention**：同じ Dense Attention の結果を、メモリ移動や Kernel の構成を改善して計算します。

FlashAttention は最後の例です。厳密な Dense Attention を効率よく実行するものであり、それ自体が Attention 行列を疎にするわけではありません。

## 代表的な Sparse Pattern

### Local / Sliding-Window Attention

各 Query は近傍のトークン、たとえば直前の一定範囲だけを参照します。Window 幅を w とすると、計算量はおおむね O(Nwd) になります。近い文脈が重要なタスクに適していますが、遠くの情報へ直接アクセスする経路は限定されます。

### Global Token

一部のトークンを Global として扱い、多くの位置と情報を交換できるようにします。少数の Global 経路によって遠距離の情報をつなげられますが、Global Token の数や実装によってコストが変わります。

### Block-Sparse Attention

Query と Key をブロック単位で扱い、選択したブロック間だけを計算します。GPU のメモリアクセスや行列演算に合わせやすい一方、ブロック内に不要な接続が含まれる場合があります。

### Dynamic / Content-Based Selection

入力内容や学習されたスコアに基づいて、Query ごとに参照する Key、Block、または Summary を選びます。遠くにある関連情報を保持しやすい一方、選択機構自体にもコストがあります。Indexer が全 Query と全 Key を比較する場合、最終 Attention が疎でも選択処理は二次計算量のままになり得ます。

## 代表的な手法

### Longformer

Local Sliding-Window Attention と、タスクに応じた Global Attention を組み合わせます。長文書を Dense Attention で処理する代わりに、構造化された Sparse Pattern を使う代表例です。

### BigBird

Local、Global、Random の接続を組み合わせます。局所構造を保ちながら、遠い位置同士で情報を伝えられるようにする設計です。

### Mistral と Sliding-Window Model

Mistral 7B は Sliding-Window Attention を使うよく知られた Decoder-only モデルです。各層が直接参照する範囲は制限されますが、層を重ねることで実効的な受容範囲は広がります。詳細はモデル構成や推論実装によって異なります。

### Native Sparse Attention（NSA）

圧縮した文脈、選択した細粒度のトークン、Local Attention を階層的に組み合わせます。学習可能な設計と、ハードウェアに合わせた実行効率を重視します。

### DeepSeek Sparse Attention（DSA）

学習された Lightning Indexer によって、Attention に使う KV Entry の一部を選択します。DeepSeek-V3.2 では Multi-head Latent Attention（MLA）と併用されています。Indexer の選択コストやメモリアクセスも、実際の性能を左右します。

## Latent Sparse Attention

**Latent Sparse Attention** は、[Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention](https://arxiv.org/abs/2610.42147)（2026年10月）の論文で使われている名称です。Key を学習された Latent Space 内で階層的にクラスタリングし、Query がクラスタ階層を評価して Attention の候補 Key を絞り込みます。

論文では、Distilled-LSA（事前学習モデルを蒸留で適応）と Native-LSA（次トークン予測目的で学習）の2つの方式を説明しています。著者らは最大1,000万トークンを含む実験結果を報告していますが、これは論文内の結果であり、任意のモデルやハードウェアで保証されるものではありません。新しいプレプリント研究として扱う必要があります。

略称 **LSA は曖昧** です。[LongCat Sparse Attention](https://arxiv.org/abs/2608.01662) も異なる方式に LSA を使っています。混同を避けるため、論文名を明記してください。

また、**Multi-head Latent Attention（MLA）** と混同しないでください。MLA は Key と Value の表現を潜在ベクトルに圧縮し、KV Cache の保存量を減らす方式です。MLA は主に KV Cache の圧縮を目的とし、それ自体が参照するトークン位置を疎にすることを意味しません。

## 効率とトレードオフ

Sparse Attention は演算量や読み出す KV データを減らせる場合がありますが、実際の高速化は非ゼロ要素数だけでは決まりません。

- **選択コスト**：Dynamic Indexer が大量のスコア計算を行うと、選択処理がボトルネックになります。
- **メモリアクセス**：不規則な読み出しは GPU の利用効率を下げることがあります。Block や階層型の設計は Locality を改善できる場合があります。
- **Kernel 対応**：Sparse Pattern を効率よく実行する Kernel が必要です。中程度の系列長では、最適化された Dense Kernel の方が速い場合もあります。
- **品質と到達範囲**：接続を減らすことで有用な長距離依存を失う可能性があります。Global Token、Summary、階層検索などで補えますが、追加の設計が必要です。
- **Workload**：Prefill、逐次 Decode、Batch Size、Cache Layout、系列長によって適した手法は変わります。

Indexer、選択、Cache 読み出し、Attention Kernel、対象タスクでの品質を含めて、End-to-End で評価することが重要です。

## 関連する効率化技術

- **Sparse Attention**：計算する Query-Key の接続を変えます。
- **Linear Attention**：特定の仮定のもとで、全組み合わせ計算を避ける Attention の定式化を使います。
- **FlashAttention**：Dense Attention のメモリ移動と Kernel 構成を改善します。
- **GQA / MQA**：Query Head が共有する Key / Value Head の数を変えます。
- **KV Cache 最適化**：過去の Key と Value の保存、量子化、ページング、再利用を改善します。

これらは組み合わせて使えます。たとえば、Grouped-Query Attention、KV Cache、Sparse Attention Selector を同時に採用するモデルも考えられます。実際の構成は名称だけから推測せず、モデルの設計を確認してください。

## Query から Key を選択する流れ

Content-based Sparse Attention では、候補の選択と最終的な Attention 計算を分けることがあります。Indexer は個々の Key、Block、または Latent Cluster を評価します。選択された Index によって、Attention Kernel が読み出す Key-Value Entry が決まります。これは概念的な流れであり、実装によって Scoring、Cache Layout、Kernel Fusion は異なります。

## 参考文献

- [Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) — Local Window と Global Attention
- [Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062) — Local、Global、Random の Sparse Connection
- [FlashAttention](https://arxiv.org/abs/2205.14135) — IO-aware な厳密 Attention
- [Native Sparse Attention](https://arxiv.org/abs/2502.11089) — 学習可能で Hardware-aligned な階層型 Sparse Attention
- [DeepSeek-V3.2 Technical Report](https://arxiv.org/abs/2512.02556) — DeepSeek Sparse Attention
- [DeepSeek-V2](https://arxiv.org/abs/2405.04434) — MLA と KV Cache 圧縮
- [Latent Sparse Attention](https://arxiv.org/abs/2610.42147) — Latent Hierarchy による超長文脈の Key 選択

## まとめ

Sparse Attention は、Attention が計算するトークン間の接続を減らす技術群です。Local、Global、Block、Dynamic Pattern は、遠距離情報へのアクセス、選択コスト、ハードウェア効率の異なるトレードオフを持ちます。最も疎な方式が最良とは限りません。必要な情報を保ち、対象 Workload で End-to-End の効果を確認できる方式を選ぶことが重要です。
