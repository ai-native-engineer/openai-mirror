<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve/ -->

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

# Retrieve project group

[ProjectGroup](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.groups%20%3E%20(model)%20project_group%20%3E%20(schema)) admin().organization().projects().groups().retrieve(GroupRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/groups/{group\_id}

Retrieves a project’s group.

##### ParametersExpand Collapse

GroupRetrieveParams params

String projectId

Optional<String> groupId

Optional<[GroupType](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/retrieve#(resource)%20admin.organization.projects.groups%20%3E%20(method)%20retrieve%20%3E%20(params)%20default%20%3E%20(param)%20group_type%20%3E%20(schema))> groupType

The type of group to retrieve.

GROUP("group")

TENANT\_GROUP("tenant\_group")

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

### Retrieve project group

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
import com.openai.models.admin.organization.projects.groups.GroupRetrieveParams;
import com.openai.models.admin.organization.projects.groups.ProjectGroup;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GroupRetrieveParams params = GroupRetrieveParams.builder()
            .projectId("project_id")
            .groupId("group_id")
            .build();
        ProjectGroup projectGroup = client.admin().organization().projects().groups().retrieve(params);

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "group_type": "group",
    "created_at": 1711471533

##### Returns Examples

    "object": "project.group",
    "project_id": "proj_abc123",
    "group_id": "group_01J1F8ABCDXYZ",
    "group_name": "Support Team",
    "group_type": "group",
    "created_at": 1711471533
