<!-- source: https://openai.com/index/unsupervised-sentiment-neuron/ -->

April 6, 2017

[Publication](/research/index/publication/)

# Unsupervised sentiment neuron

We’ve developed an unsupervised system which learns an excellent representation of sentiment, despite being trained only to predict the next character in the text of Amazon reviews.

[(opens in a new window)](https://arxiv.org/abs/1704.01444)[(opens in a new window)](https://github.com/openai/generating-reviews-discovering-sentiment)

![Unsupervised Sentiment Neuron](https://images.ctfassets.net/kftzwdyauwt9/02933f53-8bbc-47d2-353690b73e22/cb1239b6bd5b5164e96d6571528443cf/unsupervised-sentiment-neuron.jpg?w=3840&q=90&fm=webp)

Illustration: Ludwig Pettersson

A [linear model⁠](/index/unsupervised-sentiment-neuron/#methodology) using this representation achieves state-of-the-art sentiment analysis accuracy on a small but extensively-studied dataset, the Stanford Sentiment Treebank (we get 91.8% accuracy versus the previous best of 90.2%), and can match the performance of previous supervised systems using 30-100x fewer labeled examples. Our representation also contains a distinct “[sentiment neuron⁠](/index/unsupervised-sentiment-neuron/#sentimentneuron)” which contains almost all of the sentiment signal.

Our system beats other approaches on Stanford Sentiment Treebank while using dramatically less data.

![Graph of labelled training examples](https://images.ctfassets.net/kftzwdyauwt9/91470318-4e2e-453a-28b0fbd62477/d4c711efe2460409193dac290577786b/image00.png?w=3840&q=90&fm=webp)

The number of labeled examples it takes two variants of our model (the green and blue lines) to match fully supervised approaches, each trained with 6,920 examples (the dashed gray lines). Our L1-regularized model (pretrained in an unsupervised fashion on Amazon reviews) matches [multichannel CNN]([https://arxiv.org/abs/1408.5882⁠(opens in a new window)](https://arxiv.org/abs/1408.5882)) performance with only 11 labeled examples, and state-of-the-art CT-LSTM Ensembles with 232 examples.

We were very surprised that our model learned an interpretable feature, and that simply [predicting⁠(opens in a new window)](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) the next character in Amazon reviews resulted in discovering the concept of sentiment. We believe the phenomenon is not specific to our model, but is instead a general property of certain large neural networks that are trained to predict the next step or dimension in their inputs.

## Methodology

We first trained a [multiplicative LSTM⁠(opens in a new window)](https://arxiv.org/abs/1609.07959) with 4,096 units on a corpus of 82 million Amazon reviews to predict the next character in a chunk of text. Training took one month across four NVIDIA Pascal GPUs, with our model processing 12,500 characters per second.

These 4,096 units (which are just a vector of floats) can be regarded as a feature vector representing the string read by the model. After training the mLSTM, we turned the model into a sentiment classifier by taking a linear combination of these units, learning the weights of the combination via the available supervised data.

## Sentiment neuron

While training the linear model with L1 regularization, we noticed it used surprisingly few of the learned units. Digging in, we realized there actually existed a single “sentiment neuron” that’s highly predictive of the sentiment value.

![Graph depicting positive and negative reviews of the value of the sentiment neuron](https://images.ctfassets.net/kftzwdyauwt9/31d10395-5a1b-40a5-c2411a224af0/3b42eaab6952a05b26091152b7cfafa7/image03-1.png?w=3840&q=90&fm=webp)

Just like with similar models, our model can be used to generate text. Unlike those models, we have a direct dial to control the sentiment of the resulting text: we simply overwrite the value of the sentiment neuron.

Loading...

## Example

The diagram below represents the character-by-character value of the sentiment neuron, displaying negative values as red and positive values as green. Note that strongly indicative words like “*best*” or “*horrendous*” cause particularly big shifts in the color.

![Sentiment Prediction](https://images.ctfassets.net/kftzwdyauwt9/06ccc782-4db8-43fc-3019f97272b4/d50a20f42a6ddd241beb6f185dee1987/sentiment-prediction.png?w=3840&q=90&fm=webp)

The sentiment neuron adjusting its value on a character-by-character basis.

It’s interesting to note that the system also makes large updates after the completion of sentences and phrases. For example, in “*And about 99.8 percent of that got lost in the film*”, there’s a negative update after “*lost*” and a larger update at the sentence’s end, even though “*in the film*” has no sentiment content on its own.

## Unsupervised learning

Labeled data are the fuel for today’s machine learning. Collecting data is easy, but scalably labeling that data is hard. It’s only feasible to generate labels for important problems where the reward is worth the effort, like machine translation, speech recognition, or self-driving.

Machine learning researchers have long dreamed of developing [unsupervised⁠(opens in a new window)](https://en.wikipedia.org/wiki/Word2vec) [learning⁠(opens in a new window)](https://arxiv.org/abs/1506.06726) [algorithms⁠(opens in a new window)](http://www.mitpressjournals.org/doi/pdfplus/10.1162/neco.2006.18.7.1527) [to⁠(opens in a new window)](http://www-cs.stanford.edu/~acoates/papers/coatesng_nntot2012.pdf) [learn⁠(opens in a new window)](https://arxiv.org/abs/1505.05192) a good representation of a dataset, which can then be used to solve tasks using only a few labeled examples. Our research implies that simply training large unsupervised next-step-prediction models on large amounts of data may be a good approach to use when creating systems with good representation learning capabilities.

## Next steps

Our results are a promising step towards general unsupervised representation learning. We found the results by exploring whether we could learn good quality representations as a side effect of language modeling, and scaled up an existing model on a carefully-chosen dataset. Yet the underlying phenomena remain more mysterious than clear.

* These results were not as strong for datasets of long documents. We suspect our character-level model struggles to remember information over hundreds to thousands of timesteps. We think it’s worth trying hierarchical models that can adapt the timescales at which they operate. Further scaling up these models may further improve representation fidelity and performance on sentiment analysis and similar tasks.
* The model struggles the more the input text diverges from review data. It’s worth verifying that broadening the corpus of text samples results in an equally informative representation that also applies to broader domains.
* Our results suggest that there exist settings where very large next-step-prediction models learn excellent unsupervised representations. Training a large neural network to predict the next frame in a large collection of videos may result in unsupervised representations for object, scene, and action classifiers.

Overall, it’s important to understand the properties of models, training regimes, and datasets that reliably lead to such excellent representations.

* [Generative Models](/research/index/?tags=generative-models)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Language](/research/index/?tags=language)

## Authors

Alec Radford, Ilya Sutskever, Rafał Józefowicz, Jack Clark, Greg Brockman

## Acknowledgments

Artwork: Ludwig Pettersson

## Related articles

![Three farmers using a mobile app outside](https://images.ctfassets.net/kftzwdyauwt9/7b26cc3b-46d8-45b0-f67f6de0c8f8/8bc94d083a5a147609cddad159243ef7/digital_green.png?w=3840&q=90&fm=webp)

[Building agricultural database for farmers

Jan 12, 2024](/index/digital-green/)

![Wix cover image](https://images.ctfassets.net/kftzwdyauwt9/6E3QyNLzuWwK3EGBHPw7nQ/fbd0c5a34cc4f4ba096028adbdda8934/oai_Wix_1x1.png?w=3840&q=90&fm=webp)

[Creating websites in minutes with AI Website Builder

May 29, 2025](/index/wix/)

![WHOOP Coach HIIT](https://images.ctfassets.net/kftzwdyauwt9/163d4817-6436-4d20-83e0963f68f1/ef4bec09f31b32f8ca8a953a09da5897/whoop.png?w=3840&q=90&fm=webp)

[Delivering LLM-powered health solutions

Jan 4, 2024](/index/whoop/)
