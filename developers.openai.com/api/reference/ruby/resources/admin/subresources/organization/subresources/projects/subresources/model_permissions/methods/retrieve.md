<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Model Permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project model permissions

admin.organization.projects.model\_permissions.retrieve(project\_id) -> [ProjectModelPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

GET/organization/projects/{project\_id}/model\_permissions

Returns model permissions for a project.

##### ParametersExpand Collapse

project\_id: String

##### ReturnsExpand Collapse

class ProjectModelPermissions { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: :allow\_list | :deny\_list

Whether the project uses an allowlist or a denylist.

One of the following:

:allow\_list

:deny\_list

model\_ids: Array[String]

The model IDs included in the model permissions policy.

object: :"project.model\_permissions"

The object type, which is always `project.model_permissions`.

### Retrieve project model permissions

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_model_permissions = openai.admin.organization.projects.model_permissions.retrieve("project_id")

puts(project_model_permissions)

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]

##### Returns Examples

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]
