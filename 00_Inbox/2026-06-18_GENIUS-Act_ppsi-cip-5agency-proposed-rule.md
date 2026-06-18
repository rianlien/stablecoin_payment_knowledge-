---
title: "GENIUS Act、PPSI に銀行並み顧客確認（CIP）義務を課す 5 機関共同 NPRM——二次市場取引は適用外（2026-06-18）"
date: 2026-06-18
source: "Coindesk / Bloomberg / FinCEN press release / ABA"
source_url: "https://www.coindesk.com/policy/2026/06/18/u-s-agencies-seek-stablecoin-customer-id-rules-akin-to-banks-in-new-genius-act-rule"
entity: "FinCEN / Federal Reserve / OCC / FDIC / NCUA"
category: regulation
primary_category: regulation
article_published_date: 2026-06-18
underlying_event_date: 2026-06-18
primary_source_date: 2026-06-18
tags:
  - GENIUS-Act
  - regulation
  - PPSI
  - AML
  - stablecoin
summary: "2026-06-18、FinCEN・連邦準備制度・OCC・FDIC・NCUA の 5 機関が共同で GENIUS Act の PPSI 向け Customer Identification Program（CIP）要件を実施する NPRM を発表。PPSI は新規顧客に対し氏名・生年月日（または設立日）・住所・政府発行 ID 番号の収集・照合・記録を義務付けられる。二次市場での取引（ユーザー間ステーブルコイン移転）は原則として CIP 義務の対象外と予備的に判断した。コメント期間は連邦官報掲載（6/22 予定）から 60 日間（〜8/21）で、7/18 の法定デッドライン内での最終規則化は事実上不可能となった。"
implications: "x402・AP4M 等を通じたエージェント主導のステーブルコイン取引は二次市場に該当し、PPSI レベルの CIP は適用されない方向性が示された。Circle・Ripple・PayPal 等の発行体は直接発行・償還チャネルでの KYC 強化を迫られる一方、プロトコルレイヤーへの CIP 適用リスクが大幅に後退した。7/18 デッドラインの実質的な未達が確定し始め、GENIUS Act 最終規則の施行は早くとも 2026 年秋以降にずれ込む見込み。"
importance: High
confidence: High
follow_up: "8/21 コメント期間終了後の最終規則化スケジュール、7/18 法定デッドライン超過時のアクション（議会への報告・延長申請・遡及的施行計画）、de minimis 閾値と KYA（Know Your Agent）義務の CIP 規則での扱い、Circle・Ripple が CIP 要件の final rule に向けてコメント提出する内容"
---

## 概要

- 2026-06-18、FinCEN（主導）・連邦準備制度（Fed）・OCC・FDIC・NCUA の 5 機関が共同 NPRM を発表
- GENIUS Act の「PPSI は銀行秘密法上の金融機関として CIP を維持すること」という法律上の義務を実施するための規則案
- PPSI が顧客に義務付ける収集情報：① 法的氏名、② 生年月日または法人設立日、③ 物理的住所、④ 政府発行 ID 番号
- 二次市場取引（ユーザー間の移転・DEX での売買等）は CIP 義務の対象外と予備的に判断——「グローバル CIP」方式（すべてのステーブルコイン取引に適用）は不実現可能として棄却
- 連邦官報掲載予定：2026-06-22。コメント期間 60 日（〜2026-08-21）
- **今回の NPRM 公表により、7/18 法定最終規則デッドラインはこの CIP 規則について事実上達成不可能となった**

## 何が起きたか

### 5 機関共同 NPRM の内容

- **発行機関**：FinCEN（主管）、Federal Reserve Board、OCC、FDIC、NCUA——GENIUS Act が定める PPSI 認可機関の全省庁が連名
- **法的根拠**：GENIUS Act §5 は「PPSI は Bank Secrecy Act（BSA）上の金融機関として扱われ、CIP を維持しなければならない」と規定。今回の NPRM はその実施規則
- **CIP の具体的要件**：
  - 新規顧客が口座開設する前に (1) 氏名（法人は名称）、(2) 生年月日（法人は設立日）、(3) 物理的住所、(4) 政府発行識別番号（SSN / パスポート番号 / EIN 等）を収集
  - 収集した情報を「実行可能な範囲で合理的に」照合・検証する手続きの整備
  - 照合に使用した情報を記録として保持
  - 当局から提供される「テロリスト / テロ組織」リストとの照合義務
