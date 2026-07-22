<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses/methods/delete/ -->

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Responses](/api/reference/cli/resources/beta/subresources/responses)

# Delete a model response

$ openai beta:responses delete

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

--response-id: string

The ID of the response to delete.

--beta: optional array of "responses\_multi\_agent=v1"

Optional beta features to enable for this request.

### Delete a model response

CLI Tool

openai beta:responses delete \
  --api-key 'My API Key' \
  --response-id resp_677efb5139a88190b512bc3fef8e535d

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
