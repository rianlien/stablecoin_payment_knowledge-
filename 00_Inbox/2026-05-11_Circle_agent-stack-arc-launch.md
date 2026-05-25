---
title: "Circle Agent Stack ローンチ + Arc ブロックチェーン $222M 資金調達：エージェント経済向け決済インフラ全投入"
date: 2026-05-11
source: Circle 公式プレスルーム・CNBC・CoinDesk
source_url: https://www.circle.com/pressroom/circle-launches-ai-infrastructure-to-power-the-agentic-economy
entity: Circle
category: 企業発表
primary_category: agentic-payments
article_published_date: 2026-05-11
underlying_event_date: 2026-05-11
primary_source_date: 2026-05-11
tags:
  - agentic-commerce
  - stablecoin
  - payments
  - protocol
  - psp
summary: "Circle が Agent Stack（Agent Wallets・Nanopayments・Agent Marketplace・Circle CLI）を正式ローンチし、同時に Arc ブロックチェーン（機関向け L1）の $222M 規模のトークンプレセールを完了。a16z（$75M リード）・BlackRock・Apollo・ICE・SBI Group ら大型機関が参加し、完全希薄化後評価額（FDV）30 億ドル。USDC を中心とした AI エージェント向け決済インフラをフルスタックで展開する戦略を明確化した。"
implications: "Circle は USDC の単なる発行体にとどまらず、エージェント向けウォレット・ナノペイメント・マーケットプレイスを一体提供するインフラプロバイダーとして再定義しようとしている。Arc が稼働すれば、USDC の主要決済チェーンが Ethereum・Solana・Base に加えて Circle 自社チェーンになる可能性があり、PSP の chain selection 戦略に直接影響する。"
importance: High
confidence: High
follow_up: "Arc メインネット稼働時期（Summer 2026）・Agent Marketplace に最初に掲載されるサービスと手数料構造・Nanopayments の手数料モデルと Circle Gateway の仕様・ARC トークンのユーティリティ設計（バリデーターコスト・決済手数料等）・既存の Nanopayments ノート（2026-04-29）との継続性確認"
---

## 概要

- Circle Internet Group が 2026-05-11 に Agent Stack と Arc ブロックチェーンの $222M 資金調達を同時に発表
- Agent Stack は AI エージェントが USDC を使って自律的に支払い・受領・サービス発見できる開発者インフラ群
- Arc は機関向け L1 ブロックチェーン（"Economic Operating System"）。Summer 2026 のメインネット稼働を目指す

## 何が起きたか

- **Agent Stack 正式ローンチ**：以下の初期プロダクトが agents.circle.com で即日利用可能に
  - **Agent Wallets**：パーミッションレス・ポリシー制御型ウォレット。AI エージェントが事前定義済みのガードレール内で資産を保有・送金・管理できる
  - **Nanopayments**（Circle Gateway 提供）：ガスフリーの USDC マイクロ送金。最小 $0.000001 から、機械速度・機械スケールで実行可能。高頻度・サブセント規模の M2M 決済に対応
  - **Agent Marketplace**：エージェントがサービスを発見・評価・統合できるキュレーテッドディレクトリ。人間とエージェント両方がサービスをプログラマティックに購入可能
  - **Circle CLI**：コマンドラインインターフェース
- **Arc 資金調達**：$222M のトークンプレセール完了。7 億 4,000 万 ARC トークンを $0.30 で販売。FDV 30 億ドル
  - 主な投資家：a16z（$75M でリード）・BlackRock・Apollo Funds・Intercontinental Exchange（ICE）・SBI Group・Janus Henderson Investors・Standard Chartered Ventures・General Catalyst・Marshall Wace・Ark Invest・Haun Ventures・Bullish
  - Arc テストネットは 2025 年 10 月に 100 以上の機関参加者で開始。2026 年 2 月時点で 1 億 6,600 万トランザクション処理・0.5 秒ファイナリティ

## 確認された事実

- Circle Agent Stack は 2026-05-11 に agents.circle.com で公開（Circle 公式プレスルーム確認）
- Arc の $222M 資金調達は CNBC・CoinDesk が独立報道（2026-05-11）
- Agent Wallets・Nanopayments・Agent Marketplace・Circle CLI は初期プロダクトとして明示
- Arc はメインネット稼働が「Summer 2026」予定
- Nanopayments は Circle Gateway インフラ上で稼働（既存の nanopayments ノートと同一コンポーネント）

## なぜ重要か

### 決済事業者視点

