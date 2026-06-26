<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Model Permissions](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project model permissions

$ openai admin:organization:projects:model-permissions delete

DELETE/organization/projects/{project\_id}/model\_permissions

Deletes model permissions for a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

##### ReturnsExpand Collapse

project\_model\_permissions\_deleted: object { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: boolean

Whether the project model permissions were deleted.

object: "project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.

### Delete project model permissions

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:model-permissions delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id

    "object": "project.model_permissions.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.model_permissions.deleted",
    "deleted": true
