<!-- source: https://developers.openai.com/api/reference/java/resources/$shared/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Shared

##### ModelsExpand Collapse

class AllModels: A class that can be one of several variants.union

String

enum ChatModel:

GPT\_5\_4("gpt-5.4")

GPT\_5\_4\_MINI("gpt-5.4-mini")

GPT\_5\_4\_NANO("gpt-5.4-nano")

GPT\_5\_4\_MINI\_2026\_03\_17("gpt-5.4-mini-2026-03-17")

GPT\_5\_4\_NANO\_2026\_03\_17("gpt-5.4-nano-2026-03-17")

GPT\_5\_3\_CHAT\_LATEST("gpt-5.3-chat-latest")

GPT\_5\_2("gpt-5.2")

GPT\_5\_2\_2025\_12\_11("gpt-5.2-2025-12-11")

GPT\_5\_2\_CHAT\_LATEST("gpt-5.2-chat-latest")

GPT\_5\_2\_PRO("gpt-5.2-pro")

GPT\_5\_2\_PRO\_2025\_12\_11("gpt-5.2-pro-2025-12-11")

GPT\_5\_1("gpt-5.1")

GPT\_5\_1\_2025\_11\_13("gpt-5.1-2025-11-13")

GPT\_5\_1\_CODEX("gpt-5.1-codex")

GPT\_5\_1\_MINI("gpt-5.1-mini")

GPT\_5\_1\_CHAT\_LATEST("gpt-5.1-chat-latest")

GPT\_5("gpt-5")

GPT\_5\_MINI("gpt-5-mini")

GPT\_5\_NANO("gpt-5-nano")

GPT\_5\_2025\_08\_07("gpt-5-2025-08-07")

GPT\_5\_MINI\_2025\_08\_07("gpt-5-mini-2025-08-07")

GPT\_5\_NANO\_2025\_08\_07("gpt-5-nano-2025-08-07")

GPT\_5\_CHAT\_LATEST("gpt-5-chat-latest")

GPT\_4\_1("gpt-4.1")

GPT\_4\_1\_MINI("gpt-4.1-mini")

GPT\_4\_1\_NANO("gpt-4.1-nano")

GPT\_4\_1\_2025\_04\_14("gpt-4.1-2025-04-14")

GPT\_4\_1\_MINI\_2025\_04\_14("gpt-4.1-mini-2025-04-14")

GPT\_4\_1\_NANO\_2025\_04\_14("gpt-4.1-nano-2025-04-14")

O4\_MINI("o4-mini")

O4\_MINI\_2025\_04\_16("o4-mini-2025-04-16")

O3("o3")

O3\_2025\_04\_16("o3-2025-04-16")

O3\_MINI("o3-mini")

O3\_MINI\_2025\_01\_31("o3-mini-2025-01-31")

O1("o1")

O1\_2024\_12\_17("o1-2024-12-17")

O1\_PREVIEW("o1-preview")

O1\_PREVIEW\_2024\_09\_12("o1-preview-2024-09-12")

O1\_MINI("o1-mini")

O1\_MINI\_2024\_09\_12("o1-mini-2024-09-12")

GPT\_4O("gpt-4o")

GPT\_4O\_2024\_11\_20("gpt-4o-2024-11-20")

GPT\_4O\_2024\_08\_06("gpt-4o-2024-08-06")

GPT\_4O\_2024\_05\_13("gpt-4o-2024-05-13")

GPT\_4O\_AUDIO\_PREVIEW("gpt-4o-audio-preview")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_10\_01("gpt-4o-audio-preview-2024-10-01")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-audio-preview-2024-12-17")

GPT\_4O\_AUDIO\_PREVIEW\_2025\_06\_03("gpt-4o-audio-preview-2025-06-03")

GPT\_4O\_MINI\_AUDIO\_PREVIEW("gpt-4o-mini-audio-preview")

GPT\_4O\_MINI\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-mini-audio-preview-2024-12-17")

GPT\_4O\_SEARCH\_PREVIEW("gpt-4o-search-preview")

GPT\_4O\_MINI\_SEARCH\_PREVIEW("gpt-4o-mini-search-preview")

GPT\_4O\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-search-preview-2025-03-11")

GPT\_4O\_MINI\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-mini-search-preview-2025-03-11")

CHATGPT\_4O\_LATEST("chatgpt-4o-latest")

