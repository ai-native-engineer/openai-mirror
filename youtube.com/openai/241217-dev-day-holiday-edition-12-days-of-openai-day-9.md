---
title: "Dev Day Holiday Edition—12 Days of OpenAI: Day 9"
channel: openai
url: https://www.youtube.com/watch?v=14leJ1fg4Pw
youtube_id: 14leJ1fg4Pw
published: 2024-12-17
duration: "22:14"
captions: en-orig
---

# Dev Day Holiday Edition—12 Days of OpenAI: Day 9

[![Dev Day Holiday Edition—12 Days of OpenAI: Day 9](https://img.youtube.com/vi/14leJ1fg4Pw/hqdefault.jpg)](https://www.youtube.com/watch?v=14leJ1fg4Pw)

<details>
<summary>자막: Dev Day Holiday Edition—12 Days of OpenAI: Day 9 (22:14)</summary>

[00:00]
day nine day nine of 12 Days welcome
everyone I'm Olivia gar I lead the
platform product at open AI today I
think is the best day like I'm very
biased today is all about developers and
startups building on top of the open AI
API zooming out we've had an API for
what four years the scale is Incredible
2 million developers building from more
than 200 countries pretty cool and so as
a thank you gift we have several new
models and features to announce today to
thank you for being a part of the
community so kind of a small dep day I
don't know North Pole senta Edition so
Michelle take it away thanks I'm
Michelle poas and I work on our post
training research team hi I'm Brian John
I'm also on the post training team at
openi awesome well like Olivia said we
just cannot stop doing Dev days so
here's another small one um today I'm
super excited to tell you that we're
launching 01 out of preview in the API
since we announced open AI 01 preview in
September developers have been building

[00:01]
super cool stuff on the API you know
agentic applications and customer
support or financial analysis and also
it's just a phenomenal coding model so
we've been really excited to see that
we've also heard feedback from
developers that you're missing kind of
the core features that you've come to
expect on our API and today we're
launching them in O in the API so we're
launching function calling structured
outputs and developer messages and uh
developer messages are a little new
they're a new spin on system messages
and they're actually part of our
instruction hierarchy work uh to teach
the models which kind of instructions to
follow in what order so the developer
message is controlled entirely by the
developer and used to steer the model
finally uh we're also launching
reasoning effort this is a new parameter
that tells the model how much to spend
time thinking it's really helpful to
save a little time and money on you know
easier problems and then you can spend
more compute on the hardest problems
where you need it I said finally but
that's not true we're also launching
Vision inputs in the awesome people have

[00:02]
just been really asking for this and we
think it'll help a lot in cases like
manufacturing or science um so super
excited to see what you build there but
actually let's see a quick demo all
right yeah let's walk through a live
demo to see some of the 's new
capabilities in the Epi uh starting with
vision so for that I've
prepared the photo scans of a text form
that I filled out with some fake data
the other day but I had some mistakes in
there and I wonder if 01 can help us
detect errors in the form but just a
quick note before we get started while
can help us detect errors in forms like
a text form it is not a substitute for
professional Judgment of course of
course all right I will open up our
developer playground which is a really
nice UI for experimenting with open AI
models in the API at the top this is our
newly introduced developer message this
is where you can provide the model with
some highle instructions or sometimes
detailed instructions on how it should
behave as a model I have a pretty simple

[00:03]
one here and then I uploaded the images
from my form and ask the model to spot
for
errors while O's thinking let's jump
back to my form to take a look at the
errors that I
had so the first one that I had the
first error I had is on line 11 for
calculating adjusted gross income AGI I
was supposed to subtract line line 10
from line n but I did the opposite I
used addition we've all been there well
happens I got a little too excited every
time I see the word
egi the second error is I use the wrong
standard deduction looking at the chart
on page four standard deduction depend
on both the filing status and also the
number of checked boxes on page one so
this means for the for o1 to figure out
the correct value for standard deduction
you need to reference content for two
other
images let see let's see what the model
get back to

[00:04]
us all right let's see the
model great it notice the arithmetic
error on line 11 um I I was supposed to
use subtraction that's good um and it
also notice the standard deduction
amount is incorrect which is also
right and based on that of course I need
to adjust my tax B income and subsequent
tax all right after fixing the those two
errors in my form I know my taxable
income now arrives at
9,325 next up I will ask in the model
based
on information from the form how
much income tax do I owe if my taxle
income is
this so what do you think the model will

[00:05]
do here really hoping it gives us a good
answer well ow doesn't have access to
the latest upto-date 2024 tax table so
but it does have access to a set of
functions we provided on the
right functions are a way for the model
to interact with your backend apis so
here we can take a look at one of those
functions so we provided it's it's
rendered in ajon schema and we provide
with a high level description for what
the function does and the set of
arguments
the model needs to provide to call the
function so this is offer function
calling feature makes sense so the model
calls this function we can call this on
the back end get the correct tax data
send it back exactly looks like the
model called the correct function here
uh with the input from a pulled from the
image does does the user see any of this
uh not really so this all happens in the
back end of your app the user will not
see any of the function calls nor the
response from your API so after we get

[00:06]
the response we will send that back to
the model and 01 will respond to the
user in a very nice looking user message
so here it tells the user about their
new updated income tax after the cor
awesome better but that's not all I
wanted to show you one last thing that's
structured outputs I will ask the model
here what what Corrections do I need in
my forms
but before I hit enter I want to provide
Model A Json schema for the response
format this will instruct the model to
Output according to this gson schema and
on top of that we also implemented
Solutions on the API backend to ensure
the model output adhere to this gson
schema 100% of the time makes sense
actually let's take a quick look at this
schema so uh it's called form correction
and it's got a list of Corrections and

[00:07]
each correction has what you'd expect so
there's the reason so we can display to
the user what they got wrong and then
it's got the location um so this is
super cool we can actually like render a
UI for the PDF and highlight exactly
what's wrong with the new value and the
old value um so structured outputs is
super useful when you don't want to kind
of render markdown from the model and
you want to just extract the Json
automatically so you can see here the
model has output uh the corrections you
can see there in the the nice Json
format we've got the new value the old
value all locations and reasons um and
so yeah this is super helpful when
you're building kind of uh Rich
featureful applications so we just
showed you a quick demo but uh you know
demos are really not enough to give you
the full story we actually run internal
evaluations which are like tests to see
how our features do before we ship them
um and so for 01 uh because it's really
important for developers we ran some
evals for API use case so I'm going to
show you a few these let's take a look

[00:08]
um first we have function calling um so
we have some internal function calling
Evas and you can see that uh this new o1
model is significantly better than gbt
40 at function calling and this actually
includes both halves of function calling
you know calling the right function when
you should and not calling a function
when you shouldn't um you can also use
function calling in conjunction with
structured outputs and you can see that
again o1 performs much better than 40
here speaking of structured outputs o1
also significantly better on this eval
this means the model does a better job
of following the format um so we take it
less off distribution when we constrain
it next is coding everyone's always
talking about coding um live bench is an
open source coding eval and we're
excited to see that 01 performs you know
much better than o1 preview and 40 on
this eval that's awesome that's huge
jump yeah and then finally we have Amy
um and on this eval you can see that o1

[00:09]
again significantly outperforms o1
preview but actually the interesting bit
here is that we have on the right o1
with structured outputs so when building
structured outputs we really wanted to
make sure the model performs just as
well when using structured outputs as
without so you can see that the
reasoning capabilities are maintained
even with this feature so you can use it
in your application and not have to
worry about the results awesome so those
are the E valves but beyond the EV vales
uh there's actually a really interesting
change in latency so 01 actually uses
60% fewer thinking tokens than 01
preview which means it's much faster and
cheaper for your
application finally we've heard a ton of
demand from you for 01 Pro in the API
and I'm sorry to say we don't have it
now but our elves are hard at work back
at the lab and it should be coming soon
we're walking very H night
yeah cool awesome thank you so much Bron
Michelle um to recap o1 in the API
function coding structured output uh
developer messages image understanding

[00:10]
will start running out to tier five
customers starting today we will receive
an email and will take us a few weeks to
get to everyone so o1 is not the only
model that we shipped uh recently uh
we've had a lot of excitement on the
realtime API how do you have like
natural human level latency speech
application so Sean give us an update
hey I'm Sean and I'm here with I'm
Andrew um and I'm here to talk about the
realtime API so if you've never used the
realtime API before it lets you build
real-time voice experiences with open AI
so think you can build your own chat GPT
advanced voice mode you can add AI
assistant you can do all these really
cool things with AI um and today we have
websocket support so you can do server
to server and send voice and get
responses back but today uh what we're
announcing is web RTC support and that's
really exciting for three reasons the
first is that web RTC was built for the
internet so if you've done conferencing
if you've done low latency video
streaming that all uses web RTC and that
handles you know the constant changing

[00:11]
of the internet it it'll change your
your bit rate it will do Echo
cancellation and so what's exciting is
now realtime API gets all of these
benefits so if I build an application
things are way easier and it just works
so to leave that in I'll show you a
little demo application to show you how
easy it is to
do so here's a little HTML and just to
give you a structure of it we have a
audio
element we have a peer connection and
what the peer connection is it's kind of
the onetoone connection between you and
the realtime API and so what we're doing
today is we're creating this peer
connection we're saying when the
realtime API sends you some audio put it
into that audio
element next we capture the microphone
and we're adding it to the peer
connection so we're saying we're going
to send one audio stream to open Ai and
then now that we've set up this pier
connection we do an offer answer and
what the offer answer does is it
collects up all the information locally
you send it via an HTTP post post and we
respond and web RTC then goes and does

[00:12]
everything for you there's no handling
of um congestion control or capturing
the audio or any of those other things
you had to deal with before that's
awesome so how does that compare to the
previous web soet integration so if you
were doing websockets before this code
would probably be between like 200 and
250 lines of code and um you would have
additional problems on top of that like
you'd have to handle back pressure and
all these things like it's it's one of
those problems that you don't realize
how frustrating it is like until you
finally go production I see so let's
actually run the code and see what it
looks like so here's the code um my
audio element and I'll refresh the
page how many days until Christmas
Christmas is on December 25th and today
is December 17th that means there are 8
days left until
Christmas nice always exciting when a
demo works okay so yeah so that that's
all it took is that so you just copy
pasted the 12 lines you execute the
script and that's it yep and like we'll

[00:13]
we'll open we'll put this code out and
so you can just go and grab that um the
only thing that you'd have to change is
your API token and so you can go and
download this code and run it um I'm
really excited to see what people build
like as we make it way easier okay so
the next thing I want to talk about I'm
going to have to bring out a little
friend so I wasn't able to get an Elf on
the Shelf this year so I got a fawn on
the lawn a new official toy so Fawn on
the
has a microcontroller in it and to give
you a sense of here it is and before I
plug it in here's how big this
microcontroller is um absolute tiny like
the size of a penny so I've got the
microcontroller in there and I'm going
to plug in and we'll see what
happens Merry Christmas what are you
talking about we're talking about adding
web RTC to the realtime

[00:14]
API oh that sounds a bit too complicated
for me how about we talk about something
more fun like delivering presents
there's nothing quite like soaring
through the sky to bring joy to everyone
on Christmas Eve okay what am I getting
for
Christmas oh I'm not supposed to spoil
the surprise but I think you might be
getting something very familiar this
year could it be some cold
oh okay um cool so we saw using the
realtime API in the reindeer so um but
that's just like a a tip of the iceberg
with all the use cases that you can
build so with something this size you
could put it on you know a wearable
device like glasses you could put it
into um cameras and and microphones
around the house you can have like
context aware assistance um like I am so
excited for what people build because
with this SDK all you have to do is set

[00:15]
your token and set some details about
your Wi-Fi in it connects like these are
microcontrollers that you can get off
from like any major real tailer you plug
it in USB and that's all like I I really
think that 30 you know 30 45 minutes
people can start doing the like building
this upu there's no soldering there's no
Hardware um we just have a speaker
plugged into a headphone jack that's
super cool super cool and we have other
updates to the realtime API number one
we heard your feedback on the cost we're
dropping the cost
so from now on GPT 40 audio tokens will
be 60% cheaper than before and we are
also shipping support for 4 mini in the
API and 4 mini audio tokens will be 10x
cheaper than the current price the
second thing is that we're shipping
support for a python SDK for the time
API to make it even easier to integrate
and lastly we're making some API changes
to make it easier for you to use
function coding and guard rails so all
of that we hope uh and we cannot wait to
see the kind of applications that you're

[00:16]
going to build all right we talked about
models we talked about API would love to
talk about fine tuning customization
that's one of the big like needs from
developers like they want to customize
the models for their own use cases what
do you have Andrew yeah so unfortunately
I don't have a reindeer to share that's
fine but we are excited to announce a
new method of fine tuning available in
our API called preference fine tuning
and we'll be using a method called
direct preference optimization which is
designed to help you create models that
better align with user preferences which
should hopefully uh give increased
performance where user feedback plays a
critical role so you guys have been
shipping a ton you're on fire like for
the past few months but we've had an API
for year F API what's new what's the
difference yeah so currently in our API
we have supervised fine tuning and the
newly announced reinforcement fine
tuning most of our users have been using
supervised fine tuning to tailor our
models for their use cases and in
supervised fine tuning you provide the
exact input and output you want the
model to have so if you're creating a
user chatbot you'd give it the user
messages and then the exact response um
and preference fine tuning it's a little
bit different so instead of the exact

[00:17]
input and output you're going to be
giving it a pair of responses where one
is preferred over the other and then our
funing process will optimize it to learn
the differences in those responses and
those differences could be things like
response formatting stylistic guidelines
or even like abstract qualities uh like
helpfulness or creativity I see I see so
typical use cases would be what customer
support copy writing creative writing
yeah exactly so if you see our models
maybe are a little bit too verose or
they're giving irrelevant answers um
this fine tuning can help guide it
toward more concise and relevant
responses by emphasizing the preferred
behavior and then deemphasizing the
unpreferred ones another really good uh
use case might be content moderation so
for example if you have a specific style
or tone you want your organization to
have uh preference fine tuning can help
guide it toward that um but yeah let me
show you actually how easy it is to
start fine tuning in our API um so here
I am on the platform UI and I'm in the
fine tuning tab so when I hit create
fine-tune now you can see that there's a
new drop down for method and I'm just
going to select direct preference

[00:18]
optimization next I'll select the base
model uh in this case I'll select GPT 40
and then finally all I have to do is
upload the training data and like I
mentioned before the format's a little
bit different so I'll go through a quick
example um in this example um we're
asking an assistant what the weather is
like in New York City and providing it
two pairs of responses like I mentioned
and maybe we're making a chat bot so we
want to be a bit more conversational so
in the preferred response it's a bit
more verbose and then also responds in
Fahrenheit and the unpreferred response
it's much more concise and responds in
Celsius so I'm going to take these
examples put them in a Json L file um
where each example is going to contain
the input messages the preferred output
and then also the non-preferred output
um so I'll go ahead and upload the data
now and we also provide some hyper
parameters to tune but I will just
select the defaults for now and hit
create and so this is going to kick off
the fine-tuning process um depending on
the data set size this could take

[00:19]
anywhere from several minutes to several
hours but once it's done we should be
able to sample from the model the same
way we would any base model in our API
man it's so exciting so have you had a
chance for people to use it yet yeah so
we've given Early Access to preference
find tuning to sever of our trusted
Partners um and we've seen good results
so far so as an example uh rogo AI is
building an AI assistant for financial
analysts and they're using our models to
rewrite and refactor user queries um to
to give more relevant answers when they
use used supervised fine tuning they
couldn't quite get it to perform better
than the base model but with preference
fine tuning they saw accuracy increase
on their internal Benchmark from 75% at
the base model to over 80% with
preference fine tuning so we're super
excited to see what other developers can
do with preference fine tuning um which
is why we're actually going to make this
available for GPT 40 today and GPT 40
mini soon um at the same price per train
token as supervised fine tuning so if
you out there are excited to start
preference F tuning I encourage you to
check out our documentation later today
that's awesome that's awesome okay there

[00:20]
is a lot to unwrap lots of gifts we
started with o1 o1 in the API with the
full production feature set such as
function coding that people expect
starting rolling out to tier five
starting today um then we talked about
the realtime API new API simpler web RTC
integration and price TP and now we're
talking preference F tuning to make it
easier to customize models for your use
cases and that's not all the team is
non-stop shipping they shipped a few new
things today and so I wanted to show you
a few uh smaller things which are coming
up um number one is we canot talk about
the developer experience and product
quality and so we're going to ship to
announce uh starting today new sdks uh
we have official support for go and uh
Java sdks you can find them here uh
please give us feedback similar to the
python SDK and um the node SDK um they
support all the API end points that you
need on open AI so here's the go one and
here is the Java one um number two We

[00:21]
Care a ton about Simplicity I'm not
going to go through the whole flow but
we have a new login sign up and flow to
get an API key so there is no need to
whatever like you know sign five terms
of services you get an API key like in
just a few
seconds next we did a bunch of De days
around the globe for the past uh few
months so actual conferences we loved it
uh I think the content was amazing and
so we just released today the talks on
YouTube so go check out the open AA
YouTube channel and you can find bu a
bunch of like pretty cool
content lastly all of that was a lot and
so we're going to do an AMA ask me
anything uh starting today with the
presenters the APM at open AI uh for the
next hour so please come and ask us any
questions that you would like on the
developer Forum uh the open a developer
Forum last last last sorry I have a bad
joke I have a bad joke uh we talked
about Co quite a bit you know how a
center has a Noy list you know of kids
like were noty why was structured

[00:22]
outputs on the noty list I don't know
tell me Santa heard it was a
schema on that note see you tomorrow for
day day day 10 of of 12 Days Bye by

</details>
