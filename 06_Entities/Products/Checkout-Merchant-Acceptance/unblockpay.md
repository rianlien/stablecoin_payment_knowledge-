# UnblockPay

## Overview

UnblockPay は、wallets、pay-ins、payouts、fiat/stablecoin conversion、webhooks、sandbox をまとめた stablecoin banking API。

## User Goal

stablecoin と local payment rails を一つの API で扱い、marketplace や treasury product に組み込みたい。

## Business Goal

UnblockPay が stablecoin-to-fiat orchestration の default backend になること。

## Category

checkout, invoicing, wallet-ux, compliance

## Core Workflow

platform は customers と wallets を作成し、pay-ins や payouts を API で実行する。裏側では blockchain networks、liquidity providers、local rails が orchestration される。

## Pricing / Business Model

API / banking infrastructure 型。詳細 pricing は source 上で未確認。

## Differentiation

wallet API、on/off-ramp、local payout を separate provider にせず、一つの banking API として束ねている点。

## Operational Notes

導入前に supported geographies、KYB / KYC responsibilities、webhook reliability、ledger / reconciliation export、SLA を確認したい。

## Risks / Open Questions

- invoice / AR workflow は外部会計前提の可能性が高い
- jurisdiction ごとの compliance handoff が要確認
- liquidity / payout failure 時の retry semantics が未確認

## Sources

- https://docs.unblockpay.com/
