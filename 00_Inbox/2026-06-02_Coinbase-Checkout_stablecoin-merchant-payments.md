---
title: "Coinbase × Checkout.com、USDC/USDT 受け入れを 1,000 社超のエンタープライズ加盟店に展開"
date: 2026-06-02
source: CoinDesk / CryptoTimes / The Paypers
source_url: https://www.cryptotimes.io/2026/06/02/checkout-com-adds-usdc-usdt-payments-via-coinbase-service/
entity: Coinbase / Checkout.com
category: merchant-readiness
primary_category: merchant-readiness
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - merchant-readiness
  - stablecoin
  - USDC
  - Coinbase
  - PSP
summary: "Coinbase と Checkout.com が提携し、Checkout.com の 1,000 社超のエンタープライズ加盟店ネットワーク向けに USDC / USDT 決済を解禁。消費者は USDC または USDT で支払い、加盟店は USD で Checkout.com の既存レール経由に決済を受け取る設計。加盟店側は追加の暗号資産技術統合不要で即日対応可能。"
implications: "大手エンタープライズ PSP である Checkout.com が Coinbase の USDC 決済インフラを採用したことで、暗号資産の直接管理を避けながらステーブルコイン決済を受け入れられる加盟店が一気に拡大する。エージェントが USDC で支払いを行う場合、このルートが既存大手加盟店での受け入れ経路になりうる。"
importance: Medium
confidence: High
follow_up: "Checkout.com 加盟店 1,000 社のうちステーブルコイン決済を実際に有効化した比率（次の四半期報告）、USDC 取引量の推移、AI エージェント起点の決済がこのルートで処理される事例の有無"
---

## 概要
- Coinbase Payments と Checkout.com が提携し、Checkout.com のエンタープライズ加盟店 1,000 社超に USDC / USDT 決済を解禁（2026年6月2日）

## 何が起きたか
- Checkout.com は Coinbase Payments のインフラを統合し、USDC・USDT による消費者決済を受け入れ開始
- 決済フロー: 消費者が USDC または USDT で支払い → Coinbase Payments が受け取り → 加盟店は USD で Checkout.com 既存レール経由に精算
- 加盟店は別途の暗号資産対応・ウォレット管理が不要
- 対象: Checkout.com のエンタープライズ顧客ネットワーク（1,000 社超）
- Visa のオンチェーン分析によると、過去12ヶ月の調整済みステーブルコイン取引量は 10.2 兆ドル（前年比 63% 増）

## 確認された事実
- underlying_event_date: 2026-06-02
- 対応ステーブルコイン: USDC、USDT
- 精算通貨: USD（加盟店）
- 技術構成: Coinbase Payments + Checkout.com 既存ゲートウェイ
- ターゲット市場: カードアクセスが不均一な地域 / 現地通貨ボラティリティが高い市場

## なぜ重要か

### 決済事業者視点
- Checkout.com が Coinbase Payments を採用したことで、エンタープライズ PSP 経由のステーブルコイン決済経路が確立された
- 加盟店が暗号資産リスクを負わない設計（USD精算）は法人採用の最大障壁を除去する

### 加盟店視点
- 既存の Checkout.com 加盟店は追加統合ゼロで USDC/USDT 決済を有効化できる
- 特に新興市場・暗号資産ユーザー比率の高いプラットフォーム向けに即効性が高い

### プロダクト視点
- AI エージェントが USDC で決済する場合、Checkout.com 加盟店はこの統合により「エージェント支払い受け入れ可能」状態になりうる
- Coinbase Payments の「USDC 支払い → USD 精算」モデルは Circle CPN と類似した設計

### 規制 / リスク視点
- 加盟店が暗号資産を直接保有しない構造のため、GENIUS Act の「許可発行体」要件の対象外と見られる
- KYC/AML は Coinbase 側が担う設計（要確認）

## 我々への示唆
- いま検討すべきこと:
  - Checkout.com 経由の USDC 受け入れを Coinbase Payments API 経由で自社プロダクトに統合できるかどうかの技術確認
  - 自社クライアント（大手加盟店）が Checkout.com を利用している場合、ステーブルコイン対応を今すぐ推奨できる
- 後で深掘りすべきこと:
  - Coinbase Payments と Circle CPN の差分——どちらが「USDC 支払い → 既存通貨精算」において費用・速度で優位か
  - 加盟店がエージェント起点の USDC 決済を受け入れる場合、Checkout.com 経由かそれとも独自統合かの判断基準
- 今は優先度が低いこと:
  - USDT 対応（USDT は GENIUS Act 準拠ステーブルコインではないため規制環境次第で変化する可能性）

## ありそうな示唆
- Checkout.com（欧州・アジア中心）が USDC 決済を採用したことで、Stripe（MPP）と Coinbase（USDC/x402）の「エージェント決済インフラ競争」に Checkout.com が第三勢力として加わりつつある
- 「消費者がステーブルコインで払い、加盟店がフィアットで受け取る」設計はエージェント決済の初期普及モデルとして有力

## 推測 / 監視ポイント
- Checkout.com の加盟店 1,000 社のうち実際に USDC 決済を有効化する割合は不明——四半期開示を待つ
- Checkout.com はアジア・中東・アフリカ市場での存在感が強く、新興市場でのステーブルコイン利用事例が最初に出てくる可能性

## 未解決の論点
- AI エージェント起点の USDC 決済がこの経路でどのように処理されるか（認証・承認フロー）
- USDT は GENIUS Act 準拠ステーブルコインか——未確定

## 参考リンク
- 一次情報: CryptoTimes（2026-06-02）https://www.cryptotimes.io/2026/06/02/checkout-com-adds-usdc-usdt-payments-via-coinbase-service/
- 補足: news.bitcoin.com https://news.bitcoin.com/coinbase-enables-stablecoin-payments-across-checkout-coms-1000-merchant-network/
- 補足: The Paypers https://thepaypers.com/crypto-web3-and-cbdc/news/checkoutcom-and-coinbase-launch-stablecoin-payments-for-enterprise-merchants

## 重要度
- Medium

## 確からしさ
- High
