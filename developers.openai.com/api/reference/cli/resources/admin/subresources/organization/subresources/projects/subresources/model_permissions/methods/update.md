<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update/ -->

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

# Modify project model permissions

$ openai admin:organization:projects:model-permissions update

POST/organization/projects/{project\_id}/model\_permissions

Updates model permissions for a project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--mode: "allow\_list" or "deny\_list"

The model permissions mode to apply.

--model-id: array of string

The model IDs included in this permissions policy.

##### ReturnsExpand Collapse

project\_model\_permissions: object { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: "allow\_list" or "deny\_list"

Whether the project uses an allowlist or a denylist.

"allow\_list"

"deny\_list"

model\_ids: array of string

The model IDs included in the model permissions policy.

object: "project.model\_permissions"

The object type, which is always `project.model_permissions`.

### Modify project model permissions

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:model-permissions update \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --mode allow_list \
  --model-id string

    "object": "project.model_permissions",
    "mode": "deny_list",
    "model_ids": [
        "o3"
    ]

##### Returns Examples

    "object": "project.model_permissions",
    "mode": "deny_list",
    "model_ids": [
        "o3"
    ]
