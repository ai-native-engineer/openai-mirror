---
title: "Using Semantic Trees In Place of Sentences | Munashe Shumba | OpenAI Scholars Demo Day 2018"
channel: openai
url: https://www.youtube.com/watch?v=dFpQ830Y5qo
youtube_id: dFpQ830Y5qo
published: 2018-10-06
duration: "10:49"
captions: en-orig
---

# Using Semantic Trees In Place of Sentences | Munashe Shumba | OpenAI Scholars Demo Day 2018

[![Using Semantic Trees In Place of Sentences | Munashe Shumba | OpenAI Scholars Demo Day 2018](https://img.youtube.com/vi/dFpQ830Y5qo/hqdefault.jpg)](https://www.youtube.com/watch?v=dFpQ830Y5qo)

<details>
<summary>자막: Using Semantic Trees In Place of Sentences | Munashe Shumba | OpenAI Scholars Demo Day 2018 (10:49)</summary>

[00:00]
hi everyone thank you for taking time to
come and see what we've been working on
last a couple of months
my name is Manoj Jaya and my project was
on investigating the effectiveness of
using somatic trees in place of regular
sentences when it comes to natural
language processing our problems so to
get started let's take a look at some
quiz questions okay
I have pairs of sentences that either
mean the same thing or doughnut hole or
somewhere in the middle I want you to
take a look at them think how closely
related in their meaning they are and
come up with a score from 1 to 5 if
that's too hard for you you could come
up with a score from low medium to high
alright I'm gonna give you couple

[00:01]
seconds to think all right now I'm gonna
tell you this course the first two
sentences they are pretty closely
related in the meaning talking about
dogs fighting wrestling sort of the same
thing the second one not really related
except that it's somebody doing
something the last one somewhere in the
middle in one sentence
there are kids with a football in the
other there kids with that if the ball
so like I say my goal is to investigate
the effectiveness of using semantic
trees in natural language processing
instead of using a regular sentences
alright so for the tests that I just
gave you the quiz if one is to build a
model for it you're probably lsdm s
because we're talking about sentences
it's sequences and it looks something
like this

[00:02]
data would flow through the Ella stem
cells from the first element of the
input to the end all right and then at
the end of the Elysium layers you have
some combination that gives you a
prediction so now let's take a look at
the inputs it's a sentence and
represented as a sequence but is that
really how we really think about
sentences is that really how we portray
the meaning of a sentence if I were to
summarize this sentence let's say maybe
it's about I mean it's really about our
fighting ok I'll put that down fighting
but who's fighting some dogs dogs and
when is it happening it's happening now
or which dogs two dots okay you can see

[00:03]
from the top you have the most important
aspect of the sentence basically the
essence are the meaning and then as you
go down you get more details about how
this is happening the further down you
get you get even more details about the
children are far the top-level aspect
same thing goes with the other sentence
which was in the quiz two dogs are
wrestling and hugging
it's about wrestling and they's hugging
happening with wrestling okay let's move
on the task that I chose for this
investigation was semantic relatedness
so you get two sentences just like in
the quiz and you have to come up with a
school that saves how similar again in
meaning the sentence is armed and I used
it is it cold sick no idea come up with
that name this dataset has 10,000 pairs

[00:04]
of our sentences 10,000 scores to go
into the
the sentences and I also used a glove
which is an embedding for words okay in
order to convert my sentences from this
data from this sick database this is
sick dealer said I used synthetic net
which is very well known as parsing on
phosphates and the output looks
something like this make some mistakes
sometimes so you have to manually
correct it so from there I built a model
again based on SDO I'm sorry LS CMS and
it looks like that same as from before
just with additional details so the
question now is how do I feed my trees
into an LST M because remember elysium
sequences they work with sentences but
trees are you know not quite sequences

[00:05]
so what I did is was to express my trees
in sequential form pretty easy I did
depth-first search
so the sentence on the left ribs end
about that tree which is truth of the
finding Simpson is from before that
becomes fighting the main main idea
forward by the children are fighting
children are dogs and are ok but dogs is
a child of its own so the child appears
in its onset Bart gets set of brackets
right in front of dogs so I trained my
models in fact I've trained two models
one I used depends the trees oh by the
way this fries are called dependency
trees so one model I use that this
depends the trees and in the other I
just use regular sentences and again
when I say dependency trees here are I'm
talking about
the sequential presentation alpha the

[00:06]
tip it is dependent the trees from the
precursor slide over here what I
observed was that the model trained on
dependency trees had significantly lower
min squid error a surprise there 0.35
and the one that was trying to radiances
had 1.3 so that's about three point
seven times the amount of the air if you
look at the scale on the horizontal axis
you can see that the trees model only
trained for very few number a very small
number of cycles so it got to the
perfect level at about 150 steps but the
other model it took about one point
eight so 106 million steps so
significant significantly more they had
about the same amount of for training
loss it's just one arrived at the same

[00:07]
loss after significantly more steps the
next step from here is to instead of
using a LCM cells I'm planning to use
three LST ohms which is this STM that is
a specifically for our trees so instead
of for working on sipping seeds it works
on trees
I'm also going to try to use that this
same idea on question answering are
using the squad database sorry the squad
dataset what I've noticed is that with
that depends the trees it's actually
really easy to manipulate them so if for
instance you wanted to up meant the
dealer could maybe change the order of
five children in the trees and then come
up with a new set of trees which you can
just pile onto your data set you have
more data it works in most cases there's
some cases where you just can't do that

[00:08]
I'd like to thank my mentor I was not
able to come to this event
my name is that yes mean she's been a
great help and also I'd like to thank
the open e aí team for supporting us
throughout this program all right I'm
gonna open out for questions so feel
free
[Applause]
yeah good that's a good question this
question was how were the scores for the
sentence pears are calculated wasn't
actually an empirical score it was
decided by people there was significant
consensus but it's really not it's
really not an empirical so you can
really quite measure it
I'm sure you could try to come up with
ways of creating a criteria for you know

[00:09]
what's a 1 and what's a 5 and wasn't
middle but uh yeah it was a lot of
people who curated the data said this
cause and there was a significant
consensus on now on the schools and you
can go and take a look at this cause and
I'll see how you feel about it when I
was looking at the date of myself just
you know taking browsing through it I
sort of agreed with this course it makes
sense but yeah it's not empirical yes
great question the question was how did
I fit in the words for the tree and what
I do with the parentheses I used our
glove for embedding the words and then
for the parentheses because you know
parentheses actually do up here in
language you could have sentences that
do have parentheses so I I couldn't

[00:10]
really use parentheses so what I did is
I created my own symbols and I
specifically made him so that they were
far away from the rest of the words
I give them you know really high values
for their vectors and the two the two
symbols for the opening parentheses in
the closing parentheses closer together
but again they were really far away from
the rest of the day just to make it
create the model that this is these are
not you know this is not the same same
kind of data all right I think that's
all I have
all right sorry I ran out of time but
thank you so much
[Applause]

</details>
