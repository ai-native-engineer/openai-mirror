<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Rate Limits](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project rate limits

admin.organization.projects.rate\_limits.list\_rate\_limits(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectRateLimit](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more } >

GET/organization/projects/{project\_id}/rate\_limits

Returns the rate limits per model for a project.

##### ParametersExpand Collapse

project\_id: String

after: String

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before: String

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, beginning with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

limit: Integer

A limit on the number of objects to be returned. The default is 100.

##### ReturnsExpand Collapse

class ProjectRateLimit { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

Represents a project rate limit config.

id: String

The identifier, which can be referenced in API endpoints.

max\_requests\_per\_1\_minute: Integer

The maximum requests per minute.

max\_tokens\_per\_1\_minute: Integer

The maximum tokens per minute.

model: String

The model this rate limit applies to.

object: :"project.rate\_limit"

The object type, which is always `project.rate_limit`

batch\_1\_day\_max\_input\_tokens: Integer

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute: Integer

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute: Integer

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day: Integer

The maximum requests per day. Only present for relevant models.

### List project rate limits

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

page = openai.admin.organization.projects.rate_limits.list_rate_limits("project_id")

puts(page)

    "object": "list",
    "data": [
          "object": "project.rate_limit",
          "id": "rl-ada",
          "model": "ada",
          "max_requests_per_1_minute": 600,
          "max_tokens_per_1_minute": 150000,
          "max_images_per_1_minute": 10
    ],
    "first_id": "rl-ada",
    "last_id": "rl-ada",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
          "object": "project.rate_limit",
          "id": "rl-ada",
          "model": "ada",
          "max_requests_per_1_minute": 600,
          "max_tokens_per_1_minute": 150000,
          "max_images_per_1_minute": 10
    ],
    "first_id": "rl-ada",
    "last_id": "rl-ada",
    "has_more": false
