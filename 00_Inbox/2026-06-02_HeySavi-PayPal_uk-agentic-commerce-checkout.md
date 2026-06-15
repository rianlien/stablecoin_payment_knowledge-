---
title: "Hey Savi と PayPal、英国で native checkout 付き agentic commerce を公開"
date: 2026-06-02
source: PayPal Newsroom
source_url: https://newsroom.paypal-corp.com/2026-06-02-Hey-Savi-and-PayPal-Launch-UKs-First-Agentic-Commerce-Platform-with-In-App-Checkout-Debenhams-Group-Joins-as-First-Retail-Adopter
entity: Hey Savi / PayPal / Debenhams Group
category: agentic-commerce / merchant-PSP-readiness / payment-authorization
primary_category: agentic-commerce
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - PayPal
  - agentic-commerce
  - merchant-readiness
  - checkout
  - Debenhams
summary: "Hey Savi と PayPal が 6 月 2 日、英国で native checkout 付き agentic commerce 体験を公開した。ファッション探索から比較、購入までをアプリ内で完結させ、Debenhams Group が最初の小売導入企業として参加する。PayPal は merchant storefront の商品データを AI platform に接続し、検索から購入までの閉ループを提供する"
implications: "PayPal は『agentic commerce の支払い部分』ではなく、merchant data access と in-app checkout の接続レイヤーまで提供し始めた。加盟店が AI storefront に流通面ごと接続される構図が見え、merchant readiness は checkout API だけでなく catalog distribution の問題でもあることが鮮明になった"
importance: Medium
confidence: High
follow_up: "PayPal.ai の merchant onboarding 条件、返品 / 不正時の責任分担、他カテゴリ展開、PayPal が提供する agentic commerce API の公開範囲を確認する"
---

## 概要
- PayPal が 2026 年 6 月 2 日、Hey Savi と組んで英国で agentic commerce 体験を公開した
- 重要なのは AI discovery から native checkout までを同じ面で閉じたことと、Debenhams Group が実導入加盟店として前面に出たこと

## 何が起きたか
- Hey Savi は brand-agnostic fashion search として、スクリーンショットや対話から商品発見を行う
- PayPal は native checkout を提供し、アプリ外遷移を減らす
- Debenhams、Karen Millen、Boohoo、Pretty Little Thing を含む Debenhams Group が最初の retail adopter として参加した
- PayPal は merchant storefront の価格、画像、説明、レビュー、在庫を AI platform 側へ接続できると説明している

## 確認された事実
- PayPal Newsroom の公開日は 2026-06-02
- 公式文面で「UK's first agentic commerce experience with native checkout powered by PayPal」とされている
- Debenhams Group が first retailer in the UK と明記されている
- UK merchants 向けに PayPal.ai で登録導線が案内されている

## なぜ重要か

### 決済事業者視点
- PSP の役割が checkout 処理だけでなく、agentic storefront への商品データ接続や merchant onboarding に広がっている
- PayPal が merchant と AI app の両側をつなぐなら、将来の agentic commerce で PSP は acceptance と discovery の両方を握る可能性がある

### 加盟店視点
- 加盟店は自社サイト訪問を待つのではなく、AI storefront 上で発見され、そのまま決済まで進む導線への対応が必要になる
- 返品、在庫同期、価格差異、キャンセル時対応など、従来の affiliate や marketplace と異なる運用論点が出る

### プロダクト視点
- main lesson は「検索体験」と「支払い体験」を別々に作らないこと。agentic commerce では、intent capture から checkout completion まで一気通貫でないと転換率が落ちやすい
- PayPal が merchant data bridge を提供するなら、catalog freshness と payment completion が同じ制御面に入る

### 規制 / リスク視点
- AI app 内購入では消費者保護、誤購入、返品導線、広告表示ルールが重要になる
- native checkout で friction は下がるが、購入主体と推薦主体の境界が曖昧になるリスクもある

## 我々への示唆
- いま検討すべきこと:
  - agentic commerce では checkout API だけでなく catalog / inventory exposure 設計も同時に評価する
  - merchant への提案を「agent から払える」だけでなく「agent に見つけられる」まで広げる
- 後で深掘りすべきこと:
  - PayPal.ai の merchant 向け仕様
  - in-app checkout 時の authorization / refund / support flow
- 今は優先度が低いこと:
  - Hey Savi 単独アプリのグロース戦略

## ありそうな示唆
- 英国先行でも、agentic commerce の実装単位は protocol 単体ではなく「AI storefront + merchant data + PSP checkout」の束で広がる可能性が高い

## 推測 / 監視ポイント
- PayPal が他カテゴリや他地域へ横展開するか
- Debenhams 以外の加盟店参加がどの程度増えるか
- PayPal の merchant data API が標準化されるか

## 未解決の論点
- AI app 内での返品・サポート責任の分界
- merchant データ更新遅延時の価格 / 在庫不一致処理
- PayPal が提供する agentic commerce API の公開度合い

## 参考リンク
- 一次情報:
  - [PayPal Newsroom（2026-06-02）](https://newsroom.paypal-corp.com/2026-06-02-Hey-Savi-and-PayPal-Launch-UKs-First-Agentic-Commerce-Platform-with-In-App-Checkout-Debenhams-Group-Joins-as-First-Retail-Adopter)
- 補足情報:
  - [PR Newswire mirror](https://www.prnewswire.com/news-releases/hey-savi-and-paypal-launch-uks-first-agentic-commerce-platform-with-in-app-checkout-debenhams-group-joins-as-first-retail-adopter-302787743.html)

## 重要度
- Medium

## 確からしさ
- High
