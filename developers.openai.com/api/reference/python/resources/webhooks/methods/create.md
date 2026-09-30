<!-- source: https://developers.openai.com/api/reference/python/resources/webhooks/methods/create/ -->

## Create Webhook Endpoint

`webhooks.create(WebhookCreateParams**kwargs)  -> WebhookEndpointWithSecret`

**post** `/webhook_endpoints`

Creates a webhook endpoint for the authenticated project.

- `event_types: List[Literal["batch.completed", "batch.failed", "batch.expired", 15 more]]`

  The event types that trigger deliveries to this endpoint.

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

- `name: str`

  A human-readable name for the webhook endpoint.

- `url: str`

  The HTTPS URL that receives webhook deliveries.

- `class WebhookEndpointWithSecret: …`

  - `id: str`

    The unique ID of the webhook endpoint.

  - `created_at: int`

    The Unix timestamp when the endpoint was created.

  - `event_types: List[str]`

    The event types that trigger deliveries to this endpoint.

  - `name: str`

    The human-readable name of the endpoint.

  - `object: Literal["webhook_endpoint"]`

    The object type, which is always webhook_endpoint.

    - `"webhook_endpoint"`

  - `signing_secret: str`

    The endpoint's signing secret. This is returned only when the endpoint is created or the secret is rotated.

  - `signing_secret_hint: Optional[str]`

    A masked hint for the endpoint's signing secret.

  - `url: str`

    The HTTPS URL that receives webhook deliveries.

  - `updated_at: Optional[int]`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
webhook_endpoint_with_secret = client.webhooks.create(
    event_types=["batch.completed"],
    name="x",
    url="https://",
print(webhook_endpoint_with_secret.id)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
