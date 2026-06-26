<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Groups

##### [List project groups](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

$ openai admin:organization:projects:groups list

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

$ openai admin:organization:projects:groups create

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

$ openai admin:organization:projects:groups retrieve

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

$ openai admin:organization:projects:groups delete

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

project\_group: object { created\_at, group\_id, group\_name, 3 more }

Details about a group’s membership in a project.

created\_at: number

Unix timestamp (in seconds) when the group was granted project access.

group\_id: string

Identifier of the group that has access to the project.

group\_name: string

Display name of the group.

group\_type: "group" or "tenant\_group"

The type of the group.

"group"

"tenant\_group"

object: "project.group"

Always `project.group`.

project\_id: string

Identifier of the project.

#### GroupsRoles

##### [List project group role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

$ openai admin:organization:projects:groups:roles list

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

$ openai admin:organization:projects:groups:roles create

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

$ openai admin:organization:projects:groups:roles retrieve

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

$ openai admin:organization:projects:groups:roles delete

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}
