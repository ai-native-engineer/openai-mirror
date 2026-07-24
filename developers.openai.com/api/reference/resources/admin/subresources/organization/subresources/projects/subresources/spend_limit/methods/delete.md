<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Delete project spend limit

DELETE/organization/projects/{project\_id}/spend\_limit

Delete a project’s hard spend limit.

##### Path ParametersExpand Collapse

project\_id: string

ProjectSpendLimitDeleted object { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.

### Delete project spend limit

HTTP

curl -X DELETE https://api.openai.com/v1/organization/projects/proj_abc/spend_limit \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "project.spend_limit.deleted",
    "deleted": true

    "object": "project.spend_limit.deleted",
    "deleted": true
