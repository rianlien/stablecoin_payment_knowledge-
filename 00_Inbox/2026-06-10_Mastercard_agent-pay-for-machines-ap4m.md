---
title: "Mastercard、AI エージェント向け機械間決済プロトコル「Agent Pay for Machines（AP4M）」を正式ローンチ——35社超のパートナーと共にカード・口座・ステーブルコイン対応"
date: 2026-06-10
source: "Mastercard / The Block / The Defiant / CoinDesk / CryptoBriefing"
source_url: "https://www.theblock.co/amp/post/404288/mastercard-agent-pay-machines-support-autonomous-ai-transactions-stablecoins"
entity: Mastercard
category: agentic-commerce / machine-payments
primary_category: agentic-commerce
article_published_date: 2026-06-10
underlying_event_date: 2026-06-10
primary_source_date: 2026-06-10
tags:
  - agentic-commerce
  - machine-payments
  - stablecoin-payments
  - agent-identity
  - multi-rail
summary: "Mastercard が 2026-06-10、AI エージェント・機械間の自律決済を支援するオープンプロトコル「Agent Pay for Machines（AP4M）」を正式ローンチ。Aave Labs・Adyen・Alchemy・Anchorage Digital・Ant International・Checkout.com・Cloudflare・Coinbase・Coinflow・Crossmint・Getnet by Santander・Global Payments・MoonPay・OKX・Polygon・Rain・Ripple・Skyfire・Solana Foundation・Stripe・t54 Labs・Tempo・Turnkey・Utila など 35 社超が launch partner として参加。カード・銀行口座・ステーブルコイン（USDC を中心に RLUSD も対応）の複数レールに対応し、エージェントごとに「Verifiable Intent」（支出上限・認可ルール）をパブリックブロックチェーン（Polygon・Solana・Base）に記録して誰でも検証できる設計。Mastercard が最終決済を保証。"
implications: "TradFi（Mastercard 決済保証・Stripe・Adyen・Global Payments）と DeFi/crypto-native（Coinbase・OKX・Solana Foundation・Polygon・Ripple/RLUSD・Aave）が一つのエージェント決済プロトコルに結集した。Verifiable Intent のオンチェーン公開は、x402・AP2・MPP が個別に解決しようとしていた「エージェント認可の検証可能性」問題を Mastercard が業界標準化する可能性を示す。既存 PSP（Stripe・Adyen）の AP4M 参加は、エージェント決済がレガシー決済インフラへの代替ではなく統合として進むことを示唆する。"
importance: High
confidence: High
follow_up: "Mastercard 決済保証の具体的条件・責任範囲・チャージバック適用、USDC/RLUSD 以外のステーブルコインへの対応拡張、x402/AP2 との相互運用性の正式発表、GENIUS Act 準拠設計の詳細（PPSI 要件との整合）、ブロックチェーン上への具体的な記録内容の一次情報確認、ユーザー秘密鍵の保管場所のリファレンス実装確認"
---

## 概要

Mastercard が 2026 年 6 月 10 日、AI エージェントおよびソフトウェアシステムが人間の介入なしに相互決済できる「Agent Pay for Machines（AP4M）」を正式ローンチ。カード・銀行口座・ステーブルコインを統合したマルチレールプロトコルで、Mastercard がエンドポイント間の決済を保証する。35 社超の launch partner を擁し、TradFi・PSP・crypto-native 企業が横断的に参加する業界初の大型エージェント決済コンソーシアムとなった。

## 何が起きたか

- **AP4M の概要**：
  - AI エージェント・機械間の自律決済を支援するオープンプロトコル
  - ユースケース：マイクロペイメント（0.01 セント以下）から大規模 B2B 取引まで対応
  - レール：カード（Mastercard ネットワーク）・銀行口座・ステーブルコイン（USDC 中心、RLUSD も対応）
  - 設計：オフチェーン認証情報（速度優先）+ オンチェーン認可記録（検証可能性）のハイブリッド

