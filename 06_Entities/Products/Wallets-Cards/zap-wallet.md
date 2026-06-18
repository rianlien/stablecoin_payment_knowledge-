# Zap Wallet

## Overview

Zap Wallet は USDC / EURC を phone number 宛てに送れる mini-app wallet。受け取り側が既存 wallet を持っていなくても、link 経由で受領できる設計。

## User Goal

consumer や small merchant が wallet address や chain 選択を意識せずに stablecoin を送受信したい。

## Business Goal

stablecoin wallet UX を messaging / contact app に近づけ、addressless payment を product として成立させること。

## Category

wallet-ux, checkout

## Core Workflow

sender は app 上で recipient の phone number を指定し、USDC または EURC を送る。recipient は SMS / link 経由で受け取り、必要に応じて wallet onboarding を進める。

## Pricing / Business Model

showcase demo。商用モデルは未確認。

## Differentiation

wallet address を見せない recipient targeting によって、stablecoin payment を contact-based transfer へ寄せている。

## Operational Notes

本番運用では phone identity verification、SIM swap 対策、unclaimed funds 処理、KYC threshold、cash-out 導線が重要になる。

## Risks / Open Questions

- phone number identity の信頼性が弱い
- recipient onboarding friction がまだ不明
- merchant settlement や accounting export の設計が未確認

## Sources

- https://ethglobal.com/showcase/zap-wallet-va5wx
