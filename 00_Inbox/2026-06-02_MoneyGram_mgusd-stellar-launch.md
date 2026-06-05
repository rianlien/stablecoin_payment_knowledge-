---
title: "MoneyGram、MGUSD ステーブルコインを Stellar で本番ローンチ——60M 顧客向け自己カストディウォレット"
date: 2026-06-05
source: PR Newswire / CoinDesk / The Block
source_url: https://www.prnewswire.com/news-releases/moneygram-launches-mgusd-a-stablecoin-to-power-its-own-global-network-302787799.html
entity:
  - MoneyGram
  - Bridge（Stripe 傘下）
  - M0 Foundation
  - Fireblocks
  - Stellar Development Foundation
category: stablecoin-payments
primary_category: stablecoin-payments
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - stablecoin
  - stablecoin-payments
  - payment-rails
  - remittance
  - consumer-wallet
summary: "MoneyGram が 2026-06-02 に Stellar チェーン上で USD ペッグのステーブルコイン MGUSD を本番ローンチ。発行体は Stripe 傘下の Bridge（GENIUS Act 準拠 PPSI）。スマートコントラクトは M0 Foundation が担当し、ウォレットインフラは Fireblocks が提供。MoneyGram アプリの自己カストディウォレットに組み込み、60M 顧客・約 50 万拠点の自社ネットワーク向けの「基盤通貨」として機能させる計画。米国ユーザーから展開開始。"
implications: "大手送金事業者が自社ブランドのステーブルコインを発行したことで、Stellar エコシステムへの機関資金流入が加速する。Bridge（Stripe）が GENIUS Act 準拠 PPSI として MGUSD を発行するモデルは、他の PSP / 送金事業者が自社ステーブルコインを発行する際の参照事例になる。エージェント決済との直接の連携は現時点では未確認。"
importance: Medium
confidence: High
follow_up: "MGUSD の x402 / MCP / agentic payments との統合有無（公式確認）。MoneyGram の API 公開によりエージェントが MGUSD 送金を実行できるかどうか。グローバル展開タイムライン（60M 顧客への順次展開）。"
---

## 概要

MoneyGram が 2026 年 6 月 2 日に自社ステーブルコイン MGUSD の本番ローンチを発表。Stellar ブロックチェーン上で動作し、発行体（PPSI）は Stripe が 2024 年末に $11 億で買収した Bridge。スマートコントラクトは M0 Foundation が担当し、Fireblocks がカストディインフラを提供。MoneyGram アプリに自己カストディウォレットを組み込み、60 万人の従業員・60M 顧客・約 50 万リテール拠点のグローバルネットワークで「基盤通貨」として機能させる。

## 何が起きたか

- MoneyGram が PR Newswire でプレスリリースを発行（2026-06-02）
- Stellar ブロックチェーン上で MGUSD を本番稼働（Testnet 移行なし、直接 Mainnet）
- 米国ユーザーから提供開始。段階的にグローバル展開（約 200 カ国対応予定）
- MoneyGram アプリで自己カストディウォレットを提供——ユーザーが MGUSD を保有し MoneyGram ネットワーク経由で送金できる
- 技術スタック：
  - 発行体（PPSI）：Bridge（Stripe 傘下、GENIUS Act 準拠）
  - スマートコントラクト：M0 Foundation
  - ウォレットインフラ：Fireblocks（初期フェーズは Fireblocks ウォレットで管理後、MoneyGram アプリウォレットに移行）
- Stellar Development Foundation との 5 年間の提携を拡張した形（既存の USDC 連携を MGUSD 発行に発展）

## 確認された事実

- PR Newswire 公式プレスリリースで確認
- Bridge（Stripe）が GENIUS Act 対応 PPSI として発行体を担うことを明記
- MoneyGram の規模：60M 顧客、約 200 カ国、約 50 万リテール拠点
- 自己カストディ設計（ユーザーがウォレット鍵を保持）
- Stellar チェーンのみでの最初のローンチ（他チェーンへの展開は未発表）

## なぜ重要か

