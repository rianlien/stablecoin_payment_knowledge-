---
title: "EIP-7503: Zero-Knowledge Wormholes — バーン→ZK証明→ミントによる送受信リンク切断"
date: 2026-04-27
source: Ethereum EIPs / Ethereum Magicians
source_url: https://eips.ethereum.org/EIPS/eip-7503
entity: Keyvan Kambakhsh, Hamid Bateni, Amir Kahoori（Nobitex Labs, 0xwormhole）
category: protocol
tags:
  - erc
  - protocol
  - stablecoin
  - kyt
summary: >
  ETH を特定のバーンアドレスに送付し、ZK 証明で「バーン事実を知っている」ことを証明しながら
  どのアドレスがバーンしたかを秘匿する。プロトコルが等価額の ETH を指定の新アドレスにミントし、
  送受信間のオンチェーンリンクを切断するコア変更型プライバシー提案。
status: draft
---

## 概要

- **プロトコル名**: EIP-7503（Zero-Knowledge Wormholes / Private Proof of Burn, PPoB）
- **開発主体**: Keyvan Kambakhsh、Hamid Bateni、Amir Kahoori（Nobitex Labs・0xwormhole チーム）
- **対象ユースケース**: プロトコルネイティブな送受信匿名化、ステーブルコインプライバシー
- **対応チェーン / ネットワーク**: Ethereum メインネット（コア変更が必要）
- **ライセンス**: ERC（オープン標準）

---

## 何を解決するプロトコルか

### 課題

Tornado Cash のようなアプリレイヤーのミキサーは：

- スマートコントラクトへの資金流入が可視であり「Tornado を使った」という事実が追跡される
- OFAC 制裁（2022年）で実質使用不可となった
- プロバイダーが特定のコントラクトに接続するだけで「疑わしい行動」と見なされるリスクがある

ERC-5564 は受取人プライバシーは保護するが、送受信のリンクは依然可視。
コア変更なしでは「どのウォレットが資金を動かしたか」を隠すことが根本的に困難。

### アプローチ

**「バーンアドレス」を利用した plausible deniability（もっともらしい否定可能性）**：

- バーンアドレスへの送金は Ethereum 上で日常的に発生しており、目立たない
- ZK 証明により「自分がバーンした」事実を証明しつつ、どのアドレスかを秘匿
- プライバシープールに属する全ての「アウトゴーイングゼロトランザクションアドレス」がデフォルトのアノニミティセットに含まれる

---

## 技術仕様

### アーキテクチャ

3 ステップフロー：**Deposit → ZK Proof → Remint**

```
1. Deposit（デポジット）
   アドレス = sha256(MAGIC_ADDRESS + secret)[12:]
   → 通常の ETH 送金と見分けがつかない

2. ZK Proof 生成（引き出し）
   - バーンアドレスの秘密 (secret) を知っていることを証明
   - プライバシープールへの参加（指定されたデポジットリストに含まれること）を証明
   - nullifier を記録してダブルスペンドを防止

3. Remint（再ミント）
   - プロトコルが等価額の ETH を指定アドレスにミント
   - 元のバーンアドレスと新アドレスの間にオンチェーンリンクなし
```

### 主要コンポーネント

| コンポーネント | 説明 |
|-------------|------|
| Magic Burn Address | `sha256(MAGIC_ADDRESS + secret)[12:]` で生成するバーンアドレス |
| Privacy Pool | 指定デポジットリスト。参加者がコンプライアンス上の属性を証明できる |
| Nullifier Set | ダブルスペンド防止のオンチェーン記録 |
| Proof of Work | スパム防止のための計算コスト |
| Deposit Limit | 1 アドレスあたりのバーン上限（セキュリティ） |

### API / インターフェース

- 新しい EIP-2718 トランザクションタイプとして実装
- ERC-20 トークン発行者が `mint` 関数を ZK 証明検証に対応させることでステーブルコインにも適用可能

### 対応通貨・アセット

- ネイティブは ETH のみ
- ERC-20（ステーブルコイン含む）は発行者が独自に対応する必要がある
- USDC・USDT 等の主要ステーブルコイン発行者の対応が課題

