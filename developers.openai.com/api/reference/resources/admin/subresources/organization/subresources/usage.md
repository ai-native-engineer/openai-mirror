<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/usage/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Usage

##### [Audio speeches](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/completions)

GET/organization/usage/completions

##### [Embeddings](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

GET/organization/usage/embeddings

##### [Images](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/images)

GET/organization/usage/images

##### [Moderations](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/moderations)

GET/organization/usage/moderations

##### [Vector stores](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/resources/admin/subresources/organization/subresources/usage/methods/costs)

GET/organization/costs

##### ModelsExpand Collapse

UsageAudioSpeechesResponse object { data, has\_more, next\_page, object }

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

UsageAudioTranscriptionsResponse object { data, has\_more, next\_page, object }

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

UsageCodeInterpreterSessionsResponse object { data, has\_more, next\_page, object }

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

UsageCompletionsResponse object { data, has\_more, next\_page, object }

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

UsageEmbeddingsResponse object { data, has\_more, next\_page, object }

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

UsageImagesResponse object { data, has\_more, next\_page, object }

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

UsageModerationsResponse object { data, has\_more, next\_page, object }

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

UsageVectorStoresResponse object { data, has\_more, next\_page, object }

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

UsageFileSearchCallsResponse object { data, has\_more, next\_page, object }

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

UsageWebSearchCallsResponse object { data, has\_more, next\_page, object }

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

UsageCostsResponse object { data, has\_more, next\_page, object }

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
