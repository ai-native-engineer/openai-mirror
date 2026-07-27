<!-- source: https://spinningup.openai.com/en/latest/ -->

* [Docs](#) »
* Welcome to Spinning Up in Deep RL!
* [Edit on GitHub](https://github.com/openai/spinningup/blob/master/docs/index.rst)

---

# Welcome to Spinning Up in Deep RL![¶](#welcome-to-spinning-up-in-deep-rl "Permalink to this headline")

![_images/spinning-up-in-rl.png](_images/spinning-up-in-rl.png)

User Documentation

* [Introduction](user/introduction.html)
  + [What This Is](user/introduction.html#what-this-is)
  + [Why We Built This](user/introduction.html#why-we-built-this)
  + [How This Serves Our Mission](user/introduction.html#how-this-serves-our-mission)
  + [Code Design Philosophy](user/introduction.html#code-design-philosophy)
  + [Long-Term Support and Support History](user/introduction.html#long-term-support-and-support-history)
* [Installation](user/installation.html)
  + [Installing Python](user/installation.html#installing-python)
  + [Installing OpenMPI](user/installation.html#installing-openmpi)
  + [Installing Spinning Up](user/installation.html#installing-spinning-up)
  + [Check Your Install](user/installation.html#check-your-install)
  + [Installing MuJoCo (Optional)](user/installation.html#installing-mujoco-optional)
* [Algorithms](user/algorithms.html)
  + [What’s Included](user/algorithms.html#what-s-included)
  + [Why These Algorithms?](user/algorithms.html#why-these-algorithms)
  + [Code Format](user/algorithms.html#code-format)
* [Running Experiments](user/running.html)
  + [Launching from the Command Line](user/running.html#launching-from-the-command-line)
  + [Launching from Scripts](user/running.html#launching-from-scripts)
* [Experiment Outputs](user/saving_and_loading.html)
  + [Algorithm Outputs](user/saving_and_loading.html#algorithm-outputs)
  + [Save Directory Location](user/saving_and_loading.html#save-directory-location)
  + [Loading and Running Trained Policies](user/saving_and_loading.html#loading-and-running-trained-policies)
* [Plotting Results](user/plotting.html)

Introduction to RL

* [Part 1: Key Concepts in RL](spinningup/rl_intro.html)
  + [What Can RL Do?](spinningup/rl_intro.html#what-can-rl-do)
  + [Key Concepts and Terminology](spinningup/rl_intro.html#key-concepts-and-terminology)
  + [(Optional) Formalism](spinningup/rl_intro.html#optional-formalism)
* [Part 2: Kinds of RL Algorithms](spinningup/rl_intro2.html)
  + [A Taxonomy of RL Algorithms](spinningup/rl_intro2.html#a-taxonomy-of-rl-algorithms)
  + [Links to Algorithms in Taxonomy](spinningup/rl_intro2.html#links-to-algorithms-in-taxonomy)
* [Part 3: Intro to Policy Optimization](spinningup/rl_intro3.html)
  + [Deriving the Simplest Policy Gradient](spinningup/rl_intro3.html#deriving-the-simplest-policy-gradient)
  + [Implementing the Simplest Policy Gradient](spinningup/rl_intro3.html#implementing-the-simplest-policy-gradient)
  + [Expected Grad-Log-Prob Lemma](spinningup/rl_intro3.html#expected-grad-log-prob-lemma)
  + [Don’t Let the Past Distract You](spinningup/rl_intro3.html#don-t-let-the-past-distract-you)
  + [Implementing Reward-to-Go Policy Gradient](spinningup/rl_intro3.html#implementing-reward-to-go-policy-gradient)
  + [Baselines in Policy Gradients](spinningup/rl_intro3.html#baselines-in-policy-gradients)
  + [Other Forms of the Policy Gradient](spinningup/rl_intro3.html#other-forms-of-the-policy-gradient)
  + [Recap](spinningup/rl_intro3.html#recap)

Resources

* [Spinning Up as a Deep RL Researcher](spinningup/spinningup.html)
  + [The Right Background](spinningup/spinningup.html#the-right-background)
  + [Learn by Doing](spinningup/spinningup.html#learn-by-doing)
  + [Developing a Research Project](spinningup/spinningup.html#developing-a-research-project)
  + [Doing Rigorous Research in RL](spinningup/spinningup.html#doing-rigorous-research-in-rl)
  + [Closing Thoughts](spinningup/spinningup.html#closing-thoughts)
  + [PS: Other Resources](spinningup/spinningup.html#ps-other-resources)
  + [References](spinningup/spinningup.html#references)
* [Key Papers in Deep RL](spinningup/keypapers.html)
  + [1. Model-Free RL](spinningup/keypapers.html#model-free-rl)
  + [2. Exploration](spinningup/keypapers.html#exploration)
  + [3. Transfer and Multitask RL](spinningup/keypapers.html#transfer-and-multitask-rl)
  + [4. Hierarchy](spinningup/keypapers.html#hierarchy)
  + [5. Memory](spinningup/keypapers.html#memory)
  + [6. Model-Based RL](spinningup/keypapers.html#model-based-rl)
  + [7. Meta-RL](spinningup/keypapers.html#meta-rl)
  + [8. Scaling RL](spinningup/keypapers.html#scaling-rl)
  + [9. RL in the Real World](spinningup/keypapers.html#rl-in-the-real-world)
  + [10. Safety](spinningup/keypapers.html#safety)
  + [11. Imitation Learning and Inverse Reinforcement Learning](spinningup/keypapers.html#imitation-learning-and-inverse-reinforcement-learning)
  + [12. Reproducibility, Analysis, and Critique](spinningup/keypapers.html#reproducibility-analysis-and-critique)
  + [13. Bonus: Classic Papers in RL Theory or Review](spinningup/keypapers.html#bonus-classic-papers-in-rl-theory-or-review)
* [Exercises](spinningup/exercises.html)
  + [Problem Set 1: Basics of Implementation](spinningup/exercises.html#problem-set-1-basics-of-implementation)
  + [Problem Set 2: Algorithm Failure Modes](spinningup/exercises.html#problem-set-2-algorithm-failure-modes)
  + [Challenges](spinningup/exercises.html#challenges)
* [Benchmarks for Spinning Up Implementations](spinningup/bench.html)
  + [Performance in Each Environment](spinningup/bench.html#performance-in-each-environment)
  + [Experiment Details](spinningup/bench.html#experiment-details)
  + [PyTorch vs Tensorflow](spinningup/bench.html#pytorch-vs-tensorflow)

Algorithms Docs

* [Vanilla Policy Gradient](algorithms/vpg.html)
  + [Background](algorithms/vpg.html#background)
  + [Documentation](algorithms/vpg.html#documentation)
  + [References](algorithms/vpg.html#references)
* [Trust Region Policy Optimization](algorithms/trpo.html)
  + [Background](algorithms/trpo.html#background)
  + [Documentation](algorithms/trpo.html#documentation)
  + [References](algorithms/trpo.html#references)
* [Proximal Policy Optimization](algorithms/ppo.html)
  + [Background](algorithms/ppo.html#background)
  + [Documentation](algorithms/ppo.html#documentation)
  + [References](algorithms/ppo.html#references)
* [Deep Deterministic Policy Gradient](algorithms/ddpg.html)
  + [Background](algorithms/ddpg.html#background)
  + [Documentation](algorithms/ddpg.html#documentation)
  + [References](algorithms/ddpg.html#references)
* [Twin Delayed DDPG](algorithms/td3.html)
  + [Background](algorithms/td3.html#background)
  + [Documentation](algorithms/td3.html#documentation)
  + [References](algorithms/td3.html#references)
* [Soft Actor-Critic](algorithms/sac.html)
  + [Background](algorithms/sac.html#background)
  + [Documentation](algorithms/sac.html#documentation)
  + [References](algorithms/sac.html#references)

Utilities Docs

* [Logger](utils/logger.html)
  + [Using a Logger](utils/logger.html#using-a-logger)
  + [Logger Classes](utils/logger.html#logger-classes)
  + [Loading Saved Models (PyTorch Only)](utils/logger.html#loading-saved-models-pytorch-only)
  + [Loading Saved Graphs (Tensorflow Only)](utils/logger.html#loading-saved-graphs-tensorflow-only)
* [Plotter](utils/plotter.html)
* [MPI Tools](utils/mpi.html)
  + [Core MPI Utilities](utils/mpi.html#module-spinup.utils.mpi_tools)
  + [MPI + PyTorch Utilities](utils/mpi.html#mpi-pytorch-utilities)
  + [MPI + Tensorflow Utilities](utils/mpi.html#mpi-tensorflow-utilities)
* [Run Utils](utils/run_utils.html)
  + [ExperimentGrid](utils/run_utils.html#experimentgrid)
  + [Calling Experiments](utils/run_utils.html#calling-experiments)

Etc.

* [Acknowledgements](etc/acknowledgements.html)
* [About the Author](etc/author.html)

# Indices and tables[¶](#indices-and-tables "Permalink to this headline")

* [Index](genindex.html)
* [Module Index](py-modindex.html)
* [Search Page](search.html)
