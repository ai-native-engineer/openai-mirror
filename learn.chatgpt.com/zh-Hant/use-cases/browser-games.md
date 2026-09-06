<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/browser-games -->

## 簡介

建置遊戲正是最能說明 Codex 不只協助生成程式碼的例子之一。真正的遊戲通常需要書面構想、算繪層、前端外殼開發、後端狀態管理、素材製作，以及持續調整視覺效果

若要讓這個使用案例發揮最佳效果，應先讓 Codex 明確寫下遊戲應具備的功能，再使用 Playwright interactive 在實際瀏覽器中測試遊戲並反覆改進。

## 從遊戲計畫開始

在讓 Codex 建立任何專案骨架之前，先要求它建立 `PLAN.md`，以具體方式定義遊戲：

- 玩家目標
- 主要循環
- 輸入方式與操作控制
- 勝利與失敗狀態
- 遊戲進程或難度
- 視覺風格
- 技術堆疊與託管方式的前提假設
- 里程碑的先後順序

這份計畫很重要，因為單是「建置遊戲」過於籠統。Codex 必須知道如何實作遊戲的每個部分，而且在建置過程中往往需要參照實作細節。

你可以使用 `/plan` 斜線指令啟用規劃模式。
將輸出內容儲存為 `PLAN.md` 檔案。

## 透過 AGENTS.md 引導 Codex 的行為

為確保 Codex 遵循計畫、驗證成果並使用合適的工具，請建立內容如下的 `AGENTS.md`：

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

如此一來，Codex 就能長時間自主執行，並視需要使用相關技能。

## 善用技能

加入 AGENTS.md 檔案中提到的技能：

- Imagegen，讓 Codex 能視需要生成遊戲的視覺素材
- Playwright interactive，讓 Codex 能在實際瀏覽器中測試遊戲
- OpenAI 文件，讓 Codex 能取得最新的 OpenAI API 文件
- 你也可以選擇新增 Context7 MCP 伺服器，以取得算繪框架的最新文件

如要進一步瞭解如何新增技能，請參閱 [技能文件](/zh-Hant/codex/build-skills)。

  **提示**：請 Codex 將圖像生成用的提示詞儲存在檔案中，以確保
  所有視覺素材的風格一致。說明你
  想生成的素材風格，並讓 Codex 撰寫可重複使用的詳細提示詞。

## 讓 Codex 執行並反覆改進

Codex 會根據初始計畫生成遊戲的第一個版本。

如果需要生成大量圖像素材，第一個版本可能會花上一段時間，有時甚至需要數小時。由於 Codex 能在實際瀏覽器中測試成果並試玩遊戲，因此即使你不提供任何輸入，它仍可長時間持續執行。

計畫定義得越明確，第一輪迭代後的最終成果就越好。

試玩時，你可以視需要提供螢幕截圖、要求變更遊戲玩法或更新視覺素材，持續反覆改進，直到對結果感到滿意。