### 決済事業者視点

- Bridge（Stripe）が PPSI として MGUSD を発行するモデルは、他のフィンテック・送金事業者が自社ブランドのステーブルコインを発行する際の最初の実証事例
- Fireblocks がカストディインフラを提供しており、Fireblocks の Agentic Payments Suite との将来的な統合可能性を示唆（ただし現時点では未確認）

### 加盟店視点

- MoneyGram の 50 万リテール拠点が MGUSD 受け取りに対応すれば、Stellar チェーン経由でのグローバル送金コスト削減が実現する
- 直接的なエージェント決済向け機能は現時点では発表されていない

### プロダクト視点

- Bridge（Stripe）が MGUSD・USDC・その他ステーブルコインの複数発行体として機能しているモデルは、PSP が「ステーブルコイン発行者兼インフラプロバイダー」として収益化する新しい事業モデルを示す
- M0 Foundation のスマートコントラクトが多くのステーブルコインで採用され始めている（Canton の JP Morgan 決済でも M0 が使用）

### 規制 / リスク視点

- Bridge が GENIUS Act 準拠の PPSI として発行体を担うことで、MGUSD は GENIUS Act の「対象外」のグレーゾーンステーブルコインではなく、規制フレームワークに準拠した発行という位置づけ
- Stellar チェーン採用はブロックチェーンとしての規制適合性（Stellar は SECにより証券ではないと判断されている）を前提としている

## 我々への示唆

- いま検討すべきこと:
  - MoneyGram API / SDK が公開された場合、MGUSD を使った送金をエージェントが実行できるかどうかを確認——60M 顧客向けの決済チャネルとして活用できる可能性
  - Bridge（Stripe）が PPSI として複数のステーブルコインを発行しているモデルが、自社が依存する USDC の代替調達可能性にどう影響するかを評価
- 後で深掘りすべきこと:
  - MGUSD と x402 / Stellar Pay の統合有無——MoneyGram が x402 エコシステムへの参加を表明した場合、Stellar チェーン上での x402 展開に発展する可能性
  - M0 Foundation のスマートコントラクト標準の詳細——他のステーブルコインとの互換性
- 今は優先度が低いこと:
  - Stellar チェーン専用サービスへの投資（主要な決済フローが Ethereum / Base / Solana / Arbitrum に集中している現状では）

## ありそうな示唆

- MGUSD のローンチは「大手送金事業者が自社ステーブルコインを発行する」波の最初の事例。Western Union（USDPT・Solana 上で 2026-05 ローンチ）との競合構造が明確になる
- Bridge（Stripe）の「ステーブルコイン発行プラットフォーム」としての地位が強化される——MGUSD 以外にも類似モデルの採用事業者が増える可能性

## 推測 / 監視ポイント

- MGUSD のグローバル展開タイムライン
- Stellar 以外のチェーンへの展開（特に Solana・Base への展開があれば x402 との接続が近づく）
- MoneyGram の API 公開——エージェントが MGUSD 送金を実行する機能の有無
- Western Union USDPT との競合（Solana vs. Stellar の対立軸で比較されるか）

## 未解決の論点

- MGUSD のエージェント決済対応有無（MoneyGram の AI エージェント向け API/MCP 提供計画）
- 60M 顧客への展開タイムライン（段階的展開の詳細）
- Stellar 以外のチェーンへの展開計画

## 参考リンク

- 一次情報: [PR Newswire（2026-06-02）](https://www.prnewswire.com/news-releases/moneygram-launches-mgusd-a-stablecoin-to-power-its-own-global-network-302787799.html)
- 補足情報: [CoinDesk（2026-06-02）](https://www.coindesk.com/business/2026/06/02/moneygram-launches-stablecoin-on-stellar-joining-rush-toward-digital-dollar-payments), [The Block（2026-06-02）](https://www.theblock.co/post/403320/moneygram-debuts-mgusd-stablecoin-on-stellar-for-its-global-payments-network)

## 重要度

- Medium

## 確からしさ

- High（PR Newswire 公式プレスリリース確認済み）
