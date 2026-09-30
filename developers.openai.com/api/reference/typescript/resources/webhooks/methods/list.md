<!-- source: https://developers.openai.com/api/reference/typescript/resources/webhooks/methods/list/ -->

## List Webhook Endpoints

`client.webhooks.list(WebhookListParamsquery?, RequestOptionsoptions?): CursorPage<WebhookEndpoint>`

**get** `/webhook_endpoints`

Returns webhook endpoints for the authenticated project in newest-first order.

- `query: WebhookListParams`

  - `after?: string | null`

    ID of the last webhook endpoint from the previous page.

  - `limit?: number`

    Maximum number of webhook endpoints to return. Defaults to 20.

- `WebhookEndpoint`

  - `id: string`

    The unique ID of the webhook endpoint.

  - `created_at: number`

    The Unix timestamp when the endpoint was created.

  - `event_types: Array<string>`

    The event types that trigger deliveries to this endpoint.

  - `name: string`

    The human-readable name of the endpoint.

  - `object: "webhook_endpoint"`

    The object type, which is always webhook_endpoint.

    - `"webhook_endpoint"`

  - `signing_secret_hint: string | null`

    A masked hint for the endpoint's signing secret.

  - `url: string`

    The HTTPS URL that receives webhook deliveries.

  - `updated_at?: number`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const webhookEndpoint of client.webhooks.list()) {
  console.log(webhookEndpoint.id);

  "data": [
      "event_types": [
        "string"
      "object": "webhook_endpoint",
      "signing_secret_hint": "signing_secret_hint",
      "url": "url",
      "updated_at": 0
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
