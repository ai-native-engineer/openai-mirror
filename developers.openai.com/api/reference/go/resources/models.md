<!-- source: https://developers.openai.com/api/reference/go/resources/models/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/go/resources/models/methods/list)

client.Models.List(ctx) (\*Page[[Model](/api/reference/go/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema))], error)

GET/models

##### [Retrieve model](/api/reference/go/resources/models/methods/retrieve)

client.Models.Get(ctx, model) (\*[Model](/api/reference/go/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)), error)

GET/models/{model}

##### [Delete a fine-tuned model](/api/reference/go/resources/models/methods/delete)

client.Models.Delete(ctx, model) (\*[ModelDeleted](/api/reference/go/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)), error)

DELETE/models/{model}

##### ModelsExpand Collapse

type Model struct{…}

Describes an OpenAI model offering that can be used with the API.

ID string

The model identifier, which can be referenced in the API endpoints.

Created int64

The Unix timestamp (in seconds) when the model was created.

formatunixtime

Object Model

The object type, which is always “model”.

OwnedBy string

The organization that owns the model.

type ModelDeleted struct{…}

ID string

Deleted bool

Object string
