<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project

POST/organization/projects/{project\_id}

Modifies a project in the organization.

##### Path ParametersExpand Collapse

project\_id: string

##### Body ParametersJSONExpand Collapse

external\_key\_id: optional string

External key ID to associate with the project.

geography: optional string

Geography for the project.

name: optional string

The updated name of the project, this name appears in reports.

##### ReturnsExpand Collapse

Project object { id, created\_at, object, 4 more }

Represents an individual project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the project was created.

formatunixtime

object: "organization.project"

The object type, which is always `organization.project`

archived\_at: optional number

The Unix timestamp (in seconds) of when the project was archived or `null`.

formatunixtime

external\_key\_id: optional string

The external key associated with the project.

name: optional string

The name of the project. This appears in reporting.

status: optional string

`active` or `archived`

### Modify project

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/organization/projects/proj_abc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "name": "Project DEF"
  }'

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
