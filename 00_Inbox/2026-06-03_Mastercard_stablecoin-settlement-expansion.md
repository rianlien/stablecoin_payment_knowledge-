---
title: "Mastercard、6ステーブルコイン・8チェーンで常時決済精算を拡張——USDC・RLUSD・PYUSD 等を対象に"
date: 2026-06-03
source: Mastercard プレスリリース / The Block / CryptoBriefing
source_url: https://www.mastercard.com/global/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
entity: Mastercard
category: stablecoin-payments
primary_category: stablecoin-payments
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - stablecoin
  - Mastercard
  - USDC
  - settlement
  - PSP
summary: "Mastercard が2026年6月3日、カード精算（settlement）に USDC・RLUSD・PYUSD・USDG・USDP・SoFiUSD の6ステーブルコインを追加し、Arbitrum・Base・Canton・Ethereum・Polygon・Solana・Tempo・XRPL の8ブロックチェーンに対応。日中（intraday）・週末・祝日でも精算可能にする。対象はイシュアー・アクワイアラー・銀行・PSP の相互間精算（消費者向けクリプトカードではない）。"
implications: "カードネットワークの基幹バックオフィス（精算レール）にステーブルコインが組み込まれることで、PSP・銀行のステーブルコイン保有ニーズが構造的に生まれる。エージェント決済がカードレール経由で処理される場合、この精算基盤がその下層インフラとして機能する。"
importance: High
confidence: High
follow_up: "実際の精算量・参加 PSP 数（四半期報告）、日本・アジア太平洋展開タイムライン、Visa との精算インフラ比較"
---

## 概要
- Mastercard が2026年6月3日、カード決済の精算（settlement）に6ステーブルコインを追加し、8ブロックチェーンでの日中・週末・祝日精算を可能にすると発表

## 何が起きたか
- 対応ステーブルコイン: USDC（Circle）・RLUSD（Ripple）・PYUSD・USDG・USDP（Paxos）・SoFiUSD（SoFi）の6種
- 対応ブロックチェーン: Arbitrum・Base・Canton・Ethereum・Polygon・Solana・Tempo・XRPL の8チェーン
- 対象取引: イシュアー・アクワイアラー・銀行・PSP 間のカード精算（消費者向けクリプトカードではない）
- 新機能: 日中精算・週末精算・祝日精算（従来は銀行営業時間内のバッチ精算のみ）
- 初期展開地域: 米国・ラテンアメリカ（2026年中に拡大予定）
- 初期パートナー: ARQ（旧 DolarApp）・CBW Bank・Cross River・Lead Bank・Nuvei

## 確認された事実
- 発表日: 2026-06-03（Mastercard 公式プレスリリース）
- 精算対象: カードネットワーク内部の B2B 精算（issuers ↔ acquirers）
- 消費者 UI: 変更なし（消費者は引き続き従来のカードで決済）
- 規模: 現在は米国・ラテンアメリカで展開開始、グローバル展開は 2026 年中

## なぜ重要か

### 決済事業者視点
- Mastercard 加盟の PSP・銀行が USDC 等を精算残高として保有できるようになる——流動性管理の選択肢が増加
- 24/7 精算は週末・祝日の売掛金回収を加速し、加盟店の資金繰りを改善
- 従来の SWIFT・FedWire 依存の精算より速く・安く・24時間対応可能

### 加盟店視点
- 直接的な加盟店向け変更はないが、PSP が受け取るステーブルコイン精算を加盟店に転嫁するサービスが生まれる可能性
- ARQ（旧 DolarApp）のようなラテンアメリカ向け PSP が最初に活用する見込み

### プロダクト視点
- Mastercard Agent Pay（エージェント決済）を活用する際、この精算インフラがバックエンドで機能する可能性
- カードレール経由のエージェント決済（Visa TAP・Mastercard Agent Pay）と USDC 精算の組み合わせが実用的に

### 規制 / リスク視点
- GENIUS Act 準拠ステーブルコイン（USDC・SoFiUSD 等）を精算に使用するため、規制上のリスクは低い
- 各国の規制対応は現地 PSP が担う設計

## 我々への示唆
- いま検討すべきこと:
  - 自社が Mastercard 加盟 PSP であれば、USDC 精算オプトインのタイムラインと条件を確認
  - Cross River・Lead Bank のような新興デジタル銀行が精算パートナーとして参加している——彼らとの提携がステーブルコイン決済インフラ整備の近道になる可能性
- 後で深掘りすべきこと:
  - Visa との精算インフラ比較（Visa は9チェーン対応を 4 月に発表済み）——どちらが PSP に有利か
  - Mastercard Agent Pay × USDC 精算の組み合わせでエージェント支払いがどのように処理されるか
- 今は優先度が低いこと:
  - 消費者向けプロダクトへの直接影響（精算レイヤーのみの変更のため）

## ありそうな示唆
- 同日（6/3）に報道された Stripe/Visa/Mastercard のステーブルコイン連合計画と合わせると、Mastercard の「自社ネットワーク精算へのステーブルコイン組み込み」は連合発行のステーブルコインを将来的に自社精算システムに統合する布石である可能性がある
- SoFiUSD が精算対象に含まれていることは、GENIUS Act 下で初めて認可された国法銀行発行ステーブルコインが主要カードネットワークに統合されたことを意味する

## 推測 / 監視ポイント
- Visa のステーブルコイン精算との競合——Visa は 4 月に9チェーンに拡張済み、Mastercard は今回 8 チェーンで追随
- アジア展開のタイムライン（Canton・XRPL を対応したのは香港・日本市場を視野に入れた可能性）
- 精算量が公開されるかどうか（Visa は過去に $7B の精算量を公開）

## 未解決の論点
- Mastercard Agent Pay とこの精算基盤の統合タイムライン
- 日本など規制の厳しい市場でのステーブルコイン精算の可否
- 各ステーブルコインの精算における優先順位（PSP がどれを選ぶか）

## 参考リンク
- 一次情報: Mastercard プレスリリース（2026-06-03）https://www.mastercard.com/global/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
- 補足: The Block https://www.theblock.co/post/403474/mastercard-expands-stablecoin-settlement-options-with-usdc-pyusd-and-rlusd
- 補足: CryptoBriefing https://cryptobriefing.com
- 補足: Benzinga https://www.benzinga.com/crypto/cryptocurrency/26/06/52968632/mastercard-expands-stablecoin-settlement-support-to-include-ripples-rlusd-circles-usdc

## 重要度
- High

## 確からしさ
- High
