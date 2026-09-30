<!-- source: https://developers.openai.com/api/reference/typescript/resources/webhooks/methods/delete/ -->

## Delete Webhook Endpoint

`client.webhooks.delete(stringwebhookEndpointID, RequestOptionsoptions?): DeletedWebhookEndpoint`

**delete** `/webhook_endpoints/{webhook_endpoint_id}`

Deletes a webhook endpoint for the authenticated project.

- `webhookEndpointID: string`

- `DeletedWebhookEndpoint`

  - `id: string`

    The ID of the deleted webhook endpoint.

  - `deleted: boolean`

    Whether the endpoint was deleted.

  - `object: "webhook_endpoint.deleted"`

    The object type, which is always webhook_endpoint.deleted.

    - `"webhook_endpoint.deleted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const deletedWebhookEndpoint = await client.webhooks.delete('whe_123');

console.log(deletedWebhookEndpoint.id);

  "deleted": true,
  "object": "webhook_endpoint.deleted"
