<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete/ -->

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

# Delete project model permissions

admin.organization.projects.model\_permissions.delete(project\_id) -> [ProjectModelPermissionsDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/model\_permissions

Deletes model permissions for a project.

##### ParametersExpand Collapse

project\_id: String

##### ReturnsExpand Collapse

class ProjectModelPermissionsDeleted { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: bool

Whether the project model permissions were deleted.

object: :"project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.

### Delete project model permissions

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

project_model_permissions_deleted = openai.admin.organization.projects.model_permissions.delete("project_id")

puts(project_model_permissions_deleted)

    "object": "project.model_permissions.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.model_permissions.deleted",
    "deleted": true
