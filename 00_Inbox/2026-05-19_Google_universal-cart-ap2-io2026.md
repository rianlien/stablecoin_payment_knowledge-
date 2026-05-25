---
title: "Google I/O 2026：Universal Cart と AP2 FIDO Alliance 移管——Gemini × 加盟店横断カートでエージェント決済の消費者インターフェースが具体化"
date: 2026-05-22
source: Google Blog / TechCrunch / The Next Web
source_url: https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/
entity: Google
category: agentic-commerce / merchant-readiness / payment-protocol
primary_category: agentic-commerce
article_published_date: 2026-05-19
underlying_event_date: 2026-05-19
primary_source_date: 2026-05-19
tags:
  - agentic-commerce
  - AP2
  - merchant-readiness
  - payment-protocol
  - Google
summary: Google が I/O 2026（2026-05-19）で Universal Cart を発表。Search・Gemini・YouTube・Gmail を横断する AI ショッピングカートで、Gemini モデルが価格監視・在庫アラートを担う。AP2（Agent Payments Protocol）を FIDO Alliance に移管し、業界標準化を加速。Nike・Walmart・Target・Shopify 加盟店等がローンチパートナー。Gemini Spark が AP2 を統合する最初の Google 製品となる予定。
implications: Google が消費者 UI 側からエージェント決済の入口を掌握する動きを本格化。AP2 の FIDO Alliance 移管により x402 Foundation（Linux Foundation）と並ぶ第二の決済プロトコル標準化ボディが形成された。加盟店は x402・AP2・MPP の複数プロトコル対応を迫られる可能性がある。
importance: High
confidence: High
follow_up: "AP2 と x402 の技術的相互運用性確認・Gemini Spark AP2 統合時期・Universal Cart への Google Pay / ステーブルコイン支払い追加可否・AP2 v0.2.0「Human Not Present」payments の商用展開スケジュール"
---

## 概要
- Google が Google I/O 2026（2026-05-19）で Universal Cart と AP2 の FIDO Alliance 移管を発表
- **Universal Cart**：Google Search・Gemini・YouTube・Gmail を横断する AI ショッピングカート。加盟店横断で商品を追加でき、価格下落アラート・価格履歴インサイトを Gemini モデルが提供
- **AP2（Agent Payments Protocol）**：FIDO Alliance に移管し、業界共通標準として推進。x402 Foundation（Linux Foundation）と並ぶ標準化ボディが形成された
- ローンチパートナー：Nike・Sephora・Target・Ulta Beauty・Walmart・Wayfair・Shopify 加盟店（Fenty・Steve Madden 等）
- 米国での Universal Cart ロールアウトは 2026 年夏（Search + Gemini app）。YouTube・Gmail は追って順次対応。Canada・Australia にも拡大予定

## 何が起きたか
- Google I/O 2026（2026-05-19）で Universal Cart を発表。Gemini モデルが動作する加盟店横断ショッピングカートで、Search・Gemini でのブラウジング中に商品を追加し、YouTube 視聴中・Gmail 確認中にも連携する
- Gemini モデルが価格下落・在庫変動を監視し、AP2 に基づくエージェント起点の購入でカート内商品を自律購入可能に（ユーザー設定範囲内）
- AP2 v0.2.0（2026 年 4 月リリース）で「Human Not Present」payments を追加済み。エージェントが限定販売チケット等を発売瞬間に自律購入できる
- AP2 を FIDO Alliance に移管し、x402 Foundation（Linux Foundation）と並ぶ第二の業界標準化ボディが形成された
- Google 製品への AP2 統合を今後数カ月で開始。Gemini Spark が最初の統合製品

## 確認された事実
- 発表日：2026-05-19（Google I/O 2026）
- Universal Cart ローンチパートナー（明示）：Nike・Sephora・Target・Ulta Beauty・Walmart・Wayfair・Shopify 加盟店（Fenty・Steve Madden 等）
- AP2 FIDO Alliance 移管：完了（I/O 2026 前後）
- AP2 v0.2.0「Human Not Present」payments：2026 年 4 月リリース済み
- Universal Cart 米国ロールアウト：2026 年夏（Search + Gemini app）。YouTube・Gmail は追って
- 国際展開：Canada・Australia（UK は後日）
- UCP（Universal Checkout Protocol）も拡張：ホテル予約・フードデリバリー・YouTube 対応を予定

