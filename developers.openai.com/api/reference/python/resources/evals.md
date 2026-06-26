<!-- source: https://developers.openai.com/api/reference/python/resources/evals/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Evals

Manage and run evals in the OpenAI platform.

##### [List evals](/api/reference/python/resources/evals/methods/list)

evals.list(EvalListParams\*\*kwargs)  -> SyncCursorPage[[EvalListResponse](/api/reference/python/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_list_response%20%3E%20(schema))]

GET/evals

##### [Create eval](/api/reference/python/resources/evals/methods/create)

evals.create(EvalCreateParams\*\*kwargs)  -> [EvalCreateResponse](/api/reference/python/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_create_response%20%3E%20(schema))

POST/evals

##### [Get an eval](/api/reference/python/resources/evals/methods/retrieve)

evals.retrieve(streval\_id)  -> [EvalRetrieveResponse](/api/reference/python/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_retrieve_response%20%3E%20(schema))

GET/evals/{eval\_id}

##### [Update an eval](/api/reference/python/resources/evals/methods/update)

evals.update(streval\_id, EvalUpdateParams\*\*kwargs)  -> [EvalUpdateResponse](/api/reference/python/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_update_response%20%3E%20(schema))

POST/evals/{eval\_id}

##### [Delete an eval](/api/reference/python/resources/evals/methods/delete)

evals.delete(streval\_id)  -> [EvalDeleteResponse](/api/reference/python/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema))

DELETE/evals/{eval\_id}

##### ModelsExpand Collapse

class EvalCustomDataSourceConfig: …

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["custom"]

The type of data source. Always `custom`.

class EvalStoredCompletionsDataSourceConfig: …

Deprecated in favor of LogsDataSourceConfig.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["stored\_completions"]

The type of data source. Always `stored_completions`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalListResponse: …

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

* Improve the quality of my chatbot
* See how well my chatbot handles customer support
* Check if o4-mini is better at my usecase than gpt-4o

id: str

Unique identifier for the evaluation.

created\_at: int

The Unix timestamp (in seconds) for when the eval was created.

formatunixtime

data\_source\_config: DataSourceConfig

Configuration of data sources used in runs of the evaluation.

One of the following:

class EvalCustomDataSourceConfig: …

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["custom"]

The type of data source. Always `custom`.

class DataSourceConfigLogs: …

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["logs"]

The type of data source. Always `logs`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalStoredCompletionsDataSourceConfig: …

Deprecated in favor of LogsDataSourceConfig.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["stored\_completions"]

The type of data source. Always `stored_completions`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: str

The name of the evaluation.

object: Literal["eval"]

The object type.

testing\_criteria: List[TestingCriterion]

A list of testing criteria.

One of the following:

class LabelModelGrader: …

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input: List[Input]

content: InputContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

labels: List[str]

The labels to assign to each item in the evaluation.

model: str

The model to use for the evaluation. Must support structured outputs.

name: str

The name of the grader.

passing\_labels: List[str]

The labels that indicate a passing result. Must be a subset of labels.

type: Literal["label\_model"]

The object type, which is always `label_model`.

class StringCheckGrader: …

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: str

The input text. This may include template strings.

name: str

The name of the grader.

operation: Literal["eq", "ne", "like", "ilike"]

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

"ne"

"like"

"ilike"

reference: str

The reference text. This may include template strings.

type: Literal["string\_check"]

The object type, which is always `string_check`.

class TestingCriterionEvalGraderTextSimilarity: …

A TextSimilarityGrader object which grades text based on similarity metrics.

pass\_threshold: float

The threshold for the score.

class TestingCriterionEvalGraderPython: …

A PythonGrader object that runs a python script on the input.

pass\_threshold: Optional[float]

The threshold for the score.

class TestingCriterionEvalGraderScoreModel: …

A ScoreModelGrader object that uses a model to assign a score to the input.

pass\_threshold: Optional[float]

The threshold for the score.

class EvalCreateResponse: …

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

* Improve the quality of my chatbot
* See how well my chatbot handles customer support
* Check if o4-mini is better at my usecase than gpt-4o

id: str

Unique identifier for the evaluation.

created\_at: int

The Unix timestamp (in seconds) for when the eval was created.

formatunixtime

data\_source\_config: DataSourceConfig

Configuration of data sources used in runs of the evaluation.

One of the following:

class EvalCustomDataSourceConfig: …

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["custom"]

The type of data source. Always `custom`.

class DataSourceConfigLogs: …

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["logs"]

The type of data source. Always `logs`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalStoredCompletionsDataSourceConfig: …

Deprecated in favor of LogsDataSourceConfig.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["stored\_completions"]

The type of data source. Always `stored_completions`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: str

The name of the evaluation.

object: Literal["eval"]

The object type.

testing\_criteria: List[TestingCriterion]

A list of testing criteria.

One of the following:

class LabelModelGrader: …

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input: List[Input]

content: InputContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

labels: List[str]

The labels to assign to each item in the evaluation.

model: str

The model to use for the evaluation. Must support structured outputs.

name: str

The name of the grader.

passing\_labels: List[str]

The labels that indicate a passing result. Must be a subset of labels.

type: Literal["label\_model"]

The object type, which is always `label_model`.

class StringCheckGrader: …

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: str

The input text. This may include template strings.

name: str

The name of the grader.

operation: Literal["eq", "ne", "like", "ilike"]

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

"ne"

"like"

"ilike"

reference: str

The reference text. This may include template strings.

type: Literal["string\_check"]

The object type, which is always `string_check`.

class TestingCriterionEvalGraderTextSimilarity: …

A TextSimilarityGrader object which grades text based on similarity metrics.

pass\_threshold: float

The threshold for the score.

class TestingCriterionEvalGraderPython: …

A PythonGrader object that runs a python script on the input.

pass\_threshold: Optional[float]

The threshold for the score.

class TestingCriterionEvalGraderScoreModel: …

A ScoreModelGrader object that uses a model to assign a score to the input.

pass\_threshold: Optional[float]

The threshold for the score.

class EvalRetrieveResponse: …

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

