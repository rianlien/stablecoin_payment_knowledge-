---
title: "Google Marketing Live 2026：UCP に Identity Linking・Catalog API・マルチアイテムカートを追加、AP2 と UCP を軸にエージェント商取引の国際展開を発表"
date: 2026-05-28
source: Google Blog / Search Engine Land
source_url: https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/
entity: Google
category: agentic-commerce / payment-protocol / merchant-PSP-readiness
primary_category: agentic-commerce
article_published_date: 2026-05-28
underlying_event_date: 2026-05-28
primary_source_date: 2026-05-28
tags:
  - UCP
  - AP2
  - agentic-commerce
  - agent-identity
  - merchant-readiness
summary: "Google が Marketing Live 2026（5/28）で Universal Commerce Protocol（UCP）の新機能 3 件と国際展開を発表。①Identity Linking（ロイヤルティ特典のエージェント経由での引き継ぎ）、②Catalog API（エージェントによるリアルタイム商品情報取得）、③マルチアイテムカート対応を追加。UCP 対応小売として Nike・Sephora・Target・Walmart・Wayfair 等を公開。Commerce Inc・Salesforce・Stripe が UCP 実装パートナーに。カナダ・オーストラリアへの国際展開も発表"
implications: "AP2＋UCP スタックが単なる Google 内部機能から、Salesforce・Stripe 経由で一般小売のエージェント商取引インフラに拡大。Identity Linking は AI エージェントがユーザーの既存会員 ID を引き継ぐ仕組みであり、agent identity の実装モデルとして重要"
importance: High
confidence: High
follow_up: "Stripe の UCP 実装の具体的な API スペック、Salesforce Commerce Cloud での UCP 対応開発者向け情報、AP2 Intent Mandate の仕様更新有無、カナダ・オーストラリアの展開タイムライン"
---

## 概要
- Google が年次マーケティングカンファレンス「Google Marketing Live 2026」（2026 年 5 月 28 日）で Universal Commerce Protocol（UCP）の新機能と国際展開を発表
- AP2（Agent Payments Protocol）と UCP は Google のエージェント商取引スタックの 2 本柱として位置づけられ、今回の発表で機能・地理的範囲が大幅に拡張

## 何が起きたか

### UCP 新機能 3 件
1. **Identity Linking**
   - ユーザーが UCP 統合プラットフォーム上でログインしていると、小売サイトと同等のロイヤルティ特典・会員価格・無料配送特典を受けられる
   - AI エージェントがユーザーのアカウント ID を小売に「接続」するメカニズム
2. **Catalog API**
   - エージェントが小売のカタログからリアルタイム商品情報（バリアント・在庫・価格）を取得できる
   - エージェントがより精度の高い購買決定を下すための基盤
3. **マルチアイテムカート対応**
   - エージェントが複数商品を一度のカートセッションで保存・処理できる（人間の通常の買い物行動に近い形）

### 国際展開・カテゴリ拡張
- UCP 対応 checkout を Canada・Australia に拡大（続いて UK を予定）
- ホテル予約・ローカルフード配達などの新カテゴリへ UCP 対応範囲を拡張予定

### 対応小売（UCP checkout 公開）
- Nike、Sephora、Target、Ulta Beauty、Walmart、Wayfair、Shopify 加盟店（Fenty・Steve Madden 等）

### UCP 実装プラットフォームパートナー
- Commerce Inc、Salesforce、Stripe（近日対応予定）

### Merchant Center オンボーディング簡略化
- Google Merchant Center 上で UCP オンボーディングを簡略化したフローを数ヶ月内に展開予定

## 確認された事実
- Google 公式ブログ（2026-05-28）で発表
- Search Engine Land が独立報道（2026-05-28）で確認
- Google Marketing Live 2026 は 5 月 28 日開催（underlying event date = 記事公開日と一致）

## なぜ重要か

### 決済事業者視点
- Stripe が UCP 実装パートナーに加わったことで、Stripe の加盟店ベース（数百万）が UCP エージェント checkout 対応に近づいた。Stripe MPP × UCP の組み合わせは最大規模のエージェント決済インフラになりうる

### 加盟店視点
- Nike・Target・Walmart 等の大手が UCP checkout を公開したことで「エージェント受け入れ加盟店」の先行事例が揃い始めた
- Merchant Center でのオンボーディング簡略化により中小事業者の参入障壁が下がる見通し

### プロダクト視点
- **Identity Linking** は agent identity の実装においてきわめて重要：AI エージェントがユーザーの既存アカウントを代理で使うことを、小売・決済・Google の三者間で標準化しようとしている。AP2 の Intent Mandate（ユーザーが何を許可したか）とセットで考えると、エージェントへの委任スコープの形式化が進んでいる
- Catalog API はエージェントが商品比較・在庫確認を行うための基盤として、x402・MPP との組み合わせにおけるプリペイメントフローを可能にする

### 規制 / リスク視点
- Identity Linking はユーザーアカウントへのエージェントアクセスを伴うため、OAuth スコープ管理・委任認証の整備が必須。GDPR・改正 PSD2 との整合性確認が必要

## 我々への示唆
- いま検討すべきこと:
  - UCP の Identity Linking 仕様を確認し、自社の agent identity 設計（who is authorized to act）とのマッピングを行う
  - Stripe の UCP 実装が公開された際に、自社の Stripe 統合を通じてエージェント checkout 対応を検討する
- 後で深掘りすべきこと:
  - AP2 の最新仕様（Intent Mandate・Cart Mandate・Payment Mandate）が今回の UCP 新機能に合わせてアップデートされているかを確認
  - Google Merchant Center の新オンボーディングフローの詳細
- 今は優先度が低いこと:
  - カナダ・オーストラリア展開の詳細スケジュール（自社が日本・欧州向け事業の場合）

## ありそうな示唆
- Salesforce + Stripe が UCP に対応することで、既存の EC プラットフォームユーザーが「エージェント受け入れ加盟店」になるためのコストが大幅に下がる。2026 年後半に UCP 採用加盟店数が急増する可能性が高い

## 推測 / 監視ポイント
- AP2 仕様（GitHub: google-agentic-commerce/AP2）が今回の発表に合わせてアップデートされているか
- Shopify の UCP ネイティブ対応（現在は Stripe 経由の想定）の独立対応時期

## 未解決の論点
- UCP × AP2 での支払い失敗（取引キャンセル・在庫切れ・金額超過）時のエラーハンドリング仕様
- Identity Linking でのユーザーの同意取得フロー（誰がいつ認証するか）

## 参考リンク
- 一次情報:
  - [Google Blog（2026-05-28）](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/)
  - [Google Blog（2026-05-28）別記事](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/)
- 補足情報:
  - [Search Engine Land（2026-05-28）](https://searchengineland.com/google-expands-universal-commerce-protocol-and-launches-new-agentic-shopping-tools-478113)

## 重要度
- High

## 確からしさ
- High
