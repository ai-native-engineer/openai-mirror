<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Groups](/api/reference/java/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update group

[GroupUpdateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20GroupUpdateResponse%20%3E%20(schema)) admin().organization().groups().update(GroupUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}

Updates a group’s information.

##### ParametersExpand Collapse

GroupUpdateParams params

Optional<String> groupId

String name

New display name for the group.

minLength1

maxLength255

##### ReturnsExpand Collapse

class GroupUpdateResponse:

Response returned after updating a group.

String id

Identifier for the group.

long createdAt

Unix timestamp (in seconds) when the group was created.

formatunixtime

boolean isScimManaged

Whether the group is managed through SCIM and controlled by your identity provider.

String name

Updated display name for the group.

### Update group

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
import com.openai.models.admin.organization.groups.GroupUpdateParams;
import com.openai.models.admin.organization.groups.GroupUpdateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GroupUpdateParams params = GroupUpdateParams.builder()
            .groupId("group_id")
            .name("x")
            .build();
        GroupUpdateResponse group = client.admin().organization().groups().update(params);

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false
