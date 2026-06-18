# AgentPay SDK

## Overview

AgentPay SDK は、AI agent 向けの self-custodial かつ policy-aware な wallet runtime / CLI。wallet access、balances、policy、transfers、approvals をローカルに管理しながら blockchain transactions を扱う。

## User Goal

builder が hosted wallet SaaS に依存せず、agent payment と approval path を self-host / local-first で持ちたい。

## Business Goal

AgentPay SDK が agent wallet governance の OSS runtime として developer adoption を獲得すること。

## Category

agent-payments, wallet-ux, compliance

## Core Workflow

operator は bootstrap script または source install で runtime を導入し、local daemon と `agentpay` CLI で wallet setup、approvals、balances、transfers を管理する。AI assistant 向け skill pack も配布される。

## Pricing / Business Model

open-source runtime / SDK 型。商用 support や周辺 managed service の詳細は source 上で未確認。

## Differentiation

payment protocol そのものではなく、approval path を持つ local wallet runtime として agent governance を具体化している点。

## Operational Notes

導入時は supported chains / assets、key management、policy rule granularity、audit trail、team approval flow を確認したい。

## Risks / Open Questions

- production readiness と supported stablecoin coverage が未確認
- enterprise key management には追加設計が必要そう
- repository activity は見えるが live merchant / live agent usage は不明

## Sources

- https://github.com/worldliberty/agentpay-sdk
