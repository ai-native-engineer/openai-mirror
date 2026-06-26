<!-- source: https://developers.openai.com/learn/audio/ -->

## Search developer resources

# Audio & Voice

[![Realtime and audio guide](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Realtime and audio guide

Guide to choosing realtime and audio build paths.

guide](https://platform.openai.com/docs/guides/realtime)[![Realtime prompting guide](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Realtime prompting guide

Guide to prompting and tuning realtime voice models.

guide](https://platform.openai.com/docs/guides/realtime-models-prompting)[![Realtime transcription guide](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Realtime transcription guide

Guide for implementing streaming realtime speech transcription.

guide](https://platform.openai.com/docs/guides/realtime-transcription)[![Realtime translation guide](https://cdn.openai.com/devhub/resources/guide-4.png)

#### Realtime translation guide

Guide to performing realtime speech translation.

guide](https://platform.openai.com/docs/guides/realtime-translation)[![Transcribing User Audio with a Separate Realtime Request](https://cdn.openai.com/devhub/resources/cookbook-1.png)

#### Transcribing User Audio with a Separate Realtime Request

Cookbook to transcribe user audio using out-of-band Realtime sessions.

cookbook](/cookbook/examples/realtime_out_of_band_transcription)[![DevDay — realtime breakout](https://cdn.openai.com/devhub/resources/video-1.png)

#### DevDay — realtime breakout

DevDay session focused on realtime agent capabilities.

video](https://www.youtube.com/watch?v=mM8KhTxwPgs)[![New audio models intro](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:mM8KhTxwPgs -->
[![OpenAI DevDay 2024 | Multimodal apps with the Realtime API](https://img.youtube.com/vi/mM8KhTxwPgs/hqdefault.jpg)](https://www.youtube.com/watch?v=mM8KhTxwPgs)

<details>
<summary>자막: OpenAI DevDay 2024 | Multimodal apps with the Realtime API (29:45)</summary>

[00:00]
[Applause]
hi everyone and welcome to the realtime
API breakout session I'm Mark an
engineer on the API team working on the
realtime API and I'm Kata and I'm part
of the developer experience te a few
weeks ago we launched the public beta of
the real time
for the first time you can build apps
with natural low latency voice
interactions all with a single
API when we first launched our first API
in 2020 it was limited to text we then
made our apis multimodal supporting
audio transcription vision and text to
speech with the new real time API we've
taken the next step we've unified these
capabilities in a single API with a

[00:01]
model that natively understands
speech since we launched this a few
weeks ago we've seen developers building
some really impressive things in public
from avatars to Voice driven web
browsing even painting with your voice
we've also seen companies start using
real-time API to power voice experiences
in their own apps from language and
health coaching to voice controls in
your IDE and before we Shi the real time
a few weeks ago the only way to build
speech top speech experiences was to
stitch different models together and
build a complex solution around them so
it was really hard to create a smooth
natural conversation flow and unless
you're using the real-time API you
actually need to stitch different models
together and so you have to perform
multiple steps you need to connect these
systems and to go from input to final
output

[00:02]
there are different steps to take into
consideration so let me show you what I
mean first you actually have to capture
the user speech and so for this you
either need a button that they can press
to let you know that they're talking or
you need to detect that they're done
speaking yourself and after that you get
audio and you need to process that audio
with a transcription service like the
transcription API that uses our whisper
model then you get text out
and you need to process that text with a
language model like gbd4 for example to
generate a
response and then the last step is to
generate voice and so for this you need
a third model for example our text to
speech model to have speech as the final
output so if you've been following each
step in this flow depends on the output
of the previous one which makes the
overall process slow first of all but

[00:03]
also it can't react fast enough to allow
for natural
Interruption and along the way the
capture speech actually loses detail and
Nuance it's like you're telling the
model what something sounds like instead
of it actually hearing it for itself so
this makes it really hard to build fluid
conversational experiences that feel
natural so before the realtime API some
of GPD 4's capab abilities weren't
available in the API yet the most
exciting one is its ability to natively
understand and generate speech what this
means is that there's no need to convert
other modalities into text for the model
to understand it can actually process
audio inputs just as well as texts and
it can also generate speech directly
without having to generate the text
first right since in the interaction
doesn't need to be split into multi mple

[00:04]
steps it can happen in real time with
much less
latency in fact this is the same
underlying model capability that powers
advanced voice mode in chat gbt so let's
take a
look what are some fun things I can do
outside this weekend the weather looks
great that sounds like a perfect
opportunity to explore the Bay Area you
could take a hike in the Mirror Woods
enjoy a picnic at Chrissy field with a
view of the Golden Gate Bridge or take a
scenic drive down Highway 1 to explore
the coastline how does that sound for a
start that sounds awesome I really like
the idea of a Scenic Drive what route
should I
take for a Scenic Drive taking Highway 1
is a fantastic
choice yes chachi's advanced voice mode
is an amazing experience I hope you all
got a chance to try it it's now
available in all of Europe and now
what's even more exciting is that with

[00:05]
the realtime API you now have access to
the same capabilities but 3D API which
means you can actually build and use
this to have the same kind of
experiences but in your own
applications so as you heard a few weeks
ago we launched the realtime API into
beta and the realtime API is designed to
enable exactly these kinds of low
latency multimodal experiences in your
own applications
the Beta release is an important first
step towards supporting the full
spectrum of modalities in a single
surface so right now we support speech
text and function calling and we're
working to add more capabilities to this
API in the
future so just to walk through what
we'll be discussing in the rest of this
session first we're going to show you a
demo of what it was like to build this
these kinds of voice experiences before
the real-time API and after the real
time API then we'll get into some live

[00:06]
coding to show you how you can start
building with it
today and finally we'll show you a demo
of how you might integrate the real-time
API into your
apps so let's see how voice assistant
apps were made before the real-time API
on kya's laptop we've got a small
example here which was implemented by
combining a few different systems so
like we said you'll need speech
transcription a language model and
you'll need to generate speech so we can
use open AIS whisper dpt4 and text to
speech apis for these okay so I have
here on my laptop a voice assistant
buils the old way so as Mark said there
are three different steps and I'm going
to ask something and then we'll see the
different steps while they are happening
on the screen ready
okay okay quick how do I unsend an

[00:07]
email okay so it's generating a text
response now he generating dis
speech this is becoming
awkward if you need to unsend an email
the process can vary depending on the
email service you use to send it okay
thank you here are some common so I'm
going to stop it there because it's way
too late but you get the gist this works
but it was we're missing out on some
important stuff it responded too slowly
to be helpful so I uh hope that email
wasn't too spicy
Kaa so let's look at something similar
implemented with real-time API this time
okay so I have here an upgraded version
of this voice assistant and so now we
don't have separate steps it's all
happening at the same time time so let's

[00:08]
try it and see the
difference hey can you hear me loud and
clear what can I help you with today
okay so I'm here on St at Dev day with a
crowd of amazing Builders and I just
want you to say hello and tell them how
excited we
are hello devday Builders it's awesome
to connect with you all I'm thrilled to
be part of this event and can't wait to
see the incredible Innovations you all
created
let's make some magic happen today you
heard her um but I actually came from
Paris I took the Eurostar and I'm
already feeling a little homesick so
would you mind saying hello but in
French this time
not

[00:09]
excep great thank you and just for
comparison how do I unsend an email to
unsend an email it depends on the email
sour okay I'm actually using
Gmail in Gmail you can unsend an email
by using the undo send feature great
thank
you okay
[Applause]
wow so huge Improvement we're going
directly from speech in to speech out
using JD for's native speech
capabilities and what that means is that
we didn't have to wait and it's really
cool to hear how expressive the voice is
relative to plain
TTS in fact since we launched realtime
API a few weeks ago we've been working
on making the voices even more Dynamic
So today we're releasing five new
upgraded voices for you to use in your
apps as a quick comparison here's what

[00:10]
it sounded like when we launched
compared to a few of the voices that are
now available today the human voice is
the most beautiful instrument of all but
the most difficult to play said Richard
Strauss but according to Maya Angelou
it's not what you say it's how you say
it words have incredible power they can
make people's hearts sore or they can
make people's hearts sore Marty grth
once said and when King George V 6 spoke
to his country in real time he said I
send to every household of my peoples
both at home and overseas this message
spoken with the same depth of feeling
for each one of you as if I were able to
cross your threshold and speak to you
myself all right of course since the
model natively understands speech you
can tune the emotion and tone of these
voices to your needs using system
messages great should we dive into how

[00:11]
this works let's do it so the realtime
API exposes a new endpoint called V1
slre time and your apps make maintain a
websocket connection and exchange Json
formatted messages with the server these
messages can contain text audio and
function calls the websocket
transport allows us to keep a stateful
connection open which is the key to
liveness here so user input including
audio can be streamed to the realtime
API in real time and output from the
model will be streamed back as soon as
it's produced so now we'll walk through
some demos to better explain how this
works yeah let's actually build
something I think that's enough
introduction uh maybe we can start with
a simple example like the one we' just
seen Mark why don't you walk us through
how you would actually build this sounds
good

[00:12]
all
right
okay so we'll we'll start small and to
more easily introduce the concept here
we're going to build a front-end web
application that uses the browser
websockets API to connect directly to
realtime API so we have here a basic
HTML file and I'm going to include some
utils here that help us deal with the
audio AP in the browser and other than
that we just have a button right now and
we sort of set up some of our our
helpers here so if we go over to the web
page and we click Start you know of
course it doesn't do anything yet
because we haven't written any code so
let's do that
now so the first thing I'll do is I will
open up a connection to the realtime API
so I'm creating a new websocket and I
have the API URL here and I passed the

[00:13]
model along as well and you'll notice
that I'm passing my API key using this
custom header so uh this is isn't really
suitable for production app but it's
great for starting to locally experiment
with the API directly in the browser so
just keep that in mind as you start
building so now that we've created our
websocket connection we will now start
handling messages from uh the real time
API so what I've done is I've defined an
on message Handler and the messages that
we get back from the API are in Json so
we'll go ahead and parse the message as
Json and the messages have each have
their own type so in this case what we
care about is the response. audio. Delta
message so this message will be sent
back from the server whenever the mod
model uh is responding with audio so

[00:14]
we'll switch on the message type and
when we get the response. audio. Delta
message we'll go ahead and base 64
decode the audio and then we'll pipe
this audio into our wave stream player
utility class which will play the audio
out on the speakers and you'll notice
here that the audio we get back is pcm1
16 so this is 24 khz wave uh the API
also supports g711 so if you're
interested in how to use different
codecs encourage you to look at the docs
and check out how that
works so this takes care of
handling audio that comes back from the
model now let's deal with taking our own
speech and sending that off to the
realtime
API so what I've done is I've added an
onopen Handler for the websocket
connection and what we'll do is first
we'll start recording
uh using the microphone and our utility

[00:15]
class here is going to let us register a
call back so that whenever any speech
comes through the microphone we'll take
that speech and we'll package it up in a
message to the realtime API called input
audiob buffer. append we'll basic D4
encode it and we'll send it
off so since we've handled both the
model output coming back to us and our
own speech going out to the model this
should be enough to to start having a
conversation so we'll switch back over
and see how it
goes can you hear me yes I can hear you
perfectly fine how can I assist you
today well I'm just demoing you off to
an audience so can you say hello hello
there it's a pleasure to meet all of you
if there's anything you'd like to ask or
know I'm here to
help all right great so we have working
speech to speech application in just a
few lines of code but let's show off uh

[00:16]
a few more features of of the API so one
of the things that by default uh the
real-time API when you open up a new
session will automatically respond to us
when we finish talking but we haven't
yet handled interruptions quite yet
quite correctly so when the response
comes back from realtime API it actually
comes back faster than real time so the
API will just give us back the model
response as as fast as it can be
generated and we'll take that response
and we'll buffer it and play it locally
so if we want interruptions to feel
natural then what we need to do is when
the user starts speaking we need to stop
the out model output from playing on the
speakers so real time API will give us
sends us an event called uh that will
help us detect when speech has started
and we can use that to sort of do our

[00:17]
logic so let's do that
now so we're now handling a different
message type this message type is called
input audiobuffer dos speech started so
this is going to be sent to us whenever
uh the server detects that the user has
started speaking and when the user
starts speaking what we'll do is we'll
interrupt any of the model output audio
that we're currently playing and our
helper here is going to give us back
this off
so this offset is the duration of audio
that we've already played and what we'll
do with that is we'll send that back to
the
API and we do this so that we can let
the model know exactly where we
interrupted right because it's sending
us audio fased in real time we want to
let it know what was actually played at
the time when we started
speaking so we just need a little bit
more metadata uh to get this all wired
up and I'm going to add that now
so we just need this current item ID and

[00:18]
this context content index and that
should be all that we need to get
interruptions working the way that we
want so let's try that
out can you hear me yes I can hear you
how can I assist you today can you tell
me five interesting places to visit in
London absolutely London is full of
fascinating spots here are five
interesting places to check out the
British museum home to a vast collection
of art oh that sounds really interesting
where is that the British museum is
located in the bloomsberry area of
London on great Russell Street it's
easily accessible by public transport
with the Tottenham Court Road and hurn
Tube stations
nearby all right so you'll notice that I
was able to interrupt the model and ask
it where that was and it knew based on
where which how much audio was played

[00:19]
out uh what I was talking about so it
knew that I was asking about the British
museum so uh yes in this brief demo we
created a voice assistant from scratch
and we introduced the basics of handling
speech in interruptions in just a single
file and we did this using vanilla front
and JavaScript just to show the API in
its simplest form but of course we don't
build production apps this way so so
let's see how this new API uh will fit
into a real life use case Kaa will you
walk us through that yeah sure so I
actually have an example for this so I
want to build this tutoring app for
students to learn about space because I
think it's a fascinating field um so I
want users to be able to ask about
anything on space but I want to make it
fun you know like we could do a simple
chat interface but where's the fun in

[00:20]
that it's 2024 I think we could do
something a bit more immersive
so I went ahead and prepared this
application
here so it's going to show up on the
screen in a
minute and it's a 3D view of the solar
system so this is just the front end and
then on the back end I set up the real
time API like Mark just explained but
this time it's part of real application
so let's try it and see if it
works hey so can you tell me what is the
biggest planet in the solar
system absolutely the biggest planet in
our solar system is Jupiter it's so
massive it has more than twice the mass
of all the other planets combined
Jupiter is the giant among
giants okay great so the real- time
interaction works and I think it's
already a more fun way of learning but

[00:21]
let's see if we can make it a bit more
interactive hey I'm curious about
Earth sure thing Earth is the third
planet from the Sun and the only one
known to support life it's packed with
diverse ecosystems abundant water and a
protective atmosphere that Shields us
from harmful solar radiation do you want
to know more about Earth's
characteristics well I see that there's
actually a lot of water there so can you
tell me how much land is there versus
water absolutely approximately 71% of
Earth surface is covered by water while
the remaining 29% is land our Blue
Marble truly lives up to its name let me
show you this on a pie chart here's the
breakdown of Earth's surface okay great
thank you I actually have a question
about Mars
now Mars the red planet what would you
like to know
so I heard there was a lot of volcanoes

[00:22]
there can you tell me which one is the
biggest absolutely the biggest volcano
on Mars and in the entire solar system
is Olympus moans it's about 13.6 miles
nearly three times the height of Mount
Everest would you like more information
on Olympus Mons yeah can you tell me
like uh what are the three uh biggest
volcanoes and show me their
heights certainly the three three
biggest volcanoes on Mars are one
Olympus Ms 13.6 mil 22 km High two ascus
mes about 11.3 M 18.1 km High three
arams around 11.2 mil 18 km High okay
great thank you I just learned
something great so let's talk about what
happened here not only could I ask

[00:23]
questions and get answers in real time
but we also saw some interactions
happening on the screen so whenever I
asked about a specific planet we flew in
to see it up close and when I asked
questions that could be answered with
data we saw some charts pop up on the
screen so how is that possible well as
Mark mentioned the realtime API supports
tool calls so I actually went ahead and
defined some tools that the model can
use use so I have this Focus Planet tool
that is called whenever we talk about a
specific Planet it just takes the planet
name as a parameter and I also have this
display data tool here and the idea is
that when something can be answered with
data the model will choose with which
chart is the most appropriate what
should be the title and what are the
data points that should be displayed so
that's already a pretty cool use of tool
calls you can trigger interactions in
your app you can make interactive apps
so that's really cool but sometimes you

[00:24]
might also need to send data back to the
model so that it can say it out loud so
let's see how we can do that so I have
this API call here that calls this
endpoint that gets the current position
of the International Space Station in
real time so it gets back the latitude
and the longitude and I have this
function fetch Isis position that just
fetches to that end point get the
response back um and I also Define here
this tool show ISS and whenever this
tool is triggered by the model we will
call that fetch ISS position function
and then send the position back to the
model so let's try it and see it in
action hey can you go back to
Earth sure thing we're back to our home
planet Earth what would you like to
explore can you tell me where is the ISS
right
now the International Space Station ISS
is currently located over the southern

[00:25]
hemisphere around - 35.6 de latitude -
32.6 1° longitude it's always orbiting
around our beautiful planet what else
can I help you with great actually how
do you know the current
position I have access to realtime data
which allows me to track the current
position of the ISS in its orbit around
Earth this information is up dated
frequently to give an accurate location
of the station as it orbits our planet
approximately every 90 minutes great
it's pretty cool isn't it what else can
I assist you with yes it is pretty cool
um great so now you know how you can
actually feed data to the model in real
time so that it can use it in
conversations with your
users okay last
question hey can you show me Pluto

[00:26]
great I heard it's not even a
planet that's right Pluto was
reclassified as a dwarf planet in 2006
by the international astronomical Union
the reason it didn't meet all the
criteria for full Planet status mainly
because it hasn't cleared its orbit of
other debris nonetheless Pluto remains a
fascinating object with its own unique
character istics what else would you
like to learn and I heard it has moons
what are those
moons great thank
you okay so if we look at what the model
is doing right here it's calling this
show moons tool with Pluto's moons as an
argument and here it's a very small
array but if you have a big array as a
parameter or if you have a long list of
par parameters you can actually stream

[00:27]
that in real time while it's being
generated to show it or to uh let your
user know about it before the tool call
exended so that's like a very convenient
way to use this information in real time
okay so great with the real time API
we've actually built an immersive app
that you can interact with through voice
and that also reacts visually to what
you're asking
thanks to twool use so I hope this is
right
yeah so I hope this isar some ideas I'm
really excited to see what you come up
with and how you'll push the boundaries
to create new delightful experiences for
your
users so now that you've seen a couple
demos of realtime API I hope you can see
how it opens up new possibilities for
low latency speech to speech apps it's

[00:28]
this is a new way to leverage the native
multimodal capabilities of GPT 40 and
support for function calling makes it
possible to deeply integrate into your
apps and as you heard in the keynote as
of today we're also reducing the cost of
using the realtime API we're able to
offer this because we implemented prompt
caching for text and audio inputs what
this means is that for any text input
that hits the cache this input will cost
50% less just like with prompt caching
for text only input in chat
completions any audio input that hits
the cache will cost 80% less so for a
typical 15minute conversation we expect
that it will cost 30% less now than it
did at launch date so we know how much
cost matters whether you're building bu
something new or scaling it out and we

[00:29]
couldn't be more excited to offer this
and if you haven't seen it please check
out our docs and additional resources
that we published to get started
building we really excited about the
potential of realtime interactions we
see this as just the beginning of a new
generation of products that are built to
be natively multimodal and speech to
speech is just a first step but in the
future we're looking forward to
unlocking the native capabilities of our
Frontier models in this very API and we
can't wait to see what you build with it
thank you

</details>


#### New audio models intro

Overview video of new audio models for speech and transcription.

video](https://www.youtube.com/watch?v=lXb0L16ISAc)[![openai.fm](https://cdn.openai.com/devhub/resources/code-1.png)

<!-- yt-inline:lXb0L16ISAc -->
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


#### openai.fm

Code samples for speech processing from the openai.fm repo.

code](https://github.com/openai/openai-fm)[![Realtime & Twilio starter app](https://cdn.openai.com/devhub/resources/code-2.png)

#### Realtime & Twilio starter app

Starter app integrating realtime agents with Twilio.

code](https://github.com/openai/openai-realtime-twilio-demo)[![Realtime agent demo](https://cdn.openai.com/devhub/resources/video-3.png)

#### Realtime agent demo

Video introduction to the TypeScript Agents SDK.

video](https://vimeo.com/1105243382)[![Realtime console](https://cdn.openai.com/devhub/resources/code-3.png)

#### Realtime console

Console application demonstrating realtime API usage.

code](https://github.com/openai/openai-realtime-console)[![Realtime intro](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Realtime intro

Introduction to building realtime voice applications.

guide](https://platform.openai.com/docs/guides/realtime-conversations)[![Realtime solar system](https://cdn.openai.com/devhub/resources/code-4.png)

#### Realtime solar system

Demo of realtime agent interactions in a solar system example.

code](https://github.com/openai/openai-realtime-solar-system)[![Realtime tool delegation guide](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Realtime tool delegation guide

Guide on delegating tasks through tools in realtime agents.

guide](https://openai.github.io/openai-agents-js/guides/voice-agents/build/#delegation-through-tools)[![Speech-to-text guide](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Speech-to-text guide

Guide for building speech recognition pipelines.

guide](https://platform.openai.com/docs/guides/speech-to-text)[![Speech-to-text intro](https://cdn.openai.com/devhub/resources/guide-4.png)

#### Speech-to-text intro

Introduction to speech recognition with OpenAI.

guide](https://platform.openai.com/docs/guides/speech-to-text)[![Voice agents guide](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Voice agents guide

Guide to building voice agents using speech-to-speech API.

guide](https://platform.openai.com/docs/guides/voice-agents)[![Voice applications intro](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Voice applications intro

Introduction to building voice-enabled applications with OpenAI.

guide](https://platform.openai.com/docs/guides/voice-agents?voice-agent-architecture=speech-to-speech#speech-to-speech-realtime-architecture)[![Audio & speech guide](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Audio & speech guide

Overview of approaches for audio processing and speech in applications.

guide](https://platform.openai.com/docs/guides/audio)[![Realtime agents starter app](https://cdn.openai.com/devhub/resources/code-1.png)

#### Realtime agents starter app

Starter app demonstrating realtime agent capabilities.

code](https://github.com/openai/openai-realtime-agents)[![Comparing Speech-to-Text Methods with the OpenAI API](https://cdn.openai.com/devhub/resources/cookbook-2.png)

#### Comparing Speech-to-Text Methods with the OpenAI API

Cookbook to compare speech-to-text methods and choose the right approach.

cookbook](/cookbook/examples/speech_transcription_methods)[![Multi-Language One-Way Translation with the Realtime API](https://cdn.openai.com/devhub/resources/cookbook-3.png)

#### Multi-Language One-Way Translation with the Realtime API

Cookbook to build one-way speech translation with the Realtime API.

cookbook](/cookbook/examples/voice_solutions/one_way_translation_using_realtime_api)
