# OffPay Wallet

## Overview

OffPay Wallet は、offline QR transfer、private settlement、viewing key を備えた self-custodial stablecoin wallet。

## User Goal

ネット接続が弱い状況でも stablecoin payment を成立させつつ、必要な場面だけ transaction history を限定開示したい。

## Business Goal

OffPay が privacy-first / offline-first stablecoin wallet という明確なポジションを取ること。

## Category

wallet-ux, compliance

## Core Workflow

user は nonce account を一度セットアップし、USDC / USDT transfer を offline で署名する。受取側は QR を読み取り、後で online settlement を反映する。必要時は scoped viewing key で監査用開示を行う。

## Pricing / Business Model

private beta / waitlist 段階。詳細 pricing は未確認。

## Differentiation

wallet simplicity ではなく、offline transfer と selective disclosure を同じ surface に載せている点。

## Operational Notes

導入前に offline transfer の失敗時 UX、double-spend 防止、merchant receipt export、viewing key 権限粒度を確認したい。

## Risks / Open Questions

- private beta のため production reliability が未確認
- consumer wallet から merchant acceptance へ広がるか不明
- privacy 機能が各 jurisdiction の audit / AML 要件とどう整合するか要確認

## Sources

- https://www.offpay.app/
