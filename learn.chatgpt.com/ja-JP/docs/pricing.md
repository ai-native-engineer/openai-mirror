<!-- source: https://learn.chatgpt.com/ja-JP/docs/pricing -->

<strong>ChatGPT Work と Codex は利用枠を共有します。</strong>
  ChatGPT 内での ChatGPT Work の利用には、Codex と同じ料金、クレジット、利用上限が適用されます。

<h2 class="sr-only">料金プラン</h2>

  <div data-content-switcher-pane data-value="individual">
    <div class="codex-pricing-grid">
      
      
      
        - Web、CLI、IDE 拡張機能、iOS で Codex を利用
        - 自動コードレビューや Slack 連携などのクラウドベースの連携機能
        - Sol、Terra、Luna を含む GPT-5.6 モデルファミリー
        - 軽量なワークロードや大量処理で、より高い利用上限が適用される GPT-5.6 Luna
        - [ChatGPT クレジット](#credits-overview)で利用枠を柔軟に拡張
        - Plus プランに含まれる
          その他の [ChatGPT の機能](https://chatgpt.com/pricing)
      
      
        - 日常的なコーディングタスク向けの高速な Codex モデル、GPT-5.3-Codex-Spark（リサーチプレビュー）へのアクセス
        - Plus の 5 倍または 20 倍の Codex 利用枠\*
        - 月額 $200 のプランでは ChatGPT 音声モードを無制限に利用可能。ただし、タスクは引き続き Codex の利用枠を消費
        - Pro プランに含まれる
          その他の [ChatGPT の機能](https://chatgpt.com/pricing)
      
      
        - CLI、SDK、または IDE 拡張機能で Codex を利用
        - クラウドベースの機能は利用不可（GitHub コードレビュー、Slack など）
        - お使いのキーでアクセスできる API モデルを利用可能
        - Codex の利用量に応じて、[API 料金](/api/docs/pricing)に基づき課金
      
    </div>

  </div>

  <div data-content-switcher-pane data-value="business-enterprise" hidden>
    <div class="codex-pricing-grid">
      
        - デスクトップアプリとモバイルアプリで ChatGPT と Codex を利用
        - クラウドチャットの実行を高速化する、より大規模な仮想マシン
        - [ChatGPT クレジット](#credits-overview)で利用枠を柔軟に拡張
        - 基本的な管理機能、SAML SSO、MFA を備えた、安全な専用ワークスペース
        - デフォルトでは、ビジネスデータを学習に使用しません。[詳しく見る
          ](https://openai.com/business-data/)
        - Business プランに含まれる
          その他の [ChatGPT の機能](https://chatgpt.com/pricing)
      
      
        - リクエストの優先処理
        - SCIM、EKM、ユーザー分析、ドメイン検証、
          ロールベースのアクセス制御（[RBAC](https://help.openai.com/en/articles/11750701-rbac)）を含む、
          エンタープライズレベルのセキュリティと管理機能
        - [Compliance
          API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Tasks) による監査ログと利用状況の監視
        - データ保持とデータレジデンシーの制御
        - Enterprise プランに含まれる
          その他の [ChatGPT の機能](https://chatgpt.com/pricing)
      
    </div>

    <div class="mt-8 mb-10 codex-pricing-grid">
      
        - CLI、SDK、IDE 拡張機能で利用できる Codex
        - クラウド機能は利用不可（GitHub のコードレビュー、Slack など）
        - 利用できるモデルは、その API キーで利用可能な API モデルに準じます
        - [API 料金](/api/docs/pricing)に基づく Codex の従量課金
      
    </div>

  </div>

## 友達や同僚の招待

対象ユーザーは、アプリ左下のプロファイルメニューから Codex の招待を送信できます。
対象の個人プランでは「 **友達を招待** 」、
対象の Business ワークスペースでは「 **同僚を招待** 」を選択します。
招待相手のメールアドレスを入力し、招待を送信してください。

招待ダイアログには、ご利用のプランやプロモーションに応じた現在の特典、招待相手の条件、招待人数の上限、特典の有効期限が表示されます。個人向けと Business 向けの紹介プログラムでは、特典と対象条件がそれぞれ異なります。現在、ChatGPT Enterprise では紹介プログラムを利用できません。

2026 年 6 月 11 日から 6 月 24 日まで、対象の Plus および Pro ユーザーは最大 3 人の友達を招待できます。
対象の招待相手が初めて Codex メッセージを送信すると、
招待した人と招待された人の双方に、後から使えるレート制限のリセットが 1 回分付与されます。
リセットは付与日から 30 日間利用できます。
Business の紹介プログラムでは、共有ワークスペース向けのクレジット特典が別途適用されます。
招待を送信する前に、[現在の利用規約](https://help.openai.com/en/articles/20001271)を
確認してください。

## よくある質問

### Sites の料金

パブリックベータ期間中、[Sites](/ja-JP/codex/sites) は対象の ChatGPT プランに含まれます。
利用できるかどうかは、プラン、地域、ワークスペースの設定によって異なります。

### プランごとの利用上限

送信できるメッセージ数は、使用するモデル、タスクの規模や複雑さ、ローカルとクラウドのどちらで実行するかによって異なります。小規模なスクリプトや定型的な関数では、利用枠の消費がごくわずかで済む場合があります。一方、大規模なプロジェクト、長時間実行するタスク、エージェントがより多くのコンテキストを保持する必要がある長時間のセッションでは、1 メッセージあたりの消費量が大幅に増えます。

似たようなタスクでも、利用枠の消費量は異なる場合があります。モデルの選択、コンテキスト、推論、ツールの使用、情報取得、キャッシュの利用がすべて使用量に影響するため、プロンプトの長さだけでは正確に見積もれません。

作業に最適な GPT-5.6 モデルを選択してください。

- **Sol** は、複雑な推論、曖昧な問題、
  高度なコーディング、重大な意思決定など、最も難度の高い作業向けに設計されています。
- **Terra** は、実運用のタスク、レポート作成、ドキュメント分析、
  コーディング、的確な判断が求められる作業を日常的に支える主力モデルです。
- **Luna** は、ルーティング、分類、抽出、
  サポート、バックグラウンドでの自動化、範囲を絞ったコーディングタスクなど、
  大量の作業を高速に処理する用途に最適化されています。

<div id="usage-limits">

以下は、5 時間あたりに送信できるローカルメッセージ数の目安です。
ChatGPT プランのクラウドチャットでは GPT-5.6 Sol が使用され、ローカルメッセージよりも利用枠を多く消費する場合があります。
これらは推定値であり、メッセージ数の上限が固定されているわけではありません。
現在の上限とリセット時刻は、[利用状況ダッシュボード](#where-can-i-see-my-current-usage-limits)で
確認してください。

</div>

  <thead class="whitespace-nowrap">
    <tr>
      <th scope="col">モデル</th>
      <th scope="col" style="text-align:center">
        Plus
      </th>
      <th scope="col" style="text-align:center">
        Pro 5x
      </th>
      <th scope="col" style="text-align:center">
        Pro 20x
      </th>
      <th scope="col" style="text-align:center">
        標準の Business
      </th>
      <th scope="col" style="text-align:center">
        API キー
      </th>
    </tr>
  </thead>
  <tbody class="whitespace-nowrap">
    <tr>
      <td>GPT-6 Astra</td>
      <td style="text-align:center">5-45</td>
      <td style="text-align:center">25-225</td>
      <td style="text-align:center">100-900</td>
      <td style="text-align:center">5-45</td>
      <td style="text-align:center">
        [従量課金](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.6 Sol</td>
      <td style="text-align:center">10-100</td>
      <td style="text-align:center">50-500</td>
      <td style="text-align:center">200-2,000</td>
      <td style="text-align:center">10-100</td>
      <td style="text-align:center">
        [従量課金](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.6 Terra</td>
      <td style="text-align:center">25-200</td>
      <td style="text-align:center">125-1,000</td>
      <td style="text-align:center">500-4,000</td>
      <td style="text-align:center">25-200</td>
      <td style="text-align:center">
        [従量課金](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.6 Luna</td>
      <td style="text-align:center">250-2,000</td>
      <td style="text-align:center">1,250-10,000</td>
      <td style="text-align:center">5,000-40,000</td>
      <td style="text-align:center">250-2,000</td>
      <td style="text-align:center">
        [従量課金](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.5</td>
      <td style="text-align:center">15-80</td>
      <td style="text-align:center">75-400</td>
      <td style="text-align:center">300-1,600</td>
      <td style="text-align:center">15-80</td>
      <td style="text-align:center">
        [従量課金](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.4</td>
      <td style="text-align:center">20-100</td>
      <td style="text-align:center">100-500</td>
      <td style="text-align:center">400-2,000</td>
      <td style="text-align:center">20-100</td>
      <td style="text-align:center">
        [従量課金](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
    <tr>
      <td>GPT-5.4 mini</td>
      <td style="text-align:center">60-350</td>
      <td style="text-align:center">300-1,750</td>
      <td style="text-align:center">1,200-7,000</td>
      <td style="text-align:center">60-350</td>
      <td style="text-align:center">
        [従量課金](https://platform.openai.com/docs/pricing)
      </td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="6" style="text-align:center">
        ローカルメッセージとクラウドチャットは、プランの利用枠を共有します。週単位の上限も適用される場合があります。
      </td>
    </tr>
    <tr>
      <td colspan="6" style="text-align:center">
        柔軟な料金体系を利用する Enterprise/Edu ユーザーには固定のレート制限はなく、
        [クレジット](#credits-overview)に応じて利用量を増やせます。
      </td>
    </tr>
    <tr>
      <td colspan="6" style="text-align:center">
        柔軟な料金体系を利用しない Enterprise および Edu プランでは、ほとんどの機能で、シートあたりの利用上限が Plus と同じです。
      </td>
    </tr>
  </tfoot>

Business（$100）には、Pro 5x の目安が適用されます。

他のエージェント型機能の料金が適用されると、それらの機能と利用上限を共有します。
現在は、Plus と Pro の [ChatGPT for
Excel](https://help.openai.com/articles/20001063) が対象です。

速度設定を変更すると、対象となるすべてのモデルでクレジット消費量が増えるため、
プランに含まれる利用枠もより速く消費します。Fast モードでは、対応モデルのクレジット消費率が高くなります。
対応モデルと料金については、[速度](/ja-JP/codex/agent-configuration/speed)をご覧ください。
画像生成でも、画質や画像サイズに応じて、プランに含まれる利用枠を平均で約 3～5 倍速く消費します。
GPT-5.3-Codex-Spark は ChatGPT Pro ユーザー限定のリサーチプレビューとして提供されており、
提供開始時点では API で利用できません。
低レイテンシーに特化したハードウェアで動作するため、別の利用上限が適用されます。
この上限は需要に応じて調整される場合があります。

### デスクトップの ChatGPT 音声モード

デスクトップの ChatGPT 音声モードには、プランに応じた別の利用枠があり、直近 5 時間の使用量で計測されます。音声で開始したタスクには、既存の Codex 利用枠が使われます。どちらかの上限に達すると、ChatGPT から通知されます。

リアルタイムの会話は GPT-Live が担当します。
既存の Codex タスクで音声を使用すると、そのタスクで選択されているモデルが作業を処理します。
利用条件とセットアップについては、[ChatGPT 音声モード](/ja-JP/codex/features/voice#start-talking)をご覧ください。

- **Plus：** 約 15～30 分
- **Pro 5x（月額 $100）：** 約 1～2.5 時間
- **Pro 20x（月額 $200）：** 音声を無制限に利用可能
- **Business：** 約 45 分
- **Enterprise / Edu（従来プラン）：** 約 45 分

音声を無制限に利用できても、Codex タスクが無制限になるわけではありません。ChatGPT 音声モードで開始したタスクは、引き続き既存の Codex 利用枠を消費します。

クレジット制または従量課金制の Business、Edu、Enterprise ワークスペースでは、デスクトップの音声機能の料金は 1 分あたり約 6 クレジットです。現在、デスクトップの ChatGPT 音声モードは API キーでは利用できません。

### 利用上限に達した場合の動作

進行中の作業は最後まで完了できるようにしたいと考えています。ターンの実行中に利用上限に達しても、公平な利用のための制限の範囲内で、エージェントはそのターンの作業を続けられます。

利用上限に達した ChatGPT Plus および Pro ユーザーは、追加のクレジットを購入することで、現在のプランをアップグレードせずに作業を続けられます。

[柔軟な
料金体系](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)を利用する Business、Edu、エンタープライズプランでは、
ワークスペース用のクレジットを追加購入して作業を続けられます。

使用上限に近づいている場合は、より小さいモデルに切り替えて、残りの利用枠を長く使うこともできます。

すべてのユーザーは、API キーを使ってローカルチャットを追加で実行することもできます。
その使用量には、[標準の API 料金](https://platform.openai.com/docs/pricing)が適用されます。

<a id="image-generation-usage-limits"></a>

### 画像生成と使用制限の関係

画像生成には、ローカルメッセージやクラウドチャットと
共通の使用制限が適用されます。画像生成を伴うターンでは、
画像の品質やサイズに応じて、画像生成を伴わない同様のターンよりも
プランに含まれる利用枠を平均で 3～5 倍のペースで消費します。利用枠を使い切った後は、
画像生成にも[クレジット](#credits-overview)が使用されます。

無料プランでは画像生成を利用できません。API キーで Codex を使用する場合、画像生成には ChatGPT のプランに含まれる利用枠ではなく、API 料金が適用されます。

### 現在の使用制限の確認方法

現在の使用制限は、[使用状況
ダッシュボード](https://chatgpt.com/codex/settings/usage)で確認できます。
Codex CLI セッションの実行中に残りの利用枠を確認するには、`/status` を使用できます。

1～2 週間ごとにダッシュボードを確認し、使用ペースと残りの利用枠を把握してください。使用量が想定より多い場合は、より小さいモデルに切り替えたり、タスクの範囲を絞ったりしても、有用な結果が得られるか検討してください。

### トークンとクレジットとは

トークンは、ChatGPT が読み書きする情報の小さな単位です。プロンプト、ファイル、チャット履歴、ツールの結果、ChatGPT の応答のすべてにトークンが使用されます。

クレジットは、クレジットベースのプランで、対象となる使用量の支払いに使う単位です。プランに含まれる利用枠を使い切った後も、利用可能なクレジットがあれば作業を続けられます。クレジットの購入価格と適用される割引は、プランや契約によって異なります。

#### トークン単価

以下のトークン単価は、入力トークン、キャッシュ済み入力トークン、
出力トークンそれぞれについて、100 万トークンあたりのクレジット数で示しています。[トークンの
詳細はこちら](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)をご覧ください。

Fast モードでは、Astra の標準レートの 2.5 倍が適用されます。

エンタープライズプランをご利用のごく一部のお客様は、新しいトークンベースの料金体系への移行が完了するまで、
引き続き従来の料金表をご利用ください。詳しくは、
[OpenAI の営業担当に
お問い合わせください](https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex)。

<div id="credits-overview">
  <table>
    <thead>
      <tr>
        <th scope="col">100 万トークンあたりのクレジット数</th>
        <th scope="col" style="text-align:center">
          入力トークン
        </th>
        <th scope="col" style="text-align:center">
          キャッシュ済み入力トークン
        </th>
        <th scope="col" style="text-align:center">
          出力トークン
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>GPT-6 Astra</td>
<td style="text-align:center">250 クレジット</td>
<td style="text-align:center">25 クレジット</td>
<td style="text-align:center">1,250 クレジット</td>
      </tr>
      <tr>
        <td>GPT-5.6 Sol</td>
<td style="text-align:center">100 クレジット</td>
<td style="text-align:center">10 クレジット</td>
<td style="text-align:center">500 クレジット</td>
      </tr>
      <tr>
        <td>Daybreak Blue</td>
<td style="text-align:center">100 クレジット</td>
<td style="text-align:center">10 クレジット</td>
<td style="text-align:center">500 クレジット</td>
      </tr>
      <tr>
        <td>Daybreak Red</td>
<td style="text-align:center">312.5 クレジット</td>
<td style="text-align:center">31.25 クレジット</td>
<td style="text-align:center">1875 クレジット</td>
      </tr>
      <tr>
        <td>GPT-5.6 Terra</td>
<td style="text-align:center">50 クレジット</td>
<td style="text-align:center">5 クレジット</td>
<td style="text-align:center">300 クレジット</td>
      </tr>
      <tr>
        <td>GPT-5.6 Luna</td>
<td style="text-align:center">5 クレジット</td>
<td style="text-align:center">0.5 クレジット</td>
<td style="text-align:center">30 クレジット</td>
      </tr>
      <tr>
        <td>GPT-5.5</td>
<td style="text-align:center">125 クレジット</td>
<td style="text-align:center">12.50 クレジット</td>
<td style="text-align:center">750 クレジット</td>
      </tr>
      <tr>
        <td>GPT-5.4</td>
<td style="text-align:center">62.50 クレジット</td>
<td style="text-align:center">6.250 クレジット</td>
<td style="text-align:center">375 クレジット</td>
      </tr>
      <tr>
        <td>GPT-5.4 mini</td>
<td style="text-align:center">18.75 クレジット</td>
<td style="text-align:center">1.875 クレジット</td>
<td style="text-align:center">113 クレジット</td>
      </tr>
      <tr>
        <td>GPT-5.3-Codex-Spark</td>
        <td colspan="3" style="text-align:center">
          リサーチプレビュー
        </td>
      </tr>
      <tr>
        <td>GPT-Image-2（画像）</td>
<td style="text-align:center">200 クレジット</td>
<td style="text-align:center">50 クレジット</td>
<td style="text-align:center">750 クレジット</td>
      </tr>
      <tr>
        <td>GPT-Image-2（テキスト）</td>
<td style="text-align:center">125 クレジット</td>
<td style="text-align:center">31.25 クレジット</td>
<td style="text-align:center">250 クレジット</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="4" style="text-align:center">
          GPT-5.6 の利用では、メッセージ 1 件あたり平均 5～30 クレジットを消費します。
        </td>
      </tr>
      <tr>
        <td colspan="4" style="text-align:center">
          対応モデルで Fast モードを使用すると、クレジットの消費レートが高くなります。
レートについては、<a href="/codex/agent-configuration/speed">速度</a>を参照してください。
        </td>
      </tr>
      <tr>
        <td colspan="4" style="text-align:center">
          Daybreak を利用するには、[Trusted Access for
          Cyber](/ja-JP/codex/cyber-safety#trusted-access-for-cyber) の承認が必要です。
          Daybreak Blue には GPT-5.6 Sol と同じクレジットレートが適用されます。Daybreak Red には、
          別途承認とプロビジョニングが必要です。
        </td>
      </tr>
    </tfoot>
  </table>
</div>

_GPT-5.6 Sol のプロモーション料金は、少なくとも 2026 年 11 月 21 日までご利用いただけます。_

速度設定により、対象となるすべてのモデルでクレジット消費量が増加します。
対応モデルで Fast モードを使用すると、クレジットの消費レートが高くなります。
対応モデルとレートについては、[速度](/ja-JP/codex/agent-configuration/speed)を参照してください。

[ChatGPT Plus と Pro のクレジットについて、
詳しくはこちらをご覧ください。](https://help.openai.com/en/articles/12642688)

[ChatGPT Business、ChatGPT Enterprise、ChatGPT Edu のクレジットについて、
詳しくはこちらをご覧ください。](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)

Business およびエンタープライズ / Edu のクレジット課金については、<a href="https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing" target="_blank" rel="noopener noreferrer">クレジットベースの料金表</a>をご利用ください。エンタープライズの契約で米ドル建ての従量課金が指定されている場合は、代わりに<a href="https://help.openai.com/en/articles/20001415-chatgpt-rate-card-enterprise-token-based-pricing" target="_blank" rel="noopener noreferrer">エンタープライズの米ドル建て料金表</a>と契約内容をご確認ください。ワークスペース管理者は、[ChatGPT Work の使用状況とコスト](/codex/enterprise/chatgpt-work-usage-and-cost#understand-tokens-and-credits)も確認できます。

### コードレビューの使用量に含まれるもの

コードレビューの使用量として計上されるのは、Codex が GitHub を通じてレビューを実行する場合に限られます。
たとえば、Pull Request で `@Codex` をタグ付けしてレビューを依頼する場合や、
リポジトリで自動レビューを有効にする場合が該当します。ローカル環境や GitHub 以外で実行したレビューには、
通常の使用制限が適用されます。

### 利用枠をより長く使うための工夫

上記の使用制限とクレジット数は平均値です。利用枠を最大限に活用するには、以下の方法をお試しください。

- **プロンプトの長さを調整してください。** エージェントへの指示は正確に伝え、
  不要なコンテキストは省いてください。
- **参照資料を絞り込んでください。** 関連するファイルだけを提供し、
  可能な場合は参照元や対象期間も限定してください。
- **目的に合った出力を指定してください。** 想定読者、形式、長さを明確にし、
  必須の作業と任意の改善を区別してください。
- **AGENTS.md の内容をコンパクトにしてください。** 大規模なプロジェクトでは、
  AGENTS.md ファイルを[リポジトリ内の
  各階層に配置する](/ja-JP/codex/agent-configuration/agents-md#layer-project-instructions)ことで、それらのファイルを通じて渡すコンテキストの量を調整できます。
- **使用する MCP サーバーの数を制限してください。** 
[MCP](/ja-JP/codex/extend/mcp) サーバーを追加するたびにメッセージのコンテキストが増え、利用枠の消費量も増加します。
  不要な MCP サーバーは無効にしてください。
- **日常的なタスクでは、より小さいモデルに切り替えてください。** GPT-5.6 Terra または
  GPT-5.6 Luna を使うと、切り替え前のモデルによっては、
  ローカルメッセージの利用枠をより長く使えます。

タスクの選び方や範囲の決め方については、[Work の
効率的な活用](/ja-JP/codex/prompting#use-work-efficiently)を参照してください。

## 機能の提供状況

<div
  id="codex-plan-region-limits"
  className="not-prose mt-3 text-sm text-secondary"
>
  <sup>\*</sup> この機能は現在、特定の地域でのみ利用できます。地域制限の詳細については、
  各機能のドキュメントをご確認ください。
</div>
<div
  id="codex-plan-plugin-limits"
  className="not-prose mt-1 text-sm text-secondary"
>
  <sup>†</sup> 一部のファーストパーティ製プラグインは利用できません。
</div>
