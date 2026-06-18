# AgentLevy

## Overview

AgentLevy は autonomous agent 間の商取引に対して、escrow、audit trail、rule-based settlement を提供する showcase。payment 実行そのものより transaction governance を重視している。

## User Goal

agent 同士に発注や支払いを任せたいが、後から取引根拠を追えず uncontrolled spend になることは避けたい。

## Business Goal

machine commerce 向けに payment と compliance の中間 layer を作り、agent transaction を扱える product pattern を示すこと。

## Category

agent-payments, compliance

## Core Workflow

agent が service purchase を行う際、資金は escrow 的に hold される。fulfillment や条件達成に応じて settlement が release され、同時に transaction trail が記録される。

## Pricing / Business Model

showcase demo。商用モデルは未確認。

## Differentiation

agent payment を wallet delegation や card permission ではなく、evidence trail と settlement conditions の問題として扱っている。

## Operational Notes

実務導入には dispute workflow、human override、merchant / provider identity、offchain fulfillment verification が必要。machine-to-machine commerce の governance 例としては示唆が強い。

## Risks / Open Questions

- escrow release condition の定義主体が不明
- human review step の挿入方法が未確認
- offchain service delivery とどう結びつけるか課題が残る

## Sources

- https://ethglobal.com/showcase/agentlevy-rddly
