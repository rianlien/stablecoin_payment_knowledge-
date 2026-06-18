# Crossmint Checkout Telegram Agent

## Overview

Crossmint Checkout Telegram Agent は、Telegram chat を入口に商品検索、wallet creation、delegation、USDC checkout までをつないだ conversational commerce demo。

## User Goal

chat interface の中で stablecoin-backed checkout を end-to-end で試したい。

## Business Goal

Crossmint の wallets、orders、delegation を chat commerce や agent checkout の参照実装として広げること。

## Category

checkout, wallet-ux, agent-payments

## Core Workflow

user は Telegram bot で商品検索し、`Buy with Crossmint` を押して web interface に遷移する。そこで wallet を作成し、delegation を有効化する。以後 bot と web interface が協調して checkout や transaction signing を進める。

## Pricing / Business Model

demo repo。収益ポイントは Crossmint の wallet、order、transaction API 利用にある。

## Differentiation

商品 discovery、wallet onboarding、delegated payment を一つの conversational flow にまとめて見せている点が強い。単なる payment widget ではなく checkout 全体の demo になっている。

## Operational Notes

Telegram Bot Token、SearchAPI.io、Crossmint staging key、ngrok を使う構成。production では catalog source、refund、order management、support tooling の補完が必要。

## Risks / Open Questions

- merchant catalog / inventory sync をどう一般化するか
- refund と failed order handling が未整理に見える
- channel 依存が強く、Telegram 外に持ち出すには追加実装が要る

## Sources

- https://github.com/Crossmint/crossmint-checkout-telegram-agent
- https://docs.crossmint.com/
