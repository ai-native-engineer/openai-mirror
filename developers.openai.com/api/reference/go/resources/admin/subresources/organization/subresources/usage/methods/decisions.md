<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/decisions/ -->

## Decisions

`client.Admin.Organization.Usage.Decisions(ctx, query) (*AdminOrganizationUsageDecisionsResponse, error)`

**get** `/organization/usage/decisions`

Get Decisions API usage details for the organization.

- `query AdminOrganizationUsageDecisionsParams`

  - `StartTime param.Field[int64]`

    Start time (Unix seconds) of the query time range, inclusive.

  - `APIKeyIDs param.Field[[]string]`

    Return only usage for these API keys.

  - `Batch param.Field[bool]`

    If `true`, return batch jobs only. If `false`, return non-batch jobs only. By default, return both.

  - `BucketWidth param.Field[AdminOrganizationUsageDecisionsParamsBucketWidth]`

    Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

    - `const AdminOrganizationUsageDecisionsParamsBucketWidth1m AdminOrganizationUsageDecisionsParamsBucketWidth = "1m"`

    - `const AdminOrganizationUsageDecisionsParamsBucketWidth1h AdminOrganizationUsageDecisionsParamsBucketWidth = "1h"`

    - `const AdminOrganizationUsageDecisionsParamsBucketWidth1d AdminOrganizationUsageDecisionsParamsBucketWidth = "1d"`

  - `EndTime param.Field[int64]`

    End time (Unix seconds) of the query time range, exclusive.

  - `GroupBy param.Field[[]string]`

    Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `batch`, `service_tier`, `api_source` or any combination of them. When grouped by `api_source`, results use `agents_api` for attributed Agents API activity and `unlabeled` for all other activity. Without source grouping, `api_source` is null.

    - `const AdminOrganizationUsageDecisionsParamsGroupByProjectID AdminOrganizationUsageDecisionsParamsGroupBy = "project_id"`

    - `const AdminOrganizationUsageDecisionsParamsGroupByUserID AdminOrganizationUsageDecisionsParamsGroupBy = "user_id"`

    - `const AdminOrganizationUsageDecisionsParamsGroupByAPIKeyID AdminOrganizationUsageDecisionsParamsGroupBy = "api_key_id"`

    - `const AdminOrganizationUsageDecisionsParamsGroupByModel AdminOrganizationUsageDecisionsParamsGroupBy = "model"`

    - `const AdminOrganizationUsageDecisionsParamsGroupByBatch AdminOrganizationUsageDecisionsParamsGroupBy = "batch"`

    - `const AdminOrganizationUsageDecisionsParamsGroupByServiceTier AdminOrganizationUsageDecisionsParamsGroupBy = "service_tier"`

    - `const AdminOrganizationUsageDecisionsParamsGroupByAPISource AdminOrganizationUsageDecisionsParamsGroupBy = "api_source"`

  - `Limit param.Field[int64]`

    Specifies the number of buckets to return.

    - `bucket_width=1d`: default: 7, max: 31
    - `bucket_width=1h`: default: 24, max: 168
    - `bucket_width=1m`: default: 60, max: 1440

  - `Models param.Field[[]string]`

    Return only usage for these models.

  - `Page param.Field[string]`

    A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

  - `ProjectIDs param.Field[[]string]`

    Return only usage for these projects.

  - `UserIDs param.Field[[]string]`

    Return only usage for these users.

- `type AdminOrganizationUsageDecisionsResponse struct{…}`

  - `Data []AdminOrganizationUsageDecisionsResponseData`

    - `EndTime int64`

    - `Object Bucket`

      - `const BucketBucket Bucket = "bucket"`

    - `Results []AdminOrganizationUsageDecisionsResponseDataResult`

      - `InputTokens int64`

        The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `NumModelRequests int64`

        The count of requests made to the model.

      - `Object OrganizationUsageDecisionsResult`

        - `const OrganizationUsageDecisionsResultOrganizationUsageDecisionsResult OrganizationUsageDecisionsResult = "organization.usage.decisions.result"`

      - `OutputTokens int64`

        The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `APIKeyID string`

        When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

      - `APISource string`

        When grouped by `api_source`, `agents_api` identifies attributed Agents API activity and `unlabeled` includes all records without published source attribution, including historical and unknown origins. Unlabeled does not imply direct API usage. Without source grouping, this field is null.

        - `const AdminOrganizationUsageDecisionsResponseDataResultAPISourceAgentsAPI AdminOrganizationUsageDecisionsResponseDataResultAPISource = "agents_api"`

        - `const AdminOrganizationUsageDecisionsResponseDataResultAPISourceUnlabeled AdminOrganizationUsageDecisionsResponseDataResultAPISource = "unlabeled"`

      - `Batch bool`

        When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

      - `InputAudioTokens int64`

        The aggregated number of uncached audio input tokens used.

      - `InputCacheWrite12hTokens int64`

        The aggregated number of input tokens written to the cache with a 12-hour retention period.

      - `InputCacheWrite30mTokens int64`

        The aggregated number of input tokens written to the cache with a 30-minute retention period.

      - `InputCacheWriteTokens int64`

        The aggregated number of input tokens written to the cache across 30-minute and 12-hour retention periods.

      - `InputCachedAudioTokens int64`

        The aggregated number of cached audio input tokens used.

      - `InputCachedImageTokens int64`

        The aggregated number of cached image input tokens used.

      - `InputCachedTextTokens int64`

        The aggregated number of cached text input tokens used.

      - `InputCachedTokens int64`

        The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `InputImageTokens int64`

        The aggregated number of uncached image input tokens used.

      - `InputTextTokens int64`

        The aggregated number of uncached text input tokens used, excluding cache-write tokens.

      - `InputUncachedTokens int64`

        The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

      - `Model string`

        When `group_by=model`, this field provides the model name of the grouped usage result.

      - `OutputAudioTokens int64`

        The aggregated number of audio output tokens used.

      - `OutputImageTokens int64`

        The aggregated number of image output tokens used.

      - `OutputTextTokens int64`

        The aggregated number of text output tokens used.

      - `ProjectID string`

        When `group_by=project_id`, this field provides the project ID of the grouped usage result.

      - `ServiceTier string`

        When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

      - `UserID string`

        When `group_by=user_id`, this field provides the user ID of the grouped usage result.

    - `StartTime int64`

  - `HasMore bool`

  - `NextPage string`

  - `Object Page`

    - `const PagePage Page = "page"`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  response, err := client.Admin.Organization.Usage.Decisions(context.TODO(), openai.AdminOrganizationUsageDecisionsParams{
    StartTime: 0,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response.Data)

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
