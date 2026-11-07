<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/decisions/ -->

## Decisions

`admin.organization.usage.decisions(UsageDecisionsParams**kwargs)  -> UsageDecisionsResponse`

**get** `/organization/usage/decisions`

Get Decisions API usage details for the organization.

- `start_time: int`

  Start time (Unix seconds) of the query time range, inclusive.

- `api_key_ids: Optional[Sequence[str]]`

  Return only usage for these API keys.

- `batch: Optional[bool]`

  If `true`, return batch jobs only. If `false`, return non-batch jobs only. By default, return both.

- `bucket_width: Optional[Literal["1m", "1h", "1d"]]`

  Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

  - `"1m"`

  - `"1h"`

  - `"1d"`

- `end_time: Optional[int]`

  End time (Unix seconds) of the query time range, exclusive.

- `group_by: Optional[List[Literal["project_id", "user_id", "api_key_id", 4 more]]]`

  Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `batch`, `service_tier`, `api_source` or any combination of them. When grouped by `api_source`, results use `agents_api` for attributed Agents API activity and `unlabeled` for all other activity. Without source grouping, `api_source` is null.

  - `"project_id"`

  - `"user_id"`

  - `"api_key_id"`

  - `"model"`

  - `"batch"`

  - `"service_tier"`

  - `"api_source"`

- `limit: Optional[int]`

  Specifies the number of buckets to return.

  - `bucket_width=1d`: default: 7, max: 31
  - `bucket_width=1h`: default: 24, max: 168
  - `bucket_width=1m`: default: 60, max: 1440

- `models: Optional[Sequence[str]]`

  Return only usage for these models.

- `page: Optional[str]`

  A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

- `project_ids: Optional[Sequence[str]]`

  Return only usage for these projects.

- `user_ids: Optional[Sequence[str]]`

  Return only usage for these users.

- `class UsageDecisionsResponse: …`

  - `data: List[Data]`

    - `end_time: int`

    - `object: Literal["bucket"]`

      - `"bucket"`

    - `results: List[DataResult]`

      - `input_tokens: int`

        The aggregated number of input tokens used, including cached and cache-write tokens. This includes text, audio, and image tokens. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `num_model_requests: int`

        The count of requests made to the model.

      - `object: Literal["organization.usage.decisions.result"]`

        - `"organization.usage.decisions.result"`

      - `output_tokens: int`

        The aggregated number of output tokens used across text, audio, and image outputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `api_key_id: Optional[str]`

        When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

      - `api_source: Optional[Literal["agents_api", "unlabeled"]]`

        When grouped by `api_source`, `agents_api` identifies attributed Agents API activity and `unlabeled` includes all records without published source attribution, including historical and unknown origins. Unlabeled does not imply direct API usage. Without source grouping, this field is null.

        - `"agents_api"`

        - `"unlabeled"`

      - `batch: Optional[bool]`

        When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

      - `input_audio_tokens: Optional[int]`

        The aggregated number of uncached audio input tokens used.

      - `input_cache_write_12h_tokens: Optional[int]`

        The aggregated number of input tokens written to the cache with a 12-hour retention period.

      - `input_cache_write_30m_tokens: Optional[int]`

        The aggregated number of input tokens written to the cache with a 30-minute retention period.

      - `input_cache_write_tokens: Optional[int]`

        The aggregated number of input tokens written to the cache across 30-minute and 12-hour retention periods.

      - `input_cached_audio_tokens: Optional[int]`

        The aggregated number of cached audio input tokens used.

      - `input_cached_image_tokens: Optional[int]`

        The aggregated number of cached image input tokens used.

      - `input_cached_text_tokens: Optional[int]`

        The aggregated number of cached text input tokens used.

      - `input_cached_tokens: Optional[int]`

        The aggregated number of cached input tokens used across text, audio, and image inputs. For customers subscribed to Scale Tier, this includes Scale Tier tokens.

      - `input_image_tokens: Optional[int]`

        The aggregated number of uncached image input tokens used.

      - `input_text_tokens: Optional[int]`

        The aggregated number of uncached text input tokens used, excluding cache-write tokens.

      - `input_uncached_tokens: Optional[int]`

        The aggregated number of uncached input tokens used across text, audio, and image inputs, excluding cache-write tokens.

      - `model: Optional[str]`

        When `group_by=model`, this field provides the model name of the grouped usage result.

      - `output_audio_tokens: Optional[int]`

        The aggregated number of audio output tokens used.

      - `output_image_tokens: Optional[int]`

        The aggregated number of image output tokens used.

      - `output_text_tokens: Optional[int]`

        The aggregated number of text output tokens used.

      - `project_id: Optional[str]`

        When `group_by=project_id`, this field provides the project ID of the grouped usage result.

      - `service_tier: Optional[str]`

        When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

      - `user_id: Optional[str]`

        When `group_by=user_id`, this field provides the user ID of the grouped usage result.

    - `start_time: int`

  - `has_more: bool`

  - `next_page: Optional[str]`

  - `object: Literal["page"]`

    - `"page"`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
response = client.admin.organization.usage.decisions(
    start_time=0,
print(response.data)

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
