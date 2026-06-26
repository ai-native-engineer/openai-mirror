<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List organization roles](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/list)

admin.organization.roles.list(RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))]

GET/organization/roles

##### [Create organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/create)

admin.organization.roles.create(RoleCreateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/organization/roles

##### [Retrieve organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

admin.organization.roles.retrieve(strrole\_id)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/update)

admin.organization.roles.update(strrole\_id, RoleUpdateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/python/resources/admin/subresources/organization/subresources/roles/methods/delete)

admin.organization.roles.delete(strrole\_id)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

class Role: …

Details about a role that can be assigned through the public Roles API.

id: str

Identifier for the role.

description: Optional[str]

Optional description of the role.

name: str

Unique name for the role.

object: Literal["role"]

Always `role`.

permissions: List[str]

Permissions granted by the role.

predefined\_role: bool

Whether the role is predefined and managed by OpenAI.

resource\_type: str

Resource type the role is bound to (for example `api.organization` or `api.project`).

class RoleDeleteResponse: …

Confirmation payload returned after deleting a role.

id: str

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: Literal["role.deleted"]

Always `role.deleted`.
