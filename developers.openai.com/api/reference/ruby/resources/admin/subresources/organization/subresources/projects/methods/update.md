<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project

admin.organization.projects.update(project\_id, \*\*kwargs) -> [Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects/{project\_id}

Modifies a project in the organization.

##### ParametersExpand Collapse

project\_id: String

external\_key\_id: String

External key ID to associate with the project.

geography: String

Geography for the project.

name: String

The updated name of the project, this name appears in reports.

##### ReturnsExpand Collapse

class Project { id, created\_at, object, 4 more }

Represents an individual project.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: :"organization.project"

The object type, which is always `organization.project`

archived\_at: Integer

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id: String

The external key associated with the project.

name: String

The name of the project. This appears in reporting.

status: String

`active` or `archived`

### Modify project

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

project = openai.admin.organization.projects.update("project_id")

puts(project)

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "object": "organization.project",
  "archived_at": 0,
  "external_key_id": "external_key_id",
  "name": "name",
  "status": "status"
