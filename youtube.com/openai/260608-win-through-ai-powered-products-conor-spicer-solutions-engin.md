---
title: "Win through AI powered products: Conor Spicer, Solutions Engineer, OpenAI"
channel: openai
url: https://www.youtube.com/watch?v=re-18gil_ec
youtube_id: re-18gil_ec
published: 2026-06-08
duration: "11:05"
captions: en-orig
---

# Win through AI powered products: Conor Spicer, Solutions Engineer, OpenAI

[![Win through AI powered products: Conor Spicer, Solutions Engineer, OpenAI](https://img.youtube.com/vi/re-18gil_ec/hqdefault.jpg)](https://www.youtube.com/watch?v=re-18gil_ec)

<details>
<summary>자막: Win through AI powered products: Conor Spicer, Solutions Engineer, OpenAI (11:05)</summary>

[00:00]
Hi everyone, good afternoon. I'm Connor
Spicer. I'm going to talk now around
actually how we build new products with
AI and how that can completely change
our clients' experiences.
So I want to introduce you to Codex.
Codex is our AI coding agent um that can
do much more than just auto complete. It
can completely automate software
development cycles and many different
tasks that developers will be doing.
We can give it a job, have it look at a
cross our code base, and run for many
hours or perhaps even a full day
until the work is done.
So back in February, we launched the
Codex desktop app. It allows anyone with
natural language to start generating
code and completing many different
tasks.
We think this Codex app is actually now
the ideal surface for both technical and
semi-technical teams across financial
services.

[00:01]
And adoption of Codex has basically
broken all of our charts. When the app
was launched back in February this year,
it passed a million downloads in the
first week. Um and from there, it's just
kept on growing. We've now got over 4
million weekly active users uh across
our Codex tools.
And inside OpenAI, our engineers are
using Codex by default. We now ship more
in a week than we would do in a month
previously. We're seeing 50% more PRs,
that's chunks of code completed and
submitted per engineer. So we're
massively able to increase the output of
code that we produce, the products that
we can ship without increasing headcount
the same amount.
It hasn't replaced our engineers at all.
In fact, what we're seeing is it's
changing their workflows and making them
dramatically more effective in what they
do.
So now imagine this in your world. We
can start refactoring and migrating
legacy COBOL systems. we can automate
regulatory reporting, creating

[00:02]
audit-ready documentation, or we can
rapidly prototype across lending,
trading, or payments products and
services which we offer. So, this is the
future of development. Um shortly, I'll
go and show a demo of what this looks
like and how it works. Um
but to walk through this, we're going to
use the scenario of Blossom Bank.
Blossom is a successful bank with a
really strong consumer banking product,
but are facing threats from competitors
and growing pressure to move quickly to
implement new features that their
customers are demanding.
One request that we keep seeing coming
up from the customer base is around
predictive budgeting. They don't just
want to be told what they've spent
anymore, but they want tools to help
them anticipate their future spending
and help them plan ahead with that.
And actually, they're hearing this a
lot. So, they are under pressure to move
quickly with this, but this is the type
of task that would have taken a long
time before and a lot of coordination
across different teams to work on this.

[00:03]
So, that's why they're turning to Codex.
In this demo, I'll now show you how we
can transform these workflows both
inside the Codex app to build our code
and get our job done much more
efficiently, but also within GitHub and
how we can use this to review the code
that we produce and make sure that it's
safe and secure to ship.
So, with that, we'll jump into our demo.
So, here we are inside the Codex
application, and this is all powered by
that very powerful GPT-5 model which we
have. Firstly, let me pull up
our consumer app.
So, this is what we want to work on. We
have a running simulation here in our
dev development environment, and keep an
eye on this weekly spend.
This is the feature which we want to
change from being historical looking
into that predictive forecasting tool
that so many of our customers are asking
for.

[00:04]
As much as I might want to get in and
immediately start writing the code, the
reality of my job is I probably have
other things to be doing. I may be
pulled into an urgent meeting around
some instance that we've had that I need
to grab other data for. Codex can help
for this.
I can ask Codex to look through the
context it has of our code base and our
documentation and other tools to help
understand this for me
and quickly grab whatever it is as soon
as I realize that I need to have it.
We'll see it looking across the
different observability tools and the
code bases to pull the summary for me.
This is the sort of thing that would
have needed coordination across many
other teams previously, but now can be
run immediately, even live in a meeting
if the topic comes up and I wasn't
expecting it. Ad hoc tooling is great.
We can ask when it we want it, but we
also want to scale this across our teams
to take these best practices and to run
them whenever I need and not be reliant
on me deciding that it's a good idea to
do this.
What you can see here is some template

[00:05]
solutions that we're seeing a lot of our
teams adopting and using that are
helpful to get started,
but I can also go in and create my own
automations
around a weekly engineering summary
where I need to understand
what is it that we've built, what is it
that we've shipped,
potentially any issues that are blocking
our team that I can helpfully have ready
for me at the start of the week.
So, now that we've freed up time,
I'm able to get back to what I enjoy
doing, which is getting the code built,
seeing these new features come to life.
We can imagine that actually the context
for this sits in many different areas. I
may have a management team who've
approved a certain definition of the
scope that they've worked on with design
and product teams and that's all set in
SharePoint. Instead of me having to
switch out across multiple apps, I can
just ask Codex to use that connector and
go and find it. Similarly, it could pull
in contacts from tools like Jira,
Notion, even my emails if people had
sent me updated specs in there.

[00:06]
Once this starts running,
Codex will understand my request to
build out the plan of how we're going to
implement this. We can see it here
searching for SharePoint to find the
file that I've referenced.
And with that, I can start to see the
stream of what it's working on. I am not
having to click through manually and
search for it, but I can still inspect
how Codex is working.
Now that it's got that file, I can see
it's the one that I was expecting, and
it's going to start inspecting my code
base and immediately build a plan.
I can open this up directly in the app,
again avoiding switching across many
different tools, understand the proposed
approach, validate before it starts
changing any code that this is what I
expect. This looks good to me, so I'm
going to go ahead and say that we can
begin to implement this plan,
but also including in here some other
tasks. Maybe I want to run tests to
check that the code it writes is going
to match anything, any standards that we
have before it starts to run for me.

[00:07]
So, I'll submit this, and this is where
Codex really gets to work. It starts
inspecting my files and immediately
starting to implement this feature
across all of the front end and back end
services which I'm running here. This is
the type of task where engineering has
completely changed. Instead of typing
the code out myself, I'm prompting this,
I'm inspecting how the agent is building
it. I can steer it at this stage before
it completes. Say, "Actually, I've a new
idea." And And once completed like this,
can go in and inspect actually what is
the code that has been written. Having
it providing me the context of this, I
can check and then build my own
understanding of that code, and see a
summary of how it's all worked.
Switching back to the app, we see the
new feature is implemented, it's been
prototyped, it's ready immediately to go
and start collecting feedback on, to
share to other people. Finally, I can
commit this and push all of this new
code, so it's ready for review. Now,
that might seem really simple.
Um and I'm sure some of you are

[00:08]
thinking, "Well, actually, we have
regulators to deal with, we have
friction with legacy portals, and we
have a lot of other challenges." Well,
the good news is Codex can help here,
too. Imagine I have this type of
very legacy-looking portal that may not
have APIs to integrate with, but I need
to submit all of the summary of my
changes to consumer-facing apps to the
regulator. This is something that would
be a blocker to a fast pace of change,
and that would take a lot of time to
pull the requirements together for it.
Using a skill in Codex and our browser
automation tooling, Codex can completely
handle this task for me, understanding
what the form requires,
going in, searching across my code to
find the relevant pieces of information,
the documentation, and the evidence for
this,
before completely populating that portal
for me. So, at this point, it's found
what it needs.
At this stage, I'm hands-off. I'll let
the automation take over. It can go into
the browser and start filling out all of
these different pieces of information
for me.

[00:09]
Where it will validate it and save the
draft, but keeping me in the loop, it
won't just hit submit. It will pull
together a summary of the changes which
it's made, share that with me,
and allow me to then check are there any
final points that I want to implement,
or do I simply want to read through
this, check it myself, and then hit
submit. Again, taking tasks that would
have taken hours previously down to
something which can run in a couple
minutes or less.
So, we're increasing the amount of code
that we're shipping.
The other aspect we want to do is how do
we review that and make sure that it's
safe as easily as possible.
Here we are in GitHub, where I have my
new change committed. Our automated set
of tests have run, and our human
reviewers have checked this and approved
this.
But, we can also have Codex embedded in
this process, where it automates the
review process. And in this case, we see
that it's actually found a cyber issue,
a potential mishandling of sensitive
fields that was missed by our human

[00:10]
reviewers, but has been caught here
that we can then even send to Codex to
start implementing the fix for us.
So, I want to leave you
at this point with a couple key
takeaways which we have.
We've seen how Codex can really
accelerate our development workflows and
the other types of tasks that our
developers and engineers are doing.
And secondly, Codex is able to not just
ship more code, but to secure it through
a production-ready contextual code
review.
And together, this combination of speed
and safety is driving so much excitement
which we're seeing around Codex today.
Let's be honest with ourselves though,
we know there's strain on organization
with all this new code, new tooling to
learn, and that's why myself and our
team focus so much on enabling and
advising our customers' engineering
teams around how we scaffold these new
processes,
so that when we scale up the volume of
code, we can really meet the moment and
create this overall win for our
customers.

</details>
