<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/groups/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Groups](/api/reference/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete group

DELETE/organization/groups/{group\_id}

Deletes a group from the organization.

##### Path ParametersExpand Collapse

group\_id: string

##### ReturnsExpand Collapse

id: string

Identifier of the deleted group.

deleted: boolean

Whether the group was deleted.

object: "group.deleted"

Always `group.deleted`.

### Delete group

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/groups/group_01J1F8ABCDXYZ \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true

##### Returns Examples

    "object": "group.deleted",
    "id": "group_01J1F8ABCDXYZ",
    "deleted": true
