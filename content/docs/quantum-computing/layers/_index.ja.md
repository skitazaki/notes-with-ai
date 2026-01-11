---
date: "2025-10-18T16:00:00+09:00"
title: "レイヤー別のプレイヤー"
description: |-
  量子コンピューティングの主要プレイヤーをレイヤー別に技術的に整理した報告です。クラウドサービス、開発者ツール（言語含む）、量子アルゴリズム、ハードウェアの観点でまとめています。
weight: 10
---

量子コンピューティングの主要プレイヤーを「レイヤー別」に技術的に整理します。クラウドアクセス可能なサービス、開発者ツール（プログラミング言語を含む）、量子アルゴリズム、量子ハードウェアの4つのカテゴリで構成しています。

## はじめに

量子コンピューティング（QC）は、重ね合わせ、エンタングルメント、干渉などの量子力学的現象を利用して、特定の問題（最適化、シミュレーション、暗号関連など）で古典計算より有利になる可能性を持ちます。
しかし、この技術スタックは複雑で、物理ハードウェアからエンドユーザーアプリケーションまで技術的な課題は多岐に渡ります。

本文書では2025年中頃時点の技術的な概観について、主要企業と技術をレイヤー別に分類して説明します。

## レイヤーの全体像

量子コンピューティングのエコシステムをレイヤーに分類し、ここでは大まかに以下のように定義します：

| レイヤー                | 機能 / 抽象化                                                                                                            | 主な責務                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **サービス（Service）** | ハードウェアの複雑さを抽象化し、深いQC知識を必要とせずにクラウド経由で利用できるドメイン／垂直アプリケーションを提供する | 実問題の解決、クラウドインターフェース、オーケストレーション、ビジネス課題を量子タスクにマッピング                                                      |
| **開発者ツール**        | プログラミング言語、SDK、シミュレータ、デバッガ、誤り緩和フレームワーク                                                  | 量子プログラムの表現、コンパイル、最適化、シミュレーション、スケジューリング。アルゴリズムとハードウェア間のファームウェア/ソフトウェアスタックの橋渡し |
| **量子アルゴリズム**    | アルゴリズム、ハイブリッドアルゴリズム、アプリケーションロジック、ドメイン固有ワークフロー                               | アルゴリズム設計（最適化、機械学習、シミュレーション、暗号など）                                                                                        |
| **量子ハードウェア**    | 実際の量子ビット（qubit）とその物理実装、制御、測定、誤り訂正、冷却、相互接続など                                        | QPUアーキテクチャ（超伝導、イオントラップ、光子、ニュートラルアトム等）、物理制御システム、ハードウェアコンポーネント                                   |

「ファームウェア／制御エレクトロニクス／量子制御システム」の中間レイヤーを、開発者ツールとハードウェアの間に分離して扱うこともあります。また、現行のNISQデバイス向けには古典-量子インターフェース／ハイブリッドレイヤーも存在します。

様々な定義や分類が存在するため、インターネットを検索してみましょう。 (例: [Wikipedia][100]、[SITSI®][9])

## プレイヤーとソリューション

主要なプレイヤーとソリューションを、関与するレイヤー別に分類して整理します。
多くの企業は複数のレイヤーにまたがっています（例：IBMはハードウェアを作る一方でQiskitやクラウドサービス、アルゴリズムの提供も行う）。

### 1 - サービス（Service）

サービスはハードウェアの複雑さを抽象化し、量子リソースをビジネスで使える形にします。
クラウドアクセス、オーケストレーション、使用分析、ドメイン特化アプリ（金融、化学、物流、材料科学など）を提供します。

**主要企業 / サービス例:**

| サービス名                  | 提供内容                                                                                                                         |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **IBM Quantum Platform**    | マネージドクラウドサービスで量子システムへアクセス、開発ツールやチュートリアルを提供 ([IBM][3])                                  |
| **Amazon Braket (AWS)**     | 複数ベンダー対応のクラウドサービス。複数のQCハードウェアやシミュレータを横断するオーケストレーションを提供 ([AWS][4])            |
| **Azure Quantum Computing** | クラウドアクセスに加え、QDKやQ#を開発者向けに提供 ([Microsoft Azure][5])                                                         |
| **Google Quantum AI**       | クラウドプラットフォームと研究連携。アルゴリズム・ハードウェア研究が強み ([Google][6])                                           |
| **D-Wave Leap**             | アニーリングアクセスとハイブリッドソルバをクラウドで提供 ([D-Wave][7])                                                           |
| **Terra Quantum**           | ハイブリッド量子クラウドプラットフォーム、量子アルゴリズムをサービスとして提供。量子安全/暗号関連も手掛ける ([Terra Quantum][8]) |

