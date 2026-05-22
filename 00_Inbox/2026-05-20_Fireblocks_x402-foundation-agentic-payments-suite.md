---
title: "Fireblocks：x402 Foundation 加盟・Agentic Payments Suite ローンチ——機関グレードのエージェント決済インフラが PSP・フィンテック向けに提供開始"
date: 2026-05-22
source: PR Newswire / Fireblocks Blog / CoinTelegraph
source_url: https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html
entity: Fireblocks
category: agentic-payments / payment-infrastructure
primary_category: agentic-payments
article_published_date: 2026-05-20
underlying_event_date: 2026-05-20
primary_source_date: 2026-05-20
tags:
  - Fireblocks
  - x402
  - agentic-payments
  - PSP
  - stablecoin-infrastructure
summary: Fireblocks が 2026-05-20 に Agentic Payments Suite をローンチし、x402 Foundation（Linux Foundation）に加盟。PSP 向け Agentic Payments Gateway（ホワイトラベル加盟店受付インフラ）とフィンテック向け Agentic Wallets（Dynamic 連携、支出委任機能付き）の 2 製品を提供。Fireblocks Policy Engine・KYT・Travel Rule・MPC カストディを全決済ライフサイクルに統合。man-in-the-middle リルーティング攻撃を防ぐ x402 security extension も提供。
implications: 機関向け暗号資産カストディ大手 Fireblocks が PSP・フィンテック向けエージェント決済インフラに参入。既存 Fireblocks 顧客（銀行・PSP・フィンテック）が即座に利用可能。x402 エコシステムへの機関グレードのコンプライアンス機能（AML/KYT/Travel Rule）が加わった。
importance: High
confidence: High
follow_up: "Agentic Payments Gateway の対応ステーブルコイン・チェーン一覧、Agentic Wallets の Dynamic 統合仕様、x402 security extension の技術仕様詳細、採用第一号 PSP の発表"
---

## 概要
- Fireblocks が 2026-05-20 に Agentic Payments Suite と x402 Foundation 加盟を発表
- **Agentic Payments Gateway**：PSP がホワイトラベルで自社加盟店ベース全体にデプロイできる agentic payment acceptance レイヤー。chain・stablecoin agnostic。Fireblocks Policy Engine・KYT・Travel Rule・MPC カストディを内包
- **Agentic Wallets**（Dynamic 連携）：フィンテックがエンドユーザー向けウォレットを発行し、AI エージェントへの支出委任を安全に設定できるインフラ。支出上限・加盟店許可リスト・時間枠・アセット制限をポリシーとして実行前に強制
- **x402 security extension**：man-in-the-middle リルーティング攻撃を防ぐ request integrity + spend governance 拡張を x402 Foundation に提供（他のファシリテーターが未対応）
- x402 Foundation メンバー：Google・Microsoft・Visa・Coinbase に Fireblocks が追加

## 何が起きたか
- Fireblocks（機関向け暗号資産カストディ大手、累計取扱高数兆ドル規模）が 2026-05-20 に PSP・フィンテック向けの Agentic Payments Suite をローンチ
- x402 Foundation（Linux Foundation ホスト）に正式加盟し、security extension を提供
- Suite の構成：①Agentic Payments Gateway（PSP 向け加盟店決済受付インフラ）、②Agentic Wallets（フィンテック向けエンドユーザーウォレット + エージェント委任機能）
- セキュリティ：Fireblocks が x402 に security extension を追加提供。リクエスト完全性とスペンドガバナンスを x402 プロトコルレベルに実装し、他のファシリテーターが未対応の man-in-the-middle リルーティング攻撃を防止
- 対応：任意のステーブルコイン × 任意のブロックチェーン（chain/stablecoin agnostic）

## 確認された事実
- 発表日：2026-05-20
- 製品：Agentic Payments Gateway（PSP 向け）+ Agentic Wallets（フィンテック向け）
- x402 Foundation 加盟済み（Linux Foundation ホスト）
- Agentic Wallets は Dynamic と連携
- Fireblocks Policy Engine・KYT・Travel Rule・MPC カストディを全製品に統合
- x402 security extension：man-in-the-middle リルーティング攻撃防止（request integrity + spend governance）を x402 Foundation に提供
- 他の x402 Foundation メンバー：Google・Microsoft・Visa・Coinbase

