<!-- source: https://developers.openai.com/api/reference/ruby/resources/models/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/ruby/resources/models/methods/list)

models.list() -> Page<[Model](/api/reference/ruby/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by } >

GET/models

##### [Retrieve model](/api/reference/ruby/resources/models/methods/retrieve)

models.retrieve(model) -> [Model](/api/reference/ruby/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) { id, created, object, owned\_by }

GET/models/{model}

##### [Delete a fine-tuned model](/api/reference/ruby/resources/models/methods/delete)

models.delete(model) -> [ModelDeleted](/api/reference/ruby/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/models/{model}

##### ModelsExpand Collapse

class Model { id, created, object, owned\_by }

Describes an OpenAI model offering that can be used with the API.

id: String

The model identifier, which can be referenced in the API endpoints.

created: Integer

The Unix timestamp (in seconds) when the model was created.

formatunixtime

object: :model

The object type, which is always “model”.

owned\_by: String

The organization that owns the model.

class ModelDeleted { id, deleted, object }

id: String

deleted: bool

object: String
