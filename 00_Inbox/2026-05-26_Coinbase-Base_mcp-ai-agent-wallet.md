---
title: "Coinbase Base、AI エージェント向け MCP サーバーをローンチ——ChatGPT・Claude からオンチェーン操作が可能に"
date: 2026-05-26
source: "Fortune / CoinDesk / CryptoTimes"
source_url: "https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/"
entity: "Coinbase / Base"
category: "agentic-commerce"
primary_category: "agent-payments"
article_published_date: 2026-05-26
underlying_event_date: 2026-05-26
primary_source_date: 2026-05-26
tags:
  - agent-payments
  - agentic-commerce
  - machine-payments
  - x402
  - stablecoin-infrastructure
summary: "Coinbase の Layer-2 ネットワーク Base が 2026 年 5 月 26 日、Model Context Protocol（MCP）サーバー「Base MCP」をローンチ。ChatGPT・Claude・Codex・Cursor などの AI エージェントが Base Account（スマートウォレット）に接続し、自然言語でトークン送金・スワップ・DeFi 操作を実行できるようになった。秘密鍵は TEE（Trusted Execution Environment）のセキュアエンクレーブ内で管理され、AI エージェントがアクセスする構造ではない。エージェントごとの支出上限・ホワイトリスト設定をインフラ層で強制できる設計。Moonwell・Morpho・Uniswap・Aerodrome 等 7 つの DeFi プロトコルとのスキルプラグインを同時リリース。Coinbase が進める x402 普及戦略の一環として位置づけられる。"
implications: "AI エージェントがウォレットを直接操作してトークン送金・スワップ・DeFi を実行できるインフラが、ユーザー承認フロー付きで本番提供された。x402 の『エージェントが自律的に決済する』ユースケースに、オンチェーン資産管理・DeFi 操作という新たな次元が加わる。エージェントへの決済権限委任設計における MPC vs. TEE vs. スマートウォレットの選択肢が具体化した。"
importance: High
confidence: High
follow_up: "Base MCP の x402 ペイメントとの統合（エージェントが DeFi 操作と同時に x402 決済も行えるか）、テンプレート支出ルールの公開仕様、Coinbase CDP の Agentic Wallets と Base MCP の機能分担の確認、他の AI エージェントフレームワーク（LangChain・AutoGPT 等）対応の発表"
---

## 概要

2026 年 5 月 26 日、Coinbase の Ethereum Layer-2 ネットワーク Base が「Base MCP」をローンチした。MCP（Model Context Protocol）を通じて ChatGPT・Claude・Codex・Cursor などの AI クライアントが Base Account（スマートウォレット）に接続し、自然言語でオンチェーン操作を実行できるようになる。

## 何が起きたか

- **Base MCP の機能**：AI エージェントが自然言語プロンプトで以下を実行できる
  - トークン残高の確認・取引履歴の表示
  - トークン送金（USDC 等）
  - トークンスワップ
  - DeFi プロトコル操作（流動性提供、レンディング等）

- **セキュリティアーキテクチャ**：
  - 秘密鍵は TEE（Trusted Execution Environment）のセキュアエンクレーブ内で生成・保管
  - AI エージェントは秘密鍵に直接アクセスしない設計
  - 操作実行前に別ウォレット UI でユーザーが承認 / 却下するフロー
  - トランザクションの事前シミュレーション機能（透明性確保）

- **エージェント制御機能**：
  - エージェントごとの支出上限設定
  - ホワイトリスト化された取引相手のみに制限可能
  - いずれもインフラ層で強制執行

- **ローンチ時のスキルプラグイン（7 つ）**：Moonwell（レンディング）・Morpho（融資最適化）・Uniswap（DEX）・Aerodrome（流動性 DEX）・Avantis（パーペチュアル）・Bankr・Virtuals

## 確認された事実

- 発表日：2026 年 5 月 26 日（Fortune, CoinDesk 等が同日報道）
- Base Account（スマートウォレット）を AI クライアントに接続する MCP サーバーとして実装
- 対応 AI クライアント：ChatGPT、Claude、Codex、Cursor（発表時点）
- 「Coinbase の x402 決済標準普及戦略の一環」と Fortune・Fortune 等が位置づけを明記
- x402 Foundation は Linux Foundation ホストのガバナンス組織

## なぜ重要か

### 決済事業者視点

- ウォレット管理・スワップ・送金が AI エージェント経由で実行可能になることで、エンドユーザーが支払いのためにウォレット操作する学習コストが下がる。コンシューマー向けエージェントがステーブルコイン決済を「透明に」仲介するシナリオが具体化する。
- TEE + ユーザー承認フローの組み合わせは「エージェントへの資金委任」のセキュリティモデルとして実運用可能な設計。PSP がエージェント決済を取り扱う際の参照モデルになりうる。

