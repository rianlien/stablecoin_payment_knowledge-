---
title: "BIS年次経済報告 2026：ステーブルコインは「お金」ではなく「ETF」——FX リスク・ドル化リスクを警告"
date: 2026-06-28
source: "BIS Annual Economic Report 2026 / CoinDesk / The Block"
source_url: "https://www.bis.org/publ/work1270.pdf"
entity: "BIS（Bank for International Settlements）"
category: regulation / stablecoin-issuer
primary_category: regulation
article_published_date: 2026-06-28
underlying_event_date: 2026-06-28
primary_source_date: 2026-06-28
tags:
  - regulation
  - stablecoin
  - payments
  - psp
summary: "BIS は 2026 年次経済報告（2026-06-28 公表）で、現在のステーブルコインが「お金」としての 4 つの要件（単一性・弾力性・相互運用性・完全性）を満たさず、ETF に近い性質を持つと結論づけた。99% が USD ペッグの約 3,200 億ドル市場は、新興市場での「ドル化」と FX スワップ市場への影響リスクをはらんでいるとして、グローバルな規制協調の必要性を強調した。"
implications: "BIS の分析はステーブルコインの法的・規制的位置づけに影響する。GENIUS Act・MiCA といった各国規制は「準備金によるパー維持」を要件とするが、BIS は運用条件下での「パー維持の不確かさ」こそが本質的な問題と指摘。規制の強化方向は ETF 類似規制（信頼性の担保）になる可能性がある。"
importance: High
confidence: High
follow_up: "BIS Working Paper 1270「Stablecoins and safe asset prices」の詳細内容確認、GENIUS Act 7/18 最終規則でこの BIS 分析が準備金要件の厳格化に影響するか、ESMA・ECB の対応コメント"
---

## 概要

BIS（国際決済銀行）が 2026-06-28 に公表した年次経済報告（Annual Economic Report 2026）で、現在のステーブルコインは ETF（上場投資信託）に近い性質を持ち、「お金」として機能するための 4 要件を充足しないと結論づけた。同時に、USD ペッグ・ステーブルコインへの非ドル通貨からの流入が新興市場の「ステーブルコイン・ドル化」を加速させているとして、国際的な規制協調の必要性を訴えた。

## 何が起きたか

- **2026-06-28**：BIS が「BIS Annual Economic Report 2026」を公表。ステーブルコインのマクロ経済・金融安定的影響を包括的に分析
- BIS は 2026 年 5 月末時点のステーブルコイン市場規模を約 **3,200 億ドル**と集計（そのうち **99% が USD ペッグ**）
- 報告書は、現在のステーブルコイン設計が「ETF シェア」に近く、「お金」としての要件を満たさないと明言
- FX リスクとして、非ドル通貨から USD ペッグ・ステーブルコインへの流入が現物 FX 市場でのドル買い圧力を生み、FX スワップ市場のコストを上昇させる可能性を指摘
- 新興国における「ステーブルコイン・ドル化」——銀行外の経路で急速に進む外貨シフト——を歴史上の「預金ドル化」よりも高速な現象として警告

## 確認された事実

- BIS は「お金」の 4 要件として **単一性（singleness）・弾力性（elasticity）・相互運用性（interoperability）・完全性（integrity）** を定義
- 現在のステーブルコインはこれらを「設計上充足しない」と明言：特に**単一性**（発行体・チェーンを越えて常にパーで交換できない）が最重要の欠如要件
- 「償還の摩擦が一般的であり、現在のステーブルコイン設計は支払い手段よりも ETF シェアに類似している」と直接記述
- ステーブルコイン取引は「中央銀行バランスシート上で決済されない」ことが根本的な差異
- 規制の不在により、一部のステーブルコインは FX 規制・資本規制の回避手段として機能している実態を指摘

## なぜ重要か

### 決済事業者視点

- BIS が「ステーブルコインは決済手段として現時点では不完全」と公式に表明したことで、中央銀行・規制当局の監督強化に向けた理論的根拠が確立した
- PSP・アクワイアラーがステーブルコイン決済を標準提供する際に「法的リスク・準拠性」の評価基準として BIS 報告書が引用される可能性が高い
- MiCA・GENIUS Act の実施過程で規制当局が「ETF 類似規制」モデル（投資家保護型）を採用するシナリオが現実味を帯びた

### 加盟店視点

- ステーブルコイン決済の導入を検討する加盟店にとって、「準備金の堅牢性＝パー維持の信頼性」が最重要評価指標であることが改めて確認された
- BIS の指摘する「運用条件下でのデペッグ・リスク」は、加盟店のステーブルコイン受け取り後の保有リスク評価に直結する

### プロダクト視点

