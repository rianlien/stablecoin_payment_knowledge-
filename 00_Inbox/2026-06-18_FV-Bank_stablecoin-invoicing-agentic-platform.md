---
title: "FV Bank、米国初のチャーター銀行によるステーブルコイン請求書発行をローンチ——agentic 対応仮想カードも開発中"
date: 2026-06-23
source: BusinessWire / AlexaBlockchain / CoinPaprika
source_url: https://www.businesswire.com/news/home/20260618149734/en/FV-Bank-Expands-Beyond-Digital-Banking-Launches-Unified-Fintech-Platform-for-Stablecoins-Payments-and-Programmable-Finance
entity: FV Bank
category: merchant-PSP-readiness / stablecoin-payments
primary_category: merchant-PSP-readiness
article_published_date: 2026-06-18
underlying_event_date: 2026-06-18
primary_source_date: 2026-06-18
tags:
  - stablecoin
  - merchant-readiness
  - psp
  - stablecoin-invoicing
  - agentic-commerce
summary: "FV Bank（米国チャーター銀行・プエルトリコ）が 2026-06-18 に統合フィンテックプラットフォームを発表。ステーブルコイン請求書発行機能（USDC / PYUSD 受け取り → 即時 USD 着金）を米国チャーター銀行として初めてリリース。続いてステーブルコイン国際送金・agentic 対応仮想カード・API マネージドアカウント・開発者向け API を今後ローンチ予定。"
implications: "規制銀行がステーブルコイン決済のフロントエンドとなることで、業者向けオンランプ・請求業務が正規の銀行インフラ内で完結するモデルが登場。agentic 対応仮想カードは AI エージェントが法人口座から直接支払いを実行できるインフラの先行形態。"
importance: Medium
confidence: High
follow_up: "agentic-ready 仮想カードの仕様・リリース時期・API の詳細、GENIUS Act 最終規則（7/18）後の PPSI 要件との適合性確認"
---

## 概要

FV Bank（米国チャーター銀行、プエルトリコ本社）が 2026 年 6 月 18 日に統合フィンテックプラットフォームを正式発表した。米国チャーター預金銀行として初めてステーブルコイン請求書発行（Stablecoin Invoicing）機能をリリース。将来的にはエージェント対応仮想カードや開発者 API を追加予定で、ステーブルコイン決済の B2B フロントエンドとして機能するインフラを構築中。

## 何が起きたか

- **Stablecoin Invoicing リリース（即日）**：事業者がダッシュボードから品目付き請求書を作成し、メールまたは決済リンクで送付。受取人が USDC または PYUSD で支払うと、数秒以内に USD として FV Bank 口座に着金
- **米国初事例**：米国チャーター預金銀行としてステーブルコイン請求書発行を提供するのは FV Bank が初
- **ロードマップ公開済みの追加機能**：
  1. 統合決済回収（unified payment collection）
  2. ステーブルコインを使った国際送金（cross-border payments）
  3. **agentic-ready 仮想カード（agentic-ready virtual cards）**
  4. API マネージドアカウント
  5. 開発者 API
- **既存インフラ**：FV Bank はすでに USDC・USDT・PYUSD の直接預金・出金・送受信に対応。45 以上の通貨でリアルタイム清算が可能

## 確認された事実

- 発表日：2026-06-18（BusinessWire プレスリリース）
- 会社概要：FV Bank は米国 SEC・FDIC の規制を受けるチャーター銀行（Puerto Rico IFE ライセンス）
- Stablecoin Invoicing は 6/18 時点で即時提供開始
- 支払い可能通貨：USDC・PYUSD（受け取り後即時 USD 変換・着金）
- agentic-ready 仮想カードは発表時点でロードマップ記載のみ、提供時期は未公開

## なぜ重要か

### 決済事業者視点

- 規制銀行インフラが「ステーブルコイン受け取り→法定通貨着金」を直接提供することで、FinTech 企業や非銀行事業者が担っていた変換レイヤーに銀行が競合参入
- GENIUS Act 発効後（2026 年末〜2027 年初）、PPSI ライセンスを持つステーブルコイン発行体と規制銀行が直接連携するモデルの先行事例として注目

