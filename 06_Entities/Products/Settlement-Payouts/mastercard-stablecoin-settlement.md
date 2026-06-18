# Mastercard stablecoin settlement

## Overview

Mastercard は 2026-06-03 に、regulated stablecoin を使う on-chain card settlement を settlement capability の新オプションとして発表した。consumer checkout ではなく issuer / acquirer の settlement timing と liquidity management を変える動き。

## User Goal

card network 上の settlement を banking hours に縛られず、より柔軟に運用する。

## Business Goal

Mastercard network を on-chain settlement 時代にも中核 infra として維持し、issuers / acquirers の liquidity need に応える。

## Category

- compliance
- checkout

## Core Workflow

1. Shopper は通常の card flow で支払う。
2. Mastercard network 上で issuer / acquirer settlement option として regulated stablecoin を使える。
3. パートナーは intraday、weekend、holiday を含む timing flexibility を得る。
4. merchant 側には既存 network protections を維持したまま settlement choice を広げる。

## Pricing / Business Model

公式発表では価格非公開。Mastercard network capability の拡張として partner に提供される。

## Differentiation

- stablecoin を consumer wallet の前面ではなく network settlement layer に置いている。
- USDC、PYUSD、USDG、USDP、RLUSD、SoFiUSD など複数 regulated stablecoin を選択肢化している。
- 既存 protections、fraud safeguards、dispute processes を維持すると明示している。

## Operational Notes

- 初期 support は ARQ、CBW Bank、Cross River、Lead Bank、Nuvei など。
- supported chains は Arbitrum、Base、Canton、Ethereum、Polygon、Solana、Tempo、XRPL。
- production volume と corridor coverage は追加確認が必要。

## Risks / Open Questions

- chargeback / reserve / adjustment が on-chain settlement とどう整合するかは未確認。
- stablecoin optionality が liquidity 改善以上の merchant value に繋がるかは partner execution 次第。
- beta 的 rollout から global default へ進むには規制差分の吸収が必要。

## Sources

- https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html
