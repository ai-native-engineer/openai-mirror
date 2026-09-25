<!-- source: https://developers.openai.com/api/reference/resources/webhooks/subresources/event_types/methods/list/ -->

[Event Types](/api/reference/resources/webhooks/subresources/event_types)

# List Webhook Event Types

GET/webhook\_event\_types

Returns webhook event types visible to the authenticated project.

WebhookEventTypeList object { data, object }

data: array of string

The webhook event types available to the authenticated project.

object: "list"

The object type, which is always list.

### List Webhook Event Types

curl https://api.openai.com/v1/webhook_event_types \

  "data": [
    "string"
  "object": "list"

  "data": [
    "string"
  "object": "list"
