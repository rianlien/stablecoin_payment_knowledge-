# Seed Finance

## Overview

Seed Finance は HackMoney 2026 で公開された reverse factoring demo。supplier invoice を buyer approval 後に USDC で即時資金化し、満期時に buyer が返済する。

## User Goal

B2B invoice payment を待たずに、supplier が working capital を早期確保したい。

## Business Goal

stablecoin payment rail を invoice financing product に変換し、supplier、buyer、liquidity provider をつなぐ新しい trade finance layer を作ること。

## Category

invoicing, compliance

## Core Workflow

supplier が invoice を出し、buyer が onchain で承認する。operator が liquidity pool から前倒し資金を供給し、supplier は即時に USDC を受け取る。buyer は満期に full amount を返済し、fee が LP yield になる。

## Pricing / Business Model

demo では invoice financing fee を 1% として説明している。想定モデルは financing fee、pool economics、operator services。

## Differentiation

invoice payment を「受け取る / 支払う」の二者問題ではなく、cash-flow transformation として product 化している点が特徴。USDC-native gas と compliance-aware chain を選んでいるのも狙いが明確。

## Operational Notes

Circle Developer-Controlled Wallets、Circle Gateway、ERC-4626 vault、operator backend を使う構成。導入時は underwriting、buyer default handling、invoice authenticity verification、legal enforceability が重要になる。

## Risks / Open Questions

- invoice fraud と double financing の防止策が未確認
- operator の審査責任と regulated boundary が未確認
- APY 前提が demo 的で、実運用の credit loss を織り込んでいない

## Sources

- https://ethglobal.com/showcase/seed-finance-c2tnd
