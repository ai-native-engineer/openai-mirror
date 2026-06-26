<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Rate Limits](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project rate limit

client.admin.organization.projects.rateLimits.updateRateLimit(stringrateLimitID, RateLimitUpdateRateLimitParams { project\_id, batch\_1\_day\_max\_input\_tokens, max\_audio\_megabytes\_per\_1\_minute, 4 more } params, RequestOptionsoptions?): [ProjectRateLimit](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

Updates a project rate limit.

##### ParametersExpand Collapse

rateLimitID: string

params: RateLimitUpdateRateLimitParams { project\_id, batch\_1\_day\_max\_input\_tokens, max\_audio\_megabytes\_per\_1\_minute, 4 more }

project\_id: string

Path param: The ID of the project.

batch\_1\_day\_max\_input\_tokens?: number

Body param: The maximum batch input tokens per day. Only relevant for certain models.

max\_audio\_megabytes\_per\_1\_minute?: number

Body param: The maximum audio megabytes per minute. Only relevant for certain models.

max\_images\_per\_1\_minute?: number

Body param: The maximum images per minute. Only relevant for certain models.

max\_requests\_per\_1\_day?: number

Body param: The maximum requests per day. Only relevant for certain models.

max\_requests\_per\_1\_minute?: number

Body param: The maximum requests per minute.

max\_tokens\_per\_1\_minute?: number

Body param: The maximum tokens per minute.

##### ReturnsExpand Collapse

ProjectRateLimit { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

Represents a project rate limit config.

id: string

The identifier, which can be referenced in API endpoints.

max\_requests\_per\_1\_minute: number

The maximum requests per minute.

max\_tokens\_per\_1\_minute: number

The maximum tokens per minute.

model: string

The model this rate limit applies to.

object: "project.rate\_limit"

The object type, which is always `project.rate_limit`

batch\_1\_day\_max\_input\_tokens?: number

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute?: number

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute?: number

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day?: number

The maximum requests per day. Only present for relevant models.

### Modify project rate limit

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const projectRateLimit = await client.admin.organization.projects.rateLimits.updateRateLimit(
  'rate_limit_id',
  { project_id: 'project_id' },
);

console.log(projectRateLimit.id);

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
