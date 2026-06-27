---
title: "OpenAI DevDay 2024 | Community Spotlight | Sierra"
channel: openai
url: https://www.youtube.com/watch?v=rL1vMr1euG8
youtube_id: rL1vMr1euG8
published: 2024-12-17
duration: "9:52"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | Sierra

[![OpenAI DevDay 2024 | Community Spotlight | Sierra](https://img.youtube.com/vi/rL1vMr1euG8/hqdefault.jpg)](https://www.youtube.com/watch?v=rL1vMr1euG8)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Sierra (9:52)</summary>

[00:00]
-Hi everyone.
My name is Karthik Narasimhan.
I lead the research team
at Sierra.
And I'm super excited today
to be talking to you all
on TAU-bench,
which is one
of our recent efforts
at benchmarking AI agents
for the real-world.
And before I begin,
I just want to state,
you know,
this is a combined effort.
You know,
lots of super excellent people
have worked on it, including
Shunyu, Noah, and Pedram.
And if you want to read
up more on TAU-bench,
we actually put it out
as a paper on archive.
So you can go and dive deeper.
So before I go into
what TAU-bench is,
just a quick raise of hands.
Like, how many people know
what an AI agent is?
Okay, that's great.
Actually, a lot of you.
That makes my job easier.
So let me just give you
a quick background on, like,
where we're coming from
at Sierra,
you know, and then I'll talk
about TAU-bench.

[00:01]
So at Sierra,
what we're doing is
we're building
the conversational AI platform
for businesses.
And what that means is,
essentially,
you know, we're making it easy
for businesses to build
their own AI agents, right?
So agents, autonomous systems
that can interact with users.
You know, be able to converse in
free-flowing natural language.
And also be able to execute
actions
and take decisions that
can help solve issues, right?
So think you want to return
your product,
or you know,
you want to change your flight.
All sorts of things.
So one of the things about
putting these kinds of agents
in the real-world is that it's
actually quite hard to evaluate
how well they do.
Right?
I'm sure you all
have your own use cases,
and, you know, everybody's
saying evals, evals, evals.
Right?
So one of the hardest things
about building these agents
and shipping them
is evaluating them, right?
And what
I'm going to talk about today is
how we are thinking about one
way of using LLMs to help do so.

[00:02]
So let me quickly run
through some challenges.
Right? These are three
challenges that I can point out.
There may be more.
With evaluating AI agents,
right?
So first of all,
if you want to put out
your agent in the real-world,
you want these agents to be able
to communicate well with humans.
Right?
So this involves
both being able to understand
what the users are saying.
Right? They may use different
tones, different styles.
Right? They may use Gen Z
language, all sorts of things.
Right?
So you want to be able --
your agent to be able
to understand
what the humans are saying.
But at the same time,
also communicate
and generate accurate language
that the humans can understand.
And on top of that,
you want your agents
to be able to execute accurate
and reliable actions.
Right?
So whether it's an API call
to return the product,
or a change of flight and so on.
But this is sort of
like the basic.
Right? So what we want on top
of this are two other things.
So first, we want these evals
to be able to measure not only

[00:03]
first order statistics,
but also measure something more.
Measure the reliability
of these agents, right?
And I'll show you
how we do that with TAU-bench.
And on top of that,
as a developer,
you also want control
in terms of what scenarios
you can test your agent on.
Right?
So you don't want to put
these agents out in the world
and then figure out,
hey, what's happening?
You want to be able to do that
before you put these
into production.
Right?
And so we thought about
all this,
and you know -- and the research
team, we're about, you know,
developing new techniques
for building these agents.
And one of the things
that we realized was,
if you look at academic
benchmarks that exist out there,
research benchmarks,
there was sort of a gap here.
Right? So there were benchmarks
in two kinds of areas.
One, dialog systems,
where people have looked at how,
you know, systems behave
and can,
you know,
have dialog with humans.
And then the other kind of side,
you know, there were
these agent benchmarks
where people are looking
at tasks like web interaction,
or software engineering
that doesn't really have much

[00:04]
to do with an actual human user.
Right? So what we want is
a combination of the two.
And TAU-bench is
essentially one solution
that we've come up
to address this gap.
Right? So TAU here essentially
is Tool-Agent-User, right?
So T-A-U.
And the benchmark's
core idea is to use LLMs
in the best way possible to make
it easy to simulate dynamic,
real-time,
realistic conversations.
Okay?
So let me just give
you a quick overview of what --
the different components
that TAU-bench has.
So TAU, tool, agent, and user.
So the agent itself,
you know, has various things
like a domain policy document
that tells it what
and what not to do.
There's tools, API, and so on.
This is standard stuff.
The tools environment
at the bottom over here,
right, is basically where you
have a combination of a database
and then some tools
that can read to and fro,
as well as write
to this particular database.
And then, the middle part here,
which is the focus of this talk,
is having a user which can
be simulated using a scenario.

[00:05]
So diving a bit deeper
into this, right?
So our user simulation
basically,
you know, is using an LLM.
And you can think of it as like,
an agent
where you can use a system
prompt to describe a scenario
and then generate the particular
user simulation that you want.
Right?
So while, you know,
previously you would have to use
human live testers to do this,
right?
We can actually use these very
good LLMs like GPT-4o and others
to build this user simulator.
So there's a lot of advantages
to doing this.
Right? So it's cheap, fast.
It's easy to scale
to a wide range of scenarios.
And the last part,
which is where I'll
talk about reliability,
you can actually rerun the
same scenario multiple times.
Right? So this is
a more realistic assessment of
how reliable the agent is
because you're able to
actually test -- you know,
if 10,000 users have
the same question
about returning their shoes,
you want the agent
to handle every single
of those 10,000 cases.
Now, of course,
there's some caveats, right?

[00:06]
So I won't go into details,
but of course, simulators have
their, sort of, issues.
So very quickly,
not going into details,
but you can actually try out
various user simulator
techniques.
Right?
So if you think about it
at a high level,
user simulators are
essentially agents themselves.
Right? So you can use
all the latest agent research.
You know, techniques like ReAct,
Reflection,
whatever is your favorite one,
to actually make this user
simulator more and more complex.
Right? And we've seen that
actually it helps with things
like hallucinations
and unreliable behavior.
So the user simulation is
one nice application of using,
you know, modern LLMs.
But the other thing
that we found
was really critical to getting
TAU-bench right
was to actually use these LLMs
to scale up data generation,
right?
So there's sort of three stages
in which we create a task
for TAU-bench.
Stage 1 and 3
are sort of manual.
But once we sort of design
the database schema,
and APIs, and policies,
we leverage the language models
like GPT-4o

[00:07]
to really scale up and generate
a lot of realistic data.
Right?
And this is important
because you want to be
able to test on scenarios
that are realistic,
and not have to hand design
every single order
or every single person's,
you know, date of birth
and things like that.
So another particular case
where LLMs are useful.
So overall I think,
you know, I'm quite bullish
on using LLMs as a way
to develop these more dynamic,
simulated benchmarks.
I think we'll see that,
you know,
coming through the field a lot.
So I'll just give you
a quick idea of, you know,
the experience
we ran with TAU-bench.
Right? It is a research paper.
So the main things
that we evaluated
were state-of-the-art LLMs
with function calling or ReAct.
And we looked at two things.
First is basically
how well can each agent
complete the task in TAU-bench.
And the second part over here
is we introduced
a new metric called pass^k,
which essentially measures
how well an agent can perform

[00:08]
if it's asked to complete
the same scenario k times.
Right? And we want the agent
to succeed on all k scenarios
to get a pass
for that particular task.
Okay? A very quick summary
of the results.
Right, you can read --
again, you can read more --
go more into the paper
and read it.
But at a high level,
there's a lot of room
for improvement
on the benchmark itself.
Right?
So you can see that there's a
bunch of these different models.
Of course, things are changing
over time, right?
So you may get
slightly different numbers
when you run it.
But the high-level bit here is,
you know,
there's a lot of room
for improvement
for these function calling
and ReAct-based agents.
But the most interesting part,
if you see on the bottom right,
is the measure of reliability
over here.
So the downward curve
that you see here
is essentially plotting
pass^k
as you increase k
on the x-axis, right?
And you can see, you know,
for almost every --
actually every single agent
over there,
it starts off quite high
when you run it once
on a particular scenario.

[00:09]
But as you rerun the same
scenario multiple times,
the pass^k score
goes down quite a bit, right?
So this basically indicates how,
you know,
the agents may not be as
reliable as you actually think
if you just run it once, right?
And I think this is
an excellent example of
where simulators can
really shine, right?
So imagine trying
to get a human tester
to run through the same scenario
32 times, right?
That's not going to happen.
And this type of scaling
is what I'm excited to see
when you use these LLM-based
simulators to test agents
for the real-world.
So that's basically it,
you know, thank you all.
If you want to play around more
with TAU-bench,
you can go and check out
the code on GitHub.
You can also read our blog post.
And like I said,
we have an archive paper out.
So, thank you all.

</details>
