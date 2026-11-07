<!-- source: https://developers.openai.com/api/reference/go/resources/decisions/methods/create/ -->

## Create a decision

`client.Decisions.New(ctx, body) (*Decision, error)`

**post** `/decisions`

Use this endpoint to quickly answer classification or scoring questions about some input. You can ask multiple questions in one request.

- `body DecisionNewParams`

  - `Input param.Field[DecisionNewParamsInputUnion]`

    The input to evaluate for every question. Provide a text string or an ordered array of messages, function calls and outputs, or custom tool calls and outputs. Each tool output must identify a matching call by call ID.

    - `string`

    - `type DecisionNewParamsInputArray []DecisionNewParamsInputArrayItemUnion`

      - `type DecisionNewParamsInputArrayItemDecisionInputUserMessage struct{…}`

        A user message containing input text, images, or JSON.

        - `Content DecisionNewParamsInputArrayItemDecisionInputUserMessageContentUnion`

          A text string or an ordered list of text, image, and JSON parts.

          - `string`

          - `type DecisionNewParamsInputArrayItemDecisionInputUserMessageContentParts []DecisionInputPartUnion`

            - `type DecisionInputText struct{…}`

              - `Text string`

                `minLength: 0`, `maxLength: 10485760`

              - `Type InputText`

                - `const InputTextInputText InputText = "input_text"`

              - `PromptCacheBreakpoint DecisionPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

                - `Mode Explicit`

                  The breakpoint mode. Always `explicit`.

                  - `const ExplicitExplicit Explicit = "explicit"`

            - `type DecisionInputImage struct{…}`

              An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

              - `ImageURL string`

                A base64-encoded image in a data URL or a publicly accessible HTTP(S) image URL.

                `minLength: 0`, `maxLength: 1073741824`

              - `Type InputImage`

                - `const InputImageInputImage InputImage = "input_image"`

              - `Detail DecisionInputImageDetail`

                The image detail level, using the selected model's image profile. Defaults to auto.

                - `const DecisionInputImageDetailLow DecisionInputImageDetail = "low"`

                - `const DecisionInputImageDetailHigh DecisionInputImageDetail = "high"`

                - `const DecisionInputImageDetailAuto DecisionInputImageDetail = "auto"`

                - `const DecisionInputImageDetailOriginal DecisionInputImageDetail = "original"`

              - `PromptCacheBreakpoint DecisionPromptCacheBreakpoint`

                Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

            - `type DecisionInputJSON struct{…}`

              A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

              - `Data DecisionInputJSONDataUnion`

                - `map[string, any]`

                - `[]map[string, any]`

              - `Type InputJSON`

                - `const InputJSONInputJSON InputJSON = "input_json"`

        - `Role User`

          - `const UserUser User = "user"`

        - `Type string`

          - `const DecisionNewParamsInputArrayItemDecisionInputUserMessageTypeMessage DecisionNewParamsInputArrayItemDecisionInputUserMessageType = "message"`

      - `type DecisionNewParamsInputArrayItemDecisionInputDeveloperMessage struct{…}`

        A developer message containing input text.

        - `Content DecisionNewParamsInputArrayItemDecisionInputDeveloperMessageContentUnion`

          A text string or an ordered list of input text parts.

          - `string`

          - `type DecisionNewParamsInputArrayItemDecisionInputDeveloperMessageContentParts []DecisionInputText`

            - `Text string`

              `minLength: 0`, `maxLength: 10485760`

            - `Type InputText`

            - `PromptCacheBreakpoint DecisionPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

        - `Role Developer`

          - `const DeveloperDeveloper Developer = "developer"`

        - `Type string`

          - `const DecisionNewParamsInputArrayItemDecisionInputDeveloperMessageTypeMessage DecisionNewParamsInputArrayItemDecisionInputDeveloperMessageType = "message"`

      - `type DecisionNewParamsInputArrayItemDecisionInputSystemMessage struct{…}`

        A system message containing input text.

        - `Content DecisionNewParamsInputArrayItemDecisionInputSystemMessageContentUnion`

          A text string or an ordered list of input text parts.

          - `string`

          - `type DecisionNewParamsInputArrayItemDecisionInputSystemMessageContentParts []DecisionInputText`

            - `Text string`

              `minLength: 0`, `maxLength: 10485760`

            - `Type InputText`

            - `PromptCacheBreakpoint DecisionPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

        - `Role System`

          - `const SystemSystem System = "system"`

        - `Type string`

          - `const DecisionNewParamsInputArrayItemDecisionInputSystemMessageTypeMessage DecisionNewParamsInputArrayItemDecisionInputSystemMessageType = "message"`

      - `type DecisionNewParamsInputArrayItemDecisionInputAssistantMessage struct{…}`

        An assistant message containing output text or refusals.

        - `Content DecisionNewParamsInputArrayItemDecisionInputAssistantMessageContentUnion`

          A text string or an ordered list of output text and refusal parts.

          - `string`

          - `type DecisionNewParamsInputArrayItemDecisionInputAssistantMessageContentParts []DecisionNewParamsInputArrayItemDecisionInputAssistantMessageContentPartsItemUnion`

            - `type DecisionNewParamsInputArrayItemDecisionInputAssistantMessageContentPartOutputText struct{…}`

              - `Text string`

                `minLength: 0`, `maxLength: 10485760`

              - `Type OutputText`

                - `const OutputTextOutputText OutputText = "output_text"`

            - `type DecisionNewParamsInputArrayItemDecisionInputAssistantMessageContentPartRefusal struct{…}`

              - `Refusal string`

                `minLength: 0`, `maxLength: 10485760`

              - `Type Refusal`

                - `const RefusalRefusal Refusal = "refusal"`

        - `Role Assistant`

          - `const AssistantAssistant Assistant = "assistant"`

        - `Phase string`

          The phase of an assistant message.

          - `const DecisionNewParamsInputArrayItemDecisionInputAssistantMessagePhaseCommentary DecisionNewParamsInputArrayItemDecisionInputAssistantMessagePhase = "commentary"`

          - `const DecisionNewParamsInputArrayItemDecisionInputAssistantMessagePhaseFinalAnswer DecisionNewParamsInputArrayItemDecisionInputAssistantMessagePhase = "final_answer"`

        - `Type string`

          - `const DecisionNewParamsInputArrayItemDecisionInputAssistantMessageTypeMessage DecisionNewParamsInputArrayItemDecisionInputAssistantMessageType = "message"`

      - `type DecisionNewParamsInputArrayItemFunctionCall struct{…}`

        - `Arguments string`

          `minLength: 0`, `maxLength: 1048576`

        - `CallID string`

          `minLength: 1`, `maxLength: 64`

        - `Name string`

          `minLength: 1`, `maxLength: 128`

        - `Type FunctionCall`

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

        - `ID string`

          `minLength: 0`, `maxLength: 1048576`

        - `Namespace string`

          `minLength: 1`, `maxLength: 64`

        - `Status string`

          - `const DecisionNewParamsInputArrayItemFunctionCallStatusInProgress DecisionNewParamsInputArrayItemFunctionCallStatus = "in_progress"`

          - `const DecisionNewParamsInputArrayItemFunctionCallStatusCompleted DecisionNewParamsInputArrayItemFunctionCallStatus = "completed"`

          - `const DecisionNewParamsInputArrayItemFunctionCallStatusIncomplete DecisionNewParamsInputArrayItemFunctionCallStatus = "incomplete"`

      - `type DecisionNewParamsInputArrayItemFunctionCallOutput struct{…}`

        - `CallID string`

          `minLength: 1`, `maxLength: 64`

        - `Output DecisionNewParamsInputArrayItemFunctionCallOutputOutputUnion`

          Text evidence or an ordered list of text and image parts.

          - `string`

          - `type DecisionNewParamsInputArrayItemFunctionCallOutputOutputParts []DecisionNewParamsInputArrayItemFunctionCallOutputOutputPartsItemUnion`

            - `type DecisionInputText struct{…}`

            - `type DecisionInputImage struct{…}`

              An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

        - `Type FunctionCallOutput`

          - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

        - `ID string`

          `minLength: 0`, `maxLength: 1048576`

        - `Status string`

          - `const DecisionNewParamsInputArrayItemFunctionCallOutputStatusInProgress DecisionNewParamsInputArrayItemFunctionCallOutputStatus = "in_progress"`

          - `const DecisionNewParamsInputArrayItemFunctionCallOutputStatusCompleted DecisionNewParamsInputArrayItemFunctionCallOutputStatus = "completed"`

          - `const DecisionNewParamsInputArrayItemFunctionCallOutputStatusIncomplete DecisionNewParamsInputArrayItemFunctionCallOutputStatus = "incomplete"`

      - `type DecisionNewParamsInputArrayItemCustomToolCall struct{…}`

        - `CallID string`

          `minLength: 1`, `maxLength: 64`

        - `Input string`

          `minLength: 0`, `maxLength: 1048576`

        - `Name string`

          `minLength: 1`, `maxLength: 64`

        - `Type CustomToolCall`

          - `const CustomToolCallCustomToolCall CustomToolCall = "custom_tool_call"`

        - `ID string`

          `minLength: 0`, `maxLength: 1048576`

        - `Namespace string`

          `minLength: 1`, `maxLength: 64`

        - `Status string`

          - `const DecisionNewParamsInputArrayItemCustomToolCallStatusInProgress DecisionNewParamsInputArrayItemCustomToolCallStatus = "in_progress"`

          - `const DecisionNewParamsInputArrayItemCustomToolCallStatusCompleted DecisionNewParamsInputArrayItemCustomToolCallStatus = "completed"`

          - `const DecisionNewParamsInputArrayItemCustomToolCallStatusIncomplete DecisionNewParamsInputArrayItemCustomToolCallStatus = "incomplete"`

      - `type DecisionNewParamsInputArrayItemCustomToolCallOutput struct{…}`

        - `CallID string`

          `minLength: 1`, `maxLength: 64`

        - `Output DecisionNewParamsInputArrayItemCustomToolCallOutputOutputUnion`

          Text evidence or an ordered list of text and image parts.

          - `string`

          - `type DecisionNewParamsInputArrayItemCustomToolCallOutputOutputParts []DecisionNewParamsInputArrayItemCustomToolCallOutputOutputPartsItemUnion`

            - `type DecisionInputText struct{…}`

            - `type DecisionInputImage struct{…}`

              An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

        - `Type CustomToolCallOutput`

          - `const CustomToolCallOutputCustomToolCallOutput CustomToolCallOutput = "custom_tool_call_output"`

        - `ID string`

          `minLength: 0`, `maxLength: 1048576`

        - `Status string`

          - `const DecisionNewParamsInputArrayItemCustomToolCallOutputStatusInProgress DecisionNewParamsInputArrayItemCustomToolCallOutputStatus = "in_progress"`

          - `const DecisionNewParamsInputArrayItemCustomToolCallOutputStatusCompleted DecisionNewParamsInputArrayItemCustomToolCallOutputStatus = "completed"`

          - `const DecisionNewParamsInputArrayItemCustomToolCallOutputStatusIncomplete DecisionNewParamsInputArrayItemCustomToolCallOutputStatus = "incomplete"`

  - `Model param.Field[string]`

    The model to use. Only `gpt-6-luna` is supported.

    `minLength: 0`, `maxLength: 1048576`

  - `Questions param.Field[[]DecisionNewParamsQuestionUnion]`

    Ask 1–400 questions about the input. Each question can be a predicate, choice, or score. Answers come back in the same order.

    `minItems: 1`, `maxItems: 400`

    - `type DecisionNewParamsQuestionPredicate struct{…}`

      Estimate how likely it is that a statement about the input is true.

      - `Instructions DecisionNewParamsQuestionPredicateInstructionsUnion`

        - `string`

        - `type DecisionNewParamsQuestionPredicateInstructionsArray []DecisionQuestionInputPartUnion`

          - `type DecisionQuestionInputText struct{…}`

            - `Text string`

              `minLength: 0`, `maxLength: 10485760`

            - `Type InputText`

              - `const InputTextInputText InputText = "input_text"`

          - `type DecisionQuestionInputImage struct{…}`

            An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

            - `ImageURL string`

              A base64-encoded image in a data URL or a publicly accessible HTTP(S) image URL.

              `minLength: 0`, `maxLength: 1073741824`

            - `Type InputImage`

              - `const InputImageInputImage InputImage = "input_image"`

            - `Detail DecisionQuestionInputImageDetail`

              The image detail level, using the selected model's image profile. Defaults to auto.

              - `const DecisionQuestionInputImageDetailLow DecisionQuestionInputImageDetail = "low"`

              - `const DecisionQuestionInputImageDetailHigh DecisionQuestionInputImageDetail = "high"`

              - `const DecisionQuestionInputImageDetailAuto DecisionQuestionInputImageDetail = "auto"`

              - `const DecisionQuestionInputImageDetailOriginal DecisionQuestionInputImageDetail = "original"`

          - `type DecisionInputJSON struct{…}`

            A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

      - `Type Predicate`

        The type of the object. Always `predicate`.

        - `const PredicatePredicate Predicate = "predicate"`

      - `Name string`

        `minLength: 0`, `maxLength: 1048576`

    - `type DecisionNewParamsQuestionChoice struct{…}`

      Choose from the supplied options based on the input.

      - `Choices []DecisionNewParamsQuestionChoiceChoice`

        Provide between 2 and 255 choices. Each choice must be unique.

        `minItems: 2`, `maxItems: 255`

        - `Value DecisionNewParamsQuestionChoiceChoiceValueUnion`

          Choice values are typed: a string and a boolean with the same text are distinct.

          - `string`

          - `bool`

        - `Description string`

          `minLength: 0`, `maxLength: 1048576`

      - `Instructions DecisionNewParamsQuestionChoiceInstructionsUnion`

        - `string`

        - `type DecisionNewParamsQuestionChoiceInstructionsArray []DecisionQuestionInputPartUnion`

          - `type DecisionQuestionInputText struct{…}`

          - `type DecisionQuestionInputImage struct{…}`

            An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

          - `type DecisionInputJSON struct{…}`

            A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

      - `Type Choice`

        The type of the object. Always `choice`.

        - `const ChoiceChoice Choice = "choice"`

      - `Name string`

        `minLength: 0`, `maxLength: 1048576`

    - `type DecisionNewParamsQuestionScore struct{…}`

      Rate the input against the supplied ordered levels.

      - `Instructions DecisionNewParamsQuestionScoreInstructionsUnion`

        - `string`

        - `type DecisionNewParamsQuestionScoreInstructionsArray []DecisionQuestionInputPartUnion`

          - `type DecisionQuestionInputText struct{…}`

          - `type DecisionQuestionInputImage struct{…}`

            An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

          - `type DecisionInputJSON struct{…}`

            A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

      - `Levels []DecisionNewParamsQuestionScoreLevel`

        `minItems: 2`, `maxItems: 10`

        - `Label string`

          `minLength: 0`, `maxLength: 1048576`

        - `Description string`

          `minLength: 0`, `maxLength: 1048576`

      - `Type Score`

        The type of the object. Always `score`.

        - `const ScoreScore Score = "score"`

      - `Name string`

        `minLength: 0`, `maxLength: 1048576`

  - `PromptCacheKey param.Field[string]`

    Partition prompt cache reuse by caller-provided key.

    `minLength: 0`, `maxLength: 64`

  - `PromptCacheOptions param.Field[DecisionNewParamsPromptCacheOptions]`

    Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](/api/docs/guides/prompt-caching) for current details.

    - `Mode string`

      Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

      - `const DecisionNewParamsPromptCacheOptionsModeImplicit DecisionNewParamsPromptCacheOptionsMode = "implicit"`

      - `const DecisionNewParamsPromptCacheOptionsModeExplicit DecisionNewParamsPromptCacheOptionsMode = "explicit"`

    - `Ttl string`

      The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

      - `const DecisionNewParamsPromptCacheOptionsTtl30m DecisionNewParamsPromptCacheOptionsTtl = "30m"`

  - `SafetyIdentifier param.Field[string]`

    Opaque caller-provided end-user identifier, scoped by the verified org. Match Responses' limit; this is never the authenticated user identity.

    `minLength: 0`, `maxLength: 128`

- `type Decision struct{…}`

  - `Answers []DecisionAnswerUnion`

    Answers in question order. Any question can return a refusal instead of an answer; other questions can still receive answers. A refusal has `type: "refusal"` and the question's `name`, or `null` if it was unnamed.

    `minItems: 0`, `maxItems: 2000`

    - `type DecisionAnswerPredicate struct{…}`

      - `Name string`

        `minLength: 0`

      - `Probability float64`

      - `Type Predicate`

        The type of the object. Always `predicate`.

        - `const PredicatePredicate Predicate = "predicate"`

    - `type DecisionAnswerChoice struct{…}`

      - `Choice DecisionAnswerChoiceChoiceUnion`

        Choice values are typed: a string and a boolean with the same text are distinct.

        - `string`

        - `bool`

      - `Confidence float64`

      - `Name string`

        `minLength: 0`

      - `Probabilities []DecisionAnswerChoiceProbability`

        `minItems: 0`, `maxItems: 2000`

        - `Probability float64`

        - `Value DecisionAnswerChoiceProbabilityValueUnion`

          Choice values are typed: a string and a boolean with the same text are distinct.

          - `string`

          - `bool`

      - `Type Choice`

        The type of the object. Always `choice`.

        - `const ChoiceChoice Choice = "choice"`

    - `type DecisionAnswerScore struct{…}`

      - `Confidence float64`

      - `Name string`

        `minLength: 0`

      - `Probabilities []DecisionAnswerScoreProbability`

        `minItems: 0`, `maxItems: 2000`

        - `Label string`

          `minLength: 0`

        - `Probability float64`

        - `Value int64`

          `format: int64`

      - `Score float64`

      - `Type Score`

        The type of the object. Always `score`.

        - `const ScoreScore Score = "score"`

    - `type DecisionAnswerRefusal struct{…}`

      The model declined to answer this question. Other questions in the same request can still receive answers.

      - `Name string`

        `minLength: 0`

      - `Type Refusal`

        The type of the object. Always `refusal`.

        - `const RefusalRefusal Refusal = "refusal"`

  - `Model string`

    The model used.

    `minLength: 0`

  - `Usage DecisionUsage`

    Token usage for the request.

    - `InputTokens int64`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `InputTokensDetails DecisionUsageInputTokensDetails`

      - `CacheWriteTokens int64`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

      - `CachedTokens int64`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `OutputTokens int64`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `OutputTokensDetails DecisionUsageOutputTokensDetails`

      - `ReasoningTokens int64`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `TotalTokens int64`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  decision, err := client.Decisions.New(context.TODO(), openai.DecisionNewParams{
    Input: openai.DecisionNewParamsInputUnion{
      OfString: openai.String("string"),
    Model: "model",
    Questions: []openai.DecisionNewParamsQuestionUnion{openai.DecisionNewParamsQuestionUnion{
      OfPredicate: &openai.DecisionNewParamsQuestionPredicate{
        Instructions: openai.DecisionNewParamsQuestionPredicateInstructionsUnion{
          OfString: openai.String("string"),
    }},
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", decision.Answers)

  "answers": [
      "probability": 0,
      "type": "predicate"
  "model": "model",
  "usage": {
    "input_tokens": -2147483648,
    "input_tokens_details": {
      "cache_write_tokens": -2147483648,
      "cached_tokens": -2147483648
    "output_tokens": -2147483648,
    "output_tokens_details": {
      "reasoning_tokens": -2147483648
    "total_tokens": -2147483648
