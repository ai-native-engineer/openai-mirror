<!-- source: https://learn.chatgpt.com/ja-JP/docs/linux/linux-app -->

Linux 向け ChatGPT デスクトップアプリはプレビュー版として提供されています。お使いの Linux ディストリビューションとプロセッサーアーキテクチャに対応するパッケージをインストールし、ChatGPT アカウントでサインインすると、プロジェクト、ローカルファイル、Codex を利用できます。

## 対応ディストリビューションとアーキテクチャ

プレビュー版は、以下の Linux ディストリビューションのデスクトップ版に対応しています。

- Ubuntu 24.04 LTS および 26.04 LTS
- Debian 13
- Fedora 43 および 44

対応する各ディストリビューションには、x64 および ARM64 プロセッサー向けのパッケージがあります。プロセッサーのアーキテクチャを確認するには、次のコマンドを実行します。

```bash
uname -m

出力が `x86_64` の場合は x64 プロセッサーです。出力が `aarch64` または
`arm64` の場合は ARM64 プロセッサーです。

## 適切なパッケージのダウンロード

Ubuntu または Debian では `.deb` を、Fedora では `.rpm` を選択します。

| ディストリビューション     | アーキテクチャ | ダウンロード                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu または Debian | x64          | [x64 向け `.deb` をダウンロード](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu または Debian | ARM64        | [ARM64 向け `.deb` をダウンロード](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [x64 向け `.rpm` をダウンロード](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [ARM64 向け `.rpm` をダウンロード](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## Ubuntu または Debian へのインストール

お使いのプロセッサーアーキテクチャに対応する `.deb` パッケージをダウンロードします。
次にターミナルを開き、パッケージがあるディレクトリに移動して、
`apt` でインストールします。

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

ARM64 の場合は、`chatgpt_amd64.deb` を `chatgpt_arm64.deb` に置き換えます。

アプリケーションメニューから **ChatGPT** を開くか、ターミナルで `chatgpt` を実行します。
ChatGPT アカウントでサインインし、
[デスクトップアプリのクイックスタート](/ja-JP/codex/quickstart?setup=app)に従ってください。

## Fedora へのインストール

お使いのプロセッサーアーキテクチャに対応する `.rpm` パッケージをダウンロードします。
次にターミナルを開き、パッケージがあるディレクトリに移動して、
`dnf` でインストールします。

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

ARM64 の場合は、`chatgpt.x86_64.rpm` を `chatgpt.aarch64.rpm` に置き換えます。

アプリケーションメニューから **ChatGPT** を開くか、ターミナルで `chatgpt` を実行します。
ChatGPT アカウントでサインインし、
[デスクトップアプリのクイックスタート](/ja-JP/codex/quickstart?setup=app)に従ってください。

## アプリの更新

このパッケージをインストールすると、署名済みの OpenAI パッケージリポジトリが設定されます。その後のアップデートは、お使いのディストリビューションのパッケージマネージャーでインストールします。

Ubuntu または Debian では、次のコマンドを実行します。

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

Fedora では、次のコマンドを実行します。

```bash
sudo dnf upgrade --refresh chatgpt

## 互換性と制限事項

プレビュー版は、
[対応ディストリビューションとアーキテクチャ](#supported-distributions-and-architectures)に記載されたデスクトップディストリビューションに対応しています。
その他の Linux ディストリビューションでも動作する可能性はありますが、正式にはサポートされていません。

一部の機能には、個別のプラットフォーム要件があります。たとえば、
[コンピューターの使用](/ja-JP/codex/computer-use)は macOS と Windows で利用できますが、
Linux のプレビュー版ではまだ利用できません。今後のリリースで Linux への対応が追加されます。

## Wayland 対応

Wayland のネイティブ対応は試験段階で、今後も改善されます。Wayland セッションでは、利用可能な場合にアプリが XWayland を使用します。Wayland をネイティブで使用するよう明示的に指定するには、アプリを完全に終了し、ターミナルから起動します。

```bash
chatgpt --ozone-platform=wayland

Wayland のネイティブ対応が成熟するまで、フローティングウィンドウ、ウィンドウの位置指定、フォーカス、キーボードショートカットなどの機能が完全には動作しない場合があります。

## 次のステップ

- [デスクトップアプリのクイックスタート](/ja-JP/codex/quickstart?setup=app)に従ってください。
- ブラウザ連携のために、[Chrome 拡張機能](/ja-JP/codex/chrome-extension)を設定します。
- ローカルプロジェクトとコマンドに関する[権限](/ja-JP/codex/permissions)を確認します。
