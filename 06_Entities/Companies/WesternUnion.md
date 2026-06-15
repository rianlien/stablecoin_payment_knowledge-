---
title: "Western Union"
type: company
updated: 2026-06-15
category: payments
tags:
  - stablecoin
  - psp
  - offchain-offramp
  - solana
  - agentic-payments
---

# Western Union

Western Union は世界 200 カ国超・36 万拠点の現金送金ネットワークを持つ決済大手。2025〜2026 年にかけて自社ステーブルコイン USDPT（Solana 上）、グローバルオフランプ API インフラ Digital Asset Network（DAN）、消費者向け Stable Card（USDPT × Visa × Rain）を相次いで立ち上げ、既存の送金ネットワークをステーブルコイン決済レールに転換する大規模な戦略転換を実行中。

この vault では、Western Union を「世界最大規模のラストマイル現金化インフラをステーブルコインに統合する既存大手」として追う。

---

## 現状の要約

### 何をしているか

- **USDPT ローンチ**：Solana 上の USD 担保ステーブルコイン USDPT を 2026 年 5 月 4 日に正式ローンチ。発行体は連邦認可カストディアン Anchorage Digital Bank N.A.、インフラは Fireblocks（カストディ・Payments Engine・Fireblocks Network）。初期展開国はフィリピンとボリビア
- **DAN（Digital Asset Network）稼働**：暗号資産ウォレットと WU の 36 万拠点を API 接続するオフランプインフラ。2026 年 4 月末に初パートナーが稼働、2026 年中に 7 社以上追加予定
- **Stable Card 展開準備**：USDPT 担保・Visa × Rain 共同開発のプリペイドカード「Stable by Western Union」を 2026 年内に 40 カ国以上でリリース予定
- **エージェント B2B 決済への転換**：初期用途はコンシューマーではなく WU グローバルエージェントネットワーク間の清算（SWIFT 代替）。24/7 決済を既存銀行経路なしで実現する設計

### 見立て

Western Union の戦略は「既存送金事業の防衛」ではなく「ステーブルコインによるインフラ再構築」として読むべきである。36 万拠点というオフランプ密度は他の PSP・ステーブルコイン発行体が短期間では追随困難な優位性であり、DAN を API 化したことで WU は「競合」から「インフラ提供者」にもなりうる立場に変わった。

一方で、USDPT が自社ステーブルコインである以上、USDC や USDT と競合するか共存するかの設計は今後の論点になる。Anchorage Digital Bank を発行体に据えた GENIUS Act 対応設計、Fireblocks をカストディに選んだ点は「規制適合エンタープライズ標準スタック」の参照例として業界全体に波及効果を持つ。

---

## Inbox との紐付け

### USDPT・Solana 展開

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-24 | [[2026-04-24_WesternUnion_usdpt-stablecoin-launch]] | Q1 決算コールで CEO が USDPT 5 月ローンチ・DAN・Stable Card を初公表 |
| 2026-05-04 | [[2026-05-04_WesternUnion_usdpt-solana-launch]] | BusinessWire で USDPT Solana 正式ローンチ発表（Anchorage × Fireblocks） |
| 2026-05-04 | [[2026-05-04_WesternUnion_usdpt-solana-mainnet-launch]] | メインネット稼働の詳細——初期ユースケース・DAN 同時稼働・規制対応の整理 |

### DAN パートナーシップ

| 日付 | ノート | 位置づけ |
|---|---|---|
| 2026-04-30 | [[2026-04-30_WesternUnion_dan-first-partner-live]] | DAN 初パートナーが 4 月最終週に稼働、7 社以上追加予定と CEO が確認 |

---

## 監視ポイント

- **DAN パートナー名公開**：初パートナーの社名・対応国・ユースケースが公開された段階で競合・協業分析を更新
- **Stable by Western Union の 40 カ国展開**：対象国リスト・Visa/Rain の役割分担・手数料モデルの公開
- **USDPT の GENIUS Act PPSI 準拠状況**：Anchorage Digital Bank の連邦特許による対応が正式に確認されるか
- **DAN の Travel Rule 対応**：ウォレット送金元 KYC の実装詳細が規制当局に開示される段階
- **フィリピン・ボリビア以外への展開タイミング**：LATAM・東南アジアの展開順序と規制クリア状況
- **USDPT vs USDC/USDT の使い分け**：WU エージェントネットワーク外での USDPT 流動性と競合ステーブルコインとの関係

---

## 参考リンク

- [Western Union IR — USDPT 初回発表（2025）](https://ir.westernunion.com/news/archived-press-releases/press-release-details/2025/Western-Union-Announces-USDPT-Stablecoin-on-Solana-and-Digital-Asset-Network/default.aspx)
- [BusinessWire — USDPT Solana ローンチ公式プレスリリース（2026-05-04）](https://www.businesswire.com/news/home/20260504531737/en/Western-Union-Launches-USDPT-on-Solana-Advancing-Regulated-Digital-Infrastructure-for-Global-Payments)
- [PRNewswire — Fireblocks 選定発表（2026-05-01）](https://www.prnewswire.com/news-releases/western-union-selects-fireblocks-to-power-its-first-stablecoin-usdpt-302760774.html)
- [CoinDesk — USDPT が WU の収益モデルを再構築しうるとのアナリスト評価（2026-05-05）](https://www.coindesk.com/business/2026/05/05/western-union-s-solana-based-stablecoin-could-reshape-its-payment-model-analyst-says)
