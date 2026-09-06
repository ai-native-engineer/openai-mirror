<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/windows-deployment -->

ユーザー自身が ChatGPT デスクトップアプリをインストールすることも、IT チームが
エンタープライズ管理ツールを使用してデプロイすることもできます。このアプリは Store 署名済みですが、
インストールや更新のためにユーザーが Microsoft Store を開く必要はありません。

## ユーザーによるアプリのインストールと更新

自分のアプリケーションを管理できるユーザーには、次のインストーラーを案内します：
[Web インストーラー](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)。
このインストーラーでは、標準のインストールと自動更新を
利用できます。インストールまたは
更新中に Microsoft Store のコンポーネントが表示されることがありますが、ユーザー自身が Microsoft Store を閲覧する必要はありません。

コマンドラインからアプリをインストールすることもできます：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## エンタープライズ管理ツールによるアプリのデプロイ

組織でソフトウェアを一元管理している場合は、Microsoft Intune または
互換性のある別のモバイルデバイス管理（MDM）もしくはソフトウェアデプロイ
プラットフォームを使用します。利用しているプラットフォームが Microsoft Store アプリのデプロイに対応している場合は、Store アプリのフローで
ChatGPT from OpenAI を検索するか、次の Store 製品 ID を使用します：

```text
9PLM9XGG6VKS

セットアップの詳細については、以下の Microsoft ドキュメントを参照してください：

- [エンタープライズ向けデプロイガイド](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Intune デプロイガイド](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [MECM デプロイガイド](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [Microsoft Store アプリを Microsoft Intune に追加](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### アプリ更新の管理

セットアップ手順とロールアウトのガイダンスについては、次のページを参照してください：
[アプリ更新の管理](/ja-JP/codex/enterprise/manage-app-updates)。

## Microsoft の配布サービスを使用しないインストール

お使いの環境で Microsoft のアプリ配布サービスを
初回インストールに使用できない場合は、Store 署名済みの MSIX パッケージをデバイスの
アーキテクチャごとにダウンロードしてください：

| デバイスのアーキテクチャ | パッケージ                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

これらの固定リンクのリンク先は、それぞれの
アーキテクチャ向けに公開されている最新の Store 署名済みパッケージです。ライセンスファイルが必要なオフラインデプロイのワークフローでは、
次のファイルもダウンロードしてください：
[オフラインライセンス（`ChatGPT-License.xml`）](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml)。
適切な MSIX と、必要に応じてライセンスファイルを MDM
またはソフトウェアデプロイプラットフォームに取り込んでください。

初回インストール後は、
`persistent.oaistatic.com` にアクセスできるデバイスで、管理対象の
構成によってアプリ内蔵のアップデーターが無効化されていない限り、更新を自動的にインストールできます。アプリ内
更新を無効にする場合は、MDM またはソフトウェアデプロイツールを通じて新しいパッケージをデプロイしてください。

このデプロイ方法：

- 制限のある環境での初回インストールに対応します。
- x64 および Arm64 デバイスに対応します。
- スタンドアロンの MSI や、Store を介さない EXE は提供されません。

## 関連リソース

- [アプリ更新の管理](/ja-JP/codex/enterprise/manage-app-updates)
- [Windows 向け ChatGPT デスクトップアプリ](/ja-JP/codex/app/windows)
