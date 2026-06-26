<!-- source: https://openai.com/index/openai-scholars-2019-final-projects/ -->

May 23, 2019

[Company](/news/company-announcements/)

# OpenAI Scholars 2019: Final projects

Our second class of OpenAI Scholars has concluded, with all eight scholars producing an exciting final project showcased at Scholars Demo Day at OpenAI.

![OpenAI Scholar presenting their 2019 Final Project](https://images.ctfassets.net/kftzwdyauwt9/202daa66-eb15-4738-9fee34033d24/90d1c6c62eb4efa529a51905b6ddbef8/openai-scholars-2019-final-projects.jpg?w=3840&q=90&fm=webp)

2019 Scholar Janet Brown. Photo: Blake Tucker

Over the past three months, we’ve seen how experienced engineers working in software, medicine, physics, child development and other fields can become machine learning practitioners with our combination of educational resources and mentorship.

* [Rewatch demo day(opens in a new window)](https://www.youtube.com/watch?v=4u218xVkjmQ)

<!-- yt-inline:4u218xVkjmQ -->
[![OpenAI Scholars Demo Day 2019](https://img.youtube.com/vi/4u218xVkjmQ/hqdefault.jpg)](https://www.youtube.com/watch?v=4u218xVkjmQ)

<details>
<summary>자막: OpenAI Scholars Demo Day 2019 (2:31:27)</summary>

[00:00]
you

[00:14]
hello everybody we're gonna go ahead and
get started
fantastic welcome to open AI scholars
demo day thank you all for being here
this evening we have eight presentations
tonight as a result of our Scholars
program we had 550 people apply and
eight scholars so that makes us a bit
more competitive than Harvard but you
know we don't want it we don't want to
break any who and the scholars have
spent the past three months studying
machine learning full-time two of those
months have been spent on a
self-selected curriculum going through
the different skills that they need to
be able to complete a final presentation
which they will be showing to you today
this is a project that they've completed

[00:15]
in one month which I've been told is a
very short amount of time to complete a
experiment in machine learning when you
are just a beginner however they've been
assisted by our really awesome mentors
who are a combination of opening eye and
external folks and we're really excited
to have everyone here so I'm gonna go
ahead and pass it off to Ilya who's
gonna say a few words before we get
started
Thanks hello everyone and welcome to the
scholars demo day it's really exciting
to see the projects that the scholars
were able to accomplish in just one
month one thing about machine learning
is that it's not the easiest field to
enter without mentorship and working
closely with a good mentor can really

[00:16]
narrow down the very big surface area of
machine learning down to manageable
pieces that make progress far more
rapidly and I can say for myself I
definitely wouldn't be where I am
without the mentorship that I received
so with this I want to say thank you and
real gratitude to all the mentors who
helped bring the scholars to where they
are right now
and finally doing a project is just in
just one months is not an easy feat at
all so congratulations on the scholars
who've done this and let's see let's see
the projects
[Applause]

[00:17]
thank you for coming to our demo day
today I'm going to talk about exploring
gamma the discount of the future or the
weight of the past so here's a bit of
background for those who are unfamiliar
with reinforcement learning it is the
framework where an agent takes action in
the environment to maximize cumulative
rewards so the measure we care about X
the expected sum of total rewards and
the measure we actually optimize is they
expected sum of total discounted rewards
so the difference of here is the
discount and not only it prevents us

[00:18]
from getting explosive sum to infinity
but also it injects some preferences
which I'm going to talk about so what is
discount factor from economics this
discount factor gamma specifies some
intertemporal temp preferences and what
I mean by preferences is to imagine a
thought experiment where if I hand you a
full approached moral or some gamma
fraction of an apple today and then I
twist the gamma until you find the
single gamma that you are indifferent
between the two then this gamma reviews
your preference so with this preference
in mind let's look at a toy example in
some simple grid word experiment here we
have two agent one has a low discount
preference so it will have a what prefer
immediate rewards such as the coins on
the Left which has lower value or the
agent on below has a high discount
meaning it will prefer long-term future

[00:19]
reward which is attainment so we can see
different preferences results in
distinctive behavior that agent could
express as a beginner 2rl algorithm we
may just ask which discount factor gamma
to use well some will tell you 0.99 or
otherwise say something close to one no
no not one for boundedness and some ways
say just try a set of commas and pick
the best so none of these answers seemed
entirely satisfactory so
I found out this about Blackwell
optimality principle actually says that
in all environments there exists an
optimal policy that simultaneously
optimal with gamma higher than some
threshold so looking at this principle
we may find it quite intuitive because
given some real world environments where
we always a maximize cumulative reward

[00:20]
that applies gamma equals 1 however in
real what we can now use gamma equal to
1 but having a gamma of 0.99 results in
a very similar intertemporal preference
as a gamma equal to 1 having a gamma
0.99 in the diamond case in the in the
grillwork case the agent will still pick
diamond over the coin despite having a
slightly lower discount factor so the
question I'm interested in is to tip our
algorithms always find the Blackwell
optimal policy for gammas above the
threshold well let's go back to this
time we'll use a lower exploration
instead of Hayek's persian in the
previous case and we see the behavior is
the same for the low discount agent
however for the highest own agent it
cannot obtain any reward so not
necessarily in this case that Alton
power algorithm could find this kind of
optimal policy so in this work we will

[00:21]
demonstrate this issue and propose
methods to repair it to do that I set up
to world war environment one with sparse
reward the other with dense reward so
the agent in red is trying to collect
all the yellow coins which will give
them positive reward and they want to
avoid poison we shall give them negative
reward and lastly they they don't want
to get trapped otherwise they will die
so the algorithm I use is from baselines
overnight spaced lines D queuing and
then the experiment setup is I only vary
the discount factor and keeping
everything else constant and here's the
initial results on the sparse
environment so I pick a set of gammas
from 0.1 0.2 0.5 0.8 and 0.99 as you can
see on
right curve the highest gamma 0.99
yields the best performance and this
seems like there might be a stretch
between gamma 0.5 and point 9 0.8 such

[00:22]
that above that all gammas or high
gammas yield optimal performance so this
is quite consistent with the back
blackwell optimality principle let's
look like how let's look at how this
will work in a dense environment so here
we see that the highest gamma which is
in pink 0.99 is actually not doing well
it's not even doing as well as the gamma
0.5 in this case so we see some
inconsistency with the Blackwell
optimality principle let's dig further
so after thinking about it my hypothesis
to this behavior is that discount factor
may play a dual role in DQ and update
and specifically it not only explicitly
specifies that intertemporal preferences
which is to discount the future but
implicitly it includes some confidence
on bootstrapping of the function

[00:23]
approximator
which is to weighing the past so I
proposed a time variant discounting
gamma of T so that when we specify a
male pick five a fraction that's a some
fraction of the total time steps and
during that period we are going to vary
our gamma from 0.1 to a final gamma that
we specified so that they have a linear
schedule then we wait earlier
experiences less the gamma will keep
fixed after the myopic fraction fraction
so using this simple scheme on the dense
environment
t queuing algorithm let's compare the
experiments so the pink curve is still
the fixed gamma from the in the dense
environment and although other colorful
curves are always different myopic
fraction and to see this more clearly I
grouped all myopic fraction setups in a

[00:24]
single block in blue and you can see
other myopic fraction no matter how
large it is outperforms the basslines
algorithm with fixed gamma and because
0.99 what wasn't doing well and then
with this initial myopia it could
actually become optimal so this is a
really good result and let's see if it
can work in the path gamma which is 0.8
in the tense environment so I do the
same thing where the pink curve is the
fixed gamma 0.8 which was the best gamma
in the dense environment and all the
myopic fraction are in blue on the right
side and then we see that any male fake
fraction could eventually achieve the
same level of performance as the
original fixed gamma and just take
longer so what about the sparse

[00:25]
environment so I tried the same thing
where on the yeah so we have the fixed
gamma on the left we have gamma of 0.8
on the right we have gamma point 99 and
you can see subsequently as we increase
the myopic fraction the longer it takes
to reach optimal but they reach optimal
nonetheless so fixed gamma yields the
best performance in this sparse
environment but all my opaque fraction
converts to optimal eventually so it
doesn't really hurt in the long run so
summing up from all this initial amalia
results we see that high discount gamma
could become optimal with initial myopia
and the benefits of this simple scheme
is that we don't need to find humour
because it improves learning intense
reward environments and doesn't harm
learning in sparse reward environment
however you may say that all our
hypothesis is that this initial myopia

[00:26]
will mitigate bias thus better
performance there might be a competing
hypothesis is by introducing this
initial myopia you may have more
exploration which might lead to better
performance so I'm trying to see whether
this benefits is result of bias
reduction or exploring
to do that I set up three experiment
where are fixed the discount factor and
for the baseline setup I have zero
myopia and load low exploration for the
myopia setup I have low myopia and low
exploration and for the exploration
setup I have zero myopia and high
exploration so to see the results let's
look at the plot on the left here our
gamma is fixed to be zero point eight
across our three setups and for the
baseline it is in pink and then we see
that it has similar performance as the
myopia which is in orange and

[00:27]
exploration actually did worse than both
of them as it because it takes longer
and on the right we have our gamma of
0.99 which is considered the poor gamma
in the dense environment and we can see
with myopia actually outperform post
baseline and exploration and with the
exploration although is eventually
surpasses baseline a bit but still takes
a long time so we can sort of conclude
that exploration helps but not
significantly and it takes longer
training time but with myopia it
improves significantly and converges
faster so as part of the future
directions we try to formalize this dual
role intuition and run more experiments
on standard testing ground and I will
also want to compare a myopia schedule
lambda versus gamma in PPO I have some
initial results and happy to discuss

[00:28]
offline after the presentation so just a
recap here some related works and final
takeaway discount factor matters in deep
reinforcement learning and it has a dual
role that specifies intertemporal
preferences and also includes confidence
on bootstrapping from function
approximation and a simple myopic
schedule is a robust and effective way
to improve performance and the same
logic may work beyond EQ
and discrete action state framework
thank you I'm happy to take questions
[Applause]

[00:29]
yeah so in the baselines dqn they have
the similar linear schedule for
exploration where it started low I
started high and become low and stay low
for the whole time yeah
hello I was wondering if you can think
of a way so I really liked this idea of
seeing Gemma as something that kind of
enclose your confidence do you think
there's a way to kind of like take you
uncertainty into account more directly
it seems like you're currently doing it
over time but do you think there's a
there's a way to like make that more
explicit by I don't know getting some
uncertainty estimate for your cue
function thank you it's a really good

[00:30]
question I'm thinking to first try it on
the generalized advantages estimate
because it exhibits basically separates
out lamda and n gamma in the equation
where I feel like lamda is precisely the
role it plays in our confidence in
bootstrapping so I guess by varying
lambda perhaps in the algorithm PPO
could help with this issue yeah
any other questions
[Applause]

[00:31]
okay so I'd like to begin by thanking
everyone at open AI who organized this
event you can't hear me how about now
okay and I'd also like to thank all of
you for attending so previously I was a
PhD student at the University of Chicago
where I studied cell biology but these
days wood excites me most is the
prospect of getting general-purpose
robots deployed in the real world and
then getting them to do useful things
and so one challenge associated with
this is that robots will have to learn
how to solve new tasks with little to no
external feedback so for the past month
I've been working on a project that

[00:32]
leverages a robot's internal motivation
and over in order to overcome this lack
of supervision so I'll start by placing
intrinsic motivation in the context of
reinforcement learning so in the
reinforcement learning setting you have
an agent that interacts with an
environment via its policy so the policy
takes in observations and outputs
actions so at every time step the agent
takes an action and receives a reward
from the environment so by learning to
maximize its total expected reward the
agent can find a good policy and
eventually learn how to solve a given
task but finding a good policy can
actually be very difficult when the
rewards from the environment are sparse
so what we really need our reward
functions that are intrinsic to the
agent instead of relying solely on
sparse extrinsic rewards okay so how do

[00:33]
you get how do you get dense intrinsic
rewards so there's actually been a lot
of work in this area but most approach
that are a lot of approaches Center on
some notion of novelty so by seeking
novelty the agent is driven to explore
and in doing so learns new skills that
might help it solve a given task
and so this approach is actually had a
lot had a lot of success recently with
solving challenging Atari games like
Montezuma's Revenge
however these ideas haven't really been
applied to robotics so in this project
I'll show you how using a simple
formulation for intrinsic rewards will
lead to nice solutions for solving
challenging robotics problems so before
I discuss the method that I use I'll
talk about the fet robotics environments
which were developed in-house at open AI

[00:34]
by matthias sitting in the back and so
the observations include the position
and velocity of the gripper and it also
includes the pose the linear velocity
and angular velocity of any object that
might be in the same the action space is
continuous and it's four dimensional and
it includes the first three dimensions
correspond to change in position along x
y&z and the fourth dimension corresponds
to opening and closing the gripper and
so again we care about the sparse reward
setting so here the agent receives at
every time step award of 0 if it solves
a task and negative one otherwise and I
just want to point out that for all of
the environments that I'm going to talk
about which include reaching pushing
sliding and picking place the agent has
at most 50 time steps to actually solve
the task ok so here's an outline of the

[00:35]
method that I use so the diagram on the
left you can see that it's very similar
to the reinforcement learning setting
that I talked about a few slides ago but
here in addition to the agent having a
policy it also has a dynamics model so
the dynamics model takes as input the
agent's current state and its action and
it makes a prediction for the next state
and I also want to note that we we could
set up the dynamics model to make
predictions for the robots change in
state
and so here's the intrinsic reward his
intrinsic reward that I'm using and what
you'll notice is that it's simply the
prediction error of the dynamics model
and so larger prediction errors should
lead to larger intrinsic rewards and so
the idea is that the the idea is that
the agent shouldn't get stuck in regions
that it's already explored and instead

[00:36]
will be encouraged to explore elsewhere
okay so for training I use simple fully
connected networks for both the policy
and the dynamics model I train the
policy using PPO which is an actor
critic architecture that was developed
here by John Shulman and briefly since
PPO is on policy I use a number of
actors in parallel to collect a large
and diverse set of data that can
actually be used to update the
parameters of both the policy and the
dynamics model okay so here's my first
set of results so I'm applying this
method to first to the simplest of the
tasks which is reaching and here I'm
comparing a baseline PPO implementation
with no intrinsic rewards to intrinsic

[00:37]
rewards that were that were generated by
predicting the full neck state or by
predicting the change in state and so
for a simple task like reaching it turns
out that you don't actually need the
intrinsic rewards but adding them you
you can see that the agents learns to
solve the task much more quickly and you
can see in the bottom panel that as the
agent learns the intrinsic reward
actually goes down okay so I next looked
at the pushing task which is actually
quite a bit more complicated than the
reaching task so unlike reaching the
baseline policy is not actually able to
solve this task but when you add in the
dense intrinsic rewards you can see that
the agent quickly learn
how to solve solve the task and near the
end of training its solving nearly 100
percent of the episodes and so when I
approach the pushing task I actually
looked at a number of different hyper

[00:38]
parameters and so I'll talk about three
here briefly so I looked at the size of
the individual layers within the network
and as you might expect larger networks
tend to perform better than smaller
networks I also looked at the learning
rate for the dynamics model and so this
actually turned out to be very important
so as you can see here smaller learning
rates tend to outperform larger learning
rates and the last thing I looked at was
saying whether or not resetting the
environment early after the agent has
already solved the task will lead to
better performance so that's where you
can see here so after the agent has
solved the task by doing an early reset
that leads to a significant boost in
performance ok so I next looked at the
pick-and-place task and this s is
actually step up in difficulty from the

[00:39]
pushing task but here the story is more
or less the same the baseline policy
cannot solve the task but adding in
either intrinsic reward can actually
lead to the agent learning how to solve
the task and for reasons I don't quite
understand yet predicting the full next
state tends to outperform predicting the
change in state so that's something I
want to look at a little bit more in the
future ok so the last thing I looked at
was a sliding task it turns out that by
comparison the sliding task is probably
more difficult than the others and so
here I actually needed a larger Network
than what was required for the others
for the other tasks and I also needed
twice as many environment interactions
for the agent to learn how to solve this
okay so to summarize consistent with
previous works my results demonstrate
that adding intrinsic rewards can
actually be useful in solving
challenging tasks with sparse rewards

[00:40]
although unnecessary
for solving the reaching task adding
intrinsic rewards as an exploration
bonus actually leads to improve
performance and intrinsic rewards were
actually necessary for solving a more
difficult task so in the future I plan
to look at slightly more complicated
tasks such as tool use and block
stacking and I also plan to look at
different kinds of inputs both both for
the policy and for the dynamics model
and in particular I'm really interested
in looking at combining different sensor
sensor modalities so looking at
combining images with depth maps with
contact information okay so with that
I'd like to thank Maddie for organizing
the Scholars Program I'd like to show my
appreciation to scholars past and
present I'd like to give a special thank
you to Matthias Alex and Lillian they

[00:41]
gave me really good feedback that I was
able to use to make modifications to
fetch environments I'd like to thank
Yura Harry Igor and Wojcik with all of
whom I've had really enlightening
conversations and I'd like to give a
special thank you to Yura and Harry
whose previous work was actually the
inspiration for this project and last
but not least I'd like to thank thank my
mentor for y'all who provided me with a
lot of encouragement and support over
the last couple of months so with that
I'd be happy to take any questions
[Applause]
have you tried Alice tiems is that
awfully that's a good question probably
when I start to incorporate different
sensory modalities I'll have to move to

[00:42]
using Elysee Ames also may help with the
Delta version of the inputs yeah I could
so I wanted to try it originally but the
the simple method that I used already
had such good performance that I'd sort
of put that off any other questions
was was there any stochastic
stochasticity in the environment yes so
every time the environment was reset the
target location would change and if
there were a block in the scene the
starting location of the block would
also change oh I see was there any
stochasticity in the transitions like
from one point in time to the next point
so like this kind of movement there was
no stochasticity the movements were
completely deterministic I see

[00:43]
how important was it to trade off the
goal-directed reward versus the
intrinsic reward like did that require
some tuning or not so much
I think most of that tuning came from
tuning the learning rate for the
dynamics model because at the if the
Dyna if the learning rate for the
dynamics model was too big then the
agent would very quickly learn how the
environment worked and so the intrinsic
rewards I would get would be really
small whereas if you delayed that it
would get larger rewards early
encouraging exploration but if you're if
you're referring to like the size of the
rewards the relative to rewards say
negative one versus with the intrinsic
reward was I did tune that quite a bit
turns out one works really nicely which
offsets the reward of negative one from

[00:44]
the environment yeah what larger rewards
don't work and smaller intrinsic rewards
don't work any other questions great
thank you
[Applause]
you
hi everyone thank you for being here
tonight and louder okay is it any better
okay thank you so um welcome so I will

[00:45]
be talking about my experiment with fine
tuning GPT two small model for question
answering tonight before I start to talk
about giving you two details about my
experiment I would like to mention the
question that I was interested in which
guided me in my decision to work on this
problem one of the biggest challenges
that we have in natural language
understanding today is the ability to
create systems that have common sense
neat reasoning which is the ability of
an intelligent system to come up with
common-sense knowledge and reason about
a given text so this is still a
notoriously difficult task and although
we have very high-performing language
models and systems today we are still
struggling to perform better in this one
so in this chart you will see you notice
that there's an increase in the
benchmark models and data sets that have

[00:46]
come out in the recent years that are
targeted exclusively for common sense
reasoning especially in 2018 alone we
have a number of data sets that were
specifically designed for common sense
reasoning and you will realize that most
of them are targeting the task of
question answering so reasoning is
necessary in in performing better better
especially in most of the NLU tasks
that's because most of the time we will
not have the solution given in a
linguistic context and there will be a
lot of ambiguities in the language that
we need to our systems are intelligent
systems needs to be able to figure out
so this is this is one of the reasons
why I
I chose the task of question answering
for my fine tuning first of all QA is

[00:47]
one of the most important natural
language understanding tasks that will
allow us to measure how a system is
doing in terms of common-sense reasoning
in addition to that QA requires a mix of
language processing and reasoning skills
within a single task and that's why it's
more practical than probably dealing
with some other more complicated than
defined tasks in addition to that better
reasoning achieved to create systems
could be applied to a variety of systems
that is not limited to natural language
processing or understanding such as
vision and robotics the examples of
which we have started to see lately so
the approach that I take in my project
was to analyze the patterns that a
fine-tuned GPT small performance on QA
tasks could reveal about how a language

[00:48]
mount model attains and performs
reasoning so for this I have
experimented with this small model and
finding that on the Stanford
question-answering dataset for those of
you who are not familiar with the data
set I will I will be giving some
informations about that oh sorry I meant
to go back the statue of the models
amount of architectures that I have
worked on the first one you see on the
on the left is a linear classifier that
I put on top of GPT to a small model the
first public release one and the one on
the on the right will be a bio SCM in a
naive attempt to circumvent and
bi-directional uni directionality of GPT
to most of my results will be based on

[00:49]
the linear model because after going
through a lot of hyper parameter tuning
and
I noticed that actually new model
perform better for those of you who are
not familiar with the squat data side
squat dataset contains over a hundred
thousand question-and-answer pairs and
which which have answers and it also has
the point tube model also has over fifty
thousand unanswerable questions with
some plausible answers added and if your
model comes up with those plausible
answer is still very informative about
how your model is doing in these two
examples that are taken from the data
sets you will see that the question with
the answer is a very factor it's styled
simple question and the one on the other
side which has a plausible answer but
you cannot actually retrieve the answer
from the from the passage that is given

[00:50]
for that question so my model was these
are representative of some of the
questions that my model was able to
answer correctly or abstain from
answering because it did not have an
answer in the data set squall has in the
development Setsuko has over 11,000
questions and 5000 of which is
unanswerable and because I thought
focusing on the unanswerable questions
and the performance of the model on this
kind of question or informative about
how the reasoning and common-sense
working for the model most of my the
most of the numbers and reports that I
will be presenting today based on those
type of questions although there are
other data sets that are specifically
designed for common-sense reasoning I
use squaws because it will be it will

[00:51]
give me a good start to understand how
such a powerful language model although
I'm using the smallest version will
perform in common sense and what are the
mistakes what are the successes and
failures that the model will make and it
will guide me to work on more complex
sophisticated data sets going forward so
the linear model that I implemented
worked relatively better in the
unanswerable questions where it was able
to pick up that the answered the
question did not have an answer and
abstain from answering to that in the
plausible answer section the model was
able to pick first I've seen from out a
spring like okay this question does not
have an answer but also able to come up
with the wasa it got wrong was able to
come up with the plausible answers which
was not extremely unreasonable in this

[00:52]
example this is a repeat this is
representative of the strategy that the
model learned from the training the
model takes attends to the first few
tokens in the question text when it's
trying to answer a question this
repeated so many times that I was like
okay this is this is definitely taking
some of the attention to the first few
question few tokens in the question text
and then trying to pull out the answer
from the from the passage as you can see
in this example the model predicted that
the answer contained the little phrase
that I correctly at the bottom but the
cone but the real answer the correct
answer was the the word concrete if if

[00:53]
we go back to the original paper of GPT
to I notice that some of the heuristics
mentioned in the paper such as how the
unsupervised 0 shall in zero shot
setting the create ask was taking up on
the questions like who what where and
when the same pattern kind of appeared
in the model that I also trained in here
some of my observations in include that
the model performs comparatively better
on questions that are unanswerable and
partial matches mainly consist of
initial tokens from the question and
when an answer is expressed in words
that are different from the question in
a way you can think about it as a
paraphrasing the model often fails to
recognize it if the order of the words
are different or used synonyms or
antonyms for expressing the same idea

[00:54]
the model was not performing very well
so for future directions I would like to
experiment more with the bigger model
which has been very recently released
and work more on the common-sense
reasoning datasets that are specifically
designed for this task in addition to
that I would like to work more on
natural language understanding two
unsupervised learning because the main
idea behind GPT 2 was also to eliminate
the need to fine tune models and create
task specific architectures so through
common sense reasoning I feel like
there's a lot that can be done in that
department to see if there if we can
actually do that and as a long-term goal
I would like to explore the interactions
between natural language understanding
and other deep learning research thank

[00:55]
you
[Applause]
I'm happy to answer questions
the questions okay thank you
[Applause]
no sorry
hello okay so good evening everyone

[00:56]
today I'm going to talk about my project
during the three three months Scholar
Program and the project is about
sentiment analysis using reinforcement
learning and since before I go into
details of my project I want to first
thank my mentor Azalea who gave me who
guided me in the process three months
with great passion and also thanks to
open a I provide me such good
opportunity and the rich resource to
learn and to develop my project okay let
me introduce more details about my
project first I want you to talk about
the motivations of my project with the
development of the neural network
there's an LP becomes a very hot topic
and because NLP can build the
computational algorithms and also let

[00:57]
the computer to learn and analyzed and
represent human language and there's a
lot of NLP tasks and among all the NLP
tasks sentiment analysis has achieved
very good performance and there's a lot
of well-tuned measured online so for
this project we propose some novel
models that can combine reinforcement
learning and a supervisor and the appeal
method to predict incentive sentiment
and send him sentiment of a sentence
and the currently as mentioned before
there's a lot of well chewed and also
help a lot of supervised learning method
about sentiment analysis online so I
think we consider this project and we
consider our L might self learn and
capture some missing informations based
on the current models so let me talk
about details about

[00:58]
as mentioned before we proposed to naga
models that combine reinforcement
learning and the sentiment analysis
supervised learning method and the first
model I will say or I would call it the
sentence structure in the simple words
we just like simple crucial words in a
sentence that are useful to predict the
sentence sentiment and we can see the
models here first when the model
consists two parts the first is the
policy network and the second is the
classification network we can see the
graph examples here for the sentence
restructure the first the top rectangle
represents the policy Network and that
means for each sentence for each word in
a sentence we sample based on the policy
whether to keep or repair until 8 this
word in a sentence to predict the
sentence sentiment so after the policy

[00:59]
network we actually pass the selected
sub sentence to our classification
network for example we have a sentence
and there's a lot of such words so maybe
as or as we expected we may remove those
words to predict the sentiment and also
the prediction will not be worse so
based on the selected sub sentence we
pass the sub sentence into the
classification that work and for this
classification that work it actually we
use the traditional supervisor learning
NLP method like a wave child long
short-term memory
transformer and also protein birth so so
some details on the right part we can
consider the sentiment analysis task as
a sequential decision and current

[01:00]
decision in a sentence always say
whether to keep or remove this word in a
sentence will affect the following
decisions and also affect the following
predictions
and which all this sequential process
can be naturally adjusted by the policy
weighed and measured and here we use the
delay and delay the reward that means we
cannot have the reward until we reach
the very end of our sentence once we
have the production of the sentence send
her a statement we can have a reward
with value and we take value 1 if we
predict correctly and with value
negative 1 if we predict well and for
the action as mentioned before it's just
for each word we'll decide whether to
keep it in the sentence or just delete
this sentence just delete this word in
the sentence and use the sub sentence to
predict the sentiment so this is our

[01:01]
first model and our second model I would
call we use the word probabilities in
the sentence to predict this sentence
sentiment so instead of considering two
networks we are only using one network
and will predict the probability of each
word and use the sum of the word log
probabilities to change the language
model and using PPO loss function
actually we've also tried other policy
gradient loss functions so we can also
see the model structure in detail here
so it represents our what probability
Network so for each word we have the
output we can have the output tensor of
the word probabilities after using the
protein pert Network and then we still
use the previous reward function with

[01:02]
value 1 if we predict correctly and the
value 0 if we predict wrong
so one thing we tried different with
previous is here we are not only using
the forward sentence order we're also
using the backward sentence order so in
this case we can have two probabilities
of the word sent word probability and we
can define the law
functions with only the forward sentence
other probabilities oh we can combine
using the both forward and a backward
sentence other probabilities so let's
see our dataset and the experiment here
so basically we evaluate our models
unsent and stamp resentment chip Bank
which is a public dataset originally
with five classes but for our experiment
we adopt binary labels so we use one for

[01:03]
positively positive sentence and zero
for negative sentence and here is the
detailed layers we tried for two models
first afford our first model the
sentence restructure for the policy
Network we'll use our print long short
term memory that output the action
sequence tensor and also state value
tensor and once we pass the selected sub
sentence to the classification Network
we tried transformer and the pre-trained
Burt has supervised the method here for
the frigate bird we'll just use the
simplest virgin birth the the name
should call based on case the bird model
and then we to chain the policy network
we've tried vanilla policy gradient
actor critique and proximal policy
optimization and wizards and for our
second model the word probabilities we

[01:04]
adopt protein birth again the simplest
the birth model to output the
probabilities of each word and then
define the PPO loss to chain the model
so let's see the result we've tried to
in valuation metrics one is the accuracy
accuracy metric that is we can consider
as the binary or discrete evaluation
metric because we have to set a
threshold based on the probabilities
from the softmax layer and another in
valuation metric is called the AUC
metric and this we can consider
as a continuous evaluation metric so
first we can see the left stop figure
and based on the based on the
transformer when we add reinforcement
learning algorithms with the PPO has
better performance compared to the
transformer only and for the bird we can

[01:05]
produce compare comparable result and
for the right sub figure we can see the
word probability using PPO here we are
using the post forward and a backward
word probabilities so one expect one
leap reason for the lower AUC evaluation
metric can be because per for the
embedding of the bird we are actually
considered about the position or
embedded so that means when we take the
backward order sometimes we might have
the poor performance but that's our
guest and we haven't figured out why it
has some low performance now let me talk
about the conclusion and the takeaways
for this project so first we can see for
the sentence restructure model will find

[01:06]
adding reinforcement learning method can
improve the performance based on the
transformer model and produced
comparable result on protein pert and
also I've I've grabbed the the little
words from the testing set based our our
sentence restructure model and most
words are like the such word as we
expected so this words are not very
important to predict sentiment set as
sentence segment in common sense and for
the AUC sometimes it should an
improvement with our models so this may
be a direction for our future like
stress howatuney
for the probabilities if we want to use
the accuracy magic
and another takeaway for this whole
project I think there's a lot of

[01:07]
combination with reinforcement learning
and a LLP tasks but for sentiment
analysis we should admit this task is
not a complex task and also this task is
very concrete task we just need to
predict which class the tension and the
sentence becomes or belongs to so in
this case actually with very concrete
language tasks maybe using reinforcement
learning cannot have better performance
compared to with only a supervised
learning method but maybe for more
complex language tasks like text
generation and a summarization using
reinforcement learning can have better
performance and also I've read some
paper during my project and find there's
a lot of implementation in text
generation and a summarization using
reinforcement learning and the last
thing or last the benefit for me is
during this project I got the chance to

[01:08]
handle all the supervised learning
algorithms for sentiment analysis like
long short-term memory attention
transformer and protein part and this
gave me a good opportunity to build a
pipeline with all the others to provide
the learning for sentiment analysis
thank you
[Applause]
do you find any specific reasons as to
why RL could be a better you know method
for the text summarization I think once
I'm not quite sure but my understanding
that we cannot have good performance for
sentiment analysis because we are
actually have very concrete actions we
just want we just have to predict

[01:09]
whether it's positive or negative in
this case for very concrete language
tasks it's very hard to define a good
reward function but for text translation
and a text summarization actually we can
have a very good definition or very good
define for the reward function and with
a good reward it might be trainable for
using reinforcement learning algorithms
yeah that's my understanding
maybe more complex language tasks can
have better performance using
reinforcement learning thank you
thank you so good news we're running
we're running right on schedule we're
gonna go ahead and take a quick
15-minute break we're gonna start the

[01:10]
next presentation at 6:45 so planned to
be back in your seats a minute or two
before then and thank you all so much
you

[01:28]
besides therapeutical treatment for
disease for example in this situation
the doctor at each time doctor leads to
decide whether to do mechanic validation
or vasopressor and the reward is whether
the patient will like discharge the from
hospital helped to fool house
just doesn't work
in drug discovery researchers needs to

[01:29]
develop some new drug structure in order
to cure some disease at each state they
start with the simplest structure and at
each state you need to decide how to
grow this structure to to some desired
properties of these components so in
this situation exploration and exploit
exploitation is really important and in
some less risky environments doctors
need to decide one and what kind of lab
tests need to be scheduled in some cases
the tests are very costly and also it
may have some side effect on the patient
so it's also important to decide some
optimal sequential actions on these
recently there are some literature's

[01:30]
working in this direction most of them
are model-based they are they have
simulated environments so they can get
many samples and relatively fewer paper
our focus our model 3 we work with
purely observational data in this case
they have we have limited sample size
and the current status of this kind of
research is really preliminary and there
are a lot of challenges associated with
our observational data I will talk about
this at the end of the talk so my
project focuses on sepsis treatment in
the intensive care unit the main
reference is this recent lateral paper
by Komarovsky and I used the same mimic
3 dataset which is a very large

[01:31]
electronic health record data set and I
used the same definition of subsist
cohort and the same state and action
space different from their paper
I use I use a different reward design so
in the original paper they assign
positive 100 reward to the treat the
patient who successfully discharged and
assigned a minus 100 reward to those who
deceased in the hospital or within 90
days after discharge and for the RL
algorithm they use the policy iteration
and I use policy situation as well as
q-learning and they also use E I see you
Dennis L which is a much larger data set
of electronic health record but I didn't
use that and we have a little bit

[01:32]
different in sample size so this is the
structure of my project I call it AI
physician so it basically the input is
the electronic health record and the
output is the optimal policy suggested
by our our algorithms so in the first
test
so the first staff works with the raw
data set and extracted to be regular
process the time series then with this
regular time series I extract it to
Markov decision tuples and based on it I
apply several different or our
algorithms because observational data
are always measured irregularly and
always some missing data in it to deal
with it I used to master first days

[01:33]
heuristic master for example the body
temperature are measured in saucers or
fara heads so there are some basic trend
transformation between them this can
help with us with to deal with some of
the missing data and I also use k-means
clustering so basically the states
within the same class they should have
similar
measurements so I feel some of the
missing data are using one using the
values from the observation the same
cluster and for interpret interpolation
I use sample and a whole master this is
basically approximate the time series
using the step function and we can use
more sophisticated Gaussian process so
at the end I'm interested in 24 hours
before and 48 hours after the onset of
sepsis and I extracted the sample every

[01:34]
four hours so for each patient we have
at most 18 steps for each patient so
once we have the regular time series we
can use the data to fill in the
environment and the replay pathogen is
container of Markov decision process
tuples that we can feed into the
algorithm this one example is the tag
tabular q the environment is used as a
folder that policy iteration algorithm
so we need to estimate from the samples
the transition matrix and the reward
matrix and will be playback buffer
actually did something like transform
the regular time series into M if it
happens and this structure follows the

[01:35]
open area team designed so it's very
week later if we want to try most more
sophisticated algorithm we can just
replace this tabular here with some
other algorithm so once we have the
regular time series we want to build our
MVP tapas the variable that
characterized the state are of 47
dimensions it basically includes the
vital measurements of
patient and also the lab measures these
are continuous measurement but I use a
clustering master to cluster it into 750
discrete state and also for the action
we care about two actions the IV fluid
and vasopressin toesik administrated in
four hours so this two are also

[01:36]
continuous but I put them into for each
of them up put them into like five
discreet pins
so there are 25 actions in total and and
for the reward design I care about three
things the first things is that whether
the vitals or the lab measurements stay
within the desired range so look at
looking at the first graph if the values
stay in that is a desired orange we
assign like zero reward but if it's like
outside of this normal range we we give
some negative reward that's basically a
penalty and the second thing we care
about if is that if if there is a chart
or sharp change in consecutive
measurements so if the change is smaller
than twenty percent then the reward is

[01:37]
zero but if it's larger than 20 percent
then it's going down and it's a negative
reward and also we consider whether this
patient successfully survived substance
were it's this or he or she deceased off
within 80 days of discharge so it's a
positive 50 and the legacy of 50 so in
the end we have two hundred seventy
eight thousand plus tuples and with this
whole dataset will run 400 times each
time we cut the
into training data set and testing data
set and we learned a policy on the
training data set and we evaluate the
policy in the testing data set because
that this is observational data so we

[01:38]
need to do off policy evaluation I use
weighted importance sampling with
bootstrapping and at the end we have a
hundred policies and associated miri
words so we choose the best policy with
the past memory world
the algorithm we use is the first one is
the physicians optimal policy the
dynamic programming policy with
estimated probability transition matrix
and reward matrix and the standard IQ
policy the weighted importance sampling
is for the off policy evaluation so we
have the behavior policy which generates
the sample we have and we have with our
learned policy PI one and we want to

[01:39]
estimate the value of Taiwan from the
data trajectories generated by PI zero
for each trajectory in the sample data
we define this likelihood ratio as the
ratio between how likely this sample can
appear in the four by following the
learned policy and the likelihood of
this sample so if showing up using the
behavior policy and then we
and then we define the weighted
importance sampling estimator as this
this part is the true reward of this
trajectory and this is basically the
likelihood ratio between how lightly it

[01:40]
is appeared in the learn the policy
world behavior policy and finally this
one is the estimator for one trajectory
so there are n trajectories in the
entire data set so we take the average
and then it's the value of this learn
the policy now this is the convergence
of Q learning we can see that after few
steps the the difference between
sequential a Q value and also the
variance decrease and this is the Q
table we learned for different policies
we can see that the physician policy
concentrates on five actions
so this the x-axis represents the
actions taken and the y axis corresponds

[01:41]
to the different states and you can see
that for action 0 5 10 15 this is the
action code it corresponds to very
oppressive zero that is the low low low
low as the dosage of vasopressor
it shows that the part of physicians
policy prefer low value of vasopressor
but the DP policy and Q learn is more
diffused over these different actions
this plot shows the distribution of
different actions over 750 States again
we can see that this is the vasopressor
dosage
the physicians policy many focus the
know vessel pressure dosage but the DP

[01:42]
policy and the q-learning also suggests
higher vessel pressure dosage and the
lower dosage of IV fluids we also
compared the value of different policies
trajectories so this the mean reward for
the DP policy is this value and for the
Cure policy's despair value we can see
that the Q policy gives higher reward
average on average and also this the x
axis corresponds to single trajectories
we

[01:43]
so the x-axis corresponds to 50
different trajectories so we can see
that for each trajectory
so basically it shows that pure learning
gives much better result and so the
fundamental challenges arise from the

[01:44]
fact that we work we are working with
observational data so we have limited
sample size and also we have to work
with off policy algorithm and how do we
estimate the policy from samples
generated by our different policy and in
the medical application
there's also partial observation there
may exist confounding factors and also
how to design reward functions so that
we can encode a domain knowledge to help
guide a eye physician to like a better
decision and future works is also
related to these problems
so I immediate thing we can do is we do
like more sophisticated data
interpolation for example with Gaussian
process so in that case we can sample
like more frequently in this case we can

[01:45]
get more data points then we can use
some more sophisticated method and also
there's like model-based LR if we can
estimate the environments then we can
simulate this more samples then we can
also again use that some deep R for the
algorithm and another 2 is related to
off policy evaluation and the reward
design so that's all thank you
any questions
hi thank you for your talk this is very
interesting can you go back to the
example you gave with regards to
vasopressors yeah okay great um do you
know if there's anything that you've
seen in the mimicry literature about
this behavior by the doctors I'm just

[01:46]
curious
it's like if this has been mentioned if
you men saw this mentioned either in in
like the original paper that you were
citing from yeah nature digital medicine
or like you know something with about
this kind of behavior I mean because I'm
assuming that if you don't have even if
you have a different reward like
something like this when you're taking
what the action you might take this
might have something you might see
something related to this I'm just kind
of curious about how you would interpret
this sort of behavior right so in the
lateral paper they actually mentioned
that according to some like medical
research they also found that the
doctors tends to use nest vasopressor
dosage and this case is also like active
research area in the medical field

[01:47]
how do you come up with rewards you know
you had chosen positive and negative 50
if you choose other things will to
behave will the policy change yes I
think so because this we encode like
three different things if we increase
like the magnitude of the final four the
outcome at the final step then the wait
for the is to like the vital normal
range of vitals and sharp changes will
like discrete the weight of the mood is
great so it's a very well it's a good
reward or not right yeah that's a very
good question I think for now mmm I
think for now it many depends on the
doctors domain knowledge right for war

[01:48]
we can experiment with the observational
data to see like to do some back testing
on the observation data to choose the
like the pasture design so it's a
combination of domain knowledge and some
testing very cross validation awesome
I went to a admin conference at Stanford
some time ago and there was a researcher
who's arguing for doctors against using
black box models in medicine I saw some
visualization last black box or because
you're definitely able to see some
values inside of the model so it's not
black box right mm-hmm right so for the
reward design you can actually put some
domain knowledge in there so it's not

[01:49]
that black box and then because this
works with tabular learning so it's like
the easier I think it's the easiest
algorithm on the RL so it can offer some
insights into the data in the situation
but I think if we want to use like more
like policy gradient or DDP tea then it
may not be able to offer some intuitive
interpretations but this is also an
active research area
[Applause]
[Music]

[01:50]
can everyone hear me mmm
great well welcome everyone thank you
all for coming this evening my name is
Edgar and I'm going to be talking about
knowledge distillation for transformer
language models just to give you an
overview what I won't be talking about
I'll introduce the transformer it
successes and limitations give you some
background about knowledge distillation
give you an interpretation of what
knowledge distillation can mean in this
context
I'll give you guys the approach that I
took I line some future work that can be
done and I'll have some time for
questions so the transformer model is

[01:51]
the latest and greatest one of the
latest and greatest in neural networks
that I've just come out it's very
powerful it can generate language like
human being it can answer questions he
can summarize texts and so much more
this was very powerful and very exciting
to me because I wanted to make resources
for people who might not necessarily
have resources and one of the ways to
provide resources people as is through
human language and so when I was
starting to play with these models I
went into some trouble and that's that
they're huge
my little MacBook was huffing and
puffing and crashing with memory and so
I couldn't imagine what would happened
if I try to run one of these on my phone
and so I was hoping to try to compress
these models and make them smaller while
still having similar levels of
performance and it's going to give you

[01:52]
give you guys a look like introduction
to the transformer but my peers have
done such a good job I'll skip past that
and tell you guys about what knowledge
distillation is so knowledge
distillation is getting a larger well
trained teacher neural network to teach
smaller and untrained student neural
network by getting the student to mimic
the outputs of the teacher if we say
that we give them both models the same
input and they give about the same
output you say that
student model is performing about just
as good as the teacher even though it's
smaller and in this specific context
something that what happens when we do
knowledge distillation is we give the
neural network a sequence of words and
we mask some of them and usually we have
a loss function because and when the

[01:53]
transformer spits out its output it
gives a probability distribution over
words and the goal is to try to guess
the word that is being masked and you
want to minimize this so you want to get
the word right but in knowledge
distillation we're able to provide the
student Network so much more information
by giving it the output of the teacher
so in this case we the output of the
teacher is a distribution over words
probably the ability distribution as
opposed to just a label which is one for
the correct word and zero for the others
and so what this distribution does is
give a probability over reasonable words
which will distill some knowledge into
the smaller Network so the man went to
the blank the right word is store but if

[01:54]
the larger neural network is able to
give the student the information that
another possible reasonable word is
groceries or bakery or and any other
synonym the student will be able to
learn a lot more and hopefully be able
to spit out the similar same
distribution for other words and some
more interpretation as to what this
means we have this idea that the neural
networks have a like certain solution
space and if the if we believe that we
can distill knowledge to the small
network we believe that the smaller
still
Network can inhabit a similar solution
space as a as a teacher and we see that
happening and sometimes that happens and

[01:55]
sometimes that doesn't so to give you an
example of when the case where and like
a function can inhabit similar solution
space to another function but it doesn't
necessarily do that as in this simple
case of curve fitting the green curve
can encompass every single which is a
much higher order polynomial can
encompass every single solution and
represent this function and so much more
because it has all these higher-order
terms but it usually doesn't even know
it's solution space is much larger and
that's because it doesn't have the right
inductive biases to find that solution
that we're looking for in the current
way that we train that model and so the
hope for the student and the teacher
transformer models the idea is that the
larger transformer can represent a
larger solution space than the smaller

[01:56]
one and the larger transformer converges
to a particular solution space and the
smaller transformer converges to another
different solution space and by training
these the smaller network on the larger
network we get the like region of
convergence in solution space to get
more closely to where the larger model
is so that they can represent the symbol
or if not same transformer by spinning
out the same outputs despite being a
different model with different weights
and different sizes and so my approach
to this was taking births the
bi-directional transform

[01:57]
and instead of having a either 24 layers
or 12 layers with 9 layers and I wanted
to reduce the dimension of the vectors
that it works with to 576 as opposed to
768 or 1024 and this initial approach
true proved to be awful actually
initially I had a accuracy of about 5%
even though I trained for 30 to GPU days
and upon closer inspection it kind of
makes sense because I ended up with
about 72 terabytes of data Wikipedia was
initially 12 gigabytes of text but by
saving the outputs of the student or of
the teacher their own network I ended up

[01:58]
with a ridiculous amount of data and too
much data for the GPU it was not able to
handle long sequences and that's because
for as opposed to each word having a
label I ended up with you have this huge
vector giving a probability distribution
for over words which is a 3522 size
vector and so I had to think of
something different because it wasn't it
wasn't going too well and so I thought
about the outputs of that teacher neural
network and realized that most of those
most of the information in that
distribution is not very useful if we
think about a masked word and consider a
30,000 552 vocabulary most of those
words are not going to be sending them
as most of them are not going to be
important and upon looking at them I
most of them had a dish probability of
like 2 to the negative 8 or something
very small not useful so I decided to

[01:59]
instead truncate the output of that
teacher neural network and only consider
10 words which left me with 384
gigabytes of data instead
and with the time that I had which was
about eight GPU days I was I was able to
get an increase to about a 7% and so
this leaves an exciting work of scaling
this the the big dogs
some of them sitting right here train
their neural network for 2048 TPU days
or 240 GPU days which is which is a lot
and so it leaves a very exciting
opportunity to scale up this task and
see if we can have a similar performance
so I like to thank my mentor
Susan Zhang wonderful guidance the rest
of the open area scholars or provided me
with a lot of support and Maddy Hall who

[02:00]
was able to organize all of us despite
juggling like 20 other things at the
same time thank you
[Applause]
no questions no questions okay
you
thank you so much for the support
everyone here listening to us okay and
thank you so much for a I for this

[02:01]
propionate for this opportunity
especially for my mentor okay Akuma Ram
and so before I start I'm going to talk
about myself so I was a support engineer
in my previous life I was doing network
security and after that I decided to
move to education and I have been doing
tons of things for education right now
actually I started a program as you as
soon as I shown open air I to try to
convince 60 plus year old people that AI
is important is just for Spanish
speakers and that's a picture of the
group right now one of the guys Rodrigo
is taking the lead
teaching them tensorflow to Udacity so
I'm very proud i've also do other things
i do kids and teachers that's me at
columbia showing the IGBT to unicorn
example to some very interested teachers
and and so my motivation behind this
project is that I think education is
completely broken I think it was badly
designed right now schools and and the
best way for us to learn and this is
what science is telling us is to do
projects right the way that we're doing

[02:02]
this program is to go there dive deep
into a subject and do something that is
meaningful for us and this apply
knowledge but the schools cannot use it
why I actually am on the founding team
of a school in New York because there is
no there's no curriculum for
project-based learning there is no time
for the teachers to learn how to do
themselves projects and if you have many
projects in a school in a classroom many
kids one project is a mess in the
classroom and the poor teachers are
actually implementing these things in
the classroom I spend tons of times
looking for resources on the web
adapting them and trying to like you
know customize into a classroom so right
now AI in education is just tracking is
just trying to see how we can
personalize learning but what if we can
actually unlock the educational content
in the web so this is a proof of concept
for that so this is my model it's richer
so creature what it does is that it was
trained on data from the Exploratorium
here in San Francisco actually they have
a great data set of activities there are
kind of projects that are used just for

[02:03]
learning and inquiry and we have 3700 of
these activities so I trained Bert
oh I'm not going to explain there
because I think so when we form a little
tree that already did that so I trained
bird to actually use another data set
that has 280,000 projects DIY projects
meaning like how to build a bicycle how
to cook and chill a bus or how to create
a robot that will tell me if I need to
water my plants to tell you what
products you need to do to learn
something in particular like in this
case biology so what did I chose
Instructables so you know I have to
collect my own data which Jesus got but
the thing is that instructable is a
marvelous website with very well
documented project but the goal of this
is not to learn is to make something
that is functional so if you learn if
you put in the search like I want to do
biology
injures return to 12 projects and three
of them are actually not related to
biology but they have great great

[02:04]
projects so with creature we can
actually get 200 projects and the
weather right because of the weather I
trained it we can actually get project I
have explanations on them so I'm just
going to read the first paragraph of
this project it says what does just your
heart sounds like how fast is it beating
what's the pattern a few students may be
able to detect movement will whomp part
of the beat which I got probably heard
in movies too this has to do with the
fact that I were hard has four chambers
which we will get to soon this comes
from two pairs of bolts in the chambers
of the heart
so this instructor wall was actually
meant to be done for like my students
and we have like many of these in the in
the search so right now the model is
doing 30 to 50 percent depend on the
labeled I have explanations from those
two to hundreds so how did I do this so
the way that I did it is I took all the
data from the text of all the activities
from Instructables and I divided between
four things descriptions instructions
explanations and tools and materials and

[02:05]
with that I trained bird to actually
predict what will be the learning topic
so each of these inspiratory on projects
they have some labels of what would you
learn and I end up having 50,000
examples I trained bird for like Tupac 9
to the minus 5 learning rate and I got I
took
20% of that for like validation I got
very good accuracy so I decided to try
it on destructible data so in this truck
table data again I took the task I chunk
it into a 512 tokens and then I predict
with that
what would you learn to do it so it was
good the result was kind of good but
then I you like develop this interface
to do active learning so what I do with
this is that I get the chunk of the text
that I actually match and then I can say
if it's like positive or negative and
with this I improve it a lot and you
know together a bit more validation I
use the own app library that is a
reduction the dimensions reduction
library to try to see what's happening

[02:06]
under the hood so this is a
visualization of the topic physics we
can see on the purple we can see
something here so on the purple one
that's mechanics on the blue one that's
electricity and magnetism and between
them kind of sound is bridging those two
clusters the orange is light and there
is like a tiny little bit green there
that is intersecting with with soundest
waves so actually wave somehow are very
far from sound but it's very interesting
this is like a lien under interesting -
like exploring what's happening with
these embeddings so I hope that by now I
convince you that AI can be used for
something else besides tracking in
education I would be very interested in
trying to do a web app what you can also
filter these projects by tools and time
that you have this was my eighth
experiment on the rest didn't work very
well but one of them that was promising
is trying to see what is the expertise
on these projects and I use another data
set from like hackster so I'm very
interested in like developing levels of

[02:07]
expertise on these kinds of things and
so I'm there I now look into something
to keep feeling my creature so if you
know about penny grant or something like
us to do with AI own education I would
be very interesting to hear it that's it
thank you
[Applause]
did you ever think about using video
yeah yeah so I actually that was one of
my first options trying to use video
especially from like TEDx a they have
like very cool content but I started
using pictures actually and it wasn't
very promising so then I got a little
bit like scared about trying video but I
think that's one of the things that I
would like to try

[02:08]
you

[02:09]
from a paper by a Borgia that looks at
all of the different gang metrics that
we have he evaluates over 24
quantitative measures and five
qualitative measures all of which are at
times used to evaluate ganz none of
which are optimal and none of which are
the tolkien's metric that can tell us
everything we need to know so the two
most quoted scores you'll find around

[02:10]
ganz are the inception score and the
fresh iron scepter distance both of them
are based on state-of-the-art
classifiers inception by Google and they
look out in the inception scores case
they look at marginal entropy of or
marginal distribution of labels in the
fresh eye inception distance case they
look at taking real and fake samples
putting through inception layers and at
the max pool three of v3 and look at the
difference between men and co-variants
it gives us an idea but you come out
with a scalar value so if I said to you
I have a Gann that's got a scalar value
of eight and one with 40 I'm not sure
you could tell me kind of what that
means other than a lower scores better
in third similarly in March
researchers from here at open AI and
Google released the activation Atlas
which gives us an unprecedented ability
to look inside neural networks and
visualize what's going on inside the
back black box so for my project I
wanted to look at what would happen if
we tried to bring these two things
together and evaluate ganz using the
activation Atlas so in terms of the
project I needed a whole ton of samples

[02:11]
thankfully big and the mammoth and
current state of the art Gann released
their fully trained image net generators
and so I was able to use began as one
set of samples and then SN Gann which is
the spectral normalization gang created
by me otto and others was state of the
art a few years ago and you know brought
a lot to the field especially around
normalization and it had a fydd score of
around 27 and they also open sourced
their fully trained image net generator
and so I was able to do it so we're
considering here real images from image
net and Gann samples from began with a
fydd score around eight point seven and
scan samples from SN gam with a fydd
score around 27 to see what we can find
I then took the inception v1 Network I
used v1 to be consistent with the work
of the original activation Atlas paper
for clarity I should note that the
fresher inception distance is most often
cow
headed on the v3 Network however began
actually used v2 for their calculations
and SN GaN used only 5000 samples for
their so it gives you a sense of how

[02:12]
difficult metrics are in this space
having done that
passing all of these samples through the
inception v1 network across nine layers
and capturing activations your hundreds
of thousands of amped activations right
massive amounts of dimensions to bring
that down to something that we can kind
of comprehend in at least I can used you
map to dimensionality reduce to 2d and
having done that we can then apply a
grid over our dense scatter plot to find
meaningful kind of grid clusters having
done that we then need to generate icons
for each of these grid cells so a grid
cell will contain a number of related
activations and the part that really
brings the activation to life activation
Atlas is creating these feature
visualizations which give you a visual
view of a direction in activation space
having done that we can then also
calculate the KL divergence between
distributions right because these grid
cells give us a sense of density between
the different distributions and then

[02:13]
lastly we can create some atlases and in
this case in contrast to the original
activation Atlas each grid cell in the
Gantt 'less will not only have the
feature visualization of the grid cell
but also a bounded colored order which
gives you an indication of the
log-likelihood between two distributions
so this particular example is comparing
began to SN gown and the blue dark blue
around the border means that in this
square began has a much higher density
it also has at the top the count of the
samples in the square so you can see how
many instances of samples from began
versus SN gamma in that Square and on
the bottom we have an indication of the
maximum logit which can give you an
indication of what that grid cell is
doing in regard to softmax at an indica
t'v level lastly you've also got a grid
spell reference which I find really
helpful when we're trying to talk about
these R squares and identify them so
just very briefly I've implemented

[02:14]
visualization of these icons very much
in keeping with the original page
and found like them that in regularizing
these icons it was really whitening as
you can see on the far right of the
slide here that did the most to ensure
that we had as much detail and kind of
visual fidelity as possible so what did
I find in terms of the difference
between all of these distributions and
again don't worry about getting the
numbers on here but broadly what we find
was really interesting is if you
compared began to image net layer by
layer the biggest divergence between
those two distributions actually occurs
right at the beginning of the network in
mixed 3a and 3b which is kind of
surprising in a way to me because early
on in an inception network the network
is looking at very low level detail
right it's looking for shapes texture
kind of brightness and so forth and one
would presume that that might be very
very similar no matter which
distribution you're putting through and

[02:15]
I'll talk a little bit about what that
may indicate then if you wanted to look
at where do we see the biggest
difference between big an and SN Y and
if we're trying to compare how good
those two distributions are where do we
see that well actually if we change the
heat map to remove those first layers we
can better see the differentiation
that's not being kind of watered down by
the first layers and actually it's right
there at mixed 5b at the end and the
bright red SN GaN really in the later
layers doesn't match the image net
distribution nearly as well as began and
that's where we can see some of the
differentiation so what I'd like to do
now is just give you a few examples from
mixed 3a and mixed 5b to bring it to
life so this is the activation Atlas 40
by 40 began versus imagenet for D first
layer in the network and what you can
see is that each of the icons is not an
image that you might recognize right
we're not seeing dogs or cats at this
level of the layer this is where we see
texture but what you saw is on one side
of the map we have that blood-red area

[02:16]
right a huge divergence and so if I look
at cell say 1511 in mix 3a what we saw
there is if you can see there's 1300 and
two samples from imagenet that fit into
that grid square but zero samples from
big Dan actually go into the grid
squares we're seeing already a huge
divergence
and when you look at the data set
examples of what the network is picking
up in that grid square it's looking for
highly detailed textural areas you can
see it's not just grass up the top with
a very cute puppy that wasn't actually
the spatial activation the grass is like
long fronds of grass right at the base
you can see on the far right a placemat
and a manhole cover with very detailed
intricate texture and actually the two
labels most represented in this grid
cell were hay and manhole covers manhole
covers surprised me at first but when
you look at them there's actually it's
over there right columns second from the
bottom
manhole color has actually have a lot of
texture in the ash felt around the

[02:17]
manhole cover itself and on the metal of
the manhole cover so we're seeing a lot
of texture so the question for me is
we'll then where did all the big and hay
and manhole covers go right where would
they be and so it actually led me to go
all the way to the other side of the map
to sell 20:32 and that's where you start
to see data set examples from big gun
and a divergence between began and image
nets so you've got way more big gun
examples in this cell than image net and
what we can see are a lot of the same
themes so we've got hey we have grass in
the bottom you even see a gray sweater
which is kind of evoking that same idea
of really detailed gray texture but the
fidelity of the texture here and the
level of detail is much less and so
already the activation atlas has shown
how the network is massively kind of
separating these and I think at 3a you
see both began and SN GaN exhibit this
same kind of quality and I think it's
telling us more about the difference
between the fidelity of images

[02:18]
especially Gann samples I was putting
through a 128 resolution and if you took
say the 512 began I'd be interested to
see how this may change so then the
question I think was really interesting
is can the activation atlas tell us
something more about how big Dan differs
from SN Gunn where where do we see that
and for that we need to look at layer 5b
which is right at the end of the network
before you hit a soft max before it's
finally classifying and so for this one
I'm showing the activation Atlas at
mixed 5b 40 by 40 grid the coloring is
showing you in
red cells where SN Gann has a much
higher density in blue cells where big
down has a much higher density right so
what's this going to tell us well the
first thing that sent me to was cell 223
which has a very big density divergence
and what's interesting about this cell
is it's looking for the Intel Busha dog
which I didn't know but is like a swiss
mountain dog very brown white and black
and it has a very specific look and in
this cell there's only about 20 to 24

[02:19]
examples of both imagenet and began but
they're very well-structured well-formed
shapes with very clear details and
snouts an interesting in this cell SN
Gynt Dan didn't manage to have any of
its samples recognized and I think what
we'll see as we go through some of these
examples is the same thing playing out
began has both a self attention
mechanism which allows it to maintain a
much better sense of global structure as
well as the mass scale of the batch
sizes that put through allows it to
maintain not just good texture in its
samples but also global structure so if
you go to cell 35 20 and we look at
cocktail shakers something that I don't
think we talked about nearly enough when
we look at Gans um but this is a really
interesting cell for me because this 328
began our samples in here in this cell
image met hits a similar kind of density
around 269 but SN gain only has 61
samples picked up and if you look to the
far right of the slide which are the SN

[02:20]
gain samples you can see that it's
struggling to maintain the outline shape
that structure and only kind of picking
up on some of the shape cues and if you
go to cell 21 22 now I'm not here to
tell you that began are solved the
uncanny valley but this cell is looking
at melo or one piece bathing suits and
what i find fascinating about how this
has been picked up by the atlas is that
both image netting began in this cell
have around about 150 samples which all
represent the bikini or one-piece
bathing suit right and if you think
about an image and it turns what it's
looking for its looking for some sans
water a lot of human skin in the image
right and maybe a piece of material SN
gain manages to hit those themes but
they're very textural with very little
shape and distinction in contrast began
and
and I use this yes you can actually see
it's actually hit the shape of a
triangle bikini and a one-piece male Oh
which in comparison to early Ganz which
could only really do skies and broad
textural things the ability to pick out

[02:21]
individual shapes in such a complex area
is pretty phenomenal and you're seeing
that play out so one of the questions I
then had the ever ending one is well
where on earth did all the SN Ganz
apples go right if we've got all of
these cells where began is that the same
sort of density as imagenet and doing
well in a distribution term where did SN
going go and that sent me to the bottom
of the map to cell 316 weasel cell so
the weasel cell here is looking for
things that are kind of white or caramel
and fluffy and don't have sharp edges or
very defined kind of structure you see
things like polar bears turning up the
second image there on image net might be
a little confusing because it's a
scooter but the part of the image that
was spatially activated was actually a
fluffy and sheepskin rug at the back of
the scooter and that's what it picked up
on so that's the sort of thing you see
in this cell and both began an image net
have you know densities there SN gaining
contrast has two x they're not the
density of image net in this cell and

[02:22]
while at first you see some of the
similar sorts of themes polar bears and
fluffiness if you actually look through
the rest of the data set examples you
start to see and so it's quite small
here but what you actually see are a
whole lot of examples from non angora
fluffy classes whether it's dogs or even
inanimate objects like buildings that
have so much artifact and kind of
overexposure in the image that they're
lumped in here and picked up by the
classifier in this area and so for me
what's what's really interesting here is
that it helped for me characterize a
couple of things one what on earth does
a fydd score of eight versus a fydd
score of 27 mean right at one level I
know that the mean and the covariance
are the distributions getting closer at
seven but well it's also kind of helping
me see here is okay if I look across the
activation Atlas well began and its
shape capacity and fidelity is allowing
it to hit many of the same grid squares
in a similar issue density to image net
SN gown is hitting some
and then having these clumps of clusters

[02:23]
in kind of amorphous areas and that's
helped helping to do it the other thing
I found really fascinating about using
the Atlas to understand it is when I
first created all the samples for SN
Gann honestly I freaked out a bit
because I look to them he's not good
enough this doesn't look like SN Gann
and what I realized is I was used to
looking at SN Gann samples in contact
sheets that showed me ten images all
from one class at a time and my human
eye when seeing ten images all from the
one class at once would infer structure
and infer a kind of meaning in those
images that the classifier may not well
pick up and so that's something I
thought was really interesting about
using this as a way to guide which
samples to investigate and so forth
because there's always an element of
going back to the samples in Ganz and so
this can help accelerate that so lastly
future directions
obviously there's about 81 activation
atlases if you think of a number of grid
cells number of sorry grid size by date
of distributions by options so working
on an interface that would allow us to

[02:24]
do that we can extend samples some non
Gans I'd love to put the spaz
transformer through this there'd also be
an opportunity I think to keep samples
the same but actually referred
discriminator out of again and actually
use that and sort of track how different
samples are being evaluated by a
discriminator through and similar to the
MIT sale work on a gander section it
would be great to take a generator and
look layer by layer how is that
generator doing what it does so lastly I
do want to thank everybody here thank
you first angel the end of my talk but
thank you to open AI Christy and Maddy
amazing and helpful and to Chris Ola and
Ludvig Schubert from the clarity team
have been amazingly open with not just
their time but their knowledge and
wisdom which has been phenomenal and
it's been a blast my fellow scholars so
thank you
[Applause]

[02:25]
how do you how do you pick cell 223 yeah
so I tried as much as possible not to
cherry-pick and just look the thing so
the the way I looked at it was to take
the log likelihood of each cell and
literally rank it and go for the ones
with the greatest divergence as the
greatest difference and interrogate
those first from both ends both from
where began was really overweight and
then where SN gown was really overweight
and compared and come at it from those
angles having done that once you're
inside a cell and you start seeing
something like you know all the hey
labels seem to be here then I would sort
of say okay where are all the hey labels
for the alternate distribution because
that can give us an idea of almost for

[02:26]
mix 3a at least I always think about it
as twin grid cells right like how are
these related and trying to look into it
that way does that help
so with big yeah I know that in the
paper they have like a truncated yeah
the truncation trick if non-tariff is
very cool with began it's you can
truncate the values of the normal that's
used for the noise vector before they
develop the samples and if in effect if
it's very very load you get a small
variety of samples coming out but
amazing fidelity it's almost like a and
and these the guys themselves say it's
almost like cherry picking your very
best options or if the truncation is
very high you end up with large variety
not so great samples these were all done
at point five truncation and a midpoint
I did some early work on looking at the
truncation and you kind of saw
gratifyingly what you might expect which
is as the truncation blew out it just

[02:27]
kind of and decrease you everything just
kind of exacerbated right things that
were not going so well got worse and so
on and so forth but it's a in that
sample extension bucket and I want to do
some more that's fine any other
questions
where you once got a question sorry yeah
I'm wondering independent of the
comparisons between the two ganz mhm I'm
wondering just what were your overall
thoughts on how well began compared to
just the image net distribution yeah so
well right let me can I not make people
sick so it if you look at apologies guys
if you look at the KL divergence by
layer if we can get there so on this

[02:28]
slide what you can see is big and versus
image net is our first one right so if
you discount layer 3a and 3b for a
moment actually all the way through
you've got pretty good kind of tracking
between image net and began and you only
see a lot of the divergence at 5b so you
I really want to rerun this with a much
higher fidelity big gun sample because a
lot of the best big and stuff that you
see those you know quintessential
examples are coming out of there 512
resolution and this is only done at 128
so I think that you would see an
improvement there and you know it's only
in those later layers and it's very
specific
unlike SN GaN where you're seeing kind
of broad issues with things being lumped
into the grid cells with git begin it
seems to be specific to categories those
categories that require more structure
and so forth does that help

[02:29]
so if everything were blue it would mean
that your kale divergence is close to
zero right which means that the
distributions are quite close the issue
with using the inception classifier
network is that saying the way in which
the classifier network understands your
images with the purpose of classifying
them they are very very close so you
have then tipped over the valance that
your swimming suit is recognizable as a
swimming suit but having a classifier
give you a complete accurate score on
being a swimming suit does not mean that
it is photorealistic to human eyes so
it's getting you a part of the way there
but if you want to do a comparison for
like photorealistic images classifier
alone doesn't do that any other

[02:30]
questions
[Applause]
so for people who might have thought of
questions during the break or just want
to chat a little bit more informally
with some of the scholars as well as the
mentors we will be here till around 8:30
and we can just mix and mingle over in
the living room as well as here but one
more round of applause for all the
scholars and thank you all for coming
and watching the presentations with us
you

</details>


![Person presenting to a live audience on Demo Day](https://images.ctfassets.net/kftzwdyauwt9/ba9cffdb-b0b8-4c4c-194f2996f3d0/8807083cc0a8c7211c046e6a98281e44/demo-day-audience.jpg?w=3840&q=90&fm=webp)

![Person gesturing and asking a question through a microphone while seated in the audience at Demo Day](https://images.ctfassets.net/kftzwdyauwt9/364ba149-0edd-4805-545855d1a4d0/785c897193139d1bc47eb25bcd5ff516/demo-day-question.jpg?w=3840&q=90&fm=webp)

![Two people standing together while one person writes on a piece of paper while the other looks on](https://images.ctfassets.net/kftzwdyauwt9/9f8222d0-9ea0-4e92-9eeb5c1f6ee5/dc0784423403926956224b0b09ae573d/demo-day-writing.jpg?w=3840&q=90&fm=webp)

Loading...

## Projects

Our Scholars demonstrate core technical skills across various expert domains and self-motivation—critical competences for a self-directed program like this one. They each entered the field of machine learning as relative newcomers, and we hope their progress shows how accessible machine learning is. To begin your learning journey, check out some of our [educational materials⁠](/index/spinning-up-in-deep-rl/). More information about the next class of Scholars and how to apply will be announced in July. Stay tuned!

*Thanks to AWS for providing compute credits to the scholars. Additional thank you to our dedicated community mentors for their time advising the scholars on their projects.*

* [Culture & Careers](/news/?tags=culture-careers)
* [2019](/news/?tags=2019)

## Related articles

![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819b4c211886a2/NewsPartnership_Cover.png?w=3840&q=90&fm=webp)

[Global news partnerships: Le Monde and Prisa Media

CompanyMar 13, 2024](/index/global-news-partnerships-le-monde-and-prisa-media/)

![New board of directors](https://images.ctfassets.net/kftzwdyauwt9/5J9s3ItUUDOTebSo0ZVmun/642e8632be32866792c7aaae0113aaa5/44.png?w=3840&q=90&fm=webp)

[OpenAI announces new members to board of directors

CompanyMar 8, 2024](/index/openai-announces-new-members-to-board-of-directors/)

![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/fdcc0dadabd87f8e9a776a2f34647de0/37.png?w=3840&q=90&fm=webp)

[Review completed & Altman, Brockman to continue to lead OpenAI

CompanyMar 8, 2024](/index/review-completed-altman-brockman-to-continue-to-lead-openai/)
