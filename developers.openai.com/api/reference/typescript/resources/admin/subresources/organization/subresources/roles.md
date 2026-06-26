<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List organization roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/list)

client.admin.organization.roles.list(RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/organization/roles

##### [Create organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/create)

client.admin.organization.roles.create(RoleCreateParams { permissions, role\_name, description } body, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles

##### [Retrieve organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

client.admin.organization.roles.retrieve(stringroleID, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/update)

client.admin.organization.roles.update(stringroleID, RoleUpdateParams { description, permissions, role\_name } body, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/delete)

client.admin.organization.roles.delete(stringroleID, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

Role { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: string

Identifier for the role.

description: string | null

Optional description of the role.

name: string

Unique name for the role.

object: "role"

Always `role`.

permissions: Array<string>

Permissions granted by the role.

predefined\_role: boolean

Whether the role is predefined and managed by OpenAI.

resource\_type: string

Resource type the role is bound to (for example `api.organization` or `api.project`).

RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.
