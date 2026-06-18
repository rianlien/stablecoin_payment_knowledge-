# x402-xrpl

## Overview

x402-xrpl は、x402 payment flow を XRP Ledger / RLUSD settlement に接続する adapter repo。

## User Goal

x402 を EVM/USDC 前提に閉じず、XRPL や RLUSD のような別 rail でも machine payments を試したい。

## Business Goal

x402 を multi-rail protocol として広げ、enterprise-friendly な stablecoin / ledger への接続可能性を高めること。

## Category

x402, agent-payments

## Core Workflow

developer は x402 request/response flow を維持したまま、settlement 部分を XRPL / RLUSD adapter に委譲して支払い検証と決済完了を処理する。

## Pricing / Business Model

open-source adapter。直接の pricing ではなく、x402 対応サービスの settlement rail choice に価値がある。

## Differentiation

x402 の価値を HTTP paywall ではなく settlement rail portability として見せている。

## Operational Notes

production 導入には finality handling、issuer assumptions、multi-rail routing、merchant reporting を詰める必要がある。

## Risks / Open Questions

- RLUSD / XRPL 特有の compliance 前提が merchant に伝わりにくい
- adapter 単体では receipt / refund / analytics が足りない
- non-EVM rail を混ぜたときの buyer UX が未整理

## Sources

- https://github.com/mpcp-protocol/x402-xrpl
