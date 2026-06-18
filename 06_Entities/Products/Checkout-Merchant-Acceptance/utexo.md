# Utexo

## Overview

Utexo は、Bitcoin を settlement anchor にした USDT payment infrastructure。RGB と Lightning を組み合わせ、payment operator が fixed-cost かつ private に stablecoin settlement できる API / Cloud product を提供する。

## User Goal

USDT payment を扱いたいが、gas volatility、public-chain 可視性、複数インフラ統合コストを減らしたい。

## Business Goal

stablecoin settlement を Bitcoin-native execution layer として再包装し、PSP / exchange / wallet / enterprise operator の default backend を取ること。

## Category

checkout, wallet-ux, compliance

## Core Workflow

operator は Utexo API か Cloud を統合し、USDT payment routing、liquidity、asset validation、settlement coordination を Utexo に委譲する。execution は off-chain で進み、cryptographic commitment が Bitcoin に anchor される。wallet や PSP は既存 UX を大きく変えずに instant settlement と fixed-fee model を得る。

## Pricing / Business Model

site 上では詳細 pricing 未確認。value proposition は deterministic fee model、private execution、single integration point にある。

## Differentiation

典型的な EVM stablecoin rail と違い、Bitcoin finality と Lightning execution を主役にしている。`stablecoin checkout` より `operator settlement backend` の設計に強く寄っている点が差分。

## Operational Notes

public-chain 上に payment flow を晒さないこと、fee volatility を避けること、pre-funding を減らすことを前面に出しており、target user は consumer ではなく payment operator。wallet UX も signer UI ではなく treasury / settlement predictability 側に重心がある。

## Risks / Open Questions

- USDT / Tether 依存度が高く rail diversification が弱い可能性
- off-chain execution failure 時の dispute / recovery flow が未確認
- AML / sanctions / travel rule responsibility の所在が要確認
- RGB / Lightning 採用が buyer / partner coverage をどこまで制限するか未確認

## Sources

- https://www.utexo.com/
- https://docs.utexo.com/
- https://www.x402.org/ecosystem
