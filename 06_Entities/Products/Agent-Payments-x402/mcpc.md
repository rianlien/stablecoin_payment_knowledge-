# `mcpc` x402 support

## Overview

`mcpc` x402 support は、Apify の MCP client CLI に paid MCP server 向け x402 handling を追加する experimental payment surface。

## User Goal

paid MCP tools をすぐ試したい developer が、独自 billing flow ではなく CLI レベルで x402 payment-required を処理したい。

## Business Goal

MCP ecosystem に usage-based paid tooling を持ち込み、tool distribution と payment を結び付けやすくすること。

## Category

x402, agent-payments

## Core Workflow

client が paid MCP server に接続すると `mcpc` が x402 payment requirement を解釈し、支払い完了後に tool access を継続する。

## Pricing / Business Model

open-source CLI の experimental support。収益化は paid MCP server / hosted wallet / settlement provider 側に属する。

## Differentiation

x402 を abstract protocol で終わらせず、MCP client CLI の実行面にそのまま差し込んでいる。

## Operational Notes

導入前に signer model、receipt persistence、usage quotas、error recovery、server-side settlement backend の前提を確認したい。

## Risks / Open Questions

- experimental support のため interface が変わりやすい
- refund / dispute / quota enforcement は別レイヤーの可能性が高い
- hosted wallet 前提だと self-hosted enterprise には刺さりにくい

## Sources

- https://github.com/apify/mcp-cli
