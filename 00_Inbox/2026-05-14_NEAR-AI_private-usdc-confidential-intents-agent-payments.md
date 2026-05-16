---
title: "NEAR AI：Confidential Intents × USDC でエージェント向けプライベートステーブルコイン決済を実装"
date: 2026-05-14
source: PR Newswire
source_url: https://www.prnewswire.com/news-releases/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy-302772311.html
entity: NEAR AI
category: 企業発表
primary_category: agentic-payments
article_published_date: 2026-05-15
underlying_event_date: 2026-05-14
primary_source_date: 2026-05-14
tags:
  - stablecoin
  - agentic-commerce
  - payments
  - privacy
  - agent-identity
summary: "NEAR AI が Confidential Intents（NEAR プライベートシャード）と USDC を統合し、AI エージェントが取引金額・相手方を外部に晒さずにステーブルコイン決済できるインフラを NEAR AI Agent Market に実装。Co-founder Illia Polosukhin は「機密ステーブルコイン決済はエージェント経済のベースライン要件」と表明。Consensus Miami（2026-05-05〜07）で Paxos が指摘した『プライバシーが主流化の次のボトルネック』論に対する最初の具体的回答。"
implications: "企業・機関がエージェントを本番デプロイする際の最大障壁だった『パブリックチェーン上での取引露出』問題に対して、実装レベルの解が提示された。B2B・機関向けエージェント決済の普及加速を左右するプライバシー基盤として注視が必要。"
importance: High
confidence: High
follow_up: "Confidential Intents の技術詳細（ZK-proof 使用の有無・NEAR プライベートシャードの仕様）。既存の ERC-5564 Stealth Addresses 等との技術比較。NEAR AI Agent Market への掲載サービスとビジネス規模の確認。USDC 以外のステーブルコインへの拡張予定。"
---

## 概要

- NEAR AI が 2026-05-14 に USDC と Confidential Intents の統合を発表。AI エージェントが NEAR AI Agent Market 上でプライベートなステーブルコイン決済を実行できるようになった。
- 技術スタック：USDC（決済通貨）＋ Confidential Intents（NEAR プライベートシャードによる機密クロスチェーン実行レイヤー）＋ IronClaw（セキュアランタイム）。
- Consensus Miami 2026（2026-05-05〜07）で Paxos の Brent Perrault が「プライバシーインフラの未整備が機関採用の最大障壁」と指摘したことへの具体的回答として位置付けられる。

## 何が起きたか

- NEAR AI Agent Market 上の AI エージェントが USDC で支払いを発行・受領できるようになった。
- Confidential Intents を通じることで、**取引金額・カウンターパーティ・商業関係の詳細がパブリックブロックチェーン上に公開されない**。
- NEAR AI は 2026-02 末の NEARCON で Confidential Intents（+ IronClaw セキュアランタイム）をローンチ済み。今回はその決済レイヤーとして USDC を統合した形。
- Agent Market はエージェントが自律的な経済的主体として機能するマーケットプレイス（エージェントがサービスを売買できる）。

## 確認された事実

- 発表日：PR Newswire リリース（302772311）、CryptoTimes が 2026-05-15 に報道
- underlying_event_date は PR Newswire のリリース番号から 2026-05-14 と推定
- 技術スタック：USDC + Confidential Intents + IronClaw（NEAR 公式 2026-02 発表時と整合）
- Co-founder Illia Polosukhin 引用："Confidential stablecoin settlement is a baseline requirement for the agentic economy. Businesses will not deploy agents that expose their revenue, counterparties, or financial operations on a public ledger."
- Confidential Intents の基盤：NEAR プライベートシャード（クロスチェーン機密実行レイヤー）

## なぜ重要か

### 決済事業者視点

- 企業がエージェントに決済権限を委任しない最大理由の一つが「パブリックチェーン上での取引露出」。競合他社・監査機関・一般に取引額・相手方が見えることは、B2B ユースケースで実質的な参入障壁だった。
- NEAR AI の Confidential Intents は、ブロックチェーンの透明性を維持しつつ取引内容を機密化するアプローチで、この障壁を実装レベルで解消しようとしている。
- PSP・PayFac が企業顧客にエージェント決済ソリューションを提案する際、「機密性」は仕様として求められる要素になる可能性が高い。

