---
title: "Adyen、エンタープライズ向けエージェントコマース API スイート「Adyen Agentic」を発表"
date: 2026-06-16
source: PR Newswire / Adyen
source_url: https://www.prnewswire.com/news-releases/adyen-announces-adyen-agentic-as-the-universal-translator-for-the-next-era-of-commerce-302801269.html
entity: Adyen
category: merchant-PSP-readiness
primary_category: merchant-PSP-readiness
article_published_date: 2026-06-16
underlying_event_date: 2026-06-16
primary_source_date: 2026-06-16
tags:
  - agentic-commerce
  - merchant-readiness
  - PSP
  - payment-infrastructure
  - API
summary: "Adyen が「Adyen Agentic」を発表。Agentic Feed・Agentic Cart・Agentic Payments の 3 層モジュール API で、エンタープライズ加盟店が既存システムを再構築せずに会話型 AI プラットフォーム上で販売できるインフラを提供。Amex・Mastercard・Salesforce・Visa をエコシステムパートナーに迎え、米国でリミテッドアベイラビリティにて開始。"
implications: "グローバル Top-5 PSP の Adyen がエージェントコマース専用インフラを本番化したことで、大手加盟店の L2（PSP 経由）エージェント対応が加速する可能性。x402 / MPP ベースの L3 ネイティブ対応とは補完関係。"
importance: High
confidence: High
follow_up: "グローバル展開タイムライン、Agentic Payments レイヤーの stablecoin 対応有無、x402 / MPP との相互運用性確認"
---

## 概要

Adyen は 2026-06-16 に「Adyen Agentic」を発表。3 層のモジュール API（Agentic Feed / Agentic Cart / Agentic Payments）で構成されたエンタープライズ向けエージェントコマースインフラ。既存の EC プラットフォームや決済フローを再構築せずに、会話型 AI プラットフォームを販売チャネルとして追加できる設計。

## 何が起きたか

- Adyen が「Adyen Agentic」を発表。公式プレスリリースおよび [adyen.com/agentic-commerce](https://www.adyen.com/agentic-commerce) で詳細を公開
- 3 層構成：
  - **Agentic Feed**：商品カタログ・価格・在庫のリアルタイムデータを AI エージェントに配信
  - **Agentic Cart**：既存のチェックアウト・税務・フルフィルメント・OMS を会話型コマースに接続
  - **Agentic Payments**：エージェント起点トランザクションの認証・トークンポータビリティ・リスク管理を担当
- エコシステムパートナー：American Express、Mastercard、Salesforce、Visa（ネットワーク・CRM 連携）
- エンタープライズ加盟店：ESW、Scheels、Sézane、SharkNinja が早期参加
- 米国のエンタープライズ加盟店向けにリミテッドアベイラビリティで開始、グローバル展開予定

## 確認された事実

- Adyen Agentic は公式プレスリリース（PR Newswire 2026-06-16）で発表
- 3 層モジュール構成が明示され、各層の機能が定義されている
- 米国エンタープライズ加盟店向けリミテッドアベイラビリティ開始（GA タイムライン未公表）
- Adyen の既存トークン化・認証・不正防止インフラの上に構築

## なぜ重要か

### 決済事業者視点

- 世界最大級の PSP（Adyen）がエージェントコマース専用製品を本番化。Stripe MPP・Visa Intelligent Commerce・Mastercard AP4M に次ぐ大型 PSP 参入
- Adyen 加盟店網（グローバルエンタープライズ中心）がエージェント決済対応 L2 に移行する経路が整備された

### 加盟店視点

- 既存の Adyen 統合を大きく変えずにエージェントコマースチャネルを追加できる。ROI 計算が比較的容易
- Agentic Payments レイヤーでエージェント固有のリスク管理（認証・トークンポータビリティ）を Adyen が吸収することで、加盟店のエージェント詐欺対策コストが下がる可能性

### プロダクト視点

- Agentic Feed（カタログ配信）+ Agentic Cart（チェックアウト接続）+ Agentic Payments（決済実行）の垂直統合は、エージェント向け UCP（Universal Cart Protocol）の Adyen 版実装と見ることができる
- Mastercard と Visa が両方エコシステムパートナーに入っており、カードネットワーク側との連携は担保されている

### 規制 / リスク視点

- Adyen は PCI DSS、3DS、MiCA 対応を既存インフラで担保済み。EU 市場向けエージェント決済の法的リスクが比較的低い経路
- stablecoin 対応の明示なし。MiCA 7/1 以降の EU 向け USDC/EURC エージェント決済が Adyen Agentic でサポートされるかは未確認

## 我々への示唆

- いま検討すべきこと:
  - 自社プロダクトの Adyen 統合ロードマップに「Adyen Agentic」早期アクセス申請を追加するか検討
  - Agentic Payments の stablecoin 対応確認（MiCA 7/1 前の EU 向け設計に影響）
- 後で深掘りすべきこと:
  - x402 / MPP との相互運用性（Adyen Agentic は独自スタックか、既存プロトコルと連携するか）
  - GA タイムラインと対象地域（欧州・アジア展開スケジュール）
- 今は優先度が低いこと:
  - 個別の加盟店（ESW・SharkNinja 等）のエージェントコマース実装詳細

## ありそうな示唆

- Adyen Agentic の登場で、エンタープライズ加盟店の「エージェントコマース対応 PSP 選定」が本格化する可能性。Stripe MPP vs Adyen Agentic の比較検討が起きる
- Agentic Payments レイヤーの stablecoin 対応が追加されれば、Circle CPN や Fireblocks Flow との統合経路が生まれる

## 推測 / 監視ポイント

- Adyen Agentic の stablecoin 決済対応（Agentic Payments レイヤーへの USDC/EURC 追加）
- GA への移行タイミングと欧州・アジア展開
- Adyen が x402 Foundation や AP2 エコシステムに参加するかどうか

## 未解決の論点

- Agentic Payments はカード決済のみか、stablecoin レール対応を含むか
- Adyen Agentic と Stripe MPP は加盟店側で競合するか、PSP として棲み分けが生まれるか

## 参考リンク

- 一次情報: [Adyen Agentic Press Release（2026-06-16）](https://www.prnewswire.com/news-releases/adyen-announces-adyen-agentic-as-the-universal-translator-for-the-next-era-of-commerce-302801269.html)
- 補足情報: [Adyen Agentic Commerce ページ](https://www.adyen.com/agentic-commerce)
- 補足情報: [Adyen Agentic 解説 - Gurufocus（2026-06-16）](https://www.gurufocus.com/news/8918992/adyen-adyey-unveils-new-api-suite-to-enhance-conversational-commerce)

## 重要度

- High

## 確からしさ

- High（公式プレスリリース・公式 Web ページで確認）
