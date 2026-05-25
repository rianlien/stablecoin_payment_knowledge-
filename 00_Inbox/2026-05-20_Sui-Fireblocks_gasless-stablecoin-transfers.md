---
title: "Sui、プロトコルレベルのガスレスステーブルコイン転送をメインネット展開 — Fireblocks が統合パートナーとして参加"
date: 2026-05-23
source: "PR Newswire / Sui Blog / Decrypt"
source_url: "https://www.prnewswire.com/news-releases/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks-302778111.html"
entity: "Mysten Labs (Sui) / Fireblocks"
category: "payments"
primary_category: "agentic-commerce"
article_published_date: 2026-05-20
underlying_event_date: 2026-05-20
primary_source_date: 2026-05-20
tags:
  - agentic-commerce
  - stablecoin-infrastructure
  - agent-payments-infrastructure
  - machine-payments
summary: "Sui ネットワークが 2026 年 5 月 20 日、ガスレスステーブルコイン転送機能をメインネットで展開開始。ステーブルコインの送付に SUI トークンのガス保有が不要になり、USDC を含む 7 種のステーブルコインに対応。Fireblocks が統合パートナーとして参加し、同日発表の Agentic Payments Suite にも接続。AI エージェントや高頻度支払いに伴うガス管理の摩擦を除去する。"
implications: "エージェント決済の主要な UX 摩擦点（ガストークン確保・管理）がプロトコルレベルで解消されることで、Sui 上での AI エージェント自律決済の実装コストが低下。Fireblocks の Agentic Payments Suite と Sui の gasless 機能の組み合わせが、エンタープライズ向けエージェント決済の最初の参照設計となりうる。"
importance: Medium
confidence: High
follow_up: "ガスレス転送の実装方式（スポンサートランザクション vs プロトコル変更）、Sui 上での x402 対応状況、Fireblocks Agentic Wallets × Sui 統合の具体的なユースケース事例、他チェーン（Base・Solana 等）の類似取り組みとの比較"
---

## 概要

Sui ネットワーク（Mysten Labs）が 2026 年 5 月 20 日、プロトコルレベルのガスレスステーブルコイン転送機能をメインネットにロールアウト開始した。ユーザー・エージェントがサポートされたステーブルコインを送付する際に、ガス費用としての SUI トークン保有が不要になる。USDC・USDY・suiUSDe・USDsui・AUSD・FDUSD・USDB の 7 種が対応。デジタル資産カストディの Fireblocks がローンチ統合パートナーとして参加しており、同日発表の Agentic Payments Suite にも接続する。

## 何が起きたか

- **発表日**：2026 年 5 月 20 日（PR Newswire / Sui ブログ同日）
- **機能概要**：ガスレスステーブルコイン転送（Gasless Stablecoin Transfers）のメインネット展開
- **対応ステーブルコイン**（7 種）：USDC・USDY・suiUSDe・USDsui・AUSD・FDUSD・USDB
- **ガス費用**：対応ステーブルコイン転送時は $0.00（バリデータへのロールアウト中）
- **Fireblocks 統合**：Fireblocks がローンチ前にネットワークへの統合を完了
- **背景**：ステーブルコイン大量送受信において「ガストークン（SUI）を別途保有・管理する必要性」がユーザー・エージェントの主要な摩擦点とされていた

## 確認された事実

- Sui 公式ブログ・PR Newswire（2026-05-20）による一次情報確認
- Fireblocks の統合はローンチ以前に完了（PR Newswire プレスリリースで明記）
- 対応 7 ステーブルコインの一覧は Sui 公式ブログで確認
- 「バリデータへのロールアウト中」という表現から、全バリデータへの展開は段階的に進行中
- ガスレスの具体的な実装方式（スポンサートランザクション/プロトコル変更）は発表時点では明記なし

## なぜ重要か

### 決済事業者視点