### 加盟店視点

- 請求書発行から USDC/PYUSD 受け取り、USD 着金まで銀行ダッシュボード上で完結。法人がステーブルコイン請求書を出す際の「オンランプを自社で用意する」手間が不要になる
- 受け取り通貨リスク（USDC 価格変動）がゼロ（即時 USD 変換）のため、加盟店の経理処理が簡素化

### プロダクト視点

- **agentic-ready 仮想カード**が実現すれば、AI エージェントが法人口座に紐づいた仮想カードを使って自律的に支出を実行できる。Stripe・Mastercard が進める Agent Pay / MPP と類似するが、規制銀行口座上で完結する点で異なる
- 開発者 API の追加により、FV Bank インフラをプログラム制御できるエージェント向け決済バックエンドとなる可能性

### 規制 / リスク視点

- FV Bank は既存の規制銀行インフラのため、GENIUS Act 下の PPSI 規制とは別トラック（銀行は PPSI 適用外）。銀行が提供するステーブルコイン請求書が GENIUS Act 最終規則の適用範囲かどうかは 7/18 以降の規則テキストで確認が必要

## 我々への示唆

- いま検討すべきこと:
  - FV Bank の Stablecoin Invoicing を B2B 請求書発行で評価。特に「USDC で送付→即時 USD 着金」が既存の Stripe/Coinbase Commerce との比較でコスト・速度・法人向け UX に優位があるか
  - agentic-ready 仮想カードのロードマップ詳細（仕様・時期・API）を問い合わせ or 発表を監視
- 後で深掘りすべきこと:
  - FV Bank API マネージドアカウントの設計（エージェントからの API コール可否、認証モデル）
  - GENIUS Act 最終規則化（7/18）後に FV Bank の銀行サービスが PPSI 規制との役割分担がどうなるか
- 今は優先度が低いこと:
  - FV Bank への直接採用（米国法人向けサービスが確認できるまで）

## ありそうな示唆

- 規制銀行が Stablecoin Invoicing と agentic-ready 仮想カードを組み合わせると、「法人がエージェントに銀行口座連動の仮想カードを渡す」という形のエージェント支出委任が、コンプライアンス対応済みのインフラ上で実現する。これは Stripe MPP や Mastercard AP4M の「PSP が決済ネットワークを通じてエージェントに spending mandate を発行する」モデルとは異なる「銀行口座ファーストのエージェント支出委任」モデル

## 推測 / 監視ポイント

- FV Bank agentic-ready 仮想カードの対応ネットワーク（Visa/Mastercard/カード番号型 vs API 型）が x402 や AP4M との接続可能性を決める
- agentic-ready 仮想カードが実際に AI エージェントフレームワーク（Coinbase AgentKit・Stripe Agentic Commerce Suite）と API 統合される場合、FV Bank は規制銀行として「エージェント支出のラストマイルインフラ」ポジションに入る

## 未解決の論点

- agentic-ready 仮想カードのリリース時期と仕様（API スタック・対応決済ネットワーク）
- GENIUS Act 最終規則下での FV Bank の位置づけ（銀行は PPSI ではないが、PPSI 発行体と提携するケースの規制当局解釈）
- PYUSD 受け取り対応は PayPal との何らかの契約があるのか（単に PYUSD を受け取れる設計か）

## 参考リンク

- 一次情報: [BusinessWire プレスリリース（2026-06-18）](https://www.businesswire.com/news/home/20260618149734/en/FV-Bank-Expands-Beyond-Digital-Banking-Launches-Unified-Fintech-Platform-for-Stablecoins-Payments-and-Programmable-Finance)
- 補足情報: [AlexaBlockchain「First US-Chartered Depository Bank to Offer Stablecoin Invoicing」](https://alexablockchain.com/first-u-s-chartered-depository-bank-to-offer-stablecoin-invoicing/) / [CoinPaprika（2026-06-18）](https://coinpaprika.com/news/fv-bank-launches-unified-fintech-platform/)

## 重要度

- Medium

## 確からしさ

- High（BusinessWire 一次プレスリリース確認済み）
