# Circle Agent Stack

## Overview

Circle Agent Stack は、USDC を中心に agent wallet、service discovery、CLI、nanopayments をまとめた agentic payments infrastructure。Circle for Agents はその product surface。

## User Goal

agent に安全な wallet と programmable payment flow を組み込み、USDC でサービス利用や収益化を行いたい。

## Business Goal

Circle が USDC rail 上で wallet、discovery、payment execution の default stack を取ること。

## Category

x402, agent-payments, wallet-ux, compliance

## Core Workflow

developer は Agent Wallet を作成し、agent に資金と policy を付与する。agent は Marketplace で service を見つけ、Gateway を使って x402 系の payment を実行する。

## Pricing / Business Model

source 上で詳細 pricing は未確認。Circle の狙いは USDC flow を wallet と marketplace まで広げることにある。

## Differentiation

wallet、marketplace、CLI、batch settlement まで同一 stack に揃っている。単一 SDK ではなく、agent の経済活動全体を product surface にしている。

## Operational Notes

policy-controlled wallet という表現から、custody と permission boundary が adoption 上の中心論点になっていることがわかる。USDC 前提の rail 集約が強い。

## Risks / Open Questions

- wallet policy の詳細粒度が不明
- cross-chain / non-USDC / non-Circle interoperability が限定される可能性
- enterprise audit / approval requirements をどこまで満たせるか要確認

## Sources

- https://investor.circle.com/news/news-details/2026/Circle-Launches-AI-Infrastructure-to-Power-the-Agentic-Economy/default.aspx
- https://agents.circle.com/
- https://www.circle.com/nanopayments