## なぜ重要か

### 決済事業者視点
- Fireblocks を既に利用している PSP（銀行・フィンテック・デジタル資産取扱業者）は Agentic Payments Gateway をホワイトラベルで即座にデプロイ可能。エージェント決済のインフラ調達コストが大幅に下がる
- Fireblocks の KYT・Travel Rule サポートはコンプライアンス面での即戦力。GENIUS Act 施行後の PPSI 要件（AML・カストディ・Travel Rule）対応にも直結

### 加盟店視点
- Agentic Payments Gateway を PSP がデプロイすることで、加盟店は個別に x402 エンドポイントを構築せず PSP 経由でエージェント決済を受け取れる。加盟店側の実装コストが下がり、x402 普及が加速する

### プロダクト視点
- Agentic Wallets の「スコープ付き取消可能権限（支出上限・加盟店許可リスト・時間枠）」は CFES ガイドライン（2026-05-13）の「認可範囲」フレームワークとほぼ合致する実装例。業界参照設計として機能する
- Dynamic 連携により既存の Web3 ウォレット認証基盤（passkey・social login）とエージェント委任が統合されうる

### 規制 / リスク視点
- Travel Rule 内蔵は FATF / FinCEN 要件への対応。x402 security extension（request integrity）は「エージェントがユーザーの指示を改ざんせず実行したことの証明」として規制対応上の evidence trail になりうる
- GENIUS Act PPSI 要件（AML・カストディ・Travel Rule）を Fireblocks インフラがカバーするため、PPSI 取得を目指す発行体には有力な技術選択肢になる

## 我々への示唆
- いま検討すべきこと:
  - Fireblocks Agentic Payments Gateway が自社 PSP インフラと統合できるか評価。対応ステーブルコイン・チェーン一覧と既存 Fireblocks 契約の有無を確認
- 後で深掘りすべきこと:
  - Agentic Wallets の Dynamic 統合仕様：既存の Web3 ログイン基盤（passkey 等）との接続可否
  - x402 security extension の技術仕様：request integrity の署名スキーム・spend governance のオンチェーン保存方式
- 今は優先度が低いこと:
  - Fireblocks の料金モデル詳細（Agentic Wallets のウォレット発行コスト）

## ありそうな示唆
- Fireblocks の参入で x402 エコシステムに機関グレードのコンプライアンス機能が加わり、規制対応 PSP・銀行系フィンテックへの x402 採用が加速する。「x402 はコンプライアンスが不十分」という懸念が薄まる可能性がある

## 推測 / 監視ポイント
- Fireblocks Agentic Payments Gateway を採用する PSP の第一号事例が出るかどうか（2026 年内）
- Fireblocks が Circle Agent Wallets・AWS AgentCore Payments と「互補インフラ（下レイヤー）」として位置づけるかどうか

## 未解決の論点
- Agentic Payments Gateway の対応ステーブルコイン一覧（USDC・USDT・USDG 等）
- Agentic Wallets の料金モデル（フィンテック向けウォレット発行コスト）
- Circle Agent Stack・AWS AgentCore との統合可否（独立 or 競合）

## 参考リンク
- 一次情報: [PR Newswire（2026-05-20）](https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html)
- 補足情報: [Fireblocks Blog](https://www.fireblocks.com/blog/agentic-payments-suite-psp-fintech) / [Fireblocks Product Page](https://www.fireblocks.com/products/agentic-payments) / [CoinTelegraph via TradingView（2026-05-20）](https://www.tradingview.com/news/cointelegraph:efaa4241b094b:0-fireblocks-launches-agentic-payment-support-joins-x402-foundation/) / [Glenbrook（2026-05-20）](https://glenbrook.com/payments_news/fireblocks-joins-x402-foundation-launches-agentic-payments-suite/) / [Fintech News SG](https://fintechnews.sg/131873/digitalassets/fireblocks-agentic-payments/)

## 重要度
- High

## 確からしさ
- High
