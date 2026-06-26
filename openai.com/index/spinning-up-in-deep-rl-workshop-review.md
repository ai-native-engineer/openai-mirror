<!-- source: https://openai.com/index/spinning-up-in-deep-rl-workshop-review/ -->

February 26, 2019

[Company](/news/company-announcements/)

# Spinning Up in Deep RL: Workshop review

On February 2, we held our first Spinning Up Workshop as part of our new education initiative at OpenAI.

![Spinning Up In Deep RL](https://images.ctfassets.net/kftzwdyauwt9/dab77530-ade6-404d-ff79cfb1080e/a51cfad289cceb4266051c4869b8523b/SpinningUpinDeepRL.jpg?w=3840&q=90&fm=webp)

We hosted ~90 people at our office and engaged nearly 300 more through our livestream. Participants came from a wide range of backgrounds, including academia, software engineering, data science, ML engineering, medicine, and education. This workshop built off our [Spinning Up in Deep RL⁠](/index/spinning-up-in-deep-rl/) resource package and took a deeper dive into RL algorithm design, robotics, and building safe AI systems.

![Person speaking into a microphone in front of a room with a live audience](https://images.ctfassets.net/kftzwdyauwt9/667f1ffa-0562-417c-ae7321e61e95/953ce3eac4275fe9e8d244748b9c82be/NM3A2096.jpg?w=3840&q=90&fm=webp)

## Building educational tools

One of the goals for education at OpenAI is to help people develop the skills needed to participate in research and development in AI—especially in deep RL, a core area of research at OpenAI. From our experience working with [Scholars⁠(opens in a new window)](https://blog.openai.com/openai-scholars-2018-final-projects/) and [Fellows⁠(opens in a new window)](https://blog.openai.com/openai-summer-fellows-2018/), we’ve found that the key ingredients for skill development are:

1. a flexible curriculum that includes core material and a review of research frontiers,
2. mentorship and discussions with experts, and
3. having the students work on projects that are at the right level to help them grow.

The challenge for education at OpenAI is to figure out how to deliver these at scale. While sharing a curriculum at scale is relatively easy, it isn’t obvious how to scale up mentorship and guidance on projects. Our working theory is that workshops might help us do just that. Our first Spinning Up workshop has given us several positive signs that this is a useful direction, and we’re excited to share what we learned.

## The crowd

![A large audience listening intently while looking ahead](https://images.ctfassets.net/kftzwdyauwt9/b3daa128-12c8-4c36-2f04caa4f9a8/d8a88cccc0219a73c90baa9f8c2207bd/NM3A2136.jpg?w=3840&q=90&fm=webp)

We hosted around 90 people at our office and involved nearly 300 more through our livestream. Our guests came from a wide range of backgrounds, including academic research, software engineering, data science, ML engineering, medicine, and education. The level of ML experience varied quite significantly across the group, from “almost none” to “built their own Dota bot!”

More than 500 people, from all around the world, applied to participate in this workshop. Although we sadly couldn’t invite everyone to this one because of space constraints, we want to continue engaging the community with future events.

## The talks

The workshop kicked off with three hours of talks. To start us off, [Joshua Achiam⁠(opens in a new window)](https://twitter.com/jachiam0) laid out the conceptual foundations of reinforcement learning and gave an overview of different kinds of RL algorithms. If you’d like to study this material, check out [Spinning Up in Deep RL⁠(opens in a new window)](https://blog.openai.com/spinning-up-in-deep-rl/).

Matthias Plappert presented on OpenAI’s [recent⁠(opens in a new window)](https://blog.openai.com/learning-dexterity/) [work⁠(opens in a new window)](https://arxiv.org/abs/1808.00177) training a dexterous robot hand in simulation to manipulate objects in the real world. Domain randomization, recurrent neural networks, and large-scale distributed training were necessary ingredients in bridging the “sim2real” gap for this task.

Dario Amodei, the leader of the Safety Team at OpenAI, presented an overview of problems in AI safety and [recent⁠(opens in a new window)](https://blog.openai.com/amplifying-ai-training/) [work⁠(opens in a new window)](https://blog.openai.com/debate/) in this space. He described the central safety problem: the fact that correctly specifying agent behavior is hard! It is easy to inadvertently give agents incentives to perform different behavior than what you would have wanted, and when agents are very powerful, this could be dangerous. Dario also described [work⁠(opens in a new window)](https://blog.openai.com/deep-reinforcement-learning-from-human-preferences/) that OpenAI and collaborators at DeepMind have done to address this issue, in which reward functions are learned from human preferences instead of designed.

## The afternoon

The workshop continued into the afternoon with a semi-structured program of hacking and breakout sessions. Participants were able to seek guidance on project ideas and research tips from our slate of volunteers, which included [Amanda Askell⁠(opens in a new window)](https://twitter.com/AmandaAskell), [Alex Ray⁠(opens in a new window)](https://twitter.com/machinaut), [Daniel Ziegler⁠(opens in a new window)](https://www.linkedin.com/in/daniel-ziegler-b4b61882), [Dylan Hadfield-Menell⁠(opens in a new window)](https://twitter.com/dhadfieldmenell), [Ethan Knight⁠(opens in a new window)](https://github.com/hyperdo?tab=repositories), [Karl Cobbe⁠(opens in a new window)](https://twitter.com/karlcobbe), [Matthias Plappert⁠(opens in a new window)](https://twitter.com/mplappert), and [Sam McCandlish⁠(opens in a new window)](https://www.linkedin.com/in/sam-mccandlish).

![A group of presenters standing in front of.a projection, facing a live audience](https://images.ctfassets.net/kftzwdyauwt9/42201a70-ed30-468d-7dec5192de99/19503399bf065d369cc24c21e9ed5a00/NM3A2433.jpg?w=3840&q=90&fm=webp)

The breakout sessions turned out to be the main highlight of the afternoon. Whereas the morning talks covered the conceptual foundations of RL, the breakout sessions were designed to help participants boost their implementation and research skills.

![Group of people sitting together around a table, focused on their laptops](https://images.ctfassets.net/kftzwdyauwt9/f305b860-c12c-4596-79ffa62c24f4/86a8fa49da184d83c9d8cdeb2db483b3/NM3A2539.jpg?w=3840&q=90&fm=webp)

In the first session, Karl Cobbe gave an introduction to [TensorFlow⁠(opens in a new window)](https://www.tensorflow.org/), a key library used in deep learning research. In the second session, “Writing DQN Together,” Daniel Ziegler led participants step-by-step through the process of implementing a deep RL algorithm. In the third session, “Advanced RL Q&A,” Joshua Achiam described recent research frontiers in RL and took audience questions about doing RL research.

![People sitting around large tables, working on their laptops, and talking in a crowded room.](https://images.ctfassets.net/kftzwdyauwt9/c33a8111-947d-4aef-7e9b2fa17e02/29ac3feee6a33d04e356a2b414743c68/NM3A2537.jpg?w=3840&q=90&fm=webp)

## Our takeaways

This was our first experiment with the workshop format, and we were generally pleased with the outcome. In particular, we found it quite gratifying to work directly with such a capable and enthusiastic group of participants. The experience, along with feedback from the group, gave us a good sense of what to keep and what to change for future workshops.

**What worked**: We asked our participants what their highlights were, and these responses are a fairly representative sample:

> “Learning A TON in a very safe, friendly environment where everyone was mainly on the same level in terms of learning.”

> “I thought the ability to get one-on-one help and to take on some ‘paired programming’-like time with folks who really know what they’re doing was incredibly helpful. The enthusiasm of the volunteers was also very high, and I felt very encouraged to ask for help.”

Responses like these gave us a sense that the workshop format shined on delivering “mentorship and discussions with experts.”

![Two people working together on their laptops](https://images.ctfassets.net/kftzwdyauwt9/d1e6d4bd-0d83-4dfd-94f2f43bd47b/a7b99368f9caa0dac15c948996383611/NM3A2532.jpg?w=3840&q=90&fm=webp)

**What could be improved**: We asked our participants what they thought we could have done differently to enhance their experience, and received responses like:

> “I would’ve liked a presentation section of potential projects that we could pursue based on our experience level.”

> “Extend the workshop to two days.”

Many participants felt like they either weren’t sure what to work on during the hackathon, or didn’t have enough time to make significant progress on their hacking project.

We think this kind of feedback is a good indicator that the 1-day workshop format isn’t enough to “have the students work on projects that are at the right level to help them grow” in RL. In the future, we’ll consider running longer events so we can meet that goal. This feedback also suggests that we should do more to create “shovel-ready” RL projects that participants can jump right in to.

![Side profile of a person sitting with earbuds in their ears, looking intently at a laptop screen of a 3D checkerboard environment](https://images.ctfassets.net/kftzwdyauwt9/98e83806-f430-44e7-9ddb3a324d9b/c234368379aa009f31571ca4ac669faa/NM3A2527-2.jpg?w=3840&q=90&fm=webp)

**What else?** Aside from the technical content of the workshop, creating a supportive and inclusive environment was top-of-mind for us, and participants told us this was important for their experience. One piece of feedback read:

> “This is the first non-female exclusive social event I’ve been to in Silicon Valley with ~50% women in the room. It was so shocking that I thought I was in the wrong room in the beginning. It was noticeably easier to socialize as a result of the gender balance, so thank you for that.”

![Two people standing and talking while holding food and beverages](https://images.ctfassets.net/kftzwdyauwt9/8765b803-c1c5-4876-74ca82011976/7af8e4c299485ed37fbf6eca304e150a/NM3A2225.jpg?w=3840&q=90&fm=webp)

## What’s next

OpenAI’s [Charter⁠(opens in a new window)](https://blog.openai.com/openai-charter/) gives us a mandate “to create a global community working together to address AGI’s global challenges,” and we’ll continue developing education at OpenAI to help serve that goal. This includes more work on resources like [Spinning Up in Deep RL⁠(opens in a new window)](https://spinningup.openai.com/en/latest/) and more events like this Spinning Up Workshop. We are currently planning a second workshop with [CHAI at Berkeley⁠(opens in a new window)](https://humancompatible.ai/), which we expect to formally announce soon.

If you would like to help us do research on RL or teach people about AI, please get in touch! [We’re hiring⁠](/careers/).

*Thanks to Maddie Hall and Loren Kwan for co-organizing the event, to Ian Atha for livestreaming and recording the lectures, as well as helping participants with Python and Tensorflow issues, and to* [*Blake Tucker*⁠(opens in a new window)](https://www.blaketucker.com/) *for filming and photography!*

* [Events](/news/?tags=events)
* [2019](/news/?tags=2019)

## Author

Joshua Achiam

## Related articles

![Procgen MineRL Competitions](https://images.ctfassets.net/kftzwdyauwt9/a16a9cb0-481d-4451-5845d309b921/1f53e9075c76a1ed16ff289164671cd3/procgen-minerl-competitions.jpg?w=3840&q=90&fm=webp)

[Procgen and MineRL Competitions

CompanyJun 20, 2020](/index/procgen-minerl-competitions/)

![Robotics Symposium 2019](https://images.ctfassets.net/kftzwdyauwt9/4057d7f8-7111-4c1f-964fddf34f3e/debbcb23613365892429afc5dd8d258e/symposium-2019.jpg?w=3840&q=90&fm=webp)

[OpenAI Robotics Symposium 2019

CompanyJun 5, 2019](/index/symposium-2019/)

![OpenAI Five competitive event in a large, dim venue with bright spotlights and a large audience](https://images.ctfassets.net/kftzwdyauwt9/75b8fbb3-f482-40da-bb453d167fa7/66214ec8757c8df68b601fc3d101e6a8/openai-five-finals.jpg?w=3840&q=90&fm=webp)

[OpenAI Five Finals

CompanyMar 26, 2019](/index/openai-five-finals/)
