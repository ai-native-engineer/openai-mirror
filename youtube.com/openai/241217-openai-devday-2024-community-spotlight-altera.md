---
title: "OpenAI DevDay 2024 | Community Spotlight | Altera"
channel: openai
url: https://www.youtube.com/watch?v=jogHE6EOfAo
youtube_id: jogHE6EOfAo
published: 2024-12-17
duration: "11:25"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | Altera

[![OpenAI DevDay 2024 | Community Spotlight | Altera](https://img.youtube.com/vi/jogHE6EOfAo/hqdefault.jpg)](https://www.youtube.com/watch?v=jogHE6EOfAo)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Altera (11:25)</summary>

[00:00]
-Hey, everyone.
All right, let's see
if this works.
We're Altera.AL.
We got in a lot of trouble
for using.
"AL" instead of "AI."
But we were adamant about it
because we're trying
to build artificial life, right?
And we think building life is
a little more
than building intelligence.
So our mission at Altera.AL
is to build digital humans
that can live --
oh, they told me not
to block the screen.
Sorry. I'm so used to that.
So it's to build digital humans
that can live, love,
and grow alongside us.
All right?
Let me tell you
a little more what that means.
My name is Robert Yang.
I've been building
digital humans really
for the last 17 years.
So before Altera, I was
an assistant professor at MIT,
where we built multi-system
neural network models, right?
So this idea
that you put together a model
with multiple system, vision,
cognition, action, and all that.

[00:01]
Right?
So nowadays, these are often
called composite architecture.
Now, when OpenAI made large
language models more accessible,
right, that was transformative
to us, like many of you.
And so I left MIT,
started Altera
with three other co-founders.
And now we're a small team
in Menlo Park,
you know, just cooking.
It's been really a privilege.
Our vision is -- Okay.
So before I talk about that,
how many of you
are building agents?
Just show of hand,
like everybody.
Right? Okay, good.
Now, we think that
we're going to have 100 billion
of these agents
with us soon enough, right?
And in particular,
we think these agents will have
fundamental human qualities.
So this is maybe a little more
controversial, right.
Not only will they help
you do work, right?
They'll be able to,
right, have autonomy
that's a cornerstone of agency.

[00:02]
But also have all the way
to emotion,
and coherence,
and maybe consciousness.
And more importantly,
they'll be able to collaborate
and progress with you
for a long time-horizon.
Right?
Nowadays, you think of agents
as they're going to help
you do something
for five minutes, 10 minutes.
Right?
But what would happen
if you let them lose
and they can do something
for an entire week?
Right?
Even better, if they can work
together with one another,
right, say, 100 of them
or 1,000 of them
for an entire week
or weeks at a time. Right?
When we get to that point,
right, that would be
really transformational.
So this is
where we want to get to.
And we'll be able to,
you know, hopefully have
humans be eventually
as effective
as entire countries.
So this is
why we started this Project Sid.
Because Sid comes from
Sid Meier,
the creator
of the Civilization games.
I've played -- yeah, yeah.
Right, Civ IV, Civ V.
I haven't played Civ VI.

[00:03]
It's okay.
I'm just old school like that.
And we wanted to build --
we wanted to experiment with
the idea of having lots and lots
of agents
just living autonomously.
See what kind of things
can happen.
So before we go into
the actual things that happened,
I'll show you just some gist
of what's going on.
So this is a Minecraft server,
right, with lots of agents
living in it autonomously.
There's no human involved.
And we wanted to see
whether or not they can have
emergent economy,
religion, government, culture,
and all that good stuff.
We gave some of them jobs.
Right? So some of them
are like merchants.
And we expected the merchants
to trade with other people.
But what we saw is
that they actually formed
this merchant hub
just autonomously
and were trading
among themselves.
And in fact, the merchant is
not even the top trader.
The top trader is this guy,
the PastaPriest.
Right, so the PastaPriest --

[00:04]
and we went in
and asked him, right,
so like, what's going on?
Why are you trading with people?
And he said he's trying
to share the blessings
of the flying Spaghetti Monster,
right, which is their god.
So there's another
religious leader in there
called an Altera priest.
He's telling them
that Altera is their creator,
which is just the truth,
you know?
All right.
So we gave them jobs, right?
It'd be kind of boring
if all they're doing
is just sticking to their jobs.
So Olivia is a farmer, right?
So she's out here
just farming by herself
and with her farmer friends.
Until one day Nora came there
and just told her
about her adventures.
And Olivia just got inspired.
And she wanted to go on
an adventure by her own.
But other people told her
to stay, right,
because they needed her.
And she eventually did stay,
right.
This is actually a little sad.
What I'm not showing you
in this video is that later on,
she actually went on an
adventure of her -- on her own.

[00:05]
So they don't have to be
stick to their roles.
And they're influenced
by social dynamics around them.
Now, the one last thing
I want to show you is some more
large-scale collaboration
among these agents, right?
So we run these simulations
all the time.
And one day our CTO went in
and saw a bunch of torches
on the ground.
And she was like,
what's going on?
And then we found out
this whole,
like, storyline that was
happening, completely emergent.
So some villagers found out
Amelia was missing, right?
So then they just gave up
on their job.
They gave up their post.
And they started
to craft these torches
and placing them on the ground.
Why?
Because they're trying
to make this town a beacon
so that Amelia can find
her way back.
So it actually has
an even richer storyline
that I can tell you
another time.
All right.
Now, this is mostly for fun.
And you're like,
oh, this is cool.
But I don't understand any
of this, right?

[00:06]
So let's get into a
little more details.
You're all building agents.
And one of the big problems
with agents
is long-term progression, right?
You have a typical agent
workflow.
You all do this.
I'm not going to belabor it,
right.
Let's say you do five
language model calls, right,
to get something done.
That's very good, right.
What happens if you have
1,000 language model calls?
Right?
Just let the machine keep going.
Right? Most of you
know that already.
This doesn't work, right?
So agent will start a loop,
right?
Just the data will degrade
and it's actually pretty simple,
right?
So for example, at some point,
if you have hallucinated data,
that data will propagate
and just pollute everything.
And on a more fundamental level,
because these agents are,
in many ways,
autoregressive, right?
They're taking their own, like,
output as their future input.
If the output data quality is
a little lower --
Hey, that's Rowan Cheung.
Thank you for your video.

[00:07]
If your output is a little --
the quality is a little lower
than your input, right?
What's going to happen
is the data quality
will exponentially degrade
when you run it for a long time.
Even after an initial gain.
Right?
So that's a big problem
facing really long-term
autonomous agents.
And what you see is then you let
these agents run a while.
They start to loop. Right?
Famously, AutoGPT was looping
a lot, right, early on.
And a better agent will loop,
like, a lot later,
but they'll still loop
at some point.
Right?
And the real,
real phase transition
is we make them not loop at all.
Right. They just continue
to make progress.
But so far, we're just trying
to make them loop later,
right, and plateau later.
So how do we measure
long-term progression?
In Minecraft there are
1,000 items you can collect,
and it takes a long,
long time to collect them.
And so what we did is we just
put a bunch of agents in there,
right, and just let them explore
the world and see what happens.
And what we saw here
is that these agents as a group

[00:08]
can continue
to explore the world
and gather items for
over three hours, right.
Three human hours,
completely autonomous.
This amounts to 5,000
language model calls per agent.
So this is way more than 50.
And now you might say, well,
I don't know about Minecraft.
I don't know
if this is impressive or not.
Right?
It turns out, in our hands,
if you're not using GPT-4o,
the plateau comes way earlier.
Right? So GPT-4o,
we're plateauing at three hours.
But with alternative models,
we're plateauing at like,
one hour, right,
or even earlier.
So using the latest language
models definitely help us.
But in the one and a half minute
I have left --
I made too many jokes,
so I'm running
behind schedule --
I'll tell you a little more
of what we're doing
besides just plugging in
the coolest model out there.
Right? So we have
this concurrent architecture
that is brain-inspired.
I'll tell you more. Right?
So most people,
when they build an agent,

[00:09]
they have this sequential
language model calls.
Right?
You stack them,
10 language model calls,
one followed by another.
Instead, we have like,
10 modules
that are running concurrently.
Why?
Because these models --
then you can have these modules
run at different times, right,
different timescale.
Then they'll be able
to process information
at different timescales.
Turn out to be really important.
And another thing is all these
modules are context dependent.
Right? They're context-based,
so they're not always run.
You can have social modules
that is only active
when you're around people.
Right? So that saves them money
and make them more adaptive.
We also have
this bottleneck module that --
we also have
this intent generation,
which is like a special module
that's making
the high-level decision.
And this module is taking
information from your states,
right?
Your long-term memory,
your short-term memory,
but it's passing
through a bottleneck.
Because that bottleneck is
really expensive, right?
People love like,
big context window.
For us, it's all
about small context window.

[00:10]
Right?
We're trying to pack
everything into a small context
and provide that
to the intent generation.
So that it can focus on
the most important information.
Right?
And finally, it makes
this decision, and we want it
to get broadcasted globally
to the agent.
Right? So that the agent
will make a coherent decision.
Right?
Let's say you make a decision.
You want your left leg
and your right leg
to both know which way
you're going, right?
So that they don't go like this.
You know? All right.
You know, some more plots.
Full model, ablation, you know,
we're doing stuff at Altera.
You know, we're improving it.
You get it.
You get it, right? All right.
But interestingly,
right, just one last point.
Interestingly, if you look at
this, right, this is early on.
For first five minutes,
there's actually no difference.
Right? Our full model is
just as good as our baseline.
The real difference is when
you run them for much longer.

[00:11]
All right. That's it.
So today I focused mostly
on the technical stuff,
but we also have a consumer
product that you can play with.
And most importantly -- right,
so we're doing a lot of research
so that we can get to this
really multi-multi-agent
collaborative future.
And if you're interested
in that, please contact us.
Thank you.

</details>
