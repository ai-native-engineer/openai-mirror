<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/methods/test/ -->

## Test Webhook Endpoint

`WebhookEndpointTestResult webhooks().test(WebhookTestParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/webhook_endpoints/{webhook_endpoint_id}/test`

Sends a sample event to a webhook endpoint for the authenticated project.

- `WebhookTestParams params`

  - `Optional<String> webhookEndpointId`

  - `EventType eventType`

    The event type to send as a sample delivery.

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

- `class WebhookEndpointTestResult:`

  - `String eventType`

    The event type sent in the test.

  - `JsonValue; object_ "webhook_endpoint.test"constant`

    The object type, which is always webhook_endpoint.test.

    - `WEBHOOK_ENDPOINT_TEST("webhook_endpoint.test")`

  - `long statusCode`

    The HTTP status code returned by the endpoint.

  - `JsonValue; success trueconstant`

    Whether the test request completed. Always true for returned results; use status_code to determine the endpoint response.

    - `TRUE(true)`

  - `String webhookEndpointId`

    The ID of the webhook endpoint that received the test.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.webhooks.WebhookEndpointTestResult;
import com.openai.models.webhooks.WebhookTestParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WebhookTestParams params = WebhookTestParams.builder()
            .webhookEndpointId("whe_123")
            .eventType(WebhookTestParams.EventType.BATCH_COMPLETED)
            .build();
        WebhookEndpointTestResult webhookEndpointTestResult = client.webhooks().test(params);

  "event_type": "event_type",
  "object": "webhook_endpoint.test",
  "status_code": 0,
  "success": true,
  "webhook_endpoint_id": "webhook_endpoint_id"
