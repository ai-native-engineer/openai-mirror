---
title: "OpenAI DevDay 2024 | Welcome + kickoff"
channel: openai
url: https://www.youtube.com/watch?v=auXCQ9-721o
youtube_id: auXCQ9-721o
published: 2024-12-17
duration: "37:06"
captions: en
---

# OpenAI DevDay 2024 | Welcome + kickoff

[![OpenAI DevDay 2024 | Welcome + kickoff](https://img.youtube.com/vi/auXCQ9-721o/hqdefault.jpg)](https://www.youtube.com/watch?v=auXCQ9-721o)

<details>
<summary>자막: OpenAI DevDay 2024 | Welcome + kickoff (37:06)</summary>

[00:00]
-Hello.
Hi.
[ Applause ]
Hi everyone.
Welcome to our second DevDay
ever.
Yes.
[ Cheers and applause ]
First, you might notice
that things look a little
different compared to last year.
I'm not Sam.
I'm not going to announce GPT-5,
but we've got some
super exciting things
in store for you today.
I'm Olivier.
I lead the API product team
at OpenAI.
And today is a unique
opportunity for all of us
to take a break
from our computers
and whatever box
we were bashing in the morning
and spend time together.
We have a jam-packed agenda;
breakout sessions,
demonstration
by the OpenAI team,
a new developer community talks,
which I'm super excited about.
Everything is designed
to give you a chance
to spend the time with the
OpenAI team and with each other.

[00:01]
I wanted to start,
but why do we even do DevDays?
Why do we have
a developer platform?
OpenAI mission is to build AGI
that benefits all of humanity.
And developers are critical
to that mission.
Put shortly,
we cannot do this without you.
You'll see the future
before everyone else
and you cannot help
but bring it to life.
Four years ago,
we trained GPT-3.
We knew we had something
pretty cool,
big on our hands with GPT-3,
but we had no idea
what was possible with it.
What are the real world
use cases of that technology?
So we built an API.
The goal of the API
was to let you all
explore what
this technology could do.
Turns out that you can do
quite a bit with GPT-3;
creating marketing content,
translating languages,
and even building a chatbot.
Looking back, GPT-3 capabilities
were very, very limited.

[00:02]
There was no tool support.
Hallucination were
all over the place.
And the latency was super,
super slow.
Fast forward to today,
AI is completely unrecognizable
compared to the GPT-3 era.
There are more AI models
than ever before.
More AI applications moving
from prototyping to production.
And new developers
are pushing the frontier
of what the models can do
every single day.
I'm pretty impressed.
Like we have now 3 million
developers building on OpenAI
across more than 200 countries.
And I just checked the stats
compared to last year's DevDay,
we tripled the number of active
applications built on OpenAI.
So thank you for being
a part of it.
We've been building
quite too at OpenAI.
In the last year, we launched
more than 100 new API features;
that includes things
like structured outputs,

[00:03]
the batch API, new
fine-tuning support for models,
new playground, and embeddings,
and so much more.
New models as well.
We introduced the new GPT-4o
and 4 mini to push the boundary
both on intelligence and cost
efficiency.
And we are not slowing down.
I'm going to cover
in the next 20 minutes,
the four top areas
of focus of OpenAI.
First, we'll cover the
best-in-class frontier models.
Second, we'll build more
powerful multimodal capability.
Third, we'll enable you
to even customize
like more deeply models.
And lastly, we'll talk about
how can you scale
even more easily on OpenAI.
Let's start by talking
about models.
Just over two weeks ago,
we introduced the world
to our first series of models
that can reason
about complex problems.
That's o1.

[00:04]
Maybe a quick show of hands,
how many of you have tried o1
in the past couple of weeks?
Full house? I love it.
We've got only early adopters
in the audience.
Okay, so as you know,
we have two versions of o1.
The first one is o1-preview,
which is a preview
of the larger o1 model
that we plan
to release very soon.
You can think of o1-preview
as the more as the world's
most powerful reasoning model.
o1-preview is designed
to solve really hard problems
that require a
long thought process.
That's o1-preview.
The second flavor is o1-mini.
o1-mini is, well, a smaller,
faster, cheaper version of o1.
o1-mini is fantastic
if you're debugging code
or building
an agentic application.
o1-mini, in general,
we found it to be really good
at coding,
math and scientific reasoning.
But what do we even mean
by reasoning?
Reasoning comes so naturally
to us as human beings
that sometimes it can be hard
to articulate.
So let me break it down.
Reasoning is the ability
for a model

[00:05]
to have a reliable chain
of thought.
The model thinks step by step
before it responds.
The model can think through
different meanings of a question
and reflect on its answer
before responding.
So let's take a look at
the quick example of chain
of thought in ChatGPT.
So I'm not going to go
into details,
but that's essentially a brain
teaser, which is non-trivial,
that requires the model
to do quite a bit
of logical reasoning.
And so as you can see,
the model is going to reason
methodically about the problem.
Thinking through each line,
each sentence of the problem
and making sure
before it answers
that the answer meets all
the requirements of my question.
Now, I know that's probably the
most common question I've got.
What the heck is the name o1?
The shift to reasoning
introduces a new shape
of AI capability.
The ability for our model
to scale
and correct its thought process,
it's pretty mind blowing.
So we are resetting the clock

[00:06]
and we are introducing
a new series of model
under the name o1.
But let's look at
a few customers.
A few of our customers
tested o1 to see what
it could do for their use case.
First, I wanted to talk
about Cognition.
So Cognition is building --
Scott.
Scott, I see you.
Cognition is building Devin
and has been testing o1
with its AI software agents
to see how much more o1
could accurately plan,
write, and debug code.
So let's learn more from Scott,
the founder of Cognition.
-Yeah, I'm Scott Wu, I'm the
CEO and co-founder at Cognition.
The thing that's interesting
about programming
is that it's changed in shape
like over and over,
over the last, you know,
50 years.
Being able to write code
out line by line is one thing,
but also being able to
understand and interpret logs,
being able to navigate
and run commands that actually,
you know, affect the real world
is a big part of programming.
This new model o1 is
really able to process

[00:07]
and make decisions
in a more human-like way.
We worked closely with Open AI
on iterating on it
and giving our feedback
and testing it out.
What we found was
that o1 was just incredible
at this kind of reasoning.
At Cognition AI,
we're building Devin,
the first
fully autonomous software agent.
And, you know,
what that means is
that Devin is able to go
and build tasks from scratch
and is able to work
on problems the same way
that a software engineer would.
And so here actually,
I asked Devin to analyze
the sentiment of this tweet
and to use a few
different ML services out there
to run those out of the box
and break down
this particular piece of text
and understand what
the sentiment is.
And so first,
Devin will make a plan of how it
plans to approach this problem.
Yeah.
And so here,
you know, it had some trouble
fetching it from the browser
and so then instead it decided
to go and go through the API
and fetch the tweet that way,
right?
And all these little decisions,
you know,
things like that
happen all the time.
Finally, it's able to get
this all the way through.

[00:08]
It says
that the predominant emotion
of this tweet is happiness.
The soul of programming
has always been the ability
to take your ideas
and turn them into reality.
And now you can be
able to do that much faster
and cleaner than ever before.
-That's super cool.
Our second example
I wanted to mention
is Casetext and Thomson Reuters.
They've been using o1
to power an AI legal assistant.
In professions like legal,
nuance and precision
are critical.
Every single word matters.
So let's take a look at
an example.
Here, I'm asking
an AI legal assistant
to verify the accuracy
of the legal statement.
On the left, 4,
on the right, o1.
So as you can see,
4 claims that there are
no errors in the statement,
which is incorrect.
However, on the right,
o1 pays attention
to very specific words,
which are critical,
like neither and nor,

[00:09]
which completely changes
the meaning of the legal text.
And so as you can see
the model here, o1,
is able to see
that there are small
but critical errors
in the document.
I mean, listen, I could
talk about reasoning for hours,
but I think it's going to be
more fun to see a live demo.
So next,
I'm going to pass it to Roman,
our Head of Developer Experience
to show you what o1 can do
in action.
Welcome, Roman.
-Thank you, Olivier.
Good morning, everyone.
It's fantastic to see you all.
In just two weeks,
we've been blown away
by the incredible projects
you've all been
already created with o1,
from tackling hard problems
to building complete apps.
So I thought,
what about kicking things
off by creating an iPhone app
from scratch here on stage?
So I had this little idea
for an ISS tracking app.
You know what,
before you start reading the
whole thing, it's a bit long.
I'm just going to copy all
of that
over to ChatGPT desktop
and send it.
On the left side, I have
an empty exclude project open.

[00:10]
And what we'll do here
is we'll take a look at
what I'm trying to build.
So this app is articulating
a few things like,
"Hey, like I'd like
to create like the ISS map.
I'd like to track it
in real time.
I'd like to fetch
the astronauts in space,"
like a pretty intricate prompt
with lots of small details.
And you might wonder, "Well, how
is that different from FOGO?"
Well, in this case,
like o1 is basically trying
to go through making a plan,
architecting what's needed,
preparing the architecture,
and ultimately finding out
which APIs to use.
So now, to save a few seconds,
I actually instructed o1
to bring everything
in a single file.
So I should be able to go
copy this whole file,
this entire file and
bring it over to the project.
So this is a real life demo.
So this is always the challenge,
the tricky part.
We never know
what's going to happen.
So I'm going to try and build
this app right away on my phone.
And it builds.
Can we bring my phone
on stage please?

[00:11]
Let's see it.
It's happening. Zero shot.
And what's pretty amazing
here is like, yeah,
the ISS is moving
like I intended.
If I go to the second tab, the
astronauts in space also work.
And I could keep on going
and I could ask o1
what should we build next?
And it can basically be
my thought partner.
And what's really,
really amazing here is like,
o1 is like having someone
that understands your vision
right away by your side.
It's able to kind of complex --
take like the complex
instructions you have
and architect the whole thing.
Lots of great ideas.
Actually, I kind of like
the second one.
If we had more time, I think I
would build the AR view for it.
Anyways, it's pretty awesome.
But we all know that
coding is more about working
on an existing code base more so
than starting fresh, right?
So I wanted to dive into
something a bit more advanced.
I took kind of
a weekend project to interface

[00:12]
with these little drones
called Tello.
But the thing is
like I'd love to play with them,
but I've never
actually programmed one before.
And so what I've done is
like I prepared a little
web interface for it in React,
but that's all I have
and I'm honestly not sure
where to start.
And that's exactly
where o1-mini comes in.
And one of the great things
about o1-mini being in the API
is that I can use it
directly from my favorite tools.
In this case,
I'm going to bring up Cursor.
So I have my entire project
here open on Cursor,
the back end, the front end,
all my react components.
And on the right side,
I have the Chat and I can zoom
in a little bit so you have --
so you can see better.
So I prepared this prompt here,
but what's going on to give
you an idea at a high level
is that I have the front end.
I have literally no backend
for now.
And I'm telling o1-mini,
"Hey, so I have this like drone,
I'd like to interface with it
in JavaScript.
I prepared some command lines."
By the way, we started
some work previously with o1

[00:13]
to figure out which was the kind
of camera stream format.
This was one
of my aha moments with o1
that figured
out the right FFmpeg.
So it's saved in one file.
And now all I want is like I'm
going to send this prompt to o1
and in a few seconds,
hopefully, it's going to
kind of craft the plan
and try to wire up all of
these missing pieces in my app.
So you can take
a quick look here.
This is my front end
that we just saw,
but the server is
completely empty
because I have not made
this work yet.
So I hopefully in a few seconds,
this is, again, very much live,
we'll see what o1-mini
cooks for us.
All right, so what
did it come up with, right?
So it basically created
the entire server for me.
That looks pretty good.
So I'm going to copy it over.
What else is missing in here?
Perfect, let's move on.
So I had previously installed
the NPM packages.
Now, let's take a look at
the command interface.
What's pretty cool
is that it did add all

[00:14]
of the WebSocket code.
And check this out,
I'm going to try to apply
these changes right here.
And now, it's actually wiring
up all of the buttons
that I had in my interface
to send the right commands
apparently
with the right formats
to the drones.
So I hope this will work.
Let's take it --
let's take a look.
So I'm going to accept
these changes.
Let's see what else?
I think we just got to start
the server.
And this I think was
already done.
This is additional.
All right, let's move on.
I think we're good.
Let's save this.
Let's go to the terminal
and let's start the server.
First of all,
I'm going to have actually
to connect to the Wi-Fi network
that it's emitting.
It's right there. Cool.
I'm going to put it down
right here and see what happens.
Let's hope for the best,
it's the time to put it to test.
So let's go here and
start a server we just created.
Cool.
Let's take a look at the UI now.
If I -- it's good news,
the battery level showed up,
let's start a video stream.

[00:15]
Does that work? It does.
Awesome.
All right, and now, let's
actually try the real thing.
All right,
the buttons are working.
Amazing. I can go a bit higher.
This is a good time
for a drone selfie.
Awesome. And we can now land.
Amazing.
[ Cheers and applause ]
Isn't that pretty cool?
Like I had no experience
working with this drone before,
and o1-mini architected the
low level code with UDP packets,
connected it with my
front end and React
components with WebSockets.
And we are really entering a new
paradigm here with reasoning.
I can't wait to see what all of
you are going to tackle with o1
from your challenges and also
solve problems for your users.
Thank you so much
and back to you, Olivier.
[ Cheers and applause ]

[00:16]
-Thank you, Roman.
That was awesome.
And that was an only an
early preview of what o1 can do.
In the last few weeks,
we have already raised the rate
limits for o1 three times.
And today, we're
going to increase them again.
So we're doubling rate limits
as of now.
-Here we go. It's live.
-So at that point,
the o1 rating meets match
GPT-4o so happy scaling.
That's all.
I was sharing with a few
of you earlier today
who do not have access yet
to o1.
And so starting now,
everyone in the audience
officially has access to o1.
So have fun,
explore what you can do with it,
and tell us what you think.
We are going to keep
working on o1.
And there are quite
a few features
that we want to ship
in the near-term.
Stuff such as function coding,
structured outputs,

[00:17]
system messages,
image support, and much more.
o1 is super exciting.
If you've tested o1 firsthand,
you will know it's not a drop-in
replacement for GPT-4o.
In a way, o1 is slower
and more expensive than 4o.
And so what we see already
from like early testing
is that the best AI applications
combine both GPT-4o and o1.
So we will keep investing
a lot in GPT-4o and 4o mini.
And we're pretty excited
to share some of the new things
that we've been building
for these models.
Let's focus on multimodality.
How can we help you build
more powerful
multimodel capabilities?
As models get smarter,
they will also be
able to understand
and respond across
all modalities;
text, images, video and audio,
of course.
And I'm sure many of you have
played with Advanced Voice Mode
in ChatGPT,
it's pretty damn cool.
And one of the top requests
we've heard again

[00:18]
and again is how can I get this
natural speech to speech feature
within my application?
And so today,
I have some pretty good news.
It's coming, it's coming.
We're announcing
the Realtime API.
The Realtime API is a
super low latency API that lets
you build AI experiences
real time within Europe.
The API streams inputs
and outputs
in real time using WebSockets.
We're launching it
starting today with support
for speech to speech,
which is the same technology
that powers Advanced Voice Mode.
yes, that powers Advanced
Voice Mode in ChatGPT.
And that will allow
you to build voice experiences
using the six voices
already available in the API.
In general, but in particular
for the Realtime API,
a demo is worth 1,000 words.
So you know what?
Let's bring back Roman on stage
to show us what's possible
with the Realtime API.

[00:19]
-Thanks, Olivier.
I'm truly excited
about this Realtime API
already kind of give
me some ideas for this,
so I'll have to work on it
after.
You know, a lot of you
have been asking about building
amazing speech-to-speech
experiences right into
your apps.
Well now, you can.
So let's take a look.
First under the hood,
this is the Open AI playground
that all of you know,
I'm sure, and it now has,
as of today,
full support
for the new Realtime API.
So in fact,
we can try it right away.
Hi there.
-Hi there.
How can I help you today?
-Hey, can you tell me
a fun fact about OpenAI DevDay?
-Sure.
Open AI DevDay is
an annual event
where developers, researchers,
and enthusiasts gather to learn
about the latest advancements
and tools from OpenAI.
-Cool. Thank you.
-It's a great op --
-Could you --
-Glad you think so.
-Could you whisper
a little secret
like your best kept secret
about being a great developer?
-Here's a little secret
for you.

[00:20]
The key to being
a great developer
is to never stop learning.
-Awesome. Thank you.
-Take your --
-Great.
-Glad you liked it.
-So as you can tell,
you have now the ability
to kind of interrupt,
generate intonations all
of the features and capabilities
you know and love from ChatGPT
as of today
in the Realtime API for you.
If I click on logs,
you'll see behind the scenes
like all
of the events coming up
on this WebSocket connection
that's fully programmable
for all of you.
Now for the playground power
users out here in the room,
I'm not sure if you've noticed
this little new shiny icon
on the top right.
If I click on it,
check this out.
If I were to build, let's say an
event assistant app for DevDay,
and if I were to just say
event assistant and hit Enter,
this is now the ability for
you to quickly generate prompts
so I can expand it from here,
but in just two words, I have a
complete prompt to get started.
And we've heard
from so many of you
how crafting prompts
can be tedious at times.
Well, we want to help you build
as fast as possible on OpenAI.

[00:21]
And by the way,
it's not just prompts.
Let's say I want to create
a new function here
and let's say I would like
to check in an attendee
for my event app
while instead of typing
the function definition by hand,
I have one ready to go.
So that's pretty convenient
and add to fingertip
also for JSON schemas.
Awesome.
But now, let's take
a look at a concrete example
of what can you build
with this Realtime API.
So for that,
I'm going to bring back our
favorite fictional travel app
from last DevDay, Wanderlust.
It's great to see so many
familiar faces in the room.
Thanks for being
on the journey with us.
So if you remember,
last year, we used this app
to show how to build
an assistant
with a text kind
of conversation, right?
So if I were to say SF here,
this was kind of the demo
of like using it with text.
Let me just refresh it
real quick.

[00:22]
All right.
-Here's San Francisco,
what can I help you with?
-Now,
the first thing you notice
is that there is a voice
speaking
and in fact I also dropped
some code to integrate
with the Realtime API
into Wanderlust
and I can click the cycle into
now turn on the voice assistant.
So let's try it.
Hey, I'm planning my trip
to OpenAI DevDay in London
and then in Singapore.
-Got it.
London and Singapore
for OpenAI DevDay.
What do you need help with?
-Could you give me
some recommendations of places
to eat in London?
-Sure thing.
Here are some tasty spots.
Dishoom, Sketch, and
Duck & Waffle are must tries.
-That sounds great.
Do you think you could also give
me some hotel recommendation?
I'm thinking about staying
in the kind of
Strand neighborhood
by the river.
-Absolutely.
In the Strand area,
the Savoy, ME London, and Strand
Palace are fantastic choices.

[00:23]
Enjoy your stay.
-Cool. I was thinking with
something more lowkey but...
All right, that's a bit far.
Let's go back to London, please.
-Sure.
Focusing on London,
for budget stays in the Strand,
try Z Hotel Strand,
Hub by Premier Inn,
or The Strand Continental.
-Awesome.
So the two things I want
to highlight here is that, one,
on the left side
you could tell we have
the complete transcript
of the real-time conversation
as it's happening
and you can have that right away
on your website at connection.
And on the right side
of the screen,
as you could tell,
the Realtime API supports
functions and tools and APIs,
which means
that you have the ability
to connect to kind of
any function.
And in this case,
for me it was
like annotating the map
and placing pinpoints on it
and so on and so forth.
So we think you're going to love
using the Realtime API.

[00:24]
And if you're users,
for instance,
are driving, learning,
cooking or any kind of context,
we think they're going to
be delighted as well.
But now, let's try
something a little harder.
So what if we could give
some extra capabilities
to our voice assistant
beyond this interface?
So let me refresh this
and go back to a different
kind of conversation.
-San Francisco, here we are.
How can I assist?
-Yeah, could we take
a look at Fort Mason, please?
-There we go.
Fort Mason, what
do you need help with there?
-Well, I have a few hundred
awesome developers here
in the room and I'm thinking
they might need a little snack.
Do you have some chocolate shops
around here?
-Absolutely.
Check out Ghirardelli Square,
Ilan's strawberries
and The Candy Store.
-Great.
Can you show me more details
about the three places?
-Details are up.
Ghirardelli Square offers
iconic sundaes.
Ilan's Strawberry Lane has
delectable chocolate
covered strawberries

[00:25]
and The Candy Store is
your go-to for vintage sweets.
Enjoy.
-Great.
So as you can tell
another example of
like pulling details with tools
in real time.
Now, what's really awesome
about the Realtime API
street pointing functions
and tools
is that you can
actually call third party APIs.
So for example,
what if we were to add Twilio's
phone calling capabilities
onto Wanderlust
by using the Twilio API.
So I see here the Ilan's
strawberries location seems
to accept AI orders.
And so what we're going to do
is like we're going to try
this live.
So I'm going to invite Ilan's
from our developer experience
team onto the stage to join me
so you can actually see
that in action.
Thanks, Ilan.
So now what I'm going to do
is I'm going to resume
that conversation we started
and we're going to try
that live.
Let's go.
Hey, Ilan's Strawberries looks
really fantastic.

[00:26]
Could you place a call
and see if you could get
us 400 strawberries
delivered to the venue?
But please keep that
under $1,500.
-I'm on it.
We'll get those strawberries
delivered for you.
-Hello.
-Hi there, is this Ilan's?
I'm Roman's AI assistant
calling about an order.
Fantastic.
Could you tell me
what flavors of strawberry dips
you have available?
-Yeah, we have chocolate,
vanilla,
and we have peanut butter.
-Great.
How much would 400 chocolate
covered strawberries cost?
-400?
Are you sure you want 400?
-Yes, 400 chocolate covered
strawberries please.
How much would that be?
-I think that'll be around
like $1,415 with 92 cents.

[00:27]
-Awesome.
Let's go ahead
and place the order
for 400 chocolate
covered strawberries.
-Great.
Where would you like that
delivered?
-Please deliver them to the
Gateway Pavilion at Fort Mason
and I'll be paying in cash.
-Okay, sweet.
So just to confirm,
you want 400 chocolate
covered strawberries
to the Gateway Pavilion?
-Yes. That's perfect.
And when can we expect delivery?
-Well, you guys are
right nearby so it'll be like,
I don't know, 37 seconds.
-That's incredibly fast,
thank you so much.
Have a wonderful day.
-Cool, you too.
Awesome.
[ Cheers and applause ]
-Thanks, Ilan.
Wasn't that cool?
Of course, this is
just a simple example showing
the power of the Realtime API
combined with tools,
but we hope that's
going to inspire many ideas

[00:28]
for your own apps and products.
And not only did we place
the call with Twilio,
but as you could see
the transcript,
we also extracted
important details
of that conversation
along the way.
So I really can wait
to see what all of you
are going to build
with this Realtime API
and I'm sure you're
going to reinvent
how humans and computers
interface with each other
with these new like
voice capabilities.
Thank you so much for your time.
I can't wait to spend time
with all of you today.
And with that, back to you,
Olivier.
[ Cheers and applause ]
-Thank you, Roman.
That was awesome.
Let's look at the few
real applications
that have been testing
the Realtime,
API in alpha
in the past few weeks.
The first one I wanted
to highlight is Healthify.
Healthify is a nutrition and
fitness coaching application.
So the Healthify team has
been testing the Realtime API
to create a more realistic
coaching experience using voice.
Not only can you have
a natural conversation
with our AI health coach,

[00:29]
but you can also ask
your AI coach to call
and connect you with a health
coach in the real world.
A second pretty cool
example is Speak.
Speak is building a
language learning application.
Speak has been testing
the Realtime API
to create a more natural and
intuitive learning experience.
Let's check it out in action.
-What I want to show you today
is something
that we call realtime roleplay
as the first thing
that we're launching
on top of the Realtime API.
Part of what's really cool about
it is that speech to speech
and the multimodality really
allows us to understand more
than just the pure
text transcript
of what a user is saying
into the app.
[ Speaking Spanish ]
-The word baño is pronounced
"ba-nyo"
with a soft "ny" sound like in
the English word canyon.
Can you try saying that again?
-[ Speaking Spanish ]
-Perfecto.
[ Speaking Spanish ]

[00:30]
-And the model
basically has a lot
of the very human-like
capabilities
of a real human teacher.
Like how amazing is that?
-The Realtime API
is working with GPT-4o.
And we will begin rollout
in public beta starting today.
[ Cheers and applause ]
That API is focused on speech
initially,
but we want to support
more modalities
over time such as video.
If you want to learn more
about the Realtime API,
there will be a breakout
session completely focused
on that later today.
All right, let's move
on to our third focus area.
We are focused on making
our models more customizable.
In the future,
I believe that every single
company will have a custom model
which is tailored to its needs.
The model will understand
really well your businesses,
your goals, your use cases.

[00:31]
Most recently, we launched
fine tuning for GPT-4o
and 4o mini to every developer.
The launch reception was
really good.
It actually broke
our dashboards.
You know,
it's a good point to have.
And today, something new.
We're excited to announce
vision fine-tuning with GPT-4o.
Vision fine-tuning means
that you can now use
images to fine-tune the model
and improve result
from image understanding tasks.
Vision fine-tuning
can be used for anything
from product recommendations,
medical imaging,
and even building
autonomous driving system.
As a matter of fact, one of
our alpha developers was Grab.
Grab is a really cool company
building
a ride sharing application
in Singapore.
They use fine-tuning
to teach its mapping system
to identify traffic signs
and count lane dividers.
It looks like
a pretty complex like problem
that you're not used to before,
but actually, Grab was
able to do that with 100 images

[00:32]
of traffic signs.
And the MO performance was
able to spot these common sites
on the road as a result.
Plenty of other use cases
from finding product defects,
creating no code UI
and so much more.
As of today,
fine-tuning with vision
is available to
every single developer on phone.
[ Applause ]
The last theme of the day is to
help you scale on our platform.
As you've noticed,
we are obsessed by bringing
down the cost of our models.
The reason is super simple.
Every time we reduce the price,
we see new types of application,
new types of use cases emerge.
We are super far
from the price equilibrium.
In a way models
are still too expensive
to deploy massive scale
in particular
on cost-sensitive use cases.
And since the release
of text-davinci-003,
which was the first version
of GPT-3.5,
we have decreased the cost
per token by 99%.

[00:33]
That's right,
today's models are more
almost 100% cheaper compared
to two years ago.
In fact, even though
the o1 model is more expensive,
it is still somehow cheaper than
GPT-4 when it first came out.
And of course,
o1 is way more powerful.
Today, we're taking one step
further with prompt caching.
[ Cheers and applause ]
Many applications pass
the same context over
and over again to the model.
For instance,
passing a code base,
passing product information,
or long multi-term
conversation history.
So starting today,
we'll give you automatically
a 50% discount for every input
token that the model
has recently seen.
That's a request that
we've heard from many of you
and we excited to make
it available to all developers.
And that happens
automatically starting today.
There is zero change for
you to do in your integration.

[00:34]
We'll have a talk later today,
a breakout about optimizing
cost and latency
and we'll talk about pump
caching in way more details.
I have something else
to announce on the topic
of making AI more affordable.
A big trend in the industry
right now is model distillation.
With distillation,
you take the outputs
of a large model
to supervise to teach
a smaller model.
And so today,
we are announcing our
own model distillation tools.
You can now easily distill
the outputs of o1
and 4o to fine tune a 4o mini
all within the OpenAI platform.
The goal is to bring even more
intelligence to small models
at a low cost for you.
Concretely, two new tools
are going to ship
to enable distillation;
store completion and evals
evaluations.
Store completion is going to let
you store your interaction
with the models directly
on your OpenAI, your logs.
This will allow you to create
super easily fine-tuning

[00:35]
data sets on OpenAI.
And we're also shipping an evals
feature in public better.
So you can run custom evals
on the OpenAI platform
to test how well
your fine-tuned model perform
against a large model.
The goal with all of this
is to make it much easier
for you to fine-tune
and evaluate a small model
to get performance
that sometimes may
even match o1 on specific tasks.
We are shipping our
model distillation tools
starting today
to all developers.
So feel free to start
testing right away
and we'll have a deep dive
later on
on the distillation
breakout session.
All right, we covered a lot
of ground today;
our new all one reasoning
models, the Realtime API,
vision fine-tuning, prompt
caching and model distillation.
At last year's DevDay,
we talked a lot about
our ambition to build AI agents.
But model capabilities
were often getting in the way.

[00:36]
Standing here today,
I feel the new o1 models take
us one step closer
to enable true agents.
And I feel truly,
truly grateful
to have the opportunity
to invent the future
together with all of you.
But we have many,
many steps to get there
and your feedback is critical
to build this future together.
So please, please,
before you leave today,
say hi to any of us
on the Open AI team.
We would love
to hear what you're building.
Before I leave,
I want to give you a quick look
of the agenda
for the rest of the day.
We've got a series
of breakout sessions and
developer community talks.
You should really check them
out.
And of course, we know DevDay is
not DevDay without Sam.
And so we will welcome Sam
and our new CPO, Kevin,
for your Fireside Chat
at 4:00 PM today.
If you want to ask
questions to Sam and Kevin,
drop questions,
there is a physical box
right outside the room,
they would love to take it.
Thank you.
Have a wonderful day
and let's go build
this better future together.
[ Cheers and applause ]

</details>
