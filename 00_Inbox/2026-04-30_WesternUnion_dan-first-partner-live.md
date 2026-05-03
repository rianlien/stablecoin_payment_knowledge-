---
title: "Western Union Digital Asset Network（DAN）、初パートナー稼働開始——USDPT は 5 月ローンチへ"
date: 2026-04-30
source: "Yahoo Finance / DefenseWorld / CoinDesk"
source_url: https://finance.yahoo.com/markets/crypto/articles/western-union-unveils-timeline-stablecoin-145505891.html
entity: WesternUnion
category: payments
tags:
  - stablecoin
  - payments
  - wallet
  - psp
summary: "Western Union の Digital Asset Network（DAN）が 2026 年 4 月最終週に初パートナーとの稼働を開始した。DAN は暗号資産ウォレットと WU の全世界 36 万拠点の現金ネットワークを API 一本で接続するオフランプインフラ。2026 年中に 7 社以上のパートナーが追加予定。Solana ベースの USDPT は 5 月ローンチが維持されている。"
implications: "オンチェーンステーブルコインを「最後の 1 マイル」で現金に変換できるグローバルインフラが初めて実際に稼働したことは、ステーブルコインのオフランプ設計において重要な参照点になる。世界 200 カ国以上・36 万拠点のオフランプが API 経由で利用可能になることの意味は大きい。"
follow_up: "初パートナーの社名・対応国、USDPT 5 月ローンチの正式日・対象地域、DAN の KYC/AML フロー詳細"
---

## 概要

Western Union が 2026 年 4 月 24 日の Q1 決算コールで予告していた **Digital Asset Network（DAN）** の初パートナー稼働が、2026 年 4 月最終週（4 月 27 日週）に実現した。DAN は暗号資産ウォレットユーザーが Western Union の全世界ネットワーク（200 カ国超・36 万拠点）を経由して資産を現地通貨で引き出せるオフランプインフラ。CEO の Devin McGranahan は同週に「今週、最初の DAN パートナーが稼働した」と確認した。

なお、Solana ベースの自社ステーブルコイン USDPT のパイロットローンチも引き続き 5 月を予定している。

## 何が起きたか

- 2026 年 4 月最終週（4 月 27 日〜5 月 3 日の間）、DAN の初パートナーが正式稼働
- 2026 年中に **7 社以上**のパートナーが追加予定
- **DAN の仕組み**：暗号資産ウォレット（任意）と Western Union の現金ネットワークを接続する API。ユーザーはウォレットから資産を送り、WU の 36 万拠点で現地通貨として現金を受け取れる
- **USDPT（Solana ベース USD 担保ステーブルコイン）**の 5 月パイロットローンチは計画通り維持
- 発行体は Anchorage Digital Bank（連邦認可の暗号資産カストディアン）
- 初期用途：消費者ウォレット → B2B エージェントへの資金決済（SWIFT 代替）
- **Stable Card**（USDPT ベース・Visa × Rain 共同開発）は 2026 年後半、数十カ国での展開予定

## なぜ重要か

### 決済事業者視点

- ステーブルコインのオフランプが「特定の取引所 or ネオバンク経由」ではなく、世界最大規模の現金送金ネットワーク経由で提供されることは、PSP のオフランプ戦略に直接影響する
- DAN を API 経由で自社プロダクトに統合できれば、自社でオフランプインフラを構築せずに 200 カ国・36 万拠点のオフランプ機能を提供できる可能性がある

### 加盟店視点

- ステーブルコインで受け取った代金を DAN 経由で現地通貨として換金する、新興国向けオフランプルートとして機能しうる
- B2B エージェント向けの用途が先行するが、消費者向け拡張（Stable Card）が並走して進む

### プロダクト視点

- 「暗号ウォレット → DAN API → 現金引き出し」というフローの UI/UX 設計は、ウォレット事業者・オフランプサービスにとっての実装参照になる
- USDPT + DAN + Stable Card という 3 層のアーキテクチャは、オンチェーン→オンランプ→現地利用 を一本のブランドで完結させる設計であり、自社プロダクトの比較対象

### 規制 / リスク視点

- DAN の AML・KYC フローは Western Union のグローバル規制対応実績に依拠していると想定されるが、ウォレット送金元の本人確認（Travel Rule）がどう処理されるかは非公開
- USDPT は GENIUS Act の PPSI（Permitted Payment Stablecoin Issuer）要件との整合性を Anchorage Digital Bank の連邦特許で確保する設計

## 我々への示唆

- いま検討すべきこと:
  - DAN の API 仕様（公開されれば）を確認し、自社のオフランプ設計と比較評価
  - 対応ウォレット・対応ステーブルコインのリストが公開され次第、自社プロダクトとの相互運用性を確認
- 後で深掘りすべきこと:
  - 7 社以上の DAN パートナーの名称・地域・ユースケースが公開されたタイミングで競合分析
  - Stable Card の展開スケジュールと日本・東南アジアへの展開有無
- 今は優先度が低いこと:
  - USDPT 自体のトークノミクス（自社プロダクトへの直接統合可能性は当面限定的）

## 未解決の論点

- DAN 初パートナーの社名・対応国・サービス内容は非公開
- DAN の Travel Rule 対応（ウォレット送金元 KYC）の実装方法
- USDPT パイロットの「5 月」が上旬か下旬か、対象国はどこか
- DAN の手数料体系・為替スプレッドの競争力

## 参考リンク

- 一次情報:
  - [Yahoo Finance（Q1 決算後インタビュー、2026-04-29）](https://finance.yahoo.com/markets/crypto/articles/western-union-unveils-timeline-stablecoin-145505891.html)
  - [DefenseWorld（Q1 Earnings Call ハイライト、2026-04-29）](https://www.defenseworld.net/2026/04/29/western-union-q1-earnings-call-highlights.html)
- 補足情報:
  - [Western Union USDPT ローンチ予告（2026-04-24）](./2026-04-24_WesternUnion_usdpt-stablecoin-launch.md)
  - [CoinDesk（2026-04-27）](https://www.coindesk.com/business/2026/04/27/western-union-eyeing-stablecoin-launch-to-settle-global-transactions-without-swift-ceo-says)

## 重要度

- Medium

## 確からしさ

- Medium（「今週稼働」の発言は確認済みだが、パートナー名・対応国は未公開）