CODEX\_MINI\_LATEST("codex-mini-latest")

GPT\_4O\_MINI("gpt-4o-mini")

GPT\_4O\_MINI\_2024\_07\_18("gpt-4o-mini-2024-07-18")

GPT\_4\_TURBO("gpt-4-turbo")

GPT\_4\_TURBO\_2024\_04\_09("gpt-4-turbo-2024-04-09")

GPT\_4\_0125\_PREVIEW("gpt-4-0125-preview")

GPT\_4\_TURBO\_PREVIEW("gpt-4-turbo-preview")

GPT\_4\_1106\_PREVIEW("gpt-4-1106-preview")

GPT\_4\_VISION\_PREVIEW("gpt-4-vision-preview")

GPT\_4("gpt-4")

GPT\_4\_0314("gpt-4-0314")

GPT\_4\_0613("gpt-4-0613")

GPT\_4\_32K("gpt-4-32k")

GPT\_4\_32K\_0314("gpt-4-32k-0314")

GPT\_4\_32K\_0613("gpt-4-32k-0613")

GPT\_3\_5\_TURBO("gpt-3.5-turbo")

GPT\_3\_5\_TURBO\_16K("gpt-3.5-turbo-16k")

GPT\_3\_5\_TURBO\_0301("gpt-3.5-turbo-0301")

GPT\_3\_5\_TURBO\_0613("gpt-3.5-turbo-0613")

GPT\_3\_5\_TURBO\_1106("gpt-3.5-turbo-1106")

GPT\_3\_5\_TURBO\_0125("gpt-3.5-turbo-0125")

GPT\_3\_5\_TURBO\_16K\_0613("gpt-3.5-turbo-16k-0613")

ResponsesOnlyModel

One of the following:

O1\_PRO("o1-pro")

O1\_PRO\_2025\_03\_19("o1-pro-2025-03-19")

O3\_PRO("o3-pro")

O3\_PRO\_2025\_06\_10("o3-pro-2025-06-10")

O3\_DEEP\_RESEARCH("o3-deep-research")

O3\_DEEP\_RESEARCH\_2025\_06\_26("o3-deep-research-2025-06-26")

O4\_MINI\_DEEP\_RESEARCH("o4-mini-deep-research")

O4\_MINI\_DEEP\_RESEARCH\_2025\_06\_26("o4-mini-deep-research-2025-06-26")

COMPUTER\_USE\_PREVIEW("computer-use-preview")

COMPUTER\_USE\_PREVIEW\_2025\_03\_11("computer-use-preview-2025-03-11")

GPT\_5\_CODEX("gpt-5-codex")

GPT\_5\_PRO("gpt-5-pro")

GPT\_5\_PRO\_2025\_10\_06("gpt-5-pro-2025-10-06")

GPT\_5\_1\_CODEX\_MAX("gpt-5.1-codex-max")

enum ChatModel:

GPT\_5\_4("gpt-5.4")

GPT\_5\_4\_MINI("gpt-5.4-mini")

GPT\_5\_4\_NANO("gpt-5.4-nano")

GPT\_5\_4\_MINI\_2026\_03\_17("gpt-5.4-mini-2026-03-17")

GPT\_5\_4\_NANO\_2026\_03\_17("gpt-5.4-nano-2026-03-17")

GPT\_5\_3\_CHAT\_LATEST("gpt-5.3-chat-latest")

GPT\_5\_2("gpt-5.2")

GPT\_5\_2\_2025\_12\_11("gpt-5.2-2025-12-11")

GPT\_5\_2\_CHAT\_LATEST("gpt-5.2-chat-latest")

GPT\_5\_2\_PRO("gpt-5.2-pro")

GPT\_5\_2\_PRO\_2025\_12\_11("gpt-5.2-pro-2025-12-11")

GPT\_5\_1("gpt-5.1")

GPT\_5\_1\_2025\_11\_13("gpt-5.1-2025-11-13")

GPT\_5\_1\_CODEX("gpt-5.1-codex")

GPT\_5\_1\_MINI("gpt-5.1-mini")

GPT\_5\_1\_CHAT\_LATEST("gpt-5.1-chat-latest")

GPT\_5("gpt-5")

GPT\_5\_MINI("gpt-5-mini")

GPT\_5\_NANO("gpt-5-nano")

GPT\_5\_2025\_08\_07("gpt-5-2025-08-07")

