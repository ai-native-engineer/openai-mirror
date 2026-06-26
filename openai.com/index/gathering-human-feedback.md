<!-- source: https://openai.com/index/gathering-human-feedback/ -->

August 3, 2017

[Release](/research/index/release/)

# Gathering human feedback

[View code(opens in a new window)](https://github.com/nottombrown/rl-teacher)

![Gathering Human Feedback](https://images.ctfassets.net/kftzwdyauwt9/c8f4669e-ce6a-4c29-83a8c68cbddd/78af9679b59629995232a07059a6d18e/image-66.webp?w=3840&q=90&fm=webp)

RL-Teacher is an open-source implementation of our interface to train AIs via occasional human feedback rather than hand-crafted reward functions. The underlying technique was developed as a step towards safe AI systems, but also applies to reinforcement learning problems with rewards that are hard to specify.

Loading...

The release contains three main components:

* A [reward predictor⁠(opens in a new window)](https://github.com/nottombrown/rl-teacher/blob/master/rl_teacher/teach.py) that can be plugged into any agent and learns to predict the actions the agent could take that a human would approve of.
* An [example agent⁠(opens in a new window)](https://github.com/nottombrown/rl-teacher/tree/master/agents) that learns via a function specified by a reward predictor. RL-Teacher ships with three pre-integrated algorithms, including [OpenAI Baselines PPO⁠(opens in a new window)](https://blog.openai.com/openai-baselines-ppo/).
* A [web-app⁠(opens in a new window)](https://github.com/nottombrown/rl-teacher/tree/master/human-feedback-api) that humans can use to give feedback, providing the data used to train the reward predictor.

The entire system consists of less than 1,000 lines of Python code (excluding the agents). After you’ve set up your web server you can launch an experiment by running:

#### Bash

```` ```
1

$ python rl_teacher/teach.py -p human --pretrain_labels 175 -e Reacher-v1 -n human-175
``` ````

Humans can give feedback via a simple web interface (shown above), which can be run locally (not recommended) or on a separate machine. Full documentation is available on the project’s [GitHub repository⁠(opens in a new window)](https://github.com/nottombrown/rl-teacher). We’re excited to see what AI researchers and engineers do with this technology—please [get in touch⁠](mailto:jack@openai.com?Subject=RL_Teacher) with any experimental results!

* [Community & Collaboration](/research/index/?tags=community-collaboration)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Tom Brown, Dario Amodei, Paul Christiano

## Related articles

![Scaling Laws For Reward Model Overoptimization](https://images.ctfassets.net/kftzwdyauwt9/a8801fe6-8892-472b-f746d1d9fb2d/547c46ed9a8a71e89efbb7a7963a8932/image-6.webp?w=3840&q=90&fm=webp)

[Scaling laws for reward model overoptimization

PublicationOct 19, 2022](/index/scaling-laws-for-reward-model-overoptimization/)

![Whisper](https://images.ctfassets.net/kftzwdyauwt9/13c810cb-0592-442d-190ab7378bef/a7cb2299d034abe93023f662f8d32263/Speech_Rec_16_9.png?w=3840&q=90&fm=webp)

[Introducing Whisper

ReleaseSep 21, 2022](/index/whisper/)

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTraining

ConclusionJun 23, 2022](/index/vpt/)
