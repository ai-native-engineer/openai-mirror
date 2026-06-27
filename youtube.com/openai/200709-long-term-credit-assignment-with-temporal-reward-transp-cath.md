---
title: "Long term credit assignment with temporal reward transp… | Cathy Yeh | OpenAI Scholars Demo Day 2020"
channel: openai
url: https://www.youtube.com/watch?v=jjmTmYMsET0
youtube_id: jjmTmYMsET0
published: 2020-07-09
duration: "17:47"
captions: en-orig
---

# Long term credit assignment with temporal reward transp… | Cathy Yeh | OpenAI Scholars Demo Day 2020

[![Long term credit assignment with temporal reward transp… | Cathy Yeh | OpenAI Scholars Demo Day 2020](https://img.youtube.com/vi/jjmTmYMsET0/hqdefault.jpg)](https://www.youtube.com/watch?v=jjmTmYMsET0)

<details>
<summary>자막: Long term credit assignment with temporal reward transp… | Cathy Yeh | OpenAI Scholars Demo Day 2020 (17:47)</summary>

[00:00]
the first graphic I wanted to share with
you guys was a graphic of reinforcement
learning agent playing an Atari breakout
video game and that's an example of a
case where standard RL can learn in a
certain environment very well but the
problem I'll be focusing on is
specifically a problem with delayed
rewards and this is very relevant to
real life because as you interact with
your environment you don't typically get
points every time you move there's
actions that are separated by very long
timescales from their effects Kathy
would you like me to help you move your
sleds yeah what I can't seem to change
my screen my keyboards not responding to
that I'll show them

[00:01]
oh okay thanks Francis and so here's the
I think I might have it apologies for
the technical difficulties
okay can you guys see my screen my
slides yes okay um so the plan is going
to be three parts so first I will
describe to you why standard RL does
struggle and these tasks with long
delayed rewards next I will describe the
temporal reward transport algorithm or
trt that I've been working on to address
this problem and then finally I will
share some results from experiments
using TRT okay so um the motto in

[00:02]
reinforcement learning is you have an
agent interacting with the world and as
it interacts it transitions from state
to state and it can pick up a reward
along that trajectory and so here I have
an equation or something called the
discounted returns and this is just the
sum of all the rewards that the agent
picks up along its trajectory um but
there's this extra bit that's added to
this returns and it's this discount
factor gamma and this gets at the crux
of why standard RL algorithms do
struggle with tasks with delayed rewards
the gamma introduces a timescale and
it's basically a heuristic that says
that you care about rewards now versus
later in the future so you're
discounting your future rewards and so
in this plot here I have an example if
you're standing at time zero and you
look forwards a hundred times steps then
the reward a hundred time steps in the
future is discounted by a factor so

[00:03]
that's about 37 percent of its original
value and so this is totally fine if
you're in an environment where your
immediate actions really just effect the
the most immediate rewards but in cases
with long delays then it's not going to
work as well and so let's take a look at
that so here's an example we have this
little guy who is walking through the
environment and at some point he can
choose to pick up a key or not
he doesn't get a reward for picking up
that key so this agent continues and
interacting with the environment until
the very end
it reaches a green goal where if it did
pick up the key in that first state then
its rewarded extra bonus points 20
points um so the problem with standard
Ariella though is that it wants to
reinforce actions based on the rewards
that were acquired after taking that
action but if we look at the rewards

[00:04]
that would weight this particular state
action pair where he's next to the key
we'd see that the future rewards are
highly attenuated and so there's a very
really low signal and learning is very
slow as a consequence and so what can we
do about that
that brings me to the next part of my
talk which is a the tier T algorithm so
this algorithm was based on work by hung
from deep mind on optimizing agent
behavior of her long time skills by
transporting value and the idea is that
if you've identified the significant
state action pairs that should receive
credit for some long-term reward then
you can splice those distant rewards to
these state action pairs so that you can
amplify the signal to reinforce those
actions and so that's what we see here
so in this original situation on the
slide this agent receives zero immediate
points we're picking up the key but we
splice in these future rewards in this
case the distal rewards might be 20
points suddenly we have a lot more

[00:05]
signal to amplify to increase the
probability of taking an action in that
state which is what we want we want the
agent to learn to pick up the key so
that brings us the next question how we
know what the significant state action
pairs are in order to receive these
spliced rewards the TRT on so that is
the problem of credit assignment in
green flow and reinforcement learning
and the way we do that and the way that
hung did it is using an intention
mechanism and so the idea is you do a
full rollout of an episode so the agent
interacts with environment at the end of
that rollout you pass the entire
sequence of states and actions to a
model in my case a binary classifier and
you look at
what state action pairs were paid most
attention to by the other frames excuse
me and so here I have a heat map and
this heat map is a plot of the attention
scores and you can see there's these two
really bright stripes oh by the way the

[00:06]
axes denote on the frames and the
trajectory you both on the x and y axis
so in this case there's two really
bright stripes and they correspond to
highly attended state in action pairs
and if we do a sanity check we can
actually bring up what that particular
observation was we see that it actually
makes sense with what we would expect so
in this case we have an attention and we
have an a an agent who's a little bread
triangle next to a key so it might be
moving forward towards it or trying to
pick it up so this is a good
confirmation that we are attending to
the important states in actions
so next step is to test out whether this
TRT algorithm works and so I created an
environment specifically constructed to
make it challenging to learn if you
don't do credits I meant over the long
timescales in this case this environment
has three phases first phase the agent
is encounter as an empty grid with just

[00:07]
a single key and Aiden can choose to
pick up that key or not but it doesn't
receive any immediate reward if it picks
it up the second phase is a distractor
phase so we fill this distractor phase
with gifts and when the agent opens a
gift it gets immediate rewards and then
the final phase this is the focus of our
evaluation is the phase at which the
agent can earn a distal reward so when
the agent navigates to the green goal if
they learn to pick up the key in phase
one it gets 20 points if it never
learned to pick up the key it just gets
five points so that's going to be the
focus of the the rest of the
experimental results I'm going to show
you we will focus to see if the agent
learns to pick up the key and
correspondingly get the twenty points in
Phase three
so the I have three separate
experimental slides I'm going to show
you
they all involve varying the parameters

[00:08]
of the distractor phase essentially
making it more and more challenging for
the agent to learn and so the three
parameters I vary are the time delay
which is the time that the agent is
forced to spend in the distractor phase
the gift reward size for the distractors
and then also the variance of the
destructor rewards okay so these plots
here show the total rewards that were
earned by the agent in Phase three to
see whether it picked up the key or not
and as you move from left to right it
becomes increasingly difficult each plot
corresponds to a certain delay and so
tau of gamma is equal to the discount
factor time scale and we see increasing
from left to right and so you can see
initially when the time delay is not
that long the agent does learn to pick
up the key doesn't do quite as well as

[00:09]
with the trt algorithm on top of the
advantage actor critic the the baseline
is a TC advantage actor critic but then
by the time you get to the rightmost
plot you can see that ATC has basically
plateaued at five and that five points
if you recall corresponds to only moving
to the goal and never really there I
need to pick up the key and whereas if
you had trt that shows consistent
progress about learning how to pick up
the key and then the next slide is the
slide with experimental results for
varying the destructor award size so
again left to right it's harder as we
increase the size of the distractor
rewards and again we see the same
pattern a TC with the trt algorithm does
better than a TC alone and then the
final slide was an experiment showing
the last returns in Phase three
when we vary the variance of the
distracted rewards so in this case we

[00:10]
have four gifts and they all have a mean
reward of five but for each gift we
sample from a uniform distribution
around five and we increasingly we
increase the range of the
a uniform distribution in order to
increase the variance and so they all
have the same being reward but there's
just greater variance and again you can
see that ATC plus trt does better than
ATC alone
so to summarize we've seen that adding
to purl reward transport on top of
standard reinforcement learning
algorithms safe to show some benefit for
long term credit assignment this work
has built directly on the ideas from the
hung paper in 2019 and the two core
concepts to take away from that are the
idea of using some sort of temporal
value or reward transport to splice on
to significant state action pairs and
then to use attention to identify the

[00:11]
important state action pairs so our
contribution here has been a completely
different architecture implementing
these two core concepts it's much
simpler than the original papers
implementation it's also much simpler
environment but I think there's
definitely merit and having showing that
this concept kind of just carries beyond
the original implementation and the
paper the implementation is also very
modular so I totally separated out the
attention part of this algorithm into a
separate classifier in order to identify
the significant state action pairs and
so you can imagine if you want to try
adding trt to some other model you can
do that it's very easy to add it on
because of the modular implementation so
in the future well there's tons of work
there's never anything where there's
always more this is just a heuristic and
so it would be interesting to move

[00:12]
beyond just a turistic but it's a useful
heuristic um and also I've only shown
you results for a very simple grid world
environment and so it would be
interesting to see how well the
algorithm can hold up in more complex
situations so with that said I had a lot
of fun working on this project and so I
want to move on to the Q&A stage but
also I want to
sent out my cops so I'd like to thank my
mentor Jerry at open AI for being with
me through this whole process I wanted
to thank opening I itself for this
wonderful opportunity and all the
different people I've talked to informal
casual conversations I've picked up so
much thank you to the program organizers
Kristina and where I have been really
wonderful so supportive of the scholars
and I also have my lovely scholars
cohort to think they were also very
supportive there was a lot of knowledge
sharing as we all ramped up on deep

[00:13]
learning at the same time finally I'd
like to thank square my employer for
giving me this chance to take some time
off to do this program and then if
you're interested in more project
details my write-up is available at my
blog if ab d be calm okay and then now
I'm going to take a look at cushioned
so the question is can you explain why
the distractor fitties makes the task
more difficult and in other words in
your opinion why does the agent not
learn the more general behavior of
simply interacting with all objects
picking up the key and opening the gifts
so I think this gets as with standard RL
algorithms
there's this idea that for policy

[00:14]
gradients if you have a policy which is
how you want to choose an action in a
particular state you can amplify it or
reduce the likelihood of doing that
taking that action based on the rewards
that follow it and because of
discounting you won't see rewards in the
far future and so in this case if you
are in the key state or in the state in
the phase one where your connects to the
key it's not gonna receive that
amplification in that particular state
because the rewards in the distractor
phase are unique to being in the state
next to those distracting gifts so the
agent very quickly learns to open the
gifts because it sees an immediate
reward from the guess so that that's
that waiting of the reward is very high
and so it reinforces this idea we want
to do the toggle action to open the
gifts and so it doesn't just translate

[00:15]
thought of that simply just because
you've learned that you have to take
this particular action in this state the
way the algorithm is set up it doesn't
just translate to learning how to do
that if your next is the key
okay the next question is I am curious
to know if using more advanced deep RL
algorithms like PPO would wait more than
the TR T's influence and the results I
guess so I'm not 100% sure about this
wording it sounds like like what would
happen if I had tried it on PPO instead
of A to C and that's a straightforward
test we can do because of the modular
and presentation on but so PPO is more
sample efficient than a 2 C it is able
to do several smaller updates compared
to one single update by ATC before

[00:16]
starting your batch of experiences so
given that I would expect it to have a
better learning curve I'm not sure if
the interaction with trt would be any
different but I would expect PPO to to
fundamentally look a little better than
the baseline that I showed here
I just haven't tested it out yet
what was the most challenging part of
your project
oh there's a lot uh well so I think at
some point when I finally when I decided
on this particular path I always had a
bunch of ideas for how to get it working
and every time I tried something new and
you commit to get hub I thought maybe
this will be it and so the the
challenging part was seeing the the
deadlines kind of looming and starting
to realize that all my fixes weren't
necessary submit necessarily becoming
like the last fix but then in the end

[00:17]
things worked out when I had like a
little I realized there's some artifacts
that were being introduced due to the
way this algorithm is set up it's very
sensitive to the full context of the
episode and I had to think about how I
can handle that because it would have
required quite a bit of reengineering of
my code with very little time in order
to do parallel training which was really
important I needed to run this on many
workers and so I I had an idea to
rejigger or something well so I'm
running out of time um but but basically
it was just pushing through and it kind
of worked out in the end so I'm really
glad of that
and then so with that okay thanks

</details>
