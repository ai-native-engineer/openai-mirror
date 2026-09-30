<!-- source: https://developers.openai.com/api/reference/ruby/resources/webhooks/methods/delete/ -->

## Delete Webhook Endpoint

`webhooks.delete(webhook_endpoint_id) -> DeletedWebhookEndpoint`

**delete** `/webhook_endpoints/{webhook_endpoint_id}`

Deletes a webhook endpoint for the authenticated project.

- `webhook_endpoint_id: String`

- `class DeletedWebhookEndpoint`

  - `id: String`

    The ID of the deleted webhook endpoint.

  - `deleted: bool`

    Whether the endpoint was deleted.

  - `object: :"webhook_endpoint.deleted"`

    The object type, which is always webhook_endpoint.deleted.

    - `:"webhook_endpoint.deleted"`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

deleted_webhook_endpoint = openai.webhooks.delete("whe_123")

puts(deleted_webhook_endpoint)

  "deleted": true,
  "object": "webhook_endpoint.deleted"
