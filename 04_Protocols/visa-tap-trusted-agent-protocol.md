---
title: Visa Trusted Agent Protocol（TAP）
type: protocol
updated: 2026-06-16
tags:
  - visa
  - tap
  - trusted-agent-protocol
  - payment-authorization
  - agentic-commerce
---

# Visa Trusted Agent Protocol（TAP）

Visa が提案するエージェント向けの信頼・認証プロトコル。AI エージェントを「正規の購買エージェント」として識別し、加盟店や PSP が悪質 bot と区別できるようにすることを目的とする。

---

## 何を解くプロトコルか

TAP が解く中心課題は、**カード加盟店が agent-originated transaction を安全に受け入れるための信頼判定**。

- エージェントが Visa 認証済みかを加盟店側で識別する
- ユーザーの支出上限、承認要否、加盟店制限などを反映する
- Visa の fraud monitoring / tokenized credential と組み合わせる
- 既存 Visa acceptance 上で agentic commerce を成立させる
- bot 対策と正規エージェント受け入れを同時に扱う

---

## レイヤー上の位置づけ

| 項目 | 内容 |
|---|---|
| 主体 | Visa |
| 主なレイヤー | エージェント認証・カードネットワーク信頼層 |
| 決済レール | Visa カードネットワーク |
| 強み | 既存加盟店網、カードネットワークのリスク管理、Visa credential との接続 |
| 弱み / 未解決 | TAP レジストリ仕様、AP2 との相互運用性、責任分担、公開 API |

TAP は x402 のようなオンチェーン決済実行プロトコルではない。カード網上で「このエージェントを信頼してよいか」を示す認証・信頼レイヤーとして捉える。

---

## 他プロトコルとの関係

| 相手 | 関係 |
|---|---|
| AP2 | 認可・委任モデルとして競合しやすい。相互運用できるかが焦点 |
| x402 | TAP が trusted agent 識別、x402 が stablecoin 決済を担う補完関係になりうる |
| MPP | Stripe 加盟店が Visa 決済を受ける場合、TAP の agent metadata と MPP / Stripe リスク管理が接続する可能性 |
| Mastercard A2A | カードネットワーク主導の agentic payments として競合 |

---

## 関連ニュース

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-05 | [[2026-05-05_Visa_agentic-ready-canada-global]] | Visa Agentic-Ready 展開の文脈 |
| 2026-05-27 | [[2026-05-27_Highnote-Visa_agentic-commerce-ai-initiated-payments]] | issuer / card program 側の agentic payments 実装 |
| 2026-05-28 | [[2026-05-28_Visa-Replit_trusted-agent-protocol]] | Replit との連携。開発者環境への TAP 統合 |
| 2026-06-11 | [[2026-06-11_Visa-OpenAI_chatgpt-agent-payments]] | ChatGPT 内 Visa カード決済連携 |

---

## 監視ポイント

- TAP レジストリの公開仕様と登録要件
- Visa Agentic-Ready 対応加盟店・PSP の数
- AP2 / FIDO Alliance との相互運用方針
- agent-originated transaction metadata が issuer / acquirer / merchant にどう渡るか
- refund、chargeback、friendly fraud 時の責任分担
