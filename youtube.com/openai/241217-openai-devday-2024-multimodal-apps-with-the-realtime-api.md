---
title: "OpenAI DevDay 2024 | Multimodal apps with the Realtime API"
channel: openai
url: https://www.youtube.com/watch?v=mM8KhTxwPgs
youtube_id: mM8KhTxwPgs
published: 2024-12-17
duration: "29:45"
captions: en-orig
---

# OpenAI DevDay 2024 | Multimodal apps with the Realtime API

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
