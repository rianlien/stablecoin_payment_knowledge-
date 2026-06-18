# Solayer Pay

## Overview

Solayer Pay は、stablecoin balance を Apple Pay / Google Pay / physical card spend に変換する wallet-and-card surface。

## User Goal

stablecoin を送金専用資産ではなく、普段の card checkout でそのまま使える spendable balance として扱いたい。

## Business Goal

Solayer が issuer-managed spend layer として継続利用され、stablecoin wallet を consumer payment product に変換すること。

## Category

wallet-ux, checkout, compliance

## Core Workflow

user は wallet を作成し KYC を通過する。stablecoin balance を funding source として virtual / physical card を使い、merchant 側では通常の card acceptance に近い形で決済が成立する。

## Pricing / Business Model

card / wallet product。source 上では詳細 pricing 未確認。interchange、FX、issuance fee などは要確認。

## Differentiation

stablecoin acceptance を merchant wallet integration ではなく card rail に吸収し、consumer 側の spend UX を主役にしている。

## Operational Notes

導入前に KYC geography、supported assets、settlement path、chargeback / refund handling、merchant descriptor / traceability を確認したい。

## Risks / Open Questions

- card rail の dispute model と on-chain funding の責任境界が複雑
- supported geographies と compliance gating が adoption 上限を決める
- merchant が stablecoin 決済として認識しづらく analytics が見えにくい可能性

## Sources

- https://solayer.org/blog/solayer-pay
