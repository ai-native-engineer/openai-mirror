<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Groups

##### [List groups](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/list)

client.Admin.Organization.Groups.List(ctx, query) (\*NextCursorPage[[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema))], error)

GET/organization/groups

##### [Create group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/create)

client.Admin.Organization.Groups.New(ctx, body) (\*[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)), error)

POST/organization/groups

##### [Retrieve group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

client.Admin.Organization.Groups.Get(ctx, groupID) (\*[Group](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/update)

client.Admin.Organization.Groups.Update(ctx, groupID, body) (\*[AdminOrganizationGroupUpdateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20AdminOrganizationGroupUpdateResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/methods/delete)

client.Admin.Organization.Groups.Delete(ctx, groupID) (\*[AdminOrganizationGroupDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20AdminOrganizationGroupDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

type Group struct{…}

Details about an organization group.

ID string

Identifier for the group.

CreatedAt int64

Unix timestamp (in seconds) when the group was created.

formatunixtime

GroupType GroupGroupType

The type of the group.

One of the following:

const GroupGroupTypeGroup GroupGroupType = "group"

const GroupGroupTypeTenantGroup GroupGroupType = "tenant\_group"

IsScimManaged bool

Whether the group is managed through SCIM and controlled by your identity provider.

Name string

Display name of the group.

#### GroupsUsers

##### [List group users](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

client.Admin.Organization.Groups.Users.List(ctx, groupID, query) (\*NextCursorPage[[OrganizationGroupUser](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20organization_group_user%20%3E%20(schema))], error)

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

client.Admin.Organization.Groups.Users.New(ctx, groupID, body) (\*[AdminOrganizationGroupUserNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserNewResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

client.Admin.Organization.Groups.Users.Get(ctx, groupID, userID) (\*[AdminOrganizationGroupUserGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserGetResponse%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

client.Admin.Organization.Groups.Users.Delete(ctx, groupID, userID) (\*[AdminOrganizationGroupUserDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20AdminOrganizationGroupUserDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

type OrganizationGroupUser struct{…}

Represents an individual user returned when inspecting group membership.

ID string

The identifier, which can be referenced in API endpoints

Email string

The email address of the user.

Name string

The name of the user.

#### GroupsRoles

##### [List group organization role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

client.Admin.Organization.Groups.Roles.List(ctx, groupID, query) (\*NextCursorPage[[AdminOrganizationGroupRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleListResponse%20%3E%20(schema))], error)

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

client.Admin.Organization.Groups.Roles.New(ctx, groupID, body) (\*[AdminOrganizationGroupRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleNewResponse%20%3E%20(schema)), error)

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

client.Admin.Organization.Groups.Roles.Get(ctx, groupID, roleID) (\*[AdminOrganizationGroupRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleGetResponse%20%3E%20(schema)), error)

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

client.Admin.Organization.Groups.Roles.Delete(ctx, groupID, roleID) (\*[AdminOrganizationGroupRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20AdminOrganizationGroupRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/groups/{group\_id}/roles/{role\_id}
