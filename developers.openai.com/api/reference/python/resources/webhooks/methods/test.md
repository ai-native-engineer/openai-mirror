<!-- source: https://developers.openai.com/api/reference/python/resources/webhooks/methods/test/ -->

## Test Webhook Endpoint

`webhooks.test(strwebhook_endpoint_id, WebhookTestParams**kwargs)  -> WebhookEndpointTestResult`

**post** `/webhook_endpoints/{webhook_endpoint_id}/test`

Sends a sample event to a webhook endpoint for the authenticated project.

- `webhook_endpoint_id: str`

- `event_type: Literal["batch.completed", "batch.failed", "batch.expired", 15 more]`

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

- `class WebhookEndpointTestResult: …`

  - `event_type: str`

    The event type sent in the test.

  - `object: Literal["webhook_endpoint.test"]`

    The object type, which is always webhook_endpoint.test.

    - `"webhook_endpoint.test"`

  - `status_code: int`

    The HTTP status code returned by the endpoint.

  - `success: Literal[true]`

    Whether the test request completed. Always true for returned results; use status_code to determine the endpoint response.

    - `true`

  - `webhook_endpoint_id: str`

    The ID of the webhook endpoint that received the test.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
webhook_endpoint_test_result = client.webhooks.test(
    webhook_endpoint_id="whe_123",
    event_type="batch.completed",
print(webhook_endpoint_test_result.webhook_endpoint_id)

  "event_type": "event_type",
  "object": "webhook_endpoint.test",
  "status_code": 0,
  "success": true,
  "webhook_endpoint_id": "webhook_endpoint_id"
