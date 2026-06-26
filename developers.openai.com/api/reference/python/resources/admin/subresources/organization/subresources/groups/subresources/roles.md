<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Groups](/api/reference/python/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List group organization role assignments](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

admin.organization.groups.roles.list(strgroup\_id, RoleListParams\*\*kwargs)  -> SyncNextCursorPage[[RoleListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_list_response%20%3E%20(schema))]

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

admin.organization.groups.roles.create(strgroup\_id, RoleCreateParams\*\*kwargs)  -> [RoleCreateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_create_response%20%3E%20(schema))

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

admin.organization.groups.roles.retrieve(strrole\_id, RoleRetrieveParams\*\*kwargs)  -> [RoleRetrieveResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_retrieve_response%20%3E%20(schema))

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/python/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

admin.organization.groups.roles.delete(strrole\_id, RoleDeleteParams\*\*kwargs)  -> [RoleDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema))

DELETE/organization/groups/{group\_id}/roles/{role\_id}

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

Role assignment linking a group to a role.

group: Group

Summary information about a group returned in role assignment responses.

id: str

Identifier for the group.

created\_at: int

Unix timestamp (in seconds) when the group was created.

formatunixtime

name: str

Display name of the group.

object: Literal["group"]

Always `group`.

scim\_managed: bool

Whether the group is managed through SCIM.

object: Literal["group.role"]

Always `group.role`.

role: [Role](/api/reference/python/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema))

Details about a role that can be assigned through the public Roles API.

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
