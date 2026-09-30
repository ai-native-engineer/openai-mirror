<!-- source: https://developers.openai.com/api/reference/resources/webhooks/methods/delete/ -->

# Delete Webhook Endpoint

DELETE/webhook\_endpoints/{webhook\_endpoint\_id}

Deletes a webhook endpoint for the authenticated project.

webhook\_endpoint\_id: string

DeletedWebhookEndpoint object { id, deleted, object }

The ID of the deleted webhook endpoint.

deleted: boolean

Whether the endpoint was deleted.

object: "webhook\_endpoint.deleted"

The object type, which is always webhook\_endpoint.deleted.

### Delete Webhook Endpoint

curl https://api.openai.com/v1/webhook_endpoints/$WEBHOOK_ENDPOINT_ID \
    -X DELETE \

  "deleted": true,
  "object": "webhook_endpoint.deleted"

  "deleted": true,
  "object": "webhook_endpoint.deleted"
