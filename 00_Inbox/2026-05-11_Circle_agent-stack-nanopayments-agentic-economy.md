---
title: "Circle Agent Stack：USDC エージェント向け金融インフラ一式をローンチ"
date: 2026-05-11
source: Circle 公式プレスルーム
source_url: https://www.circle.com/pressroom/circle-launches-ai-infrastructure-to-power-the-agentic-economy
entity: Circle
category: 企業発表
primary_category: agentic-payments
article_published_date: 2026-05-11
underlying_event_date: 2026-05-11
primary_source_date: 2026-05-11
tags:
  - agentic-commerce
  - payments
  - stablecoin
  - protocol
  - psp
summary: "Circle が 2026-05-11 に Circle Agent Stack を発表。Agent Wallets（ポリシー管理型）・Nanopayments（最小 $0.000001、ガスレス）・Circle CLI・Agent Marketplace の 4 製品で AI エージェント向け金融インフラを一括提供。USDC を機械間決済の基軸通貨に据え、同日 Arc ブロックチェーンの $222M プレセール（BlackRock・a16z・ARK 参加）も発表。"
implications: "USDC の発行体である Circle 自身がエージェント決済スタック全体を垂直統合した。PSP・PayFac はエージェント向け決済において Circle との競合・補完ポジションを再定義する必要がある。Nanopayments の $0.000001 最小単位は x402・MPP のマイクロペイメントユースケースに直接対応。"
importance: High
confidence: High
follow_up: "Agent Marketplace に掲載されるサービス・手数料・対応チェーンの詳細確認。Arc ブロックチェーンの技術仕様と既存 Base/Solana との差別化ポイント。Circle Gateway の Nanopayments が GENIUS Act のペイメントステーブルコイン定義に適合するかの法的検討。"
---

## 概要

- Circle が 2026-05-11 に Circle Agent Stack を正式発表。AI エージェントが自律的に資産を保持・送金・サービス購入できる金融インフラを一括提供した。
- 4 製品：Agent Wallets、Nanopayments（powered by Circle Gateway）、Circle CLI、Agent Marketplace。
- 同日、エンタープライズ向けブロックチェーン Arc の ARC トークンプレセール $222M を発表。BlackRock・a16z crypto・ARK Invest 等が参加。Arc FDV は $30 億。

## 何が起きたか

- **Circle Agent Stack** として以下 4 製品を同日リリース：
  1. **Agent Wallets**：許可不要・ポリシー制御型ウォレット。エージェントが自律的に資金保持・送金・管理できる
  2. **Nanopayments（powered by Circle Gateway）**：ガスレスで最小 $0.000001 の USDC 転送。マシンスピード・大規模向けの高頻度・サブセント・機械間決済フロー用
  3. **Circle CLI**：開発者・AI エージェント向けコマンドラインインターフェース
  4. **Agent Marketplace**：エージェントサービスの一覧ディレクトリ（エージェントがサービスを探して購入できる）
- エントリポイントは agents.circle.com。USDC を機軸通貨として設計。
- Arc ブロックチェーン：「インターネットの Economic OS」として設計されたエンタープライズ向け L1。Visa がアンカーバリデーターとして参加。ARC トークン $222M プレセール。

## 確認された事実

- 発表日：2026-05-11（Circle 公式プレスルーム・投資家向け IR・The Paypers・Blockhead 等が確認）
- Nanopayments の最小送金単位：$0.000001 USDC、ガスレス
- Arc トークンプレセール調達額：$222M（BlackRock、a16z crypto、ARK Invest 参加）
- Arc FDV：$30 億
- 製品は即日提供開始（agents.circle.com）

## なぜ重要か

### 決済事業者視点

- USDC 発行体が決済インフラ上流（ウォレット・マーケットプレイス・CLI）を自社で垂直統合。独立系 PSP は、Circle エコシステム上のレイヤーとして機能するか、非 USDC スタックで差別化するかを選択する局面が近づいた。
- Nanopayments の $0.000001 最小単位は、x402 や MPP のマイクロペイメントユースケースで実際に使える決済原子単位として設計されており、API 課金・AI 推論課金・エージェント間決済に直接対応。

### 加盟店視点

