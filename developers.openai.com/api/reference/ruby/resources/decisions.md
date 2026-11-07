<!-- source: https://developers.openai.com/api/reference/ruby/resources/decisions/ -->

# Decisions

## Create a decision

`decisions.create(**kwargs) -> Decision`

**post** `/decisions`

Use this endpoint to quickly answer classification or scoring questions about some input. You can ask multiple questions in one request.

### Parameters

- `input: String | Array[DecisionInputUserMessage{ content, role, type} | DecisionInputDeveloperMessage{ content, role, type} | DecisionInputSystemMessage{ content, role, type} | 5 more]`

  The input to evaluate for every question. Provide a text string or an ordered array of messages, function calls and outputs, or custom tool calls and outputs. Each tool output must identify a matching call by call ID.

  - `String = String`

  - `UnionMember1 = Array[DecisionInputUserMessage{ content, role, type} | DecisionInputDeveloperMessage{ content, role, type} | DecisionInputSystemMessage{ content, role, type} | 5 more]`

    - `class DecisionInputUserMessage`

      A user message containing input text, images, or JSON.

      - `content: String | Array[DecisionInputPart]`

        A text string or an ordered list of text, image, and JSON parts.

        - `String = String`

        - `Parts = Array[DecisionInputPart]`

          - `class DecisionInputText`

            - `text: String`

              `minLength: 0`, `maxLength: 10485760`

            - `type: :input_text`

              - `:input_text`

            - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

              - `mode: :explicit`

                The breakpoint mode. Always `explicit`.

                - `:explicit`

          - `class DecisionInputImage`

            An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

            - `image_url: String`

              A base64-encoded image in a data URL or a publicly accessible HTTP(S) image URL.

              `minLength: 0`, `maxLength: 1073741824`

            - `type: :input_image`

              - `:input_image`

            - `detail: :low | :high | :auto | :original`

              The image detail level, using the selected model's image profile. Defaults to auto.

              - `:low`

              - `:high`

              - `:auto`

              - `:original`

            - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

              Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

          - `class DecisionInputJSON`

            A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

            - `data: Hash[Symbol, untyped] | Array[Hash[Symbol, untyped]]`

              - `UnionMember0 = Hash[Symbol, untyped]`

              - `UnionMember1 = Array[Hash[Symbol, untyped]]`

            - `type: :input_json`

              - `:input_json`

      - `role: :user`

        - `:user`

      - `type: :message`

        - `:message`

    - `class DecisionInputDeveloperMessage`

      A developer message containing input text.

      - `content: String | Array[DecisionInputText]`

        A text string or an ordered list of input text parts.

        - `String = String`

        - `Parts = Array[DecisionInputText]`

          - `text: String`

            `minLength: 0`, `maxLength: 10485760`

          - `type: :input_text`

          - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

            Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

      - `role: :developer`

        - `:developer`

      - `type: :message`

        - `:message`

    - `class DecisionInputSystemMessage`

      A system message containing input text.

      - `content: String | Array[DecisionInputText]`

        A text string or an ordered list of input text parts.

        - `String = String`

        - `Parts = Array[DecisionInputText]`

          - `text: String`

            `minLength: 0`, `maxLength: 10485760`

          - `type: :input_text`

          - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

            Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

      - `role: :system`

        - `:system`

      - `type: :message`

        - `:message`

    - `class DecisionInputAssistantMessage`

      An assistant message containing output text or refusals.

      - `content: String | Array[OutputText{ text, type} | Refusal{ refusal, type}]`

        A text string or an ordered list of output text and refusal parts.

        - `String = String`

        - `Parts = Array[OutputText{ text, type} | Refusal{ refusal, type}]`

          - `class OutputText`

            - `text: String`

              `minLength: 0`, `maxLength: 10485760`

            - `type: :output_text`

              - `:output_text`

          - `class Refusal`

            - `refusal: String`

              `minLength: 0`, `maxLength: 10485760`

            - `type: :refusal`

              - `:refusal`

      - `role: :assistant`

        - `:assistant`

      - `phase: :commentary | :final_answer`

        The phase of an assistant message.

        - `:commentary`

        - `:final_answer`

      - `type: :message`

        - `:message`

    - `class FunctionCall`

      - `arguments: String`

        `minLength: 0`, `maxLength: 1048576`

      - `call_id: String`

        `minLength: 1`, `maxLength: 64`

      - `name: String`

        `minLength: 1`, `maxLength: 128`

      - `type: :function_call`

        - `:function_call`

      - `id: String`

        `minLength: 0`, `maxLength: 1048576`

      - `namespace: String`

        `minLength: 1`, `maxLength: 64`

      - `status: :in_progress | :completed | :incomplete`

        - `:in_progress`

        - `:completed`

        - `:incomplete`

    - `class FunctionCallOutput`

      - `call_id: String`

        `minLength: 1`, `maxLength: 64`

      - `output: String | Array[DecisionInputText | DecisionInputImage]`

        Text evidence or an ordered list of text and image parts.

        - `String = String`

        - `Parts = Array[DecisionInputText | DecisionInputImage]`

          - `class DecisionInputText`

          - `class DecisionInputImage`

            An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

      - `type: :function_call_output`

        - `:function_call_output`

      - `id: String`

        `minLength: 0`, `maxLength: 1048576`

      - `status: :in_progress | :completed | :incomplete`

        - `:in_progress`

        - `:completed`

        - `:incomplete`

    - `class CustomToolCall`

      - `call_id: String`

        `minLength: 1`, `maxLength: 64`

      - `input: String`

        `minLength: 0`, `maxLength: 1048576`

      - `name: String`

        `minLength: 1`, `maxLength: 64`

      - `type: :custom_tool_call`

        - `:custom_tool_call`

      - `id: String`

        `minLength: 0`, `maxLength: 1048576`

      - `namespace: String`

        `minLength: 1`, `maxLength: 64`

      - `status: :in_progress | :completed | :incomplete`

        - `:in_progress`

        - `:completed`

        - `:incomplete`

    - `class CustomToolCallOutput`

      - `call_id: String`

        `minLength: 1`, `maxLength: 64`

      - `output: String | Array[DecisionInputText | DecisionInputImage]`

        Text evidence or an ordered list of text and image parts.

        - `String = String`

        - `Parts = Array[DecisionInputText | DecisionInputImage]`

          - `class DecisionInputText`

          - `class DecisionInputImage`

            An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

      - `type: :custom_tool_call_output`

        - `:custom_tool_call_output`

      - `id: String`

        `minLength: 0`, `maxLength: 1048576`

      - `status: :in_progress | :completed | :incomplete`

        - `:in_progress`

        - `:completed`

        - `:incomplete`

