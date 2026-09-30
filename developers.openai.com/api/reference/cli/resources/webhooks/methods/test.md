<!-- source: https://developers.openai.com/api/reference/cli/resources/webhooks/methods/test/ -->

## Test Webhook Endpoint

`$ openai webhooks test`

**post** `/webhook_endpoints/{webhook_endpoint_id}/test`

Sends a sample event to a webhook endpoint for the authenticated project.

- `--webhook-endpoint-id: string`

  The ID of the webhook endpoint to test.

- `--event-type: "batch.completed" or "batch.failed" or "batch.expired" or 15 more`

  The event type to send as a sample delivery.

- `webhook_endpoint_test_result: object { event_type, object, status_code, 2 more }`

  - `event_type: string`

    The event type sent in the test.

  - `object: "webhook_endpoint.test"`

    The object type, which is always webhook_endpoint.test.

  - `status_code: number`

    The HTTP status code returned by the endpoint.

  - `success: true`

    Whether the test request completed. Always true for returned results; use status_code to determine the endpoint response.

  - `webhook_endpoint_id: string`

    The ID of the webhook endpoint that received the test.

```cli
openai webhooks test \
  --api-key 'My API Key' \
  --webhook-endpoint-id whe_123 \
  --event-type batch.completed

  "event_type": "event_type",
  "object": "webhook_endpoint.test",
  "status_code": 0,
  "success": true,
  "webhook_endpoint_id": "webhook_endpoint_id"
