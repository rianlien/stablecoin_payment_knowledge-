---
title: "Worldline・ING・Mastercard、欧州初のライブ本番エージェント決済を完了"
date: 2026-06-04
source: "Worldline / Mastercard Newsroom / GlobeNewswire"
source_url: "https://worldline.com/en/home/top-navigation/media-relations/press-release/pr-2026_06_02_01"
entity: "Worldline, ING, Mastercard"
category: "agentic-commerce"
primary_category: "agentic-payments"
article_published_date: 2026-06-02
underlying_event_date: 2026-06-02
primary_source_date: 2026-06-02
tags:
  - agentic-commerce
  - payment-authorization
  - merchant-PSP-readiness
  - mastercard-agent-pay
  - europe
summary: >
  Worldline・ING・Mastercard が Money 20/20 Europe（アムステルダム）で、欧州初の本番エンドツーエンド・エージェント決済の完了を発表。ING カードホルダーとオランダ加盟店の間で Mastercard ネットワーク上で実施。Mastercard Agent Pay フレームワークを利用し、消費者が最終承認を行う設計。ベルギーと同一インフラで稼働。
implications: >
  欧州のエージェント決済インフラが「概念実証」から「本番稼働」に移行した最初の確認事例。Worldline（PSP）＋ ING（イシュアー）＋ Mastercard（ネットワーク）の三層が実際の消費者と加盟店を結んで稼働したことは、欧州でのエージェント決済商用化が射程に入ったことを示す。
importance: High
confidence: High
follow_up: "Worldline の他の欧州 PSP パートナーへの展開状況、ING 以外の欧州イシュアーの参加スケジュール、消費者承認なし（完全委任型）の取引へのロードマップ"
---

## 概要

2026 年 6 月 2 日、Money 20/20 Europe（アムステルダム）にて Worldline・ING・Mastercard が欧州初の本番エンドツーエンド・エージェント決済の完了を発表した。ING カードホルダーとオランダの加盟店との間で、Mastercard ネットワークを経由して実施された。

## 何が起きたか

- **場所・日時**：Money 20/20 Europe（アムステルダム）、2026 年 6 月 2 日
- **参加エンティティ**：Worldline（アクワイアラー / PSP）、ING（カードイシュアー）、Mastercard（ネットワーク）
- **ユースケース**：ING カードホルダーが結婚記念日のプレゼントをオンラインで検索 → 加盟店の AI エージェントが予算内でコンサートチケットをキュレーション → 消費者が明示的に承認 → 決済完了
- **地理的範囲**：オランダ加盟店とベルギーで同一インフラ上で稼働、Mastercard ネットワーク全体に対応
- **フレームワーク**：Mastercard Agent Pay（Agentic Token + Verifiable Intent）を使用

## 確認された事実

- 欧州で初めて本番環境（production）でのエンドツーエンド・エージェント決済が実行された
- Worldline（PSP）・ING（イシュアー）・Mastercard（ネットワーク）の三者が実際の取引で協調動作した
- 消費者が最終購買決定を明示的に承認する設計（consumer-driven approval）を採用
- ベルギーと同じ技術インフラを使用し、複数市場跨ぎの動作が確認された
- Mastercard によれば、欧州の全 Mastercard イシュアーがネットワークレベルで Agent Pay に対応済み

## なぜ重要か

### 決済事業者視点

- Worldline が欧州 PSP として最初の本番エージェント決済アクワイアラーとなった事例は、他の欧州 PSP（Adyen, Nexi 等）が Agent Pay 対応を加速させる圧力になる
- PSP 側の技術要件（動的認可ロジック・エージェントトークン発行・消費者承認フロー）が実装済みであることが示された

### 加盟店視点

- 加盟店が「AI エージェントからの購買」を受け入れるために必要な商用インフラが欧州でも整ってきた
- 現段階は「消費者が明示承認する」モデルであり、完全自律型（消費者が不在で完結）とは異なる

### プロダクト視点

- Mastercard Agent Pay の Verifiable Intent が欧州の多市場をまたいで実稼働したことは、技術仕様の成熟を示す
- 今後のロードマップとして「定期取引」「事前委任型購買（predefined parameters）」への拡張が言及された

### 規制 / リスク視点

- 消費者承認モデルは GDPR / PSD2 / PSD3 の消費者保護要件と整合しやすい設計
- 欧州での本番稼働は MiCA 後の規制環境下でのエージェント決済の可能性を示す

## 我々への示唆

- いま検討すべきこと:
  - Worldline 統合パートナーとして自社製品が欧州の Agent Pay エコシステムに接続できるかを確認する
  - Mastercard Agent Pay の欧州向け技術仕様（消費者承認フローの実装要件）を入手する
- 後で深掘りすべきこと:
  - Worldline 以外の欧州 PSP（Adyen / Nexi / Payone）の Agent Pay 対応状況
  - ING 以外の欧州イシュアーの実稼働タイムライン
  - 「事前委任型（predefined parameters）」への拡張スケジュールと仕様
- 今は優先度が低いこと:
  - 消費者承認なし・完全自律型のエージェント決済は規制上まだ不確実なため、今すぐ設計に組み込む必要はない

## ありそうな示唆

- Worldline の先行事例を受けて Adyen・Nexi・Payone が 2026 年 Q3 以内に Agent Pay 統合を発表する可能性が高い
- Money 20/20 Europe での発表であることから、欧州主要 PSP への普及は 2026 年後半に加速すると予想される

## 推測 / 監視ポイント

- 「消費者が事前に委任し、その後のトランザクションは不在で完結する」設計への移行タイミングはいつか？
- AP2 FIDO Alliance の Intent Mandate と Mastercard Agent Pay の Verifiable Intent は統合・相互運用されるか？
- Mastercard と Worldline の今後のユースケース発表（旅行・サブスクリプション・定期発注）

## 未解決の論点

- Mastercard Agent Pay と Visa Intelligent Commerce（Agentic Ready）は欧州でどのように競合・共存するか？
- 消費者承認フローの UX はどう設計されたか（通知方式、タイムアウト設定など）？
- 実取引規模（件数・金額）の公開はあるか？

## 参考リンク

- 一次情報: [Worldline プレスリリース（2026-06-02）](https://worldline.com/en/home/top-navigation/media-relations/press-release/pr-2026_06_02_01)
- 補足情報: [Mastercard Newsroom Europe](https://www.mastercard.com/news/europe/en/newsroom/press-releases/en/2026/worldline-ing-and-mastercard-complete-a-live-end-to-end-european-agentic-payment-in-production/) / [GlobeNewswire](https://www.globenewswire.com/news-release/2026/06/02/3305397/0/en/) / [Finextra](https://www.finextra.com/newsarticle/47844/ing-completes-live-end-to-end-european-agentic-payment-transaction) / [LeapRate](https://www.leaprate.com/forex/technology/worldline-ing-mastercard-europe-first-live-agentic-payment-transaction/)

## 重要度

- High

## 確からしさ

- High
