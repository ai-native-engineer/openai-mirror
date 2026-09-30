<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/retrieve/ -->

## Retrieve Webhook Endpoint

`client.Webhooks.Get(ctx, webhookEndpointID) (*WebhookEndpoint, error)`

**get** `/webhook_endpoints/{webhook_endpoint_id}`

Retrieves a webhook endpoint for the authenticated project.

- `webhookEndpointID string`

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

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  webhookEndpoint, err := client.Webhooks.Get(context.TODO(), "whe_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", webhookEndpoint.ID)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
