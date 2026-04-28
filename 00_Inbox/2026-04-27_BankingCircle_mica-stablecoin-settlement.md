---
title: "Banking Circle、MiCA CASP ライセンス取得後にステーブルコイン決済清算サービスをローンチ"
date: 2026-04-27
source: "Banking Circle / CoinTelegraph"
source_url: https://cointelegraph.com/news/mica-licensed-banking-circle-launches-stablecoin-settlement-europe
entity: BankingCircle
category: payments
tags:
  - stablecoin
  - regulation
  - payments
  - psp
summary: "ルクセンブルク拠点の Banking Circle が MiCA に基づく CASP（暗号資産サービスプロバイダー）ライセンスを 4 月 15 日に取得したことを受け、4 月 27 日にステーブルコイン決済清算サービスをローンチ。USDC・USDG（Paxos 発行）・EURI（自社発行 EUR ステーブルコイン）の 3 銘柄を中心に、法定通貨とステーブルコイン間の相互変換を銀行のコアインフラから直接提供する。PSP・マーケットプレイスが主な対象顧客。"
implications: "EU 圏で MiCA 準拠のステーブルコイン決済インフラを銀行ライセンス上で提供する事例が登場。規制済み銀行インフラとブロックチェーン決済の統合モデルとして参照点になりうる。"
follow_up: "Banking Circle の EURI 保有要件・MiCA 適合コスト・他欧州銀行への拡大動向"
---

## 概要

ルクセンブルクを本拠地とする決済専門銀行 **Banking Circle** が、ルクセンブルク金融監督局 CSSF（Commission de Surveillance du Secteur Financier）から **MiCA に基づく CASP ライセンスを 2026 年 4 月 15 日に取得**し、それに続いて **4 月 27 日にステーブルコイン決済清算サービスを正式ローンチ**した。

## 何が起きたか

- **対応ステーブルコイン**: USDC（Circle 発行）、USDG（Paxos 発行、Global Dollar Network）、EURI（Banking Circle が自行として発行する MiCA 準拠 EUR ステーブルコイン）の 3 銘柄
- **サービス内容**: Banking Circle のコアインフラ（トレジャリーシステム）から直接、法定通貨→ステーブルコインおよびステーブルコイン→法定通貨の変換と決済清算を提供。既存の銀行口座やトレジャリー機能と統合済み
- **ターゲット顧客**: PSP（決済サービスプロバイダー）、マーケットプレイス、法人顧客。ブロックチェーンの 24/7 稼働性と銀行水準のコンプライアンス・リスク管理を組み合わせた「規制準拠かつ即時決済」を訴求
- **市場規模（同社引用）**: ステーブルコイン市場は約 2,500 億ユーロ、決済関連取引は年間約 3,300 億ユーロと推計
- **CEO Laust Bertelsen コメント**: 「ステーブルコインはニッチなイノベーションから、クロスボーダー決済・トレジャリー管理・金融包摂のコアインフラへと急速に進化した。当行の CASP ライセンスは Banking Circle 自身にとっても、決済エコシステム全体にとっても重要なマイルストーン」

## なぜ重要か

### 決済事業者視点
- EU 域内で**MiCA 準拠＋銀行ライセンス**のダブルライセンスを持つ事業者がステーブルコイン決済を提供するケースが初めて登場。PSP が自社でブロックチェーン対応を開発せずにステーブルコイン決済を使えるインフラが整いつつある
- USDG（Paxos/Global Dollar Network：Mastercard・Robinhood・Kraken・DBS 参加）も対応することで、主要ステーブルコイン規格をひとつの銀行インフラで処理できる

### 加盟店視点
- PSP を経由して Banking Circle に接続する加盟店は、追加開発なしにステーブルコイン決済とフィアット決済を同一の清算フローで扱える可能性が生まれる

### プロダクト視点
- EURI（EUR 担保）の存在は、EUR 建てステーブルコイン決済を規制準拠で行えるインフラが EU 内に整いつつあることを示す。将来的に EUR 建てステーブルコインペイメントが B2B 送金で普及するシナリオを前倒しする可能性
- Banking Circle は既存の PSP 向けバンキング・サービスを強みに持つため、顧客 PSP のステーブルコイン対応を一括支援するモデルへの拡張が考えられる

### 規制 / リスク視点
- MiCA CASP ライセンスの取得は、欧州でのステーブルコインサービスに必要な規制要件を Banking Circle が充足したことを意味する。他の欧州 PSP が同社のインフラを活用して「MiCA 対応を外注」する動きが加速する可能性
- 日本規制との比較：MiCA の CASP フレームワークと日本の資金決済法上の暗号資産交換業との整合性整理が今後の課題

## 我々への示唆
- いま検討すべきこと:
  - Banking Circle の決済インフラ API 仕様と、Circle CPN・Bridge（Stripe 傘下）との比較評価（欧州展開を検討する場合の MiCA 対応コスト観点）
  - EURI（EUR ステーブルコイン）対応のロードマップが自社プロダクトに与えるインパクト評価
- 後で深掘りすべきこと:
  - Banking Circle の USDG 対応の詳細（Global Dollar Network 参加企業との相互接続性）
  - 同社の EURI 準備資産構成と MiCA の保有要件への適合状況
- 今は優先度が低いこと:
  - 日本・アジアへの直接的な事業展開（現時点では EU/ルクセンブルク中心）

## 未解決の論点
- Banking Circle の EURI の具体的な準備資産構成・発行残高・流通状況は未確認
- Banking Circle が採用した USDG（Paxos の Global Dollar Network）への参加経緯・条件は未公表
- ステーブルコイン決済のオンボーディング期間・KYB・AML フローの詳細は未公開

## 参考リンク
- 一次情報:
  - [Banking Circle 公式 Finextra 発表（2026-04-27）](https://www.finextra.com/pressarticle/109595/banking-circle-launches-stablecoin-clearing-service)
  - [CoinTelegraph 報道（2026-04-27）](https://cointelegraph.com/news/mica-licensed-banking-circle-launches-stablecoin-settlement-europe)
- 補足情報:
  - [FF News（詳細）](https://ffnews.com/newsarticle/cryptocurrency/banking-circle-introduces-stablecoin-settlement-services-following-casp-license-approval/)
  - [PYMNTS.com 報道](https://www.pymnts.com/blockchain/2026/banking-circle-unveils-stablecoin-settlement-after-landing-crypto-license/)
  - [Crypto Economy（Paxos USDG 背景）](https://crypto-economy.com/banking-circle-launches-regulated-stablecoin-settlement-after-securing-luxembourg-casp-license/)

## 重要度
- High

## 確からしさ
- High
