---
title: "Learning Dexterity"
channel: openai
url: https://www.youtube.com/watch?v=jwSbzNHGflM
youtube_id: jwSbzNHGflM
published: 2018-07-30
duration: "3:29"
captions: en
---

# Learning Dexterity

[![Learning Dexterity](https://img.youtube.com/vi/jwSbzNHGflM/hqdefault.jpg)](https://www.youtube.com/watch?v=jwSbzNHGflM)

<details>
<summary>자막: Learning Dexterity (3:29)</summary>

[00:00]
We're working on teaching robots to solve a wide variety of tasks without having to program them for any one specific task.
Here a robot has learned to rotate a block into any orientation we'd like.
Once it succeeds at that we give it a new goal and so on.
The system runs on a human-like robot hand and we use reinforcement learning and
simulation to teach the robot how to solve tasks in the real world.

[00:01]
To learn how to solve a task like this,
we show it many different variations of the world where the rules are slightly different every time.
This is a technique called domain randomization and it affects for example the color of the cube and of the background.
However, we take this technique beyond just how the environment looks.
We also randomize aspects like how fast the hand can move, how heavy the block is, and the friction between the block and the hand.
Our learning algorithm sees all of these different worlds and this lets it learn a way of manipulating the block that is very robust.
Robust enough so that eventually we can accomplish the same task in the real world.
To simulate all of these possible variants of the environment,
we've built a system that runs the training processes in the cloud on thousands of machines.
It's called Rapid and we've used the same system before to solve complex video games.
First rollout workers collect experience from many different variations of the environment.
They send this experience data to the optimizer which uses it to improve the parameters of the model controlling the robot.
Finally updated parameters make their way back to the rollout workers to complete the cycle.

[00:02]
One thing that's very interesting to us is how general the system is.
Not only can it rotate blocks but it can perform tasks with other shapes as well.
If you wanted to write a controller for this task the old-fashioned way
you'd sit down and write out exactly if I'm in this position move this finger in this direction.
If I'm in this other position move here and so on. It's very meticulous.
Instead our system can learn to manipulate objects of all kinds of shapes without any additional human help.
We hope that with this approach we can solve more and more complex tasks in the future so that we can go even further
beyond what today's hand-programmed robots can do.

</details>
