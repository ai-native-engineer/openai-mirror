<!-- source: https://developers.openai.com/learn/ -->

## Search developer resources

# Get inspired and build

AgentsVoiceFine-tuningCustomer Service

## Learning tracks

[![Building agents](https://cdn.openai.com/devhub/tracks/agents-card.png)

#### Building agents

Learn how to build agents: Foundational concepts to practical implementation](/tracks/building-agents)[![AI app development: Concept to production](https://cdn.openai.com/devhub/tracks/ai-app-dev-card.png)

#### AI app development: Concept to production

Build, deploy, and optimize AI apps.](/tracks/ai-application-development)[![Model optimization](https://cdn.openai.com/devhub/tracks/model-optimization-card.png)

#### Model optimization

Fine-tune, distill, and optimize models for the best performance and cost.](/tracks/model-optimization)

## Demo apps

[View all](/learn/code)

[![ChatKit starter app](https://cdn.openai.com/devhub/resources/code-1.png)

#### ChatKit starter app

Integrate ChatKit with an Agent Builder workflow in your application.

code](https://github.com/openai/openai-chatkit-starter-app)[![Apps SDK examples](https://cdn.openai.com/devhub/resources/code-2.png)

#### Apps SDK examples

Example demo apps and corresponding MCP servers for the Apps SDK.

code](https://github.com/openai/openai-apps-sdk-examples)[![Responses starter app](https://cdn.openai.com/devhub/resources/code-3.png)

#### Responses starter app

Starter application demonstrating OpenAI Responses API with tools.

code](https://github.com/openai/openai-responses-starter-app)

## Videos

[View all](/learn/videos)

[![Codex for (almost) everything](https://i.ytimg.com/vi/Lm7-yFZ5fZQ/hqdefault.jpg)

#### Codex for (almost) everything

See the latest Codex app updates for working across more of the software development lifecycle.

video](https://www.youtube.com/watch?v=Lm7-yFZ5fZQ)[![Codex code review](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:Lm7-yFZ5fZQ -->
[![YouTube Lm7-yFZ5fZQ](https://img.youtube.com/vi/Lm7-yFZ5fZQ/hqdefault.jpg)](https://www.youtube.com/watch?v=Lm7-yFZ5fZQ)

<details>
<summary>자막: YouTube Lm7-yFZ5fZQ</summary>

_(자막 없음)_

</details>


#### Codex code review

Walkthrough of how Codex drives end-to-end pull request reviews with the new onboarding flow.

video](https://www.youtube.com/watch?v=HwbSWVg5Ln4)[![Introducing the Codex app](https://cdn.openai.com/devhub/resources/video-3.png)

<!-- yt-inline:HwbSWVg5Ln4 -->
[![Automatic code reviews with OpenAI Codex](https://img.youtube.com/vi/HwbSWVg5Ln4/hqdefault.jpg)](https://www.youtube.com/watch?v=HwbSWVg5Ln4)

<details>
<summary>자막: Automatic code reviews with OpenAI Codex (8:20)</summary>

[00:00]
Code review, but one take, two. Comment
mark. I agree.
You're getting
Hey everyone, I'm Romain. And I'm Maya.
Codex needs to do two things really well
to be an effective coding teammate.
First, it needs to work with all your
tools. And second, it also needs to plug
into all of your team workflows.
Code review is one of the most important
workflows for any engineering team, and
we want to help there as well.
With GPT-5 and now GPT-5 Codex, we
trained these models specifically to
find bugs and investigate some issues.
Maya, why don't you tell us more? Sure.
I work on alignment team within OpenAI
research, and code review is a very
important research project for us. As
the AI capabilities grow and we have
more and more powerful coding agents, we
are producing a lot of code, and human
verification is becoming the bottleneck.
So, we need to make sure that while also
training powerful models to help humans
in verification, and that our
verification abilities are scaling as

[00:01]
fast as AI capabilities. That's why we
trained code review models, and we could
have done it just like other research
exercise internally, but it's actually
way more useful to have it interact with
our OpenAI code base and also release it
externally. Well, I'm very much aligned
with our philosophy at OpenAI of like
iterative deployment and making sure the
technology under its contact with
reality. So, I'd love to enable code
review. Can you show us how to do it?
Absolutely. So, the first thing you will
have to do is to go in your Codex web
setting and just enable it. So, that's
all it takes. And now, going forward to
understand like any PR submitted to that
repo will be automatically reviewed by
Codex. Exactly. So, for example, here I
quickly coded up some simple extension.
I created a pull request, and it's
marked as ready for review. The code
review agents will pick it up and start
reviewing it. And in the meantime,
there's a little bit of a an emoji with
the eyes over here. Exactly.
>> Um why don't you show us one where Codex

[00:02]
has already completed the review? So,
here's another one. It looks a bit
different because here I triggered the
review already when the PR was in a
draft stage, and I didn't yet want it
real humans to look at it. So, that's an
interesting technique. So, you manually
add Codex with the message, and it
sounds like in this case, you also
wanted to have specific instructions,
right? Yeah, so you can always comment
at Codex review this PR, and you can add
some extra information. For example,
something that would help the agent
understand the PR, or you can instruct
it to focus on some specific area. Here,
what what I love about Codex code
review, and I want people to understand
like it's not just static analysis,
right? Like the model has access to
tools. It's able to check its own work,
to run tests and commands. Can you show
us what happened behind the scene for
this PR? Yeah, so one important thing to
note is the model doesn't only look at
the diff. It has access to the whole
repository. It can track down
dependencies. It could try to understand
it in a broader code base, which is very

[00:03]
important when you're working on a very
complex code base, where you're not the
only contributor and you don't
understand it in its entirety.
>> And here, it sounds like you can also
review all of the logs that led to that
particular review, right? Yeah, so here
the model was not only browsing through
the code base, but it actually decided
to form some hypotheses and write some
Python code to test the hypothesis and
check whether it's actually correct and
show it on a couple of examples. That's
really cool. And I'm curious like how
was this model trained? Like did we do
anything specific to like make it so
good at like catching bugs? Yeah, so it
is part of the Codex training, but we
added some specific tasks in which we
wanted to really prioritize catching
bugs that actually matter and people
would be willing to fix in real life. We
also made sure that we aimed for very
high precision rate. When we evaluated
it against the previous generation of
the models, we have shown that it has

[00:04]
much lower incorrect comments rate. But
to be fair, the most important
evaluation is just people using it in
practice and it finding the real bugs
and simultaneously not being annoying by
outputting too much comments. Mhm, yeah.
So, you showed us like a couple examples
with GPT-OSS. Now, I'd love to touch
more on like how we use it internally at
OpenAI. Yeah, we've already used it for
a while, and we have gotten a lot of
examples of it really saving us from
having critical issues. So, it saved us
from having some important training run
bugs that would potentially delayed some
important model releases or some
configurations that would not be
normally visible just from the diff
alone. It also allows us to more
confidently contribute to the code bases
that we're not fully familiar with. So,
for example, here we have Alex, our
Codex PM, contributing towards the VS
Code extension Yep. and implementing a
change. Code review model decided that
it's not the correct way to implement

[00:05]
it. Right, it sounds like it caught a
bug in terms of like removing a React
prop here with the CSS. Yeah, it was not
really possible to spot this bug without
understanding of the broader code base
here. But then, I love Alexi's follow-up
as well. At Codex, fair enough, fix it
up cuz you can keep on going with this
conversation and and ask Codex to take
it over. Yeah, after code review bot
produces a finding, you can always ask
Codex to trigger a new task and actually
fix it, which is a very nice workflow to
do. Yeah, that's really amazing and
really the vision of having Codex at any
point and any surface as your teammate
that's able to kind of do work for you.
And what I love about like Codex code
review here in this case is that you may
have like amazing engineers on your
team, but they may not have like many
hours to spend to kind of not just look
at a diff, but like run every possible
scenario in their head. And here, you
have Codex that's able to do that in its
own time. And one thing I wanted to
touch on as well is that we now have

[00:06]
like agents.md, right? This like open
format for coding agents, including
Codex,
to kind of like follow some specific
instructions. Have you like used
agents.md like in your case to kind of
give Codex code review some extra
instructions? We actually trained the
model specifically to be steerable
either with with custom user
instructions or look for agents.md
within the code base.
So, if you add some custom code review
guidelines to your package, that would
help model to understand the code base,
but also potential requirements about
what it should pay special attention to
in code review, or maybe what kind of
problems to ignore and don't bother your
developers about. That's awesome. Uh you
can even like ask some custom special
instructions about the style it responds
to. So, for example, since I needed a
little bit more validation, I wanted
Codex to tell me every time I make a bug
that I'm still an amazing programmer.
That's awesome, and you are.
Uh what we've been looking at here so
far is been Codex reviewing code in the

[00:07]
cloud. But just recently, we also
introduced review in the Codex CLI. So,
you can have a review in the terminal as
well. So, very often, you want to review
the code already before it makes it into
the GitHub. For that purpose, CLI is
perfect. And it also can execute more
things locally on your computer. So, you
could just /review
in order to tell the model to review
your current changes. And we're going to
improve on this feature a lot over the
next weeks. So, it's basically like
making sure all of your changes that
you're introducing locally don't have
like bugs before you submit them to to a
PR. Exactly. Amazing. Well, there you
have it, Codex code review.
So, with Codex, you now have an amazing
coding agent to pair with locally in the
terminal or in your code editor,
an awesome teammate to send tasks to in
the cloud at any time. You also have the
ability for Codex to review your changes
locally or your PRs on GitHub before
your co-workers even get to them. It's

[00:08]
going to help you catch bugs before they
hit production, and we can't wait to see
how that's going to accelerate your team
and ultimately help you ship better and
safer products.
Thanks for watching.
Back to work. Indeed.

</details>


#### Introducing the Codex app

See the Codex app in action and how it helps you build and ship faster.

video](https://www.youtube.com/watch?v=HFM3se4lNiw)

<!-- yt-inline:HFM3se4lNiw -->
[![Introducing the Codex app](https://img.youtube.com/vi/HFM3se4lNiw/hqdefault.jpg)](https://www.youtube.com/watch?v=HFM3se4lNiw)

<details>
<summary>자막: Introducing the Codex app (4:21)</summary>

[00:00]
Today, we're excited to introduce the Codex app.
Now you have one place to manage your
projects and delegate real work to Codex.
Instead of juggling terminal windows,
you get a single command center to
run and supervise agents.
Let me show you how it works.
On the left, you can see my projects.
And for each of them,
I can see the tasks that Codex completed,
and some of them are running live as we speak.
On the right, this is the main
conversation screen.
Let's start with this iOS app I've
been building.
It tracks the ISS in real time and
let's say I want to build new features for it.
I can type or better yet I can
just speak my mind and dictate.
Add a new screen that shows the
Astronomy Picture of the Day from NASA.
And that's it Codex is now taking care
of all that for me and
will figure out the right APIs to build it.
While that's running let's take a look
at another project I've been meaning
to migrate for a while.
Here Codex is updating all the
dependencies and in that task it's

[00:01]
even migrating from WebSockets to
WebRTC
for our speech-to-speech integration.
Now some of these tasks take a while,
minutes if not hours,
especially when you're working
on a large codebase. And
that's a big shift in how we build
software. Now you
can supervise your agents and
simply check in when they're done.
But let's go back to our first task.
Here you can see how Codex has been
approaching the problem
the steps it's taking and
the progress as it goes. And
it's done. Now if I click on
the right side I see the diff.
I can review exactly what changed in
the Swift code,
I can leave in-line comments for
feedback, ask for another iteration
or just merge if it looks right. Now if
I need to go deeper I can always
open the changes in
Xcode but in this case I'll just build
and run the app directly from here.
Working with the Codex app makes
building more fun, you know,
I don't have to
spend a lot of time editing code but
rather just thinking about how to
shape the app the way I want it
to be. Let's bring the iOS simulator on screen

[00:02]
and here it is. I just gave one
sentence to Codex and
it built this entire new
feature for me. Isn't that amazing?
Let's switch to another project I've been
working on. It's a web-based fitness
tracker. Well for visual tasks like this
one I want to stick closer to the
experience I'm building. So
by clicking on
top right corner I can pop the
conversation out like this and
bring Codex with me and I can dictate,
animate the bars to simulate progress
and now I'll be able in a few
seconds to see the changes
apply live, it really feels like
collaborating with a teammate and
here we go. Now another powerful
part of the Codex app is skills.
Skills let Codex connect to all of
your favorite tools.
In fact, this app was actually
implemented using the Figma skill,
which automatically used MCP behind
the scenes and set things up for me.
Let me quickly show you the design.
This is the homepage and if
I click one component,

[00:03]
for instance, you can see how the
spacing, the textiles and
all of that are defined right there.
So Codex has not been working from
a screenshot.
It's actually reading the structure
of the design file, including those
variables to generate real code using
our design system.
and that's why it matches the design so well.
Of course, you can also create your
own skill for yourself or for your team
so it can really fit your workflow.
Now, what's really powerful with the Codex app
is that you can even turn these skills
into automations.
Imagine you have tasks that you want
running at a specific cadence.
Maybe that's triaging alerts from
Sentry or bugs and tickets from Linear.
Well, you can now have that handled
in the background while
you focus on building.
There are many more features in the
Codex app, including working with
isolated environments
called worktrees, so this way you can
give each agent a copy of the code
so you don't have to worry about
conflicts or
breaking your setup.
You can also delegate any task,
especially the long-running ones,

[00:04]
to Codex in the cloud
with the exact same interface.
This was just a quick tour.
The Codex app is a brand new way
to build software.
For me, it means spending a lot less
time writing code and
a lot more time creating,
refining ideas and bringing them to life.
We can't wait to see what you build with it.

</details>

