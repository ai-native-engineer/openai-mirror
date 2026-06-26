<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Data Retention](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project data retention

admin.organization.projects.data\_retention.retrieve(project\_id) -> [ProjectDataRetention](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

GET/organization/projects/{project\_id}/data\_retention

Retrieves project data retention controls.

##### ParametersExpand Collapse

project\_id: String

##### ReturnsExpand Collapse

class ProjectDataRetention { object, type }

Represents a project’s data retention control setting.

object: :"project.data\_retention"

The object type, which is always `project.data_retention`.

type: :organization\_default | :none | :zero\_data\_retention | 3 more

The configured project data retention type.

One of the following:

:organization\_default

:none

:zero\_data\_retention

:modified\_abuse\_monitoring

:enhanced\_zero\_data\_retention

:enhanced\_modified\_abuse\_monitoring

### Retrieve project data retention

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

project_data_retention = openai.admin.organization.projects.data_retention.retrieve("project_id")

puts(project_data_retention)

    "object": "project.data_retention",
    "type": "organization_default"

##### Returns Examples

    "object": "project.data_retention",
    "type": "organization_default"
