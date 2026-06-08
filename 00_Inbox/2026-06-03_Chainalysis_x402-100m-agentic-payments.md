---
title: "Chainalysis レポート: x402 エージェント決済が Base で累計1億件を突破"
date: 2026-06-03
source: Chainalysis / CryptoTimes / CryptoBriefing
source_url: https://www.chainalysis.com/blog/x402-agentic-payments-adoption/
entity: Chainalysis / Coinbase / Base
category: x402
primary_category: x402
article_published_date: 2026-06-03
underlying_event_date: 2026-06-03
primary_source_date: 2026-06-03
tags:
  - x402
  - agentic-commerce
  - machine-payments
  - Base
  - Coinbase
summary: "Chainalysis が2026年6月3日に公開したレポートで、x402 プロトコルによるエージェント決済が Coinbase の Base チェーン上で累計1億件を突破したと報告。2025年Q3のほぼゼロから急成長し、特に Q4 2025 に PING（pay-to-mint ミームコイン）によるトランザクション爆発が貢献。直近30日間: 7,241万件・$2,424万。$1以上の取引が全量の95%（2025年初頭の49%から上昇）。"
implications: "x402 が3四半期で1億件を達成したことは、プロトコルのテクニカルな実現可能性を示す。ただし成長の大部分がミームコイン投機（PING）に依存していた点は、持続性に疑問を残す。$1以上取引の比率上昇は、より実際の商取引に近いユースケースへのシフトを示唆する。"
importance: Medium
confidence: High
follow_up: "PING を除いた純粋な AI エージェント取引件数と金額の開示、旅行分野（Amadeus 等）追加による単価変化、6月月次データ"
---

## 概要
- Chainalysis が x402 プロトコルの詳細分析レポートを2026年6月3日に公開
- 累計取引件数が Base チェーンで1億件突破（2025 Q3 ほぼゼロから約3四半期で達成）

## 何が起きたか
- x402 累計件数: 1億件超（Base チェーン上）
- 成長タイムライン: 2025 Q3 ほぼゼロ → Q4 2025 急増 → 2026 初頭に1億件
- Q4 2025 の急増要因: PING（pay-to-mint ミームコイン）——pay-to-mint の仕組みが x402 を活用し、1週間で10,000%超の取引急増、PINGだけで初月 15 万件超
- 直近30日間: 7,241万件、$2,424万の出来高
- 取引単価の変化: $1以上 = 全量の95%（2025年初頭49%から上昇）；$0.10〜$1 = 4%（同46%から急落）
- USDC が x402 決済の 99.8% を占める
- x402 の仕組み: エージェントがリソースをリクエスト → サーバーが HTTP 402 + 支払い仕様を返す → エージェントが USDC オンチェーン決済 → レシートを添付して再リクエスト

## 確認された事実
- レポート発行: Chainalysis（2026-06-03）
- 累計件数: 1億件超（Base 上）
- 直近30日: 7,241万件・$2,424万
- $1以上取引比率: 95%（前年初頭49%）
- 主要決済通貨: USDC（99.8%）
- 成長の主要ドライバー: PING ミームコイン（Q4 2025）、その後も継続成長

## なぜ重要か

### 決済事業者視点
- x402 が3四半期で1億件を達成した事実は、プロトコルの技術的実現可能性を証明する
- ただし Chainalysis 自身も「成長の大部分は PING 投機」と分析しており、純粋な AI エージェント商取引の件数は不明

### 加盟店視点
- $1以上取引が 95% に増加したことは、マイクロペイメント・投機から実際の商取引への移行を示唆
- 旅行分野（Amadeus・Tripadvisor・FlightAware 追加: 5月29日発表）が今後の単価上昇を牽引する可能性

### プロダクト視点
- x402 のプロダクト採用を検討する際、現在の1億件のうちどれだけが「実際のエージェント商取引」かを分離する必要がある
- MCP 統合（Kustodia など）が増えることで、AI エージェントの x402 利用が本格化する見込み

### 規制 / リスク視点
- PING のようなミームコイン投機が取引件数を水増ししているため、規制当局が「エージェント決済の実態規模」を評価する際の参照として使うと過大評価になるリスクがある

## 我々への示唆
- いま検討すべきこと:
  - x402 の「エージェント商取引限定」の取引件数・金額を Chainalysis レポートから抽出し、PING 除外後の実態を把握する
- 後で深掘りすべきこと:
  - 旅行分野参加後（6月）の月次出来高——単価が大幅に上昇するか
  - Chainalysis が「商取引」と「投機」を分類する方法論の確認
- 今は優先度が低いこと:
  - 1億件という数字だけを拠り所にした意思決定（PING バイアスが大きい可能性）

## ありそうな示唆
- x402 が「AI エージェントの実際の商取引プロトコル」として成立するには、ミームコイン依存から実際のサービス決済（API 課金・旅行・データ購入）へのシフトが必要
- $1以上の取引比率が 95% まで上昇しているのは、実際の商取引利用が増えている兆候——今後6ヶ月のデータが分水嶺

## 推測 / 監視ポイント
- PING のような次の投機イベントがあれば再び急増するが、それは「エージェント決済の成長」とは別物
- 旅行 GDS（Amadeus）と x402 の実統合深度（直接 API か第三者ラッパーか）が単価上昇の鍵
- Chainalysis 月次データが定期的に公開されるかどうか

## 未解決の論点
- PING 除外後の純粋な AI エージェント商取引件数
- 7,241万件（直近30日）の内訳——旅行・API 課金・コンテンツ等のカテゴリ別
- Base 以外（Arbitrum・Ethereum・Solana）での x402 取引件数

## 参考リンク
- 一次情報: Chainalysis ブログ（2026-06-03）https://www.chainalysis.com/blog/x402-agentic-payments-adoption/
- 補足: CryptoTimes（2026-06-03）https://www.cryptotimes.io/2026/06/03/agentic-payments-hit-100m-transactions-on-base-reports-chainalysis/
- 補足: CryptoBriefing https://cryptobriefing.com/coinbase-x402-protocol-100m-transactions-base/
- 補足: Crowdfund Insider https://www.crowdfundinsider.com/2026/06/283501-chainalysis-shares-insights-on-agentic-payments-reaching-key-milestone-x402-protocol-shows-signs-of-traction-on-base/
- 関連先行ノート: [[2026-05-29_Base_x402-agentic-economy-is-here]]（5月29日時点の公式統計: 310万件）

## 重要度
- Medium

## 確からしさ
- High（Chainalysis による一次分析、ただし PING バイアスは推測を要する部分）
