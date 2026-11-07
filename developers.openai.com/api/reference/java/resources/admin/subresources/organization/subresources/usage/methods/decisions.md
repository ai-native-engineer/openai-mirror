<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/decisions/ -->

## Decisions

`UsageDecisionsResponse admin().organization().usage().decisions(UsageDecisionsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/usage/decisions`

Get Decisions API usage details for the organization.

- `UsageDecisionsParams params`

  - `long startTime`

    Start time (Unix seconds) of the query time range, inclusive.

  - `Optional<List<String>> apiKeyIds`

    Return only usage for these API keys.

  - `Optional<Boolean> batch`

    If `true`, return batch jobs only. If `false`, return non-batch jobs only. By default, return both.

  - `Optional<BucketWidth> bucketWidth`

    Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

    - `_1M("1m")`

    - `_1H("1h")`

    - `_1D("1d")`

  - `Optional<Long> endTime`

    End time (Unix seconds) of the query time range, exclusive.

  - `Optional<List<GroupBy>> groupBy`

    Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `batch`, `service_tier`, `api_source` or any combination of them. When grouped by `api_source`, results use `agents_api` for attributed Agents API activity and `unlabeled` for all other activity. Without source grouping, `api_source` is null.

    - `PROJECT_ID("project_id")`

    - `USER_ID("user_id")`

    - `API_KEY_ID("api_key_id")`

    - `MODEL("model")`

    - `BATCH("batch")`

    - `SERVICE_TIER("service_tier")`

    - `API_SOURCE("api_source")`

  - `Optional<Long> limit`

    Specifies the number of buckets to return.

    - `bucket_width=1d`: default: 7, max: 31
    - `bucket_width=1h`: default: 24, max: 168
    - `bucket_width=1m`: default: 60, max: 1440

  - `Optional<List<String>> models`

    Return only usage for these models.

  - `Optional<String> page`

    A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

  - `Optional<List<String>> projectIds`

    Return only usage for these projects.

  - `Optional<List<String>> userIds`

    Return only usage for these users.

- `class UsageDecisionsResponse:`

  - `List<Data> data`

    - `long endTime`

    - `JsonValue; object_ "bucket"constant`

      - `BUCKET("bucket")`

    - `List<Result> results`

      - `long inputTokens`

        The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `long numModelRequests`

        The count of requests made to the model.

      - `JsonValue; object_ "organization.usage.decisions.result"constant`

        - `ORGANIZATION_USAGE_DECISIONS_RESULT("organization.usage.decisions.result")`

      - `long outputTokens`

        The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `Optional<String> apiKeyId`

        When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

      - `Optional<ApiSource> apiSource`

        When grouped by `api_source`, `agents_api` identifies attributed Agents API activity and `unlabeled` includes all records without published source attribution, including historical and unknown origins. Unlabeled does not imply direct API usage. Without source grouping, this field is null.

        - `AGENTS_API("agents_api")`

        - `UNLABELED("unlabeled")`

      - `Optional<Boolean> batch`

        When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

      - `Optional<Long> inputAudioTokens`

        The aggregated number of uncached audio input tokens used.

      - `Optional<Long> inputCacheWrite12hTokens`

        The aggregated number of input tokens written to the cache with a 12-hour retention period.

      - `Optional<Long> inputCacheWrite30mTokens`

        The aggregated number of input tokens written to the cache with a 30-minute retention period.

      - `Optional<Long> inputCacheWriteTokens`

        The aggregated number of input tokens written to the cache across 30-minute and 12-hour retention periods.

      - `Optional<Long> inputCachedAudioTokens`

        The aggregated number of cached audio input tokens used.

      - `Optional<Long> inputCachedImageTokens`

        The aggregated number of cached image input tokens used.

      - `Optional<Long> inputCachedTextTokens`

        The aggregated number of cached text input tokens used.

      - `Optional<Long> inputCachedTokens`

        The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `Optional<Long> inputImageTokens`

        The aggregated number of uncached image input tokens used.

      - `Optional<Long> inputTextTokens`

        The aggregated number of uncached text input tokens used, excluding cache-write tokens.

      - `Optional<Long> inputUncachedTokens`

        The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

      - `Optional<String> model`

        When `group_by=model`, this field provides the model name of the grouped usage result.

      - `Optional<Long> outputAudioTokens`

        The aggregated number of audio output tokens used.

      - `Optional<Long> outputImageTokens`

        The aggregated number of image output tokens used.

      - `Optional<Long> outputTextTokens`

        The aggregated number of text output tokens used.

      - `Optional<String> projectId`

        When `group_by=project_id`, this field provides the project ID of the grouped usage result.

      - `Optional<String> serviceTier`

        When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

      - `Optional<String> userId`

        When `group_by=user_id`, this field provides the user ID of the grouped usage result.

    - `long startTime`

  - `boolean hasMore`

  - `Optional<String> nextPage`

  - `JsonValue; object_ "page"constant`

    - `PAGE("page")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.usage.UsageDecisionsParams;
import com.openai.models.admin.organization.usage.UsageDecisionsResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UsageDecisionsParams params = UsageDecisionsParams.builder()
            .startTime(0L)
            .build();
        UsageDecisionsResponse response = client.admin().organization().usage().decisions(params);

  "data": [
      "end_time": 0,
      "object": "bucket",
      "results": [
          "input_tokens": 0,
          "num_model_requests": 0,
          "object": "organization.usage.decisions.result",
          "output_tokens": 0,
          "api_key_id": "api_key_id",
          "api_source": "agents_api",
          "batch": true,
          "input_audio_tokens": 0,
          "input_cache_write_12h_tokens": 0,
          "input_cache_write_30m_tokens": 0,
          "input_cache_write_tokens": 0,
          "input_cached_audio_tokens": 0,
          "input_cached_image_tokens": 0,
          "input_cached_text_tokens": 0,
          "input_cached_tokens": 0,
          "input_image_tokens": 0,
          "input_text_tokens": 0,
          "input_uncached_tokens": 0,
          "model": "model",
          "output_audio_tokens": 0,
          "output_image_tokens": 0,
          "output_text_tokens": 0,
          "project_id": "project_id",
          "service_tier": "service_tier",
          "user_id": "user_id"
      "start_time": 0
  "has_more": true,
  "next_page": "next_page",
  "object": "page"
