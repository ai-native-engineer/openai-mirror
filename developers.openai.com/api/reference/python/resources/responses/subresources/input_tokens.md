<!-- source: https://developers.openai.com/api/reference/python/resources/responses/subresources/input_tokens/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Responses](/api/reference/python/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Input Tokens

##### [Get input token counts](/api/reference/python/resources/responses/subresources/input_tokens/methods/count)

responses.input\_tokens.count(InputTokenCountParams\*\*kwargs)  -> [InputTokenCountResponse](/api/reference/python/resources/responses#(resource)%20responses.input_tokens%20%3E%20(model)%20input_token_count_response%20%3E%20(schema))

POST/responses/input\_tokens

##### ModelsExpand Collapse

class InputTokenCountResponse: …

input\_tokens: int

object: Literal["response.input\_tokens"]
