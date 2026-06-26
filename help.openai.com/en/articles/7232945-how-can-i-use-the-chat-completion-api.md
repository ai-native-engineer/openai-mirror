<!-- source: https://help.openai.com/en/articles/7232945-how-can-i-use-the-chat-completion-api -->

# How can I use the Chat Completion API?

Learn how to get started with the OpenAI Chat Completions API

Updated: 14 days ago

As of May 21 2025, we’ve added new built-in tools to the Responses API—[remote MCP servers](https://platform.openai.com/docs/guides/tools-remote-mcp), Image Generation, Code Interpreter, and an upgraded File Search—along with background mode and encrypted content, so you can build agents that pull richer context and run more reliably. For details, see our [Responses API](https://platform.openai.com/docs/quickstart?api-mode=responses) docs.

Please visit our [developer text generation guide](https://platform.openai.com/docs/guides/text?api-mode=chat) for details for how to use the Chat Completions API. If you want to get started with your first API request to the Chat Completions API, head to our [developer quickstart](https://platform.openai.com/docs/quickstart?api-mode=chat). Please find the comparison between capabilities supported in the Responses API and Completions API [here](https://platform.openai.com/docs/guides/responses-vs-chat-completions). We recommend using Responses API, unless is it lacking capabilities that Completions API offers.  
  
  
**Does OpenAI store the data that is passed into the API?**  
  
As of March 1st, 2023, we retain customer API data for 30 days but no longer use customer data sent via the API to improve our models. You can learn more about our [Enterprise privacy](https://openai.com/enterprise-privacy/) page.  
  
  
**How do I keep the Chat session focused on a topic?**  
  
Use developer instructions to set the assistant's topic, role, and constraints. Developer messages are prioritized above user messages, and you can learn more about ways to steer the session topic under [message role and instruction following](https://platform.openai.com/docs/guides/text#message-roles-and-instruction-following).  
  
  
**What's the rate limits for the Chat Completions API?**  
  
The rate limit for the Chat Completions API depends on what model you are using. Head to our [rate limits guide](https://platform.openai.com/docs/guides/rate-limits) or your [limits page](https://platform.openai.com/account/limits) for details on the limits.
