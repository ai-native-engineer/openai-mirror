<!-- source: https://openai.com/index/measuring-goodharts-law/ -->

April 13, 2022

[Publication](/research/index/publication/)

# Measuring Goodhart’s law

![Measuring Goodhart’s Law](https://images.ctfassets.net/kftzwdyauwt9/bc7398a0-41a2-49ac-550027540010/5da5f59157a3accae2bc9bd28fd47177/image-11.webp?w=3840&q=90&fm=webp)

Goodhart’s law famously says: “When a measure becomes a target, it ceases to be a good measure.” Although originally from economics, it’s something we have to grapple with at OpenAI when figuring out how to optimize objectives that are difficult or costly to measure.

[Goodhart’s law⁠(opens in a new window)](https://en.wikipedia.org/wiki/Goodhart%27s_law) famously says: “When a measure becomes a target, it ceases to be a good measure.” Although originally from economics, it’s something we have to grapple with at OpenAI when figuring out how to optimize objectives that are difficult or costly to measure. It’s often necessary to introduce some **proxy objective** that’s easier or cheaper to measure, but when we do this, we need to be careful not to optimize it too much.

For example, as part of our work to [align⁠](/alignment/) models like GPT‑3 with human intent and values, we would like to optimize things like “How [helpful⁠](/index/instruction-following/) is this response?”, or “How [factually accurate⁠](/index/webgpt/) is this claim?”. These are complex objectives that require humans to carefully check things over. For this reason, we train a model to predict these human preferences, known as a **reward model**, and use the reward model’s predictions as a proxy objective. But it’s important to keep track of how well the true objective is being optimized.

In this post we’ll look at some of the mathematics behind how we do this. We’ll focus on a setting that is particularly clean to analyze, in which we have access to the true objective. In practice, even human preferences can fail to measure what we really care about, but we’re setting that issue aside in this post.

## Best-of-n sampling

There are many ways in which one could optimize the proxy objective, but perhaps the simplest is **best-of-n n n sampling**, also known as **rejection sampling** or **reranking**. We simply sample n times and take the one that scores the highest according to the proxy objective.

Although this method is very simple, it can actually be competitive with more advanced techniques such as reinforcement learning, albeit at the cost of more inference-time compute. For example, in [WebGPT⁠](/index/webgpt/), our best-of-64 model outperformed our reinforcement learning model, perhaps in part because the best-of-64 model got to browse many more websites. Even applying best-of-4 provided a significant boost to human preferences.

In addition, best-of-n n n sampling has reliable performance and is straightforward to analyze mathematically, making it well-suited to empirical studies of Goodhart’s law and related phenomena.

## The mathematics of best-of-n sampling

Let’s study best-of-n n n sampling more formally. Suppose we have some sample space S S S (such as the set of possible question-answer pairs), some probability distribution P P P over S S S, a true objective (or “reward”) Rtrue:S→R R\_{\text{true}}:S\to\mathbb R Rtrue​:S→R, and a proxy objective Rproxy:S→R R\_{\text{proxy}}:S\to\mathbb RRproxy​:S→R. Let’s say that we somehow optimize Rproxy R\_{\text{proxy}} Rproxy​ and thereby obtain some new distribution P′ P^\prime P′. Then:

* The expectation Ex′∼P′[Rtrue(x′)] \mathbb E\_{x^\prime\sim P^\prime}\left[R\_{\text{true}}\left(x^\prime\right)\right] Ex′∼P′​[Rtrue​(x′)] measures how well we have optimized the true objective.
* The [KL divergence⁠(opens in a new window)](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) DKL(P′∥P) D\_{\text{KL}}\left(P^\prime\parallel P\right) DKL​(P′∥P) measures how much optimization we have done. For example, if P′ P^\prime P′ is obtained by taking the first sample from P P P that lies in some subset S′⊆S S^\prime\subseteq S S′⊆S, then this KL divergence is just the negative log probability that a sample from P P P lies in S′ S^\prime S′.

It turns out that in the case of best-of- n n n sampling, both of these quantities can be estimated efficiently using samples from P P P.

Let’s look at the expectation first. The naive approach is to use a Monte Carlo estimator: run best-of- n n n sampling many times, measure the true objective on those samples, and average the results. However, there is a better estimator. If we have N≥n N\geq n N≥n samples from P P P overall, then we can simultaneously consider *every possible subset* of these samples of size n n n, weight each sample by the number of subsets for which it is the best according to the proxy objective, and then take the weighted average true objective score. This weight is just the binomial coefficient (k−1n−1) \binom{k-1}{n-1} (n−1k−1​), where k k k is the rank of the sample under the proxy objective, from 1 1 1 (worst) up to N N N (best).[A](#citation-bottom-A)

The sum of these weights is (Nn) \binom{N}{n} (nN​), giving a proof of the [Hockey-stick identity⁠(opens in a new window)](https://en.wikipedia.org/wiki/Hockey-stick_identity). For a formal derivation of the estimator described here, see Appendix I of the [WebGPT paper⁠(opens in a new window)](https://arxiv.org/pdf/2112.09332.pdf).

As well as using samples more efficiently, this also allows us to reuse samples for different values of n n n. As for the KL divergence, surprisingly, this turns out to have an exact formula that works for any continuous probability distribution P P P (i.e., as long as P P P has no point masses). One might naively guess that the answer is log⁡n \log n logn, since best-of-n n n is doing something like taking the top 1n \frac 1n n1​ of the distribution, and this is roughly correct: the exact answer is log⁡n−n−1n \log n-\frac{n-1}n logn−nn−1​. [B](#citation-bottom-B)

Together, these estimators allow us to easily analyze how the true objective varies with the amount of optimization applied to the proxy objective.

Here’s a real-life example from [WebGPT⁠](/index/webgpt/):

Loading...

## Going beyond best-of-n sampling

The main limitation of best-of-n n n sampling is that the KL divergence grows logarithmically with n n n, so it is only suitable for applying a small amount of optimization.

To apply more optimization, we typically use reinforcement learning. In the settings we’ve studied so far, such as [summarization⁠](/index/learning-to-summarize-with-human-feedback/#optimizingtherewardmodel), we’ve typically been able to reach a KL of around 10 [nats⁠(opens in a new window)](https://en.wikipedia.org/wiki/Nat_(unit)) using reinforcement learning before the true objective starts to decrease due to Goodhart’s law. We’d have to take n to be around 60,000 to reach this KL using best-of-n n n, and we hope to be able to reach much larger KLs than this with improvements to our reward modeling and reinforcement learning practices.

However, not all nats are equal. Empirically, for small KL budgets, best-of-n n n better optimizes both the proxy and the true objectives than reinforcement learning. Intuitively, best-of-n n n is the “brute force” approach, making it more information-theoretically efficient than reinforcement learning, but less computationally efficient at large KLs.[C](#citation-bottom-C)

*We’re actively studying the scaling properties of proxy objectives as part of our work to* [*align*⁠](/alignment/) *our models with human intent and values. If you’d like to help us with this research, we’re* [*hiring*⁠](/careers/research-engineer/)*!*

* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Reasonings & Policy](/research/index/?tags=reasoning-policy)

## Footnotes

1. A

   The sum of these weights is (Nn) \binom{N}{n} (nN​), giving a proof of the [Hockey-stick identity⁠(opens in a new window)](https://en.wikipedia.org/wiki/Hockey-stick_identity). For a formal derivation of the estimator described here, see Appendix I of the [WebGPT paper⁠(opens in a new window)](https://arxiv.org/pdf/2112.09332.pdf).
2. B

   Hint: express the PDF of the best-of-n n n distribution as a function of both the PDF and the CDF of the original distribution.
3. C

   Best-of-nnn is not necessarily optimal in the information-theoretic sense, however. For example, if PPP has a [heavy right tail⁠(opens in a new window)](https://en.wikipedia.org/wiki/Heavy-tailed_distribution), then for any x>0x>0x>0 and any ε>0\varepsilon>0ε>0, there is a distribution QQQ such that Ey∼Q[y]>x\mathbb E\_{y\sim Q}\left[y\right]>xEy∼Q​[y]>x and DKL(Q∥P)<εD\_{\text{KL}}\left(Q\parallel P\right)<\varepsilonDKL​(Q∥P)<ε (exercise).

## Authors

Jacob Hilton, Leo Gao

## Acknowledgments

Thanks to Suchir Balaji, Paul Christiano, William Guss, Vineet Kosaraju, John Schulman, Nisan Stiennon, Jeff Wu, and Daniel Ziegler for discussions related to the ideas in this post. Thanks to Greg Brockman, Jan Leike, Holly Mandel, John Schulman, and Jeff Wu for feedback on drafts. Thanks to Bianca Martin, Steve Dowling, Natalie Summers and Justin Jay Wang for communications and design.

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
