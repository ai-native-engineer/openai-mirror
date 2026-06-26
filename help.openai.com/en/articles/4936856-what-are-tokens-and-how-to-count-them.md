<!-- source: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them -->

# What are tokens and how to count them?

Updated: 9 days ago

# What are tokens?

Tokens are the building blocks of text that OpenAI models process. They can be as short as a single character or as long as a full word, depending on the language and context. Spaces, punctuation, and partial words all contribute to token counts. This is how the API internally segments your text before generating a response.

Helpful rules of thumb for English:

* 1 token ≈ 4 characters
* 1 token ≈ ¾ of a word
* 100 tokens ≈ 75 words
* 1–2 sentences ≈ 30 tokens
* 1 paragraph ≈ 100 tokens
* ~1,500 words ≈ 2,048 tokens

Tokenization varies by model and encoding. Use the Tokenizer tool or `tiktoken.encoding_for_model(model)` to get the exact count for your target model.

# Examples

Here are some real-world text samples with their approximate token counts:

* Wayne Gretzky’s quote “You miss 100% of the shots you don’t take” = 11 tokens
* The OpenAI Charter = 476 tokens
* The US Declaration of Independence = 1,695 tokens

# How token counts are calculated

When you send text to the API:

1. The text is split into tokens.
2. The model processes these tokens.
3. The response is generated as a sequence of tokens, then converted back to text.

Token usage is tracked in several categories:

* **Input tokens** – tokens in your request.
* **Output tokens** – tokens generated in the response.
* **Cached tokens** – reused tokens in conversation history (often billed at a reduced rate).
* **Reasoning tokens** – in some advanced models, extra “thinking steps” are included internally before producing the final output.

These counts appear in your API response metadata and are used for billing and usage tracking.

To further explore tokenization, you can use our interactive [Tokenizer tool](https://platform.openai.com/tokenizer), which allows you to calculate the number of tokens and see how text is broken into tokens.   
  
Alternatively, if you'd like to tokenize text programmatically, use [Tiktoken](https://github.com/openai/tiktoken) as a fast BPE tokenizer specifically used for OpenAI models.

# Token Limits

Each [model](https://beta.openai.com/docs/engines/gpt-3) has a maximum combined token limit (input + output). Current high-capacity models support up to hundreds of thousands of tokens in context, though practical limits may vary depending on the model version and your usage tier.

If you exceed the limit, you can:

* Shorten or rephrase prompts.
* Break large text into smaller chunks.
* Summarize or pre-process inputs before sending them.

# Token Pricing

API usage is priced per token, varying by model and whether tokens are input, output, or cached. See OpenAI’s [pricing page](https://openai.com/api/pricing/) for current rates. Some reasoning models may use more tokens internally but aim to improve efficiency by reducing the number of tokens needed per completed task.

# Exploring tokens

The API treats words according to their context in the corpus data. Models take the prompt, convert the input into a list of tokens, processes the prompt, and convert the predicted tokens back to the words we see in the response.

What might appear as two identical words to us may be generated into different tokens depending on how they are structured within the text. Consider how the API generates token values for the word ‘*red*’ based on its context within the text:

![Sentence split into color-coded tokens with Text selected over Token IDs](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b6df6a77ec1edf15ef51a78d/9df1d32b543da45a2200bab3a2dd8586/v_Sp27FQeadYK4lYgk8CA_l2mR70v-WSOUyXfjjpPj_Ny9Dc8RRWnxon4o_ct59dqOgPY_5D88puOFdquuKueWRsD8sM9DSB7yBntE3KqnrMPhHR91BHClTFTnab3u6i)

![Token ID output as a list of integers with the Token IDs tab selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-cf2bb5e9315674131fad16b0/0a500eb3a2728d5bcd0b450154c4d17c/_Q6XzFgIIAIDmUVdCFHF1vGyic8hG61Pc-3eOIAtOG29qBxEgXsUzCOm_k2xIn2UfrV9PPCIBuz6YOcPYru_ssvFZymE8ijKKxxHNEZd8Wx-BwimhfXXNipF6TXm2-Xy)

In the first example above the token “2266” for ‘ red’ includes a trailing space (Note, these are example token ID's for demonstration purposes).

![Sentence split into color-coded token blocks: My favorite color is Red.](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-421996280ff7e407be77fd34/636bf79a39ae2a97c6a1d482a51691ff/vvmePo3aWbhExL36QLsDYXe8OaeFvzeqEj4zqXqRGV-5xFA6W8zXu1QQMvsMlycoje4OJPCuA1YMLpokaAvaVH_CXzWuZInVhCE4wByMEiakQ9HObxECfbo36pKASPtK)

![Tokenizer output with Token IDs selected and a list of numeric token IDs](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-aa796598a1627279282fc77c/c85fae326d2e2a414c4c683439fc18e8/lRvNrEim9UIXmL5j6ahrf2Mcb46uTyMyoL66xygd2GYFJeP4o0DjyBg2B3lIXnZhd1GuWnqIQWJDJ7yrjSzX8JCNMnJ24BJ_Yfy5CLqbFny6Kns4kVIA2ofPhDBq_AYV)

The token “2296” for ‘ Red’ (with a leading space and starting with a capital letter) is different from the token “2266” for ‘ red’ with a lowercase letter.

![Tokenizer example splitting “Red is my favorite color.” into color-coded tokens](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-6f07a5c35de10c4616886ae5/16ff17d79fe6e7e7cc561e5a98ec8e6a/4P-Lfk9pc5SwjUw0PqcOrCmT2Tyo1KE86v_xseULCBSbqXA7k2JVEvFMD3ZVu7PxAq0zFf1xV74r3eoou2RONtvZnxAQjHYig1iXYK98up5c-c1lJrMn-N9uxkCHl3MU)

![Tokenizer output with Token IDs selected and a list of token ID numbers](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d5145bd864bf7bd4cdd3612e/0dfceb7c4ab276a4a8c307344f223abb/tWm5ZRDcO4XniG3GnopnJ1lvrKoCxU75Pea3H2Qd8MyGHr-w6Brv4ITnbqpP229XFvz_7m1zOcJnYR0ZXWXlZAJ0x-XUcWucTa3qmcAy5_heEK8NXABMIbmshRNiQjdM)

When ‘Red’ is used in the beginning of a sentence, the generated token does not include a leading space. The token “7738” is different from the previous two examples of the word.

## Observations:

The more probable/frequent a token is, the lower the token number assigned to it:

* The token generated for the period is the same (“13”) in all 3 sentences. This is because, contextually, the period is used pretty similarly throughout the corpus data.
* The token generated for ‘red’ varies depending on its placement within the sentence:

  + Lowercase in the middle of a sentence: ‘ red’ - (token: “2266”)
  + Uppercase in the middle of a sentence: ‘ Red’ - (token: “2297”)
  + Uppercase at the beginning of a sentence: ‘Red’ - (token: “7738”)
