<!-- source: https://developers.openai.com/api/reference/java/resources/decisions/ -->

[Skip to content](#_top)

For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending
`.md` to the page URL.

Copy Markdown

# Decisions

##### [Create a decision](/api/reference/java/resources/decisions/methods/create)

[Decision](/api/reference/java/resources/decisions#(resource)%20decisions%20%3E%20(model)%20decision%20%3E%20(schema)) decisions().create(DecisionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST

/decisions

##### ModelsExpand Collapse

class Decision:

class DecisionChoiceOption:

class DecisionChoiceValue: A class that can be one of several variants.

union

Choice values are typed: a string and a boolean with the same text are distinct.

class DecisionInputImage:

An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

class DecisionInputItem: A class that can be one of several variants.

union

A user message containing input text, images, or JSON.

class DecisionInputMessage: A class that can be one of several variants.

union

A user message containing input text, images, or JSON.

class DecisionInputPart: A class that can be one of several variants.

union

An image provided as a base64 data URL or a publicly accessible HTTP(S) URL. File IDs are not supported.

class DecisionInputText:

class DecisionPromptCacheBreakpoint:

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.
