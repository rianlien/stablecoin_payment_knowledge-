# MoonPay Headless Onramps

## Overview

MoonPay Headless Onramps は、Apple Pay、cards、Google Pay を使った one-tap crypto / stablecoin funding を、自社 UI に組み込める headless checkout surface。

## User Goal

ユーザーに friction の少ない stablecoin acquisition 導線を product 内に埋め込みたい。

## Business Goal

hosted widget 依存を減らし、enterprise app や wallet product に deeper integration させること。

## Category

checkout, wallet-ux

## Core Workflow

product team は MoonPay を一度統合し、自社 UI から Apple Pay、card、Google Pay ベースの purchase flow を呼び出す。ユーザーは one-tap で crypto / stablecoin を取得できる。

## Pricing / Business Model

公開リリースでは fee detail は不明。収益は on/off-ramp、trading、crypto payments、stablecoin infrastructure を単一 integration に束ねることで取る構造に見える。

## Differentiation

onramp を standalone widget ではなく headless checkout component として売っている。wallet funding を product-native UX に埋め込める点が大きい。

## Operational Notes

リリースでは US、EEA、100+ countries をカバーする one-tap purchases と、single integration で複数 rail を扱う点を前面に出している。

## Risks / Open Questions

- KYC / fraud review の UI 負担が headless 実装側にどれだけ返るか
- supported assets と post-purchase wallet UX の境界が見えにくい
- acquisition 後の payment / spend flow とつなげる設計が必要

## Sources

- https://www.prnewswire.com/news-releases/moonpay-launches-headless-onramps-302771903.html
