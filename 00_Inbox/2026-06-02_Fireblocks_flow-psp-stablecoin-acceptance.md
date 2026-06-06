---
title: "Fireblocks、PSP・フィンテック向けステーブルコイン受け取りインフラ「Fireblocks Flow」をローンチ"
date: 2026-06-02
source: "PR Newswire / Fireblocks Blog / Fintech Singapore / TipRanks"
source_url: "https://www.prnewswire.com/news-releases/fireblocks-launches-flow-stablecoin-acceptance-for-psps-and-fintechs-302788865.html"
entity: "Fireblocks / Flutterwave / Nuvion"
category: "merchant-PSP-readiness"
primary_category: "stablecoin-payments"
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - merchant-PSP-readiness
  - stablecoin
  - payments
  - payment-rails
  - machine-payments
summary: "Fireblocks が 2026 年 6 月 2 日、Money20/20 Europe（アムステルダム）にて PSP・フィンテック向けステーブルコイン受け取りインフラ「Fireblocks Flow」をローンチ。PSP の既存決済フローに統合するだけで、加盟店がいかなるデジタルアセットでも受け取り・選択したステーブルコインで決済できるようになる。EVM・Solana・Bitcoin の 800 超ウォレットに対応。Open Transaction Layer（OTL、2026-05-28 開始）準拠設計。ローンチパートナーはアフリカ最大 PSP の Flutterwave と B2B 多通貨バンキングの Nuvion。"
implications: "従来の PSP がステーブルコイン受け取り対応を『数週間〜数ヶ月の開発』なしに導入できるプラグアンドプレイ型インフラが登場した。Flutterwave を通じたアフリカ・新興市場への展開と、OTL 準拠による相互運用性の担保が、PSP 主導のステーブルコイン決済普及を加速する可能性がある。"
importance: Medium
confidence: High
follow_up: "Fireblocks Flow での agentic payments 対応有無（AI エージェントからの stablecoin 支払いを受け取る設計かどうか）、OTL 対応 PSP の件数推移、Flutterwave 経由のアフリカ展開における採用指標、Mastercard BVNK との競合・補完関係"
---

## 概要

Fireblocks が 2026 年 6 月 2 日、Money20/20 Europe にて「Fireblocks Flow」をローンチした。PSP・フィンテックが自社の既存決済フローを大幅に変更することなく、顧客からのステーブルコイン・デジタルアセット受け取りに対応できるインフラ。5 月 28 日に立ち上がった Open Transaction Layer（OTL）への対応も組み込まれている。

## 何が起きたか

### Fireblocks Flow の概要

- **対象**：PSP（Payment Service Provider）・フィンテック企業
- **機能**：
  - 顧客（消費者・法人）が任意のデジタルアセット（ステーブルコイン・暗号資産）で支払えるようにする
  - PSP は決済を任意のステーブルコインで受け取り・決済（settle）できる
  - 既存の決済フローに統合する形で動作（PSP がシステムを再構築する必要はない）
- **接続性**：EVM チェーン・Solana・Bitcoin 上の 800 超外部ウォレット、および Coinbase・Kraken・Crypto.com 等の主要取引所に接続
- **OTL（Open Transaction Layer）対応**：2026 年 5 月 28 日に Fireblocks・Robinhood・MetaMask 等が立ち上げたオンチェーン取引の ID・メッセージ・コーディネーション標準。Flow は OTL 対応設計のため、OTL 参加 PSP が増えるにつれて自動的に接続性が拡張される

### ローンチパートナー

- **Flutterwave**：アフリカ最大の決済プラットフォーム。Flow を用いて消費者・法人から任意デジタルアセットで受け取り、PSP 選択ステーブルコインに変換する仕組みを導入
- **Nuvion**：B2B 多通貨バンキングプラットフォーム（100 市場・50 通貨対応）。ステーブルコイン支払い対応に Flow を採用

### 発表背景：OTL との関係

- OTL（Open Transaction Layer）は 2026 年 5 月 28 日に Fireblocks が中心となり立ち上げた、30 超の金融機関・ブロックチェーン・インフラ企業が参加するオープン標準
- Robinhood・eToro・MetaMask が OTL をサポート
- Flow は OTL 互換設計のため、新たな PSP が OTL に参加するたびに Flow の接続対象が自動拡張する

## 確認された事実

- PR Newswire 公式プレスリリース（2026-06-02）による
- Money20/20 Europe（6/2〜6/4）での公式ローンチ発表
- Flutterwave がローンチパートナーとして明示
- OTL 対応は Fireblocks ブログで確認

