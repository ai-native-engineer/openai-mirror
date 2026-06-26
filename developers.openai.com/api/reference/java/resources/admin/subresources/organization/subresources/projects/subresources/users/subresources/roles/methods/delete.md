<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign project role from user

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().projects().users().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

Unassigns a project role from a user within a project.

##### ParametersExpand Collapse

RoleDeleteParams params

String projectId

String userId

Optional<String> roleId

##### ReturnsExpand Collapse

class RoleDeleteResponse:

Confirmation payload returned after unassigning a role.

boolean deleted

Whether the assignment was removed.

String object\_

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign project role from user

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
import com.openai.models.admin.organization.projects.users.roles.RoleDeleteParams;
import com.openai.models.admin.organization.projects.users.roles.RoleDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleDeleteParams params = RoleDeleteParams.builder()
            .projectId("project_id")
            .userId("user_id")
            .roleId("role_id")
            .build();
        RoleDeleteResponse role = client.admin().organization().projects().users().roles().delete(params);

    "object": "user.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "user.role.deleted",
    "deleted": true
