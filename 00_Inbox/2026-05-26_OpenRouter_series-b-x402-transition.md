---
title: "OpenRouter、Google CapitalG主導1.13億ドルシリーズBを調達しx402決済への移行を計画"
date: 2026-05-26
source: BusinessWire / SiliconAngle / TechCrunch / Cryptobriefing
source_url: https://siliconangle.com/2026/05/26/openrouter-raises-113m-bring-order-enterprise-ai-inference-routing/
entity: OpenRouter
category: machine-payments
primary_category: machine-payments
article_published_date: 2026-05-26
underlying_event_date: 2026-05-26
primary_source_date: 2026-05-26
tags:
  - openrouter
  - x402
  - machine-payments
  - api-billing
  - agentic-commerce
summary: "OpenRouterがGoogle CapitalG主導の1.13億ドルシリーズBを調達し評価額1.3億ドルに。週250兆トークン処理（月1,000兆トークン）・400以上のモデル・800万ユーザー規模のAI推論ルーティングプラットフォームが、従来のAPIキー課金からx402プロトコルによるペイ・パー・ユースUSDC決済への移行を計画。x402は同時期に2,000以上のAPIで累計5,000万ドルの処理を達成。"
implications: "AI推論市場で最大規模に近いルーターがx402に移行すると、USDC決済量が飛躍的に増加し、x402エコシステムのGMVが大幅に押し上げられる。ただし移行計画の一次確認は未済。"
importance: High
confidence: Medium
follow_up: "OpenRouter公式アナウンスメントでのx402移行スケジュール発表、x402累計処理量の次のマイルストーン（$100M到達時期）、移行後のOpenRouterユーザー向けUSDCウォレット要件の確認"
---

## 概要

2026年5月26日、AI推論ルーティングプラットフォームのOpenRouterがGoogle CapitalG主導の1.13億ドルシリーズBを調達。評価額は約1.3B USD（1年前の約$547Mから2倍超）。処理規模は月1,000兆トークン（25T/週）、400以上のモデル、800万ユーザー。同時期の第三者報道では、OpenRouterが従来のAPIキー・サブスクリプション課金からx402プロトコルによるペイ・パー・ユースUSDC決済への移行を計画していることが報じられた。x402プロトコルは同時期に2,000以上のAPIで累計5,000万ドルのUSDC決済を処理している。

## 何が起きたか

- OpenRouter、Google CapitalG主導のシリーズB 1.13億ドルを調達（2026-05-26 BusinessWire公式発表）
  - 参加投資家：NVentures（NVIDIA）、ServiceNow Ventures、MongoDB Ventures、Snowflake Ventures、Databricks Ventures、a16z、Menlo Ventures
  - 評価額：約1.3B USD（1年前比約2倍）
- OpenRouterの規模：400以上のモデルを提供、800万ユーザー、週250兆トークン処理（月1,000兆トークン、6ヶ月で5倍増）
- 年間推論トラフィック：約$10億超（報道ベース）
- x402移行計画：APIキー・アカウントベース課金からペイ・パー・ユースUSDC決済に移行予定とCryptobriefingが報道（~2026-05-23）
- x402プロトコルの状況（同時期集計）：累計5,000万ドルのUSDC決済処理、2,000以上のAPI対応

## 確認された事実

- 調達額：1.13億ドル（公式BusinessWire発表 2026-05-26）
- 評価額：約1.3B USD（1年で2倍超）
- 規模：25T tokens/週（月1,000兆トークン）、400+モデル、800万ユーザー
- x402移行：Cryptobriefing記事（~2026-05-23）での報道。OpenRouter公式アナウンスメントでの一次確認は未済
- x402累計処理量：5,000万ドル超、2,000+ APIs（第三者集計、集計方法・期間の詳細不明）

## なぜ重要か

### 決済事業者視点

- 年間$10億超の推論トラフィックをルーティングするOpenRouterがx402に移行すると、USDC決済量が飛躍的に増加。ステーブルコイン決済レールがAPIビリングの主流になるシナリオが現実味を帯びる
- x402のGMVが急増すると、x402ファシリテーター（現在はCoinbase CDP）への処理手数料ビジネスも拡大——PSPにとってのx402参入機会が増大

