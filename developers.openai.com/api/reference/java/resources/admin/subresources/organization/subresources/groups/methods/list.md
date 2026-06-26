<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/list/ -->

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

# List groups

GroupListPage admin().organization().groups().list(GroupListParamsparams = GroupListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups

Lists all groups in the organization.

##### ParametersExpand Collapse

GroupListParams params

Optional<String> after

A cursor for use in pagination. `after` is a group ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with group\_abc, your subsequent call can include `after=group_abc` in order to fetch the next page of the list.

Optional<Long> limit

A limit on the number of groups to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

Optional<[Order](/api/reference/java/resources/admin/subresources/organization/subresources/groups/methods/list#(resource)%20admin.organization.groups%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Specifies the sort order of the returned groups.

ASC("asc")

DESC("desc")

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

### List groups

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
import com.openai.models.admin.organization.groups.GroupListPage;
import com.openai.models.admin.organization.groups.GroupListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GroupListPage page = client.admin().organization().groups().list();

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "object": "group",
            "id": "group_01J1F8ABCDXYZ",
            "name": "Support Team",
            "created_at": 1711471533,
            "is_scim_managed": false
    ],
    "has_more": false,
    "next": null
