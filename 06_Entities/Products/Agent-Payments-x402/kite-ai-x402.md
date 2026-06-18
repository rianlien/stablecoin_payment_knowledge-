# Kite AI

## Overview

Kite AI は、budgets、permissions、stablecoin-native settlement を中心にした agent payment infrastructure として x402 ecosystem で紹介されている。wallet を持たせるだけでなく、spend governance を main surface にしている点が重要。

## User Goal

AI agent に payment capability を持たせたいが、permission と budget control を同時に設計したい。

## Business Goal

agent payment の rail ではなく governance shell を押さえ、policy-aware runtime の標準面を取る。

## Category

agent-payments, x402, wallet-ux

## Core Workflow

platform team は agent に payment runtime を持たせつつ、budget と permissions を定義する。agent は許可範囲内で stablecoin-native payment を実行し、operator は scope を制御する。

## Pricing / Business Model

未確認。value は settlement fee ではなく controlled spend と governance packaging にある。

## Differentiation

rail enablement より permission-first packaging を前に出している。agent payment の本体が `支払えるか` ではなく `どこまで任せるか` であることを強く反映している。

## Operational Notes

wallet UX は end-user signer UI だけでなく、operator が budget と spend scope を把握できる control UX に広がっている。Kite AI はその shift を示す早期 signal として有用。

## Risks / Open Questions

- SDK / hosted control plane / custody model の切り分けが不明
- supported chains / assets / merchant integrations が不明
- audit export と approval queue があるか不明

## Sources

- https://www.x402.org/ecosystem
