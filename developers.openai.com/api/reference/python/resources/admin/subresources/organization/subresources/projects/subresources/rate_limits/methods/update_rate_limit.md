<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit/ -->

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

# Modify project rate limit

admin.organization.projects.rate\_limits.update\_rate\_limit(strrate\_limit\_id, RateLimitUpdateRateLimitParams\*\*kwargs)  -> [ProjectRateLimit](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

Updates a project rate limit.

##### ParametersExpand Collapse

project\_id: str

rate\_limit\_id: str

batch\_1\_day\_max\_input\_tokens: Optional[int]

The maximum batch input tokens per day. Only relevant for certain models.

max\_audio\_megabytes\_per\_1\_minute: Optional[int]

The maximum audio megabytes per minute. Only relevant for certain models.

max\_images\_per\_1\_minute: Optional[int]

The maximum images per minute. Only relevant for certain models.

max\_requests\_per\_1\_day: Optional[int]

The maximum requests per day. Only relevant for certain models.

max\_requests\_per\_1\_minute: Optional[int]

The maximum requests per minute.

max\_tokens\_per\_1\_minute: Optional[int]

The maximum tokens per minute.

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

### Modify project rate limit

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
project_rate_limit = client.admin.organization.projects.rate_limits.update_rate_limit(
    rate_limit_id="rate_limit_id",
    project_id="project_id",
print(project_rate_limit.id)

    "object": "project.rate_limit",
    "id": "rl-ada",
    "model": "ada",
    "max_requests_per_1_minute": 600,
    "max_tokens_per_1_minute": 150000,
    "max_images_per_1_minute": 10

##### Returns Examples

    "object": "project.rate_limit",
    "id": "rl-ada",
    "model": "ada",
    "max_requests_per_1_minute": 600,
    "max_tokens_per_1_minute": 150000,
    "max_images_per_1_minute": 10
