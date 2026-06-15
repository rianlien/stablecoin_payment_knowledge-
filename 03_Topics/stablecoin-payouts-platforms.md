---
title: "ステーブルコイン・ペイアウト（プラットフォーム・加盟店向け）"
type: topic
updated: 2026-06-15
tags:
  - stablecoin
  - payouts
  - merchant-readiness
  - PSP-readiness
  - cross-border-payments
---

# ステーブルコイン・ペイアウト（プラットフォーム・加盟店向け）

プラットフォームや PSP がステーブルコインを使って加盟店・ギグワーカー・クリエイター・フリーランサーへ支払いを行う動き。DoorDash・Meta・Walmart（OnePay）・MassPay など大手プレイヤーが2026年春以降に相次いで実装または発表しており、ACH・SWIFT に代わる国際ペイアウトレールとしての地位を急速に確立しつつある。

---

## 全体像

### 採用の背景

従来の国際送金（ACH は1〜3営業日、SWIFT は手数料が高く着地が遅い）に対し、ステーブルコインは「24/7・1秒未満のファイナリティ・40〜70% のコスト削減」を提供できる。これが特に以下の場面で採用を加速させている。

- **マーケットプレイス型プラットフォーム**（DoorDash、Uber 系）：加盟店・配達員への即時送金
- **クリエイターエコノミー**（Meta/Instagram）：フリーランサー・インフルエンサーへの報酬支払い
- **コンシューマー金融アプリ**（Walmart の OnePay）：ユーザーへの即時口座入金・送金
- **B2B グローバル送金フィンテック**（MassPay）：1099 コントラクター・ギグワーカーへの国際支払い

### インフラの構図

2026年時点で主に3つのインフラ経路が並走している。

1. **Stripe / Tempo スタック**：DoorDash・OnePay (Walmart) が採用。Tempo はStripe・Paradigm が支援する決済特化 Layer-1 ブロックチェーン（2026年3月に50億ドル評価・5億ドル調達）。Stripe の Bridge・Metronome と統合し、加盟店精算から AI トークン消費課金まで対応。
2. **Circle USDC / CPN（Circle Payments Network）**：Meta（Stripe 経由）・MassPay が採用。USDC を既存ウォレット（MetaMask・Phantom・GCash 等）に着金させ、オフランプは利用者が個別に行う設計。
3. **Coinbase Payments**：MassPay（Coinbase 提携）・Checkout.com（Coinbase Payments 統合）が採用。「USDC 支払い → USD 精算」のモデルで加盟店側の暗号資産リスクをゼロにする。

### ペイアウトの受取側設計

加盟店・労働者がどのように受け取るかでモデルが分かれる。

| モデル | 例 | 受取側のオフランプ |
|---|---|---|
| USDC 着金（ウォレット） | Meta クリエイター | 利用者が自力でフィアット換金 |
| 銀行口座への即時入金 | OnePay、DoorDash Dasher | ステーブルコインレール経由で銀行口座に変換 |
| ローカル通貨着金 | MassPay（180カ国） | MassPay がラストマイル換金を担当 |
| USD 精算（フィアット変換済み） | Checkout.com 加盟店 | Coinbase Payments が変換、加盟店は USD 受取 |

---

## 主要ノート

| 日付 | ノート | 概要 |
|---|---|---|
| 2026-04-21 | [[2026-04-21_DoorDash-Tempo_stablecoin-merchant-payouts]] | DoorDash が Tempo 上で40カ国超の加盟店・配達員向けステーブルコイン決済を発表 |
| 2026-04-28 | [[2026-04-28_OnePay-Tempo_stablecoin-payouts-partnership]] | Walmart 傘下 OnePay が Tempo と提携、Banking 製品にステーブルコインペイアウトを追加 |
| 2026-04-28 | [[2026-04-28_OnePay-Tempo_stablecoin-payouts-walmart]] | OnePay が Tempo バリデーターノードも起動——インフラ参加者として関与を深化 |
| 2026-04-29 | [[2026-04-29_Meta_usdc-creator-payouts-stripe]] | Meta が Stripe 経由で USDC クリエイター報酬支払いを開始（コロンビア・フィリピン先行） |
| 2026-05-13 | [[2026-05-13_Stripe-Tempo_streaming-stablecoin-payments]] | Stripe × Tempo で AI トークン消費に応じたストリーミング決済（利用量課金）を発表 |
| 2026-06-02 | [[2026-06-02_Coinbase-Checkout_stablecoin-merchant-payments]] | Coinbase × Checkout.com で 1,000 社超の加盟店に USDC/USDT 決済を解禁 |
| 2026-06-11 | [[2026-06-11_MassPay-Coinbase_stablecoin-payouts]] | MassPay × Coinbase 提携で USDC クロスボーダー送金を 180 カ国に展開 |

---

## 現状の論点

- **インフラ収束 vs. 分散**：Tempo（Stripe エコシステム）・Circle CPN・Coinbase Payments の3経路が並走しており、どれが標準ペイアウトレールになるか未確定。大手プラットフォームが複数経路を並行採用する可能性もある。
- **オフランプの整備**：加盟店・ワーカーが USDC を受け取っても現地通貨への換金手段が整わない地域では実用性が制限される。MassPay のようなラストマイル事業者の役割が鍵を握る。
- **GENIUS Act 対応**：2025年7月成立の GENIUS Act 以降、ペイアウトに使用するステーブルコインの「許可発行体」要件への準拠が採用判断に影響する。USDT の準拠状況は未確定のため、USDC が法人採用の実質標準になる可能性が高い。
- **エージェント決済との接続**：プラットフォーム → 加盟店のペイアウトレールが整備されると、将来的にはエージェントが自律的に発注・支払いを行うフローへの転用が自然になる。x402 や Circle Agent Stack との統合が次のステップとして浮上しつつある。
- **課金粒度の拡張**：Stripe × Metronome × Tempo のストリーミング決済モデルは、「1件のペイアウト」から「API コール・トークン消費単位のリアルタイム回収」へ課金粒度を細分化する試みであり、ペイアウトの概念自体を更新している。

---

## 監視ポイント

- DoorDash・OnePay のステーブルコインペイアウト実際の稼働量データ（Q2〜Q3 2026 公開予定）
- MassPay の初年度ステーブルコイン送金額（CEO 予測の9桁達成の可否）
- Meta のグローバル展開スケジュール（コロンビア・フィリピン以降の対象国）
- Checkout.com の1,000社加盟店のうち USDC 決済を実際に有効化した比率
- Stripe / Tempo ストリーミング決済の日本提供可否（GENIUS Act 対応・日本資金決済法との整合性）
- Circle CPN と Coinbase Payments のどちらが B2B ペイアウト市場で主要インフラになるか
- USDT の GENIUS Act 準拠状況の確定——USDC 一極化 vs. マルチコイン設計の分岐点

---

## 関連ページ

- [[x402-ecosystem]]
- [[agent-payment-authorization]]
- [[psp-merchant-readiness]]
- [[MOC_Regulation]]
