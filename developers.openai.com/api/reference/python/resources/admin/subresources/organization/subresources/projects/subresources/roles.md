<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project roles](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

admin.organization.projects.roles.list(strproject\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))]

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

admin.organization.projects.roles.create(strproject\_id, RoleCreateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

admin.organization.projects.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

admin.organization.projects.roles.update(strrole\_id, RoleUpdateParams\*\*kwargs)  -> [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

admin.organization.projects.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/projects/{project\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleDeleteResponse: …

Confirmation payload returned after deleting a role.

id: str

Identifier of the deleted role.

deleted: bool

Whether the role was deleted.

object: Literal["role.deleted"]

Always `role.deleted`.
