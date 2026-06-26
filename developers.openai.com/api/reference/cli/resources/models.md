<!-- source: https://developers.openai.com/api/reference/cli/resources/models/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/cli/resources/models/methods/list)

$ openai models list

GET/models

##### [Retrieve model](/api/reference/cli/resources/models/methods/retrieve)

$ openai models retrieve

GET/models/{model}

##### [Delete a fine-tuned model](/api/reference/cli/resources/models/methods/delete)

$ openai models delete

DELETE/models/{model}

##### ModelsExpand Collapse

model: object { id, created, object, owned\_by }

Describes an OpenAI model offering that can be used with the API.

id: string

The model identifier, which can be referenced in the API endpoints.

created: number

The Unix timestamp (in seconds) when the model was created.

object: "model"

The object type, which is always “model”.

owned\_by: string

The organization that owns the model.

model\_deleted: object { id, deleted, object }

id: string

deleted: boolean

object: string
