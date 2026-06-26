<!-- source: https://developers.openai.com/api/reference/cli/resources/vector_stores/methods/search/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Vector Stores](/api/reference/cli/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Search vector store

$ openai vector-stores search

POST/vector\_stores/{vector\_store\_id}/search

Search a vector store for relevant chunks based on a query and file attributes filter.

##### ParametersExpand Collapse

--vector-store-id: string

The ID of the vector store to search.

--query: string or array of string

A query string for a search

--filters: optional [ComparisonFilter](/api/reference/cli/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/cli/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }

A filter to apply based on file attributes.

--max-num-results: optional number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

--ranking-options: optional object { ranker, score\_threshold }

Ranking options for search.

--rewrite-query: optional boolean

Whether to rewrite the natural language query for vector search.

##### ReturnsExpand Collapse

VectorStoreSearchResultsPage: object { data, has\_more, next\_page, 2 more }

data: array of object { attributes, content, file\_id, 2 more }

The list of search result items.

attributes: map[string or number or boolean]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

content: array of object { text, type }

Content chunks from the file.

text: string

The text content returned from search.

type: "text"

The type of content.

"text"

file\_id: string

The ID of the vector store file.

filename: string

The name of the vector store file.

score: number

The similarity score for the result.

has\_more: boolean

Indicates if there are more results to fetch.

next\_page: string

The token for the next page, if any.

object: "vector\_store.search\_results.page"

The object type, which is always `vector_store.search_results.page`

search\_query: array of string

### Search vector store

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai vector-stores search \
  --api-key 'My API Key' \
  --vector-store-id vs_abc123 \
  --query string

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
