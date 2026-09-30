<!-- source: https://developers.openai.com/api/reference/ruby/resources/webhooks/methods/rotate_secret/ -->

## Rotate Webhook Endpoint Signing Secret

`webhooks.rotate_secret(webhook_endpoint_id, **kwargs) -> WebhookEndpointWithSecret`

**post** `/webhook_endpoints/{webhook_endpoint_id}/rotate_secret`

Rotates the signing secret for a webhook endpoint in the authenticated project.

- `webhook_endpoint_id: String`

- `keep_old_secret_active_for_24_hours: bool`

  Whether to keep the previous signing secret valid for 24 hours after rotation. Defaults to false, which invalidates the previous secret immediately.

- `class WebhookEndpointWithSecret`

  - `id: String`

    The unique ID of the webhook endpoint.

  - `created_at: Integer`

    The Unix timestamp when the endpoint was created.

  - `event_types: Array[String]`

    The event types that trigger deliveries to this endpoint.

  - `name: String`

    The human-readable name of the endpoint.

  - `object: :webhook_endpoint`

    The object type, which is always webhook_endpoint.

    - `:webhook_endpoint`

  - `signing_secret: String`

    The endpoint's signing secret. This is returned only when the endpoint is created or the secret is rotated.

  - `signing_secret_hint: String`

    A masked hint for the endpoint's signing secret.

  - `url: String`

    The HTTPS URL that receives webhook deliveries.

  - `updated_at: Integer`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

webhook_endpoint_with_secret = openai.webhooks.rotate_secret("whe_123")

puts(webhook_endpoint_with_secret)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
