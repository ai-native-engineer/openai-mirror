<!-- source: https://developers.openai.com/api/reference/python/resources/webhooks/methods/rotate_secret/ -->

## Rotate Webhook Endpoint Signing Secret

`webhooks.rotate_secret(strwebhook_endpoint_id, WebhookRotateSecretParams**kwargs)  -> WebhookEndpointWithSecret`

**post** `/webhook_endpoints/{webhook_endpoint_id}/rotate_secret`

Rotates the signing secret for a webhook endpoint in the authenticated project.

- `webhook_endpoint_id: str`

- `keep_old_secret_active_for_24_hours: Optional[bool]`

  Whether to keep the previous signing secret valid for 24 hours after rotation. Defaults to false, which invalidates the previous secret immediately.

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
webhook_endpoint_with_secret = client.webhooks.rotate_secret(
    webhook_endpoint_id="whe_123",
print(webhook_endpoint_with_secret.id)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
