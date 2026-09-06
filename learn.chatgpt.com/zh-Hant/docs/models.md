<!-- source: https://learn.chatgpt.com/zh-Hant/docs/models -->

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## 選擇模型

在 ChatGPT 桌面版應用程式中，使用撰寫工具下方的模型與推理控制項，
選擇可用的模型並調整其推理強度。

較高的推理強度可改善複雜任務的結果，但需要
更多時間，也會使用更多 Token。請先使用預設強度，
在任務需要更深入的規劃或分析時再提高強度。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式不侷限於
由單一智慧體執行任務。它會使用
[子代理程式](/codex/agent-configuration/subagents)加速處理複雜工作，
因此適合可拆分給多個子代理程式處理的大型任務。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## 選擇模型

這些建議適用於網頁版 **ChatGPT Work** 。使用
撰寫工具下方的模型與推理控制項，選擇可用的模型
並調整其推理強度。

較高的推理強度可改善複雜任務的結果，但需要
更多時間，也會使用更多 Token。請先使用預設強度，
在任務需要更深入的規劃或分析時再提高強度。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式不侷限於
由單一智慧體執行任務。它會使用
[子代理程式](/codex/agent-configuration/subagents)加速處理複雜工作，
因此適合可拆分給多個子代理程式處理的大型任務。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(22rem,25rem)] lg:items-start">
  <div class="min-w-0">

## 選擇模型

在互動式 CLI 工作階段中，使用 `/model` 切換模型或調整
推理程度。啟動 Codex 時，你也可以使用
`--model` 或其別名 `-m` 選擇模型：

相同選項也適用於非互動式執行。例如：

提高推理程度可以改善複雜任務的結果，但需要更長時間，
也會使用更多 Token。請先使用預設的推理程度，
在任務需要更深入的規劃或分析時再提高。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式不限於
由單一智慧體執行任務。它會透過
[子代理程式](/codex/agent-configuration/subagents)加速處理複雜工作，
適合可拆分給多個子代理程式處理的大型任務。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## 選擇模型

使用撰寫工具下方的模型切換器，選擇可用的模型與
推理程度。

提高推理程度可以改善複雜任務的結果，但需要更長時間，
也會使用更多 Token。請先使用預設的推理程度，
在任務需要更深入的規劃或分析時再提高。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式不限於
由單一智慧體執行任務。它會透過
[子代理程式](/codex/agent-configuration/subagents)加速處理複雜工作，
適合可拆分給多個子代理程式處理的大型任務。

  </div>
  
</div>

<a id="recommended-models"></a>
<a id="other-models"></a>
<a id="deprecated-codex-models"></a>
<a id="configure-your-default-local-model"></a>
<a id="choose-a-model-for-cloud-tasks"></a>
<a id="gpt-6-astra"></a>

## 推薦模型

<a id="app-compare-models"></a>

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  

  

</div>

