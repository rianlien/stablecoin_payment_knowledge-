---
title: "Circle"
type: company
updated: 2026-06-15
category: payments
tags:
  - stablecoin
  - USDC
  - agent-payments
  - payment-rails
  - agentic-commerce
---

# Circle

Circle Internet Group は USDC の発行体であり、ステーブルコイン決済インフラの中核プロバイダー。2026 年に入り、USDC の単なる発行・流通基盤にとどまらず、AI エージェント向けの決済フルスタック（Agent Stack）と機関向け決済ネットワーク（CPN）を一体で展開するインフラ企業へと明確に転換した。Arc ブロックチェーン（機関向け L1）の $222M 資金調達により、Stripe や Coinbase と並ぶエージェント経済の中央インフラ競争の主要プレイヤーとして位置づけられている。

この vault では、Circle を「USDC を軸にエージェント決済スタックと機関向け決済ネットワークを垂直統合しようとしている企業」として追う。

---

## 現状の要約

### 何をしているか

- **USDC 発行・流通基盤**：流通量 $77B（2026年5月時点）、オンチェーン累計 $70 兆超の決済処理実績。OCC 国内信託チャーター条件付き承認（2025年12月）により連邦規制基盤を確立
- **Circle Payments Network（CPN）**：銀行・PSP・フィンテックが自社でデジタル資産を保有せずに USDC 決済レールにアクセスできる B2B 決済ネットワーク。年間換算取引量 $83 億（2026年3月末）。Veem・Thunes・Worldline・Nium などが参加し、190 カ国・100 通貨でのペイアウトに対応
- **Agent Stack**：AI エージェント向けの決済インフラスイート（agents.circle.com）。Agent Wallets（ポリシー制御型）・Nanopayments（最小 $0.000001 USDC・ガスフリー・11チェーン対応）・Agent Marketplace・Circle CLI の 4 製品を正式提供（2026年5月11日ローンチ）
- **Arc ブロックチェーン**：機関向け L1「Economic Operating System」。Summer 2026 メインネット予定。$222M トークンプレセール完了（a16z $75M リード、BlackRock・Apollo・ICE・SBI Group 参加）
- **Circle Mint / 社内採用実績**：グループ 8 子会社間 $6,800 万の移転価格決済を USDC で 30 分以内に完了（2026年3月）。企業財務への USDC 活用の概念実証として機能

### 見立て

Circle は 2026 年に「USDC 発行体」から「エージェント決済の中央インフラ」への戦略転換を明確にした。CPN（機関向け決済ネットワーク）と Agent Stack（エージェント向け決済プリミティブ）を同時に展開することで、決済フローの上流（エージェントが USDC を支払う）から下流（CPN + Nium でローカル通貨着地）までを垂直統合する構造を作ろうとしている。Stripe（Tempo + MPP）・Coinbase（x402）・AWS（AgentCore Payments）と競合しながら、Arc という自社チェーンを持つ点で独自の競争軸を形成する。

一方で、Circle が CPN や Agent Wallets の中間レイヤーを握ることによるロックインリスク、GENIUS Act 下での PPSI ライセンス要件への対応、ARC トークンの証券性リスクなど、監視すべき不確実性も多い。今後 6〜12 か月が、Circle が「デファクトのエージェント決済インフラ」として定着できるかどうかの分水嶺になる。

---

## Inbox との紐付け

### 社内採用・実証

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-03-07 | [[2026-03-07_Circle_usdc-internal-treasury]] | USDC を社内 B2B 決済に本格採用、8 子会社間 $6,800 万を 30 分以内に決済 |

### Nanopayments・Agent Stack ローンチ

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-29 | [[2026-04-29_Circle_nanopayments-mainnet]] | Nanopayments メインネット正式稼働（11 チェーン・ガスフリー・最小 $0.000001）|
| 2026-05-01 | [[2026-05-01_Circle_nanopayments-mainnet]] | Nanopayments メインネット続報 |
| 2026-05-11 | [[2026-05-11_Circle_agent-stack-nanopayments-launch]] | Agent Stack 正式ローンチ（Agent Wallets・Nanopayments・Marketplace・CLI）|
| 2026-05-11 | [[2026-05-11_Circle_agent-stack-nanopayments-agentic-economy]] | Agent Stack のエージェント経済向け位置づけ詳細 |
| 2026-05-11 | [[2026-05-11_Circle_agent-stack-arc-launch]] | Arc ブロックチェーン $222M 資金調達・a16z/BlackRock/Apollo 参加 |

### CPN・決済ネットワーク拡大

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-08 | [[2026-04-08_Circle_cpn-managed-payments]] | CPN Managed Payments 正式ローンチ（Worldline・Veem・Thunes 参加）|
| 2026-05-27 | [[2026-05-27_Circle-Nium_cpn-usdc-global-payouts]] | Nium が CPN グローバルペイアウトパートナーに参加（190 カ国・100 通貨）|
| 2026-06-11 | [[2026-06-11_MassPay-Coinbase_stablecoin-payouts]] | MassPay が Coinbase USDC インフラと Circle CPN を活用してグローバルペイアウトを展開 |

---

## 監視ポイント

- **Arc メインネット稼働（Summer 2026 予定）**：Ethereum・Solana・Base に加えて Circle 自社チェーンが稼働した場合の PSP の chain selection への影響。Visa・Mastercard の Arc 対応発表の有無
- **Agent Marketplace の成長**：x402 や MCP との互換性を持つサービスが登録されるか、独自スタックで閉じるか。エージェントからの商業受注の実事例が出るか
- **Nanopayments の手数料モデル**：ガスフリーを維持する Circle の収益化構造。大量エージェントトラフィック発生時のコスト持続可能性
- **GENIUS Act 対応**：PPSI ライセンス申請状況と CPN 参加金融機関への要件波及
- **ARC トークンの規制リスク**：米国での証券性判断。CLARITY Act の市場構造規制対象になるか
- **競合との差別化**：Stripe Tempo・Coinbase x402・AWS AgentCore との技術・手数料・カバレッジ比較が明確になる時期

---

## 参考リンク

- [Circle 公式サイト](https://www.circle.com)
- [Circle Agent Stack](https://agents.circle.com)
- [Circle Nanopayments 製品ページ](https://www.circle.com/nanopayments)
- [CPN Managed Payments プレスリリース（2026-04-08）](https://www.circle.com/pressroom/circle-launches-cpn-managed-payments-a-full-stack-platform-for-seamless-stablecoin-settlement)
- [Agent Stack ローンチ プレスリリース（2026-05-11）](https://www.circle.com/pressroom/circle-launches-ai-infrastructure-to-power-the-agentic-economy)
- [Nium × CPN プレスリリース（2026-05-27）](https://www.circle.com/pressroom/nium-and-circle-to-connect-usdc-settlement-with-global-payouts)
