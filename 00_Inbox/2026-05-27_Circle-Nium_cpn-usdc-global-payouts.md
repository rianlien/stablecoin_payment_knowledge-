---
title: "Circle Payments Network、Nium をグローバルペイアウトパートナーに追加——USDC 決済を 190 カ国・100 通貨で着地可能に"
date: 2026-05-27
source: "PR Newswire / Circle公式 / The Block / American Banker"
source_url: "https://www.circle.com/pressroom/nium-and-circle-to-connect-usdc-settlement-with-global-payouts"
entity: "Circle / Nium"
category: "payment-rails"
primary_category: "stablecoin-payments"
article_published_date: 2026-05-27
underlying_event_date: 2026-05-27
primary_source_date: 2026-05-27
tags:
  - circle
  - stablecoin-payments
  - payment-rails
  - agentic-commerce
  - cross-border
summary: "NiumがCircle Payments Network（CPN）のグローバルペイアウトパートナーに参加。金融機関はUSDCで決済後、Niumの190カ国・100通貨の払い出しインフラへ単一統合でアクセス可能に。CPN年間換算取引量$83億（2026年3月末時点）。Circle VP はアジェンティックコマースへの準備として明示的に位置づけ。"
implications: "Circle Agent Stack（5月11日発表）から始まる「エージェントがUSDCで支払う」フローに対し、CPN+Niumがラストマイル着地を提供する構造が完成。クロスボーダーのエージェント決済がローカル通貨で受け取れるインフラとして、x402/AP2エコシステム上のBtoB決済の地理的カバレッジが190カ国に広がる。"
importance: Medium
confidence: High
follow_up: "CPN経由x402決済の実際の処理事例（Circle Agent Stack＋CPN＋Niumを一気通貫で使う商業事例）、Niumのエージェント向け入金APIの公開有無、CPNの次のパートナー追加発表"
---

## 概要

Circle は 2026 年 5 月 27 日、クロスボーダー決済会社 Nium が Circle Payments Network（CPN）のグローバルペイアウトパートナーとして参加することを発表。金融機関は CPN 経由で USDC 決済後、Nium のペイアウトインフラを通じて 190 カ国・100 通貨での着地払いを単一統合で実現できるようになった。

## 何が起きたか

- Nium が CPN のグローバルペイアウトパートナーとして参加（2026 年 5 月 27 日 PR Newswire / Circle 公式）
- 金融機関は CPN 上で USDC 建て決済後、Nium の 190 カ国・100 通貨の払い出しインフラに単一 API 接続でアクセス可能に
- 事前資金調達（プリファンディング）要件の削減、オンチェーン透明性によるリアルタイムトラッキングが実現
- CPN の年間換算取引量は $83 億（2026 年 3 月 31 日時点の直近 30 日ベース）

## 確認された事実

- 発表日：2026 年 5 月 27 日（PR Newswire / Circle 公式プレスルーム）
- CPN（Circle Payments Network）：金融機関が USDC 決済レールにアクセスするための Circle の B2B 決済ネットワーク
- Nium：クロスボーダー決済インフラ企業。190 カ国・100 通貨のペイアウトネットワークを保有
- CPN 年間換算処理量：$83 億（2026 年 3 月 31 日時点の直近 30 日実績ベース）
- Circle VP Spencer Spinelli 発言：「Agentic commerce will require payment infrastructure that can support increasingly automated and real-time decision making.（アジェンティックコマースには、自動化されたリアルタイムの意思決定を支えられる決済インフラが必要）」
- 既存 CPN 参加事業者に Nium のペイアウトネットワーク全体が開放——新規の国・通貨対応を追加契約なしに利用可能

## なぜ重要か

### 決済事業者視点

- CPN に乗っている PSP・銀行・フィンテックが、今後 Nium ペイアウトを通じてエージェント決済の最終着地を 190 カ国で提供できるようになる
- プリファンディング削減とオンチェーン透明性は、エージェント決済の速度要件（即時確認）に適合する設計

### 加盟店視点

