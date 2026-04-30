---
title: "Stripe Sessions 2026：ステーブルコイン決済 32 市場拡大・Bridge 強化・Link 実装仕様"
date: 2026-04-30
source: Stripe 公式ブログ / Stripe Docs
source_url: https://stripe.com/blog/everything-we-announced-at-sessions-2026
entity: Stripe
category: 企業発表
tags:
  - stablecoin
  - payments
  - psp
  - wallet
  - regulation
summary: "Stripe が Sessions 2026 カンファレンスで、ステーブルコイン決済受け入れを 32 市場追加、USDT 対応プレビュー（Q2）、BTC・SOL・ETH 対応（Q4）を発表。Bridge の対応チェーン・通貨を大幅拡充し、Privy 連携ノンカストディアルウォレットも公開。Link 経由のステーブルコイン受け取り仕様も Docs で詳細が明らかになった。"
implications: "PSP としてステーブルコインを『決済の一形態』として完全統合するフェーズに入った。Bridge による多通貨・多チェーン対応は、Stripe を事実上のステーブルコイン清算レイヤーとして位置付ける戦略。"
follow_up: "USDT Q2 対応の正式 GA、BTC/SOL/ETH Q4 対応の規制対応状況、米国以外での Link ステーブルコイン解禁タイミング"
---

## 概要

Stripe は Sessions 2026 カンファレンス（2026-04-30）において、ステーブルコイン決済インフラの大規模拡張を発表した。受け入れ可能市場の拡大、Bridge による多チェーン・多通貨対応、Privy 連携ノンカストディアルウォレット提供が柱。Stripe Docs（`docs.stripe.com/payments/link/stablecoins`）では Link 経由のステーブルコイン受け取りの現行仕様も同時公開された。

## 何が起きたか

**ステーブルコイン受け入れ拡大**
- ステーブルコイン決済の受け入れを 32 市場に追加（GA）
- USDT を決済通貨として受け入れるプレビューを発表（Q2 2026 予定）
- BTC・SOL・ETH の決済通貨対応を Q4 2026 にプレビュー予定
- ステーブルコイン裏付けカードを 30 カ国で提供（国内・国際決済両対応）

**Bridge 対応拡張**
- オンランプ/オフランプ通貨に COP（コロンビアペソ）と GBP（英ポンド）を追加（既存: USD・BRL・EUR・MXN）
- 対応ステーブルコインに USDG・CASH・USDSui・USDCBL を追加
- 対応ブロックチェーンに Tempo・Plasma・Celo・Sui を追加

**Privy 連携ノンカストディアルウォレット**
- Privy との提携により 150 カ国以上でクロスボーダー即時送金を可能にするノンカストディアルウォレットを提供
- カストディアル/セルフカストディアルをウォレット単位で柔軟に選択可能

**Treasury・グローバル送金拡充**
- Treasury のステーブルコイン対応を 41 市場追加（年末までに対応予定）
- フィアット 100 カ国以上・ステーブルコイン 160 カ国での送金に対応

**Link ステーブルコイン受け取り仕様（Docs 情報）**
- 対応フロー: Payment Links・Stripe Checkout・Elements のみ（他フロー非対応）
- 対象取引: USD 建て $1〜$10,000、一回払い・オンセッション取引のみ
- 対象事業者: 現時点では米国事業者のみ
- 顧客側: 任意のクリプトウォレット・トークン・ネットワークで支払い可能
- 着金: Stripe 残高には USD として着金（ステーブルコイン変換は Stripe が処理）
- チャージバック非対応、返金はステーブルコインで元ウォレットへ
- テスト時はブロックチェーンテストネット・テストネット資金ウォレットを使用

## なぜ重要か

### 決済事業者視点
- Stripe が PSP として「ステーブルコインを別のプロダクト」ではなく「既存の決済フローの延長」として統合したことで、競合 PSP（Adyen・Braintree 等）への対比上の優位性が明確化
- Bridge の多チェーン・多通貨拡張により、Stripe は事実上のステーブルコイン清算レイヤーとして機能し始めた。Circle CPN との直接競合関係が明確化

### 加盟店視点
- 現時点で Link ステーブルコイン受け取りは米国事業者・USD 建て限定。日本・EU 加盟店は当面対象外だが、32 市場拡大のロードマップ上に含まれる可能性がある
- 受け取りが USD 着金のため、ステーブルコイン変動リスクを取る必要がない点は導入障壁を低下させる
- チャージバック非対応は高額取引・コンシューマー向け利用では制約になりうる

### プロダクト視点
- Privy ノンカストディアルウォレット + Bridge のオンランプ/オフランプが組み合わさることで、Stripe は「発行→保管→送金→受け取り」のステーブルコインライフサイクル全体をカバーするスタックを持った
- Bridge の USDG（Global Dollar Network）対応は、Paxos エコシステムとの連携を示す（Banking Circle も USDG 対応を同時期に発表）

### 規制 / リスク視点
- BTC・SOL・ETH の決済通貨対応（Q4）は、ステーブルコインではなく暗号資産そのものを受け取ることを意味する。米国の暗号資産規制（GENIUS Act とは別軸）への対応が必要
- チャージバック非対応・返金ルールの明示は、消費者保護規制（EU PSD3・英国 PSR 等）との整合性で今後問われる可能性がある

## 我々への示唆

- いま検討すべきこと:
  - Stripe の Link ステーブルコイン仕様（米国・USD 限定）が、自社プロダクトの対象市場・通貨と合致するか評価
  - Bridge の COP・GBP 対応追加が、自社の新興国・英語圏展開ロードマップと重なるなら Bridge API の優先評価を検討
- 後で深掘りすべきこと:
  - Bridge の USDG・CASH・USDSui・USDCBL 各ステーブルコインの発行体・準備資産・コンプライアンス要件の比較
  - Privy ノンカストディアルウォレットの KYC/AML フロー詳細（Stripe が担うか、事業者側か）
- 今は優先度が低いこと:
  - BTC・SOL・ETH 対応（Q4 プレビュー）は規制動向次第。現時点では情報収集にとどめる

## 未解決の論点

- Link ステーブルコイン受け取りで「任意のトークン・ネットワーク」とあるが、実際にサポートされるチェーン/トークンの具体的なリストは非公開
- Bridge の USDCBL（Coinbase-linked?）の発行体・バッキング詳細が不明
- Privy 連携ウォレットにおける Stripe vs Privy のカストディ責任分担・ライセンス主体

## 参考リンク

- 一次情報: [Stripe Sessions 2026 発表まとめ](https://stripe.com/blog/everything-we-announced-at-sessions-2026)
- 一次情報: [Stripe Docs — Link Stablecoin Payments](https://docs.stripe.com/payments/link/stablecoins)
- 補足情報: [DoorDash × Tempo ステーブルコイン加盟店送金（2026-04-21）](./2026-04-21_DoorDash-Tempo_stablecoin-merchant-payouts.md)
- 補足情報: [Veem × Bridge ステーブルコイン口座（2026-04-22）](./2026-04-22_Veem-Bridge_stablecoin-accounts-launch.md)
- 補足情報: [Banking Circle MiCA ステーブルコイン決済（2026-04-27）](./2026-04-27_BankingCircle_mica-stablecoin-settlement.md)

## 重要度

- High

## 確からしさ

- High（Stripe 公式ブログ + Stripe Docs による一次情報）
