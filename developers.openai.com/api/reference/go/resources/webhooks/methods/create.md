<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/create/ -->

## Create Webhook Endpoint

`client.Webhooks.New(ctx, body) (*WebhookEndpointWithSecret, error)`

**post** `/webhook_endpoints`

Creates a webhook endpoint for the authenticated project.

- `body WebhookNewParams`

  - `EventTypes param.Field[[]string]`

    The event types that trigger deliveries to this endpoint.

    - `const WebhookNewParamsEventTypeBatchCompleted WebhookNewParamsEventType = "batch.completed"`

    - `const WebhookNewParamsEventTypeBatchFailed WebhookNewParamsEventType = "batch.failed"`

    - `const WebhookNewParamsEventTypeBatchExpired WebhookNewParamsEventType = "batch.expired"`

    - `const WebhookNewParamsEventTypeBatchCancelled WebhookNewParamsEventType = "batch.cancelled"`

    - `const WebhookNewParamsEventTypeResponseCompleted WebhookNewParamsEventType = "response.completed"`

    - `const WebhookNewParamsEventTypeResponseFailed WebhookNewParamsEventType = "response.failed"`

    - `const WebhookNewParamsEventTypeResponseCancelled WebhookNewParamsEventType = "response.cancelled"`

    - `const WebhookNewParamsEventTypeResponseIncomplete WebhookNewParamsEventType = "response.incomplete"`

    - `const WebhookNewParamsEventTypeEvalRunSucceeded WebhookNewParamsEventType = "eval.run.succeeded"`

    - `const WebhookNewParamsEventTypeEvalRunFailed WebhookNewParamsEventType = "eval.run.failed"`

    - `const WebhookNewParamsEventTypeEvalRunCanceled WebhookNewParamsEventType = "eval.run.canceled"`

    - `const WebhookNewParamsEventTypeFineTuningJobSucceeded WebhookNewParamsEventType = "fine_tuning.job.succeeded"`

    - `const WebhookNewParamsEventTypeFineTuningJobFailed WebhookNewParamsEventType = "fine_tuning.job.failed"`

    - `const WebhookNewParamsEventTypeFineTuningJobCancelled WebhookNewParamsEventType = "fine_tuning.job.cancelled"`

    - `const WebhookNewParamsEventTypeRealtimeCallIncoming WebhookNewParamsEventType = "realtime.call.incoming"`

    - `const WebhookNewParamsEventTypeVideoCompleted WebhookNewParamsEventType = "video.completed"`

    - `const WebhookNewParamsEventTypeVideoFailed WebhookNewParamsEventType = "video.failed"`

    - `const WebhookNewParamsEventTypeSafetyAlertCreated WebhookNewParamsEventType = "safety.alert.created"`

  - `Name param.Field[string]`

    A human-readable name for the webhook endpoint.

  - `URL param.Field[string]`

    The HTTPS URL that receives webhook deliveries.

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
  webhookEndpointWithSecret, err := client.Webhooks.New(context.TODO(), webhooks.WebhookNewParams{
    EventTypes: []string{"batch.completed"},
    Name: "x",
    URL: "https://",
  })
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
