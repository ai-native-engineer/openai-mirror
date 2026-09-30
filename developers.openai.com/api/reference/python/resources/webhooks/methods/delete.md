<!-- source: https://developers.openai.com/api/reference/python/resources/webhooks/methods/delete/ -->

## Delete Webhook Endpoint

`webhooks.delete(strwebhook_endpoint_id)  -> DeletedWebhookEndpoint`

**delete** `/webhook_endpoints/{webhook_endpoint_id}`

Deletes a webhook endpoint for the authenticated project.

- `webhook_endpoint_id: str`

- `class DeletedWebhookEndpoint: …`

  - `id: str`

    The ID of the deleted webhook endpoint.

  - `deleted: bool`

    Whether the endpoint was deleted.

  - `object: Literal["webhook_endpoint.deleted"]`

    The object type, which is always webhook_endpoint.deleted.

    - `"webhook_endpoint.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
deleted_webhook_endpoint = client.webhooks.delete(
    "whe_123",
print(deleted_webhook_endpoint.id)

  "deleted": true,
  "object": "webhook_endpoint.deleted"
