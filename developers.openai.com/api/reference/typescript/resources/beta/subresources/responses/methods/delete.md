<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/delete/ -->

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Responses](/api/reference/typescript/resources/beta/subresources/responses)

# Delete a model response

client.beta.responses.delete(stringresponseID, ResponseDeleteParams { betas } params?, RequestOptionsoptions?): void

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

responseID: string

params: ResponseDeleteParams { betas }

betas?: Array<"responses\_multi\_agent=v1">

Optional beta features to enable for this request.

### Delete a model response

TypeScript

import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.delete("resp_123");
console.log(response);

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
