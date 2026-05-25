---
title: "NEAR AI：USDC × Confidential Intents でエージェント向けプライベートステーブルコイン決済を実装"
date: 2026-05-14
source: PR Newswire・CryptoTimes
source_url: https://www.prnewswire.com/news-releases/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy-302772311.html
entity: NEAR AI
category: 企業発表
primary_category: agentic-payments
article_published_date: 2026-05-14
underlying_event_date: 2026-05-14
primary_source_date: 2026-05-14
tags:
  - agentic-commerce
  - stablecoin
  - privacy
  - protocol
  - payments
summary: "NEAR AI が USDC と Confidential Intents を統合し、NEAR AI Agent Market 上の AI エージェントがプライベートな USDC 決済を実行できる環境を整備。取引金額・カウンターパーティ・ルーティングパスを秘匿しながら、クロスチェーンでプログラマブルに決済できる。Confidential Intents は NEAR の秘密シャード（プライベートシャード）によるコンフィデンシャル実行レイヤー。"
implications: "Paxos が Consensus Miami（2026-05-07〜09）で『プライバシーインフラの未整備がステーブルコイン機関向け採用の最大障壁』と指摘した課題に対する、最初の具体的な実装事例。コンフィデンシャルコンピューティングを決済レイヤーに組み合わせる構成は、B2B・機関向けユースケースへの応用可能性が高く、プライバシー対応の技術標準形成を促す可能性がある。"
importance: Medium
confidence: High
follow_up: "Confidential Intents の詳細技術仕様（MPC・ZK・TEE のどれか）・NEAR AI Agent Market の現規模（エージェント数・取引量）・USDC 以外の通貨対応予定・Circle との公式パートナーシップの有無・IronClaw セキュアランタイムとの統合状況"
---

## 概要

- NEAR AI が USDC と Confidential Intents を統合し、AI エージェント向けのプライベートなステーブルコイン決済レイヤーを整備
- NEAR AI Agent Market 上のエージェントは、取引内容（金額・相手方・ルーティング）を公開せずに USDC で決済できるようになった
- Confidential Intents は 2026 年 2 月の NEARCON（後半）で IronClaw セキュアランタイムとともに発表された既存インフラ。今回はその決済レイヤー追加としての統合

## 何が起きたか

- **NEAR AI × USDC 統合**：Circle との協力のもと、NEAR AI Agent Market が USDC を決済通貨としてネイティブサポート
- **Confidential Intents の仕組み**：NEAR のプライベートシャードによるコンフィデンシャルクロスチェーン実行レイヤー。ルーティングパス・カウンターパーティ・経済的関係を秘匿した状態で決済を実行する
- **対象ユースケース**：AI エージェントが企業のバックオフィスを管理したり、サプライヤーと調整する際に、財務活動を機密保持しながら自律的に処理できる
- **技術スタック**：USDC（決済単位）+ Confidential Intents（秘密実行レイヤー）+ NEAR プライベートシャード（インフラ）

## 確認された事実

- PR Newswire 公式プレスリリース（2026-05-14）で統合を確認
- CryptoTimes が 2026-05-15 に独立報道
- Confidential Intents は 2026 年 2 月の NEARCON で IronClaw セキュアランタイムとともに発表済み（統合以前から存在するインフラ）
- NEAR AI Agent Market が USDC をネイティブ決済通貨としてサポートしたのは今回が初
- 取引金額・カウンターパーティ・ルーティングパスの 3 要素が秘匿対象として明示されている

## なぜ重要か

### 決済事業者視点

- プライバシー対応のステーブルコイン決済インフラが実用段階に入った。公開ブロックチェーン上での取引可視性という制約に具体的な技術的回答が提示された
- PSP がエージェント向け B2B 決済を提供する際に、プライバシー要件（競合他社への情報漏洩防止・機密取引保護）に対応できるかどうかが差別化要因になる可能性がある

### 加盟店視点

