---
title: "x402 プロトコルが Injective に対応——AI エージェントが DeFi 特化チェーン上でリアルタイム USDC 決済"
date: 2026-06-09
source: "Injective 公式ブログ / KuCoin News / CoinCu"
source_url: "https://injective.com/blog/x402"
entity: "Coinbase / Injective Protocol"
category: x402 / machine-payments / agentic-commerce
primary_category: machine-payments
article_published_date: 2026-06-09
underlying_event_date: 2026-06-09
primary_source_date: 2026-06-09
tags:
  - x402
  - machine-payments
  - Injective
  - USDC
  - AI-agent
summary: "Coinbase の x402 決済プロトコルが Injective（DeFi 特化型 L1）本番チェーン上でライブになった。AI エージェントが USDC で API・オンチェーンサービスの料金を約 650ms でリアルタイム決済できる設計。x402 はこれで Base・Solana・Arbitrum・XRPL・Casper・Injective の 6+ チェーンに展開。Injective の DeFi 特化アーキテクチャはエージェント向け自律トレーディング・流動性提供ユースケースへの応用が見込まれる。"
implications: "x402 のマルチチェーン展開が加速し、DeFi 特化チェーン上での AI エージェント決済インフラが整った。Injective は高頻度・低遅延取引と DeFi 特化設計を持つため、AI エージェントによる自律的なオンチェーン金融活動（スワップ・流動性提供・予測市場等）の決済レールとして機能する。"
importance: Medium
confidence: High（Injective 公式ブログ・KuCoin News で確認）
follow_up: "Injective 上の x402 取引件数・ステーブルコイン種別、Injective DeFi エコシステムでの AI エージェントユースケース拡大、x402 対応チェーン間のクロスチェーン決済設計"
---

## 概要

- Coinbase の x402 決済プロトコルが Injective（DeFi 特化型 Layer 1 ブロックチェーン）本番チェーン上でライブになった（2026-06-09）
- AI エージェントが USDC を使って API・オンチェーンサービスの料金を人間の介在なしにリアルタイム決済できる
- 決済確定時間：約 650ms
- x402 はこれまで Base・Solana・Arbitrum・Casper 等でライブ、2026-06-10 の Ripple XRPL AI Starter Kit によって XRPL にも対応——今回の Injective で 6+ チェーンに拡大

## 何が起きたか

- Coinbase の x402 フレームワークが Injective チェーン上で本番稼働
- AI エージェントが HTTP 402 Payment Required レスポンスを受け取ると、Injective 上で USDC 取引を実行し、サービスへのアクセスを自動的に取得する
- Injective が選定された理由：DeFi インフラへの特化・高頻度・低遅延取引のサポート（エージェントワークフローの決済需要と整合）

## 確認された事実

- ライブ日：2026-06-09
- 対応チェーン：Injective（本番環境）
- 決済通貨：USDC
- 決済確定：約 650ms
- 設計：HTTP 402 → エージェントが Injective 上で USDC 決済 → サービスアクセス取得
- 発表元：Injective 公式ブログ・KuCoin News・CoinCu

## なぜ重要か

### 決済事業者視点

- x402 がまた別の主要チェーンに展開したことで、x402 インテグレーターは Injective エコシステムのユーザー・サービスにもリーチできる
- Injective はオンチェーン DEX・パーペチュアル先物・予測市場等の DeFi プリミティブが充実しており、AI エージェントによる自律金融活動の決済レールになりえる

### 加盟店視点

- Injective エコシステム上の API 提供者（DeFi プロトコル・データフィード・オンチェーンインフラ）が x402 を使って AI エージェントへのサービス課金ができるようになる
- DeFi ユースケース（トレーディング・流動性提供）は旅行（Travala）・コンテンツ（Cryptorefills）とは異なる高頻度・小額取引パターンを持つ

### プロダクト視点

- x402 Foundation はいまや Base・Solana・Arbitrum・XRPL・Casper・Injective という多様なアーキテクチャのチェーンに対応。「オープン標準」としての性格が具体化しており、特定チェーンへの依存リスクが低下している
- Injective 対応は Mastercard AP4M（6/10 ローンチ）との関係でも注目——AP4M は Polygon・Solana・Base の 3 チェーン対応であり、Injective は AP4M 対象外。x402 は AP4M より広いチェーンカバレッジを持つことになる

### 規制 / リスク視点

- x402 の Injective 展開は Chain-agnostic なオープン標準としての設計を体現。GENIUS Act 準拠 PPSI ステーブルコイン（USDC）での決済を前提とするため、規制上のリスクは Base/Solana 上の x402 と同等
- Injective は DeFi 特化設計のため、CLARITY Act が通過した場合のデセントラライズド交換・デリバティブ取引への規制との関係を確認する必要がある

## 我々への示唆

- いま検討すべきこと:
  - x402 プロダクトの Injective チェーン対応計画——特に DeFi ユースケース（自律トレーディング・流動性提供に対するエージェント支払い）が自社の対象領域かを確認
  - AP4M（Polygon/Solana/Base）vs x402（6+ チェーン）の対応チェーン差分を把握し、「AP4M 未対応チェーン上のエージェント決済」では x402 が唯一の標準プロトコルになっている点を設計上の優位性として評価する
- 後で深掘りすべきこと:
  - Injective の AI エージェントユースケース成熟度（Injective の DeFi プロトコルが x402 を実際に採用するまでの時間軸）
  - x402 の 6+ チェーン間での流動性・相互運用性の整備状況
- 今は優先度が低いこと:
  - Injective のトークン（INJ）価格動向——決済インフラとしての評価とは分離して考える

## ありそうな示唆

- Injective 上での x402 採用が DeFi エコシステムに広がると、AI エージェントが自律的にオンチェーン金融活動（スワップ・LP・先物）を実行しながら、インフラコストを x402 で自動決済するという「エージェントによる DeFi 自律運用」が現実化する最初の足がかりになりうる

## 推測 / 監視ポイント

- Injective 上の x402 取引件数の伸び——Base・Solana と比較した初期採用率
- Injective エコシステムの API プロバイダー（データフィード・オンチェーンデータ）が x402 を採用するタイムライン
- AP4M と x402 の Injective 上での共存または競合（AP4M が Injective に対応した場合）

## 未解決の論点

- Injective 上の x402 は USDC のみか、INJ・その他トークンでの支払いも可能か
- x402 の Injective 上でのガス費用設計（USDC 払い時のガス代の処理方法）
- Injective の DeFi 取引（DEX 等）に x402 を適用する場合の規制上の扱い（CLARITY Act 管轄の可能性）

## 参考リンク

- 一次情報: [Injective 公式ブログ（2026-06-09）](https://injective.com/blog/x402)
- 補足情報: [KuCoin News（2026-06-09）](https://www.kucoin.com/news/flash/coinbase-s-x402-protocol-launches-on-injective-enabling-ai-agents-to-pay-fees)
- 補足情報: [CoinCu（2026-06-09）](https://coincu.com/coinbase-x402-protocol-launches-on-injective-ai-agents-pay-fees/)

## 重要度

- Medium

## 確からしさ

- High
