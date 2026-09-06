<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/windows-deployment -->

使用者可以自行安裝 ChatGPT 桌面應用程式，您的 IT 團隊也可以
使用企業管理工具進行部署。此應用程式已由 Store 簽署，但
使用者無須開啟 Microsoft Store 即可安裝或更新。

## 讓使用者自行安裝及更新應用程式

如果使用者可以自行管理應用程式，請引導他們使用
[網頁安裝程式](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)。
此安裝程式提供標準安裝與自動更新
體驗。安裝或
更新期間可能會出現 Microsoft Store 元件，但使用者無須自行瀏覽 Store。

您也可以透過指令列安裝此應用程式：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## 使用企業管理工具部署應用程式

如果您的組織集中管理軟體，請使用 Microsoft Intune 或
其他相容的行動裝置管理（MDM）或軟體部署
平台。如果您的平台支援 Microsoft Store 應用程式部署，請在 Store 應用程式流程中搜尋
OpenAI 的 ChatGPT，或使用以下 Store 產品 ID：

```text
9PLM9XGG6VKS

如需設定詳細資訊，請參閱以下 Microsoft 文件：

- [企業部署指南](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Intune 部署指南](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [MECM 部署指南](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [將 Microsoft Store 應用程式新增至 Microsoft Intune](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### 管理應用程式更新

如需設定說明與推出指引，請參閱
[管理應用程式更新](/zh-Hant/codex/enterprise/manage-app-updates)。

## 不使用 Microsoft 散發服務進行安裝

如果您的環境無法使用 Microsoft 應用程式散發服務進行
初次安裝，請為每種裝置
架構下載由 Store 簽署的 MSIX 套件：

| 裝置架構 | 套件                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

這些固定連結指向每種
架構最新發佈且由 Store 簽署的套件。對於需要授權檔案的離線部署工作流程，
也請下載
[離線授權（`ChatGPT-License.xml`）](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml)。
請將適用的 MSIX 匯入您的 MDM
或軟體部署平台，並視需要一併匯入授權檔案。

初次安裝後，能連線至
`persistent.oaistatic.com` 的裝置可自動安裝更新，除非受管理的
組態停用應用程式的內建更新程式。如果您停用應用程式內
更新，請透過 MDM 或軟體部署工具部署較新的套件。

此部署方式：

- 支援在受限環境中進行初次安裝。
- 支援 x64 和 Arm64 裝置。
- 不提供獨立的 MSI，也不提供非 Store 版 EXE。

## 相關資源

- [管理應用程式更新](/zh-Hant/codex/enterprise/manage-app-updates)
- [Windows 版 ChatGPT 桌面應用程式](/zh-Hant/codex/app/windows)