可用性取決於推出進度、登入方式及所用的用戶端。
如需瞭解各方案的存取權與用量，請參閱[定價](/zh-Hant/codex/pricing)；
如需瞭解企業存取權，請參閱
[工作區模型可用性](/zh-Hant/codex/enterprise/workspace-model-availability#gpt-6-astra-in-enterprise)。

  請先使用帳戶可用的預設效能設定。朝
**更聰明** 調整可獲得更深入的推理，朝 **更快** 調整則能以更快的速度、更低的成本完成工作。
  若要使用 `gpt-5.6-luna` 或指定模型、推理強度
  或速度，請開啟 **進階** 。

選擇器示意圖顯示的是 GPT-5.6 控制項。對符合資格的 Pro、Business ($100) 和企業帳戶，Astra 推出後會將效能選項更新為 Terra 輕度、Sol 輕度、Sol 中、Astra 輕度、Astra 中及 Astra 極高。選項可能因方案及推出階段而異。

### 實驗性上下文管理

在支援的 Codex 用戶端上，使用 ChatGPT Plus 或 Pro 登入的使用者可以選擇啟用實驗性上下文管理。Astra 會跨上下文視窗保留筆記，並可搜尋同一任務中較早的訊息與工具結果。這項實驗預設關閉，推出時不開放給使用 Business、企業帳戶或 API 金鑰登入的使用者。

若要啟用，請在 `config.toml` 中設定 `features.context_management.experimental_mode = true`，
然後開始新任務。設定詳情請參閱[組態參考資料](/zh-Hant/codex/config-file/config-reference)，
檔案位置則請參閱[組態基本概念](/zh-Hant/codex/config-file/config-basic)。
工作區的要求仍然適用。

<a id="choosing-sol-terra-and-luna"></a>

## 如何選擇 Astra、Sol、Terra 和 Luna

若任務涉及多個步驟與工具，
且需要最強的能力，請選擇 **Astra** 。 **Sol** 擅長深入處理並精修成果， **Terra** 適合日常工作，
 **Luna** 則適合明確、可重複的任務。

### 各模型的強項

- **Astra，適合最棘手的端到端工作。** 若完整工作流程涵蓋程式碼、應用程式與研究，
  並需要持續推理與判斷，請選擇 Astra。
  請提供來源、範本、限制條件與檢查標準，
  讓它明確掌握什麼樣的成果才有用。Astra 更擅長提出有針對性的問題並納入你的指引，
  同時兼顧原始目標與限制條件。
- **Sol，適合複雜、開放式的工作。** 若任務需求不明確、難度高或價值高，
  而且需要更多分析、判斷或潤飾，請選擇 Sol，例如
  複雜的程式碼變更、深度研究，或需要精心潤飾的文件。對於範圍較窄的任務，
  請明確訂出完成標準，讓工作保持聚焦。
- **Terra，務實的全方位選擇。** 如果日常工作需要強大的推理與工具使用能力，
  但不需要像 Sol 那樣深入，請選擇 Terra。
  過去交給 GPT-5.5 處理的工作，也很適合先從 Terra 開始。
- **Luna，適合明確、可重複的任務。** 如果清楚什麼樣的成果才符合要求，請選擇 Luna 處理
  需求具體、數量多的任務，例如擷取、
  分類、轉換與結構化摘要。

### 選擇推理強度

請使用能產生所需結果的最低推理強度。遇到需要更多規劃、分析或檢查的任務時，再提高強度。

- ChatGPT 桌面版應用程式、網頁版 ChatGPT Work 和 IDE 擴充功能中的**輕度** ，或
  CLI 中的 **低** ，適合快速且範圍明確的任務。
- **中** 可兼顧速度與深度，適合需要更多規劃的任務。
- **高** 和 **極高** 適合涉及多個步驟、來源
  或取捨的困難工作。

GPT-5.5 與 GPT-5.6 的推理強度並無完全對應的關係。請先以較低的設定嘗試一項熟悉的任務，再依結果調整。

### 瞭解何時使用 Max 或 Ultra

**Max** 讓所選模型有更多時間針對單一任務進行推理。
處理最棘手的問題，且推理深度比速度或用量更重要時，請使用 Max。
若在選項中看不到 Max，就需要在應用程式設定中啟用。

**Ultra** 使用[子代理程式](/zh-Hant/codex/agent-configuration/subagents)
平行處理複雜任務中的不同部分。當工作能合理拆分為幾個部分時，
就適合選擇 Ultra。大多數任務不需要 Max 或 Ultra。

如果桌面 App 的模型滑桿沒有顯示 Ultra，請前往
**設定** \> **組態**，然後開啟 **在模型選擇器滑桿中顯示 Ultra**。

## 其他模型

使用 ChatGPT 登入時，Codex 搭配上述建議模型的效果最佳。

  <strong>
    GPT-5.4 和 GPT-5.4 mini 將於 2026 年 8 月 31 日在 Codex 中停止提供。
  </strong>{" "}
  若使用 ChatGPT 登入，請在已儲存的組態、自訂智慧體和排程任務中，將 `gpt-5.4` 替換為 `gpt-5.6-terra`，並
將 `gpt-5.4-mini` 替換為 `gpt-5.6-luna`。
  OpenAI API 和使用你自己的 API 金鑰驗證身分的 Codex
  不受影響。

  <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    

    

    

  </div>

你也可以依據特定使用情境，將 Codex 設為使用任何支援 [Chat Completions](https://platform.openai.com/docs/api-reference/chat) 或 [Responses API](https://platform.openai.com/docs/api-reference/responses) 的模型與供應商。

  對 Chat Completions API 的支援已棄用，並將在
未來的 Codex 版本中移除。

## 已棄用的 Codex 模型

透過 ChatGPT 登入 Codex 時，`gpt-5.4` 和 `gpt-5.4-mini` 模型將於
2026 年 8 月 31 日停止提供。請在工作區預設值、已儲存的模型設定、受管理的設定、
自訂智慧體及排程任務中，將 `gpt-5.4` 替換為 `gpt-5.6-terra`，
並將 `gpt-5.4-mini` 替換為 `gpt-5.6-luna`。

在透過 ChatGPT 登入的 Codex 中，`gpt-5.2` 和 `gpt-5.3-codex` 模型已棄用。
請更新仍參照這些模型的指令碼、組態檔，以及
`codex exec --model` 指令。

OpenAI API 以及使用你自己的 API 金鑰驗證身分的 Codex，
不受 GPT-5.4 停止提供的影響。若要瞭解目前可用的 API 模型，請參閱
[API 模型頁面](/api/docs/models)。

## 設定本機預設模型

ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能共用同一份 `config.toml`
[組態檔](/zh-Hant/codex/config-file/config-basic)。若要指定模型，請在組態檔中新增
`model` 項目。如果未指定模型，
ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能會使用建議的模型。

## 選擇雲端對話使用的模型

目前無法變更 Codex 雲端對話的預設模型。
