<!-- source: https://developers.openai.com/api/reference/ruby/resources/vector_stores/methods/search/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Vector Stores](/api/reference/ruby/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Search vector store

vector\_stores.search(vector\_store\_id, \*\*kwargs) -> Page<[VectorStoreSearchResponse](/api/reference/ruby/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema)) { attributes, content, file\_id, 2 more } >

POST/vector\_stores/{vector\_store\_id}/search

Search a vector store for relevant chunks based on a query and file attributes filter.

##### ParametersExpand Collapse

vector\_store\_id: String

query: String | Array[String]

A query string for a search

One of the following:

String = String

UnionMember1 = Array[String]

filters: [ComparisonFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }

A filter to apply based on file attributes.

One of the following:

class ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: String

The key to compare against the value.

type: :eq | :ne | :gt | 5 more

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

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

One of the following:

String = String

Float = Float

class CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array[[ComparisonFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | untyped]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: String

The key to compare against the value.

type: :eq | :ne | :gt | 5 more

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

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

One of the following:

String = String

Float = Float

UnionMember1 = untyped

type: :and | :or

Type of operation: `and` or `or`.

One of the following:

:and

:or

max\_num\_results: Integer

The maximum number of results to return. This number should be between 1 and 50 inclusive.

minimum1

maximum50

ranking\_options: RankingOptions{ ranker, score\_threshold}

Ranking options for search.

ranker: :none | :auto | :"default-2024-11-15"

Enable re-ranking; set to `none` to disable, which can help reduce latency.

One of the following:

:none

:auto

:"default-2024-11-15"

score\_threshold: Float

minimum0

maximum1

rewrite\_query: bool

Whether to rewrite the natural language query for vector search.

##### ReturnsExpand Collapse

class VectorStoreSearchResponse { attributes, content, file\_id, 2 more }

attributes: Hash[Symbol, String | Float | bool]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

String = String

Float = Float

UnionMember2 = bool

content: Array[Content{ text, type}]

Content chunks from the file.

text: String

The text content returned from search.

type: :text

The type of content.

file\_id: String

The ID of the vector store file.

filename: String

The name of the vector store file.

score: Float

The similarity score for the result.

minimum0

maximum1

### Search vector store

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.vector_stores.search("vs_abc123", query: "string")

puts(page)

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
