<!-- source: https://help.openai.com/en/articles/6824809-embeddings-faq -->

# Embeddings FAQ

FAQ for the new and improved embedding models

Updated: 10 days ago

On January 25, 2024 we released two new embeddings models: `text-embedding-3-small` and `text-embedding-3-large`. These are our newest and most performant embedding models with lower costs, higher multilingual performance, and a new parameter for shortening embeddings. [Read more](https://platform.openai.com/docs/guides/embeddings/).

## What's different about the latest embeddings models?

Our latest v3 models provide stronger performance on common benchmarks at a reduced price. You can read more about the performance improvements in the [announcement blog post](https://openai.com/blog/new-embedding-models-and-api-updates) and [developer documentation](https://platform.openai.com/docs/guides/embeddings/).

## How can I tell how many tokens a string will have before I try to embed it?

You can use [OpenAI's Tiktoken package](https://github.com/openai/tiktoken) to check how many tokens a string will have. Learn more in our [embeddings developer guide](https://platform.openai.com/docs/guides/embeddings/how-can-i-tell-how-many-tokens-a-string-has-before-i-embed-it).

## How can I retrieve K nearest embedding vectors quickly?

For searching over many vectors quickly, we recommend using a [vector database](https://platform.openai.com/docs/guides/embeddings/how-can-i-retrieve-k-nearest-embedding-vectors-quickly).

## Which distance function should I use?

OpenAI API embedding outputs are L2-normalized to length 1 by default, including after shortening with the `dimensions` parameter, which means that:

OpenAI embeddings are normalized to length 1, which means that:

* Cosine similarity can be computed slightly faster using just a dot product
* Cosine similarity and Euclidean distance will result in the identical rankings
