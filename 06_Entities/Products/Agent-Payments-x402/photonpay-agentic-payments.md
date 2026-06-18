# PhotonPay Agentic Payments

## Overview

PhotonPay は、stablecoin-powered financial operating system を名乗る cross-border payments infra で、2026-05-14 に Mastercard と組んだ live agentic payment demo を公開した。AI agent に tokenized card を割り当て、実際の booking payment を end-to-end で完了させている。

## User Goal

AI agent に実際の支払い実行権を与えつつ、enterprise が受け入れられる認証・監査・network trust を保ちたい。

## Business Goal

stablecoin / fiat 両対応の programmable financial layer を、agentic commerce 時代の execution backbone として取りにいくこと。

## Category

agent-payments, compliance

## Core Workflow

AI agent がユーザー代理で購入先を選び、PhotonPay の programmable infrastructure 上で tokenized card payment を実行する。Mastercard Agent Pay が認証と security を提供し、PhotonPay 側が orchestration と settlement responsiveness を担う。

## Pricing / Business Model

明示 pricing は未確認。推定では enterprise / platform 向け API-driven payment infra として、account、payout、issuing、FX、settlement で収益化する。

## Differentiation

stablecoin native をうたいながら、実際の execution surface を既存 card network に接続している点が重要。agentic payment を「onchain だけで閉じない」現実路線として見やすい。

## Operational Notes

公式情報では user authorization、identity verification、data protection を transaction flow に含めている。導入時の論点は、policy engine の責任分界、agent authority revoke、dispute / chargeback handling、treasury funding path。

## Risks / Open Questions

- live demo から一般提供までの距離が不明
- stablecoin treasury との接続方式が未確認
- merchant dispute、refund、chargeback の扱いが未確認

## Sources

- https://www.photonpay.com/uk/news/article/photonpay-completes-its-first-live-agentic-payment-together-with-mastercard
