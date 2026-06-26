<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Groups

##### [List groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/list)

$ openai admin:organization:groups list

GET/organization/groups

##### [Create group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/create)

$ openai admin:organization:groups create

POST/organization/groups

##### [Retrieve group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

$ openai admin:organization:groups retrieve

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/update)

$ openai admin:organization:groups update

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/delete)

$ openai admin:organization:groups delete

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

group: object { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

group\_type: "group" or "tenant\_group"

The type of the group.

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

#### GroupsUsers

##### [List group users](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

$ openai admin:organization:groups:users list

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

$ openai admin:organization:groups:users create

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

$ openai admin:organization:groups:users retrieve

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

$ openai admin:organization:groups:users delete

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

organization\_group\_user: object { id, email, name }

Represents an individual user returned when inspecting group membership.

id: string

The identifier, which can be referenced in API endpoints

email: string

The email address of the user.

name: string

The name of the user.

#### GroupsRoles

##### [List group organization role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

$ openai admin:organization:groups:roles list

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

$ openai admin:organization:groups:roles create

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

$ openai admin:organization:groups:roles retrieve

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

$ openai admin:organization:groups:roles delete

DELETE/organization/groups/{group\_id}/roles/{role\_id}
