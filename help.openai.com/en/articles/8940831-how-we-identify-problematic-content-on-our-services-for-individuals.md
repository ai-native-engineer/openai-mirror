<!-- source: https://help.openai.com/en/articles/8940831-how-we-identify-problematic-content-on-our-services-for-individuals -->

# How we identify problematic content on our services for individuals

Updated: 3 days ago

We believe in responsible, iterative development and deployment as a means to achieving safe artificial general intelligence. We do a considerable amount of safety and alignment [testing](https://openai.com/blog/red-teaming-network) and [mitigation](https://openai.com/blog/our-approach-to-alignment-research) before ever launching a model to the public, and we also have automated and human systems in place to help detect problematic content that appears on our services for individuals such as ChatGPT and GPTs. We outline some of those efforts below.

# ChatGPT and ImageGen

We use automated tools, such as an internal version of our [/moderations API](https://platform.openai.com/docs/api-reference/moderations), to detect content (prompts, completions, uploads) that may be harmful or violate our Usage Policies. If we detect problematic content, we’ll typically either warn you that your content may violate our usage policies or block the model from responding to your prompt. We may also prevent the chat with the problematic prompt or completion from being shared. In a very limited set of circumstances, we may also ban your account for egregious behavior.  
  
We also accept human reports of problematic content on ChatGPT. We use a combination of automated systems and a trained team of experts to review these reports.

* **ChatGPT**: If someone shares a chat that you believe to contain problematic content, you can also [report it to us](/en/articles/7943618-how-do-i-report-harmful-or-illegal-content-in-a-shared-link).

For more details on how to report content directly in ChatGPT, see [this article](/en/articles/8940836-how-to-report-content).

# GPTs

We also use automated tools such as our [/moderation API](https://platform.openai.com/docs/api-reference/moderations) to see if a GPT is potentially problematic. If we detect problematic content associated with the GPT, we’ll take action, such as preventing it from being distributed. The builder is able to edit the configuration of the GPT or API to remove the problematic content or can appeal the decision through an in-product flow. In a very limited set of circumstances, we may also ban the builder’s account for egregious behavior.  
  
We also accept human reports of problematic GPTs. If you see a GPT that you believe to be violating our usage policies or otherwise reflect problematic content, you can also [report it to us](/en/articles/8554982-how-should-i-report-a-gpt). We use a combination of automated systems and a trained team of experts to review these reports.
