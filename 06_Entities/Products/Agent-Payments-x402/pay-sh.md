# Pay.sh

## Overview

Pay.sh は、AI agent 向けの pay-as-you-go API directory / payment proxy。agent は account 作成、API key 発行、subscription 契約なしで API を call し、stablecoin で request ごとに支払える。

## User Goal

agent が human onboarding を挟まずに外部 API を即時利用したい。

## Business Goal

API provider に対して、signup-less な agent-native billing surface を提供し、catalog/discovery 面も握ること。

## Category

x402, agent-payments

## Core Workflow

provider は service を Pay.sh catalog に載せる。agent は catalog から service と価格を見つけ、call 時に payment を付けて実行する。決済は stablecoin で処理され、provider は pay-per-call で収益化できる。

## Pricing / Business Model

source 上では endpoint ごとの従量課金。free tier と metered endpoint が混在している。platform value は billing abstraction と discovery の両方にある。

## Differentiation

決済 gateway だけでなく catalog が前面にある。agent が「払える」だけでなく「何に払うか見つけられる」点が重要。

## Operational Notes

Google Cloud 連携を前面に出しつつ、AI/ML、maps、data、messaging など複数カテゴリの live service を持つ。provider と buyer の双方にとって request-native pricing を見せる設計。

## Risks / Open Questions

- provider onboarding / listing quality の基準が不明
- failed execution や refund の取り扱いが不明
- enterprise buyer 向けの budget / allowlist / audit UX が見えない

## Sources

- https://pay.sh/
- https://solana.com/uk/news/solana-foundation-launches-pay-sh-in-collaboration-with-google-cloud
- https://github.com/solana-foundation/pay
