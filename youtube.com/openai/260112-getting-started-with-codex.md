---
title: "Getting started with Codex"
channel: openai
url: https://www.youtube.com/watch?v=px7XlbYgk7I
youtube_id: px7XlbYgk7I
published: 2026-01-12
duration: "53:01"
captions: en-orig
---

# Getting started with Codex

[![Getting started with Codex](https://img.youtube.com/vi/px7XlbYgk7I/hqdefault.jpg)](https://www.youtube.com/watch?v=px7XlbYgk7I)

<details>
<summary>자막: Getting started with Codex (53:01)</summary>

[00:00]
Hi, welcome to today's getting started
with Codex session. I'm Derek. And I'm
Charlie. And we work with customers to
help them get on boarded to Codex.
It's a really exciting time in the AI
coding space and it's quickly changing
how developers work. So Codex is
OpenAI's coding agent that developers
can use across different surfaces and
we've seen firsthand how developers are
delegating routine and time-consuming
tasks to Codex and spending more time on
complex and novel challenges like design
and architecture. And we've seen a lot
of excitement from the developer
community about Codex and our goal this
session today is to give you a
high-level introduction to Codex.
So we're going to cover a few different
topics here. First, we're going to walk
through just the introduction to Codex,
what it is, kind of what the extent of
the product is. Then we'll talk about
installation and setup, how to get
started with Codex. We'll then dive into

[00:01]
agents.md, a readme format for Codex and
how to configure Codex with config.toml.
We'll also talk about prompting with
Codex and some of the best practices
around that. We'll give you some CLI and
IDE tips and tricks, talk about MCP
configuration and then dive into
advanced use cases and give you some
follow-up additional resources.
So you can use Codex in multiple clients
today. So the CLI allows for lightweight
interaction in the terminal. It also
offers a headless SDK mode for more
advanced programmability.
So Codex's IDE extension works with any
VS code-based IDE and really allows
developers to write code in more of a
rich graphical user interface and you
can also kick off remote tasks in a
cloud environment as needed. And with
Codex's cloud environments, it really
allows you to run multiple parallel
tasks in the background even with your
laptop closed. So it's really ideal for
kicking off async tasks like code review
or working while on the go with your
mobile phone. So for today's session,
we'll focus more on the CLI and the IDE

[00:02]
extension.
So here are a few of the ways that
customers are using Codex today and how
it can integrate with your team's
workflows. As Derek mentioned, you can
kick off code reviews in Codex cloud
when a PR gets opened and Codex can
provide comments and find critical bugs
and issues before they get merged into
production.
You can also use it with slack mention.
So you can integrate Codex into slack,
at mention it and then it picks up the
whole conversation thread that you've
maybe been chatting with your team about
and then implements it and gives you a
PR.
You can also build your own integrations
with a Codex SDK. This allows you to run
Codex programmatically in your own
containers and so you can get structured
output of code out of Codex and we'll
cover this kind of in the the back half
of the presentation here.
So OpenAI at its core is a research
company and Codex is backed by our
state-of-the-art models, most recently
GPT-5.1 Codex Max, which is our best
model for agentic coding. So it's
specifically trained in the Codex CLI

[00:03]
harness and our continuous focus will be
to have each model generation be more
efficient, be able to run faster and
longer and to generate even better
production-ready code. So our models are
natively trained
in Linux, macOS, Windows environments,
so it'll be very reliable in bash and
PowerShell and will adhere to the
sandboxing rules. We also train the
model to be able to accurately
auto-compact long conversations, so you
can have Codex work for you on
longer-running tasks. So for example,
really large-scale refactor tasks. Yeah,
Windows support and those long-running
tasks are like maybe the two of the
biggest feature requests we've been
getting with Codex.
And we also recently published a guide
that tells your team how to build an
AI-native engineering team. It goes
through how we can use coding agents to
accelerate different parts of the
software development life cycle. We
broke it down into seven phases that
span planning and design all the way to
documentation and maintenance. And as we
go through today's session, I would just
encourage you to think about how Codex

[00:04]
can help your team in these different
areas. Even though we're starting with
just the basics here, all of this is
applicable throughout the software
development life cycle.
So let's get started. As a quick
reminder again, the focus of today's
session is the CLI and the IDE surfaces.
We'll be using an open-source
repository. So if you're new to Codex,
we definitely encourage you to follow
along using the same repository or just
repository of your choice.
So let's dive right in. So how do we get
started? Let's start with installing
Codex CLI on your local machine. So you
can install in a couple ways. You can
install using brew or npm, which is the
suggested method since it's going to be
the most up-to-date. Our team ships
very, very quickly, sometimes multiple
times per week. So this way you're
always going to be on top of the latest
release. When you run Codex sessions as
well, there's going to be a banner on
the top you if you if there's a newer

[00:05]
version to update to.
If you want, you can look at the latest
binary releases on GitHub since Codex is
open-source, Codex CLI is open-source.
And you can also look at the change log
on our developers' website for more
specific changes for each version.
So you can install the
Codex CLI extension in VS Code as well.
And so to do that, you can open VS Code
and click on the extensions tab here and
search OpenAI Codex. And so you want to
make sure you're looking at the official
one made by OpenAI as seen here. And
when you download it, you'll see the
version that you have and you'll be able
to switch between pre-release version
and the release candidate. And you can
also toggle on auto-update or not. I
definitely recommend toggling on
auto-updates since you want to make sure
you're seeing the latest updates for the
IDE extension.
So let's talk about actually signing in

[00:06]
with
your ChatGPT Enterprise account to use
Codex. So there's two different ways and
if you use either way, you'll be signed
in on both sides. So on the IDE
extension, when you first open it,
you'll be able to see a splash screen
that says sign in. And so when you click
on that, it'll bring you to a sign-in
page similar to how you'll see on the
Codex CLI, which I'll demonstrate now.
So in the Codex CLI, all you need to do
is type Codex login, which will take you
to a page where you can sign in with
your work email. It'll probably route
you through your internal SSO to be able
to log in. And once you're you're done
with that, you'll be able to start using
Codex locally on your computer on the
CLI and the IDE extension.
So let me go back here. And so once
you're in Codex CLI, I'll show you how
to start running it in a second. You'll
see that there's a couple slash commands
that I'll note throughout this session.
The first one is slash status. This just
gives you a high-level overview of the

[00:07]
model that you're using, the directory,
the sandbox mode, the approval policy,
how much context window you have left.
So for example, just to go back to the
CLI here, I'm on this specific version,
I'm using this model and currently in
the agents.md
directory. And so what you can do is go
to slash status and you'll see here that
I'm using this specific set of
configurations
with my account and my session ID as
well.
And so let's get started by cloning the
repository that we'll be using here
today. So we're using the agents.md
website, which you'll see here.
So Charlie will talk more about
agents.md and why it's very important.
But for today, we'll be cloning this
repository that's open-source. So once
you clone that repository through this
link below, just CD into that file,
install npm and then npm run dev. So

[00:08]
you'll be able to run it locally and I
will do the same here
as well. npm run dev. It's kind of meta
we're using the agents.md microsite
>> [laughter]
>> while also talking about agents.md and
the IDE extension. Yeah.
But you know, We want to hammer in
agents.md today. Yeah.
Awesome. So we've set up agents.md and
I'm running it locally now.
So I'll hand it over to Charlie to to
take a little deeper on agents.md.
Great. All right, so we have a project
set up and we want to work on it.
>> [snorts]
>> We can use agents.md to help get Codex
clued in to how this project is going to
work. Why do we need an agents.md? Well,
when you think about it, coding agents
don't really retain any context between
sessions. Every time you start it up,
it's coming in with a fresh context
window. Agents.md ensures that the
instructions that you want to give the
agent, to just give it the background,
the TLDR on your project, are always

[00:09]
loaded automatically. Codex will always
load this file in if it's in the
directory where you're starting Codex.
You can use it basically as a
lightweight readme that allows your
agent to quickly understand and get up
to speed on your project and just get
that context it needs to actually be
able to do its work.
So there are a few different ways that
you can use agents.md. You can create it
with a slash init command in the Codex
CLI and this will auto-generate a
agents.md file for you just in the
directory where you're working. You can
also create an agents.md file in your
Codex home folder, which is a global
agents.md.
This is good for just kind of global
configs that you always want Codex to
adhere to, things like using specific
tools that are, you know, just things
that you use or different kind of ways
you want the agent to act.
You can also create different agents.md
files within your project and even
subdirectories within your project. And
these are really good for giving
repo-specific context. Usually we'll put
one in the get root of the project that
kind of is kind of a starter place for
Codex because that's where we typically

[00:10]
start up Codex. We might also include it
in subdirectories for different
services. They just tell Codex as it
goes into that directory, okay, here's
what you're actually working on here.
Here's the context that you need to pay
attention to.
Right. So, what's included in an
agent.md? Common sections that we often
have in here are the project overview
and the structure, um just giving Codex
pointers on where to go for different
files. Also, how to build the project
and running tests commands.
Doing helpful CLI tools that you might
use for yourself like the GitHub CLI for
example or different MCP servers that
you want to integrate. And also giving
Codex a workflow just talking about how
to go about implementing a feature from
front to back.
Lastly, you can include pointers to
other task-specific guidance in
different files for the agent so that
the agent can do progressive discovery
as it wants to find out more about how
to do things in your project.
So, some of the best practices that we
recommend here. The first is to keep it
brief and focused. If you include too

[00:11]
many instructions, it can confuse the
the coding agent and it won't know
exactly what to pay attention to or if
they're conflicting, it can spend a lot
of time figuring out how to resolve the
conflicts.
Most of OpenAI's agent.md files and we
looked at the Monterey boat to figure
this out were less than 100 lines. So,
they really don't need to be that long.
The second recommendation is to focus on
unlocking agentic loops. So, anytime you
can give the agent feedback or a way to
get feedback from tools like linters,
tests, etc. and verify its work, it
really accelerates how much the agent
can do. And a good kind of intuition to
build here is after you run Codex, if
you're finding that you run commands to
say say check did the code compile or
maybe grab screenshots or something like
that, see if you can add those as
different commands and instructions for
Codex and have it just do that itself
and unlock those loops.
Next, we recommend continually updating
the agent.md file. As Codex encounters
mistakes that maybe it makes or kind of
gotchas. So, if you're watching Codex do
a rollout and you see it took a really

[00:12]
long time to derive the specific command
it needed to run your test suite for
example, just add that command into your
agent.md next time and watch how Codex
will pull that into its context and then
run a lot faster.
And then you can also point it to
task-specific files. And we'll talk
about this in the next section, but
basically reference other .md files from
the main agent.md file.
So, just to look at an example of this
pointing Codex to task-specific docs.
You can use agent.md to tell Codex where
else to look. Agent.md is always loaded
into context so it has to be kind of
general. And what you could do is just
add a section here that says
task-specific documentation and then
call out different task-specific
documents that are located in your
repository. For example, we might have
an execplans.md file for planning large
tasks. We might have a frontend.md file
that's specific for doing front-end
tasks. We might have an architecture.md
file that outlines specific
architectural judgment calls that you
need to make when you're doing a feature

[00:13]
that requires large architectural
changes.
Codex will read this in the agent.md,
understand that it can call on these
things in its context, and then if needs
to, it'll go and read the file and read
it into its context, which allows it
again to do progressive discovery on
these things and kind of gear up to the
different challenges you're giving it.
So, here's an example of providing a
planning template with plans.md. You can
use agent.md to point Codex to a
plans.md file. And this is basically a
template that tells the agent how to
build out a plan for larger multi-step
kind of projects that we want to take
on. Codex will generate a markdown file
using this exec plan as a template and
it can update this individual plan as a
living document. So, it'll go through
and actually check things off a
checklist
and kind of update its progress here.
And this helps Codex really run large
refactors, do large kind of cross code
base sweeps, or work on multi-hour
project tasks just more effectively by
having a place where it can track how it
executes and update as it progresses.

[00:14]
I'll note you can also use MCP servers
for this, but there's nothing like just
having a markdown file for the models to
read and having it checked into Git.
It, you know, just makes it easy for the
models to keep that context up to date.
And you can see an example of using
plans.md on the OpenAI cookbook which
I've linked to here as well. Agent.md is
really a cheat sheet at the end of the
day. And the Charlie the example of
Charlie just mentioned with plans.md,
one of our engineers was able to run a
10-plus hour refactor
with Codex and was it was successful in
the end. So, this is a great example of
what you can use Codex for today. Yeah.
All right, let's talk about how to
further customize Codex to the way you
work in addition to agent.md, which is
the configuration TOML file. So, Codex
CLI was written in Rust, hence why it's
in a TOML file. As you can see here on
the right, there's a couple different
areas that you can customize and have it

[00:15]
run as default when you have when you
start a Codex session. For example, you
can specify the default model, the
default model reasoning effort, sandbox
mode, approval policy, which I'll talk
about in the subsequent slide. You can
also toggle certain features to be
default on. For example, web search.
You can also specify different profiles.
So, for example, sometimes
I just want to start a Codex session
that defaults to
the fastest model with the lowest
reasoning effort to get the fastest
responses. So, I created a profile
called fast so I can just do Codex
{dash}p {space} fast and it'll create
that specific configuration for the
session. And as Charlie mentioned, you
know, MCP is an area that you can also
configure Codex to work with. So, in
this example, we have one of the MCPs
that we'll cover later in the session as
an example on the right. So, this is
just the tip of the iceberg as you can
see on
this slide here, there's a lot of
different configurations that you can do

[00:16]
with the Codex CLI.
And if you go to this website, you'll
see a lot of different uh configurations
for you. To go Yeah, one of my favorites
to set here is the terminal
notifications. It allows you to get like
a pop-up when Codex finishes a task,
which some people don't like. I actually
like it because Codex will run in the
background and like ring a bell when
it's done for me. So, that's nice, but A
lot of bells going off. Yeah.
To go back to the last slide here. So,
approval policy and sandbox mode are two
areas I just want to dive a little
further into. The default for Codex is
to have the approval mode on request,
which is Codex will run until it decides
it needs to ask you for any escalated
permissions. The other default is
workspace right as the sandbox mode.
What that does is Codex will write to
files in your current directory and not
anything outside. But as you can see
here, there's a couple configurations
that you can change with the default
when you start a Codex session.

[00:17]
Awesome. Let's turn it back over to
Charlie to talk about prompting with
Codex.
All right. So, similar to writing an
agent.md file, your prompt is kind of
the ultimate context that you want to
give Codex, right? And so, writing good
prompt really determines kind of what
you get out of Codex. There are a few
tips here which we found to be kind of
universally helpful. So, the first is to
use at mention to just point Codex to a,
you know, file within your code base
that you want to start focusing on. I
use this a lot and it doesn't
necessarily have to be the file that
you, you know, end up wanting to analyze
or kind of like pull in, but a starting
point to kind of anchor Codex where it
can start then traversing all the code
paths is really helpful.
When we see the agent kind of go off the
rails, a lot of times it's because it
starts looking in a part of the code
base where it's just not really relevant
to what you're trying to do. So, if you
can anchor it with this, super helpful.
The next recommendation is to start with
small tasks before you move on to larger
ones. So,
if you're new to prompting with a tool
like Codex, small tasks are going to be
easier for you to test out and kind of

[00:18]
review to start. And as you get more
comfortable, ramp up asking Codex to do
kind of more and more tasks and larger
units of work. But as a tip here, you
can actually use Codex to help break
tasks down. And it can do this by
looking at your code base. So, if you
ask it to do kind of just a pure
research effort to go look through your
code base and figure out how it would
implement a feature and break it into
small tasks, it'll actually come up with
very small units of work that you can
then just prompt it to do and follow up
on and follow along with.
We always recommend including
verification steps. So, provide Codex
with the steps to check its work. For
example, running tests, linters, etc. If
this isn't in your agent.md, it's good
to include in your prompt. Another way
to do this is just just tell Codex, here
are the requirements that you need to
implement in order for this feature to
be considered complete. And it can use
that as kind of a yardstick to measure
its progress as it works along.
The next is if you're debugging, which
is one of the top use cases of Codex,
just paste the full stack trace into
Codex. Give Codex the full kind of
detail there and it can use that to

[00:19]
navigate your code base and figure out
what's generating the error.
Super super helpful. Um
As we mentioned before, you can
customize how Codex does its work by
using agent.md.
And we also recommend that you try
open-ended prompts.
This can be great to just brainstorm
ideas for feature improvements or how to
improve performance.
You can ask Codex kind of after you
implement a feature, what would you
consider building next? And Codex is
actually really good at kind of looking
at your code base and holistically
considering, okay, here's what I would
add. So, [snorts] there's more on the
developers website on this and we
encourage you to check out the prompting
guide for Codex as well.
>> thing Codex does as well is Codex CLI
actually gives you next steps, suggested
next steps when you come up with when
you ask it a prompt. So, this is a great
way for you to continue the brainstorm
conversation as you said.
>> Yeah. Yeah.
So, some uh starter tasks, you know, if
you were to just try Codex today,
explain the code base, uh just write a
quick read me based on something that
you're interested in the code base or
maybe another team's code base um at

[00:20]
your company. Use it for bug fixing. Uh
just paste in the stack trace and have
it uh work on fixing a bug for you. Uh
have it expand test coverage. So take a
look at a feature and ask it, you know,
where which edge cases do we need to
consider? Um are there other things that
we need to add in here to complete our
test coverage? And it can build out this
test for you. And then also doing
refactors across many files. So maybe we
want to make a generic component that's
kind of spread across multiple different
implementations. Um Codex can look
through and identify patterns extract
that component and then make it kind of
generic across all those different
interfaces. It's really good at those
kind of refactoring tasks. And one
underrated area is writing
documentation. Uh engineers typically
don't like doing that. So I I love uh
using Codex CLI to help me write the
documentation as needed.
>> Keeps it up to date as you're as you're
building things. So let's take a look at
this in the CLI of how you can send a
read-only prompt and change the
reasoning effort uh with Codex. Um if
you're in the CLI, you can fire it up
using Codex and then use {slash} models

[00:21]
to switch between uh medium uh low,
medium, and high. Um let me pull this up
and show you what this looks like in VS
Code. Um so I'm in VS Code and I'm just
going to um pull open uh Codex in the
side panel here. Um I have a few options
down at the bottom. I can go and select
if I want to work locally, which we're
going to focus on today, but you can
also actually run tasks in the cloud. Um
so if you've connected uh Codex Cloud,
uh you can have your agent spin up a
cloud container, run multiple different
iterations in parallel on those
containers, uh and it's a great way to
get different versions going.
We can also switch the different modes
that Codex has access to here. So for
this, um I'm just going to ask it about
the code base. I'll put it into chat
mode, but I can also put it into agent
mode or agent full access mode or a
custom configuration mode here.
And then lastly, I can pick the
different reasoning models and the
different models here and also the
reasoning level uh that I want Codex to
use. This will be a pretty simple
question. I'll just say, you know, can
you can you tell me
uh about this project?

[00:22]
You can make this more custom, um and
it'll go through, it will actually
research kind of what's going on in the
project. You can see it's starting its
chain of thought here. Um and once uh it
gets going working with this, we can see
the steps that it's following. So it'll
give us a summary of what it's trying.
Uh you can actually check out uh kind of
the files uh that it's read down here.
Um and when it's done, it'll produce a
full summary for us to actually go and
review here. One of the things that I
love that's kind of a more advanced way
of using this is actually asking it to
look through the Git history and it can
use Git uh just like it would on a seal
in the command line to figure out maybe
who committed to this file or what were
the recent changes that, you know,
happened in the project. Um super super
helpful way to get on board with Codex.
>> Codex is a know-it-all historian. Yeah.
Yeah. Um so that's sending like a
read-only, you know, prompt, but
obviously we also want to be able to
make changes. So um here's an example uh
that I've already kind of uh pre-built
here. I wanted to create a simple HTML
page uh called assets.html which shows

[00:23]
how the files in this agents.md project
are related. So we could generate a
markdown file or we could generate a
whole documentation website. So let's
generate a documentation website. Um
just to show how I did this, if I go
back here and actually um view the
different uh prompts that I have, um I
can see the different conversations uh
that I have uh going here.
Um and if I go into this one, here's
where we created the uh simple HTML
um
site, I can see that it created this
assets.html file for me. I can click to
open that in the side panel. Um and I
can also go and see kind of the summary
of the chain of thought. Um so Codex
went and actually implemented this as a
file here. Um if I pull it up here and
uh grab it, it's in assets.html.
Um You can just go to Chrome and show
it.
>> And if we pull it open in Chrome here,
um I can tab over to
If I tab over to Chrome here, let me get

[00:24]
this going again here.
Um
Oop.
Is it in
>> It's right here. Oh, there we go.
If I tab over to Chrome here, I can pull
this open and we have this file that's
already kind of generated a really nice
looking like documentation page for us
here where it's calling out kind of the
different um you know, flows [snorts] in
the project where all the different
files do. Again, super simple example,
but just kind of a
quick uh run-through of what Codex can
generate really quickly for you. Um All
right. So let's go back into uh the
presentation here real quick. And um
there we go. Um so we can also send a
prompt that makes further changes to the
site. So not just kind of like
documenting things, but like changing
existing functionality. Um so that for
this one, I can say, can you implement,
you know, next to the explore examples,
view on GitHub buttons and maybe a
download button and another one to copy
the page's markdown. Um so all I need to
do to do this is open up um
a new conversation here. I'll just start

[00:25]
a new chat and say, uh can you implement
uh some hero buttons
um to download the repo,
link to GitHub,
um and copy the markdown of the site.
Let's kick that off there and um I'm
actually going to pause this real quick.
I'm going to switch it over into agent
mode so that it can go
uh and implement this for me and then
let me run this again here.
So this will kick off Codex and it will
actually go and uh work on implementing
these new buttons for us.
Uh looks like it's exploring the files.
Uh it's reading kind of our hero file to
figure out where we want to put that in
there. One of the nice things about the
IDE, it gives you these pills that kind
of allow you to click and open up the
file that Codex is referencing so you
can follow along with it. Um
It's come up with a planning uh
uh task list here that kind of shows us
how it's going to think through the
different steps that it wants to uh work

[00:26]
on. And then when it's done, it'll
actually have added these buttons to the
site for us. So
it'll just go through there a little bit
and kind of figure out exactly what it
wants to uh what it wants to add.
Um
Yeah. Okay, so we just wrapped up the
task there and then if we go over to
check out agents.md in the browser now,
you can see it's added a few different
buttons here where we can download the
repo, we can view it on GitHub, we can
copy the markdown, etc. and Codex has
just implemented that for us based off
of a simple prompt there. Um So pretty
cool how how quickly we can just
implement things with that.
All right.
I'll be here for some more CLI and IDE
tips and tricks. Thanks, Charlie. Um
let's talk about some uh different tips
and tricks uh across this two surfaces,
the CLI and the IDE. So Charlie already
mentioned this briefly earlier, but you
can point Codex to specific files in
your code base. Um for example, in the

[00:27]
CLI, um I can quickly
just at-mention any sort of file. So um
I can specify a file and ask any
question so Codex knows exactly where to
look at. Um also within the IDE
extension, I can also do the same. I can
pick a specific file. One thing to note
here as well is you can actually bind
specific keyboard shortcuts um to uh
specific functionality. So here there's
one that you can actually bind and add
context by just highlighting specific
parts of the text in a file. So I bind a
command-shift-C personally, and as you
can see here, I added context for the
hero.tsx file, um these specific 10
lines by just binding the hotkey there.
So just another tip in terms of what you
can do with the Codex um
in the CLI and the IDE extension. So you
can also use to-dos in Codex IDE and
this is a feature that I personally love
using. So for example, uh if I go back
to this uh IDE extension, I can actually

[00:28]
go to a specific part of the file. In
this case, I believe I have a to-do
already here um that asks Codex to do
something similar to what Charlie did,
which is to implement a button to
download markdown, to view on GitHub.
And once you have that to-do created,
you can actually just click on implement
with Codex. And it will actually fire
off a task on the right here. I won't
have it fully run since we've already
completed this task, but as you can see
here, you can technically have a lot of
different to-dos within um your code and
actually just have Codex implement all
of them for you, which is fantastic.
So let me go back to the slides here. So
another area that um a lot of people use
Codex for is to actually prompt Codex
with an image example. So in this case,
if I go to the agents.md file, you see
here there's no background color for uh
these three setup commands. What I can
do is actually just take a screenshot of
it and ask Codex to make the inline

[00:29]
background code chips orange. So in this
case, maybe I'll just use the um ID CLI
here since we've already used the IDE
for a couple examples. In this case,
I'll just paste in the screenshot here.
Can you make the inline um
chips
orange.
Great. So Codex is able to read that um
as you can see. Um it will explore the
code base and find exactly where it
needs to update. Um in a few seconds
here, it will be able to actually change
the background colors um of those three
setup commands to be orange. Super
helpful. Like anytime you find yourself
trying to describe like which button
third from the left or whatever like
Codex is supposed to modify or like you
just give it a image, it's to understand
the image Exactly.
>> change it based off of that.
>> As you can see here, it added a couple
lines, took out a line here. So, if I
actually go back, great, it was able to
implement according to what I asked it
to do, which is fantastic. So, um you

[00:30]
can also do this in the IDE. Just to
quickly show how that would work, you
would just click on the plus and add
image. As you can see here, I can
specify the screenshot.png that I have
on my desktop and do the exact same
thing on the IDE extension.
All right. So, one other great tip is to
um know how to resume a Codex session.
So, within the CLI, when you quit a
session, typically um people want to
sometimes go back to the session to
continue the conversation, especially
when there's still um huge amount of
context remaining. So, one thing you can
do is in the Codex CLI interface is um
just run Codex resume.
And so, what this will do is come back
with all the previous conversations that
you had with Codex, and you can actually
just go specifically back to
conversation. In this case, um I went
back to this specific conversation, and
I can just continue it. So,
this is just an example where, for
example, I can just ask Codex to change

[00:31]
the chip code to green after I changed
it to orange. So, again, this is a very
very simple example of how you can
resume conversations. Um and as you can
see within Codex CLI, there is a session
ID. So, if you want to go back to a very
specific session and not have to scroll
through um the Codex resume UI, you can
just run the specific command, and it'll
go back to that session. And uh Charlie
already um showed this earlier, but you
can always go back within the IDE and
search for a specific task and and show
that uh accordingly and continue the
conversation.
Yeah, as you can tell, context
management is just so important to
getting the right results out of there,
and that session contains all of the
context that you've given the model. So,
I use it a lot as kind of like just
almost like a mini project container for
a specific aspect of a project that I'm
working on. Maybe like I have a test
session that I'm kind of working on, or
I have like a set specific session for
implementing a front-end feature or
something like that.
>> Yeah. Definitely very very helpful.
Another great tip is you can actually

[00:32]
use Codex in the IDE extension
to generate Mermaid sequence diagrams.
So, this will show you how, you know,
the processes operate with one another
and in what order order in the repo. So,
to show this in the IDE extension, um I
can go back. Sorry, too many windows.
And actually show you that I ran this
earlier. So, all I asked is, "Provide me
a clean Mermaid sequence diagram for
this codebase." And it came back with a
very concise sequence diagram that I I
can copy, I can download. Um and this is
really great um for complex repos.
Awesome.
So, one other area that we briefly
touched on earlier is web search is
default to be off um for Codex. And so,
what you can do in the config.toml file
is to have the web search request
default to be true. If you don't have
that in your config.toml, you can also
just pass in a configuration flag. So,
in this case, you can just ask Codex
with enable web search request to add

[00:33]
something like the latest news footer uh
box that gives you the current article
of uh of the next next.js um 15. And so,
this is just in a a quick example of how
um you can pass in specific
configurations when you start a Codex
session.
And one great area that a lot of our
users use Codex for is to add specific
custom commands. So, in this case, um
you can go to your Codex home folder and
create a prompts file folder and add it
add test.md uh file as an example. So,
what this file will do is ask Codex to
generate unit tests for any of the files
that changed um and use the existing
test runner and just to keep the diffs
minimal. So, what you can do, and let me
demonstrate very quickly, is you can go
to your Codex home folder. In this case,
I just opened it within VS VS Code, and
you can create, like I mentioned, a
prompts folder, and in here I added an

[00:34]
at test.md file. And so, what that does
is if I go back to Codex CLI, um you
know, if you just added it, you should
quit and just restart it. What you'll
see is that if you type in prompts,
you'll actually see the at test.md file
here. So, when you click enter, it'll
actually uh pull in the exact uh
um instructions that you gave this uh
markdown file and actually generate the
unit tests for for any of the files that
changed. So, very very convenient, and
you know, obviously, this is just one
example of a custom command that you can
add for Codex.
So, let's move on to MCP. So, you know,
MCP is as most people know here, it's
it's really a protocol for connecting,
you know, models to any sort of
additional tools and context. So, with
Codex, we support standard IO and also
HTTP transport. And so, here are just a
couple examples of common, you know, MCP

[00:35]
servers that a lot of our customers use.
For example, people connect the Figma
MCP server, so they can generate any
sort of front-end designs based on
mockups there. Um the Jira um and Linear
MCPs are both very popular. Uh so, for
example, you can see what tickets are
assigned to you. You can have Codex
actually create the changes code changes
for you and update the ticket to done,
for example. Um you can also use, for
example, Context Seven to implement any
third-party API callouts.
And also, the DataDog MCP server is
hugely popular to diagnose any
production issues as well. But, you
know, as you know, there's a lot of
different MCP servers out there um and
Codex is able to connect to these
servers for um additional context.
So, here is just one example. Uh we
called it a cupcake MCP. This is um a
very simple example that we created just
for this session. Um so, what this does
is just returns um an example of how

[00:36]
many cupcakes someone has ordered.
Um just a very simple example here. And
to run that command um and to add the
MCP to Codex, uh what I'll do here,
um as you can see here, this is the the
uh generating unit tests um that I did
earlier. In this case, I'll I'll just
quit um and start it again. And I copied
in this command to to add this cupcake
MCP server. So, with Codex, we made it
very simple for you to just type in
Codex MCP add and add in the um
parameters. And when I click enter, um
it added a global MCP server called
cupcake MCP. And to show that it
actually did add, if I go back to the
config.toml file, as you can see here,
if I
reduce the size of this, it did add um
the
um MCP server here. So, you can also
just directly add it in your
config.toml, but we've seen a lot of our
users just use the simple Codex MCP add
as an example.

[00:37]
So, um to use one example on how to use
the cupcake MCP, so, we are going to ask
Codex to add a section at the bottom of
the agents.md page that just fetches uh
Rachel's cupcake order. Um and very
simple, um I'll just use this to
illustrate how um MCP connections work
within Codex. And so, I'm starting
another Codex session here, and I'm
going to paste in this request. And so,
as you'll see in a second, it'll be able
to call the Codex uh cupcake MCP server
and actually add this uh piece of code
at the bottom of the agents.md page.
Cool.
I'm waiting for it to pop up. It's going
to get It's going to call it.
>> Yeah, yeah, yeah.
>> [laughter]
>> It'll come in a few few seconds here.
It's analyzing the integration options
for Rachel's order. It's serious
business here. It's searching for

[00:38]
cupcake.
And
there we go. It called cupcake MCP
search and it was able to fetch her
order. As you can see here, Rachel
ordered seven marble cupcakes for
pickup. I'm getting hungry just looking
at this.
Um and what it'll do, Codex will add
this to the bottom of the agents.md
file.
So, pretty simple, but you can see how
you could extend this to, you know, for
example, like production logs that, you
know, maybe you want to pull down to
diagnose a performance issue or like
grab like a Jira ticket and like pull in
the context from that ticket for Codex
to work on. So, again, super basic
example to start, but I think like
indicates, you know, how much you can
actually do with MCP. Exactly, exactly.
I will move on to the next example as it
completes this task. So, one other MCP I
just want to mention that is hugely
popular is Context Seven, where it can
pull in the most up-to-date
documentation for uh any framework out

[00:39]
there. So, what you can also do is use a
similar Codex MCP add command to add
Context Seven as an MCP server in your
config. So, in this case, um I did
already add
um
Context Seven. So, you can see here, I
already have Context Seven present in my
config.toml file. And so, the next
example, I will use this, but I do see
that the cupcake example um was
finished. And so, let me actually go
back to the
file here, the agents.md file running
locally on my computer, and I'll reload
it.
And it should be able to show me um the
cupcakes example at the bottom.
Let me scroll to the bottom here.
There we go.
>> It looks like yes, indeed Rachel has
seven marble cupcakes ready for pickup.
So, I know what I'll be doing after this
[laughter] session.
>> [gasps]
>> All right, so let's move on to this
example, which is using context seven.
So,
this example I'm going to ask Codex to

[00:40]
implement an input on the agents MD page
running locally where people can
actually generate their own agents MD
file using a small prompt that actually
calls open AI's responses API and it'll
actually take the latest docs from
context seven to get the latest API
spec. And so, let me copy this prompt
and let's go with the IDE extension for
this example. And so, I'm going to keep
it on agents.
Maybe in this case, I'll use a different
model. I'll use GPT 51 Codex mini. I'll
use medium and I'll ask it to implement
this input for me. So, what you'll see
in a second, it's able to call
the context seven MCP and actually add
this change to to the agents MD page.
So, as you can see here, it's able to
retrieve context seven's library docs.
It's able to now explore
different files. It's reading our agents

[00:41]
MD that's present in our repository.
It looks like it's preparing to add the
agents MD generator. So,
very quickly it's able to understand
what my
request is, look at the docs and
actually read through the the different
files within this repository. And this
is super helpful, right? Because, you
know, models have so much pre-training
context, but it kind of has like a
knowledge cutoff date. And so, like as
programming frameworks evolve and
documentation gets updated, things like
context seven or really any MCP that you
want to integrate, a lot of customers
build their own internal documentation
MCPs just helps Codex stay in sync with
the actual implementation that, you
know, as it updates in real time.
Definitely. Definitely.
Awesome. See, it's continuing to work.
In this case, I will go back to the
slides and talk about the next
tip that I have, which is actually to
add
more custom instructions to your global

[00:42]
agents MD that sits in your Codex home
folder that Charlie mentioned earlier.
So, in this case,
if you don't want to have to ask Codex
to look at context seven every time, you
can actually add a specific input within
the Codex home folder, which I'll show
you here,
um, which is to actually say, when
implementing new features of any, you
know, external libraries or APIs, always
search if there is relevant
documentation on context seven. As you
can see, I have a I have a couple other
lines on my personal Codex home agents
MD file, but what this will do is
actually allow the user to not even
specify context seven and Codex will be
able to read your global agents.md and
actually call the exact same MCP server
without you specifying it, which is
fantastic. So, I believe, perfect
timing, it looks like it's about to be
done with all three. Looks like it was
able to change three files. It added

[00:43]
almost 300 lines of code.
As Charlie mentioned, you can also look
at the specific diff as well.
Looks like it's, you know, doing serious
business here looking through
>> [laughter]
>> some of the files.
Um,
all right, let's go back to this
this last tip that I have before this
prompt finishes, which is actually to
use Codex to review your code for you.
So, there's a couple ways to do that
within the CLI and the IDE. Within the
CLI, there's four options. You can have
Codex review against a specific base
branch. You can have Codex review all
your uncommitted code locally.
You can also have Codex review specific
commit. And you can also provide custom
review instructions on top. As Charlie
mentioned earlier when we were talking
about agents MD, you can actually have a
specific separate MD file that's not
directly in agents MD. So, for example,
what I've seen a lot of users do is
create a code review guidelines.md

[00:44]
that's referred to within the agents.md
file to not overflow the agents MD file
with too many lines. So, this is one
great way to steer Codex to understand
how to actually review your specific
team's code. And within the IDE, there's
also the ability to
review code as I'll show here in a
second. There is slash commands here.
So, when you click on code review, you
can also review it against a specific
base branch or review your uncommitted
changes. But before we do that, let's
take a look at what Codex was able to do
with adding this input.
So, let's go back to this file and see
if it was able to add this responses API
section. So, great. Looks like it's able
to add a section that will actually use
open AI's responses API to generate an
agents.md file with your prompt. So,
just a great way to do that. So,
I will quickly show how to

[00:45]
fire [snorts] off the code review. So,
again, you can use Codex CLI with the
review command. So, you can review your
uncommitted changes, review a specific
commit or add custom review
instructions. In this case, I'll quickly
show how it works within the IDE
extension. So, I can click on code
review here and click on review
uncommitted changes and it'll be able to
actually run through and it'll come back
with a couple
responses. Usually, it'll look to see if
there's any P0 or P1 issues and it'll
definitely surface that. It'll also
surface sometimes P2 or P3 issues
and it's just a great way to know what
you need to fix and actually ask Codex
to fix it for you because it does come
back with
a button within the IDE extension where
you can just click on it and it'll help
you fix the issue, which is pretty
awesome. Exactly. What a great way
>> [laughter]
>> to do everything in one with the Codex
CLI and the IDE extension.
>> I think one of the most important things
we found with code review is that it
really can't be too noisy. Like if it's

[00:46]
commenting on too much, people just tune
it out. And so, the model has actually
been trained to kind of really only
focus on those P0 or like P1 issues. And
sometimes they'll find P2s or like P3s,
but like I often find usually when it
comments, it's like if I don't fix this,
it's going to break in production.
>> Exactly. It's definitely It's definitely
found some
code issues internally that it helped
fix
and it's just a great way to not have an
expensive linter, right? Because it
always comes back with something that is
actually an issue that you can actually
have Codex fix for you.
Now, let's hand it back over to Charlie
to talk about some of the juicy advanced
use cases. Yeah, so one of the things
that I get really excited about with
Codex CLI is that you can use it
obviously interactively, but you can
also use it programmatically. So, you
can build it into different pipelines or
build different use cases with it that
kind of run on your own containers and
just do really whatever you want to

[00:47]
build.
So, to kind of show this, I wanted to
jump into the terminal here
and just pull up Codex and should kind
of show what this looks like. So, in our
agents MD file
in our agents MD site here, we have a
special file that I've created. I'll
actually show this over here called
Codex output schema. If I close Codex on
the side here, we can see what this is.
It's just a JSON file that adheres to
the open AI structured output schema
format. And this tells Codex precisely
the format that we need to receive a
response back in. So, for this example,
I was working on doing like a code style
analysis kind of checker. And um,
it had a few different properties. It
has to include like the number of files
that it analyzed, the total number of
issues that it found, the overall score
from zero to 100. We can also define
like an array so that we can have
individual items for every single issue
that it finds. And each of these can
have their own required fields. It's a
very extensible format. And what we can

[00:48]
do is actually run Codex with this and
do Codex exact, which is Codex's
headless mode,
analyze this app for code quality issues
and then give it this output schema
param and just have it generate JSON.
I'll fire this off here and you can see
rather than going into an interactive
terminal mode, Codex is just streaming
kind of the raw logs out, which we can
consume. But to kind of give you an
example of what this looks like, we can
see it already ran through this here.
And when it's done, it prints out this
valid JSON that we parsed with JQ.
It gives you all of the total files, the
total issues, the file citations, the
line numbers, the severity of the issue,
the description all in a structured
format. And we can do a ton of stuff
with this. For example, if we want to
make an API request for every single
issue that it finds or you want to save
each one to a database, we can build
this into an app. We can run it in our
CI/CD pipeline.
It's a very simple but powerful kind of
primitive to be able to do a lot of
programmatic work with Codex. So, what
can we use to actually build with this?

[00:49]
Um,
you can do things like security triage.
You can make a test coverage bot. You
can do a refactor and cleanup
automation. You can do a release hygiene
automation that creates change logs and
readmes every time you mint a new
release. All these things are kind of
things you can just build into the
software development life cycle here.
And on top of that, we can actually get
a bit more advanced. Instead of just
doing a single step workflow, we can
build advanced multi-step workflows with
the open AI agents SDK and Codex. So,
open AI's agents SDK
helps us build agent handoffs and scope
agent context and tooling to individual
agents. And Codex can actually work as
an MCP server within agents SDK. It
basically makes it a tool that can be
called by the agent. This is extremely
powerful because we can use the agents
SDK to say
create a front-end agent that's just
focused on building front end or a PM
agent that's just focused on doing
project management or back-end engineer
that just focuses on the back end. Give

[00:50]
them each their own MCP tools, their own
context, and tell them to hand off to
one another. And because we're using the
agents SDK, we automatically get traces,
which you can see on the side here, that
shows how Codex is called or different
agents are handing off to each other
before they call Codex in the context
that they gave Codex before they asked
it to write some code. We have a whole
example in the OpenAI Cookbook, but we
think this is a really neat way to build
out some of these longer controlled
rollouts that we want to do for big
refactors or big feature work.
The next one I'll call out is on-prem
code review. So, similar to what we saw
with the example with parsing JSON,
you can build your own code review the
same as what is built into GitHub with
Codex Cloud, just running in your own
containers. This can be super useful if
you're on-prem or if you have another
SCM that's not GitHub,
you can just build this there.
Uses Codex's unique code review
capabilities. You can use the exact same
prompt that we include in the CLI and
Codex Cloud,
and you can use structured outputs to
flag the different issues that it finds

[00:51]
and just run in your own pipeline.
Similar to that, you can go beyond doing
code review and actually auto-fix CI.
So, if tests fail when you push up, you
know, your your something like your pull
request, you can have Codex trigger
based off of that, check out your
branch, make a pull request back on top
of that with a fix to make tests pass,
and then just merge your your PR from
there and save a bunch of time that way.
And then what we actually use on the
Codex open source repo is triggering
Codex whenever issue gets created to
auto-label the the issue. This is pretty
basic, but super super helpful.
Basically, we can use Codex to
categorize the issues based off of a
series of predefined labels, and this
doesn't need to match any kind of like
specific, you know, text matching or
anything like that. Codex can kind of
understand the intent of the issue and
use that to apply a label, which our
team then uses to figure out how we're
going to tackle the issue itself.

[00:52]
So, before we wrap up, I just want to
share a few additional resources. Some
for all users. So, for the Codex
documentation, go to
developers.openai.com/codex.
Lots of great tips there and kind of
full documentation available. We also
have a series of Codex Cookbooks, which
are guides that we've put together based
off of our own kind of experience
onboarding customers and experience from
our engineers internally at OpenAI. And
then also the Codex changelog, which
captures all of the different features
that are being added to Codex. As I
mentioned, we're shipping pretty
rapidly, so that updates pretty
frequently.
If you're an admin, we have an
enterprise admin guide for you as well
as a security guide, and then rate card
that captures the credits that are used
by Codex so you can understand usage.
And with that, that's that's it. Thanks
for watching our presentation,
and we hope
you are able to use Codex and spin up on
it well.
Thank you so much.

</details>
