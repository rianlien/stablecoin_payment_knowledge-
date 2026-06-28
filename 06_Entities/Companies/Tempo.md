---
title: "Tempo"
type: company
updated: 2026-06-28
category: infrastructure
tags:
  - stablecoin
  - payments
  - agentic-commerce
  - company
---

# Tempo

Tempo は Stripe と Paradigm が共同でインキュベートした決済特化型 Layer-1 ブロックチェーン。Machine Payments Protocol（MPP）を通じて AI エージェントからの決済受け入れを標準化する方向に軸足を置いている。

---

## 現状の要約

### 何をしているか

- **決済特化 L1 ブロックチェーンの提供**: Stripe と Paradigm が 2025 年 9 月に発表した決済特化 Layer-1 ブロックチェーン。2026 年 3 月に評価額 50 億ドルで 5 億ドルを調達（PR Newswire / PYMNTS 報道ベース、Inbox ノートの二次情報として引用）。
- **Machine Payments Protocol（MPP）のローンチ**: Stripe Sessions 2026（2026-04-30）で Stripe と共同策定したオープン標準 MPP を正式発表。AI エージェントやサービスがプログラムで決済を送受信するための仕様。
- **MPP の最初の実動実装（2026-05-06）**: RedotPay（700 万人超ユーザー・100 か国以上）が Stripe Sessions 発表からわずか 1 週間で MPP 上に AI エージェント決済を本番ローンチ。
- **大手エコシステムパートナーの獲得**:
  - OnePay（Walmart 出資）：ステーブルコインペイアウト・即時口座入金機能を追加。Tempo バリデーターノードを運用。
  - DoorDash：加盟店向けステーブルコインペイアウトを実装（2026-04-21）。
  - Klarna：KlarnaUSD を Tempo 上で展開。
  - Visa、BankingCircle：清算・決済パートナーとして参加。

### 見立て

Tempo は Stripe という既存の決済インフラ企業を後ろ盾に、MPP という「エージェント決済の標準仕様」を通じてエコシステムを構築しようとしている。2025 年 9 月の発表から 1 年足らずで DoorDash・OnePay・Klarna・Visa という大型パートナーを揃えた速度は注目に値する。一方で x402（Linux Foundation・Coinbase 系）との標準競争が本格化しており、どちらを選択するかの判断が PSP・フィンテック各社に迫られている段階にある。RedotPay の MPP ローンチが示すように、実装速度は速いが、Stripe 以外の大手 PSP がどちらを選ぶかが長期的な標準化の行方を左右すると見られる。

---

## MPP（Machine Payments Protocol）の概要

- **策定**: Tempo + Stripe が共同策定したオープン標準
- **目的**: AI エージェントやサービスがプログラムで決済を送受信するための仕様
- **競合**: x402（HTTP 402 ベース、Linux Foundation 管理、Coinbase 主導）
- **詳細**: [[mpp-machine-payments-protocol]] を参照

---

## 主要パートナー（確認済み）

| パートナー | 内容 |
|---|---|
| OnePay（Walmart 出資） | ステーブルコインペイアウト・即時口座入金、Tempo バリデーター運用 |
| DoorDash | 加盟店向けステーブルコインペイアウト |
| RedotPay | MPP 上でエージェント決済を本番ローンチ（700 万人超・100 か国以上） |
| Klarna | KlarnaUSD の展開 |
| Visa | 清算・決済参加 |
| BankingCircle | 決済参加 |

---

## 監視ポイント

- MPP 仕様のオープン化状況（公開ドキュメントの拡充）
- x402 vs MPP の採用企業数・処理量の推移
- Tempo 上での AI エージェント決済における KYC/AML の適用層
- Stripe 以外の大手 PSP（Adyen・Worldpay 等）の MPP 採用動向
- RedotPay 第二フェーズ（「決済スキル」ダウンロード機能、2026 年 6 月予定）の実装状況

---

## Inbox との紐付け

| 日付 | ノート | 位置づけ一行 |
|---|---|---|
| 2026-04-28 | [[2026-04-28_OnePay-Tempo_stablecoin-payouts-partnership]] | OnePay が Tempo と提携——ステーブルコインペイアウト・即時口座入金・バリデーター運用を表明 |
| 2026-04-28 | [[2026-04-28_OnePay-Tempo_stablecoin-payouts-walmart]] | Walmart 傘下 OnePay の Tempo 参加——DoorDash に続く大手リテール系プレイヤーの採用でエコシステム拡大 |
| 2026-04-29 | [[2026-04-29_OnePay-Tempo_stablecoin-payouts-walmart]] | OnePay × Tempo の続報——Walmart の 1.5 億人顧客網と Tempo ブロックチェーンの接続 |
| 2026-05-06 | [[2026-05-06_RedotPay-Tempo_mpp-agentic-payments-launch]] | RedotPay が MPP 上でエージェント決済を本番ローンチ——Stripe Sessions 発表から 1 週間での実装 |
