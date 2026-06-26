<!-- source: https://help.openai.com/en/articles/6643200-why-am-i-getting-different-completions-on-playground-vs-the-api -->

# Why am I getting different completions on Playground vs. the API?

Troubleshooting discrepancies between completions

Updated: 14 days ago

If your **temperature** is set above 0, the model will generate outputs with some randomness, so seeing different completions is expected. When you want consistent, repeatable results, use **temperature = 0**.  
  
If temperature is already 0 and results still differ, here are the most common causes:  
  
---

## Prompt differences

Check that the prompt is **exactly the same** in both environments. Even a single extra space, newline, or hidden character can cause a different output.  
  
---

## Parameter mismatches

Ensure that all relevant parameters match between Playground and API requests:

* `temperature`
* `top_p`
* `max_tokens`
* `frequency_penalty`
* `presence_penalty`

Also confirm that the **model name** is identical. Different models will naturally produce different outputs, even with the same prompt and settings.  
  
---

## Playground presets vs. API defaults

Playground may apply certain default settings. In the API, if you omit a parameter, it will use its own default, which might not match Playground behavior. To ensure consistency, **explicitly set all parameters in your API request**.  
  
---

## Formatting or encoding differences

Ensure that the request you send to the API is **identical** to the prompt in Playground. Differences can occur from:

* JSON escaping
* Line endings or indentation
* Extra whitespace

If you've double-checked all of these things and are still seeing discrepancies, ask for help on the [**Community Forum**](https://community.openai.com/), where users may have experienced similar issues or may be able to assist in troubleshooting your specific case.
