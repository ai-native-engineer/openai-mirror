<!-- source: https://developers.openai.com/blog/codex-at-devday/ -->

## Search the blog

![How Codex ran OpenAI DevDay 2025](/images/blog/codex-at-devday.png)

This week we wrapped up our third and largest OpenAI DevDay in San Francisco. The event was the result of the hard work of people across the company. But as we approached DevDay one thing came up again and again in discussions: “I couldn’t have done this without [Codex](/codex)”.

This year was the first DevDay with Codex. We used it in everything that we built: from stage demos (even those not about Codex), to the arcade machines in the community hall, to the products themselves, Codex was a key part of creating DevDay 2025.

Here’s a brief glimpse behind the scenes of a couple of ways that Codex helped us save time, problem solve, multi-task, prioritize, and get organized.

## Controlling cameras and creating a venue lighting MCP

Let’s start with the most obvious project: Romain Huet’s keynote demo of Codex. If you missed it, you can [check it out here](https://www.youtube.com/live/hS1YqcewH0c?si=gw-CPYc-bZ9f0huh&t=2067).

<!-- yt-inline:hS1YqcewH0c -->
[![OpenAI DevDay 2025: Opening Keynote with Sam Altman](https://img.youtube.com/vi/hS1YqcewH0c/hqdefault.jpg)](https://www.youtube.com/watch?v=hS1YqcewH0c)

<details>
<summary>자막: OpenAI DevDay 2025: Opening Keynote with Sam Altman (52:39)</summary>

[00:00]
[Music]
Thank you.
Good morning and welcome to Devday. Thanks for
being here in San Francisco, the city where we
started and where we are committed to building
the future of AI. It's been almost 2 years since
our first Devday. We, but most importantly, all of
you have come a long way since then. Back in 2023,
we had 2 million weekly developers and 100 million
weekly Chacht users. We were processing about 300
million tokens per minute on our API and that
felt like a lot to us at least at the time.

[00:01]
Today 4 million developers have built with open
AI. More than 800 people use chatbt every week
and we process over 6 billion tokens per
minute on the API. Thanks to all of you,
AI has gone from something people build play
with to something people build with every day.
Before we get started with all of today's
announcements, we want to do something fun.
On the screen behind me are the names of
the developers in the room who have built
apps on our platforms that have crossed some
big milestones. 10 billion tokens processed,
100 billion, even 1 trillion. Let's
give them a round of applause.
[Applause] On behalf of all of us at OpenAI,
thank you for doing such incredible work. You
are the ones pushing the future forward and seeing
what you've already done makes us so excited about
what comes next. While it's exciting to celebrate
how far you all have come, we are still so early

[00:02]
on this journey. So today, we're going to focus on
what matters most to you all, which is making it
easier to build with AI. We've been listening to
developers, hearing where you get stuck, what you
want us to build next, so that you can build more
things. And we've got four things for you today.
We're going to show you how we're making it
possible to build apps inside of Chat GBT and
how we can help you get a lot of distribution.
We're going to show you how building agents is
going to be much faster and better. You'll see how
we're making it easier to write software, taking
on the repetitive parts of coding so you can focus
on systems and creativity. And underneath all
of this, we'll give you updates to models and
APIs to support everything you want to build.
We think this is the best time in history to be a
builder. It has never been faster to go from idea
to product. You can really feel the acceleration
at this point. So to get started, let's take a
look at apps inside of chatbt. We want chatbt
to be a great way for people to make progress,

[00:03]
to be more productive, more inventive, to learn
faster, to do whatever they're trying to do in
their lives better. We have been continuously
amazed by the creative ways that people use it.
Since our first dev day, we've been working to try
to figure out how to open up Chachi to developers.
And we've tried things like GPTs. We've adopted
standards like MCPS. And we've made it possible
for developers to connect Chachib to more and more
applications. Some of this stuff has worked, some
of it hasn't, but we've learned a lot along the
way. And today, we're going to open up Chachib for
developers to build real apps inside of Chachibbt.
This will enable a new generation of apps that
are interactive, adaptive, and personalized that
you can chat with. So to build them, today we're
launching the apps SDK, which will be available
in preview starting today. With the apps SDK,
you get the full stack. You can connect your data,
trigger actions, render a fully interactive UI,
and more. The apps SDK is built on MCP. You
get full control over your backend logic and

[00:04]
front-end UI. We've published the standard
so that anyone can integrate the apps SDK.
When you build with the apps SDK, your apps can
reach hundreds of millions of Chat GBT users.
We hope this will be a big deal for helping
developers rapidly scale products. Thank you.
You're welcome. Um, if a user has already
subscribed to your existing product,
they'll be able to log in right from
the conversation. And in the future,
we're going to support many ways to monetize,
including the new Agentic commerce protocol
that offers instant checkout right inside
of Chachibbt. So, let's take a look at a few
examples. When someone's using ChateBT, you'll
be able to find an app by asking for it by name.
For example, you could sketch out a product flow
for chatbt and then say, "Figma, turn the sketch

[00:05]
into a workable diagram." The Figma app will take
over, respond, and complete the action. You can
also then launch Fig Jam from Chachbt if you
want to iterate further. We're also making apps
discoverable right in the conversation. So, when a
user asks for something, we can surface a relevant
app as a recommendation. Maybe a user says they
need a playlist for their party this weekend.
Chachi could then recommend building it in
Spotify. It's an easy way to find the right
app or have the right app presented to you at the
right time. And there will be a whole bunch of
new ways for developers to get discovered.
So now rather than just talk about this,
I'd like to invite Alexi to the stage and we
will show you a live demo. [Music] [Applause]
Hi, I'm Alexi, a software engineer on Chat GBT
working on apps SDK. I'm super excited to showcase
some of the first apps users will be able to
interact with today. The magic of these apps
is combining their rich interactive visuals with
the power of chatbt. Let's start with Corsera.

[00:06]
Let's say I don't spend enough time
thinking about machine learning at
work and I want to learn more. I can
I can ask the Corsera app in chatbt
to help me learn more about this. I can
say Corsera, can you teach me something
about machine learning? Since this is
my first time using Corsera in chatbt,
I'll need to consent to connect. The next time
I use it, I'll be able to dive in immediately.
You'll notice I asked ChatVt for the Corsera
app directly, but chatbt can also suggest apps
if relevant to the conversation. Apps in chatbt
by default are displayed in line and can support
anything that you can render on the web like this
video shown here. Apps SDK also supports picturein
picture or expanding to a full screen layout.
So now that I have my course up, let's play the

[00:07]
video. Playing the video immediately pins it to
the top of my screen, which is really helpful for
something like Corsera because you can access
your conversation while watching the video.
Let's skip ahead a little bit and say I want to
go a little bit deeper on something mentioned
in the video. I can ask chatbt, can you explain
more about what they're saying right now? Apps
SDK provides an API to expose context back to
chatbt from your app, ensuring that the model
always knows about exactly what your user is
interacting with. We're calling it talking
to apps and it's really part of the magic here.
I'm super excited about how learning with chatbt,
one of our top use cases, is continuing to
get better. And with apps and the apps SDK,
you can unlock richer educational experiences for
users around the world. So here, chatbt responded
and explained that the instructor is talking
about data preparation steps before training

[00:08]
a machine learning model. And then it breaks
it down in simple terms for me. I don't need
to explain what I'm seeing in the video.
Chatbt sees it right away. So here I was
able to connect to Corsair's app, discover
and start playing a course and directly
engage with a video through text all within
my existing chatbt conversation. Pretty cool.
Users also love being creative in chatbt. Here I
have a conversation where I've been brainstorming
some ideas to help my younger siblings dog walking
business. We've gone back and forth a few times
and now it's time to make this into a reality. I'm
pretty happy with some of the names here. Uh, so
let's let's take this walk this wag name. And now
I'm going to ask Canva to turn that into a poster.
I can say, Canva, can you make me a poster with
the walk this wag name? I want it to be colorful,
whimsical, bright, and I prefer Oops. I ask
Corsera for a typing course, too, maybe. Um,

[00:09]
I prefer sans sif fonts. Cool. Send that off. And
now in the background, Canva is generating posters
based on the context for my conversation. Canva
is great at creating assets like this. And now
you can kick it off directly from chatbt. Whether
you're making professional marketing assets for
OpenAI or just a fun demo for Devday, Canva is
right there in the conversation as you work.
Apps SDK, as Sam mentioned, is built on MCP,
an open standard we've loved building on at
OpenAI. And if you have an existing MCP, it's
really quick to enhance it with the apps SDK.
All you have to do is add a resource that
returns HTML and the app would be able to
be up everywhere chatbt is distributed across web
and mobile. As you can see, this is a live demo,
so we're experiencing a little bit of latency,
but here we go. Canva has returned four poster

[00:10]
examples to us. We see them in line just like the
Corsera video as well as chatbt kind of explaining
what it's done for us. But we can explore another
modality in apps SDK which is full screen. I click
an asset and the app requests full screen. We're
able to focus on a specific asset and from here
I can see it in more detail. I can ask chatbt
to request changes, maybe visual tweaks just
like with our image generation experience. But
since we're in San Francisco and it's dev day,
let's ask Canva to convert this into a
pitch deck. I can say, "Canva, can you
please make this poster into a pitch deck? We're
trying to raise a seed round for dog walking."
I'll send that off. And since now Canvas is going
to make us a couple of slide decks, it may take a
moment. So, in the interest of time, we'll move
on to show one more demo. While that loads,
say the dog walking business is going really well
and we want to expand to another city. I can ask

[00:11]
chatbt based on our conversations, what would be
a good city to expand the dog walking to? Chatbt
of course knows what we've been talking about.
Super enthusiastically says Pittsburgh. Great.
Now I can invoke the Zillow app to say
please show me some homes for sale there.
And now chatbt is talking to Zillow to
fetch the latest housing data and we'll
get a interactive map embedded in chatbt and
we'll explore how the full screen experience
there goes. So we have our map gorgeous loading
state and boom we have a bunch of homes here.
It also looks like our slide decks are done. So,
we'll go back to those in a moment. But this map
is a little hard to see in the inline view. So, I
can click a specific home and open it full screen.

[00:12]
And now we have most of the Zillow experience
embedded in ChatBt. You can request a tour.
All the actions that you would expect from Zillow.
But we have a lot of options here and it's kind of
hard to parse. So I can ask chatbt, can you filter
this to just be threebedroom homes with a yard for
the dog? Of course, chatbt will talk to Zillow
again. And because the app is in full screen,
it can now just update the data that's provided
to it without needing to create a new instance. We
see chatbt came back. We get the message overlay
here. If I click that, I can view my conversation
over the Zello app and even open it to the full
height. Cool. Let's zoom in and find a specific
home we may be interested in. Now, because the
Zillow app is exposing context back to CHBT,
it knows what I'm looking at. I can ask for more
information about this home, like how close is
this to a dog park. Chatbt is able to compose
the context from Zillow with other tools at its

[00:13]
disposal, like search. So, it's able to give
more information about this home. From here,
I could invoke other Zillow tools, maybe find out
the affordability of it, but it'll provide the
best answer every time. This is a great example
of how dynamic an experience with apps SDK can
be. This all started from an inline map, and now
we're able to go back and forth between talking
to the app, asking Chatbt questions, or just
using the Zillow experience. Let's check back
in on those slide decks. So, if I pop back over
into this conversation, see Canva has given us a
few options here. Like the look of this blue. So,
if we open that up, we now see the slides in full
screen and I can see all the beautiful slides that
Canva has generated for me. When I'm ready, I can
just like the posters, I could ask for
follow-up edits. And when I'm ready,

[00:14]
I can open this in Canva to get the
real slides out. and hopefully close
the seed round. So there it is. The magic
of apps and chatbt conversations that unite
the intelligence of chatbt with your favorite
products resulting in truly novel experiences.
I'm so excited to keep building this with all of
you. Can't wait to see what you do with it. Now
back to Sam for more on apps. That was awesome.
Thanks Lexi. That was great. It's very hard to
type and talk in front of a bunch of people at
the same time. So, you did very well. Uh we're
excited for you to try out the apps that you saw
in the demos along with a few more from these
launch partners. They'll be available in chatbt
today and this is just the beginning. We're going
to roll out more apps from partners in the weeks
ahead. For developers, the apps SDK is available
in preview to start building with today.
Our goal is to get this in your hands early,
hear your feedback, build it together with you,
and then later this year, developers will be able

[00:15]
to submit apps for review and publication. We'll
also release a directory that users can browse
in addition to discovery and conversation. Any
apps that meet the standards provided in our
developer guidelines will be eligible to be
listed. Apps that meet higher standards for
design and functionality will get featured
more prominently, including in the directory
and suggested as apps and conversations. We've
published a draft of the developer guidelines
along with the apps SDK so you'll know what to
expect and we'll share more and monetization from
apps soon. We'd also love your feedback about what
you'd want. This should be an exciting new chapter
for developers and for chatbt users. So that was
apps and we hope everyone loves it. Thank you.
So next we want to talk about building agents
and how we're going to make this simpler and
more effective. AI has moved in the last
couple of years from systems that you can
ask anything to to systems that you can ask to
do anything for you. And we're starting to see

[00:16]
this through agents software that can take
on tasks with context tools and trust. But
for all the excitement around agents and all
the potential, very few are actually making
it into production and into major use. It's hard
to know where to start, what frameworks to use,
and there's a lot of work. There's orchestration,
eval loops, connecting tools, building a good UI,
and each of these layers adds a lot of
complexity before you know what's really
going to work. Clearly, there's a ton of
energy and the opportunity is very real. So,
we've talked to thousands of teams, many of them
in this room, who are building agents to reimagine
how work gets done. And we're we've asked what
we can do to make agents much easier to build.
So today we're going to launch something to help
with that. The goal here is something for every
builder that wants to go from idea to agent faster
and easier. So we're excited to introduce a new
thing called agent kit. Agent kit is a complete
set of building blocks available in the OpenAI
platform designed to help you take agents from
prototype to production. It is everything you

[00:17]
need to build, deploy, and optimize agentic
workflows with way less friction. Our hope is
that everyone from individual developers to large
enterprises will get a lot of value from this and
we'll talk about a few of the core capabilities
now. So the first one is agent builder. This is a
canvas to build agents. It's a fast visual way
to design the logic steps, test the flows and
ship ideas. It's built on top of the responses API
that hundreds of thousands of developers already
use. So most of you who have used our platform
before should be familiar with the foundation.
The second thing is chat kit. We've heard this
one loud and clear and we're making it easy to
bring great chat experiences right into your own
apps. You get a simple embeddible chat interface
that you can make your own. You can bring your own
brand, your own workflows, whatever makes your own
product unique. And you can see in the video here
how chat can work across each agent node and call
on tools to form the best response. And then
finally, evals for agents. We're shipping new

[00:18]
features dedicated to measuring the performance
of agents. You get trace grading to help you
understand agent decision step by step. You get
data sets so you can assess individual agent
nodes. You get automated prompt optimization. And
you can even now run emails on external models
directly from the OpenAI platform. This is all the
stuff that we wished we had when we were trying
to build our first agents. And of course, agents
need access to data. So with OpenAI's connector
registry, you can securely connect agents to your
internal tools and third party systems through an
admin control panel while keeping everything
safe and under your control. So let's look at
a couple of examples. Albertson's runs over 2,000
grocery stores across the US. More than 37 million
people shop there each week. And each store is
like its own little economy. Managers have to
make all these constant decisions, you know,
tweaking this promotion or that product mix.
resetting the displays, working with a bunch of
vendors. It's like a lot of stuff. So, Albertson's

[00:19]
built an agent using agent kit. So, now imagine
a situation where sales are unexpectedly down for
ice cream, down 32%. Uh before this would have
kicked off a long process of reporting. There'd
be spreadsheets and meetings, a lot of panic,
they sell a lot of ice cream, very important
to them. Um now, an associate can just ask the
agent what's going on. The agent will look at
the full context of everything it can discover,
seasonality, historical trends, external factors,
and it'll give a recommendation. Maybe it's time
to adjust the display or to run a local ad. So,
let's take a look at another agent. HubSpot is a
customer platform used by hundreds of thousands of
organizations around the world. And they used
agent kit to improve the responses of Breeze,
their AI tool, using the custom responses widget.
So in this example, a HubSpot customer called Luma
Plants gets a question about why a plant is not
doing so well in Arizona. It then uses the Breeze
assistant to search its own knowledge base, look
up local treatments for the state's low humidity,

[00:20]
pulls in policy details, and puts everything
together. It then offers multiple ideas and
a recommendation. So this is how we imagine
intelligence working across many different
sources, all operating together to deliver
smart, useful answers to customers. And
it's a great example of the thing that you can
build with agent kit. We have a bunch of great
agent launch partners that have already scaled
agents using agent kit and it's available to
everyone starting today. So let's do a live
demo and I will pass it off to Christina.
Thanks Sam. Hi everyone. I'm Christina and I
work on the team building agent kit. Today I
want to show you how Agent Kit helps developers
create agents faster than ever before. So you may
have already seen our Devday website. It's the
site here that all of you have access to and has
everything about today's schedule. But right now
it's just a static page. What if it could actually

[00:21]
help you navigate the day and point you to the
sessions that are most relevant to you? We're
open AI. We need to have AI in our Devday website.
So that's what we're going to build together. an
agent powered by agent kit deployed right here
inside this site. And to make this interesting,
I'm going to give myself eight minutes to build
and ship an agent right here in front of you.
You just heard how hard it is to build an
agent. So, this is going to be a bit of a
challenge. And I'm going to start the clock now
to keep me honest. We have a clock going. So,
I'm starting in the workflow builder in the OpenAI
platform. And instead of starting with code, we
can actually wire nodes up visually. Agent Builder
helps you model really complex workflows in an
easy and visual way using the common patterns um
that we've learned from building agents ourselves.
So here on the left, we've already extracted
the common building blocks. For example,
tools like file search and MCP, guard rails,
human in the loop, and other logical nodes. Today,

[00:22]
I'm planning on building a workflow that uses two
specialized agents. The first will be a sessions
agent which will return information about the
schedule and the second will be a more generic
devay information agent. So I'm starting off with
a categorizing agent to just help route um and
categorize the type of message coming in whether
it's asking about a specific session or something
more generic. And then I've added in an if else
node to route behavior based on that classifier.
Next I'll create the session agent. Here I'll drag
and drop um an agent node. I'll call this session
agent. I'll give it the context um about kind of
grabbing information about a session. And then I
can add in various tools here. Today I already
have um a doc with all the information about
sessions. So I'll simply drop that in. Let's call
this sessions and attach it. So this agent now has
all the information needed to answer my questions.
Um but showing the schedule should also be fun
and visually interesting, not just plain text. So,
I'll also create a widget for them. I'll head over

[00:23]
to our widget builder. Um, here I could create a
widget from scratch. I can browse the gallery to
learn about other widgets and reuse them. But for
today, I've actually already designed a widget for
this use case. In this case, it's an onboarding
session widget for Fro, one of our Devday friends
that you'll see around the venue who's holding a
101 onboarding session um in Golden Gate Park. So,
we can simply download this and then head back
over to our uh to our agent and just attach it in
as I don't think I clicked download. So, let me
go back and actually click the button download.
There we go. Great. So, head over and attach it
as an output format for the sessions agent that
we just created. Drop that in. We can preview
it to make sure we added in the right widget
and everything looks ready to go. So this session
agent is now done. Um next I'll create the general

[00:24]
dev day agent. So once again I'll drag in an agent
node. Let's call this the dev day agent. We'll
once again give it some context about what it's
doing. Um and then we'll also make it speak in
the style of froge just to make it really on brand
with the day. Um we'll add in a file once again.
So, we have a file with all of the information
about the day. Call this dev day. Attach it. This
agent is ready to go as well. And we'll attach
that here. Now, it looks like I have a couple
more minutes. So, let's add in some additional
security with one of the pre-built guardrails. So,
one of the most important things when building
agents is being able to trust them. And guardrails
help you have that confidence, protecting
against hallucinations, adding moderation,
blocking PII. In this case, we already have um a
couple pre-built guardrails. I'll turn one on for
a PII and then I'll just include name as well so
I can easily verify its behavior. I'll attach this

[00:25]
in to the beginning of the workflow to make sure
Froge is really protected against PII. And then
I'll add in an additional agent to handle cases
when um this information is passed in. So again,
I'll make it speak in the style of froze to
stay consistent and I'll remind it that um it
cannot help with questions that contain sensitive
information and remove kind of the context. Um
great. So I think this workflow is ready to go.
I can also configure um the output to determine
what shows up to the end user. In this case, I I
can also turn off um file search sources if that
is kind of more internal. Um and I think that's
it. Let's test it out. I can preview this directly
from um our agent builder. So here I can ask what
session to attend to learn about building agents.
And I can see this message moving its way through
that workflow we just created. Checking guardrail,
categorizing intent, pulling information from
the file of sessions that I just added in. Um,

[00:26]
finding the right session, using the widget
that I added. Um, and determining, you know,
orchestrating agents at scale at 11:15 with James
and Rohan is like the best session for me to go
to to learn more about this. Um, and then I
see a couple ribbits because this is this is
actually Fro talking to me and and ribbiting at
me. So, okay, I think this agent looks good. need
need to watch the time. Um, so we just built a few
specialized agents using tools. We added in guard
rails. We customized them using some widgets and
then we also tested out the workflow in preview.
The one thing we haven't yet done is a full set
of evals. And we can also do that directly from
the agent builder um to make sure that everything
behaves exactly as expected before going live. Um,
but right now I've got a giant clock chasing me
and devday is waiting. So let's publish this. Um,
hit publish here. Let's call this ask froge.
Hit publish. Um, and I now have a fully
deployed published agent in production with a
workflow ID that I could use to run directly

[00:27]
on the right. On the right, we also have code
export in case I want to run this in my own
environment, in my own servers. But you can see
this is this is quite a bit of code to write.
And so I'm just going to stick with using the
workflow ID that we just created and then head
over to my site. So here in my Dubday site, I'm
first going to create a chatkit session using
um the the workflow that we just created. I'll
simply drop in that workflow um ID. I'll add in
the chatkit react component using that client
secret that we just created in our own server.
And then adding in visual customization as well to
again make this really froze themed. In this case,
it's going to be called ask froge. It's
going to continue to rivet in the placeholder
um and it'll have some froze specific colors
and starter prompts. I'll add this froze chat
um in a bottom sheet so it'll come up from
the bottom of the page. And then finally,
I'll add in a link to ask froge at the top
of the site um so that it's really front and

[00:28]
center on our website. So let's go back to our
site. There it is. Ask froge top of the site.
Let's try it out. So, what session to attend
to learn about building agents? And again,
this is running through that exact same workflow
we just created, checking for guardrails,
categorizing the message, pulling from tools from
file search, using the widget that we designed,
and then again deciding orchestrating agents at
scale is the right um session for me to go to
and and continuing to rivet in this style
approach. So, okay, great. We've done it.
The agent is ready. We can stop the clock. The
agent is ready with uh 49 seconds to spare. Um
and I can keep iterating on this agent directly
in the um in the visual builder and also deploy
these changes directly to my site without making
any code changes at all. This includes adding new

[00:29]
tools, um, adding new widgets for other use cases,
adding new guardrails, and I can even wire it up
to client side tools to take actions directly
in my website. Um, so in just a few minutes,
we've designed an agent workflow visually. We
added in some tools and widgets. We previewed it,
we deployed it, we tested it, and now you all
can use it. This is actually live now in your
Devday site. um you can tap your badge and you
should be able to to see it and use it and um
find the sessions that are best for you. So we're
looking forward to using it and meeting Frozeing
all the new experiences that you'll now be able
to build using agent kit. Thanks and back to Sam.
Thank you Christina. I think that's so cool. I
can't wait to see what you'll all build with it.
So, we've looked at AI apps, agents, uh, but
now let's shift to one more thing that's just as
important. How we write software. One of the most
exciting things happening with AI is that we're

[00:30]
entering a new era with that changes how software
gets written. Anyone with an idea can build
apps for themselves, their families, or their
communities. And before we talk about codeex,
we want to show you a few examples. In Japan, an
89year-old retiree taught himself to code with
the help of Chachi BT. He's now built 11 iPhone
apps for elderly users. He's turning a lifetime
of wisdom into tools that help others live
more independently. In Spain, Pal Garcia and
members of domestic data streamers are helping
people reconnect with memories using ChachiBT,
image generation, and Sora. At ASU, med students
needed a better way to practice the kinds of
difficult human conversations they'll have as
doctors. So, they built a virtual patient app
with our models where they can try, fail, and
get better before they step into a real exam
room. And at Versailles in France, visitors can
now walk the palace and talk to it. They built

[00:31]
an experience where you have a live discussion
with art and sculptures with our real-time API.
History becomes a conversation. It's awesome
to see what people are building and this is why
we're so excited to give developers even more
tools to build faster. So earlier this year,
we launched a research preview of Codex, OpenAI's
software engineering agent built to work alongside
developers and speed up how software gets created.
Since then, Codex has become very loved and grown
into a much more capable collaborator. It
works everywhere you code now. your IDE,
the terminal, GitHub, and in the cloud. Your
chat GBT account connects everything so you
can move your work seamlessly between your tools.
We've released a ton of new features for Codeex,
and it now runs on the new GPT5 codeex model,
a version of GPT5 purposely trained for codeex
and Aenta coding. This model is better at
tasks like code refactoring and code review,

[00:32]
and it can dynamically adjust its thinking time
for the complexity of the task. Developers love
this new model and the codec usage has gone up
really fast. One of our key metrics for looking
at this is daily messages. The number of tasks
and conversations that developers have with codecs
each day. Since early August, daily messages are
up 10x across codecs. And this rapid usage has
also helped GPT5 codeex become one of our fastest
growing models ever. Since its release, we have
served over 40 trillion tokens from the model.
Internally at this point, Codeex is everywhere we
build. Almost all new code written at OpenAI today
is written by Codex users. Our engineers that use
Codex complete 70% more pull requests each week.
And nearly every OpenAI PR goes through a Codex
review. And from that, people get more depth than
they'd expect, even from a very senior engineer.
Starting today, Codex is officially out of
research preview and into G. And while Thank you,

[00:33]
And while Codeex already has a lot of
traction with individual developers,
today we're introducing a new set of features to
make Codeex more helpful for engineering teams.
First, we have a Slack integration. This has
been very much requested so that you can ask
codecs to write code or answer questions directly
from team conversations in Slack. Second, a new
codec SDK so that you can extend and automate
codecs in your team's own workflows. And third,
new admin tools and reporting, including
environment controls, monitoring, analytics,
dashboards, and more so that enterprises
can better manage codecs. Expect to see a
lot more codec improvements coming soon. One
of the things that's been really inspiring
to us is to see the breadth of people using
codecs. From developers building side project
on weekends to high growth startups to big
global enterprises, Cisco rolled out codecs

[00:34]
across its entire engineering or they're now able
to get through code reviews 50% faster and have
reduced the average project timeline from weeks
to days. So for our next demo, we want to show
you something fun. We're going to show you how
can you can use the new codecs and our APIs to
turn anything around you into workable software.
And for that, please welcome Raman to the stage.
Good morning, everyone. Last year, we built an
iPhone app from scratch, and we even programmed
a mini drone live on stage using 01, our first
reasoning model. It was kind of vibe coding
before we even had a name for it, frankly. But
the progress since has been incredible. Codex
is now a teammate that understands your context.
It works alongside you and it can reliably take
on work for your team. And we thought about how do
we best show you all of the cool things that Codex
can now do. We had a lot of ideas, but one that we
kind of kept coming back to is what about building
something that we could all experience and see
together here in this room right now. So that's

[00:35]
our challenge. If you look up here, some of you
might notice a camera that's mounting above the
stage. And I thought maybe we could start there.
And so earlier I asked Codex CLI to create a very
simple control panel interface with a very like
simple interface. See a camera feed on the left,
some buttons on the right. And if we can bring
my laptop on screen, you'll see what uh what
Codex came up with. Initially did it really well,
but then I also added the Figma branding from the
dev day event so it could pull the exact colors
and components to actually render it perfectly
matching our design. Great. So that's our place
to get started. Now I haven't written a single
line of code, but let's dive in and see what we
can do on top of that. Now switching over here to
uh we're going to skip this version. Skipping over
here to my terminal uh which wanted to update uh
I'm sure you uh you can see like we have Codex
CLI. It's logged in with my chat GPT account and

[00:36]
it's powered by GPT5 codeex our net new model
that Sam mentioned. Now, let's start by asking
this question that I'm sure many of you have not
asked a coding agent before. How to control a Sony
FR7 camera in Node. And honestly, I did not know
how to get started. I saw there was a C++ SDK and
I thought maybe like Codex, we want to use that
and turn it into JavaScript. But then it had a
much better idea than that. Uh I realized that
there's a Visca protocol apparently to control
these cameras. So, you know, as you can see, Codex
can respond pretty fast for questions like this.
And this all seemed promising to me. So basically
I went ahead and I typed this script over to Codex
to completely scaffold an integration using
the Visca protocol and wire it up to that uh
control panel. Now Codex is becoming harder and
harder to demo by the way because it can really
work tirelessly on your task. I've seen it work
for up to seven hours on a very big refactoring
for instance and get it right which is pretty
outstanding. here. If I we switch over and if

[00:37]
we scroll back up, you know, it updated its plan
along the way, wrote a lot of code and everything.
And this was the final result. As you can see on
the screen, it worked for over 13 minutes on that
one task, but it did everything I wanted it to do.
So, let's take a closer look. If I jump over to
VS Code now, you can see on the right side of the
screen, we also have our Codex integration in the
ID. And these are the files that the Codeex CLI
came up with for the camera control. So you can
see it built a node server. It also figured
out all of the UDP packets to send to this
camera. Imagine the time it would have taken me to
actually learn this protocol that's over 30 years
old by the way. Codeex even figured out that there
was like some very specific headers to to send for
this particular camera. All right. So with uh this
UI components now wired up the servers running. So
we can uh take a quick look and try this. So here
if I turn on the camera. There we go. We have the

[00:38]
camera. That's all of you. Awesome. And let's try
the controls. Boom. I can actually control the
camera now from this interface. It's pretty cool.
All right. But controlling with buttons is nice,
but I think we can do something better. So
I'm going to try to send uh another task, but
live this time inside our ID extension. So check
this out. wire up an Xbox wireless controller to
control the camera. So, I'm going to send this one
right now. I was uh backstage earlier and I found
this Xbox controller. I wasn't sure who's playing
back there, but I thought this could be something
we could try. Uh so, we're going to leave it here.
And as you can see now, like Codeex made a plan.
Apparently, three tasks have to be completed. It's
now exploring the file. It's figuring out how to
wire up this game pad. And what's interesting here
is you can see in the ID we also have this concept
of auto context. And what that means is that your
prompts can be pretty short because codeex will

[00:39]
kind of understand your intent. It will see like
the the recent files that you've used and really
kind of adjust accordingly. So as you can see
we're now at task number two. This one will
probably take another minute or so. So we'll leave
it run in the background. So in the meantime, what
else could we do? Well, I thought one exciting
interface is voice. So, to save us a few minutes,
I've already asked Codeex to integrate with our
real-time API and our agents SDK, and I wanted
to wire up all of this into the app right here on
this green little dot at the bottom right of the
screen. But what's great about the real-time API
is that it brings natural speech to speech into
your app, but it also connects to any MCP server
in the context of that conversation. And so that
really got me thinking, what else could we show
you in this room and turn into an MCP server? And
then I thought, wait, we have a lighting system.
So maybe we could wire up the lighting system of
the venue over to an MCP server. So let me check
out this task that I sent to Codex, but this time

[00:40]
in CEX cloud. So you can see here my prompt. I
asked Codex to uh, you know, wire up this MCP
server for this very specific model of lighting
system. I gave it like the the reference docs that
I found and I gave it the exact interface that
I wanted to have for my UI to work. But what's
fascinating to me is like if you look at the
logs for instance like that's really the magic of
uh the agentic behavior of codeex like I could
have asked a teammate to do that but because the
task was very specific now codeex is my teammate
and if you look at how it went through the process
it actually figured at some point that it needed
to kind of find new information about command 8 to
move forward. So then he went ahead to fetch the
GitHub docs again to kind of really like operate
and call tools along the way. And that's really
the magic of GPT5 codeex. You can really let it
go off do some complex tasks and and you'll see
this like aentic behavior emerge. And then after

[00:41]
that I did one more turn to actually ask Codex
to like include the read me information so I can
understand how to run it. And sure enough here
is my MCP server. Now going back to uh VS Code.
What's also very interesting sounds like the Xbox
task just finished. We'll see that in a moment.
Awesome. Uh and now going back here, you can
see that you have uh all of your local but also
your cloud tasks right here inside uh the VS Code
extension. So if I click on the build MCP server
for instance, this is the task I just showed you
uh on uh Codeexcloud. And here I can actually
apply all of the changes locally if I want to test
them. So I can just go ahead and click apply. And
now all of the changes with this MCP server are
now included locally. Now I didn't want to watch
you uh I didn't want to let you watch me do npm
install here on stage. So I just took that MCP
server already and I started to install all of
the dependencies to make it run. So let's now
put all of that to the test. But first of all, if
we go back to our app right here, let's see if we
can actually control this camera now with this
Xbox controller. There we go. It works. That's

[00:42]
pretty awesome. What's funny is like I didn't even
specify to codeex which button should do what,
but it figured that the joystick was probably a
good idea. So that's that's actually perfect. But
let's uh do the real test now. Let's enter voice
mode and see uh what happens. So sorry in advance
AV team, but we'll try to see if Codex figured
this out uh to control the lights. Hi there.
Hello.
Hi there. I can hear you loud and clear.
Let me know what you need. Yeah. What do
you see on the camera? I see a large
audience in front of you with rows of
attendees seated and ready. The room is
well lit and the crowd stretches far back
filling the space. That's right. Could you
uh shine the lights towards the audience?

[00:43]
There we go. Oh, I've just lit up
the audience with a nice bright
wash. They should be perfectly highlighted now.
Can you uh greet everyone here in the room
now? Absolutely. The audience lights are
up. Let's welcome this fantastic crowd.
Hello, amazing developers at Fort Mason.
We are so excited to have you here for an
incredible day. Awesome. Could you now do
something fun with the lights and say hi
to people tuning in on the live stream?
We've got the fun lights rolling now. Some
dynamic colorful effects in motion. And to
everyone watching the live stream, thanks for
joining us. This is going to be an amazing
experience. Cool. All right, let's go back
to normal now. Awesome. So, I still have not
written a single line of code, by the way, to make
this happen. But there's one more thing I wanted

[00:44]
to show you. Last but not least, Sam mentioned
that we're launching a Codex SDK today. And so,
I wanted to finish up with something that gives
you a little bit of a glimpse into what might
be the future of software engineering. So,
let me go back into voice mode and try this.
Hi, could you ask Codeex to show a credits
overlay like at the end of the movie,
but this time the cast is all FD attendees?
I'm running that with codeex now. I'll
let you know when it's ready. Great. Um,
in the meantime, could you start a
countdown and take a photo of all of us?
Oh, and there we go.

[00:45]
So, to explain you what just happened here,
when I sent uh a task to the voice agent,
it also added codeex SDK as a tool. And what that
means is that now on the fly I can reprogram this
app in real time and instantly adapt it to user
needs or any kind of feedback they have. So in
this case when I asked to create a credits
overlay it was able to go ahead and edit the
code inside this React app reloaded find what it
needed to complete the task and now the credits
are rolling. It's pretty amazing. So with
all that we took voice, we took a sketch,
we took some devices around us and we turned all
of this into workable software and all of that
without writing a single line of code by hand. So
really give Codex your most ambitious ideas. Give
Codex your most complex coding problems and
see what happens. I think you'll be as amazed
as we are every day. The only limit now is your
imagination. Thank you so much. Back to you, Sam.

[00:46]
Thanks Raman. Uh this is the biggest change to
how software gets created that I have ever seen
and we can't wait to see what you all will
do with it. I think the future is going to
be very bright. We've covered a lot today but
obviously models matter a lot too. So I want
to share a few model updates. Back in August
we launched GBT5. We trained it to be really
good at steering agents and endto-end
coding and GPT5 has delivered on that.
Leading coding startups like Cursor,
Windsurf, and Verscell are using GPT5
to change how software gets written and
ship in their apps. And then after that,
we released GPT5 Pro, the most intelligent model
that we've ever shipped. Today, we're launching
GPT5 Pro in the API. It's available to
all developers, and we hope you enjoy.
GPT5 Pro is great for assisting with
really hard tasks, domains like finance,

[00:47]
legal, healthcare, and much more where you
need high accuracy and depth of reasoning.
version of the advanced voice model we shipped
two months ago with the same voice quality
and expressiveness. Personally, I think
that voice is going to become one of the
primary ways that people interact with AI. And
this is a big leap towards that reality. Now,
I want to shift gears and talk
about what's new for creators. Uh,
and this has been a hotly requested
one, so we hope you'll like it. Uh,
we've been seeing incredible work from filmmakers,
designers, game developers, educators, and more
using AI as part of their creative process. Today,
we're releasing a preview of Sora 2 in the API.
You now have access to the same model that powers
Sora 2's stunning video outputs right in your own
app. One of the biggest jumps that we've made
with this model is how controllable it is.

[00:48]
You can give it detailed instructions
and it holds onto the state while
delivering results that feel stylized,
accurate, and composed. For example,
you can take the iPhone view and prompt Sora to
expand it into a sweeping cinematic wideshot.
But one of the most exciting things that we've
been working on is how well this new model can
pair sound with visuals. Not just speech, but rich
soundscapes, ambient audio, synchronized effects
that are grounded in what you're seeing.
So, here's an example in this kayak video.
You can also bring pieces of the
real world into Sora 2. For example,
you could take a picture of your dog and give
your dog some new friends. Look who's coming,
buddy. Here they all are. Good pups. Come on.
That's it. Everybody together. Happy dogs.

[00:49]
So, Sor Sora 2 is also great for concept
development. You can just describe a
general vibe or a product and Sora will
give you a visual starting point. So,
here we're going to use it to generate
concepts for an e-commerce ad. When your
new place feels like a blank canvas, find the
pieces that make it yours. Browse, customize,
and check out in minutes. Delivered fast to
your door. People seem to love Sora 2. It's
been on the top of the app store since we've
launched it and the creativity that people are
demonstrating has been super fun for us to watch.
We hope that now with Sora 2 preview in the API,
you will generate the same high-quality videos
directly inside your products complete with the
realistic and synchronized sound and find all
sorts of great new things to build. Just like
our other modalities, it's built for flexibility.
You get to control video length, aspect ratio,
resolution, easily remix videos. Mattel has
been a great partner working with us to test

[00:50]
Sora 2 in the API and seeing what they can do
to bring product ideas to life more quickly. So,
one of their designers can now start with a
sketch and then turn these early concepts into
something that you can see and share and react
to. So, let's take a look at how this works.
[Music] [Applause]
That that is a very cool new way to build toys.
Uh and it's incredible to watch with AI how fast
ideas can turn into sharable, workable designs.
So, we're excited to see what else you'll come
up with as you use Sor 2 in your own products.
We hope that today gave you a few ideas of new

[00:51]
things to build. We want OpenAI to be a great
platform for this new era of building. We think
things are going to get pretty incredible
pretty soon. All of our announcements today
are aimed to support you in this work. The apps
SDK for building native apps inside of Chat GPT.
Agent kit so you can deploy agents wherever
you'd like easily and with more confidence.
a more powerful codeex changing the way software
gets written helping your team ship faster and new
models in the API GPT5 Pro Sora 2 and Realtime
Mini that expand what's possible we're watching
something significant happen I think software
used to take months or years to build you saw
that it can take minutes now to build with AI you
don't need a huge team you need a good idea and
you can just sort of bring it to reality faster
than ever for. So, thank you all for being here
and thank you for building. Our goal, one second,
I'm almost done. Uh, our goal is to make AI useful

[00:52]
for everyone. And that goal won't happen without
all of you. So, we're very grateful that you're
here to build with us. And also a huge thanks
to the team that made today possible. A huge
amount of work went into this. And there's a
lot more work. There's a lot more happening
throughout the day. So, enjoy the sessions
and we'll see you later. Thank you very much.
[Music]

</details>


As Romain mentioned, everything you see in this demo beyond using our [Realtime agents starter app](https://github.com/openai/openai-agents-js/tree/main/examples/realtime-next) was built by Codex.

The demo actually started with the idea of wanting to show how Realtime was controlling the camera and lights in the audience. But as Romain started digging into this project, he faced the challenge of programmatically controlling the camera and lights.

Codex was able to figure out a solution to control the network enabled camera using the VISCA protocol (a protocol from the early 90s!), implement the protocol entirely on its own, and even go ahead and build an MCP server to control the protocol of the lights.

Using the [Codex CLI](/codex/cli), Romain was able to work on both problems in parallel and have an initial version up and running in an afternoon without having to touch the keyboard–avoiding what would have otherwise been an extensive research and hacking session.

## Bringing the beats

One of the big launches at DevDay was the [Apps SDK](https://developers.openai.com/apps-sdk), which lets you build rich app experiences directly within ChatGPT. For Katia Gil Guzman’s Developer State of the Union demo, the idea was to build on the light MCP server that Codex had built for Romain and have a rich beat pad interface.

This meant building a visually pleasing interface that was also functionally working, including handling the connection with the lights MCP server to control the lights and allow for it to play different instruments.

Thanks to [Codex Cloud](/codex/cloud) and best-of-N, Katia was able to not only get a functional app out quickly, but iterate on multiple different designs in parallel. She tried out everything from more futuristic modern looks to more OpenAI DevDay branded UIs and even experimented with different features, all without wasting time and effort.

![A picture of Katia on stage at DevDay 2025 with the beatpad demo running in the background](/images/blog/codex-at-devday/beatpad-demo.jpg)

## Multi-tasking game design

If you wandered the hallways of DevDay, you might have seen ArcadeGPT, two arcade cabinets that let you customize your own video game by remixing a collection of existing video games using GPT-5.

As Kevin Whinnery started building the foundation, he needed a range of starting games for GPT-5 to remix–and he needed them fast. To create and iterate on them quickly, he had seven (!!) different terminals open, each with an instance of Codex CLI working on one single-file Phaser game implementation.

Thanks to Codex CLI, he could iterate on each of the games asynchronously, testing them all at the same time to provide attendees with a wide range of games to play and remix.

![A screenshot of the ArcadeGPT title screen](/images/blog/codex-at-devday/arcadegpt1.png)

![A screenshot of the ArcadeGPT game generation screen showing both the prompt, code that's being generated and a tetris game to play while waiting](/images/blog/codex-at-devday/arcadegpt2.png)

![A screenshot of one of the games generated by Codex](/images/blog/codex-at-devday/arcadegpt3.png)

## Rebuilding demo apps

Personally, I used Codex for basically every task leading up to DevDay. It’s hard to cover every single moment that I felt grateful for Codex, but one stood out.

I had been working on the fine-tuning demo for my [Open Models talk](https://www.youtube.com/watch?v=1HL2YHRj270) and used Streamlit for all of it. But the Streamlit app felt convoluted, was hard to grasp for the audience, and had some behavioral bugs that weren’t easy to fix. After taking some screenshots and creating a quick initial design using v0, I downloaded the mock [Next.js](https://nextjs.org) app and put the Codex IDE extension to work.

<!-- yt-inline:1HL2YHRj270 -->
[![Building with Open Models](https://img.youtube.com/vi/1HL2YHRj270/hqdefault.jpg)](https://www.youtube.com/watch?v=1HL2YHRj270)

<details>
<summary>자막: Building with Open Models (22:37)</summary>

[00:00]
Good afternoon everyone. My name is
Dominic Kundal and I work on developer
experience here at OpenAI. Before we get
started, a quick raise of hands. How
many of you are using a combination of
open and proprietary models?
All right, that's quite a lot. How many
of you are using or have used GPOSS
before?
All right, that's uh more than I
expected, but hopefully we can get it to
100% at the end of the talk. Um, so over
the next 25 minutes, we'll talk about
GPTOSS, our latest open model series
that we released in August earlier this
year. Uh, why you might want to use them
and how they fit into the broader OpenAI
ecosystem.
But first, what is GPOSS? GPTOSS is our
model family consisting of two models.
GPOSS 20B, our medium-sized model that
can run on higherend consumer hardware
with at least 16 GB of VRAM. So, a

[00:01]
top-of-the-line consumer graphics card
or recent mid-tier MacBook. And then
GPUs 12B, our larger model that can run
on a single 80 GB GPU like an Nvidia
H100 or an AMD Mi300X or even a
top-of-the-line MacBook like this 128 GB
MacBook Pro.
But why did we build these models? Well,
first of all, because you all kept
asking us to.
But uh joking aside, we know that
proprietary hosted models aren't always
an option for you. Whether you have data
requirements where your data needs to
stay on premise for safety or privacy
reasons or you have specific hardware
requirements where your data needs to uh
stay on or you have specific hardware
requirements or latency requirements or
maybe your use case is has to run
completely offline because of flaky or
non-existent internet connections.
There's a wide range of reasons why you
might want to pick an open model and we
know that a lot of you already have to

[00:02]
deal with that mix of proprietary and
open models for your use cases. Because
of that, we wanted to make sure that we
offer you the best possible experience.
Both of the open models are reasoning
models with variable levels of reasoning
and raw chain of thought access. And
they're the only open models that can
perform tool calling as part of the
chain of thought, including web browsing
and Python tool calling. Meaning the
model can combine a series of tool calls
and reason between them to make uh uh to
more effectively achieve complex tasks.
And both of the models are permissively
licensed under the Apache 2 license,
meaning you can use them both in
commercial applications or fine-tune
them to make them your own as long as
you adhere to local laws in your region.
These models should also instantly feel
familiar to you if you've used or other
reasoning models like Open AI's 03, 04
mini or GPT5 as they introduce the same
variable reasoning, chain of thought,
function calling, browsing, and Python
capabilities.

[00:03]
In fact, GP2s 12B and 20B have nothing
to hide when you compare them to 03 and
04 mini. On humanity's last exam, for
example, a benchmark designed to test
knowledge of uh test AI at the frontier
of human knowledge. Both GPUs 20B and
12B perform on par with O4 Mini. Except
in our case, GPOSS 20B can run entirely
locally on your laptop.
And even with complex math problems like
Amy 2025, the models are able to keep up
with 03 level performance. to repeat
that that is real state-of-the-art level
intelligence that you can run now
locally on your computer
and these models are designed to be used
in agentic use cases. So function
calling performance is incredibly
important in Towbench retail for example
which tests the model's ability to use
tools to resolve a retail customer
service issue across multiple turns. Uh
both models are performing extremely
well especially given their size

[00:04]
and overall the models fit very well
into our open AI ecosystem. You can use
them in the agents SDK or with codec cli
and increasingly more providers like
grock hugging face vlmvidia
and as of today LM studio have started
offering their own responses APIs. That
way they should work directly within
your existing projects and allow you to
mix and match them with other open
models.
And when building these models, we tried
to really listen to community feedback.
And two of the biggest asks we heard
from the community were for one us to
not hold back when it comes to
capabilities, especially for agentic use
cases, and to have efficient models. And
we tried to balance these two and are
pretty happy with the result in the
overall um open models market space,
striking a great performance between a
great balance between performance and
size.
And the feedback from the community and
our partners has been great so far. In
total, it's been downloaded over 23
million times on our hugging face

[00:05]
organization alone. And people love
using the model for local use cases, its
tool capabil tool calling capabilities,
and the overall cost efficiency of the
model.
Some of my favorite use cases of GP2s so
far came from our six week long
hackathon that wrapped up a few weeks
ago. You'll see some of the examples
later on in the developer state of the
union, but we've seen people use we've
seen people use GPTOSS for controlling
robots, discussing sensitive topics in
their own personal diaries, fine-tuning
it for uh to be a subject matter expert
on highly specialized topics or even
just to be a better storyteller. have it
used in offline coding assistance and
even use it use its coding ability to
create a fully on premise cyber security
operations center to help protect
systems without disclosing sensitive
data just to name a few. That's why
we've invested in GPOSS
to give developers the flexibility and
control to build the models the the the

[00:06]
way that they know best and to run it
anywhere. Enough talking though. Let's
actually see GP2S action in a couple of
examples.
So since GPUs is an open model um
there's a wide range of ways that you
can run and host it on servers. You can
use frameworks like VLM and transformers
or for local inference you can use
projects like Llama CPP LM Studio or
Lama. For this demo we'll actually build
a chat agent that will help me keep
track of my finances without revealing
my own private financial data and by
leaving it entirely local. To power the
agent, we'll run GPUs 12B. So that's the
larger model completely locally on my
MacBook using Olama, but the same thing
should work with other inference
solutions.
I've already downloaded the model on my
laptop since I didn't want you all to
watch me download 70 GB on conference
Wi-Fi. Um, but because of that, we can
actually go and turn off our Wi-Fi here
since the model is entirely local. All

[00:07]
right, we've turned off the Wi-Fi and
with that we're completely at the will
of the of the model and the demo gods.
So, wish me luck. We can see if the
model is running by using the Olama CLI
here
and send a friendly greeting to the
model and we can see the model going
through its reasoning process and
responding accordingly. All right. So
now that we know that the model is
running, we need to use uh we need to
use a local API to integrate it into our
app. Olama and most inference providers
um already provide a chat completions
API, but in our case, we want to harness
the full power of the model. So instead,
we'll run our own responses API proxy
that
Let's get out of here.
All right. Hi. There we go. Um, we're
going to run our own responses API proxy

[00:08]
that we shipped as part of GPUs and that
is available on GitHub. This proxy will
expose built built-in Python and
browsing tools on top of sending the
token generation to our inference
provider in this case running on this
device.
Now, let's actually build the agent. Uh
for this I'll be using the agents SDK
for TypeScript to build our finance
agent that powers the chat interface
that you can see on the right. We
already have a very basic setup here
where we have the chat interface hooked
up to the agent on the left and then
configure the agent to use our locally
running responses API and for it to use
the Python code interpreter as a tool.
So right now this agent is pretty
generic. Um but we can see what it can
do by asking a question like what is the
square root of
some random number
and we should see as I mentioned earlier
that the model can perform tool calls as

[00:09]
part of the chain of thought. So you can
see here um it's starting to think
through the steps it has to do. it tries
to use the Python code interpreter,
realize that it actually was trying to
use some uh dependencies that it didn't
have and correct automatically. This is
the same kind of behavior as what you
would see from models like GPT5, 03 or
04 mini, except that in this case it is
completely offline. That means we can
build agents the same way that we're
used to with these models, but for
sensitive data that might have to remain
on premise.
for my finance agent, for example, I
have a bunch of financial files um
scattered in my directory, but I should
probably clean up this situation because
there's a couple of files that I don't
want to have leave the system. Um but
since we're running the model locally, I
don't actually have to worry about this.
With GPUs, we can equip our agent with
the necessary tools to handle sensitive
data while keeping the data entirely
local. to connect uh to the file system.

[00:10]
We're actually going to use an MCP
server that exposes the necessary tools
for the agent to browse and open files.
Let's add the MCP server
and then connect to the MCP server again
entirely locally and provide it to our
agent here.
We can now check if it if it works by
asking how many files are
in the top level.
And you can see it's going through its
reasoning steps again using the
different MCP tools to browse the system
and get the information. And we get an
answer. So now let's try a more complex
question like summarize my overall
portfolio growth
in 2024 in percentage

[00:11]
and this is where you can really see the
power of GPTOSS coming to uh coming into
place where we're using the tools as
part of the chain of thought. performs
multiple requests to the file system
things, write some Python code to
interpret it and then give us an answer
um directly to us without having to um
go back and forth with the user. Now,
now all of this has been fully running
offline leaving the data entirely on
premise. But especially if you're using
the smaller GPUs 20B model, there might
be moments where you need the model to
know more or you're hitting other
capability limits. For that, we're
actually going to connect back to the
internet. And I'm going to show you two
more things. One, I want to provide the
model with the ability to do web
browsing. And two, I want to give it
access to GPT5 for some additional
tasks.
For browsing, the model was trained on a
generic browsing tool, meaning that you
can build entirely your own browsing
browser tool on your proprietary search
provider, run your browsing through your

[00:12]
own proxies if you want to apply content
filters, or even have a fully offline or
on premise search index. In our case
though, we're uh we'll use an example
search provider. We have two on GitHub.
One is Exa and the other one is u.com.
And in our case, we're going to use the
XA API.
This is already set up by us using the
responses API proxy that we're you uh
that we set up earlier. So I just have
to enable it. But how enabling web
search works will depend on your
inference provider. And the same goes
for Python. So some of the inference
providers might not support this yet. I
also want the agent to be able to create
me little interfaces uh to be able to
dive into the data that I'm working
through. While the model is great at
coding, it's not our best model for
coding. For that I actually want to give
it GPT5 as an agent that our agent can
use as a tool.
So in this case
I already have an HTML HTML agent here

[00:13]
that is using GPT5 and is specialized on
writing inter interface code in HTML and
nothing else. I also have an input guard
rail here that checks if anything looks
like a social security number to avoid
accidentally passing any sensitive data
to my remote GPT5 model. You could do
the same check type of checks with other
confidential data that you want to make
sure stays on premise.
All right, we need to still add this
here.
So I'm going to pass it in and I'm just
going to give it a tool name of
generateization.
And with that we can ask a task like
create a bar chart of my individual
stock gains in 2024.
Got to put a comma there.
All

[00:14]
right.
Now we we should see the model going
through the same steps again. Reading
the f reading the necessary files crunch
using Python to crunch the necessary
numbers and then using GPT5
once it has the data. See,
so you can see here it was calling the
code interpreter to actually process
that um file. Seems like it messed up
something and like this is the benefit
of that chain of thought reasoning and
it can actually go and recover.
So um every once in a while you might
run into these situations. Uh there we
go. Got the data.
Um
oh there you go. Now it's calling the
generate um generate visualization tool.
And you can actually see here that
because my
social security number check is

[00:15]
relatively rudimentary, every once in a
while it might run into things where
like that regular expression gets
triggered. So in this case the model
realized that and again selfcorrected
and performed another tool call to the
model here. And now in a second we
should get back the result.
See? Come on internet.
All right. While we're waiting for that,
let's move on. As you saw, GP There we
go.
All right. Thank you.
Um, so as you saw, GPOSS seamlessly fits
into the broader OpenAI ecosystem. We're
able to write a uh write an agent the
same way using the agents SDK tools that
you're already familiar with. Run it
entirely offline and the model behave
the same way as our other reasoning
models do. And we're able to leverage
GPT5 for task that is less equipped to
do.
One more thing though that we can do

[00:16]
with GPUs is to make it our own by
fine-tuning it. Maybe you're not quite
happy with the performance of GPTOSS on
a specific topic or task. Or maybe you
want the model to be a subject matter
expert on a specific field or some
internal data. Traditionally, that would
mean that to use a technique called
supervised fine-tuning where at a high
level, we give the model a bunch of
input and output examples and train the
model on those to get better at similar
inputs. However, with GPUs's reasoning
capabilities, a more interesting way of
fine-tuning and personalizing GPUs is
doing additional reinforcement
fine-tuning where we give the model
inputs and a reward function that tells
the model how good the output was. To
give you an example of fine-tuning, um
I'm we're going to briefly see it in
action, but since watching a model
fine-tune for hours might not be the
most interesting thing you can do today,
uh I already fine-tuned a model ahead of
time.
So before I explain you what we did, how
many of you know this game of 2048?

[00:17]
All right, cool. So in these games, for
those of you who don't know, uh the as a
player, you try to combine different
tiles with the same number that are next
to each other by swiping up, down, left,
right, and to merge these tiles and
eventually reach 2048. We wanted GPUs
20B to play the same game by having it
write a Python function that encodes a
strategy to actually play the game. And
as you will probably see here, the base
model is decently okay at playing it,
but occasionally writes wrong or very
basic code where it doesn't get far in
the game, especially on low reasoning.
So, if we're testing this out here, um,
seems like this did okay, but it
definitely didn't get very far on the
board.
So instead, we fine-tuned a dedicated
model by giving it a reward function
that takes the board strategy and then
place boards on it. So that and then we
used a and to see how far it gets and

[00:18]
then we used a technique called uh gpo
uh which is a reinforcement train uh
reinforcement fine-tuning technique and
a tool called unsllo to actually
fine-tune the model. This is a
non-trivial amount of code. if I scroll
through this entire uh entire notebook.
So if you do want to check this out, uh
it's available on our GPOSS GitHub page
and you can check it out there and retry
it yourself.
So let's actually see this in action. Um
by having GPUs and uh and our fine-tuned
version each generate five different
strategies here. So uh we can see the
model is starting to kick off all of
these different Python strategies. It's
a bit harder to read at the second while
it's still generating. But every once in
a while, both models will return some
more like rudimentary techniques, uh,
rudimentary strategies.
But it's also pretty hard for you to
distinguish between them and which one
is better or not. So, in order for us to
figure out if the model actually did a

[00:19]
better job, we're going to have the two
models with these five strategies play a
100 boards against each other to see
which one gets better. So, we're almost
there. Some of them are still
generating.
Um, let's see how many. One. All right.
Looks like we're done here. So, let's
run this. And
demo gods. Come on. Yes.
So, you can see model B, which is
actually our fine-tuned version of the
model, um, won quite significantly in in
the different games playing against each
other and also got it overall a total
higher score.
All right, I do have one confession to
make though. I mentioned earlier that we
were running GPSS entirely locally. And
while that was the case for the first
demo, these two models were actually not
running on my device. They are still
running entirely locally though and not
on some GPU in the cloud. Instead, um I
actually got to run them on a very
special piece of hardware.

[00:20]
So years ago, uh, Jensen delivered the
very first DGX1 to OpenAI. And you can
see it here on the screen. It was a
milestone in compute. And while it would
be fun to run these two models on a
DGX1, it doesn't quite fit on the
podium. And you all would have probably
figured this out by now. So instead
though, I have a great alternative.
This is the DGX1 uh DGX Spark from
Nvidia. And this little beast contains
the same amount of compute as the DGX1
and in fact is currently running both of
these models, but also fine-tuned the
model while standing on my desk. You're
all some of the very first people
actually to see this live outside of a
lab. Um, and Nvidia was so kind to give
it to us for this demo. Um, in fact,
it's not available at all yet. There's a
pre-production system that Nvidia
provided to us to help get the system
ready for developers like you all. And
because it's still pre-production
hardware and software, it might not be

[00:21]
fully representative of its final
capabilities and performance, but it's
been a lot of fun to work with. Um, so
if you want to check out the code for
the fine-tuning to learn more and try it
out yourself, even if you don't have a
DJX Spark yet, um, you can find it on
GitHub.
All right, to summarize uh, what we've
seen so far, GPOSS is a great option if
you need to run the model locally.
um or on premise for example for safety,
privacy or low latency use cases. And
GPSS seamlessly integrates with uh the
OpenAI tools that you're already using
including the agents SDK and the codec
cli. So whether you're building an agent
that has to run locally or you're trying
to code offline, GPUs can be useful. And
GPUs and GPT5 can work hand inand
allowing you for this allowing you for
use cases where you need to run a blend
of models to get both state-of-the-art
performance and some of the benefits of
open models. Lastly, GPUs can be

[00:22]
fine-tuned for your own use cases,
giving you the ability to have your own
expert models on uh on your use cases
while leveraging the same intelligence
and capabilities of OpenAI's reasoning
models, all while running fully on your
own hardware of choice.
If you do want to learn more, you can
check out all of the resources on
openai.com/openmodels.
And with that, thank you very much.

</details>


I asked it to take my Streamlit app and create a FastAPI server that would perform the same work and connect it to my [Next.js](https://nextjs.org) front-end. After firing off the task, I went to lunch and came back to a fully implemented and working application. From there, I was able to have Codex work on additional tasks to create additional pages that helped me better illustrate the demo.

Without Codex, this demo would have never landed on time.

![Screenshot of the IDE Extension with a prompt to port the Streamlit app to Next.js using a FastAPI server](/images/blog/codex-at-devday/streamlit-duel.png)

## Making it real

Erika Kettleson was able to save time by using the Codex IDE extension to turn an entire booth demo into reality. She started with a sketch that was fed into Codex to create the initial UI, and even had Codex write evals to help determine the best model to use to generate SVGs while trading off speed and quality. Codex helped Erika evaluate the tradeoffs of using a single or multi-agent architecture for the demo and then refactored the whole codebase to move to the single agent architecture.

And after building it all, Codex created detailed Mermaid diagrams that Erika used at the booth to explain to people how the app worked.

![Screenshot of Erika's booth demo](/images/blog/codex-at-devday/booth-demo.png)

![Screenshot of the SVG eval results that Codex generated](/images/blog/codex-at-devday/svg-eval.png)

## Reviewing at scale

One part of the [AgentKit launch](https://openai.com/index/introducing-agentkit/) was the release of our new Guardrails SDKs for [Python](https://pypi.org/project/openai-guardrails/) and [TypeScript](https://www.npmjs.com/package/@openai/guardrails). These SDKs are designed to work with our Agents SDKs in [Python](https://openai.github.io/openai-agents-python) and [TypeScript](https://openai.github.io/openai-agents-js) and with Agent Builder. To ensure that developers had a great experience with the SDKs, Kazuhiro (Kaz) Sera came onto the project to help get the project over the finish line.

He used Codex to quickly ramp up with the codebase of the two SDKs, identify the root causes of some of the bugs that he and Codex identified, use the Codex CLI and IDE extension to fix them and leverage Codex code review to identify any outstanding bugs.

Thanks to Codex he was able to do all of that to help the team get the SDKs out while also using the same tools to polish the [ChatKit](https://platform.openai.com/docs/guides/chatkit) sample apps that we released the same day.

## Juggling multiple projects at once

Leading up to DevDay, a lot of us were working on increasing projects at the same time. Codex allowed us to delegate across both local and cloud tasks using the IDE extension and CLI to tackle several tasks at once.

Often you would see us run 3-4 completely independent tasks at the same time. For example, in my own case I had Codex at the same time: build Jupyter notebook support into the [gpt-oss server](https://github.com/openai/gpt-oss), refactor and fix some bugs on my agent demo, restructure some Codex docs, and debug my fine-tuning run.

To quickly context switch on our side, we wouldn’t spend a lot of time carefully crafting the right prompt–instead, we’d describe the problem in short sentences to Codex, fire off the task, immediately switch to the next one, and return later to check in on the status of Codex. Even leaving your desk quickly included the habit of “let me just send off one more Codex task” before getting up.

## Getting organized

Launching multiple new products for developers comes with a lot of new documentation that, in the early stages, gets written in documents all over the place: whether it’s inside GitHub repositories, in Google Docs, or in Notion. Often, these documents get iterated on until the very last minute. This launch was no different.

Thanks to Codex Cloud, the team was able to take the fragmented documents, hand them off to Codex with a rough description of how we wanted them to be broken up and organized across our docs, and let Codex handle the rest. Codex split up the files, converted them into MDX files, set up the necessary navigation structures and opened up a PR that we could share with teams for review and iteration thanks to deploy previews.

Without Codex, this would have normally taken hours (if not days) leading up to DevDay.

## Dealing with side quests

Lastly, we’ve all been there–you’re working on the most important task but suddenly you remember this one task you had been planning to do, but you keep getting distracted.

The night before DevDay wasn’t much different. Between rehearsals we were trying to get everything ready for the big day. Katia was getting ready to go onstage to rehearse her demo when she realized she hadn’t shipped an updated 404 page like she had planned.

She quickly opened up another tab on Codex Web and sent a task asking Codex to implement a new [developers.openai.com/404](https://developers.openai.com/404) while using the best-of-n feature to have Codex create two attempts at the same time.

Before Katia went on stage five minutes later, she was able to review the two options thanks to the preview screenshots in Codex, quickly check out the page to make a couple edits using the IDE extension, and ship the newly redesigned 404 page.

![Screenshot of Codex Web incl. a preview of the 404 page](/images/blog/codex-at-devday/404-page-codex.png)

## Just scratching the surface

We could probably talk for hours about how Codex helped us shape DevDay, let alone how it helps every one of us on a day-to-day basis–but this is just a glimpse into how we’re using Codex across OpenAI.

If you want to learn more about how we use Codex and some best practices, [check out our DevDay talk about Codex](https://www.youtube.com/watch?v=Gr41tYOzE20) or [check out our documentation](https://developers.openai.com/codex).

<!-- yt-inline:Gr41tYOzE20 -->
[![Shipping with Codex](https://img.youtube.com/vi/Gr41tYOzE20/hqdefault.jpg)](https://www.youtube.com/watch?v=Gr41tYOzE20)

<details>
<summary>자막: Shipping with Codex (28:53)</summary>

[00:00]
I'm Thibaud.
And I'm here at OpenAI and I build
Codex.
With Codex, we're building an AI
software engineer.
I personally like to think about it as a
little bit like a human teammate.
You can pair program with it on your
computer.
You can delegate to it. Or, as you'll
see, you can give it a job without
explicit prompting.
There's been, recently,
a massive vibe shift.
This has started from August, where we
had pretty decent usage, and since then,
thanks to all of you,
we've grown tenfold.
Today, I want to start by sharing some
of the recent updates that have created
this vibe shift.
Then, we'll bring some engineers from

[00:01]
OpenAI to show you some examples of how
we use Codex day-to-day.
Some of them are building here on the
Codex team. Some of them are just really
excited users of Codex at OpenAI.
Let's first talk about some of those
updates.
Codex now works everywhere you build.
Whether it's in your IDE, your terminal,
GitHub, web, or mobile.
No matter where you are,
it is the same powerful agent under the
hood.
The first and most important improvement
we made was to completely overhaul the
agent.
We think of the agent as a combination
of two things.
The reasoning model under the hood and
its tool harness to allow it to act and
impact change upon the world to create
value for you.
First, the model.
In August, we shipped GPT-5, our best
agentic model thus far.

[00:02]
That was until we listened to your
feedback.
And we approved upon it by shipping
GPT-5 Codex, a model that was further
optimized for work within Codex,
improving by being smarter, better
following code style, and adapting its
thinking time.
One of my favorite quotes from the
feedback from you all was that it feels
a little bit more like a true senior
engineer because it gives such few
compliments. And it also pushes back
on bad ideas.
Next, we completely rewrote the harness
to make most of the new models.
Add support for planning, MCP, auto
compaction,
so that you can have these really long
conversations and interactions, and so
much more.
At this point, we started seeing the CLI
usage take off.
But, there's more feedback.

[00:03]
The model felt really good. The agent
was useful, but the CLI felt early.
We appreciate the feedback, and so we
decided to completely revamp the Codex
CLI. We simplified approvals modes,
created a more legible UI, and added a
ton of polish polish.
And by default, it works with
sandboxing, so it is safe by default,
but you always have control.
It's been a work in progress, and we
shipped a big update last Friday.
We'll ship a new release today again.
More feedback from you all. A bunch of
you collaborate with the agent and want
to look at the code at the same time.
This is why we shipped it in the IDE
directly as a native extension.
Here, it works with your code alongside,
you know, you having control over your
IDE, get this little collaborator. It
works in VS Code, it works in Cursor,
and other popular forks.

[00:04]
This immediately took off.
Within the first week, we had 100,000
users. Many of you, I'm sure, are in
this room. A lot of our users prefer to
use Codex in their IDE directly. Part of
the magic here is that it is the exact
same agent.
It is the same open-source harness that
is powering the CLI bundled right within
the extension.
At the same time, we're also upgrading
Codex Cloud
so that
you could run many more tasks in
parallel.
For us, this is still the beginning, but
we think it's incredibly cool to be able
to command Codex through your phone.
Cloud tasks now run 90% faster
faster. They can set up their
dependencies automatically and verify
their work by taking screenshots and
sending them to you.
Giving the agent its own computer really
feels magical when it works.
And then, you can start working with
agents like this in tools like GitHub.

[00:05]
Or now Slack.
Here's an example of one engineer. Some
of you might know him.
Who had a question. And then another
engineer, Steve Lee, immediately jumps
on it and delegates it to Codex. Here,
Codex receives the entire context from
the thread and just gets to work. A
couple of minutes later, it posts a
solution together with a summary. It
actually went, explored the whole
problem, and wrote some code.
All of this progress means that we can
write code so much faster,
which also means that we have a lot of
code collectively to review.
Validating and reviewing code is now
becoming a huge bottleneck.
This We've been thinking about this for
a while.
Past experiments with code review at
OpenAI showed that it could be
useful, but also oftentimes noisy.
Previous attempts had to be turned off
because users were complaining about the
lack of signal.

[00:06]
So, we purposely trained GPT-5 Codex to
be great at ultra-thorough code review.
It goes through the dependencies, all
the code in depth inside its little
container,
truly explores the contract of like your
intent and what actually happens in the
implementation,
and then comes back with high-quality
findings. We now find that many teams
decide to enable it by default and
almost and want to make it mandatory
because it is such a high signal
finding every time.
You can trigger it while pairing with
Codex, or you can completely automate it
by running on every PR in GitHub.
Okay.
It's been a busy few months for a small,
growing team.
We've been using Codex to build Codex.
There's really no way we could have done
it without it.
Even more fun has been seeing OpenAI as
a whole get accelerated.
Today,

[00:07]
92%
almost all of OpenAI technical staff
uses Codex daily.
Up from 50% around last July.
Engineers that use Codex submit 70% more
PRs per week.
And pretty much all PRs are reviewed by
Codex.
When it finds an issue, people are
actually excited. It saves you time. You
ship with more confidence.
There's nothing worse than finding a bug
after you actually shipped the feature.
When we as a team see the stats, it
feels great. But even better is being at
lunch with someone
who then goes, "Hey, I use Codex all the
time. Here's a cool thing that I do with
it. Do you want to hear about it?"
And so we wanted to give you a taste of
that.
So, let's get to lunch with a few
teammates
and hear about their stories. They'll
show you real workflows of our teams,
how they use it every day.

[00:08]
Please welcome Nacho to the stage to
talk about iterating on UI
for the ChatGPT iOS app.
[Applause]
Thanks, Thibaud.
Hello. My name is Nacho Soto. I'm a
member of the core iOS team at OpenAI.
Going to do two things today. I'm going
to tell you about a workflow that I use
frequently when building the ChatGPT
app. And I'd like to share a demo that
shows you how I do this.
Let's start with the demo.
Thibaud asked me to build a weather app.
So, I have a starter project with just
an empty window.
And I've also asked ChatGPT to make a
mock-up of what I want the UI to look
like.
So, I'm going to ask Codex
to implement that design.
Great. While that's running, let me tell
you what's special about how Codex is

[00:09]
going to implement this.
Working in the ChatGPT core team means I
spend a lot of time on infrastructure,
performance, but also do some amount of
front-end work.
Recently, I worked on this small feature
where we simplified our personalization
screen to make our new ChatGPT
personalities more discoverable.
And I'm sure you've run into something
like this before. With that last 10% of
polish, like getting these headers and
footers aligned, it's actually taking
90% of the time.
But Codex can help you with that 10%.
And you can work on that while you do
something else. Maybe you're watching
some of the other DevDay talks.
You can even have nine other terminal
tabs running Codex if you want to be a
true 10x engineer.
Who here has been sent a pull request
from a junior engineer, and within a few
seconds you you that they didn't
actually test it, cuz there's no way
that it works.

[00:10]
If you used ChatGPT or any other agent 6
months ago, you were working with that
junior engineer.
But Codex is not.
Like Tevo said, I would argue that Codex
is now a senior engineer.
It doesn't just write the code and
assume that it works. It will verify
that it does.
I'm a big fan of TDD, test-driven
development. And I think Codex really
thrives with that workflow.
It will run your tests, fix the code,
run your tests again, over and over
until they pass.
But why stop at unit tests?
Codex is multimodal, which means it can
also verify its work visually.
A few weeks ago, we gave Codex that
superpower of being able to see images.
So, I taught it to generate snapshots
for the UI code that it writes.
And best of all, it's actually very
simple.
First,

[00:11]
I made this very simple makefile that
runs the unit tests to extract the
SwiftUI previews.
And that calls a small Python script,
which Codex wrote, by the way.
And that extracts those images, puts
them in a folder so Codex can find them.
Then in the agents.md I just told Codex
about that script, and I've asked it to
use it to verify its work.
We use this workflow to build the
ChatGPT iOS and Mac app. You could do
the same on web, for example, with tools
like Storybook or Playwright.
So, that's my workflow. I give Codex
some tools to generate screenshots so we
can verify the UI code that it writes.
Let's check in and see how Codex is
doing.
Okay, so if I scroll back,
looks like it wrote some code, started
with a plan
uh to review the existing code, uh
implement the UI, and provide preview

[00:12]
data to verify that it's good. So,
great, looks like it wrote all that
code, ran the snapshot tests.
Cool. So, uh
no, I guess no, but for 3 minutes, go
ahead and run that up.
Cool.
So, obviously this is a very simple
example, but it actually scales with how
many changes to match larger projects
like the ChatGPT app.
And it can run for many hours depending
on the tasks, iterating over and over
until it's pixel perfect.
And speaking of working for many hours,
I like to pass it over to Freal, who's
going to show us how to scale these
verification loops to run for longer
periods of time and more complex
problems.
Thank you.
[Applause]
Thanks, Nacho.
I'm Freal, and I work on developer
productivity.
Here at OpenAI, I've set high scores for

[00:13]
the longest sessions or the most tokens
produced.
I'm known as the guy that gets Codex to
do this.
For being able to use Codex to one-shot
big features and complex code changes.
I've seen the GPT-5 Codex model work for
over 7 hours productively. That was my
prompt. Or process more than 150 million
tokens over the course of a marathon
session.
This is one of those projects.
It's a complex refactor, a major feature
for my my personal JSON parser project.
And for large projects like this, there
can be long periods of time where it
seems like
all of the tests are failing until the
work is complete, especially when you're
making that core change.
Now, this is a JSON parser built for
streaming tool calls,
a parser for the AI age.
And this person this PR has over 15,000
lines of code changed, and it was
created over many hours of work from
Codex,
but only a few minutes and a handful of
prompts from me.
Let's walk through how I go from prompt
to pull request.

[00:14]
We'll do this in just a couple prompts.
First, we'll tell Codex that we want a
plan to implement our feature.
Then, we're going to review that plan
and tell it to execute. And finally, we
ship.
Here, I've opened my project in VS Code,
and I'll open up our Codex extension as
well.
Uh I have a fairly complex feature I
want to implement, and I've prepared
that in a document for me for me to
read.
And I'm going to tell Codex that I want
it to write a plan to implement this
feature, and I've described the end
state.
But I want Codex to do the heavy lifting
for me and research how to integrate
this library into my parser.
So, what I do is I ask Codex to write a
spec.
And I'm going to go ahead and kick that
off.
And actually, I'm going to turn off auto
context here. A little bit of an aside,
I've rehearsed this a few times, and
it's actually found finished specs from

[00:15]
my Git history and cheated and copied
right to the end of the process.
So, I'm going to have it really do the
work.
And uh
you'll notice I don't need to tell it a
lot. I've given it my example, I've told
it to do some research,
follow the example of the code that I've
already got.
So,
while that's working, let me show you
what I mean by a plan or an exec spec.
This is my plans.md file. I've
abbreviated everything here so we don't
have to read all of it. It's 160 lines.
Uh but really what I'm doing here is I'm
writing a design document for design
documents.
Codex is now a senior engineer, after
all, so we should be asking it to do
some of its own paperwork, too.
And like most engineers writing a design
doc, it's going to start by copying from
an example. I've got one here.
And I tell it,
you know, this plan is going to contain
is going to be a living document. It's
going to describe its big picture. It's

[00:16]
going to have a to-do list and progress
that it keeps up to date.
And I also want to say,
why do I keep on saying exec plan?
And I'm doing that because I want to
give the model a term to anchor on and
know when I use the term exec plan,
use plans.md to design that, to iterate
on it, and follow up.
It's good to give it a a term that's
unique so that it knows to reflect back
on that. And when I say that, it's
something special, not just any design
doc or implementation spec.
So,
in this spec, we've got our progress,
our surprises and discoveries. We even
have a decision log in here for me to
keep track of what it's been working on.
Now,
normally I don't ask engineers to write
this much. I only do that when maybe I
don't like their project.
[Laughter]
But in this case, this helps Codex steer
towards a completed project. It is its
memory as it works on this large plan.
And after this talk, we'll upload the
plans.md recipe to our OpenAI cookbooks

[00:17]
so any of you can adopt it in your
repositories.
Now,
how does it know
how to use this plans.md? As I mentioned
earlier,
I've used my agents.md.
I drop a couple lines here in my
agents.md, just a few instructions. When
you're working on something complex,
this is what an exec plan is, refer
plans.md,
make sure that you're following that.
Now, as you can see, it's doing quite a
bit of research on the side here, so
let's go ahead and look at a completed
spec.
So, I've switched over to a completed
session here, and it's written my spec.
Let me open up that plan here.
So,
I can review this. I can give it
feedback. I can look at Okay, that looks
like, you know,
quite a lot of words, but it is what I
wanted to do, and it has a plan.
Looks like a couple spikes, some
features that it wants to implement, and
of course documentation. So, that looks

[00:18]
good to me. I'm going to go ahead and
tell
Codex,
let's go ahead
and implement.
And we can't type today. There we go.
And
so while that runs, uh I like to keep an
eye on Codex. It keeps something
scrolling on my screen. My manager knows
that I'm still working.
And I like to watch the tests. So,
what I'll do is I'll kick off these
tests. They run very fast. Uh Codex
helped me write all of these, by the
way, from simple property tests or
simple uh unit tests to exhaustive
property tests. There's even some
fuzzing in this crate.
And uh so, I'll keep an eye on this, and
if it stays red for too long, I might
intervene and say, you know, Codex,
maybe we need to back out. Maybe that
plan is going a little off the rails.
All right, let's go ahead and look at
what it's completed in this project. So,
I'm skipping ahead to Codex having
finished that task. By the way, that

[00:19]
took over an hour in my my previous
session, so we're skipping ahead quite a
ways. And it looks like it's written
some new tests.
Um they're all passing, which is great.
Uh let's go ahead and look at the
changes.
Okay.
Wow, and it looks like it vendored in
and even maybe forked or updated the
upstream library to make some changes to
implement what it needed to do.
Now,
again, I don't have all day to read all
of this to you, so I'm going to go ahead
and open up the plan again.
So, I open up the plan, and I can see in
the progress, it's checked off some big
items. It's completed some spikes.
It's updated documentation in the
readme.
Plans.md specifies that all of these
plans have to be a living document, and
so I can use this as an executive
summary to know what it's accomplished.
That way I don't have to read all the
code myself.
Okay.
It looks like it's done and the tests
are passing.
So,

[00:20]
uh
what I've shown you today is we can go
from
uh
an implementation idea feature
a prompt to a PR in only a few steps.
Rigorous planning and thorough testing
enabled the model to work on this
feature for a sustained period of time.
And let's just see how many lines of
code it's written.
Crashed.
Okay.
4,200 lines of code and just about an
hour of work.
Incredible.
Now,
I could just merge this as is, but I
would really like another set of eyes on
this code.
Thankfully, we have Daniel up next to
talk about code review.
Hello.

[00:21]
All right, my name is Daniel and I'm an
engineer here on the Codex team. So, uh
today I want to talk about code reviews.
As Thibault mentioned, we launched code
reviews on GitHub a couple months ago
and it has been a huge hit.
Um
both externally, but especially
internally, we love code reviews. We
have them running on all of our PRs and
it's finding so many bugs that we would
have otherwise missed. And some of these
bugs are so complex that you have to
like read and reread the comment a
couple times to even understand what
it's saying. So, I highly highly
recommend you enable code reviews for
all your GitHub PRs.
Um
here's an example of one of my PRs
that's on the Codex repo. It's open
source.
So,
I uh
pushed a feature and then immediately
Codex started reviewing my code and it
found a P1 issue. Great.

[00:22]
Uh so, then I said, "Thanks, Codex.
Please fix it." And that kicked off a
background task um to to make that
change. And then once that got merged, I
said, "All right, Codex. Um
now that you have all this, now that you
have this change, review it again. Make
sure we don't have any issues."
And then it found another issue.
And then uh I was just embarrassed.
So,
this got me thinking.
What if you could have a workflow where
you create a feature
and then you review it for bugs and then
if there are any bugs, you fix it and
then you review it again and then you
fix and review and fix and review until
theoretically your code doesn't have any
issues.
So,
uh we decided to make this super easy by
bringing code reviews to local as well.
And I'm going to show you how to do that
with slash commands. And this is what I
do every day before I even submit the
PR.
Okay.
Uh so, I'm working on a little feature.

[00:23]
Uh you can see it has like three
different commits. It's a pretty small
one.
Um and I have the CLI running on the
side. So,
all I have to do is write {slash}
review,
hit enter,
and then you'll see there are a couple
different options here.
So, the first option is reviewing
against a base branch, just like a PR.
So, this would take a some of your well,
all of your commits in your base branch,
compare it to main,
uh just like a normal PR, and then look
at the whole diff and try to find any
uh issues with it.
There are other options, too, like
reviewing uncommitted changes or
specific commit or custom review
instructions, but what I usually do at
the end of the day when I have a bunch
of different commits is just review the
whole thing. So, I select the first
option. Now, I have to select a base
branch. Usually main is the first one,
so I hit enter again.
And now code review begins.
So,
a question I have is

[00:24]
why is it so good?
Why is GPT-5 Codex so good at code
reviews? Because we actually trained it
specifically on finding very technical
bugs and it will go on for a very long
time researching all sorts of different
files and then when it has a hypothesis
for something that could be wrong, it'll
even write tests, um scripts, execute
them to make sure that it gives you like
one or maybe at most two critical issues
that you have to fix before you land
your PR. It doesn't give you like 20 or
30 different things that it one shots
from just looking at your diff. It
doesn't waste your time.
So, um
yeah, there's actually a bug here.
Uh
If anyone gets Oh, nice.
It It got it for us.
Um so, it's a P0. Great. Um
and it's exactly correct. So, we aren't
supposed to be hardcoding the string
here in the code. We should be getting

[00:25]
that dynamically. So,
all I have to do now is tell Codex,
please fix.
Uh and usually I don't even read the
comments, so
uh
it just goes.
But,
yeah, and the ni- the nice thing about
reviews in the CLI is that it actually
spawns a separate thread from the
parent. So, let's say you've been
working on this feature and it is like
super biased, you know, you have to do
this feature like this, you have to
implement it like that.
The review thread is separate. It has a
fresh pair of eyes, a fresh context, new
chat, uh so it doesn't have that same
implementation bias and it'll help find
these bugs for you.
Uh so, yeah, that is going to go ahead
and and uh you know, give us some
changes. While that runs, I want to
actually show you how you can enable
um reviews on all your PRs. So, go to
chat.openai.com/codex.

[00:26]
And then
you just connect your GitHub.
And then there's a button here called
enable code review.
So, this will take you to the code
review settings and you can have like
repository level settings to say like I
want this repo to get code reviews, I
want that one to not, but I just have
this toggle over here that I just say,
"Review all of my pull requests. Please
make sure I don't ship any regressions
to prod."
So,
let's go back.
Fantastic.
Uh it made the change. Let's see.
That looks correct. Yeah, now it's
getting the prompt directory
dynamically. So, now that this is done,
what I want to do is I want to run
{slash} review again.
So, I hit {slash} review, enter, enter.
Great. So, this will start another
review thread. And then once that goes
on, hopefully it won't find any issues,
but if there are any issues, you can
continue it again.
Um and then once that's done, it gives
you a thumbs up.

[00:27]
You commit.
You push to get. And then you get one
final thumbs up from uh Codex on your PR
and you're merged.
So,
that is what I do every day
using {slash} review in my daily
workflow before I even create a PR.
Thank you so much and I'll hand it back
to Thibault to wrap it up.
[Music]
All right, folks.
That's it.
I hope today's demos gave you a glimpse
of
how we're shipping faster and with more
confidence with Codex and a little bit
about where we're going.
If you haven't tried Codex yet, just npm
install. This will give you Codex right
in your terminal. Then you just type
Codex and you could get going and use a
lot of the things that we demoed you
today. Everything we showed to you today
is real and you can use it right away.
Gabriel Peel, one of the people here

[00:28]
working on the Codex team, actually just
sent me a message that the V045
of the CLI is out like right now. It has
a few
incremental updates and also support for
uh OAuth MCP, which I think is very
cool. Uh so, just go and install it. Um
and this will give you the latest
version. And then if you want to hang
with a few of the people building Codex,
uh just come and join us at the booths.
Uh there will be some of us there and
also some of the, you know, top users of
Codex here at OpenAI. We also have
uh a Q&A
on uh Discord that you can join and uh
this will uh start shortly. So, come and
say hi. Don't be shy. And uh thank you
for joining today.
[Music]
[Applause]

</details>

