# ATXP

## Overview

ATXP は、AI agent が self-register して wallet、email、funding、paid tool access をまとめて持てる agent account layer。

## User Goal

agent ごとに API key と vendor account を人手配布せず、funded identity をすぐ作りたい。

## Business Goal

ATXP が agent economy の default account / funding primitive を取ること。

## Category

agent-payments, x402, wallet-ux

## Core Workflow

developer または agent は CLI で account を作成し、wallet address と connection token を受け取る。そこから paid tools や LLM endpoint を使い、必要なら追加資金を入れる。

## Pricing / Business Model

usage-based account / tool access 型。初期 credits あり。詳細 pricing は source 上で未確認。

## Differentiation

wallet 単体ではなく、agent identity、funding、tool access を 1 account としてまとめている。hub 上で x402 / MPP compatibility も打ち出している。

## Operational Notes

導入前に budget controls、org ownership、account recovery、audit logging、enterprise approval path を確認したい。

## Risks / Open Questions

- compatibility と native settlement support の境界が不明
- enterprise governance 機能の厚みが未確認
- account portability と lock-in がどれくらいか要確認

## Sources

- https://docs.atxp.ai/agents/index
- https://hub.atxp.ai/