化学シミュレーションや金融向けのように業界特化型のサービスを提供するプレイヤーも存在します。 たとえば [QC Ware][11],
[Quantistry][14], [1QBit][12], [algorithmiq][13] などが挙げられます。

### 2 - 開発者ツール

開発者ツールは量子プログラムの記述、シミュレーション、コンパイル、最適化、ハードウェアインターフェースを提供し、ハードウェアをより扱いやすく抽象化します。

**主要ツール / フレームワーク:**

| ツール                    | 提供内容                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Qiskit (IBM)**          | Python SDK。回路構築、トランスパイラ、シミュレータ、ランタイムツール、豊富なエコシステム([IBM][20], [GitHub][39])                                 |
| **Braket SDK (AWS)**      | マルチベンダーデバイス抽象化、シミュレータ、ハードウェアバックエンド ([GitHub][21])                                                               |
| **QDK と Q# (Microsoft)** | QDKとQ#はAzure Quantumと統合されたSDK／言語で、シミュレータやパートナーハードウェアで実行可能 ([Microsoft Learn][22], [GitHub][41])               |
| **Cirq (Google)**         | ゲートレベル制御に向いたPythonフレームワーク。NISQ実験に適する ([Google Quantum AI][23], [GitHub][40])                                            |
| **PennyLane (Xanadu)**    | TensorFlowやPyTorchと統合されたPythonフレームワーク。量子ー古典ハイブリッドの自動微分に強み ([PennyLane][24], [arXiv][25])                        |
| **Ocean (D-Wave)**        | アニーリング／最適化向けのツール群。アニーリングパラダイムに特化 ([D-Wave][26], [GitHub][27])                                                     |
| **ProjectQ**              | ハードウェア非依存のコンパイラフレームワーク。シミュレータ対応でコンパイル最適化研究に適す ([ProjectQ][28], [GitHub][29], [arXiv][30])            |
| **XACC**                  | 量子—古典ハイブリッド計算のためのインフラ。コンパイラ／ランタイム／実行のサービス指向アーキテクチャを提供 ([XACC][31], [GitHub][32], [arXiv][33]) |
| **Quil (Rigetti)**        | ハイブリッドな古典／量子計算を表現する言語。Quil SDKで量子プログラム記述可能 ([Rigetti][38])                                                      |
| **Classiq**               | 量子アルゴリズムとアプリケーションのコレクション、Jupyterノートブック等でのサンプル ([Classiq][36], [GitHub][37])                                 |

**プログラミング言語／言語パラダイム:**

- 現在多くのツールはPythonを採用（Qiskit, Cirq, PennyLane, Braket）。
- MicrosoftはQ#を開発し、より高レベルの量子アルゴリズム表現を目指している。
- [OpenQASM][34] のようなアセンブリレベル言語や、論理／物理量子ビットを対象とするコンパイラレイヤの研究も進んでいる。

**その他ミドルウェア／ツール群:**

- エラー緩和ライブラリ
- 量子制御ソフトウェア（例：[Q-CTRL][35]）
- シミュレータ／エミュレータ
- ファームウェア／スケジューラー層

### 3 - 量子アルゴリズム

量子アルゴリズム層では、量子並列性を利用して古典コンピュータでは困難な問題を解くアルゴリズム群や、ハイブリッドワークフロー、ドメイン固有のアプリケーションロジックが取り扱われます。

**アルゴリズムの種類:**

| アルゴリズム類型                   | 目的 / ユースケース                                                                                  |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **量子シミュレーション**           | 分子・物質の振る舞いをシミュレートし、古典コンピュータでは困難な現象を解析（量子化学、Many-body 系） |
| **最適化**                         | 組合せ最適化やスケジューリング、ポートフォリオ最適化などを量子古典ハイブリッドで解く                 |
| **量子機械学習（QML）**            | 量子と機械学習の組合せ。データ埋め込みやカーネル法で表現力や計算効率の向上を目指す                   |
| **量子アニーリング**               | アニーリングを使った最適化手法。特定クラスの問題に効率的にアプローチ                                 |
| **量子暗号**                       | 量子力学を利用した安全通信（QKD）や、量子耐性を持つ暗号プロトコル                                    |
| **誤り訂正／フォールトトレランス** | 量子情報を保護するためのコードや手法。論理量子ビットやシンドローム抽出等                             |

