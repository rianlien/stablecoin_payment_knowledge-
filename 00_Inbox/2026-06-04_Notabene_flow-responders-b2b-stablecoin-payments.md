---
title: "Notabene、Flow responder を数百機関へ拡張し B2B stablecoin payments の到達性を引き上げ"
date: 2026-06-04
source: PR Newswire / Notabene
source_url: https://www.prnewswire.com/apac/news-releases/notabene-flow-activates-hundreds-of-customers-enabling-stablecoin-b2b-payments-across-the-globe-819974824.html
entity: Notabene
category: machine-payments / stablecoin-infrastructure / payment-authorization
primary_category: machine-payments
article_published_date: 2026-06-04
underlying_event_date: 2026-06-04
primary_source_date: 2026-06-04
tags:
  - Notabene
  - stablecoin-infrastructure
  - B2B-payments
  - payment-authorization
  - machine-payments
summary: "Notabene が 6 月 4 日、Notabene Flow の responder capabilities を network-wide rollout し、既存ネットワーク上の数百の regulated institution 顧客から Flow payment を受けられる状態にした。payment link を受け取った payer は、自分が既に使っている hosted wallet から追加 onboarding なしで支払いを完了できる"
implications: "2 月の Flow ローンチ後、今回は reachability の実装段階に進んだ。agentic / B2B stablecoin payments は決済手段の存在だけでは足りず、『相手が既存口座からそのまま払えるか』が adoption のボトルネックであることを示している"
importance: Medium
confidence: High
follow_up: "live responder 数の正確な開示、対応 wallet / institution 範囲、self-hosted wallet の実運用比率、invoice / recurring payment の実績件数を確認する"
---

## 概要
- Notabene が 2026 年 6 月 4 日、Flow の responder rollout を公表した
- 新しい rail の追加ではなく、既存 network 上の到達性を一気に上げた点が今回の本質

## 何が起きたか
- Notabene Network に既に接続済みの exchanges、custodians、payment providers、banks へ Flow responder capabilities を rollout した
- これにより、Flow payment link を送られた支払者は、自分の hosted wallet から追加 onboarding なしで支払える
- self-hosted wallet からの支払い経路も用意されている
- Notabene は Flow を TAP ベースの open network として位置付けている

## 確認された事実
- PR Newswire 上の公式発表日は 2026-06-04
- 公式文面で hundreds of regulated digital asset institutions の顧客が Flow payment を完了できる状態になったと説明している
- responder rollout は既存の Notabene customer base に対する network-wide rollout と記載されている

## なぜ重要か

### 決済事業者視点
- B2B stablecoin payments の実用性は protocol の elegance より受け手ネットワークの reach で決まる。Notabene はその reach を network effect として前面に出した
- hosted wallet から追加統合なしで払える設計は、institution 向け stablecoin PSP の普及に必要な条件をよく表している

### 加盟店視点
- 高額 B2B 請求では、相手に新しい wallet や app を入れさせないことが重要。既存 account から払えるなら導入障壁は大きく下がる
- invoice、pull payment、recurring flow がそのまま使えるなら、crypto native でない finance team にも提案しやすい

### プロダクト視点
- payment link、counterparty verification、pre-settlement authorization、reconciliation を一連の flow として束ねる設計は、agentic B2B billing に近い
- machine payments でも最重要なのは「即時 settlement」単体ではなく「authorization と context が事前共有されること」だと再確認できる

### 規制 / リスク視点
- Travel Rule compliant multi-party flow を前提にしているため、regulated institution 間の導入現実性は高い
- 一方で、network 外の相手、失敗時 reversal、chargeback 相当の処理は依然として観察が必要

## 我々への示唆
- いま検討すべきこと:
  - B2B / machine payment では reachability を主要 KPI に置く
  - onboarding friction を下げるため、既存口座・既存 wallet からの支払い完了率を重視して設計する
- 後で深掘りすべきこと:
  - TAP / Flow の responder 実装要件
  - invoice、subscription、payout のどこが最も伸びるか
- 今は優先度が低いこと:
  - self-hosted wallet 向け細かな UX

## ありそうな示唆
- stablecoin B2B payments は「新しい network を作る」より「既存 regulated network に payment responder を有効化する」ほうが普及速度が速い可能性が高い

## 推測 / 監視ポイント
- responder 数が数百から何千へ伸びるか
- Flow の recurring / agentic billing 実績が開示されるか
- TAP が他の stablecoin payment network へ広がるか

## 未解決の論点
- active responder の正確な定義
- hosted wallet と self-hosted wallet の利用比率
- dispute や reversal の標準処理

## 参考リンク
- 一次情報:
  - [PR Newswire（2026-06-04）](https://www.prnewswire.com/apac/news-releases/notabene-flow-activates-hundreds-of-customers-enabling-stablecoin-b2b-payments-across-the-globe-819974824.html)
  - [Notabene Flow](https://notabene.id/flow)
- 補足情報:
  - [Notabene developer docs](https://devx.notabene.id/docs/introduction)

## 重要度
- Medium

## 確からしさ
- High
