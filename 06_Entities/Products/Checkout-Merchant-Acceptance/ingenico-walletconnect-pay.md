# Ingenico + WalletConnect Pay

## Overview

Ingenico と WalletConnect Pay の組み合わせは、physical checkout で native stablecoin acceptance を有効化する merchant-facing solution。wallet から merchant payment provider へ直接流す設計で、crypto-linked card に寄らない。

## User Goal

店頭 POS で stablecoin 支払いを受けたいが、新しい hardware や複雑な treasury 運用は増やしたくない。

## Business Goal

acquirer / PSP / merchant に対して、既存 infrastructure を活かした in-store stablecoin acceptance を提供すること。

## Category

checkout, wallet-ux, compliance

## Core Workflow

consumer は mobile wallet から支払う。WalletConnect Pay が native stablecoin transaction を流し、merchant 側は payment provider 経由で受け取る。Ingenico 側は既存 POS infrastructure に統合する。

## Pricing / Business Model

公開情報では詳細不明。value は hardware 追加不要、merchant が digital currency balance を保持しなくてよいことにある。

## Differentiation

consumer crypto UX をそのまま店頭に持ち込むのではなく、merchant の導入負荷を抑えた acceptance model にしている点が現実的。

## Operational Notes

公式発表では、supported stablecoins、faster settlement、legacy infrastructure 依存の削減を訴求しつつ、secure、compliant、seamless であることを前提にしている。

## Risks / Open Questions

- refunds、partial capture、chargeback 相当の扱いが不明
- merchant settlement currency と statement 表示がどうなるか
- chain / wallet / region ごとの制約がどこまであるか

## Sources

- https://ingenico.com/en/newsroom/press-releases/ingenico-launches-digital-currency-solution-enabling-stablecoin-payments-0
