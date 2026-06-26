<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Rate Limits

##### [List project rate limits](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits)

RateLimitListRateLimitsPage admin().organization().projects().rateLimits().listRateLimits(RateLimitListRateLimitsParamsparams = RateLimitListRateLimitsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/rate\_limits

##### [Modify project rate limit](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit)

[ProjectRateLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) admin().organization().projects().rateLimits().updateRateLimit(RateLimitUpdateRateLimitParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

##### ModelsExpand Collapse

class ProjectRateLimit:

Represents a project rate limit config.

String id

The identifier, which can be referenced in API endpoints.

long maxRequestsPer1Minute

The maximum requests per minute.

long maxTokensPer1Minute

The maximum tokens per minute.

String model

The model this rate limit applies to.

JsonValue; object\_ "project.rate\_limit"constant"project.rate\_limit"constant

The object type, which is always `project.rate_limit`

Optional<Long> batch1DayMaxInputTokens

The maximum batch input tokens per day. Only present for relevant models.

Optional<Long> maxAudioMegabytesPer1Minute

The maximum audio megabytes per minute. Only present for relevant models.

Optional<Long> maxImagesPer1Minute

The maximum images per minute. Only present for relevant models.

Optional<Long> maxRequestsPer1Day

The maximum requests per day. Only present for relevant models.
