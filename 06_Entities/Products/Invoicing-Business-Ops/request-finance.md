# Request Finance

## Overview

Request Finance は、stablecoin / crypto / fiat を使った請求、支払い、会計、経費管理をまとめる finance operations product。2026-03 以降は USDC-funded virtual cards と regulated-service unlock を前面に出し、invoice だけでなく spend management まで拡張している。

## User Goal

stablecoin treasury を持つ企業が、請求から支払い、記録、承認までを実務として回したい。

## Business Goal

単発送金ツールではなく、stablecoin-native finance stack として経理運用の中核を取ること。

## Category

invoicing, compliance, wallet-ux

## Core Workflow

請求書発行、bill intake、recipient verification、stablecoin or fiat payment execution、reconciliation、accounting export を一連で回す。加えて verified business は card account に supported stablecoin を入れ、virtual card を発行して支出管理まで同じ product 内で回せる。

## Pricing / Business Model

subscription 型。上位機能として crypto-to-fiat、cards、advanced controls、API を提供する。

## Differentiation

請求、承認、送金、カード、会計連携を一続きの finance workflow として扱う点。stablecoin payments を「finance ops」に落としている。

## Operational Notes

invoice payment detection、double payment protection、approval policy、test payments など、実務運用で必要な細部が強い。2026-03 以降の docs では、regulated service は verification 前提で、cards は USDC 1:1 top-up、custom spending limits、freeze / cancel、unified activity view を打ち出している。card balance は Request が custody せず、Kulipa と Privy を含む regulated partner stack 上で保持される。

## Risks / Open Questions

- ERP / accounting integration の深さ要確認
- entity / jurisdiction ごとの利用可能機能差分要確認
- cards の発行地域、card partner boundary、support responsibility 要確認

## Sources

- https://www.request.finance/
- https://www.request.finance/pricing
- https://help.request.finance/en/articles/12866642-why-should-i-verify-my-account-with-request-finance-kyb-c
- https://help.request.finance/en/articles/12888867-cards-overview
- https://help.request.finance/en/articles/13513399-what-is-the-card-account
