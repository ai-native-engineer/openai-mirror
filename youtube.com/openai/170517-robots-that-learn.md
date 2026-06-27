---
title: "Robots that Learn"
channel: openai
url: https://www.youtube.com/watch?v=0iYxqo1_nJA
youtube_id: 0iYxqo1_nJA
published: 2017-05-17
duration: "2:52"
captions: en
---

# Robots that Learn

[![Robots that Learn](https://img.youtube.com/vi/0iYxqo1_nJA/hqdefault.jpg)](https://www.youtube.com/watch?v=0iYxqo1_nJA)

<details>
<summary>자막: Robots that Learn (2:52)</summary>

[00:00]
Infants are born with the ability to imitate
what other people do.
Here, a ten-minute-old newborn sees another
person stick their tongue out for the first
time.
In response, he sticks his own tongue out.
Imitation allows humans to learn new behaviors
rapidly.
We would like our robots to be able to learn
this way, too.
We’ve built a proof of concept system, trained
entirely in simulation: we teach the robot
a new task by demonstrating how to assemble
block towers in a way we desire — in this
case a single stack of six virtual blocks
to form a tower.
Previously, the robot has seen other examples
of manipulating blocks, but not this particular
one.
Our robot has now learned the task, even though
its movements have to be different from the
ones in the demonstration.

[00:01]
With a single demonstration of the task, we
can replicate it in a number of initial conditions.
Teaching the robot how to build a different
block arrangement requires only a single new
demonstration.
Here’s how our system works: the robot perceives
the environment with its camera, and manipulates
the blocks with its arm.
At its core, there are two neural networks,
working together.
The camera image is first processed by the
vision network.
Then, based on the recorded demonstration,
the imitation network figures out what action
to take next.
Our vision network is a deep neural net that
takes a camera image and determines the position
of the blocks relative to the robot.
To train the network, we use only simulated
data, using domain randomization to learn
a robust vision model.
We generate thousands of different object
locations, light settings and surface textures,

[00:02]
and show these examples to the network.
After training, the network can find the blocks
in the physical world, even though it has
never seen images from a real camera before.
Now that we know the location of the blocks,
the imitation network takes over.
Its goal is to mimic the task shown by the
demonstrator.
This neural net is trained to predict what
action the demonstrator would have taken in
the same situation.
On its own, it has learned to scan through
the demonstration and pay attention to the
relevant frames that tell it what to do next.
Nothing in our technique is specific to blocks.
This system is an early prototype, and will
form the backbone of the general-purpose robotic
systems we’re developing at OpenAI.

</details>
