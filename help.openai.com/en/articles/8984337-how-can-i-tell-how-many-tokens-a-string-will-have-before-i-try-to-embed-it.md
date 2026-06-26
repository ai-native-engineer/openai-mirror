<!-- source: https://help.openai.com/en/articles/8984337-how-can-i-tell-how-many-tokens-a-string-will-have-before-i-try-to-embed-it -->

# How can I tell how many tokens a string will have before I try to embed it?

Calculating/approximating tokens for an embedding

Updated: 12 days ago

Before sending a string for embedding, you can estimate how many tokens it will use by applying OpenAI’s [tiktoken tokenizer library](https://github.com/openai/tiktoken).

This is especially useful because embedding models (like `text-embedding-3-small`) have maximum token limits you’ll need to stay within.

---

## How to Count Tokens with Tiktoken

You can use the `tiktoken` Python package to calculate the number of tokens a string will generate.

Here’s a sample code snippet:

```
import tiktoken  
  
def num_tokens_from_string(string: str, encoding_name: str) -> int:  
    """Returns the number of tokens in a text string."""  
    encoding = tiktoken.get_encoding(encoding_name)  
    num_tokens = len(encoding.encode(string))  
    return num_tokens  
  
# Example usage  
num_tokens = num_tokens_from_string("tiktoken is great!", "cl100k_base")  
print(num_tokens)
```

**Important**:

* For **third-generation embedding models** (e.g., `text-embedding-3-small` or `text-embedding-3-large`), you should use the `"cl100k_base"` encoding.
* Different models may require different encodings — always refer to the model documentation if unsure.

---

## Why Token Counting Matters

* If your string exceeds the model’s maximum input size, your API request will fail.
* Accurately counting tokens ahead of time ensures smoother embedding workflows and prevents errors during processing.

---

## Helpful Links

* [How to count tokens with tiktoken (OpenAI Cookbook)](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
* [Embedding model documentation](https://platform.openai.com/docs/guides/embeddings)
