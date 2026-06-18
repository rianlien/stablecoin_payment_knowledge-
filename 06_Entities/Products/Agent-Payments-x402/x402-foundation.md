# x402 Foundation

## Overview

x402 Foundation は、HTTP-native stablecoin payments のための x402 spec、middleware、examples、developer docs を public repo として提供する reference stack。

## User Goal

developer team が pay-per-request API や agent tool monetization を、closed hosted service に依存しすぎず実装したい。

## Business Goal

x402 ecosystem の adoption を広げ、payment-gated internet resource の標準的な実装導線を作ること。

## Category

x402, agent-payments

## Core Workflow

developer は repo の spec と examples を使って x402-enabled endpoint を実装し、client は payment-required flow に沿って USDC payment を行い resource access を得る。

## Pricing / Business Model

open-source / ecosystem layer。直接的 pricing はない。

## Differentiation

protocol 説明だけでなく middleware と reference code を揃え、x402 を再利用可能な builder surface にしている。

## Operational Notes

production では facilitator choice、settlement monitoring、usage metering、refund / fulfillment semantics、merchant support layer を別途設計する必要がある。

## Risks / Open Questions

- facilitator dependency をどこまで抽象化できるか不明
- idempotency と dispute / refund の標準化が未成熟
- supported chains / assets の広がりが adoption を左右する

## Sources

- https://github.com/x402-foundation/x402
