<!-- source: https://developers.openai.com/api/reference/ruby/resources/webhooks/methods/list/ -->

## List Webhook Endpoints

`webhooks.list(**kwargs) -> CursorPage<WebhookEndpoint>`

**get** `/webhook_endpoints`

Returns webhook endpoints for the authenticated project in newest-first order.

- `after: String`

  ID of the last webhook endpoint from the previous page.

- `limit: Integer`

  Maximum number of webhook endpoints to return. Defaults to 20.

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

page = openai.webhooks.list

puts(page)

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
