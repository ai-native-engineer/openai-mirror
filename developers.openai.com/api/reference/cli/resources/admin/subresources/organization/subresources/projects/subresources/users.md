<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/ -->

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

# Users

##### [List project users](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

$ openai admin:organization:projects:users list

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

$ openai admin:organization:projects:users create

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

$ openai admin:organization:projects:users retrieve

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

$ openai admin:organization:projects:users update

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

$ openai admin:organization:projects:users delete

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

project\_user: object { id, added\_at, object, 3 more }

Represents an individual user in a project.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the project was added.

object: "organization.project.user"

The object type, which is always `organization.project.user`

role: string

`owner` or `member`

email: optional string

The email address of the user

name: optional string

The name of the user

#### UsersRoles

##### [List project user role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

$ openai admin:organization:projects:users:roles list

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

$ openai admin:organization:projects:users:roles create

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

$ openai admin:organization:projects:users:roles retrieve

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

$ openai admin:organization:projects:users:roles delete

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}