- **Verifiable Intent（検証可能な意図）**：
  - 各エージェントに支出上限・認可ルールを定義した「Verifiable Intent」を割り当て
  - 認可情報をパブリックブロックチェーン（Polygon・Solana・Base）に記録
  - 誰でもチェーンを参照することでエージェントが人間が認可したスコープ内で動いているかを確認可能
  - 中央集権的な Mastercard データベースへの依存を排除

- **Launch Partner（35 社超）**：
  - **PSP / Acquirer**：Adyen、Checkout.com、Getnet by Santander、Global Payments、Stripe
  - **Crypto-native**：Aave Labs、Alchemy、Anchorage Digital、Coinbase、Coinflow、Crossmint、MoonPay、OKX、Polygon、Rain、Ripple（RLUSD / XRPL）、Skyfire、Solana Foundation、t54 Labs
  - **Infrastructure**：Cloudflare、Basis Theory、Turnkey、Utila
  - **Payments-adjacent**：Ant International、BVNK、Catena、Lovable、Mastercard Merchant Cloud、Nevermined、PayOS、Sapiom、Tempo

- **決済確定**：Mastercard がすべての AP4M 取引の最終決済を保証。チェーン上の認可スマートコントラクトを参照しながら、実行はオフチェーン認証情報ベースで行う

- **今後の計画**：2026 年内にさらに多くのブロックチェーンへの対応を拡大予定

## 確認された事実

- 発表日：2026-06-10
- 参加パートナー数：35 社超（プレスリリース確認）
- 対応チェーン（Verifiable Intent 記録用）：Polygon・Solana・Base
- 対応ステーブルコイン：USDC（Base・Polygon・Arbitrum・Solana）、RLUSD（XRPL 経由、Ripple パートナーシップ）
- 決済レール：カード・銀行口座・ステーブルコイン（マルチレール）
- 出典：Mastercard プレスリリース・The Block・The Defiant・CoinDesk・CryptoBriefing 等複数メディアが同日報道

## なぜ重要か

### 決済事業者視点

- Stripe・Adyen・Global Payments が「エージェント決済の標準インフラ」として AP4M に参加したことで、既存 PSP のエージェント決済対応が「API 追加」ではなく「Mastercard 保証のマルチレール統合」として確立される
- Mastercard の決済保証は、x402 や AP2 にはない「決済リスクのファーストパーティ引き受け」機能。これは PSP が加盟店にエージェント決済を提案する際のセールスポイントになる

### 加盟店視点

- 加盟店は「エージェント決済 = チャージバック・詐欺リスクが高い新規チャネル」という懸念なく、AP4M を通じて AI エージェントからの支払いを受け入れられる
- Mastercard 保証とオンチェーン認可検証により、「エージェントが認可された範囲内でのみ支払う」ことが技術的に保証される

### プロダクト視点

- Verifiable Intent の「オンチェーン公開認可」設計は、AP2 の W3C Verifiable Credentials・x402 のセッションキー（ERC-7715）と共存可能か、またはいずれかを代替するかが重要な設計判断点
- Tempo（MPP）が AP4M のパートナーに入ったことで、MPP と AP4M の相互運用性または統合が期待できる。Rain（ステーブルコインカード）と Crossmint の参加もエコシステムの厚みを示す

### 規制 / リスク視点

- Verifiable Intent のオンチェーン記録は、GENIUS Act の AML/CFT 要件（トランザクションモニタリング）との整合性が高い可能性がある——認可記録が公的に検証可能であれば、規制当局が要求する「エージェントの行動追跡性」を技術的に実現できる
- ただし、GENIUS Act のマイクロペイメント de minimis 免除（AML 閾値）の扱いと Mastercard の決済保証責任の交差点が規制上の未解決事項として残る

## 我々への示唆

