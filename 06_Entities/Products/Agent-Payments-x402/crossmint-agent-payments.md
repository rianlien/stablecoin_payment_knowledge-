# Crossmint Agent Payments

## Overview

Crossmint は agent payments を、card permissions と stablecoin wallet delegation の両面から扱う docs / quickstart を公開している。browser checkout、fast checkout、x402、MPP を payment flow matrix として整理し、agent ごとに適した rail を選ばせる。

## User Goal

developer が agent に支払い権限を与えつつ、wallet custody や card data exposure を避け、scope と revoke を保ったまま決済させたい。

## Business Goal

Crossmint の wallet / card / checkout infrastructure を agent economy 向けの default payment layer にすること。

## Category

agent-payments, wallet-ux, compliance, x402

## Core Workflow

card flow では、ユーザーが card を保存・検証し、agent に spending rules 付き permission を passkey で承認する。agent は merchant-scoped one-time card credentials を使って browser checkout や API checkout を実行する。wallet flow では、ユーザーが non-custodial wallet を作成・資金投入し、agent signer に spend cap、counterparty、time window を委任する。agent はその scope 内で stablecoin transaction や x402 / MPP payment を実行する。

## Pricing / Business Model

platform / developer 向け infra business。wallets、cards、checkout、agent payment orchestration が収益ポイント。

## Differentiation

agent payment を単一 rail の話にせず、「merchant checkout は card、machine payment は stablecoin」という routing model で見せている点が実務的。spending rules、passkey approval、non-custodial delegation を product の中心に置いているのも強い。

## Operational Notes

docs 上では Visa VIC、Mastercard Agent Pay、PCI-compliant vaulting、stablecoin wallets、x402 / MPP support が説明されている。実装前は network coverage、revocation UX、audit export、merchant support boundary の確認が必要。

## Risks / Open Questions

- eligible cards が限定的で geography 依存が大きい
- wallet delegation の production-grade monitoring / audit が未確認
- one policy engine で card rail と stablecoin rail を統合できるか未確認

## Sources

- https://docs.crossmint.com/agents/overview
- https://docs.crossmint.com/agents/how-agents-pay
- https://docs.crossmint.com/agents/payment-methods/cards/create-card-permissions
