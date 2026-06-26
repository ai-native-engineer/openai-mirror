<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unassign project role from group

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().projects().groups().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

Unassigns a project role from a group within a project.

##### ParametersExpand Collapse

RoleDeleteParams params

String projectId

String groupId

Optional<String> roleId

##### ReturnsExpand Collapse

class RoleDeleteResponse:

Confirmation payload returned after unassigning a role.

boolean deleted

Whether the assignment was removed.

String object\_

Identifier for the deleted assignment, such as `group.role.deleted` or `user.role.deleted`.

### Unassign project role from group

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
import com.openai.models.admin.organization.projects.groups.roles.RoleDeleteParams;
import com.openai.models.admin.organization.projects.groups.roles.RoleDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleDeleteParams params = RoleDeleteParams.builder()
            .projectId("project_id")
            .groupId("group_id")
            .roleId("role_id")
            .build();
        RoleDeleteResponse role = client.admin().organization().projects().groups().roles().delete(params);

    "object": "group.role.deleted",
    "deleted": true

##### Returns Examples

    "object": "group.role.deleted",
    "deleted": true
