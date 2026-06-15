---
title: "Robinhood"
type: company
updated: 2026-06-15
category: payments
tags:
  - agentic-commerce
  - agent-payments
  - payment-authorization
  - spending-mandate
  - retail-finance
---

# Robinhood

Robinhoodは米国の大手リテール向けフィンテック企業。2026年5月、AI エージェントによる株式取引（Agentic Trading）とクレジットカード決済（Agentic Credit Card）を同時ローンチし、消費者向けエージェント決済を実規模で実装した最初の大手リテールブランドとなった。既存の Mastercard ネットワーク上で動作する点が特徴で、加盟店側の追加対応なしにエージェント起点の購買が発生する構造を作った。

この vault では、Robinhood を「カードレール上のエージェント spending mandate の先行参照実装」として追う。

---

## 現状の要約

### 何をしているか

- **Agentic Trading（ベータ）**：ユーザーが専用の分離口座を設定し、AIエージェント（Claude・ChatGPT・Codex・Cursor 他 MCP 対応エージェント）が株式の自律売買を実行。メインポートフォリオとは完全分離、取引ごとに通知、即時切断可能
- **Agentic Credit Card**：Robinhood Gold カードとは別番号の専用バーチャルカードをエージェントに付与。月額支出上限・通知・手動承認トグルによる消費者コントロールを標準装備し、エージェント購入に 3% キャッシュバックを適用
- **MCP 統合**：Robinhood MCP Server を公開し、サードパーティ AI エージェントをプラットフォームに接続できるオープン方針を採用

### 見立て

Robinhoodの実装が示した最も重要なことは「カードレールとMCPの組み合わせで、既存インフラを変えずにエージェント決済が機能する」という事実だ。x402やステーブルコイン決済が新しいレールを必要とするのに対し、Robinhoodモデルは加盟店も規制も変更せずに70万人規模で本番稼働した。「専用バーチャルカード＋支出上限＋revocable権限」という3点セットが、エージェント spending mandate のミニマル実装として業界標準の参照点になる可能性が高い。

一方で、Agentic Trading（株式取引委任）はSEC・FINRAの規制解釈が未整理のまま稼働しており、ロボアドバイザーとの規制上の境界がどう引かれるかが今後の最大の不確定要素。エージェントによる誤発注・不正利用の責任帰属も未確定で、チャージバック処理の実務設計はこれから問われることになる。

---

## Inbox との紐付け

### ローンチ・発表（2026年5月）

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-27 | [[2026-05-27_Robinhood_agentic-trading-credit-card-agent-payments]] | 一次情報（Robinhood Newsroom）ベース。認可設計の詳細・消費者コントロール・規制論点を網羅 |
| 2026-05-27 | [[2026-05-27_Robinhood_agentic-trading-agentic-credit-card]] | CNBC 独自取材ベース。MCP 統合・spending mandate の設計思想・Goldman Sachs 評価を記録 |
| 2026-05-27 | [[2026-05-27_Robinhood_agentic-credit-card-trading]] | Fortune / CNBC / Bloomberg ベース。加盟店視点・カードレール vs ステーブルコインの比較論点を記録 |

---

## 監視ポイント

- Robinhood Gold ユーザーのエージェント決済採用率（Q2 2026 決算での言及見込み）
- Agentic Trading のオプション・暗号資産・先物への拡張タイムライン
- SEC・FINRA によるエージェント株式取引の規制解釈明確化（ロボアドバイザー扱いかどうか）
- 他フィンテック（Cash App・PayPal・Revolut・Fidelity・Schwab）の類似機能展開タイムライン
- Robinhood MCP Server の公開仕様と、x402 / AP2 との互換性の有無
- エージェント起点のチャージバック・不正利用事例の初報

---

## 参考リンク

- [Robinhood Newsroom — Robinhood is now open to agents（2026-05-27）](https://robinhood.com/us/en/newsroom/robinhood-is-now-open-to-agents/)
- [Fortune（2026-05-27）](https://fortune.com/2026/05/27/robinhood-ai-agents/)
- [CNBC（2026-05-27）](https://www.cnbc.com/2026/05/27/your-ai-agent-can-now-trade-for-you-on-robinhood-and-buy-stuff-with-your-credit-card-too.html)
- [TechCrunch（2026-05-27）](https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/)
- [American Banker（2026-05-27）](https://www.americanbanker.com/payments/news/robinhood-launches-agentic-trading-and-an-agentic-credit-card)
