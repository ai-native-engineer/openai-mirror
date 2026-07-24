<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit/methods/delete/ -->

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Spend Limit](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/spend_limit)

# Delete project spend limit

$ openai admin:organization:projects:spend-limit delete

DELETE/organization/projects/{project\_id}/spend\_limit

Delete a project’s hard spend limit.

##### ParametersExpand Collapse

--project-id: string

The ID of the project whose hard spend limit is being managed.

project\_spend\_limit\_deleted: object { deleted, object }

Confirmation payload returned after deleting a project hard spend limit.

deleted: boolean

Whether the hard spend limit was deleted.

object: "project.spend\_limit.deleted"

The object type, which is always `project.spend_limit.deleted`.

### Delete project spend limit

CLI Tool

openai admin:organization:projects:spend-limit delete \
  --admin-api-key 'My Admin API Key' \
  --project-id proj_123

    "object": "project.spend_limit.deleted",
    "deleted": true

    "object": "project.spend_limit.deleted",
    "deleted": true
