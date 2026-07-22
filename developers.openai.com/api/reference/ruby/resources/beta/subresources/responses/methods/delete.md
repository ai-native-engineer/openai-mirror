<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/responses/methods/delete/ -->

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Responses](/api/reference/ruby/resources/beta/subresources/responses)

# Delete a model response

beta.responses.delete(response\_id, \*\*kwargs) -> void

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

response\_id: String

betas: Array[:"responses\_multi\_agent=v1"]

### Delete a model response

Ruby

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.beta.responses.delete("resp_677efb5139a88190b512bc3fef8e535d")

puts(result)

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
