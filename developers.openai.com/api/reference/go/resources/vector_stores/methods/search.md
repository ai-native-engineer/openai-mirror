<!-- source: https://developers.openai.com/api/reference/go/resources/vector_stores/methods/search/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Vector Stores](/api/reference/go/resources/vector_stores)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Search vector store

client.VectorStores.Search(ctx, vectorStoreID, body) (\*Page[[VectorStoreSearchResponse](/api/reference/go/resources/vector_stores#(resource)%20vector_stores%20%3E%20(model)%20VectorStoreSearchResponse%20%3E%20(schema))], error)

POST/vector\_stores/{vector\_store\_id}/search

Search a vector store for relevant chunks based on a query and file attributes filter.

##### ParametersExpand Collapse

vectorStoreID string

body VectorStoreSearchParams

Query param.Field[[VectorStoreSearchParamsQueryUnion](/api/reference/go/resources/vector_stores/methods/search#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%20default%20%3E%20(param)%20query%20%3E%20(schema))]

A query string for a search

string

type VectorStoreSearchParamsQueryArray []string

Filters param.Field[[VectorStoreSearchParamsFiltersUnion](/api/reference/go/resources/vector_stores/methods/search#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%20default%20%3E%20(param)%20filters%20%3E%20(schema))]Optional

A filter to apply based on file attributes.

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

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

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

MaxNumResults param.Field[int64]Optional

The maximum number of results to return. This number should be between 1 and 50 inclusive.

minimum1

maximum50

RankingOptions param.Field[[VectorStoreSearchParamsRankingOptions](/api/reference/go/resources/vector_stores/methods/search#(resource)%20vector_stores%20%3E%20(method)%20search%20%3E%20(params)%20default%20%3E%20(param)%20ranking_options%20%3E%20(schema))]Optional

Ranking options for search.

Ranker stringOptional

Enable re-ranking; set to `none` to disable, which can help reduce latency.

One of the following:

const VectorStoreSearchParamsRankingOptionsRankerNone VectorStoreSearchParamsRankingOptionsRanker = "none"

const VectorStoreSearchParamsRankingOptionsRankerAuto VectorStoreSearchParamsRankingOptionsRanker = "auto"

const VectorStoreSearchParamsRankingOptionsRankerDefault2024\_11\_15 VectorStoreSearchParamsRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

minimum0

maximum1

RewriteQuery param.Field[bool]Optional

Whether to rewrite the natural language query for vector search.

##### ReturnsExpand Collapse

type VectorStoreSearchResponse struct{…}

Attributes map[string, VectorStoreSearchResponseAttributeUnion]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

One of the following:

string

float64

bool

Content []VectorStoreSearchResponseContent

Content chunks from the file.

Text string

The text content returned from search.

Type string

The type of content.

FileID string

The ID of the vector store file.

Filename string

The name of the vector store file.

Score float64

The similarity score for the result.

minimum0

maximum1

### Search vector store

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.VectorStores.Search(
    context.TODO(),
    "vs_abc123",
    openai.VectorStoreSearchParams{
      Query: openai.VectorStoreSearchParamsQueryUnion{
        OfString: openai.String("string"),
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
