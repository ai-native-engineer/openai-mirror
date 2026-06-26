<!-- source: https://openai.com/index/hackathon-follow-up/ -->

March 15, 2018

[Company](/news/company-announcements/)

# Report from the OpenAI hackathon

On March 3rd, we hosted our first hackathon with 100 members of the artificial intelligence community.

![Hackathon Followup](https://images.ctfassets.net/kftzwdyauwt9/9d21ff95-0741-460a-25557238bf5f/0de17dc8d70f473c21d50074118e1ef7/hackathon-follow-up.jpg?w=3840&q=90&fm=webp)

On March 3rd, we hosted our first [hackathon⁠(opens in a new window)](https://blog.openai.com/hackathon/) with 100 members of the artificial intelligence community. We had over 500 RSVPs arrive within two days of announcing the event—if you didn’t make it this time, please RSVP again in the future!

Thank you to [Cirrascale⁠(opens in a new window)](http://www.cirrascale.com/) for providing GPU machines during the hackathon.

## The crowd

Our applicants included high schoolers, industry practitioners, engineers for nonprofits (not just at OpenAI!), researchers at universities, and more, with interests spanning healthcare to AGI. We could only accommodate one hundred people this time so we tried to pick a balanced crowd with a wide range of backgrounds and levels of experience. In particular, we strove to achieve gender balance; many attendees told us that this kind of representation made a positive difference for their experience of the hackathon.

## The talks

![Two people seated in armchairs holding and talking into microphones](https://images.ctfassets.net/kftzwdyauwt9/19a8578b-f647-43fc-f98921ad9254/bf1e09edeaafe9a403b0c26a812b2580/2018-03-03_OpenAI_090930.jpg?w=3840&q=90&fm=webp)

We kicked the day off with a series of talks on OpenAI’s mission and the technical topics that we focus on in our research. Sam Altman took questions on AGI timelines, safety issues, and the importance of avoiding AI arms races. Sam described how he personally came to focus on AI safety: he saw it as an underfunded, under-explored area with the potential to impact everyone. Josh Achiam gave an introduction to reinforcement learning, which is one of our main research areas; we’ve open-sourced [the slides and sample code⁠(opens in a new window)](https://github.com/jachiam/rl-intro) from his talk. Ilya Sutskever talked about self-play with RL agents; for an overview of the work covered, see our recent [blog⁠(opens in a new window)](https://blog.openai.com/meta-learning-for-wrestling/) [posts⁠(opens in a new window)](https://blog.openai.com/competitive-self-play/) and [code⁠(opens in a new window)](https://github.com/openai/robosumo) [releases⁠(opens in a new window)](https://github.com/openai/multiagent-competition). Alec Radford provided a tutorial and survey of the many different kinds of GANs and we’ve made the [tutorial code⁠(opens in a new window)](https://github.com/Newmu/gan_tutorial) available.

## The hacking

![Aerial shot of a group of people sitting around a large table, working on their laptops](https://images.ctfassets.net/kftzwdyauwt9/61ecf41e-a559-46ce-d7b9215e0cd9/9bbf0f105a96299c6dd05897e154e2c1/2018-03-03_OpenAI_112356.jpg?w=3840&q=90&fm=webp)

After the talks wrapped up, the hacking began. Over the course of an 8-hour code sprint participants authored dozens of AI projects on topics ranging from safety to healthcare. Some of our favorites:

* Jiale Xian, Clarence Leung, Kyle Zheng, Madeline Hawkins, and Stergios Hetelekides worked on an image classifier to identify purine-rich seafoods that gout patients should avoid.

Loading...

* [Arthur Juliani⁠(opens in a new window)](https://twitter.com/awjuliani/status/970496935982333953) implemented PPO with curiosity-based intrinsic rewards and trained an agent to smash block towers:

Loading...

* High schoolers Ethan Knight and Osher Lerner worked on [Natural Q-Learning⁠(opens in a new window)](https://github.com/hyperdo/natural-gradient-deep-q-learning) based on one of our [requests for research⁠(opens in a new window)](https://github.com/openai/requests-for-research/blob/master/_requests_for_research/natural-q-learning.html).
* Malhar Patel and Lee Redden worked on [AeroEnv⁠(opens in a new window)](https://github.com/LeeRedden/OpenAIHackathon), a Gym interface for a physical robot.
* Rodger Luo implemented [Q-learning in Processing⁠(opens in a new window)](https://github.com/RodgerLuo/RL_Processing), a programming tool for media artists.
* Andy Matuschak developed the [scrying pen⁠(opens in a new window)](https://andymatuschak.org/scrying-pen/), a fun and unique tool for machine-assisted sketching based on [SketchRNNs⁠(opens in a new window)](https://github.com/tensorflow/magenta-demos/tree/master/sketch-rnn-js).
* James Giammona and Brad Neuberg generated [ideas⁠(opens in a new window)](https://paper.dropbox.com/doc/Safety-Distance-Move-Slow-and-Dont-Break-Things-JlrnhtfqENPdfcfTTWfaT?_tk=share_copylink) for how RL agents might avoid dangerous parts of the environment that they haven’t seen before.

![Person looking over the shoulder of people sitting around a table with laptops](https://images.ctfassets.net/kftzwdyauwt9/b3702859-b777-4346-a220fac3f14f/2b87f33f84ef67d7356f4707407d4976/2018-03-03_OpenAI_112343.jpg?w=3840&q=90&fm=webp)

We got a [lot⁠(opens in a new window)](https://twitter.com/malharhar/status/970458361274617857?ref_src=twsrc%5Etfw) [of⁠(opens in a new window)](https://twitter.com/me_develops/status/970185621787430918?ref_src=twsrc%5Etfw) [helpful⁠(opens in a new window)](https://twitter.com/catherineols/status/970374298593460224?ref_src=twsrc%5Etfw) [feedback⁠(opens in a new window)](https://twitter.com/ngundotra/status/970579444002729984?ref_src=twsrc%5Etfw) [from⁠(opens in a new window)](https://twitter.com/Smerity/status/970029887518945280?ref_src=twsrc%5Etfw) hackathon attendees, which we’ll use to make even more interesting events in the future: stay tuned! If you’d like to work on AI as your day job, you may be interested in our [Scholars⁠(opens in a new window)](https://blog.openai.com/openai-scholars/) or [Fellows⁠(opens in a new window)](https://jobs.lever.co/openai/54ddfefe-6483-4bba-a828-11a156eae7eb) programs (you’re of course always welcome to apply [full-time⁠(opens in a new window)](https://jobs.lever.co/openai/)).

* [Events](/news/?tags=events)
* [Community](/news/?tags=community)
* [2018](/news/?tags=2018)

## Authors

Joshua Achiam, Parnian Barekatain

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
