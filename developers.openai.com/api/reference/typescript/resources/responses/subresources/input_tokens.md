<!-- source: https://developers.openai.com/api/reference/typescript/resources/responses/subresources/input_tokens/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Responses](/api/reference/typescript/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Input Tokens

##### [Get input token counts](/api/reference/typescript/resources/responses/subresources/input_tokens/methods/count)

client.responses.inputTokens.count(InputTokenCountParams { conversation, input, instructions, 9 more } body?, RequestOptionsoptions?): [InputTokenCountResponse](/api/reference/typescript/resources/responses#(resource)%20responses.input_tokens%20%3E%20(model)%20input_token_count_response%20%3E%20(schema)) { input\_tokens, object }

POST/responses/input\_tokens

##### ModelsExpand Collapse

InputTokenCountResponse { input\_tokens, object }

input\_tokens: number

object: "response.input\_tokens"
