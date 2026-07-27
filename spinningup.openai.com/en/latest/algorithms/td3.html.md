<!-- source: https://spinningup.openai.com/en/latest/algorithms/td3.html -->

* [Docs](../index.html) »
* Twin Delayed DDPG
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/algorithms/td3.rst)

---

# [Twin Delayed DDPG](#id1)[¶](#twin-delayed-ddpg "Permalink to this headline")

Table of Contents

* [Twin Delayed DDPG](#twin-delayed-ddpg)
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
    - [Other Public Implementations](#other-public-implementations)

## [Background](#id2)[¶](#background "Permalink to this headline")

(Previously: [Background for DDPG](../algorithms/ddpg.html#background))

While DDPG can achieve great performance sometimes, it is frequently brittle with respect to hyperparameters and other kinds of tuning. A common failure mode for DDPG is that the learned Q-function begins to dramatically overestimate Q-values, which then leads to the policy breaking, because it exploits the errors in the Q-function. Twin Delayed DDPG (TD3) is an algorithm that addresses this issue by introducing three critical tricks:

**Trick One: Clipped Double-Q Learning.** TD3 learns *two* Q-functions instead of one (hence “twin”), and uses the smaller of the two Q-values to form the targets in the Bellman error loss functions.

**Trick Two: “Delayed” Policy Updates.** TD3 updates the policy (and target networks) less frequently than the Q-function. The paper recommends one policy update for every two Q-function updates.

**Trick Three: Target Policy Smoothing.** TD3 adds noise to the target action, to make it harder for the policy to exploit Q-function errors by smoothing out Q along changes in action.

Together, these three tricks result in substantially improved performance over baseline DDPG.

### [Quick Facts](#id3)[¶](#quick-facts "Permalink to this headline")

* TD3 is an off-policy algorithm.
* TD3 can only be used for environments with continuous action spaces.
* The Spinning Up implementation of TD3 does not support parallelization.

### [Key Equations](#id4)[¶](#key-equations "Permalink to this headline")

TD3 concurrently learns two Q-functions, ![Q_{\phi_1}](../_images/math/8795d42bd263dcbe55d123e7466b2dd5091490a7.svg) and ![Q_{\phi_2}](../_images/math/ac4e235414bfd47d449e3440ba29ae8470d3952e.svg), by mean square Bellman error minimization, in almost the same way that DDPG learns its single Q-function. To show exactly how TD3 does this and how it differs from normal DDPG, we’ll work from the innermost part of the loss function outwards.

First: **target policy smoothing**. Actions used to form the Q-learning target are based on the target policy, ![\mu_{\theta_{\text{targ}}}](../_images/math/a325c9e05fa2ccce85eb2384ca00b4888d1c7824.svg), but with clipped noise added on each dimension of the action. After adding the clipped noise, the target action is then clipped to lie in the valid action range (all valid actions, ![a](../_images/math/76a319586cd215c8f2075b938fc6f6e07c81714b.svg), satisfy ![a_{Low} \leq a \leq a_{High}](../_images/math/a5132668c0af8733656505c5fb6c1dff4a7907a1.svg)). The target actions are thus:

![a'(s') = \text{clip}\left(\mu_{\theta_{\text{targ}}}(s') + \text{clip}(\epsilon,-c,c), a_{Low}, a_{High}\right), \;\;\;\;\; \epsilon \sim \mathcal{N}(0, \sigma)](../_images/math/8efd61c40551db4eddb3f780d2804cac34c8ae52.svg)

Target policy smoothing essentially serves as a regularizer for the algorithm. It addresses a particular failure mode that can happen in DDPG: if the Q-function approximator develops an incorrect sharp peak for some actions, the policy will quickly exploit that peak and then have brittle or incorrect behavior. This can be averted by smoothing out the Q-function over similar actions, which target policy smoothing is designed to do.

Next: **clipped double-Q learning**. Both Q-functions use a single target, calculated using whichever of the two Q-functions gives a smaller target value:

![y(r,s',d) = r + \gamma (1 - d) \min_{i=1,2} Q_{\phi_{i, \text{targ}}}(s', a'(s')),](../_images/math/70901eaea34c31e03bb878d7a710a33cb75d1143.svg)

and then both are learned by regressing to this target:

![L(\phi_1, {\mathcal D}) = \underE{(s,a,r,s',d) \sim {\mathcal D}}{
    \Bigg( Q_{\phi_1}(s,a) - y(r,s',d) \Bigg)^2
    },](../_images/math/7d5c18f49a242cc3eec554f717fe4f3bfc119bab.svg)

![L(\phi_2, {\mathcal D}) = \underE{(s,a,r,s',d) \sim {\mathcal D}}{
    \Bigg( Q_{\phi_2}(s,a) - y(r,s',d) \Bigg)^2
    }.](../_images/math/cd73726a8a3845ade467aed57714912f868f6b36.svg)

Using the smaller Q-value for the target, and regressing towards that, helps fend off overestimation in the Q-function.

Lastly: the policy is learned just by maximizing ![Q_{\phi_1}](../_images/math/8795d42bd263dcbe55d123e7466b2dd5091490a7.svg):

![\max_{\theta} \underset{s \sim {\mathcal D}}{{\mathrm E}}\left[ Q_{\phi_1}(s, \mu_{\theta}(s)) \right],](../_images/math/9ed1a541005a48d51b624c3b329897064ec2c065.svg)

which is pretty much unchanged from DDPG. However, in TD3, the policy is updated less frequently than the Q-functions are. This helps damp the volatility that normally arises in DDPG because of how a policy update changes the target.

### [Exploration vs. Exploitation](#id5)[¶](#exploration-vs-exploitation "Permalink to this headline")

TD3 trains a deterministic policy in an off-policy way. Because the policy is deterministic, if the agent were to explore on-policy, in the beginning it would probably not try a wide enough variety of actions to find useful learning signals. To make TD3 policies explore better, we add noise to their actions at training time, typically uncorrelated mean-zero Gaussian noise. To facilitate getting higher-quality training data, you may reduce the scale of the noise over the course of training. (We do not do this in our implementation, and keep noise scale fixed throughout.)

At test time, to see how well the policy exploits what it has learned, we do not add noise to the actions.

You Should Know

Our TD3 implementation uses a trick to improve exploration at the start of training. For a fixed number of steps at the beginning (set with the `start_steps` keyword argument), the agent takes actions which are sampled from a uniform random distribution over valid actions. After that, it returns to normal TD3 exploration.

### [Pseudocode](#id6)[¶](#pseudocode "Permalink to this headline")

![\begin{algorithm}[H]
    \caption{Twin Delayed DDPG}
    \label{alg1}
\begin{algorithmic}[1]
    \STATE Input: initial policy parameters $\theta$, Q-function parameters $\phi_1$, $\phi_2$, empty replay buffer $\mathcal{D}$
    \STATE Set target parameters equal to main parameters $\theta_{\text{targ}} \leftarrow \theta$, $\phi_{\text{targ},1} \leftarrow \phi_1$, $\phi_{\text{targ},2} \leftarrow \phi_2$
    \REPEAT
        \STATE Observe state $s$ and select action $a = \text{clip}(\mu_{\theta}(s) + \epsilon, a_{Low}, a_{High})$, where $\epsilon \sim \mathcal{N}$
        \STATE Execute $a$ in the environment
        \STATE Observe next state $s'$, reward $r$, and done signal $d$ to indicate whether $s'$ is terminal
        \STATE Store $(s,a,r,s',d)$ in replay buffer $\mathcal{D}$
        \STATE If $s'$ is terminal, reset environment state.
        \IF{it's time to update}
            \FOR{$j$ in range(however many updates)}
                \STATE Randomly sample a batch of transitions, $B = \{ (s,a,r,s',d) \}$ from $\mathcal{D}$
                \STATE Compute target actions
                \begin{equation*}
                    a'(s') = \text{clip}\left(\mu_{\theta_{\text{targ}}}(s') + \text{clip}(\epsilon,-c,c), a_{Low}, a_{High}\right), \;\;\;\;\; \epsilon \sim \mathcal{N}(0, \sigma)
                \end{equation*}
                \STATE Compute targets
                \begin{equation*}
                    y(r,s',d) = r + \gamma (1-d) \min_{i=1,2} Q_{\phi_{\text{targ},i}}(s', a'(s'))
                \end{equation*}
                \STATE Update Q-functions by one step of gradient descent using
                \begin{align*}
                    & \nabla_{\phi_i} \frac{1}{|B|}\sum_{(s,a,r,s',d) \in B} \left( Q_{\phi_i}(s,a) - y(r,s',d) \right)^2 && \text{for } i=1,2
                \end{align*}
                \IF{ $j \mod$ \texttt{policy\_delay} $ = 0$}
                    \STATE Update policy by one step of gradient ascent using
                    \begin{equation*}
                        \nabla_{\theta} \frac{1}{|B|}\sum_{s \in B}Q_{\phi_1}(s, \mu_{\theta}(s))
                    \end{equation*}
                    \STATE Update target networks with
                    \begin{align*}
                        \phi_{\text{targ},i} &\leftarrow \rho \phi_{\text{targ}, i} + (1-\rho) \phi_i && \text{for } i=1,2\\
                        \theta_{\text{targ}} &\leftarrow \rho \theta_{\text{targ}} + (1-\rho) \theta
                    \end{align*}
                \ENDIF
            \ENDFOR
        \ENDIF
    \UNTIL{convergence}
\end{algorithmic}
\end{algorithm}](../_images/math/b7dfe8fa3a703b9657dcecb624c4457926e0ce8a.svg)

## [Documentation](#id7)[¶](#documentation "Permalink to this headline")

You Should Know

In what follows, we give documentation for the PyTorch and Tensorflow implementations of TD3 in Spinning Up. They have nearly identical function calls and docstrings, except for details relating to model construction. However, we include both full docstrings for completeness.

### [Documentation: PyTorch Version](#id8)[¶](#documentation-pytorch-version "Permalink to this headline")

`spinup.``td3_pytorch`(*env\_fn*, *actor\_critic=<MagicMock spec='str' id='140554319654248'>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=100*, *replay\_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi\_lr=0.001*, *q\_lr=0.001*, *batch\_size=100*, *start\_steps=10000*, *update\_after=1000*, *update\_every=50*, *act\_noise=0.1*, *target\_noise=0.2*, *noise\_clip=0.5*, *policy\_delay=2*, *num\_test\_episodes=10*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=1*)[¶](#spinup.td3_pytorch "Permalink to this definition")
:   Twin Delayed Deep Deterministic Policy Gradient (TD3)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – The constructor method for a PyTorch Module with an `act`   method, a `pi` module, a `q1` module, and a `q2` module.   The `act` method and `pi` module should accept batches of   observations as inputs, and `q1` and `q2` should accept a batch   of observations and a batch of actions as inputs. When called,   these should return:     | Call | Output Shape | Description |   | --- | --- | --- |   | `act` | (batch, act\_dim) | Numpy array of actions for each  observation. |   | `pi` | (batch, act\_dim) | Tensor containing actions from policy  given observations. |   | `q1` | (batch,) | Tensor containing one current estimate  of Q\* for the provided observations  and actions. (Critical: make sure to  flatten this!) |   | `q2` | (batch,) | Tensor containing the other current  estimate of Q\* for the provided observations  and actions. (Critical: make sure to  flatten this!) | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the ActorCritic object   you provided to TD3. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs to run and train agent. * **replay\_size** (*int*) – Maximum length of replay buffer. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **polyak** (*float*) – Interpolation factor in polyak averaging for target   networks. Target networks are updated towards main networks   according to:  \theta_{\text{targ}} \leftarrow   \rho \theta_{\text{targ}} + (1-\rho) \theta  where \rho is polyak. (Always between 0 and 1, usually   close to 1.) * **pi\_lr** (*float*) – Learning rate for policy. * **q\_lr** (*float*) – Learning rate for Q-networks. * **batch\_size** (*int*) – Minibatch size for SGD. * **start\_steps** (*int*) – Number of steps for uniform-random action selection,   before running real policy. Helps exploration. * **update\_after** (*int*) – Number of env interactions to collect before   starting to do gradient descent updates. Ensures replay buffer   is full enough for useful updates. * **update\_every** (*int*) – Number of env interactions that should elapse   between gradient descent updates. Note: Regardless of how long   you wait between updates, the ratio of env steps to gradient steps   is locked to 1. * **act\_noise** (*float*) – Stddev for Gaussian exploration noise added to   policy at training time. (At test time, no noise is added.) * **target\_noise** (*float*) – Stddev for smoothing noise added to target   policy. * **noise\_clip** (*float*) – Limit for absolute value of target policy   smoothing noise. * **policy\_delay** (*int*) – Policy will only be updated once every   policy\_delay times for each update of the Q-networks. * **num\_test\_episodes** (*int*) – Number of episodes to test the deterministic   policy at the end of each epoch. * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: PyTorch Version](#id9)[¶](#saved-model-contents-pytorch-version "Permalink to this headline")

The PyTorch saved model can be loaded with `ac = torch.load('path/to/model.pt')`, yielding an actor-critic object (`ac`) that has the properties described in the docstring for `td3_pytorch`.

You can get actions from this model with

```
actions = ac.act(torch.as_tensor(obs, dtype=torch.float32))
```

### [Documentation: Tensorflow Version](#id10)[¶](#documentation-tensorflow-version "Permalink to this headline")

`spinup.``td3_tf1`(*env\_fn*, *actor\_critic=<function mlp\_actor\_critic>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=100*, *replay\_size=1000000*, *gamma=0.99*, *polyak=0.995*, *pi\_lr=0.001*, *q\_lr=0.001*, *batch\_size=100*, *start\_steps=10000*, *update\_after=1000*, *update\_every=50*, *act\_noise=0.1*, *target\_noise=0.2*, *noise\_clip=0.5*, *policy\_delay=2*, *num\_test\_episodes=10*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=1*)[¶](#spinup.td3_tf1 "Permalink to this definition")
:   Twin Delayed Deep Deterministic Policy Gradient (TD3)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – A function which takes in placeholder symbols   for state, `x_ph`, and action, `a_ph`, and returns the main   outputs from the agent’s Tensorflow computation graph:     | Symbol | Shape | Description |   | --- | --- | --- |   | `pi` | (batch, act\_dim) | Deterministically computes actions  from policy given states. |   | `q1` | (batch,) | Gives one estimate of Q\* for  states in `x_ph` and actions in  `a_ph`. |   | `q2` | (batch,) | Gives another estimate of Q\* for  states in `x_ph` and actions in  `a_ph`. |   | `q1_pi` | (batch,) | Gives the composition of `q1` and  `pi` for states in `x_ph`:  q1(x, pi(x)). | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the actor\_critic   function you provided to TD3. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs to run and train agent. * **replay\_size** (*int*) – Maximum length of replay buffer. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **polyak** (*float*) – Interpolation factor in polyak averaging for target   networks. Target networks are updated towards main networks   according to:  \theta_{\text{targ}} \leftarrow   \rho \theta_{\text{targ}} + (1-\rho) \theta  where \rho is polyak. (Always between 0 and 1, usually   close to 1.) * **pi\_lr** (*float*) – Learning rate for policy. * **q\_lr** (*float*) – Learning rate for Q-networks. * **batch\_size** (*int*) – Minibatch size for SGD. * **start\_steps** (*int*) – Number of steps for uniform-random action selection,   before running real policy. Helps exploration. * **update\_after** (*int*) – Number of env interactions to collect before   starting to do gradient descent updates. Ensures replay buffer   is full enough for useful updates. * **update\_every** (*int*) – Number of env interactions that should elapse   between gradient descent updates. Note: Regardless of how long   you wait between updates, the ratio of env steps to gradient steps   is locked to 1. * **act\_noise** (*float*) – Stddev for Gaussian exploration noise added to   policy at training time. (At test time, no noise is added.) * **target\_noise** (*float*) – Stddev for smoothing noise added to target   policy. * **noise\_clip** (*float*) – Limit for absolute value of target policy   smoothing noise. * **policy\_delay** (*int*) – Policy will only be updated once every   policy\_delay times for each update of the Q-networks. * **num\_test\_episodes** (*int*) – Number of episodes to test the deterministic   policy at the end of each epoch. * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. |

### [Saved Model Contents: Tensorflow Version](#id11)[¶](#saved-model-contents-tensorflow-version "Permalink to this headline")

The computation graph saved by the logger includes:

| Key | Value |
| --- | --- |
| `x` | Tensorflow placeholder for state input. |
| `a` | Tensorflow placeholder for action input. |
| `pi` | Deterministically computes an action from the agent, conditioned  on states in `x`. |
| `q1` | Gives one action-value estimate for states in `x` and actions in `a`. |
| `q2` | Gives the other action-value estimate for states in `x` and actions in `a`. |

This saved model can be accessed either by

* running the trained policy with the [test\_policy.py](../user/saving_and_loading.html#loading-and-running-trained-policies) tool,
* or loading the whole saved graph into a program with [restore\_tf\_graph](../utils/logger.html#spinup.utils.logx.restore_tf_graph).

## [References](#id12)[¶](#references "Permalink to this headline")

### [Relevant Papers](#id13)[¶](#relevant-papers "Permalink to this headline")

* [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477), Fujimoto et al, 2018

### [Other Public Implementations](#id14)[¶](#other-public-implementations "Permalink to this headline")

* [TD3 release repo](https://github.com/sfujim/TD3)