## なぜ重要か

### 決済事業者視点
- Google の Universal Cart が消費者の「支払い起点」を Google エコシステムに統合しようとしている。PSP がこれまで「加盟店のチェックアウト画面」を起点に設計してきた構造が変わり、エージェント経由の購入では Google / Gemini が起点になる可能性がある。PSP は AP2 との統合対応が必要になりうる
- AP2 が FIDO Alliance 標準になる場合、FIDO2/WebAuthn との整合がとれた認証・決済フローが PSP 側に要求される可能性がある

### 加盟店視点
- Nike・Walmart・Target 等の大手加盟店が AP2 + Universal Cart に対応済み。未対応加盟店は Google Gemini ユーザーのエージェント購入フローから除外されるリスク
- Shopify 加盟店（Fenty・Steve Madden 等）がデフォルトで含まれる。Shopify の AP2 統合により、Shopify 利用加盟店は自動的にエージェント決済の受け皿になる可能性がある

### プロダクト視点
- AP2 の FIDO Alliance 移管により x402 Foundation と並ぶ標準化ボディが生まれた。両プロトコルの相互運用性（補完か競合か）が開発者エコシステムの主要設計論点になる
- Universal Cart が「ユーザーの支出委任インターフェース」として機能する場合、AP2 の spending mandate 設計が実質的な「エージェント決済認可モデル」の de facto になりうる

### 規制 / リスク視点
- AP2 の FIDO Alliance 移管は、既存の FIDO2/WebAuthn フレームワークへの整合を意味する。エージェント identity（verifiable credentials）と FIDO 認証の組み合わせが規制対応設計の参照事例になりうる

## 我々への示唆
- いま検討すべきこと:
  - AP2 と x402 の相互運用性確認：AP2 に準拠した加盟店が x402 でも決済を受け取れるか。2 プロトコルへの同時対応が必要な可能性
  - Shopify AP2 統合のデフォルト状態確認：自社が Shopify ベースの加盟店向けプロダクトを持つ場合、AP2 対応がすでに完了しているかを確認する
- 後で深掘りすべきこと:
  - AP2 v0.2.0「Human Not Present」payments のユースケース（限定販売・リアルタイム価格反応）と自社プロダクトへの応用可否
  - FIDO Alliance AP2 WG のメンバー構成・標準化スケジュール
- 今は優先度が低いこと:
  - Universal Cart の YouTube・Gmail 統合（2026 年夏以降）

## ありそうな示唆
- Google Gemini + Universal Cart + AP2 は、「エージェントが自律的に商品を購入する」消費者向けインターフェースの最初の大規模実装。Apple・Amazon・Microsoft も同等の機能を追うと予想される
- AP2 の FIDO Alliance 移管により、既存の「パスキー/WebAuthn」インフラを持つ決済プレイヤーは AP2 対応コストが下がる可能性がある

## 推測 / 監視ポイント
- AP2 と x402 が「競合プロトコル」か「相互運用可能な補完プロトコル」かは未決定。Coinbase（x402 創始）と Google（AP2）の関係と、両者が x402 Foundation と FIDO Alliance でどう協調するかが焦点
- Universal Cart が Google Pay と統合された場合、USDC/ステーブルコイン決済オプションが追加される可能性（AP2 v0.2.0 時点では未確認）

## 未解決の論点
- AP2 と x402 の技術的相互運用性（エンドポイント仕様の共通性）
- Universal Cart での支払い方法（現状は Google Pay / カード主体か？ AP2 でのステーブルコイン決済サポート時期）
- Gemini Spark AP2 統合の詳細・リリース時期

## 参考リンク
- 一次情報: [Google Blog - Universal Cart（2026-05-19）](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/) / [Google I/O 2026 全発表まとめ](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- 補足情報: [TechCrunch（2026-05-19）](https://techcrunch.com/2026/05/19/googles-new-universal-cart-wants-to-follow-your-entire-shopping-journey-across-the-internet/) / [The Next Web](https://thenextweb.com/news/google-universal-cart-agent-payments-shopping-io-2026) / [Efficiently Connected - UCP and AP2](https://www.efficientlyconnected.com/google-io-2026-agentic-commerce-protocols-ucp-ap2/)

## 重要度
- High

## 確からしさ
- High
