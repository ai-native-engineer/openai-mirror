<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project roles](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list)

client.Admin.Organization.Projects.Roles.List(ctx, projectID, query) (\*NextCursorPage[[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))], error)

GET/projects/{project\_id}/roles

##### [Create project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/create)

client.Admin.Organization.Projects.Roles.New(ctx, projectID, body) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

POST/projects/{project\_id}/roles

##### [Retrieve project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/retrieve)

client.Admin.Organization.Projects.Roles.Get(ctx, projectID, roleID) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

GET/projects/{project\_id}/roles/{role\_id}

##### [Update project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update)

client.Admin.Organization.Projects.Roles.Update(ctx, projectID, roleID, body) (\*[Role](/api/reference/go/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)), error)

POST/projects/{project\_id}/roles/{role\_id}

##### [Delete project role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete)

client.Admin.Organization.Projects.Roles.Delete(ctx, projectID, roleID) (\*[AdminOrganizationProjectRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20AdminOrganizationProjectRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/projects/{project\_id}/roles/{role\_id}
