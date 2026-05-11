---
title: "Western Union、USDPT ステーブルコインを Solana メインネットで正式ローンチ——エージェント決済・200か国オフランプ接続"
date: 2026-05-04
source: "BusinessWire / Decrypt / CoinDesk"
source_url: "https://www.businesswire.com/news/home/20260504531737/en/Western-Union-Launches-USDPT-on-Solana-Advancing-Regulated-Digital-Infrastructure-for-Global-Payments"
entity: "WesternUnion"
category: "payments"
tags:
  - stablecoin
  - payments
  - psp
  - wallet
summary: "Western Union が 2026 年 5 月 4 日、Solana ブロックチェーン上で自社ステーブルコイン USDPT（U.S. Dollar Payment Token）を正式ローンチ。発行体は連邦認可の Anchorage Digital Bank N.A.。初期ユースケースはエージェント間・内部清算で、消費者向け「Stable by Western Union」は 2026 年内に 40 か国以上で展開予定。Digital Asset Network（DAN）は免許保有の仮想通貨取引所・カストディアンと WU の 200 か国・36 万拠点を API 接続するオフランプインフラとして同時稼働。"
implications: "世界最大規模の送金ネットワークがステーブルコインレールに移行したことで、PSP のオフランプ設計・競合分析において WU の DAN が重要な参照インフラになった。Fireblocks を技術基盤に選択した点はカストディ・鍵管理のエンタープライズ標準との整合を示す。"
follow_up: "Stable by Western Union の 40 か国展開タイムライン・対象国、DAN API の外部統合要件、USDPT の GENIUS Act PPSI 準拠状況の詳細、Fireblocks 統合の技術スタック"
---

## 概要

Western Union は 2026 年 5 月 4 日（BusinessWire 公式プレスリリース日）、Solana ブロックチェーン上で自社初のステーブルコイン USDPT（U.S. Dollar Payment Token）を正式ローンチした。同社が 2025 年 10 月に発表し、2026 年 4 月末の Q1 決算で 5 月ローンチを改めて確認していた計画が具体化したもの。

## 何が起きたか

**USDPT の基本仕様**
- 発行体：Anchorage Digital Bank N.A.（米国初の連邦認可暗号資産銀行）
- チェーン：Solana
- 裏付け：米ドル 1:1 で完全準備
- カストディ技術基盤：Fireblocks（2026 年 5 月 1 日付でパートナーシップ発表）

**初期ユースケース**
- WU の全世界エージェントネットワーク間の資金清算（SWIFT 代替）
- WU 内部トレジャリー管理
- 免許保有仮想通貨取引所・カストディアンとの流動性決済

**Digital Asset Network（DAN）の同時稼働**
- 免許保有の仮想通貨取引所・カストディアンを WU グローバル支払いインフラに API 接続
- エンドユーザーがオンチェーン資産を現地通貨として 200 か国・36 万拠点で受け取り可能なオフランプインフラ
- 2026 年中に 7 社以上のパートナーが追加予定（初パートナーは 4 月最終週に稼働済み）

**消費者向けプロダクト（今後）**
- 「Stable by Western Union」：2026 年内に 40 か国以上でリリース予定のコンシューマー向け支払い機能
- Visa × Rain 共同開発の Stable Card（USDPT 担保）も 2026 年後半に展開予定

**規制対応**
- USDPT は GENIUS Act の PPSI（Permitted Payment Stablecoin Issuer）要件に Anchorage Digital Bank の連邦特許で準拠する設計
- 2026 年 5 月 5 日の CoinDesk アナリスト記事が「USDPT は WU の収益モデルを再構築しうる」と評価

## なぜ重要か

### 決済事業者視点
- 1 億人超の顧客・200 か国・36 万拠点という世界最大規模の送金ネットワークがステーブルコインレールで稼働することで、PSP がオフランプ設計を検討する際の主要参照先が変化する
- DAN の API を通じて既存ウォレット・オンチェーンプロダクトを WU の現金払い出しネットワークに接続できる可能性が生まれた

### 加盟店視点
- ステーブルコインで受け取った代金の現地通貨換金ルートとして DAN が機能しうる。特に新興国・銀行口座普及率の低い市場でのオフランプが実用的になる

### プロダクト視点
- Solana の低コスト・高スループット選択は、決済用途でのチェーン選定の参照例になる
- Fireblocks をカストディ・鍵管理に採用した点は、エンタープライズ向けステーブルコイン発行の「業界標準スタック」として確認される

### 規制 / リスク視点
- Anchorage Digital Bank（連邦認可）が発行体になることで GENIUS Act の PPSI 要件に準拠する「銀行系ステーブルコイン発行モデル」が確立した
- DAN の Travel Rule・KYC フローの詳細は未公開。ウォレット送金元の本人確認がどう処理されるかが規制リスクの主要論点

## 我々への示唆

- いま検討すべきこと:
  - DAN の外部パートナー参加要件（免許・対応地域・手数料）を問い合わせ、自社プロダクトのオフランプ強化に活用できるか評価
  - Stable by Western Union（40 か国展開予定）の対象地域が自社サービス地域と重複するかを確認し、競合・協業のシナリオを整理
- 後で深掘りすべきこと:
  - Fireblocks + Anchorage + Solana の技術スタック詳細と自社統合コストの試算
  - USDPT の Travel Rule 対応・AML スクリーニング実装の詳細（規制コンプライアンス参照）
- 今は優先度が低いこと:
  - Stable Card（USDPT × Visa × Rain）の個人向けリテール詳細。自社がカード発行体でない限り直接の実装検討は不要

## 未解決の論点

- DAN の外部統合 API は公開予定か、招待制か
- Stable by Western Union の 40 か国はどの地域か（アジア・LATAM・アフリカ？）
- USDPT の GENIUS Act PPSI 準拠の具体的な申請・承認状況
- Fireblocks は清算の技術基盤だが、エンドユーザーの KYC・AML は誰が担うか

## 参考リンク

- 一次情報: [BusinessWire 公式プレスリリース（2026-05-04）](https://www.businesswire.com/news/home/20260504531737/en/Western-Union-Launches-USDPT-on-Solana-Advancing-Regulated-Digital-Infrastructure-for-Global-Payments)
- 一次情報: [Fireblocks パートナーシップ PR Newswire（2026-05-01）](https://www.prnewswire.com/news-releases/western-union-selects-fireblocks-to-power-its-first-stablecoin-usdpt-302760774.html)
- 補足情報: [Decrypt（2026-05-04）](https://decrypt.co/366677/western-union-usdpt-stablecoin-solana-anchorage-digital)
- 補足情報: [CoinDesk アナリスト評価（2026-05-05）](https://www.coindesk.com/business/2026/05/05/western-union-s-solana-based-stablecoin-could-reshape-its-payment-model-analyst-says)
- 関連ノート: [WU USDPT 発表（2026-04-24）](./2026-04-24_WesternUnion_usdpt-stablecoin-launch.md)
- 関連ノート: [WU DAN 初パートナー稼働（2026-04-30）](./2026-04-30_WesternUnion_dan-first-partner-live.md)

## 重要度
- High

## 確からしさ
- High（BusinessWire 公式プレスリリース・Fireblocks PR Newswire による）