GPT\_5\_MINI\_2025\_08\_07("gpt-5-mini-2025-08-07")

GPT\_5\_NANO\_2025\_08\_07("gpt-5-nano-2025-08-07")

GPT\_5\_CHAT\_LATEST("gpt-5-chat-latest")

GPT\_4\_1("gpt-4.1")

GPT\_4\_1\_MINI("gpt-4.1-mini")

GPT\_4\_1\_NANO("gpt-4.1-nano")

GPT\_4\_1\_2025\_04\_14("gpt-4.1-2025-04-14")

GPT\_4\_1\_MINI\_2025\_04\_14("gpt-4.1-mini-2025-04-14")

GPT\_4\_1\_NANO\_2025\_04\_14("gpt-4.1-nano-2025-04-14")

O4\_MINI("o4-mini")

O4\_MINI\_2025\_04\_16("o4-mini-2025-04-16")

O3("o3")

O3\_2025\_04\_16("o3-2025-04-16")

O3\_MINI("o3-mini")

O3\_MINI\_2025\_01\_31("o3-mini-2025-01-31")

O1("o1")

O1\_2024\_12\_17("o1-2024-12-17")

O1\_PREVIEW("o1-preview")

O1\_PREVIEW\_2024\_09\_12("o1-preview-2024-09-12")

O1\_MINI("o1-mini")

O1\_MINI\_2024\_09\_12("o1-mini-2024-09-12")

GPT\_4O("gpt-4o")

GPT\_4O\_2024\_11\_20("gpt-4o-2024-11-20")

GPT\_4O\_2024\_08\_06("gpt-4o-2024-08-06")

GPT\_4O\_2024\_05\_13("gpt-4o-2024-05-13")

GPT\_4O\_AUDIO\_PREVIEW("gpt-4o-audio-preview")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_10\_01("gpt-4o-audio-preview-2024-10-01")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-audio-preview-2024-12-17")

GPT\_4O\_AUDIO\_PREVIEW\_2025\_06\_03("gpt-4o-audio-preview-2025-06-03")

GPT\_4O\_MINI\_AUDIO\_PREVIEW("gpt-4o-mini-audio-preview")

GPT\_4O\_MINI\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-mini-audio-preview-2024-12-17")

GPT\_4O\_SEARCH\_PREVIEW("gpt-4o-search-preview")

GPT\_4O\_MINI\_SEARCH\_PREVIEW("gpt-4o-mini-search-preview")

GPT\_4O\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-search-preview-2025-03-11")

GPT\_4O\_MINI\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-mini-search-preview-2025-03-11")

CHATGPT\_4O\_LATEST("chatgpt-4o-latest")

CODEX\_MINI\_LATEST("codex-mini-latest")

GPT\_4O\_MINI("gpt-4o-mini")

GPT\_4O\_MINI\_2024\_07\_18("gpt-4o-mini-2024-07-18")

GPT\_4\_TURBO("gpt-4-turbo")

GPT\_4\_TURBO\_2024\_04\_09("gpt-4-turbo-2024-04-09")

GPT\_4\_0125\_PREVIEW("gpt-4-0125-preview")

GPT\_4\_TURBO\_PREVIEW("gpt-4-turbo-preview")

GPT\_4\_1106\_PREVIEW("gpt-4-1106-preview")

GPT\_4\_VISION\_PREVIEW("gpt-4-vision-preview")

GPT\_4("gpt-4")

GPT\_4\_0314("gpt-4-0314")

GPT\_4\_0613("gpt-4-0613")

GPT\_4\_32K("gpt-4-32k")

GPT\_4\_32K\_0314("gpt-4-32k-0314")

GPT\_4\_32K\_0613("gpt-4-32k-0613")

GPT\_3\_5\_TURBO("gpt-3.5-turbo")

GPT\_3\_5\_TURBO\_16K("gpt-3.5-turbo-16k")

GPT\_3\_5\_TURBO\_0301("gpt-3.5-turbo-0301")

GPT\_3\_5\_TURBO\_0613("gpt-3.5-turbo-0613")

GPT\_3\_5\_TURBO\_1106("gpt-3.5-turbo-1106")

GPT\_3\_5\_TURBO\_0125("gpt-3.5-turbo-0125")

GPT\_3\_5\_TURBO\_16K\_0613("gpt-3.5-turbo-16k-0613")

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

One of the following:

AND("and")

OR("or")

