---
title: "Workspace agents in ChatGPT: Product feedback routing agent"
channel: openai
url: https://www.youtube.com/watch?v=bk2H8WfHZZk
youtube_id: bk2H8WfHZZk
published: 2026-04-22
duration: "3:10"
captions: en-orig
---

# Workspace agents in ChatGPT: Product feedback routing agent

[![Workspace agents in ChatGPT: Product feedback routing agent](https://img.youtube.com/vi/bk2H8WfHZZk/hqdefault.jpg)](https://www.youtube.com/watch?v=bk2H8WfHZZk)

<details>
<summary>자막: Workspace agents in ChatGPT: Product feedback routing agent (3:10)</summary>

[00:00]
[music]
>> Hi, I'm Nikhil, and I'm going to show
you how to build an agent that [music]
reads through product feedback,
summarizes recurring issues, and creates
follow-up work and routes [music] it to
the right team.
First, I start in the agent creation
step, [music] and I'm going to describe
in plain language what I want my agent
to do.
Chat GPT will take that [music] plain
language and turn it into a structured
plan for how to build out the agent. The
first thing Chat [music] GPT will do is
set up the app connections. In this
case,
>> [music]
>> I want it to access feedback from web
forums, so it needs access to web
search,
uh as well as Slack, so it needs the
Slack [music] connector set up.
My agent should then group this feedback
into recurring issues and pain points,
post a daily summary to my product
leadership team in Slack,
and be able to create issues in Linear,
which is my ticket management system,
based on [music] what it found.

[00:01]
So, we can [music] see Chat GPT going
ahead and automatically setting up those
tools, and I can view and modify those
permissions. And those permissions
really matter because my agent can only
use the tools and data I give it access
[music] to. Chat GPT will also draft up
the instructions for exactly how the
agent should operate, what the output
format should be,
and once I'm happy with that, I can go
ahead and create the agent. In this
case, I will trigger my agent directly
from [music] within Chat GPT, but I can
also run it on a schedule, and I can
also trigger it from other work
surfaces, like directly from Slack.
In this case, I'm going to ask it to run
and summarize [music] feedback for my
product.
We can see as the agent runs, it is
reading data from those different
sources I gave it access to. [music]
It is grouping that feedback, and it is

[00:02]
synthesizing it into a summary for my
product leadership team. And then it's
going to post that summary automatically
for me in the right [music] Slack
channel.
I'm going to ask my agent [music] to go
ahead and update Linear with the
information that it's found. So, once I
kick this off, my agent uses the Linear
integration. It first checks if there
are existing issues. If there are, it
will enrich those issues with the new
data points from the new customer
feedback. If those issues don't exist,
it will go ahead and create them.
So, we can see that as the agent goes
along, it automatically creates within
Linear these three new tickets. And each
ticket has a lot of rich context [music]
on exactly what the customer was
observing and how to fix it.

</details>
