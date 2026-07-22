<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/responses/methods/delete/ -->

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Responses](/api/reference/go/resources/beta/subresources/responses)

# Delete a model response

client.Beta.Responses.Delete(ctx, responseID, body) error

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

responseID string

body BetaResponseDeleteParams

Betas param.Field[[]string]Optional

Optional beta features to enable for this request.

const BetaResponseDeleteParamsOpenAIBetaResponsesMultiAgentV1 BetaResponseDeleteParamsOpenAIBeta = "responses\_multi\_agent=v1"

### Delete a model response

Go

package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Beta.Responses.Delete(
    context.TODO(),
    "resp_677efb5139a88190b512bc3fef8e535d",
    openai.BetaResponseDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
