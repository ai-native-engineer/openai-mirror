<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Rate Limits](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project rate limit

$ openai admin:organization:projects:rate-limits update-rate-limit

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

Updates a project rate limit.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--rate-limit-id: string

The ID of the rate limit.

--batch-1-day-max-input-tokens: optional number

The maximum batch input tokens per day. Only relevant for certain models.

--max-audio-megabytes-per-1-minute: optional number

The maximum audio megabytes per minute. Only relevant for certain models.

--max-images-per-1-minute: optional number

The maximum images per minute. Only relevant for certain models.

--max-requests-per-1-day: optional number

The maximum requests per day. Only relevant for certain models.

--max-requests-per-1-minute: optional number

The maximum requests per minute.

--max-tokens-per-1-minute: optional number

The maximum tokens per minute.

##### ReturnsExpand Collapse

project\_rate\_limit: object { id, max\_requests\_per\_1\_minute, max\_tokens\_per\_1\_minute, 6 more }

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

batch\_1\_day\_max\_input\_tokens: optional number

The maximum batch input tokens per day. Only present for relevant models.

max\_audio\_megabytes\_per\_1\_minute: optional number

The maximum audio megabytes per minute. Only present for relevant models.

max\_images\_per\_1\_minute: optional number

The maximum images per minute. Only present for relevant models.

max\_requests\_per\_1\_day: optional number

The maximum requests per day. Only present for relevant models.

### Modify project rate limit

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:rate-limits update-rate-limit \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --rate-limit-id rate_limit_id

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
