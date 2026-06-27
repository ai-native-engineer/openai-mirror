---
title: "Ingredients for Robotics Research"
channel: openai
url: https://www.youtube.com/watch?v=8Np3eC_PTFo
youtube_id: 8Np3eC_PTFo
published: 2018-02-26
duration: "1:57"
captions: en
---

# Ingredients for Robotics Research

[![Ingredients for Robotics Research](https://img.youtube.com/vi/8Np3eC_PTFo/hqdefault.jpg)](https://www.youtube.com/watch?v=8Np3eC_PTFo)

<details>
<summary>자막: Ingredients for Robotics Research (1:57)</summary>

[00:00]
Today, we're releasing new Gym
environments and Baselines for
goal-based robotics tasks. The tasks
include a ShadowHand robot that
manipulates an object. The hand is
flexible enough to handle a number of
different items. We also added new
environments for the Fetch robot where
it learns to nudge a block, slide a puck,
as well as grasp a block and lift it up.
Along with the environments, we're also
updating Baselines, our library of
reinforcement learning code. One of the
algorithms we use to train agents on the
new tasks is Hindsight Experience
Replay, or HER for short. HER allows an
agent to learn from failures. For example,
here Fetch is trying to slide a puck

[00:01]
towards a goal. Unfortunately, in this
first attempt, we missed the goal. Usually
we would now just try again and hope for
a better result. However, while the puck
did not end up at the goal, it did land
somewhere else. With HER, instead of the
original goal, we pretend that we in fact
wanted to slide the puck to where it
landed. If our goal had been here, this
attempt would have been successful.
Over time, this helps us learn how to achieve
all possible goals.
The new environments are available in Gym today, and Hindsight Experience Replay is available in Baselines.

</details>