class CustomToolInputFormat: A class that can be one of several variants.union

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

Grammar

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class ErrorObject:

Optional<String> code

String message

Optional<String> param

String type

class FunctionDefinition:

String name

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

Optional<String> description

A description of what the function does, used by the model to choose when and how to call the function.

Optional<[FunctionParameters](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))> parameters

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

class FunctionParameters:

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

enum OAuthErrorCode:

INVALID\_GRANT("invalid\_grant")

INVALID\_SUBJECT\_TOKEN("invalid\_subject\_token")

class Reasoning:

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Optional<Context> context

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

One of the following:

AUTO("auto")

CURRENT\_TURN("current\_turn")

ALL\_TURNS("all\_turns")

Optional<[ReasoningEffort](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))> effort

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

DeprecatedOptional<GenerateSummary> generateSummary

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

One of the following:

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<Summary> summary

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

One of the following:

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

enum ReasoningEffort:

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

class ResponseFormatJsonObject:

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

class ResponseFormatJsonSchema:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

JsonSchema jsonSchema

Structured Outputs configuration options, including a JSON Schema.

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Schema> schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

class ResponseFormatText:

Default response format. Used to generate text responses.

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

class ResponseFormatTextGrammar:

A custom grammar for the model to follow when generating text.
Learn more in the [custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars).

String grammar

The custom grammar for the model to follow.

JsonValue; type "grammar"constant"grammar"constant

The type of response format being defined. Always `grammar`.

class ResponseFormatTextPython:

Configure the model to generate valid Python code. See the
[custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars) for more details.

JsonValue; type "python"constant"python"constant

The type of response format being defined. Always `python`.

class ResponsesModel: A class that can be one of several variants.union

String

enum ChatModel:

GPT\_5\_4("gpt-5.4")

GPT\_5\_4\_MINI("gpt-5.4-mini")

GPT\_5\_4\_NANO("gpt-5.4-nano")

GPT\_5\_4\_MINI\_2026\_03\_17("gpt-5.4-mini-2026-03-17")

GPT\_5\_4\_NANO\_2026\_03\_17("gpt-5.4-nano-2026-03-17")

GPT\_5\_3\_CHAT\_LATEST("gpt-5.3-chat-latest")

GPT\_5\_2("gpt-5.2")

GPT\_5\_2\_2025\_12\_11("gpt-5.2-2025-12-11")

GPT\_5\_2\_CHAT\_LATEST("gpt-5.2-chat-latest")

GPT\_5\_2\_PRO("gpt-5.2-pro")

GPT\_5\_2\_PRO\_2025\_12\_11("gpt-5.2-pro-2025-12-11")

GPT\_5\_1("gpt-5.1")

GPT\_5\_1\_2025\_11\_13("gpt-5.1-2025-11-13")

GPT\_5\_1\_CODEX("gpt-5.1-codex")

GPT\_5\_1\_MINI("gpt-5.1-mini")

GPT\_5\_1\_CHAT\_LATEST("gpt-5.1-chat-latest")

GPT\_5("gpt-5")

GPT\_5\_MINI("gpt-5-mini")

GPT\_5\_NANO("gpt-5-nano")

GPT\_5\_2025\_08\_07("gpt-5-2025-08-07")

GPT\_5\_MINI\_2025\_08\_07("gpt-5-mini-2025-08-07")

GPT\_5\_NANO\_2025\_08\_07("gpt-5-nano-2025-08-07")

GPT\_5\_CHAT\_LATEST("gpt-5-chat-latest")

GPT\_4\_1("gpt-4.1")

GPT\_4\_1\_MINI("gpt-4.1-mini")

GPT\_4\_1\_NANO("gpt-4.1-nano")

GPT\_4\_1\_2025\_04\_14("gpt-4.1-2025-04-14")

GPT\_4\_1\_MINI\_2025\_04\_14("gpt-4.1-mini-2025-04-14")

GPT\_4\_1\_NANO\_2025\_04\_14("gpt-4.1-nano-2025-04-14")

O4\_MINI("o4-mini")

O4\_MINI\_2025\_04\_16("o4-mini-2025-04-16")

O3("o3")

O3\_2025\_04\_16("o3-2025-04-16")

O3\_MINI("o3-mini")

O3\_MINI\_2025\_01\_31("o3-mini-2025-01-31")

O1("o1")

