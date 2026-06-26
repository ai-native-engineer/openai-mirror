<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list/ -->

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

# List project roles

RoleListPage admin().organization().projects().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/projects/{project\_id}/roles

Lists the roles configured for a project.

##### ParametersExpand Collapse

RoleListParams params

Optional<String> projectId

Optional<String> after

Cursor for pagination. Provide the value from the previous response’s `next` field to continue listing roles.

Optional<Long> limit

A limit on the number of roles to return. Defaults to 1000.

minimum0

maximum1000

Optional<[Order](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/list#(resource)%20admin.organization.projects.roles%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order for the returned roles.

ASC("asc")

DESC("desc")

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

### List project roles

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
import com.openai.models.admin.organization.projects.roles.RoleListPage;
import com.openai.models.admin.organization.projects.roles.RoleListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleListPage page = client.admin().organization().projects().roles().list("project_id");

    "object": "list",
    "data": [
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
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
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
    ],
    "has_more": false,
    "next": null
