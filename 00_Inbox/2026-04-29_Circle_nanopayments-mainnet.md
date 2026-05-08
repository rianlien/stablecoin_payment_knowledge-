---
title: "Circle、ナノペイメントをメインネットで正式ローンチ——AIエージェント向けガスフリーUSDCマイクロ決済が11チェーンで稼働開始"
date: 2026-04-29
source: "Circle公式ブログ / The Defiant / Crowdfund Insider"
source_url: "https://www.circle.com/blog/nanopayments-powered-by-circle-gateway-is-now-live-on-mainnet"
entity: "Circle"
category: "payments"
tags:
  - stablecoin
  - payments
  - agentic-commerce
  - protocol
  - wallet
summary: "Circleが2026年4月29日、Circle Gateway上のナノペイメントをメインネットで正式稼働させた。$0.000001からのUSDCガスフリー送金を11チェーンでサポート。AIエージェント・API・機械間決済のインフラとして設計されており、x402やMPPとの補完的ポジションを占める。"
implications: "アジェンティック決済の基礎プリミティブが実稼働フェーズへ移行。エージェント間マイクロペイメントの技術的ハードルが実質ゼロに近づいた。"
follow_up: "手数料体系の詳細、x402との統合有無、日本語対応チェーンの追加予定"
---

## 概要

Circleは2026年4月29日、Circle Gateway上のナノペイメント機能をメインネットで正式ローンチした。最小$0.000001（1マイクロセント）からのUSDCガスフリー送金を、11ブロックチェーン上で利用可能にする。AIエージェント・開発者・インフラチームを主な対象とした「エージェンティック経済の金融レール」として位置づけられている。

## 何が起きたか

- **2026年4月29日、Circle公式ブログで発表**: 「Nanopayments powered by Circle Gateway is now live on mainnet」
- **対応チェーン（11種）**: Arbitrum、Avalanche、Base、Ethereum、HyperEVM、Optimism、Polygon PoS、Sei、Sonic、Unichain、World Chain
- **特徴**: ガスフリー、最小$0.000001、即時検証、USDC建て
- **テストネット先行**: テストネットで先行検証後、今回メインネット移行
- **初期統合パートナー**: AIsa、AgentCard、Alchemy、Arrays、blockrun.ai、Goldsky、Meridian、QuickNode
- **Circle Gateway基盤**: ナノペイメントはCircle GatewayのAPIレイヤーとして提供。開発者はGateway APIを通じて送受金を管理

## なぜ重要か

### 決済事業者視点
- ガス代ゼロでサブセント決済が成立するため、マイクロペイメントビジネスモデルの経済的フィージビリティが初めて確保された
- 複数チェーン対応により、PSPがチェーン選択を顧客任せにできるマルチレール戦略が現実的になった

### 加盟店視点
- API課金・コンテンツ単位課金・AIサービス従量課金など、従来カード決済では採算が合わなかった超小額課金モデルへの道が開かれた
- ゲーム内アイテム・リサーチデータ・分析フィードなど、0.001〜0.01ドル規模の取引が実装可能になった

### プロダクト視点
- x402プロトコルやStripeのMPP（Machine Payments Protocol）と組み合わせると、エージェントが自律的にAPIを呼び出してマイクロペイメントする完全スタックが成立する
- Circle GatewayのAPIは既存のUSDCインフラとの親和性が高く、既存PSPシステムへの組み込みコストが低い

### 規制 / リスク視点
- USDCはGENIUS Act準拠の規制対象ステーブルコインであるため、コンプライアンス的な安全度は比較的高い
- エージェント間送金のAML追跡はウォレットアドレス単位の取引が細分化されるため、KYT要件の具体的な適用方法は未確定

## 我々への示唆

- いま検討すべきこと:
  - Circle Gateway APIの仕様を確認し、自社サービスのマイクロ課金ユースケースへの適合性を評価
  - x402またはMPPとのナノペイメント統合がどの程度シームレスに実現できるかを技術検証
- 後で深掘りすべきこと:
  - 手数料体系の詳細（ガス代ゼロの場合、Circleの収益化モデルは何か）
  - HyperEVM・Sei・Sonic等の新規チェーン追加タイミングと日本向けチェーンの追加予定
- 今は優先度が低いこと:
  - ゲーム・コンテンツ分野への展開（現時点では自社事業外）

## 未解決の論点

- Circleがガス代を内部負担する場合の持続可能性——大量エージェントトラフィック発生時のコスト構造は？
- KYT・AMLはナノ単位の大量取引でどう機能するか？集約取引単位でのレポートに切り替わるのか？
- x402との統合は公式サポートされるのか、それとも開発者がアダプター層を自作する必要があるのか？
- World Chain（Worldcoin）対応の意味合い——生体認証と決済の統合を視野に入れているか？

## 参考リンク

- 一次情報: [Circle公式ブログ](https://www.circle.com/blog/nanopayments-powered-by-circle-gateway-is-now-live-on-mainnet)
- 補足情報: [The Defiant](https://thedefiant.io/news/defi/circle-launches-gas-free-nanopayments-on-mainnet-across-11-blockchains) / [Crowdfund Insider](https://www.crowdfundinsider.com/2026/05/276951-circle-launches-nanopayments-on-mainnet-enabling-usdc-micro-transactions-for-agentic-economy/) / [Circle Nanopayments製品ページ](https://www.circle.com/nanopayments)

## 重要度
- Medium

## 確からしさ
- High
