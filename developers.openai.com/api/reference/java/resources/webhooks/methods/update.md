<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/methods/update/ -->

## Update Webhook Endpoint

`WebhookEndpoint webhooks().update(WebhookUpdateParamsparams = WebhookUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/webhook_endpoints/{webhook_endpoint_id}`

Updates a webhook endpoint for the authenticated project.

- `WebhookUpdateParams params`

  - `Optional<String> webhookEndpointId`

  - `Optional<List<EventType>> eventTypes`

    The complete set of event types that should trigger deliveries.

    - `BATCH_COMPLETED("batch.completed")`

    - `BATCH_FAILED("batch.failed")`

    - `BATCH_EXPIRED("batch.expired")`

    - `BATCH_CANCELLED("batch.cancelled")`

    - `RESPONSE_COMPLETED("response.completed")`

    - `RESPONSE_FAILED("response.failed")`

    - `RESPONSE_CANCELLED("response.cancelled")`

    - `RESPONSE_INCOMPLETE("response.incomplete")`

    - `EVAL_RUN_SUCCEEDED("eval.run.succeeded")`

    - `EVAL_RUN_FAILED("eval.run.failed")`

    - `EVAL_RUN_CANCELED("eval.run.canceled")`

    - `FINE_TUNING_JOB_SUCCEEDED("fine_tuning.job.succeeded")`

    - `FINE_TUNING_JOB_FAILED("fine_tuning.job.failed")`

    - `FINE_TUNING_JOB_CANCELLED("fine_tuning.job.cancelled")`

    - `REALTIME_CALL_INCOMING("realtime.call.incoming")`

    - `VIDEO_COMPLETED("video.completed")`

    - `VIDEO_FAILED("video.failed")`

    - `SAFETY_ALERT_CREATED("safety.alert.created")`

  - `Optional<String> name`

    A new human-readable name for the webhook endpoint.

  - `Optional<String> url`

    A new HTTPS URL that receives webhook deliveries.

- `class WebhookEndpoint:`

  - `String id`

    The unique ID of the webhook endpoint.

  - `long createdAt`

    The Unix timestamp when the endpoint was created.

  - `List<String> eventTypes`

    The event types that trigger deliveries to this endpoint.

  - `String name`

    The human-readable name of the endpoint.

  - `JsonValue; object_ "webhook_endpoint"constant`

    The object type, which is always webhook_endpoint.

    - `WEBHOOK_ENDPOINT("webhook_endpoint")`

  - `Optional<String> signingSecretHint`

    A masked hint for the endpoint's signing secret.

  - `String url`

    The HTTPS URL that receives webhook deliveries.

  - `Optional<Long> updatedAt`

    The Unix timestamp of the last endpoint configuration or signing-secret change. Initialized at creation; tests and unchanged updates do not advance it.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.webhooks.WebhookEndpoint;
import com.openai.models.webhooks.WebhookUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WebhookEndpoint webhookEndpoint = client.webhooks().update("whe_123");

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
