---
title: "Casper Network、x402 AI Toolkit を本番ローンチ——WebAssembly ネイティブ L1 初の HTTP-based マイクロペイメント"
date: 2026-06-05
source: Chainwire / Benzinga / crypto.news
source_url: https://chainwire.org/2026/06/04/casper-network-launches-ai-toolkit-with-autonomous-payments-and-app-building-tools/
entity:
  - Casper Association
  - Casper Network
category: machine-payments
primary_category: machine-payments
article_published_date: 2026-06-04
underlying_event_date: 2026-06-04
primary_source_date: 2026-06-04
tags:
  - x402
  - machine-payments
  - agentic-commerce
  - payment-protocol
  - MCP
summary: "Casper Network が 2026-06-04 に Casper AI Toolkit を Mainnet で本番ローンチ。x402 Facilitator を実装した最初の WebAssembly ネイティブ L1 ブロックチェーンとなり、AI エージェントが MCP 経由でウォレット操作・トランザクション送信・コントラクト実行を実行できる。$15 万の Agentic Buildathon を同時開始。"
implications: "x402 エコシステムが Base 以外のチェーンに拡張される最初の本番事例（WebAssembly 系 L1）。MCP 統合による開発者エコシステムの拡張は x402 の採用チェーンを多様化するが、トラフィックが分散し Base 中心の出来高への直接貢献は限定的。"
importance: Medium
confidence: High
follow_up: "Casper x402 上の最初の商業取引（Buildathon 成果物）。Base x402 と Casper x402 のトークン・決済フロー互換性確認。$15 万 Buildathon の参加者数・成果物の質。"
---

## 概要

Casper Association が 2026 年 6 月 4 日に Casper AI Toolkit の Mainnet 本番ローンチを発表。x402 Facilitator（x402 の决済プロセスを処理するオンチェーンコンポーネント）を Casper Mainnet に実装し、WebAssembly（WASM）ネイティブ L1 ブロックチェーンとして初めて HTTP-based のマイクロペイメントインフラを AI エージェント向けに提供。Model Context Protocol（MCP）との統合により、Claude・ChatGPT 等の AI エージェントが Casper ウォレットを自然言語で操作できる。

## 何が起きたか

- Casper Association が Chainwire・Benzinga を通じてプレスリリースを配信（2026-06-04）
- Casper AI Toolkit の主要コンポーネント：
  1. **x402 Facilitator**：Casper Mainnet 上で稼働する x402 決済プロセッサ。HTTP 402 レスポンスを受信した AI エージェントが CSPR / ステーブルコインで自律決済を実行できる
  2. **MCP Integration**：AI エージェントが Casper ウォレットに MCP 経由で接続し、残高照会・トランザクション送信・コントラクト状態読取・イベントモニタリングを自然言語で実行
  3. **Agentic Buildathon**：$150,000 の開発者支援プログラムを同時開始
- Casper 2 アップグレード（2025 年 Q4 完了）で導入された WASM ネイティブアーキテクチャを基盤とした最初の Agentic 対応機能
- Istanbul Blockchain Week（6/2〜）でのハンズオンワークショップと連動したリリース

## 確認された事実

- Chainwire プレスリリース（2026-06-04）で確認
- x402 Facilitator は Mainnet で稼働（Testnet 段階ではなく本番）
- MCP 統合は Claude・ChatGPT 等の主要 AI モデルに対応
- $150,000 の Buildathon は公式確認済み
- Casper Manifest（2026-05-12 公開）で予告されていたロードマップの最初の実施アイテム

## なぜ重要か

### 決済事業者視点

- x402 が Base（Coinbase）・Arbitrum・Solana 等を超えて WASM ネイティブ L1 に拡張することで、エンタープライズグレードのスマートコントラクト実行環境（WASM）での x402 活用が可能になる
- Casper は規制準拠 RWA（Real World Assets）への対応を強調している——金融機関向け RWA トークンの決済が x402 経由で実行されるシナリオを Casper は想定している

### 加盟店視点

- x402 対応 API・MCP サーバー・データサービスを Casper 上に展開する開発者が増えれば、加盟店が受け入れ可能な決済チェーンの選択肢が広がる
- 現時点では Casper エコシステムは Base・Solana と比較して小規模

### プロダクト視点

- MCP との統合設計は Base MCP（Coinbase、5 月 26 日ノート）と同様のアーキテクチャ——「AI エージェントが MCP 経由でウォレット操作 + x402 決済実行」が複数チェーンで実装される汎用パターンになりつつある
- WebAssembly ランタイムは EVM（Ethereum Virtual Machine）に対して特定のパフォーマンス・セキュリティ特性を持つ——エンタープライズ向けコントラクト実行で優位性がある場合

### 規制 / リスク視点

- Casper は WASM と GENIUS Act 準拠設計を組み合わせており、規制適合性を訴求している（詳細は Casper Manifest を参照）
- 新興 L1 としての採用リスク（流動性・エコシステム成熟度の問題）は残る

## 我々への示唆

- いま検討すべきこと:
  - x402 実装を Base 以外のチェーンに拡張する計画がある場合、Casper の WASM 対応は参照実装として有用。Buildathon 成果物を確認する
- 後で深掘りすべきこと:
  - Casper x402 Facilitator の技術仕様と Base x402 との互換性——同一の x402 クライアントが Casper と Base を透過的に利用できるかどうか
  - Casper Manifest の規制準拠 RWA 計画——金融機関がステーブルコイン / トークン化資産を Casper 上で発行する場合のエージェント決済との接続シナリオ
- 今は優先度が低いこと:
  - Casper エコシステムへの直接投資・統合（採用規模が Base・Solana と比較して現時点では小さい）

## ありそうな示唆

- x402 の「マルチチェーン化」は不可避。Casper の参加は Base（Coinbase）中心の現エコシステムを多様化し、x402 Foundation（Linux Foundation 傘下）の「誰でも参加できるオープン標準」としての性格を強化する
- Buildathon で有力な成果物が出た場合（特に金融機関向け RWA + x402 の組み合わせ）、Casper x402 が独自のニッチ（規制準拠 RWA 決済）を確立する可能性がある

## 推測 / 監視ポイント

- $150,000 Buildathon の成果発表（6〜7 月）
- Casper x402 の最初の商業取引の発表
- x402 Foundation（Linux Foundation）による Casper の公式 x402 実装としての認定有無

## 未解決の論点

- Casper x402 Facilitator が処理できる決済通貨（CSPR のみか USDC 等のステーブルコインも対応か）
- Base x402 との相互運用性（エージェントが一つのウォレットで Base / Casper 両方で x402 決済できるか）
- Casper の日本・東アジア市場での展開計画

## 参考リンク

- 一次情報: [Chainwire（2026-06-04）](https://chainwire.org/2026/06/04/casper-network-launches-ai-toolkit-with-autonomous-payments-and-app-building-tools/)
- 補足情報: [Benzinga（2026-06-04）](https://www.benzinga.com/pressreleases/26/06/53002364/casper-network-launches-ai-toolkit-becoming-first-webassembly-native-blockchain-with-live-x402-paym), [crypto.news（2026-06-04）](https://crypto.news/casper-network-launches-ai-toolkit-with-autonomous-payments-and-app-building-tools/)

## 重要度

- Medium

## 確からしさ

- High（公式プレスリリース確認済み）
