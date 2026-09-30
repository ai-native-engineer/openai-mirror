<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/delete/ -->

## Delete Webhook Endpoint

`client.Webhooks.Delete(ctx, webhookEndpointID) (*DeletedWebhookEndpoint, error)`

**delete** `/webhook_endpoints/{webhook_endpoint_id}`

Deletes a webhook endpoint for the authenticated project.

- `webhookEndpointID string`

- `type DeletedWebhookEndpoint struct{…}`

  - `ID string`

    The ID of the deleted webhook endpoint.

  - `Deleted bool`

    Whether the endpoint was deleted.

  - `Object WebhookEndpointDeleted`

    The object type, which is always webhook_endpoint.deleted.

    - `const WebhookEndpointDeletedWebhookEndpointDeleted WebhookEndpointDeleted = "webhook_endpoint.deleted"`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  deletedWebhookEndpoint, err := client.Webhooks.Delete(context.TODO(), "whe_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", deletedWebhookEndpoint.ID)

  "deleted": true,
  "object": "webhook_endpoint.deleted"
