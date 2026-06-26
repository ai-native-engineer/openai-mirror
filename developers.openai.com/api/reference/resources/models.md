<!-- source: https://developers.openai.com/api/reference/resources/models/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/resources/models/methods/list)

GET/models

##### [Retrieve model](/api/reference/resources/models/methods/retrieve)

GET/models/{model}

##### [Delete a fine-tuned model](/api/reference/resources/models/methods/delete)

DELETE/models/{model}

##### ModelsExpand Collapse

Model object { id, created, object, owned\_by }

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

ModelDeleted object { id, deleted, object }

id: string

deleted: boolean

object: string
