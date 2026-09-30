<!-- source: https://developers.openai.com/api/reference/resources/webhooks/methods/test/ -->

# Test Webhook Endpoint

POST/webhook\_endpoints/{webhook\_endpoint\_id}/test

Sends a sample event to a webhook endpoint for the authenticated project.

webhook\_endpoint\_id: string

##### Body ParametersJSONExpand Collapse

event\_type: "batch.completed" or "batch.failed" or "batch.expired" or 15 more

The event type to send as a sample delivery.

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

WebhookEndpointTestResult object { event\_type, object, status\_code, 2 more }

event\_type: string

The event type sent in the test.

object: "webhook\_endpoint.test"

The object type, which is always webhook\_endpoint.test.

status\_code: number

The HTTP status code returned by the endpoint.

success: true

Whether the test request completed. Always true for returned results; use status\_code to determine the endpoint response.

webhook\_endpoint\_id: string

The ID of the webhook endpoint that received the test.

### Test Webhook Endpoint

curl https://api.openai.com/v1/webhook_endpoints/$WEBHOOK_ENDPOINT_ID/test \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
          "event_type": "batch.completed"
        }'

  "event_type": "event_type",
  "object": "webhook_endpoint.test",
  "status_code": 0,
  "success": true,
  "webhook_endpoint_id": "webhook_endpoint_id"

  "event_type": "event_type",
  "object": "webhook_endpoint.test",
  "status_code": 0,
  "success": true,
  "webhook_endpoint_id": "webhook_endpoint_id"
