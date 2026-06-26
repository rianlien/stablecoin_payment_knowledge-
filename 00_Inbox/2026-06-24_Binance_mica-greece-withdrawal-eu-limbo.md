---
title: "Binance、ギリシャ MiCA 申請を正式撤回——7/1 直前に EU ユーザーをリンボ状態に"
date: 2026-06-24
source: "CoinDesk / Decrypt / Yahoo Finance / Binance 公式ブログ"
source_url: "https://www.coindesk.com/policy/2026/06/24/binance-withdraws-greek-mica-bid-but-vows-to-remain-in-europe"
entity: "Binance"
category: regulation
primary_category: regulation
article_published_date: 2026-06-24
underlying_event_date: 2026-06-24
primary_source_date: 2026-06-24
tags:
  - MiCA
  - stablecoin-regulation
  - EU
  - regulation
  - psp
summary: "Binance が 2026-06-24 にギリシャ資本市場委員会（HCMC）への MiCA ライセンス申請を正式撤回。MiCA 移行期間終了（7/1）まで残り 7 日の時点での撤退確定。Binance は「EU には留まる」と表明し、別 EU 加盟国（フランスが有力候補）での申請を目指すと発表。ただし 7/1 までに新規認可を得るのは事実上不可能で、EU ユーザーへのサービス変更・制限が確定。"
implications: "Binance の EU 撤退確定により EU 内ステーブルコイン（USDC/EURC）流動性が MiCA 認可取得済みの Coinbase EU・Kraken・OKX・Crypto.com 等に集中。EU 向けオンランプ/オフランプとして Binance に依存していた x402 / agent payments フローの再設計が必要。"
importance: High
confidence: High
follow_up: "Binance の EU ユーザー向けサービス変更内容の通知（7/1 以前の詳細）、次の申請先 EU 加盟国（フランス AMF での DASP 登録活用の可能性）、EU 内 USDC 流動性への短期インパクト（Coinbase EU・Kraken への流入量）、フランス規制当局のパスポーティング問題"
---

## 概要

- 2026-06-24、Binance がギリシャ資本市場委員会（HCMC）への MiCA CASP ライセンス申請を正式撤回
- MiCA 移行期間終了（2026-07-01）まで残り 7 日時点での撤退確定
- EU 全域でのサービス継続に必要な「少なくとも 1 加盟国での認可」を欠いた状態で 7/1 を迎えることが確定
- Binance は「EU 市場は離れない」と表明。別加盟国での新規申請を目指すが、7/1 以降は EU ユーザー向けサービスに制限が生じる

## 何が起きたか

- **撤回理由**：ギリシャ HCMC が申請を拒否する方向との Reuters 報道（6/16）が背景。6/24 に Binance が撤回を正式発表
- **EU 内での認可状況**：Binance は EU 27 加盟国のうちギリシャ・アイルランド・ラトビアでも申請または交渉を行っていたが、いずれの規制当局も過去の法的問題・企業ガバナンス構造への懸念を理由に難色を示したとされる
- **次の申請先**：フランスが最有力候補。Binance はフランス AMF に DASP（デジタル資産サービスプロバイダー）として既に登録済みで、MiCA CASP 申請に転換できる可能性があるが、フランス当局はパスポーティング（緩い規制国での認可取得→他国拡大）に懸念を示している
- **競合比較**：Coinbase（ルクセンブルク CSSF）、Kraken（アイルランド中央銀行）、OKX（マルタ MFSA）、Crypto.com が MiCA CASP 認可を取得済みで、MiCA 施行後の EU 市場での競争優位を確立
- **EU ユーザーへの影響**：7/1 以降に一部サービス変更・口座制限の可能性。Binance はメール・アプリ内通知で影響を受けるユーザーへ直接連絡することを約束

## 確認された事実

- 2026-06-24：Binance が HCMC への MiCA 申請を正式撤回（Binance 公式ブログ・CoinDesk 報道で確認）
- 撤回理由は「タイムラインが遅く、正式決定がない」と Binance は説明（HCMC の拒否方向の報道とは若干ニュアンス違い）
- Binance Europe の責任者が「Binance は EU を離れない」とコメント（Reuters 報道）
- EU 全体で MiCA 全面認可を受けた CASP は約 210 社（3,000 社超の申請のうち約 7%）
- MiCA 移行期間終了後（7/1 以降）は、非認可 CASP が EU ユーザーに対してサービスを提供することは直接の MiCA 違反

