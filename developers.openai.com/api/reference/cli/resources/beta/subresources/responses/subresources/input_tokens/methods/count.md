<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses/subresources/input_tokens/methods/count/ -->

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Responses](/api/reference/cli/resources/beta/subresources/responses)

[Input Tokens](/api/reference/cli/resources/beta/subresources/responses/subresources/input_tokens)

# Get input token counts

$ openai beta:responses:input-tokens count

POST/responses/input\_tokens

Returns input token counts of the request.

Returns an object with `object` set to `response.input_tokens` and an `input_tokens` count.

##### ParametersExpand Collapse

--conversation: optional string or [BetaResponseConversationParam](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_conversation_param%20%3E%20(schema)) { id }

Body param: The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.
Input items and output items from this response are automatically added to this conversation after this response completes.

--input: optional string or array of [BetaResponseInputItem](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))

Body param: Text, image, or file inputs to the model, used to generate a response

--instructions: optional string

Body param: A system (or developer) message inserted into the model’s context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

--model: optional string

Body param: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

--parallel-tool-calls: optional boolean

Body param: Whether to allow the model to run tool calls in parallel.

--personality: optional string or "friendly" or "pragmatic"

Body param: A model-owned style preset to apply to this request. Omit this parameter to use the model’s default style. Supported values may expand over time. Values must be at most 64 characters.

--previous-response-id: optional string

Body param: The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

--reasoning: optional object { context, effort, generate\_summary, 2 more }

Body param: **gpt-5 and o-series models only** Configuration options for [reasoning models](https://platform.openai.com/docs/guides/reasoning).

--text: optional object { format, verbosity }

Body param: Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

--tool-choice: optional [BetaToolChoiceOptions](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) or [BetaToolChoiceAllowed](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_allowed%20%3E%20(schema)) { mode, tools, type }  or [BetaToolChoiceTypes](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_types%20%3E%20(schema)) { type }  or 6 more

Body param: Controls which tool the model should use, if any.

--tool: optional array of [BetaTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

Body param: An array of tools the model may call while generating a response. You can specify which tool to use by setting the `tool_choice` parameter.

Deprecated--truncation: optional "auto" or "disabled"

Body param: The truncation strategy to use for the model response. - `auto`: If the input to this Response exceeds the model’s context window size, the model will truncate the response to fit the context window by dropping items from the beginning of the conversation. - `disabled` (default): If the input size will exceed the context window size for a model, the request will fail with a 400 error.

--beta: optional array of "responses\_multi\_agent=v1"

Header param: Optional beta features to enable for this request.

##### ReturnsExpand Collapse

BetaResponseInputTokenCountResponse: object { input\_tokens, object }

input\_tokens: number

object: "response.input\_tokens"

### Get input token counts

CLI Tool

openai beta:responses:input-tokens count \
  --api-key 'My API Key'

  "object": "response.input_tokens",
  "input_tokens": 11

  "object": "response.input_tokens",
  "input_tokens": 11
