<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/prisma-airs -->

連接 Palo Alto Networks Prisma AIRS，以便在
Codex 提示詞送達模型前套用您的安全性政策。工作區管理員只需為工作區設定一次
這項整合。

Prisma AIRS 可套用您在安全性設定檔中設定的防護措施，例如
資料外洩防護、提示注入偵測，以及惡意 URL
偵測。

## 開始之前

您需要：

- 啟用了 Prisma AIRS 存取權的 ChatGPT 工作區。請聯絡您的 OpenAI
客戶團隊以申請存取權。
- 工作區管理員權限。
- Prisma AIRS API 金鑰、已設定的安全性設定檔，以及您部署環境所使用的
服務端點。

## 連接 Prisma AIRS

1. 開啟 [Codex 資料控制項](https://chatgpt.com/codex/cloud/settings/data)，並以
   工作區管理員身分進行操作。
2. 在 **外部防護機制** 下找到 **Prisma AIRS**。如果這個區段無法
   使用，請聯絡您的 OpenAI 客戶團隊，要求為您的工作區啟用存取權。
3. 輸入您的 **API 金鑰**、**安全性設定檔** 名稱或 ID，以及 **端點
   URL**。
4. 選擇 **強制執行模式**，以及 **AIRS 失敗時** 的處理方式。
5. 選取 **儲存連線**。Codex 會驗證連線，並加密您的
   API 金鑰。
6. 選取 **測試連線**，以驗證已儲存的組態。
7. 開啟 **啟用 Prisma AIRS**，即可開始掃描整個
   工作區的提示詞。

僅儲存連線不會啟用掃描。您還必須開啟 **啟用
Prisma AIRS**。

## 選擇端點

請使用適用於 Prisma AIRS 部署的核准端點：

| 地區        | 端點                                                 |
| ------------- | -------------------------------------------------------- |
| 美國 | `https://service.api.aisecurity.paloaltonetworks.com`    |
| 德國       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| 印度         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| 新加坡     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

Codex 預設使用美國端點。工作區的資料駐留
需求可能會限制您可使用的端點。

## 選擇提示詞的處理方式

**強制執行模式** 決定 Prisma AIRS 標記提示詞時的處理方式：

- **封鎖**：在提示詞送達模型前加以封鎖。這是預設設定。
- **僅警示**：記錄偵測結果，並允許提示詞繼續處理。

**AIRS 失敗時** 決定 Prisma AIRS 無法使用或
未回應時的處理方式：

- **允許提示詞**：在未完成掃描的情況下繼續處理。這是預設設定。
- **封鎖提示詞**：暫停處理提示詞，直到 Prisma AIRS 能夠掃描為止。

如果您的安全性政策要求每則適用範圍內的提示詞
都必須取得掃描判定，請選擇 **封鎖提示詞**。

## 瞭解會掃描哪些內容

Codex 會將新提交的提示詞文字傳送至已設定的 Prisma AIRS 端點
進行檢查。這適用於涵蓋範圍內的 Codex 工作流程，包括 App、CLI、
IDE 擴充功能和雲端，前提是使用者已登入所設定的 ChatGPT
工作區。使用平台 API 金鑰完成身分驗證的工作階段不在涵蓋範圍內。請參閱
[強制使用登入方式或工作區](/zh-Hant/codex/auth#enforce-a-login-method-or-workspace)，
以要求使用指定的登入方式和工作區。

Prisma AIRS 不會透過這項整合掃描助理回覆、工具呼叫、工具結果、檔案，
也不會掃描圖像。您設定的安全性設定檔會決定
Prisma AIRS 偵測哪些威脅和敏感資料。

Codex 會加密您的 API 金鑰，且儲存後絕不再顯示。請先審查 Palo
Alto Networks 的資料處理、保留和駐留政策，再啟用
提示詞檢查。這些政策適用於傳送至 Prisma AIRS 的提示詞。

## 管理連線

返回 [Codex 資料控制項](https://chatgpt.com/codex/cloud/settings/data)
以管理這項整合：

- 選取 **測試連線**，以驗證您已儲存的 API 金鑰、安全性設定檔，
  以及端點。
- 輸入新金鑰並選取 **輪替 API 金鑰**，即可取代已儲存的金鑰，
  且不會變更其他設定。
- 關閉 **啟用 Prisma AIRS** 可停止掃描，同時保留已儲存的
  組態。
- 選取 **中斷連線**，然後確認，即可停止掃描並刪除已儲存的
  連線和 API 金鑰。

如需更全面的工作區設定與政策管理資訊，請參閱
[管理員導入指南](/zh-Hant/codex/enterprise/admin-setup) 和
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)。
