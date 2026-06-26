<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/ -->

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

# Groups

##### [List project groups](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/list)

client.Admin.Organization.Projects.Groups.List(ctx, projectID, query) (\*NextCursorPage[[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/groups

##### [Add project group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create)

client.Admin.Organization.Projects.Groups.New(ctx, projectID, body) (\*[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/groups

##### [Retrieve project group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve)

client.Admin.Organization.Projects.Groups.Get(ctx, projectID, groupID, query) (\*[ProjectGroup](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/groups/{group\_id}

##### [Remove project group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete)

client.Admin.Organization.Projects.Groups.Delete(ctx, projectID, groupID) (\*[AdminOrganizationProjectGroupDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20AdminOrganizationProjectGroupDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/groups/{group\_id}

##### ModelsExpand Collapse

type ProjectGroup struct{…}

Details about a group’s membership in a project.

CreatedAt int64

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

GroupID string

Identifier of the group that has access to the project.

GroupName string

Display name of the group.

GroupType ProjectGroupGroupType

The type of the group.

One of the following:

const ProjectGroupGroupTypeGroup ProjectGroupGroupType = "group"

const ProjectGroupGroupTypeTenantGroup ProjectGroupGroupType = "tenant\_group"

Object ProjectGroup

Always `project.group`.

ProjectID string

Identifier of the project.

#### GroupsRoles

##### [List project group role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

client.Admin.Organization.Projects.Groups.Roles.List(ctx, projectID, groupID, query) (\*NextCursorPage[[AdminOrganizationProjectGroupRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleListResponse%20%3E%20(schema))], error)

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

client.Admin.Organization.Projects.Groups.Roles.New(ctx, projectID, groupID, body) (\*[AdminOrganizationProjectGroupRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleNewResponse%20%3E%20(schema)), error)

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

client.Admin.Organization.Projects.Groups.Roles.Get(ctx, projectID, groupID, roleID) (\*[AdminOrganizationProjectGroupRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleGetResponse%20%3E%20(schema)), error)

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

client.Admin.Organization.Projects.Groups.Roles.Delete(ctx, projectID, groupID, roleID) (\*[AdminOrganizationProjectGroupRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20AdminOrganizationProjectGroupRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}
