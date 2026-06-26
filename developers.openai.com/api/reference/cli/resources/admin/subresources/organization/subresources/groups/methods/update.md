<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/update/ -->

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

# Update group

$ openai admin:organization:groups update

POST/organization/groups/{group\_id}

Updates a group’s information.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to update.

--name: string

New display name for the group.

##### ReturnsExpand Collapse

AdminOrganizationGroupUpdateResponse: object { id, created\_at, is\_scim\_managed, name }

Response returned after updating a group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Updated display name for the group.

### Update group

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups update \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id \
  --name x

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false
