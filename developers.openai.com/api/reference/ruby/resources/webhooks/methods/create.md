<!-- source: https://developers.openai.com/api/reference/ruby/resources/webhooks/methods/create/ -->

## Create Webhook Endpoint

`webhooks.create(**kwargs) -> WebhookEndpointWithSecret`

**post** `/webhook_endpoints`

Creates a webhook endpoint for the authenticated project.

- `event_types: Array[:"batch.completed" | :"batch.failed" | :"batch.expired" | 15 more]`

  The event types that trigger deliveries to this endpoint.

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

  A human-readable name for the webhook endpoint.

- `url: String`

  The HTTPS URL that receives webhook deliveries.

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

webhook_endpoint_with_secret = openai.webhooks.create(event_types: [:"batch.completed"], name: "x", url: "https://")

puts(webhook_endpoint_with_secret)

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