O1\_2024\_12\_17("o1-2024-12-17")

O1\_PREVIEW("o1-preview")

O1\_PREVIEW\_2024\_09\_12("o1-preview-2024-09-12")

O1\_MINI("o1-mini")

O1\_MINI\_2024\_09\_12("o1-mini-2024-09-12")

GPT\_4O("gpt-4o")

GPT\_4O\_2024\_11\_20("gpt-4o-2024-11-20")

GPT\_4O\_2024\_08\_06("gpt-4o-2024-08-06")

GPT\_4O\_2024\_05\_13("gpt-4o-2024-05-13")

GPT\_4O\_AUDIO\_PREVIEW("gpt-4o-audio-preview")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_10\_01("gpt-4o-audio-preview-2024-10-01")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-audio-preview-2024-12-17")

GPT\_4O\_AUDIO\_PREVIEW\_2025\_06\_03("gpt-4o-audio-preview-2025-06-03")

GPT\_4O\_MINI\_AUDIO\_PREVIEW("gpt-4o-mini-audio-preview")

GPT\_4O\_MINI\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-mini-audio-preview-2024-12-17")

GPT\_4O\_SEARCH\_PREVIEW("gpt-4o-search-preview")

GPT\_4O\_MINI\_SEARCH\_PREVIEW("gpt-4o-mini-search-preview")

GPT\_4O\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-search-preview-2025-03-11")

GPT\_4O\_MINI\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-mini-search-preview-2025-03-11")

CHATGPT\_4O\_LATEST("chatgpt-4o-latest")

CODEX\_MINI\_LATEST("codex-mini-latest")

GPT\_4O\_MINI("gpt-4o-mini")

GPT\_4O\_MINI\_2024\_07\_18("gpt-4o-mini-2024-07-18")

GPT\_4\_TURBO("gpt-4-turbo")

GPT\_4\_TURBO\_2024\_04\_09("gpt-4-turbo-2024-04-09")

GPT\_4\_0125\_PREVIEW("gpt-4-0125-preview")

GPT\_4\_TURBO\_PREVIEW("gpt-4-turbo-preview")

GPT\_4\_1106\_PREVIEW("gpt-4-1106-preview")

GPT\_4\_VISION\_PREVIEW("gpt-4-vision-preview")

GPT\_4("gpt-4")

GPT\_4\_0314("gpt-4-0314")

GPT\_4\_0613("gpt-4-0613")

GPT\_4\_32K("gpt-4-32k")

GPT\_4\_32K\_0314("gpt-4-32k-0314")

GPT\_4\_32K\_0613("gpt-4-32k-0613")

GPT\_3\_5\_TURBO("gpt-3.5-turbo")

GPT\_3\_5\_TURBO\_16K("gpt-3.5-turbo-16k")

GPT\_3\_5\_TURBO\_0301("gpt-3.5-turbo-0301")

GPT\_3\_5\_TURBO\_0613("gpt-3.5-turbo-0613")

GPT\_3\_5\_TURBO\_1106("gpt-3.5-turbo-1106")

GPT\_3\_5\_TURBO\_0125("gpt-3.5-turbo-0125")

GPT\_3\_5\_TURBO\_16K\_0613("gpt-3.5-turbo-16k-0613")

ResponsesOnlyModel

One of the following:

O1\_PRO("o1-pro")

O1\_PRO\_2025\_03\_19("o1-pro-2025-03-19")

O3\_PRO("o3-pro")

O3\_PRO\_2025\_06\_10("o3-pro-2025-06-10")

O3\_DEEP\_RESEARCH("o3-deep-research")

O3\_DEEP\_RESEARCH\_2025\_06\_26("o3-deep-research-2025-06-26")

O4\_MINI\_DEEP\_RESEARCH("o4-mini-deep-research")

O4\_MINI\_DEEP\_RESEARCH\_2025\_06\_26("o4-mini-deep-research-2025-06-26")

COMPUTER\_USE\_PREVIEW("computer-use-preview")

COMPUTER\_USE\_PREVIEW\_2025\_03\_11("computer-use-preview-2025-03-11")

GPT\_5\_CODEX("gpt-5-codex")

GPT\_5\_PRO("gpt-5-pro")

GPT\_5\_PRO\_2025\_10\_06("gpt-5-pro-2025-10-06")

GPT\_5\_1\_CODEX\_MAX("gpt-5.1-codex-max")
