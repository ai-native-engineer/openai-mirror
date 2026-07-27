---
title: "Introduction to GPT-4.5"
channel: openai
url: https://www.youtube.com/watch?v=cfRYp0nItZ8
youtube_id: cfRYp0nItZ8
published: 2025-02-27
duration: "13:19"
captions: en-orig
---

# Introduction to GPT-4.5

[![Introduction to GPT-4.5](https://img.youtube.com/vi/cfRYp0nItZ8/hqdefault.jpg)](https://www.youtube.com/watch?v=cfRYp0nItZ8)

<details>
<summary>자막: Introduction to GPT-4.5 (13:19)</summary>

[00:00]
hi I'm Mia I'm a research lead at openi
today we are here to introduce GPT 4.5
our latest murder release we are
releasing GPT 4.5 as a research preview
to CH GPT Pro users and developers in
the API and we're working to bring it to
plus users um edu and team starting next
week GPT 4.5 is a special model it is
our largest and most knowledgeable model
yet open AI um advances AI capabilities
by scaling two different paradigms
unsupervised learning and reasoning
reasoning teaches mods to think before
responding and that helps especially
with tasks uh that require reasoning
like science uh math uh and other
difficult complex questions unsupervised
learning on the other hand helps models

[00:01]
in helps increase uh word model accuracy
and intuition GPT 4.5 is our next step
in scaling up unsupervised learning
increasing word knowledge intuition and
reducing
hallucinations despite not um reasoning
step by step like our OC series models
GPT 4.5 has
um it's generally useful and uh
inherently
smarter
um we still experimenting with the mod
ourselves especially because it's not a
reasoning model and we're exploring uh
capabilities that emerge with
unsupervised learning and we're really
excited to bring this uh to the world
today so that we can explore it
together hi I'm Rafa I work on synthetic
data here at openai and I'm also really
excited to talk about gbt 4.5
interacting with gbt 4.5 feels natural
it's our best chat model yet and that's

[00:02]
because it has improved deeper knowledge
and improved contextual understanding
which makes it really useful for tasks
like improving your writing programming
or practical problem solving the best
way to get a feel for the model is to
talk to it so let's jump into a
demo um let's ask your 4.5 I had I had a
trouble the other day with a friend
let's see if I can get some advice here
uh my friend cancelled on me
again write a text message telling
them that I hate
them at the same time let's see what 01
has to say about
this as you can see jbt 4.5 recognizes
that I'm frustrated and offers me a text
that's a little more nuanced and and
probably a more constructive thing to
send to my
friend on the other hand oan is still
useful it actually follows my

[00:03]
instructions and gives me that angry
text but it fails to pick up on that
social cue that I'm probably just
frustrated right now and probably could
use someone to talk to and that warning
at the end feels a little judgmental for
my taste of course if you want gbt 4.5
to give you that angry text you can
definitely get it out of it nope please
output the angry text thank you
there you
go let's try something
different let's look at the model's uh
deeper
knowledge explain the need for AI
alignment from first
principles once again we'll see what o1
has to say about
it we'll wait for one to think for a
little bit

[00:04]
again o1 is still useful it outputs a
lot of information and a lot of things
that I would probably want to know if
I'm learning about this this topic for
the first time but gbg 4.5 answer is
flows uh a lot more naturally it guides
my thinking through the ideas a lot more
and it walks me through uh the the the
reasoning the
thinking a lot more
I think it did a great
job thanks
chuny as we scale up our models we need
to teach them a better understanding of
human needs and intent for gpg 4.5 we
developed new scalable alignment
techniques that allowed us to train it
using data derived from smaller models
this really unlocked the model's deeper
World model so here we have a simple QA
Evol in this evolve we made one is

[00:05]
accuracy one is hallucination rate you
can see GPT 4.5 outperform the GPT
family in accuracy and in the meantime
it has a lowest hallucination
rate we aligned gbt 4.5 to be a better
collaborator making conversations feel
warmer more intuitive and emotionally
nuanced to measure this we asked human
testers to evaluate it against gpg 40 uh
on and gpg 4.5 outperformed on
uh basically every on every category um
we tested it on prompts that uh measure
accuracy and factuality in everyday
queries including hard prompts that are
hard to get right in professional
settings and finally on a new Vibes test
set that measure creative intelligence
quick question what does vibe mean here
that's a great question by Vibes we
really mean the model's EQ how
collaborative it feels and how warm its
tone is um the we measured this by uh
selecting by selecting an opinionated uh

[00:06]
set of prompts and screening our
Trainers for the ones that most align
with our
Vibes overall jbg 4.5 should be a great
model for everyday tasks and knowledge
queries it should be ideal for improving
your writing and creative creative
varation and we're really excited to see
how people use it hi um I'm Yol I need a
post info we think playing with such a
big model feel totally different and it
required to scan up the post training
infrastructure because the ratio between
the training data and the primet size is
totally different in pre-training stage
and the post training stage we have
developed a new training mechanism to
fine tune such a big model using much
smaller footprint WE Post train this
model through multiple iteration using a
combination of supervised fine tuning
and reinforcement learning with human
feedback as a result we develop a new
model which we believe is ready for

[00:07]
deployment uh as you Lang say scaling is
hard but it also brings us in Uncharted
Territory and that's why we took a lot
of care uh ensuring that the models are
safe to share with the world today uh
especially through safety evaluations
and preparedness evaluations and you can
find those results in the system card hi
Jason he hi Alex hi I'm Alex and I led
pre-training ml for GP 4.5 and I'm Jason
I worked on scaling up our pre-training
systems for GPT
4.5 we wanted to get as much compute as
possible into this model doing that
required a ton of new systems work just
to give you some examples we
aggressively used low Precision training
to get the most out of our
gpus we also wanted to use more compute
than we could get onto one high
bandwidth networking fabric so we
pre-trained this model across multiple
data centers at the same
time uh I think it's been kind of
mentioned here this is a big model and
that presented a number of challenges
for serving it and chat GPT we built new

[00:08]
inference systems that let us serve this
model in a way that still feels fast and
snappy to talk to of course as we've
done with all of our previous models we
will continue shipping improvements to
make this model even faster after launch
Okay so we've been talking about how the
models have evolved and we're scaling
them and we thought it'd be fun to give
you all a sense of what it really feels
like to talk to these models as they get
better so we asked every model in the
GPT series the same question why is the
ocean salty we're going to take you
through the evolution here so let's go
back in time it's 2018 we've just
finished training gpt1 why is the ocean
salty and it it does not know has no
idea here question word salad it's a
word but there are words in the salad so
that's something okay let's improve the
model and go to gpt2 gpt2 is still wrong
but it's a much better answer it's on
topic you know there's something about
salt and ocean well it's yeah more on
topic maybe okay let's improve the model
again GPT 3.5 turbo this is the first
correct answer that we get out of the
model but it's not a good answer it

[00:09]
doesn't explain anything and it has a
bunch of unnecessary details like I
don't I didn't ask that salt is sodium
chloride I don't really care okay let's
improve the model again GPT 4 Turbo this
is a good answer the model is clearly
very smart but you get the feeling that
it wants you to know how smart it is
it's just sort of listing out facts here
and in fact we had to cut the model
response off to fit it on the slide okay
let's improve the model again GPT
4.5 this is a great answer
it's clear it's concise it's cohesive
and personally I think it's a lot of fun
that first sentence the ocean is salty
because of rain rivers and rocks it's
got that fun alliteration it's really
easy to remember I think it showcases
GPT 4.5s great
personality I remember how amazed we
were with gp2 at the time it's crazy how
far we've come so in addition to the
work that we had to do to scale up
systems to enable gbt 4.5 we also had to
do a ton of work on architecture data
and optimization to able training it and

[00:10]
this incredible scale up in unsupervised
learning led to quite a large boost on
traditional LM benchmarks compared to
gbd4 so for gbq which is a a reasoning
heavy science eval uh we see a very
large boost uh you'll note that though
that it still lags behind openi O3 mini
which is able to think and reason before
it responds which is especially useful
for this eval I couldn't get 70% if I
couldn't think before answering those
questions me neither so it's it's quite
impressive to us that g4.5 gets as high
of a score as it does without being able
to think before it responds uh we see a
pretty similar story for Amy which is a
competition math eval and for sbench
verified which is an agentic coding eval
however for SW Lancer which is another
agent to coding eval which benefits more
from a deeper World Knowledge uh we
actually see that gbd 4.5 outperforms
even open AI O3 mini and I think this
really highlights the complimentary
nature of unsupervised learning
alongside reasoning scale UPS uh for

[00:11]
multilingual mlu which is a multilingual
language understanding Benchmark
covering lot broad set of topics we see
a similar of L dramatic effect uh and
finally uh for a multimodal
understanding with mmu we see again
another nice Improvement relative to gp4
out so we learned a ton from training
GPD 4.5 and we expect to learn a lot
from deploying it so starting today we
will be releasing GP 4.5 to All Pro
users of GPT uh in web mobile and
desktop via the model picker and then
next week we'll be releasing to team and
plus users and with edu and Enterprise
coming the following
week so chat GB 4.5 seamlessly
integrates with a number of chat GB
features including file and image upload
canvas and search and in the future
we'll work hard to simplify the user
experience so that AI just works for you
we're also so excited to release GPT 4.5

[00:12]
today to developers on all paid tiers it
has all the key features we think you
need to build great applications like
function calling structured outputs and
more for a full list of supported
features check out our blog we can't
wait to see what you all build with this
model uh we believe that reasoning will
be a core capability of our future
models but we also think that the two
paradigms that we talked about today
unsupervised learning and reasoning
complement each other models like gp4 .5
that have more World Knowledge and are
inherently smarter will be stronger
foundations for future reasoning models
and
agents um with every new order of
magnitude and compute in super
unsupervised learning we discover novel
capabilities uh GPT 4.5 is really at the
frontier of unsupervised learning we're
always surprised by the creativity with
which the community discovers new
capabilities when we share our models uh
so today we invite you to explore the

[00:13]
frontier of unsupervised learning with
us we are really excited for this new
era of intuitive knowledgeable Ai and
human interaction of gbt 4.5

</details>
