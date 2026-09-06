<!-- source: https://learn.chatgpt.com/ja-JP/docs/whats-new -->

この週刊ダイジェストでは、仕事の進め方を変えるヒントになる ChatGPT と Codex の機能を
具体例や詳しい情報へのリンクとともに紹介します。バージョンごとのすべての更新、バグ修正、
細かな改善については、[Codex の変更履歴](/codex/changelog)をご覧ください。

## 2026 年 8 月 31 日～9 月 4 日

### GPT-6 Astra による難度の高い仕事への取り組み

[GPT-6 Astra](/ja-JP/codex/models#gpt-6-astra) は、高度な推論、コンピューターの使用、
より優れた判断力を組み合わせ、Codex と ChatGPT Work で
コード、アプリ、リサーチにまたがる複雑な仕事に対応します。ワークフローの実行から結果の確認、
テンプレートやタスクに合ったドキュメント、スプレッドシート、
プレゼンテーションの作成まで活用できます。

お使いのアカウントで Astra が利用可能になったら、モデルセレクターで選択してください。
大規模なタスクを始める前に、[使用量と料金](/ja-JP/codex/pricing)を確認してください。
Enterprise で利用するには、提供対象であることに加え、
管理者が有効にする必要があります。

## 2026 年 8 月 24～28 日

### より多くのウェブサイトでの作業

- **お使いのブラウザでの作業：** ChatGPT デスクトップアプリから、Chrome に加えて [Edge、Brave、Opera、Vivaldi](/ja-JP/codex/chrome-extension) でも作業できます。
  開いているタブを ChatGPT Work または Codex のチャットに取り込み、
  サインイン済みのウェブサイトで作業できます。
  Opera はブラウザの操作に対応していますが、サイドチャットは利用できません。

- **ウェブサイトが提供するツールの利用：** [サイトツール（WebMCP）](/ja-JP/codex/webmcp)を使うと、ChatGPT Work と Codex が
  デスクトップアプリの内蔵ブラウザで、ウェブサイトが提供するアクションを利用できます。
  たとえば、ドキュメントエディタは、セクションを検索したりコメントを追加したりするツールを提供できます。
  デスクトップアプリを更新し、GPT-5.6 Sol または GPT-5.6 Terra を使用してください。
  サイトツールは GPT-5.6 Luna では利用できず、
  Enterprise または Edu のワークスペースでも利用できません。

- **クラウドブラウザからのサインイン：** 対象プランでは、
  Web、iOS、Android の ChatGPT Work で、ウェブサイトのアカウントが必要なタスクを続行できます。
  [サインインのリクエスト](/ja-JP/codex/browser?surface=web#web-sign-in-to-a-website)に従い、
  チャットではなくサインイン手続きで必要な情報を入力してください。
  この操作でローカルのブラウザプロファイルが接続されることはありません。
  Enterprise または Edu のワークスペースでは、ウェブサイトへのサインインを利用できません。

利用できるかどうかは、提供状況とワークスペースの設定によって異なります。

[8 月 25 日のブラウザの
リリースノートをご覧ください](/codex/changelog#codex-2026-08-25-browser)。

### アプリのイベントを使ったスケジュール済みタスクの実行

[スケジュール済みタスク](/ja-JP/codex/automations?surface=web#web-trigger-tasks-from-app-events)は、Gmail、Slack、GitHub で
対応するイベントが発生したときにも起動できるようになりました。イベントトリガーを使うと、
一定間隔でポーリングせずに、新着メールのトリアージ、チャンネルのアクティビティの要約、
Pull Request のフィードバックへの対応を行えます。

イベントをトリガーとするタスクは、対象プランの Web 版およびモバイル版 ChatGPT で利用できます。まず、該当するアプリを接続し、アプリが要求するアクセスを承認してください。管理対象ワークスペースでは、管理者がアクセスを制御できます。

<PromptComponent
  prompt={`<owner>/<repository> 内の自分の Pull Request に新しいレビューフィードバックが届いたら、その内容を要約し、修正計画を作成してください。`}
/>

[8 月 25 日の
リリースノートをご覧ください](/codex/changelog#codex-2026-08-25-event-triggers)。

## 2026 年 8 月 17～21 日

### より多くのアプリやコンテンツを活用した作業

- **Apple Messages：** [Mac の Messages でチャットの検索、メッセージの要約、返信案の作成、送信ができます](/ja-JP/codex/plugins?surface=app#app-use-apple-messages-from-codex)。このプラグインは、macOS 版 ChatGPT デスクトップアプリのすべてのプランで利用できます。通常の ChatGPT チャットではなく、ChatGPT Work と Codex で使用してください。デフォルトでは、メッセージとその送信先をユーザーが承認した後にのみ、ChatGPT がメッセージを送信します。

- **Site の共同編集：** 利用可能な場合は、[ワークスペースのアクティブなメンバーを編集者として招待](/ja-JP/codex/sites#collaborate-on-a-site)できます。オーナーが Site を初めて公開した後、編集者は Site を改善したり、更新内容を公開したりできます。招待された編集者は Site の稼働中のデータベースのデータを閲覧できますが、共有と設定の管理権限はオーナーが保持します。

- **Site の URL の編集：** 利用可能な場合は、再デプロイせずに、[既存の Site 用に ChatGPT がホストする新しいアドレスを選択](/ja-JP/codex/sites#change-a-site-url)できます。以前のアドレスへのアクセスは、新しいアドレスにリダイレクトされます。

- **欧州でのコンピューターの使用履歴：** EEA、スイス、英国で[コンピューターの使用履歴](/ja-JP/codex/customization/computer-history)を利用できます。macOS を使用する ChatGPT Pro、Business、Enterprise のユーザー向けには、引き続きデフォルトでオフになっています。Business と Enterprise の管理者は、事前にアクセスを有効にする必要があります。

- **スレッドのスナップショットの共有：** macOS 版 ChatGPT デスクトップアプリから[ローカルの Codex スレッドの読み取り専用スナップショットを共有](/ja-JP/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread)できます。個人アカウントのリンクは、そのリンクを持つ人なら誰でも閲覧できますが、ワークスペースアカウントのリンクは作成元のワークスペース内でのみ閲覧できます。Codex は既知のシークレットのパターンに一致する情報をマスクしますが、機密情報が残る可能性があるため、共有前にスナップショットをレビューしてください。

- **ピン留めしたスレッドの統合：** [ピン留めしたチャット](/ja-JP/codex/projects?surface=app#app-organize-projects-and-chats)をデスクトップと iOS の間で同期できます。

[8 月 20 日のリリースノートをご覧ください](/codex/changelog#codex-2026-08-20-app)。

### Codex Cloud での GitLab プロジェクトの利用

[GitLab のサポート](/ja-JP/codex/third-party/gitlab)は、すべての ChatGPT プランで
ベータ版として利用できます。プロジェクトを接続してクラウド環境を作成し、
イシューやマージリクエストで `@codex` を使ってタスクを開始したり、
単発または自動のマージリクエストレビューを依頼したりできます。

この連携は Codex Cloud で動作し、管理対象ワークスペースの管理者が無効にできます。GitLab をトリガーとするアクティビティには、該当する Webhook を設定する権限が必要です。GitLab Self-Managed と GitLab Dedicated への接続には、ワークスペース管理者による設定が必要です。Webhook のアクティビティには GitLab 19.0 以降が必要です。

[8 月 19 日の GitLab の
リリースノートをご覧ください](/codex/changelog#codex-2026-08-19-gitlab)。

### レビュー用の公開プラグインメタデータのエクスポート

対象となる ChatGPT Enterprise ワークスペースのオーナーと管理者は、
ワークスペースに表示される公開プラグインの CSV をダウンロードできます。
[管理 \> プラグイン](https://chatgpt.com/admin/plugins)で **公開**を選択し、
ダウンロードアイコン（**CSV をエクスポート**）を選択してください。

エクスポートには、プラグイン、アプリ、チャットスキルの名前と説明に加え、開発者、バージョン、追加日（UTC）、OpenAI による検証のメタデータが含まれます。最大 48 時間前の公開カタログのスナップショットが使用され、ワークスペース向けに作成されたプラグインは含まれません。FedRAMP ワークスペースではエクスポートを利用できません。

[8 月 17 日の管理者向けエクスポート機能の
リリースノートをご覧ください](/codex/changelog#codex-2026-08-17-admin-csv)。

## 2026 年 8 月 10～14 日

### コンピューターの使用履歴を使った過去の作業の検索

[コンピューターの使用履歴](/ja-JP/codex/customization/computer-history)は、アプリやウェブサイトでのアクティビティを
検索可能なタイムラインとメモリに変換し、ChatGPT と Codex が
利用できるようにします。そのコンテキストを共有したい場合にのみ有効にし、
対象のアプリやウェブサイトを選択してください。収集の一時停止や履歴の確認、
削除はいつでも行えます。

コンピューターの使用履歴は、ChatGPT Pro、Business、Enterprise のお客様向けに、macOS 版 ChatGPT デスクトップアプリで提供されています。Business と Enterprise では、管理者が事前にアクセスを有効にする必要があります。初期提供の対象地域に欧州連合、スイス、英国は含まれません。

### Linux での ChatGPT デスクトップアプリの利用

[Linux 版 ChatGPT デスクトップアプリ](/ja-JP/codex/linux/linux-app)のプレビュー版が利用可能になりました。
対応する Ubuntu または Debian ディストリビューションでは `.deb` パッケージを、
Fedora では `.rpm` パッケージをインストールしてください。
x64 と ARM64 の両方のプロセッサ向けにパッケージが提供されています。

ChatGPT アカウントでサインインすると、プロジェクト、ローカルファイル、Codex を利用できます。コンピューターの使用などの一部の機能は、Linux プレビュー版ではまだ利用できません。

### 既存のエージェント設定と作業内容の引き継ぎ

**Claude Code**、<strong>Claude Cowork</strong>、または **Cursor** から、ChatGPT デスクトップアプリに[指示、設定、スキル、プラグイン、プロジェクト、
最近の作業内容をインポート](/codex/import)できます。
インポートした作業内容を同期するには、
**設定 \> インポート** で自動更新をオンにしてください。

Codex CLI では、`/import` を使って、Claude Code または Cursor から
対応する設定や最近のチャットをローカルセッションに取り込めます。

[8 月 11 日のデスクトップ版と CLI の
リリースノート](/codex/changelog#codex-2026-08-11-app)をご覧ください。

### 防御目的のセキュリティ業務に適したアクセスの選択

Daybreak では、承認された防御担当者向けに 2 つのティアを提供しています。 **Daybreak Blue** は、
コードのセキュリティレビュー、インシデント対応、
パッチの検証など、一般的な防御業務を支援します。 **Daybreak Red** の利用には別途承認が必要で、
許可されたセキュリティ評価に向けて専用に学習されたモデルにアクセスできます。

アクセスには [Trusted Access for
Cyber](/ja-JP/codex/cyber-safety#trusted-access-for-cyber) が必要です。
アクセスは、承認されたアイデンティティ、ワークスペースまたは組織、モデル、製品の利用環境に限定されます。

[8 月 10 日の Daybreak に関する
発表](/codex/changelog#codex-2026-08-10-daybreak)をご覧ください。

## 2026 年 8 月 3～7 日

### ChatGPT 音声モードを使ったファイルやプロジェクトの相談

[ChatGPT 音声モード](/ja-JP/codex/features/voice)が、アップロードしたファイルと
[ChatGPT プロジェクト](/ja-JP/codex/projects)に対応しました。
音声会話中に文書について質問したり、プロジェクト内の最近のチャット、ソース、指示を使って
作業を続けたりできます。

### 教育専用プラグインを使った学習と指導

3 つの新しい[プラグイン](/ja-JP/codex/plugins)により、ChatGPT Work と Codex で
授業に特化したワークフローを利用できます。 **College Student** は学習ガイド、練習用クイズ、
フラッシュカード、対話形式の解説を作成します。 **College Educator** は、
コース計画、教材、評価課題の作成を支援します。 **K–12 Educator** は、
授業計画、授業で使う資料、
さまざまな学習者に合わせた教材の作成を支援します。

これらのプラグインは、ChatGPT Edu と、学区単位で導入された ChatGPT for Teachers で利用できます。
利用可能なツールと権限は学校が管理します。
[教育向けプラグインに関する
発表](https://openai.com/index/learn-teach-chatgpt-work-codex/)をご覧ください。

### 保存済みファイルの再利用と過去の作業のすばやい検索

Web 版では、ライブラリに保存したファイルを再アップロードせずに会話へ追加したり、ライブラリ内を検索したり、見出し、リンク、リストを保ったまま書式付きテキストを貼り付けたりできます。Web、iOS、Android の検索では、フォルダーや会話のタイトルも検索対象になります。

Enterprise と Edu を含むすべての ChatGPT プランで、10,000 文字を超えるテキストを貼り付けると
添付ファイルになるようになりました。内容をメッセージ内に戻したい場合は、 **テキスト欄に表示** を
選択してください。

[ChatGPT の
リリースノート](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)をご覧ください。

### ChatGPT Work の残り利用枠の確認

個人向けプランおよび ChatGPT Business の対象ユーザーは、
Web 版のサイドバーで ChatGPT Work の残り利用枠を直接確認できます。利用できるクレジットの選択肢は、
アカウントとワークスペースの権限によって異なります。ChatGPT Work と Codex は、引き続き
同じ[利用上限とクレジット](/ja-JP/codex/pricing)を共有します。

### ChatGPT での GPT-5.6 の応答方法の選択

ChatGPT Plus と Pro のユーザーは、新しいスライダーで GPT-5.6 Sol が応答時にどの程度思考するかを調整できます。更新されたモデルは、事実の正確さが向上し、要点を押さえた回答を返すようになりました。無料プランと Go プランでは、GPT-5.6 Luna が ChatGPT のデフォルトモデルになります。

これらの変更は ChatGPT の会話に適用されます。
ChatGPT Work や Codex でのモデルの動作は変わりません。[ChatGPT の
リリースノート](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)をご覧ください。

### Codex CLI 0.147.0 での作業の整理とエージェントの切り替え

[Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0) では、
手動で並べ替えられ、次回以降も保持されるチャットセクションと、環境間で持ち運べる Agent Plugins が追加されました。
ローカル、個人用、ワークスペース、リモートのプラグインカタログを横断して検索できます。
また、同期済みの会話を重複させることなく、
[Cursor と Claude Code の設定をインポート](/ja-JP/codex/import)できます。

`--approve-for-me` を使うと、対象となる[承認リクエストの
自動レビュー](/ja-JP/codex/sandboxing/auto-review)を、ファイルシステムやネットワークの権限を拡大することなく有効にできます。
Amazon Bedrock のセッションでは、キャッシュを利用したウェブ検索と、
リモートでの会話のコンパクションも利用できるようになりました。

### 詳細なセキュリティスキャンの進捗確認と再開

ホスト型 Codex Security プラグインのバージョン `0.1.16` から `0.1.18` では、
スキャン進捗のリアルタイム表示、トークン使用量の実測、再開可能な詳細スキャン、
探索上限の設定が追加されました。最新リリースでは、リポジトリのスキャンと、その作業を委任されたワーカー向けの
Amazon Bedrock 認証にも対応しています。

[Codex Security ワークベンチ](/ja-JP/codex/security/plugin/workbench)で、
スキャンの進捗や検出結果を確認できます。より徹底した評価が必要な場合は、[詳細スキャンの
設定](/ja-JP/codex/security/plugin/deep-scans)を行ってください。
インストール済みのバージョンが対応している機能は、[プラグインの変更履歴](/ja-JP/codex/security/plugin/changelog)で
確認してください。

### GitHub Pull Request のセキュリティリスクのレビュー

[Codex Security Review](/ja-JP/codex/security/security-review) は、Pull Request の変更を、
リポジトリのコンテキスト、脅威モデル、セキュリティガイダンスと併せて分析します。
Pull Request が作成されたときや新しいコミットが追加されたときに自動レビューを行うよう設定できます。
`@codex security review` で直接レビューを依頼することもできます。

この機能は、対象となる ChatGPT Enterprise、Business、Edu、Pro のお客様向けにリサーチプレビューとして提供されています。Plus では利用できず、利用上限が適用される場合があります。

## 2026 年 7 月 27～31 日

### GPT-5.6 Terra と Luna をより低料金で利用

GPT-5.6 Terra の料金が 20%、GPT-5.6 Luna の料金が 80% 引き下げられました。
入力、キャッシュ済み入力、出力の料金は、それぞれ同じ割合で引き下げられています。
[利用上限と料金](/ja-JP/codex/pricing)の改定により、Terra は日常的な作業にさらに適したモデルとなり、
Luna は範囲を絞ったコーディングや大量のタスクに特に役立ちます。

### ブラウザと開いているタブから役立つコンテキストを検索

ChatGPT デスクトップアプリの[内蔵ブラウザ](/ja-JP/codex/browser)では、
閲覧履歴からページを見つけたり、アドレスバーから直接 Google で検索したりできます。
タスクに以前のコンテキストが必要な場合は、
ChatGPT が閲覧履歴を検索することもできます。

[Chrome 拡張機能](/ja-JP/codex/chrome-extension)では、開いているタブにメンションしたり、
ページ内で選択したテキストをサイドチャットに取り込んだり、YouTube 動画について質問したり、
ページのコンテキストメニューから「 **ChatGPT に質問** 」を選択したりできます。
ChatGPT が閲覧履歴の情報をタスクに取り込む前に、
閲覧履歴の使用リクエストを確認して承認してください。

### 複数のリポジトリにまたがる変更のレビュー

[ローカルプロジェクトに複数の
フォルダーが含まれている](/ja-JP/codex/projects#use-local-projects-for-folders-and-codebases)場合、
デスクトップアプリにはすべてのリポジトリと、それぞれの変更行が表示されます。
「**レビュー** 」を選択すると、個別のレビュー画面を切り替えることなく、
差分をまとめて確認できます。

### 会話内での生成画像の調整

生成した画像を拡大ビューアーで開くと、
「**フォーカス表示** 」と「 **canvas 表示**」を切り替えられます。複数の画像にコメントを追加し、
残したいバージョンを選択して、チャットを離れることなく特定の箇所の編集を依頼できます。
詳しくは、[画像生成](/ja-JP/codex/image-generation)をご覧ください。

### 対応が必要なチャットの確認

デスクトップアプリの新しい **アクティビティビュー** には、最近やり取りしたチャットと
対応が必要な作業がまとまっています。サイドバーのベルを選択すると、
このビューを開けます。

[7 月 30 日のデスクトップ版
リリースノート](/codex/changelog#codex-2026-07-30-app)をご覧ください。

### 「ChatGPT でサインイン」によるパートナーツールとの連携

「**ChatGPT でサインイン** 」のベータ版が、対応プラグインと
パートナーサイト向けに順次提供されています。まず Airtable、GitLab、HubSpot、Notion、Supabase、
Vercel から提供が始まっています。パートナーのアカウントを少ない手順で作成または連携し、
ChatGPT や Codex でそのサービスを使い始められます。

パートナーに共有される情報は、名前、メールアドレス、および設定されている場合の
プロフィール写真のみです。各プラグインが要求するアクセスについては、引き続き個別のレビューと
承認が必要です。[7 月 29 日のサインインに関する
発表](/codex/changelog#codex-2026-07-29)をご覧ください。

### 学術研究専用ワークスペースでの共同作業

[ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/) は、
対象となる大学教員と博士研究員に、専用の ChatGPT ワークスペースを
12 か月間無料で提供します。承認されたチームには、同じ機関に所属する
確認済みの研究者が最大 5 人参加でき、ビジネス向けのデータ保護と
ChatGPT Pro と同等の利用上限が適用されます。参加者は ChatGPT、ChatGPT Work、Codex で
GPT-5.6 を研究やコーディングのワークフローに利用できます。

このプログラムの対象は ChatGPT の利用であり、OpenAI API クレジットは含まれません。利用資格を得るには、
[所属機関の確認と
要件を満たす研究論文](https://help.openai.com/en/articles/20001406)が必要です。

### iOS での Codex タスク再開の信頼性向上

iOS 版 ChatGPT 1.2026.202 では、アプリに戻ったときや Face ID でデバイスのロックを解除したときに、タスクへより確実に再接続できるようになりました。音声会話では、選択した ChatGPT の音声が使われ、利用上限に関する警告が表示されます。また、コンポーザーでインストール済みのプラグインとそのスキルが、デスクトップアプリと同じように提案されるようになりました。

このリリースでは、目標の一時停止と再開の操作、インラインの表と
表示テーマ、大規模なワークスペースの差分、選択したテキストの参照、モデルの復元も
改善されています。[7 月 27 日の iOS 版
リリースノート](/codex/changelog#codex-2026-07-27-mobile)をご覧ください。

### セキュリティスキャンの比較と検出結果の管理

ホスト型の Codex Security プラグイン `0.1.14` と `0.1.15` では、スキャンの比較、
誤検知に関するフィードバック、適用範囲を指定した `SECURITY.md` ポリシーが追加され、リポジトリと
検出結果の履歴もわかりやすくなりました。Linear や GitHub イシューで追跡する検出結果を
選択できます。提案された操作は、ユーザーが承認する前に Codex がレビューします。

デスクトップアプリの既存の [Codex Security
ワークベンチ](/ja-JP/codex/security/plugin/workbench)で、保存済みのスキャン、検出結果、
リポジトリ履歴、修正対応を確認できます。ホスト型プラグインの
カタログではバージョン `0.1.15`、公開 CLI プラグインマーケットプレイスでは
バージョン `0.1.11` が提供されています。新機能を利用する前に、[Codex Security プラグインの
変更履歴](/ja-JP/codex/security/plugin/changelog)を確認してください。

### ターミナル、CI、TypeScript からのセキュリティスキャンの実行

一般公開されている `@openai/codex-security` CLI と TypeScript SDK がバージョン
`0.1.5` になりました。リリース番号は Codex Security プラグインとは別に管理されています。
このパッケージを使うと、[CLI からスキャンを実行](/ja-JP/codex/security/cli)したり、
[CI](/ja-JP/codex/security/cli/ci) で Pull Request の変更をレビューして SARIF 結果をアップロードしたりできます。
また、再開可能な[一括スキャン](/ja-JP/codex/security/cli/bulk-scans)を、GitHub リポジトリや
固定済みの CSV インベントリを対象に実行できます。

[Codex Security TypeScript SDK](/ja-JP/codex/security/sdk) を使うと、
スキャン、進捗報告、コスト管理、キャンセルの機能を独自のツールに
組み込むこともできます。パッケージは一般公開されていますが、スキャンの実行には引き続き Codex Security へのアクセス権が必要です。
リポジトリ全体を対象とする一部のスキャンには、Trusted Access for Cyber も必要です。

### Codex CLI 0.146.0 のセッション整理と機能拡張

[Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0) では、
`/new release prep` や `/clear bug bash` で新しいチャットに名前を付けたり、
重要なスレッドをピン留めしたり、並行する会話を閉じずに切り替えたりできます。
また、会話を一時的にフォークする機能、対応するカスタムモデルプロバイダー向けの
単独で使えるウェブ検索、エグゼキューターが提供するスキルが追加されました。Agent Plugins の
マニフェスト、ワークスペースでのプラグイン公開、ほかのプラグインマーケットプレイスにも対応しました。

カスタムクライアントでは、[App Server](/ja-JP/codex/app-server) を使ってピン留め済みのスレッドを
絞り込んだり、メモリ内でフォークを作成したり、インストール済みコネクタの状態を確認したり、
コネクタのメタデータを読み取ったりできます。試験的な WebSocket サポートにより、app-server を
リモートの Code Mode ホストに接続することもできます。リモート接続を公開する前に、
[app-server のセキュリティ要件](/ja-JP/codex/app-server#connect-the-cli-terminal-ui)を
確認してください。このリリースでは、プロキシ対応、
MCP の再接続、ターミナルの応答性、Windows サンドボックスの信頼性も改善されています。

### ホスト型 Codex での GPT-5.6 Sol の利用

[GPT-5.6 Sol](/ja-JP/codex/models#recommended-models) が、対象のお客様向けの Codex Cloud のコードレビューと
品質保証で使われるようになりました。Sol は、複雑なコーディング、リサーチ、
コンピューターの使用、セキュリティ作業に向けた GPT-5.6 のフラッグシップモデルです。
Codex Cloud ではモデルが自動的に選択されます。Terra と Luna は、対応する
ローカル環境やウェブのインターフェースで引き続き利用できます。

### GPT-5.4 モデルの提供終了に向けた準備

8 月 31 日をもって、ChatGPT でサインインしているユーザー向けの Codex で、
GPT-5.4 と GPT-5.4 mini の提供が終了します。ワークスペースのデフォルト設定、保存済みのモデル設定、
管理対象の構成、カスタムエージェント、スケジュール済みタスクで、
`gpt-5.4` を `gpt-5.6-terra` に、`gpt-5.4-mini` を `gpt-5.6-luna` に置き換えてください。

OpenAI API と API キーで認証された Codex セッションは
影響を受けません。提供終了日までに、[非推奨の Codex モデル](/ja-JP/codex/models#deprecated-codex-models)と
[ワークスペースでのモデルの
利用可否](/ja-JP/codex/enterprise/workspace-model-availability)を
確認してください。

## 2026 年 7 月 20～24 日

### ChatGPT 音声モードを使った作業の相談

GPT-Live を搭載した [ChatGPT 音声モード](/ja-JP/codex/features/voice)では、
ChatGPT デスクトップアプリのチャット、Work、Codex で、作業について話し合いながら
タスクを調整できます。音声モードで新しいチャットやタスクを開始し、ChatGPT にほかのスレッドでの作業の開始、確認、
進め方の変更を依頼できます。

macOS では、 **画面のコンテキスト** がオンのときに「これを見て」と話しかけると、
最前面のウィンドウの[アプリショット](/ja-JP/codex/appshots)を共有できます。

音声機能は、Plus、Pro、Business、Edu、Enterprise プランで、
デスクトップアプリおよび[ iOS のリモート](/ja-JP/codex/remote-connections#set-up-mobile-access)から利用できます。

### 1 つのローカルプロジェクトで複数フォルダーにまたがる作業

ChatGPT デスクトップアプリのローカルプロジェクトに、関連する複数のフォルダーを追加できるようになりました。
新しいチャットや Git 操作、
`AGENTS.md`、スキル、`config.toml` の自動検出に使うプライマリフォルダーを選択します。セカンダリフォルダーも引き続き、
ファイルの検索、読み取り、編集に利用できます。

**プロジェクトを編集** を開き、[フォルダーの追加と
プライマリフォルダーの選択](/ja-JP/codex/projects#use-local-projects-for-folders-and-codebases)を行います。

[7 月 23 日のリリースノート](/codex/changelog#codex-2026-07-23-app)をご覧ください。

## 2026 年 7 月 13 日～17 日

### デスクトップでの Work の会話とプロジェクトの一元管理

ChatGPT デスクトップアプリでは、チャットと Work の会話が ChatGPT ビューにまとめて表示されるようになりました。クラウドの Work の会話はウェブ、モバイル、デスクトップ間で同期され、ローカルの Work の会話はコンピューター上に保持されます。デスクトップアプリで ChatGPT のプロジェクトを利用できます。Codex では、開発者向けワークフロー用の専用ビューと独立した履歴が引き続き提供されます。

[デスクトップでの
 ChatGPT Work と Codex の比較](/ja-JP/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop)を参考に、
タスクに合ったビューを選択してください。

### Codex Micro による Codex の並列作業の操作

7 月 15 日、OpenAI と Work Louder は、ChatGPT デスクトップアプリの Codex を操作する数量限定の物理コントローラー、
[Codex Micro](/ja-JP/codex/features/codex-micro) を発売しました。
エージェントキーでは、最大 6 件のチャットの状態を表示し、チャットを切り替えられます。
カスタマイズ可能なコマンドキー、アナログスティック、ダイヤルを使えば、
キーボードから手を離さずに、よく使う操作やスキルの実行、プッシュトゥトークの開始、
推論強度の調整ができます。

### Amazon Bedrock での GPT-5.6 の利用

GPT-5.6 Sol、Terra、Luna が Amazon Bedrock で一般提供されるようになりました。
ローカルの ChatGPT Work と Codex では、
Bedrock API キーまたは AWS SDK の認証情報チェーンを使って、組み込みの [`amazon-bedrock` プロバイダー](/ja-JP/codex/amazon-bedrock)を利用できます。
対象は、ChatGPT デスクトップアプリの Work と Codex、
Codex CLI、IDE 拡張機能、Codex SDK です。

### iOS での Codex タスクの可視化の確認

iOS 版 ChatGPT 1.2026.188 では、Codex タスクにインラインの可視化が追加され、
会話からのタスクの作成と管理も改善されました。
新しく作成したタスクへのリンクも、より確実に機能するようになりました。
[7 月 13 日の iOS リリースノート](/codex/changelog#codex-2026-07-13-mobile)をご覧ください。

## 2026 年 7 月 6 日～10 日

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### ChatGPT での大きな目標への挑戦

ChatGPT の [ChatGPT Work](/ja-JP/codex/get-started-with-work) は、
ファイルや[プラグイン](/ja-JP/codex/plugins)からコンテキストを集め、
さまざまなワークフローで操作を実行し、レビュー可能なドキュメント、プレゼンテーション、
スプレッドシート、Sites などの成果物を作成できます。
[GPT-5.6](/ja-JP/codex/models) を搭載し、目標を手順に分解して何時間も作業を進められます。
その間、ユーザーは進捗を確認したり、質問に答えたり、方針を変えたり、
重要な操作を承認したりできます。

[スケジュール済みタスク](/ja-JP/codex/automations)は、1 回限り、スケジュールに従って、イベントの発生時、
または変化を監視しながら実行できるため、
ユーザーが不在でも作業を進められます。

### 用途に合った GPT-5.6 モデルの選択

[GPT-5.6 ファミリー](/ja-JP/codex/models#recommended-models)には、ChatGPT Work、ChatGPT デスクトップアプリ、
Codex CLI、Codex IDE 拡張機能で利用できる 3 つの推奨モデルがあります。
Sol は、複雑なコーディング、コンピューターの使用、リサーチ、セキュリティ業務向けのフラッグシップモデルです。
Terra は日常的な作業に向けて性能とコストのバランスを取り、Luna は最も高速で、最も低コストのモデルです。
デフォルトの **パワー** 設定では、
推論強度「中」の Sol を使用します。

### ChatGPT デスクトップアプリでの Codex の利用

7 月 9 日、Codex App は macOS と Windows 向けの
[ChatGPT デスクトップアプリ](/ja-JP/codex/app)に統合されました。Codex は、ChatGPT のチャットや Work と並んで、
コーディング専用の機能を引き続き提供します。
Codex では、差分内のインライン編集、サイドパネルでの Pull Request のレビュー、
GPT-5.6 によって高速化された[コンピューターの使用](/ja-JP/codex/computer-use)、
複数のリポジトリを含むプロジェクトを利用できます。

既存の Codex App ユーザーは、通常どおりアップデートできます。Codex をデフォルトのビューに設定したり、Codex のロゴをアプリアイコンに使ったり、ChatGPT モバイルアプリからデスクトップの Codex プロジェクトにアクセスしたりできます。更新されたデスクトップアプリは、無料版を含むすべての ChatGPT プランで、世界中で利用できます。

## 2026 年 6 月 15 日～19 日

### 実演したワークフローのスキル化と再利用

[記録と再生](/ja-JP/codex/extend/record-and-replay)では、macOS 上で ChatGPT や Codex にワークフローを実演し、
その操作を再利用可能なスキルに変換できます。
言葉で説明するより実演する方が簡単な繰り返し作業に利用し、
生成されたスキルを調整して、新しい入力で再実行できます。提供開始時点では、
EEA、英国、スイスは対象外で、利用には「コンピューターの使用」が必要です。

<a id="continue-a-task-on-another-host"></a>

### 別のホストでのチャットの継続

[チャットの引き継ぎ](/ja-JP/codex/remote-connections#hand-off-a-chat-between-hosts)では、
ローカルのコンピューターと接続済みのリモートホストの間で、チャットとその Git の状態を移動します。
Codex は移動先で Worktree を作成または再利用してチャットを転送し、
対応するプロジェクトで作業を続けられます。

同じデスクトップ版のリリースでは、スケジュール済みタスクの実行履歴に一括操作も追加されました。すべての実行を既読にしたり、対象となる実行をまとめてアーカイブしたりできます。

### iOS からのワークスペースの閲覧とレビュー

iOS 版 ChatGPT モバイルアプリの **リモート** に、ワークスペースのファイルブラウザ、
新しいチャット用のディレクトリ選択、差分の展開・折りたたみ操作、
MCP の承認をチャット単位または複数のチャットにわたって適用する選択肢が追加されました。

コンピューターの使用、Chrome 拡張機能、メモリ、Chronicle も、EEA、英国、スイスで順次提供が始まりました。これらの地域では、メモリは引き続きデフォルトでオフです。Chronicle は、macOS を利用する ChatGPT Pro 契約者向けの、オプトイン方式のリサーチプレビューです。

[6 月 15 日の iOS](/codex/changelog#codex-2026-06-15-mobile)、
[6 月 16 日の提供状況](/codex/changelog#codex-2026-06-16-app)、
[6 月 18 日のアプリ](/codex/changelog#codex-2026-06-18-app)のリリースノートをご覧ください。

## 2026 年 6 月 8 日～12 日

### ブラウザの開発者モードによるウェブアプリのデバッグ

[開発者モード](/ja-JP/codex/browser?surface=app#app-developer-mode)では、Codex が Chrome と内蔵ブラウザの
Chrome DevTools Protocol 機能に制御された範囲でアクセスできます。
アプリのプロファイリングやデバッグ中に、ネットワークトラフィック、コンソール出力、実行時エラー、
ページの状態を調べられます。**設定** \> **ブラウザ**の **開発者モード** で、
 **CDP へのフルアクセスを有効にする**をオンにします。
Codex は、ウェブサイトでそのアクセス権を使う前に明示的な承認を求めます。

CDP と DOM スナップショットの最適化でブラウザとの往復通信が減り、ブラウザ操作も最大 2 倍高速になりました。

  
    
  

### Codex への設定の移行

新しい移行フローにより、初期設定時に他のコーディングエージェントから対応する設定をインポートできるようになりました。
Codex App には、プロジェクトの指示を作成する `/init` も追加され、
プラグイン管理、ブラウザの診断、
完了したチャットの要約も改善されました。

<a id="set-up-codex-tasks-from-ios"></a>

### iOS からの Codex チャットのセットアップ

iOS のリモートで、ブランチの選択、Worktree の作成、環境セットアップスクリプトの実行、目標の管理、インラインレビューコメントの追加ができるようになりました。

[6 月 9 日のアプリ](/codex/changelog#codex-2026-06-09-app)、
[6 月 9 日の iOS](/codex/changelog#codex-2026-06-09-mobile)、
[6 月 11 日のアプリ](/codex/changelog#codex-2026-06-11-app)のリリースノートをご覧ください。

## 2026 年 6 月 1 日～5 日

### Sites によるウェブサイトの構築とデプロイ

[Sites](/ja-JP/codex/sites) を使うと、ChatGPT で OpenAI がホストするウェブサイト、
ダッシュボード、社内ツール、ウェブアプリ、ゲームを作成、保存、デプロイ、検査できます。
Web 版とデスクトップ版の ChatGPT には Sites 専用の入口があり、
プロジェクトを再び開いたり、ホスト環境の値やシークレットを管理したりできます。
別途デプロイ環境を構築する必要はありません。

### Amazon Bedrock での Codex の利用

ローカルワークフローで [Amazon Bedrock を通じて Codex を利用](/ja-JP/codex/amazon-bedrock)でき、
認証、アカウント制御、請求は AWS が管理します。
iOS のリモートには、任意で有効にできるアプリ内ロック、フォローアップの動作設定、
差分の行の折り返し、Windows マシンへの SSH 接続も追加されました。
デスクトップアプリには、ターミナルの配置設定と、
プロファイル画面でアクティビティの分析情報を確認できる機能が追加されました。

[2026 年 6 月のすべてのリリースノートをご覧ください](/codex/changelog#month-2026-06)。

## 2026 年 5 月 25～29 日

### Windows アプリの操作と Codex のリモート制御

[コンピューターの使用](/ja-JP/codex/computer-use#windows-foreground-use)が、Windows デスクトップアプリでの
画面の確認、クリック、文字入力に対応しました。使い始める前に、
コンピューターの使用プラグインをインストールしてください。Windows では、Codex はアクティブなデスクトップを使用し、
タスクの実行中はフォアグラウンドを占有します。リモート接続も Windows に対応しています。
ChatGPT モバイルアプリで **リモート** を開くと、Windows デバイスで作業を開始できます。
また、ChatGPT デスクトップアプリを実行している Mac を使用し、
別の場所から進捗を確認することもできます。

iOS のリモートには、Spotlight とショートカットからのアクセス、アーカイブ済みチャットの閲覧、
`/side`、レンダリングされた画像を保存またはコピーするオプションも追加されました。
デスクトップアプリには、ローカルプロジェクトや Worktree でのチャット間の連携、
過去のチャットを内容やブランチ名で検索する機能、
バックグラウンドのサブエージェントを見分けるための統一された識別表示が追加されました。

[5 月 25 日の iOS](/codex/changelog#codex-2026-05-25-mobile) と
[5 月 29 日のアプリ](/codex/changelog#codex-2026-05-28-app)のリリースノートをご覧ください。

## 2026 年 5 月 18～22 日

### Appshots による Mac のあらゆるアプリから Codex へのコンテキスト共有

[Appshots](/ja-JP/codex/appshots) では、両方の Command キーを押すと、
最前面のアプリウィンドウのスクリーンショットと取得可能なテキストを Codex に送信できます。
画面の内容をコピーして貼り付けたり、言葉で説明したりしなくても、
Codex はデザインツール、ダッシュボード、ドキュメント、その他のアプリから作業のコンテキストを得られます。

### 長時間かかる目標の進捗確認

[目標モード](/ja-JP/codex/prompting#goal-mode)が実験段階を終え、
Codex App、IDE 拡張機能、CLI で利用できるようになりました。
達成に数時間から数日かかる目標に向けた作業に使えます。[ロック中の使用](/ja-JP/codex/computer-use#locked-use)を利用すると、
Mac がロックされた後も、Codex は承認済みのコンピューターの使用による作業を継続できます。
ChatGPT モバイルアプリの**リモート** 経由でも継続できます。ChatGPT Business のワークスペースでは、
[再利用可能なプラグインのバンドルをワークスペースのメンバーと共有](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace)することもできます。

[5 月 21 日のリリースノートをご覧ください](/codex/changelog#codex-2026-05-21)。

## 2026 年 5 月 11～15 日

### デスクトップでの作業をモバイルから継続

ChatGPT モバイルアプリの **リモート** では、
ChatGPT デスクトップアプリを実行している Mac に接続できます。作業は接続先のホスト上で実行されるため、
スマートフォンから続きを進める際も、プロジェクト、ファイル、認証情報、
プラグイン、スキル、構成を引き続き利用できます。ホストを設定して別のデバイスから作業を再開する方法は、
[リモート接続](/ja-JP/codex/remote-connections)をご覧ください。

### 信頼できるワークフローの自動化

エージェントのライフサイクルの主要なタイミングでカスタムコマンドを実行できるフックの
一般提供が始まりました。ChatGPT Enterprise の管理者は、
信頼できるスクリプト、スケジューラー、プライベート CI ランナー向けに
[Codex アクセストークン](/ja-JP/codex/enterprise/access-tokens)を有効にすることもできます。エンタープライズ向けのガイダンスも拡充され、
Codex のセットアップの一元管理や制御も対象になりました。

[5 月 14 日のリリースノートをご覧ください](/codex/changelog#codex-2026-05-13-app)。

## 2026 年 5 月 4～8 日

### Chrome 拡張機能による複数タブでの作業

[Chrome 拡張機能](/ja-JP/codex/chrome-extension)は、ブラウザを占有せずに、
複数のタブでバックグラウンドの作業を並行して実行できます。
Codex が利用できるウェブサイトはユーザーが管理できるため、
複数のウェブアプリでのリサーチ、データ入力、検証を 1 つのタスクにまとめて行いやすくなります。

Codex App には、音声入力の整形機能と、名前、
ファイルパス、コード内のシンボル用のカスタム辞書も追加されました。ChatGPT Enterprise のワークスペース所有者は、
信頼できる非対話型のローカルワークフロー用の
[Codex アクセストークン](/ja-JP/codex/enterprise/access-tokens)の作成をメンバーに許可できます。

[5 月 5 日のアプリ](/codex/changelog#codex-2026-05-05-app)、
[5 月 5 日のアクセストークン](/codex/changelog#codex-2026-05-05)、
[Codex for Chrome](/codex/changelog#codex-2026-05-07) のリリースノートをご覧ください。

## 2026 年 4 月 20～24 日

### 複雑な作業への GPT-5.5 の活用

[GPT-5.5](/ja-JP/codex/models) が、ほとんどのタスクに推奨されるモデルとして Codex に登場しました。
実装、デバッグ、テスト、コンピューターの使用、
リサーチ、知識労働の成果物を完成させる作業に強みがあります。

### Codex によるブラウザ操作と承認リクエストのレビュー

[内蔵ブラウザでのコンピューターの使用](/ja-JP/codex/browser?surface=app#app-computer-use-in-the-browser)により、
Codex はローカル開発サーバーやファイルから読み込んだページをクリック操作し、
問題を再現して修正を検証できます。対象となる承認リクエストには、
[承認リクエストの自動レビュー](/ja-JP/codex/sandboxing/auto-review)も利用でき、
アクションの実行前にレビューの状況とリスクが表示されます。

[4 月 23 日のリリースノートをご覧ください](/codex/changelog#codex-2026-04-23)。

## 2026 年 4 月 13 日～17 日

### プレビューと操作を一か所に集約

[内蔵ブラウザ](/ja-JP/codex/browser?surface=app)にライブプレビューとページへのコメント機能が加わり、
[コンピューターの使用](/ja-JP/codex/computer-use)では Codex が macOS アプリの画面を確認し、
操作できるようになりました。これらの機能により、画面の実装とエンドツーエンドの検証を、
コード変更と同じタスク内で行えるようになりました。

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### チャットから始めて、そのまま作業を継続

[単独チャット](/ja-JP/codex/projects#start-without-a-project)により、
プロジェクトフォルダーを選ばずに作業を始められるようになりました。
同じリリースでは、[チャット内のスケジュール済みタスク](/ja-JP/codex/automations#schedule-a-task-inside-a-chat)、
Pull Request のコンテキスト、より充実したファイルプレビュー、
複数のチャットにまたがる作業を支える[メモリ](/ja-JP/codex/customization/memories)が追加されました。

[4 月 16 日の Codex App リリースノート](/codex/changelog#codex-2026-04-16-app)をご覧ください。

## 2026 年 4 月 6 日～10 日

### アプリ内での Pull Request のレビューと変更の反映

レビュー機能に、折りたためるインラインコメントと、インライン表示および独立表示のレビューモードが追加され、Git とソースのコンテキストも分かりやすく表示されるようになりました。その後、Pull Request のアクティビティ、コメント、プッシュの選択肢も、ワークスペースのファイルタブとともにアプリ内で利用できるようになり、ツールを切り替えずに変更を確認して対応できるようになりました。

[4 月 9 日](/codex/changelog#codex-2026-04-09-app)と
[4 月 10 日](/codex/changelog#codex-2026-04-10-app)の Codex App リリースノート、または
[アプリ内で変更をレビューする方法](/ja-JP/codex/code-review?surface=app)をご覧ください。

## 2026 年 3 月 23 日～27 日

### ワークフローのプラグイン化

[プラグイン](/ja-JP/codex/plugins)が、スキル、コネクタ、MCP サーバーをまとめて
インストールできるパッケージとして登場しました。一連のワークフローを見つけてインストールし、共有しやすくなりました。
また、プラグインとスキルのページが刷新され、内容や状態が分かりやすくなりました。
同じ週には、過去のチャットを検索する機能も追加されました。

[タスク検索](/codex/changelog#codex-2026-03-24-app)、
[プラグインのリリース](/codex/changelog#codex-2026-03-25)、
[Codex App](/codex/changelog#codex-2026-03-25-app) のリリースノートをご覧ください。

## 2026 年 3 月 16 日～20 日

### 過去のメッセージからの分岐とコンポーザーでのツール選択

過去のメッセージからチャットをフォークできるようになり、
元の流れを残したまま、新しいアプローチを試しやすくなりました。下書き中もモデルや推論の設定コマンドを使えるようになり、
有効化したスキルは `@` メニューに表示されるようになりました。
また、GPT-5.4 mini が、軽量なタスクやサブエージェント向けのより高速な選択肢として加わりました。

[GPT-5.4 mini](/codex/changelog#codex-2026-03-17)、
[チャット操作](/codex/changelog#codex-2026-03-18-app)、
[スキルメニュー](/codex/changelog#codex-2026-03-19-app)のリリースノートをご覧ください。

## 2026 年 3 月 9 日～13 日

### 作業に合う環境でのスケジュール設定

[スケジュール済みタスク](/ja-JP/codex/automations)を、モデルと推論強度を明示的に指定して、
ローカルまたは Worktree 内で実行できるようになりました。再利用可能なテンプレートにより、
よく使うタスクをすばやく設定できるようになりました。
カスタムテーマでワークスペースも好みに合わせやすくなりました。

  
    
  

### Codex によるターミナル出力の確認

Codex は現在のチャットの[統合ターミナル](/ja-JP/codex/integrated-terminal#run-and-validate-your-project)も
読み取れるようになりました。ユーザーに出力の貼り付けを求めず、
実行中の開発サーバーやビルドの出力を直接確認できるようになりました。

[3 月 11 日](/codex/changelog#codex-2026-03-11-app)と
[3 月 12 日](/codex/changelog#codex-2026-03-12-app)の Codex App のリリースノートをご覧ください。

## 2026 年 3 月 2～6 日

### Windows での Codex のネイティブ実行

Codex App が [Windows](/ja-JP/codex/windows/windows-app) 向けに登場し、PowerShell とサンドボックスをネイティブにサポートするとともに、
Worktree、スケジュール済みタスク、スキルにも対応しました。
Linux 環境を好む開発者は、引き続き WSL を利用できました。

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### ローカルと Worktree 間でのチャットの移動

[ローカルと Worktree 間の引き継ぎ](/ja-JP/codex/environments/git-worktrees#working-between-local-and-worktree)により、
コンテキストを保ったまま進行中のチャットを移動できるようになりました。
同じ週には GPT-5.4 も Codex に登場し、
コーディング、コンピューターの使用、より長いコンテキストを扱うワークフローに対応しました。

[Windows 版の提供開始](/codex/changelog#codex-2026-03-04-app)、
[Worktree の引き継ぎ](/codex/changelog#codex-2026-03-03-app)、
[GPT-5.4](/codex/changelog#codex-2026-03-05) のリリースノートをご覧ください。

## 2026 年 2 月 9～13 日

### リアルタイムでのコード改善と別のアプローチへの分岐

GPT-5.3-Codex-Spark は、リアルタイムでコードの改善を繰り返せる、ほぼ即座に応答するモデルとしてリサーチプレビューでの提供を開始しました。アプリにはチャットのフォーク機能と、常に最前面に表示されるフローティングチャットウィンドウも追加され、別のアプローチを試したり、エディターやブラウザの横に Codex を表示しておいたりできるようになりました。

[Spark](/codex/changelog#codex-2026-02-12) と
[Codex App](/codex/changelog#codex-2026-02-12-app) のリリースノート、または
現在の[モデルガイド](/ja-JP/codex/models)をご覧ください。

## 2026 年 2 月 2～6 日

### macOS 向け Codex App の登場

Codex App は、プロジェクトのチャットを並行して進められるデスクトップワークスペースとして登場し、
組み込みの Git レビュー、Worktree、スキル、スケジュール済みタスク、音声入力を備えていました。
これらの機能は現在、[ChatGPT デスクトップアプリ](/ja-JP/codex/app)の Codex で利用できます。

  
    
  

### 進行中の作業の軌道修正とファイルの追加

ターン途中の軌道修正により、進行中の応答を中断することなく Codex に方針の変更を指示できるようになり、
画像以外のファイルも添付できるようになりました。
こうした仕組みが、Codex に必要なコンテキストとともに追加の指示を伝えて[軌道修正したり、指示をキューに追加したりする](/ja-JP/codex/prompting#steering-and-queuing)
ための基盤となりました。

[Codex App の提供開始時のリリースノート](/codex/changelog#codex-2026-02-02)と
[2 月 5 日のアプリのリリースノート](/codex/changelog#codex-2026-02-05-app)をご覧ください。
