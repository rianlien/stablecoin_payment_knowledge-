# World x402 identity-gated payments

## Overview

World x402 identity-gated payments は、World ID と x402 payment flow を組み合わせ、verified human layer を payment execution に持ち込む product signal。frictionless stablecoin rail に payer legitimacy を加える設計として読むのが自然。

## User Goal

bot / sybil を避けつつ、human-verified payment flow を構築したい。

## Business Goal

identity assurance を payment flow の前段に置き、trust-sensitive commerce の導入障壁を下げる。

## Category

wallet-ux, compliance, x402

## Core Workflow

merchant または provider は x402 payment flow に World ID verification を差し込む。payer は verification を伴う形で支払いを実行し、merchant 側は verified human signal を payment 判断に使う。

## Pricing / Business Model

未確認。identity infrastructure と payment flow integration の組み合わせとして売られる可能性が高い。

## Differentiation

stablecoin payment の frictionless 性と payer legitimacy の両立を狙う点が特徴。KYC shell とは別に、`verified human` を payment UX に直接足すレイヤとして見える。

## Operational Notes

wallet UX の観点では、署名 UI だけでなく `この支払いは誰のものか` をどう示すかが重要になる。World の signal は、compliance を onboarding 書類ではなく execution-time trust signal に寄せている。

## Risks / Open Questions

- World ID verification が optional か mandatory か不明
- business buyer / software agent / human payer の混在にどう対応するか不明
- privacy disclosure と false reject handling が不明

## Sources

- https://www.x402.org/ecosystem
