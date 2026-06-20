---
title: "MOC: 企業"
type: moc
updated: 2026-06-20
tags:
  - company
  - stablecoin
  - payments
---

# MOC: 企業

ステーブルコイン決済・エージェント決済・オンチェーン金融インフラに関わる企業ページの索引。

ニュース単体ではなく、企業ごとの「現状」「戦略」「関連 inbox ニュース」を追うために使う。
プロダクト単位の比較は [[06_Entities/Products/index|Product Notes]] を起点にする。

---

## 企業ページ

| 企業 | 現在の主な位置づけ | 関連テーマ |
|---|---|---|
| [[Stripe]] | PSP / Bridge / Tempo / Privy / Link を組み合わせ、法定通貨圏とステーブルコイン決済を接続 | stablecoin payments, MPP, Bridge, wallet |
| [[Coinbase]] | x402 / Base / CDP / custody / USDC 流動性でオンチェーン決済の開発者基盤を形成 | x402, agentic commerce, USDC payments |
| [[Circle]] | USDC 発行体・CPN・Arc・Agent Stack でエージェント経済の中央インフラ競争の主要プレイヤー | USDC, CPN, agent-stack, stablecoin payments |
| [[Visa]] | TAP・VIC・Agentic Registry でカードネットワーク側のエージェント決済インフラを整備 | agentic commerce, TAP, stablecoin settlement |
| [[Mastercard]] | AP4M・ステーブルコイン 24/7 オンチェーン清算・BVNK 買収でフルスタック化 | AP4M, agentic commerce, stablecoin settlement |
| [[Google]] | AP2 / UCP 主導でエージェントコマースの ID・カタログ・決済承認の標準化を推進 | AP2, UCP, agentic commerce |
| [[AllUnity]] | EU MiCA 準拠非 USD EMT（EURAU/CHFAU/SEKAU）+ x402 Agentic Payments で欧州エージェント決済レールを構築 | MiCA, x402, stablecoin-issuer, Europe |
| [[Block-CashApp]] | Cash App の USDC 機能（6,000 万 MAU）で消費者向けステーブルコイン決済を主流化 | USDC, consumer payments, stablecoin payments |
| [[Fireblocks]] | Agentic Payments Suite（Gateway + Wallets）+ x402 Foundation 参加で機関グレードエージェント決済インフラを提供 | x402, agentic commerce, custody |
| [[Parallel]] | エージェント向けウェブ API（MPP/x402 実装）+ Index コンテンツ補償モデルで API billing の実装事例を提供 | x402, MPP, api-billing |
| [[Robinhood]] | Agentic Trading・Agentic Credit Card で消費者エージェント決済を Mastercard レール上で実規模実装 | agentic commerce, consumer payments |
| [[WesternUnion]] | USDPT・DAN・Stable Card で既存 200 カ国送金ネットワークをステーブルコインレールに転換中 | stablecoin payments, cross-border, offramp |

---

## 追加候補

| 企業 | 追加する理由 |
|---|---|
| AWS | AgentCore Payments、x402 採用、エージェント決済のクラウド実装 |
| Tempo | Stripe / Paradigm 支援の決済特化チェーン。Stripe ページの補助から独立化余地あり |

---

## 運用ルール

- 企業ページは `06_Entities/Companies/` に置く。
- プロダクト単位のノートは `06_Entities/Products/` に置く。
- 1社1ファイルを原則とする。
- 子会社・買収企業・主要プロダクトは、当面は親会社ページの `aliases` と本文セクションにまとめる。
- ニュースが 3 件以上たまり、独自戦略として追う価値が出たら独立ページ化する。
- 各企業ページには以下を含める。
  - 現状の要約
  - 何をしているか
  - inbox との紐付け
  - 競争上の論点
  - 監視ポイント
  - 参考リンク

---

## 関連 MOC

- [[MOC_Stablecoin_Payments]]
- [[MOC_Protocols]]
- [[MOC_Regulation]]
- [[MOC_agent-payments-stack]]
