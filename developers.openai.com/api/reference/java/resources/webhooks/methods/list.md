<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/methods/list/ -->

## List Webhook Endpoints

`WebhookListPage webhooks().list(WebhookListParamsparams = WebhookListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/webhook_endpoints`

Returns webhook endpoints for the authenticated project in newest-first order.

- `WebhookListParams params`

  - `Optional<String> after`

    ID of the last webhook endpoint from the previous page.

  - `Optional<Long> limit`

    Maximum number of webhook endpoints to return. Defaults to 20.

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
import com.openai.models.webhooks.WebhookListPage;
import com.openai.models.webhooks.WebhookListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WebhookListPage page = client.webhooks().list();

  "data": [
      "event_types": [
        "string"
      "object": "webhook_endpoint",
      "signing_secret_hint": "signing_secret_hint",
      "url": "url",
      "updated_at": 0
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
