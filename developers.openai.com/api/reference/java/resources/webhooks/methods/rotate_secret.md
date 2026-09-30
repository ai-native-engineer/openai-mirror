<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/methods/rotate_secret/ -->

## Rotate Webhook Endpoint Signing Secret

`WebhookEndpointWithSecret webhooks().rotateSecret(WebhookRotateSecretParamsparams = WebhookRotateSecretParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/webhook_endpoints/{webhook_endpoint_id}/rotate_secret`

Rotates the signing secret for a webhook endpoint in the authenticated project.

- `WebhookRotateSecretParams params`

  - `Optional<String> webhookEndpointId`

  - `Optional<Boolean> keepOldSecretActiveFor24Hours`

    Whether to keep the previous signing secret valid for 24 hours after rotation. Defaults to false, which invalidates the previous secret immediately.

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
import com.openai.models.webhooks.WebhookEndpointWithSecret;
import com.openai.models.webhooks.WebhookRotateSecretParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WebhookEndpointWithSecret webhookEndpointWithSecret = client.webhooks().rotateSecret("whe_123");

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret": "signing_secret",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
