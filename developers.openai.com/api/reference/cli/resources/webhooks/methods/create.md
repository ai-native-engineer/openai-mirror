<!-- source: https://developers.openai.com/api/reference/cli/resources/webhooks/methods/create/ -->

## Create Webhook Endpoint

`$ openai webhooks create`

**post** `/webhook_endpoints`

Creates a webhook endpoint for the authenticated project.

- `--event-type: array of "batch.completed" or "batch.failed" or "batch.expired" or 15 more`

  The event types that trigger deliveries to this endpoint.

- `--name: string`

  A human-readable name for the webhook endpoint.

- `--url: string`

  The HTTPS URL that receives webhook deliveries.

- `webhook_endpoint_with_secret: object { id, created_at, event_types, 6 more }`

  - `id: string`

    The unique ID of the webhook endpoint.

  - `created_at: number`

    The Unix timestamp when the endpoint was created.

  - `event_types: array of string`

    The event types that trigger deliveries to this endpoint.

  - `name: string`

    The human-readable name of the endpoint.

  - `object: "webhook_endpoint"`

    The object type, which is always webhook_endpoint.

  - `signing_secret: string`

    The endpoint's signing secret. This is returned only when the endpoint is created or the secret is rotated.

  - `signing_secret_hint: string`

    A masked hint for the endpoint's signing secret.

  - `url: string`

    The HTTPS URL that receives webhook deliveries.

  - `updated_at: optional number`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```cli
openai webhooks create \
  --api-key 'My API Key' \
  --event-type batch.completed \
  --name x \
  --url https://

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
