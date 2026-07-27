---
title: "OpenAI Spinning Up in Deep RL Workshop"
channel: openai
url: https://www.youtube.com/watch?v=fdY7dt3ijgY
youtube_id: fdY7dt3ijgY
published: 2019-02-02
duration: "3:24:33"
captions: en
---

# OpenAI Spinning Up in Deep RL Workshop

[![OpenAI Spinning Up in Deep RL Workshop](https://img.youtube.com/vi/fdY7dt3ijgY/hqdefault.jpg)](https://www.youtube.com/watch?v=fdY7dt3ijgY)

<details>
<summary>자막: OpenAI Spinning Up in Deep RL Workshop (3:24:33)</summary>

[00:25]
Hello, and good morning everyone!
Hi! I'm Josh Achiam, I'm a Safety researcher
here at OpenAI and I'm the main author
of Spinning Up in Deep RL up and thank you
all so much for being here today at OpenAI's 1st Spinning Up Workshop.
oFor people who are tuning in on the
livestream I'd like to let you know that
there is a minor technical difficulty
and so we will not be able to broadcast
the slides directly from my computer
into the livestream video so you'll be
seeing the screen through the camera. In
the event that that's not enough for you
to see it clearly I just open sourced
the repo that has the PDFs for these
slides so please go to github.com slash
open AI slash spinning up - workshop and

[00:26]
you'll find in the RL intro folder RL
intro PDF which will be the presentation
that I'm about to give so hopefully that
makes it easier for you to follow along
so since this is kind of a new thing
that we're doing I'd like to start today
by talking about what it is and why
we're doing it and what we hope you get
out of it from being here education at
open AI is this concept that as part of
our mission we want to make sure that we
provide for the public good and that we
help foster a global community around
AGI which is the thing that at opening I
we care the most about and are trying to
figure out how to make sure happens in a
way that's safe and beneficial for all
of humanity so for those of you who
aren't already familiar AGI is
artificial general intelligence the idea
is that this is going to be some very
powerful AI technology that'll have the
ability to change pretty much everything
about how we do anything something that

[00:27]
could potentially do most economically
valuable work something that could solve
tasks that currently only human
intelligence is capable of solving and
so we think it's really important that
we help people become aware of what AGI
is and what the technology that'll
likely underlie it is so that you can
think critically about issues that might
come up in the future and also if you're
interested
participate because we really need for
people to step up and help make sure
that this technology is safe and does
what we wanted to do and doesn't cause
anything harmful or detrimental to the
world so spinning up is the first thing
that we're launching under this
education at open AI initiative and the
goal is to help people acquire technical
skills in the research topics that we
care about so spinning up in deep RL is
a resource that hopefully all of you
have seen by now it contains a number of
different pieces including a short intro
to reinforcement learning so what is

[00:28]
this thing that we're doing so much
research about at open AI an essay about
how you would go about becoming a
researcher if you're interested in
joining a curated list of important
papers in the field so this is
particularly important because since
this is an emerging field there isn't
really a clear consensus on the best way
to learn it or a textbook that
completely illuminates the way from
start to finish and a lot of the
important knowledge right now is still
in research papers so if you want to
find out the most stuff about this you
have to go digging and hopefully this
helps you figure out where to look also
a code repo of key algorithms because
for any of you who have tried hacking in
this field before I'm sure you found
that there were a lot of very confusing
resources out there really excellent
ones but nonetheless ones that made
non-obvious choices and didn't clearly
connect what they were doing to why they
were doing it and so we hope that the
repo that we provide and spinning up in
deep RL is part of something to bridge

[00:29]
the gap there and of course some
exercises so if you want to actually try
coding something up there are a few
ideas there for for what to do to get
you familiar with some of the key pieces
of math or algorithms or what kind of
bugs you might expect and so why are we
having workshops so in addition to
putting these resources online we think
it's gonna really help people if we work
with you one-on-one if we can see you
face-to-face and talk with you and have
the kind of conversations and share the
ideas that just you know don't come up
in the sort of open loop control thing
that happens when we put information on
the Internet
today we'd like to have you come away
from this with a better sense of what
the current capabilities and limitations
are in deeper I'll tell you a little bit
about what kind of research is out there
so if you want to go and follow some
line of thinking you know what's been
done and what hasn't and we'd like you
to actually try building and running

[00:30]
algorithms for deep reinforcement
learning for possibly for the first time
and show you how to be confident in
doing that so that if you want to keep
doing it afterwards you're able to all
right so then what is deep reinforcement
learning why do we need it why do we
care about it
deep reinforcement learning is the
combination of reinforcement learning
with deep learning RL reinforcement
learning is about solving problems by
trial and error and deep learning is
about using these very powerful function
approximate errs called deep neural
networks to solve problems and deep
reinforcement learning is just
straightforwardly the combination where
we're gonna have something that's
learning by trial and error and the
thing that's getting learned is a deep
neural network that's going to make some
kind of decision or evaluate some
situation and use that ultimately to in

[00:31]
some environment make decisions that
lead to rewards where reward is just
some measure of how good or bad an
outcome was so when would you want to
use RL RL is useful when for one there's
a sequential decision making problem -
you don't know what the right thing to
do in that situation is already if you
have the optimal behavior say from
having watched human experts enough and
you have just a ton of data on exactly
what to do in every situation then you
can use the standard tools of say
supervised learning to exactly get some
machine learning system to duplicate
that behavior but when you don't have
access to that or when you suspect that
what appears to be expert human behavior
is in fact suboptimal
in that situation you may want to try
reinforcement learning instead because
it could discover
things that wouldn't have otherwise been
known and you also have to be able to
evaluate whether or not a behavior or an
outcome was good or bad this is pretty

[00:32]
critical
so RL is good when it's easier to
evaluate behaviors than to generate them
or to exactly solve for them and when
would you use deep learning
so the typical paradigm for deep
learning is that you want to approximate
some very complicated function a
function that usually requires some
amount of intelligence so for instance
if a human looks at a picture of a bird
and then knows what species of bird that
is that's a thing that you can't really
write down a simple mathematical rule to
do if you want to get a machine to do
that you have to teach it from data and
other problems that you know you would
want to do this for typically have
inputs or outputs that are very high
dimensional because it's just quite hard
to from an image or from a video stream
or from an audio stream go to a decision
rule without doing some sort of learning
in the middle and also you typically

[00:33]
want to have lots and lots of data
because getting machine learning systems
to behave in any reasonable way requires
that you give them sufficient examples
and there are tons of problems where
this is exactly what you have and in
those domains deep learning has been
very successful at exceeding whatever
was previously the state of the art from
any other methods that existed before
and creating things that are now
standard consumer products things that
were magic 10 years ago are like
completely normal now the idea that we
have super excellent image recognition
facial classification that you can talk
to your phone and it's going to know
what you said and it's not just going to
come up with some completely random
gobbledygook
this is getting better because we're
able to leverage this very powerful
technology that is deep learning for
these problems and so deep RL is when
you have some very hard high dimensional
problem where you can evaluate behaviors
and you want to get a machine to learn
how to do it because you can't write

[00:34]
down how it should in fact behave and
some very simple examples of this are
say video games we
you want to go from a computer looking
at an image of the screen so just raw
pixels to a decision rule that scores
the most possible points in the game or
behaves in a way which is cool or
interesting or exciting or perhaps a
really sophisticated strategy game like
go we're really deep thinking and
intuition and creativity is necessary to
make progress you can't write down a
simple rule for that but you can learn
it with reinforcement learning or
perhaps you want to control some complex
humanoid some some robot to run around
and do stuff
or maybe something which is a little
less silly maybe a little more real
maybe you want to get robots in a
factory to quickly learn a new task when
the robot uprising happens it's because
of this we're very sorry for this
research this was trained by the way
with an algorithm that was developed

[00:35]
here at open a I called proximal policy
optimization it's one of the algorithms
and spinning up and if you haven't had
any experience with it then we won't get
into it in this lecture today but any
other point in the afternoon during the
hackathon happy to go into detail so
before we proceed into the are L
specific stuff this is a crowd with a
pretty wide range of backgrounds and so
I just want to do a very brief recap of
some of the patterns from deep learning
what do you expect when you set up a
deep learning problem what does that
look like what do you have to think
about so we typically talk about it in
terms of the language of finding a model
that is able to give the right outputs
for certain inputs so in this case the
model is going to be some function of
the inputs and parameters and the
parameters are adjustable we control
them we change them and we want to
change them in a way that's going to

[00:36]
make the model behave according to some
design specification the way that we
provide the design specification and get
the parameters to satisfy it is by
setting up some kind of loss function
this tells you in a nutshell how good
the model is at doing the thing that you
want it to do usually some measure of
just how close the output from the model
is to the
I earn output and the critical thing
about this loss function is that it has
to be differentiable with respect to the
parameters in the model and when you
have that set up oh and of course
there's data as well so you have a bunch
of different examples of inputs and
outputs and your loss function reflects
how well your model performs across all
of them typically as just some average
overpour data point losses so with this
set up you can then proceed to find the
optimal model through gradient descent
the idea is that the gradient is a
mathematical object that tells you how
much the loss changes in response to a
change in the parameters and then you
want to knowing that change the

[00:37]
parameters in a way which is fruitful
that is it reduces the loss it reduces
the measure of error so what makes deep
learning deep what is the deep part it's
this idea that function composition is
at the core of the models that we make
and that we consider so function
composition just means that you have a
bunch of different parametrized
functions and the outputs of one are the
inputs to the next one and you can
arrange these in many different
topologies we'll call these
architectures for neural networks the
very simplest kind is just one where you
have an input layer and then there is a
matrix that multiplies that and then you
maybe add some bias to that vector and
then you pass that through a nonlinear
activation function typically this is
going to squash the outputs from that
first linear transformation into
something which maybe is in the range
from 0 to 1 or 0 to infinity something

[00:38]
relatively simple but that non-linearity
happens to do a lot of work and then
when you have successive layers what it
allows the model to do ultimately is
represent successively more complex
features internally so you might think
of the output of each layer as being a
new representation of the original input
which has maybe rearranged the
information in a way which is easier for
some kind of final decision making
procedure at the end of the network to
make the right decision based on aside
from that very simple
there are also substantially more
complex ones so the other two diagrams
on this slide are for lsdm networks so
that's in the lower left and the
transformer network that's on the right
an LS TM network is a recurrent neural
network the idea is that this is the
kind of network that can accept a time
series of inputs and produce a time
series of outputs and internally it has
some very complicated mechanisms for
making sure that information gets

[00:39]
propagated effectively across time steps
in a hidden state so that when you make
a decision somewhere in the future you
can remember something that you saw in
the past and then you can update the
network in a way which is stable and
reasonable the transformer network is
substantially more complicated and it
allows networks to do something called
attending over their various inputs so
at attention it's something which is a
concept that we can all kind of relate
to when we look at the world we don't
actually process literally every piece
of data that we take in concurrently we
particularly attend to whatever happens
to be say in the center of our field of
view or whatever we're thinking about at
the moment whatever is most urgent and
attention neural networks are able to
basically do that when they make some
decision on the basis of a lot of data
they can select out the most important
pieces of the data for making particular
kinds of decisions and that turns out to
be very helpful in practice a few other

[00:40]
things about deep learning and this is
mostly just I'm checking off some boxes
if you want depth on this I strongly
recommend that you go see the spinning
up essay where there are a bunch of
links to papers and other resources that
will give you detailed information about
this but to check off the boxes we might
talk about regularizer x' so the idea is
that sometimes optimizing your loss
function picking the model that actually
gives the lowest value of your loss
function may not be the best thing to do
you may wind up with a phenomenon called
overfitting where you've made your model
behave perfectly with respect to the
data that you showed it but then it does
a terrible job when it's given any other
data
because it learned a decision rule which
was entirely too specific but with
regularization you trade off the loss
against something which has nothing to
do with performance on the particular
task but just kind of says hey cool your
jets a little bit

[00:41]
don't be so avid about satisfying that
objective and then it turns out that
regularization actually leads to models
that do a better job of generalizing to
unseen data then there are also a couple
of things that make the optimization
process smoother and easier so you might
do some kind of normalization technique
where internally there's some output in
the middle of the network where it's
good to adjustably rescale that and
shift it around and that's better than
just letting the network do whatever it
would have done if you didn't do this
kind of normalization it's sort of
spooky and there are some legitimate
complaints inside the community about
whether or not we really understand why
this helps but it seems to so it's worth
knowing about also you might use a more
powerful optimizer than standard
gradient descent this comes up also in
reinforcement learning actually many of
the things that we've been talking about
in these past few slides show up in deep
reinforcement learning which is why I'm
bringing them up
adaptive optimizers do something special

[00:42]
in figuring out how to tune the learning
rate the amount by which you change each
parameter at each step of updating in a
way which leads to typically faster
convergence so you get to the to the
optimum point a little bit sooner or a
little bit easier there's also the
Reaper amortization trick but that's
quite complicated and so we won't
actually talk about it it's on the slide
so that you know where to look all right
that's all this stuff from deep learning
that I wanted to talk about
now onto reinforcement learning so first
and foremost we have to talk about how
do you formulate a reinforcement
learning problem what does that mean
what does that do what are the pieces of
it how do they fit together we typically
use the language of saying that there's
an agent that interacts with an
environment so the agent is whatever
thing is making some kind of decision
the environment is wherever those
decisions are happening and the thing
that creates the consequences of those

[00:43]
decisions
and there's this loop where the
environment has some state and has some
measure of how good it is to be in that
state that's a reward and the agent gets
to observe the state and possibly the
reward it uses the reward for learning
whether or not it observes it as a
subtle technical detail but anyway
okay the agent gets a state observation
and a reward and then the agent makes
some kind of decision about what action
to take it picks the action and it
executes sit in the environment and then
the state of the environment changes
there's a new state of the environment
the agent perceives it the agent acts
etc the goal of the agent is to figure
out what decisions will maximize the sum
total of rewards that it'll ever get
actually it's slightly more specific
than this and there are a couple of
different formulations that we can
choose and we'll talk about them
momentarily but that's basically it in a
nutshell we want to maximize this sum of
rewards that we get and the agent is
going to figure out how to attain that

[00:44]
goal through trial and error so you just
don't know in advance what the right
thing to do is so you have to just try
things see what happens see how much
reward you get and then adjust your
decision on the basis of that so
reinforcement learning is about
algorithms for doing precisely that but
before we can talk about the algorithms
we have to introduce a bunch of
terminology for those of you who have
done the work of going through the
spinning up material online this will
probably be quite familiar and I'm
mostly going through it for the benefit
of the audience that I expect might
watch this in the future as a starting
point for this so bear with me I'll try
to go through this reasonably quickly
but we have to talk about observations
and actions policies trajectories
rewards and returns what the RL
optimization problem actually is how we
formalize it and then value in action
value functions and also advantage
functions so there's a whole lot of
stuff that you kind of have to know and
unpack in order to really fruitfully

[00:45]
progress and reinforcement learning and
and these are just those central pieces
so observations and actions a state is
something which tells you absolutely
everything about the environment
the agent usually doesn't get access to
the state there is usually some stuff
that's just hidden from the agent so
what the agent perceives is called an
observation if the observation contains
all the information in a state we called
this environment fully observed if it
doesn't we call it partially observed
and states observations and actions can
be continuous or discrete for all of the
problems that we care about in deep RL
the observations are continuous and the
actions might be discrete or continuous
a policy is a rule for selecting actions
there are a couple of different ways
that you can get to this kind of rule
we typically classify them as one of two
kinds stochastic or deterministic a
stochastic policy is a rule for randomly
selecting an action on the basis of the
most recent observation or possibly

[00:46]
preceding observations as well a
deterministic policy is just a map
directly from observation to action and
no randomness involved at all you may be
wondering why it would be useful to have
a random policy at all because it might
seem like randomness is just sort of
dangerous but actually it can be quite
helpful and there are some very
principled ways of optimizing stochastic
policies and it's a little bit harder to
optimize completely deterministic
policies there may also be a matter of
robustness in that having a little bit
of randomness can make you more robust
sometimes to perturbation then having
learned a brittle specific deterministic
policy so now just to give some sort of
concrete examples in tensorflow
because I assume that most of you will
probably have met tensorflow as your
first deep learning library and if not
pi torch and for those of you who are
stuck with tensorflow I'm so sorry you
probably should have picked pi torch I
know I should have but but here we are

[00:47]
so in in tensorflow for a stochastic
policy over discrete actions we might
first set up a placeholder for loading
in observations and then we might set up
a multi-layer perceptron network and MLP
network so this is just the most basic
kind of feed-forward neural network the
thing that I talked about earlier which
is a succession of linear transforms of
inputs followed by nonlinear transforms
of inputs
in this case the linear transforms take
you to something of size 64 and there
are two of them and then the activation
is at an H activation so this gets you
to a range of minus one to one in a nice
smooth way and and then we produce
logits based on the output from that
piece of the network so logits are
basically something that proceeds having
probabilities for particular actions if
you take the softmax of the logit that's
not a function you're familiar with I
recommend looking it up it's just

[00:48]
something that exponentiate Sall the
logits and then divides by the sum of of
those exponentiated logins so so it
normalizes the distribution to to being
a probability distribution all the
entries have to be greater than zero and
sum up to 1 so we get logits and then we
get actions by using TF multinomial to
sample something stochastically assuming
that the probabilities are based on
taking the softmax of those logits you
can ignore the squeeze that's just there
for making sure that certain things
actually work and then in the
deterministic policy let's say we have a
continuous action case so we want to
output a vector of actions where each
entry can be any real value number we
will just go from observation to network
to a final layer which is just going to
be the actions all right so that's
policies let's talk about a trajectory a
trajectory is a complete sequence of
states and actions through the history
of an environment the agent starts in a
state takes an action then there's a

[00:49]
next state next action etc the first
state in the environment is sampled from
some previous distribution over starting
States and then afterwards state
transitions are going to be either
deterministic or stochastic but there's
just some rule in the environment that
given the current state and the current
action whatever action the agent took
picks what the next state is a
trajectory is also sometimes called an
episode or a rollout you'll see this
terminology used completely
interchangeably so just be aware that's
out there there's I'm so sorry in every
new ish field a lot of terminology
confusion we're different people in
different
areas of academia worked on it for a
while and use different terms and then
in the end we're left with just a weird
mishmash notation - you're gonna see
some notation where states and actions
are notated by s and a and then in code
you'll see some places where it's X and
u and this is because of the ancient

[00:50]
eternal conflict between the control
theorists and the reinforcement learning
theorists and we're just stuck with it
now so that aside let's talk about
rewards and returns so a reward function
is going to map from the states and
actions or states and actions and
possibly next States on to just some
number that tells you good or bad
positive is good negative is bad the
more positive the better and you have to
if you're a designer setting up a
reinforcement learning problem you have
to pick with that reward function is
going to be so you want to make sure
that you incentivize the stuff that you
want to have happen and disincentivize
stuff that you don't want to have happen
so as a very simple example suppose that
you want a robot to run forward but you
don't want it to waste a ton of energy
so maybe you will give it a reward
proportional to its forward velocity but
you'll penalize it proportionally to the
some of the action magnet or to the
action magnitude so you'll discourage

[00:51]
superfluous actions the return of a
trajectory is going to be some
cumulative reward along it we have two
ways of formulating this and what you're
going to find in deep reinforcement
learning implementations is that we're
going to completely conflate which
problem we're trying to solve with the
other but the finite horizon
undiscounted sum of rewards works when
you have a finite horizon it doesn't
work when you have an infinite horizon
because if you have an infinite sum of
things it might diverge unless you do
some kind of discounting so in this
other case infinite horizon discounted
some of returns you have a discount
factor gamma between 0 & 1 and that's
how you down weight things that happen
in the future this makes sure that this
is a reasonably well-defined quantity
but why would it make sense to discount
things you probably would rather someone
tell you that they're gonna give you
$100 today than $100 in a hundred years
right like it's just good to get
upfront then there's the reward to go
this is closely related it's basically

[00:52]
just a measure of return starting from a
particular time step or state so the
reward to go from some point in time is
just the sum of rewards that'll happen
after that point in time and now we can
talk about the reinforcement learning
problem just formally we're going to set
up a performance measure for a
particular policy PI J of Pi which is
the expected value of return for
whichever formulation we've picked
according to a distribution over
trajectories in the environment based on
the choice of policy so what that means
is that again start states come from a
starting distribution transitions in the
environment are based on something in
the environment that transition
distribution P and actions will come
from the policy conditioned on the the
observations of the states and we want
to find the optimal policy PI star which
maximizes this now we have to talk about
value functions so value functions are
measures of how much reward you expect
to get from a particular State or state

[00:53]
action pair assuming that you're going
to behave a certain way so we have the
on policy value function and action
value function V PI and Q PI which
respectively tell you how good it is to
be in a particular state and how good it
is to be in a particular state action
pair assuming that forever after being
in those places you act according to the
policy PI and then there's also V star
and Q star same thing except if you were
to act according to the optimal policy
it's great to know Q star as we'll talk
about momentarily value and action value
functions are connected the value is
just the expected action value expecting
over what option you might take
according to the current policy and the
advantage function tells you how much
better a given action is than average
and it's just the difference between Q
and V these value functions satisfy
recursive bellman equations these are
super important and they're the
foundation of a bunch of algorithms so
they're really worth knowing and kind of
just worth grappling with I think that
these can be particularly tricky at

[00:54]
first I remember the first time that I
met reinforcement learning I was just so
turned around and lost by these the
notion that there was going to be this
recursive equation where the definition
of a thing depended on itself was quite
confusing but it's it's it's worth just
hitting your head on for a while until
it makes sense but what it's saying is
that the value of being in a particular
place is going to be as good as whatever
reward you get for being in that place
plus all the rewards that you'll ever
get for all the places you'll go
afterwards now why is it great to know Q
star Q star tells you if you're gonna
act according to the optimal policy
forever after you started in this state
and took this action and we don't care
what policy this action came from how
well will you do so that means that if
you want to do the best you possibly can
do all you need to know is what action
maximizes Q star in a particular state
and then take that action because that's
gonna be the best action in that state

[00:55]
and then afterwards you've assumed that
you're gonna do the best that you can
ever possibly do so if you have Q star
you basically have the optimal policy so
this is going to lead us ultimately to
the two different kinds of algorithms
and reinforcement learning for control
where in one case we'll try to directly
optimize a policy and in the other case
we'll try to find Q star now if we want
to find Q star we have to set up a
function approximator for it q theta
which will represent by some kind of
deep neural network and we're gonna want
to measure how good is it at
approximating Q star and this is what
that recursive bellman equation is gonna
be really helpful for because the
beautiful thing is we don't need to have
acted according to the optimal policy to
check how well Q theta fits that bellman
equation we just need a bunch of
examples of state action next state and
reward tuples and if we have enough of
those over enough of the environment
then we can probably do a pretty good

[00:56]
job of fitting q theta based on that
bellman equation based on maybe this
means squared bellman error and then use
that afterwards for control which is
having a decision-making rule by the way
I apologize if anything has been
confusing about my using sort of the
terminology of control interchangeably
with the terminology of reinforcement
learning when I say control I mean
having the best
policy so now what kinds of RL
algorithms are out there behold a
taxonomy which is much more restrictive
than it looks it looks very pretty and
it looks very definitive but it's
actually masking a lot of subtlety and
you know detailed choices and the fact
that there's actually a lot more bleed
over between these things than you might
expect
but at a very high level this is a
useful picture to start with that we
have two different kinds of RL
algorithms ones where we have access to
the model of the environment and ones
where we don't so what that means a
model of the environment is something

[00:57]
which tells us if we're in a given state
and we take a particular action what's
gonna happen next the model would
predict what the state of the
environment will be after that and
that's really useful because if we can
forward simulate the environment then
that's extremely helpful for evaluating
our current policy it's extremely
helpful for figuring out what a better
action would be than the one that we
might want to take so if you don't have
a model you're quite limited you just
have to figure out how to do well based
on experiences that you've seen your
direct interactions of the environment
you don't get any other information but
if you do have a model it's quite
potentially powerful although as we'll
discuss the methods for model-based
reinforcement learning are not quite as
mature so far as the methods for model
free reinforcement learning so now okay
that last slide was just a ton of
acronyms maybe not that insightful let's
talk about what these algorithms are
doing there are three key pieces in any
reinforcement learning algorithm for one

[00:58]
you're going to run the policy in the
environment you're going to actually try
things and get to some signal error or
otherwise and then you're going to have
to reflect and evaluate whether or not
those decisions were good ones whether
or not those actions were the right ones
you have to figure out how good your
current policy is so that you can use
that information to improve it so you
run the policy you evaluate the policy
you improve the policy and there are a
bunch of different ways of doing that
and we'll go into some depth about how
different algorithms go about doing that
so let's start with policy optimization
minor interlude in the chat last night I
surveyed people to see what they were
interested in
I asked if people were interested in
math there's gonna be some math so first
at a very high level zooming out ten

[00:59]
thousand foot view in policy
optimization we're going to run the
policy by collecting complete
trajectories or snippets of trajectories
based on our current stochastic policy
and we're going to explicitly represent
that stochastic policy with a neural
network that perhaps gives these
sufficient statistics of the action
distribution or something else that we
can use to derive that and sample from
it and then we're going to evaluate the
policy by figuring out the on policy
value function and advantage function
and we're going to evaluate those things
for all the states and actions in the
trajectories that we sampled and then
we're going to improve the policy by
making it more likely that we take the
actions that led to higher advantage and
making it less likely that we take the
actions that led to lower advantage less
likely that we take the bad actions how
do we do that we're going to have to

[01:00]
talk about some math now I realize
there's a chance that most of you maybe
weren't expecting that we would be doing
any kind of deep mathematical excursion
but if there's one thing that I want you
to take away from today aside from just
being excited about deep RL it's a
realization that there are some
limitations to what deep RL can
currently do and that this is not really
a hundred percent done as a technology
where you can just apply it to a problem
without really thinking about what it's
doing under the hood and get a good
solution it's not a black box technology
yet so if you want to try deep RL on a
problem and grapple with getting it to
work you do have to kind of understand
what's going on under the hood and that
means taking a look at some of the gory
mathematical details understanding how
they connect and forming an intuition
for how those details will shape the
failure
most of your algorithm so what we'll
talk about we're just gonna talk about
vanilla policy gradient we're gonna talk
about how you derive the policy gradient

[01:01]
and a bunch of different equivalent
expressions for it and then we'll get to
the pseudocode for the sort of standard
version of vanilla policy gradient which
includes maybe a few more tricks and
details than the very most basic vanilla
version apologies for the choice of
words there but all of this stuff is
critical to understanding more advanced
policy optimization algorithms like Terp
oh and PPO we won't be covering them in
these slides but again happy to talk
about them offline during the hackathon
so in policy grading algorithms what we
want to do is we want to find some kind
of expression for the gradient of the
policy performance with respect to the
parameters of the policy and we want to
just directly gradient to send on those
parameters so we're going to move the
parameters in the direction that
increases performance and is this gonna
be easy or hard well if we just try
putting the gradient onto the policy

[01:02]
performance we run into a problem all
the parameters are down here in the
distribution they're not inside here
where we would like them if we want to
get something that we can actually use
we'll have to do some messy work to
bring the gradient inside of an
expectation which we could then form a
sample estimate of so step one to
getting the gradient symbol somewhere
helpful we're going to recognize that
this expectation can be rewritten as an
integral going through all of the events
in trajectory space every possible
trajectory of the density the
probability mass or density for that
trajectory based on that policy times
the return that you would get for being
on that trajectory and now we can bring
the gradient in because the limits of
this integral don't have anything to do
with the parameters and then we apply
the log derivative trick so this is a
really helpful mathematical trick comes
up all over the place and deep
reinforcement learning it's basically
just this notion that the derivative of
log of sum

[01:03]
thing is one over that something times
the derivative of that something and we
rearrange it slightly but it lets us go
from the gradient with respect to theta
of P to P times gradient log P this is
great because now we have an expectation
again we have an expectation based on
trajectories sampled according to the
current policy so if we have that data
we can make a sample estimate certainly
so the very nice thing here is that what
we did after bringing the gradient
inside the integral and doing this log
derivative trick is that we now have
something which is an expectation again
because we're integrating through all
possible trajectories of the probability
density associated to that trajectory
times something which is a function of
that trajectory so this is an
expectation and we can form a sample
estimate of it that we can use in a
practical algorithm but we're not
completely finished yet because we still
have to talk about what's the gradient
of that log probability for a trajectory

[01:04]
how does that depend on the parameters
of the policy so let's go back to the
picture that we had in the beginning
there's a starting state which is drawn
from some distribution based on the
environment and then after that you pick
it the agent picks in action based on PI
theta and it has probability PI theta a
given s for time step 0 then the
environment picks the next state
according to whatever distribution it
has over next States given your most
recent action in the most recent state
by the way this is something that I lost
over earlier slightly more formalism
details that you don't quite need to
know but this is called the Markov
property this notion that picking the
next state only depends on the most
recent thing that happened and doesn't
depend on the past before it that's the
the Markov property and you'll find a
whole bunch of math if you go digging
for it but you don't have to for for
this at the very least so then what we
have is that the probability of the

[01:05]
trajectory is going to be just the
probability of that first state x the
probabilities of each transition and
action selection that happens afterwards
so we get that expression up there at
the top and now if we want to take its
gradient of its log we just
pretty straightforwardly compute first
the log of that thing turns that product
into a bunch of sums the gradient goes
through the sums and now all the terms
that are based on distributions from the
environment have no dependence on the
parameters of the policy the environment
doesn't care what the policy is it's
just going to behave in whatever way it
does so those have no dependence on the
parameters those derivatives are zero
and what we're left with is just
something which is as some overtime
steps of gradients of the policy and the
beautiful thing is because we control
the policy and we have explicitly
represented it as a neural network and
we can compute all of its gradients this
is a thing that we can calculate so now

[01:06]
we're at something where we can in fact
calculate a sample estimate of this
gradient of policy performance and use
that as the basis for a gradient ascent
algorithm for improving performance but
it's not good enough we're not done yet
yes the function capital e so so this
this capital e is an expectation and if
we want to form an estimate for the
expectation so we're not going to
compute the expectation exactly what
we're going to do is we're going to see
what happens for a bunch of different
trajectories that are sampled according
to the distribution specified in that
expectation and then we're just going to
average them and in the limit as we have
an infinite amount of data that sample
average becomes exactly equal to the
expectation yes

[01:07]
absolutely absolutely you can so it is a
bunch of derivatives of the final output
with respect to each one of the
parameters right because there are many
inputs to this function and we're going
to have a derivative with respect to all
of them yes I'm sorry can you repeat the
question yes can we tie this explicitly
to reward so inside the expectation here
we have R of tau so that's the return
measure that we've chosen whichever one
we picked either the infinite horizon
discounted sum of rewards along the
trajectory tau or just the finite
horizon undiscounted sum of rewards so
that R of tau is the sum of all the
rewards in a particular trajectory and
that's actually why the the variance of
this is going to be so unnecessarily
high they're going to be a bunch of

[01:08]
terms in this sample expression actually
just in that expectation which which
have expectation zero on average they're
zero they don't contribute anything but
we sample them anyway and the samples
will have noise on them and so we'll
just wind up getting the noise we won't
get much signal from them so can we
eliminate a whole bunch of terms yes we
absolutely can the intuition here is
that if I give you a reward in the past
and you want to update the action that
you just took really what you care about
for figuring out whether or not the
action that you just took was good or
bad are the consequences of that action
you don't care about what preceded it
that action and what preceded it are
almost completely uncorrelated there
you're not going to to get anything by
by updating the likelihood of that
action based on an old reward so that in

[01:09]
expectation is going to be zero and
knowing that we can now expand out this
return measure and we're going to
get this in the finite horizon case just
for simplicity but this analysis also
extends to the infinite horizon case so
we now have a sum of grad log probs of
the policy times the sum of rewards
we're gonna pull the sums out of this
expression so that we can just look at a
policy update at a particular time step
times a reward from a different time
step and then based on that thing that
we asserted above we're gonna drop all
the terms that are inconsequential all
of those are zero and so what we're left
with after we take away all the ones
where T greater than T Prime we're left
with this sum sum over the time steps
for the policy times a sum over time
steps for rewards that goes for all of
the time steps after the corresponding

[01:10]
policy time step and then if we bring
that back in what we're seeing now is
that we want to for each time step
adjust the probability of the action
from that time step in proportion to the
sum of rewards that came afterwards only
the consequences of an action will
affect its update yes so it's not that
you don't consider past actions the sum
over here in the beginning runs over all
time steps so every action is going to
get to some update it's just a matter of
which rewards are used in figuring out
the update for that action and it should
only be the ones that were consequences
of it yes yes
um well we do care about the future
right because here we have a sum of

[01:11]
rewards after a particular time step all
the rewards in the future from that time
step so so that expectation that's just
saying that an action that happens later
shouldn't be affected by a reward that
happened before it it should only only
be affected by the rewards that happen
afterwards so in the in the next slide
actually we'll see how this expression
that we have down here at the bottom
connects to the value functions so what
we currently have is what I'll call the
reward to go policy gradient because
what we're doing is we're adjusting the
probabilities of action proportionally
to the reward to go what we're going to
do now is go from that into an
expression that has q pi the action

[01:12]
value on policy for a state action pair
instead of that reward to go and this
works because you can break up the
expectation so first we're gonna pull
the sum over time steps out of this and
then this expectation over trajectories
this is sort of subtle and and maybe a
little math here then we can go into
detail on here but I recommend that you
go look on the spinning up website in RL
intro part 3 there's a link separately
to a proof about this but if we think
about the average thing that's going to
happen over all trajectories that's
going to be equivalent to the average
thing that happens over all of the cases
of something with the first T time steps
of the trajectory we're inside of the
expectation we've moved all the stuff
that happens in the future
and we were able to move it inside past
this one because this only depends on

[01:13]
time step T this doesn't depend on stuff
after T so only this
it's gonna be affected by averaging over
the future and then it turns out that
that expression the average sum of
rewards that you get starting from a
time step assuming that the state and
action for that time step were fixed
that's exactly equal to the action value
that's exactly saying how good is it to
be in a particular state take a
particular action and then forever after
act according to a particular policy and
now we have this expression for the
policy gradient at the bottom we're most
of the way through the math okay but
what is a baseline a baseline is a
really important thing because it's
another tool in our Arsenal for taking a
policy gradient expression and turning

[01:14]
it into something which is lower
variance more likely to be useful for
producing a good update to the policy
and it's also the namesake for opening
eye baselines
well let's save one of them it's a
couple of things but we have a
expression here at the top which I claim
is basically true which is that the
gradient policy gradient is the thing
that we had before but instead of Q we
subtract out some function of state some
function b of st and i claim that in
expectation it works out exactly the
same and so there's a short proof here
for that which is that if we look at the
expectation for that part of it what
happens if you take the expected
gradient of the log probability of an
action in a state times some function b
of st the b doesn't have anything to do
with the action so it's a constant with

[01:15]
respect to this expectation so we pull
it out and then what we're left with is
an expectation over actions which will
rewrite and now we have it in
probability times grad log prop we're
going to reverse the log derivative
trick from earlier so this is now an
integral over actions of the gradient of
the probability of that action and we
can pull out the gradients
we're just sort of reversing the
procedure from earlier this thing this
integral over all possible actions of
the probabilities of those actions
that's just going to sum up to one
that's just saying probability
distribution is normalized all of the
chances together have to come out to
equaling 100% of sum them up and the
derivative of a constant since that's a
constant is nothing constant has no rate
of change
so we get zero so all of the terms of
grad log prob times the baseline in
expectation or zero so we're free to add
this baseline without changing what the

[01:16]
policy gradient is in expectation but we
can pick it in ways that are fruitful
and make the estimate better so the
typical thing to do is to pick the
baseline to be the value function and
this leads us to kind of our our final
sort of ultimate form of the policy
gradient the form with advantage
functions and why is this good why is
this good the advantage function says
how much better in action is than
average why would you prefer that over
just how good the action is well let's
say you have two actions one gets you a
hundred dollars one gets you one hundred
and one dollars you only sample the one
that gets you one hundred now when
you're trying to update your policy you
can feel really great about that oh man
100 is a big number I feel great
I'm gonna double down on that action
you're acting sub-optimally if you had
been picking 5050 on average you would
have gotten a hundred dollars and fifty
cents and you would have realized that
the advantage of taking the action that
you picked one hundred dollars and fifty
minus a hundred dollars and fifty cents

[01:17]
you lost fifty cents should pick the
other action so you prefer to use
advantages to figure out which actions
to increase the likelihood of as opposed
to just Q values all right summing it up
we have these four different forms of
the policy gradient they're all tightly
connected we care about the last one but
to get to the last one we had to go
through the pain but now that we've all
gone through that pain together you're
stronger you can go and you can
implement this and it'll work and you'll
know why it works and you'll feel good
about that and if it breaks you can fix
it
all right so then just to sum it up this
key concept we want to push up the
probabilities of good actions push down
the probabilities of bad ones and also
importantly that expectation requires
trajectories sampled from the current
policy so this is the concept of being
on policy and reinforcement learning
that if you want to update your policy
you have to use data from that policy

[01:18]
you can't use data from some other
policy unless you appropriately
reweighed it but relating data is
complicated and really tricky so it's
sort of preferred to not do it unless
you are trying to build something new
and cool and super sample efficient and
you're willing to spend a lot of time
and effort doing research on making sure
that it actually works but ok so the
policy gradient expression gives us the
policy improvement step coming back
coming back a bit oh yeah sure the
question was how do we know what the
average reward would have been so that
we could figure out how to make the
advantage function in the first place do
we compute it as we go and and actually
that's exactly what the next slide is
about which is how do we do that

[01:19]
business of policy evaluation how do we
find an estimate of the advantage
function which is actually good and
reasonable if we just have a bunch of
data where do we get the value function
that we might use to subtract out as a
baseline and the idea here is that we're
going to learn it from data and
typically it's going to be by regression
so this will be a subroutine that you'll
find in most policy optimization
algorithms where you're going to have a
value function approximator another
neural network and you're going to at
each epoch of the policy optimization
algorithm update the value network to
try to match the empirical returns that
you saw so for a particular state the
value should be more or less the sum of
discounted rewards that you saw off to
then
and then when you have the value
function approximator you can use that
to estimate advantages and we'll talk a
bit about estimating advantages from
value function approximate us on the

[01:20]
next slide but first you may have
noticed that I pulled a fast one on you
which is that we went from in all the
preceding slides dealing with the finite
horizon undiscounted case and then here
in our optimization problem for learning
the value function I've dropped in
discount factors why is that the answer
is because everyone does it this is
where there's not a particularly good
reason in my opinion that this happens
but pretty much every policy
optimization algorithm that I'm aware of
every every single implementation uses
discounted value functions and advantage
functions but then treats the policy
optimization part as undiscounted it
creates some bias it seems to work
shrug it's perfectly reasonable to do
that so it sometimes seems to be helpful
to set the discount factor to something
a little smaller than one so keeping it
completely undiscounted would be gamma
equals 1 for whatever reason with some

[01:21]
optimization problems there's some some
RL problems it's a little bit harder if
you pick gamma equals 1 than gamma 0.95
and i can't say that there's a
particularly good reason for this I
would speculate that like in the
beginning of training if you pick a very
high discount factor those empirical
returns will be very noisy and if you
choose a discount factor less than 1
what you're going to do is you're going
to attenuate some of the noise you'll
bias that sum of rewards so that
whatever happens soonest matters most
and if you happen to see a few positive
rewards in a row then you'll latch on to
that whereas maybe because of noise if
you had really paid attention to
everything out to infinity you'd have
just gotten a bunch of positives and
negatives and positives and negative and
they would have cancelled out uh I think
it's it's ok to think about it like that
yeah

[01:22]
yes yes that after a certain point the
trajectory just ends you get it to time
step T and then it's over
that's finite horizon infinite horizon
you go out to infinity alright so then
how do we calculate the advantage
function given data from trajectories
and a value function approximator so a
thing that I want to introduce here is
this notion of n step advantage
estimates so what you're going to do is
you're going to have a thing over on the
left side that approximates Q pi and a
thing over on the right side that
approximates V PI so this thing for Q pi
remember that that's supposed to be an
estimate for how well you'll ever do if
you start in a state take an action and
then act according to the policy forever
after you can just use the empirical
return the reward to go from that state
as a sample estimate of the expected
value which is the Q value but in an N
step advantage estimate what we're going

[01:23]
to do is we're not going to go all the
way out to the end of the trajectory in
that sample estimate for Q we're going
to go n steps in and then use the value
function approximator to assume what's
going to happen for the rest of it and
this corresponds to a decision about how
much bias or variance we find acceptable
in this advantage estimator so if you
pick n equals 0 then your advantage
estimator in that case would be just the
reward plus gamma times the value
function approximator for the next time
step minus the value function
approximator for the current time step
and that's gonna be very high bias
because whatever is wrong with your
value function is not going to be wrong
with your advantage function but it'll
be really low variance because the only
thing that's going to have variance to
it is the reward and the stochasticity
in the next state transition but if on
the other hand you pick n equals
infinity so for the q approximator you
just take the exact sum of rewards that

[01:24]
you got in the real trajectory and then
at the end you subtract out the value
function at st you're going to accept
all of the variance that's in the
environment
but the nice thing is you don't have
bias in forming your policy gradient
estimator with this because in
expectation the Q part is going to be
exactly Q in expectation and the B part
recall that that was a baseline that we
added with a guarantee of no bias in the
policy gradient so on expectation that
part falls out and it's fine
so the bias-variance tradeoff is
typically mitigated through what we call
generalized advantage estimation so this
is a way of interpolating between all of
those different possible choices of n
step advantage estimate where we use a
factor called lambda so this is sort of
like another discount factor as the
interpolation variable and it's a hyper
parameter and you choose it in each

[01:25]
implementation that you make and it's
generally good to set it somewhere
between like 0.9 and 97 usually it's a
set it and forget it in my experience I
can I can't think of very many cases
when I saw a substantial difference in
algorithm performance from adjusting it
beyond that kind of narrow range if you
set it equal to one then you'll get
exactly the case of the N equals
infinity and if you set it to zero then
you'll get exactly the N equals zero
case so it's good to kind of leave it in
the range where it's putting a little
bit more weight on the real empirical
returns than the biased value estimator
but not all the way to the extreme okay
at long last I give you the pseudocode
for the full vanilla policy gradient
algorithm that incorporates everything
that we've talked about so far what
we're going to do is collect a set of
trajectories by running the current
policy in the environment and then we'll
compute the rewards to go so that we can
use them as targets for the value

[01:26]
function approximator will compute the
advantage function estimates with any
method of advantage estimation but
typically generalized advantage
estimation and then we're gonna use
those to estimate the policy gradient
with that we take a step of gradient
this gradient descent we might use an
adaptive optimizer like Adam to
accelerate the rate at which we learn
and then we're going to do the
supervised learning problem of trying to
get the value function approximator to
match the empirical returns and that's
how we learn our value function and then
we loop that's vanilla policy gradient
yeah absolutely
so yes usually you will pick networks
have the same size for policy and value
function in cases where the environment
is partially observed you may want to
have a single core recurrent neural

[01:27]
network that's going to be able to
remember past information and then give
that corner all Network separate outputs
for policy and value function and then
you'll train that jointly and it gets a
little bit complicated because I can't
say that there's any good work in RL
theory that I'm aware of that reasons
about how it alters performance for the
final policy to be simultaneously
optimizing with respect to both
objectives on the same model but that's
what you would do in that situation so
so yes typically they'll be about the
same size unless they're actually
sharing parameters and then they're sort
of the same model yes
does the choice of initial policy affect
convergence wonderful question and sadly
in a lot of cases yeah so this is part
of what goes into my saying that deep
reinforcement learning is not a
technology that's ready to be used as a

[01:28]
black box yet so when we do experiments
in deep reinforcement learning we
typically run the same exact experiment
with different choices of new of seed
for the random number generators and
what we find is that the seed which in
the beginning of the algorithm only
changes the initialization of the
policies and value functions happens to
matter quite significantly some seeds
learn some seeds don't some seeds learn
much slowly much more slowly than others
and there's no particularly good reason
for it
we are generally quite heartened when we
find an algorithm that appears to be
robust to initial conditions and where
the
average of the learning curves is quite
narrow we think that's great and it
doesn't quite happen as often as we
would hope all right do we have any
other questions about policy gradients
so in the bottom right hand corner there
that says 47 out of 63 I may have
slightly miscalibrated

[01:29]
how long parts one and Part two were
relative to the initial time slots of 45
minutes and 1 hour respectively this is
by far the longer one but since we've
been at it for an hour I think this is a
good point to take a 15-minute break and
we'll pick back up to discuss q-learning
after coffee thank you so much

[01:46]
we will be resuming with Joshua Humes

[01:47]
introduction to RL in two minutes

[01:48]
hello
hi everyone we're about to get started
for the second part of intro to RL and
just as a heads up
I prepared entirely too many slides for
the hour and 45 minutes that I was
scheduled to speak please bear with that

[01:49]
because you know this is the first time
we're doing this and so I'm still
getting calibrated on what we can get
through in that amount of time but
everything that I don't cover by 11 a.m.
when I hand over the mic to the next
speaker I'm more than happy to share
with you later today during the
hackathon so in particular the material
that I expect that we won't quite get to
will involve an overview of what's been
accomplished recently in deep
reinforcement learning and where the
challenges and limitations are and what
the research horizons look like on those
limitations but before we do any of that
let's continue our discussion from
earlier and talk about the next major
family for algorithms for deep RL for
control which is to say cue learning so
there are a lot of algorithms that fall
under this umbrella deep Q learning was
one of the first algorithms that really
made deep reinforcement learning viable
and popular speaking from personal
experience I just started my graduate

[01:50]
student career in 2014 when I heard
about the playing Atari with deep
reinforcement learning paper I was just
becoming aware of topics in AI and AI
research and that completely and totally
blew my mind it was the most exciting
thing that I had ever seen that a
computer could just figure out from
looking at what was happening on a
screen how to behave how to play a game
how to do something that I thought
required some human spark of
understanding and capability for joy and
the in the computer had it it was
beautiful and amazing and it made me
want to study this and participate in
taking this technology all the way from
where it was at that point to what it
could be in the future
anyway q-learning
so back to this RL loop that we have run
policy evaluate policy improve policy in

[01:51]
q-learning you run the policy by taking
a step in the environment either
randomly so there's going to be some
stochasticity in what you do or you're
going to act in a way which is called
greedy with respect to your current Q
function approximator so remember what
you're trying to learn is Q star the
optimal action value function and if you
happen to have Q star then whatever
action is the maximum or maximizes q
theta in a particular state is the best
action to take um but when you don't in
fact have q theta equals Q star then the
the maximizing action probably isn't
great so exploring a little bit by
acting randomly is going to help you and
then once you've taken that step in the
environment so you send an action to it
and you get back a reward in the next
state you store that transition state
action reward next state in a replay

[01:52]
buffer you save it for later because
you're going to use it for learning how
to evaluate the policy which is to say
updating q theta to try to have it fit
that bellman equation and once you have
that the policy improvement step is just
looking into q theta and saying what's
the action that maximizes this policy
improvement is basically implicit in Q
learning and we're gonna structure our
discussion about Q learning around the
original deep Q networks algorithm but
pretty much everything in this
discussion is quite general for Q
learning methods because they all kind
of share this common DNA of you take a
step in the environment you take some
gradient descent steps on your Q
function to minimize a mean squared
bellman error and you use the techniques
that will describe in a minute
experience replay on target networks to
stabilize the learning procedure so Q
learning updates by bootstrapping so

[01:53]
what is what is that it's this notion of
how
are we actually going to fit q2 that
bellman equation so we talked about
minimizing mean squared bellman error
and it's a useful picture to start with
and so I'm gonna keep using that
terminology although in a few slides I'm
going to tell you something completely
different and ask you to ignore this and
pretend you never heard it but this is
where all the papers start and this is
where all the tutorials starts so it's
good to familiarize you what you're
going to do to update Q is set up this
loss function where you're going to
average or sum over data from your
replay buffer D and you're gonna have
these transitions state action next
state reward and you're going to regress
Q theta against targets Y where those
Y's are obtained basically from that
bellman back up from that bellman
equation as the reward plus the Q value

[01:54]
in the next time step and this is based
on the bellman equation for the optimal
action value function so it's gonna have
that Max over next actions which is to
say that it's going to assume that you
know if Q theta was optimal if it was Q
star then whichever action maximized it
in that state would be the best one to
take and that would be the best value
there so interestingly you don't
propagate gradients through why even
though why has the dependence on the
parameters of Q theta and the reasons
for this are kind of mathy so we'll get
to them in a bit okay
getting this to work so there are two
main techniques that I mentioned there's
experienced replaying there's target
networks
the idea behind experience replay is
just that you want to use a really wide
distribution of data for training your Q
function you don't want to fit it really
well to a very narrow region of
transition space because if you do it's
not gonna be good anywhere else and if

[01:55]
it's not good anywhere else you're not
going to be able to bootstrap it to the
correct values even in the places where
you've been trying to fit it
you'll get nothing which is actually
useful for control so experience replay
helps you broaden that data distribution
fit q well everywhere gets something
which is good for control target
networks
so bootstrapping with function
approximator is super super super
unstable that thing that we said on the
previous slide where the Y's depend
exactly on the current Thetas actually
throw that out can't do that that won't
work
if you try to do it what's gonna happen
is typically the keys will explode
they'll go to something really large or
really negative and that'll happen
really fast you won't be able to control
it even with reasonably well tuned
learning rates you probably won't be
able to stop it so instead what we're
gonna do is we're gonna have target
network Q theta Targ and we're gonna
make sure that that network tracks
reasonably closely to Q theta but
there's going to be a lag so that it

[01:56]
updates more slowly so that if you make
an update to Q theta which pushes a Q
value too high or a little too low then
that doesn't immediately propagate into
Q theta Targ and therefore does not
propagate into the bootstrap so this is
this wide thing we're gonna call this
the bootstrap and then this tamps down
on instability grants it why if Q
learning is so horrific ly unstable
would we want to do it like this in the
first place why wouldn't we just
differentiate through with respect to
that bootstrap and the answer is it if
you differentiate all the way through it
tends to not work that well and the
reason that this thing does the reason
that it works well if you do this kind
of bootstrapping approach as long as you
take some appropriate precautions has
something to do with the theory
underlying Q learning and we'll talk
about that in a few slides but not quite
yet you're spared for now so also

[01:57]
another note in DQ networks the
particular algorithm that we're talking
about right now
action space matters a lot so what we
did in describing that bootstrap we had
a maximization over actions of the q
function if you have a q function that
accepts as input a continuous state and
a continuous action and feeds that into
a deep neural network trying to figure
out the action that maximizes the Q
function output is really hard that
would be a non-trivial optimization
problem an expensive subroutine so if we
want to be able to
get that max over actions that's a case
where we won't really be able to do it
so dq1 will apply specifically to the
discrete action case where we're able to
use a network architecture that instead
of taking a continuous action as an
input at the bottom of the network emits
action values for each possible output
for each possible action at the end of
the network so a single observation goes
in and then K action values come out

[01:58]
where K is the number of actions one for
each action and then because there's
just a finite number of them it's very
easy to figure out which action maximize
the Q value we can compare all of them
directly so now but we can talk about
the pseudocode for deep Q learning this
is relatively straightforward based on
the stuff that we just described there's
one thing which is a little more
specific than what I mentioned which is
this business of Epsilon greedy
exploration so I mentioned before that
you're going to explore by sometimes
taking a completely random action and
sometimes taking the action which is
greedy which maximizes your current Q
function approximator so epsilon greedy
is a strategy for doing that where with
probability epsilon where epsilon is
going to be something small you'll pick
a completely random action so uniform
random over the K different choices and
with probability 1 minus Epsilon most of
the time you'll pick the action that's
greedy with respect to your current Q

[01:59]
function so that's the run policy step
and then after you store that transition
into the replay buffer and anneal
Epsilon because over time you want to
explore less and exploit more you want
to rely on the policy as it gets better
after doing that you're now going to
evaluate the policy by learning Q star
from the data by improving q theta to be
a better reflector of Q star so that's
exactly the step of gradient descent
that we described which is that you
sample some transitions from your replay
buffer from your from your experience
replay memory and you compute the
bootstraps for those transitions and
there's a special case for if a
transition ended in a terminal state
which
that we don't give it a value after that
particular time step and then we use
those Y values in our bootstraps Q value
regression update the parameters and
then every once in a while with some

[02:00]
frequency will copy over the parameters
of the main q network onto the target
network so that's the target network
lagging the q network ensuring stability
and that's deep Q learning in a nutshell
this algorithm kicked off everything I
mean a whole bunch of stuff that
preceded it you can't really point to
any one moment in the history of a field
that you know had no precedent before
this there was neural fitted Q before
that there was Q learning with linear
function approximation and there were
all kinds of algorithms for trying to
get things to work with nonlinear
function approximation like deep neural
networks but but but this was the one
that got a lot of people really really
excited so anyhow caveat emptor buyer
beware this can break this will not work
on every problem out of the box you'll
try it in some places and it just won't
work you'll fiddle with hyper parameters
and it still won't work you'll try some

[02:01]
tricks to stabilize it because there are
pretty much infinity tricks to make deep
Q learning better at this point and some
of the time that still won't work so
this picture here is from a recent paper
which I really love and which I strongly
recommend that you take a look at if you
get interested in seeing some analysis
of failure modes for algorithms in deep
RL it's called deep reinforcement
learning and the deadly triad the deadly
triad is a set of traits that deep
reinforcement learning algorithms might
have which are known to occasionally
cause divergence and to create
substantial obstacles to theoreticians
who would like to come up with
algorithms that have provable
convergence guarantees so the deadly
triad consists of function approximation
off policy learning and bootstrapping
which are exactly the three things the
deep Q learning relies on we have
function approximation in the form of
neural networks we have auth policy
learning in the form of

[02:02]
spirits replay and we have bootstrapping
in the form of using the target network
with a one-step backup as the regression
target for q and so deep Q learning
works a whole lot of the time and then
some of the time it just doesn't so in
this set of experiments what the
researchers did was they examined deep Q
learning and a few variants of it a
bleeding on whether they would include a
target network so here this Q does not
have a target network the regression
target that it uses is exactly based on
Q theta naught Q theta tark and tried it
with a target network and then tried a
couple of other tricks that relate to
how you use the target network to
possibly either estimate the value in
the bootstrap or select the action in
the bootstrap and those are tricks that
are known to potentially help they
looked at at all these different cases

[02:03]
for many different Atari games as the
experimental test bed and they clipped
the rewards in the environments into a
certain range so that they knew exactly
mathematically what the ceiling for
possible real Q value would be they
chose it to be a hundred and they looked
and saw over all the experiments that
they ran how often did the maximum
absolute learned Q value in an
experiment exceed the threshold which
they knew was the real true maximum
possible Q value and the answer was a
lot so this shows that Q learning
without target networks is very unstable
in that a lot of the time you will get
this this divergence phenomenon and even
as you include tricks that make it
progressively more stable you'll still
expect to see divergence every now and
then so we're gonna dive into a little
bit of math now to kind of get maybe
some intuition for why this is the case
and what deep Q learning algorithms are

[02:04]
really trying to do and how that
translates into the algorithm or doesn't
so we're going to start by taking the
operator view of the bellman equation so
the optimal bellman operator t'east
is a map from cue functions on to other
cue functions and the value of T star
for a particular state action pair is
given by the the cue right by the
bellman equation that we saw before the
optimal cue function is the fixed point
of T star so Q star equals T star Q star
that's great and T star has this special
thing about it which is that it's a
contraction map on the space of Q
functions contraction maps have some
very special properties that we're gonna
talk about now yay
so the main thing about a contraction
map is this idea that if you have two
points and you apply the contraction map
to both of them they'll basically be

[02:05]
closer with respect to some distance
function after you've applied that map
to both of them than they were before
so expressed mathematically we have some
some norm some distance of the norm of a
thing minus the other thing and the norm
of f of X minus f of Y is going to be
less than or equal to some constant
factor times the norm of the difference
between x and y that distance between x
and y and when that beta is less than
one then we have a contraction that's
saying it's getting closer together it's
shrinking why do we care about
contractions because they have unique
fixed points and you can get to them by
just repeatedly applying the operator to
any initial point this is something
called the binocs 20 room if you're
interested in going on Wikipedia and
finding something which is going to be
more precise than however I've typed
this up but in a nutshell to show you
that they have unique let's forget about

[02:06]
uniqueness for a moment but at the very
least that repeatedly applying this
operator will get you to a fixed point
if we look at a sequence of points X and
we have a contraction map F with modulus
beta and each point in the sequence is
just yet generated by F of the previous
point and we look at the distance
between successive iterates what we see
is that it's shrinking as a function of
the iteration number so in the limit as
the iteration number goes to infinity
that distance will shrink to zero it
will converge repeatedly applying it
will get you to the fixed point t star
is a contraction on Q functions so if
you could represent the entirety of the
Q function that is to say the Q values
for every state action pair in the
entirety of the environment which for
all the environments that we care about
in deep reinforcement learning you
cannot easily do you can only do this
with function approximation which is to

[02:07]
say you're going to generalize whatever
you choose for the value in one state
action pair will have some influence on
another you can't completely separate
them when you do function approximation
but putting that aside so we could
represent all the action values for
every state action pair and we applied T
star the operator to that function we
would get a new function Q which is
closer to optimal than the one that went
in and if we applied it over and over
and over again we would eventually get
to Q star the fixed point of T star this
is value iteration
it's a classic algorithm and
reinforcement learning so before
function approximation before deep when
you had environments where there were a
discrete number of states and a discrete
number of actions and you could
represent the Q values in a table of
elements one for each state action pair
you could compute this exactly and use
this as a way to get to Q star now when
you live in the problems that we do when

[02:08]
you're trying to solve high dimensional
complex video games high dimensional
complex strategy games you can't use the
table yet use a function approximator
and now your problem is that you can't
compute all of T star Qi and even if you
could you probably couldn't find a
choice of parameters that would allow
you to exactly represent it so if you
want to do this kind of value iteration
you have to do it approximately and this
is roughly what Q learning algorithms
with function approximation try to do
which is that they push the parameters
of the network in the direction such
that you move Q theta towards T
star q theta and sometimes this works
and sometimes it doesn't because when
you go to this function approximation
setting this operation is not
necessarily going to be a contraction on
the space of Q functions you might have
lost that property if you did expect
divergence in fact I expect things to

[02:09]
blow up horribly if you preserved it or
if you've done enough tricks to
stabilize it things will work pretty
well in my experience Q learning
algorithms and their variants tend to be
extremely sample efficient when they
work which is quite desirable and it's
very nice if they can recycle off policy
data because on policy methods sadly
have to throw away tons of it but last
point on Q learning what you normally
see in deep learning algorithms and deep
RL algorithms is that paradigm of
there's an objective function and you
optimize it and you find the model that
optimizes the objective in Q learning
don't be misled into believing however
many times you see it that the mean
squared bellman error it's really the
thing that you're optimizing you change
that function every time you change the
target the thing that you're really
doing is this sort of approximate value
iteration you're trying to apply an
approximate operator which is going to
get you to something better you're not

[02:10]
trying to minimize a loss that's not to
say that there aren't variants of these
kinds of algorithms that do involve
well-defined loss functions there's a
whole family of algorithms called
gradient temporal difference methods
which if you are theoretically inclined
and willing to go down a deep deep deep
rabbit hole I recommend you check out
talk to me if you want references also
in the spinning up key papers doc I
believe there's a book in the bonus
section for classic RL papers and review
papers choppa Sabbath Baris book on RL
algorithms from 2010 which recaps a lot
of this really great old stuff including
gradient temporal difference algorithms
so I recommend you check that out if
you're interested yes I'm actually
working on some research on that right
now
like I
talk to me offline yes yes yes so so
this thing yes it's called a temporal

[02:11]
difference error because it is the
difference in the Q value based on the
next time step versus the current time
step yeah yes absolutely what is the
difference between off policy and on
policy the on policy algorithms have
updates which are based on the expected
values of things where the distribution
and that expectation depends on the
current policy so if you want to form a
sample estimate of the thing in the
update equation then you first have to
run the current policy collect
interactions with the environment on the
current policy and use those samples for
forming that sample estimate that's on
policy because all the data that you use
has to be generated by the policy that

[02:12]
you're using at the time in off policy
methods like q-learning what you do when
you make an update is you use experience
which might have been generated by older
policies not the current one so the
current policy you could think of as
being implicitly expressed in the in the
Q function approximator is current value
but many steps ago it was different and
you got whatever data you got from
interacting with the environment you put
that in your replay buffer and then many
steps later you still sample those
states and actions from that replay
buffer to help you form your your new
update to the current q function so when
the data was generated by a different
policy that's off policy yes
in what sort of gaming situation would
we maybe use deep q-learning or like
what's a use case for it so there's a
fabulous use case actually Facebook

[02:13]
recently released a paper on their
machine learning and RL learning there
RL platform called horizon which they
used to train with deep Q learning
neural networks for making decisions
about when to send you push
notifications so actually DQ n is in
your phones right now okay then let's
proceed to the next part which is model
based stuff so I'm going to be pretty
brief about model based stuff there's a
very wide variety of different model
based algorithms and we're not going to
drill down into them the way that we
drill down into policy learning and Q
learning but we will give a relatively
brief overview of some of the more
salient points and a few algorithms that
I think are particularly interesting so
back to the loop run policy evaluate
policy improve policy where do models
fit in so recall that a model of the
environment lets you predict what's
gonna happen next you can use that for

[02:14]
pretty much any of these while you're
running your policy before you take an
action you can stop and imagine what's
gonna happen if you try many different
things you can create partial rollouts
that you can use to evaluate your
different choices and then you might
pick something different than you would
have otherwise so that's maybe where it
can appear in running ball and running
the policy in evaluating the policy you
can use that same kind of approach of
just simulating look-ahead data to help
you get a maybe a more stable backup for
your q function or just use some kind of
Monte Carlo tree search style algorithm
where you're going to propagate Q values
back and figure out like an average case
Q value and then for improving the
policy you can regress your policy
network if you have explicitly
represented one towards whatever the
outputs were from that look-ahead
planning process so if you have a model

[02:15]
it's very powerful you can use the
a lot of different ways you can embed it
pretty deeply in into RL the problem is
that models are very hard to learn and
you usually don't have them so let's say
you have just made a wonderful brand new
complex physical robot unless you have a
lot of hours to spare and control theory
expertise you probably do not know how
to fully characterize that and have a
simulator model which is going to be
accurate in any reasonable way certainly
not accurate enough for training it in
simulation and then directly applying
that simulation trained policy into the
real world you may want to try learning
a policy from data but this can be quite
tricky although there are some really
exceptional success cases but because
yes uh yes you could make that argument
so I let's say hardness to learn is not
a fuck oh I suppose sorry the question

[02:16]
was can you make the same argument for
value functions and I would say that
hardness to learn in this case should be
interpreted more as has the research
community figured out really robust
reliable standard methods for doing it
yet but not necessarily whether there's
some intrinsic quality of hardness
finding the correct model is a
supervised learning problem if you have
enough data part of the problem in RL is
that you usually don't have enough data
and you would have to get it by
interacting with the environment and
there may be areas in the environment
very critical to decision making which
you've just never observed yet so
imagine that you are in a giant maze and
you can try to learn a model of the maze
as you go but until you've seen the exit
your model does not going to be very
helpful for you and navigating except to
help you perhaps avoid repeating places
that you've been to already but but yeah

[02:17]
in practice models tend to be so far
hard to learn so let's look at maybe one
case study in ways that you can use
models so this is the case of planning
and/or expert iteration the basic idea
is that you're going to use your model
from a current state to look ahead into
the future and help guide your decision
about what action to take
so in planning you might explicitly just
base your decision about what action to
take on whatever the output from that
look-ahead process is and your current
value function in expert iteration
you're not only going to do that but
then you're also going to have a
explicit representation of a policy
which you'll try to improve by
regressing it towards the output from
the look-ahead process so as a case
study consider alpha 0 alpha 0 is an
algorithm which has succeeded at
achieving superhuman performance in a
wide variety of complex 2-player fully
observed strategy games particularly
chess go and shogi so this was a

[02:18]
successor to alphago the algorithm that
beat human grandmasters and go and alpha
0 at the algorithm level is sort of
beautifully simple you have a neural
network that emits two things a
probability distribution over moves to
play P and a value network that says
basically whether or not you're gonna
win or lose B and you learn this with
this very simple regression approach
where you're gonna move the value
function to be more like whatever the
true outcomes from games work and you're
going to update the policy by using a
model-based look-ahead operator to
figure out what a better policy would
have been based on your current policy
and value function and you're just going
to move your current policy towards that
and then there's also some
regularization very straightforward and
the look ahead is done with Monte Carlo
tree search so that's just stochastic
lis considering different possible

[02:19]
outcomes and then aggregating data after
having done partial rollouts down the
game tree to figure out what would have
been the best thing to do so this is one
model-based approach now this required
having a perfect model of the
environment and in games like chess ergo
this is feasible because you could fully
Express the rules in a way which is easy
to compute and forward simulate
and you don't have to learn anything
from data and you also don't have
anything which is partially observed so
your model doesn't have to do anything
fancy to keep track of what's going on
in the background very straightforward
and this kind of approach can be very
very powerful but the problem is that
most conditions are not quite as ideal
as this so another family of approaches
is where you're going to use the model
for policy evaluation so let's say that
you have learned a model or perhaps
you're given one but more often than not

[02:20]
for these algorithms you're trying to
learn it concurrently with experience
you learn some models and then you're
going to have the agent quote dream in
them the agent will sample a bunch of
fictitious trajectories inside of the
simulator and use those as the basis for
a policy improvement step and algorithms
that are like this
there's model ensemble TRP oh and I want
to say Mehta policy optimization or
model-based Mehta policy optimization
then you could also instead of using
this for computing advantages and and a
policy optimization style improvement
you could use this for Q learning as
well where perhaps instead of forming
the target based on the bootstrap which
might be inaccurate on particular
regions of state action space that you
haven't visited you could use the model
to simulate what the bootstrap might be
in those cases and use that as your
backup for Q learning so that's an
approach called model-based value
expansion and these algorithms the gain

[02:21]
that you get from doing this is
ultimately in-sample efficiency so what
happens in normal deep RL is that you
use tons and tons of data from
interacting with the environment to try
to improve your policy or your q
function and you make progress at
whatever pace when you use the model and
you offload a whole lot of the
improvement steps on to experience
collected in the model that frees you up
from having to have collected that
amount of experience in the real world
as long as your model is good enough if
your models not good this won't be very
helpful but if it is good and if you
only needed a little bit of data to
train your model then you can get a lot
of mileage out of it and your overall RL
algorithm will have used less
interactions with the real environment
and otherwise this is great for cases
where interacting with the real
environment is very expensive so for
instance if you want to train something
on a physical robot that can be an
expensive process the robot might be
slow the robot might break the robot
might have all kinds of things where
it's difficult to get it to do that or

[02:22]
it's difficult to reset it you probably
don't want to have to spend that many
man-hours waiting around for the robot
to finish its learning procedure so if
you can offload some of that time into
simulation then it makes life better
yes is that what you would apply for
self-driving cars that's a good question
so I'm not actually all that familiar
with cases where self-driving cars have
fruitfully made use of deep RL that's
not to say that they don't I just don't
know I would imagine that in
self-driving cars it's probably more a
matter of collecting data from
experienced human experts and then using
that data as the basis for learning a
behavioral policy but I'm also happy to
you know go through this later and see
what we can find in the literature yes
what would model-based RL be more geared
towards transfer learning I think it

[02:23]
could potentially be quite helpful so
certainly when we think about trying to
get robotics to transfer from say
simulation to reality you know we want
to make sure that the model used in
simulation is high fidelity with respect
to reality and if that's the case then
this model you can think about sim to
real as sort of a model-based approach
and perhaps it's gonna be very helpful
all right and then there's this other
completely orthogonal way of using
models which I'm really fond of because
it's just sort of weird which is that
you actually take the model and embed it
inside of a model free agent where the
model is going to receive inputs from
the from the environment and use that
with some internal process of perhaps
imagining some futures and then

[02:24]
transforming whatever representation and
has of those futures into something
which then becomes side information to
the model free agent so you train the
model separately from the agent the
module that provides some information
based on the model to the agent is sort
of decoupled from it except that however
it's going to process however the model
free agent will process that information
is based purely on the model free
learning so this is an approach called
imagination Augmented agents I think
this is really interesting and really
neat I'm not aware of a whole lot of
follow-up work from when this came out I
want to say last year or the year before
but I just think that because it is so
different from the other model-based
approaches that's cool whenever there's
something different it's cool all right
that takes me to what was originally
intended to be the end of part one but
it's now the end of both parts thank you
so much
at this point I would like to turn over
the mic and the stage to Matthias

[02:25]
Clapperton who is a researcher on the
robotics team at open AI and he'll be
presenting on the work on the robotics
team for learning how to do complex
manipulation with deep reinforcement
learning on a real physical robot great
thank you
we have a computer suite

[02:26]
yay I think it works okay thank you
cool so hey everybody my name is Matias
as Josh mentioned I'm super excited to
be here and talk a little bit about what
robotics that openly is doing and to
talk that I'm going to present this call
it's called learning dexterity as I
mentioned this is basically the effort
of the entire robotics teams for many
months so everything I'm kind of talking
about is not just my work but these are
robotics teams okay cool
so let's maybe start with talking a
little bit about what robotics at open
era is actually trying to do and the
ultimate goal I guess robotics at open

[02:27]
eye has is suppose some form of general
purpose robot so I think this kind of
picture illustrates as well very well we
have human-like robots today and we know
that humans can do a very very large
amount of different jobs and skills so
that can include things like cooking it
can include things like actual labor in
some form of agricultural thing
maybe it's very precise kind of things
like surgery or building things and
putting things together in this kind of
stuff and ideally we would like to have
a robot that has a similar similar level
of dexterity and a similar level of well
general purpose Ness if you will the way
robotics looks right now it's very
different from that so we have these
kind of very specialized robots so an
example I think that is good it's the
Roomba which is on the lower in the
upper left corner here that can clean
your house but it can only clean your
house it can only vacuum your house and
similarly your things like self-driving
cars which to some extent also robots

[02:28]
that are very good at one thing which is
driving themselves but they cannot do
anything else and the robots there are
more kind of versatile and more
complicated they are either very often
controlled by humans so an example for
that would be doing surgery so we have
robots that can assist humans in that
but they're always controlled by human
operator which is a surgeon or we have
more complicated robots in factories but
those are typically just programmed to
basically blindly execute a given show
secretary so someone sits with the robot
and figures out how to do a certain
process in a factory and the robot is
very very stupid and has no idea what's
going on so the question of course is
how can we kind of step away from that
paradigm and how can we have robots that
work in an actual physical world and
aware of their surroundings and given
that this is the spinning out workshop
that's concerned with ll it's not so
surprising that we think RL may be a
good approach to that and we know that
RL works really well in certain domains
so I've picked out two examples here

[02:29]
that probably most people have seen on
the left side we have alphago zero
playing against Lisa at all and a game
of Go and as you know alphago zero won
this game
in fact I think one almost all games
that it has ever played and the
follow-up versions of alphago zero
beyond beyond human capabilities when it
comes to playing go similarly we have
dota 2 so this is some of the work that
the dota team at opening AI has been
doing for a while we have this door
abort called opening at five that is
very very good at playing the game dota
2 which is a 5v5 multiplayer game and it
is approaching like professional levels
so it's it's consistently winning and
can semi-pros and we are already playing
against some pros in fact we've done
that last summer at the International
unfortunately we have not yet won
against those pros so the question is
how does this work in robotics and of

[02:30]
course yes like a lot of work in this in
robotics it's not like we we are the
only ones doing this and I just like to
give a bunch of examples that I think
are kind of illustrating what people are
typically doing today
the first approach here is somewhat
reason it's from 2017 and I think it
looks really cool so you can see the
agent is even able to use certain tools
so in this case a hammer it can open
doors it can do all sorts of things
the unfortunate thing here is that all
of this looks really cool about it's
only in simulation and ultimately in
robotics it doesn't really count if it's
only in simulation because you want the
physical robot to do something otherwise
it's not very useful
so the other approach that people have
been taking is to train on the actual
robot itself so this is a some work from
2016 where people have been doing
dextrose in hand manipulation so the
goal of the robot here is to kind of
manipulate this this tube filled with

[02:31]
coffee beans for some reason into a
target orientation and they do all the
learning on the on the actual robot and
that of course has the advantage of not
having to do any form of transfer
because you learn on the robot you
exactly know how the robot is going to
work and once you have a good policy
you're done the downside of that of
course is that well you have to run on
the actual robot so it kind of breaks a
lot on you it's very slow to do you
can't really scale this up unless you
get a lot of robots which is actually
something that people are doing so this
is the approach thing by Google and
typical Google fashion scale it up so
just get a lot of robots and let them do
it for two months in parallel and then
you can suddenly train on the robot
because well you have 20 of those doing
it in parallel and it can do very
meaningful stuff so in this case they
have learned to grasp arbitrary objects
out of this kind of box that I have
sitting here and this is actually very
impressive demo like this kind of been
picking stuff is actually very hard the

[02:32]
thing is still that obviously this does
not really scale all that well because
this is a relatively simple task yet you
need 20 robots going for two months and
you will also just have to babysit the
robot all the time right like you'll
have to repair it when it breaks you'll
have to kind of reset the environment
when certain objects fall out of the bin
and all of this kind of stuff so it's
just a lot of work so what we're trying
to do is to kind of combine the benefits
of those two approaches so training in
simulation and then transferring to the
physical world which is called sim to
real and I'll be talking a lot more
about this but before I do that I'd like
to introduce you to the test that we
actually have in mind when we when we do
our research so we decided to do
dextrose in hand manipulation and the
reason for that is that it is first of
all very hard to do and then second of
it is something that we're interested in
because we know that our hands these

[02:33]
universal end effectors right so human
hands are very versatile in what they
can do it they can be very dexterous you
can do an cooking thing or you can
operate on a human if you're searching
at least but you can also do very heavy
lifting with it and you can use tools
made for you nuts hands and these kind
of things so so this is basically the
motivation for why we choose this kind
of hand and just kind of tasks because
it's hard and because it's also
ultimately useful for the channel
purpose robot we would like to build and
the reason why it's hard I think is
summarized relatively well in this this
kind of slide so we use a hand called
the shadow Dexter's hand which is
depicted in this picture it has 24
joints and it has 20 actuators so what
this means is that your policy it and
every time set has to produce an action
for 20 individual actuaries and it
actually has to coordinate right like
you'll have to have different joints
work together to do certain things so

[02:34]
it's a really high dimensional kind of
control problem that's typically well
out of reach of what traditional control
problems can solve as I mentioned
ultimately we wanna run this on real
hardware and so we have to work with the
real hard way and all its flaws and
issues so this includes things like
noisy and delayed sensing so that's just
a fact of physical hardware systems
right like they will not have perfect
information and they will have delays
and certain certain quirks that you kind
of have to deal with the other issue
that comes out of this sensing is that
you actually have to handle partial
observability so in simulation you have
perfect knowledge of everything that's
going on because well it's your
simulation and you can just read out
from your simulation what the current
state is but on the physical system you
can only use what you can actually sense
so obviously certain things like the
friction for instance of the system
cannot directly be observed and then
last of all this is actually super hard
to simulate as it turns out the reason
for that is that you have a lot of
contacts going on so if you have

[02:35]
something in your hand like you kind of
constantly touch it and contexts are
notoriously hard to model accurately
first of all and then the hand itself is
also incredibly complicated so it's 10
actuated which means that you kind of
have tendons pulling and just causes a
lot of unmodeled kind of things in you
and your hardware that you have not
modeled in simulation cool so as I
mentioned we set out to solve this
problem with our seem to real approach
so we trained in simulation and then we
transfer to the physical hardware and
while this sounds very easy it is not
very easy because the transfer problem
as you'll see is actually not very easy
to overcome but before we talk about
that let's have a look at what what we
can do in simulation and what the policy
that we train looks like in simulation I
think this also illustrates the task at
hand so that you can actually understand
later what what the robot is trying to
do so as you can see you kind of have
this block with colored faces and the

[02:36]
task is to rotate this block into the
desired target orientation that you have
and the target is depicted as this kind
of like semi-transparent additional
block on the right hand side so now it's
trying to bring up the blue face a yeah
it got it and then kind of moves on to
the next goal and as you can see it just
kind of involved like it coordinating
its fingers it has to kind of use its
permit it's kind of using gravity to let
it roll and it's like even in simulation
this is not super easy to learn the hard
way itself looks like this so this is
the cage we call it it houses all sorts
of things in the middle of course you
have the shadow Dexter's hand which is
the robot itself and then you have it
surrounded by quite a lot of these face
based tracking cameras so we have 12 of
those in total and what they do is they
provide you with relatively accurate
sensing in in Cartesian space so we have
LED markers on the hand itself so we

[02:37]
know where the hand is and we also have
LED markers on the object so we know
where the object is and those guys
basically they sense the slide of the
LED and since multiple cameras can kind
of see the same LED marker that it can
do triangulation and you can recover the
position in in space from that
information
we also have an alternative setup
because as I mentioned ultimately we'd
like to have something that's more
general and having a motion capture
system is not very kind of real-world
like so we also have RGB camera so those
are regular RGB cameras we have three of
them surrounding the scene and they can
also be used for sensing in fact they
can be used for post estimation of the
object so you don't even have to have
any any special kind of sensing on the
object itself the cameras can do it for
you and the reason why we have three is
just just so they can first kind of
recover depth information and then
second they can also kind of work around

[02:38]
occlusions because it's in the hand from
certain angles you cannot sometimes see
the object because it's kind of covered
by the hand so this is how it looks up
close when we run things so as you can
see we have the we have the hand with
the block in it palm and in this case
it's the block that we use for face
based tracking so you can kind of also
see the LEDs on it that we use this is
simply much easier to do when when kind
of testing these algorithms so we have
these kind of world setups all right so
the big question of course is how do we
do the transfer so I showed you a video
of the policy doing its thing in
simulation and I showed you the physical
Hardware so we can have all the building
blocks but how can we actually transfer
it to the physical robot and if you just
train it in simulation it will not work
at all it's the short version so I'll be
showing some kind of numbers for that as
well but there you can believe me if I
say the transfer problem is really the
core issue that we're dealing with here

[02:39]
and the approach that we're taking is
relatively straightforward actually so
what we do is we use two main techniques
the first one of course being
reinforcement learning to learn the
actual control policy and then the
second technique being the main
randomization to make sure that the
learn control policy actually transfers
to the physical system and I'll be
speaking about both of those in a little
bit more detail so let's get started
with the main randomization so this is a
technique that has been used for a
little while
pretty popular paper when it comes to
this is from 2016 in this paper what
they did is they learn to fly a drone
and the way they approach this is they
trained in only in simulation using
these kind of randomized buildings so
you can kind of see it has a lot of
different rooms in it the textures are
very different so the walls look
different of ceilings of floors and they
train a drone to fly in all of those

[02:40]
rooms and what they then do is they take
this drone that was only ever flying
inside a simulation and show that they
can actually fly another completely
different actual room simply because it
kind of has seen all of this variant
doing during its training it kind of
like from its perspective what happens
is that the policy think so justice is
another like randomization it's kind of
weird but oh well I know how to handle
it so it flies in the actual room and
people that open either has been using
similar approaches as well so this is
some work from my colleague Josh Tobin
what he has been doing is he has been
using domain randomization for grasping
so this is using a robot called the
fetch
so it's you'll see a better picture in a
moment but it's basically a a simple
robot armed with a parallel group at the
end and what he would like to do is pick
up these objects that you kind of see in
these randomized scenes and by basically
using the same approach so he's

[02:41]
randomizing all sorts of things like the
looks of the objects of shape of the
objects the background the color of the
table as you can see he can then use
this information or this training to
transfer to the physical robot even
though it has never seen the actual
physical table and what was pretty
surprising in this research is that it
turns out you don't even need
photorealistic rendering so as you can
see like this it looks not realistic at
all it's like pretty computer graphics
and and still it transfers to the
physical to the physical world so the
important thing here is that you have
this variety and not necessarily
realistic environments yeah yes so all
of the the two approaches that I showed
are using
using vision to learn a policy yes in
this case I think it's actually not
using the vision to learn a policy
directly I think it's instead just
predicting the location of the object
and then there's a policy that the
Kinect can grasp it from that so some
some other work in this domain which i

[02:42]
think is equally important is physics
randomization and this has been done by
Jason pang who used to be an intern at
open air in 2017 and he's basically
using the same idea of randomizing but
now for physics instead of visual
appearances so it's kind of hard to like
visualize what's going on but what the
policy in training sees a certain worlds
that are just different so maybe they
have different masses maybe they have
different frictions of the table maybe
the robot itself behaves differently and
so on and so forth and what he was able
to show is that this again is sufficient
to train strictly in simulation and then
transfer to the physical robot so the
test at hand here is again with the
fetch robot and it's trying to move this
this park to the goal location which is
marked in in red and on the left hand
side you see a policy that has been

[02:43]
trained with those physics
randomizations and on the right hand
side it has been trained without and as
you can see obviously the one on the
left hand side does a pretty decent job
it's like relatively precise it can push
the park where it wants to go and the
one on the right kind of freaks out so
it shakes very violently in fact the
building was shaking when he was
deploying this and it cannot really do
with the job and the reason is that it
well has kind of over fit to the
simulation which simply is not fully
accurate even though it's calibrated to
be close to the robot and then it
doesn't generalize to the actual
physical world where's the one with
physics randomization stars okay of
course so that's the main randomization
in a nutshell so both the visual
randomization and the physics
randomization yeah
yeah it's it's not very realistic
honestly I mean it's realistic in the
sense that it's the physical so if you
randomize too much your simulation will
become unstable because you've set in
certain parameters such that they cannot

[02:44]
make sense anymore
but it's not very realistic like the
masses will be very high sometimes it's
like smart to move the puck and it's
more about diversity again yeah okay
cool
so I'll now speak about our approach so
what I previously talked about was
mostly other people's work even though
they're also in the robotics team but
this is the the learning dexterity
approach that we took so again remember
the goal is to have the shadow hand
rotate an object in hand and to kind of
start it off I think it makes sense to
just give you the the overview of the
entire system and then we'll kind of
dive into some of them details after
that so again as I mentioned everything
we do is only in simulation so we never
see the actual physical robot until we
run on it like we've never seen it so so
the way it works is that we collect a
lot of data in simulations so we have
many many simulations running in
parallel which is kind of depicted here
in box a and all of those are randomized
which is kind of visualized by them

[02:45]
having different visual appearances but
also think physics randomizations so the
friction and the masses will also be
randomized and using this collected data
we basically end up training two
different networks so one of them is a
policy and the other one is job is a
vision network because we'd ultimately
like to run this from vision alone
without the face base the policy network
is what is depicted in Box B here and
the way it works is that it takes the
observed robot state which is the
position of the five fingertips so you
have doting coaches in a space of 15
dimensions in total so it knows where
its fingertips are and then also the
pose of the object so that means just at
the orientation and the rotation in
space sorry the position and the
rotation in space and this information
is then fed into an LSD and policy so
it's a recurrent policy and it produces
the next action and we train this in
simulation using reinforcement learning
the second network that we have which is
actually distinct they are not
end-to-end

[02:46]
this is two networks that we train
separately it's a vision Network and the
rate and vision Network uses works is
that it takes three different images so
remember we had these three RGB cameras
surrounding so images rendered from the
perspective of those but again only in
simulation and then using a
convolutional neural network predicts
the pose of the object from that
information from those images and again
this is only trained in simulation when
it comes to actually deploying this to
transfer as you can maybe kind of guess
is that we can combine those two systems
to get us what we ultimately would like
so you use the actual cameras to sense
the position or the pose of the object
using the vision network so you feed it
into that and then by having the object
pose and the fingertip locations you use
your L SCM policy to produce actions and
that allows the robot to basically see
what is going on and react accordingly
and of all only being trained in
simulation yeah potentially honestly we

[02:47]
have mostly used this approach because
we knew it worked from previous research
it is almost as accurate as face base
and face base is very very accurate I
think if you spend a lot of time you
could probably develop something with
more traditional methods I don't
question it but like we would like to
have something that's more general again
and having a convolution that conversion
neural network - it seemed like the most
general approach we could have yeah yeah
it's kind of interesting so ideally you
would just use whatever the robot has as
joint sensing so it knows it should know
what its own joints are as it turns out
the sensor in the shadow hand uses
hall-effect sensing which is a magnetic

[02:48]
kind of sensor and they interfere quite
a lot so if you think as a close
together you will actually not know
where your fingers are so that's the
reason why we don't use it we would like
to use it but it turned out to be not
precise enough for what we ultimately
wanted to do so we couldn't actually
rely
but yeah you're right like like this is
more for more for work around like
ideally the robot should just tell us
what the joint positions are and then we
wouldn't need the fingertip positions no
it actually has very limited information
it's very surprising that it works like
that yeah yes yeah yeah very good
question this is there's a lot of debate
about this I don't think it does we have
some indication that it doesn't in fact
it seems to help like the performance
seems to improve over the board like we
have certain ways of measuring symptom
transfer and when we randomize more we
tend to get better performance on all
the environments so I don't think it's

[02:49]
it's compromising actually I think it's
more of an adaptive policy but then
there's people who disagree so it's
currently a little bit unclear okay cool
so as I mentioned we need to randomize
and of course we use appearance
randomization so this is only for the
vision Network so this is basically what
I've described before just for our setup
so you can kind of see we have three
different cameras showing the same scene
and we randomize this scene quite quite
heavily so the robot changes its color
the background changes its color
importantly the block itself stays
mostly the same because it actually has
that color like you cannot randomize the
dye but rarely but we changed the
material of the of the block as well so
it looks slightly different and then we
of course have that vision network which
again is relatively straightforward so
the way it works is it takes those three
camera images then uses convolutions and
the rest net architecture and spatial
softmax to kind of process them and then

[02:50]
simply calculates all the things and
produces the final object position on
object rotation so the pose of the
object and this is simply trained with
supervised learning because in
simulation you actually have perfect
ground truth which is another very
convenient thing you actually perfectly
precisely know where your your object is
you have not to actually sense it at all
and this is what the model actually sees
so it's actually I think very
interesting because it looks very very
different from
randomization and yet it generalizes to
that simply because it has seen enough
variety that it's kind of okay with with
yet another variety that's kind of weird
but still within distribution in that
sense so when it comes to the physics
randomizations that we use we randomized
quite a lot of things as well so we have
things like object dimensions for
instance we have things like masses
obviously and then mostly things about
the robot itself so things like the way
we actuate the robot things like damping
within its joints and all of this stuff

[02:51]
and the reason for that is that it's
actually very hard to measure this so
another neat thing is that you can in
this physics randomization actually
account for your uncertainty so for the
object dimensions we know those with
relatively little uncertainty because we
can just measure the dimension of the
block but things like the actuation we
learn much less about and so we kind of
widen the randomizations for those and
another kind of cool thing is that we
randomized the gravity vector which may
seem a little bit weird but it basically
amounts to like when you when you mount
the hand it's not perfectly parallel to
the to the floor like it will be
slightly angled because of imperfections
and by randomizing the gravity vector
you kind of get this effect as well like
it's sometimes slightly angled and it
turned out to be actually very useful
and then we of course also have noisy
observations and noisy actions simply
because it's a rare reality of the of
the physical system the policy is very
very simple so what it gets is the noisy
observations so that's five fingertip
positions and the poles of the object
and the goal so it's knows what it wants

[02:52]
to do and then we normalize a little bit
so this is just making sure that things
have a zero mean and unit variance and
then use one fully connected value layer
and one lsdm to produce the actual
distribution and from that we sample and
then perform perform that on the robot
so it's a relatively shallow and
relatively small network over all the
more so yeah
they only come in through the simulation
they cannot be observed directly so
sorry

[02:53]
they are simply set in the simulation so
the environment has been changed but the
policy cannot sense this directly it has
to infer this basically because on the
physical robot it also cannot sense it
like we don't know what it is on the
physical system so it basically what
what we think it ultimately ends up
doing is some form of system
identification so when it's running it's
implicitly inferring certain information
about the environment and then using
this information to kind of adapt itself
accordingly yeah sorry I couldn't hear
yeah so so we add Gaussian noise to the
observations and to the actions yeah all
right so I think I'm running a little
bit late actually how bad is this huh
okay then we have to hurry a little bit
cooler so disappeared of training let me

[02:54]
speak about this and then I'll show a
video so disappeared training I think is
very interesting because we use
basically the same system that the dota
team uses as well so we have a very
large-scale kind of system and the way
it works is that we have role of workers
who generate a lot of experience and
then we have an optimizing machine
that's kind of using this information to
update its policy and we use approximate
policy optimization for that so a non
policy algorithm as I think josh has
explained earlier today and I think it's
kind of cool that we use the same system
estera let me skip over some things but
I think I've want to show this so this
is when it's running on the physical
robot as you can see it's using vision
so there are no markers on the actual
object the robot hand is doing all of
this this is not cut in any way it is
not sped up again the goal is depicted
in the right corner here so it will try
to get the e face front and the end face
up top and it will get 250 successful

[02:55]
rotations in this case so it can do
quite a lot of those and it can run on
the on the physical system and if I have
enough time one one kind of final thing
that I think is actually very
interesting is that it actually learns
certain strategies that happen to have
names so we have thing a pivoting where
you kind of like use two fingers to
create a rotational axis and then you
rotate around that and things like
finger gating and the reason why they
have names is because they are used by
humans as well and they have been kind
of studied very well they emerge
automatically in our case so we have
never shown the robot what a human would
do it has kind of discovered that itself
and the reason why they come up is
simply because it has a human-like
morphology right like it has a
human-like hand and it just turns out
that these strategies are equally useful
for humans and robots but they have kind
of been rediscovered quote-unquote which
i think is a really
thing so I wanted to mention that and
yet we have some qualitative results
that show that randomizations are very
important so if you don't randomized you

[02:56]
get no successes if you randomized you
do it turns out memory is very important
so you need an LLC M you cannot simply
have a feed for policy and you need a
lot of experience so for the final
policy we use a hundred years worth of
data so imagine doing that on the
physical robot like probably not such a
good idea so but we can get away with it
because we use simulation so we do all
of this in 50 hours and I think with
that I have to close all right thank you
great thank you so much Matthias we're
gonna switch out the slides and then
please welcome to the stage the leader
of the safety team at open AI dario
Amadei all right just a minute to get
the slides

[02:57]
right
very good thing that you're ensuring
that computers in the future will not be
as malicious so I work on a team at open
AI that thinks about making AI systems

[02:58]
do what humans want them to do
which is you know kind of very central
to open the eyes mission and you know
which which we think of as you know
something that our focus on
distinguishes us from from other
organizations we think it's very
important particularly as systems get
more capable to ensure that they you
know both in a narrow and broad sense
benefit society
so this workshops called spinning up in
in deep RL so it's useful to step back
and you know think about what is what is
RL accomplished in the last couple years
and where is it going so you know this
is actually out of date we should add
add a couple things to it but you know
if we look at playing games like go if
we look at for about a year ago multi
agent behaviors where you can use RL and
self play to train agents to sumo

[02:59]
wrestle each other off a pad we are able
to play competitively against
professional professional players in
dota 2 the robot results which you just
saw and you know we should probably add
just in the last week or two you know
the results we've seen on StarCraft
which is you know in some ways similar
to dota but just a different kind of
game with the different kind of
properties and yet you know that shows
that these techniques are really are
really pretty general and are are
advancing pretty quickly so you know if
we step back and reflect on you know
kind of where are things going you know
some properties that we could point out
of these RL agents that are becoming
more and more true right that we're not
true five years ago but are becoming
more and
are true we have systems that have an
extended interaction with complex
real-time environment they have a very
high level of autonomy and speed you can
imagine systems like this in the real

[03:00]
world being used to make decisions
faster than humans can intervene or in
more complex ways than humans could you
know could hope to understand so
regulating the economy or financial
system managing large networks of
computers these are the kinds of things
that as RL technology matures it will be
better and better better and better able
to do and you know the these systems
unlike supervised learning systems and
unlike in any interesting way you know
the simple RL systems were a few years
ago these systems are able to teach
themselves and discover their own
strategies and in many cases they
discover non-trivial strategies you know
just like we saw with the robot it kind
of recapitulating a lot of strategies
that humans use you know we see in go
and dota and Starcraft a lot of human
strategies that have names you know the
RL system discovers and recapitulates
but it also sometimes discover

[03:01]
strategies that a human would never
would never have thought of so if we
look at what these properties mean
together one thing it means is that the
connection between us as designers
specifying what we want the system to do
and what the system actually does in
theory the system does in theory if
everything is done right the system does
what we want but that that rope it's
longer it's more afraid it's more
tenuous
than for just kind of less less
autonomous systems that we've we've
designed in the past
and there are many ways relative to you
know simple computer systems or machine
learning systems like supervised
learning for for these systems to go
wrong and so a couple years ago several
people on most most of whom are now now
now constitute the the open a nice
safety team started started thinking
about this you know we're worried about
current systems worried about tomorrow
systems eventually we're worried about

[03:02]
you
about about building general
intelligence and what that what that
will mean for the world and making sure
that those systems are safe so you know
we wrote kind of a position paper and
this kind of started us thinking about
you know the directions and how to even
think about this problem of you know do
systems reliably do do what we want them
to do and the the kind of general
framework and division we came up with
was okay so you know let's let's let's
narrowly scope the problem we're not
we're speaking not about kind of wider
or societal impacts although those are
also important but you know just
narrowly the designer had a clear thing
they wanted the system to do and then
you know the system gets trained it gets
deployed it goes through some long
process actual system fails at this
catastrophic ly and we kind of divide it
up into into a couple things one is you
know you're you're giving the system
some Direction some objective function

[03:03]
that it learns from like the reward in
RL there are ways for that to be subtly
wrong and you can get spectacularly
wrong behavior if that happens you might
have the right objective function but
your system has problems with robustness
doesn't generalize well it you know
exhibits on exhibits unpredictable
behavior as its learning it does
dangerous things even if the final
policy it's gonna learn makes sense and
then as a reminder that you know there
like this
all exists on top of kind of software
implementation that has bugs in and of
itself and so you know these the a and B
are new but they're layered on top of
the general just the general
unreliability of software so kind of a
useful way to think about let's put CSI
because it's not really a machine
learning problem or just you know a
reminder that this is layered on top of
existing problems but a crude analogy we
can make is you know it's a bit like the
simple statistical concepts of bias and
variance right better a better objective
function you know that's that's about

[03:04]
reducing bias and making sure your aim
for the right target robustness is is
about making sure that you're narrowly
cluster around the target and that you
always get what you're intending to get
so we're interested in in both problem
because I have limited time I'm going to
talk about our work on the getting the
objective function side right I think
you know open AI does more the opening I
safety team does more of that relative
to other you know other teams say at
Google brain or deep mind that that
think about these problems and so I'll
mostly talk about that but increasingly
and maybe I'll have a little bit of time
to talk about it at the end we're also
thinking about the robustness direction
and how these two things interact so
just to be clear about what we mean I
think this this this this video has been
widely circulated so I apologize if for
people who are already familiar with it
but you know about about a year and a

[03:05]
half ago we you know we were we were
training lots of flash games using RL
and you know there there happens to be
this boat race game so you know I I just
set lots of lots of games running with
with a reward function so the way this
boat race works is supposed to go along
the course and you're supposed to that
you're supposed to finish the course but
the way the reward function works and
it's hard to reach in and write a
different reward function is you get you
get points for you know these markers
along the way that are mostly along the
course but it turns out there's this
this little Lagoon in the corner of the
course where you can go around in
circles and get more and more power-ups
and that turns out to get you a faster
rate of power up to naturally finishing
the course there's nothing wrong with RL
here the system did what it was supposed
to do but it identifies the weakness of
the connection between a reward function
in the final behavior the reward
function that you specify that you may
think corresponds to some behavior that
you want may in fact correspond to very

[03:06]
different behaviors and you get no
feedback on that other than just finding
out what the system does right when I
first trained this I trained along with
a bunch of other games
two days later I looked at this I'm like
what what in the world has what in the
world is this doing it doesn't make any
sense and then I thought about it alone
I'm like oh of course that makes sense
and you know so the more powerful the
system is the more autonomous it is the
less of human is paying attention to it
the more potential there is this is like
you know
generate dozens of these examples but
you know robotic system where we forgot
to make the table totally fixed it has a
high mass but it's not fixed turns out
to be easy it's hard to send the send
the puck exactly to the point you want
it to be it's easier to send the puck
observe if it's gonna be a little to the
right or a little to the left and then
nudge the table so that it hits it
exactly it's very it's very clever it's
a correct solution to the problem but
the problem was not the right problem so

[03:07]
the general approach that we've kind of
hit on and we've been pursuing the
strategy for about a year a year a year
a year and a half is that the this
training loop is too long right the
human at the beginning says here's a
mathematical roared function like go go
optimize this then you look back at the
end of training you might get the right
thing you might not if you don't you
have to go back to the beginning or you
know maybe the system is already doing
something dangerous so maybe we should
have humans be involved interactively in
the training process right when we train
humans to do things it's not just like
here's your goal go off tell me what you
did you know two weeks later so if we if
we do this is there a way that we can
use a human to decide what the reward
function is in a continuous way that's
more reliable that's more naturalistic
so that the system ends up imbued with
human goals and values but it's able to
act faster and bigger than human scale
once it's trained it knows what the
human wants and it does it example of
this is like instead of RL we can learn

[03:08]
from demonstrations but that kind of has
the same problem a human demonstrates at
AI system copies it and there's kind of
it's hard it's hard to do better than
the human it's hard to course-correct
it's hard for the human to say you
should be doing this instead of this and
traditional RL has has a loop that's too
long so the kind of first effort we did
in this direction was we called it deep
RL from human preferences so the idea is
you know I want this thing to do a back
flip and I you know it's hard to
mathematically specify the reward
function for a back flip
we tried by looking at all the
individual joint angles and you know it
turns out it just gives you some
think very very like you know very
awkward looking but what we do instead
is and you know this is now running for
the second time but a human looks at the
behavior of the system and says which of
these is more like a backflip than the
other the system just starts by acting
randomly it has it has just like a

[03:09]
random reward function and human gives
it feedback on what what is more like
what the human wants and then the AI
system you know like the the RL system
has a reward predictor and it tries to
fit a reward predictor consistent with
what the human says the human prefers
and then in the background it's running
a whole bunch of copies of of the RL
environment and those copies optimize
the reward function that it learns from
the human the human only ever has to
give feedback on a very small fraction
of the AI systems behavior doesn't have
to see everything it does just has to
get enough samples to give the to give
the policy an idea of what the reward
function should be so another way to put
it is the human trains the reward
function and the reward function trains
the RL system so what I just said can be
kind of pictured in this the grey part
is the standard set up for for for
reinforcement learning where you have an

[03:10]
RL Aughra than the environment they
exchange observations and actions and
there's a reward that kind of that kind
of you know comes from the ether that
was ultimately specified by a designer
but that isn't thought about as being
part of the problem here what we have is
that reward starts out being completely
random and the human sees examples of
the agent's behavior and feeds them to a
reward predictor so the reward predictor
is changing and improving and adapting
over time and the RL system is both
learning from the existing reward
function and adapting to changes in the
reward function
so we did several versions of it in our
paper and we found that a simple active
learning technique helped relative to
random it didn't help by that much but
but it helped the idea is you train an
ensemble of reward predictors that are
trained on subsets of the data and that
that allows you to have kind of like

[03:11]
semi independent predictors and you can
pick examples where the predictors are
uncertain meaning that those are parts
of the space or situations where there's
just the reward predictor has more
uncertainty and so would like more
feedback from the human that helps you
can go much more sophisticated in that
direction right the system could like
ask the human like what you know like
you know what what am i doing that's
wrong what am i doing that's not clear
the human could say to the system like
you know I'd like you to produce some
examples of this right and then it
becomes much more like a like teacher to
human teacher to human pupil teaching
process and a lot of what we're doing is
kind of going in that direction but we
kind of have to start so imitation
learning has the following limitations
when you do imitation learning you
except for noise reduction which is
usually a small effect you can't perform

[03:12]
better than the human does so as we'll
see in some future tasks here there are
cases where learning from preferences
allows you to perform better than how
the human does the reason for that is
with imitation learning you just do what
the human does here you learn what the
human wants and once you learn the
reward function you could do it better
than the human right so consider
something like you know if I didn't know
how to play go I can teach you the rules
of go and then you can do RL on the
rules of go and get much better than me
or you can just copy my moves if you're
just copying my moves you can never do
better than me if I teach you the rules
and then you use RL to learn how to
learn how to play you can you can then
you can then in principle do better
another another difference is you tend
to get kind of like
better sample sample you tend to get
like better sample efficiency you can

[03:13]
come up with strategies that a human
wouldn't would you can come up with
strategies that human wouldn't have
thought of and many tasks a human just
can't do so actually this backflip task
it's actually very hard for a human to
demonstrate that task like you'd have to
get a VR setup and if we look at like
the tasks of the future right where you
know like let's say I want to defend you
know a large corporate IT network or
something and I want to respond to
threats in real time that's just
something where I I can't get training
data from a human I'm asking the machine
to do things that a human can't can't do
which is what we ultimately want AI
systems to be able to do does that kind
of answer the question yeah so we have
an option in this paper for basically I
don't know or I think we had separate
options for I don't know or it just
throws out the data or these two look
about the same in which case it like

[03:14]
waits them equally in the predictor and
in yeah so that's that's easy to
incorporate I think ultimately the
communication needs to be in terms of
language and not in terms of clicking
left or right and then that will kind of
like make a richer space for doing
things and saying I don't know or like
show me some other examples these things
aren't comparable at all become much
more common so the nice thing about this
is given an environment without changing
the code at all only changing what the
human provides as feedback you can get
totally different behaviors so in about
half an hour a human can train this this
are all system this is like simple
simple atari enduro game i can train it
to do the usual thing which is to to
race ahead of all the other cars but i
can also train it to go exactly at the
same speed as other cars and when it
does that you know it's able to actually
get there very very effectively like you

[03:15]
know stay exactly even with other cars
which isn't it isn't easy you have to go
at kind of exactly the same speed and
match their speed and so
exact same code just the human provided
different different feedback one thing
we show is if we don't give you the
rewards for Atari games we just hide
this hide them from you humans giving
feedback on basically you know trying to
get the system to get the highest score
that it can works really well on the
kind of right of each panel those like
colored bars that are moving that
represents how much reward the system is
thinks that it's getting or just how
much how much it thinks to give an
action is good so if you look at the
breakout case when the ball hits the
paddle instead of so on the Left when
the ball hits the paddle instead of you
know instant instead of instead of the
ball going to the bottom it says yeah I
got a lot of reward from that same with
pong the when it surfaces to get oxygen
and Seaquest it's very very very high

[03:16]
very high reward level so the predictors
seem to correspond to what you know to
what human would say is good behavior
which is not surprising because of human
training them so we did did a bunch of
we did a bunch of experiments and you
know with fixed reward Atari games your
goal is just to do as good as you would
if you knew the reward right so you're
like hiding the reward from yourself and
you're trying to learn the reward from a
human so most of the time it does it
does almost as good but actually there
are cases where it can do better
we're in enduro that the algorithm we
used a3c has trouble learning enduro
because of sparsity of the reward but a
human actually helps to shape the reward
right in enduro you have to like kind of
like read the control stick to go at a
certain speed in order to get in order
to get any reward at all so you can
start you can start to move and the RL
system doesn't give you any reward and
then you have to keep moving faster and
faster to get reward and some some

[03:17]
algorithms never figure that out but the
human will basically say okay yeah you
went ahead you made progress that's
better than when you're not moving and
so little by little with just with a few
feedback points it can lead the system
and so the human can shape the reward
and they're actually cases like the the
curve for enduro in the bottom right
where you can actually do better than
the human did or you can actually do
better than that
standard then a standard oral algorithm
did even though you had less information
instead of knowing the right reward
function you just had a human indicate
the reward function also works for a
bunch of kind of like simulated robotics
tasks we haven't really tried it in the
real world relevant to the question
about demonstrations we've we actually
followed this up with an effort
combining human feedback with
demonstrations so what that did is you
know there's some tasks
human can do it but we liken it you we'd
like the RL system to do it better
however we can initialize from human

[03:18]
human demonstrations the AI system
copies that but then on top of that on
top of that initialization we run RL RL
with human preferences so there's no
reward function there's no like
programmatic reward function anywhere
it's entirely learning from humans but
the first step the human demonstrates
and then the second step the AI system
copies in the human says it would be
better if you could do it this way and
again the second step allows you to
exceed human performance or do tasks
that humans can't do right the humans
like this is as well as I know how to do
it the AI system copies that the the
human says you know ok well I wouldn't
be able to do this myself but if you
move back and forth really quickly and
shot those two ships that will be better
than if you didn't do that the AI system
is capable of that and so it can
bootstrap itself to kind of beyond
beyond human capabilities more recently
and we don't have any work out on this
but I think we will soon we've started
applying this to natural language so in
the last year or so there have been kind

[03:19]
of big a lot of progress on large
language models like open the eyes GPT
and google's burt where you just take a
big corpus of text you train just just a
big transformer model to to predict the
next word or the next token and that
allows you to generate very coherent
text and can also be fine-tuned to solve
a lot of linguistic tasks so one one
idea there is can we find two NAT via RL
from human preferences right I have a
language model it's
a lot of text some of its happy some of
its sad five five minutes yeah you know
some of its formal statements or
informal statements some of its jokes
the language model maybe has some idea
in its internal representation of the
difference between those things but you
know if I just sample from the language
model it just kind of gives me random
samples of stuff so can i push this

[03:20]
language model in directions and to
produce behaviors that only a human can
specify that can't be specified
programmatically so things like
statements that rhyme or our-our
statements that are in iambic pentameter
could you make a system that is you know
from the logic of learning from human
preferences is a better poet than any
human could be or something like this or
you know makes makes like very positive
sentiment statements that are you know
that it's hard to find enough enough
positive sentiment statements to to copy
from so that's the direction we're going
in and then I think you know like a long
term vision for it would be you know we
would you know we want a system that
basically has an ongoing dialogue with
with a human the human asset to do
something really complicated like
planning and executing the mission to
Mars you know the system kind of kind of
clarifies ss4 instructions while it's
learning and while it's doing the task
and we make sure that that things like

[03:21]
pathological solutions the problem don't
happen one way to get to Mars really
quickly is you know to escape from Earth
and propel yourself by dropping a bunch
of like nuclear explosions back at earth
that would work that would get you to
Mars this project called the Orion
project in the 1950s although plan was
to detonate the nuclear weapons when
they were like far away from Earth but
this is not a solution we would favor
how do we make sure that that that AI
systems don't don't do things like that
cool so I've only talked about a subset
of what the safety team is working on
but you know we have around 15 members
here some of some of these efforts were
done in collaboration with with with
deep mind and various various academic
and
we have a number of kind of interns and
faculty affiliates but you know we're a
safety team is is is continuing to hire
and we're we're interested in you know

[03:22]
further advancing these and these in
other areas thank you so much sorry oh
hello everyone we are now at the
conclusion of today's morning talks but
before we break for lunch I would like
to invite all of the volunteers who are
joining us today from open AI and
Berkeley and New Haven school to please
come up to the front so as we proceed
into the afternoon hackathon and
breakout sessions these will be the
faces that will be around to help you
that you should ask questions to these
people are all talented researchers or
contributors or engineers in this space
many of these people are employees of
open AI ever and we also have I think
the only person here who's not currently
employed by opening I was previously
employed by open AI so if you want to

[03:23]
pick our brains about what it's like
here what we do why it matters please
feel free can we just have everyone get
maybe a sense to introduce themselves
sure I am Daniel I work on the safety
team as a male engineer working on the
language fine-tuning project from a
human feedback
yeah Matthias I've owned robotics I'm
Ethan I'm on the safety team working on
model-based or LM safe exploration with
Josh I'm Carl I'm on the games team
primarily studying transfer learning and
procedurally generated environments my
name is Dylan I'm a PhD student at UC
Berkeley and I mainly work on preference
learning I'm Amanda and I'm on the
policy team here opening I I marry I
work on the safety team on safe
exploration alright and another thing
that I want to say thank you all so much
for being here today something that I

[03:24]
hope we can do is really make this a
useful experience
for all of you and I hope that over the
course of the day that you know you give
us feedback about what you find helpful
and not helpful and what it is that
you're hoping to get out of this
experience so that we can figure out you
know how to help you get to that and and
thank you so much please enjoy lunch

</details>
