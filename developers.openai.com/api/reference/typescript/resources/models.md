<!-- source: https://developers.openai.com/api/reference/typescript/resources/models/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/typescript/resources/models/methods/list)

client.models.list(RequestOptionsoptions?): Page<[Model](/api/reference/typescript/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by } >

GET/models

##### [Retrieve model](/api/reference/typescript/resources/models/methods/retrieve)

client.models.retrieve(stringmodel, RequestOptionsoptions?): [Model](/api/reference/typescript/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by }

GET/models/{model}

##### [Delete a fine-tuned model](/api/reference/typescript/resources/models/methods/delete)

client.models.delete(stringmodel, RequestOptionsoptions?): [ModelDeleted](/api/reference/typescript/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/models/{model}

##### ModelsExpand Collapse

Model { id, created, object, owned\_by }

Describes an OpenAI model offering that can be used with the API.

id: string

The model identifier, which can be referenced in the API endpoints.

created: number

The Unix timestamp (in seconds) when the model was created.

formatunixtime

object: "model"

The object type, which is always “model”.

owned\_by: string

The organization that owns the model.

ModelDeleted { id, deleted, object }

id: string

deleted: boolean

object: string
