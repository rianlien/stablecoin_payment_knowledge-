---
title: "Coinbase"
type: company
updated: 2026-06-18
category: crypto-exchange
tags:
  - stablecoin
  - payments
  - x402
  - agentic-commerce
  - company
aliases:
  - Coinbase Developer Platform
  - CDP
  - x402
---

# Coinbase

Coinbase は、取引所・カストディ事業から、USDC 決済、x402、Base、Agentic Wallet、B2B 支払いインフラへ広げている。

この vault では、Coinbase を「オンチェーン決済の開発者基盤と機関向け流動性を押さえ、AI エージェント決済の標準化を主導する企業」として追う。

ネットワークとしての Base は [[Base]] を参照。

---

## 現状の要約

### 何をしているか

- **x402 の標準化**: HTTP 402 を使った API / AI / machine payments の支払い標準を Linux Foundation に移管し、業界連合化している。2026-06-03 に Chainalysis が累計1億件突破を確認（ただし成長の大部分は PING ミームコインに依存）。
- **Base MCP Server**: 2026-05-26 ローンチ。ChatGPT・Claude 等の AI エージェントが Base Account（スマートウォレット）に接続し、自然言語でトークン送金・スワップ・DeFi 操作を実行できる。秘密鍵は TEE セキュアエンクレーブで管理。エージェントごとの支出上限・ホワイトリストをインフラ層で強制できる設計。
- **AWS CloudFront への x402 統合**: 2026-06-15 に AWS WAF が AI トラフィック課金機能を CloudFront 全体に展開。コンソール変更のみで既存 CloudFront ユーザー（インターネット約 25% をカバー）が x402 有料ゲートウェイを設置可能になった。
- **Agentic.market の流通面構築**: x402 対応サービスを発見・比較・利用できるマーケットプレイスを作り、AI エージェントの購買導線を用意している。
- **Base / Solana / Polygon 等の決済対応拡大**: CDP facilitator を通じて複数チェーンで USDC / ERC-20 決済を処理する方向。x402 は Arbitrum にも拡張済み（2026-05-14）。
- **Checkout.com との加盟店展開**: 2026-06-02 に Checkout.com 傘下の 1,000 社超エンタープライズ加盟店へ USDC/USDT 決済を解禁。加盟店は暗号資産統合なしで USD 着金のまま受け取り可能。
- **B2B クロスボーダー決済インフラ**: Nium などの決済インフラ企業に Coinbase の USDC / custody / liquidity を組み込む。
- **機関向けトレジャリー・運用**: CUSHY など、ステーブルコイン残高を機関向けクレジット商品へ接続する動き。

### 見立て

Coinbase の戦略は、Base や x402 を使って「開発者がオンチェーン決済を組み込む入口」を押さえること。Stripe が加盟店・法定通貨側から入るのに対し、Coinbase はプロトコル、ウォレット、カストディ、チェーン、USDC 流動性をまとめて提供する。

x402 の累計1億件突破（Chainalysis, 2026-06-03）と AWS CloudFront 統合（2026-06-15）により、x402 の潜在利用可能規模が一気に拡大した。一方で、Stripe・Visa・Mastercard との共同ステーブルコインプラットフォーム計画が報道されており（2026-06-03）、Coinbase の参加可否（Circle USDC との収益分配契約との兼ね合い）が今後の戦略の分水嶺になる可能性がある。

---

## 主要レイヤー

| レイヤー | Coinbase の動き | 意味 |
|---|---|---|
| L0 / チェーン | Base、Solana、Polygon 等への x402 facilitator 対応 | 開発者が複数チェーンで支払いを受けられる |
| L1 / ウォレット | Agentic Wallet / Coinbase wallet infrastructure | AI エージェントが支払い主体を持てる |
| L2 / 流動性・カストディ | USDC、Coinbase Prime、custody | B2B 決済・機関運用の裏側を担う |
| L3 / プロトコル | [[x402]] | API / AI / コンテンツ課金を HTTP 上で実行 |
| L5 / アプリ | Agentic.market | エージェントが購入できるサービス面を持つ |

