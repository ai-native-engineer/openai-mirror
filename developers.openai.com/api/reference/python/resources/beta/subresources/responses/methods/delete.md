<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/methods/delete/ -->

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Responses](/api/reference/python/resources/beta/subresources/responses)

# Delete a model response

beta.responses.delete(strresponse\_id, ResponseDeleteParams\*\*kwargs)

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

response\_id: str

betas: Optional[List[Literal["responses\_multi\_agent=v1"]]]

### Delete a model response

Python

from openai import OpenAI
client = OpenAI()

response = client.responses.delete("resp_123")
print(response)

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
