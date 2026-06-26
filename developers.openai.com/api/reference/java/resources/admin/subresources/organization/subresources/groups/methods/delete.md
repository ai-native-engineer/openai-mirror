<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/delete/ -->

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

# Delete group

[GroupDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20GroupDeleteResponse%20%3E%20(schema)) admin().organization().groups().delete(GroupDeleteParamsparams = GroupDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/groups/{group\_id}

Deletes a group from the organization.

##### ParametersExpand Collapse

GroupDeleteParams params

Optional<String> groupId

##### ReturnsExpand Collapse

class GroupDeleteResponse:

Confirmation payload returned after deleting a group.

String id

Identifier of the deleted group.

boolean deleted

Whether the group was deleted.

JsonValue; object\_ "group.deleted"constant"group.deleted"constant

Always `group.deleted`.

### Delete group

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
import com.openai.models.admin.organization.groups.GroupDeleteParams;
import com.openai.models.admin.organization.groups.GroupDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GroupDeleteResponse group = client.admin().organization().groups().delete("group_id");

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true

##### Returns Examples

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true
