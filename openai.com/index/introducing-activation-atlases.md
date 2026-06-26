<!-- source: https://openai.com/index/introducing-activation-atlases/ -->

March 6, 2019

[Publication](/research/index/publication/)

# Introducing Activation Atlases

[Read paper(opens in a new window)](https://distill.pub/2019/activation-atlas/)[(opens in a new window)](https://github.com/tensorflow/lucid/#activation-atlas-notebooks)[Try demo(opens in a new window)](https://distill.pub/2019/activation-atlas/app.html)

![Introducing Activation Atlases](https://images.ctfassets.net/kftzwdyauwt9/b34269e0-a42b-44bd-478f46bf97c4/596c1fd1f91833900a3a6c1f1b08667f/image-22.webp?w=3840&q=90&fm=webp)

We’ve created [*activation atlases*⁠(opens in a new window)](https://distill.pub/2019/activation-atlas) (in [collaboration⁠(opens in a new window)](https://ai.googleblog.com/2019/03/exploring-neural-networks.html) with Google researchers), a new technique for visualizing what interactions between neurons can represent. As AI systems are deployed in increasingly sensitive contexts, having a better understanding of their internal decision-making processes will let us identify weaknesses and investigate failures.

Modern neural networks are [often⁠(opens in a new window)](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/) [criticized⁠(opens in a new window)](https://www.nytimes.com/2017/11/21/magazine/can-ai-be-taught-to-explain-itself.html) as being a “black box.” Despite their success at a variety of problems, we have a limited understanding of how they make decisions internally. Activation atlases are a new way to see some of what goes on inside that box.

![Visualization of an image atlas](https://images.ctfassets.net/kftzwdyauwt9/e8983184-36f0-4b5b-971757756ba0/57ca9f8026e727185c1087636361112d/atlas-jpg-80.jpg?w=3840&q=90&fm=webp)

Activation atlases build on feature visualization, a technique for studying what the hidden layers of neural networks can represent. [Early⁠(opens in a new window)](https://pdfs.semanticscholar.org/65d9/94fb778a8d9e0f632659fb33a082949a50d3.pdf) [work⁠(opens in a new window)](https://arxiv.org/pdf/1312.6034v2.pdf) in feature visualization primarily focused on [individual neurons⁠(opens in a new window)](https://distill.pub/2017/feature-visualization/). By collecting hundreds of thousands of examples of neurons interacting and visualizing those, activation atlases move from individual neurons to visualizing the space those neurons jointly represent.

![Visualization of an image mapping process](https://images.ctfassets.net/kftzwdyauwt9/8cf29c43-9a72-49b6-2ff4cdda2da9/3307ed75446f4f58b27908f4d78af725/process.png?w=3840&q=90&fm=webp)

Understanding what’s going on inside neural nets isn’t solely a question of scientific curiosity—our lack of understanding handicaps our ability to audit neural networks and, in high stakes contexts, ensure they are safe. Normally, if one was going to deploy a critical piece of software one could review all the paths through the code, or even do formal verification, but with neural networks, our ability to do this kind of review has presently been much more limited. With activation atlases humans can discover unanticipated issues in neural networks—for example, places where the network is relying on spurious correlations to classify images, or where re-using a feature between two classes leads to strange bugs. Humans can even use this understanding to “[attack⁠(opens in a new window)](https://arxiv.org/pdf/1312.6199.pdf)” the model, modifying images to fool it.

For example, a special kind of activation atlas can be created to show how a network tells apart frying pans and woks. Many of the things we see are what one expects. Frying pans are more squarish, while woks are rounder and deeper. But it also seems like the model has learned that frying pans and woks can also be distinguished by food around them—in particular, wok is supported by the presence of noodles. Adding noodles to the corner of the image will fool the model 45% of the time! This is similar to work like [adversarial patches⁠(opens in a new window)](https://arxiv.org/pdf/1712.09665.pdf), but based on human understanding.

![Wok Atlas](https://images.ctfassets.net/kftzwdyauwt9/f7db0d72-d631-44cb-9c7b8e15a3fb/9f995c253caceafed6874b009c181368/wok-atlas.png?w=3840&q=90&fm=webp)

Other human-designed attacks based on the network overloading certain feature detectors are often more effective (some succeed as often as 93% of the time). But the noodle example is particularly interesting because it’s a case of the model picking up on something that is correlated, but not causal, with the correct answer. This has structural similarities to types of errors we might be particularly worried about, such as fairness and bias issues.

Activation atlases worked better than we anticipated and seem to strongly suggest that neural network activations can be meaningful to humans. This gives us increased optimism that it is possible to achieve interpretability in vision models in a strong sense.

We’re excited to have done this work in [collaboration⁠(opens in a new window)](https://ai.googleblog.com/2019/03/exploring-neural-networks.html) with researchers at Google. We believe that working together on safety-relevant research helps us all ensure the best outcome for society as AI research progresses.

*Want to make neural networks not be a black box?* [*Apply*⁠](/careers/) *to work at OpenAI.*

* [Ethics & Safety](/research/index/?tags=ethics-safety)
* [Language](/research/index/?tags=language)

## Authors

Chris Olah, Ludwig Schubert

## Acknowledgments

Thanks to our co-authors at Google: Shan Carter, Zan Armstrong and Ian Johnson.

Thanks to Greg Brockman, Dario Amodei, Jack Clark and Ashley Pilipiszyn for feedback on this blog post.

We also thank Christian Howard for his help in coordination from the Google side, Phillip Isola for being Distill’s acting editor and Arvind Satyanarayan for feedback on our paper.

## Related articles

![Disrupting malicious > media](https://images.ctfassets.net/kftzwdyauwt9/5080983d-9c4d-4479-17e421d7380a/0b42f77c2478bc5bc7bde3fddfc68462/45.png?w=3840&q=90&fm=webp)

[Disrupting malicious uses of AI by state-affiliated threat actors

SecurityFeb 14, 2024](/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)

![](https://images.ctfassets.net/kftzwdyauwt9/ec66425e-99ca-4314-d04b087f8727/de7341b6a5281c2a220b93a737ce19b0/building-an-early-warning-system-for-llm-aided-biological-threat-creation.jpg?w=3840&q=90&fm=webp)

[Building an early warning system for LLM-aided biological threat creation

PublicationJan 31, 2024](/index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/)

![Democratic Inputs To AI Grant Program Update](https://images.ctfassets.net/kftzwdyauwt9/f50ce1d2-4f61-4ed2-e560c624d631/6f4dd4542898a35d0a91b137f85c9834/Democratic_inputs_to_AI_grant_program_lessons_learned_and_implementation_plans.jpg?w=3840&q=90&fm=webp)

[Democratic inputs to AI grant program: lessons learned and implementation plans

SafetyJan 16, 2024](/index/democratic-inputs-to-ai-grant-program-update/)
