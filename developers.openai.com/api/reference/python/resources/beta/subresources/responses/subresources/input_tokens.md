<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/subresources/input_tokens/ -->

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Responses](/api/reference/python/resources/beta/subresources/responses)

# Input Tokens

##### [Get input token counts](/api/reference/python/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

beta.responses.input\_tokens.count(InputTokenCountParams\*\*kwargs)  -> [InputTokenCountResponse](/api/reference/python/resources/beta#(resource)%20beta.responses.input_tokens%20%3E%20(model)%20input_token_count_response%20%3E%20(schema))

POST/responses/input\_tokens

##### ModelsExpand Collapse

class InputTokenCountResponse: …

input\_tokens: int

object: Literal["response.input\_tokens"]
