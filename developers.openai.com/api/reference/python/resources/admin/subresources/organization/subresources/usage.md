<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/usage/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Usage

##### [Audio speeches](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/audio_speeches)

admin.organization.usage.audio\_speeches(UsageAudioSpeechesParams\*\*kwargs)  -> [UsageAudioSpeechesResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_speeches_response%20%3E%20(schema))

GET/organization/usage/audio\_speeches

##### [Audio transcriptions](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/audio_transcriptions)

admin.organization.usage.audio\_transcriptions(UsageAudioTranscriptionsParams\*\*kwargs)  -> [UsageAudioTranscriptionsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_audio_transcriptions_response%20%3E%20(schema))

GET/organization/usage/audio\_transcriptions

##### [Code interpreter sessions](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/code_interpreter_sessions)

admin.organization.usage.code\_interpreter\_sessions(UsageCodeInterpreterSessionsParams\*\*kwargs)  -> [UsageCodeInterpreterSessionsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_code_interpreter_sessions_response%20%3E%20(schema))

GET/organization/usage/code\_interpreter\_sessions

##### [Completions](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/completions)

admin.organization.usage.completions(UsageCompletionsParams\*\*kwargs)  -> [UsageCompletionsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_completions_response%20%3E%20(schema))

GET/organization/usage/completions

##### [Embeddings](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/embeddings)

admin.organization.usage.embeddings(UsageEmbeddingsParams\*\*kwargs)  -> [UsageEmbeddingsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_embeddings_response%20%3E%20(schema))

GET/organization/usage/embeddings

##### [Images](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/images)

admin.organization.usage.images(UsageImagesParams\*\*kwargs)  -> [UsageImagesResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_images_response%20%3E%20(schema))

GET/organization/usage/images

##### [Moderations](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/moderations)

admin.organization.usage.moderations(UsageModerationsParams\*\*kwargs)  -> [UsageModerationsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_moderations_response%20%3E%20(schema))

GET/organization/usage/moderations

##### [Vector stores](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/vector_stores)

admin.organization.usage.vector\_stores(UsageVectorStoresParams\*\*kwargs)  -> [UsageVectorStoresResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_vector_stores_response%20%3E%20(schema))

GET/organization/usage/vector\_stores

##### [File search calls](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/file_search_calls)

admin.organization.usage.file\_search\_calls(UsageFileSearchCallsParams\*\*kwargs)  -> [UsageFileSearchCallsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_file_search_calls_response%20%3E%20(schema))

GET/organization/usage/file\_search\_calls

##### [Web search calls](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/web_search_calls)

admin.organization.usage.web\_search\_calls(UsageWebSearchCallsParams\*\*kwargs)  -> [UsageWebSearchCallsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_web_search_calls_response%20%3E%20(schema))

GET/organization/usage/web\_search\_calls

##### [Costs](/api/reference/python/resources/admin/subresources/organization/subresources/usage/methods/costs)

admin.organization.usage.costs(UsageCostsParams\*\*kwargs)  -> [UsageCostsResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_costs_response%20%3E%20(schema))

GET/organization/costs

##### ModelsExpand Collapse

class UsageAudioSpeechesResponse: …

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

class UsageAudioTranscriptionsResponse: …

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

class UsageCodeInterpreterSessionsResponse: …

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

class UsageCompletionsResponse: …

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

class UsageEmbeddingsResponse: …

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

class UsageImagesResponse: …

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

class UsageModerationsResponse: …

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

class UsageVectorStoresResponse: …

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

class UsageWebSearchCallsResponse: …

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

class UsageCostsResponse: …

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
