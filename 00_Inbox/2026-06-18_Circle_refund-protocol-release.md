---
title: "Circle、非カストディアル・ステーブルコイン返金プロトコルの新リリースを公開（2026-06-18）"
date: 2026-06-18
source: GitHub circlefin/refund-protocol
source_url: https://github.com/circlefin/refund-protocol/releases
entity: Circle
category: stablecoin-payments
primary_category: merchant-PSP-readiness
article_published_date: 2026-06-18
underlying_event_date: 2026-06-18
primary_source_date: 2026-06-18
tags:
  - stablecoin
  - merchant-readiness
  - Circle
  - USDC
  - payment-authorization
summary: "Circle が circlefin/refund-protocol の新リリース（release-2026-06-18T213046）を公開。アービター仲裁型の非カストディアル・ステーブルコイン返金/チャージバックプロトコルで、受取側がウォレット資金の管理を維持しながら第三者アービターが紛争を仲裁する設計。ただし「アービターが早期引き出し関数を使って他ユーザーの資金を引き出せる」脆弱性が報告されており、修正が開発中とされている。"
implications: "ステーブルコイン決済における返金/チャージバック機能の欠如は加盟店採用の主要障壁のひとつ。Circle が非カストディアルな解決策を提供することで、PSP・加盟店のステーブルコイン本番採用が前進しうる。ただし現時点では未修正の脆弱性が存在し、本番投入には十分なセキュリティ審査が必要。"
importance: Medium
confidence: Medium
follow_up: "アービター脆弱性の修正完了・セキュリティ監査（Audit）の完了と公表、加盟店・PSP による本番採用事例、GENIUS Act・MiCA 下での仲裁型返金プロトコルの規制適合性確認"
---

## 概要

Circle が GitHub の `circlefin/refund-protocol` リポジトリで新リリース（release-2026-06-18T213046）を公開した。ステーブルコイン（主に USDC）取引における返金・チャージバックを非カストディアルかつ第三者仲裁型で処理するスマートコントラクトプロトコル。従来、ステーブルコイン決済は「送ったら取り戻せない（irreversibility）」という特性から加盟店採用の障壁だったが、このプロトコルは受取側の資金管理権を維持しながら紛争解決の仕組みを提供する。

## 何が起きたか

- `circlefin/refund-protocol` に 2026-06-18 付けのリリース（release-2026-06-18T213046）が公開
- 本リポジトリは計 4 リリースを持ち、今回が最新版
- プロトコル設計：送金者と受取者の間に「アービター」が仲裁者として入る 3 者モデル。受取側がウォレット管理権を保持したまま紛争解決を行える
- 目的：「ステーブルコイン決済のユーザー体験を向上させながら、受取側の資金管理権を維持する」（リポジトリの説明文より）
- **セキュリティ上の注意事項**：「早期引き出し（early withdrawal）関数の問題により、アービターが他ユーザーの資金を引き出せる」脆弱性が報告されており、修正開発中とリポジトリに明記されている

## 確認された事実

- GitHub circlefin/refund-protocol に 2026-06-18 付けリリースが存在（一次情報）
- セキュリティ notice がリポジトリに公開されている（アービターによる資金流出リスクを認識・修正中）
- プロトコルは Solidity ベースのスマートコントラクト（ブロックチェーン特定は未確認）
- Circle（circlefin organization）が公式で管理するリポジトリ

## なぜ重要か

### 決済事業者視点

- ステーブルコイン決済を導入したい PSP にとって「返金・チャージバック処理をどうするか」は未解決の重要課題。Circle が公式に非カストディアル返金プロトコルを提供することで、PSP が独自実装する負担が減る
- 仲裁モデルは既存の AML・コンプライアンスフレームワークとの統合設計が必要になる（アービターの法的地位・KYC 義務等）

### 加盟店視点

- 消費者が「ステーブルコインで払ったのに返金できない」という懸念を払拭できれば、加盟店がステーブルコイン受け入れを表明しやすくなる
- 既存のクレジットカードの chargeback と同等の保護が提供できれば、消費者保護規制（EU の Consumer Rights Directive 等）との整合性が高まる

### プロダクト視点

- AP2（Agentic Payments Protocol）や x402 のエコシステムでは「エージェントが誤って支払った」「サービスが提供されなかった」ケースの返金処理が設計課題。このプロトコルがそのインフラになりうる
- 非カストディアル設計は加盟店のステーブルコイン保有リスクを軽減する

### 規制 / リスク視点

- **現時点では脆弱性あり**（アービターが他ユーザーの資金を引き出せる）。修正完了・外部監査（Audit）完了前の本番採用は推奨できない
- MiCA（EU）・GENIUS Act（米国）下での「アービター」の法的定義・規制上の地位が明確化されていない。規制当局がアービターを PSP・VASP として分類するリスクを検討する必要がある
- 日本の資金移動業・電子マネー規制における仲裁型返金モデルの適合性も未検討

## 我々への示唆

- いま検討すべきこと:
  - この返金プロトコルの設計を確認し、自社のステーブルコイン決済システムに組み込めるかを技術的に評価する（脆弱性修正後）
  - アービターの法的地位を GENIUS Act・MiCA・日本法の各枠組みで確認する
- 後で深掘りすべきこと:
  - セキュリティ監査（Audit）完了後のリリースを待って本番採用可能性を評価
  - x402 や AP2 ペイメントフローとの統合設計（エージェント主導の返金申請フロー）
- 今は優先度が低いこと:
  - アービター選定・運用コストの詳細見積もり（本番化フェーズで検討）

## ありそうな示唆

- Circle がこのプロトコルを提供する背景には、GENIUS Act 最終規則（7/18 デッドライン）・MiCA 施行（7/1）を見据えた「ステーブルコイン決済の消費者保護要件への対応」がある可能性がある。規制当局が消費者保護の証明を求めるタイミングで、参照実装として活用できる地位を Circle が確立しようとしているとみられる

## 推測 / 監視ポイント

- アービター脆弱性の修正完了タイミングと修正後のセキュリティ監査（Audit）実施・結果公表
- Circle が自社の CPN（Circle Payments Network）や Agent Stack にこのプロトコルを統合するかどうか
- 他の stablecoin 発行体（Paxos・Fiserv FIUSD 等）が同様の返金プロトコルを提供するか

## 未解決の論点

- プロトコルが対応するブロックチェーン（Base？ Ethereum mainnet？Solana？）が未確認
- アービターの選定プロセスと KYC/AML 義務の扱いが未公開
- GENIUS Act の PPSI 定義上、アービターを担う主体がライセンスを要するかどうか

## 参考リンク

- 一次情報: [circlefin/refund-protocol releases（GitHub）](https://github.com/circlefin/refund-protocol/releases)
- 補足情報: [circlefin/refund-protocol README（GitHub）](https://github.com/circlefin/refund-protocol)

## 重要度
- Medium

## 確からしさ
- Medium（GitHub リリースで確認。対応チェーン・監査状況・外部採用事例は未確認。脆弱性は Circle が公認）
