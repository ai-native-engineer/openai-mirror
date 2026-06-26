<!-- source: https://openai.com/index/extensions-and-limitations-of-the-neural-gpu/ -->

November 2, 2016

[Publication](/research/index/publication/)

# Extensions and limitations of the neural GPU

[Read paper(opens in a new window)](https://arxiv.org/abs/1611.00736)

![Extensions And Limitations Of The Neural Gpu](https://images.ctfassets.net/kftzwdyauwt9/19ccf94c-6cba-41fd-6db550d64966/c3a04ac501f99577f6d6766e2a27e068/image-13.webp?w=3840&q=90&fm=webp)

## Abstract

The Neural GPU is a recent model that can learn algorithms such as multi-digit binary addition and binary multiplication in a way that generalizes to inputs of arbitrary length. We show that there are two simple ways of improving the performance of the Neural GPU: by carefully designing a curriculum, and by increasing model size. The latter requires a memory efficient implementation, as a naive implementation of the Neural GPU is memory intensive. We find that these techniques increase the set of algorithmic problems that can be solved by the Neural GPU: we have been able to learn to perform all the arithmetic operations (and generalize to arbitrarily long numbers) when the arguments are given in the decimal representation (which, surprisingly, has not been possible before). We have also been able to train the Neural GPU to evaluate long arithmetic expressions with multiple operands that require respecting the precedence order of the operands, although these have succeeded only in their binary representation, and not with perfect accuracy. In addition, we gain insight into the Neural GPU by investigating its failure modes. We find that Neural GPUs that correctly generalize to arbitrarily long numbers still fail to compute the correct answer on highly-symmetric, atypical inputs: for example, a Neural GPU that achieves near-perfect generalization on decimal multiplication of up to 100-digit long numbers can fail on 000000…002×000000…002 while succeeding at 2×2. These failure modes are reminiscent of adversarial examples.

* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Eric Price, Wojciech Zaremba, Ilya Sutskever

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