- `model: String`

  The model to use. Only `gpt-6-luna` is supported.

  `minLength: 0`, `maxLength: 1048576`

- `questions: Array[Predicate{ instructions, type, name} | Choice{ choices, instructions, type, name} | Score{ instructions, levels, type, name}]`

  Ask 1–400 questions about the input. Each question can be a predicate, choice, or score. Answers come back in the same order.

  `minItems: 1`, `maxItems: 400`

  - `class Predicate`

    Estimate how likely it is that a statement about the input is true.

    - `instructions: String | Array[DecisionQuestionInputPart]`

      - `String = String`

      - `UnionMember1 = Array[DecisionQuestionInputPart]`

        - `class DecisionQuestionInputText`

          - `text: String`

            `minLength: 0`, `maxLength: 10485760`

          - `type: :input_text`

            - `:input_text`

        - `class DecisionQuestionInputImage`

          An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

          - `image_url: String`

            A base64-encoded image in a data URL or a publicly accessible HTTP(S) image URL.

            `minLength: 0`, `maxLength: 1073741824`

          - `type: :input_image`

            - `:input_image`

          - `detail: :low | :high | :auto | :original`

            The image detail level, using the selected model's image profile. Defaults to auto.

            - `:low`

            - `:high`

            - `:auto`

            - `:original`

        - `class DecisionInputJSON`

          A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

    - `type: :predicate`

      The type of the object. Always `predicate`.

      - `:predicate`

    - `name: String`

      `minLength: 0`, `maxLength: 1048576`

  - `class Choice`

    Choose from the supplied options based on the input.

    - `choices: Array[Choice{ value, description}]`

      Provide between 2 and 255 choices. Each choice must be unique.

      `minItems: 2`, `maxItems: 255`

      - `value: String | bool`

        Choice values are typed: a string and a boolean with the same text are distinct.

        - `String = String`

        - `UnionMember1 = bool`

      - `description: String`

        `minLength: 0`, `maxLength: 1048576`

    - `instructions: String | Array[DecisionQuestionInputPart]`

      - `String = String`

      - `UnionMember1 = Array[DecisionQuestionInputPart]`

        - `class DecisionQuestionInputText`

        - `class DecisionQuestionInputImage`

          An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

        - `class DecisionInputJSON`

          A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

    - `type: :choice`

      The type of the object. Always `choice`.

      - `:choice`

    - `name: String`

      `minLength: 0`, `maxLength: 1048576`

  - `class Score`

    Rate the input against the supplied ordered levels.

    - `instructions: String | Array[DecisionQuestionInputPart]`

      - `String = String`

      - `UnionMember1 = Array[DecisionQuestionInputPart]`

        - `class DecisionQuestionInputText`

        - `class DecisionQuestionInputImage`

          An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

        - `class DecisionInputJSON`

          A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

    - `levels: Array[Level{ label, description}]`

      `minItems: 2`, `maxItems: 10`

      - `label: String`

        `minLength: 0`, `maxLength: 1048576`

      - `description: String`

        `minLength: 0`, `maxLength: 1048576`

    - `type: :score`

      The type of the object. Always `score`.

      - `:score`

    - `name: String`

      `minLength: 0`, `maxLength: 1048576`

