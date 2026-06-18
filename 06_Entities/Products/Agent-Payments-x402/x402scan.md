# x402scan

## Overview

x402scan は、x402 server と resource を発見し、transaction volume や facilitator 情報を見ながらアクセスできる x402 ecosystem explorer。単なる protocol repo ではなく、discovery と trust を担う operational surface になっている。

## User Goal

x402 で何が買えるのか、どの server が生きているのか、どの facilitator を使っているのかを素早く把握したい。

## Business Goal

x402 ecosystem の discovery layer を握り、buyers と sellers の探索コストを下げながら ecosystem 標準に近い位置を取ること。

## Category

x402, agent-payments

## Core Workflow

operator は x402 schema を返す URL を登録する。x402scan 側は resource を自動追加し、buyer は explorer 上で resource と volume を確認し、embedded wallet からアクセスできる。

## Pricing / Business Model

公開 source では明示 pricing なし。現時点では ecosystem index と trust surface の確立が主眼に見える。

## Differentiation

protocol 自体ではなく discovery を product 化している点が重要。x402 では seller onboarding 以上に buyer trust と resource findability が adoption の制約になっており、そこに直接答えている。

## Operational Notes

repo README では x402 server、transaction volumes、embedded wallet access を明示。facilitator config と discovery document guide も持ち、単なる一覧ではなく ecosystem metadata hub として作られている。

## Risks / Open Questions

- volume metrics の品質保証がどこまであるか
- spammy resource や low-quality server をどう扱うか
- enterprise buyer 向けに allowlist / audit export を持つのか

## Sources

- https://github.com/Merit-Systems/x402scan
