<!-- source: https://developers.openai.com/api/reference/cli/resources/responses/subresources/input_tokens/methods/count/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Responses](/api/reference/cli/resources/responses)

[Input Tokens](/api/reference/cli/resources/responses/subresources/input_tokens)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get input token counts

$ openai responses:input-tokens count

POST/responses/input\_tokens

Returns input token counts of the request.

Returns an object with `object` set to `response.input_tokens` and an `input_tokens` count.

##### ParametersExpand Collapse

--conversation: optional string or [ResponseConversationParam](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_conversation_param%20%3E%20(schema)) { id }

The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.
Input items and output items from this response are automatically added to this conversation after this response completes.

--input: optional string or array of [ResponseInputItem](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_item%20%3E%20(schema))

Text, image, or file inputs to the model, used to generate a response

--instructions: optional string

A system (or developer) message inserted into the model’s context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

--model: optional string

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

--parallel-tool-calls: optional boolean

Whether to allow the model to run tool calls in parallel.

--personality: optional string or "friendly" or "pragmatic"

A model-owned style preset to apply to this request. Omit this parameter to use the model’s default style. Supported values may expand over time. Values must be at most 64 characters.

--previous-response-id: optional string

The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

--reasoning: optional object { context, effort, generate\_summary, summary }

**gpt-5 and o-series models only** Configuration options for [reasoning models](https://platform.openai.com/docs/guides/reasoning).

--text: optional object { format, verbosity }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

--tool-choice: optional [ToolChoiceOptions](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) or [ToolChoiceAllowed](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_allowed%20%3E%20(schema)) { mode, tools, type }  or [ToolChoiceTypes](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_types%20%3E%20(schema)) { type }  or 5 more

Controls which tool the model should use, if any.

--tool: optional array of [Tool](/api/reference/cli/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))

An array of tools the model may call while generating a response. You can specify which tool to use by setting the `tool_choice` parameter.

Deprecated--truncation: optional "auto" or "disabled"

The truncation strategy to use for the model response. - `auto`: If the input to this Response exceeds the model’s context window size, the model will truncate the response to fit the context window by dropping items from the beginning of the conversation. - `disabled` (default): If the input size will exceed the context window size for a model, the request will fail with a 400 error.

##### ReturnsExpand Collapse

InputTokenCountResponse: object { input\_tokens, object }

input\_tokens: number

object: "response.input\_tokens"

### Get input token counts

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai responses:input-tokens count \
  --api-key 'My API Key'

  "object": "response.input_tokens",
  "input_tokens": 11

##### Returns Examples

  "object": "response.input_tokens",
  "input_tokens": 11
