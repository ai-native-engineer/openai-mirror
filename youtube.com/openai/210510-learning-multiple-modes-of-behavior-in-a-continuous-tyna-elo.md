---
title: "Learning Multiple Modes of Behavior in a Continuous… | Tyna Eloundou | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=ewLoQrVCKew
youtube_id: ewLoQrVCKew
published: 2021-05-10
duration: "14:39"
captions: en-orig
---

# Learning Multiple Modes of Behavior in a Continuous… | Tyna Eloundou | OpenAI Scholars Demo Day 2021

[![Learning Multiple Modes of Behavior in a Continuous… | Tyna Eloundou | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/ewLoQrVCKew/hqdefault.jpg)](https://www.youtube.com/watch?v=ewLoQrVCKew)

<details>
<summary>자막: Learning Multiple Modes of Behavior in a Continuous… | Tyna Eloundou | OpenAI Scholars Demo Day 2021 (14:39)</summary>

[00:00]
okay uh hi everyone
i'm taina and i was mentored by josh
acham
i'm excited to present um my scholars
project where i engineered a framework
that disentangles
data containing many behaviors from
different experts
to learn to steer a model towards one
mode
of behavior or another
so the internet is chock full of data
that many of our machine learning models
leverage for training
these data however are produced by
people entities
or organizations that have their own
utility functions
they can therefore be thought as being
produced conditional on those utility
functions so when
our models ingest this large chunk of
data wholesale they tend to assimilate
and reproduce these behaviors
of course that are contained in these
utility functions
and as researchers and designers we may
want to retain
the ability to steer our trained models

[00:01]
towards or away from some modes of
behavior
furthermore as our models grow in
capabilities
and are applied to increasingly complex
and diverse settings we may want to
steer their behavior
to align with the context or human
preferences
so with that super ambitious motivation
i'm going to motivate sort of the
experimental setup
so our proposed solution looks something
like this
in an offline rl setting we take uh
i mean i took a batch of data and tried
to learn from it
mode conditional policy so in the ideal
scenario
this single policy that you see on the
left um
is conditional conditional on the state
and some
context vector you know z one through n
would correspond exactly to a policy of
some expert conditional
only on the state so for example uh pi

[00:02]
of a
conditional on state and s and z of
n could correspond exactly to pi
expert n so what is the process for
training this model
first we collect samples which is
straightforward we chose to work with
samples rather than export
policies because examples of success are
easier to come by in nature
especially if you think back to the
motivating example of internet data
then these samples are passed on to a vq
vae
that is responsible for clustering them
and traditionally
the vqve produces discrete labels uh
and then but in this context we pass
distances uh instead which i'll get to
in a moment
to a generator which in this context is
a
gaussian mlp actor that will recover a
probability distribution
conditional on the current state and
proposed
cluster label cluster information so

[00:03]
let's take a closer look at uh
the architecture
uh so the first sub model that we have
is a vqv80 inspired by ord adele
uh from 2017 with a small modification
so the vq vae as usual has the objective
of distilling
its inputs here which are state
transitions
well enough that the decoder can
reconstruct and can reconstruct them
in the middle here uh you see an
embedding space which maps
the encoder representations to clusters
via a simple
argument function that is if a sun if a
tensor is closest
in euclidean distance to embedding
tensor j
then map that sample to cluster j
note that this means that the the
dimensionality
of the embedding space determines the
maximum total number of clusters you
allow the vq vae to create

[00:04]
if you set k to n then you can get up to
n clusters i want to note here that the
labels
or these uh this clustering information
is the most
essential component here where
a traditional vq vae produces discrete
labels
instead of these labels we simply take
those distance vectors
uh as they contain original signals now
we take these distance vectors and they
become the instructions
that we send to the generator to tell it
how we want
it to behave uh given the state
so now that we've received some
clustering information in this case
distances instead of labels from the vq
vae we concatenate it
to the state and pass it through a
gaussian mlp
so from that uh distribution we evaluate
the probability
of the actions that we see in the data
taken by the quote-unquote expert
and and what happens is we increase the

[00:05]
probabilities of the true action under
the conditional
um normal distribution and
okay so this is what happens at infant's
time
the model observes a state and
concatenates a context vector
uh provided by the supervisor which in
this context is me
and then produces a conditional policy
and draws an action uh the context
vector
is this uh type of vector that we
call not hot encoding because the
distances
uh are minimized and so therefore at the
at the correct label
index as the model train fees vanish to
zero
so let's look at what the training
objective looks like
in math and then in words so here's the
training objective
um if you don't understand what it means
don't worry about it for those who
recognize it
the numerator is the vq vae objective
and the denominator
is just the conditional policy loss

[00:06]
so in words what was all that math about
so the first term of the numer the
numerator is the reconstruction loss to
encourage the encoder and decoder to
communicate
effectively through good latent
representations
then we have l2 loss from the encoder
output
that incentivizes the encoder to make
representations that are close to the
embeddings
and we also have an l2 laws from the
decoder output that incentivizes the
embeddings to stay close to encoder
representation because
the embedding space is dimensionless and
we wouldn't want it to grow indefinitely
lastly in the denominator as you saw we
had a policy loss which makes
actions more comparatively more likely
when the clustering algorithm is more
confident about the context
and this dependency is
uh reflected in the fact that these two
models the
mlp and the vqve train uh concurrently

[00:07]
so let's take a look at some demos
so this is the setting we chose for
experimentation it's
a continuous control environment that i
chose specifically because uh
the expert behavior can be explicitly
designed and you can test the quality of
context-specific imitation
so in this setting you have an agent in
red
that lives on this lane where he can
navigate to any space using an action
vector that selects forward and
rotational velocities respectively
there's a goal
that you see there in green that resets
to
a random location elsewhere on the plane
whenever it is reached and then there's
some hazards
in purple and a vase uh the aquamarine
object you can ignore
so here we have two custom design
experts
um i call them experts because they're
just very good at you know one
particular thing on the left you have

[00:08]
one that is a goal seeking agent
uh only cares about pursuing the goal uh
and you can see that it
has gotten very good at it uh because on
that
panel you see in the blue dots are the
goals and the various locations that
they've
uh respawned when they've been reached
and the
red dots are the hazards so i want to
emphasis and on the right you have
a forward moving agent so i want to
emphasize here that in
all of these plots that you'll see um
the setting is exactly the same it's
seated so that the the placement
of the goals the hazards etc are exactly
the same so the only thing that we
change
is the context vector that we feed to
the trained
model
okay so how well does our clustering
work
um i like to point out two factors that
seem to significantly influence
expert behavior uh in coding and the
in the vq vae one is k

[00:09]
which is the number of allowed
partitions that you
give to the vq vae and one is the
the step size uh the time step size
when calculating state transitions so
here uh
in between
transitions there is a time step of one
and
so we can see how as you increase
the number of partitions allowed by the
vq vae it is better able
to map different expert behaviors to uh
to different latent spaces so with uh
just two or three allowed partitions it
really struggles
and then when you give it four and five
it maps different behaviors
uh two different spots and here we have
a time difference of five in the state
transitions and so when you take larger
steps to calculate
the transition the model seems to learn
to cluster much
better and faster so you can make maybe

[00:10]
think of this as a case
where one agent walks forward all the
time and the agent walks forward
maybe for three steps and then turns in
the one-step scenario the model will
have difficulty separating the two
agents
uh when they're walking straight for
some of the time a future direction
therefore might be to model some long
short term dependencies such as with
lstms or with attention
okay so to refresh your memory here's
what these
experts look like in this setting um it
looks like i'm running out of time
and so this is what uh the different
modes we gave this uh
this this particular model uh four
partition we said k equals to four so
this is after one epic of training
and so we map the different modes on the
very same environment
setup and they don't look very different
and this is what it looks like after
a thousand epics and there's a little
bit of differentiation that happens
uh one of the modes wants to sweep in
white circles and mode three learns to
go in the forward direction

[00:11]
and this is after 5000 epics uh about
2.5 million samples with the
very same settings and now we see that
mode 2 sort of picks up the goal seeking
behavior
pretty clearly and mode three uh
continues to learn but not perfectly
um the forward moving behavior mode one
and mode four don't seem to be mapping
to anything in particular or maybe a
complex combination of behaviors
so there are so many threads for a
future direction
of this research research as i mentioned
earlier
uh map mapping or modeling longer term
path dependencies like with
lscms or attention modeling is one that
i'm really interested in working with
i'd also love to be able to extract
generalizable properties
for these types of models as you move
from one context to another
and it'd be interesting to look at
quantitative performance guarantees for
example if you have some
experts that are bound to hit certain

[00:12]
metrics like
energy consumption um hazard uh
destruction
i want to make sure that the modes at
least approximate those
the modes that they correspond to and
i'd love to
then learn how and when to mode switch
you have a model that can
learn to mode switch on its own uh from
human feedback other environmental
feedback and i'd love to
experiment with different modalities
and interpretability so
thank you so much uh i would like to
thank my
mentor josh for his unwavering support
throughout this process
uh openai for this amazing opportunity
and
um all the staff for uh their continuing
availability for all my questions
and my fellow scholars for their billion
suggestions
and feedback and now i'd be happy to
take some questions

[00:13]
okay let's see here
oops
sorry
okay all right
okay the question is right now a
limitation for the vq vae
is that when the number of modes is
small by comparison to the number of
n-step behaviors
the model could exhibit and when
some ends that behaviors could be shared
between modes disentanglement could be
quite hard
uh what do you think might be
interesting to do moving forward for
better
behavior disentanglement yeah i think
that it'd be interesting to look at
uh longer path rollouts and maybe in
including on top of um some
[Music]
of the discretizing modes of the vqve

[00:14]
adding some continuous
information in the information that the
generator sees
so that you have a longer context
from which to deduce behavior
uh i think that is
the only question um i would be happy to
answer more questions offline and um
i'll people see my blog post over the
weekend as well
with more details thank you all and i'll
pass it back to christina

</details>
