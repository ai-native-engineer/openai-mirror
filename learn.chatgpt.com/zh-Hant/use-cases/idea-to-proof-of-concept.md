<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/idea-to-proof-of-concept -->

## 先確立視覺方向

GPT Image 2 很擅長生成高品質 UI 模擬稿。探索新構想時，你不必從零開始，可以運用圖像生成來確立視覺方向。

有兩種做法：

- 使用 ImageGen 技能反覆調整視覺方向，對生成的 UI 設計感到滿意後，就可以要求 Codex 打造符合該視覺設計的原型。這種情況下，請選取 Codex、開始新對話，並附上你最終想實作的圖像，而不是直接繼續原本的 ChatGPT 對話。能參考使用者提供的附件時，Codex 的表現會更好。
- 只要使用外掛程式並描述你的構想即可：外掛程式會為你擬定視覺方向，並處理後續步驟。

## 善用外掛程式

如果在開始實作前不需要反覆調整視覺方向，你可以使用外掛程式並描述你的構想。

請使用 [Build Web Apps 外掛程式](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)
來製作 Web 應用程式、儀表板、創意網站和以前端為主的工具。其
工作流程會讓 Codex 先生成設計、用程式碼重現該設計，並使用
瀏覽器將結果與概念比對。

請使用 [Game Studio 外掛程式](https://github.com/openai/plugins/tree/main/plugins/game-studio)
來製作瀏覽器遊戲形式的概念驗證。在擴充遊戲之前，這套流程應先定義玩家
可執行的動作、第一個可玩的遊戲循環、引擎、素材工作流程、HUD、控制方式和瀏覽器
測試。

## 迭代工作流程

良好的概念驗證，應將範圍控制在可快速實作並與團隊共同驗證的 MVP。
若要確認 MVP 是否如預期運作，可以使用 Playwright interactive，讓 Codex 驗證自己的實作成果。

第一個版本正常運作後，你可以在同一個對話中提出範圍明確的變更要求，繼續進行迭代：
