# Apify MCP x402 Payments

## Overview

Apify MCP x402 Payments は、MCP 経由の paid tool call を API token ではなく x402 または Skyfire payment token で支払えるようにする monetization surface。

## User Goal

agent が web/data tools を呼ぶたびに、account-less に usage-based payment したい。

## Business Goal

Apify が既存 Actor marketplace を agent-native billing に拡張すること。

## Category

x402, agent-payments

## Core Workflow

agent は x402 wallet か Skyfire account を用意し、Apify MCP server に接続する。paid tool 実行前に prepayment し、call 後は未使用残高が保持または返金される。

## Pricing / Business Model

paid Actor usage 課金。x402 と Skyfire の prepaid balance model。

## Differentiation

x402 を protocol demo ではなく、既存 MCP tool marketplace の billing option として実装している点。

## Operational Notes

導入前に failed run refund、tool provider settlement、ledger export、buyer dispute handling を確認したい。

## Risks / Open Questions

- prepaid balance model が高頻度利用で friction にならないか要確認
- provider 側 accounting と usage reconciliation の surface が未確認
- x402 / Skyfire 間の運用差分が team に伝わりづらい可能性

## Sources

- https://github.com/apify/apify-mcp-server
