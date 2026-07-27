<!-- source: https://spinningup.openai.com/en/latest/user/installation.html -->

* [Docs](../index.html) »
* Installation
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/user/installation.rst)

---

# [Installation](#id3)[¶](#installation "Permalink to this headline")

Table of Contents

* [Installation](#installation)
  + [Installing Python](#installing-python)
  + [Installing OpenMPI](#installing-openmpi)
    - [Ubuntu](#ubuntu)
    - [Mac OS X](#mac-os-x)
  + [Installing Spinning Up](#installing-spinning-up)
  + [Check Your Install](#check-your-install)
  + [Installing MuJoCo (Optional)](#installing-mujoco-optional)

Spinning Up requires Python3, OpenAI Gym, and OpenMPI.

Spinning Up is currently only supported on Linux and OSX. It may be possible to install on Windows, though this hasn’t been extensively tested. [[1]](#id2)

You Should Know

Many examples and benchmarks in Spinning Up refer to RL environments that use the [MuJoCo](http://www.mujoco.org/index.html) physics engine. MuJoCo is a proprietary software that requires a license, which is free to trial and free for students, but otherwise is not free. As a result, installing it is optional, but because of its importance to the research community—it is the de facto standard for benchmarking deep RL algorithms in continuous control—it is preferred.

Don’t worry if you decide not to install MuJoCo, though. You can definitely get started in RL by running RL algorithms on the [Classic Control](https://gym.openai.com/envs/#classic_control) and [Box2d](https://gym.openai.com/envs/#box2d) environments in Gym, which are totally free to use.

|  |  |
| --- | --- |
| [[1]](#id1) | It looks like at least one person has figured out [a workaround for running on Windows](https://github.com/openai/spinningup/issues/23). If you try another way and succeed, please let us know how you did it! |

## [Installing Python](#id4)[¶](#installing-python "Permalink to this headline")

We recommend installing Python through Anaconda. Anaconda is a library that includes Python and many useful packages for Python, as well as an environment manager called conda that makes package management simple.

Follow [the installation instructions](https://docs.continuum.io/anaconda/install/) for Anaconda here. Download and install Anaconda3 (at time of writing, [Anaconda3-5.3.0](https://repo.anaconda.com/archive/)). Then create a conda Python 3.6 env for organizing packages used in Spinning Up:

```
conda create -n spinningup python=3.6
```

To use Python from the environment you just created, activate the environment with:

```
conda activate spinningup
```

You Should Know

If you’re new to python environments and package management, this stuff can quickly get confusing or overwhelming, and you’ll probably hit some snags along the way. (Especially, you should expect problems like, “I just installed this thing, but it says it’s not found when I try to use it!”) You may want to read through some clean explanations about what package management is, why it’s a good idea, and what commands you’ll typically have to execute to correctly use it.

[FreeCodeCamp](https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c) has a good explanation worth reading. There’s a shorter description on [Towards Data Science](https://towardsdatascience.com/environment-management-with-conda-python-2-3-b9961a8a5097) which is also helpful and informative. Finally, if you’re an extremely patient person, you may want to read the (dry, but very informative) [documentation page from Conda](https://conda.io/docs/user-guide/tasks/manage-environments.html).

## [Installing OpenMPI](#id5)[¶](#installing-openmpi "Permalink to this headline")

### [Ubuntu](#id6)[¶](#ubuntu "Permalink to this headline")

```
sudo apt-get update && sudo apt-get install libopenmpi-dev
```

### [Mac OS X](#id7)[¶](#mac-os-x "Permalink to this headline")

Installation of system packages on Mac requires [Homebrew](https://brew.sh). With Homebrew installed, run the follwing:

```
brew install openmpi
```

## [Installing Spinning Up](#id8)[¶](#installing-spinning-up "Permalink to this headline")

```
git clone https://github.com/openai/spinningup.git
cd spinningup
pip install -e .
```

You Should Know

Spinning Up defaults to installing everything in Gym **except** the MuJoCo environments. In case you run into any trouble with the Gym installation, check out the [Gym](https://github.com/openai/gym) github page for help. If you want the MuJoCo environments, see the optional installation section below.

## [Check Your Install](#id9)[¶](#check-your-install "Permalink to this headline")

To see if you’ve successfully installed Spinning Up, try running PPO in the LunarLander-v2 environment with

```
python -m spinup.run ppo --hid "[32,32]" --env LunarLander-v2 --exp_name installtest --gamma 0.999
```

This might run for around 10 minutes, and you can leave it going in the background while you continue reading through documentation. This won’t train the agent to completion, but will run it for long enough that you can see *some* learning progress when the results come in.

After it finishes training, watch a video of the trained policy with

```
python -m spinup.run test_policy data/installtest/installtest_s0
```

And plot the results with

```
python -m spinup.run plot data/installtest/installtest_s0
```

## [Installing MuJoCo (Optional)](#id10)[¶](#installing-mujoco-optional "Permalink to this headline")

First, go to the [mujoco-py](https://github.com/openai/mujoco-py) github page. Follow the installation instructions in the README, which describe how to install the MuJoCo physics engine and the mujoco-py package (which allows the use of MuJoCo from Python).

You Should Know

In order to use the MuJoCo simulator, you will need to get a [MuJoCo license](https://www.roboti.us/license.html). Free 30-day licenses are available to anyone, and free 1-year licenses are available to full-time students.

Once you have installed MuJoCo, install the corresponding Gym environments with

```
pip install gym[mujoco,robotics]
```

And then check that things are working by running PPO in the Walker2d-v2 environment with

```
python -m spinup.run ppo --hid "[32,32]" --env Walker2d-v2 --exp_name mujocotest
```
