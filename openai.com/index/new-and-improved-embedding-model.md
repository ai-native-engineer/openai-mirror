<!-- source: https://openai.com/index/new-and-improved-embedding-model/ -->

December 15, 2022

[Product](/news/product-releases/)

# New and improved embedding model

[Read documentation(opens in a new window)](https://beta.openai.com/docs/guides/embeddings)

![A soft-focus landscape painting depicting a green foreground, a pastel pink and beige field, and distant hills beneath a bright pink and light blue sky.](https://images.ctfassets.net/kftzwdyauwt9/266Oz4WaWnYHxkErVdrfYD/a986d84d80b9d5a277732bb0aac706c9/new-and-improved-embedding-model.jpg?w=3840&q=90&fm=webp)

The new model, `text-embedding-ada-002`, replaces five separate models for text search, text similarity, and code search, and outperforms our previous most capable model, Davinci, at most tasks, while being priced 99.8% lower.

Embeddings are numerical representations of concepts converted to number sequences, which make it easy for computers to understand the relationships between those concepts. Since the [initial launch⁠](/index/introducing-text-and-code-embeddings/) of the OpenAI [/embeddings⁠(opens in a new window)](https://beta.openai.com/docs/api-reference/embeddings) endpoint, many applications have incorporated embeddings to personalize, recommend, and search content.

Loading...

You can query the [/embeddings⁠(opens in a new window)](https://beta.openai.com/docs/api-reference/embeddings) endpoint for the new model with two lines of code using our [OpenAI Python Library⁠(opens in a new window)](https://github.com/openai/openai-python), just like you could with previous models:

```
import openai
response = openai.Embedding.create(
  input="porcine pals say",
  model="text-embedding-ada-002"
)
```

Print response

## Model improvements

**Stronger performance**. `text-embedding-ada-002` outperforms all the old embedding models on text search, code search, and sentence similarity tasks and gets comparable performance on text classification. For each task category, we evaluate the models on the datasets used in [old embeddings⁠(opens in a new window)](https://arxiv.org/abs/2201.10005).

| Model | Performance |
| --- | --- |
| `text-embedding-ada-002` | 53.3 |
| `text-search-davinci-*-001` | 52.8 |
| `text-search-curie-*-001` | 50.9 |
| `text-search-babbage-*-001` | 50.4 |
| `text-search-ada-*-001` | 49.0 |

Dataset: [BEIR](https://github.com/UKPLab/beir) (ArguAna, ClimateFEVER, DBPedia, FEVER, FiQA2018, HotpotQA, NFCorpus, QuoraRetrieval, SciFact, TRECCOVID, Touche2020)

**Unification of capabilities**. We have significantly simplified the interface of the [/embeddings⁠(opens in a new window)](https://beta.openai.com/docs/api-reference/embeddings) endpoint by merging the five separate models shown above (`text-similarity`, `text-search-query`, `text-search-doc`, `code-search-text` and `code-search-code`) into a single new model. This single representation performs better than our previous embedding models across a diverse set of text search, sentence similarity, and code search benchmarks.

**Longer context.** The context length of the new model is increased by a factor of four, from 2048 to 8192, making it more convenient to work with long documents.

**Smaller embedding size.** The new embeddings have only 1536 dimensions, one-eighth the size of `davinci-001` embeddings, making the new embeddings more cost effective in working with vector databases.

**Reduced price.** We have reduced the price of new embedding models by 90% compared to old models of the same size. The new model achieves better or similar performance as the old Davinci models at a 99.8% lower price.

Overall, the new embedding model is a much more powerful tool for natural language processing and code tasks. We are excited to see how our customers will use it to create even more capable applications in their respective fields.

## Limitations

The new `text-embedding-ada-002` model is not outperforming `text-similarity-davinci-001` on the SentEval linear probing classification benchmark. For tasks that require training a light-weighted linear layer on top of embedding vectors for classification prediction, we suggest comparing the new model to `text-similarity-davinci-001` and choosing whichever model gives optimal performance.

Check the [Limitations & Risks⁠(opens in a new window)](https://beta.openai.com/docs/guides/embeddings/limitations-risks) section in the embeddings documentation for general limitations of our embedding models.

## Examples of the embeddings API in action

[**Kalendar AI**⁠(opens in a new window)](https://kalendar.ai/) is a sales outreach product that uses embeddings to match the right sales pitch to the right customers out of a dataset containing 340M profiles. This automation relies on similarity between embeddings of customer profiles and sale pitches to rank up most suitable matches, eliminating 40–56% of unwanted targeting compared to their old approach.

[**Notion**⁠(opens in a new window)](https://www.notion.so/), the online workspace company, will use OpenAI’s new embeddings to improve Notion search beyond today’s keyword matching systems.

* [Read documentation(opens in a new window)](https://beta.openai.com/docs/guides/embeddings)

* [API Platform](/news/?tags=api-platform)
* [2022](/news/?tags=2022)

## Authors

Ryan Greene, Ted Sanders, Lilian Weng, Arvind Neelakantan

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