### 加盟店視点

- OpenRouter経由でモデルを提供するプロバイダー（Anthropic・OpenAI・Google等）がx402決済を受け取るシナリオでは、API加盟店がx402対応するだけで大量の自動決済を取り込める
- 従来のインボイス・月次課金モデルから、リクエスト単位の即時USDC決済への移行はB2B APIビジネスの収益構造を変える

### プロダクト視点

- x402ペイ・パー・ユースモデルは「リクエスト単位の超高頻度決済」を前提としており、従来のサブスクリプション課金では実現できなかった従量課金の粒度を実現
- OpenRouterのルーティングアルゴリズム（コスト・精度・速度）がx402決済に統合されると、エージェントが「最も安い+最も速いモデル」を自動選択してその場でUSDCで支払うアーキテクチャが完成

### 規制 / リスク視点

- OpenRouterがx402（USDC）決済に移行する場合、GENIUS Act下でのPPSI（許可済みステーブルコイン発行者）要件・AML規制への準拠が新たな課題になる
- x402決済における課税（API利用料としてのUSDC受け取り）の扱いは各国で不明確——日本では仮想通貨課税規制の適用可能性あり

## 我々への示唆

- いま検討すべきこと:
  - OpenRouterのx402移行の一次確認——OpenRouter公式アナウンスメントページを確認し、移行タイムラインと対象範囲を把握
  - x402のペイ・パー・ユースAPIビリングを自社サービスに適用した場合のUX・Unit Economicsを試算（OpenRouterの事例が参考になる）
- 後で深掘りすべきこと:
  - OpenRouter x402移行後のUSDC決済量推移——現在の月額$10億推論課金がどの割合でx402に移行するか
  - x402の2,000+ API / $50M実績の集計方法と内訳（OpenRouter向け vs その他の分類）
- 今は優先度が低いこと:
  - NVIDIA・ServiceNow等の戦略的投資家の意図の読み取り——x402・ステーブルコイン文脈での戦略は不明

## ありそうな示唆

- OpenRouterのx402移行が実現した場合、AI推論の支払いがUSDCのオンチェーン決済になることで「AI利用料 = ステーブルコイン決済」の実例が月1,000兆トークン規模で生まれる。x402エコシステムGMVを大幅に押し上げる
- Google CapitalGがOpenRouterに出資していることで、GoogleのAP2（FIDO Alliance）とx402の接続がOpenRouter経由で進む可能性（GoogleはAP2とx402の両方に関与）

## 推測 / 監視ポイント

- OpenRouter公式アナウンスメントでのx402移行スケジュール発表
- 移行後のUSDC決済量（x402.org・Cryptobriefing等の追跡報道）
- x402の次の累計マイルストーン（$100M到達時期）

## 未解決の論点

- OpenRouterのx402移行が公式発表されていない（Cryptobriefing報道が一次）——公式確認が必要
- x402移行の対象範囲（全モデル/全ユーザーか、一部先行か）
- x402 USDC決済に移行した場合のOpenRouterユーザー向けUXの変化（暗号資産ウォレット保有要件）

## 参考リンク

- 一次情報: [BusinessWire（2026-05-26）](https://www.businesswire.com/news/home/20260526953416/en/OpenRouter-Raises-$113-Million-CapitalG-led-Series-B-as-Weekly-Volume-Explodes-to-25T-Tokens)
- 補足情報: [SiliconAngle（2026-05-26）](https://siliconangle.com/2026/05/26/openrouter-raises-113m-bring-order-enterprise-ai-inference-routing/) / [TechCrunch（2026-05-26）](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/) / [Cryptobriefing（~2026-05-23）](https://cryptobriefing.com/x402-protocol-50m-payments-openrouter/)

## 重要度

- High

## 確からしさ

- Medium（シリーズB自体はHigh。x402移行はCryptobriefing報道のみで一次確認未済のためMedium）
