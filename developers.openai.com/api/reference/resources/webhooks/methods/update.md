<!-- source: https://developers.openai.com/api/reference/resources/webhooks/methods/update/ -->

# Update Webhook Endpoint

POST/webhook\_endpoints/{webhook\_endpoint\_id}

Updates a webhook endpoint for the authenticated project.

webhook\_endpoint\_id: string

##### Body ParametersJSONExpand Collapse

event\_types: optional array of "batch.completed" or "batch.failed" or "batch.expired" or 15 more

The complete set of event types that should trigger deliveries.

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

name: optional string

A new human-readable name for the webhook endpoint.

minLength1

maxLength256

url: optional string

A new HTTPS URL that receives webhook deliveries.

maxLength2048

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

### Update Webhook Endpoint

curl https://api.openai.com/v1/webhook_endpoints/$WEBHOOK_ENDPOINT_ID \
    -X POST \

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
