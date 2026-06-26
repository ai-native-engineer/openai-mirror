<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/archive/ -->

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

# Archive project

admin.organization.projects.archive(project\_id) -> [Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more }

POST/organization/projects/{project\_id}/archive

Archives a project in the organization. Archived projects cannot be used or updated.

##### ParametersExpand Collapse

project\_id: String

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

### Archive project

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

project = openai.admin.organization.projects.archive("project_id")

puts(project)

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project DEF",
    "created_at": 1711471533,
    "archived_at": 1711471533,
    "status": "archived"

##### Returns Examples

    "id": "proj_abc",
    "object": "organization.project",
    "name": "Project DEF",
    "created_at": 1711471533,
    "archived_at": 1711471533,
    "status": "archived"
