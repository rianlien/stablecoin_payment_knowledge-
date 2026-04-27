---
title: "ERC-5564: Stealth Addresses — 受取人プライバシーのための使い捨てアドレス規格"
date: 2026-04-27
source: Ethereum EIPs
source_url: https://eips.ethereum.org/EIPS/eip-5564
entity: Ethereum コミュニティ（主導: Toni Wahrstätter, Matt Solomon, Ben DiFrancesco, Vitalik Buterin）
category: protocol
tags:
  - erc
  - protocol
  - stablecoin
  - wallet
summary: >
  送信者が受取人の公開鍵から使い捨てのステルスアドレスを非インタラクティブに生成する ERC 規格。
  受取人のみが viewing key でオンチェーンの資金を検出・回収できるため、
  第三者に受取人アドレスを紐づけられることなく送金できる。
status: draft
---

## 概要

- **プロトコル名**: ERC-5564（Stealth Addresses）
- **開発主体**: Toni Wahrstätter、Matt Solomon（a16z）、Ben DiFrancesco、Vitalik Buterin
- **対象ユースケース**: 給与支払い・匿名寄付・マルチシグ署名者匿名化・プライベート投資
- **対応チェーン / ネットワーク**: Ethereum メインネット（EVM 互換 L2 に移植可能）
- **ライセンス**: ERC（オープン標準）

---

## 何を解決するプロトコルか

### 課題

Ethereum 上での送金は受取人のウォレットアドレスがオンチェーンに公開される。
同一アドレスを使い続けると、誰がどこから資金を受け取ったかが第三者に追跡可能になり、
個人・法人を問わずプライバシーリスクが生じる。

- 受取人が公開アドレスを共有するたびに、全送金履歴が紐づいてしまう
- 都度新アドレスを発行するには受取人・送信者の事前調整が必要で実用的でない
- ENS 等の人間が読めるアドレスは利便性と引き換えに追跡容易性を高める

### アプローチ

**非インタラクティブなステルスアドレス生成**により、受取人の事前関与なしに、
送信者が使い捨ての受取専用アドレスを都度生成する。

1. 受取人は `spending public key`（支出鍵）と `viewing public key`（閲覧鍵）を公開登録
2. 送信者はエフェメラル鍵ペアを生成し、受取人の閲覧公開鍵との ECDH で共有秘密を算出
3. 共有秘密から 1 回限りのステルスアドレスを導出して送金
4. オンチェーンにはエフェメラル公開鍵と 1 バイトの "view tag" だけを記録
5. 受取人は viewing private key で全エフェメラル公開鍵を走査し、view tag が一致するものだけ復号 → 約 1/6 の計算コストで自分宛の資金を特定
6. spending private key でのみ資金を引き出せる

---

## 技術仕様

### アーキテクチャ

- シングルトンコントラクトをチェーン固定アドレスにデプロイ（ERC-4788 方式）
- 送金時に `Announcement` イベントをエミット（エフェメラル公開鍵・view tag・メタデータを含む）
- 受取人は Announcement イベントを走査して自分宛の送金を検出する

### 主要コンポーネント

| コンポーネント | 説明 |
|-------------|------|
| `ERC5564Announcer` | アナウンスメントを受け付けるシングルトンコントラクト |
| Spending Public Key | 資金の引き出しに必要な公開鍵（33バイト、圧縮） |
| Viewing Public Key | ステルスアドレス検出に使う公開鍵（33バイト、圧縮） |
| Ephemeral Public Key | 送信者が都度生成する使い捨て公開鍵 |
| View Tag | 受取人走査コストを削減する 1 バイトのヒント値 |

### API / インターフェース

```solidity
interface IERC5564Announcer {
    event Announcement(
        uint256 indexed schemeId,
        address indexed stealthAddress,
        address indexed caller,
        bytes ephemeralPubKey,
        bytes metadata
    );

    function announce(
        uint256 schemeId,
        address stealthAddress,
        bytes memory ephemeralPubKey,
        bytes memory metadata
    ) external;
}
```

