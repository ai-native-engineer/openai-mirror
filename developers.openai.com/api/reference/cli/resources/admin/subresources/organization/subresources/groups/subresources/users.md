<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

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
