# Daily News Collection Skill

## Purpose
ステーブルコイン決済に関する重要なニュースや更新情報を、毎日1回収集し、
チームで再利用可能な日本語 Markdown ノートとして整理する。

## When to use
- 日次のニュース収集を行うとき
- `/00_Inbox/` に新規ニュースノートを追加するとき
- `/01_Daily-Briefs/` の日次まとめを作成または更新するとき

## Time window
- 収集対象は直近7日間に公開または重要更新された情報とする
- 実行頻度は毎日1回を想定する
- 直近24時間のみではなく、直近7日間を確認して取りこぼしを防ぐ

## Source priority
優先順位は以下の通り。
1. 公式発表
2. 規制当局・法令・ガイドライン
3. 決算資料・投資家向け資料
4. 公式ブログ・一次インタビュー
5. 信頼できる業界メディア

## Topic priority
以下のテーマに関係する情報を優先する。
- 店舗決済
- EC決済
- クロスボーダー決済
- PSP / PayFac / acquiring / treasury
- stablecoin
- wallet
- custody / self-custody
- on/off ramp
- KYT / AML / compliance
- payment orchestration
- settlement / reconciliation
- x402
- agentic commerce
- machine payments
- ERC-4337
- payment authorization
- API課金 / micropayments
- 国内外の決済事業者、金融機関、規制当局の動向

## Selection criteria
以下のいずれかに当てはまる情報を優先して採用する。
- 実運用に影響する
- 市場構造が変わる
- 規制やリスク評価に影響する
- プロダクト戦略に示唆がある
- 導入障壁または成功条件を示している

## Deduplication rules
新規ノートを作る前に、必ず `/00_Inbox/` と `/01_Daily-Briefs/` を確認すること。

以下の場合は重複として扱い、新規ノートを作らない。
- 同じ発表や同じ出来事を、別メディアが言い換えて報じているだけ
- 既に同じ論点のノートが存在する
- 元情報が同じで、新しい事実が追加されていない

以下の場合は新規ノートを作ってよい。
- 正式ローンチ
- 提携の実装進展
- 規制方針の重要変更
- 新しい地域展開
- 続報によって実務的な意味が変わった場合
- 既存ニュースに対して新しい一次情報が追加された場合

## Output count
- 1回の実行で作成する新規ニュースノートは原則3〜5件まで
- 条件に合う重要ニュースが少ない場合は、無理に件数を埋めない
- ノイズが多い日は少数精鋭を優先する
- source には情報源の名称を入れる
- source_url には最も一次情報に近いURLを入れる
- 参考リンクには、一次情報を最優先で記載し、必要に応じて補足情報を追加する

## Output language
- ノート本文は必ず自然な日本語で書く
- YAML frontmatter の key は英語のままにする
- 会社名、プロダクト名、規格名、法令名などは必要に応じて原文を残してよい
- 英語ソースでも本文は日本語で要約する

## Note format
- `/90_Templates/news_note_template.md` に従う
- 1ニュースにつき1ファイル作成する
- 保存先は `/00_Inbox/`
- ファイル名は以下の形式とする

`YYYY-MM-DD_<entity>_<short-slug>.md`

例:
`2026-04-23_circle_usdc_expansion.md`

## Note requirements
各ニュースノートには以下を必ず含める。
- 何が起きたか
- その事実は何に基づくか
- なぜ重要か
- 我々への示唆
- 追加で確認すべき論点
- 重要度
- 確からしさ
- 参考リンク

## Daily brief rules
その日の実行では、`/01_Daily-Briefs/YYYY-MM-DD.md` を作成または更新する。

日次まとめには以下を含める。
- 今日新規採用したニュース一覧
- 各ニュースの1〜3行要約
- 今日の重要論点
- 共通して見える市場変化や示唆
- 継続監視すべき事項

日次まとめには、重複として除外した話題は載せない。
日次まとめは「今日新しく採用したもの」だけを対象にする。

## Importance scale
- High: 事業方針、優先順位、実運用に影響する
- Medium: 継続監視が必要
- Low: 参考情報としては有用だが、直近の優先度は高くない

## Confidence scale
- High: 一次情報または複数の信頼できる情報源で確認できる
- Medium: 信頼できる二次情報に基づく
- Low: 単一ソースまたは不確実性が高い

## Tagging rules
- 既存タグを最優先で使う
- 新規タグは必要な場合のみ追加する
- 1ノートあたりのタグは3〜5個まで
- 表記ゆれを避ける
- tags は YAML 配列で出力する

## Preferred tags
- stablecoin
- payments
- regulation
- kyt
- wallet
- psp
- agentic-commerce
- x402
- merchant

## Working style
- 単なるニュース要約ではなく、再利用できる知識資産として整理する
- 事実と解釈を分ける
- 推測は推測と明記する
- 重要でない話題を無理に拾わない
- 後で週次まとめや MOC に統合しやすい粒度で書く