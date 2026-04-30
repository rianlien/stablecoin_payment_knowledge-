---
title: "Visa、ステーブルコイン清算ネットワークを 9 チェーンに拡張・年率換算 70 億ドル突破"
date: 2026-04-29
source: "Visa / CoinDesk / The Block / PYMNTS"
source_url: https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx
entity: Visa
category: payments
tags:
  - stablecoin
  - payments
  - protocol
  - psp
summary: "Visa が 2026 年 4 月 29 日、ステーブルコイン決済清算パイロットに Arc・Base・Canton・Polygon・Tempo の 5 チェーンを追加し、対応ネットワーク数を 9 に拡大した。年率換算の清算取引量は 70 億ドル（前四半期比 50% 増）に達し、50 か国以上で 130 以上のステーブルコイン連動カードプログラムを展開中。"
implications: "Visa が Stripe の Tempo、Coinbase の Base、Circle の Arc という 3 大決済・ステーブルコインインフラを一気に清算対象に取り込んだことで、ステーブルコイン決済ネットワークの相互接続性が大幅に向上。PSP がステーブルコインとカードネットワーク清算を統合的に扱える環境が整いつつある。"
follow_up: "各チェーン別の清算量内訳、Tempo（Stripe）・Base（Coinbase）の具体的な清算事例、日本での Visa ステーブルコイン連動カード展開可能性"
---

## 概要

Visa が 2026 年 4 月 29 日、ステーブルコイン清算パイロットプログラムに **5 つのブロックチェーンを追加**し、対応チェーン数を合計 **9** に拡大した。あわせて年率換算の清算取引量が **70 億ドル**（前四半期比 **50% 増**、前四半期比較の前期値は約 47 億ドル）に達したと発表。既存カードインフラとブロックチェーン決済レールの統合が加速している。

## 何が起きたか

### 新たに追加された 5 チェーン

| チェーン | 開発元 | 特徴 |
|----------|--------|------|
| **Arc** | Circle | Circle が構築したステーブルコイン・オンチェーン決済に特化した Layer-1 |
| **Base** | Coinbase | Ethereum L2。高速・低コスト。Coinbase エコシステムの中核 |
| **Canton** | Digital Asset / Goldman Sachs ほか | 機関投資家向け設定可能プライバシーチェーン |
| **Polygon** | Polygon Labs | 主要 EVM 互換 L2。グローバルに広範なエコシステム |
| **Tempo** | Stripe / Paradigm | Stripe が Paradigm と共同で構築したステーブルコイン決済に特化した L1 |

### 既存の 4 チェーン
Avalanche、Ethereum、Solana、Stellar

### 主要メトリクス
- **清算取引量**: 年率換算 70 億ドル（前四半期比 50% 増）
- **ステーブルコイン連動カードプログラム**: 50 か国以上で 130 以上
- パイロット開始から累積清算取引量は着実に拡大中

## なぜ重要か

### 決済事業者視点
- Stripe の Tempo と Coinbase の Base が Visa 清算ネットワークに加わったことで、「ステーブルコインで入金・Visa カードで出金」というフローが実際の清算インフラとして機能し始めた
- PSP は Visa の清算レールとステーブルコインレールを統合して扱えるようになり、加盟店向けのセトルメント選択肢が拡大する
- 50 か国超・130 カードプログラムという実績は、ステーブルコイン清算が「実験」段階を脱していることを示す

### 加盟店視点
- Visa ネットワークに接続された加盟店が、間接的にステーブルコインでの清算を受け取れるようになる経路が広がる
- DoorDash + Tempo（既報）や Meta + Stripe（本日報告）と組み合わせると、大手プラットフォームから加盟店への支払いがステーブルコインレールを経由してカード清算に統合されるシナリオが現実的になる

### プロダクト視点
- Circle Arc の Visa 採用は、Circle が USDC の流通インフラとして独自 L1 を Visa 清算に直接接続する戦略の一環。USDC の決済インフラとしての地位強化
- Base（Coinbase）の追加は、Coinbase の stablecoin 事業（USDC 共同管理・Base での USDC 発行）をカードネットワークに直結させる
- Canton（機関投資家向けプライバシー）の採用は、B2B・機関向けトレード清算領域での Visa の存在感拡大を示唆

### 規制 / リスク視点
- 9 チェーン対応は、単一チェーン障害や規制変更によるリスクを分散するマルチチェーン戦略。ステーブルコイン清算インフラのレジリエンスが向上
- Canton の機関向けプライバシー機能は、MiCA・GENIUS Act 等の規制に対応した機関決済で活用される可能性

## 我々への示唆
- いま検討すべきこと:
  - Tempo（Stripe）・Base（Coinbase）を経由した Visa 清算の API 仕様を確認し、自社決済フローとの統合可能性を評価
  - ステーブルコイン連動 Visa カードプログラムが自社の消費者向けプロダクトに適用できる国・ユースケースを洗い出す
- 後で深掘りすべきこと:
  - 各チェーン別の清算量・手数料構造（Visa はまだ詳細を非公開）
  - Canton（機関向けプライバシー）のユースケースが日本の機関決済・トレード清算に応用できるか
- 今は優先度が低いこと:
  - Arc（Circle L1）の技術詳細（まだ開発初期段階）

## 未解決の論点
- 各チェーン別の清算量内訳・手数料は未公開
- 70 億ドルのうちどの割合が B2B vs. 消費者向けかは不明
- Visa の日本展開タイムラインにステーブルコイン清算が含まれるかは未確認

## 参考リンク
- 一次情報:
  - [Visa 公式プレスリリース（2026-04-29）](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx)
  - [Visa ニュースルーム](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22336.html)
- 補足情報:
  - [CoinDesk 報道（2026-04-29）](https://www.coindesk.com/business/2026/04/29/visa-expands-stablecoin-settlement-network-as-volume-hits-usd7-billion-run-rate)
  - [The Block（2026-04-29）](https://www.theblock.co/post/399405/visa-stablecoin-settlement-hits-7-billion-run-rate-pilot-expands-nine-blockchains)
  - [Decrypt（チェーン詳細）](https://decrypt.co/365968/visa-base-polygon-canton-arc-tempo-stablecoin-settlement-program)
  - [PYMNTS.com](https://www.pymnts.com/visa/2026/visa-adds-5-blockchains-as-stablecoin-settlement-volume-surges/)

## 重要度
- High

## 確からしさ
- High
