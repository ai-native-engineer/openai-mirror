---
title: "Operationalizing AI in workflows: Lee Spacagna, Solutions Engineer, OpenAI"
channel: openai
url: https://www.youtube.com/watch?v=fAxlEcXiSts
youtube_id: fAxlEcXiSts
published: 2026-06-08
duration: "11:41"
captions: en-orig
---

# Operationalizing AI in workflows: Lee Spacagna, Solutions Engineer, OpenAI

[![Operationalizing AI in workflows: Lee Spacagna, Solutions Engineer, OpenAI](https://img.youtube.com/vi/fAxlEcXiSts/hqdefault.jpg)](https://www.youtube.com/watch?v=fAxlEcXiSts)

<details>
<summary>자막: Operationalizing AI in workflows: Lee Spacagna, Solutions Engineer, OpenAI (11:41)</summary>

[00:00]
[music]
>> Hi everyone. My name's Lee and I'm a
lead solution engineer here at Open AI,
working very closely with financial
services customers across EMEA.
Today, we've got some really exciting
things to show you, some of which we
only launched last week.
Every day when I work with financial
services institutions, they always have
one question, where can AI actually
change how my business runs?
Today, there are two paths for AI
adoption. First, giving ChatGPT and
Codex so that employees can use AI in
their daily work.
Second, there's systems. This is where
companies are building entirely new
products. They enhancing their customer
service, they're improving client
advisory, and they're working on
operational support.
So, it looks like this. We've got
ChatGPT and Codex working from the
bottom up using employees as they get
more AI literate.
And then we've got AI systems from
top-down, and these are those major
transformational initiatives.
But, there's a missing layer in the
middle.

[00:01]
The automation at the team and the
department level. And this is a gap that
the new ChatGPT workspace agents is
designed to close, and that's what I'll
be demoing for you today.
When we say agents, we mean AI systems
that we can delegate meaningful tasks
to, not just ask questions of.
And we can do that by using tools that
we already rely on, like email,
calendar, and those productivity apps
that we're using every day.
And we want these agents to complete
work in the same way that people do.
And in the last few months, there's been
a huge jump in capabilities. And we had
another leap last week with GPT 5.5.
Today, agents take on complex work that
used to take hours or days, and they can
handle them from start to finish.
But, what happens when you need to build
something custom, and you need to
delegate something that your team or
your departments are currently working
on?
Many of you have already built custom
GPTs.
With workspace agents, we have evolved
that into something much more powerful.
We've got a new agent builder, which
brings shared applications, skills, and
deployment all to one platform. And this
allows these agents to work in the same

[00:02]
place that work already happens.
So now let's jump into the demo.
This is the is the standard chat GPT
interface that I'm sure you're all
familiar with.
But down the left-hand side, you can now
see we've got an agents option that we
can start with.
And now for many teams, the challenge
isn't a lack of work to automate, it's
that the work is spread across meetings,
documents, emails, and other systems.
And the decisions all depend on specific
context.
So today, I'm going to show you how I
can quickly spin up an Agenty co-worker.
In this case, I want to build my own
chief of staff agent.
I want it to help me coordinate work,
track priorities, prepare meetings, and
help keep the team moving. Every
function can delegate meaningful work to
agents, and these can understand the
role, use the right tools, and they can
operate with how the team already works.
Here, I'm going to use one of the
templates we've got already for the
chief of staff agent here, and you can
see this already has a set of
instructions. It already has a set of
tools that it's able to work with, and
it already has capabilities that I can
start using.

[00:03]
Next, you can see here I want to start
connecting some of those tools that I
mentioned to make sure it's correct for
my workflow. In this case, I'm going to
use the Microsoft set of tools here. So
we've got things like Outlook Calendar,
Teams, and then my Outlook email.
Now, we can see that the instructions
are going to be automatically written by
another agent. So you don't need prompt
engineering skills, you don't need any
technical skills at all.
But what it means is that as a business
user, you can you now use an agent to
build another agent for you just with
natural language.
And that's it. That's the initial
version. I haven't written any code, and
I've got the first version of the agent
ready to go.
But now I want to customize this to my
own requirements. I want it at 9:00
a.m., I want it to run every day. I want
it to look at all of my meetings, look
at all of the applications, look at my
emails that came in overnight, and
generate a daily brief so that I could
arrive and be prepared for all of the
meetings for the day.

[00:04]
So, once again, here I just give the
instructions again in natural language,
telling it I want it to run at 9:00 a.m.
No technical skills needed here at all.
And within a matter of seconds, we can
see that it's able to customize my
agents to my team's requirements and
work exactly how I like to work every
day.
So, once this is done, we can go and
test our agent.
And we can now see there's two starter
prompts underneath to get me started. If
I want to, I can give it its own set of
instructions to perform for me, but you
can see that there's two already there
to go. And you can think of these as
capabilities that have already been
built into this agent.
So, let's ask it to prepare the today's
brief.
Here, you you can see I'm asking it to
do a concise brief using all of the
available information that I mentioned
earlier, highlight priorities,
decisions, blockers, and follow-ups, and
then post these in the CFO team channel
in the daily prep channel.

[00:05]
And now we can see the agent spinning
up.
It's going to start grabbing all of
those details, connecting into my email,
connecting to my calendar, and all those
other sources that I mentioned. It's
going to check all of those meetings
that I've got for the day. It's going to
cross-reference that with information
that might be in my emails. It's going
to pull all of the contacts needed from
all of these sources.
And the first time it runs, it's going
to ask me to uh give permission to post
to the Teams channel, so it's just going
to set that up now. And we'll go and
give it the the approval and see how
that's worked.
And that's it. That's now posted to
Teams. So, let's now go and have a look
at what it was able to generate for me.
So, now over in Teams, we can see in the
daily prep channel, we can see that
there's an update, so let's go and have
a look what it posted.
And we can see our Chief of Staff agent
from ChatGPT has gone and collected all
that information and then it has posted
that daily brief for me inside Teams,
exactly where I want the information to
be for my daily work.
So within a couple of minutes, we've
built an agent from scratch. We've
connected it to tools that I use every
day. We've given it some customized

[00:06]
guidance and we now have a running chief
of staff agent for my whole team.
But let's go back to the agent and take
it a step further.
This This week my team have been burning
themselves out running from meeting to
meeting and they haven't had any time to
prep in between.
So now let's add a new capability. I
want the agent to proactively research
before every meeting, like having an
expert chief of staff who's the telling
me who's there, what's the latest and
then what's the goal of that meeting.
So for this we need some additional
context for some other tools. So now
let's go and add some more that are
available.
I'm going to start off with SharePoint.
This is where I'm storing all of the
company information, all the information
that I've taken as notes that's shared
across the organization. So we're going
to add that.
And next I want to add Salesforce for
all of that CRM and all that kind of
rich information about all the contacts
from that customer.
So we're going to add Salesforce as
well.
And now that's done. We've got those two
apps connected.
You can also add other apps that you use
every day here as well or even custom

[00:07]
applications that you just you have
inside your business. Next is skills.
Skills are a way of capturing snippets
of information instructions to perform
critical tasks.
Think of these as an amazing way to
capture all of that those tribal
knowledge and conventions that are
currently trapped in people's heads and
we can turn those into repeatable
workflows.
You can see that there's two skills
already in use here. We've got the chief
of staff skill and we've got a final
brief formatting skill.
But now let's go and add another one
that I've already been using across my
team. So I've already got a skill here
for meeting prep. This tells chat GPT
the way that I want this information to
be structured, the key information
that's needed, the source of this
information and where I want that
information to be posted. So let's go
and add that to my agent as well.
Finally, let's save our changes.
And now I want to give the agent some
more instructions about what to do with
these new applications that I've gone
and connected. So, again, we'll use the
agent on the side to have a natural
language conversation and give it this
additional context to go and update the

[00:08]
agent.
So, here there's all the information.
I've just added Salesforce and
SharePoint, add a new capability. I want
it to be able to generate these quick
meeting briefs in
in ChatGPT. And all the information I
want to give it is just give me the
information for the next meeting.
So, it needs to go through here and make
the updates. Um and then it's it will
also um add a new starter prompt there
for me to use in a second.
So, now again, let's go and update this.
And now we can go and deploy this and
it's now available for the whole team.
So, let's go and use it.
And here is my completed agent, deployed
and ready. And now you can see we've now
got a third starter prompt underneath as
well to prepare me for my next meeting.
Now it's going to run, pull all of those
contacts from those different sources
including Salesforce
um and SharePoint that I went and added.
It's going to go and um to check all of
the information, put that together into
a concise brief in the way that the

[00:09]
skill gave the instructions to go and
represent that. And personally, I have
one of these running every day.
Um I have my own agent that checks all
of my emails that come in overnight, the
important updates from across the
business, the things that I said I would
do on Slack yesterday or on calls and
all of the contacts from the
transcripts. And now it means I get that
first hour of my day back cuz I come
into the into work in the morning and
all of my emails have a draft ready to
go with all of the context from across
the business. And it means that I can
just go through all of those emails and
click send and just approve those and
get those out to my customers. And it's
completely transformed the way that I
work.
So, So we can see here we're all ready
to go for that next meeting.
Before the team was understaffed and
they couldn't prep for those meetings,
but now we've enabled everyone to turn
up as if they've been prepped by their
own chief of staff agent.
But that was just one example there, but
this is a pattern that you can apply
across the business.
We've seen examples of agents like KYC
onboarding, AML investigations,
relationship management, and more.

[00:10]
The opportunity here isn't about one
single automation project. It's actually
about a brand new operating model. Every
team can spin up a role-specific agent
to take manual work off their plate and
help the business move faster.
But the next question is is what if
we've got thousands of these agents? How
do we manage them?
And that's where Frontier comes in.
Frontier is our platform for deploying
and managing agents at scale.
It connects to systems usually in silos,
things like data warehouses, CRM, and
internal applications.
It gives AI co-workers the same shared
context that the teams currently rely
on.
And from there, agents can reason over
data, they can run code, they can use
tools, and they can take actions all in
a governed environment.
And the key thing here as well is as
they work, the system improves. They
will learn from interactions, they will
evaluate their performance over time,
and it means that the more they do, the
better they get, just like human workers
in the business right now.
So today it's possible to build in

[00:11]
ChatGPT, Codex, and the API, and we want
to make it easier to deploy
out-of-the-box agents, plugins, and
skills all specific for financial
services workflows.
This matters because it moves the system
towards much more automation.
We can use purpose-built agents that
plug directly into work, and they can
handle all of the repeatable processes
with even less lift and customization.
With all those foundations in place,
agents become incredibly powerful,
allowing you to delegate more workflows
to AI over time. And next, Stephanie is
going to show you how teams are using
them to create transformative impacts
across the workforce. Thank you.
>> [applause]

</details>
