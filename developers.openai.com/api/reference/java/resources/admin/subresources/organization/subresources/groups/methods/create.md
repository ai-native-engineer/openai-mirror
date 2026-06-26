<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/create/ -->

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

# Create group

[Group](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) admin().organization().groups().create(GroupCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups

Creates a new group in the organization.

##### ParametersExpand Collapse

GroupCreateParams params

String name

Human readable name for the group.

minLength1

maxLength255

##### ReturnsExpand Collapse

class Group:

Details about an organization group.

String id

Identifier for the group.

long createdAt

Unix timestamp (in seconds) when the group was created.

formatunixtime

GroupType groupType

The type of the group.

One of the following:

GROUP("group")

TENANT\_GROUP("tenant\_group")

boolean isScimManaged

Whether the group is managed through SCIM and controlled by your identity provider.

String name

Display name of the group.

### Create group

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
import com.openai.models.admin.organization.groups.Group;
import com.openai.models.admin.organization.groups.GroupCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GroupCreateParams params = GroupCreateParams.builder()
            .name("x")
            .build();
        Group group = client.admin().organization().groups().create(params);

    "object": "group",
    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "object": "group",
    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false
