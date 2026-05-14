# stablecoin_payment_knowledge-
ステーブルコイン決済関連のニュースや情報を集めるプロジェクト

## Purpose
ステーブルコイン決済関連ニュースと示唆を、チームで再利用可能な Markdown 資産として蓄積する。

## Setup
1. リポジトリをローカルにクローンする。

```bash
git clone https://github.com/rianlien/stablecoin_payment_knowledge-.git
```

2. PCに Obsidian をインストールする。
3. Obsidianを開き、`Open folder as vault` からクローンしたリポジトリフォルダーをvaultとして選択する。
4. Obsidianの `Settings` > `Community plugins` からコミュニティプラグインを有効化し、`Git` プラグインをインストールする。
5. Obsidianのコマンドパレットを開き、`Git: Pull` を実行する。

これでGitHub上の最新状態をローカルのObsidian vaultに反映できる。

## Folder rules
- 00_Inbox: 1ニュース1ファイル
- 01_Daily-Briefs: 日次まとめ（月別フォルダで管理）
- 02_Weekly: 週次まとめ
- 03_Topics: テーマ別の論点整理
- 04_Protocols: EIP/ERCなどプロトコル仕様の調査メモ
- 05_MOCs: 関連ノートを束ねるMOC（Map of Content）
- 06_Entities: 企業・組織・人物など、ニュース横断で追う対象
- 90_Templates: テンプレート

## Editing rules
- 事実と解釈を分ける
- 出典を残す
- 既存タグを優先する
- 規制ニュースは誇張しない
