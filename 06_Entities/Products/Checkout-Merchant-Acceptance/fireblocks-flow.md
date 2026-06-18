# Fireblocks Flow

## Overview

Fireblocks Flow は、PSP と fintech 向けの stablecoin acceptance infrastructure。consumer が持つ wallet / token / chain の多様性を、merchant 側では既存 checkout と reconciliation surface の延長で扱えるようにする。

## User Goal

stablecoin checkout を追加したいが、wallet coverage、conversion、settlement、台帳照合を個別に組み合わせたくない。

## Business Goal

stablecoin acceptance を PSP 向けの導入しやすい infra product にし、Fireblocks の custody / settlement / compliance 面を merchant acquiring に拡張すること。

## Category

checkout, compliance

## Core Workflow

PSP / fintech は Flow を checkout または deposit flow に統合する。payer は既存の external wallet や exchange balance から支払い、Flow が stablecoin acceptance、必要な conversion、settlement、reconciliation をまとめて処理する。

## Pricing / Business Model

enterprise infrastructure 型。公開 source では料金詳細は未確認。

## Differentiation

`crypto checkout widget` ではなく、PSP が既存 merchant stack に stablecoin を後付けするための infrastructure として設計されている点が強い。wallet coverage と reconciliation を同じ product surface に乗せている。

## Operational Notes

導入前に確認したいのは、refund / dispute handling、merchant settlement asset の選択肢、OTL compatibility の実効性、台帳エクスポート粒度、supported geographies。

## Risks / Open Questions

- OTL compatibility が launch partner 外でも実運用上の接続簡略化につながるか未確認
- merchant-facing reporting と accounting handoff の粒度が未確認
- liquidity / conversion / FX responsibility boundary がどこまで Fireblocks 側にあるか不明

## Sources

- https://www.prnewswire.com/news-releases/fireblocks-launches-flow-stablecoin-acceptance-for-psps-and-fintechs-302788865.html
