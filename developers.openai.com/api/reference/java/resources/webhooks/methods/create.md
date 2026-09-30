<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/methods/create/ -->

## Create Webhook Endpoint

`WebhookEndpointWithSecret webhooks().create(WebhookCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/webhook_endpoints`

Creates a webhook endpoint for the authenticated project.

- `WebhookCreateParams params`

  - `List<EventType> eventTypes`

    The event types that trigger deliveries to this endpoint.

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

  - `String name`

    A human-readable name for the webhook endpoint.

  - `String url`

    The HTTPS URL that receives webhook deliveries.

- `class WebhookEndpointWithSecret:`

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

  - `String signingSecret`

    The endpoint's signing secret. This is returned only when the endpoint is created or the secret is rotated.

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
import com.openai.models.webhooks.WebhookCreateParams;
import com.openai.models.webhooks.WebhookEndpointWithSecret;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WebhookCreateParams params = WebhookCreateParams.builder()
            .addEventType(WebhookCreateParams.EventType.BATCH_COMPLETED)
            .name("x")
            .url("https://")
            .build();
        WebhookEndpointWithSecret webhookEndpointWithSecret = client.webhooks().create(params);

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
