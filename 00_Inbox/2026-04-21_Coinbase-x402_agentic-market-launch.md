---
title: "Coinbase、x402プロトコル上にAI エージェント向けサービスマーケットプレイス「Agentic.market」をローンチ"
date: 2026-04-21
source: "Coinbase Developer Platform / The Paypers / Invezz"
source_url: "https://www.coinbase.com/developer-platform/discover/launches/agentic-market"
entity: "Coinbase / x402"
category: "agentic-commerce"
tags:
  - x402
  - agentic-commerce
  - stablecoin
  - payments
summary: "Coinbase が x402 プロトコル上に AI エージェント専用のサービスマーケットプレイス「Agentic.market」を 2026 年 4 月 20 日にローンチ。Bloomberg・AWS・CoinGecko・OpenAI 等のサービスを API キー不要・USDC 決済で AI エージェントが自律的に購入できる。"
implications: "x402 が実際に流通するマーケットプレイスを持ったことで、アジェンティック・コマースの基盤が「プロトコル定義」から「サービス流通」フェーズに移行した。PSP は自律決済フローへの対応とコンプライアンス設計を具体的に検討すべき段階に入った。"
follow_up: "Agentic.market の日次取引量の推移、Circle CPN との連携状況、非 Base チェーンへの展開計画"
---

## 概要

Coinbase が x402 プロトコルを活用した AI エージェント向けサービスマーケットプレイス「Agentic.market」を 2026 年 4 月 20 日に正式ローンチした。AI エージェントが Bloomberg データ・AWS Lambda・CoinGecko API などのデジタルサービスを API キーや事前アカウント登録なしに USDC で即時購入できる仕組みを提供する。x402 Foundation の設立（4 月 2 日）から約 3 週間で、実際のサービス流通を担うマーケットプレイスが稼働開始した形となる。

## 何が起きたか

- **ローンチ日**：2026 年 4 月 20 日（公式発表は 4 月 21 日）
- **プラットフォーム構成**：7 カテゴリ（推論・データ・メディア・検索・ソーシャル・インフラ・取引）に分類されたサービスディレクトリ
- **参加プロバイダー**：OpenAI、Bloomberg、AWS Lambda、CoinGecko、Coinbase RAT 等
- **決済インフラ**：Base ブロックチェーン上の USDC を決済レールとして採用。Coinbase の Payments MCP（Model Context Protocol 拡張）経由で Anthropic Claude・Google モデル等の LLM がオンチェーンウォレットに直接アクセス可能
- **自律決済の仕組み**：各 AI エージェントは Agentic Wallet を持ち、サービス発見→価格比較→USDC 支払い→サービス取得を人間の介入なしに完結できる
- **採用状況**（2026 年 4 月 21 日時点）：約 69,000 のアクティブ AI エージェントが x402 上で稼働、累計 1 億 6,500 万件超のトランザクション・総額 5,000 万ドルを処理済み
- **x402 Foundation エコシステム**：Linux Foundation 傘下、バッカーには Cloudflare・Stripe・AWS・Google・Visa・Circle・Solana Foundation・Mastercard 等 20 社超

## なぜ重要か

### 決済事業者視点

- AI エージェントが自律的に USDC でサービスを購入する「機械間決済（M2M payments）」が実用フェーズに移行した最初の大規模商用プラットフォームとなる
- 従来型カード決済では経済的に成立しないマイクロペイメント（0.01 セント以下）が x402 で実現しており、PSP が対応すべき新しい決済単位が生まれている

### 加盟店視点

- Bloomberg・AWS 等のデータプロバイダーが新たな収益チャネルとして AI エージェント向け従量課金を開始。加盟店サイドの API エコノミーに変化が起きている
- サブスクリプション型 API 課金から「ペイ・パー・コール」モデルへの移行が加速する可能性がある

### プロダクト視点

- Anthropic Claude・Google モデルが x402 対応済みであることは、Claude Code（当社使用ツール）を含む LLM ベースのエージェントが Agentic.market に直接接続可能であることを意味する
- Payments MCP により、エージェントへのウォレット統合が開発者にとって標準的なパターンになりつつある

### 規制 / リスク視点

- USDC on Base を使用するため、Base は Circle が KYC/AML を管理する「許可型」環境ではなくパブリックチェーン。エージェント発の取引に対する KYT（Know Your Transaction）・AML 義務がどの主体に帰属するかはまだ明確でない
- 自律エージェントが契約主体となった場合の責任の所在（エージェント所有者 vs. プラットフォーム vs. サービスプロバイダー）は未解決

## 我々への示唆

- いま検討すべきこと:
  - エージェント向け決済フローを自社プロダクトロードマップに組み込む場合の API 設計（Agentic Wallet のオンボーディング・KYC フローを含む）
  - x402 プロトコルへの適合コスト評価（x402 Foundation の開発者向けドキュメントの確認）
- 後で深掘りすべきこと:
  - 実際の日次取引量・エージェント数の推移（ローンチ発表数値 vs. オンチェーン実績）
  - Circle CPN Managed Payments と x402/Agentic.market の統合状況
  - 非 Base チェーン（Ethereum L1・Solana 等）への x402 対応拡大状況
- 今は優先度が低いこと:
  - 個別サービスプロバイダーの収益評価

## 未解決の論点

- 自律エージェントによる取引に対する KYT・AML 義務はどの主体（エージェント所有者、プラットフォーム、ブロックチェーン）が担うか？
- Agentic.market の日次オンチェーン取引量はどの程度か（x402 Foundation 設立時点では実取引量は累計 $50M に対して日次約 $28,000 と乖離が大きかった）？
- 決済最終性に関する法的整理（USDC on Base のトランザクション確定性と従来型決済の「取消不能性」の対比）は進んでいるか？

## 参考リンク

- 一次情報:
  - [Agentic.market 公式ページ（Coinbase）](https://www.coinbase.com/developer-platform/discover/launches/agentic-market)
  - [Coinbase Developer Platform ローンチ発表](https://www.coinbase.com/developer-platform/discover/launches/agentic-market)
- 補足情報:
  - [Invezz — 詳細記事（2026-04-21）](https://invezz.com/news/2026/04/21/coinbase-backed-x402-launches-agentic-market-to-power-ai-agent-services/)
  - [The Paypers 報道](https://thepaypers.com/crypto-web3-and-cbdc/news/coinbase-rolls-out-agenticmarket-via-x402)
  - [AWS Industries — x402 とアジェンティック・コマース解説](https://aws.amazon.com/blogs/industries/x402-and-agentic-commerce-redefining-autonomous-payments-in-financial-services/)
  - [既存ノート：x402 Foundation Linux Foundation 移管（2026-04-02）](2026-04-02_x402-Foundation_linux-foundation-launch.md)

## 重要度

- High

## 確からしさ

- High
