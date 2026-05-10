+++
date = '2026-05-10T13:00:00+09:00'
title = 'AI エージェントと自律的認可'
weight = 6
prev = '/docs/acc/workload-identity'
next = '/docs/acc/defense-in-depth'
+++

AI エージェントは、既存権限の上に載る単なる UI 機能ではなく、制約付きで動作する運用上の identity として扱うべきです。

## Executive Summary

AI エージェントは、文脈を読み、ツールを選び、アクションを生成し、人間より高い速度と規模で複数システムをまたいで動けます。これにより認可問題の性質が変わります。重要なのは、エージェントが認証されているかだけではありません。委譲された権限が、どのように境界づけられ、説明され、監視され、剥奪されるかです。

そのため agent security では、tool scope、memory access、approval boundary、execution environment を明示的に制御する必要があります。これがない場合、広い権限と確率的挙動の組み合わせにより、新しい confused deputy や prompt injection のリスクが生まれます。

## Core Concepts

### principal としてのエージェント

エージェントは次の形で振る舞います。

- 人間 principal の代理として動く
- 自身の service identity で動く
- 特定タスク用に発行された delegated capability を用いて動く

これらを混同すべきではありません。「ユーザーの代理」という説明だけでは trust model になりません。誰が何を、どの期間、どのツールに、どの policy constraint 付きで委譲したのかを記録する必要があります。

### 主なリスク領域

- **Prompt injection** によりツール利用やデータ解釈が変えられる
- **Over-permissioned tools** により小さな文脈露出が大きな侵害に発展する
- **Memory leakage** によりタスク間の機微情報が露出する
- **Multi-agent chains** により計画と実行の責任境界が曖昧になる
- **Agent impersonation** は共有または常在の tool credential で起こりやすい

### より良い制御モデル

有望なパターンとして、capability-based delegation、ephemeral execution identity、高感度操作に対する human-in-the-loop approval、sandbox 化された tool runtime、暗号的に束縛された delegation record があります。

## Implementation and Operations

### 設計ガイダンス

- 広い user token の再利用ではなく、task-scoped credential を発行する
- read、write、approval を分離する
- agent memory は tenant、workflow、retention class ごとに隔離する
- tool invocation 自体を policy enforcement point として扱う
- intent、prompt context class、selected tool、approval、outcome を記録する

### 実務的な承認モデル

低リスク操作は、境界づけられた policy 内で事前承認できる場合があります。中リスク操作には、データ分類検証や異常検知などの二次チェックを入れます。権限変更、本番書き込み、規制データの持ち出しなど高リスク操作には、明示的な承認または暗号的委譲が必要です。

目標は自律性を完全に止めることではありません。自律的挙動を、境界づけられ、可観測で、統制可能なものにすることです。
