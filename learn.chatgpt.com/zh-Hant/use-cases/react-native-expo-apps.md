<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/react-native-expo-apps -->

## 從 Expo Go 開始

如果想讓 Codex 將行動應用程式構想轉化為一款
經過測試的 React Native 應用程式，Expo 是很理想的預設選擇。實用的迭代流程是先執行 `expo start`，接著透過 Expo Go
在裝置上測試；只有當應用程式需要
自訂原生程式碼、發布至應用程式商店，或 Expo Go 無法執行的功能時，才改用開發用戶端或 EAS 建置。

這樣可讓 Codex 專注於應用程式工作流程，不必在第一輪
就花時間設定原生 IDE 與模擬器、處理佈建，或設定建置組態。

## 使用 Expo 外掛程式

Expo 發布了一款 [Expo 外掛程式](https://docs.expo.dev/skills/)，為 Codex 提供 Expo 原生開發指引，涵蓋 Expo Router、原生 UI、表單、
導覽、動畫、資料擷取、NativeWind 設定、Expo 模組、開發
用戶端、部署、升級，以及 Codex Run 動作串接。

當 Codex 正在建置新的 Expo 畫面、加入套件、串接 API
呼叫、準備開發用戶端，或準備將應用程式發布至 TestFlight、App
Store、Play Store 或 EAS Hosting 時，請使用此外掛程式。

你也可以選擇加入 [Expo MCP 伺服器](https://docs.expo.dev/eas/ai/mcp/)；適用於任務需要查閱最新的
Expo 文件、安裝相容套件、進行 EAS 建置與
工作流程操作、擷取螢幕截圖、與模擬器互動、使用 React Native DevTools，
或存取 TestFlight 資料時。

## 迭代流程

1. 請 Codex 檢查程式碼庫，並確認這是新的 Expo 應用程式，還是
現有的 Expo 專案。
2. 從 Expo Router 和 Expo Go 開始，並使用 `npx expo install` 新增
   Expo 套件。
3. 請 Codex 建置一套完整的工作流程，納入具原生體驗的導覽、
載入狀態、空白狀態及錯誤狀態。
4. 採用最快且可行的方式驗證，例如在裝置或
模擬器上使用 Expo Go；只有在需要時，才改用開發用戶端或 EAS。

## 建議的後續提示詞
