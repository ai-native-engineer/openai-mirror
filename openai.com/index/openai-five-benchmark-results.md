<!-- source: https://openai.com/index/openai-five-benchmark-results/ -->

August 6, 2018

[Milestone](/research/index/milestone/)

# OpenAI Five Benchmark: Results

![Two people wearing headphones and sitting at a desk in front of monitors, playing a video game while a live audience watches](https://images.ctfassets.net/kftzwdyauwt9/e982d0ec-f741-4f17-7670a8d27e81/e2bf83e85cc7c231c2ffd465a02dbf97/openai-five-benchmark-results.jpg?w=3840&q=90&fm=webp)

Yesterday, [OpenAI Five⁠](/index/openai-five/) won a best-of-three against a team of 99.95th percentile Dota players: [Blitz⁠(opens in a new window)](https://liquipedia.net/dota2/Blitz), [Cap⁠(opens in a new window)](https://liquipedia.net/dota2/Capitalist), [Fogged⁠(opens in a new window)](https://liquipedia.net/dota2/Fogged), [Merlini⁠(opens in a new window)](https://liquipedia.net/dota2/Merlini), and [MoonMeander⁠(opens in a new window)](https://liquipedia.net/dota2/MoonMeander)—four of whom have played Dota professionally—in front of a live audience and 100,000 concurrent livestream viewers.

The human team won game three after the audience adversarially selected Five’s heroes. We also showed our preliminary work to introspect Five’s view of the game, including its probability of winning, which made predictions surprising to the human observers. These results show that Five is a step towards advanced AI systems which can handle the complexity and uncertainty of the [real world⁠](/index/learning-dexterity/).

*In case you missed it: the livestream from the Benchmark commentated by* [*Purge*⁠(opens in a new window)](https://twitter.com/PurgeGamers) *and* [*ODPixel*⁠(opens in a new window)](https://twitter.com/ODPixel)*.* [*Christy*⁠(opens in a new window)](https://twitter.com/cbd/status/1026182729291812864) *and* [*Greg*⁠(opens in a new window)](https://twitter.com/gdb/status/1026175234825547776) *also both livetweeted the event.*

Loading...

## Overview of the day

### Audience game

The day began with a team of volunteers from the audience bravely playing the first public match against OpenAI Five. Five won within the first 14 minutes (an evenly-matched game generally takes 45 minutes).

![Large, crowded venue with an audience facing a panel of people speaking](https://images.ctfassets.net/kftzwdyauwt9/a18db10a-5691-45fa-87759bfdeb6a/46490c22a29006afe32c805f703564c6/DSC_7309-2.jpg?w=3840&q=90&fm=webp)

![Row of people wearing headsets and playing Dota on computer monitors](https://images.ctfassets.net/kftzwdyauwt9/a18db10a-5691-45fa-c5a173648a97/b86ad4a5c00419b8b3b4dd94bb69778b/DSC_7344-1.jpg?w=3840&q=90&fm=webp)

### Games 1 and 2

![Person embracing his teammate](https://images.ctfassets.net/kftzwdyauwt9/3679ae4e-eb76-47ba-d4a03e0242c6/61fb74e41275e805cb9b52338ea19439/DSC_7477-1.jpg?w=3840&q=90&fm=webp)

We revealed a new OpenAI Five capability—the ability to [draft⁠(opens in a new window)](https://dota2.gamepedia.com/Game_modes#Captains_Mode). Drafting is considered an [extremely challenging⁠(opens in a new window)](https://www.reddit.com/r/DotA2/comments/6zmj06/guide_to_drafting_applied_to_ti7_grand_finals/) part of Dota, since heroes interact with each other in complex ways.

![OpenAI Five team probability estimate](https://images.ctfassets.net/kftzwdyauwt9/a8a26ad6-0073-4e0e-38c196ae5174/b12a0d343e9fe0f4f5652d97b1ed362a/game1-draft.png?w=3840&q=90&fm=webp)

In late June we added a win probability output to our neural network to introspect what OpenAI Five is predicting. When later considering drafting, we realized we could use this to evaluate the win probability of any draft: just look at the prediction on the first frame of a game with that lineup. In one week of implementation, we crafted a fake frame for each of the 11 million possible team matchups and wrote a tree search to find OpenAI Five’s optimal draft.

![Focus on a row of people looking upwards](https://images.ctfassets.net/kftzwdyauwt9/0586c226-1d38-4f1d-6328ac12e3a2/b2d7f04f727a246a9ef61b704acfdf33/DSC_7862-1.jpg?w=3840&q=90&fm=webp)

After the game 1 draft, OpenAI Five predicted a 95% win probability, even though the matchup seemed about even to the human observers. It won the first game in 21 minutes and 37 seconds. After the game 2 draft, OpenAI Five predicted a 76.2% win probability, and won the second in 24 minutes and 53 seconds.

### Game 3: audience draft

For the third game, we asked the audience to draft OpenAI Five’s heroes. As [expected⁠(opens in a new window)](https://twitter.com/gdb/status/1026235489425088513), they selected an adversarial lineup.

Loading...

Before the game began, OpenAI Five predicted a 2.9% chance of winning. Five played on despite the bad odds, and at one point made enough progress to predict a 17% win probability, before ultimately losing after 35 minutes and 47 seconds.

![People greeting each other behind a long desk with black monitors](https://images.ctfassets.net/kftzwdyauwt9/24586777-db05-47d0-c551e39eca1c/987a94b46e1f60bfe97a2c0f19756331/DSC_8547-1.jpg?w=3840&q=90&fm=webp)

## Training

Our usual development cycle is to train each major revision of the system from scratch. However, this version of OpenAI Five contains parameters that have been training since June 9th across six major system revisions. Each revision was initialized with parameters from the previous one.

We invested heavily in “surgery” tooling which allows us to map old parameters to a new network architecture. For example, when we first trained warding, we shared a single action head for determining where to move and where to place a ward. But Five would often drop wards seemingly in the direction it was trying to go, and we hypothesized it was allocating its capacity primarily to movement. Our tooling let us split the head into two clones initialized with the same parameters.

We estimate that we used the following amounts of [compute⁠](/index/ai-and-compute/) to train our various Dota systems:

* 1v1 model: 8 petaflop/s-days
* June 6th model: 11 petaflop/s-days[A](#citation-bottom-A)
* Aug 5th model: 35 petaflop/s-days[A](#citation-bottom-A)

We are also releasing our latest [network architecture⁠(opens in a new window)](https://cdn.openai.com/dota_benchmark_results/network_diagram_08_06_2018.pdf).

## Peaking at the model

We can get some insight into the model’s planning via an output which predicts where a hero will be in the future. In the following video, the highlighted boxes show the predicted location of Sven in 6 seconds:

We can also train outputs to predict various other quantities — last hits, tower counts, and the like:

Making our model function requires working through many bugs and unexpected behaviors. Here are some examples:

## What’s next

These results give us confidence in moving to the next phase of this project: playing a team of professionals at The International later this month. We will announce details of the games once they are confirmed—[follow us⁠(opens in a new window)](https://twitter.com/openai) on Twitter to stay up to date!

* [OpenAI Five](/research/index/?tags=openai-five)
* [Community & Collaboration](/research/index/?tags=community-collaboration)
* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Software & Engineering](/research/index/?tags=software-engineering)

## Footnotes

1. A

   We revised these numbers after a more rigorous analysis (4/14/19)

## Author

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
