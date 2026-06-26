<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/groups/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Groups](/api/reference/go/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

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
