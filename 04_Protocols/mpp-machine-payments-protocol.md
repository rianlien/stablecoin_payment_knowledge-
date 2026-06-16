---
title: Machine Payments Protocol（MPP）
type: protocol
updated: 2026-06-16
tags:
  - stripe
  - mpp
  - agent-payments
  - agentic-commerce
---

# Machine Payments Protocol（MPP）

Stripe が提案する AI エージェント向け決済プロトコル。Stripe の加盟店網、Link、Bridge、Privy、Shared Payment Tokens などを組み合わせ、エージェントが既存の Stripe 決済インフラ上で支払いを実行できるようにする構想。

---

## 何を解くプロトコルか

MPP が解く中心課題は、**既存の Stripe 加盟店・PSP インフラを大きく変えずに、エージェント起点の支払いを受け入れること**。

- エージェントがマイクロ・定期・オンデマンド決済を実行する
- Stripe / Link / Bridge / Privy を通じて支払い手段を抽象化する
- 加盟店がエージェント向けの承認・支出ルールを管理する
- Radar などの既存リスク管理と組み合わせて正規エージェントを識別する

---

## レイヤー上の位置づけ

| 項目 | 内容 |
|---|---|
| 主体 | Stripe |
| 主なレイヤー | 支払いプロトコル層 / PSP 実装層 |
| 決済レール | Stripe 決済基盤、カード、銀行、stablecoin、BNPL 等 |
| 強み | 加盟店網、既存 Stripe API、支払い手段の広さ、運用機能 |
| 弱み / 未解決 | 仕様公開範囲、Stripe 依存、x402 との相互運用性 |

MPP はオープンな web 標準というより、Stripe の決済・ウォレット・リスク管理スタックをエージェント決済向けに拡張するアプローチとして見るのが近い。

---

## 他プロトコルとの関係

| 相手 | 関係 |
|---|---|
| x402 | machine payment / API 課金では競合。AWS AgentCore では共存する可能性が示されている |
| AP2 | AP2 が委任・認可、MPP が Stripe 上の支払い実行を担う補完関係になりうる |
| Visa TAP | TAP がカードネットワーク側の trusted agent 識別、MPP が Stripe 加盟店側の受け入れを担う可能性 |
| Circle CPN / Bridge | stablecoin の着地・精算インフラとして補完関係 |

---

## 関連ニュース

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-30 | [[2026-04-30_Stripe-Sessions-2026_MPP-agentic-payments]] | MPP 発表。Stripe Sessions 2026 の中心トピック |
| 2026-05-06 | [[2026-05-06_RedotPay-Tempo_mpp-agentic-payments-launch]] | Tempo / RedotPay 文脈での agentic payments 実装 |
| 2026-05-07 | [[2026-05-07_AWS_bedrock-agentcore-payments-x402]] | AWS AgentCore における x402 との共存論点 |

---

## 監視ポイント

- MPP の公開仕様・SDK・参加条件
- Stripe が x402 Foundation 参加企業として MPP と x402 をどう整理するか
- Link エージェントウォレットの GA と対応加盟店数
- Radar のエージェント識別機能の実装シグナル
- BNPL や stablecoin をエージェントが使う場合の責任分担
