<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/windows-deployment -->

用户可以自行安装 ChatGPT 桌面应用，您的 IT 团队也可以
使用企业管理工具部署该应用。该应用已由 Microsoft Store 签名，但
用户无需打开 Microsoft Store 即可安装或更新。

## 允许用户安装和更新应用

如果用户可以管理自己的应用，请引导他们使用
[Web 安装程序](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)。
该安装程序提供标准的安装和自动更新
体验。安装或
更新过程中可能会出现 Microsoft Store 组件，但用户无需自行浏览 Microsoft Store。

您也可以从命令行安装该应用：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore

## 使用企业管理工具部署应用

如果您的组织集中管理软件，请使用 Microsoft Intune 或
其他兼容的移动设备管理（MDM）或软件部署
平台。如果您的平台支持 Microsoft Store 应用部署，请在 Microsoft Store 应用部署流程中搜索
ChatGPT from OpenAI，或使用以下 Microsoft Store 产品 ID：

```text
9PLM9XGG6VKS

有关设置详情，请参阅以下 Microsoft 文档：

- [企业部署指南](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDVdo5pE5P3QKg5r0eieSvfAeE7cW0yy58ncBFW7OYajwU?e=dGH94F)
- [Intune 部署指南](https://1drv.ms/b/c/123ec1ed6c72a14a/IQDh_5o31T6XT7bUn5RPldEJAZX58gEuRr8YnJD7d2IMpec?e=nByKw6)
- [MECM 部署指南](https://1drv.ms/b/c/123ec1ed6c72a14a/IQB829f_TSbkR7-H9qA4Q9ntAa9D2He3qMjXksWi2ozdeg8?e=GTKgAl)
- [将 Microsoft Store 应用添加到 Microsoft Intune](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-microsoft-store)

<a id="manage-in-app-updates"></a>

### 管理应用更新

如需了解设置说明和部署指导，请参阅
[管理应用更新](/zh-Hans/codex/enterprise/manage-app-updates)。

## 在不使用 Microsoft 分发服务的情况下安装

如果您的环境无法使用 Microsoft 应用分发服务
完成初始安装，请下载经 Microsoft Store 签名且适用于每种设备
架构的 MSIX 软件包：

| 设备架构 | 软件包                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| x64                 | [ChatGPT-x64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-x64.msix)     |
| Arm64               | [ChatGPT-arm64.msix](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-arm64.msix) |

这些固定链接分别指向为每种
架构发布的最新软件包，且软件包均经 Microsoft Store 签名。对于需要许可证文件的离线部署工作流，
还请下载
[离线许可证（`ChatGPT-License.xml`）](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-License.xml)。
将相应的 MSIX 以及许可证文件（如有需要）导入您的 MDM
或软件部署平台。

初始安装完成后，能够访问
`persistent.oaistatic.com` 的设备可以自动安装更新，除非受管
配置禁用了应用的内置更新程序。如果您禁用了应用内
更新，请通过 MDM 或软件部署工具部署较新的软件包。

此部署方式：

- 支持在受限环境中进行初始安装。
- 支持 x64 和 Arm64 设备。
- 不提供独立的 MSI 或非 Store 版 EXE。

## 相关资源

- [管理应用更新](/zh-Hans/codex/enterprise/manage-app-updates)
- [Windows 版 ChatGPT 桌面应用](/zh-Hans/codex/app/windows)
