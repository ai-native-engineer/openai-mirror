<!-- source: https://help.openai.com/en/articles/5428082-how-to-incorporate-a-safety-identifier -->

# How to Incorporate a Safety Identifier

Updated: 14 days ago

The OpenAI [Safety Best Practices](https://platform.openai.com/docs/guides/safety-best-practices) are intended to limit the possibility of misuse.

Sending safety identifiers in your requests can be a useful tool to help OpenAI monitor and detect abuse. This allows OpenAI to provide your team with more actionable feedback in the event that we detect any policy violations in your application.  
  
A safety identifier should be a string that uniquely identifies each user. Hash the username or email address in order to avoid sending us any identifying information. If you offer a preview of your product to non-logged in users, you can send a session ID instead.

The safety identifier supersedes the previous `user` parameter which was previously present for the same purpose.

Include safety identifiers in your API requests with the `safety_identifier` parameter:

### Python — Chat Completions API

```
from openai import OpenAI  
client = OpenAI()  
  
response = client.chat.completions.create(  
  model="gpt-5-mini",  
  messages=[  
    {"role": "user", "content": "This is a test"}  
  ],  
  safety_identifier="user_123456"  
)
```

### Python — Responses API

```
from openai import OpenAI  
client = OpenAI()  
  
response = client.responses.create(  
  model="gpt-5-mini",  
  input="This is a test",  
  safety_identifier="user_123456"  
)
```
