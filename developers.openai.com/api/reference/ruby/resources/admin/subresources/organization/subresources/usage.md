<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Usage

##### [Audio speeches](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

admin.organization.usage.audio\_speeches(\*\*kwargs) -> [UsageAudioSpeechesResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

admin.organization.usage.audio\_transcriptions(\*\*kwargs) -> [UsageAudioTranscriptionsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

admin.organization.usage.code\_interpreter\_sessions(\*\*kwargs) -> [UsageCodeInterpreterSessionsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/completions)

admin.organization.usage.completions(\*\*kwargs) -> [UsageCompletionsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/completions

##### [Embeddings](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

admin.organization.usage.embeddings(\*\*kwargs) -> [UsageEmbeddingsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/embeddings

##### [Images](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/images)

admin.organization.usage.images(\*\*kwargs) -> [UsageImagesResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/images

##### [Moderations](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/moderations)

admin.organization.usage.moderations(\*\*kwargs) -> [UsageModerationsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_moderations_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/moderations

##### [Vector stores](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

admin.organization.usage.vector\_stores(\*\*kwargs) -> [UsageVectorStoresResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_vector_stores_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

admin.organization.usage.file\_search\_calls(\*\*kwargs) -> [UsageFileSearchCallsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_file_search_calls_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

admin.organization.usage.web\_search\_calls(\*\*kwargs) -> [UsageWebSearchCallsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_web_search_calls_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/ruby/resources/admin/subresources/organization/subresources/usage/methods/costs)

admin.organization.usage.costs(\*\*kwargs) -> [UsageCostsResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_costs_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/costs

##### ModelsExpand Collapse

class UsageAudioSpeechesResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageAudioTranscriptionsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageCodeInterpreterSessionsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageCompletionsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageEmbeddingsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageImagesResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageModerationsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageVectorStoresResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageFileSearchCallsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageWebSearchCallsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page

class UsageCostsResponse { data, has\_more, next\_page, object }

data: Array[Data{ end\_time, object, results, start\_time}]

end\_time: Integer

object: :bucket

results: Array[OrganizationUsageCompletionsResult{ input\_tokens, num\_model\_requests, object, 10 more} | OrganizationUsageEmbeddingsResult{ input\_tokens, num\_model\_requests, object, 4 more} | OrganizationUsageModerationsResult{ input\_tokens, num\_model\_requests, object, 4 more} | 8 more]

One of the following:

class OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.completions.result"

output\_tokens: Integer

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch: bool

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens: Integer

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens: Integer

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens: Integer

The aggregated number of audio output tokens used.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier: String

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.embeddings.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: Integer

The aggregated number of input tokens used.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.moderations.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: Integer

The number of images processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.images.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size: String

When `group_by=size`, this field provides the image size of the grouped usage result.

source: String

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: Integer

The number of characters processed.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_speeches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: Integer

The count of requests made to the model.

object: :"organization.usage.audio\_transcriptions.result"

seconds: Integer

The number of seconds processed.

formatint64

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: :"organization.usage.vector\_stores.result"

usage\_bytes: Integer

The vector stores usage in bytes.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: Integer

The number of code interpreter sessions.

object: :"organization.usage.code\_interpreter\_sessions.result"

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

class OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: Integer

The count of file search calls.

object: :"organization.usage.file\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id: String

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

class OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: Integer

The count of model requests.

num\_requests: Integer

The count of web search calls.

object: :"organization.usage.web\_searches.result"

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level: String

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model: String

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id: String

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

class OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: :"organization.costs.result"

amount: Amount{ currency, value}

The monetary value in its associated currency.

currency: String

Lowercase ISO-4217 currency e.g. “usd”

value: Float

The numeric value of the cost.

api\_key\_id: String

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item: String

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id: String

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity: Float

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: Integer

has\_more: bool

next\_page: String

object: :page
