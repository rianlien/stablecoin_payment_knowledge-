# NEAR AI private USDC payments

## Overview

NEAR AI は Confidential Intents と USDC を組み合わせ、NEAR AI Agent Market 上で confidential な stablecoin payments を可能にする layer を公開した。agent marketplace の支払いを public-chain の露出から少し切り離す狙いが強い。

## User Goal

agent に仕事を発注し、その支払いを onchain で完了したいが、金額や取引相手を public に晒したくない。

## Business Goal

agent marketplace を enterprise adoption 可能な payment substrate に近づけ、privacy-sensitive use case を取り込むこと。

## Category

agent-payments, compliance

## Core Workflow

user / business は NEAR AI Agent Market で job を post し、agent が task を完了し、支払いは Confidential Intents 経由で USDC settlement される。

## Pricing / Business Model

公開リリース上では fee model は不明。価値は agent marketplace の confidential settlement 機能にある。

## Differentiation

stablecoin rails の speed や cost ではなく、commercial relationship の秘匿を主価値として出している。agentic commerce を business 向けに持っていくなら自然な方向。

## Operational Notes

公式リリースでは、amount や counterparty を publicly reveal しないこと、task posting から settlement まで decentralized infrastructure 上で回ることを強調している。

## Risks / Open Questions

- screening / sanctions / tax record をどう整備するか
- refund / dispute を confidential flow でどう扱うか
- closed marketplace から broader payment workflow へ広げられるか

## Sources

- https://www.prnewswire.com/news-releases/near-ai-brings-private-usdc-stablecoin-payments-to-the-agentic-economy-302772311.html
