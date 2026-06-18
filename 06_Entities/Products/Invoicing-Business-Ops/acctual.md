# Acctual

## Overview

Acctual は、stablecoin invoicing を「相手に chain を選ばせない支払い体験」として再設計している invoicing / payment routing product。invoice link 上で stablecoin と fiat の複数手段を提示し、受け手は希望の wallet / bank account で受け取れる。

## User Goal

stablecoin で早く支払いを受けたいが、取引先に crypto の複雑さを押し付けたくない。

## Business Goal

cross-border invoice collection を簡単にし、payment method mismatch を routing layer で吸収すること。

## Category

invoicing, wallet-ux, compliance

## Core Workflow

user は invoice を作り、希望する受取方法を指定する。Acctual は payment link 上で複数の fiat / stablecoin option を生成し、payer は都合のよい方法で支払う。受け手には指定先へ same-day で送金し、receipt と tracking を残す。

## Pricing / Business Model

公開 blog では flexible payment options に 1% fee。invoice product と routing / conversion convenience が収益源。

## Differentiation

「USDC invoice を送れる」ではなく、「相手が stablecoin を使わなくても invoice を払える」を前面に出している。導入障壁を receiver ではなく payer 側の friction として捉えているのが強い。

## Operational Notes

公開情報では 15 通りまでの payment option 生成、wallet / bank direct payout、QuickBooks sync or manual export、funds non-custodial、USDC / USDT / DAI / PYUSD と USD / EUR support を示している。

## Risks / Open Questions

- supported geography と entity eligibility の詳細が必要
- high-volume team 向け approval / permission 管理の情報が薄い
- refund / reversal / failed payout の運用が不明

## Sources

- https://www.acctual.com/stablecoin-invoicing
- https://www.acctual.com/blog/get-paid-same-day