## なぜ重要か

### 決済事業者視点
- PSP がステーブルコイン受け取りに対応する際の「開発コスト・技術負債」を大幅に下げるインフラ。特に中小 PSP・新興市場 PSP にとって独自開発コストを削減できる
- Flutterwave という最大の実装事例が、アフリカ・新興市場でのステーブルコイン PSP 展開を後押しする——Circle CPN + Nium の法人決済ルートとの組み合わせで、エージェント決済のグローバル「着地」インフラが充実する

### 加盟店視点
- Flutterwave 経由でアフリカ加盟店がステーブルコイン受け取りに対応できれば、エージェント決済（AI が B2B 支払いを実行）の「着地点」が拡大する
- OTL 対応により、将来的に加盟店は Flow 対応 PSP を通じて複数の決済レール（ステーブルコイン・カード・CBDC）を統一インターフェースで管理できる可能性がある

### プロダクト視点
- Fireblocks は今年 5 月に Agentic Payments Suite（x402 対応）を発表済み。Flow は「エージェントが支払う」側（Agentic Payments Suite）と「PSP が受け取る」側を繋ぐ最後のピースとして機能しうる
- OTL の「ID・メッセージ・コーディネーション」レイヤーは、エージェント決済における「誰が誰に何を支払ったか」のトレーサビリティ確保に使える可能性がある

### 規制 / リスク視点
- OTL の「コンプライアンス対応オンチェーン取引」設計は GENIUS Act 施行後の PPSI 要件（AML・KYC）に対応した設計を目指していると推測される。詳細仕様の確認が必要

## 我々への示唆
- いま検討すべきこと:
  - Fireblocks Agentic Payments Suite（既存ノート参照）と Flow の統合設計——エージェントが x402 で支払い、受け取り側 PSP が Flow で処理するエンドツーエンドフローの技術仕様を確認する
  - OTL への参加コスト・要件の調査——自社製品またはパートナー PSP が OTL に参加することで得られるメリットを評価
- 後で深掘りすべきこと:
  - Flutterwave 経由のアフリカ展開での実採用指標（初回開示タイミング）
  - Mastercard BVNK との競合設計——BVNK も PSP 向けデジタルアセット決済インフラ。Flow と BVNK の差別化要因を確認
- 今は優先度が低いこと:
  - Flow の詳細な手数料体系（初期フェーズでは非公開の可能性）

## ありそうな示唆
- Fireblocks が Agentic Payments Suite（エージェント支払い側）と Flow（PSP 受け取り側）を両方持つことは、Fireblocks が agentic commerce の「中間インフラ」としてのポジションを確立しようとしていることを示す

## 推測 / 監視ポイント
- OTL が Visa TAP / AP2 / Mastercard Verifiable Intent と統合されれば、Fireblocks Flow が agentic commerce の「認証 → 支払い → 受け取り → 決済」の全フローを担うインフラになりうる
- Flutterwave 経由のアフリカ展開は、エージェント決済が先進国だけでなく新興市場で実需として機能するかの試金石になる

## 未解決の論点
- Flow は AI エージェント（x402 / MPP 経由）からの支払いを受け取る設計にも対応しているか？（技術仕様未確認）
- OTL への参加に必要な技術・法務要件は何か？
- Fireblocks Flow の決済完結時間と手数料の仕様は？

## 参考リンク
- 一次情報:
  - [PR Newswire（2026-06-02）](https://www.prnewswire.com/news-releases/fireblocks-launches-flow-stablecoin-acceptance-for-psps-and-fintechs-302788865.html)
  - [Fireblocks Blog「Introducing Fireblocks Flow」](https://www.fireblocks.com/blog/introducing-fireblocks-flow)
- 補足情報:
  - [Fintech Singapore（2026-06-02）](https://fintechnews.sg/132560/digitalassets/fireblocks-flow/)
  - [TipRanks（2026-06-02）](https://www.tipranks.com/news/private-companies/fireblocks-unveils-flow-to-power-stablecoin-acceptance-for-psps-and-fintechs)
  - [Fireblocks OTL ブログ](https://www.fireblocks.com/blog/otl-coordination-layer-onchain)
  - [関連ノート：Fireblocks Agentic Payments Suite（2026-05-20）](2026-05-20_Fireblocks_agentic-payments-suite-x402-foundation.md)

## 重要度
- Medium

## 確からしさ
- High（PR Newswire 公式プレスリリースおよび Fireblocks ブログによる公式発表）