- `prompt_cache_key: String`

  Partition prompt cache reuse by caller-provided key.

  `minLength: 0`, `maxLength: 64`

- `prompt_cache_options: PromptCacheOptions{ mode, ttl}`

  Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](/api/docs/guides/prompt-caching) for current details.

  - `mode: :implicit | :explicit`

    Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

    - `:implicit`

    - `:explicit`

  - `ttl: :"30m"`

    The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

    - `:"30m"`

- `safety_identifier: String`

  Opaque caller-provided end-user identifier, scoped by the verified org. Match Responses' limit; this is never the authenticated user identity.

  `minLength: 0`, `maxLength: 128`

### Returns

- `class Decision`

  - `answers: Array[Predicate{ name, probability, type} | Choice{ choice, confidence, name, 2 more} | Score{ confidence, name, probabilities, 2 more} | Refusal{ name, type}]`

    Answers in question order. Any question can return a refusal instead of an answer; other questions can still receive answers. A refusal has `type: "refusal"` and the question's `name`, or `null` if it was unnamed.

    `minItems: 0`, `maxItems: 2000`

    - `class Predicate`

      - `name: String`

        `minLength: 0`

      - `probability: Float`

      - `type: :predicate`

        The type of the object. Always `predicate`.

        - `:predicate`

    - `class Choice`

      - `choice: String | bool`

        Choice values are typed: a string and a boolean with the same text are distinct.

        - `String = String`

        - `UnionMember1 = bool`

      - `confidence: Float`

      - `name: String`

        `minLength: 0`

      - `probabilities: Array[Probability{ probability, value}]`

        `minItems: 0`, `maxItems: 2000`

        - `probability: Float`

        - `value: String | bool`

          Choice values are typed: a string and a boolean with the same text are distinct.

          - `String = String`

          - `UnionMember1 = bool`

      - `type: :choice`

        The type of the object. Always `choice`.

        - `:choice`

    - `class Score`

      - `confidence: Float`

      - `name: String`

        `minLength: 0`

      - `probabilities: Array[Probability{ label, probability, value}]`

        `minItems: 0`, `maxItems: 2000`

        - `label: String`

          `minLength: 0`

        - `probability: Float`

        - `value: Integer`

          `format: int64`

      - `score: Float`

      - `type: :score`

        The type of the object. Always `score`.

        - `:score`

    - `class Refusal`

      The model declined to answer this question. Other questions in the same request can still receive answers.

      - `name: String`

        `minLength: 0`

      - `type: :refusal`

        The type of the object. Always `refusal`.

        - `:refusal`

  - `model: String`

    The model used.

    `minLength: 0`

  - `usage: Usage{ input_tokens, input_tokens_details, output_tokens, 2 more}`

    Token usage for the request.

    - `input_tokens: Integer`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `input_tokens_details: InputTokensDetails{ cache_write_tokens, cached_tokens}`

      - `cache_write_tokens: Integer`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

      - `cached_tokens: Integer`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `output_tokens: Integer`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      - `reasoning_tokens: Integer`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `total_tokens: Integer`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

decision = openai.decisions.create(
  input: "string",
  model: "model",
  questions: [{instructions: "string", type: :predicate}]
)