以下、主要領域ごとに5行程度で簡潔にまとめます。

**量子シミュレーション**

量子シミュレーションは、古典コンピュータでは困難な分子や物質の動的・静的性質を扱うために用いられます。

- **代表的アルゴリズム:** VQE（Variational Quantum Eigensolver）、QPE（Quantum Phase Estimation）。
- **キーワード:** ハミルトニアン、固有状態、量子化学、Many-body 系。
- **主要プレイヤー:** IBM、Google、Quantinuum、Xanadu、Microsoft（Azure Quantum）。
- 化学設計や超伝導体研究、分子エネルギー計算が主な応用分野。

**最適化（例: QAOA, VQE）**

最適化分野は、量子古典ハイブリッド法で組合せ最適化や制約付き問題に取り組みます。

- **代表的アルゴリズム:** Quantum Approximate Optimization Algorithm (QAOA)、Variational Quantum Eigensolver
  (VQE)、Grover検索の変種。
- **キーワード:** ハイブリッド最適化、変分回路、コスト関数、量子優位性の検証。
- **主要プレイヤー:** D-Wave、IBM、Zapata、QC Ware、Rigetti。
- ロジスティクス、金融、資源配分への応用が進む。

**量子機械学習（QML）**

QMLは量子計算と機械学習を融合し、表現力や計算面での利点を探る分野です。

- **代表的アルゴリズム:** 量子カーネル法、QNN（Quantum Neural Networks）、HHL（線形方程式ソルバー）。
- **キーワード:** 変分回路、データエンコーディング、特徴写像、ハイブリッドモデル。
- **主要プレイヤー:** Xanadu（PennyLane）、IBM（Qiskit Machine Learning）、Google（TensorFlow Quantum）、Amazon Braket。
- パターン認識や生成モデリングなどがターゲット。

**量子アニーリング**

量子アニーリングは、エネルギー地形をたどって最適解を探索する手法で、組合せ最適化に適します。

- **代表的アルゴリズム:** 量子アディアバティックアルゴリズム、イジングモデルへのマッピング。
- **キーワード:** エネルギー地形、トンネリング、アニーリングスケジュール、スピンネットワーク。
- **主要プレイヤー:** D-Wave、富士通（Digital Annealer）、東芝。
- ノイズに強い条件下で有効な組合せ最適化問題に適用される。

**量子暗号**

量子暗号は量子力学を利用した安全な通信を実現します（古典暗号では達成できない性質を提供）。

- **代表的アルゴリズム／プロトコル:** BB84、E91（エンタングルメントベースの鍵交換）、ポスト量子暗号。
- **キーワード:** Quantum Key Distribution (QKD)、ノークローン定理、量子チャネル、安全性証明。
- **主要プレイヤー:** ID Quantique、東芝、NEC、Quantum Xchange、中国のQuantumCTek。
- 量子安全インフラや通信のための基盤技術。

**誤り訂正 & フォールトトレランス**

量子誤り訂正は壊れやすい量子状態を安定化し、大規模計算を可能にするために必要です。

- **代表的手法:** サーフェスコード、Bacon-Shor、Steane符号、連結符号。
- **キーワード:** 論理量子ビット、シンドローム復号、閾値、フォールトトレラントゲート。
- **主要プレイヤー:** Google、IBM、Quantinuum、PsiQuantum、Microsoft（トポロジカル量子ビット研究）。
- DiVincenzoの条件 (後半に記載) に照らしてスケーラブルな量子コンピュータを目指す。

### 4 - 量子ハードウェア

量子ハードウェアは最も物理的に要求の高い基盤レイヤーで、量子ビットの実装、制御システム、冷却、相互接続などを含みます。

**主要な量子ビット技術:**

