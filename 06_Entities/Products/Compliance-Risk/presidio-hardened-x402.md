# presidio-hardened-x402

## Overview

presidio-hardened-x402 は、x402 payment request を送る前に PII redaction、spending policy、replay detection、audit logging、optional remote screening を適用する open-source security middleware。2026-06-16 時点の GitHub では `v0.5.0` として rail-agnostic screening core、`bindings/x402`、partner conformance suite を前面に出している。

## User Goal

x402 を demo のままではなく、privacy / policy / audit を含む production-like flow で試したい。

## Business Goal

x402 adoption の実運用 blocker を middleware として先回りし、agent payment stack の hardening layer として使われること。

## Category

x402, compliance, agent-payments

## Core Workflow

developer は既存の signer や x402 client の前段に `HardenedX402Client` を置く。`402 Payment Required` を受けた後、middleware が metadata を scan して PII redaction と policy check を実施し、replay guard と audit log を通してから payment header を送る。現行の訴求は `x402 hardening` だけでなく、他 rail にも移植可能な screening pipeline を OEM 的に埋め込める点にある。

## Pricing / Business Model

open-source project。PyPI package として配布され、hosted remote screening は opt-in の補助機能として使える。repo 上では semver guarantee と partner-runnable conformance suite も打ち出しており、実験 repo から reusable component へ寄せにいっている。

## Differentiation

`x402 can pay` ではなく `x402 can pay safely` を front message にしている。per-origin wallet allowlist、multi-party authorization、audit chain まで含め、merchant 導入で実際に必要になる control plane をまとめている。さらに screening core と binding layer を分けたことで、rail fragmentation に備えた reusable hardening layer として見やすくなった。

## Operational Notes

client-side middleware なので既存 stack に挟み込みやすい一方、false positive、policy tuning、audit log 保管、remote screening の data path は別途設計が必要。official x402 SDK との互換範囲や production reference も確認したい。CDP / LangChain / CrewAI quickstart はあるが、merchant-side verifier や hosted gateway への接続実績はまだ見えていない。

## Risks / Open Questions

- client-side hardening だけで十分か、server-side verifier 側にも対応が必要か
- supported wallets / signers の現実的なカバレッジが未確認
- remote screening を使う場合の data residency と contractual boundary が要確認

## Sources

- https://github.com/presidio-v/presidio-hardened-x402
- https://arxiv.org/abs/2604.11430
