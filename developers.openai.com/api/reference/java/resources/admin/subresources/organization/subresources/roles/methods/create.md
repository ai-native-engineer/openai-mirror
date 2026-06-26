<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create organization role

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/roles

Creates a custom role for the organization.

##### ParametersExpand Collapse

RoleCreateParams params

List<String> permissions

Permissions to grant to the role.

String roleName

Unique name for the role.

Optional<String> description

Optional description of the role.

##### ReturnsExpand Collapse

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

### Create organization role

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
import com.openai.models.admin.organization.roles.Role;
import com.openai.models.admin.organization.roles.RoleCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleCreateParams params = RoleCreateParams.builder()
            .addPermission("string")
            .roleName("role_name")
            .build();
        Role role = client.admin().organization().roles().create(params);

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
