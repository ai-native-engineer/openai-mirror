<!-- source: https://developers.openai.com/api/reference/typescript/resources/webhooks/methods/create/ -->

## Create Webhook Endpoint

`client.webhooks.create(WebhookCreateParamsbody, RequestOptionsoptions?): WebhookEndpointWithSecret`

**post** `/webhook_endpoints`

Creates a webhook endpoint for the authenticated project.

- `body: WebhookCreateParams`

  - `event_types: Array<"batch.completed" | "batch.failed" | "batch.expired" | 15 more>`

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

  - `name: string`

    A human-readable name for the webhook endpoint.

  - `url: string`

    The HTTPS URL that receives webhook deliveries.

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

const webhookEndpointWithSecret = await client.webhooks.create({
  event_types: ['batch.completed'],
  name: 'x',
  url: 'https://',
});

console.log(webhookEndpointWithSecret.id);

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