---

## エコシステム・採用状況

### 主要参加者・パートナー

- Nobitex Labs（イラン最大の暗号資産取引所）が主導
- 0xwormhole チームが技術開発
- Ethereum Magicians フォーラムでコミュニティ議論が進行

### 実採用事例

- **Stagnant 状態**：コアプロトコル変更（ハードフォーク必要）のためコンセンサス形成が困難
- 実本番デプロイはゼロ
- アイデアとして Privacy Pool（Vitalik Buterin 提案）と思想的に近い

### 競合・類似プロトコル

| プロトコル | 違い |
|-----------|------|
| Tornado Cash | アプリ層ミキサー。使用事実がオンチェーンで追跡可能・OFAC 制裁済み |
| ERC-5564 | 受取人プライバシーのみ。コア変更不要 |
| EIP-8182 | ベースレイヤー埋め込みのシールドプール。より包括的 |
| Aztec Network | ZK rollup。Ethereum とは別の実行環境 |

---

## 決済事業者・PSP としての評価

### 統合のしやすさ

- **コア変更（ハードフォーク）が必要**のため、PSP が独自に対応することは不可能
- Ethereum コミュニティのコンセンサスが得られなければ実装されない
- Stagnant 状態のため、現時点での実装計画はなし

### コンプライアンス対応

- Privacy Pool 機構により、参加者が「制裁対象でないこと」を ZK 証明できる設計（Vitalik Buterin の Privacy Pools 論文と整合）
- 送金額はバーンアドレスへの送金として**オンチェーンに公開**される（金額プライバシーなし）
- KYT ツールでバーンアドレスへの送金を追跡は可能だが、プライバシープール内での紐づけはできない
- **規制リスク**: Tornado Cash と同様の「制裁対象サービス」として当局が見なす可能性がある

### スケーラビリティ・コスト

- ZK 証明生成はユーザー側の計算コストが高い（数秒〜数十秒）
- バーンアドレスの蓄積でアノニミティセットが拡大し、プライバシー強度は向上
- PoW 要件がスパム防止として機能するが UX を損なう

### リスク・懸念点

- **Stagnant**：Ethereum コア開発者からの積極的支持がなく、実現見通しが不透明
- 金額プライバシーがない（バーン額がオンチェーンで可視）
- 規制当局による Tornado Cash 的な扱いリスク
- OFAC 制裁懸念（Nobitex が主導しているため地政学リスクも）

---

## 我々への示唆

- **いま検討すべきこと**:
  - Privacy Pools 概念（Vitalik 提案）との関係を把握し、今後の Ethereum ロードマップ上でのプライバシー方針を理解する
  - KYT ベンダー（Chainalysis 等）が ZK Proof of Burn をどう扱うか調査
- **後で深掘りすべきこと**:
  - Stagnant から復活する可能性があるか Ethereum Magicians の議論を定期モニタリング
  - ステーブルコイン発行者（Circle・Tether）が同様のバーン→ミント機構を採用する可能性
- **今は優先度が低いこと**:
  - 実装・統合の技術検討（Stagnant のため時期尚早）

---

## 未解決の論点

- Privacy Pool の「許可リスト」をだれが管理するか（中央集権化リスク）
- Ethereum コア開発者がプライバシーをプロトコルレイヤーに埋め込む意思があるか
- EIP-8182 と重複する提案であり、後者が採択されれば EIP-7503 の存在意義は薄れる
- Nobitex Labs（イラン企業）主導であることが欧米規制当局の心証に影響するか

---

## 参考リンク

- 公式ドキュメント: https://eips.ethereum.org/EIPS/eip-7503
- Ethereum Magicians: https://ethereum-magicians.org/t/eip-7503-zero-knowledge-wormholes-private-proof-of-burn-ppob/15456
- 補足解説: https://hackernoon.com/eip-7503-zero-knowledge-wormholes-for-private-ethereum-transactions
- 関連提案: [[ERC-5564_Stealth-Addresses]]、[[EIP-8182_Private-ETH-ERC20-Transfers]]

---

## 重要度

Medium

## 確からしさ

Medium
