<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Usage](/api/reference/resources/admin/subresources/organization/subresources/usage)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Audio transcriptions

GET/organization/usage/audio\_transcriptions

Get audio transcriptions usage details for the organization.

##### Query ParametersExpand Collapse

start\_time: number

Start time (Unix seconds) of the query time range, inclusive.

api\_key\_ids: optional array of string

Return only usage for these API keys.

bucket\_width: optional "1m" or "1h" or "1d"

Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

One of the following:

"1m"

"1h"

"1d"

end\_time: optional number

End time (Unix seconds) of the query time range, exclusive.

group\_by: optional array of "project\_id" or "user\_id" or "api\_key\_id" or "model"

Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `model` or any combination of them.

One of the following:

"project\_id"

"user\_id"

"api\_key\_id"

"model"

limit: optional number

Specifies the number of buckets to return.

* `bucket_width=1d`: default: 7, max: 31
* `bucket_width=1h`: default: 24, max: 168
* `bucket_width=1m`: default: 60, max: 1440

models: optional array of string

Return only usage for these models.

page: optional string

A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

project\_ids: optional array of string

Return only usage for these projects.

user\_ids: optional array of string

Return only usage for these users.

##### ReturnsExpand Collapse

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

One of the following:

OrganizationUsageCompletionsResult object { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: optional boolean

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: optional number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: optional number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: optional number

The aggregated number of audio output tokens used.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: optional string

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult object { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult object { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: optional string

When `group_by=size`, this field provides the image size of the grouped usage result.

source: optional string

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult object { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult object { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: optional string

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult object { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: optional string

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult object { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount: optional object { currency, value }

The monetary value in its associated currency.

currency: optional string

Lowercase ISO-4217 currency e.g. “usd”

value: optional number

The numeric value of the cost.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: optional string

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: optional number

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string

object: "page"

### Audio transcriptions

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl "https://api.openai.com/v1/organization/usage/audio_transcriptions?start_time=1730419200&limit=1" \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json"

    "object": "page",
    "data": [
            "object": "bucket",
            "start_time": 1730419200,
            "end_time": 1730505600,
            "results": [
                    "object": "organization.usage.audio_transcriptions.result",
                    "seconds": 20,
                    "num_model_requests": 1,
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
                    "object": "organization.usage.audio_transcriptions.result",
                    "seconds": 20,
                    "num_model_requests": 1,
                    "project_id": null,
                    "user_id": null,
                    "api_key_id": null,
                    "model": null
            ]
    ],
    "has_more": false,
    "next_page": null
