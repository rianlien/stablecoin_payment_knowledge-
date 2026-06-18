# Lightspark Grid Global Accounts

## Overview

Lightspark は Grid Global Accounts に AI agent support を追加し、fiat account details と stablecoin rails をまとめた treasury surface の上で agent が口座確認や送金操作を行えるようにしている。

## User Goal

finance / ops team が stablecoin と fiat をまたぐ資金移動を、wallet 個別管理ではなく一つの operational account surface で扱いたい。

## Business Goal

Lightspark の cross-border money movement infrastructure を、agent-enabled treasury workflow の基盤として広げること。

## Category

agent-payments, wallet-ux, compliance

## Core Workflow

企業は Grid Global Accounts 上で USD / EUR の account details と stablecoin rails を持つ。operator または agent は balance を確認し、受取・支払先に応じて fiat rail か stablecoin rail を使って送金する。AI agent support により、一部の treasury action を agent workflow に組み込める。

## Pricing / Business Model

infrastructure / embedded finance 型。具体的 pricing は source 上で未確認。

## Differentiation

stablecoin wallet を単体 product として見せず、fiat account abstraction とセットで treasury workflow に埋め込んでいる点が強い。agent support も payment rail 単体ではなく operational account に付いている。

## Operational Notes

導入判断では beneficiary controls、approval flow、reconciliation export、fiat/stablecoin failure handling の確認が必要。agent がどこまで autonomous に実行できるかは source 上で限定的。

## Risks / Open Questions

- agent action の権限境界と revoke UX が未確認
- audit log と segregation of duties がどこまであるか不明
- geography ごとの fiat rail coverage が要確認

## Sources

- https://www.lightspark.com/news/lightspark/introducing-ai-agent-support-for-grid-global-accounts
