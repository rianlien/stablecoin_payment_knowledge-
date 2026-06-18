# AgentPay MCP

## Overview

AgentPay MCP は、x402 を使う paid MCP tool に対して、支払い前の approval、budget cap、allowlist、audit trail を挟む non-custodial payment governance layer。

## User Goal

AI agent に paid tool を使わせたいが、勝手な支出や不明な merchant への支払いを避けたい。

## Business Goal

agent payments を本番導入する際の governance / safety layer を提供し、単なる payment execution から差別化すること。

## Category

x402, agent-payments, compliance, wallet-ux

## Core Workflow

agent は `x402_pay` を呼ぶ。AgentPay MCP は approval state と spend policy を確認し、許可されていれば署名と支払いを行い、tool、merchant、amount、receipt、policy result を audit trail に残す。

## Pricing / Business Model

OSS repo として公開。商用化ポイントは governance、multi-rail routing、auditability、enterprise control plane の可能性が大きい。

## Differentiation

payment proxy の代替ではなく、payment 実行前に policy decision を置くところが本質。agent payments の導入障壁を、決済手段ではなく統制問題として扱っている。

## Operational Notes

repo 上では spend caps、daily limits、human approval queues、non-custodial local signing、multi-chain x402 v2、Stripe Machine Payments Protocol routing に触れている。paid MCP 実装にそのまま差し込みやすい。

## Risks / Open Questions

- merchant trust / identity verification をどこまで補完するか
- approval queue が高頻度支払いでボトルネック化しないか
- audit row を finance / security tooling に出す export 面が十分か

## Sources

- https://github.com/up2itnow0822/agentpay-mcp
