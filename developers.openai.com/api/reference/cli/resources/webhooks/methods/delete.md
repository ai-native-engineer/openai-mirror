<!-- source: https://developers.openai.com/api/reference/cli/resources/webhooks/methods/delete/ -->

## Delete Webhook Endpoint

`$ openai webhooks delete`

**delete** `/webhook_endpoints/{webhook_endpoint_id}`

Deletes a webhook endpoint for the authenticated project.

- `--webhook-endpoint-id: string`

  The ID of the webhook endpoint to delete.

- `deleted_webhook_endpoint: object { id, deleted, object }`

  - `id: string`

    The ID of the deleted webhook endpoint.

  - `deleted: boolean`

    Whether the endpoint was deleted.

  - `object: "webhook_endpoint.deleted"`

    The object type, which is always webhook_endpoint.deleted.

```cli
openai webhooks delete \
  --api-key 'My API Key' \
  --webhook-endpoint-id whe_123

  "deleted": true,
  "object": "webhook_endpoint.deleted"
