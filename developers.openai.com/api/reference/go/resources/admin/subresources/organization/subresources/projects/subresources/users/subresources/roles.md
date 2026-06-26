<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project user role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

client.Admin.Organization.Projects.Users.Roles.List(ctx, projectID, userID, query) (\*NextCursorPage[[AdminOrganizationProjectUserRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleListResponse%20%3E%20(schema))], error)

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

client.Admin.Organization.Projects.Users.Roles.New(ctx, projectID, userID, body) (\*[AdminOrganizationProjectUserRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleNewResponse%20%3E%20(schema)), error)

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

client.Admin.Organization.Projects.Users.Roles.Get(ctx, projectID, userID, roleID) (\*[AdminOrganizationProjectUserRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleGetResponse%20%3E%20(schema)), error)

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

client.Admin.Organization.Projects.Users.Roles.Delete(ctx, projectID, userID, roleID) (\*[AdminOrganizationProjectUserRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20AdminOrganizationProjectUserRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}
