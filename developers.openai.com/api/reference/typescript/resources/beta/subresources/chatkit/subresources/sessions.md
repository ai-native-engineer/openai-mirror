<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/chatkit/subresources/sessions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[ChatKit](/api/reference/typescript/resources/beta/subresources/chatkit)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Sessions

##### [Cancel chat session](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel)

client.beta.chatkit.sessions.cancel(stringsessionID, RequestOptionsoptions?): [ChatSession](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) { id, chatkit\_configuration, client\_secret, 7 more }

POST/chatkit/sessions/{session\_id}/cancel

##### [Create ChatKit session](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/sessions/methods/create)

client.beta.chatkit.sessions.create(SessionCreateParams { user, workflow, chatkit\_configuration, 2 more } body, RequestOptionsoptions?): [ChatSession](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) { id, chatkit\_configuration, client\_secret, 7 more }

POST/chatkit/sessions
