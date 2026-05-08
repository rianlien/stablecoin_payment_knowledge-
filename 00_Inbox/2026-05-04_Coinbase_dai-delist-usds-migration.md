---
title: "Coinbase、DAI を 5 月 4 日付で上場廃止——残高を USDS（Sky Protocol）に 1:1 自動移行"
date: 2026-05-04
source: "CoinAlertNews / Crypto.news / Coinbase Help"
source_url: "https://coinalertnews.com/news/2026/04/30/coinbase-delist-dai-stablecoin"
entity: "Coinbase / Sky Protocol (元 MakerDAO)"
category: "stablecoin"
tags:
  - stablecoin
  - regulation
  - wallet
summary: "Coinbase は 2026 年 5 月 4 日付で DAI（ダイ）の取引を停止し、同日中に残高を USDS（Sky Protocol の後継ステーブルコイン）に 1:1 比率・手数料なしで自動移行すると発表（発表日 4 月 30 日）。ただし EU / EEA 指定国のユーザーは自動移行の対象外。5 月 4〜6 日は送金・受け取りも一時停止。MakerDAO が Sky Protocol にリブランドして以降、主要取引所での DAI 廃止が完了する節目となる。"
implications: "主要取引所でのDAI → USDS 移行の完了は、DeFi エコシステムの主要ステーブルコインが SKY プロトコルのガバナンスへ統合されることを意味する。EEA 除外はMiCA 準拠観点から注目。PSP・ウォレット事業者でDAIを扱う場合、USDS への移行対応が必要になりうる。"
follow_up: "EEA 対象国ユーザーへの対応方針（Coinbase の発表）、USDS の MiCA 準拠状況、他取引所での DAI 上場廃止動向"
---

## 概要

2026 年 4 月 30 日、Coinbase は DAI（ダイ）の取引停止と USDS への自動移行計画を発表した。**2026 年 5 月 4 日**を期日として、coinbase.com およびモバイルアプリ上での DAI 取引を停止。5 月 4 日時点で残高のある DAI は **USDS（Sky Protocol）に 1:1・手数料なし**で自動変換される。ただし **EU / EEA 指定国のユーザーは自動移行の対象外**。

## 何が起きたか

- **発表日**：2026 年 4 月 30 日
- **取引停止日**：2026 年 5 月 4 日
- **送受金停止期間**：2026 年 5 月 4 日〜6 日（一時停止後、6 日以降は送受金のみ再開予定）
- **移行レート**：1 DAI → 1 USDS（手数料なし）
- **EEA 対象国除外**：AT・BE・BG・CY・CZ・DE・DK・EE・ES・FI・FR・GR・HR・HU・IE・IS 等の EU/EEA 加盟国のユーザーは自動移行されない（残高の扱いは個別対応が必要）
- **背景**：MakerDAO が 2024 年に **Sky Protocol** にリブランド。DAI の後継として USDS を発行。Coinbase は Sky Protocol との連携を深め、USDC との協調関係も強化している

## なぜ重要か

### 決済事業者視点

- PSP・PayFac が DAI を決済通貨・清算通貨として利用している場合、Coinbase 上での DAI サポート終了に伴い、USDS または他のステーブルコインへの移行が必要になる可能性がある
- USDS は MakerDAO 後継の Sky Protocol が発行するが、USDC より新しい発行体であり、取引相手方リスク・準備金透明性の評価が必要

### 加盟店視点

- DAI 受け取り対応をしている加盟店にとって、Coinbase 上での DAI → USDS 移行は、加盟店側のウォレット管理やバックオフィス処理への影響が生じる可能性がある

### プロダクト視点

- EEA 対象国ユーザーへの移行除外は、欧州向けプロダクトで DAI を扱う場合に特別な対応が必要なことを示す。MiCA 文脈で USDS が EU 認可を受けているかの確認が必要
- Shift4 が USDS も取り扱う場合など、マルチステーブルコイン決済プラットフォームは USDS の流動性確認が要るタイミング

### 規制 / リスク視点

- EEA 対象国除外の背景は、USDS が MiCA 適合の承認を取得していない可能性が高い。規制準拠ステーブルコインを採用するにあたって、MiCA 承認状況の確認が欧州展開の前提条件
- Banking Circle が MiCA 準拠ステーブルコイン清算をサービス化している（4 月 27 日ノート参照）中で、USDS の MiCA 適合性は今後の欧州展開に影響する

## 我々への示唆

- いま検討すべきこと:
  - 自社プロダクト・サービスで DAI を扱っている場合、USDS への移行を受け入れるか、USDC 等への切り替えを選ぶか判断する
  - 欧州ユーザーがいる場合、Coinbase の EEA 除外措置の詳細を確認し、同様のリスクが自社サービスにないか点検
- 後で深掘りすべきこと:
  - USDS の MiCA 承認状況・準備金構成・監査報告の確認
  - Sky Protocol のロードマップ（USDS の流動性・取引所対応状況の評価）
- 今は優先度が低いこと:
  - DAI の DeFi プロトコル上での残存流動性（Aave・Uniswap 等では引き続き DAI が流通するため、直接的な影響は限定的）

## 未解決の論点

- EU / EEA 対象国ユーザーの DAI 残高はどのように処理されるか（引き出しのみ可能か、別の対応が提供されるか）
- USDS は MiCA 準拠の電子マネートークン（EMT）として承認される見通しはあるか
- 他の主要取引所（Binance・Kraken・OKX 等）も同様に DAI 上場廃止を進めるか

## 参考リンク

- 一次情報:
  - [CoinAlertNews — Coinbase DAI 上場廃止発表（2026-04-30）](https://coinalertnews.com/news/2026/04/30/coinbase-delist-dai-stablecoin)
  - [Coinbase Help — Token delistings and migrations](https://help.coinbase.com/en/coinbase/trading-and-funding/sending-or-receiving-cryptocurrency/token-migrations)
- 補足情報:
  - [Crypto.news — 上場廃止スケジュール詳細（2026-04-30）](https://crypto.news/coinbase-to-delist-dai-stablecoin-as-may-deadline-approaches/)
  - [Crypto Economy — DAI → USDS 移行の背景解説](https://crypto-economy.com/dai-transition-underway-as-coinbase-sets-schedule-for-usds-migration/)
  - [関連ノート：BankingCircle MiCA ステーブルコイン清算（2026-04-27）](2026-04-27_BankingCircle_mica-stablecoin-settlement.md)

## 重要度

- Medium

## 確からしさ

- High
