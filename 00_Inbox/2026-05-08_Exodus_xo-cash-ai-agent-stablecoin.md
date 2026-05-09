---
title: "Exodus XO Cash：AI エージェント向け初のステーブルコイン・AgentKit SDK 正式ローンチ"
date: 2026-05-08
source: "GlobeNewswire / CoinTelegraph / AMBCrypto"
source_url: "https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/exodus-launches-xo-cash-as-the-first-stablecoin-built-for-ai-agents.html"
entity: "Exodus Movement / MoonPay / Monavate"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - agent-payments
  - wallet
  - stablecoin
  - payments
summary: "Exodus Movement（NYSE: EXOD）が 2026 年 5 月 8 日、AI エージェント専用設計の Solana ベースのステーブルコイン「XO Cash」と、エージェントウォレットを API 1 コールで発行できる SDK「AgentKit」を正式ローンチ。MoonPay・Monavate との共同開発で、エージェントが秘密鍵を持たずに支払えるアーキテクチャと、ユーザーが支出上限・利用可能加盟店・レート制限を設定できる制御モデルを実装。Visa 加盟店でのデビットカード決済にも同一の支出ルールを適用する。"
implications: "AWS AgentCore（x402）・MoonAgents Card（Mastercard）に続く第三の AI エージェント決済インフラが登場。Exodus Pay の既存カードインフラを再利用した実装は実績ある設計だが、USDC/USDT との連携設計が既存の x402・MPP インフラとどう接続されるかが競争上の重要論点。"
follow_up: "XO Cash と USDC の準備金・裏付け構造の詳細、AgentKit の開発者採用状況、Visa 加盟店決済のリアルタイム清算フロー、x402 との相互運用性"
article_published_date: 2026-05-08
underlying_event_date: 2026-05-08
primary_source_date: 2026-05-08
---

## 概要

- Exodus Movement（NYSE: EXOD）が AI エージェント専用設計のステーブルコイン「XO Cash」と「AgentKit SDK」を 2026 年 5 月 8 日にローンチ
- Solana 上で発行、MoonPay・Monavate との共同開発
- エージェントが秘密鍵を保持せずに支払い、ユーザーが支出ルールをいつでも設定・変更できる制御モデル
- 単一 API コールでエージェントにウォレットとデビットカードを発行可能

## 何が起きたか

- **発表日**：2026 年 5 月 8 日（GlobeNewswire 公式プレスリリース）
- **発行体**：Exodus Movement, Inc.（NYSE: EXOD）
- **ローンチした製品**：
  - **XO Cash**：Solana 上の AI エージェント向けステーブルコイン
  - **AgentKit SDK**：エージェントウォレットを API 1 コールで発行するデベロッパー向け SDK
- **開発パートナー**：MoonPay（ステーブルコイン決済インフラ）・Monavate（Mastercard プリンシパルメンバー、カードインフラ）
- **主要な仕様**：
  - エージェントは秘密鍵を保持しない（Exodus Pay 残高から直接支出するアーキテクチャ）
  - ユーザーが各エージェントに対して以下のルールを設定・随時変更可能：1日あたり支出上限・1取引あたり上限・利用可能加盟店・レート制限
  - AgentKit から API 1 コールで Visa デビットカードも発行可能（同一のカードインフラ）
  - Visa 加盟店ならどこでも決済可能。カード決済にもウォレット側の支出ルールを自動適用
  - XO Cash ↔ USDC / USDT の自動変換（単一トランザクション内で完結）
- **MoonAgents Card との関係**：MoonPay が 5 月 1 日に発表した MoonAgents Card（Monavate インフラ使用）と同一の決済基盤を利用する別製品。XO Cash は Exodus のブランドで発行し、AgentKit で開発者向けに提供する点が異なる

## なぜ重要か

### 決済事業者視点

