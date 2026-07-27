<!-- source: https://spinningup.openai.com/en/latest/algorithms/trpo.html -->

* [Docs](../index.html) »
* Trust Region Policy Optimization
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/algorithms/trpo.rst)

---

# [Trust Region Policy Optimization](#id4)[¶](#trust-region-policy-optimization "Permalink to this headline")

Table of Contents

* [Trust Region Policy Optimization](#trust-region-policy-optimization)
  + [Background](#background)
    - [Quick Facts](#quick-facts)
    - [Key Equations](#key-equations)
    - [Exploration vs. Exploitation](#exploration-vs-exploitation)
    - [Pseudocode](#pseudocode)
  + [Documentation](#documentation)
    - [Saved Model Contents](#saved-model-contents)
  + [References](#references)
    - [Relevant Papers](#relevant-papers)
    - [Why These Papers?](#why-these-papers)
    - [Other Public Implementations](#other-public-implementations)

## [Background](#id5)[¶](#background "Permalink to this headline")

(Previously: [Background for VPG](../algorithms/vpg.html#background))

TRPO updates policies by taking the largest step possible to improve performance, while satisfying a special constraint on how close the new and old policies are allowed to be. The constraint is expressed in terms of [KL-Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence), a measure of (something like, but not exactly) distance between probability distributions.

This is different from normal policy gradient, which keeps new and old policies close in parameter space. But even seemingly small differences in parameter space can have very large differences in performance—so a single bad step can collapse the policy performance. This makes it dangerous to use large step sizes with vanilla policy gradients, thus hurting its sample efficiency. TRPO nicely avoids this kind of collapse, and tends to quickly and monotonically improve performance.

### [Quick Facts](#id6)[¶](#quick-facts "Permalink to this headline")

* TRPO is an on-policy algorithm.
* TRPO can be used for environments with either discrete or continuous action spaces.
* The Spinning Up implementation of TRPO supports parallelization with MPI.

### [Key Equations](#id7)[¶](#key-equations "Permalink to this headline")

Let ![\pi_{\theta}](../_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg) denote a policy with parameters ![\theta](../_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg). The theoretical TRPO update is:

![\theta_{k+1} = \arg \max_{\theta} \; & {\mathcal L}(\theta_k, \theta) \\
\text{s.t.} \; & \bar{D}_{KL}(\theta || \theta_k) \leq \delta](../_images/math/23edf1f72f63a4729c40371c1481a36549a0b713.svg)

where ![{\mathcal L}(\theta_k, \theta)](../_images/math/0837b005b194415b2b922e42be1df8601b552857.svg) is the *surrogate advantage*, a measure of how policy ![\pi_{\theta}](../_images/math/6a71f04b65d9524fb656715cda85d7540a9ddf9f.svg) performs relative to the old policy ![\pi_{\theta_k}](../_images/math/d8bb9f337fa712549e0428223df820773aa1169d.svg) using data from the old policy:

![{\mathcal L}(\theta_k, \theta) = \underE{s,a \sim \pi_{\theta_k}}{
    \frac{\pi_{\theta}(a|s)}{\pi_{\theta_k}(a|s)} A^{\pi_{\theta_k}}(s,a)
    },](../_images/math/ae8edab1e9c727bed15e54d4dda492382538b5fe.svg)

and ![\bar{D}_{KL}(\theta || \theta_k)](../_images/math/88396050a58384b85dfaa6fce02cf39d98c78c4b.svg) is an average KL-divergence between policies across states visited by the old policy:

![\bar{D}_{KL}(\theta || \theta_k) = \underE{s \sim \pi_{\theta_k}}{
    D_{KL}\left(\pi_{\theta}(\cdot|s) || \pi_{\theta_k} (\cdot|s) \right)
}.](../_images/math/78a651e0ce4979bd3e17198594ad952ac20b9b45.svg)

You Should Know

The objective and constraint are both zero when ![\theta = \theta_k](../_images/math/2ae54d61543a208d042466ff3554871467c23d30.svg). Furthermore, the gradient of the constraint with respect to ![\theta](../_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg) is zero when ![\theta = \theta_k](../_images/math/2ae54d61543a208d042466ff3554871467c23d30.svg). Proving these facts requires some subtle command of the relevant math—it’s an exercise worth doing, whenever you feel ready!

The theoretical TRPO update isn’t the easiest to work with, so TRPO makes some approximations to get an answer quickly. We Taylor expand the objective and constraint to leading order around ![\theta_k](../_images/math/a485f77ef16acbb27539cdfe8286cd6029ccfd26.svg):

![{\mathcal L}(\theta_k, \theta) &\approx g^T (\theta - \theta_k) \\
\bar{D}_{KL}(\theta || \theta_k) & \approx \frac{1}{2} (\theta - \theta_k)^T H (\theta - \theta_k)](../_images/math/7cdaa039734ec1d09adcc3e4dc351085823085cf.svg)

resulting in an approximate optimization problem,

![\theta_{k+1} = \arg \max_{\theta} \; & g^T (\theta - \theta_k) \\
\text{s.t.} \; & \frac{1}{2} (\theta - \theta_k)^T H (\theta - \theta_k) \leq \delta.](../_images/math/69c9dcbe2fe1c669a1b2cb3a312a479cdfcb27a1.svg)

You Should Know

By happy coincidence, the gradient ![g](../_images/math/7c8bf3a1920993c53ae254d3f08d697f368af350.svg) of the surrogate advantage function with respect to ![\theta](../_images/math/ce5edddd490112350f4bd555d9390e0e845f754a.svg), evaluated at ![\theta = \theta_k](../_images/math/2ae54d61543a208d042466ff3554871467c23d30.svg), is exactly equal to the policy gradient, ![\nabla_{\theta} J(\pi_{\theta})](../_images/math/fdc185c68404ece5c4deef076c9713af689421a2.svg)! Try proving this, if you feel comfortable diving into the math.

This approximate problem can be analytically solved by the methods of Lagrangian duality [[1]](#id2), yielding the solution:

![\theta_{k+1} = \theta_k + \sqrt{\frac{2 \delta}{g^T H^{-1} g}} H^{-1} g.](../_images/math/e990f7ff0230a8fa93cf1242ea0d49fdf63d05d7.svg)

If we were to stop here, and just use this final result, the algorithm would be exactly calculating the [Natural Policy Gradient](https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf). A problem is that, due to the approximation errors introduced by the Taylor expansion, this may not satisfy the KL constraint, or actually improve the surrogate advantage. TRPO adds a modification to this update rule: a backtracking line search,

![\theta_{k+1} = \theta_k + \alpha^j \sqrt{\frac{2 \delta}{g^T H^{-1} g}} H^{-1} g,](../_images/math/03cabd66ab79d8c17e36fc4247bb46fe0c6dcbfc.svg)

where ![\alpha \in (0,1)](../_images/math/85e2502878c575c6e250a9224be42065ac9844d2.svg) is the backtracking coefficient, and ![j](../_images/math/b42a5fa0aad66603180aff0fc5e346e98a2364ca.svg) is the smallest nonnegative integer such that ![\pi_{\theta_{k+1}}](../_images/math/3944f0149054734c7f8537d8f9316cd77cbbb143.svg) satisfies the KL constraint and produces a positive surrogate advantage.

Lastly: computing and storing the matrix inverse, ![H^{-1}](../_images/math/c61d52a1bdbbfa95c007324ae431066f95be2296.svg), is painfully expensive when dealing with neural network policies with thousands or millions of parameters. TRPO sidesteps the issue by using the [conjugate gradient](https://en.wikipedia.org/wiki/Conjugate_gradient_method) algorithm to solve ![Hx = g](../_images/math/1e5b7619f5aff65751670c7d6b3527e5721a9033.svg) for ![x = H^{-1} g](../_images/math/a0181d85fab06c9716a1bb2561dbf0f8534ef172.svg), requiring only a function which can compute the matrix-vector product ![Hx](../_images/math/7c097b2fe748e8a45446bdc5d27721c82b75e969.svg) instead of computing and storing the whole matrix ![H](../_images/math/bf6bcb1745aeab36cdc185e9f75bbfd3998352ce.svg) directly. This is not too hard to do: we set up a symbolic operation to calculate

![Hx = \nabla_{\theta} \left( \left(\nabla_{\theta} \bar{D}_{KL}(\theta || \theta_k)\right)^T x \right),](../_images/math/2b50eb41a25af9e480d1c6facfafe1218624fc35.svg)

which gives us the correct output without computing the whole matrix.

|  |  |
| --- | --- |
| [[1]](#id1) | See [Convex Optimization](http://stanford.edu/~boyd/cvxbook/) by Boyd and Vandenberghe, especially chapters 2 through 5. |

### [Exploration vs. Exploitation](#id8)[¶](#exploration-vs-exploitation "Permalink to this headline")

TRPO trains a stochastic policy in an on-policy way. This means that it explores by sampling actions according to the latest version of its stochastic policy. The amount of randomness in action selection depends on both initial conditions and the training procedure. Over the course of training, the policy typically becomes progressively less random, as the update rule encourages it to exploit rewards that it has already found. This may cause the policy to get trapped in local optima.

### [Pseudocode](#id9)[¶](#pseudocode "Permalink to this headline")

![\begin{algorithm}[H]
    \caption{Trust Region Policy Optimization}
    \label{alg1}
\begin{algorithmic}[1]
    \STATE Input: initial policy parameters $\theta_0$, initial value function parameters $\phi_0$
    \STATE Hyperparameters: KL-divergence limit $\delta$, backtracking coefficient $\alpha$, maximum number of backtracking steps $K$
    \FOR{$k = 0,1,2,...$}
    \STATE Collect set of trajectories ${\mathcal D}_k = \{\tau_i\}$ by running policy $\pi_k = \pi(\theta_k)$ in the environment.
    \STATE Compute rewards-to-go $\hat{R}_t$.
    \STATE Compute advantage estimates, $\hat{A}_t$ (using any method of advantage estimation) based on the current value function $V_{\phi_k}$.
    \STATE Estimate policy gradient as
        \begin{equation*}
        \hat{g}_k = \frac{1}{|{\mathcal D}_k|} \sum_{\tau \in {\mathcal D}_k} \sum_{t=0}^T \left. \nabla_{\theta} \log\pi_{\theta}(a_t|s_t)\right|_{\theta_k} \hat{A}_t.
        \end{equation*}
    \STATE Use the conjugate gradient algorithm to compute
        \begin{equation*}
        \hat{x}_k \approx \hat{H}_k^{-1} \hat{g}_k,
        \end{equation*}
        where $\hat{H}_k$ is the Hessian of the sample average KL-divergence.
    \STATE Update the policy by backtracking line search with
        \begin{equation*}
        \theta_{k+1} = \theta_k + \alpha^j \sqrt{ \frac{2\delta}{\hat{x}_k^T \hat{H}_k \hat{x}_k}} \hat{x}_k,
        \end{equation*}
        where $j \in \{0, 1, 2, ... K\}$ is the smallest value which improves the sample loss and satisfies the sample KL-divergence constraint.
    \STATE Fit value function by regression on mean-squared error:
        \begin{equation*}
        \phi_{k+1} = \arg \min_{\phi} \frac{1}{|{\mathcal D}_k| T} \sum_{\tau \in {\mathcal D}_k} \sum_{t=0}^T\left( V_{\phi} (s_t) - \hat{R}_t \right)^2,
        \end{equation*}
        typically via some gradient descent algorithm.
    \ENDFOR
\end{algorithmic}
\end{algorithm}](../_images/math/5808864ea60ebc3702704717d9f4c3773c90540d.svg)

## [Documentation](#id10)[¶](#documentation "Permalink to this headline")

You Should Know

Spinning Up currently only has a Tensorflow implementation of TRPO.

`spinup.``trpo_tf1`(*env\_fn*, *actor\_critic=<function mlp\_actor\_critic>*, *ac\_kwargs={}*, *seed=0*, *steps\_per\_epoch=4000*, *epochs=50*, *gamma=0.99*, *delta=0.01*, *vf\_lr=0.001*, *train\_v\_iters=80*, *damping\_coeff=0.1*, *cg\_iters=10*, *backtrack\_iters=10*, *backtrack\_coeff=0.8*, *lam=0.97*, *max\_ep\_len=1000*, *logger\_kwargs={}*, *save\_freq=10*, *algo='trpo'*)[¶](#spinup.trpo_tf1 "Permalink to this definition")
:   Trust Region Policy Optimization

    (with support for Natural Policy Gradient)

    | Parameters: | * **env\_fn** – A function which creates a copy of the environment.   The environment must satisfy the OpenAI Gym API. * **actor\_critic** – A function which takes in placeholder symbols   for state, `x_ph`, and action, `a_ph`, and returns the main   outputs from the agent’s Tensorflow computation graph:     | Symbol | Shape | Description |   | --- | --- | --- |   | `pi` | (batch, act\_dim) | Samples actions from policy given  states. |   | `logp` | (batch,) | Gives log probability, according to  the policy, of taking actions `a_ph`  in states `x_ph`. |   | `logp_pi` | (batch,) | Gives log probability, according to  the policy, of the action sampled by  `pi`. |   | `info` | N/A | A dict of any intermediate quantities  (from calculating the policy or log  probabilities) which are needed for  analytically computing KL divergence.  (eg sufficient statistics of the  distributions) |   | `info_phs` | N/A | A dict of placeholders for old values  of the entries in `info`. |   | `d_kl` | () | A symbol for computing the mean KL  divergence between the current policy  (`pi`) and the old policy (as  specified by the inputs to  `info_phs`) over the batch of  states given in `x_ph`. |   | `v` | (batch,) | Gives the value estimate for states  in `x_ph`. (Critical: make sure  to flatten this!) | * **ac\_kwargs** (*dict*) – Any kwargs appropriate for the actor\_critic   function you provided to TRPO. * **seed** (*int*) – Seed for random number generators. * **steps\_per\_epoch** (*int*) – Number of steps of interaction (state-action pairs)   for the agent and the environment in each epoch. * **epochs** (*int*) – Number of epochs of interaction (equivalent to   number of policy updates) to perform. * **gamma** (*float*) – Discount factor. (Always between 0 and 1.) * **delta** (*float*) – KL-divergence limit for TRPO / NPG update.   (Should be small for stability. Values like 0.01, 0.05.) * **vf\_lr** (*float*) – Learning rate for value function optimizer. * **train\_v\_iters** (*int*) – Number of gradient descent steps to take on   value function per epoch. * **damping\_coeff** (*float*) – Artifact for numerical stability, should be   smallish. Adjusts Hessian-vector product calculation:  Hv \rightarrow (\alpha I + H)v  where \alpha is the damping coefficient.   Probably don’t play with this hyperparameter. * **cg\_iters** (*int*) – Number of iterations of conjugate gradient to perform.   Increasing this will lead to a more accurate approximation   to H^{-1} g, and possibly slightly-improved performance,   but at the cost of slowing things down.  Also probably don’t play with this hyperparameter. * **backtrack\_iters** (*int*) – Maximum number of steps allowed in the   backtracking line search. Since the line search usually doesn’t   backtrack, and usually only steps back once when it does, this   hyperparameter doesn’t often matter. * **backtrack\_coeff** (*float*) – How far back to step during backtracking line   search. (Always between 0 and 1, usually above 0.5.) * **lam** (*float*) – Lambda for GAE-Lambda. (Always between 0 and 1,   close to 1.) * **max\_ep\_len** (*int*) – Maximum length of trajectory / episode / rollout. * **logger\_kwargs** (*dict*) – Keyword args for EpochLogger. * **save\_freq** (*int*) – How often (in terms of gap between epochs) to save   the current policy and value function. * **algo** – Either ‘trpo’ or ‘npg’: this code supports both, since they are   almost the same. |

### [Saved Model Contents](#id11)[¶](#saved-model-contents "Permalink to this headline")

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

* [Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477), Schulman et al. 2015
* [High Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438), Schulman et al. 2016
* [Approximately Optimal Approximate Reinforcement Learning](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/KakadeLangford-icml2002.pdf), Kakade and Langford 2002

### [Why These Papers?](#id14)[¶](#why-these-papers "Permalink to this headline")

Schulman 2015 is included because it is the original paper describing TRPO. Schulman 2016 is included because our implementation of TRPO makes use of Generalized Advantage Estimation for computing the policy gradient. Kakade and Langford 2002 is included because it contains theoretical results which motivate and deeply connect to the theoretical foundations of TRPO.

### [Other Public Implementations](#id15)[¶](#other-public-implementations "Permalink to this headline")

* [Baselines](https://github.com/openai/baselines/tree/master/baselines/trpo_mpi)
* [ModularRL](https://github.com/joschu/modular_rl/blob/master/modular_rl/trpo.py)
* [rllab](https://github.com/rll/rllab/blob/master/rllab/algos/trpo.py)
