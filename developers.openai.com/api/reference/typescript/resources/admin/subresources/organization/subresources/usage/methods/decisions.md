<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/decisions/ -->

## Decisions

`client.admin.organization.usage.decisions(UsageDecisionsParamsquery, RequestOptionsoptions?): UsageDecisionsResponse`

**get** `/organization/usage/decisions`

Get Decisions API usage details for the organization.

- `query: UsageDecisionsParams`

  - `start_time: number`

    Start time (Unix seconds) of the query time range, inclusive.

  - `api_key_ids?: Array<string> | null`

    Return only usage for these API keys.

  - `batch?: boolean | null`

    If `true`, return batch jobs only. If `false`, return non-batch jobs only. By default, return both.

  - `bucket_width?: "1m" | "1h" | "1d" | null`

    Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

    - `"1m"`

    - `"1h"`

    - `"1d"`

  - `end_time?: number | null`

    End time (Unix seconds) of the query time range, exclusive.

  - `group_by?: Array<"project_id" | "user_id" | "api_key_id" | 4 more> | null`

    Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `batch`, `service_tier`, `api_source` or any combination of them. When grouped by `api_source`, results use `agents_api` for attributed Agents API activity and `unlabeled` for all other activity. Without source grouping, `api_source` is null.

    - `"project_id"`

    - `"user_id"`

    - `"api_key_id"`

    - `"model"`

    - `"batch"`

    - `"service_tier"`

    - `"api_source"`

  - `limit?: number | null`

    Specifies the number of buckets to return.

    - `bucket_width=1d`: default: 7, max: 31
    - `bucket_width=1h`: default: 24, max: 168
    - `bucket_width=1m`: default: 60, max: 1440

  - `models?: Array<string> | null`

    Return only usage for these models.

  - `page?: string | null`

    A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

  - `project_ids?: Array<string> | null`

    Return only usage for these projects.

  - `user_ids?: Array<string> | null`

    Return only usage for these users.

- `UsageDecisionsResponse`

  - `data: Array<Data>`

    - `end_time: number`

    - `object: "bucket"`

      - `"bucket"`

    - `results: Array<Result>`

      - `input_tokens: number`

        The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `num_model_requests: number`

        The count of requests made to the model.

      - `object: "organization.usage.decisions.result"`

        - `"organization.usage.decisions.result"`

      - `output_tokens: number`

        The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `api_key_id?: string | null`

        When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

      - `api_source?: "agents_api" | "unlabeled" | null`

        When grouped by `api_source`, `agents_api` identifies attributed Agents API activity and `unlabeled` includes all records without published source attribution, including historical and unknown origins. Unlabeled does not imply direct API usage. Without source grouping, this field is null.

        - `"agents_api"`

        - `"unlabeled"`

      - `batch?: boolean | null`

        When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

      - `input_audio_tokens?: number | null`

        The aggregated number of uncached audio input tokens used.

      - `input_cache_write_12h_tokens?: number | null`

        The aggregated number of input tokens written to the cache with a 12-hour retention period.

      - `input_cache_write_30m_tokens?: number | null`

        The aggregated number of input tokens written to the cache with a 30-minute retention period.

      - `input_cache_write_tokens?: number | null`

        The aggregated number of input tokens written to the cache across 30-minute and 12-hour retention periods.

      - `input_cached_audio_tokens?: number | null`

        The aggregated number of cached audio input tokens used.

      - `input_cached_image_tokens?: number | null`

        The aggregated number of cached image input tokens used.

      - `input_cached_text_tokens?: number | null`

        The aggregated number of cached text input tokens used.

      - `input_cached_tokens?: number | null`

        The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `input_image_tokens?: number | null`

        The aggregated number of uncached image input tokens used.

      - `input_text_tokens?: number | null`

        The aggregated number of uncached text input tokens used, excluding cache-write tokens.

      - `input_uncached_tokens?: number | null`

        The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

      - `model?: string | null`

        When `group_by=model`, this field provides the model name of the grouped usage result.

      - `output_audio_tokens?: number | null`

        The aggregated number of audio output tokens used.

      - `output_image_tokens?: number | null`

        The aggregated number of image output tokens used.

      - `output_text_tokens?: number | null`

        The aggregated number of text output tokens used.

      - `project_id?: string | null`

        When `group_by=project_id`, this field provides the project ID of the grouped usage result.

      - `service_tier?: string | null`

        When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

      - `user_id?: string | null`

        When `group_by=user_id`, this field provides the user ID of the grouped usage result.

    - `start_time: number`

  - `has_more: boolean`

  - `next_page: string | null`

  - `object: "page"`

    - `"page"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted
});

const response = await client.admin.organization.usage.decisions({ start_time: 0 });

console.log(response.data);

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
