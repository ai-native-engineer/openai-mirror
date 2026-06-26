<!-- source: https://developers.openai.com/api/reference/python/resources/models/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/python/resources/models/methods/list)

models.list()  -> SyncPage[[Model](/api/reference/python/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema))]

GET/models

##### [Retrieve model](/api/reference/python/resources/models/methods/retrieve)

models.retrieve(strmodel)  -> [Model](/api/reference/python/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema))

GET/models/{model}

##### [Delete a fine-tuned model](/api/reference/python/resources/models/methods/delete)

models.delete(strmodel)  -> [ModelDeleted](/api/reference/python/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema))

DELETE/models/{model}

##### ModelsExpand Collapse

class Model: …

Describes an OpenAI model offering that can be used with the API.

id: str

The model identifier, which can be referenced in the API endpoints.

created: int

The Unix timestamp (in seconds) when the model was created.

formatunixtime

object: Literal["model"]

The object type, which is always “model”.

owned\_by: str

The organization that owns the model.

class ModelDeleted: …

id: str

deleted: bool

object: str