* Improve the quality of my chatbot
* See how well my chatbot handles customer support
* Check if o4-mini is better at my usecase than gpt-4o

id: str

Unique identifier for the evaluation.

created\_at: int

The Unix timestamp (in seconds) for when the eval was created.

formatunixtime

data\_source\_config: DataSourceConfig

Configuration of data sources used in runs of the evaluation.

One of the following:

class EvalCustomDataSourceConfig: …

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["custom"]

The type of data source. Always `custom`.

class DataSourceConfigLogs: …

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["logs"]

The type of data source. Always `logs`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalStoredCompletionsDataSourceConfig: …

Deprecated in favor of LogsDataSourceConfig.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["stored\_completions"]

The type of data source. Always `stored_completions`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: str

The name of the evaluation.

object: Literal["eval"]

The object type.

testing\_criteria: List[TestingCriterion]

A list of testing criteria.

One of the following:

class LabelModelGrader: …

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input: List[Input]

content: InputContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

labels: List[str]

The labels to assign to each item in the evaluation.

model: str

The model to use for the evaluation. Must support structured outputs.

name: str

The name of the grader.

passing\_labels: List[str]

The labels that indicate a passing result. Must be a subset of labels.

type: Literal["label\_model"]

The object type, which is always `label_model`.

class StringCheckGrader: …

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: str

The input text. This may include template strings.

name: str

The name of the grader.

operation: Literal["eq", "ne", "like", "ilike"]

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

"ne"

"like"

"ilike"

reference: str

The reference text. This may include template strings.

type: Literal["string\_check"]

The object type, which is always `string_check`.

class TestingCriterionEvalGraderTextSimilarity: …

A TextSimilarityGrader object which grades text based on similarity metrics.

pass\_threshold: float

The threshold for the score.

class TestingCriterionEvalGraderPython: …

A PythonGrader object that runs a python script on the input.

pass\_threshold: Optional[float]

The threshold for the score.

class TestingCriterionEvalGraderScoreModel: …

A ScoreModelGrader object that uses a model to assign a score to the input.

pass\_threshold: Optional[float]

The threshold for the score.

class EvalUpdateResponse: …

An Eval object with a data source config and testing criteria.
An Eval represents a task to be done for your LLM integration.
Like:

* Improve the quality of my chatbot
* See how well my chatbot handles customer support
* Check if o4-mini is better at my usecase than gpt-4o

id: str

Unique identifier for the evaluation.

created\_at: int

The Unix timestamp (in seconds) for when the eval was created.

formatunixtime

data\_source\_config: DataSourceConfig

Configuration of data sources used in runs of the evaluation.

One of the following:

class EvalCustomDataSourceConfig: …

A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
The response schema defines the shape of the data that will be:

* Used to define your testing criteria and
* What data is required when creating a run

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["custom"]

The type of data source. Always `custom`.

class DataSourceConfigLogs: …

A LogsDataSourceConfig which specifies the metadata property of your logs query.
This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
The schema returned by this data source config is used to defined what variables are available in your evals.
`item` and `sample` are both defined when using this data source config.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["logs"]

The type of data source. Always `logs`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

class EvalStoredCompletionsDataSourceConfig: …

Deprecated in favor of LogsDataSourceConfig.

schema: Dict[str, object]

The json schema for the run data source items.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["stored\_completions"]

The type of data source. Always `stored_completions`.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: str

The name of the evaluation.

object: Literal["eval"]

The object type.

testing\_criteria: List[TestingCriterion]

A list of testing criteria.

One of the following:

class LabelModelGrader: …

A LabelModelGrader object which uses a model to assign labels to each item
in the evaluation.

input: List[Input]

content: InputContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

labels: List[str]

The labels to assign to each item in the evaluation.

model: str

The model to use for the evaluation. Must support structured outputs.

name: str

The name of the grader.

passing\_labels: List[str]

The labels that indicate a passing result. Must be a subset of labels.

type: Literal["label\_model"]

The object type, which is always `label_model`.

class StringCheckGrader: …

A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

input: str

The input text. This may include template strings.

name: str

The name of the grader.

operation: Literal["eq", "ne", "like", "ilike"]

The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

One of the following:

"eq"

"ne"

"like"

"ilike"

reference: str

The reference text. This may include template strings.

type: Literal["string\_check"]

The object type, which is always `string_check`.

class TestingCriterionEvalGraderTextSimilarity: …

A TextSimilarityGrader object which grades text based on similarity metrics.

pass\_threshold: float

The threshold for the score.

class TestingCriterionEvalGraderPython: …

A PythonGrader object that runs a python script on the input.

pass\_threshold: Optional[float]

The threshold for the score.

class TestingCriterionEvalGraderScoreModel: …

A ScoreModelGrader object that uses a model to assign a score to the input.

pass\_threshold: Optional[float]

The threshold for the score.

class EvalDeleteResponse: …

deleted: bool

eval\_id: str

object: str

#### EvalsRuns

Manage and run evals in the OpenAI platform.

##### [Get eval runs](/api/reference/python/resources/evals/subresources/runs/methods/list)

evals.runs.list(streval\_id, RunListParams\*\*kwargs)  -> SyncCursorPage[[RunListResponse](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema))]

GET/evals/{eval\_id}/runs

##### [Create eval run](/api/reference/python/resources/evals/subresources/runs/methods/create)

evals.runs.create(streval\_id, RunCreateParams\*\*kwargs)  -> [RunCreateResponse](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_create_response%20%3E%20(schema))

POST/evals/{eval\_id}/runs

##### [Get an eval run](/api/reference/python/resources/evals/subresources/runs/methods/retrieve)

evals.runs.retrieve(strrun\_id, RunRetrieveParams\*\*kwargs)  -> [RunRetrieveResponse](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_retrieve_response%20%3E%20(schema))

GET/evals/{eval\_id}/runs/{run\_id}

##### [Cancel eval run](/api/reference/python/resources/evals/subresources/runs/methods/cancel)

evals.runs.cancel(strrun\_id, RunCancelParams\*\*kwargs)  -> [RunCancelResponse](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema))

