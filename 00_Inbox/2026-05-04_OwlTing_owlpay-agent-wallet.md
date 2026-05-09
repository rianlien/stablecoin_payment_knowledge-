---
title: "OwlTing OwlPay Agent Wallet：40 州 MTL × Visa Direct 対応の AI エージェント向けセルフカストディウォレット正式ローンチ"
date: 2026-05-04
source: "GlobeNewswire / The Fintech Times / Finextra"
source_url: "https://www.globenewswire.com/news-release/2026/05/04/3286859/0/en/OwlTing-Group-NASDAQ-OWLS-Launches-OwlPay-Agent-Wallet-Targeting-the-Emerging-Multi-Trillion-Dollar-Agentic-Commerce-Economy.html"
entity: "OwlTing Group"
category: "agentic-commerce"
tags:
  - agentic-commerce
  - agent-payments
  - wallet
  - payments
  - compliance
summary: "OwlTing Group（NASDAQ: OWLS）が 2026 年 5 月 4 日、AI エージェントがユーザーに代わってステーブルコインの送受信・管理を行えるセルフカストディウォレット「OwlPay Agent Wallet」を正式ローンチ。米国 40 州の MTL と Visa Direct 連携を備えた規制対応済みインフラとして、ETH・Stellar・Solana に対応。エージェントがウォレット操作を技術設定不要で自動習得する組み込みエージェントスキルを特徴とする。"
implications: "規制対応済み（MTL 40 州）の AI エージェント向けウォレットが実用化されたことで、コンプライアンスを重視する金融機関・PSP がエージェント向け決済インフラを採用する際の参照モデルになり得る。Visa Direct 連携はデビットカードでのオンランプを見据えた設計で、法定通貨←→ステーブルコインの往来が規制の範囲内で実現できるかが重要な確認点。"
follow_up: "Visa Direct 対応のローンチ時期、デビットカード連携の具体的なユーザーフロー、MTL 保有による OFAC/AML コンプライアンスの実装詳細、他のエージェント決済インフラ（x402・MPP・AgentCore）との連携可能性"
article_published_date: 2026-05-04
underlying_event_date: 2026-05-04
primary_source_date: 2026-05-04
---

## 概要

- OwlTing Group（NASDAQ: OWLS）が AI エージェント向けセルフカストディウォレット「OwlPay Agent Wallet」を 2026 年 5 月 4 日に正式ローンチ
- 秘密鍵はユーザーデバイスにローカル保存するセルフカストディ設計
- 米国 40 州の Money Transmitter License（MTL）と Visa Direct 連携を規制インフラとして保有
- ETH エコシステム・Stellar・Solana の 3 チェーン対応

## 何が起きたか

- **発表日**：2026 年 5 月 4 日（GlobeNewswire 公式プレスリリース）
- **発行体**：OwlTing Group, Inc.（NASDAQ: OWLS）
- **製品概要**：AI エージェントがユーザーに代わって自律的にステーブルコインの送受信・残高確認・取引履歴閲覧を行えるデジタルウォレット
- **技術仕様**：
  - セルフカストディ：秘密鍵と認証情報をユーザーのデバイスにローカル生成・保存
  - 対応チェーン：Ethereum エコシステム、Stellar、Solana
  - 単一のオンボーディングフローでアカウント作成・ウォレット生成・本人確認を完結
- **組み込みエージェントスキル**：ウォレットインストール後、AI アシスタントが技術設定なしでウォレット操作を自動習得
- **ローンチ時の機能**：ウォレットアドレス生成、ステーブルコイン送金、残高確認、取引履歴閲覧
- **規制インフラ**：
  - 米国 40 州の Money Transmitter License（MTL）を保有（既存 OwlPay 事業の規制基盤を援用）
  - Visa Direct 連携：米国対象取引でのデビットカード連携を予定
- **ロードマップ（今後対応予定）**：
  - 米国の適格デビットカードでのステーブルコイン購入・換金
  - クロスチェーンブリッジ
  - アドレスブック（受取人の命名管理）
  - 追加チェーンのサポート
- **ユーザー体験例**：「私のオンライン購入を支払って」「100 USDC を日本の友人に送って」という自然言語指示で、エージェントがユーザーの授権範囲内でステーブルコイン決済やクロスボーダー送金を自律実行

## なぜ重要か

### 決済事業者視点

