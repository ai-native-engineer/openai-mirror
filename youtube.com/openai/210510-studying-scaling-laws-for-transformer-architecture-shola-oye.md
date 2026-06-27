---
title: "Studying Scaling Laws for Transformer Architecture … | Shola Oyedele | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=HYijvkoXgPE
youtube_id: HYijvkoXgPE
published: 2021-05-10
duration: "16:22"
captions: en-orig
---

# Studying Scaling Laws for Transformer Architecture … | Shola Oyedele | OpenAI Scholars Demo Day 2021

[![Studying Scaling Laws for Transformer Architecture … | Shola Oyedele | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/HYijvkoXgPE/hqdefault.jpg)](https://www.youtube.com/watch?v=HYijvkoXgPE)

<details>
<summary>자막: Studying Scaling Laws for Transformer Architecture … | Shola Oyedele | OpenAI Scholars Demo Day 2021 (16:22)</summary>

[00:00]
um so i'll get started um hey everyone
um my name is shola um i'm going to be
talking about scaling laws for
transformer
architecture variants um
and so today's talk is going to be
broken down into three main sections
first a discussion of the problem and
context behind pursuing this research
an overview of the research and any
findings from the experiments
as well as an overview of sort of future
opportunities
available for research on this topic um
at first we're going to dive into the
problem statement behind this research
and project
specifically um resources already been
done in the space
and to provide context on this research
project
i wanted to sorry about that
specifically i want to chat about
research that's already been done in the
space to provide context on sort of this
research project
so scaling laws for neural language
models was a recent paper that came out

[00:01]
of open ai
i imagine that most people in this room
are familiar with this research so i'll
try to keep my comments brief
um this paper introduced empirical
um scaling laws for the performance of
machine learning models
as a function of a number of key
parameters
or key attributes model size which is
defined by the number of model
parameters
data set size and compute compute
referring to the total
compute budget used to train the model
as defined in the paper
compute compute is referred as the
number of
not embedding compute used during
training can be estimated
as c equals 6 nps where b is the batch
size
s is the number of parameter updates and
the factor 6 accounts for the forward
and backwards passes
so the graph to the left is from the
original paper
and illustrates how language modeling
performance
increases so it improves smoothly as we

[00:02]
increase
model size and data set size and compute
with optimal performance gained when all
three are sort of scaled in tandem
um and sort of given that lfc
is its own function for every model um i
consider
lines that were within five percent of
each other to be within a margin of
uncertainty
um so the further away lfc was sort of
the more consistent
significant i consider the results um
and
llc can be calculated
with irreducible loss or without but in
my experiments
i exclusively calculated it without for
simplicity
um it should be noted that
so this is lfc um the equation that sort
of represents this power line here
and this m term here is sort of the
constant term that controls the
trade-off between
um loss and compute um if you see me

[00:03]
looking off to my right i'm looking at
my monitor
to make sure i'm pointing at the right
thing um
so this is the existing research work
that led to my research
project while the original paper study
scaling laws on decoder only
transformers i wanted to understand how
these laws
trend among different transformer
architectures
so before we get into more background
let's talk about motivation
um so i was interested in working with
transformers because of their impact on
the nlp space
when you add scaling laws which
introduce the ability to forecast loss
with respect to compute
i was curious to know how these laws
could generalize among
the different types of transformer
architectures
i was also curious it's where the
constraints of scaling laws
and i thought trying to reproduce
scaling laws
um but on different types of
architectures or different types of
transformers
could tell us more about what
generalizes among
the different algorithms versus being

[00:04]
sort of a standalone feature of the
original decoder only transformer
so at best it would be an opportunity to
understand the connection between
transformer architecture components
and model performance at worst it would
be an opportunity to understand the
constraints of scaling laws particularly
when exploring more models
so i'll sort of discuss next
the types of architectures i
experimented on why i chose them the
differences
and what i think we can expect from the
resulting architectures
so the transformer architectures i
studied followed into two categories
causal language modeling which is
predicting
the next token and sequence and mass
language modeling
which refers to predicting the mass word
which may be any word within
the sentence so the only difference
between the two
is the way that the model is trained so
the same architecture can be used for
both types of language modeling
and you'll see later on in the

[00:05]
presentation that i did this with bert
although burt was originally released as
a mass language model
there is a causal implementation of it
and i ran my experiments on both types
so a little bit of background and i'll
try to speed through this just because i
know this is a lot of information
but the architectures that i experiment
with are shown here
they were picked based on their
architecture and ease of implementation
so in the interest of time i'll try to
be brief and maybe just highlight some
of
the more important characteristics um
i think i mentioned earlier that in that
in the original
scaling loss paper it was studied only
on the decoder only transformer
um since the data set the data set size
and machine
that i use are all different from the
original paper i decided to experiment
on
a transformer that was similar to what
was used in the original
paper and for that i used gbt2
for that as it was the closest to what
was in the original paper and i thought

[00:06]
it would be a good reference point to
put the others in context
as you'll see the other two causal
language models
that i experiment with or transformer
excel and reformer
um
you'll also see that bert like i
mentioned
was was experimented on using his mass
implementation but then also
its causal implementation as well
and so you know bur is a mass language
model that uses
random masking and um next sentence
prediction
um the only difference sort of
between the two as far as the causal and
the mass implementation is the way the
model is trained
uh meaning that the same architecture
can be used for both types of modeling
so i really want to point that out just
because it will become important
later in the presentation but um just
wanted to call that out
and then of course these last two mass

[00:07]
language models which are both
um sort of based off of or both sort of
similar and inspired by bert
um i'll sort of skip that in the
interest of time
so my hypothesis is that the impact of
transformer architectural scaling laws
depends on how significantly that
architecture impacts
model size data set size and and most
likely compute
so given reformers
focus on reducing its memory and compute
during training that's embedded in its
architecture
my prediction was that you would see
that the reformer architecture
particularly
outperformed the other models given the
insight
on the original paper on how weekly
performance trends with model shape
i predicted that bird scaling laws would
have little to no change between the
causal and the mass
version and that you would see
the all of the mass language models sort
of have scaling laws that
are within a sort of a margin of

[00:08]
uncertainty or sort of
um have only the difference of a
constant pre-factor
within them um so next i want to talk
about experiments
um methodology preliminary findings and
research implementations
i'm going to try and speak a little bit
faster because i think i'm running a
little bit slower on time
um so for methamp methodology um one of
the key tasks of my research project was
calculating um the compute efficient
frontier fit
that's lfc and on transformer
architectures
doing language modeling and essentially
trying to understand
how lfc changes with respect to
algorithmic changes within an
architectural family
um so once i decided which models to
study i proposed several model sizes
and then produced a learning curve for
each run ideally training at least four
to five sizes for every model
and sort of the number of parameters
ranging between 2 million and 350
million
um with some variation between the
different um
the different architecture um this graph

[00:09]
highlights
sort of uh one of the typical loss
versus estimated compute
and here i just want to point out that
we sort of see this front
formation of a pareto frontier
and this sort of i would say line that's
adjacent to this curve
is the scaling law um that i'm going to
be looking for
and then sort of evaluating between the
models
um so these are some of the preliminary
findings
um that i had i think the numbers
are less important but more so just the
relationship between one another
um so on this slide we can see that the
same architecture using a different
method of training
can produce different llc's um so
this result was initially surprising
because i had assumed that the same
that we'd see the same lfc um because
they have the same architecture
but it actually makes sense conceptually
once you consider the same architecture
when trained differently

[00:10]
processes data differently so in the
case of bert
when it's trained as a mass language
model the context is encoded
bidirectionally so you have sort of
semantic information on the left and the
right
as such is the case when you are
when you are sort of decoding mass words
both um
anywhere sort of within a sentence
versus in the causal implementation
um you only ever see words to the left
of the word that you're predicting
um and so that was pretty surprising
in terms of um the results
um another another one that was pretty
interesting was sort of
um reform reformed a sort of like tiered
pareto frontier
meaning that some of the larger meaning
that some of the larger models
don't perform any better than the
smallest within the same tier
but they do use more compute so
essentially these models would be
sort of needlessly more expensive um

[00:11]
when you could just use this one
so that i thought was um pretty
interesting
reformer did have sort of one of the
best locs
of the models i tested um
i think particularly with reformer i
would want to
sort of see how this pattern persists
with some of the other architectures
and to sort of see if this is a pattern
that you can find with
all of the transformers that all the
transformers whose architecture directly
impacts compute
um so that may be like the evolved
transformer um
versus just reformer um so some of the
limitations i had
um i did limited hyper parameter sweeps
um some of the problems that i that i
found could have been solved
with that um really calculating scaling
laws with
irreducible loss um could have made the
the fits more precise which could have
revealed additional information
um the other piece is that like the

[00:12]
nature of this research in general is
that some of the comparisons are just
simply
apples to oranges and that there are way
too sort of
variations within the two different
architectures um and so
i think the next time i would really
want to to figure out a way to
isolate um as much of the differences as
possible so you know
what in particular is driving the
changes in lfc
um and last sort of why it matters um
so the architecture that scales best
is the most cost effective model to use
this is why this research matters
because it allows us to find the
architecture
to find that architecture and
potentially use our findings to
understand
what future architectures could look
like that continue to optimize
cost as we can see over time
the gap widens in terms of
the the gown widens in terms of

[00:13]
model perform the model performance you
receive
for the same amount of compute um and if
the slope is steep enough
and architecture can consistently begin
to outpace other architectures within
the expected range of compute
um so this sort of matters because
currently we're seeing ever increasing
amounts of acute uh
compute being used in the industry um
these scaling laws
um allow for up to allow for us to
optimize
large computer regimes and choose the
best architecture and model size that
helps reach this aim in my experiments
the reformer model was that architecture
that
produced the best power laws in
comparison to the others
the reformer model was designed to be an
efficient transformer and utilizes
several techniques to
reduce memory footprint and compute time
i think this directly i think this
direct impact on compute time is likely
why we see
such improved performance with it was

[00:14]
the only transformer architecture i
experimented with that had this property
but in my next experiments i'd like to
explain
expand the architectures i consider to
similar
styles of transformers and so
what's next for me is really just
continuing this study
doing more hyper parameting to expanding
the list
of models that i'm using and really just
expanding the experiment suite
to be able to more exhaustively draw
correlations and draw insights as far as
the connection between model performance
and compute
with respect to transformer architecture
um and last but not least lastly i just
wanted to say thank you um
i think it's been amazing time at open
ai it's been an incredible opportunity
um i really wanted to say a special
thank you to my mentors aaray and nick
and really thankful that i've been able
to have two um everyone else at openai
mariah christina pamela kathy
alithea i also wanted to say

[00:15]
special thanks to the tools that helped
made my research possible
um it would not have been possible to do
this
without open source tools like hugging
face deep speed and azure
and i think i might be out of time
so we'll see what
um what francis says but if anyone has
any questions feel free to ask um
if not we'll see what happens with
respect to time
yeah you can take one question okay um
do we have any questions
um okay so i see a question here that
said any
intuition as to the tier structure of
the of the reformer
um i don't think so i think that
so i think my only hypothesis would be
that um
because sort of the reformers
differences
because the performance differences are
sort of related to using tricks to
specifically
reduce memory and compute um my

[00:16]
thought is that the hyper parameters
matter a bit more with
reformers specifically that might not
necessarily
be the case with burt and transform
excel in any of the others
um so i couldn't isolate which one
specifically that was sort of driving
that change but that's sort of my
thoughts behind it

</details>
