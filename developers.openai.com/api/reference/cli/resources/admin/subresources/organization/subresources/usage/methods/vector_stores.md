<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/usage/methods/vector_stores/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Usage](/api/reference/cli/resources/admin/subresources/organization/subresources/usage)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Vector stores

$ openai admin:organization:usage vector-stores

GET/organization/usage/vector\_stores

Get vector stores usage details for the organization.

##### ParametersExpand Collapse

--start-time: number

Start time (Unix seconds) of the query time range, inclusive.

--bucket-width: optional "1m" or "1h" or "1d"

Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

--end-time: optional number

End time (Unix seconds) of the query time range, exclusive.

--group-by: optional array of "project\_id"

Group the usage data by the specified fields. Support fields include `project_id`.

--limit: optional number

Specifies the number of buckets to return.

* `bucket_width=1d`: default: 7, max: 31
* `bucket_width=1h`: default: 24, max: 168
* `bucket_width=1m`: default: 60, max: 1440

--page: optional string

A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

--project-id: optional array of string

Return only usage for these projects.

##### ReturnsExpand Collapse

AdminOrganizationUsageVectorStoresResponse: object { data, has\_more, next\_page, object }

data: array of object { end\_time, object, results, start\_time }

end\_time: number

object: "bucket"

results: array of object { input\_tokens, num\_model\_requests, object, 10 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or object { input\_tokens, num\_model\_requests, object, 4 more }  or 8 more

organization.usage.completions.result: object { input\_tokens, num\_model\_requests, object, 10 more }

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

organization.usage.embeddings.result: object { input\_tokens, num\_model\_requests, object, 4 more }

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

organization.usage.moderations.result: object { input\_tokens, num\_model\_requests, object, 4 more }

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

organization.usage.images.result: object { images, num\_model\_requests, object, 6 more }

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

organization.usage.audio\_speeches.result: object { characters, num\_model\_requests, object, 4 more }

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

organization.usage.audio\_transcriptions.result: object { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

api\_key\_id: optional string

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: optional string

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: optional string

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

organization.usage.vector\_stores.result: object { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

organization.usage.code\_interpreter\_sessions.result: object { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id: optional string

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

organization.usage.file\_searches.result: object { num\_requests, object, api\_key\_id, 3 more }

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

organization.usage.web\_searches.result: object { num\_model\_requests, num\_requests, object, 5 more }

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

organization.costs.result: object { object, amount, api\_key\_id, 3 more }

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

### Vector stores

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:usage vector-stores \
  --admin-api-key 'My Admin API Key' \
  --start-time 0

    "object": "page",
    "data": [
            "object": "bucket",
            "start_time": 1730419200,
            "end_time": 1730505600,
            "results": [
                    "object": "organization.usage.vector_stores.result",
                    "usage_bytes": 1024,
                    "project_id": null
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
                    "object": "organization.usage.vector_stores.result",
                    "usage_bytes": 1024,
                    "project_id": null
            ]
    ],
    "has_more": false,
    "next_page": null
