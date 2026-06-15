---
title: "Fireblocks、Flow を公開し PSP・フィンテック向け stablecoin acceptance をプロダクト化"
date: 2026-06-02
source: PR Newswire / Fireblocks
source_url: https://www.prnewswire.com/news-releases/fireblocks-launches-flow-stablecoin-acceptance-for-psps-and-fintechs-302788865.html
entity: Fireblocks
category: merchant-PSP-readiness / stablecoin-infrastructure / machine-payments
primary_category: merchant-PSP-readiness
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - Fireblocks
  - PSP
  - stablecoin-infrastructure
  - merchant-readiness
  - machine-payments
summary: "Fireblocks が 6 月 2 日、Flow を公開。PSP・フィンテックが加盟店に stablecoin acceptance を提供するための統合プロダクトで、ウォレット、KYB/KYC、オフランプ、法定通貨建て精算、コンプライアンスをまとめて扱う。発表時点で OTL（Open Transaction Layer）を活用し、より複雑な multi-step payment flow を構成できることも打ち出した"
implications: "Fireblocks は 5 月 20 日の Agentic Payments Suite 発表を受けて、6 月 2 日に merchant acceptance 側の実装をさらに具体化した。OTL を組み合わせることで『受け取る』だけでなく、承認・換金・会計連携まで含む機械決済フロー基盤に進もうとしている"
importance: Medium
confidence: High
follow_up: "Flow の pricing、対応地域、PSP 導入事例、OTL 依存部分の仕様、x402 / MPP との接続、法定通貨精算時のリスク分担を確認する"
---

## 概要
- Fireblocks が 2026 年 6 月 2 日、Flow を正式公開した
- 対象は PSP・フィンテックで、加盟店向け stablecoin acceptance をプロダクトとして短期間に立ち上げることを狙っている

## 何が起きたか
- Flow は、加盟店受け入れに必要な口座生成、審査、コンプライアンス、換金、精算などを一体化して提供する
- Fireblocks は OTL を使って multi-step transaction flow を調整できる点も合わせて訴求している
- そのため、単なる「USDC を受け取る SDK」ではなく、PSP が自社の商品として stablecoin acceptance を組み込む基盤に近い

## 確認された事実
- PR Newswire 上の公式発表日は 2026-06-02
- Fireblocks 公式ブログでも Flow の公開が確認できる
- 公式発表では、PSP やフィンテックが自社顧客へ stablecoin acceptance を提供するための運用機能一式を含むと説明されている
- OTL との連携により、より複雑な payment flows を扱えることが明記されている

## なぜ重要か

### 決済事業者視点
- stablecoin acceptance は単体 API ではなく、換金、照合、審査、サポート運用まで含めて初めて商用化できる。Flow はその運用面を PSP 向け商品としてまとめにきた
- 既存 PSP が agentic commerce 時代の受け入れレールを準備する際、最短で導入できる有力候補になる

### 加盟店視点
- 加盟店は直接ブロックチェーン運用を持たずに、PSP 経由で stablecoin acceptance を導入できる可能性が高まる
- 将来的に agent-led checkout で stablecoin が使われる場合も、加盟店は Fireblocks ではなく PSP 契約変更で対応できる構造になりうる

### プロダクト視点
- 5 月 20 日の Agentic Payments Suite が「エージェントが支払う側・PSP が受ける側」の概念提示だったのに対し、Flow は merchant acceptance をより単体商品として明確化している
- OTL 統合を明示したことで、単発決済よりも複雑な機械決済ワークフローを扱う意図が見える

### 規制 / リスク視点
- 法定通貨精算やコンプライアンスをまとめて扱う設計は、加盟店に暗号資産保有リスクを直接負わせない方向
- ただし、PSP と Fireblocks の責任分界、規制地域ごとの実装差、オフランプ先のリスクは要確認

## 我々への示唆
- いま検討すべきこと:
  - PSP が加盟店向けに stablecoin acceptance を提供する場合に必要なオペレーション要件を、Flow の構成要素ベースで棚卸しする
  - Flow と Fireblocks Agentic Payments Suite の役割分担を整理し、受け取り側の実装選択肢として比較する
- 後で深掘りすべきこと:
  - OTL を使った multi-step payment flow の参照実装
  - 自社が想定する merchant onboarding / settlement / reconciliation と整合するか
- 今は優先度が低いこと:
  - Flow 単体のブランド訴求

## ありそうな示唆
- Stablecoin acceptance は、将来的な agentic commerce 対応の前提機能として PSP 商品化が進む可能性が高い。Flow はその商用化テンプレート候補になりうる

## 推測 / 監視ポイント
- Flow が実際にどの PSP に採用されるか
- OTL 統合が単なる将来構想か、すでに本番で使われているか
- x402 / AP2 / card-based agentic payment とどう棲み分けるか

## 未解決の論点
- 対応ステーブルコインと対応地域の詳細
- 法定通貨精算時のタイムラインと失敗時処理
- 加盟店が返金・取消をどう扱うのか

## 参考リンク
- 一次情報:
  - [PR Newswire（2026-06-02）](https://www.prnewswire.com/news-releases/fireblocks-launches-flow-stablecoin-acceptance-for-psps-and-fintechs-302788865.html)
  - [Fireblocks Blog（2026-06-02）](https://www.fireblocks.com/blog/launching-flow-stablecoin-acceptance-for-psps-fintechs/)
- 補足情報:
  - なし

## 重要度
- Medium

## 確からしさ
- High
