# Stripe x402 integration

## Overview

Stripe x402 integration は、x402 を使う stablecoin payments を internet commerce に接続する merchant-adjacent infra signal。独立 docs は今回確認できていないが、`x402.org ecosystem` 上では「stablecoin payments for internet commerce」を担う実装面として扱われている。

## User Goal

stablecoin / x402 を既存の merchant or internet commerce stack に寄せて導入したい。

## Business Goal

新しい crypto checkout 導線を別建てせず、既存 commerce shell の中に stablecoin acceptance を取り込む。

## Category

checkout, x402

## Core Workflow

merchant または platform は x402-compatible payment flow を既存 commerce stack に差し込む。buyer 側は x402 / stablecoin rail で支払い、merchant 側は internet commerce の文脈で受け取る。実際の dashboard / API / settlement flow は今回未確認。

## Pricing / Business Model

未確認。merchant acquiring または payments infrastructure の延長で monetization される可能性が高いが、現時点では推測に留まる。

## Differentiation

stablecoin payment を crypto-native wallet UX としてではなく、merchant-facing commerce infrastructure として見せられる点が大きい。builder にとっては新しい rails より既存運用面に吸収できることが重要。

## Operational Notes

この signal が重要なのは、stablecoin acceptance の採用条件が `wallet を見せるか` ではなく `merchant に新しい運用系を増やさないか` だから。独立一次ソースが確認できるまでは、実装成熟度は保留扱いが妥当。

## Risks / Open Questions

- actual integration surface が API か dashboard か不明
- refund / dispute / reconciliation の扱いが不明
- settlement asset と fiat handoff をどこまで既存面に寄せるか不明

## Sources

- https://www.x402.org/ecosystem
