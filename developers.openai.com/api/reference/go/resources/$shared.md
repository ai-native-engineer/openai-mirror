<!-- source: https://developers.openai.com/api/reference/go/resources/$shared/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Shared

##### ModelsExpand Collapse

type AllModels interface{…}

One of the following:

string

type ChatModel string

One of the following:

const ChatModelGPT5\_4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4"

const ChatModelGPT5\_4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini"

const ChatModelGPT5\_4Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano"

const ChatModelGPT5\_4Mini2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini-2026-03-17"

const ChatModelGPT5\_4Nano2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano-2026-03-17"

const ChatModelGPT5\_3ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.3-chat-latest"

const ChatModelGPT5\_2 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2"

const ChatModelGPT5\_2\_2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-2025-12-11"

const ChatModelGPT5\_2ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-chat-latest"

const ChatModelGPT5\_2Pro [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro"

const ChatModelGPT5\_2Pro2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro-2025-12-11"

const ChatModelGPT5\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1"

const ChatModelGPT5\_1\_2025\_11\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-2025-11-13"

const ChatModelGPT5\_1Codex [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-codex"

const ChatModelGPT5\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-mini"

const ChatModelGPT5\_1ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-chat-latest"

const ChatModelGPT5 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5"

const ChatModelGPT5Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini"

const ChatModelGPT5Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano"

const ChatModelGPT5\_2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-2025-08-07"

const ChatModelGPT5Mini2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini-2025-08-07"

const ChatModelGPT5Nano2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano-2025-08-07"

const ChatModelGPT5ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-chat-latest"

const ChatModelGPT4\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1"

const ChatModelGPT4\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini"

const ChatModelGPT4\_1Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano"

const ChatModelGPT4\_1\_2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-2025-04-14"

const ChatModelGPT4\_1Mini2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini-2025-04-14"

const ChatModelGPT4\_1Nano2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano-2025-04-14"

const ChatModelO4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini"

const ChatModelO4Mini2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini-2025-04-16"

const ChatModelO3 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3"

const ChatModelO3\_2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-2025-04-16"

const ChatModelO3Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini"

const ChatModelO3Mini2025\_01\_31 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini-2025-01-31"

const ChatModelO1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1"

const ChatModelO1\_2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-2024-12-17"

const ChatModelO1Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview"

const ChatModelO1Preview2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview-2024-09-12"

const ChatModelO1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini"

const ChatModelO1Mini2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini-2024-09-12"

const ChatModelGPT4o [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o"

const ChatModelGPT4o2024\_11\_20 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-11-20"

const ChatModelGPT4o2024\_08\_06 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-08-06"

const ChatModelGPT4o2024\_05\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-05-13"

const ChatModelGPT4oAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview"

const ChatModelGPT4oAudioPreview2024\_10\_01 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-10-01"

const ChatModelGPT4oAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-12-17"

const ChatModelGPT4oAudioPreview2025\_06\_03 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2025-06-03"

const ChatModelGPT4oMiniAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview"

const ChatModelGPT4oMiniAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview-2024-12-17"

const ChatModelGPT4oSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview"

const ChatModelGPT4oMiniSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview"

const ChatModelGPT4oSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview-2025-03-11"

const ChatModelGPT4oMiniSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview-2025-03-11"

const ChatModelChatgpt4oLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "chatgpt-4o-latest"

const ChatModelCodexMiniLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "codex-mini-latest"

const ChatModelGPT4oMini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini"

const ChatModelGPT4oMini2024\_07\_18 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-2024-07-18"

const ChatModelGPT4Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo"

const ChatModelGPT4Turbo2024\_04\_09 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-2024-04-09"

const ChatModelGPT4\_0125Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0125-preview"

const ChatModelGPT4TurboPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-preview"

const ChatModelGPT4\_1106Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-1106-preview"

const ChatModelGPT4VisionPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-vision-preview"

const ChatModelGPT4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4"

const ChatModelGPT4\_0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0314"

const ChatModelGPT4\_0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0613"

const ChatModelGPT4\_32k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k"

const ChatModelGPT4\_32k0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0314"

const ChatModelGPT4\_32k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0613"

const ChatModelGPT3\_5Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo"

const ChatModelGPT3\_5Turbo16k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k"

const ChatModelGPT3\_5Turbo0301 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0301"

const ChatModelGPT3\_5Turbo0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0613"

const ChatModelGPT3\_5Turbo1106 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-1106"

const ChatModelGPT3\_5Turbo0125 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0125"

const ChatModelGPT3\_5Turbo16k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k-0613"

type AllModels string

One of the following:

const AllModelsO1Pro AllModels = "o1-pro"

const AllModelsO1Pro2025\_03\_19 AllModels = "o1-pro-2025-03-19"

const AllModelsO3Pro AllModels = "o3-pro"

const AllModelsO3Pro2025\_06\_10 AllModels = "o3-pro-2025-06-10"

const AllModelsO3DeepResearch AllModels = "o3-deep-research"

const AllModelsO3DeepResearch2025\_06\_26 AllModels = "o3-deep-research-2025-06-26"

const AllModelsO4MiniDeepResearch AllModels = "o4-mini-deep-research"

const AllModelsO4MiniDeepResearch2025\_06\_26 AllModels = "o4-mini-deep-research-2025-06-26"

const AllModelsComputerUsePreview AllModels = "computer-use-preview"

const AllModelsComputerUsePreview2025\_03\_11 AllModels = "computer-use-preview-2025-03-11"

const AllModelsGPT5Codex AllModels = "gpt-5-codex"

const AllModelsGPT5Pro AllModels = "gpt-5-pro"

const AllModelsGPT5Pro2025\_10\_06 AllModels = "gpt-5-pro-2025-10-06"

const AllModelsGPT5\_1CodexMax AllModels = "gpt-5.1-codex-max"

type ChatModel string

One of the following:

const ChatModelGPT5\_4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4"

const ChatModelGPT5\_4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini"

const ChatModelGPT5\_4Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano"

const ChatModelGPT5\_4Mini2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini-2026-03-17"

const ChatModelGPT5\_4Nano2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano-2026-03-17"

const ChatModelGPT5\_3ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.3-chat-latest"

const ChatModelGPT5\_2 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2"

const ChatModelGPT5\_2\_2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-2025-12-11"

const ChatModelGPT5\_2ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-chat-latest"

const ChatModelGPT5\_2Pro [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro"

const ChatModelGPT5\_2Pro2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro-2025-12-11"

const ChatModelGPT5\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1"

const ChatModelGPT5\_1\_2025\_11\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-2025-11-13"

const ChatModelGPT5\_1Codex [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-codex"

const ChatModelGPT5\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-mini"

const ChatModelGPT5\_1ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-chat-latest"

const ChatModelGPT5 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5"

const ChatModelGPT5Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini"

const ChatModelGPT5Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano"

const ChatModelGPT5\_2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-2025-08-07"

const ChatModelGPT5Mini2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini-2025-08-07"

const ChatModelGPT5Nano2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano-2025-08-07"

const ChatModelGPT5ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-chat-latest"

const ChatModelGPT4\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1"

const ChatModelGPT4\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini"

const ChatModelGPT4\_1Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano"

const ChatModelGPT4\_1\_2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-2025-04-14"

const ChatModelGPT4\_1Mini2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini-2025-04-14"

const ChatModelGPT4\_1Nano2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano-2025-04-14"

const ChatModelO4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini"

const ChatModelO4Mini2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini-2025-04-16"

const ChatModelO3 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3"

const ChatModelO3\_2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-2025-04-16"

const ChatModelO3Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini"

const ChatModelO3Mini2025\_01\_31 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini-2025-01-31"

const ChatModelO1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1"

const ChatModelO1\_2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-2024-12-17"

const ChatModelO1Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview"

const ChatModelO1Preview2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview-2024-09-12"

const ChatModelO1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini"

const ChatModelO1Mini2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini-2024-09-12"

const ChatModelGPT4o [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o"

const ChatModelGPT4o2024\_11\_20 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-11-20"

const ChatModelGPT4o2024\_08\_06 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-08-06"

const ChatModelGPT4o2024\_05\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-05-13"

const ChatModelGPT4oAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview"

const ChatModelGPT4oAudioPreview2024\_10\_01 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-10-01"

const ChatModelGPT4oAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-12-17"

const ChatModelGPT4oAudioPreview2025\_06\_03 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2025-06-03"

const ChatModelGPT4oMiniAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview"

const ChatModelGPT4oMiniAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview-2024-12-17"

const ChatModelGPT4oSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview"

const ChatModelGPT4oMiniSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview"

const ChatModelGPT4oSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview-2025-03-11"

const ChatModelGPT4oMiniSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview-2025-03-11"

const ChatModelChatgpt4oLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "chatgpt-4o-latest"

const ChatModelCodexMiniLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "codex-mini-latest"

const ChatModelGPT4oMini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini"

const ChatModelGPT4oMini2024\_07\_18 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-2024-07-18"

const ChatModelGPT4Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo"

const ChatModelGPT4Turbo2024\_04\_09 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-2024-04-09"

const ChatModelGPT4\_0125Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0125-preview"

const ChatModelGPT4TurboPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-preview"

const ChatModelGPT4\_1106Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-1106-preview"

const ChatModelGPT4VisionPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-vision-preview"

const ChatModelGPT4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4"

const ChatModelGPT4\_0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0314"

const ChatModelGPT4\_0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0613"

const ChatModelGPT4\_32k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k"

const ChatModelGPT4\_32k0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0314"

const ChatModelGPT4\_32k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0613"

const ChatModelGPT3\_5Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo"

const ChatModelGPT3\_5Turbo16k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k"

const ChatModelGPT3\_5Turbo0301 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0301"

const ChatModelGPT3\_5Turbo0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0613"

const ChatModelGPT3\_5Turbo1106 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-1106"

const ChatModelGPT3\_5Turbo0125 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0125"

const ChatModelGPT3\_5Turbo16k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k-0613"

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

type CustomToolInputFormatUnion interface{…}

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type ErrorObject struct{…}

Code string

Message string

Param string

Type string

type FunctionDefinition struct{…}

Name string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the function does, used by the model to choose when and how to call the function.

Parameters [FunctionParameters](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))Optional

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

Strict boolOptional

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type FunctionParameters map[string, any]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

type Metadata map[string, string]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

type OAuthErrorCode interface{…}

One of the following:

type OAuthErrorCode string

One of the following:

const OAuthErrorCodeInvalidGrant OAuthErrorCode = "invalid\_grant"

const OAuthErrorCodeInvalidSubjectToken OAuthErrorCode = "invalid\_subject\_token"

string

type Reasoning struct{…}

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Context ReasoningContextOptional

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

One of the following:

const ReasoningContextAuto ReasoningContext = "auto"

const ReasoningContextCurrentTurn ReasoningContext = "current\_turn"

const ReasoningContextAllTurns ReasoningContext = "all\_turns"

Effort [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))Optional

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

DeprecatedGenerateSummary ReasoningGenerateSummaryOptional

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

One of the following:

const ReasoningGenerateSummaryAuto ReasoningGenerateSummary = "auto"

const ReasoningGenerateSummaryConcise ReasoningGenerateSummary = "concise"

const ReasoningGenerateSummaryDetailed ReasoningGenerateSummary = "detailed"

Summary ReasoningSummaryOptional

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

One of the following:

const ReasoningSummaryAuto ReasoningSummary = "auto"

const ReasoningSummaryConcise ReasoningSummary = "concise"

const ReasoningSummaryDetailed ReasoningSummary = "detailed"

type ReasoningEffort string

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

const ReasoningEffortNone [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "none"

const ReasoningEffortMinimal [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "minimal"

const ReasoningEffortLow [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "low"

const ReasoningEffortMedium [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "medium"

const ReasoningEffortHigh [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "high"

const ReasoningEffortXhigh [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "xhigh"

type ResponseFormatJSONObject struct{…}

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

Type JSONObject

The type of response format being defined. Always `json_object`.

type ResponseFormatJSONSchema struct{…}

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

JSONSchema ResponseFormatJSONSchemaJSONSchema

Structured Outputs configuration options, including a JSON Schema.

Name string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the response format is for, used by the model to
determine how to respond in the format.

Schema map[string, any]Optional

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

Strict boolOptional

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Type JSONSchema

The type of response format being defined. Always `json_schema`.

type ResponseFormatText struct{…}

Default response format. Used to generate text responses.

Type Text

The type of response format being defined. Always `text`.

type ResponseFormatTextGrammar struct{…}

A custom grammar for the model to follow when generating text.
Learn more in the [custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars).

Grammar string

The custom grammar for the model to follow.

Type Grammar

The type of response format being defined. Always `grammar`.

type ResponseFormatTextPython struct{…}

Configure the model to generate valid Python code. See the
[custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars) for more details.

Type Python

The type of response format being defined. Always `python`.

type ResponsesModel interface{…}

One of the following:

string

type ChatModel string

One of the following:

const ChatModelGPT5\_4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4"

const ChatModelGPT5\_4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini"

const ChatModelGPT5\_4Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano"

const ChatModelGPT5\_4Mini2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini-2026-03-17"

const ChatModelGPT5\_4Nano2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano-2026-03-17"

const ChatModelGPT5\_3ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.3-chat-latest"

const ChatModelGPT5\_2 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2"

const ChatModelGPT5\_2\_2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-2025-12-11"

const ChatModelGPT5\_2ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-chat-latest"

const ChatModelGPT5\_2Pro [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro"

const ChatModelGPT5\_2Pro2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro-2025-12-11"

const ChatModelGPT5\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1"

const ChatModelGPT5\_1\_2025\_11\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-2025-11-13"

const ChatModelGPT5\_1Codex [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-codex"

const ChatModelGPT5\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-mini"

const ChatModelGPT5\_1ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-chat-latest"

const ChatModelGPT5 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5"

const ChatModelGPT5Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini"

const ChatModelGPT5Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano"

const ChatModelGPT5\_2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-2025-08-07"

const ChatModelGPT5Mini2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini-2025-08-07"

const ChatModelGPT5Nano2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano-2025-08-07"

const ChatModelGPT5ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-chat-latest"

const ChatModelGPT4\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1"

const ChatModelGPT4\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini"

const ChatModelGPT4\_1Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano"

const ChatModelGPT4\_1\_2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-2025-04-14"

const ChatModelGPT4\_1Mini2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini-2025-04-14"

const ChatModelGPT4\_1Nano2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano-2025-04-14"

const ChatModelO4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini"

const ChatModelO4Mini2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini-2025-04-16"

const ChatModelO3 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3"

const ChatModelO3\_2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-2025-04-16"

const ChatModelO3Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini"

const ChatModelO3Mini2025\_01\_31 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini-2025-01-31"

const ChatModelO1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1"

const ChatModelO1\_2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-2024-12-17"

const ChatModelO1Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview"

const ChatModelO1Preview2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview-2024-09-12"

const ChatModelO1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini"

const ChatModelO1Mini2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini-2024-09-12"

const ChatModelGPT4o [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o"

const ChatModelGPT4o2024\_11\_20 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-11-20"

const ChatModelGPT4o2024\_08\_06 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-08-06"

const ChatModelGPT4o2024\_05\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-05-13"

const ChatModelGPT4oAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview"

const ChatModelGPT4oAudioPreview2024\_10\_01 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-10-01"

const ChatModelGPT4oAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-12-17"

const ChatModelGPT4oAudioPreview2025\_06\_03 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2025-06-03"

const ChatModelGPT4oMiniAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview"

const ChatModelGPT4oMiniAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview-2024-12-17"

const ChatModelGPT4oSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview"

const ChatModelGPT4oMiniSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview"

const ChatModelGPT4oSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview-2025-03-11"

const ChatModelGPT4oMiniSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview-2025-03-11"

const ChatModelChatgpt4oLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "chatgpt-4o-latest"

const ChatModelCodexMiniLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "codex-mini-latest"

const ChatModelGPT4oMini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini"

const ChatModelGPT4oMini2024\_07\_18 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-2024-07-18"

const ChatModelGPT4Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo"

const ChatModelGPT4Turbo2024\_04\_09 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-2024-04-09"

const ChatModelGPT4\_0125Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0125-preview"

const ChatModelGPT4TurboPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-preview"

const ChatModelGPT4\_1106Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-1106-preview"

const ChatModelGPT4VisionPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-vision-preview"

const ChatModelGPT4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4"

const ChatModelGPT4\_0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0314"

const ChatModelGPT4\_0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0613"

const ChatModelGPT4\_32k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k"

const ChatModelGPT4\_32k0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0314"

const ChatModelGPT4\_32k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0613"

const ChatModelGPT3\_5Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo"

const ChatModelGPT3\_5Turbo16k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k"

const ChatModelGPT3\_5Turbo0301 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0301"

const ChatModelGPT3\_5Turbo0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0613"

const ChatModelGPT3\_5Turbo1106 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-1106"

const ChatModelGPT3\_5Turbo0125 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0125"

const ChatModelGPT3\_5Turbo16k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k-0613"

type ResponsesModel string

One of the following:

const ResponsesModelO1Pro ResponsesModel = "o1-pro"

const ResponsesModelO1Pro2025\_03\_19 ResponsesModel = "o1-pro-2025-03-19"

const ResponsesModelO3Pro ResponsesModel = "o3-pro"

const ResponsesModelO3Pro2025\_06\_10 ResponsesModel = "o3-pro-2025-06-10"

const ResponsesModelO3DeepResearch ResponsesModel = "o3-deep-research"

const ResponsesModelO3DeepResearch2025\_06\_26 ResponsesModel = "o3-deep-research-2025-06-26"

const ResponsesModelO4MiniDeepResearch ResponsesModel = "o4-mini-deep-research"

const ResponsesModelO4MiniDeepResearch2025\_06\_26 ResponsesModel = "o4-mini-deep-research-2025-06-26"

const ResponsesModelComputerUsePreview ResponsesModel = "computer-use-preview"

const ResponsesModelComputerUsePreview2025\_03\_11 ResponsesModel = "computer-use-preview-2025-03-11"

const ResponsesModelGPT5Codex ResponsesModel = "gpt-5-codex"

const ResponsesModelGPT5Pro ResponsesModel = "gpt-5-pro"

const ResponsesModelGPT5Pro2025\_10\_06 ResponsesModel = "gpt-5-pro-2025-10-06"

const ResponsesModelGPT5\_1CodexMax ResponsesModel = "gpt-5.1-codex-max"
