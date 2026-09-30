<!-- source: https://developers.openai.com/api/reference/resources/webhooks/methods/retrieve/ -->

# Retrieve Webhook Endpoint

GET/webhook\_endpoints/{webhook\_endpoint\_id}

Retrieves a webhook endpoint for the authenticated project.

webhook\_endpoint\_id: string

WebhookEndpoint object { id, created\_at, event\_types, 5 more }

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

### Retrieve Webhook Endpoint

curl https://api.openai.com/v1/webhook_endpoints/$WEBHOOK_ENDPOINT_ID \

  "created_at": 0,
  "event_types": [
    "string"
  "name": "name",
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0

  "created_at": 0,
  "event_types": [
    "string"
  "name": "name",
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