puts(decision)
```

#### 200 — Example

```json
{
  "answers": [
    {
      "name": "name",
      "probability": 0,
      "type": "predicate"
    }
  ],
  "model": "model",
  "usage": {
    "input_tokens": -2147483648,
    "input_tokens_details": {
      "cache_write_tokens": -2147483648,
      "cached_tokens": -2147483648
    },
    "output_tokens": -2147483648,
    "output_tokens_details": {
      "reasoning_tokens": -2147483648
    },
    "total_tokens": -2147483648
  }
}
```

## Domain Types

### Decision

- `class Decision`

  - `answers: Array[Predicate{ name, probability, type} | Choice{ choice, confidence, name, 2 more} | Score{ confidence, name, probabilities, 2 more} | Refusal{ name, type}]`

    Answers in question order. Any question can return a refusal instead of an answer; other questions can still receive answers. A refusal has `type: "refusal"` and the question's `name`, or `null` if it was unnamed.

    `minItems: 0`, `maxItems: 2000`

    - `class Predicate`

      - `name: String`

        `minLength: 0`

      - `probability: Float`

      - `type: :predicate`

        The type of the object. Always `predicate`.

        - `:predicate`

    - `class Choice`

      - `choice: String | bool`

        Choice values are typed: a string and a boolean with the same text are distinct.

        - `String = String`

        - `UnionMember1 = bool`

      - `confidence: Float`

      - `name: String`

        `minLength: 0`

      - `probabilities: Array[Probability{ probability, value}]`

        `minItems: 0`, `maxItems: 2000`

        - `probability: Float`

        - `value: String | bool`

          Choice values are typed: a string and a boolean with the same text are distinct.

          - `String = String`

          - `UnionMember1 = bool`

      - `type: :choice`

        The type of the object. Always `choice`.

        - `:choice`

    - `class Score`

      - `confidence: Float`

      - `name: String`

        `minLength: 0`

      - `probabilities: Array[Probability{ label, probability, value}]`

        `minItems: 0`, `maxItems: 2000`

        - `label: String`

          `minLength: 0`

        - `probability: Float`

        - `value: Integer`

          `format: int64`

      - `score: Float`

      - `type: :score`

        The type of the object. Always `score`.

        - `:score`

    - `class Refusal`

      The model declined to answer this question. Other questions in the same request can still receive answers.

      - `name: String`

        `minLength: 0`

      - `type: :refusal`

        The type of the object. Always `refusal`.

        - `:refusal`

  - `model: String`

    The model used.

    `minLength: 0`

  - `usage: Usage{ input_tokens, input_tokens_details, output_tokens, 2 more}`

    Token usage for the request.

    - `input_tokens: Integer`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `input_tokens_details: InputTokensDetails{ cache_write_tokens, cached_tokens}`

      - `cache_write_tokens: Integer`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

      - `cached_tokens: Integer`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `output_tokens: Integer`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      - `reasoning_tokens: Integer`

        `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

    - `total_tokens: Integer`

      `format: int64`, `minimum: -2147483648`, `maximum: 2147483647`

### Decision Input Image

- `class DecisionInputImage`

  An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

  - `image_url: String`

    A base64-encoded image in a data URL or a publicly accessible HTTP(S) image URL.

    `minLength: 0`, `maxLength: 1073741824`

  - `type: :input_image`

    - `:input_image`

  - `detail: :low | :high | :auto | :original`

    The image detail level, using the selected model's image profile. Defaults to auto.

    - `:low`

    - `:high`

    - `:auto`

    - `:original`

  - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

    Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

    - `mode: :explicit`

      The breakpoint mode. Always `explicit`.

      - `:explicit`

### Decision Input Message

