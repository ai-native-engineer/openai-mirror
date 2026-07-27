---
title: "Audio Models in the API"
channel: openai
url: https://www.youtube.com/watch?v=lXb0L16ISAc
youtube_id: lXb0L16ISAc
published: 2025-03-20
duration: "15:25"
captions: en-orig
---

# Audio Models in the API

[![Audio Models in the API](https://img.youtube.com/vi/lXb0L16ISAc/hqdefault.jpg)](https://www.youtube.com/watch?v=lXb0L16ISAc)

<details>
<summary>자막: Audio Models in the API (15:25)</summary>

[00:00]
hello everyone and welcome to another
live stream of open AI I'm Olivia gar I
lead the open platform as you all know
we've been busy building agents for the
past few months deep operator research
um deep research operator and just last
week we released the agent asdk which
allows you to build your own custom
agents today is really really exciting
we're moving beyond text to voice
agents many people prefer to speak and
to listen over writing and reading so in
a way voice is a very natural human
interface and today we're going to
enable developers and businesses to
build voice agents agents which are
reliable accurate and flexible and so
we're going to announce a bunch of new
models and tools for that so let's hear
it directly from the team who built that
offering thank you Olivia

[00:01]
hi everyone I'm Shen I work on open AI
research team hello I'm yaroslav I'm
engineer on openi API team and I'm Jeff
Harris I work on the open AI API product
team today we're releasing three new
models and a bunch of new tools and
capabilities designed to make it really
easy for developers to build Rich
humanlike voice experiences we have two
new state-of-the-art speech to text
models that outperform our previous
model whisper on literally every
language that we've tested we have a new
text to speech model that for the first
time let's Developers control not just
what the model says but how it says it
and then we have a big update to our
agents SDK to make it really easy to
turn text based agents into voice agents
so let's post for a second what is a
voice agent and how do I even build one
yeah great question we think of agents
in general as AI systems that can act
independently on behalf of a user or a
developer so you might see a text agent
if you visit a website and you see a
chat box in the bottom right and you
want to ask about the product catalog or
your recent orders that's by text you
can do the same thing with voice so you

[00:02]
can call in and be speaking to an AI
voice um there's other ways to use voice
agents one of my favorites is language
learning experiences where you can have
a voice agent that's coaching you on
pronunciation creating a lesson plan for
you doing mock conversations with you in
the language that you're learning many
many ways to build voice agents um and
we see two primary approaches that
developers take the first one is using
more futuristic speech to speech models
these are models that are capable of
understanding audio directly and
speaking directly back they're really
fast they're what powers advanced voice
mode and chat GPT and our real-time API
the other approach which a lot of
developers do as the way to get started
in voice is what we think of as a
chained approach where you take a speech
to text model understands what the user
says turns it into a text transcript
that's then processed by a Texton llm
like GPT 40 and then that model figures
out an appropriate response and passes
it to a text to speech model to speak
back to the user developers often love
the chain approach first cuz it's

[00:03]
modular they can mix and match all the
different components so they're using
the best models for their use case they
also love it because it's the easiest
way to get really high reliability the
gold standard in terms of intelligence
is still Tex based models though the
speech to speech models are't catching
up quickly and then the third reason
they love it is it's easier to get
started you can take all of the work
that you've done in a text based agent
and you can Preen to speech to text
model on one side put text to speech on
the other side and now you have a voice
agent so for today we're mostly going to
focus on how we have new tools to help
you build voice agents with that change
approach so let's get into it a few
things to cover we'll start with speech
to text where we have two new models GPT
40 transcribe and GPT 4 mini transcribe
you you've been working on these models
I'd love to hear how they were built and
how they perform yeah thank you Jeff I'm
happy to introduce more technical
details for our new uh Speech to Text
models um compared to our last
generation models whisper and the
whisper 3 our new generation model is
based on our Lar speech model this means

[00:04]
this new model has been train on
trillions of audio tokens it all also
inest our latest Technologies and also
architecture of our models we also
distill the larger model down to a much
smaller size one which is the GPT 40
mini transcribe the smaller size model
is faster and more efficient it also
retain as good transcription capability
as possible compared to the larger
models let's see how good our models are
we measure the accuracy say of our
transcription by word error rate the
word error rate is the percentage of
words that our model gets wrong so of
course the lower the word error rate is
it means the higher our model actually
performs and then the dark blue is the
newest 40 and the one beside it is 4
mini exactly as you can see compared to
our previous generation models with per
two and with per three our newest model
actually perform almost like um on every
single language we performed across the
board nice aome very cool let's also

[00:05]
take a look at uh where we are you know
on the compared to the other options on
the market nice so what I'm seeing here
is that the new model is state-ofthe-art
across many languages English Spanish
more um and then actually for om Min is
state-ofthe-art if not for its bigger
Brother model as well yeah if you are
actually looking for a very high
accuracy transcription model our model
definitely is the best choice for you
great so that's GPT 40 transcribe and GP
4 mini transcribe 40 is available in the
API today for just. 6 cents per minute
same price as whisper and 40 mini
transcribe is3 cents so half price
really really great state-of-the-art
options we're also enhancing our speech
to text apis with streaming so
developers can pass in a continuous
stream of audio into the model and get a
continuous stream of text and response
that makes it easier to build really
fast experiences and we're bundling into
these apis a bunch of hard problems that
developers need to solve to build voice
experiences so they come with noise

[00:06]
cancellation so the model isn't going to
get tripped up by background sounds they
also include a new semantic voice
activity detector which chunks the audio
up based on when the model thinks the
user is actually finished speaking so as
a developer you don't need to worry
about processing some half-spoken idea
um and all those capabilities are
available in the speech to text apis as
well as in our real-time API so very
excited for you to check that out next
capability is a new text to speech model
GPT 40 Mini TTS yav would love for you
to show us how this one works yeah let
me pull this up so um this is openfm um
it's a website uh we built just to make
it easy to play with this new model um
so as you can see there are a bunch of
voices that you can choose from um there
are different prompts that we
pregenerated but you can also type in
your own so this is basically a new
field that we added it's an instructions
field that tells the model how you want
it to speak the text um so yeah let's
Maybe try um try some um mad scientist

[00:07]
please exactly yeah as you can see like
we prompted basically like how we want
to deliver what kind of tone we want
high energy it's chaotic exactly all
right let's see what that's
like
and it may be busy all right busy yeah
let's try again one more
time the Stars tremble before my genius
the rift is open the energy surging
unstable perhaps dangerous most
certainly Captain Ryland this is really
intense okay so that's a lot I'm curious
if we took the same voice and tried to
yeah let's make
it how about let's say um the live
stream is going really well you're doing
great
yeah typing under pressure

[00:08]
let see how it
goes this live stream is going really
well you are doing great thank
you so that's super fun I love the Retro
look if developers want to play with
this and actually figure out how to code
against it what do they do yeah so you
can just click here and then we show you
basically some Snippets in Python
JavaScript or if you just prefer to curl
it directly and Ju Just to be clear the
tone the the personality is not tuned
into the model it's just prompted
exactly yes you can just prompt it um
and you can be as specific as you want
you can tell it exactly what kind of
pacing what kind of motion you want to
here um so it's very easy to to play
with you can just like you don't even
have to follow this form and just type
in anything free form that's awesome
very cool so that's gbt for Min TTS
available in the API today for just one
cent per minute very economical option
for generating really Lively audio we
thought the last thing to show would be
how this all comes together and to do
that we're really releasing an update to

[00:09]
our agents SDK our agents SDK launched
just last week as a way to really
encapsulate a lot of the best practices
that we've seen in terms of building
reliable text agents guard rails
function calls WR tools it handles all
that stuff for you and today we're
making it really easy to convert those
text agents that you've already built
into voice agents so yav I'd love for
you to show us the code changes involved
to make that conversion yeah um uh so
this here is the demo that we showed
last week so it's an AI stylist U it's a
customer support agent uh which you can
use to look up um some pagonia jacket
orders um so let's first see how it
works this is just like a text based
agent
okay so I'm just going to ask for some
recent ORD so you see it's see debug
information yeah yeah and then yeah it
just printed the last orders so it's
like the same thing that that we showed
last week okay now if I wanted to use
this on the phone what would I do
exactly so let me pull up the code so
here you can see um it's the same
configuration that we had last week it's

[00:10]
using the agents DEC um and we have
three agents here so we have three agent
um that receives the initial message and
decides what agent is going to process
it uh we have stylist agent which has
access to web search tool it helps you
pick a style and then we have customer
support agent which we just saw um and
it has access to past orders and it can
also submit refunds now let me open the
backend server code so it's a very
simple uh web socket uh backend um since
last week our team has made changes to
the UI so now U I can record audio and
it can play audio back and then that
audio is streamed to the back end uh
with this websocket connection um so
what I'm showing here is um is a
workflow so it's the same type of
workflow that our um agents SDK already
supports it's a text based workflow so
it takes in user text and then we pass
it to the run runner which feeds it to
the llm and then we get back the output
in the streaming fashion again as text
and then we send it to UI and then make
it available for Downstream processing
so this part is the same um and this is

[00:11]
the implementation of the the back end
so basically like when we get a message
from user We Run The workflow get back
text and then stream it to the UI so now
let me show you how to turn it into a
voice agent just with a few lines of
code um so first of all we need to also
handle audio messages from the
UI so I have some Snippets I prepare to
make it easier to demo so basically we
get a new chunk um of audio and then we
need to accumulate those audio chunks
first
um I need to make sure I don't
forget to initialize the buffer right
and so now let's see once we get the the
full audio what we need to do is we need
to send it to the agent so here um we
are getting the um the the audio we
concatenate all the chunks and then we
feed it into this voice pipeline so
voice pipeline is a New Concept we're
introducing um essentially what it can
do it can take your existing workflow
and it can add speech to text on one
side and text to speech on the other
side so essentially it will take audio

[00:12]
it will convert it to text feed it to
that workflow which I just showed
earlier it will get back text in a
streaming fashion if needed and it will
convert it back to speech um and you get
the output as a speech so here all those
events this is this is audio and then we
send it to the UI to to play um so I
just saved it yeah let's let's see Let
me refresh this um and let's see hey
what was my last
order so it's doing the tool call
your last order was on February 9th 2024
you ordered some Patagonia shorts in
Olive and it's all fulfilled if you need
help what was the order
number the order number for your
Patagonia shorts is
a507 if you need anything else feel free
to ask awesome so that was like nine
lines of code to build the voice agent
it's voice agent very cool and I guess
if I'm a developer I'm going to be
wondering if I build a voice agent how
do debug it how do I figure out if it's

[00:13]
working well what do we have there um
it's a very good question so um this is
a tracing UI that we demoed last week um
and we updated it to support audio now
um so let's see so this seems like um my
most recent chat I practiced a lot um
and
uh we can see that uh there are traces
here from our um most recent
conversation Let
me refresh this oh this is the most
recent chat um
yeah so so we can see that there are
traces here from our most recent
conversation um and as you can see there
are like all sorts of events so for
example we can click on this one this is
my first um request to the agent let's
play it hey what was my last order yeah
so it's integrated with audio you can
play it you can look up metadata you can
see different timelines latencies errors
and so on awesome that's PR cool so two
new speech to text models GPT 40
transcrip and gp4 on many transcribe

[00:14]
we're releasing the new text to speech
model and open ai. FM and then this
update to the agents SDK to make it
really easy to put it all together into
Rich reliable voice experiences that's
awesome we cannot wait to see what voice
agents you build with those new
technologies and we have more coming in
the coming month before we part one last
thing open.fm the demo that Yos showed
with the m scientist is actually live
open ey. FM um it's fun frankly we had
so much fun playing with it in the past
couple of days and so we thought why not
do a contest uh you know just like an
old school like radio station like a
radio contest if you will um and so you
have until tomorrow night so Friday
night to go on. FM and come up with like
the most creative like use of that text
to speech technology and share it with
open ey Twitter um and we'll pick three
winners and we have this amazing gift uh
for the winners which is a radio from
our friends at teenage engineering

[00:15]
special edition there are only three in
the world because there is op logo in
the back um anyway go to pfm share it on
Twitter and we'll send a tweet with like
more details on the terms of the context
um have fun and yeah see you thanks
thank you
[Music]

</details>
