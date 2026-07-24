<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Spend Limit](/api/reference/resources/admin/subresources/organization/subresources/spend_limit)

# Delete organization spend limit

DELETE/organization/spend\_limit

Delete the organization’s hard spend limit.

OrganizationSpendLimitDeleted object { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.

### Delete organization spend limit

HTTP

curl -X DELETE https://api.openai.com/v1/organization/spend_limit \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "organization.spend_limit.deleted",
    "deleted": true

    "object": "organization.spend_limit.deleted",
    "deleted": true
