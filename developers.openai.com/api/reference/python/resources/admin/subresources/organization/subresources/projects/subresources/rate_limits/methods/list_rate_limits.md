<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Rate Limits](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project rate limits

admin.organization.projects.rate\_limits.list\_rate\_limits(strproject\_id, RateLimitListRateLimitsParams\*\*kwargs)  -> SyncConversationCursorPage[[ProjectRateLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))]

GET/organization/projects/{project\_id}/rate\_limits

Returns the rate limits per model for a project.

##### ParametersExpand Collapse

project\_id: str

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

before: Optional[str]

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, beginning with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

limit: Optional[int]

A limit on the number of objects to be returned. The default is 100.

##### ReturnsExpand Collapse

class ProjectRateLimit: …

Represents a project rate limit config.

id: str

The identifier, which can be referenced in API endpoints.

max\_requests\_per\_1\_minute: int

The maximum requests per minute.

max\_tokens\_per\_1\_minute: int

The maximum tokens per minute.

model: str

The model this rate limit applies to.

object: Literal["project.rate\_limit"]

The object type, which is always `project.rate_limit`

batch\_1\_day\_max\_input\_tokens: Optional[int]

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute: Optional[int]

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute: Optional[int]

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day: Optional[int]

The maximum requests per day. Only present for relevant models.

### List project rate limits

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
page = client.admin.organization.projects.rate_limits.list_rate_limits(
    project_id="project_id",
page = page.data[0]
print(page.id)

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
