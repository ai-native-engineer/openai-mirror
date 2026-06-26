<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/roles/methods/delete/ -->

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

# Delete project role

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().projects().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/projects/{project\_id}/roles/{role\_id}

Deletes a custom role from a project.

##### ParametersExpand Collapse

RoleDeleteParams params

String projectId

Optional<String> roleId

##### ReturnsExpand Collapse

class RoleDeleteResponse:

Confirmation payload returned after deleting a role.

String id

Identifier of the deleted role.

boolean deleted

Whether the role was deleted.

JsonValue; object\_ "role.deleted"constant"role.deleted"constant

Always `role.deleted`.

### Delete project role

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
import com.openai.models.admin.organization.projects.roles.RoleDeleteParams;
import com.openai.models.admin.organization.projects.roles.RoleDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleDeleteParams params = RoleDeleteParams.builder()
            .projectId("project_id")
            .roleId("role_id")
            .build();
        RoleDeleteResponse role = client.admin().organization().projects().roles().delete(params);

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8PROJ",
    "deleted": true
