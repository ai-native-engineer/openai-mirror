<!-- source: https://developers.openai.com/api/reference/resources/webhooks/methods/create/ -->

# Create Webhook Endpoint

POST/webhook\_endpoints

Creates a webhook endpoint for the authenticated project.

##### Body ParametersJSONExpand Collapse

event\_types: array of "batch.completed" or "batch.failed" or "batch.expired" or 15 more

The event types that trigger deliveries to this endpoint.

"batch.completed"

"batch.failed"

"batch.expired"

"batch.cancelled"

"response.completed"

"response.failed"

"response.cancelled"

"response.incomplete"

"eval.run.succeeded"

"eval.run.failed"

"eval.run.canceled"

"fine\_tuning.job.succeeded"

"fine\_tuning.job.failed"

"fine\_tuning.job.cancelled"

"realtime.call.incoming"

"video.completed"

"video.failed"

"safety.alert.created"

name: string

A human-readable name for the webhook endpoint.

minLength1

maxLength256

url: string

The HTTPS URL that receives webhook deliveries.

maxLength2048

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

### Create Webhook Endpoint

curl https://api.openai.com/v1/webhook_endpoints \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
          "event_types": [
            "batch.completed"
          "name": "x",
          "url": "https://"
        }'

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
