<!-- source: https://developers.openai.com/learn/scaling/ -->

## Search developer resources

# Scaling

[![API deployment checklist](https://cdn.openai.com/devhub/resources/guide-1.png)

#### API deployment checklist

Checklist for tuning Responses API applications before launch.

guide](/api/docs/guides/deployment-checklist)[![Shipping with Codex](https://cdn.openai.com/devhub/resources/video-1.png)

#### Shipping with Codex

DevDay talk on building, testing, and delivering products with Codex.

video](https://www.youtube.com/watch?v=Gr41tYOzE20)[![Rate limits guide](https://cdn.openai.com/devhub/resources/guide-2.png)

<!-- yt-inline:Gr41tYOzE20 -->
[![Shipping with Codex](https://img.youtube.com/vi/Gr41tYOzE20/hqdefault.jpg)](https://www.youtube.com/watch?v=Gr41tYOzE20)

<details>
<summary>자막: Shipping with Codex (28:53)</summary>

[00:00]
I'm Thibaud.
And I'm here at OpenAI and I build
Codex.
With Codex, we're building an AI
software engineer.
I personally like to think about it as a
little bit like a human teammate.
You can pair program with it on your
computer.
You can delegate to it. Or, as you'll
see, you can give it a job without
explicit prompting.
There's been, recently,
a massive vibe shift.
This has started from August, where we
had pretty decent usage, and since then,
thanks to all of you,
we've grown tenfold.
Today, I want to start by sharing some
of the recent updates that have created
this vibe shift.
Then, we'll bring some engineers from

[00:01]
OpenAI to show you some examples of how
we use Codex day-to-day.
Some of them are building here on the
Codex team. Some of them are just really
excited users of Codex at OpenAI.
Let's first talk about some of those
updates.
Codex now works everywhere you build.
Whether it's in your IDE, your terminal,
GitHub, web, or mobile.
No matter where you are,
it is the same powerful agent under the
hood.
The first and most important improvement
we made was to completely overhaul the
agent.
We think of the agent as a combination
of two things.
The reasoning model under the hood and
its tool harness to allow it to act and
impact change upon the world to create
value for you.
First, the model.
In August, we shipped GPT-5, our best
agentic model thus far.

[00:02]
That was until we listened to your
feedback.
And we approved upon it by shipping
GPT-5 Codex, a model that was further
optimized for work within Codex,
improving by being smarter, better
following code style, and adapting its
thinking time.
One of my favorite quotes from the
feedback from you all was that it feels
a little bit more like a true senior
engineer because it gives such few
compliments. And it also pushes back
on bad ideas.
Next, we completely rewrote the harness
to make most of the new models.
Add support for planning, MCP, auto
compaction,
so that you can have these really long
conversations and interactions, and so
much more.
At this point, we started seeing the CLI
usage take off.
But, there's more feedback.

[00:03]
The model felt really good. The agent
was useful, but the CLI felt early.
We appreciate the feedback, and so we
decided to completely revamp the Codex
CLI. We simplified approvals modes,
created a more legible UI, and added a
ton of polish polish.
And by default, it works with
sandboxing, so it is safe by default,
but you always have control.
It's been a work in progress, and we
shipped a big update last Friday.
We'll ship a new release today again.
More feedback from you all. A bunch of
you collaborate with the agent and want
to look at the code at the same time.
This is why we shipped it in the IDE
directly as a native extension.
Here, it works with your code alongside,
you know, you having control over your
IDE, get this little collaborator. It
works in VS Code, it works in Cursor,
and other popular forks.

[00:04]
This immediately took off.
Within the first week, we had 100,000
users. Many of you, I'm sure, are in
this room. A lot of our users prefer to
use Codex in their IDE directly. Part of
the magic here is that it is the exact
same agent.
It is the same open-source harness that
is powering the CLI bundled right within
the extension.
At the same time, we're also upgrading
Codex Cloud
so that
you could run many more tasks in
parallel.
For us, this is still the beginning, but
we think it's incredibly cool to be able
to command Codex through your phone.
Cloud tasks now run 90% faster
faster. They can set up their
dependencies automatically and verify
their work by taking screenshots and
sending them to you.
Giving the agent its own computer really
feels magical when it works.
And then, you can start working with
agents like this in tools like GitHub.

[00:05]
Or now Slack.
Here's an example of one engineer. Some
of you might know him.
Who had a question. And then another
engineer, Steve Lee, immediately jumps
on it and delegates it to Codex. Here,
Codex receives the entire context from
the thread and just gets to work. A
couple of minutes later, it posts a
solution together with a summary. It
actually went, explored the whole
problem, and wrote some code.
All of this progress means that we can
write code so much faster,
which also means that we have a lot of
code collectively to review.
Validating and reviewing code is now
becoming a huge bottleneck.
This We've been thinking about this for
a while.
Past experiments with code review at
OpenAI showed that it could be
useful, but also oftentimes noisy.
Previous attempts had to be turned off
because users were complaining about the
lack of signal.

[00:06]
So, we purposely trained GPT-5 Codex to
be great at ultra-thorough code review.
It goes through the dependencies, all
the code in depth inside its little
container,
truly explores the contract of like your
intent and what actually happens in the
implementation,
and then comes back with high-quality
findings. We now find that many teams
decide to enable it by default and
almost and want to make it mandatory
because it is such a high signal
finding every time.
You can trigger it while pairing with
Codex, or you can completely automate it
by running on every PR in GitHub.
Okay.
It's been a busy few months for a small,
growing team.
We've been using Codex to build Codex.
There's really no way we could have done
it without it.
Even more fun has been seeing OpenAI as
a whole get accelerated.
Today,

[00:07]
92%
almost all of OpenAI technical staff
uses Codex daily.
Up from 50% around last July.
Engineers that use Codex submit 70% more
PRs per week.
And pretty much all PRs are reviewed by
Codex.
When it finds an issue, people are
actually excited. It saves you time. You
ship with more confidence.
There's nothing worse than finding a bug
after you actually shipped the feature.
When we as a team see the stats, it
feels great. But even better is being at
lunch with someone
who then goes, "Hey, I use Codex all the
time. Here's a cool thing that I do with
it. Do you want to hear about it?"
And so we wanted to give you a taste of
that.
So, let's get to lunch with a few
teammates
and hear about their stories. They'll
show you real workflows of our teams,
how they use it every day.

[00:08]
Please welcome Nacho to the stage to
talk about iterating on UI
for the ChatGPT iOS app.
[Applause]
Thanks, Thibaud.
Hello. My name is Nacho Soto. I'm a
member of the core iOS team at OpenAI.
Going to do two things today. I'm going
to tell you about a workflow that I use
frequently when building the ChatGPT
app. And I'd like to share a demo that
shows you how I do this.
Let's start with the demo.
Thibaud asked me to build a weather app.
So, I have a starter project with just
an empty window.
And I've also asked ChatGPT to make a
mock-up of what I want the UI to look
like.
So, I'm going to ask Codex
to implement that design.
Great. While that's running, let me tell
you what's special about how Codex is

[00:09]
going to implement this.
Working in the ChatGPT core team means I
spend a lot of time on infrastructure,
performance, but also do some amount of
front-end work.
Recently, I worked on this small feature
where we simplified our personalization
screen to make our new ChatGPT
personalities more discoverable.
And I'm sure you've run into something
like this before. With that last 10% of
polish, like getting these headers and
footers aligned, it's actually taking
90% of the time.
But Codex can help you with that 10%.
And you can work on that while you do
something else. Maybe you're watching
some of the other DevDay talks.
You can even have nine other terminal
tabs running Codex if you want to be a
true 10x engineer.
Who here has been sent a pull request
from a junior engineer, and within a few
seconds you you that they didn't
actually test it, cuz there's no way
that it works.

[00:10]
If you used ChatGPT or any other agent 6
months ago, you were working with that
junior engineer.
But Codex is not.
Like Tevo said, I would argue that Codex
is now a senior engineer.
It doesn't just write the code and
assume that it works. It will verify
that it does.
I'm a big fan of TDD, test-driven
development. And I think Codex really
thrives with that workflow.
It will run your tests, fix the code,
run your tests again, over and over
until they pass.
But why stop at unit tests?
Codex is multimodal, which means it can
also verify its work visually.
A few weeks ago, we gave Codex that
superpower of being able to see images.
So, I taught it to generate snapshots
for the UI code that it writes.
And best of all, it's actually very
simple.
First,

[00:11]
I made this very simple makefile that
runs the unit tests to extract the
SwiftUI previews.
And that calls a small Python script,
which Codex wrote, by the way.
And that extracts those images, puts
them in a folder so Codex can find them.
Then in the agents.md I just told Codex
about that script, and I've asked it to
use it to verify its work.
We use this workflow to build the
ChatGPT iOS and Mac app. You could do
the same on web, for example, with tools
like Storybook or Playwright.
So, that's my workflow. I give Codex
some tools to generate screenshots so we
can verify the UI code that it writes.
Let's check in and see how Codex is
doing.
Okay, so if I scroll back,
looks like it wrote some code, started
with a plan
uh to review the existing code, uh
implement the UI, and provide preview

[00:12]
data to verify that it's good. So,
great, looks like it wrote all that
code, ran the snapshot tests.
Cool. So, uh
no, I guess no, but for 3 minutes, go
ahead and run that up.
Cool.
So, obviously this is a very simple
example, but it actually scales with how
many changes to match larger projects
like the ChatGPT app.
And it can run for many hours depending
on the tasks, iterating over and over
until it's pixel perfect.
And speaking of working for many hours,
I like to pass it over to Freal, who's
going to show us how to scale these
verification loops to run for longer
periods of time and more complex
problems.
Thank you.
[Applause]
Thanks, Nacho.
I'm Freal, and I work on developer
productivity.
Here at OpenAI, I've set high scores for

[00:13]
the longest sessions or the most tokens
produced.
I'm known as the guy that gets Codex to
do this.
For being able to use Codex to one-shot
big features and complex code changes.
I've seen the GPT-5 Codex model work for
over 7 hours productively. That was my
prompt. Or process more than 150 million
tokens over the course of a marathon
session.
This is one of those projects.
It's a complex refactor, a major feature
for my my personal JSON parser project.
And for large projects like this, there
can be long periods of time where it
seems like
all of the tests are failing until the
work is complete, especially when you're
making that core change.
Now, this is a JSON parser built for
streaming tool calls,
a parser for the AI age.
And this person this PR has over 15,000
lines of code changed, and it was
created over many hours of work from
Codex,
but only a few minutes and a handful of
prompts from me.
Let's walk through how I go from prompt
to pull request.

[00:14]
We'll do this in just a couple prompts.
First, we'll tell Codex that we want a
plan to implement our feature.
Then, we're going to review that plan
and tell it to execute. And finally, we
ship.
Here, I've opened my project in VS Code,
and I'll open up our Codex extension as
well.
Uh I have a fairly complex feature I
want to implement, and I've prepared
that in a document for me for me to
read.
And I'm going to tell Codex that I want
it to write a plan to implement this
feature, and I've described the end
state.
But I want Codex to do the heavy lifting
for me and research how to integrate
this library into my parser.
So, what I do is I ask Codex to write a
spec.
And I'm going to go ahead and kick that
off.
And actually, I'm going to turn off auto
context here. A little bit of an aside,
I've rehearsed this a few times, and
it's actually found finished specs from

[00:15]
my Git history and cheated and copied
right to the end of the process.
So, I'm going to have it really do the
work.
And uh
you'll notice I don't need to tell it a
lot. I've given it my example, I've told
it to do some research,
follow the example of the code that I've
already got.
So,
while that's working, let me show you
what I mean by a plan or an exec spec.
This is my plans.md file. I've
abbreviated everything here so we don't
have to read all of it. It's 160 lines.
Uh but really what I'm doing here is I'm
writing a design document for design
documents.
Codex is now a senior engineer, after
all, so we should be asking it to do
some of its own paperwork, too.
And like most engineers writing a design
doc, it's going to start by copying from
an example. I've got one here.
And I tell it,
you know, this plan is going to contain
is going to be a living document. It's
going to describe its big picture. It's

[00:16]
going to have a to-do list and progress
that it keeps up to date.
And I also want to say,
why do I keep on saying exec plan?
And I'm doing that because I want to
give the model a term to anchor on and
know when I use the term exec plan,
use plans.md to design that, to iterate
on it, and follow up.
It's good to give it a a term that's
unique so that it knows to reflect back
on that. And when I say that, it's
something special, not just any design
doc or implementation spec.
So,
in this spec, we've got our progress,
our surprises and discoveries. We even
have a decision log in here for me to
keep track of what it's been working on.
Now,
normally I don't ask engineers to write
this much. I only do that when maybe I
don't like their project.
[Laughter]
But in this case, this helps Codex steer
towards a completed project. It is its
memory as it works on this large plan.
And after this talk, we'll upload the
plans.md recipe to our OpenAI cookbooks

[00:17]
so any of you can adopt it in your
repositories.
Now,
how does it know
how to use this plans.md? As I mentioned
earlier,
I've used my agents.md.
I drop a couple lines here in my
agents.md, just a few instructions. When
you're working on something complex,
this is what an exec plan is, refer
plans.md,
make sure that you're following that.
Now, as you can see, it's doing quite a
bit of research on the side here, so
let's go ahead and look at a completed
spec.
So, I've switched over to a completed
session here, and it's written my spec.
Let me open up that plan here.
So,
I can review this. I can give it
feedback. I can look at Okay, that looks
like, you know,
quite a lot of words, but it is what I
wanted to do, and it has a plan.
Looks like a couple spikes, some
features that it wants to implement, and
of course documentation. So, that looks

[00:18]
good to me. I'm going to go ahead and
tell
Codex,
let's go ahead
and implement.
And we can't type today. There we go.
And
so while that runs, uh I like to keep an
eye on Codex. It keeps something
scrolling on my screen. My manager knows
that I'm still working.
And I like to watch the tests. So,
what I'll do is I'll kick off these
tests. They run very fast. Uh Codex
helped me write all of these, by the
way, from simple property tests or
simple uh unit tests to exhaustive
property tests. There's even some
fuzzing in this crate.
And uh so, I'll keep an eye on this, and
if it stays red for too long, I might
intervene and say, you know, Codex,
maybe we need to back out. Maybe that
plan is going a little off the rails.
All right, let's go ahead and look at
what it's completed in this project. So,
I'm skipping ahead to Codex having
finished that task. By the way, that

[00:19]
took over an hour in my my previous
session, so we're skipping ahead quite a
ways. And it looks like it's written
some new tests.
Um they're all passing, which is great.
Uh let's go ahead and look at the
changes.
Okay.
Wow, and it looks like it vendored in
and even maybe forked or updated the
upstream library to make some changes to
implement what it needed to do.
Now,
again, I don't have all day to read all
of this to you, so I'm going to go ahead
and open up the plan again.
So, I open up the plan, and I can see in
the progress, it's checked off some big
items. It's completed some spikes.
It's updated documentation in the
readme.
Plans.md specifies that all of these
plans have to be a living document, and
so I can use this as an executive
summary to know what it's accomplished.
That way I don't have to read all the
code myself.
Okay.
It looks like it's done and the tests
are passing.
So,

[00:20]
uh
what I've shown you today is we can go
from
uh
an implementation idea feature
a prompt to a PR in only a few steps.
Rigorous planning and thorough testing
enabled the model to work on this
feature for a sustained period of time.
And let's just see how many lines of
code it's written.
Crashed.
Okay.
4,200 lines of code and just about an
hour of work.
Incredible.
Now,
I could just merge this as is, but I
would really like another set of eyes on
this code.
Thankfully, we have Daniel up next to
talk about code review.
Hello.

[00:21]
All right, my name is Daniel and I'm an
engineer here on the Codex team. So, uh
today I want to talk about code reviews.
As Thibault mentioned, we launched code
reviews on GitHub a couple months ago
and it has been a huge hit.
Um
both externally, but especially
internally, we love code reviews. We
have them running on all of our PRs and
it's finding so many bugs that we would
have otherwise missed. And some of these
bugs are so complex that you have to
like read and reread the comment a
couple times to even understand what
it's saying. So, I highly highly
recommend you enable code reviews for
all your GitHub PRs.
Um
here's an example of one of my PRs
that's on the Codex repo. It's open
source.
So,
I uh
pushed a feature and then immediately
Codex started reviewing my code and it
found a P1 issue. Great.

[00:22]
Uh so, then I said, "Thanks, Codex.
Please fix it." And that kicked off a
background task um to to make that
change. And then once that got merged, I
said, "All right, Codex. Um
now that you have all this, now that you
have this change, review it again. Make
sure we don't have any issues."
And then it found another issue.
And then uh I was just embarrassed.
So,
this got me thinking.
What if you could have a workflow where
you create a feature
and then you review it for bugs and then
if there are any bugs, you fix it and
then you review it again and then you
fix and review and fix and review until
theoretically your code doesn't have any
issues.
So,
uh we decided to make this super easy by
bringing code reviews to local as well.
And I'm going to show you how to do that
with slash commands. And this is what I
do every day before I even submit the
PR.
Okay.
Uh so, I'm working on a little feature.

[00:23]
Uh you can see it has like three
different commits. It's a pretty small
one.
Um and I have the CLI running on the
side. So,
all I have to do is write {slash}
review,
hit enter,
and then you'll see there are a couple
different options here.
So, the first option is reviewing
against a base branch, just like a PR.
So, this would take a some of your well,
all of your commits in your base branch,
compare it to main,
uh just like a normal PR, and then look
at the whole diff and try to find any
uh issues with it.
There are other options, too, like
reviewing uncommitted changes or
specific commit or custom review
instructions, but what I usually do at
the end of the day when I have a bunch
of different commits is just review the
whole thing. So, I select the first
option. Now, I have to select a base
branch. Usually main is the first one,
so I hit enter again.
And now code review begins.
So,
a question I have is

[00:24]
why is it so good?
Why is GPT-5 Codex so good at code
reviews? Because we actually trained it
specifically on finding very technical
bugs and it will go on for a very long
time researching all sorts of different
files and then when it has a hypothesis
for something that could be wrong, it'll
even write tests, um scripts, execute
them to make sure that it gives you like
one or maybe at most two critical issues
that you have to fix before you land
your PR. It doesn't give you like 20 or
30 different things that it one shots
from just looking at your diff. It
doesn't waste your time.
So, um
yeah, there's actually a bug here.
Uh
If anyone gets Oh, nice.
It It got it for us.
Um so, it's a P0. Great. Um
and it's exactly correct. So, we aren't
supposed to be hardcoding the string
here in the code. We should be getting

[00:25]
that dynamically. So,
all I have to do now is tell Codex,
please fix.
Uh and usually I don't even read the
comments, so
uh
it just goes.
But,
yeah, and the ni- the nice thing about
reviews in the CLI is that it actually
spawns a separate thread from the
parent. So, let's say you've been
working on this feature and it is like
super biased, you know, you have to do
this feature like this, you have to
implement it like that.
The review thread is separate. It has a
fresh pair of eyes, a fresh context, new
chat, uh so it doesn't have that same
implementation bias and it'll help find
these bugs for you.
Uh so, yeah, that is going to go ahead
and and uh you know, give us some
changes. While that runs, I want to
actually show you how you can enable
um reviews on all your PRs. So, go to
chat.openai.com/codex.

[00:26]
And then
you just connect your GitHub.
And then there's a button here called
enable code review.
So, this will take you to the code
review settings and you can have like
repository level settings to say like I
want this repo to get code reviews, I
want that one to not, but I just have
this toggle over here that I just say,
"Review all of my pull requests. Please
make sure I don't ship any regressions
to prod."
So,
let's go back.
Fantastic.
Uh it made the change. Let's see.
That looks correct. Yeah, now it's
getting the prompt directory
dynamically. So, now that this is done,
what I want to do is I want to run
{slash} review again.
So, I hit {slash} review, enter, enter.
Great. So, this will start another
review thread. And then once that goes
on, hopefully it won't find any issues,
but if there are any issues, you can
continue it again.
Um and then once that's done, it gives
you a thumbs up.

[00:27]
You commit.
You push to get. And then you get one
final thumbs up from uh Codex on your PR
and you're merged.
So,
that is what I do every day
using {slash} review in my daily
workflow before I even create a PR.
Thank you so much and I'll hand it back
to Thibault to wrap it up.
[Music]
All right, folks.
That's it.
I hope today's demos gave you a glimpse
of
how we're shipping faster and with more
confidence with Codex and a little bit
about where we're going.
If you haven't tried Codex yet, just npm
install. This will give you Codex right
in your terminal. Then you just type
Codex and you could get going and use a
lot of the things that we demoed you
today. Everything we showed to you today
is real and you can use it right away.
Gabriel Peel, one of the people here

[00:28]
working on the Codex team, actually just
sent me a message that the V045
of the CLI is out like right now. It has
a few
incremental updates and also support for
uh OAuth MCP, which I think is very
cool. Uh so, just go and install it. Um
and this will give you the latest
version. And then if you want to hang
with a few of the people building Codex,
uh just come and join us at the booths.
Uh there will be some of us there and
also some of the, you know, top users of
Codex here at OpenAI. We also have
uh a Q&A
on uh Discord that you can join and uh
this will uh start shortly. So, come and
say hi. Don't be shy. And uh thank you
for joining today.
[Music]
[Applause]

</details>


#### Rate limits guide

Guide to understanding and managing rate limits

guide](https://platform.openai.com/docs/guides/rate-limits)[![Balance accuracy, latency, and cost](https://cdn.openai.com/devhub/resources/video-2.png)

#### Balance accuracy, latency, and cost

Talk on optimizing AI systems for accuracy, speed, and cost.

video](https://www.youtube.com/watch?v=Bx6sUDRMx-8)[![DevDay — optimization breakout](https://cdn.openai.com/devhub/resources/video-3.png)

<!-- yt-inline:Bx6sUDRMx-8 -->
[![OpenAI DevDay 2024 | Balancing accuracy, latency, and cost at scale](https://img.youtube.com/vi/Bx6sUDRMx-8/hqdefault.jpg)](https://www.youtube.com/watch?v=Bx6sUDRMx-8)

<details>
<summary>자막: OpenAI DevDay 2024 | Balancing accuracy, latency, and cost at scale (33:36)</summary>

[00:00]
[ Applause ]
-You built an app and its
user base is expanding, quickly.
Doubling or more.
And the growth isn't
slowing down.
The success is exciting,
but the challenge is
scaling sustainably.
What worked for a 1,000 users,
often doesn't extend
to one million.
You'll need to make critical
decisions about which LLM's
to use,
how to predict and manage costs.
And how to keep
response times fast.
I'm Colin Jarvis, I lead the AI
Solutions Team here at OpenAI.
-And I'm Jeff Harris,
I'm one of the product
leads on the API platform team.
Today we're going to cover
common pitfalls and techniques
for stealing your apps
on our platform.
And to start I wish
I could tell you
that there was one playbook
that would just work
to give you the perfect way
to optimize now in the app.
Of course there isn't.
There are lots of techniques
and many tradeoffs to be had.

[00:01]
But we're hoping that this talk
gives you a set of approaches
and best practices to consider
and that you walk away
with some optimization ideas
that do end up working really
great for what you're building.
And the first thing I'll say
before we talk about
how you should optimize,
is, we think optimizing your
apps is central to what we do.
So we push out models
that are more intelligent,
we make models that are faster,
GPT-4o is twice as fast
as 4 Turbo.
And we push relentlessly
on cost.
So, I love this chart
since text-davinci-003,
which came out in 2022.
That was the
less capable model than 4o mini.
And our cost per token
has decreased
since then by about 99%.
So that's a really good trend
to be on the back of.
Another example,
the 32k version of GPT-4,
if you wanted a million tokens
from that model,
that cost $120.
So, quite expensive.
Today, if you do that
with GPT-4o mini,
that's 60 cents.
So, 200 times improvement
in just about a year and a half.

[00:02]
Now, these lower costs,
combined with fine tuned,
smaller models like 4o mini,
they've unlocked a lot
of new use cases.
And we see this in our data.
Since we released 4o mini,
in July,
token consumption on our
platform has more than doubled.
So a ton of new ways
of using our API.
But, more models brings
more questions.
When to use 4o mini?
When to use 4o?
When is reasoning required?
We've worked with lots
of builders like you
across many different sizes
and use cases.
And we've developed
a pretty good mental model,
to help you work through
those kinds of decisions.
So Colin's going to talk about
how to improve accuracy.
The quality of the outputs
of the model.
And then I'm going to be back
in just a few minutes
to talk about how
to optimize latency and cost.
-Cool.
Skill and AI apps involves
balancing accuracy,
latency and costs
in a way that maintains accuracy
at the lowest cost and speed.
It's important to keep that
in mind as we go through,
because clearly none of this
is going to be silver bullets,

[00:03]
we're just trying to kind of
share some of the tradeoffs
that we've seen work well
in this area.
To accomplish this
we've worked out an approach
that generalizes pretty well
across most of our customers.
This is a start
by optimizing for accuracy.
So use the
most intelligent model you have
until you hit your
accuracy target.
Accuracy target is
typically something
that means that hasn't meaning
in business terms.
Like 90% of our
customer service tickets
are going to be routed
correctly on the first attempt.
Once you've hit your
accuracy target,
you then optimize
for latency and cost.
With the aim being
to maintain that accuracy,
with the cheapest fastest model
possible.
I'm going to begin with
how to ensure
your solution is going to be
accurate in production.
So, optimizing for accuracy
is all
that starting with that accuracy
target that means something.
So first we need to build
the right evaluations,
so that we can measure
whether or not our models
performing as expected.
I know you folks know that,
so we're going to
just kind of recap
that and then we're going
to share some best practices
that we've seen from folks
built in the real world.

[00:04]
Then we want to establish
a minimum accuracy
target to deliver ROI.
This is an area
that a lot of folks skip.
But what we find is a lot of
folks start arguing about like,
what accuracy is good
enough for production.
It's an area
that a lot of folks get stuck at
and can't actually
like take the final leap.
And we want to share some ways
that we seen customers
kind of communicate that
to get past that.
And lastly, once you have
that accuracy target,
you get to the actual
optimization bit.
Of like choosing
your prompt engineering, rag,
fine tuning techniques,
to actually reach
that accuracy target.
So, first step, is
to develop your baseline evals.
So, it's being like almost two
years since ChatGPT came out,
but a lot of people
still skip this step.
So I want to just start
here just to recap,
kind of make sure
that we're on the same page.
I know all of you
know what evals are,
so I'll just recap
the basics quickly.
So, we encourage our customers
to embrace eval
driven development.
So, within an LOM you
can never consider a component
like built into you've
got an eval to actually test
whether it runs end-to-end and
actually produces that results
that you're intending.

[00:05]
Evals come in a lot of flavors,
but the two like QA's
we try and flip frame
them are component evals.
So, like simple evals
that function like a unit test,
usually deterministic,
usually tests
like a single component
to make sure it's working.
And then end-to-end evals.
Which are more of like
your kind of black block text.
Where you're going to put in
the input
at the start of the process.
And then you're going to measure
what comes out at the very end
and it might be
like a multi-step network
or something that's working
through that eval.
Probably sounds
like a lot of work,
but, we found some
effective ways of scaling these
that I want to share
with you guys
that we've been working through
with some of our customers.
So, I want to go through
an example for customer service,
because this a
pretty common use case
that we run to
with our customers.
Reasonably complex,
you usually got a network
of multiple assistants
with instructions and tools
that are trying to do things.
So, a couple examples,
simple component, evals,
like did this question
get routed to the right intent?
Simple true false check.
Did it call the right tools
for this intent?
And then, did the customer
achieve their objective?
They came in looking
to get a return for $23.

[00:06]
Did they actually get that?
Now the,
I guess the best practice
that we found here
is customers using LLM's
to pretend to be customers
and red team their solution.
So, effectively what
we'll do is like,
spin up a bunch
of customer LLM's
and then run those
through our network.
And those are going to act
as like an automated test.
That's going to track
diversions,
where if we like change
a prompt here,
we want to check that actually
everything's still being routed
and completed correctly.
So, I'll just quickly show
a network here.
If this works.
If, cool.
So, I want to talk to
this network
and kind of share
how this works.
So, a lot of details here.
The main thing
to take away here,
is this a fairly typical
customer service network.
You've got a bunch of intents,
each of those intents routes to
an instruction and some tools.
So, the way
that we're approaching this with
all customer service
customers now is,
we'll start off by mining
historic conversations.

[00:07]
And for every one
we're going to set an objective
that customers trying to do.
They were trying
to get a refund for $12,
they were trying to book
a return, whatever it might be.
Then we give those to an LM
and get them to pretend
to be that customer
and run through the network
and then we mark
whether all these evals pass.
So, in this case,
this customer tried to purchase
plan b and they went through,
they got the upgrade plan intent
and they successfully did that.
Then we run through
another customer.
And they failed to get routed
correctly, so they fail.
And then we run
through another one.
And they get routed correctly,
but then they fail
to follow the instructions.
So, this won't be 100% accurate,
but we seen customers use
this to scale,
their customer service networks,
because they're
able to test like,
it's almost acts like
every time you raise a PR,
you're going to rerun
this unmade tests
and figure out
whether your customer
service network has regressed.
The reason
I wanted to share this,
I mean, seems pretty basic,
but a lot of the time
the biggest problem
with customer service networks
is divergence.

[00:08]
So, we change something
way over here in the network,
how does it affect
the whole network?
And the reason why I'm sharing
this particular approach,
we did this with a customer,
where they started off
with 50 routines
that were being covered.
We eventually scaled to like
over 400, using this method.
And the roll-out
of the new routines got faster
and faster just because
this was kind of our base
and we ended up with
over 1,000 evals
that we ran each time
that we made
a material change the network.
So, once you have your evals,
then the next step is probably
the biggest area of friction
for customers
are deploying to production.
Which is deciding like when is
enough to go to production?
How accurate is good enough?
You're never going to get
100% with LLM's.
So, how much is good enough?
So, I want to take an example
from one of our customers.
We had done two pilots for their
customer service application.
And accuracy was sitting
at between like 80 and 85%.
The business wasn't
comfortable to ship,
so we needed to agree
on a target to aim for.
So, what we did was
we built a cost model
to help them model
out the different scenarios
and decide how, like where
to set that accuracy target.

[00:09]
So, we took 100,000 cases and
we set a bunch of assumptions.
The first one was
that we're going to save $20
for everyone with the AI
successfully triage's
on the first attempt.
For the ones that get escalated,
we're going to lose $40.
Because each of those is going
to need a human to work on it
for a series of minutes.
And then of those ones
that get escalated,
5% of customers
are going to get so annoyed
that they're going to churn.
So, we're going to leave,
we're going to lose $1,000
for each of those customers.
What we ended up with
was a break-even point of 81.
5% accuracy to basically break
even on the solution.
Then we agreed with management,
right, let's go for 90%
and that is going to be an area
that we're actually comfortable
to ship at.
Now, the interesting
like addendum to this story,
is that people often have
a higher expectation
of accuracy for LLM's,
than they do for people,
it's probably not a surprise
from folks in the room.
And in this case,
when we set this 90%
accuracy marker and met it,
they also wanted to do
an AB test on humans.
So what we did was do a
parallel check of human agents.

[00:10]
So the fully human tickets,
we took a few of this
and we tested those to see
how they performed.
And they ended up
at 66% accuracy.
So, in the end, it was fairly
simple decision to ship at 90.
So, I think
that the key thing here is,
once you got your evals,
and your accuracy target,
then you know
how much to optimize.
So this stage we got
the business onboard,
we've got evals that measure it,
we know that 90% is the target.
So then we need to hill climb
against that 90%
and actually get there.
So, here, I want to revisit
our optimization techniques.
So, this four-box
model is pretty common asset
that we use within OpenAI.
So, typically you start
in the bottom left corner.
Prompt engineering,
best place to start.
Again with a prompt
of explicit instructions,
make an eval,
figure out why your,
where your evals are feeling
and then decide
where to optimize from there.
If your models failing
because it needs new context,
so it needs new information
that it hasn't been trained on,
then you retrieval
augmented generation or RAG.

[00:11]
It's failing because
it's following instructions
inconsistently, or needs more
examples to the task or style
you're ask for,
you need fine-tuning.
We have a lot of other resources
that a go into a bit more detail
on this.
So for now
I just want to call out a couple
of like key principles
that we've seen about these
over the last I"d say
six months.
Where the Meta is
like changing slightly for each
of these techniques.
First one, it's prompt
and engineering.
So, we get a question a lot
of like,
does long context replace RAG?
And the answer is,
it doesn't for now,
but I think it allows
you to scale prompt engineering
much more effectively.
So we see long context is really
good way of like figuring out
how far you can push
the context window.
So, you might not need
as effective a RAG application,
for example,
if you can stuff it
with like 60k tokens
rather than 5k tokens.
And still maintain performance
against your evals.
The other thing
that we're seeing
is automating
prompt optimization.
So, there's a concept
called meta prompting,
where you effectively make
a wrapping prompt

[00:12]
that looks at your application.
You give it the prompt
and the eval results
and then it tries
to iterate your prompt for you.
And you basically do
this almost grid search
where you're running evals,
it's iterating your prompt,
then you're feeding back
into this like wrapping prompt
and it's improving
your prompt again.
And this is an area
where we're seeing,
I think all the stuff
we've talked about so far,
it's like a lot
of manual iteration.
And I think the real difference
with meta prompting
is that people are starting
to lean models
to actually accelerate that
for you.
And I think one area
that we're seeing
that have like a lot of effect
is actually with o1.
One of the use cases
that o1 is like best at
is actually meta prompting.
We did it with a customer for,
to generate customer
service routines
and then optimized them.
And it saved them like
probably like, I think
we did a couple weeks work
into like about a day or two.
So, it's definitely
that I encourage you guys to try
and we do have
some cookbooks showing as well,
coming as well to like show you
how to do that.
So, once you move past
prompt engineering, there's RAG.
So, I know everybody
in the room knows about RAG,
so I just want to call
out a couple of things.
Which are probably most key

[00:13]
that I've seen
over the last few months
to making RAG applications work.
First one, is that not every
problem needs a semantic search.
Probably fairly obvious,
but, we see a lot of I think one
of the most like obvious
and simple optimizations
that people do,
is put in a classification step
at the start
and saying, based
on what this customer is asked,
does this require
a semantic search?
Does it require
a keyword search?
Or does it require
like an analytical
question answer the question.
And we're seeing a lot
more folks choose databases
where you can have vectors,
as well as keyword search,
as well as like write in sequel,
to answer certain questions.
And it's
pretty simple optimization,
but I think it's actually one
that you get like a ton
of mileage one
that I'd suggest people try.
The other one, is extending
your evals to cover retrieval.
So, once you add retrieval
you have like a new access
on your evals.
And like frameworks
like RAG apps
and this sort of thing
just kind of formalize this.
But the important thing is like
extending every eval example,
to show the context
that you've got.
And then highlight, you know,
are we retrieving
the right context?
Could the model
actually answer with the content
that it was given?

[00:14]
Again, fairly straightforward,
but again, something
that a lot of folks don't do
when they're working
with RAG applications, so.
There's a couple things there.
The last one is fine-tuning.
And I don't want to labor
fine-tuning,
because I know
that you folks have heard a lot
about distillation today.
So the main thing
with fine-tuning
is to start small and build up.
You'd be
surprised how few examples
fine-tuning needs to perform
well, typically for like 50 plus
examples is enough
to start with.
Making a feedback loop.
So making a way
to like log positive
and negative responses
and then feed those back in.
Again, fairly straightforward
but,
a useful like kind of aspect
here.
And the last thing
is considering distillation.
So, just like meta prompting,
having a way
to like scale up and
actually let the system learn
and actually feed those like
feed those positive
and negative
examples back into the retrain
whatever model you've got.
It is a fairly like kind of
key aspect but, for fine-tuning.
So, to kind of bring this
to life
how we've seen this
like actually work in real life,
I want to share
a customer example here.
And for this one,

[00:15]
we had a customer
that had two different domains
that they were using
for a RAG pipeline.
And they were
fairly nuanced questions
that they were trying to answer.
So the baseline
we were working from was 45%,
which is pretty bad,
that was like
a standard retrieval
with cosine similarity.
They also worked in
a regulated industry.
So, what we did was, get our
baseline evals, 45%, not great.
And then we set
our accuracy target.
For that,
we decided to maximize
for false negatives
rather than false positives.
So we'd be happy if the model
says it doesn't know rather
than it hallucinate.
And we used that set our
kind of tolerance for this one.
Then we targeted 95%
accuracy on an eval set.
And kind of had at it.
And the route that we took
to optimization is here.
The reason I included
the like ticks and crosses
with each of these is, to show
that we tried a ton of stuff
and not everything worked.
But, the kind of key,
the key things
that improved performance,
first of all,
were chunking and embedding.
So doing a grid search across
different chunking strategies
and figuring out what
like the right area
to set our tolerance was.

[00:16]
To get to 85% we then added
that classification step
I talked about.
So, if somebody types
in one word,
you want to do a keyword search
rather than a semantic search.
Pretty straightforward,
but again 20%
percentage point boost.
As well as a reranking step.
So taking all the context
and then training
a domain specific reranker.
So depending which domain
the question was for,
we had a specific reranker
which would rerank
the content of the chunks.
And then the last thing
that got us from 85 to 95
is a lot of time
people would ask analytical
questions of this RAG system.
And often RAG systems
will just like fetch the.
10 documents and give
you the wrong answer for a lot
of these questions.
So, we added some tools
so that it could write
sequel on the content
and we also added
query expansion.
Where we fine-tuned
a query expansion model
to basically infer
what the customer wanted.
And that was what we
eventually shipped with.
So, I guess just bringing
all this together that
we talked about
for optimizing for accuracy,
start with building evals
to understand
how the apps performing.
You then set an accuracy target
that makes an ROI

[00:17]
and keeps your application safe.
And then you optimize
using prompt engineering,
RAG and fine-tuning
until you hit your target.
And that point you have
an accurate app.
But the problem is
it might be slow and expensive.
And solve those problems,
I'll pass it over to Jeff.
So thank you all very much.
-Fantastic.
So, first, you focus on accuracy
you need to build a product
that works.
But once you've achieved
that desired accuracy it's time
to improve latency and cost.
And it's both
for the obvious reason
and saving their users
time and yourselves money.
But also more profoundly
because if you can reduce
the latency and cost
for each of your requests,
then you can do more inference
with the same dollar and time
budget, which is
just another way of implying
more intelligence
to the same request.
And another pretty central way
of improving accuracy.
So, let's start by talking about
techniques to improve latency.
And then we'll get to cost.
The first thing
to understand about latency
is an LLM is not a database.

[00:18]
You should not be fixating
on total request latency,
that's not the right way
to think about latency for LLM.
Instead you want to break it
down
into three different
subcomponents
that make up
total request latency.
And those are
the network latency,
that's how much time
it takes for the request
once its entered our system.
To land on the GPU's
and then get back to you.
Input latency, commonly called
a time to first token.
That's the amount of time
it takes to process the prompt
and then output latency,
for every token
that's generated,
you pay the pretty much
fixed latency cost
for each generated token.
You combine those things
together
and that's
total request latency.
What we see for many customers
is that the vast majority
of their time
is spent on output latency,
it's been generating tokens.
Usually like 90% plus
of the time.
So that's probably the first
thing you'd think to optimize,
but there are cases,
like if you're building
a classifier on long documents,
where input token speed
is actually going to be
the thing that dominates.
So really depends on
your use case.

[00:19]
So we broke down total request
latency and I'll say first,
that when you think about
total request latency,
I'm telling you
not to fixate on that,
but most customers
will be paying attention to
how long it takes
for the LLM to complete.
Unless you're doing
a streaming chat application,
the thing they're going to care
about, okay, the answer is done.
But even with that frame,
even knowing that the final
thing customers care about,
for as developers
you want to be a little bit
more focused on the details.
So we talked about
this network latency, TTFT,
that's the prompt latency time
to first token.
And then the output latency,
we call that TBT or time
between tokens.
And you take the time
between tokens
times the number of tokens
that you generate,
and that's what
the composes the output latency.
So that's the basic formula
that you should just always have
in the back of your mind,
when you're thinking about why
are my requests taking so long
and how can I make them faster.
Now let's just break this
up one at a time
and talk about each component
and how it works
and what you can do.

[00:20]
So first network latency.
Unfortunately
network latency is on us,
it is the time from when
the request enters our system,
to when it lands on GPUs,
and when the request finishes,
to when it get backs to you.
It'll add about 200 milliseconds
to your total request time
just to be routed
through our services.
One of the really nice pieces
of news is this is a central
that we've been focusing on
for the last six months or so.
And I'll say historically,
our system has been pretty dumb
where all of our requests
had been routed through a few
central choke points in the US.
And then they land on GPU's and
then they come back to the US
and they get back to you.
Which means
that for a standard request
you're often hopping
across the ocean multiple times.
Not ideal for
really lower network latency.
But we're actually just throwing
out right now regionalizations,
so if you'd pay attention
to your metric,
you should be seeing
network latency go down
over these last few weeks.
And first I'll say,
I'm not allowed to tell where
our actual data centers are,
since this
a little illustrative,
but you can see that
instead of having

[00:21]
just centralized choke points,
we now take requests,
we find that data centers that
are closest to those requests,
we try to process them
completely locally.
So it's one really,
really meaningful way
of reducing network latency.
Alright.
So stuff
that you can affect real easily,
time to first token.
This is the latency
that it takes to process prompts
and there's a few
important techniques
that really help optimize here.
The first, the obvious one is
just to use shorter prompts.
And I know Colin just said,
you want to put more context,
more examples in your prompts.
And I wish I could tell you
that that didn't come
at a latency cost,
it does come
at a minor latency cost.
The longer your prompts are,
the longer it will take
to process the prompts.
Usually prompts are about
20 to 50 times faster per token
than output latency,
depending on the model.
So, that is the tradeoff
you have to make between the
amount of data in your prompt
and how fast you want
your prompt to be processed.
One of the really nice things
that we just released today
is generations
in our playground.

[00:22]
Where you can actually tell
a model
that we've tuned for
prompts engineering to say,
I want the prompt
to be able to do these thing
and I want it to be concise.
And I want to it be brief
and the model will
actually help form a prompt
that meets this criteria
and does the right balance
between verbosity
and also gravity.
So, that's one technique.
Second technique
for improving prompts
and we'll talk about this a lot,
is choosing a model
the right size.
Depending on which model
you choose the time to
first token varies
quite meaningfully.
So, o1 in GPT-4o,
both have a time to first token
of about 200 milliseconds.
But 1 mini
is about 50 milliseconds,
so super, super fast.
And then GPT-4o mini is
somewhere in between,
it's about 140 milliseconds,
it's the standard time
to first token
that we see across many,
many requests in our system.
And then the third way
to improve prompt latency,
I'll just dangle, it's
what we call prompt cashing.
We're just really seeing this
today,
but it's a way
to speed up your requests
if you have repeated prompts
and we'll talk about it

[00:23]
a little bit more
in the cost section
in just a couple minutes.
So that's time
to first token prompt latency.
Then the final component,
the component is probably where
you're spending the most time,
is time between token
or output latency.
So, time between tokens
takes most of the time
and that's true for our classic
models,
like GPT-4o and 4o mini.
But it's really true
for our raising models,
like o1 preview and o1 mini.
Where each of those train
of thought tokens
is an output token.
So, each token
that the model is thinking
inside its head
is actually adding
a fixed cost to the latency.
And there could be a lot
of tokens there.
So what can you do?
Well, the first thing
to understand about time
between tokens is,
one of the biggest determiners
of this speed
is just simply
supply and demand.
How many tokens
our system is processing,
versus how much capacity the
system is provisioned against.
And what you can see here
is a pretty typical week for us.
Where the weekends tend
to be the fastest time
where had the least demands,
the tokens are being spent
out the fastest.

[00:24]
And then during weekdays,
typically the morning
specific time,
is when we have the most demand
and the models
will be at their slowest
over the course of the week.
And the way that
we optimize this internally,
is we have latency targets that
we set on a per model basis.
The units here
are tokens per second,
so want fast higher numbers mean
that they're faster.
And what these numbers
mean is this is the slowest
we ever want the model to be.
So at 8:00 a.m. on Monday,
which is typically one
of our slowest times,
we want GPT-4o to be
at least 22 tokens per second,
if not faster.
And you can see here,
GPT-4o and o1
generate
tokens at about the same speed,
4o mini meaning only faster
and then o1 mini is hugely
faster,
extremely fast model.
But it's also generating a lot
of chain of thought tokens.
So you can pick smaller models
if that's possible.
You can't really move all
of your traffic to weekends,
although if you can that's
a very straightforward way

[00:25]
to make things faster.
But one of the other things
you can think about
to improve time between
tokens latency is reducing
the number of output tokens.
This is, can make a huge
difference in total requests.
So if you have one request
that's generating
100 output tokens
and then you have
another request
that's generating
1,000 output tokens,
that second request is literally
going to take about ten times
as long, it's going to be
substantially slower.
So you really want to
be thinking about
how to prompt the model
to be concise in its output
and just give you the bear
minimum amount of information
that you need to build
the experiences you want.
And then the last way that,
just talked about,
I should also mention that,
one thing that's
a little bit subtle in time
between token latency
is the length of the prompt
actually makes a difference too.
So if you have one request that
has 1,000 prompt tokens in it
and another request that
100,000 prompt tokens in it,
that second request
for each token
it generates is going to be
a little bit slower.
Because for each token
it has to be paying attention

[00:26]
to the whole 100,000
long context.
So shortening prompts
does have a small affect
on the generation speed.
And then the final thing,
the final way
to improve time
between token latency
is choose smaller models.
If you can get away
with 4o mini,
that's a
very straightforward way
to make your application faster.
Alright.
So we've broken down latency,
we talked about network latency,
prompt latency
and then output latency.
Let's close out
by talking about cost,
the different ways you can make
more requests with less money.
So, the first thing to know
is that many of techniques
that we've already touched in
improve both latency and cost.
A lot of ways that
you make requests faster are,
will also just save you money.
So, as a
very straightforward example,
we build by token
and also tokens cost
a fixed amount of time,
so if you use fewer tokens
it's obviously going to go
meaningfully faster.
But there are some optimizations
that apply just to cost.
The first thing
I wanted to just plug is,
we have great usage limits
in our developer console

[00:27]
where you can see how much
you're spending on a per project
basis and get alerts
when your spend is more
than what you're expecting.
This is a really straightforward
way to manage costs to make sure
if there's different efforts
happening inside your company,
that you're really aware of how
much each of them are spending
and you're not getting surprised
by sudden surge in usage
over the weekend.
So just always good
to use those tools
and really setup projects
on a granular way
to control your costs.
And just keep
that good visibility.
One of the things you can do
to actually reduce costs is
with prompt caching.
This is a feature
that we're just launching today.
And the way it works,
is if a prompt lands
on an engine
that's already seen that prompt
and has it in cache,
it won't recompute the
activation's for that prompt,
those are like the
internal model states associated
with that prompt.
And instead it can just go
straight to the generation step.
So this is a way to both speed
up the prompt processing time,
but also to just save money.
One of the key things
that you should think about
with prompt caching,

[00:28]
is the way it works
is it's doing a prefix match.
If you can see in this example,
you have first request
on the left.
And then if you send
the exact same request,
plus a couple things at the end.
It's all a prompt match.
But if you change
just one character
at the very beginning of the
prompt, it's a complete mess.
None of the other activation's
are going to help
your prompt speed at all.
So what that means
if you're building applications,
is you really want to put
the static stuff
at the beginning of the prompt.
So that's like your instructions
for how your agent should work,
your one shot examples,
your function calls,
all of that stuff belongs
at the beginning of the prompt.
And then at the end
of the prompt
you want to put the things
that are more variable,
like information
that are specific user,
or what's been said
previously in the conversation.
Typically our system
will keep prompt caches alive
for about five to 10 minutes.
This will all just happen
automatically
without needing to
be involved at all.
But one of the second ways
that you can kind of
improve prompt caching rate,
is just keep a steady cadence
of requests.

[00:29]
We will always clear
the prompt cache within an hour,
but as long as you keep hitting
with the same prompt prefix,
within about five to 10 minutes
you'll keep those prompts
active the whole time.
And how does that manifest
in terms of money saved?
Well we just announcing this
today, so,
for all of our
most recent models,
you can immediately start
saving 50% on any cache token.
And one of the
really nice things
about this implementation,
is that there's
no extra work required.
Hopefully your bills
are just going down as of today,
if you have your cache prompts.
You don't need to pay extra
to use this feature,
you just save from making
their traffic more efficient.
The last thing
that I wanted to cover it terms
of saving cost, is our BatchAPI.
And I think our BatchAPI is
a little bit of a sleep or hit.
But it is 50% off
both prompts and output tokens.
By running requests
asynchronously.
So instead of hitting the model
and the model applying
as quickly as possible,
you create a batch file,
which is a sequence
of really a lot of requests,

[00:30]
huge numbers of requests.
You submit to the BatchAPI
and it will complete
this job within 24 hours,
it's often much faster
if you're submitting
the job not at peak time.
And of the really nice things
about this service,
is that anything
you pass to the BatchAPI,
it doesn't count against
your regular rate limits.
So it's a completely
separate pool of capacity
that you can just use
and pay half price on.
What we have generally found is
that most developers have
at least a few cases
they really benefit from Batch.
So that could be
content generation,
you're making a bunch of sites,
it could be running evals,
ingesting and categorizing
a really big backlog of data,
indexing data
from embedding based retrieval,
doing bit translation jobs.
Those are all things
that don't need to be run
where every token is generated
within 40 milliseconds,
so they're all
really good use cases for Batch.
And to the extent
you can offer work there,
you're both saving half
of the spend
and then you're also
of course not using any
of your other rate limits.
You just can scale more
for the services
that need to be
more synchronous.

[00:31]
Just to give you one example of
how people use this.
One of our partners, Echo AI,
they categorized customer calls,
so they summarized
the customer call.
After they transcribed it,
they classify it.
They put takeaways
and follow ups
and the BatchAPI saves
them 50% of the cost,
because they don't need to be
purely synchronous.
And what's let's them do,
is by reducing their cost
they're actually able to pass
on lower prices to customers.
The way that they built this
is that they've designed it
near real time system
that processes every call
that comes in.
Creates batch jobs, sometimes
really small batch jobs,
with just a few requests.
And then it's tracking all
of the batch jobs
that are in the system,
so as soon at they complete,
they can notify the customer.
This isn't going to be
less than one minute
response times necessarily.
But it is way cheaper than
running requests synchronously
and it lets them scale
a lot more
and just ask them more questions
about their costs.
So, we just released
the BatchAPI in the spring.
They've been using it
for a few months.

[00:32]
So for save them
tens of thousands of dollars,
it's pretty good
for early prototyping here.
They're expecting today
they used 16% of their traffic,
is moved over to the BatchAPI.
They're expecting
for their particular use case
that get to that 75%
of their traffic.
And are aiming
to save about $1 million
over the next six months.
So it's a
really substantial amount
that you can save if you can
really bifurcate your workloads,
to the ones
that you need to be synchronous
and the ones that don't.
Alright. So, we have hit you
with many, many different ideas.
We've shared a lot of things.
The good news is that a lot
of the techniques
that we have
for optimizing cost and latency,
they're highly overlapping.
You optimize one
you tend to optimize the other.
And if you can apply
a good smattering
of these best practices,
you're going to built
experiences
that are state of the art in
terms of balancing intelligence,
speed and affordability.
Also say that I'm
sure there are many techniques
that we didn't mention here
and there probably lots
that we don't know.
So, if there's something we
missed that you found effective,

[00:33]
we'd love to hear about it
after the talk.
And to close I'll just say,
once more that I wish
there was one playbook
for balancing accuracy,
latency and cost.
There is not that thing.
This is actually the central art
in building LLM applications,
is making the right tradeoffs
between these three
different key strengths.
So, I hope that we gave
you some ideas to think about
and on behalf of myself,
Colin and the team,
we're very, very excited
to see what you build.
Thank you.
[ Applause ]

</details>


#### DevDay — optimization breakout

DevDay session discussing optimization of models and prompts.

video](https://www.youtube.com/watch?v=Bx6sUDRMx-8)[![Evals Best Practices](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Evals Best Practices

Best practices for designing and running evals.

guide](https://platform.openai.com/docs/guides/evaluation-best-practices)[![Getting Started with Evals](https://cdn.openai.com/devhub/resources/guide-4.png)

#### Getting Started with Evals

Step-by-step guide to setting up your first eval.

guide](https://platform.openai.com/docs/guides/evaluation-getting-started)[![Graders](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Graders

Guide to using graders for evaluations.

guide](https://platform.openai.com/docs/guides/graders)[![Keep costs low & accuracy high](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Keep costs low & accuracy high

Guide on balancing cost efficiency with model accuracy.

guide](https://platform.openai.com/docs/guides/reasoning-best-practices#how-to-keep-costs-low-and-accuracy-high)[![Latency optimization guide](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Latency optimization guide

Best practices for reducing model response latency.

guide](https://platform.openai.com/docs/guides/latency-optimization)[![Launch apps with evaluations](https://cdn.openai.com/devhub/resources/video-4.png)

#### Launch apps with evaluations

Video on incorporating evals when deploying AI products.

video](https://vimeo.com/1105244173)[![LLM correctness and consistency](https://cdn.openai.com/devhub/resources/guide-4.png)

#### LLM correctness and consistency

Best practices for achieving accurate and consistent model outputs.

guide](https://platform.openai.com/docs/guides/optimizing-llm-accuracy)[![Model optimization guide](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Model optimization guide

Guide on optimizing OpenAI models for performance and cost.

guide](https://platform.openai.com/docs/guides/model-optimization)[![Predicted outputs guide](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Predicted outputs guide

Guide to understanding and using predicted outputs.

guide](https://platform.openai.com/docs/guides/predicted-outputs)[![Production best practices](https://cdn.openai.com/devhub/resources/guide-3.png)

#### Production best practices

Guide on best practices for running AI applications in production

guide](https://platform.openai.com/docs/guides/production-best-practices)[![Prompt Optimizer](https://cdn.openai.com/devhub/resources/guide-4.png)

#### Prompt Optimizer

Guide to refining prompts with the Prompt Optimizer.

guide](https://platform.openai.com/docs/guides/prompt-optimizer)[![Reinforcement fine-tuning overview](https://cdn.openai.com/devhub/resources/guide-1.png)

#### Reinforcement fine-tuning overview

Guide on reinforcement learning-based fine-tuning techniques.

guide](https://platform.openai.com/docs/guides/reinforcement-fine-tuning)[![Working with the Evals API](https://cdn.openai.com/devhub/resources/guide-2.png)

#### Working with the Evals API

Guide to building evaluations with the Evals API.

guide](https://platform.openai.com/docs/guides/evals)[![Eval Driven System Design - From Prototype to Production](https://cdn.openai.com/devhub/resources/cookbook-1.png)

#### Eval Driven System Design - From Prototype to Production

Cookbook for eval-driven design of a receipt parsing automation workflow.

cookbook](/cookbook/examples/partners/eval_driven_system_design/receipt_inspection)[![Reinforcement Fine-Tuning for Conversational Reasoning with the OpenAI API](https://cdn.openai.com/devhub/resources/cookbook-2.png)

#### Reinforcement Fine-Tuning for Conversational Reasoning with the OpenAI API

Cookbook for reinforcement fine-tuning conversational reasoning using HealthBench evaluations.

cookbook](/cookbook/examples/fine-tuned_qa/reinforcement_finetuning_healthbench)[![Evals API Use-case - Responses Evaluation](https://cdn.openai.com/devhub/resources/cookbook-3.png)

#### Evals API Use-case - Responses Evaluation

Cookbook to evaluate new models against stored Responses API logs.

cookbook](/cookbook/examples/evaluation/use-cases/responses-evaluation)