- **スコープの限定（重要）**：
  - 今回の CIP 義務は「PPSI と顧客の直接取引（発行・償還）」に限定
  - 二次市場取引（ユーザー間での USDC / RLUSD 移転、DEX での売買等）は原則として PPSI の CIP 義務を発生させない——予備的な判断として NPRM に明記
  - 規制当局はコメント期間中にこの境界の妥当性についてフィードバックを求めている

### タイムラインへの影響

- 連邦官報掲載：2026-06-22（予定）
- コメント締切：2026-08-21（60 日後）
- 法定最終規則デッドライン：2026-07-18
- **矛盾**：コメント期間が 7/18 を 34 日上回る。今回の CIP 規則については 7/18 最終規則化は論理的に不可能

### GENIUS Act 全体の NPRM 進行状況

| NPRM | 発行機関 | コメント期限 | 備考 |
|---|---|---|---|
| OCC 実施規則（連邦適格 PPSI） | OCC | 2026-05-01（終了） | 最終規則化フェーズ |
| FDIC 申請手続き | FDIC | 2026-05-18（終了） | 最終規則化フェーズ |
| 財務省・州制度認定原則 | Treasury | 2026-06-02（終了） | 最終規則化フェーズ |
| FDIC 実体基準 | FDIC | 2026-06-09（終了） | 最終規則化フェーズ |
| FinCEN・OFAC 共同 AML/CFT 規則 | FinCEN / OFAC | 2026-06-09（終了） | 最終規則化フェーズ |
| **CIP 規則（今回）** | **FinCEN / Fed / OCC / FDIC / NCUA** | **2026-08-21** | **7/18 前最終規則化不可** |

## 確認された事実

- 5 機関共同発表日：2026-06-18
- 発表機関：FinCEN・連邦準備制度・OCC・FDIC・NCUA（5 機関すべて）
- 収集義務 4 項目：氏名・生年月日（設立日）・住所・政府発行 ID
- 二次市場取引の CIP 適用除外：NPRM の予備的判断として明記（ただしコメントを求める）
- グローバル CIP 方式：「不実現可能（unfeasible）」として予備的に棄却
- 連邦官報掲載予定：2026-06-22
- コメント期間：60 日（〜2026-08-21）
- 7/18 法定デッドライン：今回の CIP 規則については達成不可能

## なぜ重要か

### 決済事業者視点

- PPSI が発行・償還チャネルでの KYC を義務化されることで、準拠ステーブルコイン（USDC・RLUSD・PYUSD）の発行コストが上昇する。PSP が PPSI ステーブルコイン受け取り側として利用する場合は直接影響を受けない
- 二次市場適用除外により、**x402 / AP4M でエージェントがステーブルコインを使って支払う行為は PPSI の CIP 義務を引き起こさない**——プロトコルレイヤーへの KYC 組み込みは不要という方向性が NPRM レベルで示された
- GENIUS Act 最終規則の全体的な完成が 2026 年秋以降にずれ込む可能性が高まった。7/18 時点では最大 6 本の NPRM のうち最後の 1 本だけがコメント期間中となり、partial final rules（5 本は確定・1 本は未定）という形になりうる

### 加盟店視点

- 加盟店が x402 / AP4M でステーブルコインを受け取ること自体は「二次市場取引」に該当するため、今回の CIP 規則の直接的な義務は生じない
- ただし加盟店が直接 PPSI（例：Circle の Mint サービス）から USDC を発行・償還する形でキャッシュマネジメントする場合は CIP 手続きが必要になる

### プロダクト視点

- **二次市場適用除外は x402・AP4M・AP2 に直接的な好材料**：エージェント決済プロトコルはユーザー間のステーブルコイン移転を行う二次市場的構造であり、今回の NPRM の方向性が最終規則に引き継がれれば、プロトコルレイヤーへの CIP 組み込みは不要になる
- GENIUS Act 7/18 遅延により、Circle の PPSI 最終認定も 2026 年秋以降になる見込み——USDC の「法的 PPSI ステータス確定」を前提にしたプロダクト設計は 9 月以降にずらすべき

### 規制 / リスク視点

- 今回の NPRM で GENIUS Act 実施規則のうち唯一コメント期間中のものが出た。7/18 を越えた場合の機関の対応（「暫定最終規則」を出すか、コメント期間中に発表するか）が明確でない
- de minimis 閾値と KYA の扱いは今回の CIP NPRM には明示的に含まれていない。依然として FinCEN/OFAC の AML/CFT NPRM（コメント終了済み）の最終規則化フェーズで決まる

## 我々への示唆

