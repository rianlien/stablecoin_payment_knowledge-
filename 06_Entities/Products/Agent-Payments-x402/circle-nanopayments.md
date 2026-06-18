# Circle Nanopayments

## Overview

Circle Nanopayments は、Circle Gateway 上で USDC の gas-free micro / nano transfer を扱う agentic payments rail。sub-cent の usage-based billing と machine-to-machine transaction を前提にしている。

## User Goal

agent、API、service 間の高頻度・少額決済を、通常のカード課金や on-chain gas cost では成立しない単価でも実装したい。

## Business Goal

Circle が USDC と Gateway を、agent economy 向けの default transaction rail にすること。

## Category

agent-payments, wallet-ux

## Core Workflow

developer は Circle Gateway で USDC balance を用意し、agent や service が payment request を作る。payer 側は支払いを sign し、Nanopayments が gas-free transfer と confirmation を行う。用途は pay-per-call、usage-based billing、M2M payments を想定している。

## Pricing / Business Model

source 上で pricing の明示は未確認。Circle の狙いは USDC flow と Gateway adoption を増やすことにある。

## Differentiation

通常の stablecoin payment を `もっと速く安く` するだけではなく、そもそも transaction size が小さすぎて既存 rails では割に合わない領域を product surface にしている点が強い。

## Operational Notes

公式 page では gas-free、permissionless、programmable が前面に出ている。導入判断では wallet provisioning、reconciliation、refund、audit export の確認が必須。

## Risks / Open Questions

- Circle Gateway 依存がどれほど強いか
- chargeback 的な dispute model をどう持つか
- merchant / API provider 向け analytics と receipt surface がどこまで揃うか

## Sources

- https://www.circle.com/nanopayments
- https://www.circle.com/blog/nanopayments-powered-by-circle-gateway-is-now-live-on-mainnet
