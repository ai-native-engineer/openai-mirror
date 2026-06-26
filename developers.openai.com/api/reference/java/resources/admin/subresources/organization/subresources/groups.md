<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/ -->

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

# Groups

##### [List groups](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/list)

GroupListPage admin().organization().groups().list(GroupListParamsparams = GroupListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups

##### [Create group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/create)

[Group](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) admin().organization().groups().create(GroupCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups

##### [Retrieve group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/retrieve)

[Group](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) admin().organization().groups().retrieve(GroupRetrieveParamsparams = GroupRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}

##### [Update group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/update)

[GroupUpdateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20GroupUpdateResponse%20%3E%20(schema)) admin().organization().groups().update(GroupUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}

##### [Delete group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/delete)

[GroupDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20GroupDeleteResponse%20%3E%20(schema)) admin().organization().groups().delete(GroupDeleteParamsparams = GroupDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/groups/{group\_id}

##### ModelsExpand Collapse

class Group:

Details about an organization group.

String id

Identifier for the group.

long createdAt

Unix timestamp (in seconds) when the group was created.

formatunixtime

GroupType groupType

The type of the group.

One of the following:

GROUP("group")

TENANT\_GROUP("tenant\_group")

boolean isScimManaged

Whether the group is managed through SCIM and controlled by your identity provider.

String name

Display name of the group.

#### GroupsUsers

##### [List group users](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list)

UserListPage admin().organization().groups().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/users

##### [Add group user](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create)

[UserCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserCreateResponse%20%3E%20(schema)) admin().organization().groups().users().create(UserCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}/users

##### [Retrieve group user](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve)

[UserRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserRetrieveResponse%20%3E%20(schema)) admin().organization().groups().users().retrieve(UserRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/users/{user\_id}

##### [Remove group user](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/delete)

[UserDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserDeleteResponse%20%3E%20(schema)) admin().organization().groups().users().delete(UserDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/groups/{group\_id}/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationGroupUser:

Represents an individual user returned when inspecting group membership.

String id

The identifier, which can be referenced in API endpoints

Optional<String> email

The email address of the user.

String name

The name of the user.

#### GroupsRoles

##### [List group organization role assignments](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

RoleListPage admin().organization().groups().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().groups().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().groups().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().groups().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/groups/{group\_id}/roles/{role\_id}
