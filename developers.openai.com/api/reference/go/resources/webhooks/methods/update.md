<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/update/ -->

## Update Webhook Endpoint

`client.Webhooks.Update(ctx, webhookEndpointID, body) (*WebhookEndpoint, error)`

**post** `/webhook_endpoints/{webhook_endpoint_id}`

Updates a webhook endpoint for the authenticated project.

- `webhookEndpointID string`

- `body WebhookUpdateParams`

  - `EventTypes param.Field[[]string]`

    The complete set of event types that should trigger deliveries.

    - `const WebhookUpdateParamsEventTypeBatchCompleted WebhookUpdateParamsEventType = "batch.completed"`

    - `const WebhookUpdateParamsEventTypeBatchFailed WebhookUpdateParamsEventType = "batch.failed"`

    - `const WebhookUpdateParamsEventTypeBatchExpired WebhookUpdateParamsEventType = "batch.expired"`

    - `const WebhookUpdateParamsEventTypeBatchCancelled WebhookUpdateParamsEventType = "batch.cancelled"`

    - `const WebhookUpdateParamsEventTypeResponseCompleted WebhookUpdateParamsEventType = "response.completed"`

    - `const WebhookUpdateParamsEventTypeResponseFailed WebhookUpdateParamsEventType = "response.failed"`

    - `const WebhookUpdateParamsEventTypeResponseCancelled WebhookUpdateParamsEventType = "response.cancelled"`

    - `const WebhookUpdateParamsEventTypeResponseIncomplete WebhookUpdateParamsEventType = "response.incomplete"`

    - `const WebhookUpdateParamsEventTypeEvalRunSucceeded WebhookUpdateParamsEventType = "eval.run.succeeded"`

    - `const WebhookUpdateParamsEventTypeEvalRunFailed WebhookUpdateParamsEventType = "eval.run.failed"`

    - `const WebhookUpdateParamsEventTypeEvalRunCanceled WebhookUpdateParamsEventType = "eval.run.canceled"`

    - `const WebhookUpdateParamsEventTypeFineTuningJobSucceeded WebhookUpdateParamsEventType = "fine_tuning.job.succeeded"`

    - `const WebhookUpdateParamsEventTypeFineTuningJobFailed WebhookUpdateParamsEventType = "fine_tuning.job.failed"`

    - `const WebhookUpdateParamsEventTypeFineTuningJobCancelled WebhookUpdateParamsEventType = "fine_tuning.job.cancelled"`

    - `const WebhookUpdateParamsEventTypeRealtimeCallIncoming WebhookUpdateParamsEventType = "realtime.call.incoming"`

    - `const WebhookUpdateParamsEventTypeVideoCompleted WebhookUpdateParamsEventType = "video.completed"`

    - `const WebhookUpdateParamsEventTypeVideoFailed WebhookUpdateParamsEventType = "video.failed"`

    - `const WebhookUpdateParamsEventTypeSafetyAlertCreated WebhookUpdateParamsEventType = "safety.alert.created"`

  - `Name param.Field[string]`

    A new human-readable name for the webhook endpoint.

  - `URL param.Field[string]`

    A new HTTPS URL that receives webhook deliveries.

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
  webhookEndpoint, err := client.Webhooks.Update(
    context.TODO(),
    "whe_123",
    webhooks.WebhookUpdateParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", webhookEndpoint.ID)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