- Circle が「USDC 発行体」から「エージェント決済フルスタックプロバイダー」に転換しようとしており、PSP が Circle インフラと競合・補完する関係を再定義する必要がある
- Arc が稼働し USDC のネイティブチェーンとして機能すれば、PSP は Solana・Ethereum・Base に加えて Arc への対応を迫られる可能性がある
- Agent Marketplace は PSP・決済 API の発見経路として、従来の Stripe Marketplace 等と競合するディレクトリになりうる

### 加盟店視点

- Nanopayments により $0.000001 単位の支払いが実用可能になることで、AI トークン消費・API コール課金・データ購入等のマイクロペイメントビジネスモデルが現実化
- Agent Marketplace 掲載が、エージェントからの受注・支払い受領の新たな獲得チャネルになりうる

### プロダクト視点

- MoonPay + Monavate スタック（カードレール）と Circle Agent Stack（USDC ネイティブ）の 2 つの主要エージェント決済アーキテクチャが対比的に整備された
- AWS AgentCore × x402（Coinbase + Stripe）と Circle Agent Stack は重複するが、Circle は自社チェーン（Arc）を持つ点で独立した競争軸を形成する

### 規制 / リスク視点

- a16z・BlackRock・ICE が Arc に参加することで、機関投資家の信認を得た新興 L1 としての位置付けが強化される
- ARC トークンのユーティリティ設計（検証コスト・ガバナンス等）が不明確な場合、米国での証券性リスクが存在する

## 我々への示唆

- いま検討すべきこと:
  - Circle Agent Stack の API 仕様（特に Agent Wallets と Nanopayments）を技術評価。既存の USDC 統合と組み合わせた際の追加価値を確認する
  - Agent Marketplace への掲載可否を検討。エージェントからの決済需要の獲得チャネルとして評価する
- 後で深掘りすべきこと:
  - Arc メインネット仕様と、現行 Ethereum/Solana 上の USDC との互換性・移行コスト
  - Nanopayments と Stripe Tempo ストリーミング決済の技術・手数料比較（AI トークン課金ユースケースでの競合軸）
- 今は優先度が低いこと:
  - ARC トークンへの投資・参加検討。Arc メインネット稼働・規制確認後に再評価

## ありそうな示唆

- Circle は Arc + Agent Stack + USDC を組み合わせた「エージェント決済の中央インフラ」として、Stripe（Tempo + MPP）と正面から競合する戦略に踏み込んだ
- a16z・BlackRock といった機関投資家が Arc に参加したことは、次の決済レール競争の主戦場が「L1 ブロックチェーンの選択」にあることを示唆する

## 推測 / 監視ポイント

- Arc が Summer 2026 にメインネット稼働した場合、Visa（既に 9 チェーン対応）・Mastercard が Arc への対応を発表するか
- Agent Marketplace が x402 と互換のサービス発見プロトコルを採用するか、独自スタックで閉じるか
- Arc のバリデーター構成に ICE・SBI Group 等の金融機関が参加する場合、決済ネットワークとしての規制上の取り扱いがどうなるか

## 未解決の論点

- ARC トークンのユーティリティ設計（ガス・バリデーター報酬・ガバナンス）の詳細
- Circle CLI・Agent Marketplace の具体的な開発者向けドキュメント
- Nanopayments の失敗時の挙動・返金・コンプライアンス処理

## 参考リンク

- 一次情報: [Circle 公式プレスルーム（2026-05-11）](https://www.circle.com/pressroom/circle-launches-ai-infrastructure-to-power-the-agentic-economy)
- 補足情報: [CNBC — Circle raises $222M from BlackRock, Apollo for Arc blockchain（2026-05-11）](https://www.cnbc.com/2026/05/11/circle-closes-222-million-from-blackrock-apollo-for-arc-blockchain.html)
- 補足情報: [CoinDesk — Circle is betting on new $3B blockchain（2026-05-11）](https://www.coindesk.com/business/2026/05/11/i-don-t-think-that-s-crazy-here-is-why-circle-is-betting-on-new-usd3-billion-blockchain)
- 補足情報: [Circle ブログ — Introducing Circle Agent Stack（2026-05-11）](https://www.circle.com/blog/introducing-circle-agent-stack-financial-infrastructure-for-the-agentic-economy)
- 関連ノート: [[2026-04-29_Circle_nanopayments-mainnet]]
- 関連ノート: [[2026-05-01_Circle_nanopayments-mainnet]]
- 関連 MOC: [[MOC_agent-payments-stack]]

## 重要度

- High

## 確からしさ

- High（Circle 公式プレスルーム・CNBC・CoinDesk が独立報道。Arc FDV・投資家リストは複数メディアで一致）
