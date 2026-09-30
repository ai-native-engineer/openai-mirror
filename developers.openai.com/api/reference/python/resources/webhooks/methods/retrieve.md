<!-- source: https://developers.openai.com/api/reference/python/resources/webhooks/methods/retrieve/ -->

## Retrieve Webhook Endpoint

`webhooks.retrieve(strwebhook_endpoint_id)  -> WebhookEndpoint`

**get** `/webhook_endpoints/{webhook_endpoint_id}`

Retrieves a webhook endpoint for the authenticated project.

- `webhook_endpoint_id: str`

- `class WebhookEndpoint: …`

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
webhook_endpoint = client.webhooks.retrieve(
    "whe_123",
print(webhook_endpoint.id)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
