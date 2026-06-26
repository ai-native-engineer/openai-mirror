<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/users/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Users

##### [List users](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/list)

admin.organization.users.list(UserListParams\*\*kwargs)  -> SyncConversationCursorPage[[OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))]

GET/organization/users

##### [Retrieve user](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/retrieve)

admin.organization.users.retrieve(struser\_id)  -> [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

GET/organization/users/{user\_id}

##### [Modify user](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/update)

admin.organization.users.update(struser\_id, UserUpdateParams\*\*kwargs)  -> [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

POST/organization/users/{user\_id}

##### [Delete user](/api/reference/python/resources/admin/subresources/organization/subresources/users/methods/delete)

admin.organization.users.delete(struser\_id)  -> [UserDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20user_delete_response%20%3E%20(schema))

DELETE/organization/users/{user\_id}

##### ModelsExpand Collapse

class OrganizationUser: …

Represents an individual `user` within an organization.

id: str

The identifier, which can be referenced in API endpoints

added\_at: int

The Unix timestamp (in seconds) of when the user was added.

formatunixtime

object: Literal["organization.user"]

The object type, which is always `organization.user`

api\_key\_last\_used\_at: Optional[int]

The Unix timestamp (in seconds) of the user’s last API key usage.

formatunixtime

created: Optional[int]

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

developer\_persona: Optional[str]

The developer persona metadata for the user.

email: Optional[str]

The email address of the user

is\_default: Optional[bool]

Whether this is the organization’s default user.

is\_scale\_tier\_authorized\_purchaser: Optional[bool]

Whether the user is an authorized purchaser for Scale Tier.

is\_scim\_managed: Optional[bool]

Whether the user is managed through SCIM.

is\_service\_account: Optional[bool]

Whether the user is a service account.

name: Optional[str]

The name of the user

projects: Optional[Projects]

Projects associated with the user, if included.

data: List[ProjectsData]

id: Optional[str]

name: Optional[str]

role: Optional[str]

object: Literal["list"]

role: Optional[str]

`owner` or `reader`

technical\_level: Optional[str]

The technical level metadata for the user.

user: Optional[User]

Nested user details.

id: str

object: Literal["user"]

banned: Optional[bool]

banned\_at: Optional[int]

formatunixtime

email: Optional[str]

enabled: Optional[bool]

name: Optional[str]

picture: Optional[str]

class UserDeleteResponse: …

id: str

deleted: bool

object: Literal["organization.user.deleted"]

#### UsersRoles

##### [List user organization role assignments](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

admin.organization.users.roles.list(struser\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

admin.organization.users.roles.create(struser\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

admin.organization.users.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/python/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

admin.organization.users.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/users/{user\_id}/roles/{role\_id}

##### ModelsExpand Collapse

class RoleListResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleCreateResponse: …

Role assignment linking a user to a role.

object: Literal["user.role"]

Always `user.role`.

role: [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

Details about a role that can be assigned through the public Roles API.

user: [OrganizationUser](/api/reference/python/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20organization_user%20%3E%20(schema))

Represents an individual `user` within an organization.

class RoleRetrieveResponse: …

Detailed information about a role assignment entry returned when listing assignments.

id: str

Identifier for the role.

assignment\_sources: Optional[List[AssignmentSource]]

Principals from which the role assignment is inherited, when available.

principal\_id: str

principal\_type: str

created\_at: Optional[int]

When the role was created.

formatunixtime

created\_by: Optional[str]

Identifier of the actor who created the role.

created\_by\_user\_obj: Optional[Dict[str, object]]

User details for the actor that created the role, when available.

description: Optional[str]

Description of the role.

metadata: Optional[Dict[str, object]]

Arbitrary metadata stored on the role.

name: str

Name of the role.

permissions: List[str]

Permissions associated with the role.

predefined\_role: bool

Whether the role is predefined by OpenAI.

resource\_type: str

Resource type the role applies to.

updated\_at: Optional[int]

When the role was last updated.

formatunixtime

class RoleDeleteResponse: …

Confirmation payload returned after unassigning a role.

deleted: bool

Whether the assignment was removed.

object: str

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.
