<!-- source: https://openai.com/index/customizing-gpt-3/ -->

December 14, 2021

[Product](/news/product-releases/)

# Customizing GPT‑3 for your application

Fine-tune with a single command.

![Customizing GPT-3](https://images.ctfassets.net/kftzwdyauwt9/3cc7fd12-8d30-4d8f-42c213795288/37e7c8274da5d005c2a078d196423507/Customizing_GPT-3_for_your_application.png?w=3840&q=90&fm=webp)

Developers can now fine-tune GPT‑3 on their own data, creating a custom version tailored to their application. Customizing makes GPT‑3 reliable for a wider variety of use cases and makes running the model cheaper and faster.

You can use an existing dataset of virtually any shape and size, or incrementally add data based on user feedback. With fine-tuning, one API customer was able to increase correct outputs from 83% to 95%. By adding new data from their product each week, another reduced error rates by 50%.

To get started, just run a single command in the OpenAI command line tool with a file you provide. Your custom version will start training and then be available immediately in our API.

* [Read documentation](https://beta.openai.com/docs/guides/fine-tuning)

Last year we [trained GPT‑3⁠(opens in a new window)](https://arxiv.org/abs/2005.14165) and made it available in [our API⁠](/api/). With only a few examples, GPT‑3 can perform a wide variety of [natural language tasks⁠(opens in a new window)](https://beta.openai.com/examples/), a concept called few-shot learning or prompt design. Customizing GPT‑3 can yield even better results because you can provide many more examples than what’s possible with prompt design.

Loading...

It takes less than 100 examples to start seeing the benefits of fine-tuning GPT‑3 and performance continues to improve as you add more data. In [research published last June⁠](/index/improving-language-model-behavior/), we showed how fine-tuning with less than 100 examples can improve GPT‑3’s performance on certain tasks. We’ve also found that each doubling of the number of examples tends to improve quality linearly.

With one of our most challenging research datasets, [grade school math problems⁠](/index/grade-school-math/), fine-tuning GPT‑3 improves accuracy by 2 to 4x over what’s possible with prompt design.

Loading...

Customizing GPT‑3 improves the reliability of output, offering more consistent results that you can count on for production use-cases. One customer found that customizing GPT‑3 reduced the frequency of unreliable outputs from 17% to 5%. Since custom versions of GPT‑3 are tailored to your application, the prompt can be much shorter, reducing costs and improving latency.

Whether text generation, summarization, classification, or any other natural language task GPT‑3 is capable of performing, customizing GPT‑3 will improve performance.

## Apps powered by customized versions of GPT-3

![Keeper Tax mobile interface with post-customized GPT-3](https://images.ctfassets.net/kftzwdyauwt9/fef9ca31-1c0b-4716-59f816f5b3c4/c294a562556da833aacf96a7751707bc/post-customized-gpt3-keeper-tax.png?w=3840&q=90&fm=webp)

**Keeper Tax** helps independent contractors and freelancers with their taxes. After a customer links their financial accounts, Keeper Tax uses various models to extract text and classify transactions. Using the classified data, Keeper Tax identifies easy-to-miss tax write-offs and helps customers file their taxes directly from the app. By customizing GPT‑3, Keeper Tax is able to continuously improve results. Once a week, Keeper Tax adds around 500 new training examples to fine-tune their model, which is leading to about a 1% accuracy improvement each week, increasing accuracy from 85% to 93%.

![Viable web interface with post-customized GPT-3](https://images.ctfassets.net/kftzwdyauwt9/7d212fdf-d304-473b-8001050efaa5/b6fa16c9d38ec465eed8582960a12ba7/post-customized-gpt3-viable.png?w=3840&q=90&fm=webp)

**Viable** helps companies get insights from their customer feedback. By customizing GPT‑3, Viable is able to transform massive amounts of unstructured data into readable natural language reports, highlighting top customer complaints, compliments, requests, and questions. Customizing GPT‑3 has increased the reliability of Viable’s reports. By using a customized version of GPT‑3, accuracy in summarizing customer feedback has improved from 66% to 90%. The result is tangible, intuitive information that customers need to inform their product decisions.

![Sana Labs web interface with post-customized GPT-3](https://images.ctfassets.net/kftzwdyauwt9/2210aa3d-9edd-43f4-cefacf664aa4/ad49d7916fae2d5a875d1f17e9592f30/post-customized-gpt3-sana-labs.png?w=3840&q=90&fm=webp)

**Sana Labs** is a global leader in the development and application of AI to learning. The Sana learning platform powers personalized learning experiences for businesses by leveraging the latest ML breakthroughs to tailor the content for each individual. By customizing GPT‑3 with their data, Sana’s question and content generation went from grammatically correct but general responses to highly accurate outputs. This yielded a 60% improvement, enabling fundamentally more personalized and effective experiences for their learners.

![Post Customized Gpt3 Elicit](https://images.ctfassets.net/kftzwdyauwt9/a6b407b8-9aa9-4a0a-f495dcb70e2e/2be327bc2d6985b78c728ead62349bf4/post-customized-gpt3-elicit.png?w=3840&q=90&fm=webp)

**Elicit** is an AI research assistant that helps people directly answer research questions using findings from academic papers. The tool finds the most relevant abstracts from a large corpus of research papers, then applies a customized version of GPT‑3 to generate the claim (if any) that the paper makes about the question. A custom version of GPT‑3 outperformed prompt design across three important measures: results were easier to understand (a 24% improvement), more accurate (a 17% improvement), and better overall (a 33% improvement).

All API customers can customize GPT‑3 today. Sign-up and get started with the [fine-tuning documentation⁠(opens in a new window)](https://beta.openai.com/docs/guides/fine-tuning).

Loading...

* [ChatGPT](/news/?tags=chatgpt)
* [2021](/news/?tags=2021)

## Authors

Rachel Lim, Michael Wu, Luke Miller

## Related articles

![ Navigating the challenges > Media item](https://images.ctfassets.net/kftzwdyauwt9/3u7r7E3gFRGZIxdKucf7f6/c09e0f83b72d37dc10c1d0563bfc5c33/oai-synthetic-voices.png?w=3840&q=90&fm=webp)

[Navigating the challenges and opportunities of synthetic voices

ProductMar 29, 2024](/index/navigating-the-challenges-and-opportunities-of-synthetic-voices/)

![New Embeddings Models And API Updates](https://images.ctfassets.net/kftzwdyauwt9/ec19d092-e613-41c0-89645a23f8f4/08a818b95c96db1db976afa564602324/new-embeddings-models-and-api-updates.jpg?w=3840&q=90&fm=webp)

[New embedding models and API updates

ProductJan 25, 2024](/index/new-embedding-models-and-api-updates/)

![introducing the gpt store](https://images.ctfassets.net/kftzwdyauwt9/3oQ0LwB3yg3R5isshaaJKi/bf1e997adf17012fceea0feb29d35bf4/introducing_the_gpt_store.jpg?w=3840&q=90&fm=webp)

[Introducing the GPT Store

ProductJan 10, 2024](/index/introducing-the-gpt-store/)
