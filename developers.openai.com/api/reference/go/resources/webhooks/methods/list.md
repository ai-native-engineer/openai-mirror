<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/list/ -->

## List Webhook Endpoints

`client.Webhooks.List(ctx, query) (*CursorPage[WebhookEndpoint], error)`

**get** `/webhook_endpoints`

Returns webhook endpoints for the authenticated project in newest-first order.

- `query WebhookListParams`

  - `After param.Field[string]`

    ID of the last webhook endpoint from the previous page.

  - `Limit param.Field[int64]`

    Maximum number of webhook endpoints to return. Defaults to 20.

- `type WebhookEndpoint struct{…}`

  - `ID string`

    The unique ID of the webhook endpoint.

  - `CreatedAt int64`

    The Unix timestamp when the endpoint was created.

  - `EventTypes []string`

    The event types that trigger deliveries to this endpoint.

  - `Name string`

    The human-readable name of the endpoint.

  - `Object WebhookEndpoint`

    The object type, which is always webhook_endpoint.

    - `const WebhookEndpointWebhookEndpoint WebhookEndpoint = "webhook_endpoint"`

  - `SigningSecretHint string`

    A masked hint for the endpoint's signing secret.

  - `URL string`

    The HTTPS URL that receives webhook deliveries.

  - `UpdatedAt int64`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
  "github.com/openai/openai-go/webhooks"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.Webhooks.List(context.TODO(), webhooks.WebhookListParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
      "event_types": [
        "string"
      "object": "webhook_endpoint",
      "signing_secret_hint": "signing_secret_hint",
      "url": "url",
      "updated_at": 0
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
