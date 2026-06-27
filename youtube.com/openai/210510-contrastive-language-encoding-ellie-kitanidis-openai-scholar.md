---
title: "Contrastive Language Encoding | Ellie Kitanidis | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=mVZE7wm1skw
youtube_id: mVZE7wm1skw
published: 2021-05-10
duration: "17:12"
captions: en-orig
---

# Contrastive Language Encoding | Ellie Kitanidis | OpenAI Scholars Demo Day 2021

[![Contrastive Language Encoding | Ellie Kitanidis | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/mVZE7wm1skw/hqdefault.jpg)](https://www.youtube.com/watch?v=mVZE7wm1skw)

<details>
<summary>자막: Contrastive Language Encoding | Ellie Kitanidis | OpenAI Scholars Demo Day 2021 (17:12)</summary>

[00:00]
awesome hi guys my name is ellie
and for my project i've been working on
pre-training a language representation
model
using contrastive learning
so i'll start by giving some background
on what contrastive learning
is and sort of putting this work into
context then i'll spend some time going
over
our framework and procedure and finally
i'll share some preliminary results
and discuss future steps
so contrastive learning is a
self-supervised method for
learning representations like a lot of
ideas in deep learning the idea of
contrastive loss
is not really new but it's just sort of
become a really
popular and active area of research
recently
in computer vision because of its
success at learning visual
representations
so the concept of contrastive learning

[00:01]
is pretty intuitive
the idea is just that similar inputs
should be
mapped closer together in representation
space
and some contrastive frameworks will
also explicitly
structure their loss functions such that
dissimilar inputs are mapped farther
apart
so you can kind of see this in this very
high level
conceptual diagram that i've included on
this slide
which should not be taken literally by
the way um but it sort of shows
the idea of contrastive learning um
so it shows that two representations of
the same
fundamental concept sort of like two
images of the same person
should be mapped close together while
two distinct concepts like two different
people
should be mapped farther apart so
in practice what usually happens is that
an
input image x is augmented to create
two different versions x1 and x2 this
augmentation is usually some combination
of
random cropping like reorientations

[00:02]
and other types of noise injection and
then the two versions x1 and x2 form a
positive pair
where the loss function should seek to
maximize the similarity between x1 and
x2
so while contrastive learning has become
a booming area of research and computer
vision
the applications to natural language
have thus far been pretty limited
um so i've listed here under nlp
basically all of the relevant papers i
came across most of which have pretty
recently hit the archive just within the
last few months
um because i'm limited to 10 minutes i'm
not gonna go through each of these
individually and discuss
them but i'm putting them up on the
slide so that you can look them up
and read about them if you're interested
um what i will say is that
in basically all of these prior works
either they're not
pre-training from scratch they're you
know fine-tuning an existing pre-trained

[00:03]
model
or they're using contrastive learning as
sort of an auxiliary
objective along with a more traditional
language modeling objective
so we became interested in whether or
not you could pre-train a language model
from scratch
using just contrastive learning by
itself
sort of just in the interest of looking
for
new language modeling approaches that
might have some
new benefits either in performance
across some subset of
tasks or scaling or both
i'm sort of specifically motivated by
the search for better
sentence level representations in
language modeling
so for our contrastive setup we
re-implemented a recent paper
in computer vision um and
you know matched the performance of that
paper
in this so-called sim cyan framework no
negative pairs are used

[00:04]
just positive pairs x1 and x2
so the augmented data pairs are fed into
an encoder
which produces the representations those
are then fed into a projector and
predictor
that are trained simultaneously with the
encoder
and the loss function in this case is
pretty simple it's just trying to
maximize the cosine similarity between
the positive pairs
um so the innovation of this particular
framework is
the addition of the predictor and the
stop gradient
such that the cosine similarity is
actually between
p1 the output of the predictor on x1
and z2 the output of the projector on x2
with the back propagation only
calculated through the branch with the
predictor
so this was shown in simsyam to
help avoid mode collapse where basically
the model just learns to map everything
to the same place in representation
space

[00:05]
since we don't have negative pairs to
sort of balance out that attractive
force
so our model oh i guess i forgot to
mention um
so for our encoder we basically just use
a
um transformer encoder um
where uh we've added a few tweaks from
openai's sparse transformer
implementation
namely uh they present this modified
residual block and also some
special initialization schemes and
activation functions
okay so our model is pre-trained on the
pile um
this is a recent large language data set
that captures a diverse range of
modalities
everything from books to code from
github repositories
web pages medical papers etc
um now a big question
possibly the biggest question in
applying contrastive learning to
language

[00:06]
is what should our augmentation method
be
um so most if not all of the papers i
cited earlier
use some form of noise injection uh such
as randomly deleting or replacing words
rearranging the order of words and so on
however
we felt that um maybe more so than in
the case of images
injecting noise into language does not
necessarily create invariant
representations
um so if i make random changes to the
structure and content of my sentence
i'm not really saying the same sentence
generally i'm not really saying anything
coherent at all so
we thought a more principally motivated
approach would be to choose
pairs of text that are near each other
in a document
and thus likely to have related content
and style
so once again due to the 10 minute limit
i won't go into the technical details of
our data processing pipeline
but i do have a few notes on the slide

[00:07]
for reference if anyone wants to
dive in deeper later
okay so now we come to the preliminary
results
um so i'll start by saying that when i
did my phd
the physics department had an unusual
way of doing things
instead of doing our dissertation
defense at the very end of our phd
we did it about halfway through and the
reasoning behind this was that they
wanted us to get a lot of expert
feedback early
on the reason i'm telling you this is
because a part of me really wishes i
could give you an update on this project
in a few weeks
when we have more conclusive results to
share but on the other hand i think it's
actually very valuable that i get to
show it to you now and
potentially solicit your feedback and
ideas
so the one thing i can state with a lot
of confidence at this point
is that training these models is really
hard um
so far we're finding these sort of spiky

[00:08]
plateaus in the loss function after the
first few thousand iterations
pretty much no matter what we do um so
i've plotted a few
examples here but they all pretty much
look like this um
so far hyper parameter sweeps are not
really giving us any insight into this
i will say i have not exhaustively
searched the parameter space by any
means
i've only been working on training this
for a couple of weeks
so it could be there's something to
uh some insight to find there but so far
we haven't seen anything
um increasing dropout and or weight
decay also
hasn't seemed to have helped um we
experimented with
adding a tank before or after the
average pool
um that goes at the end of our encoder
that also did not seem to particularly
help
so we wanted to test that this
training difficulty is related to the
contrast of loss
um so we tried training the model with

[00:09]
an mlm like objective instead
for anyone not in the language modeling
world that stands for
masked language modeling basically we
replace
10 of the tokens with random tokens and
then
take our same encoder and feed it into a
linear and sigmoid layer instead so now
the task is
to predict the replacement mask um
this is slightly different than the bert
objective of trying to predict the
masked tokens
since we don't have a decoder or
anything generative
we're just trying to predict the mask
itself
and when we train this model we find
that we get much more nicely behaved
loss functions so that does seem to
indicate that it is the contrastive loss
that's causing the problems
as another sort of probe we decided to
see how well the model can match
queries to relevant keys so we randomly
selected a thousand text pairs from the

[00:10]
data
with the same selection parameters as
were used in pre-training
and we let these be query key pairs we
then created a cosine similarity matrix
of
encoded queries dotted with encoded keys
and calculated the percent of queries
for which the corresponding
key was in the top k most similar
so for example out of a thousand query
key pairs if the model's totally random
i would expect
that the matching key uh to be in the
query
the query's top five most similar uh 0.5
percent of the time
instead we consistently see about 20 um
and likewise for the top 100 we see 60
what's kind of interesting about this is
that doing the same
test on the mlm version of the model
we actually get smaller values so 5 and
25 respectively perhaps
the contrastive version of the model is
better at this type of task
of course this could very well wash out

[00:11]
at larger scales and with more training
these were only trained for you know the
first
2000 iterations or so um because of the
noisy plateau issues so this is far from
a conclusive statement
but more of an interesting preliminary
finding
finally we do have evaluation set up for
two downstream
tasks from the glue benchmark set of
course again at this stage of training
the results and the configurations used
to get them
are far from final um so we include them
more just to give a sense of
uh where the performance gap is
currently
um so the two tasks we evaluate on are
rte
and mnli these are both textual
entailment classification tasks
in other words for a given premise and
hypothesis
does the premise imply that the
hypothesis is true
um i'm going a little bit over on time
so i will skip discussing
the details of implementation and i'll

[00:12]
just talk really quickly about this
table
so this is the maximum validation
accuracy for these two tasks they're
both classification tasks
classes mli is three classes um
and the third row is basically the
results using
um a pre-trained burp model that i just
took off hugging face
so the values aren't exactly the values
from the burp paper but they're the
values
that i got in my fine-tuning pipeline
very close to the values from the paper
and we see that for
our model in both versions there's about
a five percent gap
in rte um so the the two models
uh perform pretty similarly um but
definitely
not uh as well as the vert pre-trained
um for mnli i actually found that uh
this is a much larger data set so it was
a lot slower and i found that
our model was very slow to converge
so i don't actually have a final value
nor do i think it's particularly helpful

[00:13]
to try to get one at this stage
but the training does start uh with a
validation accuracy of about
60 percent so it is doing something
um but the the slowness to converge
does uh indicate that it's doing a lot
of training from scratch which is
unfortunate
um so the last thing i'll say about this
is that um
obviously this is not an
apples-to-apples comparison um
not only because we cut the pre-training
so prematurely but also
the model is smaller than bert base
but it is still i think helpful to see
that five percent gap
um and whether or not that can be closed
um
by improving those parameters
okay so very very quickly next steps
obviously our immediate next steps are
to try to improve the training
just do a lot more experiments with
learning rate parameters and
augmentation parameters
and maybe expand our scope a little bit
in terms of including negative pairs
and different types of loss functions

[00:14]
potentially also exploring different
augmentation methods that might work
better
more broadly if we were to get this type
of model to
work obviously we would be interested in
probing its scaling behavior um and also
its performance on a
wider variety of tasks yeah so i've gone
a little bit over
but thank you guys so much for listening
and of course thank you to
my mentor and the program coordinators
and my fellow scholars
this has been an amazing experience and
i'll
take a couple of questions and then pass
it
all off
okay so the first question is these
results make me curious about the input
pairs you selected
could you talk a little bit more about
it yes i can really briefly
show you a slide that i had skipped

[00:15]
um so uh basically we started out
thinking about how to do this
at the sentence level so we started with
just
sentence pairs basically and we would
allow them to be separated by some
distance that was a hyper parameter
and we actually made it really
open-ended by having a minimum
and maximum separation such that it
could be
a random separation between those two
intervals and eventually we ended up
moving towards larger pieces of text
mostly because the evals were all more
than one sentence so it just made sense
to
take on that level of abstraction um so
we now
choose chunks of text of some number of
sentences
which is also a hyper parameter and
we've explored
um those three hyper parameters as well
um

[00:16]
we then tokenize using a uh subword
tokenization
and truncate our pad to the maximum
sequence length
um okay i'll take one more question
do you plan to try out contrastive
losses with negative pairs
such as nce to compare with simpson
byol lost performance yeah so as i was
saying
um so far these preliminary results do
seem to
indicate that um the simscyan framework
might not work so well uh for a messier
more complex
data set like language and so we would
definitely be interested
in trying more complex
loss functions that do include the
negative terms so something like nce
um definitely would be uh something we
want to look at
okay i've gone a little bit over but
thank you guys so much for the questions
and um
if i didn't get to your question please

[00:17]
just look me up on linkedin
or on slack if you're at openai and i
would love to keep chatting about it
offline
okay so i will now pass it on to cujo

</details>
