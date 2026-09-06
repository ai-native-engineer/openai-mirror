<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/api-integration-migrations -->

## 簡介

隨著我們推出新模型與 API 功能，建議您升級整合，以受益於最新的改進。
從一個模型換到另一個模型，通常不只是更新模型名稱這麼簡單。

API 可能有所變更。例如，針對 GPT-5.4 模型，我們在助理訊息中新增了 `phase` 參數，整合時務必納入這項參數。更重要的是，模型行為可能有所不同，因此需要修改現有的提示詞。

遷移至新模型時，除了進行必要的程式碼變更，也務必評估對工作流程的影響。

## 善用 OpenAI 文件技能

[模型指引](/api/docs/guides/latest-model)頁面彙整了各代模型在 API 功能、模型行為、遷移與提示詞方面的指引。

OpenAI 文件技能也包含[具體指引](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md)，可作為遷移參考。針對目前的升級目標，請參閱[模型指引](/api/docs/guides/latest-model)頁面。

Codex 現在已內建 OpenAI 文件技能，因此使用 OpenAI API 進行開發時，請務必在提示詞中提及這項技能，以取得所有最新文件與指引。

## 建立穩健的評估流程

Codex 可依據最新的提示詞指引自動更新您的提示詞，但您仍應建立自動化驗證機制，確認整合是否如預期運作。

請務必建立一套評估流程，讓您每次變更整合時都能執行，以確認行為沒有出現迴歸問題。

這份 [Cookbook 指南](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel)詳細說明如何使用我們的 [Evals API](/api/docs/guides/evals) 建立這樣的流程。