### 加盟店視点

- NEAR AI Agent Market に参加する事業者（AI サービスを売る側）も、売上・顧客関係が競合に見えない形で収益化できることは実用的な価値がある。
- ただし、Agent Market の現在の規模・市場カバレッジは限定的（NEAR エコシステム内）。

### プロダクト視点

- 技術的アプローチの比較：
  - ERC-5564 Stealth Addresses：受取人アドレスを秘匿。送金者・金額は見える可能性
  - ZK-proof 系：計算コストが高い。コンプライアンス向け選択的開示の実装が複雑
  - NEAR Confidential Intents：プライベートシャードによるオフチェーン実行 + クロスチェーン決済。詳細仕様は未確認
- 機密決済 × コンプライアンス（選択的開示・AML 対応）の両立設計が実用化の鍵。

### 規制 / リスク視点

- プライバシー強化型決済は AML・制裁スクリーニングの規制との整合が課題。"Confidential" が当局から見えないのか、選択的に開示できるのかは法的に重要な違い。
- IronClaw（セキュアランタイム）が監査証跡・KYC/AML 記録をどう保持するかが規制適合の分かれ目。

## 我々への示唆

- いま検討すべきこと:
  - Confidential Intents の技術詳細（ZK-proof 使用有無・選択的開示の可否・当局へのアクセス方法）を確認し、自社が提供するエージェント決済に求められるプライバシー要件の水準と照合する
  - B2B 顧客向けのエージェント決済提案において「機密性」を仕様として明示できるか検討する
- 後で深掘りすべきこと:
  - NEAR Confidential Intents と ERC-5564・ZK-proof ベース実装の技術比較（速度・コスト・規制適合性）
  - NEAR AI Agent Market の現在のサービスカテゴリ・取引規模・主要参加者
- 今は優先度が低いこと:
  - NEAR トークン自体の投資観点（今回は決済インフラ視点での評価を優先）

## ありそうな示唆

- Paxos・NEAR AI・Circle（プライバシー研究継続中）と複数のプレイヤーが「プライバシーがスケールの壁」という同じ問題を認識している。最初に「規制準拠 + 機密性」を両立させた実装を普及させたプレイヤーが、機関向けエージェント決済の標準インフラを押さえる可能性がある。
- 「Confidential stablecoin settlement is a baseline requirement」という Polosukhin の発言は、業界コンセンサス形成の起点になりうる。2026 年後半の業界イベントで類似の発言が増えれば、規制当局もプライバシー対応型コンプライアンスフレームワークの整備に動く可能性がある。

## 推測 / 監視ポイント

- NEAR Confidential Intents が AML・OFAC スクリーニングとどう共存するか（選択的開示 API の有無）
- NEAR AI Agent Market の USDC 決済規模が Q3 2026 にどう推移するか
- 他チェーン（Ethereum・Solana・Base）での類似プライバシー実装との競争状況
- GENIUS Act・CLARITY Act が「プライバシー強化型ステーブルコイン決済」に対して追加規制を設けるかどうか

## 未解決の論点

- Confidential Intents の詳細技術仕様（ZK-proof ベースか TEE ベースか・証明サイズ・確定時間）
- コンプライアンス向け選択的開示の仕組みと当局への情報提供方法
- NEAR AI Agent Market への参加・掲載条件と現在の取引規模
- USDC 以外（USDT・EURC 等）への拡張ロードマップ

## 参考リンク

- 一次情報: [PR Newswire（2026-05-14）](https://www.prnewswire.com/news-releases/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy-302772311.html)
- 補足情報: [CryptoTimes（2026-05-15）](https://www.cryptotimes.io/2026/05/15/near-ai-integrates-private-usdc-payments-for-agentic-commerce/)
- 補足情報: [aithority.com](https://aithority.com/machine-learning/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy/)
- 関連ノート: [[2026-05-08_Consensus-Miami_stablecoin-permission-slip]]（Paxos のプライバシー指摘）

## 重要度

- High

## 確からしさ

- High（PR Newswire 公式リリース・複数媒体確認。underlying_event_date は PR 番号から推定で ±1 日の誤差の可能性あり）
