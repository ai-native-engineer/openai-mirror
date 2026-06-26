<!-- source: https://developers.openai.com/api/reference/java/resources/models/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Models

List and describe the various models available in the API.

##### [List models](/api/reference/java/resources/models/methods/list)

ModelListPage models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/models

##### [Retrieve model](/api/reference/java/resources/models/methods/retrieve)

[Model](/api/reference/java/resources/models#(resource)%20models%20%3E%20(model)%20model%20%3E%20(schema)) models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/models/{model}

##### [Delete a fine-tuned model](/api/reference/java/resources/models/methods/delete)

[ModelDeleted](/api/reference/java/resources/models#(resource)%20models%20%3E%20(model)%20model_deleted%20%3E%20(schema)) models().delete(ModelDeleteParamsparams = ModelDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/models/{model}

##### ModelsExpand Collapse

class Model:

Describes an OpenAI model offering that can be used with the API.

String id

The model identifier, which can be referenced in the API endpoints.

long created

The Unix timestamp (in seconds) when the model was created.

formatunixtime

JsonValue; object\_ "model"constant"model"constant

The object type, which is always “model”.

String ownedBy

The organization that owns the model.

class ModelDeleted:

String id

boolean deleted

String object\_
