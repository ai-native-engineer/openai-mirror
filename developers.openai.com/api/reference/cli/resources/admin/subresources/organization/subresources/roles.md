<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/roles/ -->

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

# Roles

##### [List organization roles](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/list)

$ openai admin:organization:roles list

GET/organization/roles

##### [Create organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/create)

$ openai admin:organization:roles create

POST/organization/roles

##### [Retrieve organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

$ openai admin:organization:roles retrieve

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/update)

$ openai admin:organization:roles update

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/roles/methods/delete)

$ openai admin:organization:roles delete

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

role: object { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: string

Identifier for the role.

description: string

Optional description of the role.

name: string

Unique name for the role.

object: "role"

Always `role`.

permissions: array of string

Permissions granted by the role.

predefined\_role: boolean

Whether the role is predefined and managed by OpenAI.

resource\_type: string

Resource type the role is bound to (for example `api.organization` or `api.project`).