- エージェント決済において「SUI ガストークンの確保・管理・補充」が不要になり、ステーブルコインのみで完結する運用が可能に。PSP がエージェント決済を Sui 上で展開する際の運用コスト（ガス管理）が削減される
- Fireblocks が統合済みのため、Fireblocks を既に使用している PSP・フィンテックは追加作業なしで本機能を活用できる

### 加盟店視点

- 高頻度の小額決済（マイクロペイメント・API 課金）において、ガストークンの底をつくリスクが除去される
- エージェントが SUI 残高不足で決済失敗するシナリオが発生しにくくなり、加盟店側のエラー率が低下

### プロダクト視点

- AI エージェントの「ガストークン自動補充ロジック」というエンジニアリング負荷が解消。エージェントのウォレット設計がシンプルになり、USDC（またはその他対応ステーブルコイン）のみを保持する設計が実現可能
- Solana（高速・低コスト）・Base（Coinbase エコシステム）との比較において、Sui の差別化要因が増加

### 規制 / リスク視点

- ガス代不要の設計は「ステーブルコイン = 電子マネー」と見なす規制当局に対し、より純粋な決済手段としての特徴を持つ。ただし規制適格性（GENIUS Act PPSI・MiCA EMT）は USDC・USDY 等の各ステーブルコインに依存し、Sui のプロトコル機能とは独立

## 我々への示唆

- いま検討すべきこと:
  - Sui 上で USDC を用いたエージェント決済を設計する場合、ガスレス機能により「SUI 補充ロジック不要」の設計が可能であることを確認。Solana・Base との UX 比較の前提として評価
  - Fireblocks Agentic Wallets（同日発表）と本機能の組み合わせが、自社エージェント決済インフラの候補として検討に値するか評価
- 後で深掘りすべきこと:
  - ガスレス転送の実装方式（スポンサートランザクション vs プロトコル内蔵 vs 別途 fee payer 設定）を技術ドキュメントで確認
  - Sui 上での x402 ファシリテーター実装状況（Coinbase CDP が Sui を x402 対応チェーンとして追加しているか）
- 今は優先度が低いこと:
  - FDUSD・USDsui 等の非主流ステーブルコインの詳細調査——USDC・USDY で対応できる場合は後回しで可

## ありそうな示唆

- Base（Ethereum L2）・Solana に次いで Sui が「エージェント決済チェーン」としての地位を強化しつつある。3 チェーン間でのエコシステム競争が本格化
- ガスレス機能の普及が進むと、エージェントのチェーン選択基準が「ガスコスト」から「エコシステム（加盟店・パートナー）」に移行する可能性

## 推測 / 監視ポイント

- 推測：他の主要チェーン（Base・Polygon・Solana）が類似のガスアブストラクション機能を実装するタイムラインが短縮される可能性（競合追随）
- 監視：Sui 上での x402 対応状況（Coinbase CDP ファシリテーターの Sui 対応発表）
- 監視：Fireblocks Agentic Wallets を使用した Sui 上での最初のエージェント決済事例
- 監視：7 種のサポートステーブルコインの拡張（USDT・EURC 等の追加）

## 未解決の論点

- ガスレス転送の実装方式が「スポンサートランザクション（送付先または第三者がガスを負担）」か「プロトコルレベルの廃止（Sui が全額負担）」かは未明確
- Sui 上での x402 対応（Coinbase CDP ファシリテーターの Sui 対応）の現状

## 参考リンク

- 一次情報: [PR Newswire（2026-05-20）](https://www.prnewswire.com/news-releases/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks-302778111.html)
- 補足情報: [Sui Blog](https://blog.sui.io/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks/) / [Decrypt（2026-05-20）](https://decrypt.co/368568/sui-launches-gasless-stablecoin-transfers-with-support-from-fireblocks) / [CryptoBriefing（2026-05-20）](https://cryptobriefing.com/sui-gasless-stablecoin-transfers-fireblocks/)

## 重要度

- Medium

## 確からしさ

- High
