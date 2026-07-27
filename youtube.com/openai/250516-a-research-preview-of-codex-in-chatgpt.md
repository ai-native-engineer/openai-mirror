---
title: "A research preview of Codex in ChatGPT"
channel: openai
url: https://www.youtube.com/watch?v=hhdpnbfH6NU
youtube_id: hhdpnbfH6NU
published: 2025-05-16
duration: "23:04"
captions: en-orig
---

# A research preview of Codex in ChatGPT

[![A research preview of Codex in ChatGPT](https://img.youtube.com/vi/hhdpnbfH6NU/hqdefault.jpg)](https://www.youtube.com/watch?v=hhdpnbfH6NU)

<details>
<summary>자막: A research preview of Codex in ChatGPT (23:04)</summary>

[00:00]
Hello everyone and
welcome. Software engineering is
changing and by the end of 2025 it's
going to look fundamentally different.
In 2021 we announced our first model
that we called codeex. This was the
first time that we've really
demonstrated what we would now call Vibe
coding. Just a couple weeks ago, we
released Codex CLI, which is a local
agent that runs on your laptop in your
own terminal that you're able to pair
with and interact with in a synchronous
fashion. Today, we're going to take a
step towards where we think software
engineering is going. And we are
releasing a new system, which is a
remote software agent that can run many
tasks in parallel. We call this system
in the grand tradition of of OpenAI
naming codecs.
The thing that is exciting about Codeex
is that it runs with your repository,
your environment on OpenAI compute. So
you're able to run many, many copies of
it. So you're able to do many tasks in
parallel, fire them off, come back to

[00:01]
them later, which is something that
we'll be showing you today. We're
rolling this out to uh chat GBT for uh
Pro, Enterprise, and Teams users
starting today, and we will be following
up with plus and edu in the future.
Codeex is powered by a new model that we
call Codex one. This is our best coding
model to date. We've taken 03 and we've
optimized it for not just the
benchmarks, but really for the kind of
code that people actually want to merge
into their codebase. So thinking about
comments, thinking about extraneous
changes, thinking about the style so
that it's something that that actually
really accelerates people's work. And so
to show you this system which we're so
excited to to share with you, uh we have
many members of the codeex team. Hey, um
I'm Hansen. I'm one of the members of
the Codex research team. I'm Josh and
I'm an engineer on the Codex team. And
I'm Tibo and I built code agents and
infrastructure to power them. I'm going
to be jumping right into the demo. So
normally you would have to connect your

[00:02]
GitHub account. I've already done that
for myself. And here I'm going to be
selecting my repo. I have selected an
open source repo, the preparedness repo
which contains some of our frontier uh
evals made by the amazing uh
preparedness team that we have here. And
this is relevant like frontier valves
are really about agents. So I'm just
going to be using that
environment. And then I'm greeted with
three tasks that we believe are good to
get started with on any repo. The first
one is an ask task which just ask the
the code agent codeex to explain the
codebase to a newcomer explain the
general structure. The second one is a
code task which asks to find and fix a
bug somewhere in the repo. Most of the
repos as you all know like have bugs. So
let's see let's see if the codeex agent
can find one. Um I did not put any bugs
in there. Uh this is code that we work
with every day. And so we're going to be
showing two repos today. One is the
preparedness repo and the other one is
the codeex cli one. And the final one is

[00:03]
one that I'm really excited about where
I ask it to go through the codebase and
not just explore the codebase but also
come up with proactive task suggestions
that it could be doing on its own. So
let's start those. Now we have three
codeex agents working on these tasks uh
concurrently just in the background. And
what I'm also going to do is um one of
my favorites is find as
many typos
um and grammar mistakes as you can and
fix
them. This I think this didn't matter.
Let's see if it understands also that my
instructions as I make typos. And I have
scheduled a task just before this before
we uh we were going to jump on this
where I asked some something quite
interesting to the codeex agent. I asked
it about one of my goals. I say my
codebase wants I want it to be
maintainable and bug free. Uh read
through the code propose some tasks that
would help with this goal and don't

[00:04]
overemphasize on to-dos. Like to-dos are
everywhere in code bases. Um those I
know about. I want novel things. And so
the codeex agent went through the
codebase um and in its little
environment as we're going to show you
it found out about multiple things.
Let's have a look. One of them here
looks like we are uh having mutable
defaults as arguments. Let's have codeex
fix that. Definitely fix that. So let's
schedule that. Um correct variable
spelling. I believe this will get fixed
as part of the other task, but let's
schedule that anyway. And then here
there was like a little consistency
about how we set
timeouts. One time we set it to 120,
another time we set it to 60. Um,
codeex, this codeex agent here has
proposed a task for itself. So we are
delegating the delegation here which
blows my mind every time. Uh, and I'm
just going to say make it 120. I think
this is like the right time out here.

[00:05]
And let's have it code out for us. And
then let's jump into maybe this task
here and see the codeex agent at work.
So this isn't running on my laptop here.
Um what exactly is going on here and
like how does this work? Yeah, that's a
great question to so um as evidenced
from just seeing all these tasks launch
in parallel. Um we now need new agentic
coding infrastructure for this world
where agents need not only their own
GPUs but also a couple of CPUs. So this
runs on opens compute infrastructure.
It's actually in fact the same
infrastructure we use for our
reinforcement learning and which means
fortunately even ahead of this launch
it's been battle tested on the large
scale uh training runs that we do and uh
crucially it's also consistent between
what the agencies during training and
what the agencies later in production.
So each of these tasks runs it in its
own microVM sandbox, file system, CPU,
memory, network policy and uh it the

[00:06]
agent has free reign within it, right?
So uh the agent has learned how to use
all your pix commands like GP set, knows
how to run linting, formatting and
obviously it likes to write and execute
a whole bunch of code. Yeah, one one
thing that I really love about this
interface is just how lightweight it
makes it to spin up tasks, right? It's
just your task left and right and I
think that really makes a big difference
for how you use it. I think it's it's a
lot of powerful infrastructure and like
the web interface makes it nice to
interface with it but I think it's also
a lot more comfort uh configurable.
Yeah. So each task runs what runs what
we call environment essentially um more
or less a repo but with environment
variables secrets and setup scripts
configured so that you can customize the
runtime to more fully unlock the agent's
capabilities. Um when we worked with
early alpha testers, we found that you
get really big early wins by installing
something as simple as a llinter or a
formatter. Um we actually now install a
lot of those by default. And of course
our power users have all their test
dependencies set up for OpenIs internal

[00:07]
environments, we have uh even pre-commit
hooks set up. So as the agents coding,
it's actually committing seeing what the
commit hooks say. Um really similar to
actually my own dev environment. That
sounds really exciting. Maybe let's
watch it work. Um, and we're going to
jump to an environment that we have
fully configured like the codeex CLI and
let's demo something cool with it. Yeah.
So, I think one of my favorite use cases
for Codeex is its ability to find and
resolve complex issues. So, even leading
up to this launch, I think Codex
actually found and fixed a couple of
critical bugs uh in our code. Um, but
here we're looking at the Codex CLI
which um TBO and I have worked on. Um,
so uh we've got a bug report from a user
here. basically uh when they have file
names with special characters, the the
diff command in the CLI uh shows up with
an error message. Um and so uh one of
the things we've trained our agents to
do is not just like re uh address these
issues, but also um we've introduced
this uh concept of an agent's MD file.

[00:08]
So we know for developers it's extremely
important to provide steerability and
instruction to to the model. And so the
first thing we'll see it do here, um,
it'll actually take a look at the agents
MD file in the repository. Um, and so
here, uh, we've provided some
instructions about the layout of the
repository. Um, you can see one of the
special instructions here. We've asked
it to print, um, some ASKI art to the
terminal. I think does that look like a
cat to you guys? It is. It's a different
cat every time. It passes my cat test.
Pretty good. Um so and then uh I think
we we also saw above that basically um
we've also told it you know here's the
TypeScript part of the repo in in in the
codec cli uh and along with some
instructions about how to run run tests
here which is pretty important for the
agent. Um so one of the cool things
about the way we train these models with
end toend reinforcement learning um they
not just write code but they also know
how to navigate the codebase uh and even
reproduce the issue. So here it's
written a little script for itself. So

[00:09]
um you can see it it's similar to us. I
don't know about you guys but I love to
use print debugging. Um never that's
something we see emergent kind of as
part of the RL training. Um it actually
like write wrote a little script here to
reproduce the issue. It's like written a
file actually like that matches the user
description and it's actually able to
like execute the code um to actually uh
verify that the the issues uh able able
to be
reproduced. is displaying a lot of like
complex behavior that is very similar to
how we all work. Um how do we teach the
agent to do that? Yeah, I think so we
have a lot of these kinds of tasks in
training. We use end to-end
reinforcement learning to not to
actually like verify that it completes
the entire uh cycle from writing code to
running tests and then we verify that
the that that it actually is able to
complete the tasks and satisfy for
example both style checks and
programmatic checks and many other

[00:10]
things. Um and then we can see that you
know on evaluations like Sweetbench uh
this results in state-of-the-art
performance. Um so yeah so it's actually
a it we can see here it's it's actually
found the issue and it's actually
writing a test for itself now um to
actually so we can see that it's it's
verifying its work for us um and it's
almost done here so it's actually you
know now it's even running llinters to
verify that the code is matching our our
style expectations and I I saw it refer
back to its agents.mmd here yeah exactly
so uh as part of the agents MD you can
provide detailed guidelines and for
example like commit messages and PR
messages and how exactly you want your
code to be structured. It looks like
it's preparing files for commit. Yeah, I
think it's almost
done. So just within you know like the
time that we spent talking um this this
change probably would have taken me you
know like at least 30 minutes or even or
even hours to to debug and um and just
in a moment I think we'll see the final

[00:11]
PR. And the other thing is you could do
this from your phone. Exactly. Yeah, it
looks like it's on the P. How does this
look to do?
Let's have a look. Um, it's kind of
tricky to review code so uh so fast
here. But one of the things here is that
it it did add a test. Uh it's a repro
test for uh the issue that we mentioned.
So this seems to match here. And also
what gives me confidence is that it
actually ran this test. And there is
like a little proof here uh which we'll
talk about later um where I gain a lot
of confidence here that this test is
actually passing. So I would just go and
like push and create a PR here. But now
that we have a whole bunch more tasks
that have completed, what do you think,
Greg? I mean I think this is magic. I'm
feel I'm definitely feeling feeling the
AGI here. Thank you. Thank you all. Um,
and you know, I think that what the

[00:12]
system in my mind shows is that we're
moving beyond thinking of our AI systems
as just language models, right? That
we're really building systems around
them. So, it's not just about the core
AI intelligence. It's really about what
tools is access to, the environment that
it is able to operate within, um, the
kinds of of sort of real world uh, you
know, sort of uh, conditions that it's
been trained to be exposed to. It's
starting to feel much more like the
interface that we're going to see for a
real AGI. Uh still still much more to
build, but it's starting to feel like it
has the right form factor. And so here
to tell you more about the how we build
the system are more members of the team.
Uh hi everyone. I'm Andre. I work on uh
research and uh systems for
reinforcement learning and coding
agents. I'm Katie. I'm on the research
team here. I'm Jerry. I also work on on
research here. If you if we look back at
the history, we've been working on large
language models. Code for many years
already. The first codeex models we have
released that powered GitHub copilot and

[00:13]
was little more than a smart
autocomplete and I think they have
started a revolution of AI powered
coding that we really see take off
today. Since then, we've worked on a lot
of things. We've improved every layer of
our pre-training stack to make our
models really, really great at all kinds
of programming tasks. At the moment GPT4
was released, it was by far the best
programming model in the world. We've
also constantly iterated on our on our
post training recipe to make the moles
in chat GPT really great at answering
users programming related questions.
Every day millions of users use CH GPT
to accelerate their work. However,
working with LLMs on a programming
related projects still feels pretty
clanky. It does require a lot of
handholding and context switching. I
believe the current paradigm of scaling
up reinforcement learning finally can
take us to the place where we can
automate larger chunks of work where our
models can work on where we can tell
them what we want to do not necessarily

[00:14]
how and they can work for extended
period of time on that task for a user
on a real production codebase. Even more
importantly the infrastructure that we
are opening up for it is perfectly
scalable. It doesn't run on your laptop.
It runs on the cloud. At a single push
of a button, you can spin up one agent,
10 agents, or 10,000 agents. It's an
ondemand AI power force multiplier. And
you are seeing really great results with
it internally.
Cool. So, I get to do the part of the
demo um that is probably the most
unlucky where I'm not going to kick off
any tasks, but I'm going to take a look
at the tasks that Tibo, Hansen, and Josh
kicked off um and hope that they're
good. And I think this is actually kind
of reflection of where engineering work
has moved over the past few years where
a lot of my time now is spent reviewing
code rather than writing it. And in that
sense, it becomes even more important
for our models to be very aligned with
what we want. So I will talk you through
how we train these models with alignment

[00:15]
in mind um as we look through a couple
of these tasks. So let me let's click
back into the one that Tibo kicked off
here. Um, so I think there's three key
parts here. On the right, we have the
actual code output produced by the
model. When we look at code and when you
review code, you might look for things
like, you know, like having sensible
changes, doing exactly what the PR
description said, and not having extra
changes. Um, you don't want extra
comments littered throughout your code.
This is feedback that we've heard about
our models before. Um, and so something
that we really focused on was like
having good code quality and style so
that code is easier to review. Another
thing that we really focused on here was
interpretability and verifiable u
outputs. So on the left side here we
have a model generated summary of
exactly what it did. Right here it added
an import for this function. It tells
you what it's doing and like why it's
doing it. And it shows you in this
citation view exactly the code that it
was referencing when it's talking about

[00:16]
what it did. And then in the testing
section here, the model actually ran the
test um that it was told to run in the
agents.mmd file. But beyond just
actually running the test, the model
actually reports whether the test passed
or failed. Um and in this case, you can
see exactly where in the work log the
ter um the test was run and you can see
and verify that it succeeded. Let's take
a look at one more task.
Okay, so here there's another task that
was done in the preparedness repo where
I can take a look over this model output
and it might pass like the smell test to
me initially, but I can see from the
model's testing output here that it
actually didn't manage to pass the test.
And so I'm looking here and it looks
like it might be something with like a
missing dependency in the environment.
Um maybe pedantic is not installed. And
so this PR might be something that I
check back out to my computer and rerun
the tests locally and maybe if I see
that this is valuable. This is something

[00:17]
I can go back to my environment
configuration and reinstall. And
ultimately I think we find codecs to be
like as trustworthy if not more
trustworthy than our own co-workers. I
don't have I don't have this kind of
access to like what Andre did on any
given day in terms of like the logs or
the actual test outputs. And I think as
we move towards this world where AI
writes more and more code, this kind of
verifiability is going to be really
important.
So, uh, I'm super excited to share this
with all of you today. I've been working
on this for more than two years.
Actually, a lot of that time with Jerry.
It's been a real blast. Um, and we're
we've been using this internally and
seeing a lot of really magical moments
start to appear. Uh we're sharing this
with you today because we think this
does represent a glimpse into the future
of how software engineering is done. Um
I'm just going to tell you a little bit
about how I use the product. So in the
leadup to this launch, uh I've ended up

[00:18]
doing a lot of coordination work. I
haven't had as much time for coding as I
maybe used to as much as I maybe ideally
would like. Sorry. Maybe Greg Greg can
empathize with that a little bit. Um,
and so if I'm like reviewing someone
else's code or uh reading through Slack
or playing with the product just to make
sure that uh it's developing well,
sometimes I'll have an idea of like a
code change I might like to make, a
change in the product or some refactor
and I'll just kick it off in codeex. It
takes like 30 seconds. It's a very
lightweight thing to do and then I'll go
back to Slack or or wherever I wherever
I am. Uh and then later I'll come back
and the task is sitting there and it's
done. And sometimes it's a small task.
It's like a simple string change.
Sometimes I was ambitious and I put in a
request for like a bigger refactor or
some sort of feature. And this by no
means works all the time. This is a
research preview. Uh we think it's still
early days. Uh but
sometimes it's like a multiund line diff
and I open it and I start reading
through it and I'm like, "Wow, this

[00:19]
actually looks like it's correct." And I
read through what the model did. Maybe
the model ran some tests. Maybe those
tests failed. and the model fixed the
the test failure. I look on the left and
all the little test results are green
and I'm like, "This change actually
looks really good. Let me open a PR.
Maybe I'll send it to a colleague for
review. Maybe they'll approve it and
we'll merge it and it lands in the
codebase." And then I take a step back
and I realize I just landed like a
non-trivial change, like a large change
often in our codebase and that branch
never even hit my laptop. uh it was just
something that happened completely
through this interaction with an async
delegation to to one of these agents and
when that works it's really a magical
moment uh and it's really amazing and
when I talk to other colleagues uh
they're using the product too and
they're using it in different ways and
they're having magical moments and
magical interactions with it of their
own and you can see some of those uh
stories in the videos that we're linking
from the blog associated with this
release. Um, so that's all very exciting

[00:20]
to see, but what I'm most excited about
is to share this with all of you today
and see what you all do with it. One of
the things that I find really exciting
about how Codeex works is it has very
nonhuman strengths and weaknesses. And
so it really means that you get much
more out of it if you start thinking of
of it as not just a static tool that you
just use like you know just without
having to build expertise but if you um
if you really optimize your codebase
around what it can do you start like
honestly most of what codeex benefits
from is just what is good software
engineering practices um in terms of of
modular code bases with good tests and
things like that um you're able to just
move so fast and we've seen that we've
seen that happen uh internally uh with
many people at OpenAI. Um we are
releasing this today to uh chat GBT
enterprise teams and uh
prousers. We're going to have very
generous rate limits. Uh we're going to

[00:21]
start out without any additional pricing
over time as we start to get some
feedback and some sense of how people
are using it, we'll introduce more rate
limits. we'll be rolling out out to plus
and edu users. Um that we'll be thinking
about if there's pricing for how to get
additional queries. Um in general, we're
just so excited to see how people use it
because we've seen every single person
at OpenAI uses codecs differently. Now,
we're not nearly at the end of this this
journey. We're very much at the
beginning uh that we're going to
continue to improve codecs. We're going
to make it be integrated into far more
systems like be there in your issue
tracker release an API so that you can
have it automatically be integrated into
your CI so if there's a CI error you
don't have to fix it anymore that Codex
takes care of it. Um we also are
continuing to develop Codeex CLI which
again is a local agent that runs on your
laptop. We're releasing a mini model
today and we're also going to be
releasing signin with with chatb to make
it easier to get up and running. Now, if
you think about it, there's two

[00:22]
different form factors that we've talked
about. There's the local synchronous on
your computer version, but there's also
what codeex is of an asynchronous in the
cloud runs on its own computer. And we
think that the future is going to be
these two systems coming together,
right? What you really want is you want
a remote co-orker with its own computer,
but who can also look over your
shoulder. And so, you're there typing
away, you're working on some change,
you're like, "Ah, I don't I want to go
to lunch. Codex, can you finish this?"
it just takes it over seamlessly and
runs it in the cloud. Or if you have a
question about something or you want to
pull down a change because your
dependency isn't installed or something
like that, it all just moves around
totally totally seamlessly. So it's a
co-orker, it's a intern that you can
delegate to. It's a mentor, it's a pair
programmer and all of these at once. And
so our goal really is to help accelerate
the useful work that is done to help it
be so there's more software engineers in
the world so that there's more
programming that is done uh that is
useful and and able to move forward move
forward the world. So we're just so
excited to see what you're going to do

[00:23]
with codeex. Thank you all.
[Music]

</details>
