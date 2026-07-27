<!-- source: https://spinningup.openai.com/en/latest/algorithms/sac.html -->

* [Docs](../index.html) »
* Soft Actor-Critic
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/algorithms/sac.rst)

---

# [Soft Actor-Critic](#id2)[¶](#soft-actor-critic "Permalink to this headline")

Table of Contents

* [Soft Actor-Critic](#soft-actor-critic)
  + [Background](#background)
    - [Quick Facts](#quick-facts)
    - [Key Equations](#key-equations)
      * [Entropy-Regularized Reinforcement Learning](#entropy-regularized-reinforcement-learning)
      * [Soft Actor-Critic](#id1)
    - [Exploration vs. Exploitation](#exploration-vs-exploitation)
    - [Pseudocode](#pseudocode)
  + [Documentation](#documentation)
    - [Documentation: PyTorch Version](#documentation-pytorch-version)
    - [Saved Model Contents: PyTorch Version](#saved-model-contents-pytorch-version)
    - [Documentation: Tensorflow Version](#documentation-tensorflow-version)
    - [Saved Model Contents: Tensorflow Version](#saved-model-contents-tensorflow-version)
  + [References](#references)
    - [Relevant Papers](#relevant-papers)
    - [Other Public Implementations](#other-public-implementations)

## [Background](#id3)[¶](#background "Permalink to this headline")

(Previously: [Background for TD3](../algorithms/td3.html#background))

Soft Actor Critic (SAC) is an algorithm that optimizes a stochastic policy in an off-policy way, forming a bridge between stochastic policy optimization and DDPG-style approaches. It isn’t a direct successor to TD3 (having been published roughly concurrently), but it incorporates the clipped double-Q trick, and due to the inherent stochasticity of the policy in SAC, it also winds up benefiting from something like target policy smoothing.

A central feature of SAC is **entropy regularization.** The policy is trained to maximize a trade-off between expected return and [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)), a measure of randomness in the policy. This has a close connection to the exploration-exploitation trade-off: increasing entropy results in more exploration, which can accelerate learning later on. It can also prevent the policy from prematurely converging to a bad local optimum.

### [Quick Facts](#id4)[¶](#quick-facts "Permalink to this headline")

* SAC is an off-policy algorithm.
* The version of SAC implemented here can only be used for environments with continuous action spaces.
* An alternate version of SAC, which slightly changes the policy update rule, can be implemented to handle discrete action spaces.
* The Spinning Up implementation of SAC does not support parallelization.

### [Key Equations](#id5)[¶](#key-equations "Permalink to this headline")

To explain Soft Actor Critic, we first have to introduce the entropy-regularized reinforcement learning setting. In entropy-regularized RL, there are slightly-different equations for value functions.

#### [Entropy-Regularized Reinforcement Learning](#id6)[¶](#entropy-regularized-reinforcement-learning "Permalink to this headline")

Entropy is a quantity which, roughly speaking, says how random a random variable is. If a coin is weighted so that it almost always comes up heads, it has low entropy; if it’s evenly weighted and has a half chance of either outcome, it has high entropy.

Let ![x](../_images/math/ea07a4204f1f53321f76d9c7e348199f0d707db1.svg) be a random variable with probability mass or density function ![P](../_images/math/4204ba416334e663d7bd7c6457d737ba3cbbfe46.svg). The entropy ![H](../_images/math/bf6bcb1745aeab36cdc185e9f75bbfd3998352ce.svg) of ![x](../_images/math/ea07a4204f1f53321f76d9c7e348199f0d707db1.svg) is computed from its distribution ![P](../_images/math/4204ba416334e663d7bd7c6457d737ba3cbbfe46.svg) according to

![H(P) = \underE{x \sim P}{-\log P(x)}.](../_images/math/1bf89d5228652e14d82657fe9f1499b136f54094.svg)

In entropy-regularized reinforcement learning, the agent gets a bonus reward at each time step proportional to the entropy of the policy at that timestep. This changes [the RL problem](../spinningup/rl_intro.html#the-rl-problem) to:

![\pi^* = \arg \max_{\pi} \underE{\tau \sim \pi}{ \sum_{t=0}^{\infty} \gamma^t \bigg( R(s_t, a_t, s_{t+1}) + \alpha H\left(\pi(\cdot|s_t)\right) \bigg)},](../_images/math/b86bf499707114c8789946df649871c5b9185b9d.svg)

where ![\alpha > 0](../_images/math/900375490edee0019a5c54a311bf91de801a1642.svg) is the trade-off coefficient. (Note: we’re assuming an infinite-horizon discounted setting here, and we’ll do the same for the rest of this page.) We can now define the slightly-different value functions in this setting. ![V^{\pi}](../_images/math/fbed8ae629f7512710c5352ca50e8f629d7f34e4.svg) is changed to include the entropy bonuses from every timestep:

![V^{\pi}(s) = \underE{\tau \sim \pi}{ \left. \sum_{t=0}^{\infty} \gamma^t \bigg( R(s_t, a_t, s_{t+1}) + \alpha H\left(\pi(\cdot|s_t)\right) \bigg) \right| s_0 = s}](../_images/math/dda9cebd308c7fe5313f6bf4cbce8d15af046279.svg)

![Q^{\pi}](../_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg) is changed to include the entropy bonuses from every timestep *except the first*:

![Q^{\pi}(s,a) = \underE{\tau \sim \pi}{ \left. \sum_{t=0}^{\infty} \gamma^t  R(s_t, a_t, s_{t+1}) + \alpha \sum_{t=1}^{\infty} \gamma^t H\left(\pi(\cdot|s_t)\right)\right| s_0 = s, a_0 = a}](../_images/math/3c1b1d100a914b01d2f537fd11bdd1159921cad2.svg)

With these definitions, ![V^{\pi}](../_images/math/fbed8ae629f7512710c5352ca50e8f629d7f34e4.svg) and ![Q^{\pi}](../_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg) are connected by:

![V^{\pi}(s) = \underE{a \sim \pi}{Q^{\pi}(s,a)} + \alpha H\left(\pi(\cdot|s)\right)](../_images/math/46d0852616c131f3d5aa2d1798328141904a764d.svg)

and the Bellman equation for ![Q^{\pi}](../_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg) is

![Q^{\pi}(s,a) &= \underE{s' \sim P \\ a' \sim \pi}{R(s,a,s') + \gamma\left(Q^{\pi}(s',a') + \alpha H\left(\pi(\cdot|s')\right) \right)} \\
&= \underE{s' \sim P}{R(s,a,s') + \gamma V^{\pi}(s')}.](../_images/math/8010672f1e8269ce985f901728e7224faa07731e.svg)

You Should Know

The way we’ve set up the value functions in the entropy-regularized setting is a little bit arbitrary, and actually we could have done it differently (eg make ![Q^{\pi}](../_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg) include the entropy bonus at the first timestep). The choice of definition may vary slightly across papers on the subject.

#### [Soft Actor-Critic](#id7)[¶](#id1 "Permalink to this headline")

SAC concurrently learns a policy ![\pi_{\theta}](../_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg) and two Q-functions ![Q_{\phi_1}, Q_{\phi_2}](../_images/math/a4f90f64839041d3c84ac2dde832e76f9d6db7b6.svg). There are two variants of SAC that are currently standard: one that uses a fixed entropy regularization coefficient ![\alpha](../_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg), and another that enforces an entropy constraint by varying ![\alpha](../_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg) over the course of training. For simplicity, Spinning Up makes use of the version with a fixed entropy regularization coefficient, but the entropy-constrained variant is generally preferred by practitioners.

You Should Know

The SAC algorithm has changed a little bit over time. An older version of SAC also learns a value function ![V_{\psi}](../_images/math/f8b8aa6de09a776f6aa37138d773730ba9e623c7.svg) in addition to the Q-functions; this page will focus on the modern version that omits the extra value function.

**Learning Q.** The Q-functions are learned in a similar way to TD3, but with a few key differences.

First, what’s similar?

1. Like in TD3, both Q-functions are learned with MSBE minimization, by regressing to a single shared target.
2. Like in TD3, the shared target is computed using target Q-networks, and the target Q-networks are obtained by polyak averaging the Q-network parameters over the course of training.
3. Like in TD3, the shared target makes use of the **clipped double-Q** trick.

What’s different?

1. Unlike in TD3, the target also includes a term that comes from SAC’s use of entropy regularization.
2. Unlike in TD3, the next-state actions used in the target come from the **current policy** instead of a target policy.
3. Unlike in TD3, there is no explicit target policy smoothing. TD3 trains a deterministic policy, and so it accomplishes smoothing by adding random noise to the next-state actions. SAC trains a stochastic policy, and so the noise from that stochasticity is sufficient to get a similar effect.

Before we give the final form of the Q-loss, let’s take a moment to discuss how the contribution from entropy regularization comes in. We’ll start by taking our recursive Bellman equation for the entropy-regularized ![Q^{\pi}](../_images/math/2bbd8ab5668fe92f59056f58c9f75a01c929e37d.svg) from earlier, and rewriting it a little bit by using the definition of entropy:

![Q^{\pi}(s,a) &= \underE{s' \sim P \\ a' \sim \pi}{R(s,a,s') + \gamma\left(Q^{\pi}(s',a') + \alpha H\left(\pi(\cdot|s')\right) \right)} \\
&= \underE{s' \sim P \\ a' \sim \pi}{R(s,a,s') + \gamma\left(Q^{\pi}(s',a') - \alpha \log \pi(a'|s') \right)}](../_images/math/1557c0c7205cbb2928eb3305b2df207e79bc70fe.svg)

The RHS is an expectation over next states (which come from the replay buffer) and next actions (which come from the current policy, and **not** the replay buffer). Since it’s an expectation, we can approximate it with samples:

![Q^{\pi}(s,a) &\approx r + \gamma\left(Q^{\pi}(s',\tilde{a}') - \alpha \log \pi(\tilde{a}'|s') \right), \;\;\;\;\;  \tilde{a}' \sim \pi(\cdot|s').](../_images/math/aa74b233b0820048f096edb81f0b3321730d71a8.svg)

You Should Know

We switch next action notation to ![\tilde{a}'](../_images/math/f1523bc2b6ea2ca935e184990079e62313c3321f.svg), instead of ![a'](../_images/math/3200e4a6949b896a76b0e83a40edb16602433fd0.svg), to highlight that the next actions have to be sampled fresh from the policy (whereas by contrast, ![r](../_images/math/5a3ac7a81362ac174d142bab198b4bd5a9e2dcee.svg) and ![s'](../_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg) should come from the replay buffer).

SAC sets up the MSBE loss for each Q-function using this kind of sample approximation for the target. The only thing still undetermined here is which Q-function gets used to compute the sample backup: like TD3, SAC uses the clipped double-Q trick, and takes the minimum Q-value between the two Q approximators.

Putting it all together, the loss functions for the Q-networks in SAC are:

![L(\phi_i, {\mathcal D}) = \underset{(s,a,r,s',d) \sim {\mathcal D}}{{\mathrm E}}\left[
    \Bigg( Q_{\phi_i}(s,a) - y(r,s',d) \Bigg)^2
    \right],](../_images/math/0bd81fc5d1cb03a33d6477f5ff10ed879ea393ec.svg)

where the target is given by

![y(r, s', d) = r + \gamma (1 - d) \left( \min_{j=1,2} Q_{\phi_{\text{targ},j}}(s', \tilde{a}') - \alpha \log \pi_{\theta}(\tilde{a}'|s') \right), \;\;\;\;\; \tilde{a}' \sim \pi_{\theta}(\cdot|s').](../_images/math/fc03ff9e9f818fb31b7724907e2b43d5101d2ab8.svg)

**Learning the Policy.** The policy should, in each state, act to maximize the expected future return plus expected future entropy. That is, it should maximize ![V^{\pi}(s)](../_images/math/a81303323c25fc13cd0652ca46d7596276e5cb7e.svg), which we expand out into

![V^{\pi}(s) &= \underE{a \sim \pi}{Q^{\pi}(s,a)} + \alpha H\left(\pi(\cdot|s)\right) \\
&= \underE{a \sim \pi}{Q^{\pi}(s,a) - \alpha \log \pi(a|s)}.](../_images/math/5ff58df73caef07f6309a1460fe57b1c34e3b374.svg)

The way we optimize the policy makes use of the **reparameterization trick**, in which a sample from ![\pi_{\theta}(\cdot|s)](../_images/math/e57f13375048b8f7343f9066b6553bc282afa326.svg) is drawn by computing a deterministic function of state, policy parameters, and independent noise. To illustrate: following the authors of the SAC paper, we use a squashed Gaussian policy, which means that samples are obtained according to

![\tilde{a}_{\theta}(s, \xi) = \tanh\left( \mu_{\theta}(s) + \sigma_{\theta}(s) \odot \xi \right), \;\;\;\;\; \xi \sim \mathcal{N}(0, I).](../_images/math/dac3ddc2ea35e8233b8bc0a905273712793ab1cb.svg)

You Should Know

This policy has two key differences from the policies we use in the other policy optimization algorithms:

**1. The squashing function.** The ![\tanh](../_images/math/c65796f3bb56c457e63ebc770e3d775cace08673.svg) in the SAC policy ensures that actions are bounded to a finite range. This is absent in the VPG, TRPO, and PPO policies. It also changes the distribution: before the ![\tanh](../_images/math/c65796f3bb56c457e63ebc770e3d775cace08673.svg) the SAC policy is a factored Gaussian like the other algorithms’ policies, but after the ![\tanh](../_images/math/c65796f3bb56c457e63ebc770e3d775cace08673.svg) it is not. (You can still compute the log-probabilities of actions in closed form, though: see the paper appendix for details.)

**2. The way standard deviations are parameterized.** In VPG, TRPO, and PPO, we represent the log std devs with state-independent parameter vectors. In SAC, we represent the log std devs as outputs from the neural network, meaning that they depend on state in a complex way. SAC with state-independent log std devs, in our experience, did not work. (Can you think of why? Or better yet: run an experiment to verify?)

The reparameterization trick allows us to rewrite the expectation over actions (which contains a pain point: the distribution depends on the policy parameters) into an expectation over noise (which removes the pain point: the distribution now has no dependence on parameters):

![\underE{a \sim \pi_{\theta}}{Q^{\pi_{\theta}}(s,a) - \alpha \log \pi_{\theta}(a|s)} = \underE{\xi \sim \mathcal{N}}{Q^{\pi_{\theta}}(s,\tilde{a}_{\theta}(s,\xi)) - \alpha \log \pi_{\theta}(\tilde{a}_{\theta}(s,\xi)|s)}](../_images/math/5713f9f99ea3532e3cbde89eac91328eb8549409.svg)

To get the policy loss, the final step is that we need to substitute ![Q^{\pi_{\theta}}](../_images/math/9c39112fd52e66e3062f93c502ade0eb9381d957.svg) with one of our function approximators. Unlike in TD3, which uses ![Q_{\phi_1}](../_images/math/8795d42bd263dcbe55d123e7466b2dd5091490a7.svg) (just the first Q approximator), SAC uses ![\min_{j=1,2} Q_{\phi_j}](../_images/math/e5d14ed1b7128d64d43af73b7d0b189c6afda8ec.svg) (the minimum of the two Q approximators). The policy is thus optimized according to

![\max_{\theta} \underE{s \sim \mathcal{D} \\ \xi \sim \mathcal{N}}{\min_{j=1,2} Q_{\phi_j}(s,\tilde{a}_{\theta}(s,\xi)) - \alpha \log \pi_{\theta}(\tilde{a}_{\theta}(s,\xi)|s)},](../_images/math/bdbe4cabbba4687b310d99e8fa67ed314339bd31.svg)

which is almost the same as the DDPG and TD3 policy optimization, except for the min-double-Q trick, the stochasticity, and the entropy term.

### [Exploration vs. Exploitation](#id8)[¶](#exploration-vs-exploitation "Permalink to this headline")

SAC trains a stochastic policy with entropy regularization, and explores in an on-policy way. The entropy regularization coefficient ![\alpha](../_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg) explicitly controls the explore-exploit tradeoff, with higher ![\alpha](../_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg) corresponding to more exploration, and lower ![\alpha](../_images/math/d8316e40b1057b06d31c2cad3a0d4cc9e75fa2c1.svg) corresponding to more exploitation. The right coefficient (the one which leads to the stablest / highest-reward learning) may vary from environment to environment, and could require careful tuning.

At test time, to see how well the policy exploits what it has learned, we remove stochasticity and use the mean action instead of a sample from the distribution. This tends to improve performance over the original stochastic policy.

You Should Know

Our SAC implementation uses a trick to improve exploration at the start of training. For a fixed number of steps at the beginning (set with the `start_steps` keyword argument), the agent takes actions which are sampled from a uniform random distribution over valid actions. After that, it returns to normal SAC exploration.

### [Pseudocode](#id9)[¶](#pseudocode "Permalink to this headline")

![\begin{algorithm}[H]
    \caption{Soft Actor-Critic}
    \label{alg1}
\begin{algorithmic}[1]
    \STATE Input: initial policy parameters $\theta$, Q-function parameters $\phi_1$, $\phi_2$, empty replay buffer $\mathcal{D}$
    \STATE Set target parameters equal to main parameters $\phi_{\text{targ},1} \leftarrow \phi_1$, $\phi_{\text{targ},2} \leftarrow \phi_2$
    \REPEAT
        \STATE Observe state $s$ and select action $a \sim \pi_{\theta}(\cdot|s)$
        \STATE Execute $a$ in the environment
        \STATE Observe next state $s'$, reward $r$, and done signal $d$ to indicate whether $s'$ is terminal
        \STATE Store $(s,a,r,s',d)$ in replay buffer $\mathcal{D}$
        \STATE If $s'$ is terminal, reset environment state.
        \IF{it's time to update}
            \FOR{$j$ in range(however many updates)}
                \STATE Randomly sample a batch of transitions, $B = \{ (s,a,r,s',d) \}$ from $\mathcal{D}$
                \STATE Compute targets for the Q functions:
                \begin{align*}
                    y (r,s',d) &= r + \gamma (1-d) \left(\min_{i=1,2} Q_{\phi_{\text{targ}, i}} (s', \tilde{a}') - \alpha \log \pi_{\theta}(\tilde{a}'|s')\right), && \tilde{a}' \sim \pi_{\theta}(\cdot|s')
                \end{align*}
                \STATE Update Q-functions by one step of gradient descent using
                \begin{align*}
                    & \nabla_{\phi_i} \frac{1}{|B|}\sum_{(s,a,r,s',d) \in B} \left( Q_{\phi_i}(s,a) - y(r,s',d) \right)^2 && \text{for } i=1,2
                \end{align*}
                \STATE Update policy by one step of gradient ascent using
                \begin{equation*}
                    \nabla_{\theta} \frac{1}{|B|}\sum_{s \in B} \Big(\min_{i=1,2} Q_{\phi_i}(s, \tilde{a}_{\theta}(s)) - \alpha \log \pi_{\theta} \left(\left. \tilde{a}_{\theta}(s) \right| s\right) \Big),
                \end{equation*}
                where $\tilde{a}_{\theta}(s)$ is a sample from $\pi_{\theta}(\cdot|s)$ which is differentiable wrt $\theta$ via the reparametrization trick.
                \STATE Update target networks with
                \begin{align*}
                    \phi_{\text{targ},i} &\leftarrow \rho \phi_{\text{targ}, i} + (1-\rho) \phi_i && \text{for } i=1,2
                \end{align*}
            \ENDFOR
        \ENDIF
    \UNTIL{convergence}
\end{algorithmic}
\end{algorithm}](../_images/math/c01f4994ae4aacf299a6b3ceceedfe0a14d4b874.svg)

## [Documentation](#id10)[¶](#documentation "Permalink to this headline")

You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow implementations of SAC in Spinning Up. They have nearly identical function calls and docstrings, except for details relating to model construction. However, we include both full docstrings for completeness.

### [Documentation: PyTorch Version](#id11)[¶](#documentation-pytorch-version "Permalink to this headline")

`spinup.``sac_pytorch`(*env\_fn*, *actor\_critic=<MagicMock spec='str' id='140554319922904'>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=100*, *replay\_size=1000000*, *gamma=0.99*, *polyak=0.995*, *lr=0.001*, *alpha=0.2*, *batch\_size=100*, *start\_steps=10000*, *update\_after=1000*, *update\_every=50*, *num\_test\_episodes=10*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=1*)[¶](#spinup.sac_pytorch "Permalink to this definition")
:   Soft Actor-Critic (SAC)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – The constructor method for a PyTorch Module with an `act`   method, a `pi` module, a `q1` module, and a `q2` module.   The `act` method and `pi` module should accept batches of   observations as inputs, and `q1` and `q2` should accept a batch   of observations and a batch of actions as inputs. When called,   `act`, `q1`, and `q2` should return:     | Call | Output Shape | Description |   | --- | --- | --- |   | `act` | (batch, act\_dim) | Numpy array of actions for each  observation. |   | `q1` | (batch,) | Tensor containing one current estimate  of Q\* for the provided observations  and actions. (Critical: make sure to  flatten this!) |   | `q2` | (batch,) | Tensor containing the other current  estimate of Q\* for the provided observations  and actions. (Critical: make sure to  flatten this!) |     Calling `pi` should return:     | Symbol | Shape | Description |   | --- | --- | --- |   | `a` | (batch, act\_dim) | Tensor containing actions from policy  given observations. |   | `logp_pi` | (batch,) | Tensor containing log probabilities of  actions in `a`. Importantly: gradients  should be able to flow back into `a`. | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the ActorCritic object   you provided to SAC. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs to run and train agent. * **replay\_size** (*int*) – Maximum length of replay buffer. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **polyak** (*float*) – Interpolation factor in polyak averaging for target   networks. Target networks are updated towards main networks   according to:  \theta_{\text{targ}} \leftarrow   \rho \theta_{\text{targ}} + (1-\rho) \theta  where \rho is polyak. (Always between 0 and 1, usually   close to 1.) * **lr** (*float*) – Learning rate (used for both policy and value learning). * **alpha** (*float*) – Entropy regularization coefficient. (Equivalent to   inverse of reward scale in the original SAC paper.) * **batch\_size** (*int*) – Minibatch size for SGD. * **start\_steps** (*int*) – Number of steps for uniform-random action selection,   before running real policy. Helps exploration. * **update\_after** (*int*) – Number of env interactions to collect before   starting to do gradient descent updates. Ensures replay buffer   is full enough for useful updates. * **update\_every** (*int*) – Number of env interactions that should elapse   between gradient descent updates. Note: Regardless of how long   you wait between updates, the ratio of env steps to gradient steps   is locked to 1. * **num\_test\_episodes** (*int*) – Number of episodes to test the deterministic   policy at the end of each epoch. * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: PyTorch Version](#id12)[¶](#saved-model-contents-pytorch-version "Permalink to this headline")

The PyTorch saved model can be loaded with `ac = torch.load('path/to/model.pt')`, yielding an actor-critic object (`ac`) that has the properties described in the docstring for `sac_pytorch`.

You can get actions from this model with

```
actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
```

### [Documentation: Tensorflow Version](#id13)[¶](#documentation-tensorflow-version "Permalink to this headline")

`spinup.``sac_tf1`(*env\_fn*, *actor\_critic=<function mlp\_actor\_critic>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=100*, *replay\_size=1000000*, *gamma=0.99*, *polyak=0.995*, *lr=0.001*, *alpha=0.2*, *batch\_size=100*, *start\_steps=10000*, *update\_after=1000*, *update\_every=50*, *num\_test\_episodes=10*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=1*)[¶](#spinup.sac_tf1 "Permalink to this definition")
:   Soft Actor-Critic (SAC)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – A function which takes in placeholder symbols   for state, `x_ph`, and action, `a_ph`, and returns the main   outputs from the agent’s Tensorflow computation graph:     | Symbol | Shape | Description |   | --- | --- | --- |   | `mu` | (batch, act\_dim) | Computes mean actions from policy  given states. |   | `pi` | (batch, act\_dim) | Samples actions from policy given  states. |   | `logp_pi` | (batch,) | Gives log probability, according to  the policy, of the action sampled by  `pi`. Critical: must be differentiable  with respect to policy parameters all  the way through action sampling. |   | `q1` | (batch,) | Gives one estimate of Q\* for  states in `x_ph` and actions in  `a_ph`. |   | `q2` | (batch,) | Gives another estimate of Q\* for  states in `x_ph` and actions in  `a_ph`. | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the actor\_critic   function you provided to SAC. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs to run and train agent. * **replay\_size** (*int*) – Maximum length of replay buffer. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **polyak** (*float*) – Interpolation factor in polyak averaging for target   networks. Target networks are updated towards main networks   according to:  \theta_{\text{targ}} \leftarrow   \rho \theta_{\text{targ}} + (1-\rho) \theta  where \rho is polyak. (Always between 0 and 1, usually   close to 1.) * **lr** (*float*) – Learning rate (used for both policy and value learning). * **alpha** (*float*) – Entropy regularization coefficient. (Equivalent to   inverse of reward scale in the original SAC paper.) * **batch\_size** (*int*) – Minibatch size for SGD. * **start\_steps** (*int*) – Number of steps for uniform-random action selection,   before running real policy. Helps exploration. * **update\_after** (*int*) – Number of env interactions to collect before   starting to do gradient descent updates. Ensures replay buffer   is full enough for useful updates. * **update\_every** (*int*) – Number of env interactions that should elapse   between gradient descent updates. Note: Regardless of how long   you wait between updates, the ratio of env steps to gradient steps   is locked to 1. * **num\_test\_episodes** (*int*) – Number of episodes to test the deterministic   policy at the end of each epoch. * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: Tensorflow Version](#id14)[¶](#saved-model-contents-tensorflow-version "Permalink to this headline")

The computation graph saved by the logger includes:

| Key | Value |
| --- | --- |
| `x` | Tensorflow placeholder for state input. |
| `a` | Tensorflow placeholder for action input. |
| `mu` | Deterministically computes mean action from the agent, given states in `x`. |
| `pi` | Samples an action from the agent, conditioned on states in `x`. |
| `q1` | Gives one action-value estimate for states in `x` and actions in `a`. |
| `q2` | Gives the other action-value estimate for states in `x` and actions in `a`. |
| `v` | Gives the value estimate for states in `x`. |

This saved model can be accessed either by

* running the trained policy with the [test\_policy.py](../user/saving_and_loading.html#loading-and-running-trained-policies) tool,
* or loading the whole saved graph into a program with [restore\_tf\_graph](../utils/logger.html#spinup.utils.logx.restore_tf_graph).

Note: for SAC, the correct evaluation policy is given by `mu` and not by `pi`. The policy `pi` may be thought of as the exploration policy, while `mu` is the exploitation policy.

## [References](#id15)[¶](#references "Permalink to this headline")

### [Relevant Papers](#id16)[¶](#relevant-papers "Permalink to this headline")

* [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://arxiv.org/abs/1801.01290), Haarnoja et al, 2018
* [Soft Actor-Critic Algorithms and Applications](https://arxiv.org/abs/1812.05905), Haarnoja et al, 2018
* [Learning to Walk via Deep Reinforcement Learning](https://arxiv.org/abs/1812.11103), Haarnoja et al, 2018

### [Other Public Implementations](#id17)[¶](#other-public-implementations "Permalink to this headline")

* [SAC release repo](https://github.com/haarnoja/sac) (original “official” codebase)
* [Softlearning repo](https://github.com/rail-berkeley/softlearning) (current “official” codebase)
* [Yarats and Kostrikov repo](https://github.com/denisyarats/pytorch_sac)
