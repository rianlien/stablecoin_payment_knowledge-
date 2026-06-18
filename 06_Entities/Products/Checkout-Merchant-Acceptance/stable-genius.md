# Stable Genius

## Overview

Stable Genius は、POS、app、web checkout で stablecoin を受け取りつつ merchant 側は USD を銀行口座で受け取れる stablecoin checkout infrastructure。

## User Goal

merchant-facing product に stablecoin acceptance を入れたいが、wallet、blockchain、bridge、off-ramp の複雑さは表に出したくない。

## Business Goal

Stable Genius が `stablecoin in / USD out` checkout layer として terminal integrator と platform operator に採用されること。

## Category

checkout, compliance

## Core Workflow

developer は payment intent を API で作成し、画面側で QR を表示する。payer は USDC で支払い、merchant system は webhook で確定を受け取る。merchant 側は自前で chain ops を持たずに USD 銀行着金まで進められる。

## Pricing / Business Model

early access / waitlist 段階。pricing と settlement fee は source 上で未確認。

## Differentiation

`Two API calls` と `merchant gets USD in their bank account` を前面に出しており、stablecoin acceptance を crypto-native wallet flow ではなく merchant settlement abstraction として見せている。

## Operational Notes

導入前に merchant onboarding API、refund、failed payment、settlement SLA、supported jurisdictions、bank payout exception handling を確認したい。

## Risks / Open Questions

- early access のため production reliability が未確認
- USD settlement の fee structure と timing が未開示
- chargeback 不在時の merchant support / dispute handling が要確認

## Sources

- https://docs.stablegenius.co/
