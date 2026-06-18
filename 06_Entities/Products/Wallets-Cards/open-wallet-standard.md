# Open Wallet Standard

## Overview

Open Wallet Standard は、local-first な wallet custody と policy-gated signing を複数 chain にまたがって共通化する OSS / SDK。stablecoin payments 自体の rail ではなく、`誰が何に署名できるか` を wallet 実装面で制御する。

## User Goal

agent や app に stablecoin spend を許可したいが、private key を hosted wallet に丸ごと預けずに local control を保ちたい。

## Business Goal

agent payments や multi-chain wallet automation のための共通 wallet substrate を取りに行くこと。

## Category

wallet-ux, agent-payments, compliance

## Core Workflow

developer は OWS で wallet を作成または接続し、pre-signing policy を設定する。agent や app は allowed chain / allowed operation / expiry の範囲でのみ署名を実行し、private key はローカル保持のまま扱われる。

## Pricing / Business Model

open-source project。商用モデルは source 上で未確認。

## Differentiation

wallet UX を `connect wallet` ではなく `policy before signing` として捉えている。stablecoin payment 導入時に必要な delegated spend boundary を wallet 実装に寄せている点が重要。

## Operational Notes

merchant allowlist、token allowlist、shared approval、audit export は追加設計が必要そうだが、chain allowlist、expiry、custom executable hook の方向性は practical。agent treasury や local operator wallet の実装に向く。

## Risks / Open Questions

- enterprise 向けの監査証跡と team approval をどこまで標準で持つか不明
- production hardening の実績がどこまであるか未確認
- hosted payment provider とどう役割分担するか整理が必要

## Sources

- https://openwallet.sh/
- https://docs.openwallet.sh/
- https://github.com/open-wallet-standard/core
