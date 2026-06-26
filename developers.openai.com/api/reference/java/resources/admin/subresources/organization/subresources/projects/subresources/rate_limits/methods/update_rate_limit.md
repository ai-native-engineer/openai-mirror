<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/update_rate_limit/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Rate Limits](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project rate limit

[ProjectRateLimit](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.rate_limits%20%3E%20(model)%20project_rate_limit%20%3E%20(schema)) admin().organization().projects().rateLimits().updateRateLimit(RateLimitUpdateRateLimitParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/rate\_limits/{rate\_limit\_id}

Updates a project rate limit.

##### ParametersExpand Collapse

RateLimitUpdateRateLimitParams params

String projectId

Optional<String> rateLimitId

Optional<Long> batch1DayMaxInputTokens

The maximum batch input tokens per day. Only relevant for certain models.

Optional<Long> maxAudioMegabytesPer1Minute

The maximum audio megabytes per minute. Only relevant for certain models.

Optional<Long> maxImagesPer1Minute

The maximum images per minute. Only relevant for certain models.

Optional<Long> maxRequestsPer1Day

The maximum requests per day. Only relevant for certain models.

Optional<Long> maxRequestsPer1Minute

The maximum requests per minute.

Optional<Long> maxTokensPer1Minute

The maximum tokens per minute.

##### ReturnsExpand Collapse

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

### Modify project rate limit

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.ratelimits.ProjectRateLimit;
import com.openai.models.admin.organization.projects.ratelimits.RateLimitUpdateRateLimitParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RateLimitUpdateRateLimitParams params = RateLimitUpdateRateLimitParams.builder()
            .projectId("project_id")
            .rateLimitId("rate_limit_id")
            .build();
        ProjectRateLimit projectRateLimit = client.admin().organization().projects().rateLimits().updateRateLimit(params);

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
