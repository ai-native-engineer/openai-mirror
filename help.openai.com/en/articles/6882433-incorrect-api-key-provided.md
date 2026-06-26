<!-- source: https://help.openai.com/en/articles/6882433-incorrect-api-key-provided -->

# Incorrect API key provided

What to do if you get an Incorrect API key error on the OpenAI API

Updated: 10 days ago

When you get the error message:

```
Incorrect API key provided: sk-*********************************ZXY. You can find your API key at https://platform.openai.com/api-keys
```

Here are a few simple steps you can take to resolve this issue.

1. Check your API key

Check your API key at <https://platform.openai.com/api-keys> and verify it with the API key shown in the error message. Sometimes, the error message may include an old or incorrect API key that you no longer use. Double-check that you are using the correct API key for the request you're making.

1. Verify that you're not using two different API keys

Another possibility is that you may have accidentally used two different API keys. Make sure that you are using the same API key throughout your application or script and not switching between different keys.

1. Ensure you have the right organization set

In some cases, you may need to specify a specific Organization ID when sending a request. Ensure the you follow our [guidelines on authentication](https://platform.openai.com/docs/api-reference/authentication).  
  
If you continue to have issues, please reach out to our support team.
