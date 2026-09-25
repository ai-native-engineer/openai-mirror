<!-- source: https://developers.openai.com/api/reference/resources/webhooks/methods/list/ -->

# List Webhook Endpoints

GET/webhook\_endpoints

Returns webhook endpoints for the authenticated project in newest-first order.

##### Query ParametersExpand Collapse

after: optional string or null

ID of the last webhook endpoint from the previous page.

limit: optional number

Maximum number of webhook endpoints to return. Defaults to 20.

minimum1

maximum100

WebhookEndpointList object { data, first\_id, has\_more, 2 more }

data: array of [WebhookEndpoint](/api/reference/resources/webhooks#(resource)%20webhooks%20%3E%20(model)%20webhook_endpoint%20%3E%20(schema)) { id, created\_at, event\_types, 5 more }

The webhook endpoints in this page.

The unique ID of the webhook endpoint.

The Unix timestamp when the endpoint was created.

event\_types: array of string

The event types that trigger deliveries to this endpoint.

name: string

The human-readable name of the endpoint.

object: "webhook\_endpoint"

The object type, which is always webhook\_endpoint.

signing\_secret\_hint: string or null

A masked hint for the endpoint’s signing secret.

url: string

The HTTPS URL that receives webhook deliveries.

updated\_at: optional number

The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

first\_id: string or null

The ID of the first endpoint in this page.

has\_more: boolean

Whether more webhook endpoints are available.

last\_id: string or null

The ID of the last endpoint in this page.

object: "list"

The object type, which is always list.

### List Webhook Endpoints

curl https://api.openai.com/v1/webhook_endpoints \

  "data": [
      "created_at": 0,
      "event_types": [
        "string"
      "name": "name",
      "object": "webhook_endpoint",
      "signing_secret_hint": "signing_secret_hint",
      "url": "url",
      "updated_at": 0
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

  "data": [
      "created_at": 0,
      "event_types": [
        "string"
      "name": "name",
      "object": "webhook_endpoint",
      "signing_secret_hint": "signing_secret_hint",
      "url": "url",
      "updated_at": 0
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
