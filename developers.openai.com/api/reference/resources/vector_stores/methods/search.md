<!-- source: https://developers.openai.com/api/reference/resources/vector_stores/methods/search/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Vector Stores](/api/reference/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Search vector store

POST/vector\_stores/{vector\_store\_id}/search

Search a vector store for relevant chunks based on a query and file attributes filter.

##### Path ParametersExpand Collapse

vector\_store\_id: string

##### Body ParametersJSONExpand Collapse

query: string or array of string

A query string for a search

One of the following:

string

array of string

filters: optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }

A filter to apply based on file attributes.

One of the following:

ComparisonFilter object { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" or "ne" or "gt" or 5 more

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

value: string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

array of string or number

One of the following:

string

number

CompoundFilter object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

ComparisonFilter object { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" or "ne" or "gt" or 5 more

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

value: string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

array of string or number

One of the following:

string

number

unknown

type: "and" or "or"

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results: optional number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

minimum1

maximum50

ranking\_options: optional object { ranker, score\_threshold }

Ranking options for search.

ranker: optional "none" or "auto" or "default-2024-11-15"

Enable re-ranking; set to `none` to disable, which can help reduce latency.

One of the following:

"none"

"auto"

"default-2024-11-15"

score\_threshold: optional number

minimum0

maximum1

rewrite\_query: optional boolean

Whether to rewrite the natural language query for vector search.

##### ReturnsExpand Collapse

data: array of object { attributes, content, file\_id, 2 more }

The list of search result items.

attributes: map[string or number or boolean]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

number

boolean

content: array of object { text, type }

Content chunks from the file.

text: string

The text content returned from search.

type: "text"

The type of content.

file\_id: string

The ID of the vector store file.

filename: string

The name of the vector store file.

score: number

The similarity score for the result.

minimum0

maximum1

has\_more: boolean

Indicates if there are more results to fetch.

next\_page: string

The token for the next page, if any.

object: "vector\_store.search\_results.page"

The object type, which is always `vector_store.search_results.page`

search\_query: array of string

### Search vector store

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST \
https://api.openai.com/v1/vector_stores/vs_abc123/search \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-H "Content-Type: application/json" \
-d '{"query": "What is the return policy?", "filters": {...}}'

  "object": "vector_store.search_results.page",
  "search_query": "What is the return policy?",
  "data": [
      "file_id": "file_123",
      "filename": "document.pdf",
      "score": 0.95,
      "attributes": {
        "author": "John Doe",
        "date": "2023-01-01"
      "content": [
          "type": "text",
          "text": "Relevant chunk"
      ]
      "file_id": "file_456",
      "filename": "notes.txt",
      "score": 0.89,
      "attributes": {
        "author": "Jane Smith",
        "date": "2023-01-02"
      "content": [
          "type": "text",
          "text": "Sample text content from the vector store."
      ]
  ],
  "has_more": false,
  "next_page": null

##### Returns Examples

  "object": "vector_store.search_results.page",
  "search_query": "What is the return policy?",
  "data": [
      "file_id": "file_123",
      "filename": "document.pdf",
      "score": 0.95,
      "attributes": {
        "author": "John Doe",
        "date": "2023-01-01"
      "content": [
          "type": "text",
          "text": "Relevant chunk"
      ]
      "file_id": "file_456",
      "filename": "notes.txt",
      "score": 0.89,
      "attributes": {
        "author": "Jane Smith",
        "date": "2023-01-02"
      "content": [
          "type": "text",
          "text": "Sample text content from the vector store."
      ]
  ],
  "has_more": false,
  "next_page": null
