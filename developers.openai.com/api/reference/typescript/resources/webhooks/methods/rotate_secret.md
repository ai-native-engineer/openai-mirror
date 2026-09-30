<!-- source: https://developers.openai.com/api/reference/typescript/resources/webhooks/methods/rotate_secret/ -->

## Rotate Webhook Endpoint Signing Secret

`client.webhooks.rotateSecret(stringwebhookEndpointID, WebhookRotateSecretParamsbody?, RequestOptionsoptions?): WebhookEndpointWithSecret`

**post** `/webhook_endpoints/{webhook_endpoint_id}/rotate_secret`

Rotates the signing secret for a webhook endpoint in the authenticated project.

- `webhookEndpointID: string`

- `body: WebhookRotateSecretParams`

  - `keep_old_secret_active_for_24_hours?: boolean`

    Whether to keep the previous signing secret valid for 24 hours after rotation. Defaults to false, which invalidates the previous secret immediately.

- `WebhookEndpointWithSecret`

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

  - `signing_secret: string`

    The endpoint's signing secret. This is returned only when the endpoint is created or the secret is rotated.

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

const webhookEndpointWithSecret = await client.webhooks.rotateSecret('whe_123');

console.log(webhookEndpointWithSecret.id);

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
