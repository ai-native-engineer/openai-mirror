<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project API key

admin.organization.projects.api\_keys.delete(api\_key\_id, \*\*kwargs) -> [APIKeyDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Deletes an API key from the project.

Returns confirmation of the key deletion, or an error if the key belonged to
a service account.

##### ParametersExpand Collapse

project\_id: String

api\_key\_id: String

##### ReturnsExpand Collapse

class APIKeyDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.project.api\_key.deleted"

### Delete project API key

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

api_key = openai.admin.organization.projects.api_keys.delete("api_key_id", project_id: "project_id")

puts(api_key)

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true
