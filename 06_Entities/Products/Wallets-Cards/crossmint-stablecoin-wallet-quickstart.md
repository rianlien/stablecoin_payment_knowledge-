# Crossmint Stablecoin Wallet Quickstart

## Overview

Crossmint Stablecoin Wallet Quickstart は、email recovery wallet を作成し、server-side signer を一度承認したあとに backend から stablecoin transfer を実行できる demo / starter。

## User Goal

agent-driven payment flow を試したいが、毎回 user wallet 署名を求める UX は避けたい。

## Business Goal

Crossmint の wallet delegation model を builder の default starter として広げること。

## Category

wallet-ux, agent-payments

## Core Workflow

user は login 時に wallet を作成し、email-OTP で backend signer を承認する。wallet を funded した後は server signer が stablecoin transfer を実行できる。結果として `one-time approval + delegated execution` の flow を短く再現できる。

## Pricing / Business Model

quickstart 自体は open-source demo。収益ポイントは Crossmint Wallets SDK と API key 利用にある。

## Differentiation

wallet creation、recovery、signer delegation、transfer までを一つの最短サンプルに落としている。抽象論ではなく delegated signer UX の雛形として価値がある。

## Operational Notes

Base Sepolia と staging API key 前提。production 利用では signer revoke、spend limits、audit history、error recovery を別途詰める必要がある。

## Risks / Open Questions

- signer scope を金額 / counterparty 単位でどこまで制御できるか
- compromised backend signer 時の remediation flow はどうなるか
- Crossmint 依存を薄くしたい場合の portability は低い可能性

## Sources

- https://github.com/Crossmint/stablecoin-wallet-quickstart
- https://docs.crossmint.com/
