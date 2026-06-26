<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/create/ -->

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

# Add project group

[ProjectGroup](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) admin().organization().projects().groups().create(GroupCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/groups

Grants a group access to a project.

##### ParametersExpand Collapse

GroupCreateParams params

Optional<String> projectId

String groupId

Identifier of the group to add to the project.

String role

Identifier of the project role to grant to the group.

##### ReturnsExpand Collapse

class ProjectGroup:

Details about a group’s membership in a project.

long createdAt

Unix timestamp (in seconds) when the group was granted project access.

formatunixtime

String groupId

Identifier of the group that has access to the project.

String groupName

Display name of the group.

GroupType groupType

The type of the group.

One of the following:

GROUP("group")

TENANT\_GROUP("tenant\_group")

JsonValue; object\_ "project.group"constant"project.group"constant

Always `project.group`.

String projectId

Identifier of the project.

### Add project group

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
import com.openai.models.admin.organization.projects.groups.GroupCreateParams;
import com.openai.models.admin.organization.projects.groups.ProjectGroup;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GroupCreateParams params = GroupCreateParams.builder()
            .projectId("project_id")
            .groupId("group_id")
            .role("role")
            .build();
        ProjectGroup projectGroup = client.admin().organization().projects().groups().create(params);

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "created_at": 1711471533
