# ClawRouter

## Overview

ClawRouter は BlockRun が公開している x402 routing / wallet auth / paywall unlock 向けの open-source project。paid API や agent tool access を self-host で検証しやすい。

## User Goal

builder が x402 payment router の責務をローカルで理解し、hosted facilitator なしでも demo や prototype を組みたい。

## Business Goal

BlockRun が x402 / agent payments 周辺の builder ecosystem に入り込み、上位 product への導線を持つこと。

## Category

x402, agent-payments

## Core Workflow

developer は repo を使って local router / server を立ち上げ、wallet auth、payment verification、resource unlock の流れを self-host で確認する。

## Pricing / Business Model

open-source demo / developer acquisition 型。詳細 business model は source 上で未確認。

## Differentiation

merchant / router 側の state と payment unlock の実装責務をコードで追えるため、hosted docs では見えない運用論点を把握しやすい。

## Operational Notes

導入前には secret management、settlement monitoring、replay protection、fulfillment failure handling、operator support surface の不足を補う必要がある。

## Risks / Open Questions

- production readiness は限定的とみるべき
- dashboard や merchant ops surface が別途必要
- facilitator / wallet provider の差し替え容易性は未確認

## Sources

- https://github.com/blockrun-ai/clawrouter
