<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/test/ -->

## Test Webhook Endpoint

`client.Webhooks.Test(ctx, webhookEndpointID, body) (*WebhookEndpointTestResult, error)`

**post** `/webhook_endpoints/{webhook_endpoint_id}/test`

Sends a sample event to a webhook endpoint for the authenticated project.

- `webhookEndpointID string`

- `body WebhookTestParams`

  - `EventType param.Field[WebhookTestParamsEventType]`

    The event type to send as a sample delivery.

    - `const WebhookTestParamsEventTypeBatchCompleted WebhookTestParamsEventType = "batch.completed"`

    - `const WebhookTestParamsEventTypeBatchFailed WebhookTestParamsEventType = "batch.failed"`

    - `const WebhookTestParamsEventTypeBatchExpired WebhookTestParamsEventType = "batch.expired"`

    - `const WebhookTestParamsEventTypeBatchCancelled WebhookTestParamsEventType = "batch.cancelled"`

    - `const WebhookTestParamsEventTypeResponseCompleted WebhookTestParamsEventType = "response.completed"`

    - `const WebhookTestParamsEventTypeResponseFailed WebhookTestParamsEventType = "response.failed"`

    - `const WebhookTestParamsEventTypeResponseCancelled WebhookTestParamsEventType = "response.cancelled"`

    - `const WebhookTestParamsEventTypeResponseIncomplete WebhookTestParamsEventType = "response.incomplete"`

    - `const WebhookTestParamsEventTypeEvalRunSucceeded WebhookTestParamsEventType = "eval.run.succeeded"`

    - `const WebhookTestParamsEventTypeEvalRunFailed WebhookTestParamsEventType = "eval.run.failed"`

    - `const WebhookTestParamsEventTypeEvalRunCanceled WebhookTestParamsEventType = "eval.run.canceled"`

    - `const WebhookTestParamsEventTypeFineTuningJobSucceeded WebhookTestParamsEventType = "fine_tuning.job.succeeded"`

    - `const WebhookTestParamsEventTypeFineTuningJobFailed WebhookTestParamsEventType = "fine_tuning.job.failed"`

    - `const WebhookTestParamsEventTypeFineTuningJobCancelled WebhookTestParamsEventType = "fine_tuning.job.cancelled"`

    - `const WebhookTestParamsEventTypeRealtimeCallIncoming WebhookTestParamsEventType = "realtime.call.incoming"`

    - `const WebhookTestParamsEventTypeVideoCompleted WebhookTestParamsEventType = "video.completed"`

    - `const WebhookTestParamsEventTypeVideoFailed WebhookTestParamsEventType = "video.failed"`

    - `const WebhookTestParamsEventTypeSafetyAlertCreated WebhookTestParamsEventType = "safety.alert.created"`

- `type WebhookEndpointTestResult struct{…}`

  - `EventType string`

    The event type sent in the test.

  - `Object WebhookEndpointTest`

    The object type, which is always webhook_endpoint.test.

    - `const WebhookEndpointTestWebhookEndpointTest WebhookEndpointTest = "webhook_endpoint.test"`

  - `StatusCode int64`

    The HTTP status code returned by the endpoint.

  - `Success bool`

    Whether the test request completed. Always true for returned results; use status_code to determine the endpoint response.

    - `const TrueTrue True = true`

  - `WebhookEndpointID string`

    The ID of the webhook endpoint that received the test.

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
  webhookEndpointTestResult, err := client.Webhooks.Test(
    context.TODO(),
    "whe_123",
    webhooks.WebhookTestParams{
      EventType: webhooks.WebhookTestParamsEventTypeBatchCompleted,
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", webhookEndpointTestResult.WebhookEndpointID)

  "event_type": "event_type",
  "object": "webhook_endpoint.test",
  "status_code": 0,
  "success": true,
  "webhook_endpoint_id": "webhook_endpoint_id"
