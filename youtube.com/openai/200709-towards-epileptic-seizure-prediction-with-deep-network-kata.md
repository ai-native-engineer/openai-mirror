---
title: "Towards Epileptic Seizure Prediction with Deep Network | Kata Slama | OpenAI Scholars Demo Day 2020"
channel: openai
url: https://www.youtube.com/watch?v=AT2XkqJAZns
youtube_id: AT2XkqJAZns
published: 2020-07-09
duration: "15:17"
captions: en-orig
---

# Towards Epileptic Seizure Prediction with Deep Network | Kata Slama | OpenAI Scholars Demo Day 2020

[![Towards Epileptic Seizure Prediction with Deep Network | Kata Slama | OpenAI Scholars Demo Day 2020](https://img.youtube.com/vi/AT2XkqJAZns/hqdefault.jpg)](https://www.youtube.com/watch?v=AT2XkqJAZns)

<details>
<summary>자막: Towards Epileptic Seizure Prediction with Deep Network | Kata Slama | OpenAI Scholars Demo Day 2020 (15:17)</summary>

[00:00]
so I'm one of the people whose
background was in neuroscience I
finished my PhD before starting the
program and I had gotten progressively
more excited about deep learning
throughout my PhD and all the exciting
things that it can do especially as
evidenced by all the cool things that
open AI keeps doing so I'm really
excited to be in this program and I
picked a project that's are close to my
heart and that works with neuroscience
data where I had some experience so I
was working on predicting epileptic
seizures using deep networks so what are
seizures a seizure is when the neurons
in your brain start to fire to
synchronously for your good
so at worst they will take over your
whole brain and you will literally pass
out if you have a lot of seizures
repeatedly so there recurring and
unpredictable you might be diagnosed
with a disorder known as epilepsy
epilepsy affects about 1% of people
across the globe and disproportionately
so in the developing world the fact that
seizures are unpredictable in particular

[00:01]
causes anxiety for sufferers they will
suffer physical injuries from accidents
because they didn't see an oncoming
seizure and also in most countries
people with epilepsy understandably are
not allowed to drive cars which will
take a toll on their quality of life in
many places in the world so if we could
predict seizures better we could
contribute to reduce anxiety fewer
injuries and in the best case we might
bring the drivers licenses back and make
it possible to drive safely again and it
also has the potential to contribute to
brain stimulation treatments to actually
alleviate the epilepsy itself now up to
20 years ago it was actually unclear if
seizure prediction was even possible
because in order to predict an upcoming
seizure there needs to be some signal
somewhere in the brain that gives away
that that a seizure is coming before the
seizure has happened so 20 years ago
people were still debating whether this
signal exists at all
now anecdotally for people with epilepsy
it was not surprising that seizures can

[00:02]
be predicted because some people with
epilepsy and hot dogs who have been able
to alert them to an oncoming seizure
ahead of time and it was only recent
recently proven that this is in fact the
case and that the dogs do it based on
so there is some brain signal that gives
away that a seizure is coming it's a bit
hard to pick out what exactly it is
epileptologists don't know exactly what
the signature is and so it's almost a
problem that asks for neural networks so
the data set that I worked on was
publicly available from Cargill and it
was she's male select pointer here so
that people can see so I used two
publicly available data set from Cargill
that had recordings from from dogs from
voltage sensors so it has time series
recorded from different places in the
dark Sprint's both from time points
right before a seizure is starting up to
when a seizure starts so when you see
this abnormal synchronous activity and

[00:03]
so the way that I worked with this data
is that I took the raw signal that was
available both from time periods really
far from a seizure so the brain is just
hanging out it's at least four hours
until any seizure and from an hour
before a seizure so when there would be
these signals that something dangerous
is going to happen we I I pack this data
into smaller time chunks which were then
basically labeled data that could lend
itself for to a classification problem
so safe epoch and then dangerous epochs
from an upcoming seizure and converted
this into an image representation and I
apologize that part of this is covered
here so into a spectrogram
representation and what spectrograms do
is that they take time series
information and and will highlight
basically the frequency content of those
time series so both if there's a lot of
lower frequency content or as here in
the simulated danger signal if there are
these periods of higher frequency
content in the original data set that I

[00:04]
worked with one second
yeah excuse me so in the data set that I
worked with it I had data from five dogs
and it was highly imbalanced so say dog
three here represented most of the data
and also we had much fewer of these
target sequences that that Herald in an
upcoming C shirt than that then we had
safe sequences this could cause a number
of problems when you train neural
networks so for example the network
might cheat and really overfit to dog
number three or just always guess that
every epoch is safe which is a problem
when you're trying to predict a seizure
so the first thing that I did was that I
sub sampled this data so that we had
equal representation from all of the
dogs and also from all of the from both
of the classes so the danger episodes
that I labeled with X's here and also
the safe episodes and some early results
that I find so in the balanced data set

[00:05]
were chance level performance would be
55% I got to 69 percent accuracy with a
rest net 18 model a baseline model which
was a regular logistic regression with
match normalization I got to 55 percent
accuracy now when you think about models
like this it's important where you set
the threshold for whether you label a
tiny part to be dangerous or safe and so
if you're working with predicting a
seizure you might want to make sure that
you catch every seizure so that you
definitely don't leave anything
unpredicted but if you do that depending
on how good your model is you might also
be creating a lot of false alarms and so
an ROC curve is a way of quantifying how
is that trade-off going and so ideally
you basically want this RC curve to push
up towards the left hand corner and you
want that area to be one you never get a
model that's that good but you want to
push it in that direction and our model
is about point 77 so what does this mean

[00:06]
in practice that if I want to catch 99%
of all of the upcoming seizures well
then I'm also going to label just over
80% of the safe episode as seizures
episode says seizures so we still have
somewhere to go but we're not a chance
another way of looking at this trade-off
is with
precision recall curve and that has this
true positive rate on the x-axis and so
in that case if I say okay I want to
catch 99 percent of all of the seizures
well then out of the the epochs that I
labeled that I labeled as being
dangerous actually only like 55 percent
of them really were dangerous that's
another way of looking at that trade-off
and a third way is something called the
confusion matrix and the way that you
want this one to look for a good model
is that you want to have really high
numbers on the diagonals and low numbers
on the off diagonals and so again we're
getting there with this model we're not

[00:07]
quite there
and so basically about 72% of the true
seizures are labeled as actually
seizures but not all of them so that's
one thing that you can take from this
confusion matrix
so in conclusion so far we've shown that
our model has shows some promise but we
still have ways to go on this and the
directions that I wanted to take this
moving forward I'm really excited to
continue working on this project is that
I want to make the prediction better by
hyper parameter tuning and
regularization there's also a lot of
opportunity to vary the neural network
architecture trying larger rest nets and
maybe sequence models and also looking
at different kinds of pre-processing
once I have a network that performs
hopefully really well I'm excited about
interpreting what the network is
learning using some of the methodology
that the clarity team at open AI is
working with I've started a bit with
visualizing the network weights but I'm

[00:08]
not ready to tell you about that yet
today and I'm also excited about looking
at activation maximization approaches
I'm really grateful for having had the
opportunity to be in this program I
learned a lot I really enjoyed working
with Pi torch every day learning how to
train and evaluate neural nets excuse me
debugging neural nets and also this side
of deep learning that you don't see when
you just look at it from the results
side so working on a virtual machine and
cloud infrastructure that's definitely
being both a challenge and really really
good a great to get experience with I'm
grateful for lots of people and I should
also say
now it's a great time to start to send
your questions over I will take those
after my thank you slide see if there's
anything there yeah so first and
foremost I'm really grateful to my
mentor Johannes who in Sam's words from
yesterday has been like a co-pilot with
me helping me debug in person and doing
pair programming with me I'm really
really grateful for the existence of
this amazing program so thank you so

[00:09]
much to Greg and Sam and open AI for
making that happen I'm grateful for our
to our program mom and dad Christine and
Mariah after Frances for organizing this
event and also our interview day my
fellow scholars have been a really
really great source of community and
support during these challenging times
that we've been here and I really
enjoyed connecting with everyone at open
AI over the course of the program so the
clarity team especially little big
interests have given me great advice
Paul and the reflection team has also
given me really great ideas and I really
really enjoyed meeting people for lunch
when we were still in the office and for
other virtual donut chats that we have
had since after that okay and are there
questions coming through are the data
from the dogs detecting seizures or
having seizures themselves a great
question so it's um I have data from
basically safe time periods let me go
back to that slide that are really far
from the seizures and then from up to

[00:10]
one hour before the seizure so we don't
actually have any data from the seizure
itself we're trying to find a signature
of when a seizure is about to happen
into the future thank you for that
question
you
yeah okay the next question says since
this is based on from neural data what
challenges do you see in making this
useful for those that suffer from
epilepsy
I am parenthesis perhaps falsely
assuming it would be difficult to have
access to this data for an average user
how can you model and how can your model
and future work plug in to their daily
lives great question so it's an it's a
matter of stages actually people with
epilepsy will sometimes choose to have
surgery to control their epilepsy and
some people will have implants like
closed loop deep brain stimulation to
control their seizures and so then you
would actually have exactly this type of

[00:11]
intracranial data to work with to make a
predictive model in other cases what
would be more relevant for most
sufferers of epilepsy is that you would
have not an implanted type of brain
recording device but a scalp EEG that's
on top of that's outside of the skull
and then you have less signal to work
with but it's still a similar signal so
the hope is that once we can figure out
good models with intracranial data that
we might also be able to train models on
on other brain data that's less invasive
but has a little bit less signal did we
have what was the reasoning for choosing
the pre trained arrest net 18 yeah so we
started with the idea that the
spectrogram is a good representation of
neural data source and neuroscientists
we often work in the spectrogram
representation and different oscillatory
frequency bands are thought to convey
different information in the brain so
once we decided to work in the
spectrogram representation really

[00:12]
they're like images and so we also
worked with a bit of vanilla coordinates
but rest nets are really quite good
models for image classification so we
decided to use that one but for sure we
could we could try other architectures
as well and that's a future direction
so sorry I should read out the question
the next question was which layers of
the network did you retrain if any so we
actually didn't use a pre trained model
so we trained the model from scratch we
use the existing resonant 18a
architecture but then trained it from
scratch did we have more questions how
similar do you expect seizure patterns
to be from one patient to another are
there categories of seizure types or is
there a wide variety of signals okay
this is a great question from one
patient to another those might be pretty
different so right now we reused all of

[00:13]
the darks data together but I know that
most in the literature successful
seizure prediction models have been
within patient so they do seem to differ
by category there are absolutely a lot
of different kinds of seizure types and
that's an open question in the
literature if you could categorize that
some types of seizures are more lend
themselves more to prediction than
others thank you
what do you think would improve the
model accuracy more data cleaner signal
yes more data more data cleaner signal
both of those things would improve the
model accuracy I should say also that
now the effects that we worked with were
from up to one hour before the seizure
started it's actually not clear how much
in advance you can predict you can't
predict a seizure it might be in some
cases that the process that that
generates the seizure has not actually
started an hour before so some of the

[00:14]
labels that we have as being danger
signals might actually not have the
information to predict the seizure so
one thing that we're going to try is to
turn it into a multi-label
classification problem and separately
predict epochs that are maybe only 10
minutes before the seizure is starting
versus the ones that are one hour before
so that would improve model accuracy
also the way that this data was set up
from Cairo was actually in 10-minute
epics and we subsample them to 22nd
epochs so we could train a second model
a hierarchy up to predict the fall
ten minute chunks that will also improve
accuracy I'm also looking at increasing
the segment lengths because maybe the
warning signal is not there in every
single 22nd epoch another thing is that
right now we treated each spectrogram
from each electrode as a separate
observation implicitly assuming
independence between electrodes which is
likely not true and there might actually
be a lot of information in the

[00:15]
correlations between electrodes but each
dog had a different number of electrodes
so it wasn't straightforward to just set
it up as a as a 3d tensor but that's
definitely something we'd like to look
at in the future to also give the
network an opportunity to learn from the
correlations

</details>