- いま検討すべきこと:
  - 二次市場適用除外の NPRM 文言を確認し、x402 / AP4M のトランザクション構造が「二次市場」に確実に分類されるかを法務チームと確認（コメント書として意見提出も検討）
  - Circle・Ripple 等の PPSI 候補が USDC / RLUSD の発行継続に使う認可ルート（連邦 PPSI vs 州ライセンス）が 7/18 前後でどう変わるかを注視——PPSI 認定遅延は発行体の法的地位に影響しない（移行期間適用）が、プロダクト上の「準拠ステーブルコイン」表示基準が変わりうる
- 後で深掘りすべきこと:
  - 8/21 コメント期間終了後の最終規則スケジュール——7/18 法定デッドラインを機関が「超過する判断」をする場合の法的根拠
  - de minimis 閾値と KYA の扱いが FinCEN/OFAC AML/CFT 最終規則でどう定められるか（エージェント決済の小額取引への適用範囲）
- 今は優先度が低いこと:
  - CIP 収集 4 項目の具体的な照合手続き設計——これは Circle / Ripple / PayPal 発行体側の問題であり、PSP / 加盟店には直接影響しない

## ありそうな示唆

- 5 機関共同 NPRM という体制は GENIUS Act の規制断片化リスク（機関ごとにバラバラな規則）を軽減する意図がある。二次市場適用除外と「グローバル CIP 棄却」がすべての機関の総意として NPRM に記載されたことで、最終規則での逆転は起きにくい——産業界はこの方向性を確定させるためにコメント期間を使って支持意見を積み上げるべき
- 7/18 デッドライン超過は避けられなくなった。規制機関が取りうる選択肢は：① 5 本の確定規則を 7/18 までに出し「最後の 1 本は追って」とする、② 全 6 本を「暫定最終規則（interim final rule）」として同時公告し 60 日後に正式確定する、③ 議会に状況報告して延長を認めてもらう——いずれにせよ GENIUS Act 発効日の見通しが変わる

## 推測 / 監視ポイント

- **8/21 コメント締切後の最終規則スケジュール**：9〜10 月に最終規則公告 → 発効は 120 日後（〜2027-01〜02）が有力シナリオ
- **7/18 を機関が「超過」する際の公式声明**：FinCEN / Fed が「コメント期間中のため 7/18 内最終規則化は不可能」と明確に声明するか
- **Circle の PPSI 認定タイムライン**：CIP 最終規則が出る前に OCC 連邦 PPSI 認定を受けることは可能か（別 NPRM の最終規則化が先行すれば可能という解釈もある）
- **de minimis 閾値の確定**：FinCEN/OFAC AML/CFT 最終規則（コメント終了済み）の公告時期——x402 / AP4M のマイクロペイメントへの AML 適用範囲が確定する

## 未解決の論点

- 今回の CIP NPRM の「二次市場適用除外」は予備的判断。コメントを受けて最終規則で逆転する可能性はあるか
- 7/18 法定デッドライン超過時の法的取り扱い——機関が義務超過した場合の法的効果（強制訴訟のリスクは低いが議会からの圧力はありうる）
- de minimis 閾値（マイクロペイメント向け）と KYA（Know Your Agent）の具体的な扱い——今回の CIP NPRM には含まれていないが、FinCEN/OFAC AML 最終規則で確定するはず

## 参考リンク

- 一次情報: [FinCEN Press Release（2026-06-18）](https://www.fincen.gov/news/news-releases/fincen-agencies-propose-rule-implement-genius-act-customer-identification)
- 一次情報: [Coindesk（2026-06-18）](https://www.coindesk.com/policy/2026/06/18/u-s-agencies-seek-stablecoin-customer-id-rules-akin-to-banks-in-new-genius-act-rule)
- 一次情報: [Bloomberg（2026-06-18）](https://www.bloomberg.com/news/articles/2026-06-18/fed-proposes-payment-stablecoin-issuer-identification-program)
- 補足情報: [PYMNTS（2026-06-18）](https://www.pymnts.com/legal/2026/federal-agencies-propose-identity-verification-rule-for-stablecoin-issuers/)
- 補足情報: [ABA（2026-06-18）](https://www.aba.com/banking-topics/compliance/regulatory-proposals/proposal-on-stablecoin-issuers)
- 補足情報: [KuCoin Flash（2026-06-18）](https://www.kucoin.com/news/flash/fed-and-4-agencies-propose-kyc-rules-for-payment-stablecoin-issuers)
- 前段ノート: [[2026-06-09_GENIUS-Act_nprm-comment-deadline-fdic-fincen]]（FinCEN/OFAC AML コメント期間終了・全 NPRM 最終規則化フェーズ移行）

## 重要度

- High

## 確からしさ

- High（FinCEN 公式プレスリリース・Coindesk・Bloomberg の複数独立報道で確認）
