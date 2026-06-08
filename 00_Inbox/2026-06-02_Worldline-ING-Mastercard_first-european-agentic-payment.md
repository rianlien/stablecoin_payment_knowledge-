---
title: "Worldline・ING・Mastercard、欧州初の本番環境エンドツーエンドエージェント決済を完了"
date: 2026-06-02
source: "Worldline プレスリリース / Mastercard Newsroom / Payment Expert / The Paypers"
source_url: "https://www.globenewswire.com/news-release/2026/06/02/3305397/0/en/WORLDLINE-Worldline-and-ING-complete-a-live-end-to-end-European-agentic-payment-in-production-Press-release.html"
entity: "Worldline / ING Bank / Mastercard"
category: "agentic-commerce"
primary_category: "payment-authorization"
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - agentic-commerce
  - payment-authorization
  - merchant-PSP-readiness
  - agent-identity
  - europe
summary: "Worldline（PSP）・ING（発行銀行）・Mastercard（カードネットワーク）が 2026 年 6 月 2 日、Money20/20 Europe（アムステルダム）にて欧州初の本番環境エンドツーエンドエージェント決済の完了を発表。ING カード保有者がオランダの加盟店でコンサートチケットを AI エージェント経由で購入した実取引。決済はMastercard ネットワーク上で処理され、Worldline がイシュイング・アクワイアリングの双方を処理した。決済にはエージェント起源を示す識別子が付与され、発行銀行がプロセス全体の可視性を維持した。"
implications: "欧州の主要カードインフラ（Worldline + ING + Mastercard）がエージェント決済の本番稼働を実証。米国外（欧州）でのカードレール上エージェント決済商業化が確認された最初の事例。認証（ING）・処理（Worldline）・ネットワーク（Mastercard）の三層分担が欧州エージェント決済の参照アーキテクチャになる可能性がある。"
importance: High
confidence: High
follow_up: "ユースケースの本番拡張予定（定期取引・委任購買スコープ拡大）、Mastercard Verifiable Intent / Agent Pay との統合状況、Worldline による他の欧州 PSP への技術展開、x402・AP2 との統合有無（現時点では未対応と見られる）"
---

## 概要

2026 年 6 月 2 日、Money20/20 Europe（アムステルダム）にて Worldline・ING・Mastercard が欧州初の本番環境エンドツーエンドエージェント決済の完了を発表した。実際の ING カード保有者がオランダの加盟店でコンサートチケットを購入したライブ取引であり、PoC やデモではなく本番インフラ上での完全な取引として実施された。

## 何が起きたか

- **取引の内容**：ING カード保有者が結婚記念日のプレゼントとしてオンラインでコンサートチケットを検索。加盟店側 AI エージェントが設定予算内でチケットを特定・提示し、消費者が明示的に承認した後に取引を完了した
- **インフラ構成**：Mastercard ネットワーク上で処理。Worldline がイシュイング・アクワイアリングのエンドツーエンドを担当。ING がイシュイング銀行として認証・承認を担当
- **技術的特徴**：取引にエージェント起源を示す識別子が付与され、発行銀行（ING）がプロセス全体を通じて完全な可視性を維持。消費者は最終購買決定の時点で明示的に承認を与える設計
- **発表場所**：Money20/20 Europe 2026（6 月 2〜4 日、アムステルダム）の基調発表として公表

## 確認された事実

- Worldline プレスリリースおよび Mastercard Newsroom による公式発表（いずれも 2026-06-02）
- 本番環境（production）でのライブ取引であることを双方が明示
- 取引インフラはベルギーを横断する既存インフラを基盤とし、Mastercard ネットワーク上で稼働
- 認証方式は「確立されたセキュリティメカニズム」（established secured mechanisms）と記載——具体的プロトコル名（AP2・Verifiable Intent 等）の明示はなし
- 将来のユースケースとして「定期取引」「委任購買（predefined parameters）」を列挙

## なぜ重要か

### 決済事業者視点
- 欧州最大級の PSP（Worldline）が Mastercard と組んでエージェント決済を本番稼働させた事実は、欧州の PSP がエージェント対応を「研究フェーズ」から「商業展開フェーズ」に移行させたことを示す
- Worldline の「イシュイング + アクワイアリング双方を担う」ポジションは、エージェント決済における PSP のワンストップ処理モデルの先例になりうる

