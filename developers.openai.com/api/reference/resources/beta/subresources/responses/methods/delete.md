<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/responses/methods/delete/ -->

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Responses](/api/reference/resources/beta/subresources/responses)

# Delete a model response

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### Path ParametersExpand Collapse

response\_id: string

##### Header ParametersExpand Collapse

"openai-beta": optional array of "responses\_multi\_agent=v1"

### Delete a model response

HTTP

curl -X DELETE https://api.openai.com/v1/responses/resp_123 \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY"

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