- Agent Marketplace を通じてエージェントがサービスを発見・購入する仕組みが整備された。加盟店がここに掲載されることで、エージェントからの自律的購入流入が期待できる。
- ただし、現行加盟店がステーブルコイン受取可能かどうか（法定通貨換算・オフランプ設計）は別途検討が必要。

### プロダクト視点

- Circle CLI + Agent Wallets + Nanopayments の組み合わせは、エージェントが「口座開設なし・KYC なし・事前登録なし」で即時に決済できるパターンを実装可能にする。
- x402（HTTP 402 Payment Required）との統合が可能かどうかが次の設計ポイント。

### 規制 / リスク視点

- GENIUS Act で「受動的利回り禁止・1:1 準備金義務」が確定している中、Nanopayments の円滑な送金がペイメントステーブルコイン定義に適合するかは検討が必要。
- Arc ブロックチェーンの ARC トークンが証券として扱われるかどうかは CLARITY Act の帰趨に依存する。

## 我々への示唆

- いま検討すべきこと:
  - agents.circle.com を確認し、Agent Wallets・Nanopayments の API 仕様・対応チェーン・手数料を評価する
  - 自社のエージェント決済スタック設計に Nanopayments を採用する場合のコスト・速度・リスクを検討する
- 後で深掘りすべきこと:
  - Arc ブロックチェーンの技術仕様（Visa バリデーター参加の意味・既存 L2 との違い）
  - Circle Gateway の法的位置付け（送金業・暗号資産交換業の観点）
- 今は優先度が低いこと:
  - ARC トークンの投資観点の分析（今回は決済インフラ視点での評価を優先）

## ありそうな示唆

- Circle は USDC の発行者であることに加え、エージェント経済の決済 OS になろうとしている。AWS AgentCore（Coinbase + Stripe 統合）と並んで、「誰のスタックの上にエージェント決済が走るか」という競争が本格化した。
- Agent Marketplace が成立すれば、エージェントが「どのサービスを使うか」を自律的に選択する際に Circle エコシステム内のサービスが優先される可能性があり、これはウォールドガーデン的な優位性を持つ。

## 推測 / 監視ポイント

- Nanopayments が x402 や MPP との相互運用性をどう設計するか（独自仕様か標準準拠か）
- Agent Marketplace に登録される最初のサービスカテゴリ（AI API・データプロバイダー・コンテンツ等）
- Arc ブロックチェーンの Visa バリデーター参加が、カード決済ネットワークとの接続設計にどう影響するか
- Circle の Q1 2026 業績（利益増・売上未達）と Arc ローンチの資金調達が IPO 後戦略にどう位置付けられるか

## 未解決の論点

- Nanopayments の対応チェーン（Arc のみか、Base・Solana も含むか）
- Agent Wallets のポリシー制御の詳細（支出上限・カテゴリ制限・マルチシグ等）
- Agent Marketplace の手数料体系と掲載条件
- USDC 決済をエージェントが行う場合の KYC/AML 適用範囲

## 参考リンク

- 一次情報: [Circle 公式プレスルーム（2026-05-11）](https://www.circle.com/pressroom/circle-launches-ai-infrastructure-to-power-the-agentic-economy)
- 一次情報: [Circle IR（2026-05-11）](https://investor.circle.com/news/news-details/2026/Circle-Launches-AI-Infrastructure-to-Power-the-Agentic-Economy/default.aspx)
- 補足情報: [Circle ブログ：Circle Agent Stack 詳細（2026-05-11）](https://www.circle.com/blog/introducing-circle-agent-stack-financial-infrastructure-for-the-agentic-economy)
- 補足情報: [Blockhead（2026-05-12）](https://www.blockhead.co/2026/05/12/circle-launches-agent-stack-to-put-usdc-at-the-centre-of-machine-to-machine-payments/)
- 補足情報: [Crowdfund Insider：Nanopayments 詳細](https://www.crowdfundinsider.com/2026/05/278131-circle-introduces-nanopayments-framework-for-agentic-ai-economies-on-arc/)

## 重要度

- High

## 確からしさ

- High（Circle 公式プレスルーム・IR・複数媒体が確認。製品仕様の細部は公式ドキュメント要確認）
