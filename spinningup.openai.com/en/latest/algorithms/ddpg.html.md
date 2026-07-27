<!-- source: https://spinningup.openai.com/en/latest/algorithms/ddpg.html -->

* [Docs](../index.html) »
* Deep Deterministic Policy Gradient
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/algorithms/ddpg.rst)

---

# [Deep Deterministic Policy Gradient](#id1)[¶](#deep-deterministic-policy-gradient "Permalink to this headline")

Table of Contents

* [Deep Deterministic Policy Gradient](#deep-deterministic-policy-gradient)
  + [Background](#background)
    - [Quick Facts](#quick-facts)
    - [Key Equations](#key-equations)
      * [The Q-Learning Side of DDPG](#the-q-learning-side-of-ddpg)
      * [The Policy Learning Side of DDPG](#the-policy-learning-side-of-ddpg)
    - [Exploration vs. Exploitation](#exploration-vs-exploitation)
    - [Pseudocode](#pseudocode)
  + [Documentation](#documentation)
    - [Documentation: PyTorch Version](#documentation-pytorch-version)
    - [Saved Model Contents: PyTorch Version](#saved-model-contents-pytorch-version)
    - [Documentation: Tensorflow Version](#documentation-tensorflow-version)
    - [Saved Model Contents: Tensorflow Version](#saved-model-contents-tensorflow-version)
  + [References](#references)
    - [Relevant Papers](#relevant-papers)
    - [Why These Papers?](#why-these-papers)
    - [Other Public Implementations](#other-public-implementations)

## [Background](#id2)[¶](#background "Permalink to this headline")

(Previously: [Introduction to RL Part 1: The Optimal Q-Function and the Optimal Action](../spinningup/rl_intro.html#the-optimal-q-function-and-the-optimal-action))

Deep Deterministic Policy Gradient (DDPG) is an algorithm which concurrently learns a Q-function and a policy. It uses off-policy data and the Bellman equation to learn the Q-function, and uses the Q-function to learn the policy.

This approach is closely connected to Q-learning, and is motivated the same way: if you know the optimal action-value function ![Q^*(s,a)](../_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg), then in any given state, the optimal action ![a^*(s)](../_images/math/baf715aa6a295b7b7d85e1e1123552c5ae705756.svg) can be found by solving

![a^*(s) = \arg \max_a Q^*(s,a).](../_images/math/82f049ec26e21eb2bfc6af21e3465707814f4838.svg)

DDPG interleaves learning an approximator to ![Q^*(s,a)](../_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg) with learning an approximator to ![a^*(s)](../_images/math/baf715aa6a295b7b7d85e1e1123552c5ae705756.svg), and it does so in a way which is specifically adapted for environments with continuous action spaces. But what does it mean that DDPG is adapted *specifically* for environments with continuous action spaces? It relates to how we compute the max over actions in ![\max_a Q^*(s,a)](../_images/math/1f3098d0653722949f8ceeefc8b5c951d99c8274.svg).

When there are a finite number of discrete actions, the max poses no problem, because we can just compute the Q-values for each action separately and directly compare them. (This also immediately gives us the action which maximizes the Q-value.) But when the action space is continuous, we can’t exhaustively evaluate the space, and solving the optimization problem is highly non-trivial. Using a normal optimization algorithm would make calculating ![\max_a Q^*(s,a)](../_images/math/1f3098d0653722949f8ceeefc8b5c951d99c8274.svg) a painfully expensive subroutine. And since it would need to be run every time the agent wants to take an action in the environment, this is unacceptable.

Because the action space is continuous, the function ![Q^*(s,a)](../_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg) is presumed to be differentiable with respect to the action argument. This allows us to set up an efficient, gradient-based learning rule for a policy ![\mu(s)](../_images/math/3c89236fa57c3dbe71f7c249a07267f83d9c638b.svg) which exploits that fact. Then, instead of running an expensive optimization subroutine each time we wish to compute ![\max_a Q(s,a)](../_images/math/03f01f77446d623f1c933e335f9f81c9a3558c4f.svg), we can approximate it with ![\max_a Q(s,a) \approx Q(s,\mu(s))](../_images/math/8070b852fa94029e80d5811417fd76818a31ec4c.svg). See the Key Equations section details.

### [Quick Facts](#id3)[¶](#quick-facts "Permalink to this headline")

* DDPG is an off-policy algorithm.
* DDPG can only be used for environments with continuous action spaces.
* DDPG can be thought of as being deep Q-learning for continuous action spaces.
* The Spinning Up implementation of DDPG does not support parallelization.

### [Key Equations](#id4)[¶](#key-equations "Permalink to this headline")

Here, we’ll explain the math behind the two parts of DDPG: learning a Q function, and learning a policy.

#### [The Q-Learning Side of DDPG](#id5)[¶](#the-q-learning-side-of-ddpg "Permalink to this headline")

First, let’s recap the Bellman equation describing the optimal action-value function, ![Q^*(s,a)](../_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg). It’s given by

![Q^*(s,a) = \underset{s' \sim P}{{\mathrm E}}\left[r(s,a) + \gamma \max_{a'} Q^*(s', a')\right]](../_images/math/3a8b6ce0d6c0b68744b5724403f5d70ed5cda5db.svg)

where ![s' \sim P](../_images/math/411171ab57c4bec0d86c9f4b495106ba5d73decc.svg) is shorthand for saying that the next state, ![s'](../_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg), is sampled by the environment from a distribution ![P(\cdot| s,a)](../_images/math/400976c62fa52ed70c85d7389f039b5e41473654.svg).

This Bellman equation is the starting point for learning an approximator to ![Q^*(s,a)](../_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg). Suppose the approximator is a neural network ![Q_{\phi}(s,a)](../_images/math/521198ffdba43bf32186f95801549cd1502b76c7.svg), with parameters ![\phi](../_images/math/3b22abcadf8773922f8db80011611bad8123a783.svg), and that we have collected a set ![{\mathcal D}](../_images/math/452456a08130b84d0c030fdc6e9b05973c5bc8b2.svg) of transitions ![(s,a,r,s',d)](../_images/math/4d273c4abe9c8d2805d78e826ee4368ed92841d7.svg) (where ![d](../_images/math/9d61e89bfc1aa6993172a3ac47ab5be75f8e9e81.svg) indicates whether state ![s'](../_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg) is terminal). We can set up a **mean-squared Bellman error (MSBE)** function, which tells us roughly how closely ![Q_{\phi}](../_images/math/c25464faf1bf4928960905461cbbabe1d2441cb2.svg) comes to satisfying the Bellman equation:

![L(\phi, {\mathcal D}) = \underset{(s,a,r,s',d) \sim {\mathcal D}}{{\mathrm E}}\left[
    \Bigg( Q_{\phi}(s,a) - \left(r + \gamma (1 - d) \max_{a'} Q_{\phi}(s',a') \right) \Bigg)^2
    \right]](../_images/math/31dda6ac0678255c4e192dd6fae4f7ed3c7cd91b.svg)

Here, in evaluating ![(1-d)](../_images/math/4591928b993b71d80f43193ffbbbef8e9f3aea10.svg), we’ve used a Python convention of evaluating `True` to 1 and `False` to zero. Thus, when `d==True`—which is to say, when ![s'](../_images/math/6e85fa05d4954e7c1e8037ee1bd163d15bc2e2d6.svg) is a terminal state—the Q-function should show that the agent gets no additional rewards after the current state. (This choice of notation corresponds to what we later implement in code.)

Q-learning algorithms for function approximators, such as DQN (and all its variants) and DDPG, are largely based on minimizing this MSBE loss function. There are two main tricks employed by all of them which are worth describing, and then a specific detail for DDPG.

**Trick One: Replay Buffers.** All standard algorithms for training a deep neural network to approximate ![Q^*(s,a)](../_images/math/cbed396f671d6fb54f6df5c044b82ab3f052d63e.svg) make use of an experience replay buffer. This is the set ![{\mathcal D}](../_images/math/452456a08130b84d0c030fdc6e9b05973c5bc8b2.svg) of previous experiences. In order for the algorithm to have stable behavior, the replay buffer should be large enough to contain a wide range of experiences, but it may not always be good to keep everything. If you only use the very-most recent data, you will overfit to that and things will break; if you use too much experience, you may slow down your learning. This may take some tuning to get right.

You Should Know

We’ve mentioned that DDPG is an off-policy algorithm: this is as good a point as any to highlight why and how. Observe that the replay buffer *should* contain old experiences, even though they might have been obtained using an outdated policy. Why are we able to use these at all? The reason is that the Bellman equation *doesn’t care* which transition tuples are used, or how the actions were selected, or what happens after a given transition, because the optimal Q-function should satisfy the Bellman equation for *all* possible transitions. So any transitions that we’ve ever experienced are fair game when trying to fit a Q-function approximator via MSBE minimization.

**Trick Two: Target Networks.** Q-learning algorithms make use of **target networks**. The term

![r + \gamma (1 - d) \max_{a'} Q_{\phi}(s',a')](../_images/math/fac308175faa67be9f5b27260abaf0ae6c4a58bb.svg)

is called the **target**, because when we minimize the MSBE loss, we are trying to make the Q-function be more like this target. Problematically, the target depends on the same parameters we are trying to train: ![\phi](../_images/math/3b22abcadf8773922f8db80011611bad8123a783.svg). This makes MSBE minimization unstable. The solution is to use a set of parameters which comes close to ![\phi](../_images/math/3b22abcadf8773922f8db80011611bad8123a783.svg), but with a time delay—that is to say, a second network, called the target network, which lags the first. The parameters of the target network are denoted ![\phi_{\text{targ}}](../_images/math/3d9fb7e74f48ade89cbbcc0f3d1f3cb89a824864.svg).

In DQN-based algorithms, the target network is just copied over from the main network every some-fixed-number of steps. In DDPG-style algorithms, the target network is updated once per main network update by polyak averaging:

![\phi_{\text{targ}} \leftarrow \rho \phi_{\text{targ}} + (1 - \rho) \phi,](../_images/math/d417987803ca9f61ac60741880a748129bd66dde.svg)

where ![\rho](../_images/math/b41ecbab285e58fd94a9b544487b74b1d992b0dd.svg) is a hyperparameter between 0 and 1 (usually close to 1). (This hyperparameter is called `polyak` in our code).

**DDPG Detail: Calculating the Max Over Actions in the Target.** As mentioned earlier: computing the maximum over actions in the target is a challenge in continuous action spaces. DDPG deals with this by using a **target policy network** to compute an action which approximately maximizes ![Q_{\phi_{\text{targ}}}](../_images/math/a50d5d2b71fa30f115adf18b0bb1354f967b064a.svg). The target policy network is found the same way as the target Q-function: by polyak averaging the policy parameters over the course of training.

Putting it all together, Q-learning in DDPG is performed by minimizing the following MSBE loss with stochastic gradient descent:

![L(\phi, {\mathcal D}) = \underset{(s,a,r,s',d) \sim {\mathcal D}}{{\mathrm E}}\left[
    \Bigg( Q_{\phi}(s,a) - \left(r + \gamma (1 - d) Q_{\phi_{\text{targ}}}(s', \mu_{\theta_{\text{targ}}}(s')) \right) \Bigg)^2
    \right],](../_images/math/4421120861d55302d76c7e2fd7cc5b2da7aea320.svg)

where ![\mu_{\theta_{\text{targ}}}](../_images/math/a325c9e05fa2ccce85eb2384ca00b4888d1c7824.svg) is the target policy.

#### [The Policy Learning Side of DDPG](#id6)[¶](#the-policy-learning-side-of-ddpg "Permalink to this headline")

Policy learning in DDPG is fairly simple. We want to learn a deterministic policy ![\mu_{\theta}(s)](../_images/math/6923cb2043e84ea05d3eddbb7436c60659243cb9.svg) which gives the action that maximizes ![Q_{\phi}(s,a)](../_images/math/521198ffdba43bf32186f95801549cd1502b76c7.svg). Because the action space is continuous, and we assume the Q-function is differentiable with respect to action, we can just perform gradient ascent (with respect to policy parameters only) to solve

![\max_{\theta} \underset{s \sim {\mathcal D}}{{\mathrm E}}\left[ Q_{\phi}(s, \mu_{\theta}(s)) \right].](../_images/math/cc4e3565d839e63e871a1cf7e3ce5e95bb616b29.svg)

Note that the Q-function parameters are treated as constants here.

### [Exploration vs. Exploitation](#id7)[¶](#exploration-vs-exploitation "Permalink to this headline")

DDPG trains a deterministic policy in an off-policy way. Because the policy is deterministic, if the agent were to explore on-policy, in the beginning it would probably not try a wide enough variety of actions to find useful learning signals. To make DDPG policies explore better, we add noise to their actions at training time. The authors of the original DDPG paper recommended time-correlated [OU noise](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process), but more recent results suggest that uncorrelated, mean-zero Gaussian noise works perfectly well. Since the latter is simpler, it is preferred. To facilitate getting higher-quality training data, you may reduce the scale of the noise over the course of training. (We do not do this in our implementation, and keep noise scale fixed throughout.)

At test time, to see how well the policy exploits what it has learned, we do not add noise to the actions.

You Should Know

Our DDPG implementation uses a trick to improve exploration at the start of training. For a fixed number of steps at the beginning (set with the `start_steps` keyword argument), the agent takes actions which are sampled from a uniform random distribution over valid actions. After that, it returns to normal DDPG exploration.

### [Pseudocode](#id8)[¶](#pseudocode "Permalink to this headline")

![\begin{algorithm}[H]
    \caption{Deep Deterministic Policy Gradient}
    \label{alg1}
\begin{algorithmic}[1]
    \STATE Input: initial policy parameters $\theta$, Q-function parameters $\phi$, empty replay buffer $\mathcal{D}$
    \STATE Set target parameters equal to main parameters $\theta_{\text{targ}} \leftarrow \theta$, $\phi_{\text{targ}} \leftarrow \phi$
    \REPEAT
        \STATE Observe state $s$ and select action $a = \text{clip}(\mu_{\theta}(s) + \epsilon, a_{Low}, a_{High})$, where $\epsilon \sim \mathcal{N}$
        \STATE Execute $a$ in the environment
        \STATE Observe next state $s'$, reward $r$, and done signal $d$ to indicate whether $s'$ is terminal
        \STATE Store $(s,a,r,s',d)$ in replay buffer $\mathcal{D}$
        \STATE If $s'$ is terminal, reset environment state.
        \IF{it's time to update}
            \FOR{however many updates}
                \STATE Randomly sample a batch of transitions, $B = \{ (s,a,r,s',d) \}$ from $\mathcal{D}$
                \STATE Compute targets
                \begin{equation*}
                    y(r,s',d) = r + \gamma (1-d) Q_{\phi_{\text{targ}}}(s', \mu_{\theta_{\text{targ}}}(s'))
                \end{equation*}
                \STATE Update Q-function by one step of gradient descent using
                \begin{equation*}
                    \nabla_{\phi} \frac{1}{|B|}\sum_{(s,a,r,s',d) \in B} \left( Q_{\phi}(s,a) - y(r,s',d) \right)^2
                \end{equation*}
                \STATE Update policy by one step of gradient ascent using
                \begin{equation*}
                    \nabla_{\theta} \frac{1}{|B|}\sum_{s \in B}Q_{\phi}(s, \mu_{\theta}(s))
                \end{equation*}
                \STATE Update target networks with
                \begin{align*}
                    \phi_{\text{targ}} &\leftarrow \rho \phi_{\text{targ}} + (1-\rho) \phi \\
                    \theta_{\text{targ}} &\leftarrow \rho \theta_{\text{targ}} + (1-\rho) \theta
                \end{align*}
            \ENDFOR
        \ENDIF
    \UNTIL{convergence}
\end{algorithmic}
\end{algorithm}](../_images/math/5811066e89799e65be299ec407846103fcf1f746.svg)

## [Documentation](#id9)[¶](#documentation "Permalink to this headline")

You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow implementations of DDPG in Spinning Up. They have nearly identical function calls and docstrings, except for details relating to model construction. However, we include both full docstrings for completeness.

### [Documentation: PyTorch Version](#id10)[¶](#documentation-pytorch-version "Permalink to this headline")

`spinup.``ddpg_pytorch`(*env\_fn*, *actor\_critic=<MagicMock spec='str' id='140554320181456'>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=100*, *replay\_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi\_lr=0.001*, *q\_lr=0.001*, *batch\_size=100*, *start\_steps=10000*, *update\_after=1000*, *update\_every=50*, *act\_noise=0.1*, *num\_test\_episodes=10*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=1*)[¶](#spinup.ddpg_pytorch "Permalink to this definition")
:   Deep Deterministic Policy Gradient (DDPG)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – The constructor method for a PyTorch Module with an `act`   method, a `pi` module, and a `q` module. The `act` method and   `pi` module should accept batches of observations as inputs,   and `q` should accept a batch of observations and a batch of   actions as inputs. When called, these should return:     | Call | Output Shape | Description |   | --- | --- | --- |   | `act` | (batch, act\_dim) | Numpy array of actions for each  observation. |   | `pi` | (batch, act\_dim) | Tensor containing actions from policy  given observations. |   | `q` | (batch,) | Tensor containing the current estimate  of Q\* for the provided observations  and actions. (Critical: make sure to  flatten this!) | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the ActorCritic object   you provided to DDPG. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs to run and train agent. * **replay\_size** (*int*) – Maximum length of replay buffer. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **polyak** (*float*) – Interpolation factor in polyak averaging for target   networks. Target networks are updated towards main networks   according to:  \theta_{\text{targ}} \leftarrow   \rho \theta_{\text{targ}} + (1-\rho) \theta  where \rho is polyak. (Always between 0 and 1, usually   close to 1.) * **pi\_lr** (*float*) – Learning rate for policy. * **q\_lr** (*float*) – Learning rate for Q-networks. * **batch\_size** (*int*) – Minibatch size for SGD. * **start\_steps** (*int*) – Number of steps for uniform-random action selection,   before running real policy. Helps exploration. * **update\_after** (*int*) – Number of env interactions to collect before   starting to do gradient descent updates. Ensures replay buffer   is full enough for useful updates. * **update\_every** (*int*) – Number of env interactions that should elapse   between gradient descent updates. Note: Regardless of how long   you wait between updates, the ratio of env steps to gradient steps   is locked to 1. * **act\_noise** (*float*) – Stddev for Gaussian exploration noise added to   policy at training time. (At test time, no noise is added.) * **num\_test\_episodes** (*int*) – Number of episodes to test the deterministic   policy at the end of each epoch. * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: PyTorch Version](#id11)[¶](#saved-model-contents-pytorch-version "Permalink to this headline")

The PyTorch saved model can be loaded with `ac = torch.load('path/to/model.pt')`, yielding an actor-critic object (`ac`) that has the properties described in the docstring for `ddpg_pytorch`.

You can get actions from this model with

```
actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
```

### [Documentation: Tensorflow Version](#id12)[¶](#documentation-tensorflow-version "Permalink to this headline")

`spinup.``ddpg_tf1`(*env\_fn*, *actor\_critic=<function mlp\_actor\_critic>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=100*, *replay\_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi\_lr=0.001*, *q\_lr=0.001*, *batch\_size=100*, *start\_steps=10000*, *update\_after=1000*, *update\_every=50*, *act\_noise=0.1*, *num\_test\_episodes=10*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=1*)[¶](#spinup.ddpg_tf1 "Permalink to this definition")
:   Deep Deterministic Policy Gradient (DDPG)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – A function which takes in placeholder symbols   for state, `x_ph`, and action, `a_ph`, and returns the main   outputs from the agent’s Tensorflow computation graph:     | Symbol | Shape | Description |   | --- | --- | --- |   | `pi` | (batch, act\_dim) | Deterministically computes actions  from policy given states. |   | `q` | (batch,) | Gives the current estimate of Q\* for  states in `x_ph` and actions in  `a_ph`. |   | `q_pi` | (batch,) | Gives the composition of `q` and  `pi` for states in `x_ph`:  q(x, pi(x)). | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the actor\_critic   function you provided to DDPG. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs to run and train agent. * **replay\_size** (*int*) – Maximum length of replay buffer. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **polyak** (*float*) – Interpolation factor in polyak averaging for target   networks. Target networks are updated towards main networks   according to:  \theta_{\text{targ}} \leftarrow   \rho \theta_{\text{targ}} + (1-\rho) \theta  where \rho is polyak. (Always between 0 and 1, usually   close to 1.) * **pi\_lr** (*float*) – Learning rate for policy. * **q\_lr** (*float*) – Learning rate for Q-networks. * **batch\_size** (*int*) – Minibatch size for SGD. * **start\_steps** (*int*) – Number of steps for uniform-random action selection,   before running real policy. Helps exploration. * **update\_after** (*int*) – Number of env interactions to collect before   starting to do gradient descent updates. Ensures replay buffer   is full enough for useful updates. * **update\_every** (*int*) – Number of env interactions that should elapse   between gradient descent updates. Note: Regardless of how long   you wait between updates, the ratio of env steps to gradient steps   is locked to 1. * **act\_noise** (*float*) – Stddev for Gaussian exploration noise added to   policy at training time. (At test time, no noise is added.) * **num\_test\_episodes** (*int*) – Number of episodes to test the deterministic   policy at the end of each epoch. * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: Tensorflow Version](#id13)[¶](#saved-model-contents-tensorflow-version "Permalink to this headline")

The computation graph saved by the logger includes:

| Key | Value |
| --- | --- |
| `x` | Tensorflow placeholder for state input. |
| `a` | Tensorflow placeholder for action input. |
| `pi` | Deterministically computes an action from the agent, conditioned  on states in `x`. |
| `q` | Gives action-value estimate for states in `x` and actions in `a`. |

This saved model can be accessed either by

* running the trained policy with the [test\_policy.py](../user/saving_and_loading.html#loading-and-running-trained-policies) tool,
* or loading the whole saved graph into a program with [restore\_tf\_graph](../utils/logger.html#spinup.utils.logx.restore_tf_graph).

## [References](#id14)[¶](#references "Permalink to this headline")

### [Relevant Papers](#id15)[¶](#relevant-papers "Permalink to this headline")

* [Deterministic Policy Gradient Algorithms](http://proceedings.mlr.press/v32/silver14.pdf), Silver et al. 2014
* [Continuous Control With Deep Reinforcement Learning](https://arxiv.org/abs/1509.02971), Lillicrap et al. 2016

### [Why These Papers?](#id16)[¶](#why-these-papers "Permalink to this headline")

Silver 2014 is included because it establishes the theory underlying deterministic policy gradients (DPG). Lillicrap 2016 is included because it adapts the theoretically-grounded DPG algorithm to the deep RL setting, giving DDPG.

### [Other Public Implementations](#id17)[¶](#other-public-implementations "Permalink to this headline")

* [Baselines](https://github.com/openai/baselines/tree/master/baselines/ddpg)
* [rllab](https://github.com/rll/rllab/blob/master/rllab/algos/ddpg.py)
* [rllib (Ray)](https://github.com/ray-project/ray/tree/master/python/ray/rllib/agents/ddpg)
* [TD3 release repo](https://github.com/sfujim/TD3)
