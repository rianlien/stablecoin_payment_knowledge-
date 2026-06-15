---
title: "UCP（Universal Commerce Protocol）"
type: protocol
updated: 2026-06-15
category: agentic-commerce
status: live
tags:
  - agentic-commerce
  - payment-protocol
  - merchant-readiness
  - agent-identity
  - Google
---

# UCP（Universal Commerce Protocol）

Google が主導し、Shopify・Stripe・Salesforce らが実装パートナーとして参加するオープンなエージェント商取引プロトコル。AI エージェントが任意の加盟店に接続し、商品発見・カタログ取得・カート構築・チェックアウトを一気通貫で実行するための「コマースの共通言語」として設計されている。2026 年 4 月時点で Amazon・Meta・Microsoft・Salesforce・Stripe が Tech Council に加わり、Shopify が全加盟店を自動オプトインさせたことで、エージェント商取引インフラとして最大規模のリーチを持つ標準に育った。

この vault では、UCP を「AP2（Agent Payments Protocol）と対をなす加盟店側エージェント接続層」として追う。AP2 が認証・支払い委任を担うのに対し、UCP はカタログ・ID 連携・カート操作を担う役割分担と捉える。

---

## プロトコルの概要

### 何を解決するか

加盟店が AI エージェントの購買意図を受け取るために必要なインターフェースが標準化されていなかった問題を解決する。2026 年 5 月時点の調査（PayPal Agentic Commerce Pulse Report）では、加盟店の 95% が AI エージェントトラフィックを確認しているにもかかわらず、機械読取可能なカタログを整備している加盟店は 20% にとどまっていた。UCP はこのギャップを埋める供給側インフラとして機能する。

### 主要コンポーネント（2026-05 時点）

| コンポーネント | 内容 |
|---|---|
| **Catalog API** | エージェントが加盟店のリアルタイム商品情報（バリアント・在庫・価格）を取得するエンドポイント |
| **Identity Linking** | AI エージェントがユーザーの既存会員 ID・ロイヤルティ特典・会員価格を引き継ぐ仕組み |
| **マルチアイテムカート** | エージェントが複数商品を一セッションで保存・処理できるカート操作 API |
| **Checkout** | エージェント起点のチェックアウトフロー（AP2 の Spending Mandate と連携） |

### AP2 との役割分担

```
[ユーザー / エージェント]
       ↓ 委任・認証（AP2 / FIDO Alliance）
[Identity Linking → Catalog API → Cart → Checkout]
       ↑ ここが UCP の担当レイヤー
       ↓ 支払い実行（AP2 Payment Mandate → x402 / Stripe MPP 等）
[決済レール]
```

---

## 展開状況

### ローンチパートナー加盟店（2026-05 時点）

Nike・Sephora・Target・Ulta Beauty・Walmart・Wayfair・Shopify 加盟店（Fenty・Steve Madden 等）

### UCP 実装プラットフォームパートナー

Commerce Inc・Salesforce・Stripe（近日対応予定、2026-05-28 発表）

### Tech Council 参加（2026 年 4 月時点）

Shopify・Google の創設メンバーに加え、Amazon・Meta・Microsoft・Salesforce・Stripe が参加。

### 地理展開

- 米国：2026 年夏に Search + Gemini app でロールアウト
- Canada・Australia：拡大済み（2026-05-28 発表）
- UK：後日対応予定

### カテゴリ拡張（予定）

- ホテル予約・ローカルフード配達への拡張を予定

---

## 主要イベント年表

| 日付 | イベント |
|---|---|
| 2026-04-03 | Google が AP2（Agent Payments Protocol）を発表。UCP はその頃から AP2 と対をなすプロトコルとして設計 |
| 2026-04-28 | AP2 v0.2 を FIDO Alliance に寄贈。Human Not Present（人不在決済）機能追加 |
| 2026-05-10 | Consensus Miami で PayPal・Google Cloud が「エージェント商取引はクリプトレールで動く」と表明 |
| 2026-05-19 | Google I/O 2026 で Universal Cart を発表。AP2 FIDO Alliance 移管を公式アナウンス |
| 2026-05-28 | Google Marketing Live 2026 で UCP 新機能 3 件（Identity Linking・Catalog API・マルチアイテムカート）と国際展開を発表 |
| 2026-05-29 | Shopify が UCP Catalog を全開発者に開放。数百万加盟店・数十億商品が UCP 経由でアクセス可能に |

