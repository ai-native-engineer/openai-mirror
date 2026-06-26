<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

client.admin.organization.projects.roles.list(stringprojectID, RoleListParams { after, limit, order } query?, RequestOptionsoptions?): NextCursorPage<[Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more } >

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

client.admin.organization.projects.roles.create(stringprojectID, RoleCreateParams { permissions, role\_name, description } body, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

client.admin.organization.projects.roles.retrieve(stringroleID, RoleRetrieveParams { project\_id } params, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

client.admin.organization.projects.roles.update(stringroleID, RoleUpdateParams { project\_id, description, permissions, role\_name } params, RequestOptionsoptions?): [Role](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) { id, description, name, 4 more }

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

client.admin.organization.projects.roles.delete(stringroleID, RoleDeleteParams { project\_id } params, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/projects/{project\_id}/roles/{role\_id}

##### ModelsExpand Collapse

RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.
