---
title: "Coinbase、DAI を 5 月 4 日に上場廃止——残高を USDS へ自動移行、EEA ユーザーは対象外"
date: 2026-04-30
source: "Coinbase ヘルプ / crypto.news / CoinAlertNews"
source_url: "https://help.coinbase.com/en/coinbase/trading-and-funding/sending-or-receiving-cryptocurrency/token-migrations"
entity: "Coinbase / Sky Protocol（旧 MakerDAO）"
category: "プラットフォーム対応"
tags:
  - stablecoin
  - wallet
  - regulation
summary: "Coinbase が 2026 年 4 月 30 日に、DAI（MakerDAO）の 5 月 4 日上場廃止と残高の USDS（Sky Protocol）への自動移行（1:1）を発表。EEA ユーザーは自動移行対象外。DAI → USDS のエコシステム移行がメジャー取引所主導で加速する一方、欧州では規制対応から自動移行を回避。"
implications: "MakerDAO の USDS 移行が主要 CEX での強制移行で加速。分散型ステーブルコインの中で最大規模だった DAI のエコシステムが USDS に統一される動きが本格化。EEA ユーザーの除外は MiCA コンプライアンス上の課題を示唆。"
follow_up: "EEA ユーザー向けの DAI 処理方法の明確化、USDS の MiCA 準拠状況、他取引所の DAI→USDS 対応タイムライン"
---

## 概要

Coinbase は 2026 年 4 月 30 日、DAI（Ethereum ベースのステーブルコイン、MakerDAO 管理）の取引を 2026 年 5 月 4 日に停止すると発表した。同日以降、Coinbase 上に残る DAI 残高は USDS（Sky Protocol、旧 MakerDAO が DAI のアップグレード版として発行）へ 1:1 で自動変換される。ただし欧州経済領域（EEA）の特定ユーザーは自動移行の対象外となっており、セルフカストディウォレットへの移動を 5 月 4 日までに行う必要がある。

## 何が起きたか

- **発表日**：2026 年 4 月 29〜30 日
- **上場廃止日**：2026 年 5 月 4 日（取引・送受信の一時停止）
- **送受信再開**：2026 年 5 月 6 日以降（ただし取引は再開せず）
- **自動変換**：Coinbase 上の DAI 残高を 1 DAI : 1 USDS のレートで USDS に自動変換
- **EEA ユーザーの扱い**：EEA の特定国ユーザーは自動移行対象外——5 月 4 日までにセルフカストディウォレットへ移動が必要
- **背景**：MakerDAO が 2024 年に Sky Protocol に組織改名し、DAI（旧ステーブルコイン）の後継として USDS（USD Savings）を発行済み。Coinbase はこの移行を取引所レベルで実施する形

## なぜ重要か

### 決済事業者視点

- Coinbase という大手 CEX が DAI を正式に上場廃止し USDS へ移行したことで、DAI を決済手段として組み込んでいる PSP・ウォレット・ゲートウェイはポジション変更を迫られる
- Shift4 のステーブルコイン清算では DAI も対応リストに含まれていたが、他取引所・PSP の DAI 対応ロードマップを確認する必要がある

### 加盟店視点

- DAI 建て決済を受け入れていた加盟店や DAI をトレジャリー資産として保有している企業は、USDS への移行コストと法的・会計処理の確認が必要

### プロダクト視点

- 分散型ステーブルコイン（DAI）が主要 CEX での扱いを失い、ガバナンストークン型から規制準拠型（USDC 等）への重力移動がさらに加速
- USDS は Sky Protocol ガバナンス下であり、GENIUS Act 準拠の「許可型発行体」要件との整合がどうなるかは未確認

### 規制 / リスク視点

- EEA ユーザーが自動移行対象外とされていることは、USDS が MiCA 上の「電子マネートークン（EMT）」規制要件を満たしていない可能性を示唆
- MiCA 下では、USDT と同様に非 EMT ステーブルコインの大規模流通に制限があるため、USDS の欧州展開は規制整備待ちの状態

## 我々への示唆

- いま検討すべきこと:
  - 自社プロダクト・決済フローで DAI を使用・保有しているかの確認。Coinbase 経由の場合は 5 月 4 日までに対応
  - USDS の発行体（Sky Protocol）の準備資産・コンプライアンス情報を確認し、DAI の代替として適切かを評価
- 後で深掘りすべきこと:
  - USDS の MiCA 準拠状況と欧州での利用可能性の確認
  - 他の主要 CEX（Binance・Kraken・OKX 等）の DAI 廃止・USDS 移行スケジュール
- 今は優先度が低いこと:
  - DAI のオンチェーン担保構造の詳細（MakerDAO プロトコルの技術的変更）

## 未解決の論点

- USDS は GENIUS Act における「許可型ステーブルコイン発行体」要件を満たすか？
- EEA ユーザーへの USDS 自動移行が回避された理由は MiCA 非準拠か、それとも別の規制要因か？
- DAI がデリスティングされる中で、分散型ステーブルコイン（担保型）全般はエコシステム内での地位を失っていくのか？

## 参考リンク

- 一次情報:
  - [Coinbase ヘルプ：Token migrations](https://help.coinbase.com/en/coinbase/trading-and-funding/sending-or-receiving-cryptocurrency/token-migrations)
- 補足情報:
  - [crypto.news 報道（2026-04-30）](https://crypto.news/coinbase-to-delist-dai-stablecoin-as-may-deadline-approaches/)
  - [CoinAlertNews（2026-04-30）](https://coinalertnews.com/news/2026/04/30/coinbase-delist-dai-stablecoin)
  - [MEXC ニュース](https://www.mexc.com/en-GB/news/1065112)

## 重要度

- Medium

## 確からしさ

- High（Coinbase 公式ヘルプページ・複数メディア一致。EEA 除外の詳細理由は未公表のため推測を含む）
