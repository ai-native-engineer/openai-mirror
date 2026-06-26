<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Groups](/api/reference/java/resources/admin/subresources/organization/subresources/groups)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assign organization role to group

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().groups().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}/roles

Assigns an organization role to a group within the organization.

##### ParametersExpand Collapse

RoleCreateParams params

Optional<String> groupId

String roleId

Identifier of the role to assign.

##### ReturnsExpand Collapse

class RoleCreateResponse:

Role assignment linking a group to a role.

Group group

Summary information about a group returned in role assignment responses.

String id

Identifier for the group.

long createdAt

Unix timestamp (in seconds) when the group was created.

formatunixtime

String name

Display name of the group.

JsonValue; object\_ "group"constant"group"constant

Always `group`.

boolean scimManaged

Whether the group is managed through SCIM.

JsonValue; object\_ "group.role"constant"group.role"constant

Always `group.role`.

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) role

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

### Assign organization role to group

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.groups.roles.RoleCreateParams;
import com.openai.models.admin.organization.groups.roles.RoleCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleCreateParams params = RoleCreateParams.builder()
            .groupId("group_id")
            .roleId("role_id")
            .build();
        RoleCreateResponse role = client.admin().organization().groups().roles().create(params);

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
    "role": {
        "object": "role",
        "id": "role_01J1F8ROLE01",
        "name": "API Group Manager",
        "description": "Allows managing organization groups",
        "permissions": [
            "api.groups.read",
            "api.groups.write"
        ],
        "resource_type": "api.organization",
        "predefined_role": false

##### Returns Examples

    "object": "group.role",
    "group": {
        "object": "group",
        "id": "group_01J1F8ABCDXYZ",
        "name": "Support Team",
        "created_at": 1711471533,
        "scim_managed": false
    "role": {
        "object": "role",
        "id": "role_01J1F8ROLE01",
        "name": "API Group Manager",
        "description": "Allows managing organization groups",
        "permissions": [
            "api.groups.read",
            "api.groups.write"
        ],
        "resource_type": "api.organization",
        "predefined_role": false
