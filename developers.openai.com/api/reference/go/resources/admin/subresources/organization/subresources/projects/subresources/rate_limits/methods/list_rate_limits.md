<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits/ -->

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

# List project rate limits

client.Admin.Organization.Projects.RateLimits.ListRateLimits(ctx, projectID, query) (\*ConversationCursorPage[[ProjectRateLimit](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/rate\_limits

Returns the rate limits per model for a project.

##### ParametersExpand Collapse

projectID string

query AdminOrganizationProjectRateLimitListRateLimitsParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Before param.Field[string]Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, beginning with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. The default is 100.

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

### List project rate limits

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
  page, err := client.Admin.Organization.Projects.RateLimits.ListRateLimits(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectRateLimitListRateLimitsParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
