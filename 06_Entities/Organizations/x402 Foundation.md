---
title: "x402 Foundation"
type: organization
updated: 2026-06-16
category: standards-body
parent: Linux Foundation
tags:
  - x402
  - standards
  - governance
  - agentic-commerce
  - payments
aliases:
  - x402 Foundation
  - Linux Foundation x402 Foundation
---

# x402 Foundation

x402 Foundation は、Linux Foundation 傘下で x402 プロトコルの標準化・ガバナンスを担う組織。会社・事業主体としての Coinbase は [[Coinbase]]、プロトコル実装や仕様論点は [[x402-ecosystem]] / [[x402-batch-settlement]] を参照。

この vault では、x402 Foundation を「Coinbase 起点の x402 を業界横断の標準候補へ移すためのガバナンス組織」として追う。

---

## 現状の要約

### 何を担っているか

- **x402 の中立化**: Coinbase が開発した x402 を Linux Foundation 傘下へ移し、特定企業依存を下げる役割を担う。
- **業界横断メンバーの受け皿**: Adyen、AWS、American Express、Circle、Cloudflare、Coinbase、Fiserv、Google、KakaoPay、Mastercard、Microsoft、Polygon Labs、Shopify、Solana Foundation、Stripe、Visa などが設立メンバーとして記録されている。
- **仕様・拡張のガバナンス**: 対応チェーン、セキュリティ拡張、承認委任レイヤーとの相互運用など、x402 の標準化論点を扱う母体。
- **エンタープライズ化の入口**: Fireblocks の参加により、PSP・銀行・フィンテック向けのコンプライアンス、KYT、Travel Rule、spend governance との接続が強まっている。

### 見立て

x402 Foundation は企業ではなく、標準化・ガバナンス組織として扱うべき対象。Coinbase の戦略ページに吸収すると「誰が事業を持つのか」と「誰が標準を管理するのか」が混ざるため、Organizations 配下に分けておくのが自然。

---

## 主要レイヤー

| レイヤー | x402 Foundation の役割 | 意味 |
|---|---|---|
| Governance | Linux Foundation 傘下で x402 を管理 | Coinbase 単独主導から業界標準候補へ移行する根拠 |
| Membership | 決済、クラウド、チェーン、EC、ウォレット事業者が参加 | PSP・クラウド・チェーン横断の採用障壁を下げる |
| Protocol evolution | 対応チェーン、セキュリティ拡張、承認委任との接続 | x402 が単なる決済実行から実運用可能な標準へ進むかを左右する |
| Market signal | 主要決済企業の参加実績 | Visa / Mastercard / Stripe などが競合しつつ標準化にも参加する構図を示す |

---

## 関連主体との関係

- **[[Coinbase]]**: x402 の創始・主要実装・CDP facilitator を担う企業。
- **[[Base]]**: x402 の主要なオンチェーン実行環境。
- **Fireblocks**: x402 Foundation に参加し、request integrity と spend governance を含む security extension を提供。
- **Stripe**: x402 Foundation 参加企業でありつつ、独自に MPP / Tempo も推進する。
- **Google / AP2**: AP2 は FIDO Alliance 側の標準化ルート。x402 とは競合だけでなく、承認委任レイヤーとして補完する可能性がある。

---

## Inbox との紐付け

### 標準化・設立

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-02 | [[2026-04-02_x402-Foundation_linux-foundation-launch]] | Linux Foundation 傘下に x402 Foundation を設立し、x402 を OSS 標準として移管 |

### チェーン拡張・仕様展開

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-13 | [[2026-05-13_x402_batch-settlement-sub-cent-ai-payments]] | x402 バッチ決済対応。サブセントの AI マイクロペイメントを可能にする仕様拡張 |
| 2026-05-14 | [[2026-05-14_x402_arbitrum-launch-agent-payments]] | Arbitrum 対応により、x402 のマルチチェーン展開が進む |

### ガバナンス・エンタープライズ対応

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-05-20 | [[2026-05-20_Fireblocks_x402-foundation-agentic-payments-suite]] | Fireblocks が x402 Foundation に参加し、機関向け agentic payments suite と security extension を提供 |
| 2026-05-27 | [[2026-05-27_x402_approval-gap-volume-data]] | x402 の承認ギャップが定量化され、AP2 / Fireblocks Policy Engine との相互運用が焦点に |

---

## 監視ポイント

- x402 Foundation の技術ガバナンスプロセスが公開されるか
- Fireblocks の security extension が x402 標準仕様に取り込まれるか
- AP2 / FIDO Alliance との spending mandate 相互運用仕様が出るか
- Coinbase facilitator 以外の独立 facilitator が増えるか
- 対応チェーン・対応ステーブルコインの拡張が、Foundation 主導の標準として整理されるか
- Stripe MPP / Mastercard AP4M / Circle Nanopayments との競合・補完関係がどう定義されるか

---

## 関連ページ

- [[x402-ecosystem]]
- [[x402-batch-settlement]]
- [[Coinbase]]
- [[Base]]
- [[MOC_Protocols]]
- [[MOC_agent-payments-stack]]

---

## 参考リンク

- 一次情報: [Linux Foundation press release](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol)
- 補足情報: [CoinDesk](https://www.coindesk.com/tech/2026/04/02/coinbase-s-ai-payments-system-joins-linux-foundation-gathers-support-from-google-stripe-aws-and-others)
- 一次情報: [x402](https://www.x402.org/)
