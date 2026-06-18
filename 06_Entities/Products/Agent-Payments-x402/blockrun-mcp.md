# BlockRun MCP

## Overview

BlockRun MCP は、search、research、markets、crypto、X/Twitter intelligence などの tool を、x402 micropayments による pay-per-call で提供する MCP project。

## User Goal

agent に高価な data / research tool を持たせつつ、subscription ではなく usage-based に支払いたい。

## Business Goal

tool seller と agent builder の間に、stablecoin-native な usage billing layer を作ること。

## Category

x402, agent-payments

## Core Workflow

builder は BlockRun MCP を agent に接続し、必要な tool call ごとに支払う。seller 側は tool endpoint を提供し、request 単位の monetization を行う。

## Pricing / Business Model

tool ごとの従量課金。BlockRun 全体では USDC pay-per-call と OpenAI-compatible SDK / router を組み合わせている。

## Differentiation

MCP tool 単位の monetization が明示的。API product ではなく agent tool surface を直接収益化している。

## Operational Notes

organization overview 上では 1M+ API calls/month、41+ models、USDC pay-per-call を掲げている。MCP server 課金の実務サンプルとして有用。

## Risks / Open Questions

- revenue export / accounting / audit support の粒度が不明
- enterprise procurement 向け controls が不明
- tool quality ranking と uptime signal が不足

## Sources

- https://github.com/BlockRunAI
- https://github.com/topics/x402
