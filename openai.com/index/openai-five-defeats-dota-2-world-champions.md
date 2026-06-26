<!-- source: https://openai.com/index/openai-five-defeats-dota-2-world-champions/ -->

April 15, 2019

[Milestone](/research/index/milestone/)

# OpenAI Five defeats Dota 2 world champions

![OpenAI Five competitive event in a large, dim venue with bright spotlights and a large audience](https://images.ctfassets.net/kftzwdyauwt9/12b8cb5b-dbf2-4e54-54ed702c36f5/692053b6fc20292d8868af782748fa4a/openai-five-defeats-dota-2-world-champions.jpg?w=3840&q=90&fm=webp)

OpenAI Five is the first AI to beat the world champions in an esports game, having won two back-to-back games versus the world champion Dota 2 team, [OG⁠(opens in a new window)](https://twitter.com/OGesports), at [Finals⁠](/index/openai-five-finals/) this weekend. Both OpenAI Five and DeepMind’s AlphaStar had previously beaten good pros privately but lost their live pro matches, making this also the first time an AI has beaten esports pros on livestream.

![Side view of OpenAI Five Dota team posing behind a panel](https://images.ctfassets.net/kftzwdyauwt9/3d8ec82e-975a-45f0-6ac2e50e2ccb/8fd053ddbe944911f0e0a5af1418c971/openai-five-final-team.jpg?w=3840&q=90&fm=webp)

At OpenAI Five Finals, we also shared two surprises:

1. OpenAI Five discovered a rudimentary ability to be a teammate with humans, even though our training process focuses exclusively on beating other bots. The ease with which we turned a competitive AI into a cooperative one makes us hopeful that future AI systems can be very beneficial for humans given active development effort.
2. From April 18–21, we’re scaling up OpenAI Five to [play the Internet⁠(opens in a new window)](https://arena.openai.com/), whether as a competitor or teammate. This final test will let us answer an important research question—to what extent OpenAI Five is exploitable or can otherwise be reliably beaten—and be potentially the largest-ever deployment of a highly-competent deep reinforcement learning agent that people can knowingly interact with.

Loading...

* [Replays + OpenAI Five planning view(opens in a new window)](#replays)

## Why Dota?

We started OpenAI Five in order to work on a problem that felt outside of the reach of existing deep reinforcement learning[A](#citation-bottom-A) algorithms. We hoped that by working on a problem that was unsolvable by current methods, we’d need to make a big increase in the capability of our tools. We were expecting to need sophisticated algorithmic ideas, such as hierarchical reinforcement learning, but we were surprised by what we found: the fundamental improvement we needed for this problem was scale. Achieving and utilizing that scale wasn’t easy and was the bulk of our research effort!

Loading...

To build OpenAI Five, we created a system called [Rapid⁠](/index/openai-five/#rapid) which let us run [PPO⁠](/index/openai-baselines-ppo/) at previously [unprecedented scale⁠](/index/openai-five/#our-approach). The results exceeded our wildest expectations, and we produced a world-class Dota bot without hitting any fundamental performance limits.

The surprising power of today’s RL algorithms comes at the cost of massive amounts of experience, which can be impractical outside of a game or simulated environment. This limitation may not be as bad as sounds—for example, we used Rapid to control a [robotic hand⁠](/index/learning-dexterity/) to dexterously reorient a block, trained entirely in simulation and executed on a physical robot. But we think decreasing the amount of experience is a next challenge for RL.

We are retiring OpenAI Five as a competitor today, but progress made and technology developed will continue to drive our future work. This isn’t the end of our Dota work—we think that Dota is a much more intrinsically interesting and difficult (and now well-understood!) environment for RL development than the standard ones used today.

## Compute

OpenAI Five’s victories on Saturday, as compared to its losses at The International 2018, are due to a major change: 8x more training compute. In many previous phases of the project, we’d drive further progress by increasing our training scale. But after The International, we’d already dedicated the vast majority of our project’s compute to training a single OpenAI Five model. So we increased the scale of compute in the only way available to us: training for longer.

![Compute versus Ts Final Log Smoothed](https://images.ctfassets.net/kftzwdyauwt9/71cff7cb-6b5e-4e0a-5f01d6bcb242/5bf6ea70a7ba4bcc4a9d616b610b75bb/compute_vs_ts_final_log_smoothed.svg?w=3840&q=90)

In total, the current version of OpenAI Five has consumed 800 petaflop/s-days and experienced about 45,000 years of Dota self-play over 10 realtime months (up from about 10,000 years over 1.5 realtime months as of The International), for an average of 250 years of simulated experience per day. The Finals version of OpenAI Five has a 99.9% winrate versus the TI version.[B](#citation-bottom-B)

## Transfer learning

The current version of OpenAI Five has been training continuously since June 2018, despite changes to the [model size⁠(opens in a new window)](https://twitter.com/openai/status/1037765547427954688?lang=en) and the game rules (including some fairly large game patch updates and newly implemented features). In each case, we were able to transfer the model over and continue training—something that is an [open challenge⁠](/index/retro-contest-results/) for RL in other domains. To the best of our knowledge, this is the first time an RL agent has been trained using such a long-lived training run.

To make this work, we’ve continued to flesh out our [surgery⁠](/index/openai-five-benchmark-results/#training) tooling so that we can start from trained parameters even across substantial architecture changes.

## More heroes

We saw very little slowdown in training going from [5⁠](/index/openai-five/) to [18⁠](/index/openai-five-benchmark/) heroes. We hypothesized the same would be true going to even more heroes, and after The International, we put a lot of effort into integrating new ones.

We spent several weeks training with hero pools up to 25 heroes, bringing those heroes to approximately 5k MMR (about 95th percentile of Dota players). Although they were still improving, they weren’t learning fast enough to reach pro level before Finals. We haven’t yet had time to investigate why, but our hypotheses range from insufficient model capacity to needing better matchmaking for the expanded hero pool to requiring more training time for new heroes to catch up to old heroes. Imagine how hard it is for a human to learn a new hero when everyone else has mastered theirs!

We believe these issues are fundamentally solvable, and solving them could be interesting in its own right. The Finals version plays with 17 heroes—we removed Lich because his abilities were changed significantly in Dota version 7.20.

## Cooperative mode

> *It actually felt nice; my Viper gave his life for me at some point. He tried to help me, thinking “I’m sure she knows what she’s doing” and then obviously I didn’t. But, you know, he believed in me. I don’t get that a lot with [human] teammates. —*[*Sheever*⁠(opens in a new window)](https://twitter.com/SheeverGaming)

![Bracket of two competing Dota teams: Sheever and Blitz versus Capitalist and ODPixel](https://images.ctfassets.net/kftzwdyauwt9/32f43b65-0baf-4687-67df2e91aa48/1434a9432c18920dea93c9c0b0372de5/coop-versus.png?w=3840&q=90&fm=webp)

OpenAI Five’s ability to play with humans presents a compelling vision for the future of human-AI interaction, one where AI systems collaborate and enhance the human experience. Our testers reported feeling supported by their bot teammates, that they learned from playing alongside these advanced systems, and that it was generally a fun experience overall.

Loading...

Note that OpenAI Five exhibits zero-shot transfer learning—it was trained to have all heroes controlled by copies of itself, but generalizes to controlling a subset of heroes, playing with or against humans. We were very surprised this worked as well as it did. In fact, we’d considered doing a cooperative match at The International but assumed it’d require dedicated training.

## Arena

We’re launching OpenAI Five Arena, a public experiment where we’ll let anyone play OpenAI Five in both competitive and cooperative modes. We’d known that our 1v1 bot would be [exploitable⁠](/index/more-on-dota-2/#bot-exploits) through clever strategies; we don’t know to what extent the same is true of OpenAI Five, but we’re excited to invite the community to help us find out!

[**Arena**⁠(opens in a new window)](https://arena.openai.com/) **opens Thursday, April 18 at 6pm PST and will close 11:59pm PST on Sunday, April 21.** Please register so we can ensure there’s enough server capacity in your region! Results of all games will be automatically reported to the Arena public leaderboard.

![Five Arena matchup](https://images.ctfassets.net/kftzwdyauwt9/be9a0fb7-2371-409d-bf22fb6769ed/3cb6564cf0aeff0b817826ebdbcd822c/five-arena.png?w=3840&q=90&fm=webp)

We’re incredibly grateful for all the support the Dota community has shown us over the past two years, and we hope that Arena will also serve as one small way of giving back. Have fun with it!

## What’s next

We will be releasing a more technical analysis of OpenAI Five once we’ve reviewed the outcomes of OpenAI Five Arena.

Afterwards, we’ll continue working with the Dota 2 environment within OpenAI. We’ve seen rapid progress in the past two years on RL capabilities, and we think that Dota 2 will continue to help us push forward what’s possible—whether with achieving competent performance from less data or true human-AI cooperation.

If you are interested in advancing AI capabilities and helping further our mission of ensuring they benefit humanity, we’re [hiring⁠](/careers/)!

* [OpenAI Five](/research/index/?tags=openai-five)
* [Community & Collaboration](/research/index/?tags=community-collaboration)
* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Software & Engineering](/research/index/?tags=software-engineering)

## Footnotes

1. A

   Deep reinforcement learning is the idea of training a deep neural network to achieve goals using rewards and punishments
2. B

   Winrate evaluated on the current game patch. This biases the winrate towards the Finals version as the TI version was trained on an older patch, but currently we don’t have another way to compare agents trained on different game versions.

## Author

## Game Replays & Planning Views

OG Game 1: [Replay⁠(opens in a new window)](https://cdn.openai.com/how-to-train-your-openai-five/og_game_1_04132013569395266.dem), [OpenAI Five planning view⁠(opens in a new window)](https://cdn.openai.com/how-to-train-your-openai-five/game1_og_minimap.mov)OG Game 2: [Replay⁠(opens in a new window)](https://cdn.openai.com/how-to-train-your-openai-five/og_game2_04132030946085141.dem), [OpenAI Five planning view⁠(opens in a new window)](https://cdn.openai.com/how-to-train-your-openai-five/game2_og_minimap.mov)Coop Game: [Replay⁠(opens in a new window)](https://cdn.openai.com/how-to-train-your-openai-five/coop_game_04132076146922985.dem), [OpenAI Five planning view⁠(opens in a new window)](https://cdn.openai.com/how-to-train-your-openai-five/coop_minimap.mov)[Planning View Legend⁠(opens in a new window)](https://cdn.openai.com/how-to-train-your-openai-five/legend_planning_view.pdf)

## Related articles

![Scaling Laws For Reward Model Overoptimization](https://images.ctfassets.net/kftzwdyauwt9/a8801fe6-8892-472b-f746d1d9fb2d/547c46ed9a8a71e89efbb7a7963a8932/image-6.webp?w=3840&q=90&fm=webp)

[Scaling laws for reward model overoptimization

PublicationOct 19, 2022](/index/scaling-laws-for-reward-model-overoptimization/)

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTraining

ConclusionJun 23, 2022](/index/vpt/)

![Techniques For Training Large Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/62793de4-0f01-42fc-539325d9af36/bc1ac82499fc1dc43f59accdd31d0195/image-9.webp?w=3840&q=90&fm=webp)

[Techniques for training large neural networks

PublicationJun 9, 2022](/index/techniques-for-training-large-neural-networks/)
