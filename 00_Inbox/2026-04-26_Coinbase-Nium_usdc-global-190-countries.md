---
title: "Coinbase × Nium、190 か国以上で USDC クロスボーダー決済レールを統合"
date: 2026-04-26
source: "Nium / CoinDesk / TNGlobal / American Banker"
source_url: https://technode.global/2026/04/23/nium-coinbase-team-up-for-global-stablecoin-payments-and-settlement/
entity: Coinbase
category: payments
tags:
  - stablecoin
  - payments
  - psp
  - wallet
summary: "グローバル決済インフラ企業 Nium が Coinbase のステーブルコインインフラを統合し、190 か国以上でクライアント（銀行・フィンテック・企業）が USDC を活用したクロスボーダー決済と法定通貨払い出しを実行できる体制を整えた。Brian Armstrong が 2026 年 4 月 26 日に X で発表。"
implications: "Nium という B2B ペイメントハブが Coinbase を USDC 流動性・カストディのバックボーンとして採用したことで、銀行・PSP が Coinbase インフラを間接的に利用するルートが実質的に完成。Coinbase のステーブルコイン事業が B2B ペイメントインフラとして機能し始めた。"
follow_up: "Nium クライアントの USDC 採用状況・実績、Coinbase のカストディ体制詳細、日本での Nium サービス展開との交点"
---

## 概要

グローバル B2B 決済インフラ企業 **Nium** が、Coinbase のステーブルコインインフラ（USDC 発行・カストディ・流動性・ウォレット）を統合し、Nium のクライアントである銀行、フィンテック、企業が **190 か国以上**でオンチェーン USDC と法定通貨払い出しをシームレスに利用できる体制を整えた。Coinbase CEO Brian Armstrong が **2026 年 4 月 26 日**に X でこの提携を発表。

## 何が起きたか

- **発表日**: Brian Armstrong の X 投稿（2026 年 4 月 26 日）、TNGlobal 報道（2026 年 4 月 23 日）
- **統合内容**: Nium が Coinbase を USDC ステーブルコイン決済の以下のコンポーネントとして採用：
  - ステーブルコインインフラ（USDC 発行・流動性）
  - ウォレット（オンチェーン USDC 保管・送受信）
  - 規制準拠カストディ
  - フィアット払い出しネットワーク（190 か国超）
- **対象顧客**: Nium のクライアント（銀行・フィンテック・大企業など）
- **用途**: クロスボーダー決済、オンチェーン USDC → フィアット払い出し、セトルメント効率化

### Nium について
- 企業向けグローバル決済インフラプロバイダー（シンガポール本拠、ユニコーン企業）
- 130 か国以上に銀行口座開設・ローカル決済ネットワーク接続・FX・カード発行の API を提供
- 世界 500 以上の銀行・PSP・企業クライアント

## なぜ重要か

### 決済事業者視点
- Nium のクライアントである銀行・PSP が、Coinbase のインフラを間接的に活用して USDC クロスボーダー決済を提供できるようになる。自社でブロックチェーンノードやカストディ体制を構築せずに、既存の Nium API 経由でステーブルコイン決済を使えることを意味する
- これにより「Coinbase インフラ → Nium API → 銀行・PSP → 法人・消費者」というスタックが形成され、Coinbase のステーブルコイン事業の B2B 分散チャネルが実質的に完成

### 加盟店視点
- Nium を使う企業顧客は、クロスボーダー支払いで USDC レールを利用しながらも受取側はフィアットで受け取れる。加盟店側のステーブルコイン対応を不要にするフローが整う

### プロダクト視点
- Coinbase が USDC の「流通インフラ」として機能することで、Coinbase の収益基盤がトレーディング（手数料）から B2B インフラフィー（カストディ・流動性供給）へ多様化する流れが鮮明になった
- Circle CPN（Circle Payments Network）との競合関係：Circle が直接 PSP をオンボードする CPN モデルと、Coinbase が Nium のような集約者経由で間接展開するモデルが並行して走ることになる

### 規制 / リスク視点
- Coinbase は信託会社チャーター（2026 年 4 月取得）を持ち、GENIUS Act 準拠のカストディ事業者として機能。Nium クライアントの規制リスクが Coinbase のライセンス体制によってカバーされる構造
- 190 か国展開は各国の規制に対応した Nium のローカル金融ライセンスを活用したもの。ステーブルコイン固有の規制（KYT・AML）は Coinbase 側で実装

## 我々への示唆
- いま検討すべきこと:
  - Nium の API で利用可能な USDC 決済機能（エンドポイント・対応国・レート）を評価し、自社のクロスボーダー決済スタックと比較
  - Circle CPN（既報：2026-04-08_Circle_cpn-managed-payments.md）と Coinbase×Nium の機能・価格・対応国比較を実施
- 後で深掘りすべきこと:
  - Nium 経由での Coinbase カストディ手数料体系（フィアット払い出しコスト）
  - 日本・アジア市場での Nium クライアント構成（日本向け展開との整合性）
- 今は優先度が低いこと:
  - Coinbase の個別 L1 技術（Base）の詳細（Nium 統合とは別レイヤー）

## 未解決の論点
- Nium クライアントがすでに USDC 統合を有効化した実績（国・取引量）は未公表
- Coinbase のカストディフィー・流動性供給モデルの詳細条件は非公開
- 日本拠点企業が Nium を経由して Coinbase USDC 決済を利用する場合の規制上の取り扱いは未確認

## 参考リンク
- 一次情報:
  - [TNGlobal 報道（2026-04-23）](https://technode.global/2026/04/23/nium-coinbase-team-up-for-global-stablecoin-payments-and-settlement/)
  - [BeInCrypto（190 か国詳細）](https://beincrypto.com/coinbase-nium-usdc-payments-190-countries/)
- 補足情報:
  - [American Banker（Coinbase 信託チャーター文脈）](https://www.americanbanker.com/payments/news/coinbase-partners-with-nium-to-boost-stablecoins)
  - [Simply Wall St（Coinbase グローバル展開）](https://simplywall.st/stocks/us/diversified-financials/nasdaq-coin/coinbase-global/news/how-investors-may-respond-to-coinbase-global-coin-powering-n)

## 重要度
- Medium

## 確からしさ
- High
