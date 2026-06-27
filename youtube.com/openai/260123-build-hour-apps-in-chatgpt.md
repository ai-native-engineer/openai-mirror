---
title: "Build Hour: Apps in ChatGPT"
channel: openai
url: https://www.youtube.com/watch?v=mFG-4vUJ0kI
youtube_id: mFG-4vUJ0kI
published: 2026-01-23
duration: "48:38"
captions: en-orig
---

# Build Hour: Apps in ChatGPT

[![Build Hour: Apps in ChatGPT](https://img.youtube.com/vi/mFG-4vUJ0kI/hqdefault.jpg)](https://www.youtube.com/watch?v=mFG-4vUJ0kI)

<details>
<summary>자막: Build Hour: Apps in ChatGPT (48:38)</summary>

[00:00]
And we're live. Hi everyone. Welcome
back to OpenAI Build Hours. I'm
Christine. I'm on the startup marketing
team and I'm here today with Corey on
our developer experience team.
>> Thanks Christine. Nice to see everybody.
Um I particularly work on chat apps but
broadly um on our developer experience
team across OpenAI's uh developer
platform and tooling.
>> So our first topic for this year is apps
in Chat GBT. Um this is our first uh
build hour of the year and I'm actually
really excited that we have students
from Berkeley, Stanford, MIT joining us
today for the first time. Um so build
hours if you're not familiar is to
really empower you with the best
practices, tools, and AI expertise to
scale your company using OpenAI APIs and
models. Right below on your screen,
there's a link where you can check out
our homepage. You can watch past build
hours on demand as well as sign up for
all upcoming ones.
So today, here's a brief snapshot of
what you can expect. So first, we're
going to do an overview on the apps

[00:01]
platform. So this is going to be what we
launched, real use cases. We're actually
going to go into chat GPT and show you
the apps that you can use right now. And
then we'll dive into building an app,
the entire process, and also how to use
codecs and our newly launched Docs MCP
server to do this. And of course the
demo. We always live build during build
hours. And today we'll be creating an
app in Chachi BT to play ping pong. We
did practice beforehand playing ping
pong. So we are definitely ready. Um and
then Corey will walk you through some
best practices on how to make your app
even better. Um so this includes UIUX
guidelines and what makes an app
actually valuable and then additional
resources so that you can build an app
and submit it um to be reviewed to be
able to be live in TATBT. And then last
is Q&A. We reserve 10 minutes for this.
Um during the session, you can actually
go into the right side of your screen if
you click over to the Q&A button. Um
feel free to submit your questions,

[00:02]
comments. Our team is in the room right
here in SF as well as New York and we'll
answer them throughout the session. Then
we will pick a few to answer live. Um so
with that, let's dive right in.
>> Thanks Christine. Um well, hey
everybody. Uh good morning, good
afternoon, good evening from wherever
you may be joining. Um I'm really
excited today chat talk about Chad PD
apps particularly the apps platform and
show you how to build. Um I know we have
a variety of folks here watching today.
So um we have both people for the first
time looking at chatb apps and I know
there's a lot of seasoned developers out
there who've been messaging me before
the live stream. So hopefully this is
helpful for both uh net new builders and
also those who are more experienced. Uh
so let's kick off and move over to the
next slide.
Great. And just to cover what we've
launched since um dev day when chatb
apps as a platform launched uh we
launched our apps SDK um everything from
the framework and how chatbt injects a
UI widget within uh the client to uh how

[00:03]
we are able to use MCP servers to pull
in different contexts and tools and
actions to take actions on behalf of the
user's intent. And as well we launched
our um apps doc um site within
developers.ai.com open.com for everybody
to learn about all the different um
components pieces um for you to build
your experiences that you'd like. And as
well, we've recently launched our um
public app submission flow as K
Christine mentioned. Uh you have the
opportunity to put your own experience
within JPT for people all over the world
to use. And as well, we have an app
marketplace for you to discover more
apps and install them into JPT. And the
last but uh last but not least, we have
a bunch of different resources we've
shipped across our UI component library
uh which helps give you already styled
um assets for you to make your app that
look and feel very succinct with the
rest of JPT. And we have an app sample
repo um please check those out. And last
but not least, what I'm excited to show
you today is our new Docs MCP server to

[00:04]
get you building even faster.
All right. Um so we're going to move
into a demo of SM apps to begin. I'm
just going to show uh what apps actually
look like within CHBT and then we'll
move on to actually creating an app.
All right. So now it's my turn to share.
I'm going to go to my screen.
Okay. Um I am actually going to go over
here and tab over really quickly. Cool.
So here we are in CHBT and I've
preloaded the All Trails app. You can go
into the plus button and then add more
apps there directly or go to our app
directory to look for different apps
that you would like to install. And you
know this weekend um I'd love to go
hiking. So let's ask All Trails app um
to help me do that. I'd like to go
hiking in Marin. Please help me find
some great trails.
Hide this. Okay.

[00:05]
So while this is happening um the model
is in taking in um my intent and then
passing that context off to all all
trails MCP app and it's providing back
um a list of data that you know is in
the all trails platform. So that's
really what's powerful about apps. You
can pull in different contextual data
that doesn't exist um potentially
publicly on the web or for the model to
directly access. All Trials has a lot of
great reviews on their site for uh that
type of information and it's presented
this UI layer for me to see um you know
where they are in the world. Um but I'd
love to do something even more powerful
here and refine that experience um by
asking it to do something and find me
dog friendly trails.
Please um find me dog friendly trails in
marine.
And at this point the model now is doing
some refinement with the all trails app.
And here we go. It's filtered some great

[00:06]
dog friendly options. And that is a
capability from the app directly that
you can provide um to create a more uh
engaging and immersive experience that
uses the power of the model. um the uh
engagement experience from a UI and as
well some logic and data that's been
brought in from all trails. Um as well
they have the capability of doing full
screen mode. So these are some great um
uh widget capabilities that we've
exposed for you to control the
experience within chatbt. So let's move
on to the next app. So if you haven't
seen the Adobe Express app, we're going
to load that one here. And you can do
some interesting um visual uh creation
directly now in chatbt. So you can say
build me
a flyer for a builder
event here
in San Francisco
on January
24th.
and let's make it outdoor clothing

[00:07]
theme. Keeping up with our hiking
adventure for this weekend.
So, while that happens, you know, a lot
of uh things are being kicked off. Um
the Adobe Express app MC MCP server is
being called. Um some logic is being
passed in for some creation. It's going
to be surfacing me different templates
right now um to pick the style and feel
of my uh flyer that it's being generated
here. I like the this one. This one's
Let's choose this one. And then at this
point, I can decide if I like it. And I
actually can fill in the context um from
above. So I'll just say um fill text
with the um event details.
And at that point, you can take the
context that you've supplied above from
your first prompt and inject that
directly into um the event template that
we chose.
Great. So, so here are some options that

[00:08]
it has chosen. Um, and you can go and
edit this further for your builder's
event. Um, you can also see this um, and
personalize this directly. Um, but what
we're going to do is just jump ahead to
the next app. I'm going to show you now
quizzes.
So, um, quizzes is an app that we built
at OpenAI for anybody to build their
own, um, quiz tool and help you, you
know, learn more information. So, I love
coffee. So, let's build a quizzes app
that tests my knowledge of how to make a
great espresso.
So, one thing interesting about the
quizzes app is all the content in this
UI here is dynamically rendered. Um, and
we did that by creating just the
structured output um within your um tool

[00:09]
response so that the UI knows um how to
exactly render out the content based off
of the context provided in. Um, so all
all of the generation here is only done
dynamically and nothing needs to be
necessarily stored um in the back end.
So that's one paradigm you could um add
into your app if you want to have
dynamic content.
It's taking a second to generate a quiz.
Let's give it a second.
All right. For a balanced espresso on
many modern machines, what brew ratio is
a common starting point? Christine, do
you know?
>> I will guess a 1:4 ratio.
>> All right. Let's see if that is.
Unfortunately, it was 1 to2. Okay. What

[00:10]
is a typical target brew temperature
range for brew for espresso? I actually
don't know this. It might be 98 to 105,
110 to 120, 80 96. Okay. Well, there you
go. You can use the quizzes app to
basically build any type of information
that you would love to be tested on and
come back to the same chat history and
and redo those for um learning. So yeah,
these are just some fun experiences to
show you what you can build within HPT.
Uh but let's actually go take a look now
um at the next piece of content. So, I'm
gonna stop sharing my screen
>> and we're back. Okay. Thanks for walking
us through all of these um apps in
ChachiBT. Feel free to try this yourself
if you're watching and play around with
it.
>> Great. So, we looked at some apps um
what we've launched and how they work in
chatbt. I'm going to just spend one to
two minutes on the app construct of what
is an app in CHBT and then we'll move in
to start building some apps ourselves.
Um so for folks um watching if you're
not already familiar with MCP as a

[00:11]
concept um MCP provides capabilities
across tools, actions and resources that
enable you know AI clients to have uh
different actions and knowledge being
brought in and taking actions on behalf
user both in read write capabilities.
And so if a user asks chat tovt um you
know for example like find me trails um
you can use the alltra trail app talk to
your MCP server which could do anything
from pulling in data from a backend to
um generating some information on the
fly and then responding back with uh the
URI um in the tool output for chatb to
to render out a web component. The web
component is optional. So you could just
have a backend only chatbt app but what
I think is most powerful is combining
both the model um data logic from MCP
server and also a web component that is
you know interactive within chatbt. So
the web component um gets loaded within
chatbt and it has access to the
windowopenai

[00:12]
uh capability uh API that is allowing
you as a developer to do things within
chatbt that provide an immersive
experience. Um we can tab two two tabs
over
Um, here we go. So, one of the things I
wanted to call out is the framework here
that we built and works within CHPT is
an open protocol. Anybody can have an
MCP server and also use the same
framework of injecting a uh widget
runtime within an AI client to have a UI
on top of an MCP server.
And just to dive a little bit deeper on
the actual web component, we've exposed
the window. OpenAI API which allows you
as a developer to have your uh widget
template call this API and do a bunch of
different things from reacting to
context updating state receiving the
tool results to um you know take some
action or call the tools directly to do
some other operation. Um yes so I'm
going to spend a few more minutes now

[00:13]
just talking about what those
capabilities are and then we'll keep
keep it moving. Um, if you're not
familiar already, um, there's the
ability to do full screen mode like we
mentioned. And as well, you can add in,
um, anything you want really in the UI
that meets our, um, app submission
guidelines and policies. And, uh,
rendering and map view is one of those
examples that creates a really immersive
experience.
>> And we have a UI component library that
we'll share um, after this live stream
and also in the chat.
Some of the display mode options that
you have is you can um just load the
widget in line. That's the most common
experience. So that in flow as a user
continues to talk with the model um it's
brought in to provide additional um
enhancement to the experience. You do
picture and picture which is quite
interesting um to always leave up some
type of floating window as a user
continues to engage and as well full
screen as I mentioned.
>> Awesome. So, I think it's time to

[00:14]
actually go through the process of
building an app. Um,
let's actually run through the process
of how to build an app. Um, and then
we'll show you how to use codeex
afterwards.
>> Awesome. So, now I'm just going to talk
as a developer to everybody listening
and kind of uh walk through what it
means to build a chatbt app. This is the
process that exists today for most um
developers and the traditional way of
building apps. You may read the docs um
and learn a lot about you know a content
an API an SDK our quick start for
example. You then may go into GitHub and
then download some code and actually see
some examples as well. You may then go
reference a component library that we
shipped which is really helpful for
people to get going quickly and use
things that are styled um already. And
then you may start um coding in your
repo um and just start hacking away,
downloading the samples, editing them
and you have to remember all these steps

[00:15]
that iterative process of understanding
the concepts looking at the components
going in the repo and you code for days
and this has been the traditional form
of software development for a long time
now which we're all familiar with and
then you also have to fix deployment and
and u manage your application and um the
runtime of that nature. This is great,
but I think we have the opportunity as
well to look at the build app process
using codecs and our um docs MTP server
to help you build that much faster in an
AI first world. So I still recommend
everybody to go build the traditional
way, read, download sample code and and
ingest information, but as well if you
want to get going quicker and also have
a really uh smart, thoughtful partner to
work with you and code pair, Codex has a
great tool here to help you build a lot
faster. So at this point we have one
more slide.
Um just want to quickly highlight that
we have our docs MCP server. Um, as I

[00:16]
mentioned earlier, MCP enables AI
clients to have additional information
and context and take actions on behalf.
What our docs MCP server does is you can
load this into codeex directly and it
has all that context on how to build an
open AI in an AI um enabled way for uh
the model to understand um you know how
to hit our API or um scaffold out code
and things of that nature. Um, so our
MTP server is is um uh based on all of
OpenAI's content. So you could build our
API um our apps SDK um and and more. But
today we'll just focus on how you can
use it to build a chat app.
>> Cool. I will switch over to you so you
can show how to do this.
>> Thank you.
Um so if you're not familiar with Codeex
already, it's really easy to get going.
You can go to OpenAI developers um site
and go over to Codex and go over to the

[00:17]
overview. And this is how you install
it. It's just an npm install command.
So, we're going to do that right now.
And here I am in the terminal and I'm
going to install Codex. I already have
Codex installed so it would scaffold
out, you know, a little bit more
packages. But there you go. I've
installed Codex. Next up, we're going to
add our MCP uh server for the OpenA
developer docs. We are in the openi
developer site again under resources and
that's where we have our link for docs
mcp again um you can use this with codec
you can use with z code you can use this
in cursor um our docs mcp server are
here to help you build um irrespective
of the platform you use for ani coding
tool so let's copy that and let's go
into our terminal again I'm going to
clear the um window I'm going to paste
that command and codeex mcp add open
developer docs and here's the URL
Great. We've added our global MTP
server. Now, anytime I talk to Codeex, I
have this information ready to go. Um,
so what I'm going to do now is also copy

[00:18]
over
a um
agents MD file into this folder. So now
all I have is this agent MD file. And
all this agents MD file is going to do
is say always use the open A developer
documentation MC server if you need to
work on anything with open API chats FDK
etc etc and that just provides um codeex
the context it needs um to always know
to use open I developer docs all right
so we've installed codeex we've
installed the docs and p server let's go
going and just scaffold out some code so
I'm going to initiate codeex by just
saying codeex and the very first time
you're running codeex in any uh
repository or workspace, you have to
enable or allow um it to take actions on
your behalf or you can require approval.
I'm going to just allow it. Great. And
here we are within codeex. Um you're
welcome to choose the model you want to
run. I use GPT 5.2 Codeex and as well I

[00:19]
stick with the default medium reasoning
level, but you can throttle those up and
down as you please. Um great. So let's
go ahead and ask Codeex to build me a
ping pong app. As you saw, there's
nothing in my repo except the agents of
D file. Um,
create me a chatbt app with a simple
UI and MCP server to play a pingpong
game. I'd like to be able to drag my
cursor to control a paddle
um that I can play
against the computer. So I just came up
with this right now and this is the
command I'm going to give Codeex and at
this point CEX is going to take um some
time to you know take on this task. It's
going to inspect the current repository
which is nothing is in it and then at
that point understand from the agent MD
instructions that it should probably use
our open AI docs MCP server to start

[00:20]
ingesting this information. As you can
see here it's understand that context
and it the first thing it did already is
now calling a developer docs MCP server
looking for the chats apps SDK quick
start which will help it scaffold out
code and actually start building out a
repo for me. And as it's building um as
it's building this out, you can actually
see what docs it's referencing.
>> Exactly. So it's looking at the quick
start and it's going to be going forth
and looking at the MCP server files,
etc., etc. Now, this is the process you
may already do um in your current
developer flow by reading the docs,
looking at, you know, quick starts and
then going from there. Um but you can
let a lot let a lot of that initial
scaffolding be driven through codeex.
Um, so while this runs in the
background, it will take a couple
minutes here to kind of build out my
initial game. I will go back to the uh
docs here and just quickly show you some
components here within the docs that it
may be looking at. So the quick start
itself for um your own level of uh

[00:21]
learning has everything you need to
build a very simple app. shows you a
simple HTML file and as well a
a basic MCP server. In this case, this
example is using um the um node MCP
server package to to start building out
your own MCP server. And it has a simple
uh tool register here and as well the
resources that it responds with and how
to run that server. So this is what the
codeex MCP server right now is ingesting
and building.
>> All right,
>> we did have a question. Um someone did
ask if um you have an example hello
world web component um and they're
struggling most with packaging. So is
that something that we can help with
using codecs?
>> Yeah. Um that's a great question. So two
things that I think that will address
that. One is take a look at our quick
start. This is essentially the hello

[00:22]
world. We also have full example repos
um in the GitHub that I will link at the
end and show you. Um but for the easiest
just getting started, you can run both a
web component and your MCP server to
build a very simple hello world app. And
what I've shown today and the task has
just finished is you can ask Codeex to
actually just scaffold out a hello world
for you um if you don't want to download
it yourself and and take on those um
initial steps. Okay, great. So let's
look at what um Codex did here. It built
a minimal CHPd app with a ping pong web
component and MCP server. Um I can um
you know look at my repo here and see
what's in here. So we have agents MC
that I already created package JSON
public where my HTML is and the server
that's there. Um let's actually just run
this MCP server. So I'm going to go into
this other tab. You can see here these
are the files that it was created. I'm
going to mpm install the packages.
And now I'm going to mpm start and run

[00:23]
this server. What was Oops, sorry. I
already have a server running in the
background. Um why don't we um
I can either change my server here like
let me do it on the fly. Can you update
server from local
host 8787 to 8000?
This is a good live debugging. Um, I
already have a port running in the
background. So, um, without me jumping
over there and killing that, I can just
tell Codex to update my server. It's
great. So, let's go back here in this
window and let's rerun that. So, I can
do mpm start.
Oh, I need to reinstall.
Okay.
Great. Well, what I'm going to do is

[00:24]
actually just turn off the other server
really quick.
All right.
All right. Let's go back to screen
share.
Okay, cool. I have my server running
right here and I am going to now tunnel
the local host at 8787
to
this endpoint.
And now we can go into chatubt here and
add this app to chatbt. Let's go into
settings and go into apps. Let's go into
create app and call this ping pong build
hour.
and add this MCP server. I'm going to
add in /mcp because you need to
reference the actual MCP server running
on my enrock tunnel. I'm going to go to
no off and I'm going to allow this app.
Let's create the app.

[00:25]
All right, let's add this app now into
chatbt ping pong bug hour and say start
match.
All right. So, this is a very basic
pingpong app that was just created. And
I Oh, looks like I have to drag my
paddle, which is kind of fun. Um,
but in just a few prompts, I'm playing
against the computer right now. Uh, I
was able to generate the um code to
scaffold out a very basic ping pong app,
which is really fun.
But what would be even more fun is to
have multiplayer uh AI insights where
the model can give me information and um
do this in real time where I can play
with um a friend who also is on chat
like Christine.
>> Okay, I'm ready.
>> So this is a simple app that we

[00:26]
generated with um Codeex. Sorry, go
here. We're running an Enro tunnel to
tunnel for our MCP server and um codeex
just scaffolded out of the code. So I
can take a look at that right here. You
can see this is um the code that's
running. But what I'm going to do now is
turn off this server and
go into
um let me and we will show you a app
that I've built
in full screen.
Okay, so we're doing this live, folks,
so bear with me. Okay, so I am now going
into here. And this is a ping pong app
that I've spent a few more days working
on or a few more hours using codecs. And
I'm going to start this server. Actually
do need to turn off the old server,
which I did. And then go and create a
new tunnel. Oop, the tunnels are
actually already live. So, at this point

[00:27]
now, I should be able to go here. And
I've spent, um, a few more hours adding
in capabilities like scores, um, a
lobby, and also, um, the ability to do
multiplayer. Um, let's do this live, and
if it doesn't work, I will debug and get
it working. But we're going to do a new
match. So, I'm gonna ask it for a new
match. And at this point, um, Christine,
you can do this as well. You're going to
do new match. So, Christine's screen is
on the right. Mine is on the left.
We've are running my MCP server and the
ping pong app that um I spent a few more
hours working on. And so this is an
example of where you could take like an
app um and I'm going to do create match.
And you're going to take this code.
>> Okay.
>> C6 C2 E9.
And you're going to join match. And when
she hits join match, the game should
move right away. So I'm only moving my
left screen here. You can see my mouse
and Christine is playing on the right.
Oh, already scored one point.
>> Okay. I have to
>> we're gonna play a full game here

[00:28]
because we I spent a few hours building
this and we want to let everybody see
this in action. But the point is this is
the first ever real time multiplayer app
ever in HBT um or at least the one I've
seen and that's a lot of fun. You can
create an experience that is both a game
or you can imagine this being done for
something more um in a in a business
workflow like um a live editor or things
of that nature. But a game is a really
fun example. you could play with your
friends. And I'm going to let Christine
score a few points here cuz she's
actually really good at ping pong. We
played and she did beat me
>> definitely.
>> So, boom. She's going to score. And
we're going to we're going to get to
seven points. So, right now, I'm just
letting the ball go through. But, let's
rally one more time and then I will miss
this next shot. Boom. Okay, we're going
to get to seven.
>> And now game's over. I lose because
screen Christine screen says she wins
which is really fun. Um but what's even
better and why this is powerful to do
within chatbt is you have the access of

[00:29]
the model right there. I've additionally
exposed a separate tool call for
postgame analysis and I think that's
what's interesting. You can create an
experience that is enriching engaging
but you can also use the model now to
take that data and give you more
information. So, I'm going to ask it um
postgame stats and analysis
left side. That's just the way I
implemented it. And Christine can do the
same thing and say postgame stats and
analysis right side.
>> So, why she does that? You can see
already here um within my widget, I've
loaded up the stats from the previous
game. I lost 37. Our average rally was
four hits. Our longest valley was seven
and I only won about 30% of the shots.
>> And it's I still lost and it's giving me
some tips. I should prioritize defense
in the first return. And that makes
sense because I let a lot of those balls
just go score on the first shot so we
can finish the game um for you know

[00:30]
demoing. Um but that that's context that
it's an understanding and letting me
know that um the way for me to improve
my game is to actually defend those
first hits. Let's see what Christine
gets.
>> Okay. So, I'm writing in the same prompt
on my side and then just clarifying that
I'm on the right side.
And then while this loads, Corey, um
just a quick call out that we're both in
developer mode.
>> Yeah, great question. Um so for me to
have loaded this locally running app, um
you have to enter developer mode, which
allowed me to create an app that I'm we
call it side loading. Um but I'm running
it locally and and having it render uh
rendering within CHBT. Um, so let's look
at your sets. Um, so you don't need to
be in developer mode to use any of the
production apps that are in the app
marketplace. But for this ping-pong app
that I just created, I'm running it
locally and um, we're in development
mode. So yeah, your score now says 73.
Your win rate was 70%. And what it's
it's giving you what you did well,
consistency, balance, exchanges, and to

[00:31]
go even better, you can start mixing
some pace and placement um, to be that
super advanced player. Um,
>> I think this sounds pretty accurate.
>> Yeah. But what's really fun here is we
played on two different computers. You
could play with any of your friends
around the world. I could send somebody
my MCP server and somebody else could
play or this app could be published in
the marketplace, which I will do, and
anybody can play ping pong um here in
CHPT and get some postgame analysis for
um how to play better. So, that's really
fun. So, this is an example of an app
that has some more capabilities, real
time stats, uh, multi- uh, uh, turn
capabilities, and um, you can use codecs
to help you iterate that much faster
getting there. I'm going to stop
sharing, and we're going to go back to
the presentation now.
Okay, so here is where we left off and
you just saw the OpenAI docs MCP server
in action.
And here's a quick recap of what we just

[00:32]
went through.
>> Yeah. So, please check out our
developers.openai.com
apps-
apps-d
site. That's where all the resources to
go deeper, learn more information or you
can just ask codeex to explain that
content for you. Um, part of today's
presentation is not just a walkthrough
of the different resources and tooling,
but kind of the paradigm of how um,
builders build today. It's really really
helpful to use AI particularly codecs to
parse this complicated and technical
information and explain it in a way
that's helpful for you. So you can ask
it about you know how does MCP servers
work? How should I structure my tool
calls? Um how should I think about
building out UI components? How should I
think about enabling full screen? And
you can use it both as a coding tool,
but also a learning um tool as well for
you to be um that much more capable and
building and and just providing things
in the world that are a great
experience.
As well, we have um uh apps that solve a

[00:33]
user problem that stand out. Um so we
haven't touched fully on this yet and
I'll get it in the next few slides, but
part of building an app is not just
building to build, right? it's building
for things that land and it really solve
people's um problems or provide them
with some utility. So I'd really
recommend thinking about how both your
UI your model brings in some contextual
data or how the user's turns in flow
provide a really enriching experience.
Things like postgame analysis, things
like um bringing in live data from an
alltrades platform. Um so yeah, think
about that about how you can really
bring utility into uh an existing flow.
And then last but not least, we talked
about codecs and how to use our docs MCP
server.
>> This is just a quick slide. Um, you saw
Corey do this live, but um, feel free to
take a screenshot so you know exactly
how to do this. Turning on developer
mode and loading in your app so you can
create your own game and play with a
friend.

[00:34]
>> Awesome. Just doing a quick time check
and we have time to now go through best
practices on iterating your app.
I won't go through in great detail all
of these different topics, but I will um
touch upon the UIUX guidelines and a few
other pieces in here, but I'd highly
recommend um to go deeper, go take a
look at um our docs where we have um
information on each of these topics. So
for UX guidelines um some of the things
that I mentioned was um you shouldn't if
you already have an existing app
platform that you've built separately
from chatbt you should be thinking about
how you distill value into the user
experience today and bring something at
the point in time that would provide you
know a delightful experience and less of
let me port over my whole experience add
you know really deep multi-pageenation
and things that just kind of keep you
stuck within that experience. Those are
great, but they're not or sorry, those
are good, but those are not necessarily
what great could look like because I
think the power of an app within CHBT is

[00:35]
the interaction between the model, the
UI, and your MCP server. Um,
awesome. Um, now looking at the
screenshots here, this is just an
example um of a UI guideline. We have a
whole page on this that goes through
like the design principles, but you know
little things like using the right font
size um you know thinking about mobile
um a lot of the traditional things about
uh web development and and native
development um persist as well when
you're thinking about building an app
within CHBT but go read the docs there
for um some more detailed information.
So we have an apps SDK UI component
library that we mentioned at the
beginning of the call. Um, we'll show
the URL for this or you can Google or
use codeex to to search for this. That
is pre-built components to style your
app. You can even tell CEX to, you know,
or you can download uh install that
package and then tell Codex to use those
same components to build your app. Um,
it's a really helpful way to kind of get
your app looking um in a polished state
ready for um app submission.

[00:36]
So just covering some of those UX
principles, extract don't port, treat
chat to PT as a home. Um you know it
owns the overall experience but you have
the ability here to customize it and
make an experience that is uh truly
unique and designed for conversational
entry. Um sometimes the users aren't
always going to be you know as exact as
um they can be and your MCP MCP server
can take that context and decide if it
really wants to uh take action or you
know let the model know that it should
you know ask for more information back.
You have the ability to decide if you
want to act on that intent or you can um
you know provide an experience right
away. So that's I think an important
part of thinking about building a chatbt
app and thinking about the different use
cases and how people decide uh to engage
with our platform and and your app as
well.
And what makes an app valuable? Um, this

[00:37]
is subjective and we're looking for all
the best cases out there, but some of
the things that we have strong
conviction on is at least one thing
better in your app, which it either can
leverage conversation and context,
multi-turn dialogue that um, you know,
you know, you can load an initial UI,
provide some information, but then you
do some refinement um, telling it to
filter or um, take an action on your
behalf. Um and
the three pillars I think you can think
about that is does this help me um know
something more? Um does this help me do
something more um taking action in MCP
or does this show me something um in a
better and more visually engaging way?
So here are some additional resources.
Um we have our GitHub examples. One of
those in particular is kitchen sync
which is a very simple not superstyled
uh chatbt app example but it does

[00:38]
implement all the different windowopeni
capabilities that allow you to do
something within the UI. So it shows you
how you can interact with state, how you
can open up full screen mode, uh picture
and picture um uh open an external link
and then you can take those examples and
implement that in your own app if you
think it's a valuable experience that
you would like to uh do today.
Um I will quickly mention some of the
app patterns here that are buckets of uh
experiences that you may be wondering
how you interact with today. Uh we've
recently enabled um the control of how
your app interacts with memories. Um as
a developer you will never have direct
access to memories. But what the model
will do is sorry when you download a
chatbt app um there will now be a there
is a toggle currently that says for the
user do you want to allow memories uh to
interact with your app? um if they've
enabled it then the model will um like

[00:39]
normal when you're interacting with CHPT
reference those if it's relevant and
then make a tool call to your MCP server
the data won't be passed over but it
will have that context when it when it
makes an interaction uh when it makes an
action and a tool call to your MCP
server they can also disallow it and
then um your app loads in only in the
context that exists within the chat
conversation
for monetization Um we have a couple
different ways of doing this today. Um
one of the you know initial examples is
you can have your app have an
authentication flow. So after the user
installs and connects their app um you
could require them to log into your
platform and then you can monetize by
just having you know your traditional
signup flows and um things of that
nature on your own site. Another more uh
native way to do this is to add in a uh
checkout like experience within your app
or a button that then opens an external

[00:40]
link to your application. And
traditionally uh what we've seen as a
good paradigm is it can deep link people
to like a final state of checking out
and then what we provide actually in the
external checkout uh window. OpenAI
capability is a redirect URL. So after
you've completed that action on your
site or platform, you can natively
direct the user back into chatbt and
continue the experience there. Last but
not least, um the agent commerce
protocol and instant checkout is
something that we are looking to expose
to more apps, developers, and builders.
Um so we are working really hard to get
that so you can actually do native uh
buying experiences directly in app that
don't require a checkout. But today, I'd
recommend um exploring the first two
options as way to adding monetization to
your app because I know it's a topic
that a lot of people are asking about.
All right, let's do a summary of
everything we've covered here today so
far. You should think about building for
the user and the model. Um, there I
think is a very unique opportunity here

[00:41]
to set the paradigms and the best
practices and the best example apps um
for a new way of development. It's not
just your code and a a UI. It's both the
model, your MCP server logic and a web
component. You can iterate faster with
AI tools in just a single prompt. I used
codeex to generate out some scaffolded
code and then had a very basic app and
you can continue iterating and um using
things like our docs MTP server to load
in um all that context in an AI first
manner to start building and iterating.
And then last but not least um utilize
the capabilities that are available. if
it's full screen mode, if it's trying to
do something in real time, um, be
creative and think about what you can
build and I'm really excited to see, you
know, what you all build here in CHBT.
>> Great. Okay, we do have some time for
Q&A. U, we did flag a few, so I
preloaded one. Um, and then we'll just
take some from the chat.
So, first question here, how is OpenAI

[00:42]
compatible with MCP? So, we talked a lot
about MCP today. Yeah, this is a great
question. Um, so I've mentioned MCP in
so many different fashions. Just to
level set, there's the MCP server that
exists for your your your app in CHBT.
We also have our own MCP server, our
docs MCP server that is able to be
loaded in as context um to any different
AI, you know, tool like codeex or within
cursor, VS code, etc. Um but as well um
now thinking about our platform and
tools like our APIs, apps SDK, things of
that nature, those are all compatible
with MCP. So you can load in an M a
different MCP server if it's for flight
data or for um you know uh bespoke
product information, etc. you can load
that into um our platform and tooling um
to build out your own AI experiences
with um you know external uh logic and

[00:43]
capabilities.
>> Um okay, this next question was do you
recommend any tooling to make the local
development experience better?
>> It's a great question. Um
there are many different things here
that you can utilize. Um two off the
back um is you do run a local server,
right? So you have a local server
running your MCP server. You do need to
tunnel that is particularly in de
development mode to um run that within
HBT. So that's a public URL that points
to your local private uh MCP server
that's running on your computer. So I
used Enro. You can also use Cloudflare
to tunnel and it's quick and easy. It's
a single um mpm install and then a
single command to actually create those
tunnels. Um but then when you think
about production, you do need to host
your MCP server somewhere with a URL
that you can um give to chatbt either
for development mode or for the public

[00:44]
app submission flow where we review your
app and then you know load that as the
experience when people connect to your
app um and install it for for the wide
distribution. So there are a number of
different hosting services out there. Um
I would explore those um if you don't
have one of yourself. And for OH, O is a
big topic. Um you can implement OOTH
yourself, but there are great O
providers out there. Um some listed on
our site. And so please explore those
for ways that you can implement O in a
in a more seamless fashion.
>> Um this is one that I just saw come in.
Uh while building the apps, can you use
other colors to make the design more
sophisticated? Are we only limited to
what's in the design system?
>> That's a great question. Um, for the
most part, you have the control and
freedom to design um, as as as you see
fit, both in terms of colors and fonts
and things of that nature. There will be
some things, for example, in our visual
guidelines where we may call out things
that are uh, not allowed, and so I would

[00:45]
review those carefully, but for the most
part, you should be able to build um, a
UI that fits your design. Um the UI
components though currently are um
already pre-styled and so they have
different you know params and controls
to change how they operate but those are
mostly um built in a specific way. Uh
but you you can design your app as
needed and um you know during app review
we'll let people know if anything is um
not particularly fitting well with an
experience um that works well for users
though.
>> Okay. Um, this one I think was when you
were demoing uh the Adobe and Chatbt.
Uh, someone asked, "Do you need an
account with Adobe to use that use the
app?"
>> That's a great question. So, for that
app, I did have to sign in. Um,
when uh I did sign in, they have, you
know, uh, common sign up uh, buttons. So
I think that's a good paradigm is if you
want to create a free user experience

[00:46]
but still have some form of
authentication you can do like you know
the the common providers that provide
signin that allows them to create an
account and then directly get into your
experience but you know as they use your
app and experience they may need to
upgrade their plan etc etc um but there
was a sign-in flow that was required and
I had previously signed in already to to
get the app running
>> but All trails, for example, did not
require me to have a signin and just
talking to their app pulls in that
information and renders the UI, etc.
>> Okay, awesome. Um, I think this one was
already answered. Um, does OpenAI have
any priorities in terms of categories
they want to showcase?
>> Oo, that's a that's a tough question.
Um, we have the existing lifestyle and
production categories in our um app
directory. um we will evolve that over
time but at the moment we haven't um
publicly shared any specific categories
that we are uh featuring um more

[00:47]
prominently. Um but we will build out
more uh specific categories as we uh
start to improve more apps and and
release them out into the ecosystem.
>> Okay. Um I think that is all we have so
far. Um, so we will just wrap up really
quickly
with some resources. Um, so here are
some links. Again, I will send these
out. The first one is the apps SDK. What
makes a great Apache BT app? This was a
whole blog actually written by Corey uh
who's presenting today. So feel free to
check that out as a recap. Um, an
additional resource, the UI guidelines
here where you can answer a lot of the
questions that um, I see in the chat
around UI. um and also link out to our
UI components. And then last but not
least, to build our repo, I did see some
last minute questions come in on this
ping pong app, how you can play, and how
you can actually iterate it and make it
your own. Um so feel free to check it
check it out and um come back for more

[00:48]
build hours. So on February 18th, we
will be talking about prompt caching and
then on February 24th, we will come back
for agent capabilities. So um everything
that you saw today on um the m the docs
mcp server and codecs are actually
applicable to these uh upcoming build
hours as well. So check out our homepage
um and feel free to register and catch
us on demand on our openai YouTube
channel. So thank you again for coming
and we will see you next time.
>> Thanks everyone.

</details>
