---
title: "Western Union、Solana ベース USDPT ステーブルコインを 5 月ローンチへ——Q1 決算で CEO が確認"
date: 2026-04-24
source: "Western Union Q1 2026 Earnings Call / CoinDesk"
source_url: https://www.coindesk.com/business/2026/04/27/western-union-eyeing-stablecoin-launch-to-settle-global-transactions-without-swift-ceo-says
entity: WesternUnion
category: payments
tags:
  - stablecoin
  - payments
  - wallet
  - psp
summary: "Western Union の CEO Devin McGranahan が 2026 年 4 月 24 日の Q1 決算コールで、Solana 上の自社ステーブルコイン USDPT を 5 月にローンチすると明言。発行体は米連邦認可の暗号資産カストディアン Anchorage Digital Bank。初期用途はエージェント間決済の SWIFT 代替。同時に Digital Asset Network（暗号ウォレット↔36 万拠点の現金ネットワーク接続）と消費者向け Stable Card（Visa・Rain 共同開発）も発表。"
implications: "世界最大級の送金ネットワーク（200 カ国超・36 万拠点）がステーブルコインをバックエンド決済に組み込む。オフランプ戦略が PSP・ウォレット事業者にとって参照モデルになりうる。"
follow_up: "5 月のパイロット対象国・エージェント実績・Stable Card の展開国と時期"
---

## 概要

Western Union の CEO Devin McGranahan が 2026 年 4 月 24 日の第 1 四半期決算コールで、同社の USD 担保ステーブルコイン **USDPT**（U.S. Dollar Payment Token）が最終準備段階を終え、**5 月にパイロットローンチ**すると発表した。USDPT は Solana 上で動作し、発行は米連邦特許銀行（federally chartered crypto custodian）である **Anchorage Digital Bank** が担う。

## 何が起きたか

- McGranahan CEO は Q1 決算コール（4 月 24 日）でスラブコインを中核的な戦略プロダクトと位置づけ、「デジタル資産に参入するかどうかの問題ではなく、どれだけ速くスケールできるかだ」と発言
- **USDPT の初期用途**：消費者向けではなく、グローバルな**エージェントネットワークとの B2B 決済決済バックエンド**。週末・祝日を含む 24/7 でエージェントへ送金決済が可能になり、SWIFT や通常の対応銀行経路を省略できる
- **Digital Asset Network（DAN）**：暗号資産ウォレットと Western Union の 200 カ国超・36 万か所の現金払い出し拠点を接続。消費者が暗号資産ウォレットから最後の 1 マイルで現金を引き出せるオフランプインフラ
- **Stable Card**：Visa および暗号資産ウォレットプロバイダー Rain との共同開発。消費者が USDPT を保有しながら、POS 端末や ATM での現地通貨自動変換でグローバルに使える USD 建てプリペイドカード。2026 年後半に「数十カ国」で展開予定
- Q1 決算サマリー：GAAP 売上高 9.83 億ドル（前年比 約 ▲1%）、GAAP EPS 0.20 ドル、調整後 EPS 0.25 ドル（市場予想 0.39 ドルを下回る）。伝統的な送金ビジネスの減収を補う成長戦略の柱としてデジタル資産を位置づけ

## なぜ重要か

### 決済事業者視点
- 世界最大級の既存インフラ（200 カ国超・36 万拠点）がステーブルコイン決済を**バックエンド決済レールとして採用**した最初の大型事例。PSP 業界全体へのシグナル効果は大きい
- エージェント向け USDPT 決済は「暗号資産ユースケース」ではなく「送金コスト削減」「決済スピード改善」の文脈で語られており、ステーブルコインの B2B 決済への本格統合が始まった

### 加盟店視点
- DAN（Digital Asset Network）はクリプトウォレット保有者が WU の現金ネットワーク経由で換金できるインフラ。ステーブルコイン受け取りを希望する加盟店のオフランプ選択肢が広がる

### プロダクト視点
- Stable Card のモデル（ステーブルコイン保有→POS で自動変換）は、日本を含む新興国向け「デジタルドル口座＋カード」のプロダクト設計において参照点になりうる
- Rain との協業モデル（専門ウォレット事業者との共同開発）は、自社でカードスタックを構築しないアセンブリー戦略の一例

### 規制 / リスク視点
- 発行体が**Anchorage Digital Bank**（連邦認可銀行）であることで、GENIUS Act の PPSI（Permitted Payment Stablecoin Issuer）規制への適合が容易になる可能性
- 米国外でのステーブルコイン流通・現金化のオペレーションは、各国 AML・外為規制の適用範囲を新たに生む

## 我々への示唆
- いま検討すべきこと:
  - WU の DAN が提供するオフランプ API の仕様確認（自社プロダクトのオフランプ選択肢として評価）
  - USDPT × Solana の決済フロー設計と、x402 や Circle CPN などの既存スタックとの比較
- 後で深掘りすべきこと:
  - 5 月パイロット後のエージェント決済の実績データ（コスト・スピード・稼働率）
  - Stable Card の展開国リストと、現地規制対応の実態
- 今は優先度が低いこと:
  - WU コンシューマー向けウォレットの直接競合としての評価（USDPT の初期用途は B2B）

## 未解決の論点
- パイロット対象国は非公表。スケールアウト計画・展開基準は未明
- Stable Card の展開における Rain と Visa の役割分担、USDPT 保有残高の管理主体は不明
- 現地通貨変換レートのスプレッドや手数料モデルが競争力を持てるかは未知数
- GENIUS Act 最終化前に米国内向け消費者提供を行う場合の規制リスク

## 参考リンク
- 一次情報:
  - [Q1 2026 決算コール要約（GuruFocus）](https://www.gurufocus.com/news/8817806/the-western-union-co-wu-q1-2026-earnings-call-highlights-navigating-challenges-and-seizing-digital-opportunities)
  - [Western Union IR プレスリリース（USDPT 初回発表 2025）](https://ir.westernunion.com/news/archived-press-releases/press-release-details/2025/Western-Union-Announces-USDPT-Stablecoin-on-Solana-and-Digital-Asset-Network/default.aspx)
- 補足情報:
  - [CoinDesk 報道（2026-04-27）](https://www.coindesk.com/business/2026/04/27/western-union-eyeing-stablecoin-launch-to-settle-global-transactions-without-swift-ceo-says)
  - [Unchained Crypto（Stable Card 詳細）](https://unchainedcrypto.com/western-union-to-launch-usdpt-stablecoin-on-solana-next-month-stable-card-planned-for-consumers-in-dozens-of-markets/)

## 重要度
- High

## 確からしさ
- High