POST/evals/{eval\_id}/runs/{run\_id}

##### [Delete eval run](/api/reference/python/resources/evals/subresources/runs/methods/delete)

evals.runs.delete(strrun\_id, RunDeleteParams\*\*kwargs)  -> [RunDeleteResponse](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_delete_response%20%3E%20(schema))

DELETE/evals/{eval\_id}/runs/{run\_id}

##### ModelsExpand Collapse

class CreateEvalCompletionsRunDataSource: …

A CompletionsRunDataSource object describing a model sampling configuration.

source: Source

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class SourceStoredCompletions: …

A StoredCompletionsRunDataSource configuration describing a set of filters

type: Literal["stored\_completions"]

The type of source. Always `stored_completions`.

created\_after: Optional[int]

An optional Unix timestamp to filter items created after this time.

created\_before: Optional[int]

An optional Unix timestamp to filter items created before this time.

limit: Optional[int]

An optional maximum number of items to return.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[str]

An optional model to filter by (e.g., ‘gpt-4o’).

type: Literal["completions"]

The type of run data source. Always `completions`.

input\_messages: Optional[InputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class InputMessagesTemplate: …

template: List[InputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [ResponseInputMessageContentList](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

str

A text input to the model.

List[[ResponseInputContent](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))]

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class InputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: InputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class InputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[SamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format: Optional[SamplingParamsResponseFormat]

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

tools: Optional[List[[ChatCompletionFunctionTool](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))]]

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class CreateEvalJSONLRunDataSource: …

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: Source

Determines what populates the `item` namespace in the data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

type: Literal["jsonl"]

The type of data source. Always `jsonl`.

class EvalAPIError: …

An object representing an error response from the Eval API.

code: str

The error code.

message: str

The error message.

class RunListResponse: …

A schema representing an evaluation run.

id: str

Unique identifier for the evaluation run.

created\_at: int

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: DataSource

Information about the run’s data source.

One of the following:

class CreateEvalJSONLRunDataSource: …

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: Source

Determines what populates the `item` namespace in the data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

type: Literal["jsonl"]

The type of data source. Always `jsonl`.

class CreateEvalCompletionsRunDataSource: …

A CompletionsRunDataSource object describing a model sampling configuration.

source: Source

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class SourceStoredCompletions: …

A StoredCompletionsRunDataSource configuration describing a set of filters

type: Literal["stored\_completions"]

The type of source. Always `stored_completions`.

created\_after: Optional[int]

An optional Unix timestamp to filter items created after this time.

created\_before: Optional[int]

An optional Unix timestamp to filter items created before this time.

limit: Optional[int]

An optional maximum number of items to return.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[str]

An optional model to filter by (e.g., ‘gpt-4o’).

type: Literal["completions"]

The type of run data source. Always `completions`.

input\_messages: Optional[InputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class InputMessagesTemplate: …

template: List[InputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [ResponseInputMessageContentList](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

str

A text input to the model.

List[[ResponseInputContent](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))]

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class InputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: InputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class InputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[SamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format: Optional[SamplingParamsResponseFormat]

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

tools: Optional[List[[ChatCompletionFunctionTool](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))]]

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class DataSourceResponses: …

A ResponsesRunDataSource object describing a model sampling configuration.

source: DataSourceResponsesSource

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class DataSourceResponsesSourceFileContent: …

content: List[DataSourceResponsesSourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class DataSourceResponsesSourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class DataSourceResponsesSourceResponses: …

A EvalResponsesSource object describing a run data source configuration.

type: Literal["responses"]

The type of run data source. Always `responses`.

created\_after: Optional[int]

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before: Optional[int]

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search: Optional[str]

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata: Optional[object]

Metadata filter for the responses. This is a query parameter used to select responses.

model: Optional[str]

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature: Optional[float]

Sampling temperature. This is a query parameter used to select responses.

tools: Optional[List[str]]

List of tool names. This is a query parameter used to select responses.

top\_p: Optional[float]

Nucleus sampling parameter. This is a query parameter used to select responses.

users: Optional[List[str]]

List of user identifiers. This is a query parameter used to select responses.

type: Literal["responses"]

The type of run data source. Always `responses`.

input\_messages: Optional[DataSourceResponsesInputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class DataSourceResponsesInputMessagesTemplate: …

template: List[DataSourceResponsesInputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class DataSourceResponsesInputMessagesTemplateTemplateChatMessage: …

content: str

The content of the message.

role: str

The role of the message (e.g. “system”, “assistant”, “user”).

class DataSourceResponsesInputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: DataSourceResponsesInputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class DataSourceResponsesInputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.name”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[DataSourceResponsesSamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

text: Optional[DataSourceResponsesSamplingParamsText]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[ResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools: Optional[List[[Tool](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]]

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

class FunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether to enforce strict parameter validation. Default `true`.

type: Literal["function"]

The type of the function tool. Always `function`.

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

class CompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[Filter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results: Optional[int]

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: Optional[RankingOptions]

Ranking options for search.

hybrid\_search: Optional[RankingOptionsHybridSearch]

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: float

The weight of the text in the reciprocal ranking fusion.

ranker: Optional[Literal["auto", "default-2024-11-15"]]

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

Filters for the search.

allowed\_domains: Optional[List[str]]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The approximate location of the user.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: Optional[Literal["approximate"]]

The type of location approximation. Always `approximate`.

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

A label for this MCP server, used to identify it in tool calls.

type: Literal["mcp"]

The type of the MCP tool. Always `mcp`.

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

One of the following:

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

authorization: Optional[str]

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

Whether this MCP tool is deferred and discovered via tool search.

headers: Optional[Dict[str, str]]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: Optional[McpRequireApproval]

Specify which of the MCP server’s tools require approval.

One of the following:

class McpRequireApprovalMcpToolApprovalFilter: …

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

"always"

"never"

server\_description: Optional[str]

Optional description of the MCP server, used to provide more context.

server\_url: Optional[str]

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: Optional[str]

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: Literal["auto"]

Always `auto`.

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: Optional[str]

File ID for the mask image.

image\_url: Optional[str]

Base64-encoded mask image.

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

environment: Optional[Environment]

One of the following:

class ContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Optional[List[Skill]]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [InlineSkillSource](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

type: Literal["inline"]

Defines an inline skill for this request.

class LocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[LocalSkill](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class ContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

One of the following:

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

parameters: Optional[object]

strict: Optional[bool]

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class ToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

One of the following:

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The user’s location.

type: Literal["approximate"]

The type of location approximation. Always `approximate`.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

An object representing an error response from the Eval API.

eval\_id: str

The identifier of the associated evaluation.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that is evaluated, if applicable.

name: str

The name of the evaluation run.

object: Literal["eval.run"]

The type of the object. Always “eval.run”.

per\_model\_usage: List[PerModelUsage]

Usage statistics for each model during the evaluation run.

cached\_tokens: int

The number of tokens retrieved from cache.

completion\_tokens: int

The number of completion tokens generated.

invocation\_count: int

The number of invocations.

model\_name: str

The name of the model.

prompt\_tokens: int

The number of prompt tokens used.

total\_tokens: int

The total number of tokens used.

per\_testing\_criteria\_results: List[PerTestingCriteriaResult]

Results per testing criteria applied during the evaluation run.

failed: int

Number of tests failed for this criteria.

passed: int

Number of tests passed for this criteria.

testing\_criteria: str

A description of the testing criteria.

report\_url: str

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts

Counters summarizing the outcomes of the evaluation run.

errored: int

Number of output items that resulted in an error.

failed: int

Number of output items that failed to pass the evaluation.

passed: int

Number of output items that passed the evaluation.

total: int

Total number of executed output items.

status: str

The status of the evaluation run.

class RunCreateResponse: …

A schema representing an evaluation run.

id: str

Unique identifier for the evaluation run.

created\_at: int

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: DataSource

Information about the run’s data source.

One of the following:

class CreateEvalJSONLRunDataSource: …

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: Source

Determines what populates the `item` namespace in the data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

type: Literal["jsonl"]

The type of data source. Always `jsonl`.

class CreateEvalCompletionsRunDataSource: …

A CompletionsRunDataSource object describing a model sampling configuration.

source: Source

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class SourceStoredCompletions: …

A StoredCompletionsRunDataSource configuration describing a set of filters

type: Literal["stored\_completions"]

The type of source. Always `stored_completions`.

created\_after: Optional[int]

An optional Unix timestamp to filter items created after this time.

created\_before: Optional[int]

An optional Unix timestamp to filter items created before this time.

limit: Optional[int]

An optional maximum number of items to return.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[str]

An optional model to filter by (e.g., ‘gpt-4o’).

type: Literal["completions"]

The type of run data source. Always `completions`.

input\_messages: Optional[InputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class InputMessagesTemplate: …

template: List[InputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [ResponseInputMessageContentList](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

str

A text input to the model.

List[[ResponseInputContent](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))]

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class InputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: InputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class InputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[SamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format: Optional[SamplingParamsResponseFormat]

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

tools: Optional[List[[ChatCompletionFunctionTool](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))]]

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class DataSourceResponses: …

A ResponsesRunDataSource object describing a model sampling configuration.

source: DataSourceResponsesSource

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class DataSourceResponsesSourceFileContent: …

content: List[DataSourceResponsesSourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class DataSourceResponsesSourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class DataSourceResponsesSourceResponses: …

A EvalResponsesSource object describing a run data source configuration.

type: Literal["responses"]

The type of run data source. Always `responses`.

created\_after: Optional[int]

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before: Optional[int]

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search: Optional[str]

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata: Optional[object]

Metadata filter for the responses. This is a query parameter used to select responses.

model: Optional[str]

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature: Optional[float]

Sampling temperature. This is a query parameter used to select responses.

tools: Optional[List[str]]

List of tool names. This is a query parameter used to select responses.

top\_p: Optional[float]

Nucleus sampling parameter. This is a query parameter used to select responses.

users: Optional[List[str]]

List of user identifiers. This is a query parameter used to select responses.

type: Literal["responses"]

The type of run data source. Always `responses`.

input\_messages: Optional[DataSourceResponsesInputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class DataSourceResponsesInputMessagesTemplate: …

template: List[DataSourceResponsesInputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class DataSourceResponsesInputMessagesTemplateTemplateChatMessage: …

content: str

The content of the message.

role: str

The role of the message (e.g. “system”, “assistant”, “user”).

class DataSourceResponsesInputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: DataSourceResponsesInputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class DataSourceResponsesInputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.name”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[DataSourceResponsesSamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

text: Optional[DataSourceResponsesSamplingParamsText]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[ResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools: Optional[List[[Tool](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]]

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

class FunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether to enforce strict parameter validation. Default `true`.

type: Literal["function"]

The type of the function tool. Always `function`.

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

class CompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[Filter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results: Optional[int]

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: Optional[RankingOptions]

Ranking options for search.

hybrid\_search: Optional[RankingOptionsHybridSearch]

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: float

The weight of the text in the reciprocal ranking fusion.

ranker: Optional[Literal["auto", "default-2024-11-15"]]

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

Filters for the search.

allowed\_domains: Optional[List[str]]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The approximate location of the user.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: Optional[Literal["approximate"]]

The type of location approximation. Always `approximate`.

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

A label for this MCP server, used to identify it in tool calls.

type: Literal["mcp"]

The type of the MCP tool. Always `mcp`.

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

One of the following:

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

authorization: Optional[str]

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

Whether this MCP tool is deferred and discovered via tool search.

headers: Optional[Dict[str, str]]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: Optional[McpRequireApproval]

Specify which of the MCP server’s tools require approval.

One of the following:

class McpRequireApprovalMcpToolApprovalFilter: …

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

"always"

"never"

server\_description: Optional[str]

Optional description of the MCP server, used to provide more context.

server\_url: Optional[str]

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: Optional[str]

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: Literal["auto"]

Always `auto`.

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: Optional[str]

File ID for the mask image.

image\_url: Optional[str]

Base64-encoded mask image.

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

environment: Optional[Environment]

One of the following:

class ContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Optional[List[Skill]]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [InlineSkillSource](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

type: Literal["inline"]

Defines an inline skill for this request.

class LocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[LocalSkill](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class ContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

One of the following:

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

parameters: Optional[object]

strict: Optional[bool]

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class ToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

One of the following:

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The user’s location.

type: Literal["approximate"]

The type of location approximation. Always `approximate`.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

An object representing an error response from the Eval API.

eval\_id: str

The identifier of the associated evaluation.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that is evaluated, if applicable.

name: str

The name of the evaluation run.

object: Literal["eval.run"]

The type of the object. Always “eval.run”.

per\_model\_usage: List[PerModelUsage]

Usage statistics for each model during the evaluation run.

cached\_tokens: int

The number of tokens retrieved from cache.

completion\_tokens: int

The number of completion tokens generated.

invocation\_count: int

The number of invocations.

model\_name: str

The name of the model.

prompt\_tokens: int

The number of prompt tokens used.

total\_tokens: int

The total number of tokens used.

per\_testing\_criteria\_results: List[PerTestingCriteriaResult]

Results per testing criteria applied during the evaluation run.

failed: int

Number of tests failed for this criteria.

passed: int

Number of tests passed for this criteria.

testing\_criteria: str

A description of the testing criteria.

report\_url: str

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts

Counters summarizing the outcomes of the evaluation run.

errored: int

Number of output items that resulted in an error.

failed: int

Number of output items that failed to pass the evaluation.

passed: int

Number of output items that passed the evaluation.

total: int

Total number of executed output items.

status: str

The status of the evaluation run.

class RunRetrieveResponse: …

A schema representing an evaluation run.

id: str

Unique identifier for the evaluation run.

created\_at: int

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: DataSource

Information about the run’s data source.

One of the following:

class CreateEvalJSONLRunDataSource: …

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: Source

Determines what populates the `item` namespace in the data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

type: Literal["jsonl"]

The type of data source. Always `jsonl`.

class CreateEvalCompletionsRunDataSource: …

A CompletionsRunDataSource object describing a model sampling configuration.

source: Source

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class SourceStoredCompletions: …

A StoredCompletionsRunDataSource configuration describing a set of filters

type: Literal["stored\_completions"]

The type of source. Always `stored_completions`.

created\_after: Optional[int]

An optional Unix timestamp to filter items created after this time.

created\_before: Optional[int]

An optional Unix timestamp to filter items created before this time.

limit: Optional[int]

An optional maximum number of items to return.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[str]

An optional model to filter by (e.g., ‘gpt-4o’).

type: Literal["completions"]

The type of run data source. Always `completions`.

input\_messages: Optional[InputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class InputMessagesTemplate: …

template: List[InputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [ResponseInputMessageContentList](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

str

A text input to the model.

List[[ResponseInputContent](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))]

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class InputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: InputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class InputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[SamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format: Optional[SamplingParamsResponseFormat]

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

tools: Optional[List[[ChatCompletionFunctionTool](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))]]

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class DataSourceResponses: …

A ResponsesRunDataSource object describing a model sampling configuration.

source: DataSourceResponsesSource

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class DataSourceResponsesSourceFileContent: …

content: List[DataSourceResponsesSourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class DataSourceResponsesSourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class DataSourceResponsesSourceResponses: …

A EvalResponsesSource object describing a run data source configuration.

type: Literal["responses"]

The type of run data source. Always `responses`.

created\_after: Optional[int]

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before: Optional[int]

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search: Optional[str]

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata: Optional[object]

Metadata filter for the responses. This is a query parameter used to select responses.

model: Optional[str]

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature: Optional[float]

Sampling temperature. This is a query parameter used to select responses.

tools: Optional[List[str]]

List of tool names. This is a query parameter used to select responses.

top\_p: Optional[float]

Nucleus sampling parameter. This is a query parameter used to select responses.

users: Optional[List[str]]

List of user identifiers. This is a query parameter used to select responses.

type: Literal["responses"]

The type of run data source. Always `responses`.

input\_messages: Optional[DataSourceResponsesInputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class DataSourceResponsesInputMessagesTemplate: …

template: List[DataSourceResponsesInputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class DataSourceResponsesInputMessagesTemplateTemplateChatMessage: …

content: str

The content of the message.

role: str

The role of the message (e.g. “system”, “assistant”, “user”).

class DataSourceResponsesInputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: DataSourceResponsesInputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class DataSourceResponsesInputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.name”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[DataSourceResponsesSamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

text: Optional[DataSourceResponsesSamplingParamsText]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[ResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools: Optional[List[[Tool](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]]

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

class FunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether to enforce strict parameter validation. Default `true`.

type: Literal["function"]

The type of the function tool. Always `function`.

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

class CompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[Filter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results: Optional[int]

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: Optional[RankingOptions]

Ranking options for search.

hybrid\_search: Optional[RankingOptionsHybridSearch]

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: float

The weight of the text in the reciprocal ranking fusion.

ranker: Optional[Literal["auto", "default-2024-11-15"]]

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

Filters for the search.

allowed\_domains: Optional[List[str]]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The approximate location of the user.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: Optional[Literal["approximate"]]

The type of location approximation. Always `approximate`.

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

A label for this MCP server, used to identify it in tool calls.

type: Literal["mcp"]

The type of the MCP tool. Always `mcp`.

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

One of the following:

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

authorization: Optional[str]

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

Whether this MCP tool is deferred and discovered via tool search.

headers: Optional[Dict[str, str]]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: Optional[McpRequireApproval]

Specify which of the MCP server’s tools require approval.

One of the following:

class McpRequireApprovalMcpToolApprovalFilter: …

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

"always"

"never"

server\_description: Optional[str]

Optional description of the MCP server, used to provide more context.

server\_url: Optional[str]

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: Optional[str]

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: Literal["auto"]

Always `auto`.

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: Optional[str]

File ID for the mask image.

image\_url: Optional[str]

Base64-encoded mask image.

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

environment: Optional[Environment]

One of the following:

class ContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Optional[List[Skill]]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [InlineSkillSource](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

type: Literal["inline"]

Defines an inline skill for this request.

class LocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[LocalSkill](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class ContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

One of the following:

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

parameters: Optional[object]

strict: Optional[bool]

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class ToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

One of the following:

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The user’s location.

type: Literal["approximate"]

The type of location approximation. Always `approximate`.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

An object representing an error response from the Eval API.

eval\_id: str

The identifier of the associated evaluation.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that is evaluated, if applicable.

name: str

The name of the evaluation run.

object: Literal["eval.run"]

The type of the object. Always “eval.run”.

per\_model\_usage: List[PerModelUsage]

Usage statistics for each model during the evaluation run.

cached\_tokens: int

The number of tokens retrieved from cache.

completion\_tokens: int

The number of completion tokens generated.

invocation\_count: int

The number of invocations.

model\_name: str

The name of the model.

prompt\_tokens: int

The number of prompt tokens used.

total\_tokens: int

The total number of tokens used.

per\_testing\_criteria\_results: List[PerTestingCriteriaResult]

Results per testing criteria applied during the evaluation run.

failed: int

Number of tests failed for this criteria.

passed: int

Number of tests passed for this criteria.

testing\_criteria: str

A description of the testing criteria.

report\_url: str

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts

Counters summarizing the outcomes of the evaluation run.

errored: int

Number of output items that resulted in an error.

failed: int

Number of output items that failed to pass the evaluation.

passed: int

Number of output items that passed the evaluation.

total: int

Total number of executed output items.

status: str

The status of the evaluation run.

class RunCancelResponse: …

A schema representing an evaluation run.

id: str

Unique identifier for the evaluation run.

created\_at: int

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: DataSource

Information about the run’s data source.

One of the following:

class CreateEvalJSONLRunDataSource: …

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: Source

Determines what populates the `item` namespace in the data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

type: Literal["jsonl"]

The type of data source. Always `jsonl`.

class CreateEvalCompletionsRunDataSource: …

A CompletionsRunDataSource object describing a model sampling configuration.

source: Source

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class SourceFileContent: …

content: List[SourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class SourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class SourceStoredCompletions: …

A StoredCompletionsRunDataSource configuration describing a set of filters

type: Literal["stored\_completions"]

The type of source. Always `stored_completions`.

created\_after: Optional[int]

An optional Unix timestamp to filter items created after this time.

created\_before: Optional[int]

An optional Unix timestamp to filter items created before this time.

limit: Optional[int]

An optional maximum number of items to return.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[str]

An optional model to filter by (e.g., ‘gpt-4o’).

type: Literal["completions"]

The type of run data source. Always `completions`.

input\_messages: Optional[InputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class InputMessagesTemplate: …

template: List[InputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [ResponseInputMessageContentList](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

str

A text input to the model.

List[[ResponseInputContent](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))]

One of the following:

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class ResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

The type of the input item. Always `input_image`.

file\_id: Optional[str]

The ID of the file to be sent to the model.

image\_url: Optional[str]

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile: …

A file input to the model.

type: Literal["input\_file"]

The type of the input item. Always `input_file`.

detail: Optional[Literal["low", "high"]]

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data: Optional[str]

The content of the file to be sent to the model.

file\_id: Optional[str]

The ID of the file to be sent to the model.

file\_url: Optional[str]

The URL of the file to be sent to the model.

formaturi

filename: Optional[str]

The name of the file to be sent to the model.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class InputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: InputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class InputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class InputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class InputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[SamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format: Optional[SamplingParamsResponseFormat]

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

tools: Optional[List[[ChatCompletionFunctionTool](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))]]

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class DataSourceResponses: …

A ResponsesRunDataSource object describing a model sampling configuration.

source: DataSourceResponsesSource

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class DataSourceResponsesSourceFileContent: …

content: List[DataSourceResponsesSourceFileContentContent]

The content of the jsonl file.

item: Dict[str, object]

sample: Optional[Dict[str, object]]

type: Literal["file\_content"]

The type of jsonl source. Always `file_content`.

class DataSourceResponsesSourceFileID: …

id: str

The identifier of the file.

type: Literal["file\_id"]

The type of jsonl source. Always `file_id`.

class DataSourceResponsesSourceResponses: …

A EvalResponsesSource object describing a run data source configuration.

type: Literal["responses"]

The type of run data source. Always `responses`.

created\_after: Optional[int]

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before: Optional[int]

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search: Optional[str]

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata: Optional[object]

Metadata filter for the responses. This is a query parameter used to select responses.

model: Optional[str]

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature: Optional[float]

Sampling temperature. This is a query parameter used to select responses.

tools: Optional[List[str]]

List of tool names. This is a query parameter used to select responses.

top\_p: Optional[float]

Nucleus sampling parameter. This is a query parameter used to select responses.

users: Optional[List[str]]

List of user identifiers. This is a query parameter used to select responses.

type: Literal["responses"]

The type of run data source. Always `responses`.

input\_messages: Optional[DataSourceResponsesInputMessages]

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class DataSourceResponsesInputMessagesTemplate: …

template: List[DataSourceResponsesInputMessagesTemplateTemplate]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class DataSourceResponsesInputMessagesTemplateTemplateChatMessage: …

content: str

The content of the message.

role: str

The role of the message (e.g. “system”, “assistant”, “user”).

class DataSourceResponsesInputMessagesTemplateTemplateEvalItem: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: DataSourceResponsesInputMessagesTemplateTemplateEvalItemContent

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class DataSourceResponsesInputMessagesTemplateTemplateEvalItemContentInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

List[GraderInputItem]

One of the following:

str

A text input to the model.

class ResponseInputText: …

A text input to the model.

text: str

The text input to the model.

type: Literal["input\_text"]

The type of the input item. Always `input_text`.

class GraderInputItemOutputText: …

A text output from the model.

text: str

The text output from the model.

type: Literal["output\_text"]

The type of the output text. Always `output_text`.

class GraderInputItemInputImage: …

An image input block used within EvalItem content arrays.

image\_url: str

The URL of the image input.

formaturi

type: Literal["input\_image"]

The type of the image input. Always `input_image`.

detail: Optional[str]

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

type: Literal["template"]

The type of input messages. Always `template`.

class DataSourceResponsesInputMessagesItemReference: …

item\_reference: str

A reference to a variable in the `item` namespace. Ie, “item.name”

type: Literal["item\_reference"]

The type of input messages. Always `item_reference`.

model: Optional[str]

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: Optional[DataSourceResponsesSamplingParams]

max\_completion\_tokens: Optional[int]

The maximum number of tokens in the generated output.

reasoning\_effort: Optional[ReasoningEffort]

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed: Optional[int]

A seed value to initialize the randomness, during sampling.

temperature: Optional[float]

A higher temperature increases randomness in the outputs.

text: Optional[DataSourceResponsesSamplingParamsText]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[ResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools: Optional[List[[Tool](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]]

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

class FunctionTool: …

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: str

The name of the function to call.

parameters: Optional[Dict[str, object]]

A JSON schema object describing the parameters of the function.

strict: Optional[bool]

Whether to enforce strict parameter validation. Default `true`.

type: Literal["function"]

The type of the function tool. Always `function`.

defer\_loading: Optional[bool]

Whether this function is deferred and loaded via tool search.

description: Optional[str]

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool: …

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: Literal["file\_search"]

The type of the file search tool. Always `file_search`.

vector\_store\_ids: List[str]

The IDs of the vector stores to search.

filters: Optional[Filters]

A filter to apply.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

class CompoundFilter: …

Combine multiple filters using `and` or `or`.

filters: List[Filter]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter: …

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: str

The key to compare against the value.

type: Literal["eq", "ne", "gt", 5 more]

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

str

float

bool

List[Union[str, float]]

One of the following:

str

float

object

type: Literal["and", "or"]

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results: Optional[int]

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: Optional[RankingOptions]

Ranking options for search.

hybrid\_search: Optional[RankingOptionsHybridSearch]

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: float

The weight of the text in the reciprocal ranking fusion.

ranker: Optional[Literal["auto", "default-2024-11-15"]]

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: Literal["computer"]

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool: …

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: int

The height of the computer display.

display\_width: int

The width of the computer display.

environment: Literal["windows", "mac", "linux", 2 more]

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool: …

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

Filters for the search.

allowed\_domains: Optional[List[str]]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The approximate location of the user.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: Optional[Literal["approximate"]]

The type of location approximation. Always `approximate`.

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

A label for this MCP server, used to identify it in tool calls.

type: Literal["mcp"]

The type of the MCP tool. Always `mcp`.

allowed\_tools: Optional[McpAllowedTools]

List of allowed tool names or a filter object.

One of the following:

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

authorization: Optional[str]

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

Whether this MCP tool is deferred and discovered via tool search.

headers: Optional[Dict[str, str]]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: Optional[McpRequireApproval]

Specify which of the MCP server’s tools require approval.

One of the following:

class McpRequireApprovalMcpToolApprovalFilter: …

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

A filter object to specify which tools are allowed.

read\_only: Optional[bool]

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Optional[List[str]]

List of allowed tool names.

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

"always"

"never"

server\_description: Optional[str]

Optional description of the MCP server, used to provide more context.

server\_url: Optional[str]

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: Optional[str]

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: Literal["auto"]

Always `auto`.

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

The type of the image generation tool. Always `image_generation`.

action: Optional[Literal["generate", "edit", "auto"]]

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity: Optional[Literal["high", "low"]]

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: Optional[str]

File ID for the mask image.

image\_url: Optional[str]

Base64-encoded mask image.

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

The image generation model to use. Default: `gpt-image-1`.

One of the following:

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression: Optional[int]

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool: …

A tool that allows the model to execute shell commands.

type: Literal["shell"]

The type of the shell tool. Always `shell`.

environment: Optional[Environment]

One of the following:

class ContainerAuto: …

type: Literal["container\_auto"]

Automatically creates a container for this request

file\_ids: Optional[List[str]]

An optional list of uploaded files to make available to your code.

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

A list of allowed domains when type is `allowlist`.

type: Literal["allowlist"]

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Optional[List[[ContainerNetworkPolicyDomainSecret](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))]]

Optional domain-scoped secrets for allowlisted domains.

domain: str

The domain associated with the secret.

minLength1

name: str

The name of the secret to inject for the domain.

minLength1

value: str

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Optional[List[Skill]]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference: …

skill\_id: str

The ID of the referenced skill.

maxLength64

minLength1

type: Literal["skill\_reference"]

References a skill created with the /v1/skills endpoint.

version: Optional[str]

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill: …

description: str

The description of the skill.

name: str

The name of the skill.

source: [InlineSkillSource](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

type: Literal["inline"]

Defines an inline skill for this request.

class LocalEnvironment: …

type: Literal["local"]

Use a local computer environment.

skills: Optional[List[[LocalSkill](/api/reference/python/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))]]

An optional list of skills.

description: str

The description of the skill.

name: str

The name of the skill.

path: str

The path to the directory containing the skill.

class ContainerReference: …

container\_id: str

The ID of the referenced container.

type: Literal["container\_reference"]

References a container created with the /v1/containers endpoint

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

class NamespaceTool: …

Groups function/custom tools under a shared namespace.

description: str

A description of the namespace shown to the model.

minLength1

name: str

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: List[Tool]

The function/custom tools available inside this namespace.

One of the following:

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

defer\_loading: Optional[bool]

Whether this function should be deferred and discovered via tool search.

description: Optional[str]

parameters: Optional[object]

strict: Optional[bool]

class CustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

The name of the custom tool, used to identify it in tool calls.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

defer\_loading: Optional[bool]

Whether this tool should be deferred and discovered via tool search.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomToolInputFormat]

The input format for the custom tool. Default is unconstrained text.

type: Literal["namespace"]

The type of the tool. Always `namespace`.

class ToolSearchTool: …

Hosted or BYOT tool search configuration for deferred tools.

type: Literal["tool\_search"]

The type of the tool. Always `tool_search`.

description: Optional[str]

Description shown to the model for a client-executed tool search tool.

execution: Optional[Literal["server", "client"]]

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters: Optional[object]

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool: …

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

One of the following:

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

The user’s location.

type: Literal["approximate"]

The type of location approximation. Always `approximate`.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool: …

Allows the assistant to create, delete, or update files using unified diffs.

type: Literal["apply\_patch"]

The type of the tool. Always `apply_patch`.

top\_p: Optional[float]

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

An object representing an error response from the Eval API.

eval\_id: str

The identifier of the associated evaluation.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that is evaluated, if applicable.

name: str

The name of the evaluation run.

object: Literal["eval.run"]

The type of the object. Always “eval.run”.

per\_model\_usage: List[PerModelUsage]

Usage statistics for each model during the evaluation run.

cached\_tokens: int

The number of tokens retrieved from cache.

completion\_tokens: int

The number of completion tokens generated.

invocation\_count: int

The number of invocations.

model\_name: str

The name of the model.

prompt\_tokens: int

The number of prompt tokens used.

total\_tokens: int

The total number of tokens used.

per\_testing\_criteria\_results: List[PerTestingCriteriaResult]

Results per testing criteria applied during the evaluation run.

failed: int

Number of tests failed for this criteria.

passed: int

Number of tests passed for this criteria.

testing\_criteria: str

A description of the testing criteria.

report\_url: str

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts

Counters summarizing the outcomes of the evaluation run.

errored: int

Number of output items that resulted in an error.

failed: int

Number of output items that failed to pass the evaluation.

passed: int

Number of output items that passed the evaluation.

total: int

Total number of executed output items.

status: str

The status of the evaluation run.

class RunDeleteResponse: …

deleted: Optional[bool]

object: Optional[str]

run\_id: Optional[str]

#### EvalsRunsOutput Items

Manage and run evals in the OpenAI platform.

##### [Get eval run output items](/api/reference/python/resources/evals/subresources/runs/subresources/output_items/methods/list)

evals.runs.output\_items.list(strrun\_id, OutputItemListParams\*\*kwargs)  -> SyncCursorPage[[OutputItemListResponse](/api/reference/python/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_list_response%20%3E%20(schema))]

GET/evals/{eval\_id}/runs/{run\_id}/output\_items

##### [Get an output item of an eval run](/api/reference/python/resources/evals/subresources/runs/subresources/output_items/methods/retrieve)

evals.runs.output\_items.retrieve(stroutput\_item\_id, OutputItemRetrieveParams\*\*kwargs)  -> [OutputItemRetrieveResponse](/api/reference/python/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_retrieve_response%20%3E%20(schema))

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}

##### ModelsExpand Collapse

class OutputItemListResponse: …

A schema representing an evaluation run output item.

id: str

Unique identifier for the evaluation run output item.

created\_at: int

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Dict[str, object]

Details of the input data source item.

datasource\_item\_id: int

The identifier for the data source item.

eval\_id: str

The identifier of the evaluation group.

object: Literal["eval.run.output\_item"]

The type of the object. Always “eval.run.output\_item”.

results: List[Result]

A list of grader results for this output item.

name: str

The name of the grader.

passed: bool

Whether the grader considered the output a pass.

score: float

The numeric score produced by the grader.

sample: Optional[Dict[str, object]]

Optional sample or intermediate data produced by the grader.

type: Optional[str]

The grader type (for example, “string-check-grader”).

run\_id: str

The identifier of the evaluation run associated with this output item.

sample: Sample

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

An object representing an error response from the Eval API.

finish\_reason: str

The reason why the sample generation was finished.

input: List[SampleInput]

An array of input messages.

content: str

The content of the message.

role: str

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: int

The maximum number of tokens allowed for completion.

model: str

The model used for generating the sample.

output: List[SampleOutput]

An array of output messages.

content: Optional[str]

The content of the message.

role: Optional[str]

The role of the message (e.g. “system”, “assistant”, “user”).

seed: int

The seed used for generating the sample.

temperature: float

The sampling temperature used.

top\_p: float

The top\_p value used for sampling.

usage: SampleUsage

Token usage details for the sample.

cached\_tokens: int

The number of tokens retrieved from cache.

completion\_tokens: int

The number of completion tokens generated.

prompt\_tokens: int

The number of prompt tokens used.

total\_tokens: int

The total number of tokens used.

status: str

The status of the evaluation run.

class OutputItemRetrieveResponse: …

A schema representing an evaluation run output item.

id: str

Unique identifier for the evaluation run output item.

created\_at: int

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Dict[str, object]

Details of the input data source item.

datasource\_item\_id: int

The identifier for the data source item.

eval\_id: str

The identifier of the evaluation group.

object: Literal["eval.run.output\_item"]

The type of the object. Always “eval.run.output\_item”.

results: List[Result]

A list of grader results for this output item.

name: str

The name of the grader.

passed: bool

Whether the grader considered the output a pass.

score: float

The numeric score produced by the grader.

sample: Optional[Dict[str, object]]

Optional sample or intermediate data produced by the grader.

type: Optional[str]

The grader type (for example, “string-check-grader”).

run\_id: str

The identifier of the evaluation run associated with this output item.

sample: Sample

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema))

An object representing an error response from the Eval API.

finish\_reason: str

The reason why the sample generation was finished.

input: List[SampleInput]

An array of input messages.

content: str

The content of the message.

role: str

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: int

The maximum number of tokens allowed for completion.

model: str

The model used for generating the sample.

output: List[SampleOutput]

An array of output messages.

content: Optional[str]

The content of the message.

role: Optional[str]

The role of the message (e.g. “system”, “assistant”, “user”).

seed: int

The seed used for generating the sample.

temperature: float

The sampling temperature used.

top\_p: float

The top\_p value used for sampling.

usage: SampleUsage

Token usage details for the sample.

cached\_tokens: int

The number of tokens retrieved from cache.

completion\_tokens: int

The number of completion tokens generated.

prompt\_tokens: int

The number of prompt tokens used.

total\_tokens: int

The total number of tokens used.

status: str

The status of the evaluation run.
