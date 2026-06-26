<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/rate_limits/methods/list_rate_limits/ -->

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

# List project rate limits

RateLimitListRateLimitsPage admin().organization().projects().rateLimits().listRateLimits(RateLimitListRateLimitsParamsparams = RateLimitListRateLimitsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/rate\_limits

Returns the rate limits per model for a project.

##### ParametersExpand Collapse

RateLimitListRateLimitsParams params

Optional<String> projectId

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<String> before

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, beginning with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. The default is 100.

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

### List project rate limits

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
import com.openai.models.admin.organization.projects.ratelimits.RateLimitListRateLimitsPage;
import com.openai.models.admin.organization.projects.ratelimits.RateLimitListRateLimitsParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RateLimitListRateLimitsPage page = client.admin().organization().projects().rateLimits().listRateLimits("project_id");

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