- 企業がサプライチェーン支払い・調達・バックオフィス処理を AI エージェントに委任する際に、取引内容が外部に露出しないことが採用の前提条件となる。この要件をステーブルコイン決済が満たせるようになった

### プロダクト視点

- 「プライベートな決済実行 + プログラマブルな認可」という組み合わせは、ERC-5564 Stealth Addresses や EIP-7503 ZK Wormholes といった Ethereum 系プライバシー標準との競合アーキテクチャになる
- NEAR のアプローチは TEE/MPC ベースのプライベートシャードを活用しており、ZK-proof ベースのアプローチとは異なる技術トレードオフを持つ

### 規制 / リスク視点

- 「取引を秘匿する」機能は AML/OFAC スクリーニングとの競合が生じうる。NEAR AI の実装がどのように選択的開示（コンプライアンス機関への情報提供）を実現するかは未確認
- EU MiCA や FATF Travel Rule との互換性が確認されるまで、規制管轄での採用リスクが残る

## 我々への示唆

- いま検討すべきこと:
  - NEAR AI Confidential Intents の技術仕様（MPC vs ZK vs TEE）を確認し、コンプライアンス機関への選択的開示機能が実装されているかを評価する
  - B2B・機関向けステーブルコイン決済の要件定義に「プライバシー対応」を正式な評価軸として追加する
- 後で深掘りすべきこと:
  - ERC-5564 Stealth Addresses・EIP-7503・NEAR Confidential Intents の技術比較（決済ユースケース向け適合性・コンプライアンス対応）
  - Circle との協力関係の詳細——USDC 統合が API レベルの実装なのか、より深い技術連携なのか
- 今は優先度が低いこと:
  - NEAR AI Agent Market への自社サービス掲載検討。市場規模・エコシステム成熟度が不明なため監視フェーズ

## ありそうな示唆

- Paxos の「プライバシーが次のボトルネック」という指摘（Consensus Miami 2026-05-08）は、業界が正確に認識した課題だった。実装が出始めたことで、次の 12〜18 か月でプライバシー対応ステーブルコイン決済の競争が本格化する
- NEAR のアプローチが普及すれば、「コンフィデンシャル実行環境での USDC 決済」が新たなカテゴリとして確立する

## 推測 / 監視ポイント

- NEAR AI Confidential Intents が FATF Travel Rule 対応の選択的開示機能を実装しているかどうか
- 他の主要エージェント決済プラットフォーム（AWS AgentCore・Circle Agent Stack・Stripe MPP）がプライバシー機能を追加する時期
- ZK-proof ベースの実装（EIP-7503 等）がステーブルコイン決済に特化した形で実用化されるタイムライン

## 未解決の論点

- Confidential Intents の詳細技術スペック（TEE・MPC・ZK のいずれか）が公開情報として確認できていない
- NEAR AI Agent Market の現時点での利用規模（エージェント数・月次取引量）が不明
- USDC 以外の通貨への対応予定
- AML/OFAC コンプライアンス機関への開示仕組みの有無

## 参考リンク

- 一次情報: [PR Newswire 公式プレスリリース（2026-05-14）](https://www.prnewswire.com/news-releases/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy-302772311.html)
- 補足情報: [CryptoTimes（2026-05-15）](https://www.cryptotimes.io/2026/05/15/near-ai-integrates-private-usdc-payments-for-agentic-commerce/)
- 関連ノート: [[2026-05-08_Consensus-Miami_stablecoin-permission-slip]]（Paxos のプライバシー指摘）
- 関連プロトコル: [[ERC-5564_Stealth-Addresses]]
- 関連プロトコル: [[EIP-7503_ZK-Wormholes]]
- 関連 MOC: [[MOC_agent-payments-stack]]

## 重要度

- Medium

## 確からしさ

- High（PR Newswire 公式プレスリリース・CryptoTimes 独立報道で確認。技術仕様の詳細は一次ドキュメント未参照）
