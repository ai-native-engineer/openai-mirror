<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve group

$ openai admin:organization:groups retrieve

GET/organization/groups/{group\_id}

Retrieves a group.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to retrieve.

##### ReturnsExpand Collapse

group: object { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

group\_type: "group" or "tenant\_group"

The type of the group.

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

### Retrieve group

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups retrieve \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"
