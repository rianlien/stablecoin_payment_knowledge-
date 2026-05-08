---
title: "Polygon × Hinkal、ZKPベースのプライベートステーブルコイン決済をメインネットでローンチ——KYTスクリーニング付き機関向けプライバシー機能"
date: 2026-05-04
source: "Polygon Labs公式ブログ / crypto.news / Bitcoin.com News"
source_url: "https://polygon.technology/blog/private-payments-are-live-on-polygon"
entity: "Polygon / Hinkal"
category: "payments"
tags:
  - stablecoin
  - payments
  - kyt
  - protocol
  - wallet
summary: "2026年5月4日、PolygonがHinkalとの連携でゼロ知識証明（ZKP）を使ったプライベートステーブルコイン決済をメインネットで正式ローンチ。USDC・USDTの送受金において送信者・受信者・金額を非公開にしつつ、規制当局向けにKYTスクリーニングを通じた取引適法性の検証を維持する。非カストディアル設計で資産は当事者以外が保有しない。機関投資家・企業財務向けの本番稼働が始まった。"
implications: "プライバシー×コンプライアンスの両立が技術的に実現した最初の主要事例。機関向けステーブルコイン決済の採用障壁を下げる可能性がある。ただし、AML当局がシールドプールをどう評価するかは未確定。"
follow_up: "シールドプールのKYTロジック詳細、規制当局（FinCEN等）の評価、他チェーン展開予定"
---

## 概要

Polygonは2026年5月4日、プライバシー技術企業Hinkalとの提携で、ゼロ知識証明（ZKP）を用いたプライベートステーブルコイン決済機能「Private Payments on Polygon」をメインネットで正式稼働させた。Polygonウォレット上から利用可能で、USDC・USDTの送金において送信者・受信者・金額をいずれも外部に公開しない。一方で、シールドプール内でHinkalのKYT（Know Your Transaction）スクリーニングを実施し、規制当局が取引の適法性を検証できる仕組みを維持している。

## 何が起きたか

- **2026年5月4日**: Polygon Labsが公式ブログで「Private Payments are Live on Polygon」を発表
- **技術構成**:
  - ZKPによる送信者・受信者・金額の秘匿（シールドプール方式）
  - Hinkalプロトコルがシールドプールを管理し、ZKPで取引内容を確認しながら詳細は非公開
  - 非カストディアル設計——資産はHinkalにもいかなる第三者にも預けられない
- **対応ステーブルコイン**: USDC・USDT
- **利用インターフェース**: Polygonウォレット（現時点）
- **KYT統合**: 規制当局が取引の合法性を検証できるよう、シールドプールにKYTスクリーニングを組み込み
- **次のステップ**: Polygonは今後さらなるプライバシー機能の拡充を予告

## なぜ重要か

### 決済事業者視点
- 企業財務・機関向け決済において「プライバシー要件とAML要件を同時に満たす」ソリューションの初期事例が登場
- 従来、法人がオンチェーン決済を避けてきた理由の一つ（取引が全世界公開になる）に対する技術的回答が出た

### 加盟店視点
- サプライヤーへの支払い・給与・M&A関連の資金移動など、公開性を避けたいB2B決済での活用可能性
- ただし現時点でPolygonウォレット限定のため、既存業務インフラへの統合には開発工数が必要

### プロダクト視点
- KYT付きシールドプールという設計モデルは、今後の規制準拠プライバシー決済の参照アーキテクチャになりうる
- EIP-7503（ZK Wormholes）・ERC-5564（Stealth Addresses）等の既存プロトコルとの差別化ポイントを整理する必要がある

### 規制 / リスク視点
- FinCEN・OFACがシールドプールをどう評価するかは未確定。シールドプール全体への制裁リスクの先例（Tornado Cash）があるため、コンプライアンスチームのレビューが不可欠
- KYTスクリーニングの内容（どの基準で「適法」と判断するか）が公開されていない点は大きなリスク要因
- 規制当局が「検証できる」とされているが、その検証プロセスの法的有効性は未確認

## 我々への示唆

- いま検討すべきこと:
  - KYTロジックの詳細と、当局への開示範囲を確認してから採用可否を判断
  - プライバシー決済ニーズを持つ法人顧客（機関・大企業財務）がいる場合はパイロット候補として評価
- 後で深掘りすべきこと:
  - シールドプールへの規制当局アクセス方法——技術的にどう実現しているか（ZK証明の種類・検証鍵管理）
  - 他チェーン（Ethereum L1・Base等）への展開予定
- 今は優先度が低いこと:
  - 個人消費者向けユースケースは規制審査が更に厳しくなる可能性があるため、B2B先行で評価

## 未解決の論点

- KYTスクリーニングの具体的な基準と、当局へのアクセス方法の詳細は？
- Tornado Cashへの制裁措置（2022年）と本サービスの法的差異をどう説明するか？
- シールドプール内に凍結対象資産が混入した場合の対処方法は？
- HinkalはFinCEN登録のMSB（Money Services Business）か否か？

## 参考リンク

- 一次情報: [Polygon Labs公式ブログ](https://polygon.technology/blog/private-payments-are-live-on-polygon)
- 補足情報: [crypto.news](https://crypto.news/polygon-rolls-out-private-stablecoin-payments-with-hidden-transfers/) / [Bitcoin.com News](https://news.bitcoin.com/polygon-unveils-private-stablecoin-payments-to-lure-traditional-finance/) / [Invezz](https://invezz.com/news/2026/05/05/polygon-introduces-private-stablecoin-payments-to-court-institutions/)

## 重要度
- Medium

## 確からしさ
- High