## なぜ重要か

### 決済事業者視点

- EU 内で最大級の流動性を持っていた Binance のオンランプ/オフランプが 7/1 以降利用不可になることが確定
- USDC の EU 内調達・換金経路に Binance を使っていた PSP や決済事業者は代替経路（Coinbase EU・Kraken・OKX）への切り替えが急務

### 加盟店視点

- Binance の EU 撤退により EU ユーザーへの暗号資産/ステーブルコイン決済の直接フローが縮小
- Visa/Mastercard/SEPA 経由の既存フローへの回帰圧力が短期的に高まる

### プロダクト視点

- x402 やエージェント決済の EU 向け設計でオンランプ/オフランプとして Binance を想定していた場合は設計変更が必要
- MiCA 認可済み CASP（Coinbase EU・Kraken・OKX）への集中により、スプレッドや手数料が短期的に上昇する可能性

### 規制 / リスク視点

- Binance が最終的に 7/1 を無認可で迎えれば、ESMA・各国 NCA は EU 内ユーザーへのサービス提供禁止措置を発動する根拠を持つ
- フランスのパスポーティング問題：フランス当局が緩い規制国経由の passporting を遮断する姿勢を示しており、Binance の「別加盟国で申請→EU 全域展開」戦略が機能するかは不透明

## 我々への示唆

- いま検討すべきこと:
  - EU 向け USDC 調達・オフランプに Binance（EU）を使っている経路がある場合は 7/1 までに代替（Coinbase EU・Kraken）への切り替えを完了する
  - x402 / エージェント決済の EU 向けファシリテーター設計からBinance アドレスを除外し、MiCA 認可 CASP のみをホワイトリストに設定
- 後で深掘りすべきこと:
  - Binance の次の申請先（フランス）の進捗と、フランスのパスポーティング問題が業界全体に波及するかどうか
  - Binance 退場後の EU 内 USDC スプレッド・流動性変化（7/1 以降 1〜2 週間で実態確認）
- 今は優先度が低いこと:
  - Binance が将来的に EU 認可を取得した場合の再参入シナリオ（短期的には非現実的）

## ありそうな示唆

- EU 内でのステーブルコイン流動性が MiCA 認可取得済み 4 社（Coinbase EU・Kraken・OKX・Crypto.com）に寡占化する構造がこれで確定
- 寡占化の副作用として EU 内の USDC/EURC スプレッドが一時的に拡大する可能性がある。Circle が EU 内の流動性プロバイダー拡充を急ぐ動機が高まる

## 推測 / 監視ポイント

- Binance がフランス AMF DASP 登録から MiCA CASP 申請に転換できるか（フランス側の審査スピード・パスポーティング問題の行方）
- 7/1 以降 Binance が EU ユーザーにどの程度のサービス変更を通知するか（口座制限・出金のみ可・全面停止）
- 退場確定後の EU 内 Tether USDT 流動性への追加的打撃（USDT は MiCA 非準拠のため既に主要取引所で制限）

## 未解決の論点

- Binance が次に申請する EU 加盟国はどこか（フランス・スペイン・イタリア等の可能性）
- フランスが Binance のパスポーティングを実際にブロックするかどうかの法的根拠
- EU 内 USDC 流動性への定量的インパクト（Binance の EU ステーブルコイン取引量シェアは非公開）

## 参考リンク

- 一次情報: [CoinDesk（2026-06-24）](https://www.coindesk.com/policy/2026/06/24/binance-withdraws-greek-mica-bid-but-vows-to-remain-in-europe)
- 補足情報: [Decrypt（2026-06-24）](https://decrypt.co/371990/binance-withdraws-mica-license-application-greece-eu-users-limbo)
- 補足情報: [Yahoo Finance（2026-06-24）](https://finance.yahoo.com/markets/crypto/articles/binance-withdraws-mica-license-application-173752458.html)
- 補足情報: [Binance 公式ブログ（2026-06-24）](https://www.binance.com/en/square/post/06-24-2026-binance-withdraws-mica-license-application-in-greece-and-plans-to-seek-approval-elsewhere-in-the-eu-337594547520578)

## 重要度

- High

## 確からしさ

- High
