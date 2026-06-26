<!-- source: https://help.openai.com/en/articles/7042661-moving-from-completions-to-chat-completions-in-the-openai-api -->

# Moving from Completions to Chat Completions in the OpenAI API

How to get migrate from the legacy OpenAI Completions API to Chat Completions

Updated: 10 days ago

Chat Completions is the standard API to use with OpenAI's latest models. You can learn about getting started with it using our [text generation developer guide](https://platform.openai.com/docs/guides/text-generation).  
  
As of March 11, 2025, we’ve released the building blocks of our new Agents platform. For details, see our API docs for our [Responses API](https://platform.openai.com/docs/quickstart?api-mode=responses), Tools including [Web Search](https://platform.openai.com/docs/guides/tools-web-search), [File Search](https://platform.openai.com/docs/guides/tools-file-search), and [Computer Use](https://platform.openai.com/docs/guides/tools-computer-use), and our [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk#page-top) with [Tracing](https://platform.openai.com/docs/guides/agents-sdk#tracing).

### Prompts to Messages

To have a more interactive and dynamic conversation with our models, you can use messages in chat formate instead of the legacy prompt-style used with completions.  
  
Here's how it works:

* Instead of sending a single string as your prompt, you send a list of messages as your input.
* Each message has a `role` and `content`.
* Common roles include `system`, `user`, `assistant`, `developer`, and `tool`. Tool messages are used for tool/function results and must correspond to assistant tool calls. For backward compatibility, function messages may still be accepted and converted to tool messages in server handling. Developer messages may be remapped depending on model support.
* The `content` contains the text of the message from the role.
* The system instruction can give high level instructions for the conversation
* The messages are processed in the order they appear in the list, and the assistant responds accordingly.

Even basic Completions requests can be completed through Chat Completions, as you can see below:

| **Then** | **Now** | | `'prompt' : 'tell me a joke'` | `'messages':` <br>`[{'role':'user', 'content':'tell me a joke'}]` |

Now, it is easier than ever to have back-and-forths with the model by extending the list of messages in the conversation.

```
'messages': [{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'why did the chicken cross the road'},   
{'role':'user', 'content':'I don't know, why did the chicken cross the road'}]
```

### System Instructions

You can also use a system level instruction to guide the model's behavior throughout the conversation. For example, using a system instruction and a message like this

```
'messages': [{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},   
{'role':'user', 'content':'tell me a joke'},
```

will result in something like

```
{...  
'message': {'role':'assistant',  
              'content':'Why did the chicken cross the road? To get to the other side, but verily, the other side was full of peril and danger, so it quickly returned from whence it came, forsooth!'}  
...}
```

If you want to explore options that don't involve hanging to manage the message conversation history yourself, check out the [Assistants API](https://platform.openai.com/docs/assistants/overview).
