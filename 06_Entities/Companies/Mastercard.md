---
title: "Mastercard"
type: company
updated: 2026-06-15
category: payments
tags:
  - agentic-commerce
  - stablecoin
  - machine-payments
  - agent-identity
  - payment-rails
---

# Mastercard

Mastercard は世界最大規模のカード決済ネットワークの一つであり、2025〜2026 年にかけて Agent Pay・AP4M（Agent Pay for Machines）・ステーブルコイン決済の 24/7 オンチェーン対応・Verifiable Intent という一連の取り組みを通じて、agentic commerce インフラの中心プレイヤーとして急速にポジションを確立している。BVNK 買収（最大 18 億ドル、2026 年末クローズ予定）により、ステーブルコイン発行・清算・カードネットワークのフルスタックを単体で保有する方向に進んでいる。

この vault では、Mastercard を「agentic commerce における TradFi 側の主要インフラ標準化プレイヤー」として追う。

---

## 現状の要約

### 何をしているか

- **AP4M（Agent Pay for Machines）の正式ローンチ**（2026-06-10）：Stripe・Adyen・Coinbase・Solana Foundation・Ripple など 35 社超の launch partner と共に、AI エージェント間の自律決済プロトコルを本番化。カード・銀行口座・ステーブルコイン（USDC・RLUSD）のマルチレールに対応し、Mastercard が最終決済を保証する
- **ステーブルコイン決済の 24/7 本番展開**（2026-06-03）：USDC・PYUSD・RLUSD など 6 種のステーブルコインを Arbitrum・Base・Canton・Ethereum・Polygon・Solana・Tempo・XRPL の 8 チェーンで受け付ける決済レールを本番化
- **Verifiable Intent によるエージェント認可設計**：エージェントごとに支出上限・認可ルールを SD-JWT 形式で定義し、Polygon・Solana・Base のパブリックチェーンに記録することで改ざん不可能な認可の検証可能性を実現（FIDO Alliance・EMVCo・W3C 標準をベース）
- **地域展開**：EEMEA では Yellow Card と提携してアフリカ・中東のステーブルコイン決済パイロットを展開。アジア太平洋では JD.com と Agent Pay の共同探索を開始。欧州では Worldline・ING と組んで本番 agentic payment フローを実装
- **BVNK 買収進行中**：ステーブルコインインフラ企業 BVNK を取得することで、フィアット↔ステーブルコイン清算とカードネットワーク清算の一体化を図る

### 見立て

Mastercard の戦略は「カードレールの上にエージェント決済・ステーブルコイン決済を重ねる」という形で、既存 PSP（Stripe・Adyen）を競合ではなくパートナーとして取り込みながら業界標準化を進めている点が特徴的だ。Verifiable Intent のオープン仕様公開と 35 社超のコンソーシアム形成は、x402・AP2・MPP といった他のエージェント決済プロトコルに対して「決済保証付きの業界標準」としての優位を打ち出す意図が読める。

一方で、Mastercard の決済保証が具体的にどこまでのリスクをカバーするか（チャージバック・詐欺補填）の詳細は未開示であり、この点が加盟店採用の最大の判断軸になる。BVNK 統合後にステーブルコインの清算スタックがどう形成されるかが 2026 年下半期の最重要確認事項。

---

## Inbox との紐付け

### Agent Pay・AP4M（エージェント決済）

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-30 | [[2026-04-30_Mastercard_q1-2026-agent-to-agent-payments]] | Q1 決算で Agent Pay のグローバル全展開・OpenAI との agent-to-agent 決済協業を開示 |
| 2026-05-18 | [[2026-05-18_Mastercard-JDcom_agent-pay-strategic-partnership]] | JD.com と Agent Pay によるアジェンティック購買ソリューションの共同探索を発表 |
| 2026-06-02 | [[2026-06-02_Worldline-ING-Mastercard_agentic-payments-europe]] | Worldline・ING と欧州で本番 agentic payment フローを実装 |
| 2026-06-10 | [[2026-06-10_Mastercard_agent-pay-for-machines-ap4m]] | AP4M 正式ローンチ：35 社超パートナー、Verifiable Intent オンチェーン公開、マルチレール対応 |

### ステーブルコイン決済・決済レール

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-04 | [[2026-05-04_Rain-Mastercard_stablecoin-card-settlement]] | Rain が Mastercard のステーブルコインカード決済パートナーとして登場 |
| 2026-05-04 | [[2026-05-04_Rain_mastercard-principal-member]] | Rain が Mastercard のプリンシパルメンバーに就任 |
| 2026-06-03 | [[2026-06-03_Mastercard_stablecoin-settlement-24-7-onchain]] | USDC・PYUSD・RLUSD を 8 チェーンで 24/7 受け付けるステーブルコイン決済を本番展開 |

### 地域展開・パートナーシップ

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-06 | [[2026-05-06_Mastercard-YellowCard_stablecoin-eemea]] | Yellow Card と EEMEA でのステーブルコイン決済パイロット（クロスボーダー送金・B2B清算・ロイヤルティ・トレジャリーの 4 領域） |

---

## 監視ポイント

- **BVNK 買収クローズ**（2026 年末予定）後のステーブルコイン清算スタック——BVNK の既存クライアント引き継ぎと AML リスク管理の詳細
- **AP4M の決済保証範囲**——チャージバック・詐欺補填がどこまでカバーされるか（加盟店採用の最大判断軸）
- **Verifiable Intent の技術的互換性**——x402（ERC-7715 セッションキー）・AP2（W3C VC）との相互運用性または競合関係の明確化
- **ステーブルコイン決済のグローバル展開タイムライン**——米国・ラテンアメリカ以外の地域（アジア太平洋・欧州）への展開時期
- **GENIUS Act 準拠設計の詳細**——AP4M が PPSI 要件を満たすステーブルコインのみを対象とするか、ラッピング設計があるかどうか
- **OpenAI との agent-to-agent 決済の具体的プロトコル仕様**——Q1 2026 決算で開示された協業の詳細
- **Worldline・ING の欧州実装の仕様公開**——agentic transaction 識別子・チャージバック責任分担の詳細

---

## 参考リンク

- [Mastercard Q1 2026 決算資料](https://investor.mastercard.com/files/doc_financials/2026/q1/1Q26-Mastercard-Earnings-Release.pdf)
- [Mastercard ステーブルコイン決済プレスリリース（2026-06-03）](https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html)
- [Verifiable Intent 公式仕様書](https://verifiableintent.dev/spec/credential-format/)
- [GitHub — agent-intent/verifiable-intent](https://github.com/agent-intent/verifiable-intent/)
- [AP4M ローンチ — The Block（2026-06-10）](https://www.theblock.co/amp/post/404288/mastercard-agent-pay-machines-support-autonomous-ai-transactions-stablecoins)
- [Mastercard × Yellow Card プレスリリース（2026-05-06）](https://www.prnewswire.com/apac/news-releases/mastercard-and-yellow-card-partner-to-unlock-stablecoin-payment-innovation-across-eemea-302765347.html)