---

## 関連ニュース

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-28 | [[2026-04-28_Google_ap2-fido-alliance]] | AP2 v0.2 FIDO Alliance 寄贈・Human Not Present 決済追加 |
| 2026-05-10 | [[2026-05-10_PayPal-Google_consensus-miami-agentic-commerce]] | Consensus Miami でのクリプトレール不可避論・加盟店カタログ整備の遅れ（95% vs 20%）を定量化 |
| 2026-05-19 | [[2026-05-19_Google_universal-cart-ap2-io2026]] | Google I/O 2026 での Universal Cart 発表・AP2 FIDO Alliance 移管公式アナウンス |
| 2026-05-28 | [[2026-05-28_Google_ucp-update-identity-linking-catalog-marketing-live]] | Google Marketing Live 2026：UCP 新機能 3 件・Stripe / Salesforce パートナー参加・国際展開 |
| 2026-05-29 | [[2026-05-29_Shopify_ucp-catalog-developer-agentic-commerce]] | Shopify が UCP Catalog を全開発者に開放、全加盟店自動オプトイン |

---

## 現状の論点

- **AP2 との役割境界**：UCP がカタログ・カート・ID 連携を担い、AP2 が認証・支払い委任を担うとされているが、実装レベルの役割分担仕様（どのエンドポイントがどちらの責務か）は公開仕様から読み切れていない
- **加盟店の自動オプトイン問題**：Shopify 加盟店は設定なしに UCP Catalog に掲載される。エージェントからの注文に対する返品・詐欺対応フローが整備されていない加盟店でトラブルが発生するリスクがある
- **Identity Linking の認証設計**：エージェントがユーザーの既存会員 ID を引き継ぐ際の OAuth スコープ・同意取得フローが未公開。GDPR・改正 PSD2 との整合確認が必要
- **支払い方法の選択肢**：UCP 経由の注文が Stripe MPP（カード）か x402（USDC）か選択可能か、あるいは一方に固定されるかは未確認
- **非 Shopify 加盟店の対応遅れ**：WooCommerce・Magento・BigCommerce 等の UCP 対応状況は未公開。Shopify への AI トラフィック集中が他プラットフォームとの格差を生む可能性

---

## 監視ポイント

- Stripe の UCP 実装 API スペックの公開（2026 年夏以降と想定）
- Shopify UCP 経由の AI エージェント購買件数の初回開示（2026 年 Q2/Q3 決算）
- Google Merchant Center 新オンボーディングフローの展開（数ヶ月内と告知）
- AP2 仕様（GitHub: google-agentic-commerce/AP2）の UCP 新機能対応アップデートの有無
- UK 展開のタイムライン確定
- UCP 注文に対するチャージバック・詐欺事例の発生と業界対応指針

---

## 参考リンク

- [Google Blog — Universal Cart 発表（2026-05-19）](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/)
- [Google Blog — Google Marketing Live 2026 UCP 新機能（2026-05-28）](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/)
- [Google Blog — Agentic Commerce 小売・プラットフォーム向け（2026-05-28）](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/)
- [Shopify Newsroom — UCP Catalog 全開発者開放（2026-05-29）](https://www.shopify.com/news/ai-commerce-at-scale)
- [shopify.dev/agents — 開発者向けドキュメント](https://shopify.dev/docs/agents)
- [Search Engine Land — UCP 新機能報道（2026-05-28）](https://searchengineland.com/google-expands-universal-commerce-protocol-and-launches-new-agentic-shopping-tools-478113)

---

## 関連ページ

- [[2026-04-28_Google_ap2-fido-alliance]]（AP2 プロトコル本体）
- [[ERC-8183_Agentic-Commerce]]（Ethereum 上のエージェント間エスクロー標準）
