<!-- source: https://spinningup.openai.com/en/latest/spinningup/bench.html -->

* [Docs](../index.html) »
* Benchmarks for Spinning Up Implementations
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/spinningup/bench.rst)

---

# [Benchmarks for Spinning Up Implementations](#id11)[¶](#benchmarks-for-spinning-up-implementations "Permalink to this headline")

Table of Contents

* [Benchmarks for Spinning Up Implementations](#benchmarks-for-spinning-up-implementations)
  + [Performance in Each Environment](#performance-in-each-environment)
    - [HalfCheetah: PyTorch Versions](#halfcheetah-pytorch-versions)
    - [HalfCheetah: Tensorflow Versions](#halfcheetah-tensorflow-versions)
    - [Hopper: PyTorch Versions](#hopper-pytorch-versions)
    - [Hopper: Tensorflow Versions](#hopper-tensorflow-versions)
    - [Walker2d: PyTorch Versions](#walker2d-pytorch-versions)
    - [Walker2d: Tensorflow Versions](#walker2d-tensorflow-versions)
    - [Swimmer: PyTorch Versions](#swimmer-pytorch-versions)
    - [Swimmer: Tensorflow Versions](#swimmer-tensorflow-versions)
    - [Ant: PyTorch Versions](#ant-pytorch-versions)
    - [Ant: Tensorflow Versions](#ant-tensorflow-versions)
  + [Experiment Details](#experiment-details)
  + [PyTorch vs Tensorflow](#pytorch-vs-tensorflow)

We benchmarked the Spinning Up algorithm implementations in five environments from the [MuJoCo](https://gym.openai.com/envs/#mujoco) Gym task suite: HalfCheetah, Hopper, Walker2d, Swimmer, and Ant.

## [Performance in Each Environment](#id12)[¶](#performance-in-each-environment "Permalink to this headline")

### [HalfCheetah: PyTorch Versions](#id13)[¶](#halfcheetah-pytorch-versions "Permalink to this headline")

![../_images/pytorch_halfcheetah_performance.svg](../_images/pytorch_halfcheetah_performance.svg)

3M timestep benchmark for HalfCheetah-v3 using **PyTorch** implementations.

### [HalfCheetah: Tensorflow Versions](#id14)[¶](#halfcheetah-tensorflow-versions "Permalink to this headline")

![../_images/tensorflow_halfcheetah_performance.svg](../_images/tensorflow_halfcheetah_performance.svg)

3M timestep benchmark for HalfCheetah-v3 using **Tensorflow** implementations.

### [Hopper: PyTorch Versions](#id15)[¶](#hopper-pytorch-versions "Permalink to this headline")

![../_images/pytorch_hopper_performance.svg](../_images/pytorch_hopper_performance.svg)

3M timestep benchmark for Hopper-v3 using **PyTorch** implementations.

### [Hopper: Tensorflow Versions](#id16)[¶](#hopper-tensorflow-versions "Permalink to this headline")

![../_images/tensorflow_hopper_performance.svg](../_images/tensorflow_hopper_performance.svg)

3M timestep benchmark for Hopper-v3 using **Tensorflow** implementations.

### [Walker2d: PyTorch Versions](#id17)[¶](#walker2d-pytorch-versions "Permalink to this headline")

![../_images/pytorch_walker2d_performance.svg](../_images/pytorch_walker2d_performance.svg)

3M timestep benchmark for Walker2d-v3 using **PyTorch** implementations.

### [Walker2d: Tensorflow Versions](#id18)[¶](#walker2d-tensorflow-versions "Permalink to this headline")

![../_images/tensorflow_walker2d_performance.svg](../_images/tensorflow_walker2d_performance.svg)

3M timestep benchmark for Walker2d-v3 using **Tensorflow** implementations.

### [Swimmer: PyTorch Versions](#id19)[¶](#swimmer-pytorch-versions "Permalink to this headline")

![../_images/pytorch_swimmer_performance.svg](../_images/pytorch_swimmer_performance.svg)

3M timestep benchmark for Swimmer-v3 using **PyTorch** implementations.

### [Swimmer: Tensorflow Versions](#id20)[¶](#swimmer-tensorflow-versions "Permalink to this headline")

![../_images/tensorflow_swimmer_performance.svg](../_images/tensorflow_swimmer_performance.svg)

3M timestep benchmark for Swimmer-v3 using **Tensorflow** implementations.

### [Ant: PyTorch Versions](#id21)[¶](#ant-pytorch-versions "Permalink to this headline")

![../_images/pytorch_ant_performance.svg](../_images/pytorch_ant_performance.svg)

3M timestep benchmark for Ant-v3 using **PyTorch** implementations.

### [Ant: Tensorflow Versions](#id22)[¶](#ant-tensorflow-versions "Permalink to this headline")

![../_images/tensorflow_ant_performance.svg](../_images/tensorflow_ant_performance.svg)

3M timestep benchmark for Ant-v3 using **Tensorflow** implementations.

## [Experiment Details](#id23)[¶](#experiment-details "Permalink to this headline")

**Random seeds.** All experiments were run for 10 random seeds each. Graphs show the average (solid line) and std dev (shaded) of performance over random seed over the course of training.

**Performance metric.** Performance for the on-policy algorithms is measured as the average trajectory return across the batch collected at each epoch. Performance for the off-policy algorithms is measured once every 10,000 steps by running the deterministic policy (or, in the case of SAC, the mean policy) without action noise for ten trajectories, and reporting the average return over those test trajectories.

**Network architectures.** The on-policy algorithms use networks of size (64, 32) with tanh units for both the policy and the value function. The off-policy algorithms use networks of size (256, 256) with relu units.

**Batch size.** The on-policy algorithms collected 4000 steps of agent-environment interaction per batch update. The off-policy algorithms used minibatches of size 100 at each gradient descent step.

All other hyperparameters are left at default settings for the Spinning Up implementations. See algorithm pages for details.

Learning curves are smoothed by averaging over a window of 11 epochs.

You Should Know

By comparison to the literature, the Spinning Up implementations of DDPG, TD3, and SAC are roughly at-parity with the best reported results for these algorithms. As a result, you can use the Spinning Up implementations of these algorithms for research purposes.

The Spinning Up implementations of VPG, TRPO, and PPO are overall a bit weaker than the best reported results for these algorithms. This is due to the absence of some standard tricks (such as observation normalization and normalized value regression targets) from our implementations. For research comparisons, you should use the implementations of TRPO or PPO from [OpenAI Baselines](https://github.com/openai/baselines).

## [PyTorch vs Tensorflow](#id24)[¶](#pytorch-vs-tensorflow "Permalink to this headline")

We provide graphs for head-to-head comparisons between the PyTorch and Tensorflow implementations of each algorithm at the following pages:

* [VPG Head-to-Head](../spinningup/bench_vpg.html)
* [PPO Head-to-Head](../spinningup/bench_ppo.html)
* [DDPG Head-to-Head](../spinningup/bench_ddpg.html)
* [TD3 Head-to-Head](../spinningup/bench_td3.html)
* [SAC Head-to-Head](../spinningup/bench_sac.html)
