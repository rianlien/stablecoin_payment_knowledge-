# StablePay

## Overview

StablePay は、thirdweb Payment API を使った Venmo-like stablecoin payments demo。email-auth wallet、username 宛て送金、multi-chain token handling をまとめ、consumer-facing stablecoin app の骨格を見せる。

## User Goal

wallet address を直接やり取りせず、メールログインと username 指定で stablecoin payments を成立させたい。

## Business Goal

builder が consumer payment UX を短期間で試せる reference app を提供すること。

## Category

wallet-ux

## Core Workflow

user は email verification で wallet を作成または復元する。recipient を username で検索し、token / chain / amount を選んで payment を作成し、thirdweb Payment API で transfer を完了する。

## Pricing / Business Model

demo / example repo。収益モデルは source 上で未確認。

## Differentiation

stablecoin transfer を `address paste` 前提にせず、recipient discovery と onboarding を UI flow の中にまとめている。insufficient funds 時の payment link など、実装論点も具体的。

## Operational Notes

P2P product に進めるなら、mistaken recipient、recovery、fraud controls、off-ramp、customer support、token-list governance を足す必要がある。とはいえ onboarding と send flow の最小骨格としてはかなり実用的。

## Risks / Open Questions

- username directory の trust / impersonation 対策が未確認
- compliance-sensitive 地域での運用前提がない
- production 向け observability や case handling が未整備

## Sources

- https://github.com/thirdweb-example/stable-pay
