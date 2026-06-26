<!-- source: https://developers.openai.com/cookbook/examples/using_embeddings/ -->

## Search the cookbook

Mar 10, 2022

# Using embeddings

This recipe is archived and may reference outdated models or APIs.

[BO](https://github.com/BorisPower)  [![Ted Sanders](https://avatars.githubusercontent.com/u/95656834?v=4)  TS](https://github.com/ted-at-openai)  [LO](https://github.com/logankilpatrick)  [![Joe Beutler](https://avatars.githubusercontent.com/u/156261485?v=4)  JB](https://joebeutler.com)

[BorisPower ,](https://github.com/BorisPower)  [Ted Sanders 
(OpenAI)
 ,](https://github.com/ted-at-openai)  [logankilpatrick ,](https://github.com/logankilpatrick)  [Joe Beutler 
(OpenAI)](https://joebeutler.com)

[View on GitHub](https://github.com/openai/openai-cookbook/blob/main/examples/Using_embeddings.ipynb) [Download raw](https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/Using_embeddings.ipynb)

## Using embeddings

This notebook contains some helpful snippets you can use to embed text with the `text-embedding-3-small` model via the OpenAI API.

from openai import OpenAI
client = OpenAI()

embedding = client.embeddings.create(
    input="Your text goes here", model="text-embedding-3-small"
).data[0].embedding
len(embedding)

1536

It’s recommended to use the ‘tenacity’ package or another exponential backoff implementation to better manage API rate limits, as hitting the API too much too fast can trigger rate limits. Using the following function ensures you get your embeddings as fast as possible.

# Negative example (slow and rate-limited)
from openai import OpenAI
client = OpenAI()

num_embeddings = 10000 # Some large number
for i in range(num_embeddings):
    embedding = client.embeddings.create(
        input="Your text goes here", model="text-embedding-3-small"
    ).data[0].embedding
    print(len(embedding))

# Best practice
from tenacity import retry, wait_random_exponential, stop_after_attempt
from openai import OpenAI
client = OpenAI()

# Retry up to 6 times with exponential backoff, starting at 1 second and maxing out at 20 seconds delay
@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_embedding(text: str, model="text-embedding-3-small") -> list[float]:
    return client.embeddings.create(input=[text], model=model).data[0].embedding

embedding = get_embedding("Your text goes here", model="text-embedding-3-small")
print(len(embedding))

1536
