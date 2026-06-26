<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/roles/ -->

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

# Roles

##### [List organization roles](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/list)

RoleListPage admin().organization().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/roles

##### [Create organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/create)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/roles

##### [Retrieve organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/retrieve)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().roles().retrieve(RoleRetrieveParamsparams = RoleRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/roles/{role\_id}

##### [Update organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/update)

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().roles().update(RoleUpdateParamsparams = RoleUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/roles/{role\_id}

##### [Delete organization role](/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().roles().delete(RoleDeleteParamsparams = RoleDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/roles/{role\_id}

##### ModelsExpand Collapse

class Role:

Details about a role that can be assigned through the public Roles API.

String id

Identifier for the role.

Optional<String> description

Optional description of the role.

String name

Unique name for the role.

JsonValue; object\_ "role"constant"role"constant

Always `role`.

List<String> permissions

Permissions granted by the role.

boolean predefinedRole

Whether the role is predefined and managed by OpenAI.

String resourceType

Resource type the role is bound to (for example `api.organization` or `api.project`).
