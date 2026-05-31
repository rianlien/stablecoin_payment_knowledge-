---
title: "Robinhood、Agentic Trading と Agentic Credit Card を同日ローンチ"
date: 2026-05-27
source: CNBC / Fortune / American Banker
source_url: https://www.cnbc.com/2026/05/27/your-ai-agent-can-now-trade-for-you-on-robinhood-and-buy-stuff-with-your-credit-card-too.html
entity: Robinhood
category: agentic-commerce / agent-payments / spending-mandate
primary_category: agentic-commerce
article_published_date: 2026-05-27
underlying_event_date: 2026-05-27
primary_source_date: 2026-05-27
tags:
  - agentic-commerce
  - agent-payments
  - spending-mandate
  - agent-identity
  - MCP
summary: "Robinhood が AI エージェントによる株式取引と実店舗・EC 購買を可能にする 2 機能を同日公開。Agentic Trading（ベータ）では分離口座内でエージェントが株式の売買を実行、Agentic Credit Card（ベータ）ではエージェントが専用バーチャルカード（Gold カードとは別番号）で購買を実行し 3% キャッシュバック付き。Claude・ChatGPT・Codex・Cursor 他 MCP 対応エージェント全般をサポート"
implications: "一般消費者向けフィンテックが AI エージェントへの実体的な金融権限委任（株式取引＋カード決済）を製品化した。エージェントへの spending mandate の実装モデルとして注目すべき事例"
importance: High
confidence: High
follow_up: "Robinhood MCP Server の公開仕様、Agentic Trading の株式以外の資産クラスへの拡張予定、Agentic Credit Card の stablecoin 対応有無"
---

## 概要
- Robinhood が 2026 年 5 月 27 日、AI エージェント向けに 2 つの新機能をベータ公開
  1. **Agentic Trading**：AI エージェントがユーザーの代わりに株式取引を自律実行
  2. **Agentic Credit Card**：AI エージェントがユーザーに代わって購買を実行する専用バーチャルカード

## 何が起きたか
- **Agentic Trading（ベータ）**
  - ユーザーが専用の「agentic trading」口座を設け、そこに割り当てた資金のみをエージェントが運用
  - メイン口座とは分離——エージェントの権限は割り当て口座内に限定
  - ポートフォリオのリバランス、テーマ（AI 株等）のモニタリング、自動取引戦略を実行
  - 取引発生のたびに通知、いつでもエージェントを即時切断可能
  - 初期サポート資産：株式のみ
- **Agentic Credit Card（ベータ）**
  - ユーザーの Robinhood Gold カードとは別番号のバーチャルカードをエージェントに付与
  - エージェントが商品を検索し、決済を自律実行
  - 3% キャッシュバック付き
  - バーチャルカードはいつでも削除可能（revocable）
- **対応エージェント**：Claude（Anthropic）、ChatGPT（OpenAI）、Codex、Codex CLI、Cursor、および Robinhood MCP を統合できるエージェント全般

## 確認された事実
- CNBC が独自取材で報道（2026-05-27）
- Fortune、American Banker が独立報道で確認
- Robinhood 公式サイトにて対応エージェントリストを公開（MCP 統合前提）
- Goldman Sachs は Robinhood 株の Buy 継続、agentic trading 機能を評価材料として明示

## なぜ重要か

### 決済事業者視点
- 従来カード業界が扱ってきた「代理人による利用（authorized user）」を AI エージェントに拡張した初の大規模消費者向け実装例。エージェントへの spending mandate をカードスキームに乗せて提供するモデルが登場した

### 加盟店視点
- Robinhood Agentic Credit Card は Mastercard ネットワーク上で動作するため、追加対応なしに既存加盟店で受け入れ可能。「エージェント受け入れ対応」をしていない加盟店でもエージェント起点の購買が発生し得る

### プロダクト視点
- 「分離口座 + revocable バーチャルカード + MCP 統合」は spending mandate の実装モデルとして参照価値が高い。AP2 の Intent Mandate・Cart Mandate・Payment Mandate と設計思想が一致する
- MCP をエージェント連携の標準インターフェイスに採用している点は、Anthropic MCP エコシステムとの統合性を示す

### 規制 / リスク視点
- 「エージェントが株式取引を行う」際の投資顧問規制（RIA 規制）への適合性は未確認。Robinhood は「ユーザーが指示を出す」という建て付けで規制対応していると見られるが、完全自律型取引との境界が曖昧
- カード不正利用発生時の責任がエージェント vs ユーザー vs Robinhood のどこに帰属するかは今後の論点

## 我々への示唆
- いま検討すべきこと:
  - Robinhood MCP Server の仕様を確認——エージェント側の実装コストと制約を把握する
  - Agentic Credit Card の「エージェント専用 revocable バーチャルカード」モデルを、自社の agent spending policy 設計の参照事例として評価
- 後で深掘りすべきこと:
  - Agentic Trading の規制対応（FINRA・SEC への届出有無）
  - 他のブローカー（Fidelity、Schwab 等）の追随タイムライン
- 今は優先度が低いこと:
  - 株式取引機能の詳細スペック（自社が金融商品取引に直接関与しないため）

## ありそうな示唆
- Robinhood MCP の成功事例が出れば、他の金融機関が同様に MCP Server を公開してエージェントに spending mandate を与えるモデルが加速する可能性が高い

## 推測 / 監視ポイント
- Agentic Credit Card が stablecoin 決済に対応するかどうか（現時点では fiat カード）
- Robinhood が Agentic Savings・Agentic Crypto Trading を追加するロードマップ

## 未解決の論点
- Agentic Trading でエージェントが取引に失敗した場合の責任帰属
- バーチャルカードの詐欺利用防止機能の仕様（現時点では不明）

## 参考リンク
- 一次情報: [CNBC（2026-05-27）](https://www.cnbc.com/2026/05/27/your-ai-agent-can-now-trade-for-you-on-robinhood-and-buy-stuff-with-your-credit-card-too.html)
- 補足情報:
  - [Fortune（2026-05-27）](https://fortune.com/2026/05/27/robinhood-ai-agents/)
  - [American Banker（2026-05-27）](https://www.americanbanker.com/payments/news/robinhood-launches-agentic-trading-and-an-agentic-credit-card)

## 重要度
- High

## 確からしさ
- High
