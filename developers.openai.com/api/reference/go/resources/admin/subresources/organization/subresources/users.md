<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/users/ -->

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

# Users

##### [List users](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/list)

client.Admin.Organization.Users.List(ctx, query) (\*ConversationCursorPage[[OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))], error)

GET/organization/users

##### [Retrieve user](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/retrieve)

client.Admin.Organization.Users.Get(ctx, userID) (\*[OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)), error)

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/update)

client.Admin.Organization.Users.Update(ctx, userID, body) (\*[OrganizationUser](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)), error)

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/go/resources/admin/subresources/organization/subresources/users/methods/delete)

client.Admin.Organization.Users.Delete(ctx, userID) (\*[AdminOrganizationUserDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20AdminOrganizationUserDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

type OrganizationUser struct{…}

Represents an individual `user` within an organization.

ID string

The identifier, which can be referenced in API endpoints

AddedAt int64

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

Object OrganizationUser

The object type, which is always `organization.user`

APIKeyLastUsedAt int64Optional

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

Created int64Optional

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

DeveloperPersona stringOptional

The developer persona metadata for the user.

Email stringOptional

The email address of the user

IsDefault boolOptional

Whether this is the organization’s default user.

IsScaleTierAuthorizedPurchaser boolOptional

Whether the user is an authorized purchaser for Scale Tier.

IsScimManaged boolOptional

Whether the user is managed through SCIM.

IsServiceAccount boolOptional

Whether the user is a service account.

Name stringOptional

The name of the user

Projects OrganizationUserProjectsOptional

Projects associated with the user, if included.

Data []OrganizationUserProjectsData

ID stringOptional

Name stringOptional

Role stringOptional

Object List

Role stringOptional

`owner` or `reader`

TechnicalLevel stringOptional

The technical level metadata for the user.

User OrganizationUserUserOptional

Nested user details.

ID string

Object User

Banned boolOptional

BannedAt int64Optional

formatunixtime

Email stringOptional

Enabled boolOptional

Name stringOptional

Picture stringOptional

#### UsersRoles

##### [List user organization role assignments](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

client.Admin.Organization.Users.Roles.List(ctx, userID, query) (\*NextCursorPage[[AdminOrganizationUserRoleListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleListResponse%20%3E%20(schema))], error)

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

client.Admin.Organization.Users.Roles.New(ctx, userID, body) (\*[AdminOrganizationUserRoleNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleNewResponse%20%3E%20(schema)), error)

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

client.Admin.Organization.Users.Roles.Get(ctx, userID, roleID) (\*[AdminOrganizationUserRoleGetResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleGetResponse%20%3E%20(schema)), error)

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/go/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

client.Admin.Organization.Users.Roles.Delete(ctx, userID, roleID) (\*[AdminOrganizationUserRoleDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20AdminOrganizationUserRoleDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/users/{user\_id}/roles/{role\_id}
