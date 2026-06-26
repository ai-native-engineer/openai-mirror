<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Remove project group

[GroupDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20GroupDeleteResponse%20%3E%20(schema)) admin().organization().projects().groups().delete(GroupDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/groups/{group\_id}

Revokes a group’s access to a project.

##### ParametersExpand Collapse

GroupDeleteParams params

String projectId

Optional<String> groupId

##### ReturnsExpand Collapse

class GroupDeleteResponse:

Confirmation payload returned after removing a group from a project.

boolean deleted

Whether the group membership in the project was removed.

JsonValue; object\_ "project.group.deleted"constant"project.group.deleted"constant

Always `project.group.deleted`.

### Remove project group

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
import com.openai.models.admin.organization.projects.groups.GroupDeleteParams;
import com.openai.models.admin.organization.projects.groups.GroupDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GroupDeleteParams params = GroupDeleteParams.builder()
            .projectId("project_id")
            .groupId("group_id")
            .build();
        GroupDeleteResponse group = client.admin().organization().projects().groups().delete(params);

    "object": "project.group.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.group.deleted",
    "deleted": true
