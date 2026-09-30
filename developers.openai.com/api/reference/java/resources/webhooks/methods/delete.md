<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/methods/delete/ -->

## Delete Webhook Endpoint

`DeletedWebhookEndpoint webhooks().delete(WebhookDeleteParamsparams = WebhookDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/webhook_endpoints/{webhook_endpoint_id}`

Deletes a webhook endpoint for the authenticated project.

- `WebhookDeleteParams params`

  - `Optional<String> webhookEndpointId`

- `class DeletedWebhookEndpoint:`

  - `String id`

    The ID of the deleted webhook endpoint.

  - `boolean deleted`

    Whether the endpoint was deleted.

  - `JsonValue; object_ "webhook_endpoint.deleted"constant`

    The object type, which is always webhook_endpoint.deleted.

    - `WEBHOOK_ENDPOINT_DELETED("webhook_endpoint.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.webhooks.DeletedWebhookEndpoint;
import com.openai.models.webhooks.WebhookDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        DeletedWebhookEndpoint deletedWebhookEndpoint = client.webhooks().delete("whe_123");

  "deleted": true,
  "object": "webhook_endpoint.deleted"
