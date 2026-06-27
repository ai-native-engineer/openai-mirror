---
title: "Feedback Loops in Opinion Modeling | Danielle Ensign | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=wZ6PqNp-W_w
youtube_id: wZ6PqNp-W_w
published: 2021-05-10
duration: "15:31"
captions: en-orig
---

# Feedback Loops in Opinion Modeling | Danielle Ensign | OpenAI Scholars Demo Day 2021

[![Feedback Loops in Opinion Modeling | Danielle Ensign | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/wZ6PqNp-W_w/hqdefault.jpg)](https://www.youtube.com/watch?v=wZ6PqNp-W_w)

<details>
<summary>자막: Feedback Loops in Opinion Modeling | Danielle Ensign | OpenAI Scholars Demo Day 2021 (15:31)</summary>

[00:00]
so my presentation is going to be on
feedback loops in opinion modeling and
i will so i'm danielle ensign my mentor
is jeff with
so i'm going to briefly overview here
where i'm going to talk about why this
is a problem we should study i'm going
to then give a literature review
of just like briefly lenses on opinion
modeling and then i'm going to talk
about the particular thing we studied
which is when models produce data
that then goes back into models in an
application of temperature decay
so why study opinion modeling well in ai
safety it would be useful to understand
how preferences change over time and
sort of open-endedness and data
augmentation it would be good to
understand
what are the processes that are leading
to this data we're sending into our
models
and in ai fairness there is this concern
that as
language models generate text in the
world they may affect sort of this
opinion ecosystem
that exists out there and so it would be
good to understand how that happens and
how it affects models themselves so
first a brief
literature review we have language

[00:01]
modeling which is essentially where you
take
lots of data and then you
feed that data into a language model and
it sort of captures a
snapshot in time um so
this is useful but it doesn't quite
capture a lot of these dynamic questions
they might ask like how the process is
changing over time and so we do have
some
previous work that people have done on
just like a facebook scale simulator or
people that study github and these find
that they're sort of these spikes but
it's hard to get sort of this detailed
analysis when you're just
doing these learning systems and so
another thing you can do is these agent
based or physics
kind of models and one thing they find
there is that reality is very sort of
nuanced it's hard to concretely define
these particular things because they're
very interacting with each other and so
one thing people do is they
try to take like a systems theory
approach where they study the structure
for many interacting parts
but the problem here is it's very hard
to have like choose the right sort of
level of fine-grainedness of your models
and so one thing you can do

[00:02]
is use these empirical laws we see in
real world data
and then use that to sort of validate
your models and then finally there's
sort of
this other perspective of looking at
these networks
and you look at sort of how the data is
moving across
through like how opinions the density of
the networks and different things like
that and i can give you some insight
into
what's happening so there's a lot of
other things in particular we decided to
study
a particular problem which is where
you have models that are outputting data
and that's fed back
into the models themselves so concretely
right now there are models like gp23
that are outputting text that's
going on the internet and this data is
going to go back into future models
and so it would be good to understand
what things we should be worried about
here what's happening
so here's the setup that we're going to
do we're going to take some data we're
going to feed it into a trained model
we're going to generate some data
we're going to use that to train another
model we're going to generate some more
data and repeat
and you can imagine a couple of
variations of this maybe we're going to
fine-tune the model instead of training

[00:03]
one from scratch or maybe we're in a
classification setting
where we label this data distribution
and that goes and that
leads to a trained model so
um very concretely here let's consider
this coin
setting where we have
so we have we're going to flip lots of
coins and then in this case we ended up
with the same amount of heads and tails
and so our new probability is 0.5
we do this again and we ended up with 13
heads and seven tails so our new
probability of heads is
0.65 and we can repeat this multiple
times
and there's a couple of things you find
when you start doing this formal
analysis on like linear classifiers or
coins
and two insights are first of all that
more data tends to lead to a decreased
step size and this just makes sense
it gives you a better estimator and the
second insight is when you look at this
we ended up at all tails and
the reason for this is because there is
some probability of just outputting the
same token over and over
and once that happens then it's going to

[00:04]
be stuck there
and so for example uh
you could imagine all heads or all tails
or or even more generally
imagine if we have more than two
outcomes in a discrete setting
so we can do some random walk on these
and eventually one of these is going to
end up at zero in which case we're back
to the two
token settings so there's some theory uh
one other
thing that's worth talking about in the
theory setting is this temperature
so with temperature i have this graph
here
and this is showing so when this red
line is is just a line of the green line
that's temperature 1.0
and when the red line is horizontal
that's temperature 0.0
so what you see here is that when we
sample with temperature what's going to
happen
is things that are 0.5 or higher are
going to be pushed up
and things that are below 0.5 are going
to be pushed down
this has real world implications because
what this means is that when we sample
from models we're going to be
perpetuating existing biases
this is biased in the technical sense uh
it's less clear if you can argue that

[00:05]
this
applies to bias like in the real world
but
uh it certainly at least seems like it
would speed up this collapse issue that
we're talking about
so there's some theory but how does this
apply in practice
well first what we did is we looked at
some engram models where you can
actually run the theory and what the
theory suggests is that it should
collapse to a single path
on the graph from the start to the end
and that path should have no cycles
because if there is a cycle that
represents two different places we went
and one of those directions is going to
be collapsed and in fact that's what we
found
uh just doing a basic n-gram this sort
of traditional
nlp modeling we found after doing ten
thousand ideas of this step it clapped
to by being missed
i will not wish the apart cousin of duty
so that's great but transformers are
really sort of more modern language
models
and so the question is what happens with
transformers there
there is this tricky question of like
how do you measure collapse and
one way you can do this is by modeling

[00:06]
temperature by modeling entropy
so if we generate lots of sentences and
then we
compute the probability of each sentence
just by multiplying the probabilities of
each word
and then average over loss of those
sentences we get a rough estimate of the
entropy of the model itself
so as a reminder here's what we're doing
we're taking data into a train model and
i'd like you to sort of guess what you
think is going to happen
with a transformer when we just feed it
back into here
so okay what we find
is that there are two settings the
the first is basically it just sort of
shoots off to
entropy randomness where it
yeah it sort of just becomes this
uniform
outputting thing roughly it still sort
of centers on things but it becomes this
very sort of random generation
the other thing we find is this behavior
here
where it sort of shoots up initially and
then it goes down
to this collapse as the theory predicted

[00:07]
concretely here so
it starts out we have this plankton or
aggressive wildlife some days in the
season just kind of standard output and
then it
if you've looked at the outputs of
language models you know that a lot of
the outputs are pretty weird
and so what's happening is the language
models are sort of getting used to the
outputs being
at least what seems to be happening is
the language models are getting used to
these outputs being weirder
than they are used to as their inputs
and so
we end up with the generation quality
seems to decrease then eventually it
hits this cat where now it's sort of
used to how weird the output is
and then we have these cycles that
happen so for example
um hi hello hi hello it might just
repeat something like that
and once that cycle appears in a
generated output
the model will see that and that will be
more likely to be produced in the future
and so we'll repeat
this um and then it'll be sort of
perpetuated in there and so if you look
at these like these are the most common
tokens at the peak they're pretty
common tokens but what happens is it

[00:08]
sort of focuses
on particularly weird little loops so in
this case it really like to say twitter
a lot or ally a lot but
you we ran some other runs so this one
eventually just focused on saying enemy
over and over
and the important point here is that we
have this collapsed behavior
so that's the theory um
what the theory also suggests is that
entropy we would or that temperature if
we have
a temperature below 0.1 or below 1.0
then we would expect it to
collapse quicker and if we have
temperature above 1.0
then we would expect it to go to this
entropy
and that is what we find so if we have
temperature below 1.0
we find that it very quickly collapses
you'll recall over here it took 250
steps
here it only took about 20 and with very
very low temperature
it collapses almost immediately to the
sentences like essentially just the most
common sentence
whereas with higher temperatures it has

[00:09]
some time to fiddle around before
it collapses and then yeah with
temperatures above 1.0 it
just sort of takes off to essentially
the maximum entropy it can get to
so future work in this direction
uh it would be good to have better
understanding of what's happening in
this process
it would be good to sort of um
to run more runs and understand some of
the variability some of these take a
very long time so it would be good to
understand if there's other kinds of
outcomes these are the i'm describing
the general patterns we've seen
it would be good to understand like if
we are perpetuating
real-world biases you know uh
there's an argument that temperature
sort of leads to these models being mode
seeking
where they will output the most common
thing and then that goes back into later
models
and so you can imagine that it should be
perpetuating bias but it's hard to
necessarily argue that
and then finally there's this
temperature decay phenomenon
where because this lower temperature

[00:10]
things are being fed back into the
models and the model
gets used to it and that we get less
entropy that seems like a problem
and so uh you know
the one other thing here is all of this
theory seems a little iffy like
in practice when we like
are feeding this models into the real
world there's some filter on what data
actually goes out there
and so to and so we should under like
and so really we should incorporate in
this model some kind of feedback
thing that is filtering what data is
going on there and so
uh this is analogous to if you have like
a go playing system then you only are
feeding back the things that do well
and so that's a relevant piece here as
well so yeah
that's my presentation um and thank you
to
everyone um my mentors and everyone that
was able to help
and uh yeah i'm open to questions now

[00:11]
cool so uh the first question
we have is for the language model at t
equals one
does entropy always increase and then
decrease
yeah so sometimes it does seem to just
take off to really high entropy
sometimes it does uh
do that up and then back down we haven't
ever seen it just go down
and honestly it's kind of weird but it
pretty like consistently goes down it
doesn't do much of a random walk
whereas for like the theory it suggests
it should be doing a bit of a random
walk and so there's a lot of open
questions there
so there's a question here would you see
the same effect if you extend the data
set instead of replacing it with model
samples
so this is another direction that you
can
yeah that i think is really interesting
it's essentially this question of
grounding
so i have a couple slides here on this
one where
you can imagine instead of just directly
using

[00:12]
the data into a trained model we
actually
have some ground truth data that we're
also feeding into the model
this in principle this can
uh help quite a bit because like we're
just doing a random walk at each step
if you bias the random walk towards a
particular distribution
then we would expect that random walk to
not or to roughly stay around there and
for
small engram models we did find that
this helped
and this is relevant in practice because
these models are going to be feeding
back into
themselves and so or and these models
are going to be taking sort of
also real world data um but yeah we
haven't validated this
on language models and i think it's a
really interesting question
yeah what are the implications of this
work first semi-supervised learning
so i

[00:13]
i think that yeah it's
um that's a tricky question i i think i
would need to
think more about that um
[Music]
yeah so you could certainly imagine
like at the limit of
labeling data just from some small set
of data
that you may end up with some
feedback loops but
it's less clear i think that's a nuanced
and tricky
question yeah i'm not sure i have a
great answer for you on that one
uh the final question we have here is
we're
able to look at what happens if the
outputs are only some smallish
percentage of the input
for the next training step mixed with
new real-world data
yeah so that's this grounding setting
and we have not ran it on language

[00:14]
models
i did ran it for the engram things and
honestly my intuition is that yeah just
a very small percent would help
significantly
you know it's worth pointing out that
these things
are like in practice we're only going to
be doing a couple steps we're not going
to be doing
10 000 steps which is how many we needed
to converge
and so like
only in practice if you have some of
this grounding data
that may make a big difference yeah
um so there was also a question have you
considered
other settings apart from the coin
setting
um yeah so we we did that setting with
lots of different models
we looked at like a linear classifier so
it's a little different there
because instead of
you know this collapse it just sort of
randomly walks
if you don't have any bias then it just
sort of keeps cycling
and yeah the

[00:15]
the general insight of sort of having
either a random walk
or collapse for discrete things seems to
be true in
a lot of settings but i i think that
it's worth doing a little more detailed
analysis there because
for some more complex models it you
might be able to say something more
interesting
um okay so that's all the time i have so
i'm gonna pass it off to jonathan
thank you everyone

</details>
