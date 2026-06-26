<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update project role

[Role](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role%20%3E%20(schema)) admin().organization().projects().roles().update(RoleUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/projects/{project\_id}/roles/{role\_id}

Updates an existing project role.

##### ParametersExpand Collapse

RoleUpdateParams params

String projectId

Optional<String> roleId

Optional<String> description

New description for the role.

Optional<List<String>> permissions

Updated set of permissions for the role.

Optional<String> roleName

New name for the role.

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

### Update project role

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
import com.openai.models.admin.organization.projects.roles.RoleUpdateParams;
import com.openai.models.admin.organization.roles.Role;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleUpdateParams params = RoleUpdateParams.builder()
            .projectId("project_id")
            .roleId("role_id")
            .build();
        Role role = client.admin().organization().projects().roles().update(params);

    "object": "role",
    "id": "role_01J1F8PROJ",
    "name": "API Project Key Manager",
    "description": "Allows managing API keys for the project",
    "permissions": [
        "api.organization.projects.api_keys.read",
        "api.organization.projects.api_keys.write"
    ],
    "resource_type": "api.project",
    "predefined_role": false

##### Returns Examples

    "object": "role",
    "id": "role_01J1F8PROJ",
    "name": "API Project Key Manager",
    "description": "Allows managing API keys for the project",
    "permissions": [
        "api.organization.projects.api_keys.read",
        "api.organization.projects.api_keys.write"
    ],
    "resource_type": "api.project",
    "predefined_role": false
