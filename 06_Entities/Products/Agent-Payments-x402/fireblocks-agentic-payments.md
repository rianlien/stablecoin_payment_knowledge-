# Fireblocks Agentic Payments Suite

## Overview

Fireblocks Agentic Payments Suite は、AI agent に stablecoin payment を実行させるための wallet orchestration、policy controls、compliance layer、x402 integration をまとめた managed product surface。

## User Goal

agent に支払いを任せたいが、wallet control、approval boundary、counterparty risk を自前実装したくない。

## Business Goal

Fireblocks が custody / wallet infra の延長で agentic payments の default control plane を取ること。

## Category

agent-payments, wallet-ux, compliance, x402

## Core Workflow

team は Fireblocks 上で agent wallet と payment policy を設定し、AI workflow から stablecoin payment を呼び出す。必要に応じて x402 flow や internal approval / compliance control を挟みながら transaction を実行する。

## Pricing / Business Model

enterprise infrastructure / managed suite 型。詳細 pricing は source 上で未確認。

## Differentiation

単なる wallet API ではなく、agent payment の governance を suite として束ねている。導入時の中心論点を rail ではなく control に置いている。

## Operational Notes

導入前に確認したいのは wallet policy granularity、human approval step、merchant allowlist、audit export、sanctions screening、x402 responsibility boundary。

## Risks / Open Questions

- approval と auto-execution の境界がどこまで configurable か不明
- x402 integration が merchant verification まで含むか不明
- non-Fireblocks stack との interoperability がどこまであるか未確認

## Sources

- https://www.fireblocks.com/products/agentic-payments
