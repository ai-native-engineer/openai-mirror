<!-- source: https://help.openai.com/en/articles/7127987-what-is-the-difference-between-prompt-tokens-and-completion-tokens -->

# What is the difference between prompt tokens and completion tokens?

What is the difference between input and output tokens?

Updated: 2 days ago

As of March 11, 2025, we’ve released the building blocks of our new Agents platform. For details, see our API docs for our [Responses API](https://platform.openai.com/docs/quickstart?api-mode=responses), Tools including [Web Search](https://platform.openai.com/docs/guides/tools-web-search), [File Search](https://platform.openai.com/docs/guides/tools-file-search), and [Computer Use](https://platform.openai.com/docs/guides/tools-computer-use), and our [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk#page-top) with [Tracing](https://platform.openai.com/docs/guides/agents-sdk#tracing).

Prompt tokens are the tokens that you input into the model. This is the number of tokens in your prompt.  
  
Completion tokens are any tokens that the model generates in response to your input. For a standard request, this is the number of tokens in the completion.  
  
Most models we offer have both limits on the number of tokens that they can take in (prompt tokens) and on the number of tokens they an output (completion or samples tokens).

This also includes any tokens generated when using a higher value of `best_of` or `n`. For example, if you are generating 3 candidate completions using `best_of = 3`, the number of sampled tokens will be at most `3 * max_tokens`.

You can read more about managing tokens in our [text generation guide](https://platform.openai.com/docs/guides/text-generation/managing-tokens).
