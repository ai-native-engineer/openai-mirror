<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/usage/methods/costs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Usage](/api/reference/typescript/resources/admin/subresources/organization/subresources/usage)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Costs

client.admin.organization.usage.costs(UsageCostsParams { start\_time, api\_key\_ids, bucket\_width, 5 more } query, RequestOptionsoptions?): [UsageCostsResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.usage%20%3E%20(model)%20usage_costs_response%20%3E%20(schema)) { data, has\_more, next\_page, object }

GET/organization/costs

Get costs details for the organization.

##### ParametersExpand Collapse

query: UsageCostsParams { start\_time, api\_key\_ids, bucket\_width, 5 more }

start\_time: number

Start time (Unix seconds) of the query time range, inclusive.

api\_key\_ids?: Array<string>

Return only costs for these API keys.

bucket\_width?: "1d"

Width of each time bucket in response. Currently only `1d` is supported, default to `1d`.

end\_time?: number

End time (Unix seconds) of the query time range, exclusive.

group\_by?: Array<"project\_id" | "line\_item" | "api\_key\_id">

Group the costs by the specified fields. Support fields include `project_id`, `line_item`, `api_key_id` and any combination of them.

One of the following:

"project\_id"

"line\_item"

"api\_key\_id"

limit?: number

A limit on the number of buckets to be returned. Limit can range between 1 and 180, and the default is 7.

page?: string

A cursor for use in pagination. Corresponding to the `next_page` field from the previous response.

project\_ids?: Array<string>

Return only costs for these projects.

##### ReturnsExpand Collapse

UsageCostsResponse { data, has\_more, next\_page, object }

data: Array<Data>

end\_time: number

object: "bucket"

results: Array<OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }  | OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }  | OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }  | 8 more>

One of the following:

OrganizationUsageCompletionsResult { input\_tokens, num\_model\_requests, object, 10 more }

The aggregated completions usage details of the specific time bucket.

input\_tokens: number

The aggregated number of text input tokens used, including cached tokens. For customers subscribe to scale tier, this includes scale tier tokens.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.completions.result"

output\_tokens: number

The aggregated number of text output tokens used. For customers subscribe to scale tier, this includes scale tier tokens.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

batch?: boolean | null

When `group_by=batch`, this field tells whether the grouped usage result is batch or not.

input\_audio\_tokens?: number

The aggregated number of audio input tokens used, including cached tokens.

input\_cached\_tokens?: number

The aggregated number of text input tokens that has been cached from previous requests. For customers subscribe to scale tier, this includes scale tier tokens.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

output\_audio\_tokens?: number

The aggregated number of audio output tokens used.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

service\_tier?: string | null

When `group_by=service_tier`, this field provides the service tier of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageEmbeddingsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated embeddings usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.embeddings.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageModerationsResult { input\_tokens, num\_model\_requests, object, 4 more }

The aggregated moderations usage details of the specific time bucket.

input\_tokens: number

The aggregated number of input tokens used.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.moderations.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageImagesResult { images, num\_model\_requests, object, 6 more }

The aggregated images usage details of the specific time bucket.

images: number

The number of images processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.images.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

size?: string | null

When `group_by=size`, this field provides the image size of the grouped usage result.

source?: string | null

When `group_by=source`, this field provides the source of the grouped usage result, possible values are `image.generation`, `image.edit`, `image.variation`.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioSpeechesResult { characters, num\_model\_requests, object, 4 more }

The aggregated audio speeches usage details of the specific time bucket.

characters: number

The number of characters processed.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_speeches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageAudioTranscriptionsResult { num\_model\_requests, object, seconds, 4 more }

The aggregated audio transcriptions usage details of the specific time bucket.

num\_model\_requests: number

The count of requests made to the model.

object: "organization.usage.audio\_transcriptions.result"

seconds: number

The number of seconds processed.

formatint64

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationUsageVectorStoresResult { object, usage\_bytes, project\_id }

The aggregated vector stores usage details of the specific time bucket.

object: "organization.usage.vector\_stores.result"

usage\_bytes: number

The vector stores usage in bytes.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageCodeInterpreterSessionsResult { num\_sessions, object, project\_id }

The aggregated code interpreter sessions usage details of the specific time bucket.

num\_sessions: number

The number of code interpreter sessions.

object: "organization.usage.code\_interpreter\_sessions.result"

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

OrganizationUsageFileSearchesResult { num\_requests, object, api\_key\_id, 3 more }

The aggregated file search calls usage details of the specific time bucket.

num\_requests: number

The count of file search calls.

object: "organization.usage.file\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

vector\_store\_id?: string | null

When `group_by=vector_store_id`, this field provides the vector store ID of the grouped usage result.

OrganizationUsageWebSearchesResult { num\_model\_requests, num\_requests, object, 5 more }

The aggregated web search calls usage details of the specific time bucket.

num\_model\_requests: number

The count of model requests.

num\_requests: number

The count of web search calls.

object: "organization.usage.web\_searches.result"

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API key ID of the grouped usage result.

context\_level?: string | null

When `group_by=context_level`, this field provides the search context size of the grouped usage result.

model?: string | null

When `group_by=model`, this field provides the model name of the grouped usage result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped usage result.

user\_id?: string | null

When `group_by=user_id`, this field provides the user ID of the grouped usage result.

OrganizationCostsResult { object, amount, api\_key\_id, 3 more }

The aggregated costs details of the specific time bucket.

object: "organization.costs.result"

amount?: Amount { currency, value }

The monetary value in its associated currency.

currency?: string

Lowercase ISO-4217 currency e.g. “usd”

value?: number

The numeric value of the cost.

api\_key\_id?: string | null

When `group_by=api_key_id`, this field provides the API Key ID of the grouped costs result.

line\_item?: string | null

When `group_by=line_item`, this field provides the line item of the grouped costs result.

project\_id?: string | null

When `group_by=project_id`, this field provides the project ID of the grouped costs result.

quantity?: number | null

When `group_by=line_item`, this field provides the quantity of the grouped costs result.

start\_time: number

has\_more: boolean

next\_page: string | null

object: "page"

### Costs

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const response = await client.admin.organization.usage.costs({ start_time: 0 });

console.log(response.data);

    "object": "page",
    "data": [
            "object": "bucket",
            "start_time": 1730419200,
            "end_time": 1730505600,
            "results": [
                    "object": "organization.costs.result",
                    "amount": {
                        "value": 0.06,
                        "currency": "usd"
                    "line_item": null,
                    "project_id": null,
                    "api_key_id": null,
                    "quantity": null
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
                    "object": "organization.costs.result",
                    "amount": {
                        "value": 0.06,
                        "currency": "usd"
                    "line_item": null,
                    "project_id": null,
                    "api_key_id": null,
                    "quantity": null
            ]
    ],
    "has_more": false,
    "next_page": null
