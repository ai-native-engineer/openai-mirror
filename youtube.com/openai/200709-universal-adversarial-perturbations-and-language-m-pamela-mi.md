---
title: "Universal Adversarial Perturbations and Language M… | Pamela Mishkin | OpenAI Scholars Demo Day 2020"
channel: openai
url: https://www.youtube.com/watch?v=7wqmXo0Jqa4
youtube_id: 7wqmXo0Jqa4
published: 2020-07-09
duration: "18:10"
captions: en-orig
---

# Universal Adversarial Perturbations and Language M… | Pamela Mishkin | OpenAI Scholars Demo Day 2020

[![Universal Adversarial Perturbations and Language M… | Pamela Mishkin | OpenAI Scholars Demo Day 2020](https://img.youtube.com/vi/7wqmXo0Jqa4/hqdefault.jpg)](https://www.youtube.com/watch?v=7wqmXo0Jqa4)

<details>
<summary>자막: Universal Adversarial Perturbations and Language M… | Pamela Mishkin | OpenAI Scholars Demo Day 2020 (18:10)</summary>

[00:00]
great thank you hi everyone I'm Pamela
welcome to this production of Hamilton
on Disney plus today we'll be talking
about that is the laugh line no I got
we're talking about adversarial attacks
on NLP models so a lot of my work in the
program has been about critically
thinking about how we motivate this work
this talk will mostly be a commentary
and analysis about the state of the
literature on adversarial attacks in NLP
so as some background the image space
has robust literature I'm using targeted
manipulations and model interpret
ability to understand and things like
adversarial attacks controllable
generation and intersectional bias these
push there's also push from policy
makers to understand how marvelous work
and what failure states exist models
exist in the wild we're beholdin for
their bias and their failure States
everyday and so I sort of wanted to
strengthen my understanding of how we

[00:01]
quantify those failure States so a lot
of this work is motivated from a 20-19
paper from Alan AI led by a team with
Eric Wallace where they define they call
a universal adversarial trigger which is
a short phrase that can cause a specific
model prediction and when concatenated
to any input from a dataset and the kind
of productive
fresh your slides so that we get the
most updated one as it seems to be stuck
stop is that there there we go okay
well if you try so the paper
demonstrates the triggers transfer
between models they're both model
agnostic and inferred agnostic what does
this look like so let's say we have a
sentiment classifier can you see the
diagram
okay um so let's say we have a sentiment

[00:02]
classifier um given the input the movie
was awful we'd expected to classify that
as negative um but a trigger would look
like something like and this is a
trigger we found when we ran this some
of you uh invigorating captivating um so
that appended to the movie was awful
would flip the resultant classifier from
negative to positive it seems like we're
still having a little bit of trouble
with your slides I'm not showing a blank
it takes a little bit to show now you're
finally know I'm fine okay can you see
them now still okay I might have to do
you might have to see my whole browser I
guess is the punchline does that is that
right yeah slide and if it doesn't
refresh really quickly we might move
your slides for you okay so so this
would flip the output from negative to

[00:03]
positive and they sort of clear why this
is a failure in the case of the
classifier right we know what the output
should be this is this is changing the
output to the wrong answer in a language
model it's a bit less clear so what a
language model does is given an input
like the movie was we'd expect it to
complete that text in a way that makes
sense given the contact so the movie was
a great film yeah okay response from a
language model what a trigger would do
here is when we append some tokens wrap
you know fun basketball football all
sports words to the movie was the
language model would instead complete
that with text about sports and it's
kind of less clear whether we should
consider this a failure this trigger in
particular prepended or appended to the
input may not be content preserving on a
simply this many words about sports
might change the meaning or intent of
the original input that's another
example adding a six token string to the

[00:04]
end of any Shakespeare play shouldn't
result in hate speech even if the play
is the Merchant of Venice so we want to
sort of understand how stealthy we need
to make these triggers to make the
the language model qualify as a failure
um and that question is clearer in other
spaces like audio or vision we can use
whether a trigger is perceptible or
imperceptible by humans as a guide we
don't have a tool to easily assess in
perceptibility for language um but one
thing we may want to try is making
trigger stealthier so both as short as
possible and constrain to language that
makes semantic or natural sense if I saw
this trigger in the wild I'd say
something's up you don't just throw a
bunch of sports words together
um whereas well it's difficult so where
it's difficult to say whether the
behavior in this slide should be
considered a mistake or not something
like this
we're just dependent cats - the movie
was and language models except dogs we
could probably say is wrong so how do we

[00:05]
find these triggers great questions um
so we can't apply the techniques develop
in the vision space directly to this
problem for one language is discrete
whereas images can be continuous as a
way of seeing that think about a rainbow
goes from red to orange to yellow we
touch every color in between we don't
have the language to describe all of
those colors in between so we
approximate this is the hot clip attack
and this slide is which you can
hopefully I'll see it um it's taken from
the original paper so we come up with a
neutral trigger in this case the the and
we'll append that to a batch of examples
we then back prop on the gradient
maximized and we'll likelihood at the
class we're trying to flip - so here you
see a bunch of positive examples of that
film and we're trying to flip those to
negative and we do this for some number
of iterations we go from the two movie
Apollo spider to zoning tapping themes
in the end so we do it for some of our

[00:06]
iterations or until we don't see any
changes in the loss and just to note in
the language model case our loss might
maximize for example the likelihood of
the target outputs we're trying to find
a trigger for so one condition on it any
user input we should reach those target
outlets and using this we replicated the
results in the original paper across
of tasks so sentiment analysis natural
language inference squad and GBD two
attacks on these tasks we see that
accuracy drops close to zero and you can
see also that we when we allow the
trigger length to increase attack
becomes more potent so the less selphie
the trigger the better it is a viewing
this increasingly the results on the
right is with random attacks rather than
hop flip and it also works pretty well
so it's unclear whether we need to do
all of this maximizing the feature space
great so why would we want them attack

[00:07]
like this
that's a good question um I think this
is where my work deviates from Wallace
is a bit the motives for an adversary to
engage in this kind of attack or weak
the clearest use of universal trigger is
that we may not have access to the
target model or the particular input at
runtime because Universal attacks do not
require a white box access and work on
any input they can be easily distributed
even without technical knowledge but
it's still kind of unclear how you to
use them so for example the threat model
is posed by a very deliberate and
unlikely attack you come up with the
universal adversarial trigger you hack
into a GPT to server you append the
trigger to all inputs come and go for
the server and you kind of watch a wreak
havoc but if your real goal is to wreak
havoc you could also just write some
hate speech and post it online which is
far easier in a car as far less
technical know-how and if we look at how
G adversaries use gbg to it in the model

[00:08]
in the wild not that many people were
really engaging in text like this just
as one example if you search for GPT 2
on YouTube some of the first results are
people being like how do I use this to
boost my channel but with largely
neutral comments not with how do I
attack someone else's channel with hate
comments so as another motivation we can
sort of think about what triggers as
examples of failure states of our model
so we've approached if not reached human
level accuracy on a number of tasks
returning to the sentiment analysis we
were talking about before here you see
that we're approaching 100% accuracy
honest
- um what a few questions remain in this
like 3% that we're missing what are we
missing how robust are these models and
what has the model really learned and
how generalize generalizable is it so -
dick on on the first question our robust
er models in real life language
undergoes perturbations all the time you
might say your friend wow that movie was
so good and they might miss the sarcasm

[00:09]
and check someone's game she said the
movie was really good and the classifier
will then say that that was a positive
review these deviations could take
multiple forms they can be adversarial
triggers they could be random noise a
typo they could be structured nuanced
tone is an example sarcasm obfuscation
hedging a lot of questions along the way
or sort of data set bias second question
how generalizable our models how prone
are they to memorization we know that
Elam's learn from any potential data
sources the model design also influences
how likely they are to generalize from
that data or memorize that data so we
see in low resource languages on google
translate given kind of nonsense
triggers the language model will devolve
into sort of satanic verses from the
Bible and this can be weird when it
comes to Bible verses but also creepy
when it means to memorize personal data
as it came from Berkeley showed so we

[00:10]
want to sort of like see triggers as
examples or ways to sort of get at
answering these questions so I tried to
do that first I looked at the
stealthiness question of just like how
good can we make the trigger given this
threat model and how and what happens
when we try and do it so we were able to
replicate the results of the original
paper the decreased accuracy on
classification tasks top tasks and
random attacks tended to work as well
when we tried to force the triggers to
be more stealthy by sampling directly
from GPT - instead of using hot flip the
results were less promising so I don't
want to say definitively that there
don't exist
stealthy triggers that will flip SSD -
for example but we weren't able to find
them in the few techniques we tried
as another one movie sort of looked at
these results in the paper that were
forcing triggers to get G B D G to
devolve into generating hate speech in

[00:11]
our experiments coming up with triggers
to generate hate speech wound up with
triggers that were largely hate speech
in and of themselves notably these
triggers transferred to GPT three as
well you saw that there are twenty
percent of cases they also create a cape
speech on GP g3 and they also regularly
highlight particular people so I'm not
going to show examples of hate speech
right now but at a lot of the racism
triggers we saw the word Coulter
presumably my friend and Poulter you saw
Hannity presumably referring to Sean
Hannity
and so while these are public figures
and we don't necessarily just be
concerned about that being private
information about them it is interesting
to note there's sort of aspects of those
particular people but G PDQ has learned
in Sanko sucked we also saw the hate
speech triggers target at a particular
protected class produced outputs against
other classes as well so racism and
sexism triggers on GPT three produce

[00:12]
ablest at homophobic text so we also
were considered how they applied to
charge but slightly less polarizing text
so we showed that triggers exist for
other top fixed looked at vaccines and
brexit um though our evaluation
suggested that they're slightly less
potent so here are two of the triggers
we found for vaccinations and and we
appended them to we used generate on
their own we use this first seven lines
of the Merchant of Venice and the first
one at the Merchant of Venice prepended
and appendage to trigger and here are
some of the results so you can see that
the first one it has to do with vaccines
which is expected but in and of itself
is not an SI backs whereas all of the
text in the target text was an tee box
um the second appended to the merchants
in Venice you sort of lose the meaning
of the trigger altogether um we see that
this is not Shakespearean language but

[00:13]
is a key PDQ approximation of it
but a penalty just one line we do sort
of still see a mixing up the queue so
this isn't the best example but we saw a
lot of examples of kind of Shakespearean
talk about sickness or illness for the
things you expect vaccines to be
associated with so whereas a racism
trigger would always produce racist
content an auntie backs trigger won't
always please auntie backs on it
so in conclusion um
targeted perturbations are a rich area
in the image space and if you used to
create generative models and as a Terp
rebill 'ti tools they are to apply this
language this method to language we need
clear normative goals for LMS and and
all these systems we did show that
models are still brittle even some of
the best trigger is transferred to gbg3
in more study of the triggers we find
would be an interesting direction to
take this so why do they behave in this
way and why do they tell us about how
models learn in general in this one way

[00:14]
one direction we might take this for
gbg3 and few shot learning you're given
a task description and a number of
examples but the class description is
written by humans with an idea of how
they would bring that task we can
instead consider the task description as
a trigger and back up on these examples
to find sort of maximize the likelihood
that the model will be able to perform
this task um so my thinks everyone
particularly my mentor Alec who I'm sure
is did not want me to thank him it's
great and my fellow scholars were great
and Christina Mariah and everyone I
chatted with on slack throughout the day
really fun program so you and I time
Thanks
it is there a way to represent languages
continuous I mean we sort of cast
language into a continuous space using

[00:15]
word vectors but it's and we can sort of
see a continuous like aspects learned of
that language so for example we take one
of these vectors for king - Queen and we
might get man - woman um I was
representing the same thing but that's
all what approximation so yeah if you
think of a language while senator
Specter couldn't attacker be motivated
by changing the sentiment um I think
they could it's just again and like if
you were to knock into a system and
upend this trigger to any task by the
time you're in assist them doing that
you could just force the output you want
um I don't know why it's lower I have a
sense of why it worked which is we were

[00:16]
using a very brittle classifier or just
looking at simple lsdm
um sorry I guess I should read the
questions why do you think the rate at
which the accuracy drops off in terms of
the trigger length is lower for random
than non-random fares um I don't have a
sense of why it's lower I think it works
because we were using a pretty brittle
classifier we're tagging sentiment on
pretty short sentences anyway so do like
the classifier is just getting
distracted by the additional words
regardless of what those words are
seemed to be uncommon or even
nonsensical phrases
on the inputs every means of trigger or
out of distribution detection I think
that's definitely a reasonable question
I think that's why that's all another
reason I think it's that you can to
frame this work as these triggers aren't
going to be seen in the wild though
absolutely if you did encounter one in

[00:17]
the wild you automatically be able to
talk to them I'm wary of anything that
sort of like suggests we just build it
attack the detector on top of a bottle
because if you look at the image space
every defense you come up with for one
of these attacks another attack just
emerges in its place I think we can
instead see the full class of things we
consider attacks or defenses and sort of
say that actually tells us something
interesting about how these models work
and we can recache the problem in that
way
hope there's nothing okay could you
experiment with the granularity of the
triggers um
did a little I also tried to do more or
and it didn't work so we did I did for
the GPD to trigger is try and sample
directly from GPD to unique language
that didn't feel jarring to encounter in
the wild and they don't work nearly as
well and when they do it sort of makes

[00:18]
sense that they work um we think it's an
example of the language model doing what
we'd want them to be wouldn't what we'd
want it to do

</details>
