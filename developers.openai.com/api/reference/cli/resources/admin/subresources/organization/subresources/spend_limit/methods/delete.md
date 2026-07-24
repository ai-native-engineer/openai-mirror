<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Spend Limit](/api/reference/cli/resources/admin/subresources/organization/subresources/spend_limit)

# Delete organization spend limit

$ openai admin:organization:spend-limit delete

DELETE/organization/spend\_limit

Delete the organization’s hard spend limit.

organization\_spend\_limit\_deleted: object { deleted, object }

Confirmation payload returned after deleting an organization hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "organization.spend\_limit.deleted"

The object type, which is always `organization.spend_limit.deleted`.

### Delete organization spend limit

CLI Tool

openai admin:organization:spend-limit delete \
  --admin-api-key 'My Admin API Key'

    "object": "organization.spend_limit.deleted",
    "deleted": true

    "object": "organization.spend_limit.deleted",
    "deleted": true
