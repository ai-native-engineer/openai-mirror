<!-- source: https://openai.com/index/retro-contest-results/ -->

June 22, 2018

[Conclusion](/research/index/conclusion/)

# Retro Contest: Results

The first run of our Retro Contest—exploring the development of algorithms that can generalize from previous experience—is now complete.

![A screenshot of the Sonic the Hedgehog video game interface](https://images.ctfassets.net/kftzwdyauwt9/ca9bbff7-d22d-4d9c-5e73e4e6168e/7817018b3e1dd3961c132da96874c996/image-47.webp?w=3840&q=90&fm=webp)

Though many approaches were tried, top results all came from tuning or extending existing algorithms such as PPO and Rainbow. There’s a long way to go: top performance was 4,692 after training while the theoretical max is 10,000. These results provide validation that our Sonic benchmark is a good problem for the community to double down on: the winning solutions are general machine learning approaches rather than competition-specific hacks, suggesting that one can’t cheat through this problem.

![Screenshot of a Sonic the Hedgehog video game.](https://images.ctfassets.net/kftzwdyauwt9/1gGJCzTHFTNJn6m4GkROAB/6cb51a280c362510874d3ee15f5da6e8/retro-contest-results.jpg?w=3840&q=90&fm=webp)

Loading...

Over the two-month contest, 923 teams registered and 229 submitted solutions to the leaderboard. Our automated evaluation systems conducted a total of 4,448 evaluations of submitted algorithms, corresponding to about 20 submissions per team. The contestants got to see their scores rise on the leaderboard, which was based on a test set of five low-quality levels that we created using a level editor. You can watch the agents play one of these levels by clicking on the [leaderboard entries⁠(opens in a new window)](https://contest.openai.com/leaderboard).

![Graph of leaderboard score over days](https://images.ctfassets.net/kftzwdyauwt9/7cb88e3c-ffaf-4888-a6021c37642b/005c2837f056331f450c30f80ff740e9/leaderboard2x-1.png?w=3840&q=90&fm=webp)

Because contestants got feedback about their submission in the form of a score and a video of the agent being tested on a level, they could easily overfit to the leaderboard test set. Therefore, we used a completely different test set for the final evaluation. Once submissions closed, we took the latest submission from the top 10 entrants and tested their agents against 11 custom Sonic levels made by skilled level designers. To reduce noise, we evaluated each contestant on each level three times, using different random seeds for the environment. The ranking changed in this final evaluation, but not to a large extent.

Loading...

## Top scores

The top 5 scoring teams are:

|  |  |  |
| --- | --- | --- |
| **Rank** | **Team** | **Score** |
| #1 | Dharmaraja | 4692 |
| #2 | mistake | 4446 |
| #3 | aborg | 4430 |
| #4 | whatever | 4274 |
| #5 | Students of Plato | 4269 |
|  | Joint PPO baseline | 4070 |
|  | Joint Rainbow baseline | 3843 |
|  | Rainbow baseline | 3498 |

**Dharmaraja** topped the scoreboard during the contest, and the lead remained on the final evaluation; **mistake** narrowly won out over **aborg** for second place. The top three teams will receive trophies.

![Trophies Three 2000](https://images.ctfassets.net/kftzwdyauwt9/3e817173-e32d-40e7-3e6e02e92e0c/012dd210dfa4943ab8d3456fbea1140e/trophies-three-edited-2000.jpg?w=3840&q=90&fm=webp)

Learning curves of the top three teams for all 11 levels are as follows (showing the standard error computed from three runs).

![Learning Curves Averaged Over 3 Trials](https://images.ctfassets.net/kftzwdyauwt9/914d05b9-eb6b-4163-49fd71807d3b/7c5eabf1a0d5961be67f0e8ee4c4ba69/learning-curves-averaged-over-3-trials2x.png?w=3840&q=90&fm=webp)

Averaging over all levels, we can see the following learning curves.

![Learning Curves Averaged Over 11 Levels And 3 Trials](https://images.ctfassets.net/kftzwdyauwt9/4a4de36c-528c-44e0-d7e20aefe454/fd06ca77faea8b60cb65c76b451f1e0f/learning-curves-averaged-over-11-levels-and-3-trials2x.png?w=3840&q=90&fm=webp)

Note that **Dharmaraja** and **aborg** start at similar scores, whereas **mistake** starts much lower. As we will describe in more detail below, these two teams fine-tuned (using PPO) from a pre-trained network, whereas **mistake** trained from scratch (using Rainbow DQN). **mistake**’s learning curves end early because they timed out at 12 hours.

## Meet the winners

Loading...

### Dharmaraja

Dharmaraja is a six-member team including Qing Da, Jing-Cheng Shi, Anxiang Zeng, Guangda Huzhang, Run-Ze Li, and Yang Yu. [Qing Da⁠(opens in a new window)](http://www.daqings.net/) and Anxiang Zeng are from the AI team within the search department of Alibaba in Hangzhou, China. In recent years, they have studied how to apply reinforcement learning to real world problems, especially in an e-commerce setting, together with [Yang Yu⁠(opens in a new window)](http://lamda.nju.edu.cn/yuy), who is an Associate Professor of the Department of Computer Science at Nanjing University, Nanjing, China.

Dharmaraja’s solution is a variant of joint PPO (described in our [tech report⁠(opens in a new window)](https://arxiv.org/abs/1804.03720)) with a few improvements. First, it uses RGB images rather than grayscale; second, it uses a slightly augmented action space, with more common button combinations; third, it uses an augmented reward function, which rewards the agent for visiting new states (as judged by a perceptual hash of the screen). In addition to these modifications, the team also tried a number of things that didn’t pan out: [DeepMimic⁠(opens in a new window)](https://arxiv.org/abs/1804.02717), object detection through [YOLO⁠(opens in a new window)](https://arxiv.org/abs/1506.02640), and some Sonic-specific ideas.

* [Get the source code(opens in a new window)](https://github.com/eyounx/RetroCodes)

Loading...

### Mistake

Team mistake consists of Peng Xu and Qiaoling Zhong. Both are second-year graduate students in Beijing, China, studying at the CAS Key Laboratory of Network Data Science and the Technology Institute of Computing Technology, Chinese Academy of Sciences. In their spare time, Peng Xu enjoys playing basketball, and Qiaoling Zhong likes to play badminton. Their favorite video games are Contra and Mario.

Mistake’s solution is based on the Rainbow baseline. They made several modifications that helped boost performance: a better value of n for n-step Q learning; an extra CNN layer added to the model, which made training slower but better; and a lower DQN target update interval. Additionally, the team tried joint training with Rainbow, but found that it actually hurt performance in their case.

* [Get the source code(opens in a new window)](https://github.com/xupe/mistake-in-retro-contest-of-OpenAI)

Loading...

### Aborg

Team Aborg is a solo effort from Alexandre Borghi. After completing a PhD in computer science in 2011, Alexandre worked for different companies in France before moving to the United Kingdom where he is a research engineer in deep learning. As both a video game and machine learning enthusiast, he spends most of his free time studying deep reinforcement learning, which led him to take part in the OpenAI Retro Contest.

Aborg’s solution, like Dharmaraja’s, is a variant of joint PPO with many improvements: more training levels from the Game Boy Advance and Master System Sonic games; a different network architecture; and fine-tuning hyper-parameters that were designed specifically for fast learning. Elaborating on the last point, Alexandre noticed that the first 150K timesteps of fine-tuning were unstable (i.e. the performance sometimes got worse), so he tuned the learning rate to fix this problem. In addition to the above changes, Alexandre tried several solutions that did not work: different optimizers, [MobileNetV2⁠(opens in a new window)](https://arxiv.org/abs/1801.04381), using color images, etc.

* [Get the source code(opens in a new window)](https://github.com/aborghi/retro_contest_agent)

## Best write-ups

The Best Write-up Prize is awarded to contestants that produced high-quality essays describing the approaches they tried.

Loading...

Now, let’s meet the winners of this prize category.

Loading...

### Dylan Djian

Dylan currently lives in Paris, France. He is a student in software development at [school 42 in Paris⁠(opens in a new window)](https://en.wikipedia.org/wiki/42_(school)). He got into machine learning after watching [a video⁠(opens in a new window)](https://www.youtube.com/watch?v=qv6UVOQ0F44) of a genetic algorithm learning how to play Mario a year and a half ago. This video sparked his interest and made him want to learn more about the field. His favorite video games are Zelda Twilight Princess and World of Warcraft.

<!-- yt-inline:qv6UVOQ0F44 -->
[![MarI/O - Machine Learning for Video Games](https://img.youtube.com/vi/qv6UVOQ0F44/hqdefault.jpg)](https://www.youtube.com/watch?v=qv6UVOQ0F44)

<details>
<summary>자막: MarI/O - Machine Learning for Video Games (5:57)</summary>

[00:00]
Welcome back. Seeing here. You're
watching a skilled player play Super
Mario World. But this player is not
human. It's a computer program I wrote
called Mario. This program started out
knowing absolutely nothing about Super
Mario World or Super Nintendo's. In
fact, it didn't even know that pressing
right on the controller would make the
player go towards the end of the level.
It learned all of these things through a
process called
neuroeolution. In this video, I want to
teach you about how Mario learned to
beat this level. Donut Plains 1. what
his brain looks like and how it's all
based on actual biological evolution.
So, let's start out by actually looking
at Mario's brain. Let's play it again,
but this time we'll look at Mario's
brain as it's making the decisions of
what buttons to press. It's going to
look a bit complicated at first, but
don't worry, I'll help break it down for
you. This structure of colored lines and
blinking boxes is called a neural
network. It's a simple mathematical
model for how a brain works, but it can
produce some very complicated behavior.
With enough computational power, a
neural network could come close to

[00:01]
simulating a real human brain, but
modern technology isn't there yet. On
the left side, you have the inputs. This
is what Mario sees. It's a simplified
view of the level. The white squares
stand for blocks the player can stand
on, and the black squares stand for
moving objects like enemies or
mushrooms. On the right side, you have
the outputs. These are the eight buttons
that Mario is able to press by using its
neural network. In between the inputs
and the outputs, all those lines and
boxes, those are the neural network.
Each free floating box is called a
neuron. And the lines connecting those
boxes are like the axons and dendrites
in a human brain. At any given time,
only some of these neurons and
connections are actually being used. And
this is what people talk about when they
say you only use 10% of your brain. The
neural network you're seeing is a pretty
complicated one. And it got so
complicated as a result of a 24-hour
evolutionary learning session. So to
explain how neural networks work, let's
rewind about 24 hours and look at how
the whole process started. This is what

[00:02]
Mario looked like at the beginning of
its training session all the way back in
generation number zero. The program is
probably even dumber than you thought at
this point. Often it just stands there
and doesn't even press any buttons. If
Mario stands still for too long, it'll
cut off the simulation and try the next
neural network. So, it's mostly just
jumping from one simulation to the next,
but occasionally the neural network says
to press the right button, and the
player starts walking right. Behavior
isn't complicated, but it's enough to
make at least some progress in the
level. Let's take a look at a sample
neural network to understand just how
that works. This is one of the randomly
generated neural networks that appeared
in the first generation of the
simulation. There are some green lines
and a red line and one neuron in the
middle. Here's how it works. A green
line is a positive connection and a red
line is a negative connection. A green
line reading from a black or white
square will turn its output the same
color. A red line reading from a black
or white square will turn its output the
opposite color. In this case, the green
lines read from the platform that the

[00:03]
player is standing on and make the
neural network press the right button as
long as the player is standing on it.
However, when the red line reads a black
square representing one of those caped
Koopas, it presses the A button and
makes the player jump. This this puts
the player in a position where the green
lines are no longer reading a white
square. So the right button turns off
and Mario just stands there. This is a
really basic example that illustrates
how a more complicated neural network
might operate. The more lines and
neurons you have, the more nuanced to
the decisions can be. So how exactly do
we get those more complicated neural
networks? The answer is evolution. When
Mario gets further right on the screen,
its fitness goes up. In this case,
fitness is a function of how far right
it gets and how quickly it gets there.
Only the neural networks that produce
the highest fitness are selected to be
bred, creating the next generation. It
took 34 generations of genetic breeding
and fitness evaluation before Mario was
able to finish the level without dying
and get a fitness score above 4,000. You

[00:04]
can see there were several places it got
stuck for a few generations, but it
always evolved out of those ruts. Let's
take a look at a few of those ruts. You
can look at the top left corner of the
screen to see what generation number
each rut occurred on. This process of
picking the fittest individuals from
each generation, breeding them together,
and adding random mutations very closely
matches the actual process of biological
evolution that took single-sellled
organisms and produced intelligent
humans. That's the power of
neuroeolution.
And though we don't yet have enough
computational resources to produce
something on the level of a human brain
this way, it's kind of neat to see what
it can do on one of my favorite
games. I didn't come up with this idea
on my own. This algorithm is called NEAT
which stands for neuroeolution of
augmenting topologies and it's based on
a paper by Kenneth Stanley and Risto
Miku Linen. It's a really great paper
that describes how to use genetic
algorithms to build up neural networks
from barebones without presupposing the

[00:05]
best structure for the neurons and their
connections. It also includes some
really cool ideas for separating genomes
into species, which a lot of genetic
algorithms don't really try and do. I
wrote Mario from scratch in Lua as a
plug-in for an emulator called Bisok. As
I close out the video, let's take a look
at the fittest neural network in each
generation. It's kind of cool how
sometimes you can see them make
modifications to each other and improve
performance, but sometimes an entirely
new species becomes prominent and
dominates the others. If you'd like to
do more reading about the concepts I
talked about in this video, I provided
some links in the video description. I
had a lot of fun working on this project
and I learned a ton. Hopefully, you
learned something, too. That's about it.
Thanks for watching.
[Music]

</details>


Loading...

### Oleg Mürk

[Oleg Mürk⁠(opens in a new window)](https://www.linkedin.com/in/oleg-m%C3%BCrk-5634b71/) hails from the San Francisco Bay Area, but is originally from Tartu, Estonia. During the day, he works with distributed data processing systems as a Chief Architect at Planet OS. In his free time, he burns “too much money” on renting GPUs for running deep learning experiments in TensorFlow. Oleg likes traveling, hiking, and kite-surfing and intends to finally learn to surf over the next 30 years. His favorite computer game (also the only one he has completed) is Wolfenstein 3D. His masterplan is to develop an automated programmer over the next 20 years and then retire.

Loading...

### Felix Yu

Felix is an entrepreneur who lives in Hong Kong. His first exposure to machine learning was a school project where he applied PCA to analyse stock data. After several years pursuing entrpreneurship, he got into ML in late 2015; he has become an [active Kaggler⁠(opens in a new window)](https://www.kaggle.com/renman) and has worked on several [side projects⁠(opens in a new window)](https://flyyufelix.github.io/) on computer vision and reinforcement learning.

## Best Supporting Material

One of the best things that came from this contest was seeing contestants helping each other out. Lots of people contributed guides for getting started, useful scripts, and troubleshooting support for other contestants.

Loading...

### Tristan Sokol

The winner of our Best Supporting Material award is [Tristan Sokol⁠(opens in a new window)](https://tristansokol.com/), who wrote [many⁠(opens in a new window)](https://medium.com/@tristansokol/discovering-q-learning-f7780a77b927) [helpful⁠(opens in a new window)](https://medium.com/@tristansokol/a-deep-dive-into-the-jerk-agent-3c553dbab442) [blog⁠(opens in a new window)](https://medium.com/@tristansokol/day-one-of-the-openai-retro-contest-1651ddcd6aa5) [posts⁠(opens in a new window)](https://medium.com/@tristansokol/openai-retro-contest-day-3-7a75289a1c9c) throughout the contest and [made a tool⁠(opens in a new window)](https://medium.com/@tristansokol/making-fun-visuals-history-maps-and-other-tool-improvements-eb5ffe187fd3) for visualizing trajectories through Sonic levels.

During the day, Tristan works for Square, helping to build their developer platform; at night, he is a designer and entrepreneur. This was the first time that he has done any AI/ML, and also his first time using Python for any real use case. Looking forward, Tristan is going to try to make cool things with TensorFlow.js. Whenever he isn’t in front of a computer, Tristan is probably in his Oakland backyard watching plants grow.

## Lessons and next steps

Contests have the potential to overhaul the prevailing consensus on what works the best, since contestants will try a diverse set of different approaches and the best one will win. In this particular contest, the top performing approaches were not radically different from the ones that we at OpenAI had found to be successful prior to the contest.

We were glad to see several of the top solutions making use of transfer learning; fine-tuning from the training levels. However, we were surprised to find that some of the top submissions were simply tuned versions of our baseline algorithms. This emphasizes the importance of hyper-parameters, especially in RL algorithms such as Rainbow DQN.

We plan to start another rendition of the contest in a few months. We hope and expect that some of the more off-beat approaches will be successful in this second round, now that people know what to expect and have begun to think deeply about the problems of fast learning and generalization in reinforcement learning. We’ll see you then, and we look forward to watching your innovative solutions climb up the scoreboard.

*Gotta Learn Fast*

* [Community & Collaboration](/research/index/?tags=community-collaboration)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Simulated Environments](/research/index/?tags=simulated-environments)

## Authors

John Schulman, Vicki Pfau, Alex Nichol, Christopher Hesse, Oleg Klimov, Larissa Schiavo

## Acknowledgments

Thanks to Kevin Wong and Cathy Trang for creating the final evaluation levels.

## Related articles

![Frontier Risk And Preparedness](https://images.ctfassets.net/kftzwdyauwt9/1f19f98e-798a-4d80-4549e8118ac0/c97816f694a725a9f292f53f1dc5f44f/frontier-risk-and-preparedness.png?w=3840&q=90&fm=webp)

[Frontier risk and preparedness

SafetyOct 26, 2023](/index/frontier-risk-and-preparedness/)

![Red Teaming Network](https://images.ctfassets.net/kftzwdyauwt9/71c1edf1-06f2-415c-b0a2fbe1cfe0/0ff4554769ae7609f53c44a160e351fe/red-teaming-network.png?w=3840&q=90&fm=webp)

[OpenAI Red Teaming Network

SafetySep 19, 2023](/index/red-teaming-network/)

![Confidence-Building Measures for Artificial Intelligence Workshop proceedings](https://images.ctfassets.net/kftzwdyauwt9/Z9HqTzpgkOEFSdz1i0Mkl/4a794853a9d3412851d52a0e18d407f3/Confidence-Building_Measures_for_Artificial_Intelligence__Workshop_proceedings.png?w=3840&q=90&fm=webp)

[Confidence-Building Measures for Artificial Intelligence: Workshop proceedings

ConclusionAug 1, 2023](/index/confidence-building-measures-for-artificial-intelligence/)
