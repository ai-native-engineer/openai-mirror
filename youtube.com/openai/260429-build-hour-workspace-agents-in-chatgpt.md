---
title: "Build Hour: Workspace agents in ChatGPT"
channel: openai
url: https://www.youtube.com/watch?v=kktBVmjA19A
youtube_id: kktBVmjA19A
published: 2026-04-29
duration: "37:52"
captions: en-orig
---

# Build Hour: Workspace agents in ChatGPT

[![Build Hour: Workspace agents in ChatGPT](https://img.youtube.com/vi/kktBVmjA19A/hqdefault.jpg)](https://www.youtube.com/watch?v=kktBVmjA19A)

<details>
<summary>자막: Build Hour: Workspace agents in ChatGPT (37:52)</summary>

[00:00]
Hello and welcome back to Build Hours.
I'm Victoria from product marketing and
I'm here with Christina and Hojun. Hi,
I'm Christina and I work on the
engineering team for workspace agents.
Hi, I'm Hojun. I'm on the solutions
engineering team. Awesome. And today
we're going to show you workspace agents
in ChatGPT.
So if this is your first Build Hour, um
Build Hours is all about helping teams
get more practical value from OpenAI
products with real examples and tips you
can use after the session. So today is a
special session focused on building
workspace agents in ChatGPT. And
workspace agents are available in
research preview today to ChatGPT
business, enterprise, EDU, and ChatGPT
for teachers plans.
So here's what we're going to cover.
First, Christina is going to start off
with a quick intro to workspace agents.
Then Hojun is going to walk through two
demos. The first is a meeting prep agent
that checks your calendar, does
research, and creates a meeting brief.
The second is a software review agent
that helps handle employee requests in

[00:01]
Slack and roots next steps based on your
policies. After that, Christina will
come back to share a few tips on getting
started, how to think about agents and
GPTs, and go into some detail on
enterprise admin controls. And then
we'll wrap up by answering your
questions live. So on the right side of
the screen, there's a Q&A chat box where
you can submit questions at any time
during the session.
So now I'll hand it over to Christina.
Great. So before we get into the demos,
I wanted to take a minute to to level
set on what workspace agents actually
are. So at a high level, workspace
agents are Codex-powered agents in
ChatGPT. They're built to handle
complex, long-running work that spans
multiple systems and they have access to
files, code, and tools. And so what
makes this really exciting is that
they're not just helping one person with
one prompt, but they can actually gather
the right context, keep going in the
background, and be shared either in
ChatGPT or Slack so a whole team can use
them together.
And they also have memory so they can be
guided in conversations and actually
improve over time.
So, getting started is quite simple. You

[00:02]
click agents in the ChatGPT sidebar,
describe a workflow that your team
already does, and ChatGPT helps turn
that into an agent.
So, today we're focused on workspace
agents, but since I mentioned Codex, I
wanted to also quickly explain how
workspace agents fit in with our other
agentic products.
The simplest way to think about it is
workspace agents are for teams. They're
built for shared work, for tasks that
run in the cloud even when your computer
is closed.
Codex is great for individuals working
with a personal agent to get work done,
and the Agents SDK is for teams that
want to build custom agents directly
into their own products and customer
experiences.
At OpenAI, many teams are already using
workspace agents across a few different
functions.
As a couple of examples, our marketing
team has built an agent that turns a
product brief directly into a website,
and this pulls requirements from Google
Docs and code. Um our accounting team
built an agent that helps prepare for
month-end close faster and more
consistently, and our finance team has
built an agent for a vendor risk review,

[00:03]
which researches vendors, assesses
signals like sanctions exposure,
financial health, and reputational risk,
and produces a structured report.
So, today Hojin is going to walk through
building two of these examples, um the
meeting prep agent and the software
reviewer. So, I'll hand it over to him.
Yeah, thanks Christina. So, uh we'll be
walking through how to build these
agents, um and we're going to start off
with this meeting prep agent. Um now,
I'm sure folks who are customer-facing
on this call, um you have just a lot of
uh customer meetings to get to every
single day. Uh so, this is an agent that
I built to help with the manual
multi-system work of customer meeting
prep.
Uh so, as you can see on the right side
here, every single morning I get a email
from my agent uh named Auto, which
checks my calendar, uh it does research
on the customer, whether it's on the web
or within my Google Drive. And I'll
actually create a meeting brief for each
meeting that it will link and provide to
me. So, you know, the hours I would

[00:04]
spend every evening building out my
meeting prep docs, uh docs that I want
to share with my team members, so uh
we're aligned on the agenda. That's all
done for me behind the scenes. Um and
the great part of this is that this
agent uh can be shared um so that others
can customize it for their specific
workflow um and get the similar value
that I'm seeing. So, let's jump in.
Uh what we'll do is actually we'll go
through this cookbook, uh which um
actually walks you through how to create
the agent that I just described, uh so
you can follow along with what I'm doing
on screen, or you can also, you know,
reference this and know that you can go
back to it um later on after this
session.
What I'll also introduce you to are some
of the demo assets that I'll be using
here today. Uh don't worry, these are
just mock events uh with some fake
customers, but I just wanted to show you
a real-live test run uh towards the end
of this demo section. Uh so here we're
going to go through um my calendar, and
then we'll also have uh some, you know,

[00:05]
sample assets uh to show you how it all
comes together. Uh so some account
notes, um other company details, um and
then a sales meeting prep to bring it
all together.
So, let's dive into ChatGPT and kick off
this agent build process.
Workspace agents um is going to allow
you to build agents uh just using
natural language. So, you can start from
a blank slate, or you can utilize some
of our friendly templates down below uh
to get started with your agent. Um but I
want to show everyone how easy it is to
build these agents from scratch. So,
let's get started with a prompt uh that
just outlines what we discussed uh in
terms of the use case, and it will get
me started uh building and working with
ChatGPT.
So here, my prompt just calls out that
it's going to help me with sales meeting
prep. It calls out the various tools and
apps that I might need. Um in this case,
it also says here, I have a template for
you to use. Uh and then last of all, you
know, just directing it to send an email

[00:06]
with a summary of my upcoming meetings
and links to the full briefs.
So, if I if I enter in that prompt, uh
what you'll see is that Chat GPT is
going to guide you throughout the build
process.
Um it's going to create an outline for
the agent plan that I can review before
getting started building. Um but I
really can just work with Chat uh GPT
here. Um just use natural language, give
it feedback, iterate together, and we
can build a really powerful complex
agent.
So, here I have um
you know, the agent plan, everything I
need, the capabilities look good. So,
let's get started with the build
process.
Um so, what you'll notice in a couple of
seconds here, um is that the agent is
going to or sorry, Chat GPT is going to
uh continue to live in the left-side
pane here um while it works on the right
side to uh wire up all of the, you know,
scheduling, the apps, uh the tools, and
also create a fine-tuned instruction
set.
Uh so, this is a really great no-code

[00:07]
way to build agents um that still, as
Christina mentioned, uh work like our
Codex uh agent. So, it can run across
long-running tasks uh behind the scenes,
access data, and take action across
systems. So, pretty shortly here, uh
we're going to see uh Chat GPT finish up
wiring up the agent, and we'll be able
to actually do a test run and show you
all of this live.
All right. So, we'll give it um a little
more time here, and I'll start to poke
around as it um finishes configuring
some of the different applications and
tools and steps.
All right. So, you can see here, um it's
finished up the instructions. Um, it's
going to, um, you know, continue to
build out the agent. At this point, I
can go in here and make modifications
directly. Um, or again, I can provide
that feedback to chat on the left side,
and it'll take care of all of that
configuration.
All right. So, almost done there. Um,

[00:08]
let me actually wire in some tools here.
Uh, so, for Google Calendar, and this is
helpful. I wanted to do this manually to
show you the configuration step. So, any
of the applications that you're
utilizing, um, you have the ability to,
you know, lock down what the agent
actually has access to. Uh, so, in this
case, we're looking at Google Calendar,
um, and I just need the agent to
reference my calendar. I don't need it
to take any write actions or anything
like that. Uh, so, I'm actually going to
disable, um, you know, those actions,
uh, for the agent to take those actions.
And I can know confidently that anytime
it's accessing my calendar, it's not
going to, um, you know, adjust or change
any events. Um, it's just going to go
about the workflow that I've described.
I'm also going to quickly add in Google
Drive, um, as well as Gmail. Um,
actually, it seems like
Okay, there we go. Uh, so, I'm going to
add in Gmail here. Um, you know, similar
configuration. Um, in this case, I

[00:09]
actually wanted to write an email to me,
uh, but maybe, you know, I can disable
some of these actions that it actually
does not need to do as a part of this
workflow.
Workspace agents is all about having the
control over what these agents are able
to do, uh, providing them a playbook,
um, and letting them execute on these
tasks on, you know, a schedule, or being
able to interface with them in tools
that your teams use today.
Let's do another configuration step
here, and I'm actually going to add in a
skill.
Um, so, we have the apps and tools that
the agent can use. Um, now, let's
actually give it some additional
direction on how to best support um, my
meeting prep creation. So, the great
thing about skills within ChatGPT and
Workspace agents is that first and
foremost, you can bring in skills from
other tools and platforms that you use
today. So, the best practices and
processes that you've codified, you can
bring them in and have your agent use
the same so that I can scale the
expertise and consistency across your

[00:10]
organization.
You can also choose popular skills
within your organization that already
exists or one of my favorite kind of
tools here is actually being able to
create a new skill and have ChatGPT
write it up much like it did for all of
the other agent configuration. So, let's
have it generate a skill here and add it
into this agent's playbook.
It'll kind of keep going through this.
So, we'll give it a few seconds here,
but I also have a kind of refined agent
that we can skip ahead to
and be able to jump into a preview run.
I always like to kind of observe what
ChatGPT and the agent is doing as a part
of the build process. So, we'll take a
look
at what it's doing for a little bit
longer here.
All right, so it's finding that template
within my skill or sorry, finding that
template within my Google Docs
adding it in with some formatting

[00:11]
instructions so that you know, and I'll
show you the final product coming up
here, but it's going to beautifully
format these meeting briefs for me with
tables,
headers, bullet points so that I can get
the information I need at a glance
especially if I'm looking at it on my
phone on the way in my morning commute.
All right, so this looks like it's
working out well. I'm actually going to
skip ahead to an agent version that's
maybe refined a bit more. You know, I've
had some time to work with it. Um and I
want to show you what it could look like
to easily run a preview test as well.
So, here um I'm going to start up a new
session. Um again, the same agent, maybe
with just a little more refinement. I've
given um ChatGPT some feedback and we've
done some preview runs. Uh so, I feel
pretty good about this agent and I'm at
that step where I can schedule and
distribute it. Uh but let's let's
actually do a quick preview test run.
So, I'm going to ask chat to do that.

[00:12]
Can you run a preview with my calendar
for tomorrow?
So, much like that experience of um or
the no-code experience of building these
agents, you can also work with ChatGPT
uh to actually, you know, run tests for
you. Like I said, you can give feedback
once uh these runs are executed. And you
can essentially, you know, continue to
work with it in this way. Um so, you
don't need IT and engineering support to
build out these workflows. We really
want to make sure that these subject
matter experts um are the ones that can
build out these flows and again,
distribute it to teams and share them um
as needed. So,
well, right on cue, we're going to get
this preview test uh kicked off. Um and
the other great part of these preview
runs is that you can see exactly what
the agent is doing. You can see um you
know, how it's pulling information from
other systems, um what its chain of
thought is, um and be able to follow
along. Now, this isn't going to be a
view that you baby sit or that an end

[00:13]
user will necessarily see every time. Uh
but it's great for those preview runs
and also show you how can how you can
look at previous
um historical runs of your agent. Um but
this is of course, especially great as
you first build out this agent and um
you do some tests before you put it into
a production setting.
All right. So, as you can see, we're
following along here um much like the
agent outline and the other ways that
chat GPT provides workspace agents
functionality. We're able to see the
high-level kind of plan for this agent
as it executes this workflow and we can
see exactly for each step you know what
it's doing, what files it's accessing,
you know how it's going about utilizing
the skills
and then we're going to get a final
result pretty shortly here that we can
review
and you know
I'll actually then show you how we can
schedule this agent, share it and

[00:14]
distribute it to your team for the for
them to remix and utilize for their own
workflows as well.
All right, well we'll let this run a
little longer but
in the demo industry as I like to call
it we have this concept of cooking demo
so much like on TV when someone's
putting together a meal and they pull
something out of the oven right away.
Let's actually skip ahead because I want
to be able to get to your questions and
the second demo agent as well. So if I
go into my inbox I have a previous run
that I used with this agent so you can
see here you know really great formatted
email with all the briefs that I need
and this is based off of my calendar and
all of the customer conversations that I
have for tomorrow. So it's a busy day
and I want to be able to go in and prep
for Blossom Mart, Petal Pay
as well as Nectar Works you know just at

[00:15]
with a lot of simplicity. So what the
agent did is it looked across my Google
Drive for all of my customer contacts,
you know maybe did some research on the
web to pull in additional information
and as you can see here it used that
skill really well to give me a highly
formatted and styled document with, you
know, the executive readout, uh customer
snapshot, meeting objective. These are
all things within my template that I
typically look for when I'm putting
together these meeting briefs. And the
great part of this is I can also share
this with my team members, so they know
exactly what the agenda will be um and
what our shared goals and outcomes uh
for the meeting will be with the
customer. So, um as you can imagine,
this is saving me, you know, hours on a
daily basis prepping for all of my
customer meetings. Um I can look at this
on the way to work or in my free time. I
don't have to do all of the manual work
um because Auto, my agent, is going to
do that for me on a scheduled basis. So,

[00:16]
let's go back to the agent and I'll show
the last sort of step here um of the
agent and its execution. So, what you
can do after, you know, running through
test is start to um share and distribute
this agent. So, um you can obviously add
a schedule for yourself and we would
want this to run daily for my workflow.
Um but let's say this starts to work
really well for you and everyone else
wants to have the same uh type of, you
know, efficiency and hour saving that
you're seeing with this agent. Well,
you're able to then enable uh sharing
for this agent. So, what it'll mean is
that anyone in your workspace will be
able to utilize this agent or duplicate
and remix it. Let's say, you know,
someone uses SharePoint instead of
Google Drive, they can make that change
to this agent and use ChatGPT to
reconfigure it. Um or maybe there are
additional steps you want to include
like having ChatGPT also create a slide
deck for you after uh putting together
briefs. You can um hopefully tell that

[00:17]
there's a lot of customize um
customization and flexibility that
Workspace agents provides to you. Um so,
hopefully you're inspired uh to build
out an agent that's similar. Um again,
you can refer back to this cookbook uh
to be able to go through uh the agents
um after this session as well.
All right. So, that was a fun one. Uh
what we did for the meeting prep agent
is we built an agent using natural
language. Uh we went into the
configuration of the app parameters and
access. Uh we enabled skills, um and
also memories. I'll include that in the
uh second agent. Um and then we ran an
agent preview, um so we can check out
the agent behavior. Um and once that
looked good, uh we decided to share it
um share the agent for team use. So, um
really helpful agent uh in my
day-to-day. Hopefully, folks um build
out your own version. But, let's go into
the second example for today.
So, this one is going to be right off
the bat uh more focused on serving the

[00:18]
needs of your organization or team
members. So, this is a software review
agent, and much like the previous agent,
this is actually an example that um is
modeled off a real agent that we have um
living in one of our Slack channels. I'm
sure everyone uh at your company, you
have a channel like this where
high-volume, high-sensitive, or
time-sensitive requests are made in
Slack to get a software tool by an
employee, you know, when they need it.
Um and typically, those channels, um you
know, I sometimes feel like the
experience is more like a chatbot. I
just get links. I have to do my own, you
know, discovery uh versus having an
agent take that action for you, where it
will research um the capabilities of
your requested vendor. It'll compare
options against the approved stack, you
know, reason across uh details like
utilization of existing tools, and then
it'll provide guidance to the user or
even take action. So, um you know, in
the cases that a human in the loop is
required, you can even escalate into

[00:19]
Jira. So, this has been an amazing agent
that internally has saved a lot of time
for our IT team, obviously, but also has
helped reduce our duplicate tool spend
and sprawl. So, really excited to go
into this example.
Um so, let me move into this experience
here. So,
um I'm going to start off from scratch
here once again just to show you that
even if we're building an agent that um
maybe takes on a little more work, uh
maybe it's a little more complex than a
personal kind of meeting prep agent that
you can still start from the same
starting point. So, here we have, you
know, a prompt and in this case I
actually have a skill that I want to
bring in. Um so, I'm going to actually
uh bring in a skill that our product or
sorry, excuse me, procurement team built
um to codify their workflow and best
practices when it comes to these uh sort
of decisions and evaluation. But, much

[00:20]
like the previous agent, I'm starting
off with the systems and um tools that
the agent will utilize and then I'm
giving this skill and we'll have ChatGPT
wired it all together.
Um I'll skip ahead a bit. We won't go
through the full build process cuz we
took a look at the previous one. Um but
again, uh I hope this inspires you to
start from scratch and maybe bring a
process or workflow that you're an
expert on and be able to build that uh
agentic team member that can either
assist or take over that work for you.
So,
awesome. Much like the previous agent,
we have the agent plan, you know, um
things look good. So, we'll get started
here. And maybe while this uh wires
together, I'll take the opportunity to
showcase uh the mock data set that this
agent is using. Um you know, in our
production agent it actually leverages a
software kind of management platform and
a custom MCP. Uh here I brought that
into Google Sheets just for simplicity
of the demo. Um but I pulled this up to

[00:21]
showcase that, you know, the agent's
actually going to look across all of the
approved software,
um you know, the utilization of uh the
tools as it is today, um and the
functionality and the capabilities of
each tool that we have, so that when a
user is requesting a tool uh for a very
specific purpose, um the agent's able to
reason and know that if it's making a
recommendation from our approved stack,
um it's actually going to meet the needs
of that user. So, that's what we have
provided to the agent. Um and what we
also have, and I'll go into, is a Slack
channel that I'll show how we can, you
know, bring that agent into Slack, uh
the interface where these requests are
being made.
So, if I go back here into Slate, um you
know, obviously, there's a lot of
configuration going on here. Um so,
maybe I'll skip ahead to
uh previously built version, but I
encourage everyone to try this out, uh
especially when you go through it for
the first time. It's one of my favorite
kind of parts of this product, uh

[00:22]
watching ChatGPT put everything together
and allowing you to follow along as
well.
All right. Right on cue, we have uh the
instructions. Um but yeah, I'm going to
skip ahead to that sort of refined agent
um and walk you through a couple of
setup steps before we go into Slack and
show a live test run. So, uh first and
foremost, um what we have here is uh the
ability to actually add Slack. Um so,
I'll showcase that by adding Actually,
I'll I'll pull this up and you'll be
able to see um that you can specify what
channel that an agent should operate in,
um as well as, you know, whether it
should respond when mentioned or for any
um
you know, relevant messages uh that it
can handle in the channel.
Uh you can also add additional
instructions. Um so, how to handle
requests, how to respond in thread, um
things like that. Uh so, there's a lot
of customization that you could do um
when it comes to integrating this agent

[00:23]
into Slack um as well. So, here, um, we
have the agent. One thing I forgot to
call on the previous agent, so I'll
bring up here, is this concept of
memory. Uh, so, memory allows your agent
to, uh, save notes, you know, contacts,
outputs, um, and other things that will
make it, uh, better at its workflow over
time. Uh, so, you can think of this as,
uh, persistent set of, uh, contacts that
the agent will keep, um, and be able to
execute on in its workflow, much like it
does with skills and tools, as well.
All right. Well, everything looks good.
Um, so, let me show you one more thing
in the platform. We'll actually go into
Slack. Um, so, on each agent screen,
you're also going to be able to see all
of its activity. So, that preview run I
showed you with the previous agent,
where you're able to see everything that
the agent did, uh, this is where, for
each agent that you create, you also
have this centralized place, uh, to view
all of the previous agent runs, um, and

[00:24]
you can go in here and check the agent
trace down to that level of detail. So,
um, this is especially handy, of course,
when you have an agent like this that is
autonomous and runs on its own, uh, so
that you can go back to any requests,
um, and everything is centrally audited
and, um, and captured for you. Um, and
this, of course, is also exportable via
our API. So, just want to show that
before we dive into the live example.
Uh, so, here I have my Slack channel and
some previous test runs. Um, I'm just
going to show you what it looks like to
kick off one of these, uh, cases, and
then I'll show you and jump ahead to the
agent response, uh, because it does take
a little more time, uh, than, of course,
a chatbot. Uh, the agent, like I
outlined, is actually going through, and
you can see here, the dialogue popped up
that it's working, it's received my
message, uh, but the agent is going to
go through and, um, you know, do some
research on Screen Studio, is going to
um, reason against um, you know, the

[00:25]
policy, the skill, um, as well as the
approved software vendor list uh, before
it gets back to the user with a
recommendation or action that it took.
So,
you know, while it's working, let's
actually go back to this one here and
I'll show you all um, you know, for the
same exact request uh, what the agent
was able to help me out with. So, Slate
responds and actually says that its
decision is that this request needs IT
review uh, versus me being able to
self-serve Screen Studio. Um, it clearly
lists out the reasoning why, the
rationale.
Um, you know, we actually have a
approved tool called Bloom um, that
would work well for my needs of needing
a high-quality uh, demo recording tool.
Uh, but it's blocked right now because
it's over utilized. There are actually
no available licenses. So, that's why
um, you know, the agent in this case has
actually chosen to escalate to IT as IT
will need to either provision additional
licenses or maybe they'll make an
exception for me um, and to use Screen

[00:26]
Studio in this case. Um, but you can see
that the agent is responding with the
sources checked with all of the
reasoning and um, guidance for the user.
So, I don't have to have this sort of
experience where I now have to look up
the tool, maybe provide my rationale.
The agent's done that work for me. And
as the final step here, um, you know,
instead of having requiring me to open
up my own ticket for IT review or
requiring IT to do that, it's also
created this nicely in Jira as a task
uh, for them to review and quickly
unblock me from uh, getting access to a
tool that I need.
So, um,
you know, this has been a really
powerful agent like I've noted. It's
handling all of these requests for our
team today um, and saving our IT and
procurement team a lot of time um, but
also, you know, making sure that users
when they have these time-sensitive
requests because they're typically made
last minute, uh they have the tools that
they need.
>> [gasps]

[00:27]
>> All right. So, with that, uh we went
into the IT agent, um how to build an
agent with existing skills, how to set
up Slack so that the agent can serve
teams within other interfaces, um how to
interact with the agent in Slack, you
know, viewing the agent run history and
traces, and then last of all, how you
can even handle escalations in Jira. So,
much like the previous agent, hopefully
this inspires folks to build out agents
that help your team members. Um but with
that, I will pass it back over to
Christina to talk through getting
started. Great. Um okay. So, now that
we've walked through some demos, I'll
cover a few few tips on how to how to
build with workspace agents. Um so,
there's really four ways to build an
agent. First, you can build one in
conversation as as we saw in the demo,
so just describe a workflow your team
already does often, and ChatGPT will
help you with the setup. Second, you can
start with one of our templates. And so,
this is a great option if you want a
faster starting point with built-in

[00:28]
skills and tools, and then go on and
customize from there. Um third, you can
bring in an existing workflow by
importing skills and apps from other
platforms so that you don't need to
start from scratch. And finally, if your
team is already using custom GPTs, you
can start to test those workflows in
workspace agents, um and we'll have an
automatic converter from GPTs to
workspace agents, um coming soon.
Um so, I also want to take a quick
second to talk about um GPTs and what um
this means for our GPT users. So, custom
GPTs were our first step towards
lightweight process automation, and many
teams have already found them helpful
for creating shared templates to be used
in ChatGPT. Um but when we first
launched GPTs, we didn't yet have the
right models or platform primitives to
make them truly powerful and extensible.
And so, workspace agents are the next
stage of GPTs. Shared agents that can
run multi-step workflows across tools on
schedules with approvals and

[00:29]
follow-through. And so, if your team
already has GPTs, I would actually start
by testing some of those workflows out
with agents.
And finally, let's talk about
permissions and admin controls. So, as
the builder, you always stay in control.
Like Hojun demoed, you decide what tools
and data your agent can use and when
approvals may be required for more
sensitive tasks. And for enterprise and
EDU plans, admins can also use
role-based access controls to define who
can use agents and which apps are
available.
And finally, the compliance API then
gives admins the ability to monitor and
manage usage over time.
So, these agents are very powerful, but
they're also built to operate within the
controls and governance that your
organization needs.
Amazing. Thank you so much, Christina
and Hojun. Um now we have some time to
answer some of the questions you've been
submitting.
Um
so, the first one that came in, quite a
few Microsoft Suite users out there. So,
maybe Hojun, can you help explain um do
agents work with Microsoft tools and a

[00:30]
bit about like
>> Yeah, absolutely. Yeah. So,
I did use the Google Drive mostly
because it's easier to set up for my
demos and I'm familiar with them, but
you can use Microsoft tools like
SharePoint, Outlook, and Teams.
Um and as you saw, you know, what you
can read or write or the agent can read
or write will depend on the specific app
and your Microsoft permissions as well
as your workspace admin settings, but
you'll be able to replicate what I built
with those suite of products as well.
Uh the last kind of distinction I'll
make um when it comes to the Slack
example, agents can run in ChatGPT and
Slack today. Not quite yet for Teams or
these tools, but we are actively
investing services and adding more soon.
Awesome. Thank you.
All right, the next question is about
memory. And then Christina, do you want
to talk about how agent memory is
different? Yeah, so Hojun touched a bit
on this in the demo. Um, but whenever
you build a workspace agent, you can
enable memory for that agent as well.
And so this is a persistent file system

[00:31]
where the agent can store files and
notes to be reused across um future
runs. Um, and you can prompt for it to
add it explicitly. It can also choose to
add it automatically. And these um this
file system is specific to every channel
that the agent is in. So if you are
using this agent in ChatGPT or you're
sharing it with someone else um in
ChatGPT, uh every user has their own
file system for their own um instance of
the agent. Um, every Slack channel also
has its own memory. So if you're in kind
of a shared Slack channel, all of the
memories within that Slack channel will
be shared across all the different
messages that are that are sent.
Very cool. Yeah. Nice. And then from now
over time is an interesting bit.
Um, cool. The other question There have
been some questions about sharing. So do
you get access automatically to all the
agents in your workspace? How do you
share them across your company?
Yeah. I can take this one. So um agents
can kept be kept private. They can be uh
specific to your workflows like I showed

[00:32]
with the first agent. Um, but they can
also be shared with anyone in your
organization with a link or they could
also be listed within your company's
workspace agent directory. So in that
case, um you know, these are agents that
can only be shared with members of your
ChatGPT workspace. Um, but within those
uh you're able to distribute your
agents. Uh you're able to allow others
to duplicate and remix those agents like
I was talking about with the sales
meeting prep. Um, and ultimately the
admins are able to control who's able to
build, publish, and share those agents
as well.
Um, and so for enterprise and EDU, um
that's uh within our admin settings, uh,
and our role-based access controls.
For now, we only, um, allow the owner of
the agent to actually make edits in that
agent, but very soon,
um, we'll allow multiple people to edit
the agent as well. Cool.
Awesome.
And can you create agents with different
roles? Like, any kind of best practices
for more specialized agents?

[00:33]
Yeah, um, I would say we just showed you
a couple, Christina alluded to the fact
that, uh, here at OpenAI, we have
agents, uh, across every single business
unit, um, and so you can have agents
with different roles. In fact, they work
best when you have a specialized role in
mind with them or for them, uh, with all
of the apps, tools, files, skills, and
instructions that they need to excel in
that role. So,
um, you can think of them as, you know,
really capable team members that you
build and you provide everything they
need to be successful, along with that
guidance. So, given that they also have
memory, like we just discussed, uh, they
can be guided or corrected over time,
uh, so they can really be improved, um,
and so, like I said, you know, get
started build these agents because it's
really easy to refine and provide
feedback, and you can continue to use
ChatGPT,
um, to, you know, change and improve
the, uh, agent behavior as well.
Awesome. Thank you.
Um, and Christina, do you have to use
the desktop app? No, um, so I mean, as

[00:34]
we as we demoed, you can, um, create,
run, share, or view these all directly
from the web. Um, you can use them in
ChatGPT, you can use them in Slack, um,
and they run in the cloud, so they keep
working even when you're away. Um, you
can also use them from the desktop app,
you can use them from mobile as well, so
really kind of across our different
surfaces. Yeah. Yeah, I'll just add to
that that both the agents that we
demonstrated today, um, aren't actually
running on the app or locally, they're
both in the cloud. Uh, one's running on
the schedule, um, and giving me notes
for my commute, and then the second one
obviously is living in Slack.
Awesome.
Cool. And Hojun, could you answer
questions about pricing? Yeah,
absolutely. So, um, pricing uh, right
now Workspace agents are in research
preview, and they're uh, free uh, until
May 6th. So, you know, I'm sound like a
broken record, but uh, when I say to
when I'm encouraging all to try it, you
know, really put it through its paces
and try it out during that period. Um,
after that, usage will move to
credit-based pricing. Um, so the number

[00:35]
of credits that an agent run consumes,
um, will obviously depend on the
complexity of the agent and the tasks
that it performs. Um, but you can think
of it similar to how we, um, or more
complex Codex tasks like you uh, that
use more credits. Um, because again,
these are agents that have the same
harness and the ability to perform uh,
long-running complex tasks. Uh, we'll be
sharing more specific guidance uh,
through admin and billing channels
regarding pricing as we get closer to
uh, on that May 6th date.
Awesome. And then we actually had a
couple more questions come in. Um, so
since you mentioned Codex, Christina,
maybe you could talk a little bit about
what makes Workspace agents different
than working with Codex? Yeah,
definitely. So, I think, um, first of
all, they're they're meant for teams,
and so they can be shared with, um,
people in different functions at your
company. Um, they also run in the cloud,
and so they run even when your when your
computer is closed. Um, and then, yeah,
again again, they can be kind of
deployed in these different environments

[00:36]
as well. So, used directly from Slack
with, um, many other triggers coming
soon.
Awesome. And then quite a few questions
around skills. Um, can you help folks
understand, you know, what's the
difference between skills and agents?
Can agents run multiple skills? And how
do you kind of determine, um, when you
should add a skill versus defining the
agent instructions?
>> Yeah, absolutely. So, I would think
about skills as being sort of, you know,
playbook, best practices, and processes
that you have that you can codify or
maybe you're already using in different
platforms and tools.
And the agent is the worker that
actually leverages that skill and other,
you know, instructions that you have to
do the real work. So, an agent can have
multiple skills and be able to utilize
them for the specific, you know, task
that that it's working on.
So, you can think of it in that way.
Once again, skills are going to be like
your best practices. Sometimes there are
scripts, there are other
kind of direction and guidance, and then
the agent will actually take on the

[00:37]
scale, will use also the apps and tools,
and execute on that work
as a whole.
Awesome.
Thank you so much for taking these
questions.
Yeah, I think we're going to wrap up and
thank you everyone so much for joining
today. So, to wrap up here, just a few
helpful resources that we will share
after this session.
So, like Hojun mentioned, the cookbook
for building the sales meeting prep, as
well as some other resources with
additional demos.
And then also want to do a quick plug on
upcoming build hours. We have two
upcoming sessions that are focused on
our API. So, you can just follow the
link here to watch
to sign up for those sessions and also
watch past build hours.
Thank you so much for attending, and
thank you so much to Christian and Hojun
again.
Yeah. Thanks all. Thank you. Thank you.

</details>
