<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/methods/list/ -->

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

# List projects

admin.organization.projects.list(\*\*kwargs) -> ConversationCursorPage<[Project](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects%20%3E%20(model)%20project%20%3E%20(schema)) { id, created\_at, object, 4 more } >

GET/organization/projects

Returns a list of projects.

##### ParametersExpand Collapse

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

include\_archived: bool

If `true` returns all projects including those that have been `archived`. Archived projects are not included by default.

limit: Integer

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List projects

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

page = openai.admin.organization.projects.list

puts(page)

    "object": "list",
    "data": [
            "id": "proj_abc",
            "object": "organization.project",
            "name": "Project example",
            "created_at": 1711471533,
            "archived_at": null,
            "status": "active"
    ],
    "first_id": "proj-abc",
    "last_id": "proj-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "id": "proj_abc",
            "object": "organization.project",
            "name": "Project example",
            "created_at": 1711471533,
            "archived_at": null,
            "status": "active"
    ],
    "first_id": "proj-abc",
    "last_id": "proj-xyz",
    "has_more": false