---

## Inbox との紐付け

### 中核ニュース

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-02 | [[2026-04-02_x402-Foundation_linux-foundation-launch]] | [[x402]] を [[x402 Foundation]] に移管し、業界標準化へ |
| 2026-04-21 | [[2026-04-21_Coinbase-x402_agentic-market-launch]] | x402 上の Agentic.market をローンチ |
| 2026-05-07 | [[2026-05-07_AWS_bedrock-agentcore-payments-x402]] | AWS AgentCore Payments が x402 / Coinbase wallet infrastructure を採用 |
| 2026-05-05 | [[2026-05-05_Solana-GoogleCloud_pay-sh-x402-agent-payments]] | Google Cloud / Solana 側で x402 ベースの Pay.sh が登場 |
| 2026-05-26 | [[2026-05-26_Coinbase-Base_mcp-ai-agent-wallet]] | [[Base]] 上の MCP 対応 AI エージェントウォレット発表 |
| 2026-06-02 | [[2026-06-02_Coinbase-Checkout_stablecoin-merchant-payments]] | マーチャント向けステーブルコイン決済受け取りソリューション |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-agentic-payments]] | Chainalysis が x402 の 1 億件突破を分析——Base がメイン環境 |
| 2026-06-03 | [[2026-06-03_Chainalysis_x402-100m-transactions-base]] | Chainalysis による x402 トランザクション 1 億件達成の統計データ |
| 2026-06-03 | [[2026-06-03_Stripe-Visa-Mastercard-Coinbase_stablecoin-consortium]] | Stripe・Visa・Mastercard との共同ステーブルコインプラットフォーム発表 |
| 2026-06-04 | [[2026-06-03_Stripe-Visa-Mastercard_joint-stablecoin-platform-report]] | Stripe・Visa・Mastercard 共同ステーブルコインプラットフォームレポート |
| 2026-06-09 | [[2026-06-09_Injective_x402-agent-payments]] | Injective Protocol が Coinbase × x402 で AI エージェント決済を実装 |
| 2026-06-11 | [[2026-06-11_MassPay-Coinbase_stablecoin-payouts]] | MassPay が Coinbase USDC インフラを活用してグローバルペイアウト |
| 2026-06-15 | [[2026-06-15_AWS-Coinbase_x402-cloudfront-waf-ai-traffic-monetization]] | AWS WAF が Coinbase x402 を採用し CloudFront 全体に AI トラフィック課金を展開。インターネット約 25% 規模の x402 有料ゲートウェイが成立 |

### B2B 決済・流動性

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-26 | [[2026-04-26_Coinbase-Nium_usdc-global-190-countries]] | Nium 経由で 190 か国以上の USDC クロスボーダー決済へ |
| 2026-04-29 | [[2026-04-29_Visa_stablecoin-settlement-9chains-7b]] | Visa が Base を含む複数チェーン清算を拡張 |
| 2026-04-30 | [[2026-04-30_Coinbase_cushy-stablecoin-credit-fund]] | CBAM がステーブルコイン担保クレジットファンド CUSHY を発表 |
| 2026-04-30 | [[2026-04-30_Coinbase_cushy-superstate-tokenized-fund]] | CUSHY / Superstate FundOS 関連の補足ノート |

