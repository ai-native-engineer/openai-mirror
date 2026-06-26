<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List organization roles](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/list)

admin.organization.roles.list(\*\*kwargs) -> NextCursorPage<[Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/organization/roles

##### [Create organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/create)

admin.organization.roles.create(\*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles

##### [Retrieve organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

admin.organization.roles.retrieve(role\_id) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/update)

admin.organization.roles.update(role\_id, \*\*kwargs) -> [Role](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/ruby/resources/admin/subresources/organization/subresources/roles/methods/delete)

admin.organization.roles.delete(role\_id) -> [RoleDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

class Role { id, description, name, 4 more }

Details about a role that can be assigned through the public Roles API.

id: String

Identifier for the role.

description: String

Optional description of the role.

name: String

Unique name for the role.

object: :role

Always `role`.

permissions: Array[String]

Permissions granted by the role.

predefined\_role: bool

Whether the role is predefined and managed by OpenAI.

resource\_type: String

Resource type the role is bound to (for example `api.organization` or `api.project`).

class RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: String

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: :"role.deleted"

Always `role.deleted`.
