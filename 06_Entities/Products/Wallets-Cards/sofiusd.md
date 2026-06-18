# SoFiUSD

## Overview

SoFiUSD は、SoFi app 内で buy / sell / hold / convert できる U.S. national bank-issued stablecoin。2026-05-27 時点で、SoFi はこれを nearly 15 million members 向けに app rollout した。

## User Goal

crypto-native app ではなく、普段の banking app の中で regulated な stablecoin を使いたい。

## Business Goal

SoFi が stablecoin を mainstream banking UX に埋め込み、deposit、payments、cross-border mobility まで広げること。

## Category

wallet-ux, compliance

## Core Workflow

SoFi member はアプリ内で SoFiUSD を buy / sell / hold / convert できる。公式発表では、次段で tokenized deposits への変換、24/7 cross-border movement、Bullish 上場による institutional liquidity 接続まで拡張するロードマップを示している。

## Pricing / Business Model

SoFi ecosystem 内の banking / asset product。詳細 fee は source 上で未確認。

## Differentiation

stablecoin を crypto wallet ではなく banking app の中に置き、1:1 redemption、bank-grade safeguards、attestations、tokenized deposits 連携まで一つの shell にまとめている。`bank app that happens to contain a stablecoin` という packaging が本質。

## Operational Notes

payment surface の実装順序、dispute handling、tokenized deposit への切り替え UX、OCC-regulated stablecoin と app-native features の責任分界を見たい。2026-05-27 の公式文面では `pay with digital assets` を掲げる一方、当面 visible なのは buy / hold / convert 導線で、実際の merchant / remittance surface は今後の確認が必要。

## Risks / Open Questions

- current phase では payment utility より hold / convert が先行している可能性
- consumer disclosure と irreversible blockchain transaction の両立が難しい
- cross-border utility がどの jurisdiction まで開くか未確認
- tokenized deposit 変換後の reversibility と deposit insurance messaging をどう見せるかが UX 上の難所

## Sources

- https://investors.sofi.com/news/news-details/2026/SoFiUSD-Becomes-the-First-Stablecoin-Issued-by-a-US-National-Bank-to-Launch-on-a-Banking-Platform/default.aspx
