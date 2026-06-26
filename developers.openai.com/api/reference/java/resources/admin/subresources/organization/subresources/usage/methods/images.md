<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/images/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Usage](/api/reference/java/resources/admin/subresources/organization/subresources/usage)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Images

[UsageImagesResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20UsageImagesResponse%20%3E%20(schema)) admin().organization().usage().images(UsageImagesParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/usage/images

Get images usage details for the organization.

##### ParametersExpand Collapse

UsageImagesParams params

long startTime

Start time (Unix seconds) of the query time range, inclusive.

Optional<List<String>> apiKeyIds

Return only usage for these API keys.

Optional<[BucketWidth](/api/reference/java/resources/admin/subresources/organization/subresources/usage/methods/images#(resource)%20admin.organization.usage%20%3E%20(method)%20images%20%3E%20(params)%20default%20%3E%20(param)%20bucket_width%20%3E%20(schema))> bucketWidth

Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

\_1M("1m")

\_1H("1h")

\_1D("1d")

Optional<Long> endTime

End time (Unix seconds) of the query time range, exclusive.

Optional<List<GroupBy>> groupBy

Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model`, `size`, `source` or any combination of them.

PROJECT\_ID("project\_id")

USER\_ID("user\_id")

API\_KEY\_ID("api\_key\_id")

MODEL("model")

SIZE("size")

SOURCE("source")

Optional<Long> limit

Specifies the number of buckets to return.

* `bucket_width=1d`: default: 7, max: 31
* `bucket_width=1h`: default: 24, max: 168
* `bucket_width=1m`: default: 60, max: 1440

Optional<List<String>> models

Return only usage for these models.

Optional<String> page

A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

Optional<List<String>> projectIds

Return only usage for these projects.

Optional<List<Size>> sizes

Return only usages for these image sizes. Possible values are `256x256`, `512x512`, `1024x1024`, `1792x1792`, `1024x1792` or any combination of them.

\_256X256("256x256")

\_512X512("512x512")

\_1024X1024("1024x1024")

\_1792X1792("1792x1792")

\_1024X1792("1024x1792")

Optional<List<Source>> sources

Return only usages for these sources. Possible values are `image.generation`, `image.edit`, `image.variation` or any combination of them.

IMAGE\_GENERATION("image.generation")

IMAGE\_EDIT("image.edit")

IMAGE\_VARIATION("image.variation")

Optional<List<String>> userIds

Return only usage for these users.

##### ReturnsExpand Collapse

class UsageImagesResponse:

List<Data> data

long endTime

JsonValue; object\_ "bucket"constant"bucket"constant

List<Result> results

One of the following:

class OrganizationUsageCompletionsResult:

The aggregated completions usage details of the specific time bucket.

long inputTokens

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

long numModelRequests

The count of requests made to the model.

JsonValue; object\_ "organization.usage.completions.result"constant"organization.usage.completions.result"constant

long outputTokens

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<Boolean> batch

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

Optional<Long> inputAudioTokens

The aggregated number of audio input tokens used, including cached tokens.

Optional<Long> inputCachedTokens

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

Optional<String> model

When `group_by=model`, this field provides the model name of the grouped usage result.

Optional<Long> outputAudioTokens

The aggregated number of audio output tokens used.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> serviceTier

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult:

The aggregated embeddings usage details of the specific time bucket.

long inputTokens

The aggregated number of input tokens used.

long numModelRequests

The count of requests made to the model.

JsonValue; object\_ "organization.usage.embeddings.result"constant"organization.usage.embeddings.result"constant

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<String> model

When `group_by=model`, this field provides the model name of the grouped usage result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult:

The aggregated moderations usage details of the specific time bucket.

long inputTokens

The aggregated number of input tokens used.

long numModelRequests

The count of requests made to the model.

JsonValue; object\_ "organization.usage.moderations.result"constant"organization.usage.moderations.result"constant

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<String> model

When `group_by=model`, this field provides the model name of the grouped usage result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult:

The aggregated images usage details of the specific time bucket.

long images

The number of images processed.

long numModelRequests

The count of requests made to the model.

JsonValue; object\_ "organization.usage.images.result"constant"organization.usage.images.result"constant

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<String> model

When `group_by=model`, this field provides the model name of the grouped usage result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> size

When `group_by=size`, this field provides the image size of the grouped usage result.

Optional<String> source

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult:

The aggregated audio speeches usage details of the specific time bucket.

long characters

The number of characters processed.

long numModelRequests

The count of requests made to the model.

JsonValue; object\_ "organization.usage.audio\_speeches.result"constant"organization.usage.audio\_speeches.result"constant

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<String> model

When `group_by=model`, this field provides the model name of the grouped usage result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult:

The aggregated audio transcriptions usage details of the specific time bucket.

long numModelRequests

The count of requests made to the model.

JsonValue; object\_ "organization.usage.audio\_transcriptions.result"constant"organization.usage.audio\_transcriptions.result"constant

long seconds

The number of seconds processed.

formatint64

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<String> model

When `group_by=model`, this field provides the model name of the grouped usage result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult:

The aggregated vector stores usage details of the specific time bucket.

JsonValue; object\_ "organization.usage.vector\_stores.result"constant"organization.usage.vector\_stores.result"constant

long usageBytes

The vector stores usage in bytes.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult:

The aggregated code interpreter sessions usage details of the specific time bucket.

long numSessions

The number of code interpreter sessions.

JsonValue; object\_ "organization.usage.code\_interpreter\_sessions.result"constant"organization.usage.code\_interpreter\_sessions.result"constant

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult:

The aggregated file search calls usage details of the specific time bucket.

long numRequests

The count of file search calls.

JsonValue; object\_ "organization.usage.file\_searches.result"constant"organization.usage.file\_searches.result"constant

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

Optional<String> vectorStoreId

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult:

The aggregated web search calls usage details of the specific time bucket.

long numModelRequests

The count of model requests.

long numRequests

The count of web search calls.

JsonValue; object\_ "organization.usage.web\_searches.result"constant"organization.usage.web\_searches.result"constant

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

Optional<String> contextLevel

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

Optional<String> model

When `group_by=model`, this field provides the model name of the grouped usage result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

Optional<String> userId

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult:

The aggregated costs details of the specific time bucket.

JsonValue; object\_ "organization.costs.result"constant"organization.costs.result"constant

Optional<Amount> amount

The monetary value in its associated currency.

Optional<String> currency

Lowercase ISO-4217 currency e.g. “usd”

Optional<Double> value

The numeric value of the cost.

Optional<String> apiKeyId

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

Optional<String> lineItem

When `group_by=line_item`, this field provides the line item of the grouped costs result.

Optional<String> projectId

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

Optional<Double> quantity

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

long startTime

boolean hasMore

Optional<String> nextPage

JsonValue; object\_ "page"constant"page"constant

### Images

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
import com.openai.models.admin.organization.usage.UsageImagesParams;
import com.openai.models.admin.organization.usage.UsageImagesResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UsageImagesParams params = UsageImagesParams.builder()
            .startTime(0L)
            .build();
        UsageImagesResponse response = client.admin().organization().usage().images(params);

    "object": "page",
    "data": [
            "object": "bucket",
            "start_time": 1730419200,
            "end_time": 1730505600,
            "results": [
                    "object": "organization.usage.images.result",
                    "images": 2,
                    "num_model_requests": 2,
                    "size": null,
                    "source": null,
                    "project_id": null,
                    "user_id": null,
                    "api_key_id": null,
                    "model": null
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
                    "object": "organization.usage.images.result",
                    "images": 2,
                    "num_model_requests": 2,
                    "size": null,
                    "source": null,
                    "project_id": null,
                    "user_id": null,
                    "api_key_id": null,
                    "model": null
            ]
    ],
    "has_more": false,
    "next_page": null
