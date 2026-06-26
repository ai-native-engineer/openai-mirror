<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/methods/delete/ -->

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

# Delete group

$ openai admin:organization:groups delete

DELETE/organization/groups/{group\_id}

Deletes a group from the organization.

##### ParametersExpand Collapse

--group-id: string

The ID of the group to delete.

##### ReturnsExpand Collapse

AdminOrganizationGroupDeleteResponse: object { id, deleted, object }

Confirmation payload returned after deleting a group.

id: string

Identifier of the deleted group.

deleted: boolean

Whether the group was deleted.

object: "group.deleted"

Always `group.deleted`.

### Delete group

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:groups delete \
  --admin-api-key 'My Admin API Key' \
  --group-id group_id

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true

##### Returns Examples

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true