- `DecisionInputMessage = User{ content, role, type} | Developer{ content, role, type} | System{ content, role, type} | Assistant{ content, role, phase, type}`

  A user message containing input text, images, or JSON.

  - `class User`

    A user message containing input text, images, or JSON.

    - `content: String | Array[DecisionInputPart]`

      A text string or an ordered list of text, image, and JSON parts.

      - `String = String`

      - `Parts = Array[DecisionInputPart]`

        - `class DecisionInputText`

          - `text: String`

            `minLength: 0`, `maxLength: 10485760`

          - `type: :input_text`

            - `:input_text`

          - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

            Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

            - `mode: :explicit`

              The breakpoint mode. Always `explicit`.

              - `:explicit`

        - `class DecisionInputImage`

          An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

          - `image_url: String`

            A base64-encoded image in a data URL or a publicly accessible HTTP(S) image URL.

            `minLength: 0`, `maxLength: 1073741824`

          - `type: :input_image`

            - `:input_image`

          - `detail: :low | :high | :auto | :original`

            The image detail level, using the selected model's image profile. Defaults to auto.

            - `:low`

            - `:high`

            - `:auto`

            - `:original`

          - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

            Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

        - `class DecisionInputJSON`

          A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

          - `data: Hash[Symbol, untyped] | Array[Hash[Symbol, untyped]]`

            - `UnionMember0 = Hash[Symbol, untyped]`

            - `UnionMember1 = Array[Hash[Symbol, untyped]]`

          - `type: :input_json`

            - `:input_json`

    - `role: :user`

      - `:user`

    - `type: :message`

      - `:message`

  - `class Developer`

    A developer message containing input text.

    - `content: String | Array[DecisionInputText]`

      A text string or an ordered list of input text parts.

      - `String = String`

      - `Parts = Array[DecisionInputText]`

        - `text: String`

          `minLength: 0`, `maxLength: 10485760`

        - `type: :input_text`

        - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

          Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

    - `role: :developer`

      - `:developer`

    - `type: :message`

      - `:message`

  - `class System`

    A system message containing input text.

    - `content: String | Array[DecisionInputText]`

      A text string or an ordered list of input text parts.

      - `String = String`

      - `Parts = Array[DecisionInputText]`

        - `text: String`

          `minLength: 0`, `maxLength: 10485760`

        - `type: :input_text`

        - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

          Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

    - `role: :system`

      - `:system`

    - `type: :message`

      - `:message`

  - `class Assistant`

    An assistant message containing output text or refusals.

    - `content: String | Array[OutputText{ text, type} | Refusal{ refusal, type}]`

      A text string or an ordered list of output text and refusal parts.

      - `String = String`

      - `Parts = Array[OutputText{ text, type} | Refusal{ refusal, type}]`

        - `class OutputText`

          - `text: String`

            `minLength: 0`, `maxLength: 10485760`

          - `type: :output_text`

            - `:output_text`

        - `class Refusal`

          - `refusal: String`

            `minLength: 0`, `maxLength: 10485760`

          - `type: :refusal`

            - `:refusal`

    - `role: :assistant`

      - `:assistant`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message.

      - `:commentary`

      - `:final_answer`

    - `type: :message`

      - `:message`

### Decision Input Part

- `DecisionInputPart = DecisionInputText | DecisionInputImage | DecisionInputJSON`

  An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

  - `class DecisionInputText`

    - `text: String`

      `minLength: 0`, `maxLength: 10485760`

    - `type: :input_text`

      - `:input_text`

    - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

      Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

      - `mode: :explicit`

        The breakpoint mode. Always `explicit`.

        - `:explicit`

  - `class DecisionInputImage`

    An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

    - `image_url: String`

      A base64-encoded image in a data URL or a publicly accessible HTTP(S) image URL.

      `minLength: 0`, `maxLength: 1073741824`

    - `type: :input_image`

      - `:input_image`

    - `detail: :low | :high | :auto | :original`

      The image detail level, using the selected model's image profile. Defaults to auto.

      - `:low`

      - `:high`

      - `:auto`

      - `:original`

    - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

      Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

  - `class DecisionInputJSON`

    A JSON object or an array of objects rendered as text. Nested values may be any JSON value. Limited to 32 container levels, 10,000 values, and 256 KiB of compact UTF-8 JSON.

    - `data: Hash[Symbol, untyped] | Array[Hash[Symbol, untyped]]`

      - `UnionMember0 = Hash[Symbol, untyped]`

      - `UnionMember1 = Array[Hash[Symbol, untyped]]`

    - `type: :input_json`

      - `:input_json`

### Decision Input Text

- `class DecisionInputText`

  - `text: String`

    `minLength: 0`, `maxLength: 10485760`

  - `type: :input_text`

    - `:input_text`

  - `prompt_cache_breakpoint: DecisionPromptCacheBreakpoint`

    Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

    - `mode: :explicit`

      The breakpoint mode. Always `explicit`.

      - `:explicit`

### Decision Prompt Cache Breakpoint

- `class DecisionPromptCacheBreakpoint`

  Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request's `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

  - `mode: :explicit`

    The breakpoint mode. Always `explicit`.

    - `:explicit`
