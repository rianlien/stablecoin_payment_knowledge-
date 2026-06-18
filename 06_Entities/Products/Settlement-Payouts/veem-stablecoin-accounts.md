# Veem Stablecoin Accounts

## Overview

Veem は 2026-04-22 に、Bridge を基盤にした stablecoin accounts and payments を launch 予定として発表した。platform や business が stablecoin を accept、hold、move できる account layer を既存 payment experience に埋め込める。

## User Goal

cross-border business payments を、bank-only flow ではなく stablecoin account を含む programmable treasury workflow として扱いたい。

## Business Goal

Veem の既存 B2B payments network に stablecoin account issuance と programmable movement を載せ、platform-facing embedded finance を強化すること。

## Category

wallet-ux, compliance, invoicing

## Core Workflow

business や platform は product 内で stablecoin account を提供し、funds の受取・保有・送金を行う。Veem は on-ramp / off-ramp と fiat/stablecoin movement を統一し、USDV を closed-loop digital dollar として使う。

## Pricing / Business Model

既存の B2B payments / embedded finance business に stablecoin account 機能を追加する構造。account issuance、payments、FX、platform integration が収益源と見られる。

## Differentiation

stablecoin を単発送金ではなく「account」として product に埋め込む点。platform が自社 UX のまま stablecoin workflow を持てる設計が特徴。

## Operational Notes

Bridge Open Issuance で USDV を発行し、Veem network の中で programmable movement を支える。導入時は closed-loop の外への interoperability、custody、reversal、jurisdiction coverage の確認が必要。

## Risks / Open Questions

- general availability と対象市場が未確認
- USDV の network 外移動や redemption 条件が未確認
- compliance review、beneficiary screening、fund safeguarding の実装境界が未確認

## Sources

- https://www.veem.com/newsroom/veem-to-launch-stablecoin-accounts-and-payments-for-global-platforms-and-businesses-powered-by-bridge/
