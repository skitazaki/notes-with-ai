+++
date = '2026-05-10T14:00:00+09:00'
title = '参照アーキテクチャ'
weight = 12
prev = '/docs/acc/decision-frameworks'
next = '/docs/acc/concept-dictionary'
+++

参照アーキテクチャは万能の設計図ではありません。原則、制御、トレードオフが現実的な環境でどう組み合わさるかを示す、調整済みの例です。

## Executive Summary

繰り返し現れる代表的な 3 パターンがあります。

- federation、PAM、governance を中核に据えた workforce architecture
- workload identity と policy enforcement を中核に据えた cloud-native platform architecture
- constrained delegation と approval boundary を中核に据えた AI-agent architecture

これらの例は、単一制御だけを最適化するのではなく、システム境界をまたいで全体を考える助けになります。

## Core Concepts

### Enterprise workforce architecture

authoritative HR が lifecycle event を identity platform に供給します。federation は社内アプリと SaaS への SSO を提供します。MFA と conditional access が assurance を高めます。高感度な管理経路は JIT elevation を伴う PAM を使います。governance system は access review と SoD check を回します。SIEM は identity、policy、privileged session のイベントを収集します。

### Cloud-native service architecture

開発者は platform-issued identity を持つ workload を配備します。service mesh や gateway が mTLS と service policy を検証します。細粒度認可はアプリまたは policy engine 層で行います。シークレットは最小化し、ephemeral credential を優先します。observability system は service identity、deployment metadata、access decision を相関します。

### AI-agent architecture

エージェントには常在の user privilege ではなく、task-bounded capability を与えます。tool call は policy check を通ります。memory は tenant と task class で分割します。高リスク操作は approval または cryptographic delegation を要求します。decision log には user intent、delegated scope、selected tool、outcome を残します。

## Implementation and Operations

### これらに共通する点

- 明示的な trust boundary
- identity issuance と authorization decision の分離
- 短命または revocable な資格情報
- 分散 enforcement を支える中央ガバナンス
- 復元と封じ込めに使える decision record

参照アーキテクチャが最も役立つのは、規制負荷、latency 許容度、チーム成熟度といったローカル制約に合わせて調整されるときであり、機械的にコピーされるときではありません。
