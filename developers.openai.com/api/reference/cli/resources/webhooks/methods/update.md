<!-- source: https://developers.openai.com/api/reference/cli/resources/webhooks/methods/update/ -->

## Update Webhook Endpoint

`$ openai webhooks update`

**post** `/webhook_endpoints/{webhook_endpoint_id}`

Updates a webhook endpoint for the authenticated project.

- `--webhook-endpoint-id: string`

  The ID of the webhook endpoint to update.

- `--event-type: optional array of "batch.completed" or "batch.failed" or "batch.expired" or 15 more`

  The complete set of event types that should trigger deliveries.

- `--name: optional string`

  A new human-readable name for the webhook endpoint.

- `--url: optional string`

  A new HTTPS URL that receives webhook deliveries.

- `webhook_endpoint: object { id, created_at, event_types, 5 more }`

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

  - `signing_secret_hint: string`

    A masked hint for the endpoint's signing secret.

  - `url: string`

    The HTTPS URL that receives webhook deliveries.

  - `updated_at: optional number`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```cli
openai webhooks update \
  --api-key 'My API Key' \
  --webhook-endpoint-id whe_123

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