- x402 / AP4M など、ステーブルコインを API 決済レールとして使うプロトコル設計において、BIS の定義する「単一性欠如」（チェーンをまたいだパー保証の欠如）が技術的な問題として顕在化する可能性
- GENIUS Act PPSI 認可ステーブルコイン（Circle USDC 等）は準備金＋換金保証が規制化されることで、BIS が指摘する「パー維持の不確かさ」を緩和できる唯一の経路

### 規制 / リスク視点

- BIS の公式見解は G20 各国の規制当局に直接影響する。特に「ETF 規制モデル」採用（ = 証券規制下への位置づけ）の政治的コスト低下
- ステーブルコイン・ドル化警告は日本・EU・新興国の中央銀行が非 USD ステーブルコインの国際的普及に対して防衛的政策（資本規制・FX 規制）を強化するトリガーになりうる
- USD ペッグ 99% という集中リスクは、単一発行体障害時の系統的ショック経路を BIS が公式に認識したことを示す

## 我々への示唆

- いま検討すべきこと:
  - GENIUS Act 最終規則（7/18）で PPSI 要件がどの程度「パー維持の法的保証」を強化するかを確認し、BIS が指摘するギャップが制度的に埋まるかを評価する
  - 自社サービスが利用するステーブルコインの「准備金構造＋換金条件」を BIS の 4 要件（単一性・弾力性・相互運用性・完全性）でスコアリングするフレームワークを内部に持つ
- 後で深掘りすべきこと:
  - BIS Working Paper 1270「Stablecoins and safe asset prices」の内容——GENIUS Act 準拠 PPSI が BIS の基準を充足できるかの定量評価
  - 「ETF 規制モデル」採用のシナリオ分析——SEC ルール 2a-7 MMF（Invesco SROF 等）が GENIUS Act 準備金要件の標準インフラになるか
  - 新興市場ドル化リスクが日本（RLUSD×SBI）・EU（Circle EURC）ベースの非 USD ステーブルコイン普及戦略に与える影響
- 今は優先度が低いこと:
  - CBDC との競合分析（BIS は CBDC 推進を明示していないが、「単一性」の最終解は CBDC とも読める）

## ありそうな示唆

- BIS の「ETF 類似」批判は、GENIUS Act PPSI 認可を受けたステーブルコインを「ETF 扱い」から除外する論拠として、規制当局が利用する可能性がある（PPSI ＝ 規制により単一性が保証された「真の決済手段」という位置づけ）
- 「ステーブルコイン・ドル化」への BIS 警告は、日本・EU・東南アジアの中央銀行が非 USD ステーブルコインの国際利用に規制上の追い風を与えるリスクを示す

## 推測 / 監視ポイント

- BIS 報告書を受けて ESMA・ECB が MiCA の EMT（電子マネートークン）要件を「BIS 4 要件充足」に紐付けて強化する動きが出るか
- GENIUS Act 7/18 最終規則が BIS の「単一性欠如」批判に対するカウンターとして「法的パー保証」を強化する規定を入れるか
- BIS Working Paper 1270 の詳細（どのステーブルコインが「ETF」扱いになるか、PPSI 認可ステーブルコインは別枠か）

## 未解決の論点

- BIS の「お金でない」という評価は規制上の分類（証券 vs 決済手段 vs EMT）に法的拘束力を持つか
- PYUSD・RLUSD・USDC の 3 者が BIS の「パー維持リスク」評価において異なるスコアになるか（準備金構造の違い）
- 「ステーブルコイン・ドル化」は BIS が想定する $1〜$3T 規模で実際に発生するか（2026 年 5 月末で $3,200 億ドル、BIS の懸念閾値まで 3〜10 倍のスケール拡大が必要）

## 参考リンク

- 一次情報:
  - [BIS Annual Economic Report 2026（BIS 公式）](https://www.bis.org/publ/arpdf/ar2026e.htm)
  - [BIS Press Release（2026-06-28）](https://www.bis.org/press/p260623.htm)
- 補足情報:
  - [CoinDesk（2026-06-29）](https://www.coindesk.com/markets/2026/06/29/bis-warns-stablecoins-are-more-like-etfs-than-actual-money-and-they-re-creating-fx-risk)
  - [The Block（2026-06-29）](https://www.theblock.co/post/406466/bis-says-stablecoins-fall-short-as-money-warns-of-emerging-market-risks-in-annual-report)
  - [PYMNTS（2026-06-29）](https://www.pymnts.com/blockchain/2026/bis-warns-current-stablecoins-threaten-global-financial-stability/)
  - [Cryptopolitan（2026-06-29）](https://www.cryptopolitan.com/bis-report-stablecoins-fail-tests-money-etfs/)

## 重要度

- High

## 確からしさ

- High
