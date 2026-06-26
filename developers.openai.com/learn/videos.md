<!-- source: https://developers.openai.com/learn/videos/ -->

## Search developer resources

# Videos

[![Codex for (almost) everything](https://i.ytimg.com/vi/Lm7-yFZ5fZQ/hqdefault.jpg)

#### Codex for (almost) everything

See the latest Codex app updates for working across more of the software development lifecycle.

video](https://www.youtube.com/watch?v=Lm7-yFZ5fZQ)[![Introducing the Codex app](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:Lm7-yFZ5fZQ -->
[![YouTube Lm7-yFZ5fZQ](https://img.youtube.com/vi/Lm7-yFZ5fZQ/hqdefault.jpg)](https://www.youtube.com/watch?v=Lm7-yFZ5fZQ)

<details>
<summary>자막: YouTube Lm7-yFZ5fZQ</summary>

_(자막 없음)_

</details>


#### Introducing the Codex app

See the Codex app in action and how it helps you build and ship faster.

video](https://www.youtube.com/watch?v=HFM3se4lNiw)[![Codex in JetBrains IDEs](https://cdn.openai.com/devhub/resources/video-3.png)

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


#### Codex in JetBrains IDEs

How to use Codex inside JetBrains IDEs like Rider, IntelliJ, PyCharm, and WebStorm.

video](https://www.youtube.com/watch?v=1XkVsE9-ZK4)[![Codex code review](https://cdn.openai.com/devhub/resources/video-4.png)

<!-- yt-inline:1XkVsE9-ZK4 -->
[![Codex in JetBrains IDEs](https://img.youtube.com/vi/1XkVsE9-ZK4/hqdefault.jpg)](https://www.youtube.com/watch?v=1XkVsE9-ZK4)

<details>
<summary>자막: Codex in JetBrains IDEs (9:48)</summary>

[00:00]
It's really important for us that Codex works anywhere you like to code.
For many of you, that place is your JetBrains IDE.
So we're super excited to announce that one of our most requested features is finally here.
Codex now works in JetBrains.
You can now collaborate with Codex directly within JetBrains IDEs
using your ChatGPT subscription, API key, or your JetBrains AI subscription.
And with me, I got Gleb from JetBrains,
who's going to give us a quick tour of Codex in JetBrains.
We know developers use our products on complex problems.
And that's where JetBrains and Codex really shine.
So I wanted to show you Codex's work on real projects inside my IDE.
It's a multi-platform Kotlin codebase for our conference.
It runs on mobile, web, and even desktop.
I'll show you how Codex helps with debugging and feature implementation
on that scale right within your IDE.
So let's start probably with the fact that you don't need to use JetBrains AI subscription to log into Codex.

[00:01]
You can use your ChatGPT account to log in or add the API key to do that.
So I'm going to log in in my Codex account, which is already done.
And then I want to, first of all, ask what this project is about, totally.
Totally, it makes sense.
Good way to start. So we can see Codex beginning to look at different files,
reading the file system. Exactly. Yeah. So it collects some context and understanding of what
does the project do. So as you can see, it's our Kotlin Conf app. By the way, you're welcome.
And so, yeah, it runs on Android, iOS, desktop, and web using the framework called Compose
multi-platform. So I will try to build this project right now to see how it actually looks like on iOS.
Cool. So this is compiling it for iOS and then

[00:02]
It compiles the project for iOS using Gradle technology. We're using the IntelliJ tools for
that. But as you can see, there are some errors, right? So, and I will probably need
to help of Codex to solve that.
So what I do is I'm just simply copy and pasting everything
that is read here and asking Codex to help me solving that.
So we can now see Codex is jumping through different tasks,
looking at the files that might be impacted based
on the stack trace.
Exactly.
And you see what exactly Codex does.
So it provides some reasoning on the certain actions that it does.
It shows the files that it's read and so on.
And this is the same Codex that I get when I run Codex CLI or if I use it in a different idea?
It is exactly the same Codex just because inside JetBrains we run evaluation to make sure the quality of CLI Codex is exactly the same as the one that users receive inside AI systems.

[00:03]
Amazing.
And it looks like it did some file changes here.
Yeah.
So actually, we can take a look on the exact changes
to make sure that they actually make sense.
You see the Codex has finished its work.
And we can try to build the project again, right?
Fingers crossed.
See if it builds.
These are just warnings, so it's not a problem.
And it builds.
All right.
Does it run?
Developers usually don't like dealing with the build issues,
and it's quite difficult to understand what exactly is happening
when the project is building.
So Codex does an amazing job understanding what exactly needs to be done here.
Yeah, we didn't really have to give it any guidance.

[00:04]
It just runs around and we figure things out.
We didn't even need to read through the errors that are here, right?
So, yeah, the app is working.
and now I guess it's time to give Codex a little bit more complex task, right?
We know that the biggest problem for all the mobile developers is localization, right?
So just because it's quite a mundane, complex task
that does not involve a lot of kind of visual changes,
but at the same time it is extremely important.
Probably the best task to give to an agent.
Sounds great.
I have a problem that I'm going to base here.
and I'm going to ask, create a localization to Spanish
for the conference app that we have.
Awesome. Let's fire it off.
While Codex is working, we still can oversee
what kind of files it looks at,

[00:05]
what kind of reasoning behind looking at these files.
When it runs the bash commands,
we can see what kind of commands it runs.
At the same time, so different developers have different tolerance towards what agent does, right?
And this is something that we consider inside our integration, where user can select different types of access modes to agent, right?
So we can restrict agent 2 from editing any file.
So it would be just read-only, extremely suitable for understanding complex code bases, or let's say search when a user just doesn't know where the certain file is located.
Agent mode allows to run commands, but at the same time it requires user approval for every command so that some quite sensitive commands would be user-reviewed.
And full access, which I currently have, actually allows agent to run any command they want, apart from the riskiest ones, and change the code files.

[00:06]
Awesome.
And then you can see, are you able to click on the actual files that it's checking out?
Yeah, so you can take a look at the file.
So it opens in IDE, so you can take a look at what exactly is written in this file
as the changes come.
That's awesome.
And I think one of the things that's interesting
is it looked like Codex was doing a lot of research
across the code base
so that if you have a complex code base,
it's going to go and first understand all the context
because we didn't give it any guidance, right?
We just sort of like say, here's the problem.
But now it's sort of like locked in
and it's just like hammering out code change after code change.
Exactly, exactly.
It's like you put a developer
that does not know a thing about this code base to a task.
So the first thing they do is to research the code.
That's right.
So agent here exactly mimics these actions.

[00:07]
Doing the research is not changing anything just because they don't know yet about the codebase.
But so once the research is done, the code changes are coming.
Amazing.
It feels like it's like everything is still very much right inside your IDE.
Exactly.
You don't have to change any of your behaviors that you're used to.
So it's just a sidebar, right?
So while agent is working, you can even close this tab and start a new conversation and asking about something else.
Or you can continue working on the files that you worked with.
So the work of an agent is paralleled with the work that developer does.
And it does not intervene with that.
So a developer does not need to wait for agent to finish working to continue their work.
They kind of coexist elegantly and parallel.
So now it's running a shell command here.
So it looks like it's running Gradle.
It tries to compile everything.

[00:08]
Yeah.
And this is like one of the interesting things about Codex.
Codex always tries to verify its own work.
So being able to then tap into the build tools and using them.
And that's an amazing part, right?
So just because just writing code is not enough.
You need to make sure that the code actually works and reiterate on that if it doesn't.
And as you can see, some of the commands are skipped.
and it's done.
You see?
So the Codex listed the files that were changed, right?
So we can take a look at the lines
that were actually updated or removed.
We can see them in a commit tool window
that they are uncommitted yet.
So we can push them to the repo.
But first of all, let's make sure that it actually works
and rerun the app to see whether the localization
actually takes place.
Cool.
And for that, we're just using the same tools
that we're used to in the IDE already.
Exactly, yeah.
So it's building, starting up the iOS simulator.

[00:09]
It starts the simulator, and I'd expect the app to be already in Spanish.
Cool. Let's see.
Oh, yeah, I can see your simulator is set to Spanish already.
It's set to Spanish just because the app is going to take the localization from the system.
So if everything went fine, the app would be already in Spanish.
And that's how Codex is natively integrated in our products.
What I showed you was all done in IntelliJ, but it also works in other JetBrains products like PyCharm, WebStorm, or Rider.
Thanks, Gleb.
These are just a few of the things that you can build with Codex inside JetBrains.
To get started, go to openai.com/codex or choose Codex inside the AI chat of your JetBrains IDE of choice.
Thank you, and we can't wait to see what you build.

</details>


#### Codex code review

Walkthrough of how Codex drives end-to-end pull request reviews with the new onboarding flow.

video](https://www.youtube.com/watch?v=HwbSWVg5Ln4)[![Build beautiful frontends with OpenAI Codex](https://cdn.openai.com/devhub/resources/video-1.png)

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


#### Build beautiful frontends with OpenAI Codex

Learn how OpenAI Codex's multimodal abilities accelerate frontend development.

video](https://www.youtube.com/watch?v=fK_bm84N7bs)[![Building with Open Models](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:fK_bm84N7bs -->
[![Build beautiful frontends with OpenAI Codex](https://img.youtube.com/vi/fK_bm84N7bs/hqdefault.jpg)](https://www.youtube.com/watch?v=fK_bm84N7bs)

<details>
<summary>자막: Build beautiful frontends with OpenAI Codex (8:29)</summary>

[00:00]
Hey everyone, I'm Roman. Codex is your
AI teammate that you can pay with
everywhere you code. Whether it's on
your computer with Codex CLI or the ID
extension or Codex cloud that you can
send tasks to anytime from the web or
your mobile phone. But one superpower we
really wanted to zoom in today is its
multimodal capabilities. But it's even
more magical when the model can have
vision understanding but also the
ability to check visually its own work.
Today I'm joined by Channing who helped
train the model to tell us more. Hi, I'm
Channing from the research team for
Codex. One of the big things we've been
focusing on is trying to give the model
more tools to leverage its multimodal
capability to just be a better software
engineer. In the same way that I might
check my own work and make sure that
things visually look the way I expect
them to, we want to have the model be
able to do that in a tight iteration.
>> That's awesome. Why don't we kind of go
through an example to see how it works?
>> Sure. We have one the last like one of
the demo apps we showed at a previous
dev day. It has one screen to kind of

[00:01]
discover destination and one assistant
where I can just type in some place.
Voila. Harris, what would you like to
know about?
>> So pretty awesome, right? But I think we
can do better with codeex now. We have
the ability to kind of take it to the
next level. So I thought why don't we
kind of whiteboard together how we could
make like this home screen more
engaging.
>> Sure. You could have like a globe in 3D.
>> Okay.
>> And as the user kind of spins the globe,
they could see the pens to explore. They
could also navigate left and right.
>> Sure. And the extra details for each of
the cities, too. Right.
>> Right. Like Tokyo. Mhm. And like all of
the details that might be like useful
for the destination.
>> Sure.
>> I think that that sounds like a good
place to start, right?
>> We should be able to just take a quick
photo of the uh the app as we sketch it
up here. We'll just go into chat GPT.
>> Yeah. Add a codeex task. Put in the
photo
and then you should be able to just
describe what you want.
>> Redesigned the home screen of Wonderlust
to show a 3D spinning globe on the left.

[00:02]
Details on the destination on the right.
The user should be able to fluidly
navigate across the globe. When they
click on the pen, they should see the
destination. And you can also map the
left and right arrows of the keyboard.
Boom. I'll just send that prom codeex.
>> Perfect. I think it should be able to do
that.
>> Perfect. Also, while we're sending that
task off, we could add an extra screen
to the app. Maybe we call it something
like the travel log. Okay.
>> Kind of like dashboard of their stats
and all that.
>> Uh, we could do like a full checklist if
you wanted to get all the contents.
>> Oh, great. I love this. Continents
checklist.
>> Could do like bottles of wine drunk
personally.
>> That's a great one. Okay. Bottles of
wine.
>> Sure.
>> Uh maybe photos taken as well.
>> Okay.
>> Maybe we'll come up with a pie chart or
whatever makes sense.
>> All right. Add one more screen to the
app called travel log. It's like a
dashboard of fun and interesting stats
for the user. Make sure the app is
responsive on mobile and make sure the
design is also consistent with
everything else. All right. And I just
send this to Codex
>> and we'll let it work.

[00:03]
>> So while this is working, I was thinking
like could you uh maybe walk us through
an example or two that you've already uh
use Codex multimodel capabilities for?
>> Sure. Love to.
>> Let's do it. Uh how I would start
usually is I would make a change. I'd
ask Codex to do it. It would, you know,
most of the time do the right thing.
Sometimes better than I expected it to.
Sometimes I want to make some tweaks and
I would take a screenshot and maybe send
that back into the app. Some of the
other people who are doing, you know,
front end development full-time as
opposed to as a side thing, they're uh
using the Playright MCP. So actually
giving the tool in the same way that the
cloud has the ability to open a browser
and look at the web app they're running
in their loop they're able to have the
model take a look at the the application
as they're working on it and check its
own work.
>> So that's when you use Codex CLI locally
for instance that you can use that and
CEDX cloud would do the same here for
the task we just sent.
>> Exactly. And then in the cloud we give
it a set of tools that are hopefully
expressive and flexible so it can
accomplish its goals and then if you do
the same thing through the MCP it can do
the same.
>> Yeah. It's really amazing how we can

[00:04]
harness those like aentic coding
capabilities, right? Whether it's in a
cloud container or like locally with
these tools. Do you have like an example
for instance that you tinkered with and
be curious to see?
>> Yeah. So, a lot of times uh you're
trying to like win someone over and one
of the best ways to do that is to
present a lot of data and it would be
you know great to work through stuff on
a whiteboard and you know build up
graphs and stuff but it's hard to to
present the data that way. Um, and so
actually a use case a lot of people have
been doing recently is they have codecs
like turn over the data or like dive
deep into a very complicated codebase
and present some visualizations or break
things down and build just like
sometimes a throwaway web application.
And so it's just like a single page that
they can, you know, they don't even need
to keep the artifact around, but you
might share the screenshot with someone.
>> That's such a fascinating use case.
>> And so I actually before we started
this, I uh gave the model uh a bunch of
open data. So New York City actually
publishes like taxi cab information. So
information about rides around the city.
And so I actually loaded that just the
data into a container and let the model

[00:05]
train on that to try to build a
dashboard. And so it actually turned out
some pretty interesting stuff, you know,
at least different theming
>> and different ways to get a structure
and present the data.
>> Mhm. It allows you to add basically
exactly as much fidelity as you want. So
like when we were over at the
whiteboard, you can do like a very thin
sketch and like have the model fill in
the details. If you wanted to take a
screenshot of a very specific like I
want my component to look this way, you
can feed that in and it'll it'll try its
best to accomplish that.
>> Yeah. You can go all the way from like a
napkin sketch like to a Figma mo
application.
>> Mhm.
>> I don't have to check this out. I don't
have to run it local. I can just like
take a look at the top level what design
I like and then I can iterate from
there.
>> Why don't we go back now and check uh
the two tasks that we sent from the
whiteboard?
>> So I guess this first one is uh where we
asked it to do the 3D globe and it looks
like it did that for us. Oh wow.
>> So looking through the log, yeah, it
pulled in 3JS, so it's actually like
animating this, building it all out. It
has a texture for like how the globe
should look.
>> I mean, it looks promising to me, but
I'm really curious to see if the
animations actually work. Do you want to

[00:06]
check out that PR locally?
>> Let's uh Yeah. So, we create a PR.
>> Yep.
>> And then we should be able to just in
the terminal check it out and then start
the dev server.
>> Oh my god.
>> All right.
>> That's incredible. Oh, the globe is is
spinning exactly like we said. It even
decided to put a tool tip on top
>> to tell how to explore.
>> Uh, that's amazing. And if you click on
one,
>> damn, it works. And it even has the
button to open the assistant.
>> Why don't we now check the travel lock
screen that we wanted to add and see
what Codex came up with.
>> So, it gave us a couple options to look
at.
>> Well, that one is really good. Oh,
>> it really matches the design of the app.
What about the mobile view? Uh,
>> so we asked to make sure that things
were responsive and so you can see it
actually took two screenshots here. It
took one at like the full desktop
resolution or like a common desktop
resolution and the other is a a common
mobile view. And what's nice is it took
like the full screen.
>> Yeah.
>> Even if it's not in that, you know,
above the fold section, you can still
see if there's an error or some, you

[00:07]
know, overlap.
>> And I'm sure that can apply to anything,
right? If I were to say make sure it
works in uh dark mode, it would take as
many screenshots as I want.
>> Yeah. Internally, people have done
exactly that. They've run their
component through like light mode, dark
mode, responsive, different sizes. Like
they have uh our design team has like
different stops. They want to make sure
everything looks good at and so you can
actually like make that part of your
prompt that you want to see all these
things and make sure you check it before
it gets PR.
>> What are some other things that you are
excited about uh multimodality and maybe
like things that you're thinking about?
>> Yeah, one of the first tools we gave it
is a browser tool and so it's ability to
to look at a website and a web
application. I think there's a lot of
other multimodal software development
tasks where being able to check your own
work in a tight iterative loop will be
an important thing. So I I think we're
trying to look at how to do uh like
mobile engineering I mean even desktop
applications. Web was really kind of a a
proof of concept to make sure we got the
loop working.
>> Thanks Jenny.
>> No problem. This was a quick tour of
multimodal capabilities in codecs. We

[00:08]
know models perform better when they can
check their own work. And previously we
could only do that with backend code.
But now by harnessing the multimodal and
agentic capabilities of GP5 codeex,
we've also unlocked that for front-end
coding. And we hope this gives you some
ideas for how you can pair with Codex as
a creative partner. To get started, go
to chajgpd.com/codex.
Thanks for watching.

</details>


#### Building with Open Models

Talk covering how developers customize and deploy OpenAI’s open models.

video](https://www.youtube.com/watch?v=1HL2YHRj270)[![Context Engineering & Coding Agents with Cursor](https://cdn.openai.com/devhub/resources/video-3.png)

<!-- yt-inline:1HL2YHRj270 -->
[![Building with Open Models](https://img.youtube.com/vi/1HL2YHRj270/hqdefault.jpg)](https://www.youtube.com/watch?v=1HL2YHRj270)

<details>
<summary>자막: Building with Open Models (22:37)</summary>

[00:00]
Good afternoon everyone. My name is
Dominic Kundal and I work on developer
experience here at OpenAI. Before we get
started, a quick raise of hands. How
many of you are using a combination of
open and proprietary models?
All right, that's quite a lot. How many
of you are using or have used GPOSS
before?
All right, that's uh more than I
expected, but hopefully we can get it to
100% at the end of the talk. Um, so over
the next 25 minutes, we'll talk about
GPTOSS, our latest open model series
that we released in August earlier this
year. Uh, why you might want to use them
and how they fit into the broader OpenAI
ecosystem.
But first, what is GPOSS? GPTOSS is our
model family consisting of two models.
GPOSS 20B, our medium-sized model that
can run on higherend consumer hardware
with at least 16 GB of VRAM. So, a

[00:01]
top-of-the-line consumer graphics card
or recent mid-tier MacBook. And then
GPUs 12B, our larger model that can run
on a single 80 GB GPU like an Nvidia
H100 or an AMD Mi300X or even a
top-of-the-line MacBook like this 128 GB
MacBook Pro.
But why did we build these models? Well,
first of all, because you all kept
asking us to.
But uh joking aside, we know that
proprietary hosted models aren't always
an option for you. Whether you have data
requirements where your data needs to
stay on premise for safety or privacy
reasons or you have specific hardware
requirements where your data needs to uh
stay on or you have specific hardware
requirements or latency requirements or
maybe your use case is has to run
completely offline because of flaky or
non-existent internet connections.
There's a wide range of reasons why you
might want to pick an open model and we
know that a lot of you already have to

[00:02]
deal with that mix of proprietary and
open models for your use cases. Because
of that, we wanted to make sure that we
offer you the best possible experience.
Both of the open models are reasoning
models with variable levels of reasoning
and raw chain of thought access. And
they're the only open models that can
perform tool calling as part of the
chain of thought, including web browsing
and Python tool calling. Meaning the
model can combine a series of tool calls
and reason between them to make uh uh to
more effectively achieve complex tasks.
And both of the models are permissively
licensed under the Apache 2 license,
meaning you can use them both in
commercial applications or fine-tune
them to make them your own as long as
you adhere to local laws in your region.
These models should also instantly feel
familiar to you if you've used or other
reasoning models like Open AI's 03, 04
mini or GPT5 as they introduce the same
variable reasoning, chain of thought,
function calling, browsing, and Python
capabilities.

[00:03]
In fact, GP2s 12B and 20B have nothing
to hide when you compare them to 03 and
04 mini. On humanity's last exam, for
example, a benchmark designed to test
knowledge of uh test AI at the frontier
of human knowledge. Both GPUs 20B and
12B perform on par with O4 Mini. Except
in our case, GPOSS 20B can run entirely
locally on your laptop.
And even with complex math problems like
Amy 2025, the models are able to keep up
with 03 level performance. to repeat
that that is real state-of-the-art level
intelligence that you can run now
locally on your computer
and these models are designed to be used
in agentic use cases. So function
calling performance is incredibly
important in Towbench retail for example
which tests the model's ability to use
tools to resolve a retail customer
service issue across multiple turns. Uh
both models are performing extremely
well especially given their size

[00:04]
and overall the models fit very well
into our open AI ecosystem. You can use
them in the agents SDK or with codec cli
and increasingly more providers like
grock hugging face vlmvidia
and as of today LM studio have started
offering their own responses APIs. That
way they should work directly within
your existing projects and allow you to
mix and match them with other open
models.
And when building these models, we tried
to really listen to community feedback.
And two of the biggest asks we heard
from the community were for one us to
not hold back when it comes to
capabilities, especially for agentic use
cases, and to have efficient models. And
we tried to balance these two and are
pretty happy with the result in the
overall um open models market space,
striking a great performance between a
great balance between performance and
size.
And the feedback from the community and
our partners has been great so far. In
total, it's been downloaded over 23
million times on our hugging face

[00:05]
organization alone. And people love
using the model for local use cases, its
tool capabil tool calling capabilities,
and the overall cost efficiency of the
model.
Some of my favorite use cases of GP2s so
far came from our six week long
hackathon that wrapped up a few weeks
ago. You'll see some of the examples
later on in the developer state of the
union, but we've seen people use we've
seen people use GPTOSS for controlling
robots, discussing sensitive topics in
their own personal diaries, fine-tuning
it for uh to be a subject matter expert
on highly specialized topics or even
just to be a better storyteller. have it
used in offline coding assistance and
even use it use its coding ability to
create a fully on premise cyber security
operations center to help protect
systems without disclosing sensitive
data just to name a few. That's why
we've invested in GPOSS
to give developers the flexibility and
control to build the models the the the

[00:06]
way that they know best and to run it
anywhere. Enough talking though. Let's
actually see GP2S action in a couple of
examples.
So since GPUs is an open model um
there's a wide range of ways that you
can run and host it on servers. You can
use frameworks like VLM and transformers
or for local inference you can use
projects like Llama CPP LM Studio or
Lama. For this demo we'll actually build
a chat agent that will help me keep
track of my finances without revealing
my own private financial data and by
leaving it entirely local. To power the
agent, we'll run GPUs 12B. So that's the
larger model completely locally on my
MacBook using Olama, but the same thing
should work with other inference
solutions.
I've already downloaded the model on my
laptop since I didn't want you all to
watch me download 70 GB on conference
Wi-Fi. Um, but because of that, we can
actually go and turn off our Wi-Fi here
since the model is entirely local. All

[00:07]
right, we've turned off the Wi-Fi and
with that we're completely at the will
of the of the model and the demo gods.
So, wish me luck. We can see if the
model is running by using the Olama CLI
here
and send a friendly greeting to the
model and we can see the model going
through its reasoning process and
responding accordingly. All right. So
now that we know that the model is
running, we need to use uh we need to
use a local API to integrate it into our
app. Olama and most inference providers
um already provide a chat completions
API, but in our case, we want to harness
the full power of the model. So instead,
we'll run our own responses API proxy
that
Let's get out of here.
All right. Hi. There we go. Um, we're
going to run our own responses API proxy

[00:08]
that we shipped as part of GPUs and that
is available on GitHub. This proxy will
expose built built-in Python and
browsing tools on top of sending the
token generation to our inference
provider in this case running on this
device.
Now, let's actually build the agent. Uh
for this I'll be using the agents SDK
for TypeScript to build our finance
agent that powers the chat interface
that you can see on the right. We
already have a very basic setup here
where we have the chat interface hooked
up to the agent on the left and then
configure the agent to use our locally
running responses API and for it to use
the Python code interpreter as a tool.
So right now this agent is pretty
generic. Um but we can see what it can
do by asking a question like what is the
square root of
some random number
and we should see as I mentioned earlier
that the model can perform tool calls as

[00:09]
part of the chain of thought. So you can
see here um it's starting to think
through the steps it has to do. it tries
to use the Python code interpreter,
realize that it actually was trying to
use some uh dependencies that it didn't
have and correct automatically. This is
the same kind of behavior as what you
would see from models like GPT5, 03 or
04 mini, except that in this case it is
completely offline. That means we can
build agents the same way that we're
used to with these models, but for
sensitive data that might have to remain
on premise.
for my finance agent, for example, I
have a bunch of financial files um
scattered in my directory, but I should
probably clean up this situation because
there's a couple of files that I don't
want to have leave the system. Um but
since we're running the model locally, I
don't actually have to worry about this.
With GPUs, we can equip our agent with
the necessary tools to handle sensitive
data while keeping the data entirely
local. to connect uh to the file system.

[00:10]
We're actually going to use an MCP
server that exposes the necessary tools
for the agent to browse and open files.
Let's add the MCP server
and then connect to the MCP server again
entirely locally and provide it to our
agent here.
We can now check if it if it works by
asking how many files are
in the top level.
And you can see it's going through its
reasoning steps again using the
different MCP tools to browse the system
and get the information. And we get an
answer. So now let's try a more complex
question like summarize my overall
portfolio growth
in 2024 in percentage

[00:11]
and this is where you can really see the
power of GPTOSS coming to uh coming into
place where we're using the tools as
part of the chain of thought. performs
multiple requests to the file system
things, write some Python code to
interpret it and then give us an answer
um directly to us without having to um
go back and forth with the user. Now,
now all of this has been fully running
offline leaving the data entirely on
premise. But especially if you're using
the smaller GPUs 20B model, there might
be moments where you need the model to
know more or you're hitting other
capability limits. For that, we're
actually going to connect back to the
internet. And I'm going to show you two
more things. One, I want to provide the
model with the ability to do web
browsing. And two, I want to give it
access to GPT5 for some additional
tasks.
For browsing, the model was trained on a
generic browsing tool, meaning that you
can build entirely your own browsing
browser tool on your proprietary search
provider, run your browsing through your

[00:12]
own proxies if you want to apply content
filters, or even have a fully offline or
on premise search index. In our case
though, we're uh we'll use an example
search provider. We have two on GitHub.
One is Exa and the other one is u.com.
And in our case, we're going to use the
XA API.
This is already set up by us using the
responses API proxy that we're you uh
that we set up earlier. So I just have
to enable it. But how enabling web
search works will depend on your
inference provider. And the same goes
for Python. So some of the inference
providers might not support this yet. I
also want the agent to be able to create
me little interfaces uh to be able to
dive into the data that I'm working
through. While the model is great at
coding, it's not our best model for
coding. For that I actually want to give
it GPT5 as an agent that our agent can
use as a tool.
So in this case
I already have an HTML HTML agent here

[00:13]
that is using GPT5 and is specialized on
writing inter interface code in HTML and
nothing else. I also have an input guard
rail here that checks if anything looks
like a social security number to avoid
accidentally passing any sensitive data
to my remote GPT5 model. You could do
the same check type of checks with other
confidential data that you want to make
sure stays on premise.
All right, we need to still add this
here.
So I'm going to pass it in and I'm just
going to give it a tool name of
generateization.
And with that we can ask a task like
create a bar chart of my individual
stock gains in 2024.
Got to put a comma there.
All

[00:14]
right.
Now we we should see the model going
through the same steps again. Reading
the f reading the necessary files crunch
using Python to crunch the necessary
numbers and then using GPT5
once it has the data. See,
so you can see here it was calling the
code interpreter to actually process
that um file. Seems like it messed up
something and like this is the benefit
of that chain of thought reasoning and
it can actually go and recover.
So um every once in a while you might
run into these situations. Uh there we
go. Got the data.
Um
oh there you go. Now it's calling the
generate um generate visualization tool.
And you can actually see here that
because my
social security number check is

[00:15]
relatively rudimentary, every once in a
while it might run into things where
like that regular expression gets
triggered. So in this case the model
realized that and again selfcorrected
and performed another tool call to the
model here. And now in a second we
should get back the result.
See? Come on internet.
All right. While we're waiting for that,
let's move on. As you saw, GP There we
go.
All right. Thank you.
Um, so as you saw, GPOSS seamlessly fits
into the broader OpenAI ecosystem. We're
able to write a uh write an agent the
same way using the agents SDK tools that
you're already familiar with. Run it
entirely offline and the model behave
the same way as our other reasoning
models do. And we're able to leverage
GPT5 for task that is less equipped to
do.
One more thing though that we can do

[00:16]
with GPUs is to make it our own by
fine-tuning it. Maybe you're not quite
happy with the performance of GPTOSS on
a specific topic or task. Or maybe you
want the model to be a subject matter
expert on a specific field or some
internal data. Traditionally, that would
mean that to use a technique called
supervised fine-tuning where at a high
level, we give the model a bunch of
input and output examples and train the
model on those to get better at similar
inputs. However, with GPUs's reasoning
capabilities, a more interesting way of
fine-tuning and personalizing GPUs is
doing additional reinforcement
fine-tuning where we give the model
inputs and a reward function that tells
the model how good the output was. To
give you an example of fine-tuning, um
I'm we're going to briefly see it in
action, but since watching a model
fine-tune for hours might not be the
most interesting thing you can do today,
uh I already fine-tuned a model ahead of
time.
So before I explain you what we did, how
many of you know this game of 2048?

[00:17]
All right, cool. So in these games, for
those of you who don't know, uh the as a
player, you try to combine different
tiles with the same number that are next
to each other by swiping up, down, left,
right, and to merge these tiles and
eventually reach 2048. We wanted GPUs
20B to play the same game by having it
write a Python function that encodes a
strategy to actually play the game. And
as you will probably see here, the base
model is decently okay at playing it,
but occasionally writes wrong or very
basic code where it doesn't get far in
the game, especially on low reasoning.
So, if we're testing this out here, um,
seems like this did okay, but it
definitely didn't get very far on the
board.
So instead, we fine-tuned a dedicated
model by giving it a reward function
that takes the board strategy and then
place boards on it. So that and then we
used a and to see how far it gets and

[00:18]
then we used a technique called uh gpo
uh which is a reinforcement train uh
reinforcement fine-tuning technique and
a tool called unsllo to actually
fine-tune the model. This is a
non-trivial amount of code. if I scroll
through this entire uh entire notebook.
So if you do want to check this out, uh
it's available on our GPOSS GitHub page
and you can check it out there and retry
it yourself.
So let's actually see this in action. Um
by having GPUs and uh and our fine-tuned
version each generate five different
strategies here. So uh we can see the
model is starting to kick off all of
these different Python strategies. It's
a bit harder to read at the second while
it's still generating. But every once in
a while, both models will return some
more like rudimentary techniques, uh,
rudimentary strategies.
But it's also pretty hard for you to
distinguish between them and which one
is better or not. So, in order for us to
figure out if the model actually did a

[00:19]
better job, we're going to have the two
models with these five strategies play a
100 boards against each other to see
which one gets better. So, we're almost
there. Some of them are still
generating.
Um, let's see how many. One. All right.
Looks like we're done here. So, let's
run this. And
demo gods. Come on. Yes.
So, you can see model B, which is
actually our fine-tuned version of the
model, um, won quite significantly in in
the different games playing against each
other and also got it overall a total
higher score.
All right, I do have one confession to
make though. I mentioned earlier that we
were running GPSS entirely locally. And
while that was the case for the first
demo, these two models were actually not
running on my device. They are still
running entirely locally though and not
on some GPU in the cloud. Instead, um I
actually got to run them on a very
special piece of hardware.

[00:20]
So years ago, uh, Jensen delivered the
very first DGX1 to OpenAI. And you can
see it here on the screen. It was a
milestone in compute. And while it would
be fun to run these two models on a
DGX1, it doesn't quite fit on the
podium. And you all would have probably
figured this out by now. So instead
though, I have a great alternative.
This is the DGX1 uh DGX Spark from
Nvidia. And this little beast contains
the same amount of compute as the DGX1
and in fact is currently running both of
these models, but also fine-tuned the
model while standing on my desk. You're
all some of the very first people
actually to see this live outside of a
lab. Um, and Nvidia was so kind to give
it to us for this demo. Um, in fact,
it's not available at all yet. There's a
pre-production system that Nvidia
provided to us to help get the system
ready for developers like you all. And
because it's still pre-production
hardware and software, it might not be

[00:21]
fully representative of its final
capabilities and performance, but it's
been a lot of fun to work with. Um, so
if you want to check out the code for
the fine-tuning to learn more and try it
out yourself, even if you don't have a
DJX Spark yet, um, you can find it on
GitHub.
All right, to summarize uh, what we've
seen so far, GPOSS is a great option if
you need to run the model locally.
um or on premise for example for safety,
privacy or low latency use cases. And
GPSS seamlessly integrates with uh the
OpenAI tools that you're already using
including the agents SDK and the codec
cli. So whether you're building an agent
that has to run locally or you're trying
to code offline, GPUs can be useful. And
GPUs and GPT5 can work hand inand
allowing you for this allowing you for
use cases where you need to run a blend
of models to get both state-of-the-art
performance and some of the benefits of
open models. Lastly, GPUs can be

[00:22]
fine-tuned for your own use cases,
giving you the ability to have your own
expert models on uh on your use cases
while leveraging the same intelligence
and capabilities of OpenAI's reasoning
models, all while running fully on your
own hardware of choice.
If you do want to learn more, you can
check out all of the resources on
openai.com/openmodels.
And with that, thank you very much.

</details>


#### Context Engineering & Coding Agents with Cursor

Session on structuring context for agent workflows inside the Cursor editor.

video](https://www.youtube.com/watch?v=3KAI__5dUn0)[![Live Demo Showcase: Tools That 10x Your Codebase](https://cdn.openai.com/devhub/resources/video-4.png)

<!-- yt-inline:3KAI__5dUn0 -->
[![Context Engineering & Coding Agents with Cursor](https://img.youtube.com/vi/3KAI__5dUn0/hqdefault.jpg)](https://www.youtube.com/watch?v=3KAI__5dUn0)

<details>
<summary>자막: Context Engineering & Coding Agents with Cursor (18:42)</summary>

[00:00]
[Applause]
I'm Lee and I'm on the cursor team and
I'm going to talk about how building
software has evolved. So, thanks for
being here.
We started with punch cards and
terminals back in the 60s where
programming was this new superpower, but
it was inaccessible to most people. And
then in the 70s, programmers grew up
writing basic on their Apple 2s and
their Commodore 64s. Then in the 80s,
gueies started to get mainstream, but
still most programming was done on
textbased terminals. It wasn't until the
'9s and the 2000s that we started to see
programming shift to graphical
interfaces. So Front Page and
Dreamweaver, which you might remember,
allowed beginners to drag and drop and
build websites. And new editors and
idees like Visual Studio made it easier
for professionals to work in very large

[00:01]
code bases. And I of course had to add
my favorite text editor, Sublime Text
here. I'm sure some of you have used it
before. It's a good one. Now with AI,
building software is becoming more
accessible and powerful than ever.
Unlike this slower shift from terminals
to the shift to write code with AI is
really being speedrun. The progress of
decades is happening in just a few
years. And with each iteration, the
interface and the UX is changing to
allow the models to achieve more
ambitious tasks. So I'd like to talk
about context engineering and how coding
agents have evolved over the past few
years from the perspective of cursor.
I'll show how we've went from
autocompleting your next action to fully
autonomous coding agents. And finally,
we'll have Michael Curser CEO talk about
the future of where we believe software
engineering is headed.
So, let's start with TAB. One of the
products that inspired Cursor was GitHub

[00:02]
C-Pilot. It showed that with
improvements to the UX of autocomplete
and with better models, we can make
writing code much easier. We released
the first version of tab back in 2023
and the experience has evolved from
predicting the next word to the next
line and then ultimately to where your
cursor is going to go next. Tab now
handles over 400 million requests per
day. And this means we have a lot of
data about which suggestions users
accept and reject. This led to us moving
from an off-the-shelf model to training
a model specialized for next action
prediction. So to improve this model, we
use data to positively reinforce
behaviors that lead to accepted
suggestions and then negatively
reinforce rejected suggestions. And
we're able to do this in near real time.
So you can accept a suggestion and then
30 minutes later the tab model has been

[00:03]
updated using online RL based on your
feedback.
Getting this experience right has taken
a lot of iterations. There's a delicate
balance between the speed of the
suggestion, the quality of the
suggestion, and also just the general UX
for how it's displayed. If it's slower
than 200 milliseconds, it kind of takes
you out of your flow. But you also don't
want to see fast unhelpful suggestions.
So with our latest release now, we show
fewer suggestions, but we have higher
confidence that they're going to be
accepted.
We find tab really helpful for domains
where AI models just aren't as helpful
yet. And the bottleneck here really is
your own typing speed. Now, most people
type at about 40 words per minute, even
though I'm sure all of you type at 90
plus, right? We've got some amazing
typists in here.
So what would it look like if we allow
the AI models to write more code for us?
This is where coding agents come in and
this is that next evolution of coding

[00:04]
with AI. You can talk to models directly
in products like cursor or like we saw
in codeex and have them create or update
entire blocks of code.
Something we've tried really hard to
make a focus in cursor is giving you
control over the level of autonomy of
working with the models. So, one of the
first features we added back in 2023 was
prompting models to add inline
suggestions. This would take your
current line as well as the broader file
context and then pass it to the model to
suggest a diff.
Shortly after, we released our first
steps towards a coding agent, which was
a feature called composer, which some of
the longtime cursor user fans may
remember. Uh, we even have a pixelated
Twitter demo that I've included here of
one of the first versions. This made it
much easier to do multifile edits with
more of a conversational UI.
And then in 2024, we added a fully
autonomous coding agent. This saw models

[00:05]
use more tokens as they were getting
better at tool calling and it allowed
cursor to self gather its own context.
So in the previous versions, you had to
provide all of that context up front,
which was a bit more difficult. So let's
talk about some of the ways that we've
optimized the cursor agent harness.
There's been a lot of talk recently
about context engineering as an
evolution of prompt engineering, which I
personally find really helpful. As
models are getting better, getting high
quality output is less about specific
prompting tricks, although those can
still help, but it's more about giving
the models the right context. And not
just any context, but intentional
context. Models get worse at recalling
information as the size of the context
increases. And in reality, you don't
want to push the limits of the context
window. You want to use a minimal amount
of highquality tokens. And this is why
the retrieval of code is actually really
important and fundamental to context

[00:06]
engineering. So let's look at an example
of searching code in a larger codebase.
We found that when you give models very
powerful tools, it can significantly
improve the rate at which code is
accepted.
Many coding agents now use commands like
GP or RIP Grep to look for direct string
matches across files and directories.
And as new models are trained on tool
calling and agents get better at using
tools, the search quality does improve.
However, we found that you can make
searching even better by automatically
indexing your codebase and creating
embeddings. So this allows us to have
semantic search. So I can ask the agent
update the top navigation, but if the
file is actually called header.tsx, tsx
semantic search allows the agent to go
and quickly and accurately find the
correct code during the retrieval
process
for generating embeddings. We also moved
from an off-the-shelf embedding model to
training a custom model that helped us

[00:07]
produce more accurate results and we
constantly AB test the performance of
using semantic search. We found that in
comparison to using GP alone, users
would send more follow-up questions and
also spend more tokens. So semantic
search is really helpful. One of the
biggest wins though is it shifts where
the compute happens. You spend the
compute and the latency upfront during
the indexing rather than at inference
time when the agent is actually being
invoked. So in other words, you're doing
the heavy lifting offline, which means
you can get faster and cheaper responses
at runtime without sacrificing
performance and putting that on the
user. So the takeaway here is you likely
want both GP and semantic search for the
best results. And we'll have a full blog
post soon that talks about some of these
results. So giving the models better
tools helps improve their quality. But
what about the UX of actually using
these coding agents? There's been a lot
of exploration with coding CLI from
OpenAI's codeex to claude to Cursor's

[00:08]
own CLI. And the idea here is to find
the most minimal abstraction over the
model, kind of iterate on the harness
and then make the agent extensible. But
we don't believe CLIs are the final
state or the end goal of working with
coding agents. What I like about the
terminal is that it opens up a new
surface for coding agents to run. So
this can be in the CLI. It can also be
on the web or from your phone. It can be
from a bug report in Slack, which I use
all the time. It can be from a backlog
item in linear just automatically
triaged for you.
Because CLI based agents are scriptable,
you can use them in any type of
environment which is really helpful. We
use this internally to automatically
write docs or update parts of our
codebase. And it can be as simple as
just doing cursor-p and then a prompt
and having text or even structured
formats like JSON come back.
We also believe that you'll need more
specialized agents, which makes sense

[00:09]
when you see the keynote today. Last
year, we started experimenting with
using AI models to read and review code
instead of just writing and editing
code. And we made an internal tool
called Bugbot. It tried to help you find
meaningful logic bugs in your code. And
after using it internally for about 6
months, we found that it actually caught
a lot of bugs that we missed on code
reviews. So we decided to make it public
and funnily enough it actually caught a
bug which took down bugbot itself which
of course we accidentally ignored. So we
learned to then really pay attention to
those bugbot comments.
Newer models are also getting very good
at longer horizon tasks. So one way
we've pushed agents to run longer inside
of cursor is having them plan and do
more research upfront. This not only
gives you a chance to verify the
requirements of what you're trying to
build and course correct along the way,
but we've also seen it significantly
improves the quality of the code

[00:10]
generated, which makes sense, right?
You're giving the models much higher
quality input context. And to do this
well, it's more than a simple prompt
change like plan better, but you
actually need to have deeper product
integration in how you store the plans,
how you edit the files, and also giving
the model new tools.
It also makes sense to allow the agent
to create and manage a to-do list. This
gives the model the critical context so
they don't forget the task it's working
on or waste tokens. And it's like they
can have notes that they can constantly
reference. One area we're still
exploring is taking your to-dos and
making them have the same source of
truth, which is your codebase, which I
know is something that I would
personally use for smaller projects
where maybe I don't need a fully
featured task management tool.
Another important part of agent
extensibility is allowing you to package
up your workflows and then share them
with your team. So custom commands are a
way to share prompts and then rules

[00:11]
allow you to include important context
in every single agent conversation. One
way our engineers have found this really
helpful internally is packaging up our
commit standards and guidelines, putting
them in slashcomit and then being able
to pass in tickets like you pass in the
linear ticket that you're working on.
Another thing that I've noticed is that
a lot of the context engineering
breakthroughs actually happen in user
space first. So all of you the power
users figure out the workflows and the
patterns that actually work really well
and then as they get adopted they make
their way back into the core product as
features. So we see this with plans,
memories and rules are really all like
this.
Speaking of teams, you want to trust
these agents to write code for you. But
that requires keeping a human in the
loop. Which is why when the agent tries
to run shell commands, cursor will ask
you if you would like to run it just
once or if you're comfortable, you can
add it to the allow list to auto run in
the future. And all these settings can
be stored in code and explicitly shared

[00:12]
with your team, including blocking
certain shell commands or actions. Our
latest release also has custom hooks, so
you can tap into every part of the
agents run. Maybe you want to have a
shell script that runs when the agent
finishes, for example.
So, we've covered a lot of ground here.
Coding agents have evolved quite a bit
in the past year, and they're getting
better and better when you give them
very powerful tools. And as the models
have got more capable, we've actually
been able to remove overly pre precise
instructions from our system prompts
that just weren't necessary anymore. So,
what would it look like if we allowed
agents to run for significantly longer?
What is the right interface for managing
multiple coding agents?
If you're just getting started coding
with agents, I don't recommend
immediately trying to juggle multiple
agents. I mean, let's be honest, are we
really being productive running nine
CLIs in parallel?

[00:13]
Probably not.
Probably not yet, though. I mean, not
only do you need to set up your local
machine for running parallel agents, but
it's also kind of hard to review the
output of all of these agents. So, we
don't think that this form factor is the
end goal or the end state, but there is
promise here. One thing we've been dog
fooding over the past few months is a
new type of interface for managing
multiple coding agents. And we found
this really helpful internally when
maybe you have an agent in the
foreground, but you need to ask
questions about the codebase or maybe do
some research about tools you want to
integrate or small refactors. When you
have this fast coding model in the
foreground, you can really stay in the
flow and then you have your parallel
agents kind of run other tasks in the
background which could run for much
longer. Those could be in the foreground
on your machine. They can be in the
background on the cloud. Each one of
these decisions has unique constraints
that right now you have to think about
and spend a lot of time on. If you're in
the cloud, you get these sandbox virtual

[00:14]
machines, which are really nice for very
long horizon tasks, but the trade-off is
that it usually takes longer to boot up
and you have to set up some initial
configuration with the environment that
you're working in. But running agents
locally in parallel is kind of a
different type of isolation. If you have
multiple agents that are trying to
modify the same set of files on your
local machine, you need to have tools
like git work trees that allow you to
have different copies of your codebase
where you can run independently. And
then you also have to think about all
the other parts of local dev like
managing accessing your database and
viewing the work trees on different
ports today. And I I talked to some
developers early like a lot of this is
happening in userland and people are
writing scripts and hacks to make this
work really well. And what we're working
on and exploring is actually building
this natively into the cursor product.
Another idea that we've started to
explore for multiple agents is being
able to have the models compete against

[00:15]
each other. So what if you had GPT5 high
reasoning versus medium or low reasoning
and then you can pick the best result or
compare results across different model
providers with cursors agent. This will
soon be an option to go from one to n
for any given prompt and any models.
Part of context engineering for agents
is making it so they can check their own
work. So the agent needs to be able to
run the code, test it, and then verify
it's actually working correctly, which
is why we're exploring giving the agent
computer use. They can then control a
browser to view network requests or take
snapshots of the DOM and even give
feedback about the design of the page.
As you can tell, there's still a lot to
figure out on the right interface, the
right product experience for managing
multiple coding agents. Some of the
things I just showed are available in
cursor today in beta. So go try them out
if you're curious. And we'll have a
stable release later this month. But I

[00:16]
would love to hear your feedback on how
you want to work with coding agents in
the future. So come find me later and we
can talk about it. And speaking of the
future, I'd like to welcome Michael to
the stage to talk about where software
engineering is headed next.
Thanks, Lee. Our goal with cursor is to
automate coding. We think that half of
that is a model problem and an autonomy
problem. And we think that half of that
is a human computer interaction problem
of what the act of building software
looks like. We want engineers to be more
ambitious, more inventive, and more
fulfilled. And today I want to hint a
little bit at the picture of the future
that I think we can create together. one
where AI frees up more time to work on
the parts of building software that you
love.
Imagine waking up in the morning,
opening cursor, and seeing that all of
your tedious work has already been
handled. On call issues were fixed and

[00:17]
triaged overnight. Boiler plate you
never wanted to write was generated,
tested, and ready to merge. A world
where code review is actually fun, too.
Instead of being buried in your busy
work, your energy goes toward the things
that drew you to engineering in the
first place, solving hard problems,
designing beautiful systems, and
building things that matter.
Imagine agents that deeply understand
your codebase, your team style, and your
product sense. Agents that come back to
you after working for long, long, long
periods of time and show their work in
higher level programming languages.
Agents that propose ideas, help you
explore new directions, break down
complex projects into pieces you can
accept, reject, or refine. Ones that
extend your ambition, but never take
away your thinking and judgment. When
you have a problem too complex for
agents, they show you what they tried.
Pulling in runtime logs or debugging

[00:18]
tools. You'll never start from scratch.
This is the future we're working
towards. a world where building software
feels less like toil and much more like
play and where creativity is the focus.
Uh, and I think it's possible sooner
than even some of the most ambitious
people in this room think.
Uh, if this vision excites you, we'd
love to chat. And if you haven't tried
cursor, we've been shipping lots of
improvements to our agent and to our
editor. We'd love to hear what you
think. Thank you.
[Applause]

</details>


#### Live Demo Showcase: Tools That 10x Your Codebase

Live walkthrough of Codex-powered tooling that accelerates software delivery.

video](https://www.youtube.com/watch?v=-l0OqapibAA)[![OpenAI Codex in your code editor](https://cdn.openai.com/devhub/resources/video-1.png)

<!-- yt-inline:-l0OqapibAA -->
[![Live Demo Showcase: Tools That 10x Your Codebase](https://img.youtube.com/vi/-l0OqapibAA/hqdefault.jpg)](https://www.youtube.com/watch?v=-l0OqapibAA)

<details>
<summary>자막: Live Demo Showcase: Tools That 10x Your Codebase (30:05)</summary>

[00:00]
Earlier this year, a tweet went viral
with a new term, vibe coding. Now, it
got a lot of polarizing reactions, but I
think one thing we can all agree on is
it really changed the way we saw how AI
was going to transform software
engineering and how products are built.
But we're not here today to talk about
buzzwords or hype or what might be
possible. Today, we are here to show you
startups that our team has been working
closely with and we have seen firsthand
how their AI coding tools have helped
tiny teams 10x their code base and punch
way above their weight. My name is Sarah
Urbonus and I lead startup marketing
here at OpenAI. I'm thrilled to be
joined on stage here today by four
incredible founders who have built tools
to help you write, review, ship, and fix
code faster than ever before and without

[00:01]
any of the AI slop. So, please join me
in welcoming our first speaker, founder
and CEO of Warp, Zach Lloyd.
>> Let's go.
>> All right.
Hi, I'm Zach, the founder and CEO of
Warp. I'm very excited to be here today.
Now, you've probably seen a lot of
incredible demos today of uh what
development agents can do for creating
code, but the truth is if you're a
professional developer working on a big
codebase, it actually can be hard to
apply agents to build software. Now, at
Warp, our mission has always been
empowering developers to ship great
life-changing software, and we're trying
to use agents to do that now. So for my
demo today, uh I'm going to use warp to
build something within warp, which is a
million lines of Rust code, and try and
show you how I I approach development on
real production grade code bases using
agents.

[00:02]
So
this is warp. Uh I'm going to go ahead
and get started with a prompt here just
so I can get the agent working and then
I'll explain exactly what it is that I'm
building.
Please take a look at the two attached
screenshots. The first one shows the
state of the current branch and the
second one shows the desired state that
I'm trying to build towards. In the
desired state, the QR code is at the top
of the referrals page and there's a new
button called copy invite link that's on
the same row as the email form field.
Please help me build this. Oh, and by
the way, I'm doing this live at OpenAI
dev day and I need to do it within the
next four minutes and 30 seconds, so go
quickly. Also take a look at the
reference file to see where the code is.
So I just spoke to warp. Uh this is
often actually how I start today. Warp
transcribes it for me. I owe it a couple
references here. So let me go ahead and
refer to a file and let me attach some
screenshots.

[00:03]
Um
how do I do that with this setup? Well,
there we go. So I drag those in and then
I'm going to go ahead and start the
agent. And this agent is using GPT5
which is one of the main coding models
that we use in Warp and it's very good.
So while this is going, let me pop open
another tab here in Warp or another pane
I should say. And in Warp, our roots are
as a terminal. So you can use any
terminal pane as either a place to run
terminal commands or a place to launch
agents. I'm going to go ahead and use it
here. Actually, I'm going to run a
terminal command which is going to run a
local version of Warp. I'm just going to
show you what it is that I'm working on.
So, you can see here in Warp, we have a
referrals feature. This is something
that if you're a Warp user and you want
to get cool t-shirts or swag, and
there's a little Easter egg in here. Uh,
you can you can use this and we're
adding the ability to have a QR code for
people who are demoing Warp on video so
people can get their referral link. But
our designer, Peter, actually asked me

[00:04]
to do this in a different way. So, he he
wants the QR code to be at the top of
the page. And we don't want this link
form field. We want an email form field
with a copy invite link button here. So
this is what I've asked the agent to
change for me. So let's go back and
while the agent is working here actually
let me tell you just a little bit more
about what warp is in general.
So warp is what we call an agentic
development environment. And the idea
here is that it borrows some of the best
parts of the terminal and some of the
best parts of the IDE all with a vision
of like how do you have first class
support for building with agents. And so
one way of conceiving of this is warp is
just a general purpose interface for
telling your computer what to do. And if
you tell it that it will do it. It has
four parts. We have a coding agent which
is actually really good. It's a top
three agent on both suede bench and
terminal bench. We have facilities for
multitasking with agents which I kind of
just showed you. Uh we have a really

[00:05]
really nice just terminal interface. So
if you just want to run terminal
commands and then we have a knowledge
store where you can store workflows and
data for agents and humans on your team.
So let's go back to the demo and see
where we're at.
And it looks like we've uh made some
coding changes. So I'm going to go ahead
and run a terminal command here to start
um building these. Actually
type
Um,
okay. So, I'm going to go ahead and
build this. And then while this is
building, I want to show you how I use
warp to work on real code bases. And so,
one of the key things here that I do now
as a developer, if I'm coding by prompt,
is I like to look at um exactly what the
agent is doing as it does it. And so,
actually, it looks like we have a
compiler here. Let me see if the agent
can go ahead and generate this fix for
me. Try to fix it one more time. But the
idea is that I like to see what the
agent is doing and actually have a view
where I can code review it as it goes.

[00:06]
And so that's what you get on the right
side here. I could actually add comments
for the agent to make changes. I could
revert the agents change if I wanted.
And I could even edit it. And so we've
brought in some of the editing features
of the IDE to make this experience more
smooth. So we're building here. Let me
take a look at what it's done. If it did
the right thing, which is possible. Live
demos. There's always some risk here. Uh
we're still waiting for for Rust to
build, but yeah, this looks generally
right. Determine the referral URL for
the QR code. Okay. Um and so yeah, while
this is going, the other thing that we
focus on in Warp is how do you it's
really how do you have a very tight
iteration loop as the agent works to
make sure that what it builds can
actually go all the way from prompt to
production. So hoping we get there. So
we're about to build and run. Let's take
a look
at what we've got.
Just enter this in

[00:07]
and see. It actually made the change for
me, which is awesome. It's not quite
perfect. There's a little bit of a fade
on the link here, but it put the QR code
at the top. Anyhow, thank you very much
for the time here. This is how we use
Warp to changes. You can check it out at
warp.dev. And now I'm going to go ahead
and now that we've shown you how to
write code, you'll need to review it.
And for that, I'm going to welcome Harzo
Gil, founder and CEO of Code Rabbit.
>> Thank you.
>> All right. Thank you, Jack.
>> Yeah. So, as we saw in Zach's talk,
generative AI like is the most
compelling use case for that has been in
terms of largest use case in token usage
has been the code generation. We have
seen like anywhere from 30 to 40% code
and up to even 90% code in many startups
is now being written by agent ready AI
with all the way from like tab
completion to coding agents in the
terminal in the IDE and now even like
background agents but all that volume of

[00:08]
code being written in short period of
time is now leading to like second order
effects where we have seen code reviews
are now becoming like a new bottleneck
because the shipping velocity has not
really changed in all these
organizations right And the companies
that we talk to, we hear from many many
senior developers that now they are like
overwhelmed with a large number of
review pull requests that they have to
now review which are sitting in their
backlog. And it's gotten to a point that
it's becoming like really unsustainable
for humans to really keep up with the
agentic software development. And that's
exactly where code rabbit comes in. So,
Code Ravbit is the leading AI code
review solution which provides like a
critical trust layer that sits between
your agentic software development and
your production and it kind of provides
like a central quality gate through
which you uh each developer when they
open a pull request it has to go through
and it flags all kind of issues in these
pull requests all the way from security
issues to applying best practices and

[00:09]
even enforcing custom policies. So, Code
Rabbit is like pretty popular like it's
used by over like several hundred
thousand developers each day and we have
reviewed like millions of pull requests
in the last couple of years and found
like millions of issues in those pull
requests. So, today I'm going to like
show you like a few open source
repositories where we are being used.
So, code review has a pretty massive
footprint in the open source as well and
we'll like see some examples
uh showing code rabbit in action. So the
first pull request this is a very recent
pull request from a project called clerk
which is a authentication platform and a
user management platform for nextjs and
javascript applications.
So one things I want to point out is
that unlike a lot of the generative AI
products uh code rabbit is not primarily
a chatbased interface. It's a background
agent which has which pretty much kicks
off as soon as the developers open up a
request. So it's like a background agent
with like kind of a zero activation

[00:10]
energy like you don't have to remember
to use it and within a few clicks your
entire organization gets onboarded into
our system and in this pull request like
code rabbit basically creates a sandbox
environment in its cloud service clones
the entire repository and does like a
deep analysis on the code and once it
done I mean it takes like 5 to 10
minutes it's part of your CI/CD flow and
once it's done you kind of get to see a
few things one is like from the code
changes we are able to understand what
the payload was and so that we can show
like a walkthrough of the code changes.
So if you're a human reviewer coming
into a pull request, you get like a
starting point, a bearing into what
these changes are. Another nice thing we
do is like we actually create a sequence
diagram which I think a lot of our
customers and the users love this
feature where it kind of shows you the
new logical flow that has been
introduced by this pull request.
But the main value of code ra code
rabbit has been in the form of
review comments. So we provide

[00:11]
actionable inline review comments just
like a human would which flags potential
issues and even like providing refactor
suggestions and sorted by criticality.
So in this case we found an issue which
was later addressed by the developer in
some of in in the in the in the in the
iterative commit. And in this case what
you will see that we do a couple of
things like we also provide the
developers like a way to accept
one-click suggestion. So each time we
flag an issue we also generate like a
fix for that issue which you can just
click a button in GitHub and and and it
will commit it for you. And the other
cool thing we do which a lot of our
users love is this agent to agent
handoff. So we also like generate a
prompt that you can take back to your
coding agents like warp or cursor or
codeex to actually go and fix the
changes. So creating like a feedback
loop. So using agentic software
development then coding which is the
inner loop and then during the review
stage we find all the um issues which

[00:12]
you can go back and fix using generative
AI. So what makes code rabbit so great
and what it does is the context we bring
in. For example, if I show you under the
review details, you will see that like
we're bringing in lot of additional
context all the way from understanding
the code graph. Um, where we are able to
pull in definitions from other files.
For instance, in while reviewing
tanstack.ts, we are like pulling in
definitions from other files. And also
like we are providing the users to
provide their own custom instructions so
they can tailor the reviews for their
own organization. And these instructions
could be about best practices or how
they like want to code in certain styles
and so on.
But often like the context we bring in
up front in front of the agent is not
enough like the context windows are
still small and the production code
bases seemed like are pretty vast right
so that's where like we do other thing
which is like agentic ver verification
so we run like an agentic explorer which
kind of navigates the code like a human
does and then it flags issues even in
the parts of the codebase that have not

[00:13]
changed. So in my second example which
by the way is from the bun project. Bun
as you know is like a high performance
up andcoming JavaScript runtime. And
this particular PR has been opened by
Robo Bun which by the way is their
Asiantic um software developer like it
kind of opens end toend PRs. And in this
PR if I scroll down
one of the comments you will notice is
a comment that uses the verification
agent. So as you can see what codeabit
does in this case it basically generates
shell commands terminal commands to do
code review. Essentially we are doing
code generation to do code reviews. And
in this case the agent is going in and
running a grep. I don't know how many of
you are familiar with that but it's a
tool that allows you to pull in patterns
from the codebase based on abstract
syntax trees. So it actually wrote a
pattern search to read the function
definition because it was not in the
provided context. And it's also running
running some rip crap queries on its own

[00:14]
like it's also like finding some
keywords which it can go and search in
the entire code base or in other files.
Now what this agent verification does is
two things. First of all it helps code
rabbit suppress a lot of noise because a
lot of the comments we will generally
generate as a first pass are usually
surface level comments not with the
whole picture of the codebase. The
second thing it does is it finds issues
which are like ripple effects in the
entire codebase. Right? So that's been
one of the things and the third thing I
want to show is that it's Code Rabbit is
like a very collaborative kind of a peer
uh developer on the team. Um and in this
example again from the bun project you
would see that this is an open source
contributor who made a code change which
was flagged by code rabbit but because
code rabbit does not have a lot of the
tribal knowledge it's just making a
guess that based on PR intent the code
should look some should be slightly
different and in this case the developer
goes back and says even though the error
doesn't say so the the the comment is

[00:15]
incorrect like I mean so there is some
confusion here so what codeabit does is
it replies back to the developer but
also creates a learning and learnings
are more like long-term memory. So in a
way like when code rabbit is provided
any non-obvious knowledge or a tribal
knowledge it kind of remember the facts
in like a long-term memory which it uses
in the future reviews to make the future
reviews more tailored and more relevant
because it's a central product. So your
entire team can collaboratively like
provide learnings to code rabbit and
make it better over time.
And as you can see as a follow- on
message, the developer is now engaging
code rabbit and it's very contextual
chat to come up what with with the right
kind of error message um that should be
shown for the user and that's where LLMs
have been great with like they are they
understand the UX the LLMs have been
trained on best practices. So this
becomes like a really indispensable tool
uh to bring bring into your team. Now
with that I would also like to highlight
that code rabbit has been one of the
biggest users of reasoning models in the

[00:16]
world. Now code review is one of the use
cases where we need a lot more reasoning
than even code generation like maybe
planning is other use case where you
need heavy reasoning. Um but then the
other one is code reviews and I want to
like point out that GPT5 has been like a
big game changer for our use case. So we
have seen like almost a 70% jump in
improvement than the previous generation
of reasoning models or the models that
we were using prior to GPT5 which has
vastly made code rabbit much much better
in the last few months alone.
And with that I would love to now next
introduce Riley who's a founder of
Charlie Labs who will come and talk
about how to ship software in the era of
AI.
[Applause]
Hey, I'm Riley Thomas, the founder of
Charlie Labs. Uh, Charlie is a fully
autonomous TypeScript engineer that
helps team ship code faster.
He does everything you're familiar with
from CLI and IDE based agents like

[00:17]
writing code, answering questions,
generating plans, and reviewing code.
But what makes Charlie special is that
he collaborates with your team directly
in GitHub, Linear, and Slack. writes
slopfree Typescript code fully
autonomously and proactively finds and
fixes bugs and tech. Um, Charlie is a
full team member, not just a single
agent that runs in isolation on a
laptop. Let me show you what it looks
like to work with Charlie.
Okay. Um, so these are some linear
issues that Charlie proactively created
earlier today. Um, the bugs and tech
debt. Uh, Charlie looked through our
sentry and through the repo to find
these and created the issues here. Um,
let's get started and just assign these

[00:18]
to him.
Okay. Um, so now Charlie is going to
start working on these issues. Um, and
while he Oh, so he's already updating
the status here. This is one of the nice
things is Charlie is good at showing
what he's doing. Um, so we'll look at
one of these bugs here. Let's do this
one. Um, so this came from Sentry. As
you can tell, there's the trim stack
trace. Um, and then Charlie was able to
cross reference that with the source
code that he also has access to um, to
find the relevant code that caused this
um, and correctly identify the root
cause which is using JSON object without
actually including JSON in the prompt.
So this is a great great catch. Um, the
cool thing about this is it's then very
easy for Charlie to fix because he's
already effectively figured it out. Um,
and you can see here he's posted a
comment. He is already reviewing his

[00:19]
changes, it looks like. Um, and he'll
keep going with this.
We'll come back to these in a minute.
For now, we're going to look at how to
make features with Charlie. Um, so
Charlie makes a really good collaborator
in Slack because he has access to your
source code, GitHub, Linear, and then
the intelligence of GBT with web search.
um which makes him fantastic for
brainstorming, coming up with specs, all
of that. Um so in this case, I'll
quickly show you the demo app that we're
working on. The lack of dark mode is
pretty harsh on this screen. Um so we
can fix that. Uh
looks like Adam. So the other cool thing
is you can go multiple humans in Charlie
in one thread all across GitHub, Linear,
and Slack. So, we got a plan. Um, Adam
specified he wants uh the default system

[00:20]
colors or the system theme to be the
default colors. Um, and then I asked
Charlie to create an issue and assign it
to himself. Um, I don't know about you
guys, but I have never met a developer
that likes writing linear issues. Um,
this is such a great thing to just
brainstorm and then when you're done say
clean it up,
which we can look at.
So got pretty standard issue here. He's
actually put the right label on. Um and
then also the call out from Adam in the
thread for the default theme. And then
again, so this happened uh earlier today
and Charlie already has a PR for this
that we can look at.
Um, one of the nice things about
Charlie's PRs is that uh because he's
running in a VM, he can run all of your
tests and types and all of that. Um,
which means CI normally passes when he
opens PRs. And then for added

[00:21]
confidence, he'll also show you which
commands uh he ran to verify the work
before opening the PR.
Let's check and make sure it works.
Look at that. We got dark mode. And
that's system because it's dark. We can
go light back to dark. Um, he also does
a quick review of his own PRs. This is a
great way to catch more issues. As
you're all aware, different context
makes him better at catching things.
Like we run review within the agent
loop, but then starting it again without
the context from GitHub is another layer
of safety, which in this case, it looks
like he actually caught uh
our our custom instructions say to use
named exports. It's using a default
export. Um so we can actually get them
to fix that. But I'm also going to just
as a reminder for you guys, this is like
a toggle list here. We'll change that to
a dropdown. So then you can review

[00:22]
Charlie's PR's.
Um, you can comment whatever you want in
here, but we're just going to say,
uh,
address your own
feedback
and change to it.
We go request changes.
Um,
and then now couple minutes from now,
Charlie will have a PR that changes that
default export to a named export and uh
adds a drop down.
So, let's go back and see how the bugs
are doing.
Look at that. We have PRs for a large
number of these um fully autonomously.
And we can take a quick look and make
sure
that our CI is passing.
Yep. All green all the way across.

[00:23]
So, that's an overview of what you can
do with a fully autonomous parallelized
agents. Um, it's important to think the
alternative to this would be wrangling a
bunch of local agents, uh, creating
branches manually, PRs manually, and if
you want to get fancy and parallelize
it, you would have the pleasure of
working with git work trees.
Um, and now we've showed you how to
write, review, and ship code. Um,
sometimes things break. Next up is Danny
Grant, the founder of jam.dev, to talk
about fixing bugs in production.
>> Sounds great.
We started Jam thinking, how do we make
software a lot faster to develop and add
more fun to it?
Dare I say vibes.
If you're not one of the hundreds of

[00:24]
thousands of people using Jam for bug
reports, you should try it. It's
awesome. But today, I want to talk about
what's next for fixing software.
We started thinking, what if you don't
have to file a bug report? What if when
the designer, PM, founder sees something
in production that they want to fix,
what if they don't actually have to ask
anyone to fix it? What if they could
just fix it themselves?
We thought it would be amazing to turn
the browser into an editor so that when
you see something that could be a little
bit better, you can make it happen. You
can just edit your site right there,
right on the page, and let an AI handle
taking your edits and turning them into
a PR.
We call it Okay, well, we named it after
the two words you're never going to have
to hear again. I'm so excited to show
you please Fix.

[00:25]
I'm going to demo Please Fix on Jam's
own website so you can see just how easy
it is to edit a live site.
One of the most common edits people
always want to make is copy. So with
please fix, here's how you do it. While
you're looking at your own site, when
you see copy you want to change, you
just click on the please fix extension.
Then you select the copy you want to
change and you just change it right
there. And when you're happy with it,
you hit submit and please fix creates
the PR for you. You can also edit
designs. So like let's make the subtitle
a little nicer. Let's make it a little
bolder. and a little smaller. And we can
change the colors. All of these tokens
in the editor are pulled from your
codebase, your design system, so
everything stays consistent and really
clean. We have a powerful editor in
line, but you don't even have to use it
if you don't want to. You can just ask
please fix to make changes for you, like
make this QR code 30% bigger, and please

[00:26]
fix is going to make that change for
you.
Like any editor, you can select multiple
elements and edit them all together. So,
let's select a bunch of images and we
can edit them in the editor or we can
also ask please fix to do something with
them. Should we add a CSS animation?
Yeah, animate these image sections
so they scale
like from 50%
when they appear on scroll.
This is totally the type of stuff that a
designer really hopes an engineer will
be able to get to before a big launch,
right? The designer puts like 20 like
kind of requests into the engineer. they
get prioritized by the PM and the
engineer gets to let's say five. This
way actually you can move without
bottlenecks on specific people. You can
move at the speed of your entire
creative team. The developer doesn't

[00:27]
have disruptions. Rather they just get
to focus on the hardest problems
building new features while everyone
gets to contribute what they can. Let's
see the animation it made. I'm going to
scroll down. You ready?
Oh, it's nice.
Hey, you know what else would be really
cool? You know, sometimes you design
something in your Figma and then you
need to apply it to your live site.
Well, what if we could just tell Please
Fix to do that for us. So, we've
actually designed an FAQ section for
this site.
And
let's have Please fix it. I'm just going
to take a screenshot of it.
And I'm going to ask please fix
to add this FAQ section attached
like an email below this and we'll say
what below which section because I want
it right below the last section of the
site.

[00:28]
There's a whole lot of GPT5 GPT5 codecs
below the scenes here and a lot of
codecs to build this. They are super
powerful models. Thanks, OpenAI.
We actually tried to build this exact
product five years ago when we first
started the company. And because there
weren't LLMs yet, we couldn't. It wasn't
production ready. And so that's why I'm
so excited to be able to show you this
today and for this to be something that
you can really use. Cool. We've got an
FAQ section. I think it looks great.
Once you're done editing your site, you
just review the changes and you can
submit a PR. So, this takes a little
while. So, I have one ready for us to
look at.
This is what a PR looks like by Please
Fix. It's really short, sweet, easy to
skim, see it in a preview branch. Uh,
when you look at the code changes that
pulls from your design system and reuses

[00:29]
whatever you're using. So, in our case,
it detects that we're using Tailwinds
and it reuses our Tailwinds classes. I'm
so excited to see what you all are going
to build with this. Go to
jam.dev/pleasfix
to sign up and let's build a whole lot
more software together. This has been
fun. Thanks y'all.
[Applause]
Awesome. Thanks, Danny. Our team works
with incredible founders from all over
the world, but not many are crazy enough
to get up on stage and live demo at one
of the biggest developer events. So,
let's give them another round of
applause. Awesome job you all.
All of the founders will be outside if
you would like to meet them, learn more
about what they're building and how you
can use it at your own startups or
building your own applications. Thank
you all for joining our first ever live
demo showcase at Devday and hope you
have a great rest of your day. Thank
you.
[Applause]

</details>


#### OpenAI Codex in your code editor

Walkthrough of the Codex IDE extension for VS Code, Cursor, and other forks.

video](https://www.youtube.com/watch?v=sd21Igx4HtA)[![Shipping with Codex](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:sd21Igx4HtA -->
[![OpenAI Codex in your code editor](https://img.youtube.com/vi/sd21Igx4HtA/hqdefault.jpg)](https://www.youtube.com/watch?v=sd21Igx4HtA)

<details>
<summary>자막: OpenAI Codex in your code editor (7:00)</summary>

[00:00]
And we'll roll in those cameras.
>> Great. Thank you.
>> Yeah.
>> Hey everyone, I'm Roma. We've been
steadily improving Codex to make it feel
like a more capable and reliable coding
collaborator. And for us, it's very
important for Codex to be everywhere you
work. And that's why we launched an ID
extension. You can now have codeex right
in your code editor, whether it's like
VS Code, Cursor, Windsor, or many
others. And with me today, I have
Gabriel, engineering lead on the
extension to give us a quick tour. We on
the team have been working really hard
to bring lots of new things to Codex and
I can't wait to show you.
>> Amazing. Let's dive in.
>> So, I'm working on this OpenA FM project
and I noticed that it's using service
workers. There's this interesting return
clause. I'm going to go over to Codeex
and just ask it why. So, what is this
clause for? You'll notice that there's
an autoc context button that tells
codeex everything that I've recently
done in my IDE.
>> So what that means here is that
basically you're using GPD5 codeex the

[00:01]
new model we launched but you're kind of
like I'm guessing prompting it a little
differently when you're in the
>> ID. Exactly. Exactly. So in this case
I've just said what is this clause for?
And it said it short circuits the effect
when the browser doesn't support service
workers which makes sense. If it
determines that something is easy or a
simple chat prompt it'll usually respond
pretty quickly. Why don't you gonna
navigate the codebase a little bit and
um let's pick something to implement.
>> Great. This button component happens to
have a to-do to add a hover state.
>> Yep.
>> And if you have codeex installed, it
will give you an opportunity to
implement any to-do comments with
codeex. So if I click it, it's going to
kick off a local conversation and give
Codex all the context it needs to fix
this.
>> That's awesome. So anyone that has like
any to-dos or any task in their backlog
can just like start sending them over to
Codeex. Yeah, that's right.
>> Can you show us a little bit like what's
happening behind the scenes now?
>> So behind the scenes when you ask Codeex
to do something, it starts exploring
your codebase and running commands and
you can see its progression as it's
going along. First, it's reading code

[00:02]
and then when it decides to run
commands, it runs in a safe sandbox that
ensures that it's not going to modify
files outside of your project. And if
the model ever needs to do something
that it thinks it can't run successfully
in the sandbox, it can ask you for
permission. It explored the codebase. It
updated the button and then it made a
bunch of changes at the end. You can
then review the changes right in your
IDE to see all the changes it made in
one place. Y
>> but I think we should just go see if it
worked.
>> Let's do it. Moment of truth.
>> Hop over to the browser and I'm going to
hover over these buttons. And as you can
see, there's a nice subtle hover state
where it the shadow expands, the card
shifts up a little bit. I was looking
around the the site and I noticed that
there's a few other elements that also
don't have a hover state. So, what I'm
going to do now is I'm going to take
this conversation we just had and I'm
going to move it from local into the
cloud. And this is going to use codeex
in the cloud to continue this task
without taking over my computer.
>> I think it's like completely changing
the way we think about engineering,

[00:03]
right? Because you can start like a task
locally upload it to your teammate in
the cloud to just take care of it.
>> That's really magical.
>> Exactly. And so this is going in the
cloud. It's going to include the changes
we just had locally, but we can come
back to it later. So we can stash our
changes or even throw them away and
bring them back from the remote tasks
later if we want.
>> Amazing. So this was a very like simple
task that you showed us. I'd like to see
like Codeex take some like initiatives
in terms of the design direction or the
I don't know like features or layout of
the app.
>> So what I'm going to do now is I'm going
to change my IDE settings to run it in
the cloud.
>> Yep.
>> And this time this is going to be a new
task. I don't need it to use my local
changes or IDE context, but I'm going to
ask it to add a button to the header to
make a really interesting thing,
something fun. It's like not just like
dark mode, something more interesting
than that. And next to it, I can tell
Codeex how many times I want it to
attempt this task. So, you just gave
those instructions and Codeex Cloud is

[00:04]
going to work separately four different
times with maybe coming up with four
different opportunities to solve that
problem.
>> Exactly. Exactly. I mean, it's it's
pretty amazing to watch Codeex work.
Every single attempt is going to be a
little bit different. In fact, we we
even have Codeex currently working on
the hover states and the theme at the
same time. I could even have another
conversation going locally if I wanted.
>> I'm curious, by the way, in your own
personal experience, like how has that
changed your workflow?
>> It's a good question. Um, back when we
were launching Codex Web, it was like
1:30 in the morning and we were trying
to get this really fun Lahi animation to
animate whenever you submit a new
conversation in Codex. Um, and it worked
perfectly locally, but when we pushed it
into production, all of the Lah
animations except for this one wouldn't
work. So, we asked Codex to attempt it
four times. Three of them did not work,
but one of them figured out this very
obscure content security policy issue
that was preventing some inline
JavaScript that happens to be in that
one animation from working and it saved
that aspect of the launch.

[00:05]
>> That's incredible. So I guess for like
very nasty or complex like bugs or like
you know things that you're kind of like
struggling to find out, this is exactly
the kind of thing that Codex can take a
look at.
>> Exactly.
>> Like even like look at it from different
angles, try different perspectives.
>> Exactly. And I I'll use it for planning,
even planning or working on a
complicated refactor where I don't even
know exactly what I want, but I'll have
Codeex take multiple attempts. And
sometimes I'll take the best aspects of
each one. That's really cool. So, what's
going on now with those four tasks?
>> Okay, let's take a look at this. So, we
have attempt number one. I'm just going
to go ahead and apply it. See what
happens. And go over to the browser. And
you can see
>> Oh, wow.
>> Oh my gosh.
>> That's very, very good actually. Very
creative. Okay.
>> I've never seen that before. the same.
Let's see what else it did.
>> Let's Let's take a look at the next one.
>> So, I'm going to revert that one and
then I'm going to apply attempt number
two.
>> Oh, yeah. The entire theme has already
changed. Interesting. Okay.
>> Uh let's take a look at the next one.
>> Wa. That's pretty cool. I'm guessing
like conversely to what we did right

[00:06]
before, now you can take any of these
cloud tasks, check them out locally, and
keep working locally in your code
editor.
>> Exactly.
>> That's very magical. Gabriel, before we
wrap, like can you check on the status
of that task that you sent at the
beginning that you started locally and
then like offloaded to Codexcloud?
>> Looks like it's done. If I open up the
hover state task that we kicked off, I
can see now that it's modified a few
additional files. And if I apply the
changes locally and then go to the
browser, you'll see that it added hover
states for a couple new items. The start
building button now has a slight hover
state as well as the switch in the top
right corner.
>> Amazing. Thanks, Gabriel. Well, we hope
this gave you a quick tour of how you
can use codeex directly in your code
editor now with the extension. It's all
included in your Chad GPT subscription.
In order to download the extension, you
can go to opener.com/codex or simply
look for codeex in your extension
marketplace. With that, thank you and we
can't wait to see what you build.

</details>


#### Shipping with Codex

DevDay talk on building, testing, and delivering products with Codex.

video](https://www.youtube.com/watch?v=Gr41tYOzE20)[![Sora, ImageGen, and Codex: The Next Wave of Creative Production](https://cdn.openai.com/devhub/resources/video-3.png)

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


#### Sora, ImageGen, and Codex: The Next Wave of Creative Production

Panel discussion on combining Sora, ImageGen, and Codex for media creation.

video](https://www.youtube.com/watch?v=70ush8Vknx8)[![Using OpenAI Codex CLI with GPT-5-Codex](https://cdn.openai.com/devhub/resources/video-4.png)

<!-- yt-inline:70ush8Vknx8 -->
[![Sora, ImageGen, and Codex: The Next Wave of Creative Production](https://img.youtube.com/vi/70ush8Vknx8/hqdefault.jpg)](https://www.youtube.com/watch?v=70ush8Vknx8)

<details>
<summary>자막: Sora, ImageGen, and Codex: The Next Wave of Creative Production (22:35)</summary>

[00:00]
Great to have you here.
Hi everyone. I'm Chad Nelson. I'm a
creative director here at OpenAI.
Stop. Stop. Stop. We'll keep it casual,
but no, this is going to be a fun talk.
Uh so in my career I've made a lot of
content, films, video games, television
shows and in all my experiences there's
been one common kind of through line
which is how am I going to make it? How
am I going to make this stuff ultimately
like what are my creative workflows that
I need? What are the tools I'm going to
use? And so what happens you start a
project
and you basically look at the tool
landscape that's out there and you say
okay what are the tools I can use?
Hopefully, they're not too generalized
or or worse, too complicated for my
project's needs. And it also doesn't
help that in kind of the landscape
today, these AI tools, I mean, literally

[00:01]
new tools are coming out every single
month.
But kind of made us ask a question. What
if you could actually develop a tool
that was perfect for your individual
project, your creative workflow, and not
have it take months to develop? So
that's something we've been thinking
about here at OpenAI and we found a
project that actually helped us test
this theory. Now a few months ago or I
should say actually it was two weeks ago
uh Native Foreign and Vertigo Films out
of the UK announced a feature film
called Critters. It's an animated film
and their team in London they basically
wanted to power or partner their artists
if you will with our latest open AI
models. And what was interesting about
this, they came to us and said, 'Well,
we want everything to make sure that
it's humanled. Like, we want our artists
to be driving the AI tools itself and
not have them kind of work the other way
around, if you will. So, their goals
were simple.
Let's start with storyboarding. Now,

[00:02]
storyboarding is this pro process where
you sketch out each scene of the film to
ultimately visualize the entire movie.
And when we sat down with their team in
the beginning, they said, "Well, this
process can typically take about a
year." Uh and and the one of the issues
with that is it takes so long that you
really only have a few chances or
iterations to kind of get it right. And
so we thought about that and we said hm
that'd be interesting. What if we could
design a tool for this very specific to
storyboarding?
So we took chat GPT5 and codeex and we
said okay let's design a tool that was
very very focused on storyboarding which
would allow you go from sketches to
something that's more of a highfidelity
render and then potentially even to
final frame and we internally dubbed
this project storyboard and to
demonstrate how it works I'd like to
introduce to you my colleague Olivia
[Applause]
Hi everyone. My name is Olivia Morgan

[00:03]
and I'm a solutions engineer here at
OpenAI.
Now, I want to use Critters as kind of
the backdrop to show you this storyboard
application that we built. And what I
hope you all take away from this today
is not just that we're able to use
codecs to accelerate the build of a
truly custom tool, but that by
thoughtfully exposing the parameters in
our image APIs and our video APIs, um
you could really unlock a lot of
creative freedom.
So I'm going to show you a demo of
storyboard and I'm going to use the
persona of a storyboard artist, but you
can imagine any creative field, right?
somebody in design, somebody in
marketing trying to generate an initial
concept.
So when I land on the storyboard page,
you see this concept of projects. Now to
start a new project, I'm going to go to
the upper right hand corner and we'll
call this project today dev day. And for
the sake of the demo, I'm going to

[00:04]
duplicate from an existing project. Now,
all this is going to do is duplicate my
project setup. And I'll explain more
about the project setup in a little bit.
Uh but that's essentially what's given
me this population of characters,
locations, and props. But you can kind
of see the framework that we're starting
with. On the lefth hand side, we bring
in sk um some sketches and some prompts.
Then we have a list of controls. Um now
these are images that are fed into our
edit endpoint on GPT image one. Um and
helps us control uh the fidelity of
those final outputs.
Now you'll notice here that I can
generate in two different presets. So I
have kind of a turbo preset in the
project setup. We have this set to
generate in black and white sketches.
And then we have a high fidelity preset.
And so the this gives us really our
final renderings if you will. So let's
walk you through an example.
So in the upper leftand corner I'm going
to upload some frames and we'll go to

[00:05]
our swimming critter, our volcano
critter, and our waving critter.
And you'll see when those hit the
storyboard, they're here on the lefth
hand side. Now, I have this critter
swimming with a yellow fish here. And we
need to add a prompt to describe the
sketch. So, I'm going to jump into my
notepad. And I'm just going to grab some
of these prompts that I have.
And we'll describe this one as a white
furry critter swimming underwater as
she's surrounded by bubbles floating up
around her. A yellow and white fish with
scales approaches.
Now I want to select the controls,
right? I want that fidelity in my final
output of what I want my critter to look
like. So here I have a list of
characters. I'm going to select uh this
critter actually for our character. But
if I had a rendering where I wanted to
use Grandpa Critter, I could select him,
too. And then we move on to locations.
So this critter is underwater. Um and
this is just an an image we took with an
iPhone. So, we'll select that underwater

[00:06]
location, but we could also play with a
desert or a forest location or bring
more locations in in our project setup.
Um, then we have this concept of props.
So, if I wanted this critter to be
wearing sunglasses, I'll show you this
in a a later generation. We could bring
that in, too. Now, let's kick off these
generations,
and I'll move on to these last two
images. So, here we've got some critters
in front of a volcano. And I'll grab
that prompt
to describe this sketch. We've got two
furry critters looking at a distant
volcano uh on the other side of a lake.
There are berry bushes on the sides, and
this is going to be early morning light.
So, again, I'm going to use that initial
critter. For the location, I don't need
to bring in an asset. We described it in
our prompt, and we'll kick off those
generations as well. And then for this
last guy, I'm actually going to show you
an example of bringing in a prompt, a
prop.
And we'll describe this sketch as

[00:07]
a white furry critter waving hello
wearing sunglasses. So you'll see in the
image he's not, but we'll bring in that
prop for it. So here's our first
critter, and we'll bring in those props,
uh, those crystal sunglasses as a prop.
So this will be what he's wearing in the
final generation.
All right. Now, before we look at these
generations, I want to take you through
the project setup.
Um, so this is what was duplicated when
I initially spun up the project. And
when we were working with the creative
team in London, they mentioned that this
part of the image generation was really
important, the ability to set an overall
style in their storyboard. So, you'll
notice up here at the top, we have that
style guide where we can kind of set the
aesthetic description that's applied to
every generation. In our case, we want
the sketch uh to uh we want to turn the
sketch of a storyboard frame into a
detailed scene. And we want to maintain
the position and the composition of the
initial sketch.
Now, for the turbo generation prompt, uh
we just want a storyboard style black
and white marker and ink rendering, no

[00:08]
color. And then for that highfidelity
generation prompt, this is a full color
highly realistic movie scene, 35mm
photography.
Now, speaking of controls or assets, um,
down here at the bottom is where we can
manage our locations, our characters,
and our props.
Now, for each image that we bring in, we
can add a description. Um, for the
characters, we actually added the
ability for GPT5 to generate the
description for us. We were kind of
playing around with these controls. So,
I'll show you an example. We'll bring in
our yellow critter. And you'll notice uh
very quickly it's fed into GPT5 and we
get a short description, a small fluffy
bright yellow critter with a round
chubby body covered in software.
Now again, these are all fed into the
prompt for that final image generation.
So both the text and those images. Um
and this is important because that GPT
image one model that we have has a um

[00:09]
high input fidelity parameter that you
can turn on and you'll kind of see how
this comes to play here in a second.
Now, the last thing I want to touch on
is this history tab. Um, when working
with the creative team in London, they
mentioned that having this concept of a
history tab was important. They wanted
to be able to see the initial sketch,
the generated images, whether or not we
were referencing certain characters,
props or locations, and then which
prompt went with the image that was
generated. And we gave them on the
righthand corner the ability to export
this all in a CSV so that they have full
auditability on all of these storyboards
that they're creating.
Now, let's go back to the storyboard
frame and see what was generated. So,
you'll remember we had that initial
sketch of the the critter underwater.
And we've got our our black and white
frames now. Um, so we have four
different presets because when you're
working with these image models, you
know, there's a little bit of creative
freedom that is to be had with these
models. And so, it just gives the artist
the ability to choose the best rendering

[00:10]
that fits the vision. Um, I can confirm
for download here in the uh bottom right
hand corner. And um, I want to get some
participation from the audience. I'm
going to look at these last four and you
cheer for me which one you like the
best. Do we like this generation? We
like this generation or this generation.
>> First one. Okay.
Okay. So, we got our our confirmed
generations. I'll go through these last
two just very quickly. Um, we now have
also our critters in front of the
volcano. So, if I can get a shout out
which one we like best, I'll confirm
that one for download.
>> I heard two.
Um, and then here at the bottom, we've
got an example of those generations with
the glasses. So, we're still waiting for
the black and white sketch, but we got
the full color generations. I kind of
like either two or four, so we're going
to go with number two. But why this is
important is when you're working with uh
you know storyboarding or you're

[00:11]
generating initial sketches a lot of
times in production you're not just
working with one image you have hundreds
of images and so the ability to do this
in bulk stage it for download and then
move it into your other creative tools
is a really powerful concept.
And when we were working with the
creative uh team in London, what we
found really fascinating is that um they
started utilizing this storyboard
concept for many different aspects
including things like environmental
design. So you'll see here uh the sketch
of an initial environment and and
storyboard's final rendering of it. uh
but also things like character design
where we're throwing an initial sketch
of the character into storyboard and
we're using storyboard to render out all
of the final details. Um now this really
opened our eyes to what a tool like this
uh could be used for in uh you know
larger enterprise applications. So
imagine you are an athleisure brand and
you're preparing for a seasonal launch
or you're an automotive company and

[00:12]
you're building a new campaign.
Um and so that's really where storyboard
comes in. turns these initial concepts
into stunning production style shots so
you can move fast and kind of stay
confident that your first sketch to
final frame is exactly how you want it.
And with the new uh Sora 2 API, we are
really excited because what this means
now for our storyboard tool is we can go
from initial sketch to a beautiful image
now to full motion. Um, and I am so
excited for you all to get your hands on
this. I think what you'll find in Sora 2
is that the motion understanding, the
physics, the ability to guide the
details through prompts and images um is
is truly truly impressive. And so you
can actually then go from visuals or
images like this
to uh full motion and sound like this.
Hey there, shiny friend. You like to

[00:13]
dance, huh? You're beautiful.
[Applause]
So, that's a little teaser of our Sora 2
API. Um, I'm so excited for you all to
get your hands on it. I'm certainly
excited to continue to build this into
storyboard. Um, and speaking of
building, next I want to bring up my
colleague Allison to actually walk you
through how we built Storyboard. But
before I bring her up here, um, Chad,
are you still around?
Um, what? I'm sorry.
>> I wanted to bring you back up here. Um,
do you think you could sketch something
that we could actually throw into
storyboard so we can actually show them
how we've been working?
>> Uh, I think you might have given me a
challenge here. I need to get the iPad.
>> Okay.
>> Hold on a second. I'll be right back.
Okay.
>> But, uh, what do you want me to draw?
>> So, I'm thinking we have the swimming
critter. We got the volcanoes. What
about the cave scene? Could you do like
a critter in a cave?
>> I got it. Let me get the iPad. Oh, I
found it. Wow. Oh, look at that. Look at

[00:14]
that. Okay. Hopefully this cord's long
enough.
>> Um, how many have like like two, three,
cuz I'm not I'm just I'm a creative
director, not a storyboard artist, but
I'll I'll try.
>> We'll give you a you got a few minutes.
Um, so while he sketches, I want to
bring up my colleague Allison to walk
you through how we built storyboard.
[Applause]
>> Thanks, Olivia. Hi, everyone. I'm
Allison August, a solutions engineering
leader at OpenAI. Now, while Chad is
going to be furiously drawing over
there, I'm going to take a few minutes
to explain how we built Storyboard in 48
hours and how it's accelerated the
design process for Critters.
So, our team has worked with many
different creatives across the industry,
from some of the largest media companies
to small teams who really need to move
fast. And what we heard was clear. They
want more control over the creative
process with AI. Now, with a lot of

[00:15]
tools today, you send a text prompt for
an image and you get an output that can
vary actually quite far from what you
want.
But creatives have a vision of how a
shot should play out in their head. They
want to be able to visualize the scene
and the style to get an output that
matches their concept rather than go
straight to final generation. And in
fact, Chad, that's your drawing there on
the right, right? It's looking pretty
good. judgment free zone.
>> It looks great, Chad. Um, so with
Storyboard, our goal was really to
create a workflow that allows creatives
to follow a process that gives them this
level of control and fidelity to bring
their light their shots to life with AI.
So, at an internal company hackathon
back in August, I worked with Olivia and
three other solutions engineers to try
to solve this problem. We had crossed
paths with the critters team a few days
before and thought we could work with
them as a thought partner to ideulate
towards a solution during this hackathon
and we built a working prototype in just
two days.

[00:16]
So to build this MVP quickly we relied
on codec cli and cursor powered by GPT5.
We built the app in Nex.js JS with
superbase as the back end which manages
project state images and authentication
and everything is deployed on Verscell.
Now on Verscell we run functions that
coordinate GPT5 image gen and now the
new SOR 2 API and for every request we
generate four image variations with GPT
image one giving creatives the option to
select the image that most closely
matches their vision. Now, as Olivia
mentioned a little earlier, GPT5 is also
embedded throughout the application to
improve our generated results from
refining an artist sketch description to
automatically generating rich character
text that drives more detailed image
outputs.
So, let's take a peek at one of our
original concepts for Storyboard. So, we
started with an interface where you
could upload one sketch at a time, add a

[00:17]
prompt, and select a character, or in
this case, a very cute little critter.
It was pretty basic. There was no
project setup, no generation history,
and you couldn't even upload sketches in
bulk.
Now, as we worked, we realized that the
concept of a project where you can bulk
upload sketches from a scene and render
different types of outputs based on a
project level configuration would be so
much more helpful for creatives. So,
here's a mockup of what we actually sent
over to the Critters team and looks a
lot more similar to what you saw Olivia
demo a little bit earlier.
So when we sent this over, the Critters
team started testing the app immediately
and they had a lot of really valuable
feedback from basic asks like adding
file name visibility to more complex
requests like adding the options to
control inputs for props and locations.
Now, initially Olivia and I hadn't
planned to make any changes after our
hackathon, but when we saw the requests
and how valuable some of these changes
could be for the team, we decided to
test Codex, our coding agent, and the

[00:18]
newest GPT5 codeex model.
So, we would send tasks to Codeex in
between meetings. We really easily
reviewed and merged PRs into production,
which Codex even allowed us to do from
our phones. Right, Olivia?
>> Yep. Now, right now you're seeing a
screenshot of my actual codeex workspace
and some of the various tasks that we
shipped. We started with some quick wins
like adding small elements to the UI,
but soon found that it actually excelled
with more complex tasks like compiling
our generation prompt based on assets
uploaded at both the project and the
sketch level.
Now, in my experience, once we built the
foundation for the application and
designed what we thought about the base
UI, Codex was really incredible at
adding the additional features and
actually troubleshooting what we needed
in record time. And every day, we
completed nearly 10 feature requests
from the Critters team, and they were
simply blown away at how quickly we ship
those improvements.
All right, Chad, this is my last slide,
so I hope you're wrapping it up over
there.
>> I'm Yes, I think we'll be ready.

[00:19]
>> I'm sure it will be great.
So to summarize on my piece here, we
partnered really closely with the
Critters team and stayed in a tight
feedback loop, which meant that with
help from Codeex, we were able to
prototype faster than we ever have
before and incorporate feedback on a
daily basis. Typically, this kind of
loop can truly take anywhere from one to
two weeks. But with Codeex, we brought
our ideation time truly down to a day.
Now, the final storyboard tool helps the
Critters team visualize thousands of
sketches across different scenes in a
matter of days. A process that normally
would have taken months. All right,
Chad, pencil's down. Can we take a look
at what you drew?
>> Yeah. So, okay.
It's this little sketch here.
>> Beautiful.
>> Uh,
you said a ca entering a cave. I gave it
a little torch, like a little, you know,
it's a dark cave.
>> So, yeah. I I'm very curious to see what
it did with it.
>> All right, so I've got the generations.

[00:20]
They just came in just in time. Um,
we've got Chad's sketch. Uh, I gave it a
little description, the front view of a
furry critter who's entering a dark
cave. We selected, you know, our critter
character as that asset that we wanted
to feed into our prop uh into our
prompt. And then we've got our black and
white generations of the adventurous
critter and our final images here that
we can stage to move into.
>> I love the torch. The torch works really
well. This is amazing. I actually really
love the fact that I can just take a
sketch like in barely what two minutes
and get it um visualized this way. And I
think that's what's been so amazing
about seeing how their team in London is
working with the tools. Uh, now we
mentioned Sor 2 and I think we wanted to
show I mean obviously I love the fish
but I think Sor 2 made that audio. The
Critters team in London put together a
little demonstration. Now they've had
access to the tool about a I don't know
a few days u when we announced it last

[00:21]
week. So let's take a look at something
they put together to show us an example
of what it can do there. Give it a quick
comb. PERFECT.
>> PICTURES UP. CAMERA STAND BY and you
sorted. Good. Camera's rolling and ready
on the big land.
>> Have the antenna tidy. Thank you.
>> All right, EVERYONE. SET
>> ROLLING ACTION.
>> HI THERE. Uh um what's my line again?
Blast it.
>> I love it. I love it.
>> I think Sora too. I mean the visual
quality is amazing. I love the sound. I
mean all the voices and all the ambient
and the music. It's amazing. But I think
what's so exciting about this time is
that we're seeing this period where
artists and developers can now work more
closely than ever before. And we've seen
what happens when you take artists and
couple them with AI. I mean that
produces, you know, amazing work. But
now how they're producing that work can
be truly transformed with these custom
tools. So I think Critters has become an
ex exceptional example of this. Uh I

[00:22]
can't wait to see what they build next
with the tools. Uh but when I look out
in this room, I see a whole room full of
developers. I mean, what excites us is
what you all will build. What creative
tools might you bring to the industry
and to artists to let them explore their
imaginations? So, with that, I'll say on
behalf of uh Olivia and Allison uh and
myself, thank you so much for coming.
Have a wonderful dev day. Thanks again.
Thank you.

</details>


#### Using OpenAI Codex CLI with GPT-5-Codex

Overview of running the Codex CLI locally with GPT-5-Codex.

video](https://www.youtube.com/watch?v=iqNzfK4_meQ)[![4o image generation intro](https://cdn.openai.com/devhub/resources/video-1.png)

<!-- yt-inline:iqNzfK4_meQ -->
[![Using OpenAI Codex CLI with GPT-5-Codex](https://img.youtube.com/vi/iqNzfK4_meQ/hqdefault.jpg)](https://www.youtube.com/watch?v=iqNzfK4_meQ)

<details>
<summary>자막: Using OpenAI Codex CLI with GPT-5-Codex (5:42)</summary>

[00:00]
Hey, what are you working on?
>> I'm trying to find a good demo.
Something that Codex can modify. We
could make this little ball thing
multiplayer.
>> That sounds very cool. Let's do it.
>> Codeex CL164. Mark.
>> Hey everyone, Roma here. Recently, we
ship GP5 and GP5 codecs and we've also
released a ton of improvements to Codex
CLI to better harness the agentic coding
capabilities of these models. And today
I'm sitting with Eson who led a lot of
this effort on the CLI. Do you want to
give us a quick tour?
>> Yeah, I'd love to. Um, we have tons of
really cool updates. You can install it
really easily with either mpm or brew
and log in with your chat GPT account.
>> So here you're in your terminal and you
just have to launch it with by codex.
>> That's all there is to it. So we'll say
make a plan for making this game
multiplayer.
What's funny is like this game was one
of the very many examples we shipped
completely built by GPT5 in one prompt.
>> Yes.
>> Like and now we can start building up

[00:01]
upon it. So what it's thinking tell us a
little more like about what's happening
which model you're using here.
>> Yeah. So this is uh going to be GPT5
codeex which is our new model and it's
really good for any sort of coding task.
>> So here it's like currently crafting the
plan. I see it's laying out the steps of
what it's supposed to do. Yep.
>> Can you expand what's happening here?
Yeah, totally. So, we can go into
transcript mode with control T and that
gives you things that are super useful
like the uh the chain of thought, the
sort of the exact code that it's doing.
>> If you don't not interested into the the
whole details, you can just like let it
uh run at a very high level telling you
like what it's doing.
>> Yes, exactly.
>> Okay. So, while it's working on this
like kind of multiplayer feature, why
don't you kind of open up a second
codeex to give us maybe a quick tour of
some of your favorite commands?
>> Yeah, so I'm a huge fan of the model
switcher. You sometimes want to use one
model for one thing, one model for
another. This allows you to change the
reasoning level,
>> right? Because with the new GP5 codeex
model, the very simple task can go very

[00:02]
fast.
>> Yes.
>> But for the more advanced one, now Codex
can work on for like up to hours at a
time. Okay. So that's SL model. What
else?
>> Yeah. Uh approvals is really useful. So
this is where you kind of get into the
sandboxing features of codecs which are
very cool, very powerful. We have three
modes. We have read only, we have auto,
and we have full access. Auto is the
default. And that allows codeex to read
files and make changes to files within
the current directory. So by default, it
stays in the boundaries of your project.
It's not going to affect anything else
on your laptop.
>> Exactly. And then if you want to be in
readon, that's kind of useful for, for
example, running outside of a git
repository. Y or if you're like, I only
care about planning. I actually don't
want Codex get distracted by trying to
edit things. And then we have Codex
resume. And that allows you to pick up
from any previous session. Super nice.
>> Why don't you uh go check back on the
status of this multiplayer game?
>> Yeah, it looks like we've got a plan. So

[00:03]
why don't we tell Codeex to do that?
>> Great.
>> So one of the things that I think is
really interesting that people sort of
miss about Codeex is that it's useful
for these coding tasks, but you can also
deploy things with it. You can use it
for S sur type things. You can figure
out like, oh, we're seeing these, you
know, this bug show up for our users.
Why is this showing up? Go look at the
logs. Um, take these disparate data
sources, combine them. Um, it's
surprisingly very, very, very good at
that sort of thing. How are we doing on
the game?
>> Yeah, I think the game is probably good
to go.
>> So, it sounds like the the moment of
truth is to play the game, but maybe
before we need to deploy it.
>> Yeah. So what I'm going to say for this
app, let's maybe uh deploy it on Versal.
>> Yep.
>> And let's use code- search in order to
tell it to hey look up the latest versal
docs.
>> Yeah. In case like you want to deploy
something very specific and you need
persistence or maybe you want to look up
the latest changes of like an API.

[00:04]
>> Yeah, exactly. We should go to approval.
We should switch it to full access. And
then we'll tell it use the Versel
command line tool
to deploy this app.
>> Cool. Sounds like it's deployed.
>> Yeah, let's do it.
>> Should we try it?
>> Yeah, let's give it a shot.
>> So, I guess I can take over this laptop.
If you want to bring yours, I'm going to
have to ping you the link.
>> Yep.
>> There you go. You should have it.
>> Ready to start.
>> Let's go.
Oh my god, this is awesome.
We are really in sync.
>> Yeah, super in sync.
>> Incredible.
>> This is all real time.
>> Who's going to be the best at this? I
don't know.
>> You seem pretty good.
>> Ah, okay.
>> To wrap us up, what have we seen? So, we
saw Codex CLI logged into your chat GPD
subscription
>> starting to like change a game.
>> Yep.
>> Make a plan to implement like a full
multiplayer game.

[00:05]
>> Yep. We saw a quick tour of the
commands, but more interestingly, you
use web search to kind of like fetch
information from the internet. You
change approval modes. We deployed this
game and we're now able to to play it.
>> Yeah, it's super easy. This is the exact
same flow that I use to, you know, do
pretty serious stuff just across like a
wide variety of languages, a wide
variety of frameworks, wide variety of
projects. Amazing. Well, as you can
tell, we're shipping a ton of
improvements across all codec surfaces.
So you can have this AI teammate at your
disposal wherever you work and in this
case right in the terminal. And we can't
wait to see what you build with Codex
CLI. See you next time.

</details>


#### 4o image generation intro

Video introduction to 4o model image generation capabilities.

video](https://www.youtube.com/watch?v=2f3K43FHRKo)[![Balance accuracy, latency, and cost](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:2f3K43FHRKo -->
[![4o Image Generation in ChatGPT and Sora](https://img.youtube.com/vi/2f3K43FHRKo/hqdefault.jpg)](https://www.youtube.com/watch?v=2f3K43FHRKo)

<details>
<summary>자막: 4o Image Generation in ChatGPT and Sora (16:07)</summary>

[00:00]
Good morning everybody. Today we have
one of the most fun cool things we have
ever launched. People have been waiting
this waiting for this for a long time.
Uh we know we've made you wait but we
think it's really worth it and we think
you're going to love it. We are
launching native images in Chad GBT.
Image generation has been around for a
while. In fact, one of the first things
that we ever were known for was the
original dolly. But image generation has
been largely a novelty. uh you've been
able to make some cool art with it and
people have done amazing things but it
has not had the power to be really
useful in a wide variety of ways. The
thing that we're going to launch today
um is native image generation in our 40
model and it's such a huge step forward
that the best way to uh the best way to
explain it to you is just to show it
which we'll do very soon. Um but this is
this is really something that we have
been excited about bringing to the world
for a long time. We think that if we can
uh offer image generation like this,
creatives, educators, small business
owners, students, way more will be able
to use this and do all kinds of new

[00:01]
things with AI that they couldn't
before. And um really the best thing to
do is just to show it to you. So I'd
like to introduce Gabe who is the lead
researcher uh and really the primary
driver of this product. And we will I'll
hand it over. Hey, so I'm Gabe uh lead
researcher. Hey, I'm Proful. I'm the
head of multimodal research. So, okay,
I'm going to jump right in with uh with
a demo. And uh the reason I'm starting
off with a demo is because I'm also
using these demos as my speaker notes.
So, uh it's a bit handy. Now, um two
years ago when we first started this
project, uh we were interested in sort
of like uh maybe a scientific question
about what native support for image
generation would look like in a model as
powerful as GBD4. We didn't know the
answer to that question. But a year
later when the model was done training,
we saw really exciting signs of life.
So, you know, we featured this in a
forum blog post if some of you will
remember. And um, you know, we saw that

[00:02]
the model could render paragraphs of
text, for example, you could combine
images in really very interesting and
novel ways. And I think we spent a lot
of time just playing with this model and
I felt that sense of like joy and
excitement. You know, I haven't felt for
a very long time, maybe even since GPD2.
I haven't either. This was one of those
really wow moments. It was a wow moment,
but that model was still a bit rough
around the edges. So, you know, it's um
you know, it it it it you know,
sometimes made typos. It you know, it
was it it was kind of unreliable, I
would say. And um so over the last year,
I've been refining this model to make it
more accessible and more uh user
friendly to the average person. And so,
um okay, the image is generating as you
can see. And um
um let me see. So it seems to have
gotten all the text. I don't see any
typos, which is good. Okay, it's still
amazing to me to see uh and you know,

[00:03]
image generation with perfect text. It
shouldn't be that impressive, but
somehow we've been waiting for this for
so long, and every time it happens, it's
like, wow, that's so cool. Yeah. and and
the number of things that like this
image had to get right in the
instructions like the you know what you
want focused on not like the that it
should be a point of view image and
where we are and then sort of to get you
know having the text like like that's
just uh this is still amazing to me.
Yeah. And point of view images are
actually really hard to do and this kind
of looks like what we see right now. It
looks like you were just taking it.
Yeah. All right. Well, I am going to
begin my demo by taking a selfie of all
of us. So
give me a nice expression.
Yeah. Okay. And I'm going to ask chat
GPT to make it into an anime frame.
So in this case, it's not just getting
the context of my text prompt, but it's
also getting this image. And it can use
both of these to produce a really nice
image for us. And this is possible
because we train for as an omniodel. So
you know, it's a model of not just
language, but images, audio, all

[00:04]
modalities in and out. It understands
them. It can generate them and it can
you know seamlessly work across these
things and we have spent a lot of effort
to you know make useful products like
first advanced voice mode where audio
just works seamlessly and now this where
images just work seamlessly across the
board. It is so cool that we're finally
getting towards this truly integrated
multimodal model that just does
everything. Yeah. And in this case, you
know, it gives the user a lot more
control because, you know, I might want
a specific style or I might want to use
a specific previous image I have or, you
know, a design palette or something. And
they can provide all of this context to
chat GPT. You can just use all of this
and, you know, produce the thing you
want. It becomes more controllable. Oh,
okay. All right. We can, you know,
you're already seeing the sky behind us,
the plants. By the way, this goes live
today in Chachi PT and Sora. Um, I think
we're already started. So, if you also
want to make an anime version of
yourself, you can you can now do that.
Yeah, I think it's already out to all
pro and uh plus should be done pretty
soon. Amazing. Nice. It'll be available

[00:05]
to free users, too.
I I see I have my little beard there. I
see your expressions and my perfect the
hand sign. And my hand sign, too. Yeah.
Nice. What should we do next with this?
Can we make a meme out of it? Oo, make
it into a meme. That's on game speaker
notes. What do you want to um you know
one of the like common memes inside of
OpenAI is feel the AGI. I have no idea
what AI will think about that but let's
try it. I do feel the AGI.
Yeah. And in this case, right, that
animating is so good. Yeah. Um and in
this case, you know, the model is seeing
all of the past context as well. And you
know, it uses all of its knowledge of,
you know, language and beams and
everything to give us a new rendition.
And this multi-turn nature makes it even
more useful to people, right? Like I can
ask for any edit I want. If it gets it
wrong, I can just be like, "Hey, you
know, fix that thing." I think that, you
know, is taking us into a direction of
making these more like tools, not toys

[00:06]
for people. And I think I'm really
excited by that. Speaking of memes, how
much like how much do you think for
knows about like common internet memes
in general? Like if we had picked I I
think it knows a lot. And in fact, when
we first put this out to, you know,
people inside Open Air, most of what we
got was memes from people. Maybe Gabe
can tell you more about that. Yeah, I
mean you know uh memes were like one of
the number one use cases for this model
in our internal version and yeah I was
just thinking about you know memes and
why this use case you know kind of
struck a chord with the company and I
what I realized is that you know as in
the last nine months as I've been
working on this model uh I've been doing
this kind of like meditative exercise
where I sort of like uh look at all the
images around me and I realized I'm just
surrounded by you know hundreds of
images maybe a day and you know all
these images you know Not necessarily
the most aesthetic or beautiful images,
but they were all created with intent.
They were all, you know, like memes.
They were all created to, you know, to
persuade, to inform, to educate. These
are the workhorse images that, you know,

[00:07]
comprise our everyday life. And what I'm
very excited is that I'll be able to be
giving this power to create workhouse
images to everyone in the world in Chbt.
Speaking of this power, um we are giving
a much higher degree of creative
expression and creative freedom than we
normally do. Um and so what we'd like is
for the model to not be offensive if you
don't want it to be, but if you want it
to be within reason, really let people
create what they need and what they want
to what they want. And uh I, you know,
we may not get the line there perfectly
on day one, but we think given what Gabe
just said, we want to lean pretty far
into creative freedom and let people get
maximum utility out of this model. and
uh you know we're excited to see what
people will do with it. Yeah, me too.
Let's look at the meme we got.
That's great.
Um okay, so thank you guys very much and
we're going to welcome a few other
research and product people to show some
more stuff unless either of you have
anything else. No, thanks. Thank you.

[00:08]
Okay. So, in addition to building uh you
know all the great research that went
into this, we really wanted to work hard
to make it a great product experience as
well. Um and so if my colleagues want to
introduce themselves, maybe starting
with Alan, we will then show you a few
more things. Hi, I'm Alan and I'm a
research scientist at OpenAI. Hi, my
name is Bench. I'm an engineer on ch.
Hi, my name is Lou. I'm a research
scientist at OpenAI.
So, uh, as our models get more capable,
uh, their knowledge of the world is
deepening. Uh, but so far, they've
really only been able to express
themselves in either text or code. And I
think what's really exciting about this
release is that now these models can
actually visualize what they know and
externalize it in a visual way. So, the
prompt that I'm going to try is make a
collable page of manga describing the
theory of relativity. And just for fun,
we'll ask it to add some humor. How well
do you find that the model understands
like visual humor versus just funny
text? I think that given that this

[00:09]
prompt is like so vague, it'll be
interesting to see, you know, what kind
of wild cardy stuff uh the model comes
up with. Um this is really just like it
leveraging the world knowledge that it
has, writing maybe an extended version
of the prompt and then giving us a nice
image. uh but you know if you have a
much more detailed sense of the kind of
story that you want to convey in this
kind of thing like a manga or an image
or in general you can definitely do
that. This model is very good at
following instructions and in the blog
post that we just put out there's a lot
of nice examples of uh of how you can do
exactly that. Um by the way images are
much slower than previous uh our
previous image generation thing but like
unbelievably better. We think it's super
super worth the wait. Uh we also will be
able to make it faster over time. Um but
you know it's just it's like quite the
uh the ratio of quality to time we think
is is already great. Yeah. Um and it
looks like it's given us not only some
English but a different language here.
But yeah, I think in general um we're

[00:10]
hoping that this model's ability to not
only generate images but also blend in
precise text in the right ways uh makes
it not only a tool for imagination but
also for for learning and for
communication. It did add some humor.
Yeah. Yeah. I like the layout. Yeah,
definitely quite colorful on the
software. That's beautiful.
Thanks, Alan. So, Alan just showed us
how much this model can shine in
professional and educational
environments. But what I love the most
about this model is how accessible it is
to everyone. For someone like me who
don't have professional artistic skills,
but still enjoys expressing my
creativity. To show you what I meant,
I've prepared something special. Let's
kick it off. Um, so I was inspired by
this trading card in my hand that I got
from our Sora launch and I thought we it
will be really cool if we can design a
new one in the same style for photo
image generation. So I took a photo of
it in the morning. This is what it looks
like. But instead of having the giant
cat king here, I would like to have my

[00:11]
dog Sani to be the main character. And
this is a photo of my dog. He's cute.
Um, and I've also included a couple
details that I would like to see on the
card, including the name of the model,
the year, and some ability where like I
could highlight and also the weight and
height for Sanji. And let's see what the
model comes up with. Why is the giant
cat king Visora? I have no idea, but I
feel the the trading card Dora was
designed by some professional designer.
So, it would be amazing if we can
actually use our model to generate that.
Yeah, I think our model has come a long
way in terms of just very precise text
rendering. So, it'll be super cool to
see how well it does with this detailed
instruction. Can I see the original
card? Yes.
Oh, it's very nice.
It looks like it's already reviewed. We
should do these for every launch. These
are cool. Yeah.
I guess now we can make them with a

[00:12]
machine. Yeah, we should definitely do
that.
Yeah. And yeah, Sanji is snowboarding,
which is something I've never seen him
doing in real life, but it'll be cool.
The text is also very crisp. Yes. Yes.
And got it got all the stats correct.
That's amazing. Um, thank you for
letting me share this little creative
moment with you. And now I'm excited to
pass it on to Lou to show you more
innovative ways of using our product.
Yeah, sure. I'm very happy to share that
with everyone today. So, we've seen the
generation from Alan and Monta. So today
I'm going to do something very special
here. So I'm going to make a memorable
coin based on the generations from these
two and also another two pictures that
is in our background. So I'm going to
first copy the pictures from
Alan and also the pictures from
Mchao and the rest of the two are the
background we show here in the demo.
So I would like to also use a special

[00:13]
hex code here. So as you can see this
special hex code is a spring color
because for and this launch both
launched in spring. So I would like to
it to be a unique color for us and also
I would like to include the text for
image gen and today's date on this
memorial cone so we can make a souvenir
for us for today. So you can see this
model is trained in non auto reggressive
way. So it is able to understand both
text and multiple images in context and
seamlessly render it in a very
harmonious way in a coin. So it's able
to can you imagine how this coin will
look like based on this not easily from
that but I'm excited to see. Yeah. Yeah.
Me too. Me too. That's what I'm thinking
of also. So we are seeing here. So we
have the fur image gen and we have the
bear that is the artistic bear there.
the radio there and also Alan's
manga and I was still amazing Sanji.

[00:14]
That's so cool. Cool. That's very cool.
I want one of those. Yes, I agree. So
now I'm I'm going to make it a
transparency background because we
really wanted this coin to be printed
out so we can have this coin physically
for us. So as you can see the model not
only can understand context in one turn
it is also understanding the context
across multiple terms in context. So
from today we can just chat to chat GBT
in a more visual way and uh this is just
a very simple example. I make a
transparency background. You can also
talk to the model. For example, imagine
how will this coin look like on the back
side or we can make a unique color for
Alan and Munchchow and me to have a
different unique color for each one. And
other than making the background
transparent, how good will it be at
keeping the actual coin itself
consistent between the two? Yeah, it's
very good at keeping the editing

[00:15]
consistent. So that is also to see you
can use CHP from today to do image
editing and image refinement in Chad and
using a very chatty
language. Cool. Here so we see the coin
here and it's in transparent background
now and it's keeping the consistency
between the previous generation. That's
awesome. Yeah, it's very cool.
Well, we're so excited to get this out
to the world. Uh, it goes live today in
Chacht and Sora. It will come to the API
soon. We we really think this is a huge
step forward in what AI models are
capable of doing visually and we cannot
wait to see what you all will create.
Thank you very much. And again,
congrats. Cheers. Thank you. Thank you.
[Music]

</details>


#### Balance accuracy, latency, and cost

Talk on optimizing AI systems for accuracy, speed, and cost.

video](https://www.youtube.com/watch?v=Bx6sUDRMx-8)[![Build hour — agentic tool calling](https://cdn.openai.com/devhub/resources/video-3.png)

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


#### Build hour — agentic tool calling

Build hour giving an overview of agentic tool calling.

video](https://webinar.openai.com/on-demand/d1a99ac5-8de8-43c5-b209-21903d76b5b2)[![Build hour — built-in tools](https://cdn.openai.com/devhub/resources/video-4.png)

#### Build hour — built-in tools

Build hour giving an overview of built-in tools available in the Responses API.

video](https://webinar.openai.com/on-demand/c17a0484-d32c-4359-b5ee-d318dad51586)[![Codex intro](https://cdn.openai.com/devhub/resources/video-1.png)

#### Codex intro

Introductory video introducing Codex and its capabilities.

video](https://www.youtube.com/watch?v=hhdpnbfH6NU)[![DevDay — distillation breakout](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:hhdpnbfH6NU -->
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


#### DevDay — distillation breakout

DevDay session on model distillation techniques.

video](https://www.youtube.com/watch?v=CqWpJFK-hOo)[![DevDay — optimization breakout](https://cdn.openai.com/devhub/resources/video-3.png)

<!-- yt-inline:CqWpJFK-hOo -->
[![YouTube CqWpJFK-hOo](https://img.youtube.com/vi/CqWpJFK-hOo/hqdefault.jpg)](https://www.youtube.com/watch?v=CqWpJFK-hOo)

<details>
<summary>자막: YouTube CqWpJFK-hOo</summary>

_(자막 없음)_

</details>


#### DevDay — optimization breakout

DevDay session discussing optimization of models and prompts.

video](https://www.youtube.com/watch?v=Bx6sUDRMx-8)[![DevDay — realtime breakout](https://cdn.openai.com/devhub/resources/video-4.png)

#### DevDay — realtime breakout

DevDay session focused on realtime agent capabilities.

video](https://www.youtube.com/watch?v=mM8KhTxwPgs)[![DevDay — structured outputs breakout](https://cdn.openai.com/devhub/resources/video-1.png)

<!-- yt-inline:mM8KhTxwPgs -->
[![OpenAI DevDay 2024 | Multimodal apps with the Realtime API](https://img.youtube.com/vi/mM8KhTxwPgs/hqdefault.jpg)](https://www.youtube.com/watch?v=mM8KhTxwPgs)

<details>
<summary>자막: OpenAI DevDay 2024 | Multimodal apps with the Realtime API (29:45)</summary>

[00:00]
[Applause]
hi everyone and welcome to the realtime
API breakout session I'm Mark an
engineer on the API team working on the
realtime API and I'm Kata and I'm part
of the developer experience te a few
weeks ago we launched the public beta of
the real time
for the first time you can build apps
with natural low latency voice
interactions all with a single
API when we first launched our first API
in 2020 it was limited to text we then
made our apis multimodal supporting
audio transcription vision and text to
speech with the new real time API we've
taken the next step we've unified these
capabilities in a single API with a

[00:01]
model that natively understands
speech since we launched this a few
weeks ago we've seen developers building
some really impressive things in public
from avatars to Voice driven web
browsing even painting with your voice
we've also seen companies start using
real-time API to power voice experiences
in their own apps from language and
health coaching to voice controls in
your IDE and before we Shi the real time
a few weeks ago the only way to build
speech top speech experiences was to
stitch different models together and
build a complex solution around them so
it was really hard to create a smooth
natural conversation flow and unless
you're using the real-time API you
actually need to stitch different models
together and so you have to perform
multiple steps you need to connect these
systems and to go from input to final
output

[00:02]
there are different steps to take into
consideration so let me show you what I
mean first you actually have to capture
the user speech and so for this you
either need a button that they can press
to let you know that they're talking or
you need to detect that they're done
speaking yourself and after that you get
audio and you need to process that audio
with a transcription service like the
transcription API that uses our whisper
model then you get text out
and you need to process that text with a
language model like gbd4 for example to
generate a
response and then the last step is to
generate voice and so for this you need
a third model for example our text to
speech model to have speech as the final
output so if you've been following each
step in this flow depends on the output
of the previous one which makes the
overall process slow first of all but

[00:03]
also it can't react fast enough to allow
for natural
Interruption and along the way the
capture speech actually loses detail and
Nuance it's like you're telling the
model what something sounds like instead
of it actually hearing it for itself so
this makes it really hard to build fluid
conversational experiences that feel
natural so before the realtime API some
of GPD 4's capab abilities weren't
available in the API yet the most
exciting one is its ability to natively
understand and generate speech what this
means is that there's no need to convert
other modalities into text for the model
to understand it can actually process
audio inputs just as well as texts and
it can also generate speech directly
without having to generate the text
first right since in the interaction
doesn't need to be split into multi mple

[00:04]
steps it can happen in real time with
much less
latency in fact this is the same
underlying model capability that powers
advanced voice mode in chat gbt so let's
take a
look what are some fun things I can do
outside this weekend the weather looks
great that sounds like a perfect
opportunity to explore the Bay Area you
could take a hike in the Mirror Woods
enjoy a picnic at Chrissy field with a
view of the Golden Gate Bridge or take a
scenic drive down Highway 1 to explore
the coastline how does that sound for a
start that sounds awesome I really like
the idea of a Scenic Drive what route
should I
take for a Scenic Drive taking Highway 1
is a fantastic
choice yes chachi's advanced voice mode
is an amazing experience I hope you all
got a chance to try it it's now
available in all of Europe and now
what's even more exciting is that with

[00:05]
the realtime API you now have access to
the same capabilities but 3D API which
means you can actually build and use
this to have the same kind of
experiences but in your own
applications so as you heard a few weeks
ago we launched the realtime API into
beta and the realtime API is designed to
enable exactly these kinds of low
latency multimodal experiences in your
own applications
the Beta release is an important first
step towards supporting the full
spectrum of modalities in a single
surface so right now we support speech
text and function calling and we're
working to add more capabilities to this
API in the
future so just to walk through what
we'll be discussing in the rest of this
session first we're going to show you a
demo of what it was like to build this
these kinds of voice experiences before
the real-time API and after the real
time API then we'll get into some live

[00:06]
coding to show you how you can start
building with it
today and finally we'll show you a demo
of how you might integrate the real-time
API into your
apps so let's see how voice assistant
apps were made before the real-time API
on kya's laptop we've got a small
example here which was implemented by
combining a few different systems so
like we said you'll need speech
transcription a language model and
you'll need to generate speech so we can
use open AIS whisper dpt4 and text to
speech apis for these okay so I have
here on my laptop a voice assistant
buils the old way so as Mark said there
are three different steps and I'm going
to ask something and then we'll see the
different steps while they are happening
on the screen ready
okay okay quick how do I unsend an

[00:07]
email okay so it's generating a text
response now he generating dis
speech this is becoming
awkward if you need to unsend an email
the process can vary depending on the
email service you use to send it okay
thank you here are some common so I'm
going to stop it there because it's way
too late but you get the gist this works
but it was we're missing out on some
important stuff it responded too slowly
to be helpful so I uh hope that email
wasn't too spicy
Kaa so let's look at something similar
implemented with real-time API this time
okay so I have here an upgraded version
of this voice assistant and so now we
don't have separate steps it's all
happening at the same time time so let's

[00:08]
try it and see the
difference hey can you hear me loud and
clear what can I help you with today
okay so I'm here on St at Dev day with a
crowd of amazing Builders and I just
want you to say hello and tell them how
excited we
are hello devday Builders it's awesome
to connect with you all I'm thrilled to
be part of this event and can't wait to
see the incredible Innovations you all
created
let's make some magic happen today you
heard her um but I actually came from
Paris I took the Eurostar and I'm
already feeling a little homesick so
would you mind saying hello but in
French this time
not

[00:09]
excep great thank you and just for
comparison how do I unsend an email to
unsend an email it depends on the email
sour okay I'm actually using
Gmail in Gmail you can unsend an email
by using the undo send feature great
thank
you okay
[Applause]
wow so huge Improvement we're going
directly from speech in to speech out
using JD for's native speech
capabilities and what that means is that
we didn't have to wait and it's really
cool to hear how expressive the voice is
relative to plain
TTS in fact since we launched realtime
API a few weeks ago we've been working
on making the voices even more Dynamic
So today we're releasing five new
upgraded voices for you to use in your
apps as a quick comparison here's what

[00:10]
it sounded like when we launched
compared to a few of the voices that are
now available today the human voice is
the most beautiful instrument of all but
the most difficult to play said Richard
Strauss but according to Maya Angelou
it's not what you say it's how you say
it words have incredible power they can
make people's hearts sore or they can
make people's hearts sore Marty grth
once said and when King George V 6 spoke
to his country in real time he said I
send to every household of my peoples
both at home and overseas this message
spoken with the same depth of feeling
for each one of you as if I were able to
cross your threshold and speak to you
myself all right of course since the
model natively understands speech you
can tune the emotion and tone of these
voices to your needs using system
messages great should we dive into how

[00:11]
this works let's do it so the realtime
API exposes a new endpoint called V1
slre time and your apps make maintain a
websocket connection and exchange Json
formatted messages with the server these
messages can contain text audio and
function calls the websocket
transport allows us to keep a stateful
connection open which is the key to
liveness here so user input including
audio can be streamed to the realtime
API in real time and output from the
model will be streamed back as soon as
it's produced so now we'll walk through
some demos to better explain how this
works yeah let's actually build
something I think that's enough
introduction uh maybe we can start with
a simple example like the one we' just
seen Mark why don't you walk us through
how you would actually build this sounds
good

[00:12]
all
right
okay so we'll we'll start small and to
more easily introduce the concept here
we're going to build a front-end web
application that uses the browser
websockets API to connect directly to
realtime API so we have here a basic
HTML file and I'm going to include some
utils here that help us deal with the
audio AP in the browser and other than
that we just have a button right now and
we sort of set up some of our our
helpers here so if we go over to the web
page and we click Start you know of
course it doesn't do anything yet
because we haven't written any code so
let's do that
now so the first thing I'll do is I will
open up a connection to the realtime API
so I'm creating a new websocket and I
have the API URL here and I passed the

[00:13]
model along as well and you'll notice
that I'm passing my API key using this
custom header so uh this is isn't really
suitable for production app but it's
great for starting to locally experiment
with the API directly in the browser so
just keep that in mind as you start
building so now that we've created our
websocket connection we will now start
handling messages from uh the real time
API so what I've done is I've defined an
on message Handler and the messages that
we get back from the API are in Json so
we'll go ahead and parse the message as
Json and the messages have each have
their own type so in this case what we
care about is the response. audio. Delta
message so this message will be sent
back from the server whenever the mod
model uh is responding with audio so

[00:14]
we'll switch on the message type and
when we get the response. audio. Delta
message we'll go ahead and base 64
decode the audio and then we'll pipe
this audio into our wave stream player
utility class which will play the audio
out on the speakers and you'll notice
here that the audio we get back is pcm1
16 so this is 24 khz wave uh the API
also supports g711 so if you're
interested in how to use different
codecs encourage you to look at the docs
and check out how that
works so this takes care of
handling audio that comes back from the
model now let's deal with taking our own
speech and sending that off to the
realtime
API so what I've done is I've added an
onopen Handler for the websocket
connection and what we'll do is first
we'll start recording
uh using the microphone and our utility

[00:15]
class here is going to let us register a
call back so that whenever any speech
comes through the microphone we'll take
that speech and we'll package it up in a
message to the realtime API called input
audiob buffer. append we'll basic D4
encode it and we'll send it
off so since we've handled both the
model output coming back to us and our
own speech going out to the model this
should be enough to to start having a
conversation so we'll switch back over
and see how it
goes can you hear me yes I can hear you
perfectly fine how can I assist you
today well I'm just demoing you off to
an audience so can you say hello hello
there it's a pleasure to meet all of you
if there's anything you'd like to ask or
know I'm here to
help all right great so we have working
speech to speech application in just a
few lines of code but let's show off uh

[00:16]
a few more features of of the API so one
of the things that by default uh the
real-time API when you open up a new
session will automatically respond to us
when we finish talking but we haven't
yet handled interruptions quite yet
quite correctly so when the response
comes back from realtime API it actually
comes back faster than real time so the
API will just give us back the model
response as as fast as it can be
generated and we'll take that response
and we'll buffer it and play it locally
so if we want interruptions to feel
natural then what we need to do is when
the user starts speaking we need to stop
the out model output from playing on the
speakers so real time API will give us
sends us an event called uh that will
help us detect when speech has started
and we can use that to sort of do our

[00:17]
logic so let's do that
now so we're now handling a different
message type this message type is called
input audiobuffer dos speech started so
this is going to be sent to us whenever
uh the server detects that the user has
started speaking and when the user
starts speaking what we'll do is we'll
interrupt any of the model output audio
that we're currently playing and our
helper here is going to give us back
this off
so this offset is the duration of audio
that we've already played and what we'll
do with that is we'll send that back to
the
API and we do this so that we can let
the model know exactly where we
interrupted right because it's sending
us audio fased in real time we want to
let it know what was actually played at
the time when we started
speaking so we just need a little bit
more metadata uh to get this all wired
up and I'm going to add that now
so we just need this current item ID and

[00:18]
this context content index and that
should be all that we need to get
interruptions working the way that we
want so let's try that
out can you hear me yes I can hear you
how can I assist you today can you tell
me five interesting places to visit in
London absolutely London is full of
fascinating spots here are five
interesting places to check out the
British museum home to a vast collection
of art oh that sounds really interesting
where is that the British museum is
located in the bloomsberry area of
London on great Russell Street it's
easily accessible by public transport
with the Tottenham Court Road and hurn
Tube stations
nearby all right so you'll notice that I
was able to interrupt the model and ask
it where that was and it knew based on
where which how much audio was played

[00:19]
out uh what I was talking about so it
knew that I was asking about the British
museum so uh yes in this brief demo we
created a voice assistant from scratch
and we introduced the basics of handling
speech in interruptions in just a single
file and we did this using vanilla front
and JavaScript just to show the API in
its simplest form but of course we don't
build production apps this way so so
let's see how this new API uh will fit
into a real life use case Kaa will you
walk us through that yeah sure so I
actually have an example for this so I
want to build this tutoring app for
students to learn about space because I
think it's a fascinating field um so I
want users to be able to ask about
anything on space but I want to make it
fun you know like we could do a simple
chat interface but where's the fun in

[00:20]
that it's 2024 I think we could do
something a bit more immersive
so I went ahead and prepared this
application
here so it's going to show up on the
screen in a
minute and it's a 3D view of the solar
system so this is just the front end and
then on the back end I set up the real
time API like Mark just explained but
this time it's part of real application
so let's try it and see if it
works hey so can you tell me what is the
biggest planet in the solar
system absolutely the biggest planet in
our solar system is Jupiter it's so
massive it has more than twice the mass
of all the other planets combined
Jupiter is the giant among
giants okay great so the real- time
interaction works and I think it's
already a more fun way of learning but

[00:21]
let's see if we can make it a bit more
interactive hey I'm curious about
Earth sure thing Earth is the third
planet from the Sun and the only one
known to support life it's packed with
diverse ecosystems abundant water and a
protective atmosphere that Shields us
from harmful solar radiation do you want
to know more about Earth's
characteristics well I see that there's
actually a lot of water there so can you
tell me how much land is there versus
water absolutely approximately 71% of
Earth surface is covered by water while
the remaining 29% is land our Blue
Marble truly lives up to its name let me
show you this on a pie chart here's the
breakdown of Earth's surface okay great
thank you I actually have a question
about Mars
now Mars the red planet what would you
like to know
so I heard there was a lot of volcanoes

[00:22]
there can you tell me which one is the
biggest absolutely the biggest volcano
on Mars and in the entire solar system
is Olympus moans it's about 13.6 miles
nearly three times the height of Mount
Everest would you like more information
on Olympus Mons yeah can you tell me
like uh what are the three uh biggest
volcanoes and show me their
heights certainly the three three
biggest volcanoes on Mars are one
Olympus Ms 13.6 mil 22 km High two ascus
mes about 11.3 M 18.1 km High three
arams around 11.2 mil 18 km High okay
great thank you I just learned
something great so let's talk about what
happened here not only could I ask

[00:23]
questions and get answers in real time
but we also saw some interactions
happening on the screen so whenever I
asked about a specific planet we flew in
to see it up close and when I asked
questions that could be answered with
data we saw some charts pop up on the
screen so how is that possible well as
Mark mentioned the realtime API supports
tool calls so I actually went ahead and
defined some tools that the model can
use use so I have this Focus Planet tool
that is called whenever we talk about a
specific Planet it just takes the planet
name as a parameter and I also have this
display data tool here and the idea is
that when something can be answered with
data the model will choose with which
chart is the most appropriate what
should be the title and what are the
data points that should be displayed so
that's already a pretty cool use of tool
calls you can trigger interactions in
your app you can make interactive apps
so that's really cool but sometimes you

[00:24]
might also need to send data back to the
model so that it can say it out loud so
let's see how we can do that so I have
this API call here that calls this
endpoint that gets the current position
of the International Space Station in
real time so it gets back the latitude
and the longitude and I have this
function fetch Isis position that just
fetches to that end point get the
response back um and I also Define here
this tool show ISS and whenever this
tool is triggered by the model we will
call that fetch ISS position function
and then send the position back to the
model so let's try it and see it in
action hey can you go back to
Earth sure thing we're back to our home
planet Earth what would you like to
explore can you tell me where is the ISS
right
now the International Space Station ISS
is currently located over the southern

[00:25]
hemisphere around - 35.6 de latitude -
32.6 1° longitude it's always orbiting
around our beautiful planet what else
can I help you with great actually how
do you know the current
position I have access to realtime data
which allows me to track the current
position of the ISS in its orbit around
Earth this information is up dated
frequently to give an accurate location
of the station as it orbits our planet
approximately every 90 minutes great
it's pretty cool isn't it what else can
I assist you with yes it is pretty cool
um great so now you know how you can
actually feed data to the model in real
time so that it can use it in
conversations with your
users okay last
question hey can you show me Pluto

[00:26]
great I heard it's not even a
planet that's right Pluto was
reclassified as a dwarf planet in 2006
by the international astronomical Union
the reason it didn't meet all the
criteria for full Planet status mainly
because it hasn't cleared its orbit of
other debris nonetheless Pluto remains a
fascinating object with its own unique
character istics what else would you
like to learn and I heard it has moons
what are those
moons great thank
you okay so if we look at what the model
is doing right here it's calling this
show moons tool with Pluto's moons as an
argument and here it's a very small
array but if you have a big array as a
parameter or if you have a long list of
par parameters you can actually stream

[00:27]
that in real time while it's being
generated to show it or to uh let your
user know about it before the tool call
exended so that's like a very convenient
way to use this information in real time
okay so great with the real time API
we've actually built an immersive app
that you can interact with through voice
and that also reacts visually to what
you're asking
thanks to twool use so I hope this is
right
yeah so I hope this isar some ideas I'm
really excited to see what you come up
with and how you'll push the boundaries
to create new delightful experiences for
your
users so now that you've seen a couple
demos of realtime API I hope you can see
how it opens up new possibilities for
low latency speech to speech apps it's

[00:28]
this is a new way to leverage the native
multimodal capabilities of GPT 40 and
support for function calling makes it
possible to deeply integrate into your
apps and as you heard in the keynote as
of today we're also reducing the cost of
using the realtime API we're able to
offer this because we implemented prompt
caching for text and audio inputs what
this means is that for any text input
that hits the cache this input will cost
50% less just like with prompt caching
for text only input in chat
completions any audio input that hits
the cache will cost 80% less so for a
typical 15minute conversation we expect
that it will cost 30% less now than it
did at launch date so we know how much
cost matters whether you're building bu
something new or scaling it out and we

[00:29]
couldn't be more excited to offer this
and if you haven't seen it please check
out our docs and additional resources
that we published to get started
building we really excited about the
potential of realtime interactions we
see this as just the beginning of a new
generation of products that are built to
be natively multimodal and speech to
speech is just a first step but in the
future we're looking forward to
unlocking the native capabilities of our
Frontier models in this very API and we
can't wait to see what you build with it
thank you

</details>


#### DevDay — structured outputs breakout

Session covering structured outputs from DevDay.

video](https://www.youtube.com/watch?v=kE4BkATIl9c)[![Launch apps with evaluations](https://cdn.openai.com/devhub/resources/video-2.png)

<!-- yt-inline:kE4BkATIl9c -->
[![OpenAI DevDay 2024 | Structured outputs for reliable applications](https://img.youtube.com/vi/kE4BkATIl9c/hqdefault.jpg)](https://www.youtube.com/watch?v=kE4BkATIl9c)

<details>
<summary>자막: OpenAI DevDay 2024 | Structured outputs for reliable applications (40:39)</summary>

[00:00]
♪♪
[ Applause ]
-Hi there.
-Hello everyone.
We're here to talk about
structured outputs,
an exciting new future
we shared in OpenAI API
in August this year.
It's been a huge unlock for
developers, working with LLMs.
And in just a few short weeks,
hundreds of thousands
of developers
have integrated it
into their applications.
My name is Atty Eleti
and I lead API design at OpenAI.
-And I'm Michelle Pokrass
and I'm the Tech Lead here
for the API.
Today we're going to talk
about three things.
First, we're going to tell you
why you need structured outputs
and we'll talk about
how the feature works
and finally we'll tell you
how we built it under the hood.
So, let's get right into it.
-Let's start at the beginning.
The year is 2020 and OpenAI
has just launched GPT-3.

[00:01]
GPT-3 can write emails,
draft blog posts
and generate movie scripts.
It was great
for text generation.
Quickly, developers, all of you,
started to find
some exciting new applications
for this technology.
From generating
end game scripts like AI Dungeon
or drafting marketing materials
like copy.ai.
Fast forward three years,
in 2023, we launched GPT-4.
A new breakthrough
in LLM intelligence.
For the first time, models were
capably of advanced reasoning,
following complex instructions,
extracting information
from long documents
and taking action
on behalf of users.
Developers took it
to the next level,
from building AI powered
productivity tools like CURSOR.
Customer service agents
like Klarna and language
learning apps like Duolingo.
All of these products
had one thing in common,
they were connecting LLMs
to the outside world.

[00:02]
From your code base, to external
APIs or on device actions.
To do this,
they needed outputs to
be structured, typically JSON.
Here's an example,
let's say you're building
a personal assistant
and you want to convert the
users message into an API call.
The user might say,
play the Beatles.
Here's what you expect,
you want a JSON object,
that says play music for the API
and the Beatles for the artist.
But too often here's
what you get.
The middle begins
with a preamble saying, sure,
hers the JSON,
to call the play music API.
Now this isn't particularly
helpful for developers,
since we need just the JSON,
not the text surrounding it.
This is a problem.
LLM outputs are
not always reliable,
making it hard to integrate
them into your acts.
Now as developers
we're tried all kinds
of tricks to solve this.

[00:03]
Some of you may have
written prompts like this.
Or even this.
Now, sometimes it works
and sometimes you have to go
all the way
and write a custom
markdown parser.
That's obviously not
how it should work.
So, to solve this problem
in June last year,
we launched function calling.
It lead the way to define tools
the model can call
using JSON schema.
You define the schema
of the function
and the model outputs JSON
adhering to it.
Unfortunately function calling
wasn't perfect.
Sometimes the model
would output invalid JSON,
such as
by adding a trailing comma.
We've all done that before.
So in November at DevDay
last year we launched JSON mode.
JSON mode ensures
valid JSON outputs.
So you never see
another pressing error.
But this still wasn't enough.
The model could output
the wrong type,

[00:04]
like a string instead of
a float, as you see here.
Or hallucinate a parameter
entirely.
This cat and mouse
game to get reliable outputs
can be really frustrating.
Fundamentally, AI applications
need reliable outputs.
So, to solve these problems once
and for all,
we introduced structured outputs
to the API in August.
Here's Michelle
to tell you more.
-So structured outputs is
a new feature designed to ensure
that middle generated outputs
will exactly match
JSON schemas supplied by you,
developers.
You can think
of structured outputs
as the difference
between suggesting to the model
to use your schema
and to constraining.
You don't have to ask
nicely anymore
and you can just supply
the JSON schema that you need.
And you might be wondering,
if this is the right solution
that finally solves the problem,
why did it take us so long
to get here?
And the answer is twofold.

[00:05]
First, we still believe
that function calling
is often the right abstraction
for this functionality
and then finally,
it actually took us a
little while to build a solution
that is performant
for inference at scale,
while constraining your outputs.
So we're going to talk
a little bit more later
about the engineering
and research
we undertook to make this work,
but for now, let's talk about
how you can use it.
So structured outputs is
available
in two modes in the API.
The first is function calling,
as Atty just showed you.
And you're probably
already familiar with it.
This feature always our models
to generate parameters
for your tool calls
and it allows developers
to connect LLMs
with functionality
in their applications.
The second mode is
the response format parameter.
This parameter is useful when
the model is responding directly
to a user, rather than emitting
a function call.
So let's start
with function calling.
If you've use it before,
you're probably pretty familiar
with the format of a request

[00:06]
that you see here.
You can see we're supplying a
JSON schema in the tool section,
and there's parameters
for the function.
This tells the model how to call
our tool and in our case,
the function is called
get weather
and it has two parameters,
location and unit.
So location is a string type
and so is unit,
but it's actually limited
to just a few fields
with the enum parameter.
When you supply a function
like this in our API,
our systems will show the model,
this spec,
and it will use that information
to generate tool calls
when it's appropriate.
Enabling structured outputs here
is really easy.
With just one like of code
I can set strict to true,
and this will enable
structured outputs.
This will use
the supplied schema
and always make sure the model's
response will follow it.
So, that's structured outputs
in function calling.
Now let's look at a quick
example in the playground.

[00:07]
And before we get into it,
I'll tell you a little bit
about a startup I'm building.
So, I'm actually building
an AI glasses product.
They're pretty hot right now.
They're really futuristic
and they're built
on the Open AI API.
These glasses have
a speaker in the stem
to read the answers
out from the assistant
and there's actually a little
AR screen for the glasses.
I actually want to make
an internal admin dashboard
to help my team answer questions
about orders that we've received
and you know,
what their shipping status is.
So I actually already have a
database with order information
and I want to connect this
assistant to that information.
So, let's get started
in the playground.
So I've actually
already created a query function
to tell the assistant
how to query my SQL database.
Let's take a quick look.
So, here's my function,
it's called query.
And it has kind of the
properties that you'd except.

[00:08]
So the first is table name
and we only had one table name,
orders, that's all
we support so far.
Then we have all
of the columns of my table.
So these are just straight
from my database.
And then you know, the meat
of this is the conditions
that we support for querying.
So, you'll notice here
that we have some operators.
My database supports equals,
greater than,
less than, and nonequals.
And then we have like
an order by.
So just stuff
you'd expect for a database.
When I use the assistant
I'll set the system message
to tell it today's date,
so it can be useful
and then a user comes in
and they're asking
to find all of the orders
shipped September 1st or later.
So let's give this a quick go.
Alright, you can see
we've got a function call back
and it looks pretty good.
I mean, the logic is right.
We're checking that shipped at
is greater than
or equal to September 1st.
But the discerning developer
will notice
that this will likely cause
your application to blow up.

[00:09]
And the reason for that is that
we're using the greater than
or equal to operator.
However, our ORM for some reason
only supports these operators
and so the greater than
or equal to will just not work.
With structured outputs,
we can set strict to true
and this will constrain
the model to only use
what you've provided.
So let's save that and retry.
Awesome!
You can see this time
we've actually used the greater
than operator and the models
done in the logic to determine,
we actually need to check
that we're greater
than the last day of August,
and not greater than or equal
to the first day of September.
So through this you can see
how structured outputs will
just eliminate a whole class
of errors for your application.
Now, let's get back to
response formats.
So in the past when you wanted
the model to respond using JSON,
you would be using JSON mode.
So, back to my
AI glasses startup.

[00:10]
Since they've got a speaker
in the stem,
I want them to read some of
the assistants response out loud
and I want to show a summarized
version in the lenses.
Before structures outputs,
I would actually just put
these instructions
into the system message
and use JSON mode.
This is pretty nice,
I would always get back JSON.
But, sometimes if the user
asked for something specific,
I would get back an extra key
or the model will,
you know, use the wrong type.
With structured outputs,
I can move these instructions
into the response format
parameter,
like you see here.
I'm going to use
the description to explain
to the model how to respond,
with the voiceover and display
parameters.
So this way the model
will always follow the format
and use these two keys.
So, let's give this
a quick go as well.
Alright, I have another tab here
and I've actually created
that schema,
so let's take a quick look.
So voiceover is our
first string property

[00:11]
and we're telling the assistant,
this will be read aloud via TTS.
And to write
out numbers and acronyms fully.
Then we have the display
property and this is,
you know, we don't have a ton
of room on the glasses,
so we're going to keep
this tight, just five words.
So I'm going to put this
into the playground,
you can see on the right here we
have the response format option.
I'm going to paste in my schema
and you'll see
that strict is set to true,
so structured outputs is on.
Now I'm going to test out
the glasses with a,
you know, typical query.
I might ask something like,
how tall is a giraffe?
When I run this,
you see that I get the output
in the form I've asked for.
So we have
the voiceover parameter,
which has spelled
out the words to make it easier
for our TTS models
to read them out.
We also have the display field,
which is just four words,
which should fit right
on the glasses.
So there you have structured
outputs with response formats.
This is just a
really quick demo,
but Atty's get into something
a little more interesting.

[00:12]
-Okay.
So, that showed us the feature,
but let's get into
some more interesting demos
and how you might use structured
outputs in your applications.
Let's imagine we're building
a fictitious company
called Convex.
Convex is an AI powered
recruiting tool.
It lets recruiters create
job postings,
submit referrals
and schedule interviews.
Behind the scenes,
Convex is a node and react app,
that uses response formats to
extract information from resumes
and uses function calling
to perform queries
over the candidate data.
Let's see it in action.
So, I've gone ahead
and created a job posting
here for an ML Engineer role
that we're hiring at Open AI.
And you can see
the job description,
the hiring manager
and someone of the candidates
that have already applied.
Now before I came on stage,
a promising candidate reached
out to me and shared his rSum.
Let's take a look.

[00:13]
Okay, Greg seems
to have a good Stripe
and has a little bit
over experience working in AI.
He has a whole bunch of skills
including coding and Python,
so seems like
a promising candidate.
Let's put it in a folder.
So, I'm going to go click in
the add candidate button here.
And select Greg's rSum
and you can see
that we're outputting the fields
from the rSum in real time.
The model is use
structured outputs
to extract this information from
the text that's within the PDF.
Let's take a look at the models
response behind the scenes.
So we see a JSON object,
with name, title, location,
contact information,
work experience,
all of this has been
extract from the rSum.
Now, let's take a look at the
code to see how this all works.
So, behind the scenes
we're using the response
format called, resume.

[00:14]
It has the fields we just saw,
like name, title,
location and so on.
And particular
for work experience,
you'll notice
that I'm using an array.
So, structured outputs supposed
to say wise subset
of JSON schema,
including arrays.
That allows the model to output
more than one work experience.
Now, some
of the JavaScript developers
in the room might also notice
that I'm using the library Zod,
to define my schema.
Zod is great.
It lets me define my schemas
in code
and get run time type safety.
The Open AI node SDK has
native support for Zod.
You can define your schemas
in it
and when the model starts
responding,
we parse the response back
into the Zod object as well,
and it supports streaming.
Very similarly the OpenAI Python
SDK supports Pydantic natively.
Okay, so let's add one
more field to the format here.
Let's add the GitHub user name.
So I'm going to go save that,

[00:15]
refresh my page, and
let's add it for one more time.
Great, the models responding
and you can see
that the GitHub user name
was also extracted.
Okay, so that was the
first feature I wanted to demo,
which is extracting information
from unstructured data
using response formats.
Next, let's see how
we can use structured outputs
in function calling.
So I'm going to go
click view all here
to open my candidate
analysis screen
and I have a helpful
AI assistant here
that I can ask questions
to analyze my data.
Now we'll see
that candidates have applied
from all over the country
in San Francisco and
New York and Austin,
but for this role
we're hiring in the SF office,
so let's filter
the candidates down.
I'm going to say filter
the candidates to those based
in San Francisco,
let's press enter.
And we see that the model called
the find candidates function,

[00:16]
with a criteria field.
The field is location
and the value is San Francisco.
And this hit our back in API
and it returned a list
of candidates that were filtered
and are based in SF.
We also noticed
that the UI on the left
has been updated
to reflect these candidates.
In this way
you can use function calling
to control the UI
of your application.
Let's look at this
behind the scenes.
So in our code
I've defined a tool
or a function called,
find candidates.
Find candidates has a schema
that includes a list of criteria
and each criteria has a field,
so that can be title,
location and so on and a value,
which is the value to filter on.
So that was a quick one
on one example
of using structured outputs
with function calling.
Let's try something harder.
Let's say graph these candidates
by years of experience.

[00:17]
You'll notice
that the model is generating UI,
a card with a header
and a bar graph
that shows all the candidates
and their years of experience,
a table with the rows as well.
Now this is not a prebuilt UI.
This is actually
the model composing a set
of react components dynamically.
We can look at the schema here
as well.
We see that the
top level properties component
and it says card and card
has a list of children,
that includes a header,
a bar chart and so on.
Here's how the schema
is defined behind the scenes.
We have a tool called
generate UI.
And generate UI has
one property called, component.
Component is an any of --
of card, header,
bar chart and so on.
And each of these schemas
is defined later on
in the defs parameter.
Now this is a really interesting
feature of structured outputs,
where you can actually use
defs to define your schemas
in one place
and use them multiple times
and you can use recursive
schema definitions as well.

[00:18]
So you'll notice that the card
schema here has a children,
which then references
component again.
So in this way a component
can have a list of children
that are components
and structured outputs
handles this
with no problem at all.
Great, so now that we have
candidates sorted
by years of experience,
let's go ahead
and schedule some interviews.
So I'm going to say,
schedule interviews
for the candidates with,
let's say for the top
three candidates,
by years of experience
with Michelle and Olivier.
So what this is going to do
is first go
and check the availability
of Michelle and Olivier
on their calendars.
Once it picks out
a few good slots
it's going to schedule
those interviews
and finally it's
going to email the candidates
that their interviews
have been booked.
So let's press enter. Awesome.
So we see
that the models calling
the fetch availability API
and got some data back,
it's now calling
the scheduled interviews API

[00:19]
and that succeeded.
And finally it's called
send emails,
with custom emails
for each candidate
and that succeeded as well.
So that's an example
of a multistep workflow,
using function calling.
Where each step benefits
from structured outputs.
Before this feature,
if any one of these steps
failed,
the whole workflow would fail.
And in production,
if one of these
had let's say a 1% error rate,
the workflow would have
an approximately 3% error rate.
You can see how important
structured outputs is
for reliability
of agentic workflows.
Okay, so that's a little demo of
how you can use
structured outputs
and real world applications.
You can use response formats
to extract information
from unstructured data.
You can use function calling
to generate UI.
And finally,
you can build agentic workflows
with 100% reliability.
To tell you about
how all of this
works under the hood,
here's Michelle.
[ Applause ]
-Thanks, Atty.
Super cool, and can't wait
to interview Greg later.

[00:20]
Let's get into how structured
outputs works under the hood.
We're going to talk
about three things.
We're going to talk about
the engineering implementation,
the research we undertook to
make our models better at format
following, and then finally some
of the interesting API
design decisions
we made to ship this feature.
To ship this,
we actually decided to take
an approach that combined
both research and engineering,
to create a holistic solution.
Doing just one of these would
make a pretty good product,
but together they are greater
than the sum of their parts.
There's actually more
to structured outputs
than just prompting
our models differently.
It creates some interesting
tradeoffs for developers,
so we thought it would be useful
to take you under the hood,
under those choices.
On the engineering side,
we decided to take an approach
known as constrained decoding,
to ensure that our models
would also follow schemas
supplied by developers.
And there's three components
of constrained decoding

[00:21]
that we're about to talk about.
The first is LLM inference,
how that works.
Then we're going to get into
token masking
and finally, we're going to talk
about the subset of JSON schema
that we support,
all of those grammars.
So let's start
with LLM inference.
LLMs operate on tokens,
which is the vocabulary
of a large language model.
This is all of the labels that
the model can output or produce.
So, let's get into
a simple example of a model
to show a small vocabulary.
This is the classic example
of an AI model.
So it's a digit recognition
model.
I want to train a model to
recognize this handwritten three
and determine what digit it is.
So the vocab of this model
is just going to be 10 labels,
the digits zero through nine.
And this is actually what a
model like that would look like.
So first we convert
our input into some sort of
computer representation
and in this case,
we're going to take every pixel
from my handwritten three
and feed that into the model.

[00:22]
Then we have the inner layers
of the model,
and then finally at the end,
the model is producing 10 values
and these are the predictions
of our labels from zero to nine.
You can actually see here
that the digit three
has a 97% probability, so
this digit is probably a three.
This is also how large language
models work for inference
in pretty broad strokes.
Rather than predicting
the digits zero through nine,
large language models predict,
you know, language.
In order to do this
they use labels
that represent language,
and one of the best ways
we found for doing this
is to use tokens.
Tokens are like words or word
fragments.
And here we have some English
text broken up into its tokens.
This is actually the text
from our blog post
and you can see
that the taken boundaries vary.
Sometimes they're an entire word
like the word "the"
or sometimes they're
a word fragment like "struct."

[00:23]
These tokens make up
the vocabulary
of large language models
and at any point the model
can product any of these,
they're all valid.
So this is
unconstrained decoding,
where there's no constraints
on what can be produced.
What you see on the screen
are actually some
of the real tokens
in the GPT-4 tokenizer.
So, there's all kinds
of parts of speech,
like individual characters,
so the exclamation point,
to full words like
"conveyer" at the bottom here.
Now let's say we're using
structured outputs
to generate an output
with this schema.
So, this schema has
a single property, value,
and that's a number type.
And we're part way
through our generation already,
so we've produced a curly brace,
some white space,
and then value.
By default,
when we sample, any token
from the vocab can be chosen.
So that can be a string
or a Boolean.
But if we did produce a Boolean
that would not match the schema,

[00:24]
so and a number like 42
would be valid.
So this tells us
that we actually need to limit
which tokens can
be produced next
and we can't just have
the entire vocab of the model.
To do this we will use a
technique known as token masking
and this constrains the tokens,
which can be picked
at the very end of sampling.
So, back to our digit example.
Here's an example
of taken masking,
let's say I have some side info
about these numbers.
I know that they're
all prime for some reason
and so I wouldn't
want to decode, you know, zero,
one, four, six,
any of the non-prime numbers.
So this is actually
what I would do.
I would kind of mask out
any of those predictions.
So what we do after
we generate their probabilities
with a for pass,
is then remove any labels
that are not supplied,
so that we will only sample
from a valid token.
This is known as masking
and we're effectively
ignoring any values

[00:25]
that we don't want to
be produced.
Large language models are
autoregressive
and that means they produce
output one token at a time.
Each time we sample a token,
that output is fed back in right
as input,
for the next inference step.
This means when sampling JSON
for your schemas,
we actually need to update
the masked tokens
at every step of inference
and we can't just do it once
at the beginning of the request.
And if that's not making sense,
look at this example.
So you can see, first, we're
allowing the curly brace token
and then once we sample it,
in step two,
you actually no longer see
the curly brace in the mask.
So you can see
that from step to step
we need to update these masks.
Because this is happening
at every inference step,
we need this operation
to be super, super fast.
At the scale that some
of your apps run,
you know, we need to make
things lightning fast
and keep inferences as fast
as possible.

[00:26]
So, you probably
already know this,
but token sampling happens
on a GPU.
And we actually do it
one batch at a time.
For each batch,
we calculate probabilities
for everything in that batch
and then we'll apply
any token masks
and then we'll sample from that
final probability distribution.
And that sampling is right here
in the orange segments.
So as you can see here,
we can actually calculate
the probabilities
and determine the masks
in parallel
and this frees up
precious GPU resources,
because we can do
the mask determination on CPU.
This is very helpful
for us to keep things fast.
You'll also notice
that we need the mask to happen
at about the same amount of time
as calculating
the probabilities.
And this is also known
as the time between tokens
and it varies based
on the size of the model.
And so we need to keep this
under even something
like 10 milliseconds.
So a naive solution
to this problem
would involve determining
these valid tokens

[00:27]
from the current state,
at every step of inference.
But like we said,
we have 10 milliseconds
so we're not super likely
to meet that budget.
So we want it to pre-compute
as much work as possible
and then reuse it when sampling
to make mass computation
more like a lookup
and less like a lot of work.
And just like you can build
an index in your SQL database
to speed up queries,
we can actually
build up an index
with the specific JSON schema
that you supply
to make fetching these masks
very fast during inference.
There's actually a lot of work
that goes into producing
this index from the JSON schema.
First, we convert
the JSON schema into a grammar.
And a grammar is actually
a formal specification
of a language.
Once we have the grammar,
we can create a parser.
And a parser is a program
that can check strings
and see if they're part
of this language.
You can think of the parser
as a program

[00:28]
that takes in a JSON blob
and tells you,
does that match the schema
or not?
Finally, once we have a parser,
we can iterate over all
of the tokens in our vocabulary
and all of the states
that are possible in the parser,
and this will determine
which tokens are valid.
This work lets us build
an index.
Our index is actually a tree,
which is a prefixed base
data structure
that allows for
O(1) lookups.
So, during inference
we're running our parser,
building up some states
and then every time
we'll traverse this tree
to find the leaf.
The leaf node will tell us what
the mask is for the next step.
Generating this index is pretty
computationally expensive.
We have to go over all
of the possible states.
So we do it just once
and then we cache it
later for fast look ups.
This is why the first query
to structured outputs
can take a little time,
usually under 10 seconds.

[00:29]
And then the following
queries are just as fast
as you normally expect.
Finally, let's talk about
the kinds of grammars
we support with
structured outputs.
A common approach
in the open source community
is using regular expressions
for determining token masks.
And this approach works
quite well for simple
or depth limited schemas.
So, for example, you
can imagine a regular expression
for our value schema
from before.
It's actually a
pretty tractable implement
with a regular expression,
which we have here.
And this regular expression has
about what you'd expect.
First we have the curly brace
and then we have
some white space, then value
and then finally a regular
expression for number types.
However you actually
can't implement all
of the expressiveness with JSON
schema with regular expressions.
They're missing basically
the memory needed to store
information about pass lookups.
So let's talk about
why that's important.

[00:30]
Here's an example of a recursive
schema from our blog post.
So this schema is useful
for generative UI
and it's kind of like what Atty
showed you just now as well.
Each component can have
a list of children
and those must also
themselves match the schema
at the top level.
So you can see the schema here
uses the ref paren
to reference the parent.
And there's actually no way
to implement a regular
expression to validate this,
because of the potential
of recursive nesting.
This is just
a fundamental limitation
of regular expressions,
because they don't have
arbitrary memory
to encode information
about past outputs.
To make this easier to grok,
here's a really simple example
of a language.
Our language is defined
as all of the strings
that have matching open
and close parens
and you can see we have
a quick example here
where all parentheses are
matches.
This is something
that's so easy to explain,
but it's not possible
to implement

[00:31]
with a regular expression.
And to show you why,
there's actually two attempts
we have here to do so.
So the first one is very simple,
we just allow arbitrary open
and closed parens.
But it's pretty clear
why this won't work,
you can have one open
and two closed parens.
So it doesn't validate
our language,
we're kind of missing the memory
of what happened before.
Our other attempt here is much
more complicated and it works,
but only up to three layers
of nesting.
We go further than that,
the regular expression
doesn't behave properly.
This is just a toy example,
but we believe that recursive
and deeply nested
schemas are often critical
for developers,
so we really wanted to find
a way to support them.
We can do so by adding
in a stack
and this gives us the memory
we need to encode information
about past outputs.
So this stack will let us
keep track of things like,
how many open parens
have I seen before?
This approach is known
as the CFG,

[00:32]
or context free grammar
approach.
It's a little trickier
to implement
but it allows
for far more expressiveness.
This is the approach
that we went with and it's
why it takes a little bit
of time
to build up this tree
for inference.
It's also why we support
recursion in deep nesting.
So, that's the engineering side
of structured outputs.
We just talked about
how LLM inference works,
why token masking is
a useful building block
and how this all comes
together in the extensive subset
of JSON schema that we support.
We believe
that this implementation results
in the greatest set
of trade outs for developers.
We've kept inferences
as fast as possible
and we supported a very wide
subset of JSON schema.
And we believe the tradeoff
of waiting a little longer,
that first request
while you're developing,
is worth it for most developers.
So now let's get into
how we've actually improved
our models with research

[00:33]
to work with structured outputs.
-Awesome.
[ Applause ]
Thank you, Michelle.
So that was a little bit
of the engineering
behind structured outputs.
Next let's talk about
the research side.
On the research side
we wanted to ship a model
that was much better at
following formats as specified.
It's not enough
to just constrain the model
to a valid output,
if those outputs are
out of distribution
or low probability
for the model.
Because the model
will often behave erratically.
Some of you may have seen this
as the infinite
new line problem before.
This happened with some
of our older models
that weren't trained
on response formats.
The models natural
inclination was to generate text
that works in JSON,
but because it was
being forced to output JSON,
the only valid
sufficiently probably token
was the new line character.
So the model would distribute
the new line token,
one after another, all the way
until it hits max tokens.
So, we wanted to avoid
this problem

[00:34]
so we specifically trained the
models to understand JSON schema
and in particular,
complex schemas better.
It's also not enough
for the model
to just understand the schema,
it needs to know what
the quality of that field is.
There's a semantic meaning
behind the keys.
For example, consider
this action item schema.
Each action item has
a description,
a due date and an owner.
To produce a good output,
it's not enough to know
that a description is a string
and the owner is a string.
The model needs to know
what kind of string
goes into a description and what
kind of string goes into owner.
So, to ensure
the models are good at this,
we train them with a whole bunch
of complex schemas,
including nested schemas.
So here are the results
from our training process.
This graph shows our models
on the x-axis
and their accuracy on one
of our evals on the y-axis.
The first three bars
from the left are GPT-4,
GPT-4 turbo
and the original GPT-4o.

[00:35]
You can see that accuracy
improved from about 26% to 86%
over the last year.
Now at the very end here,
you see the results
for our latest model.
The orange bar shows the models
results with just prompting
and it has an accuracy of 85%.
When you add in the
newly trained response format,
we see that the yellow bar,
the accuracy improves to 93%.
This is much better,
but still not 100%.
So to get to 100%, we can enable
constrained decoding,
as Michelle shared earlier,
giving us a perfect score
on the green bar.
So in this way, combining
research to improve the model,
with engineering to implement
constrained decoding,
brings out the
best possible results.
Okay, finally let's get into
some interesting design
tradeoffs we made
when creating this feature.
We'll talk about three things,
additional properties,
required properties
and the order of properties.
Let's start
with additional properties.
So one of the controversial API
design decision we had to make,

[00:36]
was deciding what
to do with properties
that were not defined
in the schema.
By default, JSON schema
always extra properties,
so all additional properties
are always allowed.
Now this is generally
not the behavior
we as developers expect.
You can imagine errors
like this,
where we have a function,
get weather,
that accepts two arguments.
If the LLM produces
an extra argument,
we get a run-time error.
So, we decided to disallow
additional properties
by default in the OpenAI API.
That said, this meant
the default in our API
was different
than the default in JSON schema,
that's not great especially
if the developer
already has a predefined schema
from elsewhere
in their application.
In general one
of our API design principles
is we prefer to explicit
rather than implicit.
So we decided to require
that developers have to parse
in additional properties false
in their schemas.
This makes the API
a little bit harder to use,
it means you have to set
this property every time,

[00:37]
but it sets expectations
better with developers.
Okay, let's talk about
required properties.
By default, in JSON schema,
all properties are optional.
This is, again, not what we
as developers expect.
To go back
to our earlier example
of the get weather function,
if the LLM decided
to skip one of the promoters,
we would again get
a run-time error.
So to make this feature
more intuitive,
we decided that all properties
were required by default
and once again to set
expectations,
we require developers
to parse this in,
in the required directive.
Now, we do have a workaround
for optional parameters,
which is to make them nullable.
This gives us the best
of both worlds.
You get optionality,
would the performance tradeoffs.
Okay, finally let's talk about
the order of properties.
My default JSON schema has
no ordering constraints,
which mean the LLM can
produce properties in any order.
But in the context
of LLMs order really matters.

[00:38]
Having the strict ordering of
properties can be really useful.
For example,
you can use an earlier field
in your schema
to condition the value
of a later field.
Such as adding a chain
of thought field to your schema.
The model will first
generate the chain of thought,
explain its thinking,
and then generate the answer.
This often improves the quality
of the answer significantly.
So to support this use case
we decided to generate
fields in the same order
that you define them in schema.
So that API design.
We wanted to make sure
that the API had good defaults,
while making the constraints
transparent to the developers.
Okay, so to bring it
all home here's Michelle.
-Awesome.
So you can see that
the engineering and research
paths of this product result
in a meaningful improvement,
but only when combined they
offer the best possible results.

[00:39]
This is actually our ethos
behind the work in
the OpenAI API.
We want to do the engineering
and research work on our end,
to make the easiest to use API
for developers.
We want to solve problems
like structured outputs for you,
so you can spend time
working on what matters most,
your application.
We think structured outputs was
the final puzzle piece
for unlocking the full power
of AI applications.
Data extraction is now reliable.
Function calls have
the required parameters.
And finally, a agentic
flows can work 100% of the time.
Since we launched
structured outputs in August,
developers like you, from
big companies to small startups,
have been building amazing apps!
We've seen customers like
Shopify use structured outputs
to reduce hallucinations
and improved the reliability
of their applications.
We've also heard
the excitement from all of you.
It's been so great
to see structured outputs solve

[00:40]
so many problems for developers.
And this is
why we do what we do.
Our mission at OpenAI is
to build safe AGI for everyone.
We build the API because we
think working with developers,
you all, is just critical
to achieving that mission.
You see the future before
anyone else, and together,
we can spread this technology
to the furthest reaches
of the world.
As follow engineers,
we feel so lucky to serve you.
So thank you for building us
and we're so excited
to see what you do.
Thank you.
[ Cheers and applause ]

</details>


#### Launch apps with evaluations

Video on incorporating evals when deploying AI products.

video](https://vimeo.com/1105244173)[![MCP intro](https://cdn.openai.com/devhub/resources/video-3.png)

#### MCP intro

Introduction video to Model Customization Platform (MCP).

video](https://vimeo.com/1105243308)[![New audio models intro](https://cdn.openai.com/devhub/resources/video-4.png)

#### New audio models intro

Overview video of new audio models for speech and transcription.

video](https://www.youtube.com/watch?v=lXb0L16ISAc)[![Realtime agent demo](https://cdn.openai.com/devhub/resources/video-1.png)

<!-- yt-inline:lXb0L16ISAc -->
[![Audio Models in the API](https://img.youtube.com/vi/lXb0L16ISAc/hqdefault.jpg)](https://www.youtube.com/watch?v=lXb0L16ISAc)

<details>
<summary>자막: Audio Models in the API (15:25)</summary>

[00:00]
hello everyone and welcome to another
live stream of open AI I'm Olivia gar I
lead the open platform as you all know
we've been busy building agents for the
past few months deep operator research
um deep research operator and just last
week we released the agent asdk which
allows you to build your own custom
agents today is really really exciting
we're moving beyond text to voice
agents many people prefer to speak and
to listen over writing and reading so in
a way voice is a very natural human
interface and today we're going to
enable developers and businesses to
build voice agents agents which are
reliable accurate and flexible and so
we're going to announce a bunch of new
models and tools for that so let's hear
it directly from the team who built that
offering thank you Olivia

[00:01]
hi everyone I'm Shen I work on open AI
research team hello I'm yaroslav I'm
engineer on openi API team and I'm Jeff
Harris I work on the open AI API product
team today we're releasing three new
models and a bunch of new tools and
capabilities designed to make it really
easy for developers to build Rich
humanlike voice experiences we have two
new state-of-the-art speech to text
models that outperform our previous
model whisper on literally every
language that we've tested we have a new
text to speech model that for the first
time let's Developers control not just
what the model says but how it says it
and then we have a big update to our
agents SDK to make it really easy to
turn text based agents into voice agents
so let's post for a second what is a
voice agent and how do I even build one
yeah great question we think of agents
in general as AI systems that can act
independently on behalf of a user or a
developer so you might see a text agent
if you visit a website and you see a
chat box in the bottom right and you
want to ask about the product catalog or
your recent orders that's by text you
can do the same thing with voice so you

[00:02]
can call in and be speaking to an AI
voice um there's other ways to use voice
agents one of my favorites is language
learning experiences where you can have
a voice agent that's coaching you on
pronunciation creating a lesson plan for
you doing mock conversations with you in
the language that you're learning many
many ways to build voice agents um and
we see two primary approaches that
developers take the first one is using
more futuristic speech to speech models
these are models that are capable of
understanding audio directly and
speaking directly back they're really
fast they're what powers advanced voice
mode and chat GPT and our real-time API
the other approach which a lot of
developers do as the way to get started
in voice is what we think of as a
chained approach where you take a speech
to text model understands what the user
says turns it into a text transcript
that's then processed by a Texton llm
like GPT 40 and then that model figures
out an appropriate response and passes
it to a text to speech model to speak
back to the user developers often love
the chain approach first cuz it's

[00:03]
modular they can mix and match all the
different components so they're using
the best models for their use case they
also love it because it's the easiest
way to get really high reliability the
gold standard in terms of intelligence
is still Tex based models though the
speech to speech models are't catching
up quickly and then the third reason
they love it is it's easier to get
started you can take all of the work
that you've done in a text based agent
and you can Preen to speech to text
model on one side put text to speech on
the other side and now you have a voice
agent so for today we're mostly going to
focus on how we have new tools to help
you build voice agents with that change
approach so let's get into it a few
things to cover we'll start with speech
to text where we have two new models GPT
40 transcribe and GPT 4 mini transcribe
you you've been working on these models
I'd love to hear how they were built and
how they perform yeah thank you Jeff I'm
happy to introduce more technical
details for our new uh Speech to Text
models um compared to our last
generation models whisper and the
whisper 3 our new generation model is
based on our Lar speech model this means

[00:04]
this new model has been train on
trillions of audio tokens it all also
inest our latest Technologies and also
architecture of our models we also
distill the larger model down to a much
smaller size one which is the GPT 40
mini transcribe the smaller size model
is faster and more efficient it also
retain as good transcription capability
as possible compared to the larger
models let's see how good our models are
we measure the accuracy say of our
transcription by word error rate the
word error rate is the percentage of
words that our model gets wrong so of
course the lower the word error rate is
it means the higher our model actually
performs and then the dark blue is the
newest 40 and the one beside it is 4
mini exactly as you can see compared to
our previous generation models with per
two and with per three our newest model
actually perform almost like um on every
single language we performed across the
board nice aome very cool let's also

[00:05]
take a look at uh where we are you know
on the compared to the other options on
the market nice so what I'm seeing here
is that the new model is state-ofthe-art
across many languages English Spanish
more um and then actually for om Min is
state-ofthe-art if not for its bigger
Brother model as well yeah if you are
actually looking for a very high
accuracy transcription model our model
definitely is the best choice for you
great so that's GPT 40 transcribe and GP
4 mini transcribe 40 is available in the
API today for just. 6 cents per minute
same price as whisper and 40 mini
transcribe is3 cents so half price
really really great state-of-the-art
options we're also enhancing our speech
to text apis with streaming so
developers can pass in a continuous
stream of audio into the model and get a
continuous stream of text and response
that makes it easier to build really
fast experiences and we're bundling into
these apis a bunch of hard problems that
developers need to solve to build voice
experiences so they come with noise

[00:06]
cancellation so the model isn't going to
get tripped up by background sounds they
also include a new semantic voice
activity detector which chunks the audio
up based on when the model thinks the
user is actually finished speaking so as
a developer you don't need to worry
about processing some half-spoken idea
um and all those capabilities are
available in the speech to text apis as
well as in our real-time API so very
excited for you to check that out next
capability is a new text to speech model
GPT 40 Mini TTS yav would love for you
to show us how this one works yeah let
me pull this up so um this is openfm um
it's a website uh we built just to make
it easy to play with this new model um
so as you can see there are a bunch of
voices that you can choose from um there
are different prompts that we
pregenerated but you can also type in
your own so this is basically a new
field that we added it's an instructions
field that tells the model how you want
it to speak the text um so yeah let's
Maybe try um try some um mad scientist

[00:07]
please exactly yeah as you can see like
we prompted basically like how we want
to deliver what kind of tone we want
high energy it's chaotic exactly all
right let's see what that's
like
and it may be busy all right busy yeah
let's try again one more
time the Stars tremble before my genius
the rift is open the energy surging
unstable perhaps dangerous most
certainly Captain Ryland this is really
intense okay so that's a lot I'm curious
if we took the same voice and tried to
yeah let's make
it how about let's say um the live
stream is going really well you're doing
great
yeah typing under pressure

[00:08]
let see how it
goes this live stream is going really
well you are doing great thank
you so that's super fun I love the Retro
look if developers want to play with
this and actually figure out how to code
against it what do they do yeah so you
can just click here and then we show you
basically some Snippets in Python
JavaScript or if you just prefer to curl
it directly and Ju Just to be clear the
tone the the personality is not tuned
into the model it's just prompted
exactly yes you can just prompt it um
and you can be as specific as you want
you can tell it exactly what kind of
pacing what kind of motion you want to
here um so it's very easy to to play
with you can just like you don't even
have to follow this form and just type
in anything free form that's awesome
very cool so that's gbt for Min TTS
available in the API today for just one
cent per minute very economical option
for generating really Lively audio we
thought the last thing to show would be
how this all comes together and to do
that we're really releasing an update to

[00:09]
our agents SDK our agents SDK launched
just last week as a way to really
encapsulate a lot of the best practices
that we've seen in terms of building
reliable text agents guard rails
function calls WR tools it handles all
that stuff for you and today we're
making it really easy to convert those
text agents that you've already built
into voice agents so yav I'd love for
you to show us the code changes involved
to make that conversion yeah um uh so
this here is the demo that we showed
last week so it's an AI stylist U it's a
customer support agent uh which you can
use to look up um some pagonia jacket
orders um so let's first see how it
works this is just like a text based
agent
okay so I'm just going to ask for some
recent ORD so you see it's see debug
information yeah yeah and then yeah it
just printed the last orders so it's
like the same thing that that we showed
last week okay now if I wanted to use
this on the phone what would I do
exactly so let me pull up the code so
here you can see um it's the same
configuration that we had last week it's

[00:10]
using the agents DEC um and we have
three agents here so we have three agent
um that receives the initial message and
decides what agent is going to process
it uh we have stylist agent which has
access to web search tool it helps you
pick a style and then we have customer
support agent which we just saw um and
it has access to past orders and it can
also submit refunds now let me open the
backend server code so it's a very
simple uh web socket uh backend um since
last week our team has made changes to
the UI so now U I can record audio and
it can play audio back and then that
audio is streamed to the back end uh
with this websocket connection um so
what I'm showing here is um is a
workflow so it's the same type of
workflow that our um agents SDK already
supports it's a text based workflow so
it takes in user text and then we pass
it to the run runner which feeds it to
the llm and then we get back the output
in the streaming fashion again as text
and then we send it to UI and then make
it available for Downstream processing
so this part is the same um and this is

[00:11]
the implementation of the the back end
so basically like when we get a message
from user We Run The workflow get back
text and then stream it to the UI so now
let me show you how to turn it into a
voice agent just with a few lines of
code um so first of all we need to also
handle audio messages from the
UI so I have some Snippets I prepare to
make it easier to demo so basically we
get a new chunk um of audio and then we
need to accumulate those audio chunks
first
um I need to make sure I don't
forget to initialize the buffer right
and so now let's see once we get the the
full audio what we need to do is we need
to send it to the agent so here um we
are getting the um the the audio we
concatenate all the chunks and then we
feed it into this voice pipeline so
voice pipeline is a New Concept we're
introducing um essentially what it can
do it can take your existing workflow
and it can add speech to text on one
side and text to speech on the other
side so essentially it will take audio

[00:12]
it will convert it to text feed it to
that workflow which I just showed
earlier it will get back text in a
streaming fashion if needed and it will
convert it back to speech um and you get
the output as a speech so here all those
events this is this is audio and then we
send it to the UI to to play um so I
just saved it yeah let's let's see Let
me refresh this um and let's see hey
what was my last
order so it's doing the tool call
your last order was on February 9th 2024
you ordered some Patagonia shorts in
Olive and it's all fulfilled if you need
help what was the order
number the order number for your
Patagonia shorts is
a507 if you need anything else feel free
to ask awesome so that was like nine
lines of code to build the voice agent
it's voice agent very cool and I guess
if I'm a developer I'm going to be
wondering if I build a voice agent how
do debug it how do I figure out if it's

[00:13]
working well what do we have there um
it's a very good question so um this is
a tracing UI that we demoed last week um
and we updated it to support audio now
um so let's see so this seems like um my
most recent chat I practiced a lot um
and
uh we can see that uh there are traces
here from our um most recent
conversation Let
me refresh this oh this is the most
recent chat um
yeah so so we can see that there are
traces here from our most recent
conversation um and as you can see there
are like all sorts of events so for
example we can click on this one this is
my first um request to the agent let's
play it hey what was my last order yeah
so it's integrated with audio you can
play it you can look up metadata you can
see different timelines latencies errors
and so on awesome that's PR cool so two
new speech to text models GPT 40
transcrip and gp4 on many transcribe

[00:14]
we're releasing the new text to speech
model and open ai. FM and then this
update to the agents SDK to make it
really easy to put it all together into
Rich reliable voice experiences that's
awesome we cannot wait to see what voice
agents you build with those new
technologies and we have more coming in
the coming month before we part one last
thing open.fm the demo that Yos showed
with the m scientist is actually live
open ey. FM um it's fun frankly we had
so much fun playing with it in the past
couple of days and so we thought why not
do a contest uh you know just like an
old school like radio station like a
radio contest if you will um and so you
have until tomorrow night so Friday
night to go on. FM and come up with like
the most creative like use of that text
to speech technology and share it with
open ey Twitter um and we'll pick three
winners and we have this amazing gift uh
for the winners which is a radio from
our friends at teenage engineering

[00:15]
special edition there are only three in
the world because there is op logo in
the back um anyway go to pfm share it on
Twitter and we'll send a tweet with like
more details on the terms of the context
um have fun and yeah see you thanks
thank you
[Music]

</details>


#### Realtime agent demo

Video introduction to the TypeScript Agents SDK.

video](https://vimeo.com/1105243382)[![Responses API — tools and features](https://cdn.openai.com/devhub/resources/video-2.png)

#### Responses API — tools and features

Overview video of available tools and capabilities in the Responses API.

video](https://vimeo.com/1105245596)[![Unlock agentic power — Agents SDK](https://cdn.openai.com/devhub/resources/video-3.png)

#### Unlock agentic power — Agents SDK

Video demonstrating advanced capabilities of the Agents SDK.

video](https://vimeo.com/1105245234)