| 物理プラットフォーム              | 基本原理                                                                   | 主要プレイヤー                 |
| --------------------------------- | -------------------------------------------------------------------------- | ------------------------------ |
| **超伝導量子ビット**              | ジョセフソン接合をマイクロ波パルスで制御                                   | IBM、Google、[Rigetti][55]     |
| **イオントラップ（Trapped Ion）** | レーザーで操作される帯電イオンを電磁場でトラップ                           | [IonQ][56], [Quantinuum][54]   |
| **光量子（Photonic）**            | 光子を用いた量子ビット。ボソンサンプリングや測定ベースQC、フォトニック回路 | [PsiQuantum][57], [Xanadu][58] |
| **中性原子（Neutral Atom）**      | 光ピンセットや格子で原子を捕捉し、レイデバーク相互作用等を利用             | [Pasqal][52], [QuEra][59]      |
| **量子アニーリング**              | 普遍的ゲートモデルではなくアディアバティック／アニーリングモデル           | [D-Wave][10]                   |
| **トポロジカル量子ビット**        | 非可換任意粒子（Non-abelian anyons）やマヨラナモードを利用する方式         | [Microsoft][60]                |

量子ゲートはマイクロ波、レーザー、光学系などを使って量子ビット状態を精密に制御して実現します。誤り訂正コード（サーフェスコード等）は安定化に不可欠です。

**補助ハードウェア／サブシステム:**

- **冷却装置（クライオジェニクス）**: 超伝導量子ビット向けの希釈冷凍機など。
- **制御電子機器／信号生成**: マイクロ波信号発生器、高速制御ライン、低雑音電子機器。
- **レーザー／光学系**: イオントラップ／中性原子向けのレーザー、光源、検出器。
- **相互接続／量子ネットワーキング**:
  光子カップリングや遠隔QKD、モジュール接続。Ciscoなどは量子システムをリンクするネットワークを研究中。 ([Cisco][51])

**具体例・ニュース:**

- Quantinuumの「黎明（Reimei）」が理研で本格稼働 - [Quantinuum][64ja] 🇯🇵（2025年2月）
- MicrosoftのMajorana 1チップ - [Microsoft][61]（2025年2月）
- IBMと理研が日本でIBM Quantum System Twoを設置 - [理研][62ja] 🇯🇵 （2025年6月）
- バスク州とIBMが欧州初のIBM Quantum System Twoを設置 - [IBM][63] 🇪🇸 （2025年10月）

## 課題とトレンド

**主要技術課題:**

- **ノイズ・誤り率・デコヒーレンス**: 誤り緩和／誤り訂正はスケーリングに向けた中心的課題。
- **スケーラビリティ**: 量子ビット数、接続性、制御オーバーヘッド、配線、冷却など。
- **物理実装のトレードオフ**: 速度、忠実度、コヒーレンス、製造可能性のバランス。
- **ランタイム／レイテンシ**: 古典コントローラと量子ハードウェア間の通信コスト。
- **標準化と相互運用性**: 共通言語、API、ハードウェア抽象化によりツールが複数ハードで動くことが必要。
- **フォールトトレランスと論理量子ビット**:
  非常に高いオーバーヘッドが必要で、ハードウェア・ファームウェア・コンパイラの協調設計が重要。

**トレンド:**

- 量子クラウド／QaaSの普及によるアクセス民主化。
- ハイブリッドアルゴリズム（変分法、QML）の成長。
- 中性原子や光フォトニクスなど、超伝導・イオントラップ以外のプラットフォームの進展。
- 量子ネットワークや相互接続、モジュラー化への関心と投資。 ([Cisco Research][50])
- 誤り訂正とフォールトトレラントアーキテクチャの研究増加。
- 開発者体験（シミュレータやツール）の改善への注力。 ([NVIDIA][53])

### DiVincenzoの条件

物理学者 David P. DiVincenzo
が提唱した「量子コンピュータが満たすべき基準（5つ＋2つ）」は、普遍的量子コンピュータの要件として現在も参照されています。([Wikipedia][101])

1. スケーラブルで特性が明確な物理的な量子ビット
2. 量子ビットを既知の初期状態に初期化する能力
3. ゲート操作時間に比べて十分に長いデコヒーレンス時間
4. 普遍的な量子ゲート集合（任意のユニタリ操作が可能）
5. 量子ビットごとの測定能力
6. 固定（stationary）量子ビットと飛翔（flying）量子ビットの相互変換能力（量子通信向け）
7. 飛翔量子ビットを忠実に伝送する能力（量子通信向け）

**現状:**

- いずれのシステムも7つ全てを完全には満たしていない。
- 超伝導やイオントラップは多くの条件を満たすが、長いコヒーレンスやスケーラビリティで課題が残る。
- フォトニクスや中性原子は（6）–（7）に強みを示す。
- Microsoftのトポロジカル量子ビット研究は、固有の誤り耐性を通じてこれらの基準へのアプローチを目指している。

