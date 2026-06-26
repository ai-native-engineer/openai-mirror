<!-- source: https://help.openai.com/en/articles/6643167-how-to-use-the-openai-api-for-qa-or-to-build-a-chatbot -->

# How to use the OpenAI API for Q&A or to build a chatbot?

Using the Embeddings and Chat Completions API to create powerful question-answering applications

Updated: 14 days ago

As of May 21 2025, we’ve added new built-in tools to the Responses API—[remote MCP servers](https://platform.openai.com/docs/guides/tools-remote-mcp), Image Generation, Code Interpreter, and an upgraded File Search—along with background mode and encrypted content, so you can build agents that pull richer context and run more reliably. For details, see our [Responses API](https://platform.openai.com/docs/quickstart?api-mode=responses) docs.

The [Embeddings](https://platform.openai.com/docs/guides/embeddings) and [Chat Completions](https://platform.openai.com/docs/guides/text-generation) APIs are a great combination to use when building a question-answering or chatbot application.  
  
Here's how you can get started:

1. Gather all of the information you need for your knowledge base. Use our Embeddings endpoint to make document embeddings for each section.
2. When a user asks a question, turn it into a query embedding and use it to find the most relevant sections from your knowledge base.
3. Use the relevant context from your knowledge base to create a prompt for the Chat Completions endpoint, which can generate an answer for your user.

We encourage you to take a look at our [detailed notebook](https://cookbook.openai.com/examples/question_answering_using_embeddings) that provides step-by-step instructions on setting up embeddings and the Chat Completions API.  
  
If you run into any issues or have questions, don't hesitate to join our  
  
  
[Community Forum](https://community.openai.com/) for help.  
  
We're excited to see what you build!
