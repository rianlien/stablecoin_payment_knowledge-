# Slash Global USD Cards

## Overview

Slash は 2026-04-30 に `Slash Global USD Cards` を公開した。Global USD Account の USDSL 残高を、U.S. entity や U.S. bank account なしで Visa 加盟店に使える business spend surface に変換する。

## User Goal

international business が stablecoin-backed USD balance を保持するだけでなく、そのまま vendor payment、ad spend、software subscription、team expense に使いたい。

## Business Goal

Slash の global account と stablecoin infrastructure を、business banking / treasury から日常支出まで拡張し、顧客の spend operating system を握ること。

## Category

wallet-ux, compliance

## Core Workflow

business は Global USD Account を開設し、ACH、SWIFT、USDC / USDT、Stripe / Shopify payout などで資金を入れる。支払い時は USDSL 残高から real-time authorization が行われ、Visa merchant では通常の card UX で決済される。dashboard では limit、freeze、team spend control を扱える。

## Pricing / Business Model

Global account、stablecoin rails、card issuing、team spend controls をまとめた business finance product。card interchange、account usage、treasury / payment services が収益源と見られる。

## Differentiation

stablecoin を off-ramp 前の treasury asset に留めず、既存 Visa acceptance に自然接続している点が強い。U.S. entity 不要の USD access と point-of-sale off-ramp を一体化しているのも practical。

## Operational Notes

公式情報では Rain partner 発行、USDSL balance からの支払い、hourly batched settlement、real-time authorization、virtual / physical cards、dashboard controls が明示されている。導入前は geography 制限、refund / dispute、bookkeeping export を確認したい。

## Risks / Open Questions

- refund、chargeback、reversal の会計・残高反映が未確認
- USDSL の redemption / reserve / safeguarding boundary の理解が必要
- country eligibility と compliance review の詳細が未確認

## Sources

- https://www.slash.com/blog/now-live-global-usd-cards
