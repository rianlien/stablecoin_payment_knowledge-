# BEEP SDK

## Overview

BEEP SDK は、Sui 上の non-custodial stablecoin payments 向けに `sdk-core`、`checkout-widget`、`cli` をまとめた TypeScript monorepo。

## User Goal

stablecoin checkout、invoice creation、agent payment、MCP server monetization を一から組まずに実装したい。

## Business Goal

BEEP が agentic finance / stablecoin checkout の builder surface を押さえ、SDK と widget から導入されること。

## Category

checkout, agent-payments, invoicing, wallet-ux

## Core Workflow

frontend は checkout widget を埋め込み、backend は `sdk-core` で invoice / payment を作る。必要に応じて CLI で MCP server scaffold を生成し、agent からの payment workflow まで接続する。

## Pricing / Business Model

SDK 自体は public repo。商用価格や merchant contract は public source 上で未確認。

## Differentiation

protocol や API だけでなく、React widget、invoice object、MCP CLI まで含めており、human checkout と agent payment を同一 repo から試せる。

## Operational Notes

導入前に merchant dashboard、reconciliation export、chargeback / mistaken payment support、supported compliance model、Sui dependency の強さを確認したい。

## Risks / Open Questions

- chain 依存が強く、 multi-chain 拡張戦略が未確認
- KYC / KYB responsibility boundary が不明
- small repo のため long-term maintenance と uptime 体制が未確認

## Sources

- https://github.com/beep-it/beep-sdk
