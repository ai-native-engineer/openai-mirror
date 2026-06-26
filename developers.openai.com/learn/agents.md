<!-- source: https://developers.openai.com/learn/agents/ -->

## Search developer resources

# Agents

[![API deployment checklist](https://cdn.openai.com/devhub/resources/guide-1.png)

#### API deployment checklist

Checklist for tuning Responses API applications before launch.

guide](/api/docs/guides/deployment-checklist)[![Codex Prompting Guide](https://cdn.openai.com/devhub/resources/cookbook-1.png)

#### Codex Prompting Guide

Codex models advance the frontier of intelligence and efficiency and our recommended agentic coding model. Follow this guide closely to ensure you’re getting th

cookbook](/cookbook/examples/gpt-5/codex_prompting_guide)[![Context Engineering & Coding Agents with Cursor](https://cdn.openai.com/devhub/resources/video-1.png)

#### Context Engineering & Coding Agents with Cursor

Session on structuring context for agent workflows inside the Cursor editor.

video](https://www.youtube.com/watch?v=3KAI__5dUn0)[![Live Demo Showcase: Tools That 10x Your Codebase](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:3KAI__5dUn0 -->
[![Context Engineering & Coding Agents with Cursor](https://img.youtube.com/vi/3KAI__5dUn0/hqdefault.jpg)](https://www.youtube.com/watch?v=3KAI__5dUn0)

<details>
<summary>자막: Context Engineering & Coding Agents with Cursor (18:42)</summary>

[00:00]
[Applause]
I'm Lee and I'm on the cursor team and
I'm going to talk about how building
software has evolved. So, thanks for
being here.
We started with punch cards and
terminals back in the 60s where
programming was this new superpower, but
it was inaccessible to most people. And
then in the 70s, programmers grew up
writing basic on their Apple 2s and
their Commodore 64s. Then in the 80s,
gueies started to get mainstream, but
still most programming was done on
textbased terminals. It wasn't until the
'9s and the 2000s that we started to see
programming shift to graphical
interfaces. So Front Page and
Dreamweaver, which you might remember,
allowed beginners to drag and drop and
build websites. And new editors and
idees like Visual Studio made it easier
for professionals to work in very large

[00:01]
code bases. And I of course had to add
my favorite text editor, Sublime Text
here. I'm sure some of you have used it
before. It's a good one. Now with AI,
building software is becoming more
accessible and powerful than ever.
Unlike this slower shift from terminals
to the shift to write code with AI is
really being speedrun. The progress of
decades is happening in just a few
years. And with each iteration, the
interface and the UX is changing to
allow the models to achieve more
ambitious tasks. So I'd like to talk
about context engineering and how coding
agents have evolved over the past few
years from the perspective of cursor.
I'll show how we've went from
autocompleting your next action to fully
autonomous coding agents. And finally,
we'll have Michael Curser CEO talk about
the future of where we believe software
engineering is headed.
So, let's start with TAB. One of the
products that inspired Cursor was GitHub

[00:02]
C-Pilot. It showed that with
improvements to the UX of autocomplete
and with better models, we can make
writing code much easier. We released
the first version of tab back in 2023
and the experience has evolved from
predicting the next word to the next
line and then ultimately to where your
cursor is going to go next. Tab now
handles over 400 million requests per
day. And this means we have a lot of
data about which suggestions users
accept and reject. This led to us moving
from an off-the-shelf model to training
a model specialized for next action
prediction. So to improve this model, we
use data to positively reinforce
behaviors that lead to accepted
suggestions and then negatively
reinforce rejected suggestions. And
we're able to do this in near real time.
So you can accept a suggestion and then
30 minutes later the tab model has been

[00:03]
updated using online RL based on your
feedback.
Getting this experience right has taken
a lot of iterations. There's a delicate
balance between the speed of the
suggestion, the quality of the
suggestion, and also just the general UX
for how it's displayed. If it's slower
than 200 milliseconds, it kind of takes
you out of your flow. But you also don't
want to see fast unhelpful suggestions.
So with our latest release now, we show
fewer suggestions, but we have higher
confidence that they're going to be
accepted.
We find tab really helpful for domains
where AI models just aren't as helpful
yet. And the bottleneck here really is
your own typing speed. Now, most people
type at about 40 words per minute, even
though I'm sure all of you type at 90
plus, right? We've got some amazing
typists in here.
So what would it look like if we allow
the AI models to write more code for us?
This is where coding agents come in and
this is that next evolution of coding

[00:04]
with AI. You can talk to models directly
in products like cursor or like we saw
in codeex and have them create or update
entire blocks of code.
Something we've tried really hard to
make a focus in cursor is giving you
control over the level of autonomy of
working with the models. So, one of the
first features we added back in 2023 was
prompting models to add inline
suggestions. This would take your
current line as well as the broader file
context and then pass it to the model to
suggest a diff.
Shortly after, we released our first
steps towards a coding agent, which was
a feature called composer, which some of
the longtime cursor user fans may
remember. Uh, we even have a pixelated
Twitter demo that I've included here of
one of the first versions. This made it
much easier to do multifile edits with
more of a conversational UI.
And then in 2024, we added a fully
autonomous coding agent. This saw models

[00:05]
use more tokens as they were getting
better at tool calling and it allowed
cursor to self gather its own context.
So in the previous versions, you had to
provide all of that context up front,
which was a bit more difficult. So let's
talk about some of the ways that we've
optimized the cursor agent harness.
There's been a lot of talk recently
about context engineering as an
evolution of prompt engineering, which I
personally find really helpful. As
models are getting better, getting high
quality output is less about specific
prompting tricks, although those can
still help, but it's more about giving
the models the right context. And not
just any context, but intentional
context. Models get worse at recalling
information as the size of the context
increases. And in reality, you don't
want to push the limits of the context
window. You want to use a minimal amount
of highquality tokens. And this is why
the retrieval of code is actually really
important and fundamental to context

[00:06]
engineering. So let's look at an example
of searching code in a larger codebase.
We found that when you give models very
powerful tools, it can significantly
improve the rate at which code is
accepted.
Many coding agents now use commands like
GP or RIP Grep to look for direct string
matches across files and directories.
And as new models are trained on tool
calling and agents get better at using
tools, the search quality does improve.
However, we found that you can make
searching even better by automatically
indexing your codebase and creating
embeddings. So this allows us to have
semantic search. So I can ask the agent
update the top navigation, but if the
file is actually called header.tsx, tsx
semantic search allows the agent to go
and quickly and accurately find the
correct code during the retrieval
process
for generating embeddings. We also moved
from an off-the-shelf embedding model to
training a custom model that helped us

[00:07]
produce more accurate results and we
constantly AB test the performance of
using semantic search. We found that in
comparison to using GP alone, users
would send more follow-up questions and
also spend more tokens. So semantic
search is really helpful. One of the
biggest wins though is it shifts where
the compute happens. You spend the
compute and the latency upfront during
the indexing rather than at inference
time when the agent is actually being
invoked. So in other words, you're doing
the heavy lifting offline, which means
you can get faster and cheaper responses
at runtime without sacrificing
performance and putting that on the
user. So the takeaway here is you likely
want both GP and semantic search for the
best results. And we'll have a full blog
post soon that talks about some of these
results. So giving the models better
tools helps improve their quality. But
what about the UX of actually using
these coding agents? There's been a lot
of exploration with coding CLI from
OpenAI's codeex to claude to Cursor's

[00:08]
own CLI. And the idea here is to find
the most minimal abstraction over the
model, kind of iterate on the harness
and then make the agent extensible. But
we don't believe CLIs are the final
state or the end goal of working with
coding agents. What I like about the
terminal is that it opens up a new
surface for coding agents to run. So
this can be in the CLI. It can also be
on the web or from your phone. It can be
from a bug report in Slack, which I use
all the time. It can be from a backlog
item in linear just automatically
triaged for you.
Because CLI based agents are scriptable,
you can use them in any type of
environment which is really helpful. We
use this internally to automatically
write docs or update parts of our
codebase. And it can be as simple as
just doing cursor-p and then a prompt
and having text or even structured
formats like JSON come back.
We also believe that you'll need more
specialized agents, which makes sense

[00:09]
when you see the keynote today. Last
year, we started experimenting with
using AI models to read and review code
instead of just writing and editing
code. And we made an internal tool
called Bugbot. It tried to help you find
meaningful logic bugs in your code. And
after using it internally for about 6
months, we found that it actually caught
a lot of bugs that we missed on code
reviews. So we decided to make it public
and funnily enough it actually caught a
bug which took down bugbot itself which
of course we accidentally ignored. So we
learned to then really pay attention to
those bugbot comments.
Newer models are also getting very good
at longer horizon tasks. So one way
we've pushed agents to run longer inside
of cursor is having them plan and do
more research upfront. This not only
gives you a chance to verify the
requirements of what you're trying to
build and course correct along the way,
but we've also seen it significantly
improves the quality of the code

[00:10]
generated, which makes sense, right?
You're giving the models much higher
quality input context. And to do this
well, it's more than a simple prompt
change like plan better, but you
actually need to have deeper product
integration in how you store the plans,
how you edit the files, and also giving
the model new tools.
It also makes sense to allow the agent
to create and manage a to-do list. This
gives the model the critical context so
they don't forget the task it's working
on or waste tokens. And it's like they
can have notes that they can constantly
reference. One area we're still
exploring is taking your to-dos and
making them have the same source of
truth, which is your codebase, which I
know is something that I would
personally use for smaller projects
where maybe I don't need a fully
featured task management tool.
Another important part of agent
extensibility is allowing you to package
up your workflows and then share them
with your team. So custom commands are a
way to share prompts and then rules

[00:11]
allow you to include important context
in every single agent conversation. One
way our engineers have found this really
helpful internally is packaging up our
commit standards and guidelines, putting
them in slashcomit and then being able
to pass in tickets like you pass in the
linear ticket that you're working on.
Another thing that I've noticed is that
a lot of the context engineering
breakthroughs actually happen in user
space first. So all of you the power
users figure out the workflows and the
patterns that actually work really well
and then as they get adopted they make
their way back into the core product as
features. So we see this with plans,
memories and rules are really all like
this.
Speaking of teams, you want to trust
these agents to write code for you. But
that requires keeping a human in the
loop. Which is why when the agent tries
to run shell commands, cursor will ask
you if you would like to run it just
once or if you're comfortable, you can
add it to the allow list to auto run in
the future. And all these settings can
be stored in code and explicitly shared

[00:12]
with your team, including blocking
certain shell commands or actions. Our
latest release also has custom hooks, so
you can tap into every part of the
agents run. Maybe you want to have a
shell script that runs when the agent
finishes, for example.
So, we've covered a lot of ground here.
Coding agents have evolved quite a bit
in the past year, and they're getting
better and better when you give them
very powerful tools. And as the models
have got more capable, we've actually
been able to remove overly pre precise
instructions from our system prompts
that just weren't necessary anymore. So,
what would it look like if we allowed
agents to run for significantly longer?
What is the right interface for managing
multiple coding agents?
If you're just getting started coding
with agents, I don't recommend
immediately trying to juggle multiple
agents. I mean, let's be honest, are we
really being productive running nine
CLIs in parallel?

[00:13]
Probably not.
Probably not yet, though. I mean, not
only do you need to set up your local
machine for running parallel agents, but
it's also kind of hard to review the
output of all of these agents. So, we
don't think that this form factor is the
end goal or the end state, but there is
promise here. One thing we've been dog
fooding over the past few months is a
new type of interface for managing
multiple coding agents. And we found
this really helpful internally when
maybe you have an agent in the
foreground, but you need to ask
questions about the codebase or maybe do
some research about tools you want to
integrate or small refactors. When you
have this fast coding model in the
foreground, you can really stay in the
flow and then you have your parallel
agents kind of run other tasks in the
background which could run for much
longer. Those could be in the foreground
on your machine. They can be in the
background on the cloud. Each one of
these decisions has unique constraints
that right now you have to think about
and spend a lot of time on. If you're in
the cloud, you get these sandbox virtual

[00:14]
machines, which are really nice for very
long horizon tasks, but the trade-off is
that it usually takes longer to boot up
and you have to set up some initial
configuration with the environment that
you're working in. But running agents
locally in parallel is kind of a
different type of isolation. If you have
multiple agents that are trying to
modify the same set of files on your
local machine, you need to have tools
like git work trees that allow you to
have different copies of your codebase
where you can run independently. And
then you also have to think about all
the other parts of local dev like
managing accessing your database and
viewing the work trees on different
ports today. And I I talked to some
developers early like a lot of this is
happening in userland and people are
writing scripts and hacks to make this
work really well. And what we're working
on and exploring is actually building
this natively into the cursor product.
Another idea that we've started to
explore for multiple agents is being
able to have the models compete against

[00:15]
each other. So what if you had GPT5 high
reasoning versus medium or low reasoning
and then you can pick the best result or
compare results across different model
providers with cursors agent. This will
soon be an option to go from one to n
for any given prompt and any models.
Part of context engineering for agents
is making it so they can check their own
work. So the agent needs to be able to
run the code, test it, and then verify
it's actually working correctly, which
is why we're exploring giving the agent
computer use. They can then control a
browser to view network requests or take
snapshots of the DOM and even give
feedback about the design of the page.
As you can tell, there's still a lot to
figure out on the right interface, the
right product experience for managing
multiple coding agents. Some of the
things I just showed are available in
cursor today in beta. So go try them out
if you're curious. And we'll have a
stable release later this month. But I

[00:16]
would love to hear your feedback on how
you want to work with coding agents in
the future. So come find me later and we
can talk about it. And speaking of the
future, I'd like to welcome Michael to
the stage to talk about where software
engineering is headed next.
Thanks, Lee. Our goal with cursor is to
automate coding. We think that half of
that is a model problem and an autonomy
problem. And we think that half of that
is a human computer interaction problem
of what the act of building software
looks like. We want engineers to be more
ambitious, more inventive, and more
fulfilled. And today I want to hint a
little bit at the picture of the future
that I think we can create together. one
where AI frees up more time to work on
the parts of building software that you
love.
Imagine waking up in the morning,
opening cursor, and seeing that all of
your tedious work has already been
handled. On call issues were fixed and

[00:17]
triaged overnight. Boiler plate you
never wanted to write was generated,
tested, and ready to merge. A world
where code review is actually fun, too.
Instead of being buried in your busy
work, your energy goes toward the things
that drew you to engineering in the
first place, solving hard problems,
designing beautiful systems, and
building things that matter.
Imagine agents that deeply understand
your codebase, your team style, and your
product sense. Agents that come back to
you after working for long, long, long
periods of time and show their work in
higher level programming languages.
Agents that propose ideas, help you
explore new directions, break down
complex projects into pieces you can
accept, reject, or refine. Ones that
extend your ambition, but never take
away your thinking and judgment. When
you have a problem too complex for
agents, they show you what they tried.
Pulling in runtime logs or debugging

[00:18]
tools. You'll never start from scratch.
This is the future we're working
towards. a world where building software
feels less like toil and much more like
play and where creativity is the focus.
Uh, and I think it's possible sooner
than even some of the most ambitious
people in this room think.
Uh, if this vision excites you, we'd
love to chat. And if you haven't tried
cursor, we've been shipping lots of
improvements to our agent and to our
editor. We'd love to hear what you
think. Thank you.
[Applause]

</details>


#### Live Demo Showcase: Tools That 10x Your Codebase

Live walkthrough of Codex-powered tooling that accelerates software delivery.

video](https://www.youtube.com/watch?v=-l0OqapibAA)[![ChatKit advanced samples](https://cdn.openai.com/devhub/resources/code-1.png)

<!-- yt-inline:-l0OqapibAA -->
[![Live Demo Showcase: Tools That 10x Your Codebase](https://img.youtube.com/vi/-l0OqapibAA/hqdefault.jpg)](https://www.youtube.com/watch?v=-l0OqapibAA)

<details>
<summary>자막: Live Demo Showcase: Tools That 10x Your Codebase (30:05)</summary>

[00:00]
Earlier this year, a tweet went viral
with a new term, vibe coding. Now, it
got a lot of polarizing reactions, but I
think one thing we can all agree on is
it really changed the way we saw how AI
was going to transform software
engineering and how products are built.
But we're not here today to talk about
buzzwords or hype or what might be
possible. Today, we are here to show you
startups that our team has been working
closely with and we have seen firsthand
how their AI coding tools have helped
tiny teams 10x their code base and punch
way above their weight. My name is Sarah
Urbonus and I lead startup marketing
here at OpenAI. I'm thrilled to be
joined on stage here today by four
incredible founders who have built tools
to help you write, review, ship, and fix
code faster than ever before and without

[00:01]
any of the AI slop. So, please join me
in welcoming our first speaker, founder
and CEO of Warp, Zach Lloyd.
>> Let's go.
>> All right.
Hi, I'm Zach, the founder and CEO of
Warp. I'm very excited to be here today.
Now, you've probably seen a lot of
incredible demos today of uh what
development agents can do for creating
code, but the truth is if you're a
professional developer working on a big
codebase, it actually can be hard to
apply agents to build software. Now, at
Warp, our mission has always been
empowering developers to ship great
life-changing software, and we're trying
to use agents to do that now. So for my
demo today, uh I'm going to use warp to
build something within warp, which is a
million lines of Rust code, and try and
show you how I I approach development on
real production grade code bases using
agents.

[00:02]
So
this is warp. Uh I'm going to go ahead
and get started with a prompt here just
so I can get the agent working and then
I'll explain exactly what it is that I'm
building.
Please take a look at the two attached
screenshots. The first one shows the
state of the current branch and the
second one shows the desired state that
I'm trying to build towards. In the
desired state, the QR code is at the top
of the referrals page and there's a new
button called copy invite link that's on
the same row as the email form field.
Please help me build this. Oh, and by
the way, I'm doing this live at OpenAI
dev day and I need to do it within the
next four minutes and 30 seconds, so go
quickly. Also take a look at the
reference file to see where the code is.
So I just spoke to warp. Uh this is
often actually how I start today. Warp
transcribes it for me. I owe it a couple
references here. So let me go ahead and
refer to a file and let me attach some
screenshots.

[00:03]
Um
how do I do that with this setup? Well,
there we go. So I drag those in and then
I'm going to go ahead and start the
agent. And this agent is using GPT5
which is one of the main coding models
that we use in Warp and it's very good.
So while this is going, let me pop open
another tab here in Warp or another pane
I should say. And in Warp, our roots are
as a terminal. So you can use any
terminal pane as either a place to run
terminal commands or a place to launch
agents. I'm going to go ahead and use it
here. Actually, I'm going to run a
terminal command which is going to run a
local version of Warp. I'm just going to
show you what it is that I'm working on.
So, you can see here in Warp, we have a
referrals feature. This is something
that if you're a Warp user and you want
to get cool t-shirts or swag, and
there's a little Easter egg in here. Uh,
you can you can use this and we're
adding the ability to have a QR code for
people who are demoing Warp on video so
people can get their referral link. But
our designer, Peter, actually asked me

[00:04]
to do this in a different way. So, he he
wants the QR code to be at the top of
the page. And we don't want this link
form field. We want an email form field
with a copy invite link button here. So
this is what I've asked the agent to
change for me. So let's go back and
while the agent is working here actually
let me tell you just a little bit more
about what warp is in general.
So warp is what we call an agentic
development environment. And the idea
here is that it borrows some of the best
parts of the terminal and some of the
best parts of the IDE all with a vision
of like how do you have first class
support for building with agents. And so
one way of conceiving of this is warp is
just a general purpose interface for
telling your computer what to do. And if
you tell it that it will do it. It has
four parts. We have a coding agent which
is actually really good. It's a top
three agent on both suede bench and
terminal bench. We have facilities for
multitasking with agents which I kind of
just showed you. Uh we have a really

[00:05]
really nice just terminal interface. So
if you just want to run terminal
commands and then we have a knowledge
store where you can store workflows and
data for agents and humans on your team.
So let's go back to the demo and see
where we're at.
And it looks like we've uh made some
coding changes. So I'm going to go ahead
and run a terminal command here to start
um building these. Actually
type
Um,
okay. So, I'm going to go ahead and
build this. And then while this is
building, I want to show you how I use
warp to work on real code bases. And so,
one of the key things here that I do now
as a developer, if I'm coding by prompt,
is I like to look at um exactly what the
agent is doing as it does it. And so,
actually, it looks like we have a
compiler here. Let me see if the agent
can go ahead and generate this fix for
me. Try to fix it one more time. But the
idea is that I like to see what the
agent is doing and actually have a view
where I can code review it as it goes.

[00:06]
And so that's what you get on the right
side here. I could actually add comments
for the agent to make changes. I could
revert the agents change if I wanted.
And I could even edit it. And so we've
brought in some of the editing features
of the IDE to make this experience more
smooth. So we're building here. Let me
take a look at what it's done. If it did
the right thing, which is possible. Live
demos. There's always some risk here. Uh
we're still waiting for for Rust to
build, but yeah, this looks generally
right. Determine the referral URL for
the QR code. Okay. Um and so yeah, while
this is going, the other thing that we
focus on in Warp is how do you it's
really how do you have a very tight
iteration loop as the agent works to
make sure that what it builds can
actually go all the way from prompt to
production. So hoping we get there. So
we're about to build and run. Let's take
a look
at what we've got.
Just enter this in

[00:07]
and see. It actually made the change for
me, which is awesome. It's not quite
perfect. There's a little bit of a fade
on the link here, but it put the QR code
at the top. Anyhow, thank you very much
for the time here. This is how we use
Warp to changes. You can check it out at
warp.dev. And now I'm going to go ahead
and now that we've shown you how to
write code, you'll need to review it.
And for that, I'm going to welcome Harzo
Gil, founder and CEO of Code Rabbit.
>> Thank you.
>> All right. Thank you, Jack.
>> Yeah. So, as we saw in Zach's talk,
generative AI like is the most
compelling use case for that has been in
terms of largest use case in token usage
has been the code generation. We have
seen like anywhere from 30 to 40% code
and up to even 90% code in many startups
is now being written by agent ready AI
with all the way from like tab
completion to coding agents in the
terminal in the IDE and now even like
background agents but all that volume of

[00:08]
code being written in short period of
time is now leading to like second order
effects where we have seen code reviews
are now becoming like a new bottleneck
because the shipping velocity has not
really changed in all these
organizations right And the companies
that we talk to, we hear from many many
senior developers that now they are like
overwhelmed with a large number of
review pull requests that they have to
now review which are sitting in their
backlog. And it's gotten to a point that
it's becoming like really unsustainable
for humans to really keep up with the
agentic software development. And that's
exactly where code rabbit comes in. So,
Code Ravbit is the leading AI code
review solution which provides like a
critical trust layer that sits between
your agentic software development and
your production and it kind of provides
like a central quality gate through
which you uh each developer when they
open a pull request it has to go through
and it flags all kind of issues in these
pull requests all the way from security
issues to applying best practices and

[00:09]
even enforcing custom policies. So, Code
Rabbit is like pretty popular like it's
used by over like several hundred
thousand developers each day and we have
reviewed like millions of pull requests
in the last couple of years and found
like millions of issues in those pull
requests. So, today I'm going to like
show you like a few open source
repositories where we are being used.
So, code review has a pretty massive
footprint in the open source as well and
we'll like see some examples
uh showing code rabbit in action. So the
first pull request this is a very recent
pull request from a project called clerk
which is a authentication platform and a
user management platform for nextjs and
javascript applications.
So one things I want to point out is
that unlike a lot of the generative AI
products uh code rabbit is not primarily
a chatbased interface. It's a background
agent which has which pretty much kicks
off as soon as the developers open up a
request. So it's like a background agent
with like kind of a zero activation

[00:10]
energy like you don't have to remember
to use it and within a few clicks your
entire organization gets onboarded into
our system and in this pull request like
code rabbit basically creates a sandbox
environment in its cloud service clones
the entire repository and does like a
deep analysis on the code and once it
done I mean it takes like 5 to 10
minutes it's part of your CI/CD flow and
once it's done you kind of get to see a
few things one is like from the code
changes we are able to understand what
the payload was and so that we can show
like a walkthrough of the code changes.
So if you're a human reviewer coming
into a pull request, you get like a
starting point, a bearing into what
these changes are. Another nice thing we
do is like we actually create a sequence
diagram which I think a lot of our
customers and the users love this
feature where it kind of shows you the
new logical flow that has been
introduced by this pull request.
But the main value of code ra code
rabbit has been in the form of
review comments. So we provide

[00:11]
actionable inline review comments just
like a human would which flags potential
issues and even like providing refactor
suggestions and sorted by criticality.
So in this case we found an issue which
was later addressed by the developer in
some of in in the in the in the in the
iterative commit. And in this case what
you will see that we do a couple of
things like we also provide the
developers like a way to accept
one-click suggestion. So each time we
flag an issue we also generate like a
fix for that issue which you can just
click a button in GitHub and and and it
will commit it for you. And the other
cool thing we do which a lot of our
users love is this agent to agent
handoff. So we also like generate a
prompt that you can take back to your
coding agents like warp or cursor or
codeex to actually go and fix the
changes. So creating like a feedback
loop. So using agentic software
development then coding which is the
inner loop and then during the review
stage we find all the um issues which

[00:12]
you can go back and fix using generative
AI. So what makes code rabbit so great
and what it does is the context we bring
in. For example, if I show you under the
review details, you will see that like
we're bringing in lot of additional
context all the way from understanding
the code graph. Um, where we are able to
pull in definitions from other files.
For instance, in while reviewing
tanstack.ts, we are like pulling in
definitions from other files. And also
like we are providing the users to
provide their own custom instructions so
they can tailor the reviews for their
own organization. And these instructions
could be about best practices or how
they like want to code in certain styles
and so on.
But often like the context we bring in
up front in front of the agent is not
enough like the context windows are
still small and the production code
bases seemed like are pretty vast right
so that's where like we do other thing
which is like agentic ver verification
so we run like an agentic explorer which
kind of navigates the code like a human
does and then it flags issues even in
the parts of the codebase that have not

[00:13]
changed. So in my second example which
by the way is from the bun project. Bun
as you know is like a high performance
up andcoming JavaScript runtime. And
this particular PR has been opened by
Robo Bun which by the way is their
Asiantic um software developer like it
kind of opens end toend PRs. And in this
PR if I scroll down
one of the comments you will notice is
a comment that uses the verification
agent. So as you can see what codeabit
does in this case it basically generates
shell commands terminal commands to do
code review. Essentially we are doing
code generation to do code reviews. And
in this case the agent is going in and
running a grep. I don't know how many of
you are familiar with that but it's a
tool that allows you to pull in patterns
from the codebase based on abstract
syntax trees. So it actually wrote a
pattern search to read the function
definition because it was not in the
provided context. And it's also running
running some rip crap queries on its own

[00:14]
like it's also like finding some
keywords which it can go and search in
the entire code base or in other files.
Now what this agent verification does is
two things. First of all it helps code
rabbit suppress a lot of noise because a
lot of the comments we will generally
generate as a first pass are usually
surface level comments not with the
whole picture of the codebase. The
second thing it does is it finds issues
which are like ripple effects in the
entire codebase. Right? So that's been
one of the things and the third thing I
want to show is that it's Code Rabbit is
like a very collaborative kind of a peer
uh developer on the team. Um and in this
example again from the bun project you
would see that this is an open source
contributor who made a code change which
was flagged by code rabbit but because
code rabbit does not have a lot of the
tribal knowledge it's just making a
guess that based on PR intent the code
should look some should be slightly
different and in this case the developer
goes back and says even though the error
doesn't say so the the the comment is

[00:15]
incorrect like I mean so there is some
confusion here so what codeabit does is
it replies back to the developer but
also creates a learning and learnings
are more like long-term memory. So in a
way like when code rabbit is provided
any non-obvious knowledge or a tribal
knowledge it kind of remember the facts
in like a long-term memory which it uses
in the future reviews to make the future
reviews more tailored and more relevant
because it's a central product. So your
entire team can collaboratively like
provide learnings to code rabbit and
make it better over time.
And as you can see as a follow- on
message, the developer is now engaging
code rabbit and it's very contextual
chat to come up what with with the right
kind of error message um that should be
shown for the user and that's where LLMs
have been great with like they are they
understand the UX the LLMs have been
trained on best practices. So this
becomes like a really indispensable tool
uh to bring bring into your team. Now
with that I would also like to highlight
that code rabbit has been one of the
biggest users of reasoning models in the

[00:16]
world. Now code review is one of the use
cases where we need a lot more reasoning
than even code generation like maybe
planning is other use case where you
need heavy reasoning. Um but then the
other one is code reviews and I want to
like point out that GPT5 has been like a
big game changer for our use case. So we
have seen like almost a 70% jump in
improvement than the previous generation
of reasoning models or the models that
we were using prior to GPT5 which has
vastly made code rabbit much much better
in the last few months alone.
And with that I would love to now next
introduce Riley who's a founder of
Charlie Labs who will come and talk
about how to ship software in the era of
AI.
[Applause]
Hey, I'm Riley Thomas, the founder of
Charlie Labs. Uh, Charlie is a fully
autonomous TypeScript engineer that
helps team ship code faster.
He does everything you're familiar with
from CLI and IDE based agents like

[00:17]
writing code, answering questions,
generating plans, and reviewing code.
But what makes Charlie special is that
he collaborates with your team directly
in GitHub, Linear, and Slack. writes
slopfree Typescript code fully
autonomously and proactively finds and
fixes bugs and tech. Um, Charlie is a
full team member, not just a single
agent that runs in isolation on a
laptop. Let me show you what it looks
like to work with Charlie.
Okay. Um, so these are some linear
issues that Charlie proactively created
earlier today. Um, the bugs and tech
debt. Uh, Charlie looked through our
sentry and through the repo to find
these and created the issues here. Um,
let's get started and just assign these

[00:18]
to him.
Okay. Um, so now Charlie is going to
start working on these issues. Um, and
while he Oh, so he's already updating
the status here. This is one of the nice
things is Charlie is good at showing
what he's doing. Um, so we'll look at
one of these bugs here. Let's do this
one. Um, so this came from Sentry. As
you can tell, there's the trim stack
trace. Um, and then Charlie was able to
cross reference that with the source
code that he also has access to um, to
find the relevant code that caused this
um, and correctly identify the root
cause which is using JSON object without
actually including JSON in the prompt.
So this is a great great catch. Um, the
cool thing about this is it's then very
easy for Charlie to fix because he's
already effectively figured it out. Um,
and you can see here he's posted a
comment. He is already reviewing his

[00:19]
changes, it looks like. Um, and he'll
keep going with this.
We'll come back to these in a minute.
For now, we're going to look at how to
make features with Charlie. Um, so
Charlie makes a really good collaborator
in Slack because he has access to your
source code, GitHub, Linear, and then
the intelligence of GBT with web search.
um which makes him fantastic for
brainstorming, coming up with specs, all
of that. Um so in this case, I'll
quickly show you the demo app that we're
working on. The lack of dark mode is
pretty harsh on this screen. Um so we
can fix that. Uh
looks like Adam. So the other cool thing
is you can go multiple humans in Charlie
in one thread all across GitHub, Linear,
and Slack. So, we got a plan. Um, Adam
specified he wants uh the default system

[00:20]
colors or the system theme to be the
default colors. Um, and then I asked
Charlie to create an issue and assign it
to himself. Um, I don't know about you
guys, but I have never met a developer
that likes writing linear issues. Um,
this is such a great thing to just
brainstorm and then when you're done say
clean it up,
which we can look at.
So got pretty standard issue here. He's
actually put the right label on. Um and
then also the call out from Adam in the
thread for the default theme. And then
again, so this happened uh earlier today
and Charlie already has a PR for this
that we can look at.
Um, one of the nice things about
Charlie's PRs is that uh because he's
running in a VM, he can run all of your
tests and types and all of that. Um,
which means CI normally passes when he
opens PRs. And then for added

[00:21]
confidence, he'll also show you which
commands uh he ran to verify the work
before opening the PR.
Let's check and make sure it works.
Look at that. We got dark mode. And
that's system because it's dark. We can
go light back to dark. Um, he also does
a quick review of his own PRs. This is a
great way to catch more issues. As
you're all aware, different context
makes him better at catching things.
Like we run review within the agent
loop, but then starting it again without
the context from GitHub is another layer
of safety, which in this case, it looks
like he actually caught uh
our our custom instructions say to use
named exports. It's using a default
export. Um so we can actually get them
to fix that. But I'm also going to just
as a reminder for you guys, this is like
a toggle list here. We'll change that to
a dropdown. So then you can review

[00:22]
Charlie's PR's.
Um, you can comment whatever you want in
here, but we're just going to say,
uh,
address your own
feedback
and change to it.
We go request changes.
Um,
and then now couple minutes from now,
Charlie will have a PR that changes that
default export to a named export and uh
adds a drop down.
So, let's go back and see how the bugs
are doing.
Look at that. We have PRs for a large
number of these um fully autonomously.
And we can take a quick look and make
sure
that our CI is passing.
Yep. All green all the way across.

[00:23]
So, that's an overview of what you can
do with a fully autonomous parallelized
agents. Um, it's important to think the
alternative to this would be wrangling a
bunch of local agents, uh, creating
branches manually, PRs manually, and if
you want to get fancy and parallelize
it, you would have the pleasure of
working with git work trees.
Um, and now we've showed you how to
write, review, and ship code. Um,
sometimes things break. Next up is Danny
Grant, the founder of jam.dev, to talk
about fixing bugs in production.
>> Sounds great.
We started Jam thinking, how do we make
software a lot faster to develop and add
more fun to it?
Dare I say vibes.
If you're not one of the hundreds of

[00:24]
thousands of people using Jam for bug
reports, you should try it. It's
awesome. But today, I want to talk about
what's next for fixing software.
We started thinking, what if you don't
have to file a bug report? What if when
the designer, PM, founder sees something
in production that they want to fix,
what if they don't actually have to ask
anyone to fix it? What if they could
just fix it themselves?
We thought it would be amazing to turn
the browser into an editor so that when
you see something that could be a little
bit better, you can make it happen. You
can just edit your site right there,
right on the page, and let an AI handle
taking your edits and turning them into
a PR.
We call it Okay, well, we named it after
the two words you're never going to have
to hear again. I'm so excited to show
you please Fix.

[00:25]
I'm going to demo Please Fix on Jam's
own website so you can see just how easy
it is to edit a live site.
One of the most common edits people
always want to make is copy. So with
please fix, here's how you do it. While
you're looking at your own site, when
you see copy you want to change, you
just click on the please fix extension.
Then you select the copy you want to
change and you just change it right
there. And when you're happy with it,
you hit submit and please fix creates
the PR for you. You can also edit
designs. So like let's make the subtitle
a little nicer. Let's make it a little
bolder. and a little smaller. And we can
change the colors. All of these tokens
in the editor are pulled from your
codebase, your design system, so
everything stays consistent and really
clean. We have a powerful editor in
line, but you don't even have to use it
if you don't want to. You can just ask
please fix to make changes for you, like
make this QR code 30% bigger, and please

[00:26]
fix is going to make that change for
you.
Like any editor, you can select multiple
elements and edit them all together. So,
let's select a bunch of images and we
can edit them in the editor or we can
also ask please fix to do something with
them. Should we add a CSS animation?
Yeah, animate these image sections
so they scale
like from 50%
when they appear on scroll.
This is totally the type of stuff that a
designer really hopes an engineer will
be able to get to before a big launch,
right? The designer puts like 20 like
kind of requests into the engineer. they
get prioritized by the PM and the
engineer gets to let's say five. This
way actually you can move without
bottlenecks on specific people. You can
move at the speed of your entire
creative team. The developer doesn't

[00:27]
have disruptions. Rather they just get
to focus on the hardest problems
building new features while everyone
gets to contribute what they can. Let's
see the animation it made. I'm going to
scroll down. You ready?
Oh, it's nice.
Hey, you know what else would be really
cool? You know, sometimes you design
something in your Figma and then you
need to apply it to your live site.
Well, what if we could just tell Please
Fix to do that for us. So, we've
actually designed an FAQ section for
this site.
And
let's have Please fix it. I'm just going
to take a screenshot of it.
And I'm going to ask please fix
to add this FAQ section attached
like an email below this and we'll say
what below which section because I want
it right below the last section of the
site.

[00:28]
There's a whole lot of GPT5 GPT5 codecs
below the scenes here and a lot of
codecs to build this. They are super
powerful models. Thanks, OpenAI.
We actually tried to build this exact
product five years ago when we first
started the company. And because there
weren't LLMs yet, we couldn't. It wasn't
production ready. And so that's why I'm
so excited to be able to show you this
today and for this to be something that
you can really use. Cool. We've got an
FAQ section. I think it looks great.
Once you're done editing your site, you
just review the changes and you can
submit a PR. So, this takes a little
while. So, I have one ready for us to
look at.
This is what a PR looks like by Please
Fix. It's really short, sweet, easy to
skim, see it in a preview branch. Uh,
when you look at the code changes that
pulls from your design system and reuses

[00:29]
whatever you're using. So, in our case,
it detects that we're using Tailwinds
and it reuses our Tailwinds classes. I'm
so excited to see what you all are going
to build with this. Go to
jam.dev/pleasfix
to sign up and let's build a whole lot
more software together. This has been
fun. Thanks y'all.
[Applause]
Awesome. Thanks, Danny. Our team works
with incredible founders from all over
the world, but not many are crazy enough
to get up on stage and live demo at one
of the biggest developer events. So,
let's give them another round of
applause. Awesome job you all.
All of the founders will be outside if
you would like to meet them, learn more
about what they're building and how you
can use it at your own startups or
building your own applications. Thank
you all for joining our first ever live
demo showcase at Devday and hope you
have a great rest of your day. Thank
you.
[Applause]

</details>


#### ChatKit advanced samples

Advanced samples showcasing the capabilities of ChatKit (part of AgentKit).

code](https://github.com/openai/openai-chatkit-advanced-samples)[![ChatKit starter app](https://cdn.openai.com/devhub/resources/code-2.png)

#### ChatKit starter app

Integrate ChatKit with an Agent Builder workflow in your application.

code](https://github.com/openai/openai-chatkit-starter-app)[![Agents SDK — Python](https://cdn.openai.com/devhub/resources/code-3.png)

#### Agents SDK — Python

Python SDK for developing agents with OpenAI.

code](https://github.com/openai/openai-agents-python)[![Agents SDK — TypeScript](https://cdn.openai.com/devhub/resources/code-4.png)

#### Agents SDK — TypeScript

TypeScript SDK for developing agents with OpenAI.

code](https://github.com/openai/openai-agents-js)[![Agents SDK quickstart](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Agents SDK quickstart

Step-by-step guide to quickly build agents with the OpenAI Agents SDK.

guide](https://openai.github.io/openai-agents-python/quickstart/)[![Agents SDK quickstart](https://cdn.openai.com/devhub/resources/code-1.png)

#### Agents SDK quickstart

Quickstart project for building agents with the Agents SDK.

code](https://openai.github.io/openai-agents-python/quickstart/)[![Background mode guide](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Background mode guide

Guide to running tasks in the background with Responses.

guide](https://platform.openai.com/docs/guides/background)[![Build hour — agentic tool calling](https://cdn.openai.com/devhub/resources/video-3.png)

#### Build hour — agentic tool calling

Build hour giving an overview of agentic tool calling.

video](https://webinar.openai.com/on-demand/d1a99ac5-8de8-43c5-b209-21903d76b5b2)[![Build hour — built-in tools](https://cdn.openai.com/devhub/resources/video-4.png)

#### Build hour — built-in tools

Build hour giving an overview of built-in tools available in the Responses API.

video](https://webinar.openai.com/on-demand/c17a0484-d32c-4359-b5ee-d318dad51586)[![Building agents guide](https://cdn.openai.com/devhub/resources/guide-4.png)

#### Building agents guide

Official guide to building agents using the OpenAI platform.

guide](https://platform.openai.com/docs/guides/agents)[![Building guardrails for agents](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Building guardrails for agents

Guide to implementing safeguards and guardrails in agent applications.

guide](https://openai.github.io/openai-agents-python/guardrails/)[![Computer Use API — starter app](https://cdn.openai.com/devhub/resources/code-2.png)

#### Computer Use API — starter app

Sample app showcasing Computer Use API integration.

code](https://github.com/openai/openai-cua-sample-app)[![Conversation state guide](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Conversation state guide

Guide for managing conversation state with the Responses API.

guide](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses)[![OpenAI models page](https://cdn.openai.com/devhub/resources/guide-3.png)

#### OpenAI models page

Overview of the models available on the OpenAI platform.

guide](https://platform.openai.com/docs/models)[![Orchestrating multiple agents](https://cdn.openai.com/devhub/resources/guide-4.png)

#### Orchestrating multiple agents

Guide to coordinating multiple agents with shared context.

guide](https://openai.github.io/openai-agents-python/multi_agent/)[![Realtime agent demo](https://cdn.openai.com/devhub/resources/video-1.png)

#### Realtime agent demo

Video introduction to the TypeScript Agents SDK.

video](https://vimeo.com/1105243382)[![Realtime tool delegation guide](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Realtime tool delegation guide

Guide on delegating tasks through tools in realtime agents.

guide](https://openai.github.io/openai-agents-js/guides/voice-agents/build/#delegation-through-tools)[![Responses API — tools and features](https://cdn.openai.com/devhub/resources/video-2.png)

#### Responses API — tools and features

Overview video of available tools and capabilities in the Responses API.

video](https://vimeo.com/1105245596)[![Responses guide](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Responses guide

Introduction to the Responses API and its endpoints.

guide](https://platform.openai.com/docs/api-reference/responses)[![Responses starter app](https://cdn.openai.com/devhub/resources/code-3.png)

#### Responses starter app

Starter application demonstrating OpenAI Responses API with tools.

code](https://github.com/openai/openai-responses-starter-app)[![Responses vs. chat completions guide](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Responses vs. chat completions guide

Comparison of the Responses API and Chat Completions.

guide](https://platform.openai.com/docs/guides/responses-vs-chat-completions)[![Tools overview guide](https://cdn.openai.com/devhub/resources/guide-4.png)

#### Tools overview guide

Guide covering realtime delegation through tools.

guide](https://openai.github.io/openai-agents-js/guides/voice-agents/build/#delegation-through-tools)[![Tracing module](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Tracing module

Guide to monitoring and debugging agents with tracing.

guide](https://openai.github.io/openai-agents-python/tracing/)[![Unlock agentic power — Agents SDK](https://cdn.openai.com/devhub/resources/video-3.png)

#### Unlock agentic power — Agents SDK

Video demonstrating advanced capabilities of the Agents SDK.

video](https://vimeo.com/1105245234)[![Voice agents guide](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Voice agents guide

Guide to building voice agents using speech-to-speech API.

guide](https://platform.openai.com/docs/guides/voice-agents)[![CS agents demo](https://cdn.openai.com/devhub/resources/code-4.png)

#### CS agents demo

Demo showcasing customer service agents orchestration.

code](https://github.com/openai/openai-cs-agents-demo)[![Realtime agents starter app](https://cdn.openai.com/devhub/resources/code-1.png)

#### Realtime agents starter app

Starter app demonstrating realtime agent capabilities.

code](https://github.com/openai/openai-realtime-agents)[![Support agent demo](https://cdn.openai.com/devhub/resources/code-2.png)

#### Support agent demo

Demo showing a customer support agent with a human in the loop.

code](https://github.com/openai/openai-support-agent-demo)[![Eval Driven System Design - From Prototype to Production](https://cdn.openai.com/devhub/resources/cookbook-2.png)

#### Eval Driven System Design - From Prototype to Production

Cookbook for eval-driven design of a receipt parsing automation workflow.

cookbook](/cookbook/examples/partners/eval_driven_system_design/receipt_inspection)[![Multi-Agent Portfolio Collaboration with OpenAI Agents SDK](https://cdn.openai.com/devhub/resources/cookbook-3.png)

#### Multi-Agent Portfolio Collaboration with OpenAI Agents SDK

Cookbook for multi-agent portfolio analysis workflows using the OpenAI Agents SDK.

cookbook](/cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration)[![o3/o4-mini Function Calling Guide](https://cdn.openai.com/devhub/resources/cookbook-4.png)

#### o3/o4-mini Function Calling Guide

Cookbook to improve o3/o4-mini function calling with prompt best practices.

cookbook](/cookbook/examples/o-series/o3o4-mini_prompting_guide)[![Evals API Use-case - Responses Evaluation](https://cdn.openai.com/devhub/resources/cookbook-1.png)

#### Evals API Use-case - Responses Evaluation

Cookbook to evaluate new models against stored Responses API logs.

cookbook](/cookbook/examples/evaluation/use-cases/responses-evaluation)[![Multi-Tool Orchestration with RAG approach using OpenAI's Responses API](https://cdn.openai.com/devhub/resources/cookbook-2.png)

#### Multi-Tool Orchestration with RAG approach using OpenAI's Responses API

Cookbook to route queries across tools with RAG using the Responses API.

cookbook](/cookbook/examples/responses_api/responses_api_tool_orchestration)[![Doing RAG on PDFs using File Search in the Responses API](https://cdn.openai.com/devhub/resources/cookbook-3.png)

#### Doing RAG on PDFs using File Search in the Responses API

Cookbook to search PDFs with the Responses API file search tool.

cookbook](/cookbook/examples/file_search_responses)[![Orchestrating Agents: Routines and Handoffs](https://cdn.openai.com/devhub/resources/cookbook-4.png)

#### Orchestrating Agents: Routines and Handoffs

Cookbook for orchestrating agent workflows with routines and handoffs.

cookbook](/cookbook/examples/orchestrating_agents)