- 米国 40 州 MTL を持つ規制対応済みの AI エージェント向けウォレットが市場に登場したことは、これまで「コンプライアンスリスクが未知」とされてきたエージェント決済において、規制枠組みの中で実装可能であることを示す先例になる
- Visa Direct 連携によりデビットカード → USDC のオンランプが将来的に可能になる。法定通貨と AI エージェント決済の接続を規制の範囲内で実現するモデルとして注目に値する

### 加盟店視点

- 現時点では加盟店向けの API・カタログ・チェックアウト統合は提供されていない。エージェントが送金・支払いを自律実行できても、加盟店側の受け取りインフラが追いついていないのが現状
- 将来的に x402・MPP 等の決済プロトコルに接続された場合、加盟店にとってエージェント購買の受け皿になり得る

### プロダクト視点

- 「技術設定不要でエージェントがウォレット操作を習得する」組み込みエージェントスキルは、開発者以外のユーザー（エンドコンシューマー）が AI エージェントにウォレットを使わせる際の UX 問題を解決しようとするアプローチ
- AWS AgentCore・Pay.sh・Exodus XO Cash 等は開発者向け API/SDK が中心だが、OwlPay Agent Wallet はコンシューマー向け UX を重視した設計で異なるターゲット層をカバーする

### 規制 / リスク視点

- 40 州 MTL の保有はエージェント決済インフラとして現時点で最も規制カバレッジが高い部類。未保有の競合製品に対する差別化要因になる
- ただし AI エージェントによる自律的な送金が「ユーザーによる授権済み取引」として MTL の規制要件を満たすかどうか、各州の具体的な解釈は未確認
- OFAC コンプライアンス（制裁スクリーニング）・AML（疑わしい取引報告）をエージェント主導の高速・大量トランザクションに対応できるかが実運用上の課題

## 我々への示唆

- いま検討すべきこと:
  - OwlPay Agent Wallet の MTL 保有がどの州の規制要件をカバーし、自社の対象市場と重なるかを確認する
  - AI エージェントが「ユーザー授権」のもとで送金する行為が、自社サービス提供州の MTL 要件においてどの主体（ユーザー？エージェント？ウォレット事業者？）の行為として扱われるかを法務と確認する
- 後で深掘りすべきこと:
  - Visa Direct 連携のデビットカードオンランプがいつ対応するか（ロードマップの具体的時期）
  - 組み込みエージェントスキルの技術仕様（どのエージェントフレームワークに対応するか）
  - OwlTing が既存の OwlPay 事業での AML/KYC インフラをエージェントウォレットにどう適用しているか
- 今は優先度が低いこと:
  - ETH / Stellar チェーンのサポート詳細（Solana が主流になりつつある現状では相対的に優先度低）

## 未解決の論点

- AI エージェントが自律実行する送金に対して、各州 MTL はどの主体を「送金業者」と認定するか？
- Visa Direct 連携はいつ利用可能になるか？米国以外にも展開予定があるか？
- 組み込みエージェントスキルはどの AI エージェントフレームワーク（LangChain・AutoGPT・Anthropic 等）に対応するか？
- OFAC・AML スクリーニングをエージェント主導の高速トランザクションにリアルタイムで適用する仕組みはあるか？

## 参考リンク

- 一次情報:
  - [GlobeNewswire 公式プレスリリース（2026-05-04）](https://www.globenewswire.com/news-release/2026/05/04/3286859/0/en/OwlTing-Group-NASDAQ-OWLS-Launches-OwlPay-Agent-Wallet-Targeting-the-Emerging-Multi-Trillion-Dollar-Agentic-Commerce-Economy.html)
- 補足情報:
  - [The Fintech Times — OwlTing Launches Self-Custody Wallet to Bring Regulated Stablecoin Payments to AI Agents](https://thefintechtimes.com/owlting-launches-self-custody-wallet-to-bring-regulated-stablecoin-payments-to-ai-agents/)
  - [Finextra — OwlTing Group launches AI agent wallet](https://www.finextra.com/pressarticle/109691/owlting-group-launches-ai-agent-wallet)
  - [関連ノート：AWS AgentCore Payments x402（2026-05-07）](2026-05-07_AWS_bedrock-agentcore-payments-x402.md)
  - [関連ノート：Exodus XO Cash AI エージェント向けステーブルコイン（2026-05-08）](2026-05-08_Exodus_xo-cash-ai-agent-stablecoin.md)
  - [関連ノート：Solana Google Cloud Pay.sh x402（2026-05-05）](2026-05-05_Solana-GoogleCloud_pay-sh-x402-agent-payments.md)

## 重要度

- Medium

## 確からしさ

- High
