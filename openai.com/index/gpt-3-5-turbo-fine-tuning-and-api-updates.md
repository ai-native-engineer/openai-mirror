<!-- source: https://openai.com/index/gpt-3-5-turbo-fine-tuning-and-api-updates/ -->

August 22, 2023

[Product](/news/product-releases/)

# GPT‑3.5 Turbo fine-tuning and API updates

Developers can now bring their own data to customize GPT‑3.5 Turbo for their use cases.

![Gpt 3.5 Turbo Fine Tuning And Api Updates](https://images.ctfassets.net/kftzwdyauwt9/d8d965fd-e54c-4c9b-b77f086f24ee/c39acb6b8a13b59ed54006d957b9250f/gpt-3-5-turbo-fine-tuning-and-api-updates.png?w=3840&q=90&fm=webp)

Fine-tuning for GPT‑3.5 Turbo is now available, with fine-tuning for GPT‑4 coming this fall. This update gives developers the ability to customize models that perform better for their use cases and run these custom models at scale. Early tests have shown a fine-tuned version of GPT‑3.5 Turbo can match, or even outperform, base GPT‑4‑level capabilities on certain narrow tasks. As with all our APIs, data sent in and out of the fine-tuning API is owned by the customer and is [not used by OpenAI⁠](/api-data-privacy/), or any other organization, to train other models.

## Fine-tuning use cases

Since the release of GPT‑3.5 Turbo, developers and businesses have asked for the ability to customize the model to create unique and differentiated experiences for their users. With this launch, developers can now run supervised fine-tuning to make this model perform better for their use cases.

In our private beta, fine-tuning customers have been able to meaningfully improve model performance across common use cases, such as:

* **Improved steerability**: Fine-tuning allows businesses to make the model follow instructions better, such as making outputs terse or always responding in a given language. For instance, developers can use fine-tuning to ensure that the model always responds in German when prompted to use that language.
* **Reliable output formatting:** Fine-tuning improves the model's ability to consistently format responses—a crucial aspect for applications demanding a specific response format, such as code completion or composing API calls. A developer can use fine-tuning to more reliably convert user prompts into high-quality JSON snippets that can be used with their own systems.
* **Custom tone:** Fine-tuning is a great way to hone the qualitative feel of the model output, such as its tone, so it better fits the voice of businesses’ brands. A business with a recognizable brand voice can use fine-tuning for the model to be more consistent with their tone.

In addition to increased performance, fine-tuning also enables businesses to **shorten their prompts** while ensuring similar performance.  Fine-tuning with GPT‑3.5‑Turbo can also handle 4k tokens—double our previous fine-tuned models. Early testers have reduced prompt size by up to 90% by fine-tuning instructions into the model itself, speeding up each API call and cutting costs.

Fine-tuning is most powerful when combined with [other techniques⁠(opens in a new window)](https://platform.openai.com/docs/guides/gpt-best-practices) such as prompt engineering, information retrieval, and function calling. Check out our [fine-tuning guide⁠(opens in a new window)](https://platform.openai.com/docs/guides/fine-tuning) to learn more. Support for fine-tuning with function calling and `gpt-3.5-turbo-16k` will be coming later this fall.

Loading...

## Safety

It is very important to us that the deployment of fine-tuning is safe. To preserve the default model's safety features through the  fine-tuning process, fine-tuning training data is passed through our Moderation API and a GPT‑4 powered moderation system to detect unsafe training data that conflict with our safety standards.

## Pricing

Fine-tuning costs are broken down into two buckets: the initial training cost and usage cost:

* Training: $0.008 / 1K Tokens
* Usage input: $0.012 / 1K Tokens
* Usage output: $0.016 / 1K Tokens

For example, a `gpt-3.5-turbo` fine-tuning job with a training file of 100,000 tokens that is trained for 3 epochs would have an expected cost of $2.40.

## Updated GPT-3 models

In July, [we announced⁠](/index/gpt-4-api-general-availability/) that the original GPT‑3 base models (`ada`, `babbage`, `curie`, and `davinci`) would be turned off on January 4th, 2024. Today, we are making `babbage-002` and `davinci-002` available as replacements for these models, either as base or fine-tuned models. Customers can access those models by querying the [Completions API⁠(opens in a new window)](https://platform.openai.com/docs/api-reference/completions).

These models can be fine-tuned with our new API endpoint `/v1/fine_tuning/jobs`. This new endpoint offers pagination and more extensibility to support the future evolution of the fine-tuning API. Transitioning from `/v1/fine-tunes` to the updated endpoint is straightforward and more details can be found in our new [fine-tuning guide⁠(opens in a new window)](https://platform.openai.com/docs/guides/fine-tuning). This deprecates the old `/v1/fine-tunes` endpoint, which will be turned off on January 4th, 2024.

Pricing for base and fine-tuned GPT‑3 models is as follows:

Loading...

* [API Platform](/news/?tags=api-platform)
* [ChatGPT](/news/?tags=chatgpt)
* [2023](/news/?tags=2023)

## Authors

Andrew Peng, Michael Wu, John Allard, Logan Kilpatrick, Steven Heidel

## Acknowledgments

Andrea Vallone, Arvind Neelakantan, Cindy Yong, Colin Jarvis, Denny Jin, Florencia Leoni Aleman, Henry Head, Ilan Bigio, Jeff Harris, Jessica Shieh, Juston Forte, Kim Malfacini, Lauren Workman, Lilian Weng, Olivier Godement, Sherwin Wu, Shyamal Anadkat, Vik Goel, Yuchen He

## Related articles

![Jetbrains > Hero > Media item > Asset](https://images.ctfassets.net/kftzwdyauwt9/46d99f08-c849-4c73-5a6c7b83ea9c/6e0eaaaf815df2a53f997b36ce57ad13/jetbrains.png?w=3840&q=90&fm=webp)

[Embedding AI into developer software

Mar 21, 2024](/index/jetbrains/)

![Unload](https://images.ctfassets.net/kftzwdyauwt9/15d768b2-bd52-4e68-bebaf96d50b3/e3f414371811a69d73091cc36a44ce8f/holiday_extras.png?w=3840&q=90&fm=webp)

[Building a data-driven, efficient culture with AI

Mar 18, 2024](/index/holiday-extras/)

![Screenshot 2024 03 12 At 1128 27am](https://images.ctfassets.net/kftzwdyauwt9/e4cda57a-c977-4855-16b96e288c99/40db1a7d78522f9f9030942dd4a3e72b/superhuman.png?w=3840&q=90&fm=webp)

[Reimagining the email experience with AI

Mar 18, 2024](/index/superhuman/)
