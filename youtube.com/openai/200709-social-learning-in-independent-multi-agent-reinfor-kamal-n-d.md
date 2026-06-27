---
title: "Social learning in independent multi-agent reinfor… | Kamal N’dousse | OpenAI Scholars Demo Day 2020"
channel: openai
url: https://www.youtube.com/watch?v=Qy9J5519s68
youtube_id: Qy9J5519s68
published: 2020-07-09
duration: "23:05"
captions: en-orig
---

# Social learning in independent multi-agent reinfor… | Kamal N’dousse | OpenAI Scholars Demo Day 2020

[![Social learning in independent multi-agent reinfor… | Kamal N’dousse | OpenAI Scholars Demo Day 2020](https://img.youtube.com/vi/Qy9J5519s68/hqdefault.jpg)](https://www.youtube.com/watch?v=Qy9J5519s68)

<details>
<summary>자막: Social learning in independent multi-agent reinfor… | Kamal N’dousse | OpenAI Scholars Demo Day 2020 (23:05)</summary>

[00:00]
Hello everyone. Um
I I'm excited to be presenting my
scholars project. Uh I've been focused
on social learning in independent
multi-agent reinforcement learning.
Um so
Oops.
Um
my interest in
social learning came
uh through reflection on
uh
how it is that I as a human have the
capacities that I do.
Um so if I had happens to have been born
in the woods away from all other humans,
I would probably just have like quickly
starve to death. But uh thanks to my
ability to tap into cultural knowledge,
um I have the potential to do all sorts
of awesome things like participate in uh
space program or
uh
lying in bed all day and browse Twitter.
Um
And I think if one were to if if one

[00:01]
were an alien who just appeared on Earth
uh and saw an example of a human in
isolation, I I think it would be very
surprising to see the
uh broad variety that of behaviors that
groups of humans uh are able to exhibit.
Um or that individual humans can do if
they can tap into that cultural
knowledge.
Um so
Yeah. Um
because of the centrality of
uh
social learning to human intelligence, I
think it's important to understand the
circumstances in which
um social learning can take place.
Um and
so in order to
uh
sort of experiment with this, uh there's
a cool anecdote from uh experimental
sociology. So basically, a group of
monkeys were put in a room along with a
ladder and some bananas were suspended
from the ceiling such that they could be
accessed by a monkey who climbed the
ladder but were otherwise inaccessible.

[00:02]
And
Really quickly, do you mind sharing your
slides
so that we can just see the image you're
talking about? Thanks.
Uh yes.
I apologize. Is that working better?
Awesome.
Cool.
Yeah, so um
Yeah, uh there's a group of monkeys in
another room. They can only reach the
bananas using a ladder. And anytime a
monkey climbed the ladder to access the
bananas, experimenters would uh spray
the rest of the monkeys with cold water.
So, the other monkeys learned that uh
they should you know, beat up the monkey
that tried to climb the ladder in order
to prevent themselves from getting
sprayed. Um
and
so, this behavior persisted even after
the monkeys stopped being sprayed with
water.
Um
and even more interestingly, when new
monkeys were introduced into the group
after the water spraying had ceased, the
uh new monkeys, of course, would try to

[00:03]
get to the bananas and then the other
monkeys would beat them up. Uh so, they
would learn not to access the bananas or
not to get the bananas, but they would
also learn to punish other monkeys that
tried to get the bananas. Uh this became
like a cultural phenomenon among the
monkeys.
Um
so,
as it happens, this experiment is
apocryphal uh and did not happen. But,
um I think it's still serves as an
interesting template for how we can try
to understand social learning.
Um so, the question I'm interested in
answering is that of whether independent
reinforcement learning agents can learn
from each other um just by virtue of the
fact that they exist in the same
environment and can maybe observe one
another.
Uh and I think this is an important
question because in as reinforcement
learning becomes more capable, it seems
likely that there will be many
environments in which uh many
reinforcement learning agents might
interact. So, for instance, uh uh
stock trading
autonomous and adaptive robots trading

[00:04]
stocks in a market. Um and so, it's
clearly important to understand the
circumstances in which they might learn
from one another
and exhibit behavior that we might not
expect if we were only looking at one of
them in isolation.
Uh so,
I will break my talk down into two
parts. First, I'll discuss the tools
that I used to approach this question.
Um and in particular, the environments
and reinforcement learning algorithms
that I used.
Um
And then, I'll talk about some actual
experiments about
learning from experts.
So,
um I developed a
an open-source grid world implementation
called Maro Grid, um which is
uh fits the standard Open AI Gym API.
It's easy to extend. So, it's easy to
put a bunch of
a large number of agents in the
environment and it's very configurable.

[00:05]
And there are also some registered
environments uh
so that uh
for reproducibility.
Um and given how obscure this domain is,
I I'm surprised that it's already got a
little bit of traction on GitHub.
Um and this is an example of
the visualizations that I built.
These agents are
effectively untrained, but it's easy to
include a lot of them in the environment
and visualize what each of them is
doing.
Uh and the particular scenario that I
spent a lot of time working with,
I call goal cycle. So, in this
environment, there are a number of goal
tiles, and agents in the environment are
rewarded for traversing them in a
certain order. And they're penalized
anytime they mess up that order.
Um
and uh it's
uh
one can uh experiment with this
particular environment, the one that I'm
showing here, um
by uh installing it uh with a Python

[00:06]
package from GitHub.
Um
so the
um
the this environment is kind of like an
analog to the room with the monkeys. So,
the reinforcement learning agents that
exist in this environment uh
can observe one another
uh and in principle interact with one
another.
Um
there are a couple uh
interesting things about this
environment.
Uh the penalty is configurable, and
changing the value of the penalty
changes the difficulty uh of learning to
explore the environment effectively.
When the penalty is low, the agents kind
of ignore the
uh
penalty incurred by stepping on the
tiles out of order. So, on the video on
the left, the agent um
is not cycling through them in order um
and
anytime the agent steps on a tile out of
order, its color resets to red.

[00:07]
When the penalty is very high,
um
exploration is costly because uh the
incurring the penalties is aversive, and
the agents learn to step on the first
tile uh where they get a reward, and
then they just avoid all of them.
Um
so by controlling again by controlling
the value of this penalty, we can change
the difficulty of exploration. And in
the context of social learning, we
change the difficulty of learning the
effective strategy directly from the
environment as opposed to learning it by
observing other agents.
Um and then the other big tool was the
reinforcement learning algorithms that I
used.
Um so I started by implementing DQN,
which is like uh pretty standard for
this sort of simple environment. Uh but
I needed to add memory in order for the
agents to be able to learn strategies
that unfold over the
uh
more than one time step.
Um

[00:08]
this didn't work super well and I spent
a lot of effort trying to improve it. Uh
notably I im- implemented prioritized
experience replay,
uh which is a kind of tricky with the um
addition of the uh LSTM.
Um that it still didn't work very well
and I So I implemented PPO and
immediately found a pretty
uh big improvement.
Um but further, I found that uh carrying
uh carrying over the
some of the tricks from the R2D2
implementation
uh and notably refreshing the hidden
states that are collected during the
environment over the course of update
steps, uh significantly improved the
agent's capacity to use their uh
memories to accomplish tasks.
Um and
these diagrams show or these plots show
the difference that it made uh for a
simple goal cycle environment where the
agent is learning to traverse the goals.

[00:09]
So basically, when this trick is
applied, uh the agents are able to uh
achieve much higher rewards and their
training is much more stable.
Um So yeah, to recap, uh
a lot large part of the effort of the
project went into developing the
reinforcement learning algorithms and
environments that uh allowed agents to
effectively learn tasks um
that uh are amenable to the kind of
experiments that I will discuss.
So
um
revisiting the original question, I'm
interested in knowing when independent
agents can learn to
um
can learn from experts to accomplish uh
tasks or can acquire skills from
experts.
So, what this might look like is
uh
we might have a bunch of experts who uh
have a high level of skill and a novice
who's introduced to the environment uh
initially is very unskillful, but then

[00:10]
uh is able to
uh
get to the point of expertise uh just by
observing the experts.
Um and we'd also want it to be the case
that the if a novice was alone, they
would be unable to learn and their uh
skill would remain low.
Um
so there is a paper that um
addresses a question like this uh called
observational learning by reinforcement
learning by Diana Borsa et al. from
DeepMind.
Um and in their paper, the experts are
hardcoded and novices use RL to
accomplish the task in a simple grid
world.
Um so
the diagram on the top shows like a high
uh bird's-eye view of the map. Uh the
expert in blue uh optimally travels to a
goal, which is which at each episode is
placed randomly at one of these 16
positions. And uh the novice needs to
learn to get to the goal as well.
Um
here's an image of that or a video of

[00:11]
that. Um
they found that the experts help
the novices learn more quickly, uh but
the presence of the experts um
even in the presence of the experts, the
novices the Sorry, the experts don't
cause the novices to do any better uh
ultimately than they would if they were
learning alone. Um
so I
started by trying to replicate um
the first finding in a
uh simple cluttered grid world, which is
like the goal cycle uh grid worlds I
showed earlier, but where there's only
one goal,
and found that found very convincingly
that the presence of experts didn't help
the novice agents
learn to accomplish their task any more
quickly.
And the takeaway here is kind of that
it's like hard to learn from social cues
in these environments.
Um
but
that doesn't prove that it's impossible,

[00:12]
and in order to uh
uh look in a more targeted way for the
circumstances in which this might
happen,
my effort shifted to different
environments, and in particular the goal
goal cycle environment.
So, the goal of my experiments has been
to construct a scenario where
in contrast to the Borsuk results,
novices and experts are the same sort of
agent, so they're both trained by
reinforcement learning,
where solitary novices struggle to
learn, and where the presence of experts
helps. And ideally, we'd want the
novices to be able to themselves become
experts, so that we can see that they
like have mastered the the skill.
Um
and as a bonus, ideally the
whereas in the Borsuk case, the
uh the information that the novices get
from the experts is
uh
or there's not all that much information
that the novices can get from the
experts because the goal was in like one

[00:13]
of 16 places, and the novices could just
like memorize the potential places.
We want something that looks a bit more
like a skill. Um and so
in the
we get this in the goal cycle
environment because the
process of uh spawning in a new
environment and trying out the different
possible cycles until identifying the
correct one
is more
is a closer analog to skill than just
like queuing as to which quadrant the
goal is in or something like that.
So, I found that
when the
goal cycles are masked from the view of
novice agents, novices do in fact learn
to follow experts. And this is
consistent with the results from Bursa.
So, in both of these videos, both of
these videos exhibit this behavior. The
novices are shown in the bottom of the
columns on the right.
Um
and yeah, in both cases the novices are

[00:14]
doing like a really robust kind of like
following behavior.
Yeah, here the
one of the experts happens to have
spawned in a
trap. Basically.
Um
and in these cases because the novices
is the novices are just following the
experts,
they end up converging to slightly lower
performance
than the experts as you can see in this
graph.
Um
So,
the so far the conclusion that I've
drawn is that it's like very hard to
learn from other
to learn from experts. And when it's
possible to
acquire a skill directly from the
environment,
it is likely that agents will do that.
Um so, in order to
The next steps for this project which
I'll continue working on
focus on trying to
create environments where the social
where the information available from the

[00:15]
experts is
more valuable cue as to how to obtain a
high reward than the information
available directly from the environment.
And so, I plan to increase the number of
goals and
experiment with different penalty values
and so on.
Um also, the Uh, in the example that I
showed, the following behavior, uh,
while it does help the agent accrue more
rewards, uh, isn't quite the same skill
that the experts are showing.
Um, going back to the monkey analogy, we
want the, uh, novice agents to be doing
the same thing that the experts are
doing, exhibiting the same skillful
behavior.
Um, and so a better way to measure that
would be by looking at the performance
of the agents when they're moved to a
new environment without agent without
experts.
Um,
and another approach is to add
mechanisms to encourage agents to learn
socially. Um,
it's

[00:16]
uh, not clear, for instance, to what
degree humans are social learners
because of, like, biological,
uh,
because they're biologically predisposed
to do so,
as opposed to because of the, uh,
environments that they're in. Obviously,
by comparing to animals, we might expect
the former. Um, but, yeah, so we can
introduce we can similarly introduce,
like, uh, these priors into agents, and
then,
uh,
we can,
uh, characterize the, uh, emergence of
the social behavior by varying or
turning down, uh, that prior.
Um,
so, yeah, I'd like to thank my mentor,
Natasha, who's been incredibly
supportive and incredibly helpful in,
uh, both helping me,
uh,
like, make the best use of, uh, learning
resources and helping me engage with
the,
uh, broader AI research community.
I'd like to thank the program
coordinators, Mariah and Christina, for
helping the program go smoothly, uh,

[00:17]
even in light of the pandemic. I'd like
to thank, uh, my fellow scholars for a
lot of incredibly informative
discussions, and, uh, uh, yeah, just
generally being extremely supportive.
Um,
special shout-outs to Winsor & Bias for
helping me keep track of my experiments.
And also to uh
Lithia Power for lending me a graphics
card that I've been using for some of
these experiments.
Um yeah, so I have time for some
questions.
Uh so the first question is, can a
novice become more expert than an expert
such that other experts learn from it?
Um that's a great question. In the
experiments I've been doing, um the
experts
continue to learn alongside the novices.
Um so
here for instance, in this plot, the uh
the experts are still learning. Uh but

[00:18]
because in this environment they happen
to be close to optimal, so we don't see
much change uh as they continue to
adapt.
Uh but in principle, yes, this could
happen. I think another
uh interesting direction
uh is for understanding like social
behavior in independent multi-agent
reinforcement learning is to uh
carefully study the impact of just like
learning in a group, um which
uh
is kind of similar to that.
Um
Yeah.
Cool. So uh another question is, could
you elaborate on hidden state refreshing
in your agent? When do you refresh the
hidden state? And how does it differ
from the R2D2 approach?
Um so
the agents that I trained uh so I
trained a lot of the agents with PPO. Uh
with PPO, agents alternate between

[00:19]
collecting experiment collecting
experience in an environment and
updating based on that experience. Um so
during the update phase,
um the
agents sample their experience and
perform a bunch of small updates based
on that batch of experience before
discarding it at the end of each uh
update. Uh so,
the
hidden states um
the
So, the
typical way that the agents um or in
typical PPO LSTM implementations, the
agents will save their hidden states as
they interact with the environment. So,
this is like uh
remembering what was in their
uh mind alongside the experiences. And
then they will
sample those as they are doing each of
these like little updates.
Um but, the
nature of the experience that they
collected depends on the values in the
hidden state. And the values in the
hidden state depend on the parameters.
So, as they update the hidden states um

[00:20]
the
uh
the
uh
behavior in their the behavior that
they're learning probably becomes less
and less representative of the um or
there's a big divergence between the
behavior in their between the data in
their experience. Um and the uh
parameters of the current values of the
parameters. So, I found that it wasn't
too costly to do this um
and I uh
have some tweaks to my like LSTM
implementation that facilitate this.
Um and in the end, I end up refreshing
them
uh basically between each iteration,
each gradient step.
Uh and
uh the R2D2 approach differs in a few
ways. Um the reason for those
differences, I think, is mainly that uh
the R2D2 approach is off-policy. Uh and
so, each gradient step uh has the
potential to or the the volume of
experience that can go into each update

[00:21]
is much larger. Uh and so, because of
this, they need to employ some tricks to
make sure that the
um
that the hidden states don't get too
stale without refreshing them between
each generation cuz that would be very
costly. But, for PPO and on-policy
reinforcement learning, it like didn't
matter too much.
Um
Another question is, why do you think
that proximal policy optimization worked
so well?
Um
That's a good question. I think um
Let's see.
So, I have been thinking a bunch about
this, and I think that uh
a lot of it in practice comes from the
fact that I uh my implementation of PPO
is based on the spinning up
implementation, uh and I guess spinning
up also deserves a shout-out. Um
And it so it inherited a lot of tweaks
that uh helped uh
helped the agent learn stably and

[00:22]
perform well. Uh and it is possible that
um if I
Yeah.
So, I I hesitate to say that uh PPO is
better than DRQN. Um that's certainly my
experience, but uh
I think
I I inherited a lot of uh
a lot of improvements from the
implementation that I based it off of.
Um and then
Yeah, the
hidden state refreshing, I think uh is
interesting.
It is
um
It Yeah, it it helped immensely with
robustness.
Um
And
yeah, I think the the reason is that it
prevents the policy from making uh
big changes over the course of each
update. Um and this yeah, helps it uh
helps ensure that the policy is
consistent with the data that it's
learning from. Um I guess
uh I I would be interested to for for

[00:23]
some clarification on that question, but
um yeah.

</details>
