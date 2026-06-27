---
title: "Developer State Of The Union"
channel: openai
url: https://www.youtube.com/watch?v=r1R3RDPvPeg
youtube_id: r1R3RDPvPeg
published: 2025-10-08
duration: "53:32"
captions: en-orig
---

# Developer State Of The Union

[![Developer State Of The Union](https://img.youtube.com/vi/r1R3RDPvPeg/hqdefault.jpg)](https://www.youtube.com/watch?v=r1R3RDPvPeg)

<details>
<summary>자막: Developer State Of The Union (53:32)</summary>

[00:00]
I'm Greg Brockman. I can't believe it's
already DevDay number three.
And now developers are key to advancing
OpenAI's mission. Um but before we're
going to talk about today, I want to
talk a little bit about how we got to
here.
So, 2015
we got together
what became the founding team of OpenAI
at an offsite in Napa for a day
and we came up with this plan
for what OpenAI was going to do.
Very simple plan, three steps, not
ordered. Uh
Step number one, solve reinforcement
learning.
Step number two,
solve unsupervised learning. Again, I
said not ordered. Uh and then step
number three is gradually learn
really complicated things.
Um now, we we're not the best at

[00:01]
spelling, uh so we misspelled gradually,
uh but fortunately later we made an AI
that could help correct that.
But so, that was our initial plan, and
the question was, well, how do you
actually turn this into practice? So,
2016, people showed up at our first
office, uh which also happened to be my
apartment, uh pictured here,
and got to work and started thinking
hard about what do we actually do to
realize this mission that we set out in
order to build AGI and make it be
something that would benefit everyone.
So, we tried a bunch of things that
didn't work.
But the first time we tried something
that did work was 2017 with our success
in the complex video game Dota 2. Does
anyone remember our Dota results? Anyone
follow us back then?
Decent number of hands. Uh it's still
probably the most fun project that many
of us have worked on. Just imagine in
arena of 20,000 screaming fans as your
AI plays against the best humans in the
world. It was like so cool to see the

[00:02]
engagement of that community.
And we had
this great success in this domain using
reinforcement learning, right? That
first step of the plan that we actually
were able to see if you scale this up,
great things will happen.
Now, there was only one step.
The next step was unsupervised learning.
And again, in 2017, we had some magic
come together. 2017 was a very
productive year. Uh this was with a
paper called the unsupervised sentiment
neuron. Uh this was the first time that
we saw semantics arise through this next
step prediction process in a really
concrete and sort of hard to deny way.
Does anyone remember this paper?
Okay, very few hands. A little less cool
than less cool than Dota, at least at
the time, uh but it really set in motion
a lot of what you've seen today. Uh the
idea behind the result was that we
trained a model, this was an LSTM before
transformers, to predict the next
character in Amazon reviews, just next
step prediction. And it learned a
state-of-the-art sentiment analysis
classifier. It learned not just where

[00:03]
the commas go, but it actually was able
to tell you if a review was positive or
negative, which is harder than it sounds
because you could have something that
says, well, this product was so amazing,
but it totally didn't work and wasn't as
advertised. And so, you you really need
to understand the meaning, not just like
look for keywords. Um but because we saw
this emerge from the data, emerge from
next step prediction, we knew what we
had to do. We had to scale this up.
And so, we did that. And by 2019,
we had GPT-3.
And we thought, this model, it feels not
just like it's learned semantics, it
feels useful. You could probably build a
product on top of this. But what kind of
product could you build? And we thought
about, well, maybe we should build
something in healthcare. Um but then you
start realizing, well, that means really
giving up on the G in the AGI, the
general, because that would mean we'd
have to go do enterprise sales to
hospitals. We'd have probably have to
hire doctors on staff. Uh it would be
just like really tunnel visioning going
all in on a specific application. All

[00:04]
right, well, okay, what about education?
But you have the exact same properties
there.
So, instead we said,
what if
we put this technology behind an API? We
let developers figure out how to connect
this technology to real-world
application.
And honestly,
this project felt doomed. It was
probably the hardest project that I've
ever worked on because it's exactly
backwards the way you're supposed to
build a startup. You're supposed to have
a problem that you want to solve, and no
one cares about the technology behind
it, not a technology in search of a
problem.
But it worked. It worked wildly, and
it's still working. And the reason it
worked is because of you, because of
developers, because of people who are
passionate about this technology and
bringing it to the world, making it
useful, doing the work to connect it to
real-world application.
So, thank you. Thank you for that.
That's it was really, really amazing to

[00:05]
see what what's happened over this time.
Now, last year, we brought together
these two pillars of unsupervised
learning and reinforcement learning into
one package. This was with the model O1,
with our reasoning models. This is all
part of the 2015 plan. I and, you know,
now we're on to trying to gradually
learn more complicated things,
connecting to real-world application,
having that flywheel. Um you know, you
do see that one thing at the top that
says, don't scale the group size, you
know, too fast. Stay off of 120 forever.
We are a little bit bigger than that
right now. Um
so, that part didn't pan out, but the
rest was was was quite refreshing.
Now, the mission, it's still far from
complete.
Fast forwarding to today, we have GPT-5,
which many of you are using to build
amazing applications.
We have Codex, which you are able to
collaborate with in developing software
for yourself, build amazing applications
on top of. And soon, as we announced
today, you'll be able to bring your
application to hundreds of millions of
users across the world in ChatGPT.

[00:06]
We are so excited to shape the future of
AI and software engineering together
with you.
And to share more about how we're all
investing in the future, the developer
tools that we're building, the things
we're building for you and together, I
am excited to welcome to the stage
Olivier. Thank you all.
Thank you, Greg.
Hi, I'm Olivier Gonaud, and I lead the
platform team at OpenAI.
Today, I want to talk to you about four
key things that we're working on.
Number one is we are building
intelligent models. Two, we are
accelerating how you code. We help you
build agents. And finally, we help you
scale your applications in ChatGPT.
So, we touched on some of those like
earlier in the keynote with Sam, but now
we're going to go deeper.
Let's start with models.
Just a few months ago, we shipped our
most capable and reliable model, GPT-5.

[00:07]
We designed GPT-5 for agentic tasks. And
by that, I mean that we made it really
good at instruction following and tool
use.
We also pushed the limits on coding
intelligence.
GPT-5 can refactor complex large code
bases. It can generate tasteful
front-end UIs from a single prompt, and
can work autonomously for hours at a
time.
And we're seeing startups like Augment
Code build long-running agents on GPT-5.
So, let's take a look here.
It's a pretty simple example, like the
user is asking the agent to take a look
at the at the GitHub issue.
Then the agent's going to take
essentially look at uh context by
calling many tools.
Uh I think the issue is adding a button
here.
It goes really fast, but anyway, you get
the idea. Um
it's pretty pretty impressive. That's a
basic like, you know, example, but we're
seeing like agents being built that call
hundreds, sometimes thousands of tools,

[00:08]
and run for like many minutes, sometimes
for many hours.
And so, that's the type of work that
GPT-5 was designed for.
But at launch, one thing was
not just any other model.
Prompts that worked with GPT-4
or O1 do not translate directly.
So, here are three principles, which
I've seen from working with a bunch of
customers, to get the most out of GPT-5.
Number one,
keep the prompt simple.
The shorter, the clearer the
instructions, the better with GPT-5.
Number two, evals.
And by the way, we built out a prompt
optimizer to help you suggest more
effective prompts to GPT-5.
And finally, iterate systematically.
Edit one variable of your prompt or your
tool calls at a time.
And we published documentation a few
weeks ago that walk you through these
steps.
So, today, GPT-5 Pro is available in the

[00:09]
API.
It's the same model which is available
in ChatGPT.
And it's even smarter than GPT-5.
It's more expensive. It thinks for
longer. So, save it for moments or use
cases where precision is everything.
And I think you will find its
intelligence hard to beat.
We also announced another model today,
the highly anticipated Sora 2 in the
API.
So, now you can generate high-quality
videos directly for your application.
And there is one person at OpenAI who
was really, really excited by that
launch.
DEVELOPERS!
[Applause]
I was here this morning, that's exactly
what happened.
Um in fact, we are shipping two Sora
models in the API. One is Sora 2. The
second one is the second one is Sora 2
Pro.
So, Sora 2 is ideal for fast
experimentation.

[00:10]
So, essentially it's useful when you
iterate fast and you refine your prompt.
And once you have a prompt that works
consistently, you switch to Sora 2 Pro.
And Sora 2 Pro pays even more closer
attention to detail.
Wanted to show you a quick example. Um
InVideo is a startup building a video
creation platform.
With Sora, creators can make all kind of
videos.
So, for instance, here it's going to be
a cinematic film about New York City
being overrun by by ducks.
[Music]
Okay, it's a little dramatic. Let's make
it a little lighter.
[Music]

[00:11]
So, I wanted to show that video mostly
because that ability to re-prompt the
video can completely change the vibe and
you can feel like the the whole like
character consistency is being held
throughout.
So, super cool.
In addition to Sora 2, we are also
shipping two other models um that bring
AI to life.
So, we're going to ship smaller voice
and smaller image generation models at a
fraction of the cost of the previous
generation.
So, first we're going to ship a brand
new mini real-time model in the API.
That's the model which is being used for
speech-to-speech.
That small model is 70% less expensive
than the large model and it has on
average the same voice quality and
expressiveness. So, it's a major win.
Second, we're shipping a new image
generation model in the API. It's a

[00:12]
smaller one. It's actually the same
model that we currently use in ChatGPT.
And the model has similar quality as the
original image and model, but we are
cutting the price by 80%.
Speaking of making AI more accessible.
Earlier this year, we released GPT OSS,
our open models. The goal was very
simple. It was to truly democratize
access to AI.
And those open models give developers
flexibility to build wherever they are.
Locally, offline, or you know, for
industries with on-prem needs. And the
response from the community has been
incredible.
We've had, I think out of this morning,
23 million downloads on Hugging Face in
a couple of months. We did a hackathon
with submission from developers across
147 countries. But I wanted to show you
a quick like, you know, a few examples
that I found really cool here.
So, on the left, what you can see is
OpenSOC, Open SOC. It's essentially a

[00:13]
security operation center to automate
repeat security tasks. It It runs
locally on GPOSS for extra data
protection.
And because it's on-prem, security teams
have full control on the data, no need
for the cloud.
On the right, what you can see is a
different one. That's Lifeline Mesh.
It's a local agent which is built for
natural disasters when the networks are
down.
So, it acts as a local mesh to keep
people connected. So, for instance,
translating languages and guiding people
towards emergency resources.
So, a couple of good examples of how GPT
OSS can put AI in people's pockets.
Next, I want to talk about coding.
Over the last few months, the team has
been really really cooking on Codex. And
in fact, knowing them, I know that as I
speak, they are cooking right now.
And Codex now works across your
terminal, your IDE, GitHub, and in the
cloud.

[00:14]
And we recently made Codex even more
capable with GPT-5 Codex, which is a
version of GPT-5 which is even more
optimized for agentic coding.
That new model is really great in
particular to collaborate with you in
real time and to take on complex work by
itself.
Plus, it has what we call adaptive
thinking. That means the model can
dynamically adapt the time it spends
thinking depending on the complexity of
the task.
And developers are already building
incredible things with Codex.
For example here is um a cool tool to
visualize complex algorithm.
Um
that second one um new app uh such as an
interactive notebook for JavaScript.
And that one, yeah, some music.
Who knew that Codex would help you like
code like house music? Um yeah, I love
this Codex vibe.
Anyway, we've been blown away by how
you're putting Codex to use.

[00:15]
And today, we ship new feature to make
Codex even more useful for teams.
We have a Slack integration. And the
goal here is that you can assign tasks
to Codex directly in Slack within the
team conversation.
We have a Codex SDK. And the goal here
is that you can trigger Codex directly
within your custom workflows.
And we are also announcing a bunch of
new enterprise features, environment
controls, monitoring, analytics
dashboards.
But let's take a look at the new
features. And to that, please welcome
Roman back on stage.
Thanks, Olivier.
It's truly amazing how Codex can boost
your productivity and help your team way
ship way faster and way better products.
But let's take a closer look at some of
the new features that we're launching
today.
Earlier this morning, I showed you Codex
over a different surfaces, CLI, code
code editor, and even Codex Cloud. But

[00:16]
let's look at our at my laptop now and
bring back some memories from last
year's Dev Day for so those of you in
the audience who were there.
So, imagine we're working on one of the
last our travel app, favorite demo app.
And let's just jump on Slack
over here.
As you can see, I have a thread going
on.
And of course, Dom is pinging me as I'm
on stage. But take a look at this first
thread here. For now, I've mentioned
that the app doesn't work well on
mobile. And Dominic also added it never
got dark mode support.
And of course, what can I do now? I can
simply add Codex in the context of the
conversation to mention, "Hey, can you
please add dark mode and mobile
support?"
And then I can see right away that Codex
thumbs up and then creates a task that's
now complete.
As for Dom, I think I'm going to tag
Codex also to add Stripe later for
subscriptions. But let's take a look at
that task that Codex created. So, if I
jump over here,
you can see that I can expand the prompt

[00:17]
with the full context of that Slack
thread. It worked for 3 and 1/2 minutes
on it. And better yet, we see a
screenshot of what Codex did here. And
so, what's amazing is that you can see
the models work better when they use
tools. And in this case, the model was
able to like use Playwright in the cloud
to actually screenshot its work. So,
here we can see that it added dark mode
support and check the mobile
responsiveness of the app
like bundled into one screenshot. And
then of course, after this, I can simply
go ahead and create a PR to fix the
issue.
All right.
Now, let's take a look at something
beyond that and talking about vision and
multimodal capabilities in particular.
When you look at vision capabilities,
one of my favorite features is what we
call best of N. It's the ability for the
model to not just have vision
capabilities for the sketch or the
pictures you send, but also use those
capabilities in the cloud. So, here I'm

[00:18]
going to jump over to another
thread here.
This task I sent to
So, take a look at this for instance.
I sent a whiteboard photo from my
ChatGPT app on my phone for a new screen
to be added to one of the last like a
travel log. As you can see, it's very
low fidelity. I had some ideas, but then
in my prompt I also mentioned add a
third screen. You can make that fun and
interesting. These are just some ideas.
Make sure the app is responsive on
mobile and so on.
And what's interesting now is like not
only do I get a beautiful screenshot of
what it came up with here, I have
multiple versions of it to choose from.
Seems like a bit of a network issue
here, but
uh
there's a screenshot here as well.
And what's amazing is like um you can go
from any of these tasks and then bring
them over to your VS Code IDE. So,
imagine for instance, you're working on
one of these tasks. I'm sure you want to
use one as a starting point, pull it
down, start iterating on it. And then
the beautiful thing is that you have

[00:19]
this magical pairing with your agent
where you can either finish up the task
locally, or you can even hand it off
back to Codex in the cloud to finish to
finish to finish it up.
Uh great. So, that's kind of like
multimodality combined with Codex Cloud.
And then of course, I can use all of
that
either with CLI or the extension.
But there's one exciting thing I want to
show you today. And it's the ability to
add MCP support. We're now supporting
MCP tools inside the CLI as well as the
IDE extension. So, if we jump over here
for instance to my terminal, I can
actually type the command {slash} MCP
and you'll see I have added two new
tools.
In here, I have the Chrome DevTools MCP
as well as the Figma MCP.
And the Figma MCP in particular is very
interesting. So, take a look at this for
instance. I'm going to bring up my Figma
file, and these are some of the
beautiful design that our designer made
for Wanderlust, and we had implemented
already some of these for last year's

[00:20]
Dev Day. But, for instance, if I scroll
over here, there's one screen here, the
trip planner, that we never got the
chance to implement. And it sounds like
now we could put Codex to the task.
So,
the one thing you have to do now is like
when you enable the ability to have an
MCP server right here in the desktop app
from Figma, I can simply one of these
components, for instance, let's say this
like date picker, and I can go back to
my VS Code extension, and take a look at
this prompt I just sent before going on
stage.
Fetch the code from the selected node on
Figma, create a new date marker
component, update my chat assistant to
put it in the center with the date of
today so I can take a look. And then
right away, you can see the most
interesting piece was this one,
where automatically Codex knew it had to
pull the code of that component from the
MCP server. It even got a screenshot in
order to be able to double-check its
work later. And finally, as we take a
look at the code, we have first a new
import for this new component, and right

[00:21]
there. And then the date marker marker
that it just created. So, now if we go
back and refresh the app here,
we'll see we have this new component
already made. So, it's pretty magical
when you think about it, because now you
can implement your layouts and your
components very very quickly. It's been
really awesome to partner with the Figma
team to work on this.
But beyond Figma, we also support dozens
of MCP tools out there. And one that I
love in particular is the Chrome
DevTools. And it just launched a couple
weeks ago, so I can go back here, for
instance, in VS Code, and let me start a
new thread and say, for instance,
open the Chrome DevTools and support and
suggest three performance improvements
for my app. So, I can fire off this
task, and right away Codex will know
that I have the Chrome DevTools enabled.
It will call that and check out what's
happening. It's currently opening a
managed browser automatically, opening
the app in its own managed browser
browser, so it will be able to kind of

[00:22]
check for console warnings, for the
network activity, for the logs, and in
this particular case, the performance
metrics. And what's very exciting is
that it will come back with an answer
for me as to what can I do to implement,
you know, changes and make my app even
faster for my developers and my
customers.
And what's amazing when you think about
what that means is that Codex previously
already had access to your server logs,
but here, for the first time, it now has
access to your design files and even
your front-end logs. And along the way,
Codex can also reference Agent MD, so
you can have your coding instructions in
that format. And it sounds like it just
finished working, so we can see the full
chain of thought. And here, for
instance, it came up with three
suggestions like about my card art, what
could I do? It sounds like my app bundle
is oversized. Maybe there's a few things
I should improve to MapKit integration.
And of course, I can just then tag Codex
again to pick those changes up and make
them happen.
So, that's MCP support within CLI and

[00:23]
the IDE.
Now, everything that I've shown you is
the power of Codex at your fingertips.
But what if it's not at your fingertips?
Let's take a look at how Codex can
really be omnipresent for you and your
team and really improve your entire
workflow beyond just individual tasks.
So, going back to the browser,
if we take a look at this,
the first thing that we launched for
having like an omnipresent agent is code
reviews on GitHub. When you activate
code reviews on GitHub, now going
forward, every PR from your team will be
automatically reviewed by Codex. And
this is huge, by the way. This is not
just static analysis of code. It's
actually deeply understanding your
project, the dependencies, it's running
commands to really check your work. So,
if you take a look at this very simple
PR I added, nothing special to report.
Codex is not adding any noise, just a
little thumbs-up emoji to notice that
it's that it's all good. But more

[00:24]
interestingly, if we take a look at this
one, now you see that like Codex picked
up something on my PR where like I
definitely missed something, and it
might actually create a bug in
production. It looks like here, for
instance, I think I I did not handle all
of the cases for streaming, etc. Well,
in fact, I can just continue the
conversation and tag at Codex, can you
please fix this? So, it can actually
continue and actually make the changes I
need to make.
So, that's really convenient, and that's
really powerful. We're using now code
review at OpenAI to review every PR that
comes in.
Great. But
it doesn't
Of course, it doesn't replace your teams
doing reviews, but it's been really
really helping us catching bugs before
they hit any of you in production.
But now, with the CLI, the IDE, and
Codex in the cloud, we have this
incredible agent. And we also wanted to
make sure that we want to like offer
this agent for all of you developers
building apps and products and features.

[00:25]
And that's why we're launching today the
Codex SDK.
With Codex SDK, we made the exact same
agent available to all of you, so you
can drop it in your workflows and really
anywhere where you need a powerful
coding agent on the fly. So, a few
examples. Imagine your PagerDuty goes
off
at night, and you know, you wake up, but
that Codex has already troubleshooted
the issues in production and prepared
the fix. Or maybe you finish rolling out
a feature to production, and you now
have some dead code or feature flags
that you want to remove. That's a great
use case for Codex SDK. Or maybe you
want to up- to update your docs every
time you're shipping code. That's also
possible.
So, I want to show you here one example
that I'm very excited about, which is
the ability to bring this Codex SDK also
not just in your workflows, but in your
apps. So, if we can bring my phone on
screen,
I'll show you this example. So, it's a
little project I've been working on
using React Native. So, it's a very
simple app

[00:26]
to track workouts.
And I started to wonder, how about
making this app kind of self-evolving?
So, as I'm speaking here, let me
start a quick a quick thread here. I'll
say
update. Sounds like the the viewport is
a little off.
Update the home screen
to
add
new trends.
Let's see if this works. Ah,
guess it's like maybe hard to access
over here.
Hm.
Let me quickly run it again.
Let's see if I can open it. We'll give
it a second. But the idea is that um
the app can now un- embed a Codex SDK to
kind of magically self-evolve and reboot
automatically. So, it's like having a
coding team mate that lives inside your
product, software that's able to build
more software. And that's really the
magic behind Codex SDK. So, let's see.
Okay.
Update the home screen

[00:27]
with two new trends.
I'm going to send this task. Codex will
be running in the background, and then
it will actually take on one of these
things, inspect the repo, and as you can
see here, it's streaming structured
outputs. So, what's interesting is that
you have JSON objects fired off to you
with like every step of the way, the
planning, the writing the code, the
running the commands. And because it
preserves this context also, your agent
can think, plan, and keep improving over
time. So, now if I go back to the home
screen, it's still working, but we
should have a couple trends popping up
in a few seconds based on this task
that's currently being done. See, like
it's currently rebuilding all of the
app, searching for trend data, and
adding some more. Of course, this is
just a demo app where I put like Codex
as a new tab, but hopefully that sparks
some ideas in your mind as to how you
could have a coding agent that's really
embedded into new features for for your
users.
And meanwhile, while this is still

[00:28]
working, another way you can deploy your
Codex SDK is with a GitHub action. We're
launching a GitHub action today, so if
you want to deploy Codex, let's say in
your CI/CD pipeline, it's pretty amazing
the power you have with just a few lines
of code. Now, with the like a couple
lines, but also a prompt written in
English, you'll be able to automate any
kind of workflow that your team needs.
And there we go. We have two new,
you know, trends that happen to update
automatically in this app based on a
simple prompt and Codex SDK inside the
app updating the app in real time.
Thank you.
So, to recap, we've seen first the new
Slack integration that lets Codex
contribute directly in your team
conversations and pick up tasks from
from any place there. We've seen the
multi-modal capabilities of Codex, its
ability to call tools both in the cloud,
but also locally, like with the MCP
tools like Figma and the Chrome
DevTools. We've seen code reviews on
GitHub, so GitHub so Codex can pick up

[00:29]
like any issues before you ship them to
production. And lastly, the power of
Codex SDK, where you have the same agent
we offer in the CLI and IDE, but now
anywhere you need a coding agent. And
think about all of the possibilities
that opens up. Like any kind of team
workflow you can think of, any product
feature you're building, now you have an
amazing coding agent at your disposal to
solve hard challenges for your team or
your users.
So, Codex is really changing the way we
build software, and that makes now the
best time to be a developer. Thank you
so much, and back to you, Olivier.
Thank you, Omar.
Now, let's talk about building agents.
And I thought it might be fun to walk
you through a quick history of API
primitives. I'm pretty excited like only
a DevDay could we nerd out on API design
history with like a thousand people.
Let's do it in two minutes. We started
with completions five years ago. I think

[00:30]
Greg had like a nice like snippet. You
gave the model a prompt and the model
finished your thoughts. Simple but
limited.
And three years ago we built chat
completions and today chat completion is
the de facto industry standard. But a
lot has changed since 2000 and 2023.
Um today models are multi-model. They
call lots of tools and of course of
course they use chain of thoughts to
reason.
And that's why we built the responses
API. And the responses API is today the
flagship API for building agents. And
hundreds of thousands of developers now
use responses every single day.
And I think there are three reasons why
the responses API is the best primitive
to build agents. Number one,
the API has built-in tools. Web search,
file search, MCP. Number two, it lets
the models call multiple tools in one
single request. And number three, it
preserves reasoning tokens across turns.
And what we saw is that the design also

[00:31]
make it faster and more cost-efficient.
On multi-turn request, on average we see
that the responses API is 20% faster
than chat completions, which is a pretty
big deal for like long request.
And you know, it just takes like four
lines of code to get started. Um pretty
cool.
But of course you need way more than
just an amazing API to build agents.
I think we can all agree like building
like good agents is pretty hard. You
have to orchestrate complex workflows
from scratch, you have to find the right
prompt,
you have to deploy custom UI, plug in
data sources, set up emails. It's a ton
of work.
And that's why I really love the agent
kit announcement from today.
It takes agent key primitives and turns
them into customizable building blocks.
And all that is built on top of the
responses API with the same powerful
capabilities.
And to bring agent key to life, I'm
thrilled to invite on stage Viral who is
director of engineering at Ramp to show
us how Ramp uses agent key to build a

[00:32]
procurement agent.
Everyone, I'm Viral. I work on the
engineering team at Ramp. This your
first time hearing about us, Ramp is a
financial operations platform designed
to save companies time and money.
I want to start off with a quick pulse
check from the audience. Raise your hand
if you've ever had to buy some software
at work.
Right, a lot of hands. Now keep your
hands up if you would describe this
process as something that was smooth or
delightful.
All right, we got some boos in the
audience. All right, yeah it's it's a
pretty rough.
Buying software is really complicated.
You don't know where to go, what your
expense policy is, why you're talking to
legal, IT, maybe five other teams are
involved for some reason. And as an
employee, you're just trying to buy the
thing that you want and get back to your
work. And so at Ramp, we were trying to
think about an entirely new way to
purchase software, one that takes
minutes, not weeks.

[00:33]
We asked ourselves, what if an agent
could automate how you purchase
software? So I'm excited to share what
we've built with OpenAI's agent kit and
I'm going to take the next few minutes
to walk through how we did this.
So over here we have our buyer agent
that we've visually composed. So to
click into some of these nodes, you can
see our initial prompt saying that this
is an assistant that helps with
procurement requests. We have our
conditions here as well. We
automatically parse the intent whether
you're asking about a vendor or maybe
some purchase info.
And we even have them route to the
specific agents on the right hand side.
So let's dive into this one. This one
has built-in tools like web search. This
is really useful when we want to search
for additional information about a
vendor, going into like a
vendor's pricing page, looking up
security documentation, getting some
trust center information. And it's all
built-in which is really useful.
So we can quickly preview this agent as
well. Say we're iterating on this live.

[00:34]
And my team has been using ChatGPT a
lot. And so why don't we have a request
for five more ChatGPT business seats?
We can fire that off.
And the agent starts processing the
request, goes through the conditions,
and now it's fetching additional
software details and you can see the
agent start to reason about the purchase
summary.
I would have had to do this manually
before, so I definitely prefer an agent
going and and looking up all this
information.
Still reasoning.
Now it's formatting it. All right,
finally we have the output. So it looks
accurate. OpenAI ChatGPT business start

[00:35]
date of this month, end date one year
from now, volume five seats. But I don't
know about you, but I definitely would
not click this if I was shown shown it
in in any app. And so we might want to
make this a lot better and and a lot
more trustworthy for our users. So we're
going to actually spend some time
updating this with OpenAI's agent kit
widget builder.
So I was working on this over lunch time
a little bit and this is kind of the
summary we have. Definitely looks a lot
better. Maybe let's make a slight tweak
over here to say what is it for instead
of vendor since that'll be really clear.
And you can see it update on the right
hand side live and we've personally
found this to be really useful when
we're working with our design team and
we want to iterate on the right UX. You
can just go into widget builder and
update something really quickly and the
most magical thing is is that you can
click download right over here. And
it'll go to my downloads file
and then we can go back into agent
builder,

[00:36]
close the preview, and we'll click this
node.
And you saw the JSON getting
updated or sent before. So we're going
to change this to a widget and then add
in the widget that we just exported.
Yeah, that looks exactly what like what
we had before.
So now that we've kind of designed the
widget to be a lot more trustworthy and
and look a lot better,
maybe let's go off and deploy it. So we
can actually click the code button over
here and I can copy this workflow ID and
and put this in my back-end code. Or if
I don't have any back-end setup, I can
click the agents SDK tab over here and
copy the generated TypeScript or Python.
This is really useful when we're working
on new product types and having all the
scaffolding included here
is is really easy and you can see it's
quite extensive.
So I've already been setting this up on
my local dev environment and I've copied
over the workflow ID. So let's just jump
into the Ramp dashboard now.
So this is the Ramp dashboard. This is
what users see when they go into Ramp.

[00:37]
And if I click this AI assistant tab
over here, this experience on the right
hand side is completely powered by chat
kit and I've even had it match Ramp's
brand colors with custom theming. So
let's add the same prompt from before.
So I need five more chat GPT
business seats.
And I have an invoice here as well that
I can drag in.
So you can see the agent start to
reason. It's fetching business vendors,
searching the web for ChatGPT business.
It's checking this request against our
expense policy. I don't know about you,
but I don't know where company's expense
policy even is, so I'm glad it's
approved. And just like that we have the
card that we're working on.
And we can go off and submit it.
Awesome.
That was way less painful than than
before.
So this specific trace worked really

[00:38]
well and it was a success, but if we
deploy this to production,
we'd want to monitor how this agent was
going. So we can actually do that really
easily just by clicking this logs tab
over here. And I can look at this one by
one, but at Ramp scale if we had
thousands of these, I definitely don't
have the time to be looking at that
every single day. So we can actually
create a grader that can assess whether
the agent is following the instructions
that we have. So
I've already pasted in Ramp's product
copy guidelines, so we want to make sure
that the agent is brief
and if errors do happen that they're
clearly explained, not just saying
error, something went wrong which I'm
sure everyone has noticed before with
some agents. And so we can click run.
And it'll start grading our trace.
One of the most useful things about this
for our team is just focusing on what we
care about which is the prompt and the
context engineering part of this, not
managing any crazy ETL pipelines, making
sure that the data is in the right place
and all our environments are set up

[00:39]
properly.
And looks like this passed. So that's
great and yeah, it looks like our our
job is done here. We have a complete
agent.
So to quickly recap, we use agent
builder to create our buyer agent
workflow, deployed it to chat kit, and
optimized it with trace grading. Result,
purchasing that used to take a couple
days or weeks now takes less than a
couple minutes. And our teams can spend
a lot more time on things that they
actually care about, not managing
procurement requests.
Our mission at Ramp is to save companies
time and money and we're excited about
all the off opportunities agent kit
offers to accelerate that. Thank you so
much.
That was awesome.
Thank you so much, Vival.
Before we move on from that topic, I
want to remind you of some new things
you can do with Agent Kit.
First, you don't have to start your
workflows from scratch. With Agent
Builder, we give you out-of-the-box

[00:40]
templates.
Here is one simple example here, uh
which is a template to help you build
customer support um agents. It's
complete with logic and guardrails, so
you know, pretty good to get started.
Second, Chat Kit supports visual widgets
to bring your conversations to life. So,
you can create widgets to display
charts, send emails, and make purchases
in chat. And all of that matches the
look and feel of your brand.
Third, you can now automatically improve
your prompts in our Evals product. So,
we did a massive update to our Evals
product. You just take a completed Eval
run,
you let the tool suggest a new prompt,
and then you run the Eval again to
measure the difference.
And many of our customers have been
getting real big value out of the Evals
product.
Take for example, Carlyle. So, Carlyle
for you for those of you who are not
aware is a global investment firm. They
use Evals to increase accuracy by 30% of
their due diligence agent.

[00:41]
Um another example which I love is
Rippling, HR software company, which is
building sales agents and cut
development time by 30% with Evals. So,
yeah, do not sleep on Evals.
And finally, the fourth uh thing you can
do is a reinforcement fine-tuning, RFT,
specifically for agents.
Today, we are extending the RFT to tool
calls. So, models can call the right
tools at the right times, which is of
course critical for agents.
And we are also shipping custom graders,
so you can measure performance on what
matters the most to you.
And many top startups have been finding
real value with RFT.
One example is Ambience. So, Ambience is
a health care startup, and they saw a
15% improvement on their internal Evals
with RFT.
Second example is Cognition, the maker
of Devin, and found that GPT-5 could now
solve hard coding problems 50% faster
with RFT because of less reasoning

[00:42]
tokens.
Finally, let's deep dive into how you
can build apps for ChatGPT.
So, as Sam mentioned earlier, the Apps
SDK is available in preview starting
today. So, you can start building and
testing fully interactive applications
inside ChatGPT.
And users will be able to chat with your
apps, so you know, they can also respond
to natural language.
It's built on top of MCP, which is a
backbone that syncs your app server, the
model, and the UI, so everything just
works together.
You are free to run your backend on
Node, Python, or any other language
which is supported by MCP.
And you can also bring your own code um
to the front end through React or any
other framework.
And that means, and it was really
important for us, is that you have full
control over the entire chat experience
for your users.
You've heard a lot of things about this
already, and so we thought it would be

[00:43]
fun to take a look at the developer
experience. So, let me invite Katya on
stage.
Thank you.
Hi everyone. I'm Katya, and I'm on the
developer experience team.
Great. So, let's see how we can start
from an existing MCP service to surface
a custom app in ChatGPT.
So, let me close this
and pull up my laptop. So, I heard we
have an MCP server to connect to the
lights in this venue, right? This
morning at the keynote, Roman showed how
we can use MCP tools and the real-time
API to change the lighting in this very
room through voice.
So, now let me show you something really
cool and new, which is controlling these
lights from ChatGPT.
Imagine being able to control any
system, access any tools directly from
the ChatGPT interface. So, let me show
you how we can do that.
So, here I'm adding this MCP server as a

[00:44]
connector to ChatGPT.
The server is running locally, but I'm
using ngrok to expose it to the internet
so that ChatGPT can see it. Very
convenient for local developments. And
this is available when you have
developer mode enabled, and it's a great
way to test integrations with ChatGPT.
Great. So, we have our MCP server here
connected uh to our tools, and these
tools, so for example, we have one tools
to uh list the tracks that are available
in the lighting system, so the lighting
cues. We also have one tool to actually
play the track. And as Olivia mentioned,
the Apps SDK allows extending the MCP
protocol to return UI components or
widgets along with the tools.
Great. So, now that we've added uh the
connector to our app, I'm actually going
to start a new conversation here and
enable it.
And I'm going to ask um
which lighting tracks are available.

[00:45]
And so,
ChatGPT is fetching the tools from my
MCP server, and it's going to find the
one corresponding to the one thing that
I asked, so list tracks.
And since my MCP server returns widget
data along with my tools, ChatGPT will
be able to render the UI directly in the
interface.
Perfect. So, now I actually want to try
and see if this works. I hope so.
So, let's play a track.
Great. It works.
Uh but that's not all.
I can also uh say in the conversation
that I want to play uh this um moving
colors light track. So, let's do that.
Let's play the moving colors
track.
And so, again,
ChatGPT will call my MCP server, this
time with the play uh track tool. So,

[00:46]
let's see what it's doing. It's calling
the tool, and uh you can really
transition seamlessly from apps to
conversations. But another cool thing
you get with the Apps SDK is the concept
of widget state. So, let's see a
concrete example.
I have this step sequencer component
here that lets you compose a new
sequence with lighting tracks that
connect to the same lighting system.
It's just a React component, so I'm
completely free to build this the way
I'm used to. So, the good news is if
you're a web developer, technically,
you're already an Apps SDK developer.
There's no new language or new framework
to learn.
And I also have this tool here in my MCP
server called create sequence that takes
parameters that represent the state of
the different tracks, the sequence, and
we're also passing in our UI components
here.
So, we've extended the MCP protocol with
a series of meta fields that contain all
the information needed on our app and

[00:47]
how to connect the tool to the static
assets.
And this is not something OpenAI
specific, right? The idea is that all
MCP developers adopt this new standard
so that compatible clients, like ChatGPT
for example, can render UI components
along with MCP tool calls.
Okay, so let's go back to our
uh conversation. Actually, I'm going to
create a new one, and uh I am going to
say I want to
create
a new sequence.
Help me make it upbeat. Surprise me.
Great.
And I wanted to have this whole
ambience, you know, so I also added the
ability to add soundtracks.
So, the model is now calling our tool,
thinking about what the right initial
state for that component should be. So,
we have an initial state in our sequence
that will uh work great with what I
asked. So, I asked for an upbeat
situation, so let's see what it comes up

[00:48]
with. So, this will take a few seconds.
So, this is the beat that ChatGPT came
up with.
[Applause]
So, let's actually play this. Let's hear
it. Let's hear it.
[Music]
Okay. Okay. It's good. It's good. I feel
like it could be a little bit better.
So, you know what? I'm actually going to
open this in full screen and just uh
play around with it. So, I'm going to
add this clap uh track here and just add
a little bit more beats. Okay, I'm just
going to preview the audio here. I don't
want to blind you.
[Music]
Okay.
That sounds cool. That sounds cool, but
I feel like it's still missing
something. So, what I'm going to do is
I'm going to save the state of um the
the sequence here, and then I'm going to
say, "Please add a uh tom track to make
it
even more upbeat." Let me remove the

[00:49]
thinking here so it's faster. Please add
a tom track.
Upbeat.
And let's go.
We can see it with the lights, too.
[Music]
Okay.
Great.
[Music]
Wait, I'm going to refresh this because
it's it's it's taking a while. Okay, so
our toms are here, and if we want to see
the full result,
let's hear it.
Okay.
[Music]
I I like this one's really cool.
So, it's a two-way communication channel
and you can really build
visual rich experiences that are
actually part of the conversation.
So, this was just one example uh showing
how you can build for a ChatGPT users
with this new service. But, since the
app SDK is based on MCP and supports any

[00:50]
web components with a simple API to keep
data in sync with the conversation,
technically, sky's the limit. So, let's
take a look at a couple other examples.
So, what I think is really interesting
about using apps inside ChatGPT is that
it knows you, right? So, it has context
about what you like and what you usually
do in the app. So, it can tell
uh it can, you know, call these apps and
bring that additional context in. So, I
can ask about uh the best pizza places
in town
and get customized results. So, we can
surface to recommendations to potential
users just when they need it. For
example, you know, here it knows that I
love a classic margarita, so it will
just do suggestions that are uh tailored
to my situation. And you can also uh
have the apps adapt to what users want
to see. So, for example, uh I can ask

[00:51]
which ones are the closest
and
I get a nice map
with a carousel.
Again, classic margarita.
And also, if you think about how ChatGPT
can help you learn, you can have those
visual immersive experiences
just uh for learning. So, for example, I
can ask about Earth. Can you tell me
about Earth and the solar system? So,
this one might bring back some memories
from last year's DevDay if you saw the
real-time session.
And here we go. So, we're focusing on
Earth.
And let's wait for it.
Great.
So, I'm going to open this in full page
and it's amazing. I have this whole new
way of learning visually directly inside
ChatGPT. Again, sky's the limit.

[00:52]
Cuz it's it's the sky here, but yeah.
Thank you.
Okay, so we've seen a few examples of
what you can do with apps in ChatGPT.
You can control lighting, you can create
music, you can get personalized
recommendations, and you can learn with
beautiful visuals. So, I hope these gave
you some ideas, but I'm sure you can
come up with a lot more. So, you can
start building with it today and later
this year when we open up app
submissions, you'll be able to bring
your apps to hundreds of millions of
ChatGPT users.
Thank you and back to Livia.
Thank you, Keita.
So, as Keita mentioned, we are just at
the first stage of the vision here.
The goal is to get this in your hands
early and hear your feedback so we can
iterate.
So, later this year, you will be able to
submit your applications for review and

[00:53]
publication.
We also plan to release a directory that
users can browse in order to discover
new applications. And we'll have more to
share on monetization soon.
This is just the beginning. So much of
what we build is influenced by
developers.
It's been an incredible day. Thank you
so much for being here and for
everything you're building.

</details>
