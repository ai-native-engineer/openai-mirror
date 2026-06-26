<!-- source: https://openai.com/index/introducing-text-and-code-embeddings/ -->

January 25, 2022

[Product](/news/product-releases/)

# Introducing text and code embeddings

We are introducing embeddings, a new endpoint in the OpenAI API that makes it easy to perform natural language and code tasks like semantic search, clustering, topic modeling, and classification.

[Read documentation(opens in a new window)](https://beta.openai.com/docs/guides/embeddings)[Read paper(opens in a new window)](https://arxiv.org/abs/2201.10005)

![An abstract landscape painting featuring a vivid blue sky with textured clouds in orange and white above rolling hills in shades of purple, green, and gold.](https://images.ctfassets.net/kftzwdyauwt9/4xj3R5liKGPVwyuNJ0ghjP/69a47222ceb6325af88c8f5102b70005/introducing-text-and-code-embeddings.jpg?w=3840&q=90&fm=webp)

Embeddings are numerical representations of concepts converted to number sequences, which make it easy for computers to understand the relationships between those concepts. Our embeddings outperform top models in 3 standard benchmarks, including a 20% relative improvement in code search.

Embeddings are useful for working with natural language and code, because they can be readily consumed and compared by other machine learning models and algorithms like clustering or search.

Loading...

Embeddings that are numerically similar are also semantically similar. For example, the embedding vector of “canine companions say” will be more similar to the embedding vector of “woof” than that of “meow.”

![Graph Of Similar Embeddings](https://images.ctfassets.net/kftzwdyauwt9/6feca3be-2b6b-4a99-fc14ed78f1ee/3373feb41e1f9f49ba2c0f1ce3332b8b/Graphofsimilarembeddings.svg?w=3840&q=90)

The new endpoint uses neural network models, which are descendants of GPT‑3, to map text and code to a vector representation—“embedding” them in a high-dimensional space. Each dimension captures some aspect of the input.

The new [/embeddings⁠(opens in a new window)](https://beta.openai.com/docs/api-reference/embeddings) endpoint in the [OpenAI API⁠(opens in a new window)](https://beta.openai.com/) provides text and code embeddings with a few lines of code:

Loading...

We’re releasing three families of embedding models, each tuned to perform well on different functionalities: text similarity, text search, and code search. The models take either text or code as input and return an embedding vector.

|  |  |  |
| --- | --- | --- |
|  | Models | Use Cases |
| Text similarity: Captures semantic similarity between pieces of text. | text-similarity-{ada, babbage, curie, davinci}-001 | Clustering, regression, anomaly detection, visualization |
| Text search: Semantic information retrieval over documents. | text-search-{ada, babbage, curie, davinci}-{query, doc}-001 | Search, context relevance, information retrieval |
| Code search: Find relevant code with a query in natural language. | code-search-{ada, babbage}-{code, text}-001 | Code search and relevance |

## Text similarity models

Text similarity models provide embeddings that capture the semantic similarity of pieces of text. These models are useful for many tasks including [clustering⁠(opens in a new window)](https://beta.openai.com/docs/guides/embeddings/clustering), [data visualization⁠(opens in a new window)](https://beta.openai.com/docs/guides/embeddings/data-visualization-in-2d), and [classification⁠(opens in a new window)](https://beta.openai.com/docs/guides/embeddings/classification-using-the-embedding-features).

The following interactive visualization shows embeddings of text samples from the DBpedia dataset:

Loading...

To compare the similarity of two pieces of text, you simply use the [dot product⁠(opens in a new window)](https://en.wikipedia.org/wiki/Dot_product) on the text embeddings. The result is a “similarity score”, sometimes called “[cosine similarity⁠(opens in a new window)](https://en.wikipedia.org/wiki/Dot_product#Application_to_the_law_of_cosines),” between –1 and 1, where a higher number means more similarity. In most applications, the embeddings can be pre-computed, and then the dot product comparison is extremely fast to carry out.

#### Python

```` ```
1

import openai, numpy as np

2

3

resp = openai.Embedding.create(

4

input=["feline friends say", "meow"],

5

engine="text-similarity-davinci-001")

6

7

embedding_a = resp['data'][0]['embedding']

8

embedding_b = resp['data'][1]['embedding']

9

10

similarity_score = np.dot(embedding_a, embedding_b)
``` ````

One popular use of embeddings is to use them as features in machine learning tasks, such as classification. In machine learning literature, when using a linear classifier, this classification task is called a “linear probe.” Our text similarity models achieve new state-of-the-art results on linear probe classification in [SentEval⁠(opens in a new window)](https://github.com/facebookresearch/SentEval) ([Conneau et al., 2018⁠(opens in a new window)](https://arxiv.org/abs/1803.05449)), a commonly used benchmark for evaluating embedding quality.

Loading...

## Text search models

Text search models provide embeddings that enable large-scale search tasks, like finding a relevant document among a collection of documents given a text query. Embedding for the documents and query are produced separately, and then cosine similarity is used to compare the similarity between the query and each document.

Embedding-based search can generalize better than word overlap techniques used in classical keyword search, because it captures the semantic meaning of text and is less sensitive to exact phrases or words. We evaluate the text search model’s performance on the [BEIR⁠(opens in a new window)](https://github.com/UKPLab/beir) ([Thakur, et al. 2021⁠(opens in a new window)](https://arxiv.org/abs/2104.08663)) search evaluation suite and obtain better search performance than previous methods. Our [text search guide⁠(opens in a new window)](https://beta.openai.com/docs/guides/embeddings/text-search-using-embeddings) provides more details on using embeddings for search tasks.

Loading...

## Code search models

Code search models provide code and text embeddings for code search tasks. Given a collection of code blocks, the task is to find the relevant code block for a natural language query. We evaluate the code search models on the [CodeSearchNet⁠(opens in a new window)](https://github.com/github/CodeSearchNet) ([Husain et al., 2019⁠(opens in a new window)](https://arxiv.org/abs/1909.09436)) evaluation suite where our embeddings achieve significantly better results than prior methods. Check out the [code search guide⁠(opens in a new window)](https://beta.openai.com/docs/guides/embeddings/code-search-using-embeddings) to use embeddings for code search.

Loading...

## Examples of the embeddings API in action

### JetBrains Research

JetBrains Research’s [Astroparticle Physics Lab⁠(opens in a new window)](https://research.jetbrains.org/groups/astroparticle-physics/) analyzes data like [The Astronomer’s Telegram⁠(opens in a new window)](https://en.wikipedia.org/wiki/The_Astronomer%27s_Telegram) and NASA’s [GCN Circulars⁠(opens in a new window)](https://gcn.gsfc.nasa.gov/), which are reports that contain astronomical events that can’t be parsed by traditional algorithms.

Powered by OpenAI’s embeddings of these astronomical reports, researchers are now able to search for events like “crab pulsar bursts” across multiple databases and publications. Embeddings also achieved 99.85% accuracy on data source classification through k-means clustering.

### FineTune Learning

[FineTune Learning⁠(opens in a new window)](https://finetunelearning.com/) is a company building hybrid human-AI solutions for learning, like [adaptive learning loops⁠(opens in a new window)](https://en.wikipedia.org/wiki/Adaptive_learning) that help students reach academic standards.

OpenAI’s embeddings significantly improved the task of finding textbook content based on learning objectives. Achieving a top-5 accuracy of 89.1%, OpenAI’s text-search-curie embeddings model outperformed previous approaches like Sentence-BERT (64.5%). While human experts are still better, the FineTune team is now able to label entire textbooks in a matter of seconds, in contrast to the hours that it took the experts.

Loading...

### Fabius

[Fabius⁠(opens in a new window)](https://www.fabius.io/) helps companies turn customer conversations into structured insights that inform planning and prioritization. OpenAI’s embeddings allow companies to more easily find and tag customer call transcripts with feature requests.

For instance, customers might use words like “automated” or “easy to use” to ask for a better self-service platform. Previously, Fabius was using fuzzy keyword search to attempt to tag those transcripts with the self-service platform label. With OpenAI’s embeddings, they’re now able to find 2x more examples in general, and 6x–10x more examples for features with abstract use cases that don’t have a clear keyword customers might use.

All API customers can get started with the [embeddings documentation⁠(opens in a new window)](https://beta.openai.com/docs/guides/embeddings) for using embeddings in their applications.

* [Read documentation](https://beta.openai.com/docs/guides/embeddings)

* [API Platform](/news/?tags=api-platform)
* [2022](/news/?tags=2022)

## Authors

Arvind Neelakantan, Lilian Weng, Boris Power, Joanne Jang

## Related articles

![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819b4c211886a2/NewsPartnership_Cover.png?w=3840&q=90&fm=webp)

[Global news partnerships: Le Monde and Prisa Media

CompanyMar 13, 2024](/index/global-news-partnerships-le-monde-and-prisa-media/)

![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/fdcc0dadabd87f8e9a776a2f34647de0/37.png?w=3840&q=90&fm=webp)

[Review completed & Altman, Brockman to continue to lead OpenAI

CompanyMar 8, 2024](/index/review-completed-altman-brockman-to-continue-to-lead-openai/)

![New board of directors](https://images.ctfassets.net/kftzwdyauwt9/5J9s3ItUUDOTebSo0ZVmun/642e8632be32866792c7aaae0113aaa5/44.png?w=3840&q=90&fm=webp)

[OpenAI announces new members to board of directors

CompanyMar 8, 2024](/index/openai-announces-new-members-to-board-of-directors/)