- B2B エージェント決済（AP 自動化・調達支払い）において、USDC で受け取り → ローカル通貨への自動転換という流れが単一統合で実現可能になる
- 190 カ国カバーは、新興市場での AI エージェント起点クロスボーダー支払いの実現可能性を大幅に高める

### プロダクト視点

- Circle Agent Stack（5/11 発表）との組み合わせ：エージェントが USDC を支払う → CPN でルーティング → Nium で各国ローカル通貨着地、というエンドツーエンドの設計が揃う
- 先行する `2026-04-08_Circle_cpn-managed-payments` で導入された「暗号資産管理不要の CPN アクセス」と組み合わさり、一般的な決済事業者がエージェント決済のクロスボーダー対応を導入しやすくなる

### 規制 / リスク視点

- GENIUS Act 最終規則（2026-07-18 デッドライン）確定後、CPN 上で USDC を扱う金融機関は PPSI ライセンス要件に準拠する必要が生じる可能性。ライセンス要件確定前のパートナー拡大は規制リスクを内包
- Nium がペイアウト先となる国（特に新興市場）での規制対応は Nium 側が担う設計——自社でのコンプライアンス対応コストを外部化できるが、Nium の規制リスクを間接的に引き受けることになる

## 我々への示唆

- いま検討すべきこと:
  - Circle Agent Stack + CPN + Nium のエンドツーエンド接続仕様の確認——自社エージェント決済プロダクトがクロスボーダーに展開する際に CPN 経由で Nium を使う選択肢の評価
- 後で深掘りすべきこと:
  - CPN の参加要件・契約形態——銀行や大型 PSP 向けか、スタートアップも参加可能か
  - Nium の API でエージェントが直接払い出しを指示できる仕様があるかどうか（エージェント起点の自律的なペイアウト管理）
- 今は優先度が低いこと:
  - CPN の金融機関ごとの対応通貨・国の詳細リスト

## ありそうな示唆

- Circle Agent Stack（エージェントがUSDCを支払う側）と CPN+Nium（受け取り側のローカル通貨着地）が揃うことで、「AI エージェントが国際送金・クロスボーダー決済を完全自律で実行する」インフラが完成に近づく
- 将来的に x402 エコシステムが CPN に接続されれば、x402 決済の着地通貨を世界 190 カ国で柔軟に設定できるようになる

## 推測 / 監視ポイント

- Circle が CPN に次のパートナーを追加する時期と対象（Airwallex・Rapyd 等の競合ペイアウトプロバイダーとの差別化）
- CPN+Nium がエージェント決済の実際の商業事例で使われたことを示す一次情報の公開時期
- GENIUS Act 最終規則（7/18）後の Circle の PPSI 申請状況と CPN の PPSI 対応方針

## 未解決の論点

- CPN 上の USDC 決済が GENIUS Act の「Permitted Payment Stablecoin」要件に適合するかどうか（Circle の PPSI ライセンス申請状況）
- Nium ペイアウトの着地時点でのステーブルコインと法定通貨の間の変換は誰が担うか（Circle か Nium か）

## 参考リンク

- 一次情報: [Circle プレスルーム（2026-05-27）](https://www.circle.com/pressroom/nium-and-circle-to-connect-usdc-settlement-with-global-payouts) / [PR Newswire（2026-05-27）](https://www.prnewswire.com/news-releases/nium-and-circle-to-connect-usdc-settlement-with-global-payouts-302783070.html) / [Nium Newsroom（2026-05-27）](https://www.nium.com/newsroom/nium-circle-usdc-settlement-global-payouts)
- 補足情報: [American Banker（2026-05-27）](https://www.americanbanker.com/payments/news/circle-and-nium-partner-to-boost-stablecoins-ai) / [The Block（2026-05-27）](https://www.theblock.co/post/402726/circle-partners-with-nium-to-connect-usdc-settlement-to-global-payout-rails) / [PYMNTS（2026-05-27）](https://www.pymnts.com/partnerships/2026/circle-and-nium-launch-stablecoin-settlement-partnership/)

## 重要度

- Medium

## 確からしさ

- High
