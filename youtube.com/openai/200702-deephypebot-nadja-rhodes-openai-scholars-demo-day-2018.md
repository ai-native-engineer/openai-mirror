---
title: "Deephypebot | Nadja Rhodes | OpenAI Scholars Demo Day 2018"
channel: openai
url: https://www.youtube.com/watch?v=7dsNeABAbz8
youtube_id: 7dsNeABAbz8
published: 2020-07-02
duration: "11:07"
captions: en-orig
---

# Deephypebot | Nadja Rhodes | OpenAI Scholars Demo Day 2018

[![Deephypebot | Nadja Rhodes | OpenAI Scholars Demo Day 2018](https://img.youtube.com/vi/7dsNeABAbz8/hqdefault.jpg)](https://www.youtube.com/watch?v=7dsNeABAbz8)

<details>
<summary>자막: Deephypebot | Nadja Rhodes | OpenAI Scholars Demo Day 2018 (11:07)</summary>

[00:00]
hello everyone my name is Naja Rhodes I
was a software engineer at Microsoft
working on web services currently at
large I guess and I dedicated my summer
as a scholar to language specifically
generative models language why would
that be I'm really intrigued by artistic
creative applications of machine
learning computer vision is where the
coolest efforts towards this kind of
thing is focused in my opinion and it's
no wonder why I'm playing with visuals
and imagery is innately memorized
mesmerizing and fun procurements
meanwhile I feel like there's a
conspicuous lack of text-based creative
projects although maybe I'm following
the wrong people on Twitter so please do
let me know if you know any about any of
cool projects or cool people working in
creative NLP because I'd love to hear
more find me at the demo tables but my
suspicion about the imbalance is that
text has a fundamental challenge it can
be really hard to make sense of erratic

[00:01]
outputs as I learned this summer it can
be literally mine
mind-numbing in their incoherence and
instead of interesting like at all so I
read a lot of bad bad samples this
summer and then it's kind of because
there's different kinds of failures
right with them images there's this cool
project called text image where you type
a caption and then the Gann tries to
generate an image that matches that
caption so you can see that you know
when it tries to generate a cat sitting
on a windowsill in a room you kind of
get something cat like there's some fur
a general shape I don't know where the
head is but you know at least it's kind
of still compelling like you can still
look at it even though it's technically
a failure both tests it's like this is
the kind of stuff I was looking at
I'm gives the unknown token and yeah and
then a bunch of like repetitive stuff
and I like this dr. Seuss quote but
unfortunately it didn't quite hold up in

[00:02]
my summer because I was reading a lot of
garbage generations but you know every
once in a while it would give me
something that was you know somewhat
cohered
like a deep house too so it's kept
trying to talk about music house music
it's trying to say something about house
music what exactly I'm not completely
sure but it's kind of delightful like
you can kind of try to get a sense of
what it's trying to say and so my goal
for the summer of tech generation what's
the aim for good descriptive meaningful
generations but if all else fails at the
very least reach this kind of level of
delightful yet coherent so general text
but of what kinds the final project idea
that drove my NLP things this summer is
what I call deep pipe pot it's my
Twitter bot for all your generating good
music commentary and the idea was to
automatically detect tweets about songs
obtain interesting attributes about the
songs from Spotify and then use that to

[00:03]
condition the language model and feed
that into my model and produce some sort
of coherent commentary about the song
and this idea was largely thanks to an
inspiring data source called the hype
machine it's a music blog aggregator
throughout undergrad and ever since I
kind of relied on it because it has this
collection of small music blogs that it
gathers and then has these charts and
you can play music click through look at
the different blogs so early in the
summer I wrote up some API calling web
scraping rate limited Python code for
collecting this training data I'm
extracting it cleaned up over about a
hundred thousand sentences and so to get
into the deep learning a little bit my
momma employs a conditional sequence to
sequence a variational Honor encoder
that's a model language and why I like
this particular architecture is because
it first learns a richer representation
latent representation
of attacks and that it uses that
representation to generate new samples
and it works at a more macro or global

[00:04]
level because it encodes the entire
sentence versus like an LS TM which is
taking a history historical context and
then trying to predict word in a word
word for word locally and the VA e also
introduced some variability in the
generation process hopefully leading to
a little bit more novelty because it
randomly samples in the Leighton space
and mine was conditional in particular
because I wanted to provide some knockin
on text or context in particular I
wanted to use genre information and
Spotify has this cool API that gives you
these really specific genres like paper
soul optimism very hipster but it was
pretty good at like pinpointing exactly
what kind of music was going on so in
addition to the knowledge of general
past his music writing it could also use
a little bit of knowledge that wasn't
maybe in the text and then once I had
the VA II I refined it with something

[00:05]
called a latent constraints can
generative adversarial Network or else
again we were calling it it helps
control aspects of the text that's
generated by kind of letting you choose
what qualifies as a satisfying sample
because some is right here this blue
circle it represents the prior which is
the entire latent space learned by the
VA II most VA ease will completely learn
to use that entire waiting space so the
green blobby area is where like the most
realistic samples kind of lie and then
the red blob is where you decide oh yeah
these are the kinds of samples that I
like out of the dataset and so when you
apply the LC again it translates the
stuff from the realistic part of the
space into that more red part of the
space that's you know for my particular
case I wanted more flowery descriptive
language instead of like stuff about
maybe the artist
thing that might be this kind of data

[00:06]
set so what's nice about this is that
there was no reach retraining of the v8
you required it was more of a fine
tuning process and yeah so and the other
things that you need something that can
you need something so you need to be
able to pick out what's flowering and
what's not basically and you could do
that by hands but I decided to use a
topic modeling to do that because my
hypothesis was that with topic modeling
I could distill the commentary into
different types and as you can see I
made for different topic groups there it
ranges from topic one which has stuff
that says like beginning when driving
drums and famous song very vocal
harmonies that's the kind of feel I was
trying to get out of my generations
versus like topic model thirty up here
which is just like tour dates and stuff
um I did keeps and I did keep some of
this stuff in the data set even though

[00:07]
it's not exactly what I wanted to
generate just because it helps to have
data that the model can just generally
get a feel for English so you don't want
to like limit the data set too much and
just pinpoint the stuff that you want
necessarily
so just real quick this was about the
the Twitter bot appointment pipeline
that I had so it'll go from like a tweet
about pumped up kicks' for example send
it to Spotify get some johner
information from it feed into the game
and then come up with something that's
like kind of related it's really catchy
but the kind that hooks in those sounds
like Pumped Up Kicks to me and yeah this
was the most liked tweet so far it's
like the ployed at the iPod but I will
say that there are a lot of mad
generations like it's like so basically

[00:08]
I had to like feed this stuff into a
spreadsheet and then the human curator
which is me he gets to pick the best
ones too sensitive Twitter looking
forward it would be cool if I could take
these kinds of lights and feed it back
into the model and say people tend to
like this kind of thing so I'm gonna
give it more of this also called human
preferences sci-fi also has this cool
API called audio features that measures
aspects of a song like dance ability
energy levels tempo valence that'll be
cool instead of a genre perhaps and in
general in my future I'd like to do more
creative coding and more stuff with
language and it'll be so I'd like to
thank my mentor Natasha Jacques she's in
London right now some shout out some
women and the other open a scholars and
urban area and general thank you for
supporting this program thank you
[Applause]

[00:09]
oh yes
yeah absolutely yeah she asked if I had
considered feeding and the likes
retweets as some sort of reward and
reinforcement learning yeah my mentor is
super into reinforcement learning I
didn't quite get that far this summer
but it would be a cool reward signal for
sharing Thanks yes
right
I think so because yeah because you Sam

[00:10]
going from late this late in space you
can give it any kind of random latent
vector and like I was showing in that
little blob like there's a lot of space
where it's just going to be garbled so
but that's the space that you're working
with and so that again was supposed to
kind of help with that in that I could
then tell it okay but these are the
kinds of thought vectors that are still
realistic and still understandable but
also creative and like novel so yeah
it's definitely when a patient of the
Dae but and that's why I kind of put the
game on top to try this help counter
that oh yeah I mentioned mentioned that
like hands-on texted hard in general and
I've made it seem like maybe it's the
thing that people do but not quite it
turns out that like text isn't the
furniture rule when you do back
propagation or whatever yourself like
but the thing that I could do was
differentiate these effects are and that
works thank you

[00:11]
[Applause]

</details>
