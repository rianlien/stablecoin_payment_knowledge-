# Bankr x402 Cloud

## Overview

Bankr x402 Cloud は、有料 API endpoint を x402 対応で素早く公開するための hosted platform。CLI と chat の両方から endpoint を作成・deploy・運用できる。

## User Goal

開発者が stablecoin 決済対応の paid API を短時間で立ち上げたい。

## Business Goal

x402 endpoint の供給を増やし、Bankr 上で hosting・discovery・payment execution をまとめて握ること。

## Category

x402, agent-payments

## Core Workflow

handler を書くか chat で生成し、価格を設定して deploy する。client は endpoint を呼び、`402` 後に自動決済し、開発者は dashboard で usage / revenue / logs を見る。

## Pricing / Business Model

free plan と platform fee model。最初の 1,000 requests は無料、その後は platform fee がかかる。

## Differentiation

x402 の支払い層を隠し、単なる request/response handler の公開体験まで落としている。chat-driven deploy は試作速度が高い。

## Operational Notes

env 管理、revenue 可視化、agent discovery まで一体化している一方、provider 依存が高くなりやすい。

## Risks / Open Questions

- 本番 SLA と performance isolation が未確認
- export / accounting / tax 周りがどこまであるか未確認
- 収益や endpoint portability がどこまで担保されるか不明

## Sources

- https://docs.bankr.bot/x402-cloud/overview
- https://docs.bankr.bot/x402-cloud/security

