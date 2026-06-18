# OwlPay Agent Wallet

## Overview

OwlPay Agent Wallet は、AI agent が user 承認の範囲で stablecoin を送受信・管理するための self-custody wallet。OwlTing の stablecoin checkout と regulated payment infrastructure の上で動く。

## User Goal

ユーザーや merchant が、AI agent に支払いを任せても custody と compliance の境界を見失わずに済むこと。

## Business Goal

OwlTing が stablecoin checkout、on/off-ramp、agent wallet を一体の regulated payment stack として位置づけること。

## Category

agent-payments, wallet-ux, checkout, compliance

## Core Workflow

ユーザーは AI assistant に OwlPay Agent Wallet を導入し、guided onboarding で wallet 生成と本人確認を完了する。以後 agent は承認された範囲で残高確認、送金、履歴確認を行い、merchant 側では OwlPay checkout rail で受け取る。

## Pricing / Business Model

wallet / payments infrastructure 型。consumer / merchant どちらで monetization するかの詳細 pricing は source 上で未確認。

## Differentiation

agent wallet 単体ではなく、state-licensed money transmission、Visa Direct funding、stablecoin checkout を含む regulated shell の一部として見せている点が practical。

## Operational Notes

導入判断では authorization scope、KYC / recovery flow、supported assistants、supported chains、merchant-side dispute / refund handling を確認したい。

## Risks / Open Questions

- agent permission の granular control がどこまであるか未確認
- self-custody recovery と support model が未確認
- cross-border recipient screening と compliance responsibility の分界が要確認

## Sources

- https://www.nasdaq.com/press-release/owlting-group-nasdaq-owls-launches-owlpay-agent-wallet-targeting-emerging-multi
- https://www.owlting.com/portal/?lang=en
