<!-- source: https://developers.openai.com/api/reference/python/resources/vector_stores/methods/search/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Vector Stores](/api/reference/python/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Search vector store

vector\_stores.search(strvector\_store\_id, VectorStoreSearchParams\*\*kwargs)  -> SyncPage[[VectorStoreSearchResponse](/api/reference/python/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20vector_store_search_response%20%3E%20(schema))]

POST/vector\_stores/{vector\_store\_id}/search

Search a vector store for relevant chunks based on a query and file attributes filter.

##### ParametersExpand Collapse

vector\_store\_id: str

query: Union[str, Sequence[str]]

A query string for a search

One of the following:

str

Sequence[str]

filters: Optional[[Filters](/api/reference/python/resources/vector_stores/methods/search#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%20default%20%3E%20(param)%20filters%20%3E%20(schema))]

A filter to apply based on file attributes.

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

minimum1

maximum50

ranking\_options: Optional[[RankingOptions](/api/reference/python/resources/vector_stores/methods/search#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%20default%20%3E%20(param)%20ranking_options%20%3E%20(schema))]

Ranking options for search.

ranker: Optional[Literal["none", "auto", "default-2024-11-15"]]

Enable re-ranking; set to `none` to disable, which can help reduce latency.

One of the following:

"none"

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

minimum0

maximum1

rewrite\_query: Optional[[bool](/api/reference/python/resources/vector_stores/methods/search#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%20default%20%3E%20(param)%20rewrite_query%20%3E%20(schema))]

Whether to rewrite the natural language query for vector search.

##### ReturnsExpand Collapse

class VectorStoreSearchResponse: …

attributes: Optional[Dict[str, Union[str, float, bool]]]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

str

float

bool

content: List[Content]

Content chunks from the file.

text: str

The text content returned from search.

type: Literal["text"]

The type of content.

file\_id: str

The ID of the vector store file.

filename: str

The name of the vector store file.

score: float

The similarity score for the result.

minimum0

maximum1

### Search vector store

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
page = client.vector_stores.search(
    vector_store_id="vs_abc123",
    query="string",
page = page.data[0]
print(page.file_id)

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
