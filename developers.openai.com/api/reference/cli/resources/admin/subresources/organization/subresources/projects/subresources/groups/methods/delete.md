<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Remove project group

$ openai admin:organization:projects:groups delete

DELETE/organization/projects/{project\_id}/groups/{group\_id}

Revokes a group’s access to a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to update.

--group-id: string

The ID of the group to remove from the project.

##### ReturnsExpand Collapse

AdminOrganizationProjectGroupDeleteResponse: object { deleted, object }

Confirmation payload returned after removing a group from a project.

deleted: boolean

Whether the group membership in the project was removed.

object: "project.group.deleted"

Always `project.group.deleted`.

### Remove project group

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:groups delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --group-id group_id

    "object": "project.group.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.group.deleted",
    "deleted": true
