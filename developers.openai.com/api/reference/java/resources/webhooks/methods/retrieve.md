<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/methods/retrieve/ -->

## Retrieve Webhook Endpoint

`WebhookEndpoint webhooks().retrieve(WebhookRetrieveParamsparams = WebhookRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/webhook_endpoints/{webhook_endpoint_id}`

Retrieves a webhook endpoint for the authenticated project.

- `WebhookRetrieveParams params`

  - `Optional<String> webhookEndpointId`

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
import com.openai.models.webhooks.WebhookRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WebhookEndpoint webhookEndpoint = client.webhooks().retrieve("whe_123");

  "event_types": [
    "string"
  "object": "webhook_endpoint",
  "signing_secret_hint": "signing_secret_hint",
  "url": "url",
  "updated_at": 0
