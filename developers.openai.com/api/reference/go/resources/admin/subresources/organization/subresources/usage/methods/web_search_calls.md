<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Usage](/api/reference/go/resources/admin/subresources/organization/subresources/usage)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Web search calls

client.Admin.Organization.Usage.WebSearchCalls(ctx, query) (\*[AdminOrganizationUsageWebSearchCallsResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20AdminOrganizationUsageWebSearchCallsResponse%20%3E%20(schema)), error)

GET/organization/usage/web\_search\_calls

Get web search calls usage details for the organization.

##### ParametersExpand Collapse

query AdminOrganizationUsageWebSearchCallsParams

StartTime param.Field[int64]

Start time (Unix seconds) of the query time range, inclusive.

APIKeyIDs param.Field[[]string]Optional

Return only usage for these API keys.

BucketWidth param.Field[[AdminOrganizationUsageWebSearchCallsParamsBucketWidth](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls#(resource)%20admin.organization.usage%20%3E%20(method)%20web_search_calls%20%3E%20(params)%20default%20%3E%20(param)%20bucket_width%20%3E%20(schema))]Optional

Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

const AdminOrganizationUsageWebSearchCallsParamsBucketWidth1m [AdminOrganizationUsageWebSearchCallsParamsBucketWidth](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls#(resource)%20admin.organization.usage%20%3E%20(method)%20web_search_calls%20%3E%20(params)%20default%20%3E%20(param)%20bucket_width%20%3E%20(schema)) = "1m"

const AdminOrganizationUsageWebSearchCallsParamsBucketWidth1h [AdminOrganizationUsageWebSearchCallsParamsBucketWidth](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls#(resource)%20admin.organization.usage%20%3E%20(method)%20web_search_calls%20%3E%20(params)%20default%20%3E%20(param)%20bucket_width%20%3E%20(schema)) = "1h"

const AdminOrganizationUsageWebSearchCallsParamsBucketWidth1d [AdminOrganizationUsageWebSearchCallsParamsBucketWidth](/api/reference/go/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls#(resource)%20admin.organization.usage%20%3E%20(method)%20web_search_calls%20%3E%20(params)%20default%20%3E%20(param)%20bucket_width%20%3E%20(schema)) = "1d"

ContextLevels param.Field[[]string]Optional

Return only web search usage for these context levels.

const AdminOrganizationUsageWebSearchCallsParamsContextLevelLow AdminOrganizationUsageWebSearchCallsParamsContextLevel = "low"

const AdminOrganizationUsageWebSearchCallsParamsContextLevelMedium AdminOrganizationUsageWebSearchCallsParamsContextLevel = "medium"

const AdminOrganizationUsageWebSearchCallsParamsContextLevelHigh AdminOrganizationUsageWebSearchCallsParamsContextLevel = "high"

EndTime param.Field[int64]Optional

End time (Unix seconds) of the query time range, exclusive.

GroupBy param.Field[[]string]Optional

Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `context_level` or any combination of them.

const AdminOrganizationUsageWebSearchCallsParamsGroupByProjectID AdminOrganizationUsageWebSearchCallsParamsGroupBy = "project\_id"

const AdminOrganizationUsageWebSearchCallsParamsGroupByUserID AdminOrganizationUsageWebSearchCallsParamsGroupBy = "user\_id"

const AdminOrganizationUsageWebSearchCallsParamsGroupByAPIKeyID AdminOrganizationUsageWebSearchCallsParamsGroupBy = "api\_key\_id"

const AdminOrganizationUsageWebSearchCallsParamsGroupByModel AdminOrganizationUsageWebSearchCallsParamsGroupBy = "model"

const AdminOrganizationUsageWebSearchCallsParamsGroupByContextLevel AdminOrganizationUsageWebSearchCallsParamsGroupBy = "context\_level"

Limit param.Field[int64]Optional

Specifies the number of buckets to return.

* `bucket_width=1d`: default: 7, max: 31
* `bucket_width=1h`: default: 24, max: 168
* `bucket_width=1m`: default: 60, max: 1440

Models param.Field[[]string]Optional

Return only usage for these models.

Page param.Field[string]Optional

A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

ProjectIDs param.Field[[]string]Optional

Return only usage for these projects.

UserIDs param.Field[[]string]Optional

Return only usage for these users.

##### ReturnsExpand Collapse

type AdminOrganizationUsageWebSearchCallsResponse struct{…}

Data []AdminOrganizationUsageWebSearchCallsResponseData

EndTime int64

Object Bucket

Results []AdminOrganizationUsageWebSearchCallsResponseDataResultUnion

One of the following:

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageCompletionsResult struct{…}

The aggregated completions usage details of the specific time bucket.

InputTokens int64

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

NumModelRequests int64

The count of requests made to the model.

Object OrganizationUsageCompletionsResult

OutputTokens int64

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Batch boolOptional

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

InputAudioTokens int64Optional

The aggregated number of audio input tokens used, including cached tokens.

InputCachedTokens int64Optional

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

Model stringOptional

When `group_by=model`, this field provides the model name of the grouped usage result.

OutputAudioTokens int64Optional

The aggregated number of audio output tokens used.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

ServiceTier stringOptional

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageEmbeddingsResult struct{…}

The aggregated embeddings usage details of the specific time bucket.

InputTokens int64

The aggregated number of input tokens used.

NumModelRequests int64

The count of requests made to the model.

Object OrganizationUsageEmbeddingsResult

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Model stringOptional

When `group_by=model`, this field provides the model name of the grouped usage result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageModerationsResult struct{…}

The aggregated moderations usage details of the specific time bucket.

InputTokens int64

The aggregated number of input tokens used.

NumModelRequests int64

The count of requests made to the model.

Object OrganizationUsageModerationsResult

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Model stringOptional

When `group_by=model`, this field provides the model name of the grouped usage result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageImagesResult struct{…}

The aggregated images usage details of the specific time bucket.

Images int64

The number of images processed.

NumModelRequests int64

The count of requests made to the model.

Object OrganizationUsageImagesResult

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Model stringOptional

When `group_by=model`, this field provides the model name of the grouped usage result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Size stringOptional

When `group_by=size`, this field provides the image size of the grouped usage result.

Source stringOptional

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageAudioSpeechesResult struct{…}

The aggregated audio speeches usage details of the specific time bucket.

Characters int64

The number of characters processed.

NumModelRequests int64

The count of requests made to the model.

Object OrganizationUsageAudioSpeechesResult

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Model stringOptional

When `group_by=model`, this field provides the model name of the grouped usage result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageAudioTranscriptionsResult struct{…}

The aggregated audio transcriptions usage details of the specific time bucket.

NumModelRequests int64

The count of requests made to the model.

Object OrganizationUsageAudioTranscriptionsResult

Seconds int64

The number of seconds processed.

formatint64

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Model stringOptional

When `group_by=model`, this field provides the model name of the grouped usage result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageVectorStoresResult struct{…}

The aggregated vector stores usage details of the specific time bucket.

Object OrganizationUsageVectorStoresResult

UsageBytes int64

The vector stores usage in bytes.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageCodeInterpreterSessionsResult struct{…}

The aggregated code interpreter sessions usage details of the specific time bucket.

NumSessions int64

The number of code interpreter sessions.

Object OrganizationUsageCodeInterpreterSessionsResult

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageFileSearchesResult struct{…}

The aggregated file search calls usage details of the specific time bucket.

NumRequests int64

The count of file search calls.

Object OrganizationUsageFileSearchesResult

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

VectorStoreID stringOptional

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationUsageWebSearchesResult struct{…}

The aggregated web search calls usage details of the specific time bucket.

NumModelRequests int64

The count of model requests.

NumRequests int64

The count of web search calls.

Object OrganizationUsageWebSearchesResult

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

ContextLevel stringOptional

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

Model stringOptional

When `group_by=model`, this field provides the model name of the grouped usage result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

UserID stringOptional

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

type AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationCostsResult struct{…}

The aggregated costs details of the specific time bucket.

Object OrganizationCostsResult

Amount AdminOrganizationUsageWebSearchCallsResponseDataResultOrganizationCostsResultAmountOptional

The monetary value in its associated currency.

Currency stringOptional

Lowercase ISO-4217 currency e.g. “usd”

Value float64Optional

The numeric value of the cost.

APIKeyID stringOptional

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

LineItem stringOptional

When `group_by=line_item`, this field provides the line item of the grouped costs result.

ProjectID stringOptional

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

Quantity float64Optional

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

StartTime int64

HasMore bool

NextPage string

Object Page

### Web search calls

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
  response, err := client.Admin.Organization.Usage.WebSearchCalls(context.TODO(), openai.AdminOrganizationUsageWebSearchCallsParams{
    StartTime: 0,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response.Data)

    "object": "page",
    "data": [
            "object": "bucket",
            "start_time": 1730419200,
            "end_time": 1730505600,
            "results": [
                    "object": "organization.usage.web_searches.result",
                    "num_model_requests": 2,
                    "num_requests": 2,
                    "project_id": null,
                    "user_id": null,
                    "api_key_id": null,
                    "model": null,
                    "context_level": null
            ]
    ],
    "has_more": false,
    "next_page": null

##### Returns Examples

    "object": "page",
    "data": [
            "object": "bucket",
            "start_time": 1730419200,
            "end_time": 1730505600,
            "results": [
                    "object": "organization.usage.web_searches.result",
                    "num_model_requests": 2,
                    "num_requests": 2,
                    "project_id": null,
                    "user_id": null,
                    "api_key_id": null,
                    "model": null,
                    "context_level": null
            ]
    ],
    "has_more": false,
    "next_page": null
