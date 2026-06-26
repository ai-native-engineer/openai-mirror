<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/ -->

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

# Users

##### [List project users](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list)

client.Admin.Organization.Projects.Users.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/users

##### [Create project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create)

client.Admin.Organization.Projects.Users.New(ctx, projectID, body) (\*[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/users

##### [Retrieve project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/retrieve)

client.Admin.Organization.Projects.Users.Get(ctx, projectID, userID) (\*[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/users/{user\_id}

##### [Modify project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update)

client.Admin.Organization.Projects.Users.Update(ctx, projectID, userID, body) (\*[ProjectUser](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/users/{user\_id}

##### [Delete project user](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete)

client.Admin.Organization.Projects.Users.Delete(ctx, projectID, userID) (\*[AdminOrganizationProjectUserDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20AdminOrganizationProjectUserDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/users/{user\_id}

##### ModelsExpand Collapse

type ProjectUser struct{…}

Represents an individual user in a project.

ID string

The identifier, which can be referenced in API endpoints

AddedAt int64

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

Object OrganizationProjectUser

The object type, which is always `organization.project.user`

Role string

`owner` or `member`

Email stringOptional

The email address of the user

Name stringOptional

The name of the user

#### UsersRoles

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
