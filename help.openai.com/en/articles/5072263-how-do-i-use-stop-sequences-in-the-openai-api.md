<!-- source: https://help.openai.com/en/articles/5072263-how-do-i-use-stop-sequences-in-the-openai-api -->

# How do I use stop sequences in the OpenAI API?

Here is what you need to know about the stop sequence parameter in the OpenAI Chat Completions API

Updated: 10 days ago

Stop sequences are used to make the model stop generating tokens at a desired point, such as the end of a sentence or a list. Using the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stop), you can specify the `stop` parameter and pass in the sequence. The model response will not contain the stop sequence and you can pass up to four stop sequences.

## Simple example:

In this [simple chat example](https://platform.openai.com/playground/p/iZJOgr4jX2BgY5CWDE1GBrgw?mode=chat), one stop sequence is used, the word "world". The system message and the user message are designed to try to get the model to output "Hello world"; when the generated text reaches the exact stop sequence "world", the response stops before including that stop sequence, so the returned output is the text before "world" (displayed as "Hello" in the playground).

You can explore additional stop sequence examples using the [OpenAI chat playground](https://platform.openai.com/playground?mode=chat).
