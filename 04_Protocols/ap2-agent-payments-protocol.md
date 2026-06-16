---
title: Agent Payments Protocol（AP2）
type: protocol
updated: 2026-06-16
tags:
  - ap2
  - google
  - fido
  - payment-authorization
  - agentic-commerce
---

# Agent Payments Protocol（AP2）

Google が発表し、FIDO Alliance に寄贈されたエージェント決済の認可・委任プロトコル。ユーザーが AI エージェントに「どの条件なら支払ってよいか」を事前に与え、その意図と承認ログを検証可能にすることを目指す。

---

## 何を解くプロトコルか

AP2 が解く中心課題は、**人間がその場にいない決済で、ユーザーの意思とエージェントの権限範囲をどう証明するか**。

- ユーザーがエージェントに支払い権限を委任する
- spending limit、merchant restriction、approval rule などを表現する
- Human Not Present 決済を扱う
- Verifiable Intent によって承認・実行ログを残す
- FIDO / passkey 系の認証モデルと接続する

---

## レイヤー上の位置づけ

| 項目 | 内容 |
|---|---|
| 主体 | Google / FIDO Alliance |
| 主なレイヤー | 認可・委任・監査ログ層 |
| 決済レール | 特定レールに依存しない設計を志向 |
| 強み | FIDO の標準化実績、Verifiable Intent、Human Not Present 対応 |
| 弱み / 未解決 | v1.0 仕様、実装範囲、カード / stablecoin 各レールとの役割分担 |

AP2 は単独の決済レールではない。x402、MPP、カード決済、stablecoin rail などの上に載る「認可・委任の共通語彙」として見るべき。

---

## 他プロトコルとの関係

| 相手 | 関係 |
|---|---|
| x402 | AP2 が認可、x402 が支払い実行。補完関係が強い |
| MPP | AP2 が委任証跡、MPP が Stripe 上の支払い実行を担う可能性 |
| Visa TAP | trusted agent / delegated payment の標準争いでは競合しやすい |
| Mastercard A2A | Mastercard が Verifiable Intent に関与しており補完関係がある |

---

## 関連ニュース

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-28 | [[2026-04-28_Google_ap2-fido-alliance]] | AP2 の FIDO Alliance 寄贈、v0.2、Human Not Present |
| 2026-05-19 | [[2026-05-19_Google_universal-cart-ap2-io2026]] | Universal Cart / agentic commerce 文脈での AP2 |
| 2026-05-05 | [[2026-05-05_Solana-GoogleCloud_pay-sh-x402-agent-payments]] | Google Cloud / x402 連携の文脈 |

---

## 監視ポイント

- FIDO Alliance での AP2 ワーキンググループ体制
- AP2 v1.0 の公開時期と仕様範囲
- Verifiable Intent がオンチェーン記録かオフチェーン署名か
- x402 / MPP / Visa TAP との相互運用性
- Human Not Present 決済に対する規制・消費者保護上の扱い