- `schemeId` で暗号方式を指定（最初の実装は SECP256k1）
- ERC-6538 と組み合わせてステルスメタアドレスの on-chain 登録が可能

### 対応通貨・アセット

- ETH・ERC-20・ERC-721・ERC-1155 すべてに適用可能
- USDC・USDT・DAI 等のステーブルコインも対象

---

## エコシステム・採用状況

### 主要参加者・パートナー

- Ethereum Foundation（Vitalik Buterin がコアに関与）
- a16z（Matt Solomon）
- Umbra Protocol（既存実装のインスピレーション元）

### 実採用事例

- Umbra Protocol が先行実装として機能しているが ERC-5564 準拠ではない
- ERC-5564 準拠の本番実装は 2026 年現在まだ限定的
- ウォレット側（MetaMask 等）の viewing key サポートが普及の鍵

### 競合・類似プロトコル

| プロトコル | 違い |
|-----------|------|
| Tornado Cash | 送受信双方のリンクを切断するが、規制リスクが高く OFAC 制裁済み |
| EIP-7503 | バーン→ミント方式で送受信リンクを切断するが受取人に特殊アドレス不要 |
| EIP-8182 | ベースレイヤー埋め込みで送受信の完全プライバシーを実現（より強力） |
| Aztec Network | ZK rollup ベースのプライバシーレイヤー。別チェーン扱い |

---

## 決済事業者・PSP としての評価

### 統合のしやすさ

- 送信者・受取人双方がウォレットレベルでの対応が必要
- ERC-6538 でのメタアドレス登録が前提となるため、エンドユーザーのオンボーディングコストが高い
- PSP がステルスアドレスへの送金を代行する仕組みは検討可能

### コンプライアンス対応

- **送信者アドレスはオンチェーンに公開されるため KYC は送信者側で実施可能**
- 受取人が特定できないため、AML/KYT ツールによる受取人側のスクリーニングは困難
- 規制当局が「受取人の匿名化」をどう位置づけるかは不明確（Tornado Cash との差別化が重要）
- view key を規制当局に開示することで選択的透明性は提供できる

### スケーラビリティ・コスト

- 受取人がイベントを走査するコストは view tag で約 1/6 に削減済み
- それでも多数の未確認アナウンスメントが蓄積すると走査コストが増大
- L2 展開でガスコストは大幅低減可能

### リスク・懸念点

- ウォレット未対応が最大の普及障壁
- 受取人プライバシーのみで送信者プライバシーはカバーしない
- 規制上の位置づけが各国で未確定

---

## 我々への示唆

- **いま検討すべきこと**:
  - ERC-5564 対応ウォレットの動向把握（MetaMask・Coinbase Wallet 等がいつ対応するか）
  - 給与・経費支払いへの応用可能性の調査（法人が従業員の受取プライバシーを保護したい需要）
- **後で深掘りすべきこと**:
  - ERC-6538 と組み合わせたフル実装の技術検証
  - 規制当局との対話：viewing key による選択的透明性がコンプライアンス要件を満たすか
- **今は優先度が低いこと**:
  - 自社プロダクトへの直接実装（ウォレットエコシステムの成熟を待つ）

---

## 未解決の論点

- 規制当局が受取人匿名化をマネーロンダリング幇助と見なすリスクはどの程度か
- ウォレット対応が進まない場合、PSP が「代理ステルスアドレス管理」を提供できるか
- view tag のビット幅（現行 1 バイト）は将来的に拡張が必要か

---

## 参考リンク

- 公式ドキュメント: https://eips.ethereum.org/EIPS/eip-5564
- 仕様書 / GitHub: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-5564.md
- 補足情報: https://www.quicknode.com/guides/ethereum-development/wallets/how-to-use-stealth-addresses-on-ethereum-eip-5564
- 関連規格: [[ERC-6538]] （ステルスメタアドレス登録）、[[EIP-8182_Private-ETH-ERC20-Transfers]]

---

## 重要度

Medium

## 確からしさ

High
