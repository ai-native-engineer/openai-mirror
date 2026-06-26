<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

##### [List users](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/list)

UserListPage admin().organization().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users

##### [Retrieve user](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/retrieve)

[OrganizationUser](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) admin().organization().users().retrieve(UserRetrieveParamsparams = UserRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/update)

[OrganizationUser](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema)) admin().organization().users().update(UserUpdateParamsparams = UserUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/delete)

[UserDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20UserDeleteResponse%20%3E%20(schema)) admin().organization().users().delete(UserDeleteParamsparams = UserDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationUser:

Represents an individual `user` within an organization.

String id

The identifier, which can be referenced in API endpoints

long addedAt

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

JsonValue; object\_ "organization.user"constant"organization.user"constant

The object type, which is always `organization.user`

Optional<Long> apiKeyLastUsedAt

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

Optional<Long> created

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

Optional<String> developerPersona

The developer persona metadata for the user.

Optional<String> email

The email address of the user

Optional<Boolean> isDefault

Whether this is the organization’s default user.

Optional<Boolean> isScaleTierAuthorizedPurchaser

Whether the user is an authorized purchaser for Scale Tier.

Optional<Boolean> isScimManaged

Whether the user is managed through SCIM.

Optional<Boolean> isServiceAccount

Whether the user is a service account.

Optional<String> name

The name of the user

Optional<Projects> projects

Projects associated with the user, if included.

List<Data> data

Optional<String> id

Optional<String> name

Optional<String> role

JsonValue; object\_ "list"constant"list"constant

Optional<String> role

`owner` or `reader`

Optional<String> technicalLevel

The technical level metadata for the user.

Optional<User> user

Nested user details.

String id

JsonValue; object\_ "user"constant"user"constant

Optional<Boolean> banned

Optional<Long> bannedAt

formatunixtime

Optional<String> email

Optional<Boolean> enabled

Optional<String> name

Optional<String> picture

#### UsersRoles

##### [List user organization role assignments](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

RoleListPage admin().organization().users().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().users().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().users().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().users().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/users/{user\_id}/roles/{role\_id}