### 加盟店視点

- Base 上の DeFi プロトコルとのネイティブな統合により、API を提供する DeFi/TradFi サービスが「エージェント経由の自然言語決済」を受け入れる準備が整う。
- x402 対応 API が Base MCP に乗れば、AI エージェントが「API 呼び出し → 自動 x402 決済」を透過的に実行するシナリオが現実的になる。

### プロダクト視点

- TEE + スマートウォレットによる「エージェントが秘密鍵を持たない」設計は、MPC ベース（Fireblocks Agent Wallets）・Circle Agent Wallets とは異なるアーキテクチャ選択。各設計のセキュリティトレードオフの比較が必要。
- スキルプラグイン方式は、エージェントの行動範囲を限定された DeFi 操作に絞り込む具体的な実装。「何をできるか」をプラグインとして管理するモデルは自社エージェント設計の参照候補。

### 規制 / リスク視点

- TEE のセキュアエンクレーブ内での鍵管理は、GENIUS Act 下での「決済手段の保管主体」の定義において、カストディアルとセルフカストディの中間的な性質を持つ可能性がある。規制当局の解釈が未確定。
- ユーザーが承認を拒否できるフローは、CFES ガイドライン（2026-05-13）の「人間による最終的な制御」要件を実質的に満たす設計。

## 我々への示唆

- いま検討すべきこと:
  - Base MCP の x402 支払い統合の有無を確認——エージェントが DeFi スワップ後に x402 API 料金を払うシーケンスが実装されているか
  - Base MCP の支出上限・ホワイトリストの API 仕様を確認し、自社のエージェント決済設計に適用できるか評価する
- 後で深掘りすべきこと:
  - TEE ベース vs. MPC ベース（Fireblocks）vs. スマートコントラクトベース（Circle）のセキュリティ・UX・規制適合性の比較マトリクス作成
  - Moonwell / Morpho 等の DeFi スキルプラグインの仕様——AI エージェントが「自律的に資産運用する」シナリオのリスク管理
- 今は優先度が低いこと:
  - 個別 DeFi プロトコルの詳細——DeFi プロトコルとして評価するよりも「エージェント決済インフラ」として評価する

## ありそうな示唆

- Base MCP は「ChatGPT や Claude がユーザーのウォレットで決済を代行する」という消費者向けエージェント決済の最も直接的な実装例となった。これが x402 と組み合わされると、AI エージェントがコンテンツ・API・サービスを自律的に購入して支払いまで行うシナリオが標準的なユーザーフローになりうる。
- Coinbase が Base MCP→x402 という統合ロードマップを進める場合、「Base = エージェント決済の標準実行環境」としてのポジションを強化する可能性がある。

## 推測 / 監視ポイント

- Base MCP と x402 の直接統合（エージェントが x402 支払いを MCP 経由で実行できるか）が発表されるか
- TEE ベースのスマートウォレット設計が規制当局に「自己カストディ」と認められるかどうか
- 他の AI フレームワーク（LangChain・CrewAI・AutoGen 等）への MCP 対応拡張発表
- Base MCP の利用状況（アクティブエージェント数・取引量）の公開

## 未解決の論点

- Base MCP の承認フローと x402 の「pre-authorized spending」の整合性——ユーザーが毎回承認する設計では大量マイクロペイメントには不向き。どこで自動化するか
- Coinbase CDP の Agent Wallets（Circle Agent Stack との競合）と Base MCP の機能重複・分担
- DeFi スキルプラグインの「承認なし自動実行」モードの有無

## 参考リンク

- 一次情報: [Fortune（2026-05-26）](https://fortune.com/2026/05/26/coinbase-pushes-further-into-ai-payments-with-new-mcp-for-base-network/)
- 補足情報: [CoinDesk（2026-05-26）](https://www.coindesk.com/tech/2026/05/26/coinbase-s-base-launches-ai-tool-for-chatgpt-to-manage-crypto-wallets-and-defi-apps)
- 補足情報: [CryptoTimes（2026-05-26）](https://www.cryptotimes.io/2026/05/26/coinbase-pushes-ai-crypto-fusion-with-new-base-mcp-tool/)
- 補足情報: [Bitcoin.com News（2026-05-26）](https://news.bitcoin.com/base-launches-mcp-gateway-letting-claude-and-chatgpt-execute-onchain-defi-actions/)

## 重要度

- High

## 確からしさ

- High（Fortune / CoinDesk の同日報道で確認）
