<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Rate Limits](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project rate limit

client.Admin.Organization.Projects.RateLimits.UpdateRateLimit(ctx, projectID, rateLimitID, body) (\*[ProjectRateLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

Updates a project rate limit.

##### ParametersExpand Collapse

projectID string

rateLimitID string

body AdminOrganizationProjectRateLimitUpdateRateLimitParams

Batch1DayMaxInputTokens param.Field[int64]Optional

The maximum batch input tokens per day. Only relevant for certain models.

MaxAudioMegabytesPer1Minute param.Field[int64]Optional

The maximum audio megabytes per minute. Only relevant for certain models.

MaxImagesPer1Minute param.Field[int64]Optional

The maximum images per minute. Only relevant for certain models.

MaxRequestsPer1Day param.Field[int64]Optional

The maximum requests per day. Only relevant for certain models.

MaxRequestsPer1Minute param.Field[int64]Optional

The maximum requests per minute.

MaxTokensPer1Minute param.Field[int64]Optional

The maximum tokens per minute.

##### ReturnsExpand Collapse

type ProjectRateLimit struct{…}

Represents a project rate limit config.

ID string

The identifier, which can be referenced in API endpoints.

MaxRequestsPer1Minute int64

The maximum requests per minute.

MaxTokensPer1Minute int64

The maximum tokens per minute.

Model string

The model this rate limit applies to.

Object ProjectRateLimit

The object type, which is always `project.rate_limit`

Batch1DayMaxInputTokens int64Optional

The maximum batch input tokens per day. Only present for relevant models.

MaxAudioMegabytesPer1Minute int64Optional

The maximum audio megabytes per minute. Only present for relevant models.

MaxImagesPer1Minute int64Optional

The maximum images per minute. Only present for relevant models.

MaxRequestsPer1Day int64Optional

The maximum requests per day. Only present for relevant models.

### Modify project rate limit

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  projectRateLimit, err := client.Admin.Organization.Projects.RateLimits.UpdateRateLimit(
    context.TODO(),
    "project_id",
    "rate_limit_id",
    openai.AdminOrganizationProjectRateLimitUpdateRateLimitParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectRateLimit.ID)

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
