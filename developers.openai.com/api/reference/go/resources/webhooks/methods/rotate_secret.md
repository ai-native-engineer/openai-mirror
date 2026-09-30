<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/rotate_secret/ -->

## Rotate Webhook Endpoint Signing Secret

`client.Webhooks.RotateSecret(ctx, webhookEndpointID, body) (*WebhookEndpointWithSecret, error)`

**post** `/webhook_endpoints/{webhook_endpoint_id}/rotate_secret`

Rotates the signing secret for a webhook endpoint in the authenticated project.

- `webhookEndpointID string`

- `body WebhookRotateSecretParams`

  - `KeepOldSecretActiveFor24Hours param.Field[bool]`

    Whether to keep the previous signing secret valid for 24 hours after rotation. Defaults to false, which invalidates the previous secret immediately.

- `type WebhookEndpointWithSecret struct{…}`

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

  - `SigningSecret string`

    The endpoint's signing secret. This is returned only when the endpoint is created or the secret is rotated.

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
  webhookEndpointWithSecret, err := client.Webhooks.RotateSecret(
    context.TODO(),
    "whe_123",
    webhooks.WebhookRotateSecretParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", webhookEndpointWithSecret.ID)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
