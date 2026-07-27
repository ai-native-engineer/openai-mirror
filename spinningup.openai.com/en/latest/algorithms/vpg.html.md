<!-- source: https://spinningup.openai.com/en/latest/algorithms/vpg.html -->

* [Docs](../index.html) »
* Vanilla Policy Gradient
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/algorithms/vpg.rst)

---

# [Vanilla Policy Gradient](#id1)[¶](#vanilla-policy-gradient "Permalink to this headline")

Table of Contents

* [Vanilla Policy Gradient](#vanilla-policy-gradient)
  + [Background](#background)
    - [Quick Facts](#quick-facts)
    - [Key Equations](#key-equations)
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

(Previously: [Introduction to RL, Part 3](../spinningup/rl_intro3.html))

The key idea underlying policy gradients is to push up the probabilities of actions that lead to higher return, and push down the probabilities of actions that lead to lower return, until you arrive at the optimal policy.

### [Quick Facts](#id3)[¶](#quick-facts "Permalink to this headline")

* VPG is an on-policy algorithm.
* VPG can be used for environments with either discrete or continuous action spaces.
* The Spinning Up implementation of VPG supports parallelization with MPI.

### [Key Equations](#id4)[¶](#key-equations "Permalink to this headline")

Let ![\pi_{\theta}](../_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg) denote a policy with parameters ![\theta](../_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg), and ![J(\pi_{\theta})](../_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg) denote the expected finite-horizon undiscounted return of the policy. The gradient of ![J(\pi_{\theta})](../_images/math/96b876944de9cf0f980fe261562e8e07029245bf.svg) is

![\nabla_{\theta} J(\pi_{\theta}) = \underE{\tau \sim \pi_{\theta}}{
    \sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}(a_t|s_t) A^{\pi_{\theta}}(s_t,a_t)
    },](../_images/math/ada1266646d71c941e77e3fd41bba9d92d06b7c2.svg)

where ![\tau](../_images/math/67a5412645decf6424bdd97aed3e9e7601bd784f.svg) is a trajectory and ![A^{\pi_{\theta}}](../_images/math/5441ceb0039c72b114bb209edcd3bbbbe486c02c.svg) is the advantage function for the current policy.

The policy gradient algorithm works by updating policy parameters via stochastic gradient ascent on policy performance:

![\theta_{k+1} = \theta_k + \alpha \nabla_{\theta} J(\pi_{\theta_k})](../_images/math/f5198e001f2c6053222b709af633865deb249cdf.svg)

Policy gradient implementations typically compute advantage function estimates based on the infinite-horizon discounted return, despite otherwise using the finite-horizon undiscounted policy gradient formula.

### [Exploration vs. Exploitation](#id5)[¶](#exploration-vs-exploitation "Permalink to this headline")

VPG trains a stochastic policy in an on-policy way. This means that it explores by sampling actions according to the latest version of its stochastic policy. The amount of randomness in action selection depends on both initial conditions and the training procedure. Over the course of training, the policy typically becomes progressively less random, as the update rule encourages it to exploit rewards that it has already found. This may cause the policy to get trapped in local optima.

### [Pseudocode](#id6)[¶](#pseudocode "Permalink to this headline")

![\begin{algorithm}[H]
    \caption{Vanilla Policy Gradient Algorithm}
    \label{alg1}
\begin{algorithmic}[1]
    \STATE Input: initial policy parameters $\theta_0$, initial value function parameters $\phi_0$
    \FOR{$k = 0,1,2,...$}
    \STATE Collect set of trajectories ${\mathcal D}_k = \{\tau_i\}$ by running policy $\pi_k = \pi(\theta_k)$ in the environment.
    \STATE Compute rewards-to-go $\hat{R}_t$.
    \STATE Compute advantage estimates, $\hat{A}_t$ (using any method of advantage estimation) based on the current value function $V_{\phi_k}$.
    \STATE Estimate policy gradient as
        \begin{equation*}
        \hat{g}_k = \frac{1}{|{\mathcal D}_k|} \sum_{\tau \in {\mathcal D}_k} \sum_{t=0}^T \left. \nabla_{\theta} \log\pi_{\theta}(a_t|s_t)\right|_{\theta_k} \hat{A}_t.
        \end{equation*}
    \STATE Compute policy update, either using standard gradient ascent,
        \begin{equation*}
        \theta_{k+1} = \theta_k + \alpha_k \hat{g}_k,
        \end{equation*}
        or via another gradient ascent algorithm like Adam.
    \STATE Fit value function by regression on mean-squared error:
        \begin{equation*}
        \phi_{k+1} = \arg \min_{\phi} \frac{1}{|{\mathcal D}_k| T} \sum_{\tau \in {\mathcal D}_k} \sum_{t=0}^T\left( V_{\phi} (s_t) - \hat{R}_t \right)^2,
        \end{equation*}
        typically via some gradient descent algorithm.
    \ENDFOR
\end{algorithmic}
\end{algorithm}](../_images/math/262538f3077a7be8ce89066abbab523575132996.svg)

## [Documentation](#id7)[¶](#documentation "Permalink to this headline")

You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow implementations of VPG in Spinning Up. They have nearly identical function calls and docstrings, except for details relating to model construction. However, we include both full docstrings for completeness.

### [Documentation: PyTorch Version](#id8)[¶](#documentation-pytorch-version "Permalink to this headline")

`spinup.``vpg_pytorch`(*env\_fn*, *actor\_critic=<MagicMock spec='str' id='140554319865336'>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=50*, *gamma=0.99*, *pi\_lr=0.0003*, *vf\_lr=0.001*, *train\_v\_iters=80*, *lam=0.97*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=10*)[¶](#spinup.vpg_pytorch "Permalink to this definition")
:   Vanilla Policy Gradient

    (with GAE-Lambda for advantage estimation)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – The constructor method for a PyTorch Module with a   `step` method, an `act` method, a `pi` module, and a `v`   module. The `step` method should accept a batch of observations   and return:     | Symbol | Shape | Description |   | --- | --- | --- |   | `a` | (batch, act\_dim) | Numpy array of actions for each  observation. |   | `v` | (batch,) | Numpy array of value estimates  for the provided observations. |   | `logp_a` | (batch,) | Numpy array of log probs for the  actions in `a`. |     The `act` method behaves the same as `step` but only returns `a`.  The `pi` module’s forward call should accept a batch of   observations and optionally a batch of actions, and return:     | Symbol | Shape | Description |   | --- | --- | --- |   | `pi` | N/A | Torch Distribution object, containing  a batch of distributions describing  the policy for the provided observations. |   | `logp_a` | (batch,) | Optional (only returned if batch of  actions is given). Tensor containing  the log probability, according to  the policy, of the provided actions.  If actions not given, will contain  `None`. |     The `v` module’s forward call should accept a batch of observations   and return:     | Symbol | Shape | Description |   | --- | --- | --- |   | `v` | (batch,) | Tensor containing the value estimates  for the provided observations. (Critical:  make sure to flatten this!) | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the ActorCritic object   you provided to VPG. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs of interaction (equivalent to   number of policy updates) to perform. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **pi\_lr** (*float*) – Learning rate for policy optimizer. * **vf\_lr** (*float*) – Learning rate for value function optimizer. * **train\_v\_iters** (*int*) – Number of gradient descent steps to take on   value function per epoch. * **lam** (*float*) – Lambda for GAE-Lambda. (Always between 0 and 1,   close to 1.) * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: PyTorch Version](#id9)[¶](#saved-model-contents-pytorch-version "Permalink to this headline")

The PyTorch saved model can be loaded with `ac = torch.load('path/to/model.pt')`, yielding an actor-critic object (`ac`) that has the properties described in the docstring for `vpg_pytorch`.

You can get actions from this model with

```
actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
```

### [Documentation: Tensorflow Version](#id10)[¶](#documentation-tensorflow-version "Permalink to this headline")

`spinup.``vpg_tf1`(*env\_fn*, *actor\_critic=<function mlp\_actor\_critic>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=50*, *gamma=0.99*, *pi\_lr=0.0003*, *vf\_lr=0.001*, *train\_v\_iters=80*, *lam=0.97*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=10*)[¶](#spinup.vpg_tf1 "Permalink to this definition")
:   Vanilla Policy Gradient

    (with GAE-Lambda for advantage estimation)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – A function which takes in placeholder symbols   for state, `x_ph`, and action, `a_ph`, and returns the main   outputs from the agent’s Tensorflow computation graph:     | Symbol | Shape | Description |   | --- | --- | --- |   | `pi` | (batch, act\_dim) | Samples actions from policy given  states. |   | `logp` | (batch,) | Gives log probability, according to  the policy, of taking actions `a_ph`  in states `x_ph`. |   | `logp_pi` | (batch,) | Gives log probability, according to  the policy, of the action sampled by  `pi`. |   | `v` | (batch,) | Gives the value estimate for states  in `x_ph`. (Critical: make sure  to flatten this!) | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the actor\_critic   function you provided to VPG. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs of interaction (equivalent to   number of policy updates) to perform. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **pi\_lr** (*float*) – Learning rate for policy optimizer. * **vf\_lr** (*float*) – Learning rate for value function optimizer. * **train\_v\_iters** (*int*) – Number of gradient descent steps to take on   value function per epoch. * **lam** (*float*) – Lambda for GAE-Lambda. (Always between 0 and 1,   close to 1.) * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: Tensorflow Version](#id11)[¶](#saved-model-contents-tensorflow-version "Permalink to this headline")

The computation graph saved by the logger includes:

| Key | Value |
| --- | --- |
| `x` | Tensorflow placeholder for state input. |
| `pi` | Samples an action from the agent, conditioned on states in `x`. |
| `v` | Gives value estimate for states in `x`. |

This saved model can be accessed either by

* running the trained policy with the [test\_policy.py](../user/saving_and_loading.html#loading-and-running-trained-policies) tool,
* or loading the whole saved graph into a program with [restore\_tf\_graph](../utils/logger.html#spinup.utils.logx.restore_tf_graph).

## [References](#id12)[¶](#references "Permalink to this headline")

### [Relevant Papers](#id13)[¶](#relevant-papers "Permalink to this headline")

* [Policy Gradient Methods for Reinforcement Learning with Function Approximation](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf), Sutton et al. 2000
* [Optimizing Expectations: From Deep Reinforcement Learning to Stochastic Computation Graphs](http://joschu.net/docs/thesis.pdf), Schulman 2016(a)
* [Benchmarking Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/1604.06778), Duan et al. 2016
* [High Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438), Schulman et al. 2016(b)

### [Why These Papers?](#id14)[¶](#why-these-papers "Permalink to this headline")

Sutton 2000 is included because it is a timeless classic of reinforcement learning theory, and contains references to the earlier work which led to modern policy gradients. Schulman 2016(a) is included because Chapter 2 contains a lucid introduction to the theory of policy gradient algorithms, including pseudocode. Duan 2016 is a clear, recent benchmark paper that shows how vanilla policy gradient in the deep RL setting (eg with neural network policies and Adam as the optimizer) compares with other deep RL algorithms. Schulman 2016(b) is included because our implementation of VPG makes use of Generalized Advantage Estimation for computing the policy gradient.

### [Other Public Implementations](#id15)[¶](#other-public-implementations "Permalink to this headline")

* [rllab](https://github.com/rll/rllab/blob/master/rllab/algos/vpg.py)
* [rllib (Ray)](https://github.com/ray-project/ray/blob/master/python/ray/rllib/agents/pg)
