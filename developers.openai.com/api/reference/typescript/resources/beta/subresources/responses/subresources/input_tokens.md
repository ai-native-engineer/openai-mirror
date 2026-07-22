<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/subresources/input_tokens/ -->

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Responses](/api/reference/typescript/resources/beta/subresources/responses)

# Input Tokens

##### [Get input token counts](/api/reference/typescript/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

client.beta.responses.inputTokens.count(InputTokenCountParams { conversation, input, instructions, 10 more } params?, RequestOptionsoptions?): [InputTokenCountResponse](/api/reference/typescript/resources/beta#(resource)%20beta.responses.input_tokens%20%3E%20(model)%20input_token_count_response%20%3E%20(schema)) { input\_tokens, object }

POST/responses/input\_tokens

##### ModelsExpand Collapse

InputTokenCountResponse { input\_tokens, object }

input\_tokens: number

object: "response.input\_tokens"
