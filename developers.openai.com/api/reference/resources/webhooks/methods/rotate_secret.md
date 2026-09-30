<!-- source: https://developers.openai.com/api/reference/resources/webhooks/methods/rotate_secret/ -->

# Rotate Webhook Endpoint Signing Secret

POST/webhook\_endpoints/{webhook\_endpoint\_id}/rotate\_secret

Rotates the signing secret for a webhook endpoint in the authenticated project.

webhook\_endpoint\_id: string

##### Body ParametersJSONExpand Collapse

keep\_old\_secret\_active\_for\_24\_hours: optional boolean

Whether to keep the previous signing secret valid for 24 hours after rotation. Defaults to false, which invalidates the previous secret immediately.

WebhookEndpointWithSecret object { id, created\_at, event\_types, 6 more }

The unique ID of the webhook endpoint.

The Unix timestamp when the endpoint was created.

event\_types: array of string

The event types that trigger deliveries to this endpoint.

name: string

The human-readable name of the endpoint.

object: "webhook\_endpoint"

The object type, which is always webhook\_endpoint.

signing\_secret: string

The endpoint’s signing secret. This is returned only when the endpoint is created or the secret is rotated.

signing\_secret\_hint: string or null

A masked hint for the endpoint’s signing secret.

url: string

The HTTPS URL that receives webhook deliveries.

updated\_at: optional number

The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

### Rotate Webhook Endpoint Signing Secret

curl https://api.openai.com/v1/webhook_endpoints/$WEBHOOK_ENDPOINT_ID/rotate_secret \
    -X POST \

  "created_at": 0,
  "event_types": [
    "string"
  "name": "name",
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0

  "created_at": 0,
  "event_types": [
    "string"
  "name": "name",
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
