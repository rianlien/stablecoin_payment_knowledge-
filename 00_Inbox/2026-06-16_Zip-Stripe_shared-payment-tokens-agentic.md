---
title: "Zip US、Stripe の Shared Payment Tokens を採用——BNPL をエージェントコマースに拡張"
date: 2026-06-16
source: PR Newswire / Yahoo Finance
source_url: https://uk.finance.yahoo.com/news/zip-us-expands-partnership-130000633.html
entity: Zip / Stripe
category: agent-payments
primary_category: merchant-PSP-readiness
article_published_date: 2026-06-16
underlying_event_date: 2026-06-16
primary_source_date: 2026-06-16
tags:
  - agentic-commerce
  - BNPL
  - Stripe-MPP
  - payment-authorization
  - merchant-readiness
summary: "Zip US が Stripe の Shared Payment Tokens（SPT）のサポートを発表。AI エージェントが顧客の代わりに取引を開始する際、カード決済以外に Zip の BNPL（後払い）オプションを利用可能にする。エージェント起点取引における支払い手段の多様化が進む。"
implications: "Stripe MPP エコシステムに BNPL が加わることで、エージェントコマースの支払い手段が拡張。カード決済中心から多様な支払い選択肢への移行が加速する可能性。"
importance: Medium
confidence: High
follow_up: "Affirm・Klarna 等他の BNPL プロバイダーの SPT 対応動向、エージェントが BNPL を選択する際のリスク管理・キャンセル処理の設計"
---

## 概要

Zip US が 2026-06-16 に Stripe の Shared Payment Tokens（SPT）サポートを発表。AI エージェントが顧客の代わりに購入を実行する際、Zip の後払い（BNPL）オプションを使えるようにする取り組み。従来のエージェント決済がカード決済中心だったのに対し、支払い手段の選択肢を広げる動き。

## 何が起きたか

- Zip US が Stripe の Shared Payment Tokens（SPT）サポートを発表（2026-06-16）
- SPT は、AI エージェントが顧客の代わりに取引を開始する際に決済認証情報を直接露出せずに支払いを実行する仕組み
- Zip US の後払い（BNPL）オプションが SPT 経由でエージェント起点取引に利用可能になる
- Stripe の Agentic Commerce Suite において、エージェントが Klarna・Affirm に加え Zip でも支払えるようになる
- エージェントは顧客の「好みの支払い手段」を維持したまま自律的に購入を実行できる

## 確認された事実

- Zip Co Limited の公式発表（PR Newswire / Yahoo Finance 2026-06-16）
- Stripe 側のコメント：Kevin Miller（Head of Payments）が「Zip を agentic transactions に加えることで、ビジネスはコンバージョンを上げつつ購入者に支払い選択肢を提供できる」と発言
- Zip US 側のコメント：Rory Herriman（U.S. CTOO）が「透明性・選択肢・信頼性を維持しながら BNPL を新しい体験に持ち込む」と発言
- 従来のエージェント決済は主にカード決済（card-on-file）依存で BNPL が使えない課題があった

## なぜ重要か

### 決済事業者視点

- エージェントコマースにおける支払い手段の多様化：Stripe MPP エコシステムが BNPL（Zip・Klarna・Affirm）を取り込むことで、PSP としての網羅性が高まる
- SPT が「カード以外の支払い手段をエージェントに安全に委任する」汎用メカニズムとして機能し始めている

### 加盟店視点

- エージェントが BNPL で決済できることで、平均注文金額（AOV）の高い購買でのコンバージョンが向上する可能性
- BNPL の返品・キャンセル・与信管理は加盟店側の対応が増える可能性（設計要確認）

### プロダクト視点

- SPT の汎用化が進めば、stablecoin・銀行振込・デジタルウォレット等も同じ仕組みでエージェントに委任できる方向性が見える
- AP2 の「Mandate（支払い委任状）」と SPT の関係が今後の重要論点になりうる

### 規制 / リスク視点

- BNPL のエージェント利用は「消費者が認識せずに後払い契約を結ぶリスク」を内包する。規制当局（CFPB・EU の BNPL 規制）の視点で注意が必要
- stablecoin 決済とは異なり BNPL の規制枠組みは既存のため、短期的な規制リスクは低い

## 我々への示唆

- いま検討すべきこと:
  - 自社エージェント決済プロダクトに SPT 対応を組み込む場合、BNPL の取り扱いポリシー（上限額・対象カテゴリ）を設計しておく
- 後で深掘りすべきこと:
  - SPT が stablecoin レール（USDC）の委任にも対応するか（Stripe の Agentic Commerce Suite ロードマップ確認）
  - AP2 Mandate と SPT の相互運用性（どちらが委任の「正規表現」になるか）
- 今は優先度が低いこと:
  - Zip の具体的な BNPL 条件・手数料体系

## ありそうな示唆

- Affirm・Klarna に加え Zip も SPT 対応したことで、BNPL 3 社が Stripe エージェントコマースに揃った形になりつつある。stablecoin（Coinbase Pay / Bridge）の SPT 対応が次のステップになりうる

## 推測 / 監視ポイント

- 他の BNPL プロバイダー（Sezzle・Paidy・Tabby 等）の SPT 対応
- Stripe SPT の stablecoin レール対応（USDC エージェント決済との統合）
- エージェントによる BNPL 利用に対する規制当局のスタンス（CFPB・EU BNPL 指令）

## 未解決の論点

- SPT 経由の BNPL でのエージェント購入について、消費者保護・不正利用時の責任分担がどうなるか
- AP2 の Payment Mandate と SPT は競合するか補完するか

## 参考リンク

- 一次情報: [Zip US Expands Partnership with Stripe（2026-06-16）](https://uk.finance.yahoo.com/news/zip-us-expands-partnership-130000633.html)
- 補足情報: [PYMNTS: Zip and Stripe Bring Flexible Payment Options to Agentic Transactions（2026-06-16）](https://www.pymnts.com/partnerships/2026/zip-stripe-bring-flexible-payment-options-agentic-transactions/)
- 補足情報: [Stripe Blog: Supporting additional payment methods for agentic commerce](https://stripe.com/blog/supporting-additional-payment-methods-for-agentic-commerce)

## 重要度

- Medium

## 確からしさ

- High（公式プレスリリース・Stripe / Zip 双方の公式コメントあり）
