---
title: "Meta、Stripe 経由で USDC クリエイター報酬支払いを開始（コロンビア・フィリピン先行）"
date: 2026-04-29
source: "Meta / CoinDesk / Fortune / Decrypt"
source_url: https://www.coindesk.com/business/2026/04/29/tech-giant-meta-starts-paying-some-creators-in-stablecoin-with-stripe-s-support
entity: Meta
category: payments
tags:
  - stablecoin
  - payments
  - wallet
  - merchant
summary: "Meta が 2026 年 4 月 29 日、Stripe の Link ウォレットを活用してクリエイターへの報酬支払いを USDC（Solana・Polygon）で開始。先行市場はコロンビアとフィリピン。自社ステーブルコイン発行は行わず Circle の USDC を採用。2022 年に頓挫した Libra/Diem 以来初の本格的なステーブルコイン展開。"
implications: "30 億超ユーザーを持つプラットフォームがステーブルコインを実用化したことで、従来型の銀行送金によるクリエイターエコノミーへの侵食が本格的に始まる。Stripe が Meta という大型顧客を取り込んだことで、ステーブルコイン決済インフラとしての地位をさらに強化。"
follow_up: "グローバル展開スケジュール、クリエイター受取ウォレットの分布、オフランプ利用率、Stripe Link の PSP ロール詳細"
---

## 概要

Meta は 2026 年 4 月 29 日、Facebook 等のプラットフォーム上でクリエイター報酬を **USDC ステーブルコイン**（Circle 発行）で受け取れる新機能を正式ローンチした。支払いインフラには **Stripe の Link ウォレット**を採用し、**Solana および Polygon** ブロックチェーンを決済レールとして使用する。初期対象市場は**コロンビアとフィリピン**に限定されており、2026 年中にグローバル展開を予定している。

## 何が起きたか

- **ローンチ日**: 2026 年 4 月 29 日（Meta 公式ページにて告知）
- **対象市場（初期）**: コロンビア・フィリピン（ドル建て報酬を受け取るクリエイターが多く、銀行送金手数料が高いため選定）
- **決済レール**: Solana および Polygon（クリエイターが選択可能）
- **利用ステーブルコイン**: USDC（Circle 発行）。Meta は自社ステーブルコインを発行しない
- **インフラパートナー**: Stripe（Link ウォレット）が技術・コンプライアンスを担当。クリエイターは Link ウォレットに外部ウォレットアドレスを登録して受取
- **対応ウォレット**: MetaMask、Phantom、Binance ウォレット、Bybit、Kraken、Exodus、Brave Wallet、Bitso、GCash（GCrypto）、Coins.ph など 10 種類以上
- **法定通貨への換金**: Meta 側では提供しない。クリエイターが自身で取引所等でフィアットに換金する必要がある
- **税務**: クリエイターは通常の Meta 税務フォーム（Form 1099 / 1042 等）を受け取る。デジタルアセット部分については Stripe が追加の暗号資産税務書類を発行する可能性がある
- **背景**: Meta は 2019 年に Libra（後の Diem）を発表したが、規制当局・議会の強い反発を受け 2022 年にプロジェクトを解散。今回は自社発行ではなく既存の規制準拠 USDC を活用することで規制リスクを回避

## なぜ重要か

### 決済事業者視点
- Meta（Facebook・Instagram）の巨大なクリエイターエコノミー（世界数十億人のアクティブユーザー）がステーブルコイン決済の実証フィールドになった。Stripe が大手プラットフォームのステーブルコイン支払いインフラを担う「B2B ステーブルコイン PSP」としての地位を固めつつある
- 既存の国際電信送金（SWIFT）や現地送金ネットワークが代替されるケースが実際に出始めている

### 加盟店視点
- クリエイターが「フィアット報酬→ステーブルコイン受取」に慣れることで、将来的にステーブルコインを日常的な支払い手段として受容する消費者層が形成される

### プロダクト視点
- Stripe Link という「ウォレット兼 KYC インフラ」が USDC の配布チャネルとして機能。ウォレット取得→ステーブルコイン保有→消費という消費者ファネルが構築される
- 対応ウォレットに GCash GCrypto・Coins.ph が含まれており、東南アジア・フィリピン向けのオンランプとして機能する可能性

### 規制 / リスク視点
- GENIUS Act 成立後（2025 年 7 月）の環境において、Meta は自社発行ではなく USDC を採用することで規制コスト・制度リスクを最小化。この「既存規制準拠ステーブルコインを活用する」モデルが大手プラットフォームの標準アプローチになる可能性がある
- コロンビア・フィリピンという初期市場の選定は、両国のデジタル金融規制が比較的受容的であること、かつ未銀行化人口の多さを反映している

## 我々への示唆
- いま検討すべきこと:
  - Stripe Link の B2B ステーブルコイン支払いインフラが、自社の決済フローに接続可能かを評価する（Meta レベルの送金先企業向けのインフラ選定観点）
  - コロンビア・フィリピン等の新興国展開で、現地クリエイター・フリーランサーへのステーブルコイン支払いニーズが自社サービスに存在するか検討
- 後で深掘りすべきこと:
  - Meta の 2026 年グローバル展開スケジュール（特に東南アジア・ラテンアメリカの次期対象国）
  - Stripe Link のオフランプ連携状況（Coins.ph・GCash GCrypto を通じた現地換金パス）
  - クリエイター実際の採用率・USDC 保有継続率（将来消費につながるか）
- 今は優先度が低いこと:
  - 日本国内向けの即時応用（GENIUS Act・フィリピン・コロンビア規制環境との差異が大きい）

## 未解決の論点
- Meta のグローバル展開予定国の具体的な名称・時期は未公表
- Stripe Link が担う KYC・AML フローの詳細（Meta 側・Stripe 側の責任分担）は未公開
- フィリピン・コロンビアのクリエイター向けオフランプ（USDC→現地通貨）の手数料・速度・実用性は検証待ち

## 参考リンク
- 一次情報:
  - [CoinDesk 報道（2026-04-29）](https://www.coindesk.com/business/2026/04/29/tech-giant-meta-starts-paying-some-creators-in-stablecoin-with-stripe-s-support)
  - [Fortune 報道（2026-04-29）](https://fortune.com/2026/04/29/meta-stablecoins-crypto-usdc-polygon-solana/)
- 補足情報:
  - [Decrypt（詳細）](https://decrypt.co/366087/meta-launches-usdc-stablecoin-creator-payouts-on-solana-and-polygon-via-stripe)
  - [Bitcoin.com News（フィリピン・コロンビア詳細）](https://news.bitcoin.com/meta-launches-usdc-stablecoin-payouts-for-creators-in-colombia-and-the-philippines/)
  - [CryptoTimes（2026-04-30）](https://www.cryptotimes.io/2026/04/30/meta-introduces-stablecoin-payments-for-creators-in-pilot-markets/)

## 重要度
- High

## 確からしさ
- High
