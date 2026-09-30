<!-- source: https://developers.openai.com/api/reference/typescript/resources/webhooks/methods/test/ -->

## Test Webhook Endpoint

`client.webhooks.test(stringwebhookEndpointID, WebhookTestParamsbody, RequestOptionsoptions?): WebhookEndpointTestResult`

**post** `/webhook_endpoints/{webhook_endpoint_id}/test`

Sends a sample event to a webhook endpoint for the authenticated project.

- `webhookEndpointID: string`

- `body: WebhookTestParams`

  - `event_type: "batch.completed" | "batch.failed" | "batch.expired" | 15 more`

    The event type to send as a sample delivery.

    - `"batch.completed"`

    - `"batch.failed"`

    - `"batch.expired"`

    - `"batch.cancelled"`

    - `"response.completed"`

    - `"response.failed"`

    - `"response.cancelled"`

    - `"response.incomplete"`

    - `"eval.run.succeeded"`

    - `"eval.run.failed"`

    - `"eval.run.canceled"`

    - `"fine_tuning.job.succeeded"`

    - `"fine_tuning.job.failed"`

    - `"fine_tuning.job.cancelled"`

    - `"realtime.call.incoming"`

    - `"video.completed"`

    - `"video.failed"`

    - `"safety.alert.created"`

- `WebhookEndpointTestResult`

  - `event_type: string`

    The event type sent in the test.

  - `object: "webhook_endpoint.test"`

    The object type, which is always webhook_endpoint.test.

    - `"webhook_endpoint.test"`

  - `status_code: number`

    The HTTP status code returned by the endpoint.

  - `success: true`

    Whether the test request completed. Always true for returned results; use status_code to determine the endpoint response.

    - `true`

  - `webhook_endpoint_id: string`

    The ID of the webhook endpoint that received the test.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const webhookEndpointTestResult = await client.webhooks.test('whe_123', {
  event_type: 'batch.completed',
});

console.log(webhookEndpointTestResult.webhook_endpoint_id);

  "event_type": "event_type",
  "object": "webhook_endpoint.test",
  "status_code": 0,
  "success": true,
  "webhook_endpoint_id": "webhook_endpoint_id"
