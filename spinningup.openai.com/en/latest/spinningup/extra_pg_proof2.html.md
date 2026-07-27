<!-- source: https://spinningup.openai.com/en/latest/spinningup/extra_pg_proof2.html -->

* [Docs](../index.html) »
* Extra Material
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/spinningup/extra_pg_proof2.rst)

---

# Extra Material[¶](#extra-material "Permalink to this headline")

## Proof for Using Q-Function in Policy Gradient Formula[¶](#proof-for-using-q-function-in-policy-gradient-formula "Permalink to this headline")

In this section, we will show that

![\nabla_{\theta} J(\pi_{\theta}) &= \underE{\tau \sim \pi_{\theta}}{\sum_{t=0}^{T} \Big( \nabla_{\theta} \log \pi_{\theta}(a_t |s_t) \Big) Q^{\pi_{\theta}}(s_t, a_t)},](../_images/math/4b2f1bfad30261bf9c79cfcec23c204f7d27c925.svg)

for the finite-horizon undiscounted return setting. (An analagous result holds in the infinite-horizon discounted case using basically the same proof.)

The proof of this claim depends on the [law of iterated expectations](https://en.wikipedia.org/wiki/Law_of_total_expectation). First, let’s rewrite the expression for the policy gradient, starting from the reward-to-go form (using the notation ![\hat{R}_t = \sum_{t'=t}^T R(s_t', a_t', s_{t'+1})](../_images/math/93d1a7a644010a1f19c48e5d562bf4385b61fd2f.svg) to help shorten things):

![\nabla_{\theta} J(\pi_{\theta}) &= \underE{\tau \sim \pi_{\theta}}{\sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}(a_t |s_t) \hat{R}_t} \\
&= \sum_{t=0}^{T} \underE{\tau \sim \pi_{\theta}}{\nabla_{\theta} \log \pi_{\theta}(a_t |s_t) \hat{R}_t}](../_images/math/c68a688cf6fab9d94bbe3856eafe6a9020e12da3.svg)

Define ![\tau_{:t} = (s_0, a_0, ..., s_t, a_t)](../_images/math/9ab1b47a2cb99159226caa7c4e67ac8f4c64ee77.svg) as the trajectory up to time ![t](../_images/math/7ed8f1921a380f7a5f45b87825838fdced658554.svg), and ![\tau_{t:}](../_images/math/9d2a79fcf2fd5f91053b653e06cf86a4e7cfd3b7.svg) as the remainder of the trajectory after that. By the law of iterated expectations, we can break up the preceding expression into:

![\nabla_{\theta} J(\pi_{\theta}) &= \sum_{t=0}^{T} \underE{\tau_{:t} \sim \pi_{\theta}}{ \underE{\tau_{t:} \sim \pi_{\theta}}{ \left. \nabla_{\theta} \log \pi_{\theta}(a_t |s_t) \hat{R}_t \right| \tau_{:t}}}](../_images/math/23f6fe0a82310a1ed75443875d381016b9f3f168.svg)

The grad-log-prob is constant with respect to the inner expectation (because it depends on ![s_t](../_images/math/4fcf0bf03c2a691496ce04ade269159d8b89caa5.svg) and ![a_t](../_images/math/39079fcebc9eb2aba4ab3fe7359b34807ceccc0e.svg), which the inner expectation conditions on as fixed in ![\tau_{:t}](../_images/math/2d97587eeb6a7ad6d9094cfc6aa37cb24c8c3c67.svg)), so it can be pulled out, leaving:

![\nabla_{\theta} J(\pi_{\theta}) &= \sum_{t=0}^{T} \underE{\tau_{:t} \sim \pi_{\theta}}{ \nabla_{\theta} \log \pi_{\theta}(a_t |s_t) \underE{\tau_{t:} \sim \pi_{\theta}}{ \left. \hat{R}_t \right| \tau_{:t}}}](../_images/math/900059084e4a2fced54f9c57972efcea670c78af.svg)

In Markov Decision Processes, the future only depends on the most recent state and action. As a result, the inner expectation—which expects over the future, conditioned on the entirety of the past (everything up to time ![t](../_images/math/7ed8f1921a380f7a5f45b87825838fdced658554.svg))—is equal to the same expectation if it only conditioned on the last timestep (just ![(s_t,a_t)](../_images/math/4d4a7d280fc856d9a70d7d6725f4cef51d69b271.svg)):

![\underE{\tau_{t:} \sim \pi_{\theta}}{ \left. \hat{R}_t \right| \tau_{:t}} = \underE{\tau_{t:} \sim \pi_{\theta}}{ \left. \hat{R}_t \right| s_t, a_t},](../_images/math/7ac77f09885856d3c50f51b9e02fe5d3611a73fe.svg)

which is the *definition* of ![Q^{\pi_{\theta}}(s_t, a_t)](../_images/math/21dcea11b74d102a8208fcb04141a15184831377.svg): the expected return, starting from state ![s_t](../_images/math/4fcf0bf03c2a691496ce04ade269159d8b89caa5.svg) and action ![a_t](../_images/math/39079fcebc9eb2aba4ab3fe7359b34807ceccc0e.svg), when acting on-policy for the rest of the trajectory.

The result follows immediately.
