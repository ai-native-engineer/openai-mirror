---
title: "Investigating Model Based RL for Continuous Control | Alex Botev | 2018 Summer Intern Open House"
channel: openai
url: https://www.youtube.com/watch?v=1_sYif82CtY
youtube_id: 1_sYif82CtY
published: 2018-09-11
duration: "16:18"
captions: en-orig
---

# Investigating Model Based RL for Continuous Control | Alex Botev | 2018 Summer Intern Open House

[![Investigating Model Based RL for Continuous Control | Alex Botev | 2018 Summer Intern Open House](https://img.youtube.com/vi/1_sYif82CtY/hqdefault.jpg)](https://www.youtube.com/watch?v=1_sYif82CtY)

<details>
<summary>자막: Investigating Model Based RL for Continuous Control | Alex Botev | 2018 Summer Intern Open House (16:18)</summary>

[00:00]
hi everyone I'm Alexander Botev I'm
currently a PhD student at University
College London and I'm doing her
internship in the robotics team for
investigating model-based reinforcement
learning for continuous control so I'm
gonna chime in some of the things that
Sally earlier mentioned on model-based
control so let's dive in so this is the
outline of the talk and so let's start
first I'm going to introduce why we care
about model-based around so I have a
small intro I guess most of you are
going to be familiar but in a formal
learning we have an agent that interacts
with an environment which is different
than standard supervised or unsupervised
learning settings and the way that the
agent interacts is true actions and the
environments gives you back so
observations in a reward signal the
agents try to maximize the cumulative
sum of the rewards over the episodes
that he experienced now the main

[00:01]
difference between a model free
algorithm and a model based algorithm is
that model free algorithms try to learn
a policy PI and most often either a
value function or an action state value
function which try to estimate how good
a particular state in the environment
are for the agent to be in and this is
done solidly true using the reward
signal and experience with the
environment well in model-based RL we
try to learn additionally an internal
dynamics model which essentially two
models how does the environment evolve
and each tries to match what you
experience to the environment and in
general we assume that we don't have
access to the environment of how it
works except through sampling so what
are the potential benefits of actually
using an internal model at all so to
some extent the kind of grail that you

[00:02]
would have if you have a perfect and
ideal model is that we can solve any
task without ever interacting with the
environment so if you have a perfect
model you can simulate it as much as you
want without interrupting with the treu
environment and you can solve any task
maybe that's solving the task
might be hard but that's kind of a
concern that we won't consider too much
so however in practice we have to learn
this model so one of the benefits is
first your task independent so all of
the policies and value functions that a
model three algorithm estimates are
based on specific rewards so if you
slightly change your task it means that
usually you have to retrain from scratch
if you have a model that's very
accurately learn on one task and you
change the reward you can retrain your
model free algorithm or do any kind of
other search based on top of it without
interacting with the environment it's
usually trains in a supervised way
sometimes in unsupervised but the

[00:03]
benefit of this is that it's much easier
to train much more stable as these
techniques don't rely on things like
bootstrapping which make training more
unstable importantly we can do we can do
planning with much more sophisticated
algorithms so for instance you can do
trajectory optimization in robotics if
you have a good model you can do tree
search like in going chess and so one of
the very hardly often mentioned argument
is that you use better you better use
your data essentially rather than just
using a single scale or rewards signal
by trying to capture all variety of the
environment you are somehow learning
faster by using more information from
the environment so a wise model based
learning card however so currently most
model free algorithm are actually more
sample efficient and model based
algorithms and have better asymptotic

[00:04]
behavior so here I'm going to show you
two environment basic it's the same
environment so it's a very simple you
have a ball that you control with torque
we thread you're gonna see how does the
real environment look like and with
green it's the prediction of a model so
on the left hand side we're gonna
measure just one step prediction so
every state the model is given what's in
the environment predicts the next state
and then project that
oops can we play the left one so as we
can see one step prediction model is
almost indistinguishable from the real
environment the error is literally very
tiny so things seems to work now okay so
maybe then we've solved model based RL
but if we try now to start from a state
and unroll the environment in the model
totally independently of each other then

[00:05]
we get this kind of behavior and like
you can see how far off the model is
going and essentially this is exactly
the same model and then if you try to
train on this kind of model by just
unrolling your model then essentially
the policies that you get are very
suboptimal and don't sometimes even work
at all in the real environment so some
of the difficulties of training a
dynamics model so first not all aspects
of the environment might be relevant for
any task that you care about so for
instance if you're a house robot maybe
what's playing on the TV will never be
helpful but that might be very
complicated to model so you might be
wasting a lot of capacity of your model
on that kind of details essentially what
I showed earlier is probably one of the
biggest issue is that compounding errors
lead to very bad predictions in long

[00:06]
horizons essentially one of the main
issues currently with model-based RL is
that if you try to unroll the models for
longer horizons they start start to
become so far away from the truth that
training on them as long as it's
important for planning that you have
long horizon goals doesn't work very
hard to estimate uncertainty for
flexible models so this is in general
problem with neural networks in machine
learning and usually we want to use
neural networks as the dynamics are
actually very complicated and finally so
in terms of the sample efficiency so
ultimata based RL might sound like it
should be more sample efficient
ever in practice to learn a very
accurate model which you can use to do
anything useful your model will require
probably a lots of data so to some
extent here there's the trade of that if
to get an accurate dynamics model you
require more data then your model free

[00:07]
algorithm requires to learn a policy
then essentially a model based RL
approach will never be more sample
efficient than a model free and there's
sort of kind of gray area of whether
it's harder to learn the dynamics or
it's very easy to learn the policy and
then you don't need a model so what I'm
investigating during my internship and
main area of research was to investigate
an idea called valve expansion and
that's mainly for actor critic
architectures so one of the main ideas
of AL expansion is to kind of try to use
the model in order to improve a model
free algorithm in terms of its sample
efficiency instability so in standard
actor critic we kind of have a action
and state coming from the environment
and then a next state sample from the
environment and we try to regress our
action value function to the target
which is usually bootstrapped

[00:08]
so what value expansion does is after we
learn a model denoted in here is Chi
essentially for every offline data that
we have collected we can use the model
to unroll it multiple steps and this way
we can get on policy targets so we don't
need any Corrections for instance that
you'd usually need with important
sampling and we can get multiple step
horizon targets using unrolling the
model now this of course realized that
the model stew is reasonably accurate to
work but essentially allows us to get a
much more stable or targets and much
better potentially by having multiple of
them and now I'm gonna show you some
results and some conclusions from my
experience in trying all this in
robotics so the first environment
that evaluated on was the standard fetch

[00:09]
tasks so these are essentially
environments in a simulator where you
have a robot with seven degrees of
freedom and it has a gripper so one of
the environment is just moving the arm
to a specific location the pick and
places you have to place a block to a
specific location the push environment
you're pushing a block on a table to
application the changes on every episode
and the slide which is usually quite
difficult if you have a puck that's on a
sliding table and you have to just push
it around until it gets to the right
place but there you must be careful that
you don't overshoot so here I'm just
putting two plots of some of the work
that I've done there's a lot more but I
don't want to bore you too much so
essentially the black lines are a
baseline deterministic policy gradient
algorithm with hints on experience Lee
replay and double key learning and it

[00:10]
specifically optimized to be a sample
efficient as possible so there was a big
hyper parameter search that I did and
essentially the red and the blue curves
are model-based approaches with value
expansion and as we can see they
outperform the baseline in some cases
that's more significant than the others
but by choosing so they're a bit fragile
to some of the hyper parameters but
essentially all of the final results
were achieved with the same hyper
parameters across the task so this
showed that this algorithm actually
could help and improve at least so
sometimes it's up to five times better
sample efficiency so some take away from
my experiments which i think are quite
important so using an samples for the
dynamics model was always necessary a
single model never worked or was never
able to beat the baseline and I think
this is reassuring team in the community

[00:11]
recently so training dynamics models
usually training them on multiple step
losses essentially trying to make them
more consistent as you feed their own
predictions into them also was necessary
for improving the baseline otherwise
usually the models converged the same
value but you kind of don't get an
improving in sample efficiency also for
the valley expansion always if you
expand for more than one or two steps
was needed in order to get an actual
benefit of the method and one thing
which was quite interesting is that
being pessimistic seems to help so
essentially when you get the multiple
horizon targets rather than taking an
average or exponential average like TG
lambda taking a minimum over the
different horizons seems to do better in
the harder environments and this is kind
of similar to the double Q learning

[00:12]
we're essentially trying off to kill
some of the overestimation bias of your
q function and I'm gonna skip this cuz I
don't have time so thank you very much
for your time
[Applause]
[Music]
so the video that I shot was with a
model the trains on the dynamics and in
both cases it's like it's trained on the
same environment the difference is of
how you generate the video so in one you
start with a state of the environment
you enroll it once and then you predict
the next state and visualize that
however after that you feed whatever was
in the real environment to the model in
the second video that I showed where you
get this huge divergence essentially you

[00:13]
start from a state and then you unroll
the two things total independently so
then they are the model at every step
takes its own predictions from the
previous time step and never kind of
gets grounded again to the true
environment does that make sense okay
yeah like I can explain that later
[Laughter]

[00:14]
so do you mean whoever this during
training or during test time so yeah so
one of the points for the multiple step
loss was essentially that however so you
can do a multiple step loss where you
feed the prediction of the model into
itself multiple times and then you
ground it to the real what you saw in
the real world you can do that however
only with deterministic models and in my
experience actually with that kind of
loss for longer horizons I usually
needed to use maybe five to eight steps
horizon losses the deterministic models
did much better than stochastic ones
which however dose you can train only
with a single step

[00:15]
so um basically it was 5050 pretty much
on two of the environments the awesome
actually on one of the environment the
septic behavior was even slightly better
than the baseline which probably
suggests that the model has learned very
accurately the environment and you're
gaining something more by having
multiple horizon targets in the other
environments in two of them they kind of
converge to the same thing in one of
them the model-based approach actually
is a bit worse in asymptotic behavior so
in general you can always do the valve
expansion and also interpolate between
the valve expansion target and the

[00:16]
real-world target which is only one step
and that for instance can elevate that
problem okay thanks for the questions
[Applause]

</details>
