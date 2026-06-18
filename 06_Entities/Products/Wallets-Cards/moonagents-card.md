# MoonAgents Card

## Overview

MoonAgents Card は、MoonPay が 2026-05-01 に公開した virtual Mastercard debit card。ユーザーや AI agent が self-custodial onchain stablecoin balance を使って、Mastercard 加盟店で支払いできるようにする。

## User Goal

stablecoin を off-ramp や custodial pre-load なしで、日常的な online spend や agent-driven purchase に使いたい。

## Business Goal

wallet funding、agent wallet tooling、card spend をひとつの developer / user flow にまとめ、agent economy 向け financial layer を広げること。

## Category

wallet-ux, agent-payments, compliance

## Core Workflow

ユーザーが KYC を完了し、MoonPay CLI などを通じて card を取得する。agent には delegated authority を与えられ、支払い時に onchain stablecoin balance から card transaction が実行される。

## Pricing / Business Model

カード program と onramp / wallet infrastructure の組み合わせ。カード利用、FX、関連 payment services が収益源と見られる。

## Differentiation

custodial residual balance を事前に積むのではなく、onchain balance から moment-of-transaction で spend させる点。agent 向けに programmatic access を前提化しているのも特徴。

## Operational Notes

Monavate と Mastercard を使う regulated card rail で、公式ページ上は KYC 前提。実導入時は delegated authority、spend limits、supported chains / assets、failed authorization handling の確認が必要。

## Risks / Open Questions

- revoke / freeze / audit UX の具体が未確認
- supported stablecoins と conversion 条件が未確認
- geography と card acceptance 制約の詳細が未確認

## Sources

- https://www.moonpay.com/it/newsroom/moonagents-card
- https://www.moonpay.com/agents/card
