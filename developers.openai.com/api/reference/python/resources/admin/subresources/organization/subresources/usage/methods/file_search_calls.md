<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Usage](/api/reference/python/resources/admin/subresources/organization/subresources/usage)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# File search calls

admin.organization.usage.file\_search\_calls(UsageFileSearchCallsParams\*\*kwargs)  -> [UsageFileSearchCallsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_file_search_calls_response%20%3E%20(schema))

GET/organization/usage/file\_search\_calls

Get file search calls usage details for the organization.

##### ParametersExpand Collapse

start\_time: int

Start time (Unix seconds) of the query time range, inclusive.

api\_key\_ids: Optional[Sequence[str]]

Return only usage for these API keys.

bucket\_width: Optional[Literal["1m", "1h", "1d"]]

Width of each time bucket in response. Currently `1m`, `1h` and `1d` are supported, default to `1d`.

One of the following:

"1m"

"1h"

"1d"

end\_time: Optional[int]

End time (Unix seconds) of the query time range, exclusive.

group\_by: Optional[List[Literal["project\_id", "user\_id", "api\_key\_id", "vector\_store\_id"]]]

Group the usage data by the specified fields. Support fields include `project_id`, `user_id`, `api_key_id`, `vector_store_id` or any combination of them.

One of the following:

"project\_id"

"user\_id"

"api\_key\_id"

"vector\_store\_id"

limit: Optional[int]

Specifies the number of buckets to return.

* `bucket_width=1d`: default: 7, max: 31
* `bucket_width=1h`: default: 24, max: 168
* `bucket_width=1m`: default: 60, max: 1440

page: Optional[str]

A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

project\_ids: Optional[Sequence[str]]

Return only usage for these projects.

user\_ids: Optional[Sequence[str]]

Return only usage for these users.

vector\_store\_ids: Optional[Sequence[str]]

Return only usage for these vector stores.

##### ReturnsExpand Collapse

class UsageFileSearchCallsResponse: …

data: List[Data]

end\_time: int

object: Literal["bucket"]

results: List[DataResult]

One of the following:

class DataResultOrganizationUsageCompletionsResult: …

The aggregated completions usage details of the specific time bucket.

input\_tokens: int

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.completions.result"]

output\_tokens: int

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: Optional[bool]

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Optional[int]

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Optional[int]

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Optional[int]

The aggregated number of audio output tokens used.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: Optional[str]

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageEmbeddingsResult: …

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.embeddings.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageModerationsResult: …

The aggregated moderations usage details of the specific time bucket.

input\_tokens: int

The aggregated number of input tokens used.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.moderations.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageImagesResult: …

The aggregated images usage details of the specific time bucket.

images: int

The number of images processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.images.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: Optional[str]

When `group_by=size`, this field provides the image size of the grouped usage result.

source: Optional[str]

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioSpeechesResult: …

The aggregated audio speeches usage details of the specific time bucket.

characters: int

The number of characters processed.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_speeches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageAudioTranscriptionsResult: …

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: int

The count of requests made to the model.

object: Literal["organization.usage.audio\_transcriptions.result"]

seconds: int

The number of seconds processed.

formatint64

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationUsageVectorStoresResult: …

The aggregated vector stores usage details of the specific time bucket.

object: Literal["organization.usage.vector\_stores.result"]

usage\_bytes: int

The vector stores usage in bytes.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageCodeInterpreterSessionsResult: …

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: int

The number of code interpreter sessions.

object: Literal["organization.usage.code\_interpreter\_sessions.result"]

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class DataResultOrganizationUsageFileSearchesResult: …

The aggregated file search calls usage details of the specific time bucket.

num\_requests: int

The count of file search calls.

object: Literal["organization.usage.file\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: Optional[str]

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class DataResultOrganizationUsageWebSearchesResult: …

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: int

The count of model requests.

num\_requests: int

The count of web search calls.

object: Literal["organization.usage.web\_searches.result"]

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: Optional[str]

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: Optional[str]

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: Optional[str]

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class DataResultOrganizationCostsResult: …

The aggregated costs details of the specific time bucket.

object: Literal["organization.costs.result"]

amount: Optional[DataResultOrganizationCostsResultAmount]

The monetary value in its associated currency.

currency: Optional[str]

Lowercase ISO-4217 currency e.g. “usd”

value: Optional[float]

The numeric value of the cost.

api\_key\_id: Optional[str]

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: Optional[str]

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: Optional[str]

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Optional[float]

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: int

has\_more: bool

next\_page: Optional[str]

object: Literal["page"]

### File search calls

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
response = client.admin.organization.usage.file_search_calls(
    start_time=0,
print(response.data)

    "object": "page",
    "data": [
            "object": "bucket",
            "start_time": 1730419200,
            "end_time": 1730505600,
            "results": [
                    "object": "organization.usage.file_searches.result",
                    "num_requests": 2,
                    "project_id": null,
                    "user_id": null,
                    "api_key_id": null,
                    "vector_store_id": null
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
                    "object": "organization.usage.file_searches.result",
                    "num_requests": 2,
                    "project_id": null,
                    "user_id": null,
                    "api_key_id": null,
                    "vector_store_id": null
            ]
    ],
    "has_more": false,
    "next_page": null