## まとめ

量子コンピューティングは急速に発展していますが、まだ初期段階にあります。レイヤードスタックモデルは、各プレイヤーの役割を整理し、技術的ボトルネックがどこにあるかを理解する上で有用です。

- **サービス／アプリケーション**層は実験やプロトタイピングで比較的成熟しており、企業利用が進んでいる。
- **開発者ツール**は成熟が進みつつあるが、最適化やハードウェア認識、使いやすさの改善余地がある。
- **アルゴリズム**は有望な手法（ハイブリッド／最適化）が多いが、フォールトトレラント環境での検証はさらなる研究が必要。
- **ハードウェア**は最も困難な層で、スケール化、誤り低減、実用的なシステム構築が課題。複数の量子ビットモダリティが進展しているが、完全にDiVincenzo基準を満たすシステムはまだない。

将来的には、レイヤー間（ハードウェア↔ファームウェア↔ソフトウェア↔アルゴリズム↔アプリケーション）の統合が重要になり、複数レイヤーをまたいで事業を展開できる企業や連携が戦略的優位を持つ可能性があります。

[1]: https://www.quantumbw.de/wp-content/uploads/2024/06/QuantumBW_Strategy-Paper_EN.pdf "WHERE"
[2]: https://thequantuminsider.com/2025/03/19/the-quantum-supply-chain-mapping-the-market-and-key-players/ "The Quantum Supply Chain: Mapping the Market and Key Players"
[3]: https://quantum.cloud.ibm.com/ "IBM Quantum Platform"
[4]: https://aws.amazon.com/en/braket/ "Amazon Braket - AWS"
[5]: https://azure.microsoft.com/en-us/solutions/quantum-computing "Azure Quantum Computing | Microsoft Azure"
[6]: https://quantumai.google/ "Google Quantum AI"
[7]: https://www.dwavequantum.com/solutions-and-products/cloud-platform/ "The Leap™ Quantum Cloud Service | D-Wave"
[8]: https://terraquantum.swiss/ "Terra Quantum"
[9]: https://sitsi.pacanalyst.com/part-7-quantum-computing-vendors-navigating-the-emerging-ecosystem/ "Part 7: Quantum Computing Vendors – Navigating the Emerging Ecosystem | sitsi"
[10]: https://www.dwavequantum.com/ "D-Wave Quantum"
[11]: https://www.qcware.com/ "QC Ware"
[12]: https://1qbit.com/ "1QBit"
[13]: https://algorithmiq.fi/ "algorithmiq.fi"
[14]: https://www.quantistry.ai/ "Quantistry - Materials Intelligence & Chemical Simulation Platform for R&D"
[20]: https://www.ibm.com/quantum/qiskit "Qiskit | IBM Quantum Computing"
[21]: https://github.com/amazon-braket/amazon-braket-sdk-python "amazon-braket/amazon-braket-sdk-python: A Python SDK for interacting with quantum devices on Amazon Braket"
[22]: https://learn.microsoft.com/en-us/azure/quantum/qdk-main-overview "Build Quantum Solutions with the Azure Quantum Development Kit - Azure Quantum | Microsoft Learn"
[23]: https://quantumai.google/cirq "Cirq | Google Quantum AI"
[24]: https://pennylane.ai/ "Quantum Programming Software — PennyLane"
[25]: https://arxiv.org/abs/1811.04968 "PennyLane: Automatic differentiation of hybrid quantum-classical computations"
[26]: https://www.dwavequantum.com/solutions-and-products/ocean/ "Ocean™ Developer Tools | D-Wave"
[27]: https://github.com/dwavesystems/dwave-ocean-sdk/ "dwavesystems/dwave-ocean-sdk: Installer for D-Wave's Ocean tools"
[28]: https://projectq.ch/ "ProjectQ – Open Source Software for Quantum Computing"
[29]: https://github.com/ProjectQ-Framework/ProjectQ "ProjectQ-Framework/ProjectQ: ProjectQ: An open source software framework for quantum computing"
[30]: https://arxiv.org/abs/1612.08091 "ProjectQ: An Open Source Software Framework for Quantum Computing"
[31]: https://xacc.readthedocs.io/en/latest/ "— XACC 1.0.0 documentation"
[32]: https://github.com/eclipse-xacc/xacc "eclipse-xacc/xacc: XACC - eXtreme-scale Accelerator programming framework"
[33]: https://arxiv.org/abs/1911.02452 "XACC: A System-Level Software Infrastructure for Heterogeneous Quantum-Classical Computing"
[34]: https://openqasm.com/ "OpenQASM Live Specification"
[35]: https://q-ctrl.com/ "We make quantum technology useful | Q-CTRL"
[36]: https://www.classiq.io/ "Classiq - Quantum Computing Software"
[37]: https://github.com/Classiq/classiq-library "Classiq/classiq-library: The Classiq Library is the largest collection of quantum algorithms and applications."
[38]: https://docs.rigetti.com/qcs/guides/quil/quil "What is Quil? | QCS Documentation"
[39]: https://github.com/Qiskit/qiskit "Qiskit/qiskit: Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives."
[40]: https://github.com/quantumlib/cirq "quantumlib/Cirq: Python framework for creating, editing, and invoking Noisy Intermediate-Scale Quantum (NISQ) circuits."
[41]: https://github.com/microsoft/qdk "microsoft/qdk: Azure Quantum Development Kit, including the Q# programming language, resource estimator, and Quantum Katas"
[50]: https://research.cisco.com/quantum-research/quantum-labs "Cisco Research | Quantum Labs"
[51]: https://blogs.cisco.com/news/cisco-quantum-labs-announces-software-that-networks-quantum-computers-together-and-enables-new-classical-applications "Cisco Quantum Labs Announces Software That Networks Quantum Computers Together and Enables New Classical Applications - Cisco Blogs"
[52]: https://www.pasqal.com/ "Pasqal"
[53]: https://www.nvidia.com/en-us/solutions/quantum-computing/ "Accelerated Quantum Computing Solutions | NVIDIA"
[54]: https://www.quantinuum.com/ "Quantinuum"
[55]: https://www.rigetti.com/ "Rigetti Computing"
[56]: https://ionq.com/ "IonQ - Trapped Ion Quantum Computing"
[57]: https://www.psiquantum.com/ "PsiQuantum"
[58]: https://www.xanadu.ai/ "Xanadu"
[59]: https://www.quera.com/ "QuEra - Quantum Computing with Neutral Atoms"
[60]: https://quantum.microsoft.com/en-us/solutions/microsoft-quantum-hardware "Microsoft Quantum Hardware"
[61]: https://news.microsoft.com/source/features/ai/microsofts-majorana-1-chip-carves-new-path-for-quantum-computing/ "Microsoft’s Majorana 1 chip carves new path for quantum computing"
[62]: https://newsroom.ibm.com/2025-06-23-ibm-and-riken-unveil-first-ibm-quantum-system-two-outside-of-the-u-s "IBM and RIKEN Unveil First IBM Quantum System Two Outside of the U.S."
[62ja]: https://www.riken.jp/pr/news/2025/20250624_1/index.html "量子コンピュータIBM Quantum System Twoを神戸で本格稼働 | 理化学研究所"
[63]: https://newsroom.ibm.com/2025-10-14-the-basque-government-and-ibm-inaugurate-europes-first-ibm-quantum-system-two-in-donostia-san-sebastian "The Basque Government and IBM Inaugurate Europe's first IBM Quantum System Two in Donostia-San Sebastián"
[64]: https://www.quantinuum.com/press-releases/quantinuums-reimei-quantum-computer-now-fully-operational-at-riken-ushering-in-a-new-era-of-hybrid-quantum-high-performance-computing "Quantinuum’s “Reimei” Quantum Computer Now Fully Operational at RIKEN, Ushering in a New Era of Hybrid Quantum High-Performance Computing"
[64ja]: https://quantinuum.co.jp/20250212-2/ "量子コンピュータ「黎明」が理化学研究所で本格稼働、量子ハイブリッド高性能コンピューティング新時代を切り拓く ～理化学研究所の世界最高水準の施設に設置された量子コンピュータ「黎明」は、物理、化学、その他の応用分野における量子コンピューティング技術の進歩をリード～ ｜ Quantinuum – クオンティニュアム株式会社"
[100]: https://en.wikipedia.org/wiki/List_of_companies_involved_in_quantum_computing,_communication_or_sensing "List of companies involved in quantum computing, communication or sensing - Wikipedia"
[101]: https://en.wikipedia.org/wiki/DiVincenzo%27s_criteria "DiVincenzo's criteria - Wikipedia"
