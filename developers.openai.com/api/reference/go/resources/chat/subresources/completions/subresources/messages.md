<!-- source: https://developers.openai.com/api/reference/go/resources/chat/subresources/completions/subresources/messages/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Chat](/api/reference/go/resources/chat)

[Completions](/api/reference/go/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Messages

Given a list of messages comprising a conversation, the model will return a response.

##### [Get chat messages](/api/reference/go/resources/chat/subresources/completions/subresources/messages/methods/list)

client.Chat.Completions.Messages.List(ctx, completionID, query) (\*CursorPage[[ChatCompletionStoreMessage](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema))], error)

GET/chat/completions/{completion\_id}/messages