- いま検討すべきこと:
  - 自社プロダクトが採用している決済レール（x402・AP2・MPP）と AP4M の相互運用性を評価する。特に Tempo が AP4M に参加した事実から、MPP ↔ AP4M の統合パスが存在する可能性を確認する
  - AP4M の Verifiable Intent 仕様が公開され次第、自社エージェントの認可設計（支出上限・許可カテゴリ）の移行コストを評価する
- 後で深掘りすべきこと:
  - Verifiable Intent の技術仕様（どのスマートコントラクト標準を使っているか）——AP2 の W3C VC・x402 の ERC-7715 との互換性が設計の分岐点になる
  - Mastercard の決済保証がチャージバック・詐欺補填にどこまで及ぶか——これが加盟店採用の最大の差別化要因になりうる
  - GENIUS Act 準拠設計の詳細（PPSI として認定されたステーブルコインのみ使うのか、あるいはラッピング設計があるのか）
- 今は優先度が低いこと:
  - AP4M 外のパートナー（Aave Labs 等 DeFi プロトコル）が実際にどの決済ユースケースに参加するか（現時点では技術的詳細不明）

## ありそうな示唆

- AP4M・x402・AP2・MPP の「プロトコル競争」は、今後の Mastercard の動向次第で「AP4M が標準レイヤー、x402 が支払いレール、AP2 が認可設計」という役割分担に収束する可能性がある
- 35 社超のパートナーのうち、既存 PSP（Stripe・Adyen・Global Payments）が参加したことで、AP4M は「決済業界の事実上の標準」に向けた最初のステップになりうる

## 推測 / 監視ポイント

- x402 Foundation との関係：t54 Labs が AP4M パートナーかつ x402 の XRPL 対応貢献者であることから、両者は競合ではなく補完関係として設計されている可能性が高い
- AllUnity（SEK ステーブルコイン）・Circle（USDC）・Paxos（USDP）等が AP4M の次波パートナーとして参加するかどうか
- AP4M の「GENIUS Act 準拠 PPSI ステーブルコインのみ対応」か「あらゆるステーブルコイン対応」かの設計詳細——前者であれば GENIUS Act 施行後の採用が加速する

## Verifiable Intent 技術詳細

