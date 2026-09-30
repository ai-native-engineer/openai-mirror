<!-- source: https://developers.openai.com/api/reference/ruby/resources/webhooks/methods/update/ -->

## Update Webhook Endpoint

`webhooks.update(webhook_endpoint_id, **kwargs) -> WebhookEndpoint`

**post** `/webhook_endpoints/{webhook_endpoint_id}`

Updates a webhook endpoint for the authenticated project.

- `webhook_endpoint_id: String`

- `event_types: Array[:"batch.completed" | :"batch.failed" | :"batch.expired" | 15 more]`

  The complete set of event types that should trigger deliveries.

  - `:"batch.completed"`

  - `:"batch.failed"`

  - `:"batch.expired"`

  - `:"batch.cancelled"`

  - `:"response.completed"`

  - `:"response.failed"`

  - `:"response.cancelled"`

  - `:"response.incomplete"`

  - `:"eval.run.succeeded"`

  - `:"eval.run.failed"`

  - `:"eval.run.canceled"`

  - `:"fine_tuning.job.succeeded"`

  - `:"fine_tuning.job.failed"`

  - `:"fine_tuning.job.cancelled"`

  - `:"realtime.call.incoming"`

  - `:"video.completed"`

  - `:"video.failed"`

  - `:"safety.alert.created"`

- `name: String`

  A new human-readable name for the webhook endpoint.

- `url: String`

  A new HTTPS URL that receives webhook deliveries.

- `class WebhookEndpoint`

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

  - `signing_secret_hint: String`

    A masked hint for the endpoint's signing secret.

  - `url: String`

    The HTTPS URL that receives webhook deliveries.

  - `updated_at: Integer`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

webhook_endpoint = openai.webhooks.update("whe_123")

puts(webhook_endpoint)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