### 加盟店視点
- 消費者の「明示的承認を最終ステップに残す」設計は、欧州の PSD2 / SCA（強力な顧客認証）要件への適合を意識したものと推測される。欧州加盟店がエージェント決済を導入する際のコンプライアンス参照として機能する

### プロダクト視点
- 「エージェント起源識別子」の付与は、エージェント発取引と人間発取引を区別するためのメタデータ設計の参照例になる。識別子の標準化（Mastercard Verifiable Intent / AP2 / Visa TAP との整合）が次の課題

### 規制 / リスク視点
- 欧州では EU AI Act（2026-08-02 高リスク AI 要件全面適用）が迫っており、「消費者が最終承認を行う」設計は EU AI Act の「人間の監視義務」に対応した設計と解釈できる
- 一方、ECB の Lagarde 総裁が 2026 年 5 月にユーロ以外のステーブルコイン利用への警戒を表明しており、欧州のエージェント決済は当面カードレール中心で進む可能性が高い

## 我々への示唆
- いま検討すべきこと:
  - Worldline の「エージェント起源識別子」の技術仕様——自社が PSP または加盟店として決済データを受け取る際に、エージェント発取引を識別できるかどうかを確認する
  - Mastercard Agent Pay / Verifiable Intent との技術的連携の有無——Worldline × ING がどのエージェント認証プロトコルを採用したかの詳細確認
- 後で深掘りすべきこと:
  - 本番環境拡張のタイムライン（定期取引・委任購買スコープの次のフェーズ）
  - 欧州他 PSP（Adyen・SIX Payments・Nexi 等）が Worldline に追随するかどうか
- 今は優先度が低いこと:
  - 取引の具体的な金額・チケット詳細（商業的機密として非公開の可能性）

## ありそうな示唆
- Mastercard ネットワーク経由のエージェント決済が欧州で本番稼働したことで、欧州の加盟店は「AI エージェントからの注文を Mastercard カードレール経由で受け入れる」ための追加インフラがほぼ不要になる
- Worldline が技術フレームワークを他の欧州 PSP に提供・ライセンスする可能性がある

## 推測 / 監視ポイント
- 今回の「消費者が明示的承認を与える」設計は、消費者委任型（consumer-delegated）エージェント決済の最初の本番事例。将来的に「エージェントが事前設定範囲内で自律決済」（fully autonomous within mandate）への拡張が発表されるか監視
- 欧州 ECB がこの事例をカードレール活用という観点でポジティブ評価するか、AI 規制観点で懸念を示すかを注視

## 未解決の論点
- 認証に使われた具体的プロトコルは AP2 / Verifiable Intent か、Mastercard 独自の仕組みか？
- OTL（Open Transaction Layer、2026-05-28 開始）との統合はあるか？
- EU AI Act の「高リスク AI」分類はこの取引の AI エージェントに適用されるか？

## 参考リンク
- 一次情報:
  - [Worldline プレスリリース（GlobeNewswire、2026-06-02）](https://www.globenewswire.com/news-release/2026/06/02/3305397/0/en/WORLDLINE-Worldline-and-ING-complete-a-live-end-to-end-European-agentic-payment-in-production-Press-release.html)
  - [Mastercard Newsroom（2026-06-02）](https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2026/worldline-ing-and-mastercard-complete-a-live-end-to-end-european-agentic-payment-in-production/)
- 補足情報:
  - [Payment Expert（2026-06-03）](https://paymentexpert.com/2026/06/03/agentic-payment-ing-worldline-masterc/)
  - [The Paypers（2026-06-02）](https://thepaypers.com/payments/news/worldline-ing-and-mastercard-execute-first-european-agentic-payment)
  - [LeapRate（2026-06-02）](https://www.leaprate.com/forex/technology/worldline-ing-mastercard-europe-first-live-agentic-payment-transaction)

## 重要度
- High

## 確からしさ
- High（Worldline プレスリリース・Mastercard Newsroom の双方による公式発表。複数メディアが同日報道）
