# PPRO + Coinbase stablecoin payments

## Overview

PPRO + Coinbase stablecoin payments は、PPRO の merchant / PSP integration に stablecoin acceptance を差し込み、merchant が既存 dashboard の中で stablecoin payment option を有効化できる joint offering。

## User Goal

merchant や PSP が、自前の crypto processing team を持たずに stablecoin acceptance を既存 payments stack に追加したい。

## Business Goal

stablecoin payments を standalone crypto product ではなく、PSP の通常メニューとして流通させること。

## Category

checkout

## Core Workflow

PSP は PPRO integration から stablecoin payment method を有効化する。consumer は対応 wallet から支払い、merchant は既存 dashboard と settlement flow の延長で stablecoin payment を受け付ける。

## Pricing / Business Model

PPRO の payment method extension 型。詳細 pricing は source 上で未確認。

## Differentiation

merchant に新しい console や運用面を覚えさせるのではなく、`current PSP surface に stablecoin を追加する` ことを前面に出している。導入ハードルを wallet UX ではなく payment ops integration で下げている。

## Operational Notes

PPRO docs では stablecoin flow が standardized `REDIRECT` pattern として記述されている。導入判断では refund / void / capture、merchant settlement currency、webhook payload、regional rollout 条件の確認が必要。

## Risks / Open Questions

- stablecoin acceptance がどの地域・merchant category に適用できるか未確認
- buyer support / failed payment support を誰が持つか不明
- merchant の accounting artifact が card / APM と同じ粒度で揃うか未確認

## Sources

- https://www.coinbase.com/fr-ca/developer-platform/discover/launches/ppro
- https://developerhub.ppro.com/global-api/docs/stablecoins
- https://www.ppro.com/news/ppro-and-coinbase-announce-strategic-collaboration-to-bring-stablecoin-payments-to-merchants/
