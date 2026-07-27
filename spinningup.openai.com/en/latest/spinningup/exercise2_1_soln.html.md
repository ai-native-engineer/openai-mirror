<!-- source: https://spinningup.openai.com/en/latest/spinningup/exercise2_1_soln.html -->

* [Docs](../index.html) »
* Solution to Exercise 2.1
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/spinningup/exercise2_1_soln.rst)

---

# Solution to Exercise 2.1[¶](#solution-to-exercise-2-1 "Permalink to this headline")

![../_images/ex2-1_trpo_hopper.png](../_images/ex2-1_trpo_hopper.png)

Learning curves for TRPO in Hopper-v2 with different values of `train_v_iters`, averaged over three random seeds.

The difference is quite substantial: with a trained value function, the agent is able to quickly make progress. With an untrained value function, the agent gets stuck early on.
