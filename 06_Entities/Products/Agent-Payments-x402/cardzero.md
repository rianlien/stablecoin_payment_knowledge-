# CardZero

## Overview

CardZero は、agent wallet、x402 payment、A2A escrow、on-chain reputation を Base 上の open stack としてまとめる agent commerce infrastructure。

## User Goal

agent に支払いを任せたいが、wallet rules、escrow、counterparty trust を別々に自作したくない。

## Business Goal

CardZero が autonomous agent commerce の settlement layer を取ること。

## Category

agent-payments, x402, wallet-ux, compliance

## Core Workflow

agent は wallet を生成し、owner が claim と funding、spending rules 設定を行う。以後 agent は API key で x402 paywall 決済や agent-to-agent job escrow を実行する。

## Pricing / Business Model

infrastructure / API 型。platform fee を含む escrow split が示されている。

## Differentiation

wallet rules、escrow、reputation まで含め、agent payment を commerce workflow として設計している点。

## Operational Notes

導入前に KYC roadmap、escrow dispute handling、Base dependency、owner recovery flow、rule granularity を確認したい。

## Risks / Open Questions

- beta 期の no-KYC posture が長続きするか不明
- reputation signal の悪用耐性が未確認
- regulated use case に入ると法務負荷が急増する可能性

## Sources

- https://cardzero.ai/