### 規制・トークン対応

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-23 | [[2026-04-23_CryptoCoalition_clarity-act-senate-letter]] | Coinbase を含む業界団体が CLARITY Act 対応で連名書簡 |
| 2026-04-30 | [[2026-04-30_Coinbase_dai-usds-migration]] | DAI から USDS への移行告知 |
| 2026-05-01 | [[2026-05-01_CLARITY-Act_stablecoin-yield-compromise]] | ステーブルコイン利回り規制に対する業界反応 |
| 2026-05-01 | [[2026-05-01_ClarityAct_stablecoin-yield-compromise]] | CLARITY Act 利回り妥協テキスト公開に対する Coinbase の公開支持・マークアップ要求 |
| 2026-05-04 | [[2026-05-04_Coinbase_dai-delist-usds-migration]] | DAI 上場廃止・USDS 自動移行の実施 |
| 2026-05-06 | [[2026-05-06_Bermuda_usdc-digital-finance-forum]] | バミューダが USDC エアドロップと Digital Finance Forum 2026 でオンチェーン国民経済を推進（Coinbase が共同実施） |
| 2026-05-13 | [[2026-05-13_x402_batch-settlement-sub-cent-ai-payments]] | x402 バッチ決済対応——$0.0001 以下の AI マイクロペイメントを Base 上で実現 |
| 2026-05-14 | [[2026-05-14_x402_arbitrum-launch-agent-payments]] | x402 が Arbitrum に対応——AI エージェントが Arbitrum 上のステーブルコインでマイクロ決済可能に |

---

## 競争上の論点

### x402 の優位性

AWS、Google Cloud / Solana、Linux Foundation、主要決済企業の参加により、x402 は AI エージェント決済の標準候補として強い位置にある。特に API 課金、AI 推論、データアクセスのようなリクエスト単位課金では、Stripe MPP より開発者標準に近い可能性がある。

### Stripe との違い

- Coinbase はオンチェーン・開発者・USDC 決済から入る。
- Stripe は加盟店・PSP・法定通貨接続から入る。
- AWS AgentCore では両社が同時に登場しており、実務上は競合だけでなく補完関係にもなる。

### Circle との違い

Coinbase は USDC の発行体ではないが、USDC の流通・カストディ・決済実行インフラを押さえる。Circle CPN が発行体主導のネットワークなら、Coinbase は開発者・取引所・カストディ主導のネットワーク。

---

## 監視ポイント

- **x402 の取引品質**: PING ミームコインを除いた純粋な AI エージェント・API 取引の件数と金額（Chainalysis の次レポートで確認）
- **AWS CloudFront × x402 の採用状況**: CloudFront 上の AI トラフィック課金有効化サイト数・USDC 決済量の公開データ
- **Stripe・Visa・Mastercard 共同プラットフォームへの参加可否**: 参加すれば Circle USDC との収益分配契約と競合する可能性。不参加なら標準化競争に対抗する独自路線を強化する必要
- **Checkout.com 加盟店でのステーブルコイン決済量**: 1,000 社超のうち実際に有効化した比率と取引量が普及度の指標
- **Base MCP の x402 決済との統合**: エージェントが DeFi 操作と x402 決済を同一コンテキストで実行できるか
- **Agentic.market のサービス数、課金単価、日次利用量**
- **CDP facilitator の対応チェーン・対応トークン拡張**
- **Nium 経由の B2B 決済実績**
- **CUSHY の適格投資家要件、規制整理**

---

## 関連 MOC

- [[MOC_Companies]]
- [[MOC_Protocols]]
- [[MOC_agent-payments-stack]]
- [[MOC_Stablecoin_Payments]]

---

## 参考リンク

- 一次情報: [Coinbase x402 product page](https://www.coinbase.com/developer-platform/products/x402)
- 一次情報: [Coinbase x402 docs](https://docs.cdp.coinbase.com/x402/welcome)
- 一次情報: [Coinbase Agentic.Market launch](https://www.coinbase.com/en-ca/developer-platform/discover/launches/agentic-market)
- 一次情報: [Coinbase / AWS AgentCore Payments](https://www.coinbase.com/blog/introducing-amazon-bedrock-agentcore-payments-powered-by-x402-and-coinbase)
- 一次情報: [Coinbase / Nium stablecoin payments](https://www.coinbase.com/en/developer-platform/discover/launches/nium)
