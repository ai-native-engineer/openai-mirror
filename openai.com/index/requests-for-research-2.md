<!-- source: https://openai.com/index/requests-for-research-2/ -->

January 31, 2018

[Release](/research/index/release/)

# Requests for Research 2.0

We’re releasing a new batch of seven unsolved problems which have come up in the course of our research at OpenAI.

![Requests For Research 20](https://images.ctfassets.net/kftzwdyauwt9/453aa6c8-82da-4d01-b339fc066cdc/b60a973ec5ddbbae1065a6ded321ebdd/requests-for-research-20.png?w=3840&q=90&fm=webp)

Like our original [Requests for Research⁠(opens in a new window)](https://github.com/openai/requests-for-research) (which [resulted⁠(opens in a new window)](http://lstm.seas.harvard.edu/latex/) [in⁠(opens in a new window)](http://kvfrans.com/static/trpo.pdf) [several⁠(opens in a new window)](https://github.com/dojoteef/glas) [papers⁠(opens in a new window)](https://arxiv.org/abs/1605.01335)), we expect these problems to be a fun and meaningful way for new people to enter the field, as well as for practitioners to hone their skills (it’s also a great way to get a [job⁠(opens in a new window)](https://www.wired.com/story/meet-the-high-schooler-shaking-up-artificial-intelligence/) at OpenAI). Many will require inventing new ideas. Please [email⁠](mailto:requests-for-research@openai.com) us with questions or solutions you’d like us to publicize!

(Also, if you don’t have deep learning background but want to learn to solve problems like these, please apply for our [Fellowship⁠(opens in a new window)](https://jobs.lever.co/openai/54ddfefe-6483-4bba-a828-11a156eae7eb) program!)

## Warmups

If you’re not sure where to begin, here are some solved starter problems.

⭐ Train an LSTM to solve the `XOR` problem: that is, given a sequence of bits, determine its parity. The [LSTM⁠(opens in a new window)](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) should consume the sequence, one bit at a time, and then output the correct answer at the sequence’s end. Test the two approaches below:

* Generate a dataset of random 100,000 binary strings of length 50. Train the LSTM; what performance do you get?
* Generate a dataset of random 100,000 binary strings, where the length of each string is independently and randomly chosen between 1 and 50. Train the LSTM. Does it succeed? What explains the difference?

⭐ Implement a clone of the classic [Snake⁠(opens in a new window)](https://www.youtube.com/watch?v=wDbTP0B94AM) game as a [Gym⁠(opens in a new window)](https://github.com/openai/gym) environment, and solve it with a [reinforcement learning⁠(opens in a new window)](https://arxiv.org/abs/1707.06347) algorithm of your choice. [Tweet⁠(opens in a new window)](https://twitter.com/openai) us videos of the agent playing. Were you able to train a policy that wins the game?

<!-- yt-inline:wDbTP0B94AM -->
[![Snake Game. The longest life. Laurie Anderson-O Superman. Youtube version](https://img.youtube.com/vi/wDbTP0B94AM/hqdefault.jpg)](https://www.youtube.com/watch?v=wDbTP0B94AM)

<details>
<summary>자막: Snake Game. The longest life. Laurie Anderson-O Superman. Youtube version (9:01)</summary>

[00:00]
H-
oh Superman
h
Oh J H.
Oh, mom and dad.
H.
Mom and dad. Ha
h.

[00:01]
[Laughter]
Oh, Superman.
H.
Oh, Jama
H.
Oh, mom and dad.
Mom and dad.
Hi.
I'm not home right now, but if you want
to leave a message, just start talking
at the sound of the tone
h.
[Music]
This is your mother. Are you there? H
Are you coming home?

[00:02]
Haha.
H
hello.
Is anybody home?
Well, you don't know me,
but I know you
h
and I got a message
to give to you. H.
Here come the plane.
[Music]
So you better get ready.
Ready to go.
You can come as you are.

[00:03]
Pay as you go.
[Music]
Hey, as you go
h
and I said, "Okay,
who is this really?" H.
And the voice said, "H,
this is the h
[Music]
that day. H,
this is the h.
The h that takes.
H.
This is the hand.

[00:04]
The hand that takes.
[Music]
Here come the plane.
Is there American planes
made in America?
Smoking or nonsmoking?
Ah. H.
[Music]
And the voice said
hither
snow nor rain
nor
shall stay
[Music]
from the swift completion
of their appointed round.

[00:05]
H P H
P H P H P H P H P H P H P H P H P H P H
P H P H P H
Cuz when love is gone
h
there's no least justice
h
and when justice is gone
h
[Music]
there's always force.
H.

[00:06]
And when is gone h
there's always mom.
Hi mom. H.
[Music]
So hold me
h
and you're m
so hold me
in and your llama
h
in your autumn. Automatic arm.
[Music]

[00:07]
Your electronic arm
in your arm.
So hold me
in. And you're long.
H
your petrochemical.
You're military
[Music]
h in your electronic.
[Music]
H.
[Music]

[00:08]
Heat.
Huh?
[Music]
Huh?

</details>


## Requests for Research

⭐⭐ **Slitherin’.** Implement and solve a multiplayer clone of the classic [Snake⁠(opens in a new window)](https://www.youtube.com/watch?v=wDbTP0B94AM) game (see [slither.io⁠(opens in a new window)](https://slither.io/) for inspiration) as a [Gym⁠(opens in a new window)](https://github.com/openai/gym) environment.

* Environment: have a reasonably large field with multiple snakes; snakes grow when eating randomly-appearing fruit; a snake dies when colliding with another snake, itself, or the wall; and the game ends when all snakes die. Start with two snakes, and scale from there.
* Agent: solve the environment using self-play with an RL algorithm of [your⁠](/index/competitive-self-play/) [choice⁠(opens in a new window)](https://deepmind.com/blog/alphago-zero-learning-scratch/). You’ll need to experiment with various approaches to overcome self-play instability (which resembles the instability people see with GANs). For example, try training your current policy against a distribution of past policies. Which approach works best?
* Inspect the learned behavior: does the agent learn to competently pursue food and avoid other snakes? Does the agent learn to attack, trap, or gang up against the competing snakes? Tweet us videos of the learned policies!

⭐⭐⭐ **Parameter Averaging in Distributed RL.** Explore the effect of parameter averaging schemes on [sample complexity⁠(opens in a new window)](https://en.wikipedia.org/wiki/Sample_complexity) and amount of communication in RL algorithms. While the simplest solution is to average the gradients from every worker on every update, you can [save⁠(opens in a new window)](https://arxiv.org/abs/1511.06051) on communication bandwidth by independently updating workers and then infrequently averaging parameters. In RL, this may have another benefit: at any given time we’ll have agents with different parameters, which could lead to better exploration behavior. Another possibility is use algorithms like [EASGD⁠(opens in a new window)](https://arxiv.org/abs/1412.6651) that bring parameters partly together each update.

⭐⭐⭐ **Transfer Learning Between Different Games via Generative Models.** Proceed as follows:

* Train 11 good policies for 11 [Atari⁠(opens in a new window)](https://github.com/openai/gym#atari) games. Generate 10,000 trajectories of 1,000 steps each from the policy for each game.
* Fit a generative model (such as the [Transformer⁠(opens in a new window)](https://arxiv.org/abs/1706.03762)) to the trajectories produced by 10 of the games.
* Then fine-tune that model on the 11th game.
* Your goal is to quantify the benefit from pre-training on the 10 games. How large does the model need to be for the pre-training to be useful? How does the size of the effect change when the amount of data from the 11th game is reduced by 10x? By 100x?

⭐⭐⭐ **Transformers with Linear Attention.** The [Transformer⁠(opens in a new window)](https://arxiv.org/abs/1706.03762) model uses soft attention with softmax. If we could instead use linear attention (which can be converted into an RNN that uses [fast weights⁠(opens in a new window)](https://arxiv.org/abs/1610.06258)), we could use the resulting model for RL. Specifically, an RL rollout with a transformer over a huge context would be impractical, but running an RNN with fast weights would be very feasible. Your goal: take any language modeling task; train a transformer; then find a way to get the same bits per character/word using a linear-attention transformer with different hyperparameters, without increasing the total number of parameters by much. Only one caveat: this may turn out to be impossible. But one potentially helpful hint: it is likely that transformers with linear attention require much higher dimensional key/value vectors compared to attention that uses the softmax, which can be done without significantly increasing the number of parameters.

⭐⭐⭐ **Learned Data Augmentation.** You could use a learned [VAE⁠(opens in a new window)](https://jaan.io/what-is-variational-autoencoder-vae-tutorial/) of data, to perform “learned data augmentation”. One would first train a VAE on input data, then each training point would be transformed by encoding to a latent space, then applying a simple (e.g. Gaussian) perturbation in latent space, then decoding back to observed space. Could we use such an approach to obtain improved generalization? A potential benefit of such data augmentation is that it could include many nonlinear transformations like viewpoint changes and changes in scene lightning. Can we approximate the set of transformations to which the label is invariant? Check out the [existing⁠(opens in a new window)](https://arxiv.org/abs/1611.01331) [work⁠(opens in a new window)](https://arxiv.org/abs/1702.05538) [on⁠(opens in a new window)](https://arxiv.org/abs/1709.01643) [this⁠(opens in a new window)](https://arxiv.org/abs/1711.04340) [topic⁠(opens in a new window)](https://arxiv.org/abs/1711.00648) [if⁠(opens in a new window)](http://cs231n.stanford.edu/reports/2017/pdfs/300.pdf) [you⁠(opens in a new window)](https://arxiv.org/abs/1710.10564) [want⁠(opens in a new window)](https://papers.nips.cc/paper/7278-learning-to-model-the-tail) a place to get started.

⭐⭐⭐⭐ **Regularization in Reinforcement Learning.** Experimentally investigate (and qualitatively explain) the effect of different regularization methods on an RL algorithm of choice. In supervised deep learning, regularization is extremely important for [improving optimization⁠(opens in a new window)](https://openreview.net/pdf?id=rk6qdGgCZ) and for preventing overfitting, with very successful methods like [dropout⁠(opens in a new window)](https://en.wikipedia.org/wiki/Convolutional_neural_network#Dropout), [batch normalization⁠(opens in a new window)](https://gab41.lab41.org/batch-normalization-what-the-hey-d480039a9e3b), and [L2 regularization⁠(opens in a new window)](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/). However, people haven’t benefited from regularization with reinforcement learning algorithms such as [policy gradients⁠(opens in a new window)](http://www.scholarpedia.org/article/Policy_gradient_methods) and [Q-learning⁠(opens in a new window)](http://mnemstudio.org/path-finding-q-learning-tutorial.htm). Incidentally, people generally use much smaller models in RL than in supervised learning, as large models perform worse — perhaps because they overfit to recent experience. To get started, [here⁠(opens in a new window)](http://sologen.net/papers/RegularizationInReinforcementLearning(PhD-Dissertation-Farahmand).pdf) is a relevant but older theoretical study.

⭐⭐⭐⭐⭐ **Automated Solutions of Olympiad Inequality Problems.** Olympiad inequality problems are simple to express, but [solving⁠(opens in a new window)](https://artofproblemsolving.com/articles/files/MildorfInequalities.pdf) them often requires clever manipulations. Build a dataset of olympiad inequality problems and write a program that can solve a large fraction of them. It’s not clear whether machine learning will be useful here, but you could potentially use a learned policy to reduce the branching factor.

Want to work on problems like these professionally? [Apply⁠](/careers/) to OpenAI!

* [Language](/research/index/?tags=language)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Ilya Sutskever, Tim Salimans, Durk Kingma

## Related articles

![Frontier Risk And Preparedness](https://images.ctfassets.net/kftzwdyauwt9/1f19f98e-798a-4d80-4549e8118ac0/c97816f694a725a9f292f53f1dc5f44f/frontier-risk-and-preparedness.png?w=3840&q=90&fm=webp)

[Frontier risk and preparedness

SafetyOct 26, 2023](/index/frontier-risk-and-preparedness/)

![Red Teaming Network](https://images.ctfassets.net/kftzwdyauwt9/71c1edf1-06f2-415c-b0a2fbe1cfe0/0ff4554769ae7609f53c44a160e351fe/red-teaming-network.png?w=3840&q=90&fm=webp)

[OpenAI Red Teaming Network

SafetySep 19, 2023](/index/red-teaming-network/)

![Confidence-Building Measures for Artificial Intelligence Workshop proceedings](https://images.ctfassets.net/kftzwdyauwt9/Z9HqTzpgkOEFSdz1i0Mkl/4a794853a9d3412851d52a0e18d407f3/Confidence-Building_Measures_for_Artificial_Intelligence__Workshop_proceedings.png?w=3840&q=90&fm=webp)

[Confidence-Building Measures for Artificial Intelligence: Workshop proceedings

ConclusionAug 1, 2023](/index/confidence-building-measures-for-artificial-intelligence/)
