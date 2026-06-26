<!-- source: https://help.openai.com/en/articles/6614209-how-do-i-check-my-token-usage -->

# How do I check my token usage?

Check your token usage for your API calls

Updated: 2 days ago

There are two main options for checking your token usage:

## 1. Usage dashboard

The [usage dashboard](https://platform.openai.com/usage) displays your API usage during the current and past monthly billing cycles. To display the usage of a particular user of your organizational account, you can use the dropdown next to "Daily usage breakdown".

## 2. Usage data from the API response

You can also access token usage data through the API. Token usage information is included in responses from our endpoints under the usage key.  
  
Here's an example:

```
{  
    "id": "chatcmpl-abc123",  
    "object": "chat.completion",  
    "created": 1677858242,  
    "model": "gpt-3.5-turbo",  
    "usage": {  
        "prompt_tokens": 13,  
        "completion_tokens": 7,  
        "total_tokens": 20  
    },  
    "choices": [  
        {  
            "message": {  
                "role": "assistant",  
                "content": "This is a test!"  
            }  
        }  
    ]  
}
```

If you're using streaming for our completions and would like to access usage data, ensure that your **stream\_options** parameter contains the following:

`stream_options: {"include_usage": true}`. Here's our cookbook for [How to stream completions](https://cookbook.openai.com/examples/how_to_stream_completions#4-how-to-get-token-usage-data-for-streamed-chat-completion-response) and our [platform documentation](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stream_options) on streaming.