- Solana 上の AI エージェント決済の「ウォレット＋カード」一体型インフラが既存の規制済みカードインフラ（Monavate = Mastercard プリンシパルメンバー）を再利用して実装された。これは Monavate のインフラが複数の AI エージェント向け製品（MoonAgents Card・XO Cash）の基盤になっていることを意味し、Monavate の市場でのポジションが急速に強化されている
- USDC/USDT への自動変換サポートは、x402・MPP 等の既存決済プロトコルとの接続を想定した設計と読める

### 加盟店視点

- Visa 加盟店にとって追加の統合は不要。エージェントが発行した仮想デビットカードからの決済は既存の Visa ネットワーク経由で処理される
- ユーザー設定の支出ルール（許可加盟店リスト）は加盟店に対して新たな支出制御の層を作る。加盟店が「エージェントによる AI 購買」を識別・管理する仕組みはまだ未整備

### プロダクト視点

- 「エージェントは秘密鍵を管理しない」という設計は AWS AgentCore（x402）・MoonAgents Card と共通するアーキテクチャ思想。エージェント決済インフラのデファクトアーキテクチャが固まりつつある
- AgentKit の「API 1 コール＝ウォレット＋カード発行」という開発者体験は、MoonPay の AgentKit と同名・同コンセプトだが異なる製品。名称の類似が開発者にとって混乱要因になる可能性がある

### 規制 / リスク視点

- Exodus は米国の送金業法（MTL）ライセンスを所持しているかどうか不明。OwlTing（40 州 MTL）と比較すると、米国での規制対応状況を確認する必要がある
- XO Cash の準備金構造・裏付け資産の透明性については公表情報が少ない。発行体として Circle や Paxos 等の規制済み発行体を使用しているか、独自発行かが重要な確認事項

## 我々への示唆

- いま検討すべきこと:
  - MoonPay AgentKit・Exodus AgentKit・AWS AgentCore・Pay.sh の 4 製品を技術仕様・対応チェーン・規制対応・開発者体験の軸で比較整理し、自社エージェント決済プロダクトの技術選択の判断材料とする
  - XO Cash の準備金・裏付け構造を確認し、発行体リスクを評価する
- 後で深掘りすべきこと:
  - AgentKit の開発者採用状況（GitHub スター数・ドキュメント充実度）
  - XO Cash と既存 x402 エコシステム（AgentCore・Pay.sh）との相互運用性の技術的詳細
  - Monavate が「MoonAgents Card + Exodus XO Cash + 他社」の複数 AI エージェント向け製品を同時に支援している構図が競争上どんな意味を持つか
- 今は優先度が低いこと:
  - XO Cash のトークノミクス詳細（AI エージェント決済プロダクト採用の観点では二次的）

## 未解決の論点

- XO Cash の準備金は何で裏付けられているか？独自発行か規制済み発行体経由か？
- Exodus が米国で送金業として適切にライセンスを取得しているか？
- XO Cash エージェントウォレットから USDC を直接支払えるとすれば、USDC の発行体である Circle との関係は？
- MoonPay AgentKit と Exodus AgentKit は競合製品か、それとも同一インフラ上の異なるレイヤーか？

## 参考リンク

- 一次情報:
  - [GlobeNewswire 公式プレスリリース（2026-05-08）](https://www.globenewswire.com/news-release/2026/05/08/3291008/0/en/exodus-launches-xo-cash-as-the-first-stablecoin-built-for-ai-agents.html)
- 補足情報:
  - [CoinTelegraph — Exodus launches AI agent-focused stablecoin on Solana](https://cointelegraph.com/news/exodus-launches-ai-agent-focused-stablecoin-on-solana)
  - [AMBCrypto — Exodus launches XO Cash as AI agents become crypto's next payments battleground](https://ambcrypto.com/exodus-launches-xo-cash-as-ai-agents-become-cryptos-next-payments-battleground/)
  - [関連ノート：MoonPay MoonAgents Card（2026-05-01）](2026-05-01_MoonPay_moonagents-card-mastercard-ai-agents.md)
  - [関連ノート：AWS AgentCore Payments（2026-05-07）](2026-05-07_AWS_bedrock-agentcore-payments-x402.md)

## 重要度

- Medium

## 確からしさ

- High
