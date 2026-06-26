<!-- source: https://openai.com/index/weight-normalization/ -->

February 25, 2016

[Publication](/research/index/publication/)

# Weight normalization: A simple reparameterization to accelerate training of deep neural networks

[Read paper(opens in a new window)](https://arxiv.org/abs/1602.07868)

![Weight Normalization A Simple Reparameterization To Accelerate Training Of Deep Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/44a6d247-bfec-43f6-e13d229a9468/f6bb97a5863649686a20688e5e72a882/weight-normalization-a-simple-reparameterization-to-accelerate-training-of-deep-neural-networks.png?w=3840&q=90&fm=webp)

## Abstract

We present weight normalization: a reparameterization of the weight vectors in a neural network that decouples the length of those weight vectors from their direction. By reparameterizing the weights in this way we improve the conditioning of the optimization problem and we speed up convergence of stochastic gradient descent. Our reparameterization is inspired by batch normalization but does not introduce any dependencies between the examples in a minibatch. This means that our method can also be applied successfully to recurrent models such as LSTMs and to noise-sensitive applications such as deep reinforcement learning or generative models, for which batch normalization is less well suited. Although our method is much simpler, it still provides much of the speed-up of full batch normalization. In addition, the computational overhead of our method is lower, permitting more optimization steps to be taken in the same amount of time. We demonstrate the usefulness of our method on applications in supervised image recognition, generative modelling, and deep reinforcement learning.

* [Exploration & Games](/research/index/?tags=exploration-game)

## Authors

Tim Salimans, Durk Kingma

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