> 公開仕様書（[verifiableintent.dev](https://verifiableintent.dev/spec/credential-format/)）および [GitHub リポジトリ](https://github.com/agent-intent/verifiable-intent/) に基づく。FIDO Alliance・EMVCo・IETF・W3C の標準仕様を組み合わせた SD-JWT ベースの設計。

### 全体構造：3層の署名チェーン（Delegation Chain）

```
L1（銀行が署名）
 ↓  sd_hash = SHA-256(L1 JWT) を L2 に埋め込む
L2（ユーザーが署名）
 ↓  sd_hash = SHA-256(L2 JWT) を L3 に埋め込む
L3（エージェントが署名）
```

各層が前層のハッシュを含むため、チェーンを辿ることで「この取引がどの人間の承認に基づくか」が一意に証明される。偽造するには銀行またはユーザーの秘密鍵を破るか、SHA-256 衝突を起こす必要がある。

---

### 各層の詳細

#### L1：発行銀行が署名（AP4M 口座登録時に一度発行）

| 項目 | 内容 |
|------|------|
| タイミング | AP4M 登録時。ユーザー操作のタイミングではない |
| 署名者 | 発行銀行（銀行の秘密鍵） |
| 常に可視のフィールド | `iss`, `sub`, `iat`, `exp`, `vct`, `cnf`（ユーザーの公開鍵）, `pan_last_four`, `scheme` |
| 選択的開示フィールド | `email` 等の身元情報（SD-JWT） |
| 有効期間 | 最大 **1年** |
| 役割 | 「このユーザーはこのカードを持つ本人」という CA 的な証明 |

`cnf.jwk` にユーザーの公開鍵が埋め込まれることが後続レイヤー検証の起点になる。

#### L2：ユーザーが署名（委任設定時）

| 項目 | 内容 |
|------|------|
| タイミング | ユーザーがバンキングアプリで委任設定した瞬間 |
| 署名者 | ユーザー（L1 の `cnf.jwk` に対応する秘密鍵） |
| 含まれる情報 | 制約パラメータ一式・エージェントの公開鍵（`cnf.jwk`）・`sd_hash`（L1 へのコミット）・`nonce`（リプレイ防止） |

**制約パラメータの粒度（機械強制可能）：**

| パラメータ | 例 |
|-----------|-----|
| 許可 MCC | `MCC 5411`（食料品）のみ、など |
| 1回あたり上限 | `$50` 以内 |
| 累計上限 | `$300` 以内 |
| 日次・週次バケット | 1日 `$100` まで（任意） |
| 有効期間 | 最大 30日（モード依存） |
| 地域制限 | 国・地域単位 |

**L2 の2モード：**

| モード | L2 に何が入るか | L3 が必要か | 有効期間 |
|--------|----------------|------------|---------|
| **Immediate（即時）** | 最終的な金額・商品まで確定（ユーザーが直接指定） | 不要（L2 が終端） | 最大 **15分** |
| **Autonomous（自律）** | 制約のみ（「$300 以内で headphone を買え」） | 必要 | **24時間〜30日** |

Autonomous モードでは、まだ `checkout_jwt` が存在しない段階でも `conditional_transaction_id`（checkout mandate disclosure のハッシュ）を使って事前コミットが可能。

#### L3：エージェントが取引実行時に生成（Autonomous モードのみ）

| 項目 | 内容 |
|------|------|
| タイミング | エージェントが具体的な取引を決定した瞬間 |
| 署名者 | エージェント（L2 の `cnf.jwk` に対応する秘密鍵） |
| 含まれる情報 | 具体的な金額・商人・商品・`sd_hash`（L2 へのコミット） |
| 有効期間 | **5分**（最大1時間）← リプレイ攻撃防止のための設計 |
| 終端性 | **エージェントは別のエージェントに再委任できない**（L3 が終端） |

L3 は2つに分かれ、それぞれ別の相手に送られる：

```
L3a → 決済ネットワーク：金額・支払先のみ開示
L3b → マーチャント：購入品目・商人 ID のみ開示

checkout_hash（L3b）= transaction_id（L3a）= SHA-256(checkout_jwt)
```

この等価性により「同一取引を指している」ことを双方が確認できる。決済ネットワークは何を買ったか知らず、マーチャントはカード情報を知らない。

---

### Credential 有効期間まとめ

| Credential | 推奨 | 最大 |
|-----------|------|------|
| L1 | 1年 | 1年 |
| L2 Immediate | 15分 | 15分 |
| L2 Autonomous | 24時間〜30日 | L1 の期限以内 |
| L3a・L3b | 5分 | 1時間 |

---

### 鍵管理（PKI）

```
銀行の秘密鍵
  → L1 全体に署名（「このユーザーは本物」を保証）
  → 銀行が管理。ユーザーには渡らない

ユーザーの公開鍵
  → L1 の cnf.jwk に埋め込まれる
  → ユーザーが生成して銀行に登録

ユーザーの秘密鍵
  → L2 の署名に使う
  → 銀行には渡らない。デバイス/ウォレット側で管理

エージェントの公開鍵
  → L2 の cnf.jwk にユーザーが指定

エージェントの秘密鍵
  → L3 の署名に使う
  → エージェント事業者側で管理
```

**ユーザーの秘密鍵の保管場所**（仕様書は強制していない・実装依存）：

| 保管場所 | 特徴 |
|---------|------|
| デバイスの Secure Enclave / TEE | 鍵がハードウェアから出ない。最も安全 |
| サーバー側 HSM | ウォレットプロバイダーが管理。プロバイダーへの信頼が必要 |
| ソフトウェアウォレット | 実装依存 |

> 仕様書明記：ユーザーの秘密鍵が漏洩した場合、L1 の有効期間中は完全なアカウント乗っ取りとして扱う

---

### 取引の検証フロー（5ステップ）

```
1. ユーザー → バンキングアプリで Mandate を承認（L2 生成・署名）
2. 銀行 → 署名済み L1 をエージェント事業者に発行
3. エージェント → L3a・L3b を生成し、それぞれ決済ネットワーク・マーチャントに提示
4. マーチャント → Mastercard API で署名チェーンをローカル検証（ミリ秒）
5. ユーザー → オーソリ完了前にリアルタイムのプッシュ通知（介入可能）
```

署名検証は Mastercard ネットワーク上でミリ秒完結。ブロックチェーンへの問い合わせは不要。

---

### セキュリティ・不正検知

**不正検知の観点（3つ）：**
- 同一 Credential の並行使用（Credential reuse patterns の監視）
- 予期しないネットワークアドレスからの提示
- 行動分析ではなく「パラメータ逸脱」ベースのスコアリング（L2 制約との比較）

**Credential 盗難リスク：**
Credential 自体が高価値な攻撃ターゲットになるため、エージェント事業者側の保管セキュリティが重要（仕様書が明記）。

---

### ブロックチェーンの正確な役割

「偽造不能」の核心は署名チェーンであり、ブロックチェーンではない。

| 役割 | 実装 |
|------|------|
| 取引の署名検証 | Mastercard ネットワーク上でローカル完結 |
| エージェントの公開鍵レジストリ | Polygon・Solana・Base 上に記録（誰でも参照可能） |
| パーミッション情報の公開記録 | 同上（改ざん不可能な台帳として機能） |

---

### 技術仕様の参考リンク

- [Verifiable Intent 公式仕様書 – Credential Format](https://verifiableintent.dev/spec/credential-format/)
- [GitHub – agent-intent/verifiable-intent](https://github.com/agent-intent/verifiable-intent/)
- [Mastercard Verifiable Intent 解説 – Digital Applied](https://www.digitalapplied.com/blog/mastercard-verifiable-intent-trust-agentic-commerce)
- [Shane De Coninck – 技術解説](https://shanedeconinck.be/posts/mastercard-verifiable-intent-agents-can-prove-what-you-approved/)

---

## 未解決の論点

- ~~Verifiable Intent の技術仕様（スマートコントラクト構造・W3C VC との関係）~~ → 公開仕様書で確認済み（上記セクション参照）
- Mastercard の「決済保証」の責任範囲：エージェントが認可外の取引を実行した場合の責任分担
- カード決済・銀行口座・ステーブルコインの 3 レールが同じ「Verifiable Intent」フレームワークで同時に処理されるかどうか（レール別に異なる認可フローが存在する可能性）
- ブロックチェーン上に具体的に何がどう記録されるかの一次情報未取得（エージェントの公開鍵レジストリの実装詳細）
- ユーザー秘密鍵の保管場所のリファレンス実装（仕様書は強制していないため、各実装がどこに落ち着くか未確認）

## 参考リンク

- 一次情報: [The Block（2026-06-10）](https://www.theblock.co/amp/post/404288/mastercard-agent-pay-machines-support-autonomous-ai-transactions-stablecoins)
- 補足情報: [CryptoBriefing（2026-06-10）](https://cryptobriefing.com/mastercard-launches-agent-pay-for-machines-settle-ai-driven-microtransactions-network-scale/)
- 補足情報: [CoinDesk（2026-06-10）](https://www.coindesk.com/business/2026/06/10/mastercard-prepares-for-a-future-where-ai-agents-make-payments-with-latest-introduction)
- 補足情報: [The Defiant（2026-06-10）](https://thedefiant.io/converge/tradfi-and-fintech/mastercard-agent-pay-machines-ap4m-ai-agents-crypto-partners)
- 補足情報: [news.bitcoin.com（2026-06-10）](https://news.bitcoin.com/mastercards-ai-payment-debut-brings-coinbase-ripple-and-30-partners-into-agent-commerce/)

## 重要度

- High

## 確からしさ

- High（Mastercard 公式プレスリリース・複数専門メディアによる確認）
