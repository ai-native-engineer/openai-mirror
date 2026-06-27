---
title: "Builders Unscripted: Ep. 1 - Peter Steinberger, Creator of OpenClaw"
channel: openai
url: https://www.youtube.com/watch?v=9jgcT0Fqt7U
youtube_id: 9jgcT0Fqt7U
published: 2026-02-24
duration: "31:28"
captions: en
---

# Builders Unscripted: Ep. 1 - Peter Steinberger, Creator of OpenClaw

[![Builders Unscripted: Ep. 1 - Peter Steinberger, Creator of OpenClaw](https://img.youtube.com/vi/9jgcT0Fqt7U/hqdefault.jpg)](https://www.youtube.com/watch?v=9jgcT0Fqt7U)

<details>
<summary>자막: Builders Unscripted: Ep. 1 - Peter Steinberger, Creator of OpenClaw (31:28)</summary>

[00:00]
Peter, welcome to OpenAI.
Thanks for having me.
We've known each other online
now for many years.
But I'm so happy to finally get the chance
to spend more time with you in person.
Likewise. Beautiful office, by the way.
Thank you, thank you.
You had a crazy couple of weeks.
We first had the idea of
doing a video together a month ago.
If we had done it,
then I would have had to intro you.
I guess you don't even need an intro
anymore.
It's not often that an open-source project
makes the Wall Street Journal.
So congrats on all the success.
How are you feeling?
Slightly sensory overload on all points.
But also, you know,
when I, when I started out this year,
like messing with AI,
I wanted to, like, inspire people.
And I feel like this is the final form.
So I'm, I'm, I'm proud.
It's been amazing.
You've been in SF for the past week.
And you attended some events
like the Codex Hackathon,

[00:01]
but you also had ClawCon, like an event
dedicated to OpenClaw.
Well,
it also was created by the community.
I created this Discord channel
about meetups after people were like,
“We need to have a meetup.”
And I'm like, “sure.”
And then I came to ClawCon
and there were like a thousand people,
and I was just blown away by like
the creativity, the
the the colors.
Like, there's so many things,
so many people excited.
I mean, that's how you realize
that you built something magical.
Like the project did not even exist
a few weeks ago, and now you have like
thousands of people embracing it,
using it, gathering to meet you in SF.
It’s pretty, it's pretty incredible.
Even in Vienna next week.
We have like already 300 people,
and it's by far
not as much of a tech scene
as San Francisco.
It's now worldwide. It’s a phenomenon.
Yeah, it's amazing that that this reaches
different continents, different cultures.

[00:02]
Indeed.
And so how has the conversation
been with like, the community here?
You spent time with the community,
some of the maintainers also that you've
kind of like brought into your project.
How has that been for you this week?
It's been quite something.
A lot of people love it,
and a lot of people have this expectation
of this
enterprise-ready final project,
when for me, for the longest time,
it was like my, my little playground.
I mean, the whole year, I'm
just marveling at what's possible now.
If you're a builder, this is like,
what a time to be alive.
Yeah.
What do you think is the most interesting
thing about building?
Like actually building,
being a builder at this moment in time.
Like, it's a very interesting time where,
like, the entire toolchain is changing,
the definition of what it is to be
a developer is also changing,
and anyone can build anything.
When I, when I started playing with,
with this new tech,
I got a dopamine hit every time. Back then
I started with Claude Code.

[00:03]
When it got something right
and it was like maybe 30% or 40% chance.
But to me it was like, BOOM
- like literally mind blowing
because I had this realization that
now I can build anything
and I'm, you know, usually also time
constrained because software is hard
and software is still hard,
but you're so much faster now.
I agree.
So if we take, a few years
back, maybe, and rewind a little bit.
So you, I got first got to know your work
back, I think in 2011
or 2012 when you build PSPDFKit. Yeah.
And from the outside it's interesting
because it feels like you've achieved
the dream of every developer
you kind of saw a problem,
you created a great solution for it.
You built a company around it,
you scaled it, you sold it.
But I'm sure that journey is never
that easy.
I mean, I didn't wake up one day
and thought,
I'm going to build
a PDF framework. That is like
-100 on my interest list.
So it kind of kind of just happened
like a weird butterfly effect

[00:04]
from being at the Nokia Development Days
to having friends that needed it.
And an American visa
taking too long kind of
emerged to me creating a company.
What I find interesting is like,
after that company,
you built, you kind of
took a break for a little while.
Yeah.
What brought you back?.
At the end, I was just really burned out.
Like I was running on high steam
for 13 years.
Running a company is hard.
Being a founder is hard. It's.
And I also didn't really,
it was my first one,
so I didn't really have the knowledge
how to, how to mitigate those things.
So I was just burning a bit too bright,
and I needed to decompress.
So I still followed the tech news
I saw, I think, the very early things
of GPT Engineer or whatever
it was called of ChatGPT,
you know, it was kind of cool, but it
didn't really excite me.

[00:05]
It’s…you always have to experience
new technology just by reading from it.
It doesn't really convey the power.
So for that, tech didn't really click,
and only when I was ready,
when I felt the need for like, okay,
I want to build something again.
And then I,
I didn't want to build it
in Apple tech anymore
because I, I'd done this
for such a long time and
the world kind of moved on a little bit.
You know, you need to,
things need to be built first.
And I kind of had to hinge back then.
But it's so hard when you go from
when you're such an expert in one field
and you move to another field.
Hard is even the wrong word.
It's more like, painful.
Because then you're like,
you have all this, this broad knowledge
of how to build things.
But to really do that without
agentic engineering
you need to still learn a lot to,

[00:06]
to move your knowledge over.
And then I thought like, let's, let's
check out what this AI stuff is.
The moment where it blew my mind was
I took this project that was halfway done
where I just.
Yeah, burned out
before finishing it, basically.
It's often the case that like for us
developers, we love having new ideas
and starting projects, but getting them to
the finish line is the hard part.
Oh, I see it all the time.
It's, it's really hard
and I would even sometimes fail.
But for this one, I,
I wantedto continue.
But I also wanted to rewrite it.
So I took the whole thing.
I made one huge Markdown file, like,
I don't know, 1.5MB with all the files.
I dragged it into Gemini Studio 2.5
at the time.
I said, “write me a spec”, and then
I had this like four-hundred-line spec.
And I dragged it into Claude Code.
And then I wrote, “build”
and I did other stuff on the main screen,
it was just like running on the side
screen for hours.
It was, it was,
things were quite a bit rougher back then.

[00:07]
And at one point it told me,
“I'm 100% production ready.”
You know, like the,
the sycophantic, Opus 3.5 or whatever
it was.
And I tried it and it crashed
and then I, like, hooked up
Playwright.
I think one of the few MCP
that I would actually use
and told it
to, like, build the login stuff.
And check the work along the way. Yeah,
with something for Twitter.
And then one hour later, it,
it actually worked.
And it did show me some stuff.
I mean, it was like the worst slop.
But to me this was like the moment
where it really clicked because like,
this is like just process wise, I got like
goosebumps, for like the possibilities.
And that was kind of the moment
where I couldn't really sleep anymore.
Because now, then like my head exploded
with all the things that I,
I always wanted to build that
I just couldn't before.
And then I just really went
into the rabbit hole.
A lot of people have seen like OpenClaw
as an overnight success for you.

[00:08]
But what I love
and what I find fascinating in your story
is kind of
how it's a culmination of so many projects
that you've been working on for the past,
like 9 or 10 months. Right?
Like when you look at your GitHub profile
is like 40 plus projects you've built.
Half of them are using the project.
Yeah, yeah.
And I think like many of those. Yeah.
You combine them all inside OpenClaw.
Yeah.
Can you tell us more about this journey,
about like, how all of these ideas
and projects made their way to OpenClaw?
I wish I could say that I had the unified
plan in the beginning, but
a lot of it was just exploration,
and I wanted things
and those things didn't exist.
And, and I just yield them or let's say,
prompted them into existence. Why?
You know, it's like, okay, let's build it.
And then and it was like step-by-step
just because I
yeah, I wanted my agent to like,
do some stuff for me.
I didn't have the this,
this just unified vision yet.
I had.
It's funny how it goes
full circle
because I wanted to have something

[00:09]
that would look at,
for example, my WhatsApp
and then I built it.
I even got the domain for that.
I built a prototype, but then I thought
all the big labs are going to build it.
And I was like, I’ll
just wait a little bit.
I focused on other stuff.
I just experimented a lot.
I, my mission was kind of like, to
have fun and inspire people.
And then by November, I,
I built a few versions of what I wanted,
but nothing really good.
And then November was like,
why are you still
why didn't the labs build any of that?
You know, like, what?
What the, what the heck are they doing?
And then I, I built
the first version that became OpenClaw.
We are at name number five now.
Still didn't fully click for me.
It was like, this is cool. Like,
took like one hour to,
like, build the first prototype
because you just
you just yield things into existence.
And then where it really clicked was

[00:10]
where I was
at this weekend trip in Marrakesh and
I, I found myself using it way more
because it was so convenient,
you know, like,
there was no, there's
no really good internet.
So WhatsApp, WhatsApp
just works everywhere.
And it was just so convenient.
But like,
I mean pictures to translate stuff
to like, find me restaurants but also like
look up stuff on my computer.
It was really cool.
I showed it to friends and I made it
like send text messages for me and, and
they wanted
it, you know, and I'm like,
you don’t use it.
You don't get that.
It's too dangerous.
And these are the only signs of like,
you know, product market fit.
If your friends already
want what you have,
even though you're going
to never design that for them,
it was more like reserved for
the technical, like peers that you have.
Yeah.
And then when it really clicked for me was
I used it so much and at some point
I sent like a voice message
and, and then I was like, wait,
this shouldn't work.
Oh yeah.
Tell me more about that story, because
I think we talked about it the other day.
That's fascinating.

[00:11]
It showed me
how good those models are in problem
solving.
You know, like, we built these things
for agentic engineering.
But really, the skill is, like,
more abstract,
like it's
if you want to be a really good coder,
you need to be a really good
problem solver.
And that just maps in any domain really.
So I, I sent this voice message
the typing indicator
appeared and I'm like, I'm very curious
what happens now.
I just I didn't build this kind of work.
And then the model just replied to me
and I'm like, “How did you do that?”
And this is like, ask the model, like how,
why, this should not work.
And the model was like, “Yeah,
you sent me a message,
but it was just a file
with no file ending.
So I just looked at the file header and
found that it's Opus, the audio codecs.
So I used FFmpeg
on my computer to convert it.
And then
I wanted to, to transcribe it,
but it didn't have Whisper installed.
So I found I looked around
and I found an OpenAI key. And
I used cURLto send the file to OpenAI and

[00:12]
got the text back and here I am.”
This is incredible.
I mean, like, that's the power of like,
giving tools and the complete access
to a computer to these like, agents.
Yeah.
And now they can just like, actually
come up with the solutions themselves,
even though you never programmed them
at all. It's so funny.
Like I told the story and people are like,
“Oh my God, it just used your key like,
this is madness.” I'm like, “No,
like I put the key in the environment
exactly for that reason.” If it's, it's
kind of like a script that you access,
my OpenAI key,
like my bot works in the same,
in the same environment.
Of course, it should access my OpenAI key,
like I put it there for that reason.
This is not bad.
This is exactly what I wanted.
Yeah.
Yeah, that's, that's
when I had my little moment.
And then every time I,
I showed it to friends,
I put them in a little group chat.
Like to be,
to be frank, like, this is, this thing
is designed for one-on-one communication.
Right?
So if you put in a group chat, pick
someone that you trust.
Really trust. Yes. Yeah.
Because it was not designed for…

[00:13]
Oh, let's just put it out there
and it will always do the right thing.
You know it is your personal assistant.
When I set it up,
I was also very intrigued.
I was like, this is a weird setup.
I'm like, where is this going to take me?
But I had also a few like, ‘aha’ moment
where, like, the more access you give it,
the more tools and skills you give it,
the more impressed you can become.
You also give it like a Vercel skill,
and then you ask it to build
a website or application,
even for an event you want to host.
Not only is it building
the app, it's also using your OpenAI key
to like make some AI features into it.
It's deploying it to Vercel.
There's already a link
you can share with friends.
It's a kind of like mind blowing step-up
change
versus just like,
oh, I'm augmenting myself to write code.
So that November and December,
I was like, hooked on this, and I, I mean,
I still do some other projects,
but like most of my time went
there but, on Twitter,
people wouldn't get it.
It's like I got very muted responses
and I'm like every time I show it
to a friend, they wanted it and I'm like,
no, no, it's not ready yet, you know?

[00:14]
So then I was like, hey,
what's the most insane thing
I can do to like,
show people how cool this is?
So I created a Discord
and just put my, my bot in there
without any security, because back then
I didn't even had sandboxing built in.
It was just very early
and I just worked in the open.
I basically built now
OpenClaw with OpenClaw and debugged it.
And then I asked the model like, “Oh,
do you see this tool called–?” “No,
I see nothing.” It's like, “Oh
yeah, check,
check your own source code.” And,
and did all a bunch of stuff
and people saw it
and then they understood.
And when you put it in Discord like this,
what kind of access did you give it?
Did you also give it like all your tweets,
for instance?
Like what kind of, like knowledge
did it have about you?
Not all of my tweets. It's too many.
But a lot of my memory stuff. Yeah. So
I actually
was monitoring it very quickly because,
yeah, prompt injection is unsolved.
But also the latest generation of models
is really good.
So I have like, one canary mysoul.md

[00:15]
that kind of defines
what are my values.
How do I want a model to, to work, to
operate, to sync what's important to me.
That’s secret.
Yeah. And people really wanted that.
And the random people come in
and try to like prompt inject
it and pasted like huge blocks of code.
And the model was like, “I'm
not reading this.” So
it was basically mocking them,
but I was still not very confident.
Right.
So, the first night was like,
got me a whole lot of interest.
And then I turned it off.
I went to bed, slept like ten hours,
woke up, it was like 800 messages.
And, on Discord
my agent was replying to every single one.
I freaked out, like I turned it off again.
I read through every single thing and,
and at some point I chilled out
because it actually didn't,
it didn't do anything malicious.
It didn't manage to get mysoul.md out.
I'm not saying this is,
I'm sure prompt injection is possible,

[00:16]
but it's not as easy as people
think it is. Right.
In the grand scheme of things,
it was actually performing
the way you wanted it to.
Yeah, my big mistake was I,
I disabled it, but I forgot that
I actually had a LaunchDaemons.
What,what's the the main thing
a LaunchDaemons does?
If the thing crashes or is killed,
it restarts it.
Yeah. Because you want reliable service.
And, like, I built this to be a reliable
service, and I just didn't think about it,
so I killed it, and it restarted
in five seconds while I went to sleep.
Now I know better, but now I'm also,
I also put in sandboxing,
so it was so proud
that it's in his Mac Studio.
It calls it, “The Castle”.
And then I put it
into a little set container.
But, you
know, those models are so creative.
Like the first time I made
a, I made an LPN docker container
and there's like nothing in it.
And I told now Molty like, “Hey,
can you check out this website?”
And they were like,
“There's not even cURL,
there's nothing in here.”
And I'm like, “Be creative.”
So it built, it built,

[00:17]
lobster cURL, just like.
Its own tool?
It just builds on its own cURL, but
like using some, some TCP socket and like,
there was like a C compiler
and then it had like
built like a crappy version of cURL,
so you could actually access a website.
And it worked.
Crazy.
So like, those things are so resourceful.
It's incredible.
Yeah.
You had some challenges too like,
you know, people really like,
taking a look at the security issues
potentially, and expecting you to have,
everything so robust from day one,
although you were just
putting an open-source project out there.
Yeah.
I always laugh
when people ask me like, “Oh,
yeah, can you put me in with like, the CEO
or Human Resources or some other member
of my team?” And I'm like, “It's
just me hacking from my cave.” Basically.
Like, but that's where you see
the dissonance, right?
This would have not been possible by
any human.
Any one human.
Yes. I have maintainers
now, and I got PRs,
but essentially I built this. Yeah.

[00:18]
Even a year ago,
it wouldn't have been possible.
There is no model for like, something like
this could be built by one person.
So it's not even,
they don’t even consider that.
Right. Yeah, let’s actually touch on that.
Like I think, on your for like,
productivity because I'm sure like
many developers must be wondering like,
how is Peter so productive?
And I was looking at your GitHub again
this morning and I saw it’s like 90,000
contributions on more than 120 projects
just this past year.
But what's also interesting is like,
you know, the past year starts very white
on the GitHub activity graph
and then light green
and then into fall around October,
November, it's very dark green.
Yeah, that's What happened?
I switched to Codex.
Like with
every generation they got better.
But it's not just that the agents got
better, the harnesses got better, also,
my understanding of how to approach this
in my workflow got better.
You know, there's these people
that write software in the old way
and the old way is going to go away.

[00:19]
And then they try,
they call it, “vibe coding”.
I think vibe coding is a slur.
And then they try AI, but
they don't understand that it's a skill.
And then you, you pick up the guitar.
You're not going to be good
at the guitar in the first day,
so they're going to have a bad experience.
And then they're like,
oh no, it's not going to work.
While if you approach it more like playful
it, you have to learn.
You have to like
I have a gut feeling now for like,
which prompt will and how long it'll take.
And if it takes longer, I'll, I reflect,
oh, maybe I made a mistake.
Maybe my architecture is wrong,
my thinking was wrong,
or maybe something else.
Just as with code,
if you, if you write code
and you have a feeling of oh, this is,
this naturally goes into my architecture
or this is, this is I'm fighting
the system and it just takes time.
And so if people want to become more
like you, what is your Codex set up today?
Because I think you've famously said, like
most people overcomplicate their setup.

[00:20]
I mean, I also over complicated my setup.
I call it, “the agentic trap”.
From your first touchpoint
in that new technology to like,
becoming really effective.
A lot of people get stuck in there trying
to like, super optimize their setup.
It doesn't
really make you more productive,
but it feels like
you're more productive. So
like I put out this one blog post,
it was very controversial,
but I just talk to it like you
just approach it like a conversation,
like your model is like,
your it's not really pair programming.
It's something different.
It's, it's, it's a conversation.
I basically tell it what I want.
I always ask the model,
do you have any questions for some reason.
Like there's always questions.
But the model by default is trained
to just solve your problem
and then would just make assumptions.
The default assumptions
might not always be the best ones,
especially, you have to remember it’s
trained with a lot of code
and also a lot of older code.
“Do you have any questions?”
is like a very important question.
People don't realize that the model
usually starts with a blank slate

[00:21]
because they don't learn like us.
Like every new session is like,
I know nothing about this codebase,
and I'll just search and find
the little things that you ask me to
and then try it to solve it.
But they don't see
usually the whole picture.
If you do this properly, you have to have
the full picture in your head
and you have to like,
help the model a little bit
to motivate it to like look here,
look there.
And Codex is just much better
at taking a broad look first.
I use a very,
a very basic approach.
I don't even use the worktrees.
I just have,
Check out 1 to 10, basically.
Keeping it simple helps me to focus
more on the actual problems.
So I don't even want to deal
with branches of worktrees.
I just focus on different problems.
Ideally, it gets easier if the project
becomes a little bit larger.
Then you can work on different things
that don't fight each other so much.
You used Codex a ton to build OpenClaw.
Yeah.
How has Codex changed the way you work?

[00:22]
Well, I tried a lot of tools,
and what I like about Codex
is that my trust in it
building what I want, from all the tools
right now, is the highest.
And the number of things
that just work is really high.
And I don't think what people realize
is that this GPT 5.2,
it was, again, like a quantum leap
in terms of, yeah, this will just work.
I'm still amazed how
well this already works.
That's fantastic.
We can just build things.
This is pretty incredible.
Yeah. Like people need to give this a try.
You famously said also
that, like, you're shipping code
now that you're not even reading.
How has that changed?
Most code is boring.
Like most code
just transforms one shape of data
into another shape of data, and eventually
the user sees it or goes somewhere else.
So like on most, most code,
it writes, I'm.
I have a pretty good understanding of what
it writes and it's enough to like that.
I, I see the stream,
and see that okay, like the mental model
I have in my head of what it creates
is approximately what it creates.

[00:23]
I was, I led the team before, right?
I had a lot of software
engineers under me.
And that also requires accepting
that they will not
write exactly the same code that I want.
In the end, you,
you should optimize a code base so agents
can do the best work, which is not always
the same as humans can do the best work.
Right.
It also means accepting that
maybe the code
is not exactly how I would like it,
how I would write it and then I could push
the model towards that.
But oftentimes
there's so many ways how we can structure
something that often it doesn't matter.
If it becomes a performance problem,
you just focus on that.
You make it better.
And your point that you just made on like,
you kind of like, the value of code
and how you approach code is also changing
a lot, how you approach open source.
Right.
Because like I was looking at like
OpenClaw,
you now had like 2000 PRs open right now.
Yeah. You all are crazy.
Before we had like AI,
you know,
you would have to read all of these PRs
because there was value in the code
being created.

[00:24]
But sometimes now you refer to that
as like not a pull request,
but a prompt request
almost because it's like more the idea
or the intention behind the PR that's
more important than the code itself.
PRs actually sometimes take me longer
than if I would approach it myself.
Because
my trust in the model not being malicious
is much higher
than an external contributor
that I never heard of before,
and we had no discussion before.
So I have to scrutinize that
a little bit more.
But then if I see a PR  I’m like, I,
I started to review
and my first question to the model is
do you understand the intent of the PR?
Because I don't really care
about the code.
I care about what is the person
actually trying to solve?
You know, it's more like an issue with
like a, here's my attempt of a solution.
But first of all, many, many people still
don't really know how to yield the agent.
And then often it's
just a very localized solution
because they, they don't have
the full system in their head.
The hard part is,
how does this little new feature
fit into my whole, my bigger system?

[00:25]
Or how does this little fix okay,
this little fix fixes a tiny thing, but
is it even the right fix? Is it, is it?
It's probably often this is like
a more systemic or an architecture issue.
So the model is actually really good
if you, you just have a conversation
and then I say okay, now build this
and it will start to build this.
So I ask the model, what's the,
what's the intent?
Is that the most optimal solution?
Sometimes it says yes, most often
it will say no.
Then I would start to explore
what would be the,
what would be the best fix.
Is this like an architectural problem?
Is it something that is, let's say,
it's a problem in message handling.
Does it only affect WhatsApp?
But maybe also,
I don't know, Signal? Yeah.
So should we, should we solve this
in a more general way?
Is this a new feature?
Do we even want a new feature?
So sometimes those discussions go on
for like ten, fifteen minutes.
I use like, voice because it's literally
like you,
you talk to a very smart coworker.
Easier to give tokens over voice than typing.

[00:26]
Yeah.
When, when I'm happy, then I have like one
slash command, like len(PR).
That explains the whole procedure, right?
To like, actually create a branch,
do all the changes, get the PR merged.
I, I wanted to create a community,
so I try to still
credit the person that created it,
even though the whole thing
takes me longer
than if I would just write it all myself.
Right. But I appreciate that people
want to be part of this.
What's your vision for OpenClaw now,
going forward
with all of these contributors
that are kind of like
surrounding the project?
And do you see yourself as kind
of a trailblazer for this idea of like,
what a personal AI agent should look like
so that, you know, a billion
people can one day use
something like that? Yeah.
I want to find the balance between
this is something that my mom can install,
but also this is something that's fun
and hackable, which is difficult.

[00:27]
You know, most open-source projects
you like, download the package.
But for the longest time my default
install was get clone, build, run.
And then you literally have
the source code on disk,
and the agent sits in the source code
and is aware of the source code.
And if you don't like anything,
you literally prompt the agent
and it would change itself like, like
actual self-modifying software.
So a lot of people that never sent me a PR
sent me a PR.
That's also
why it's more like a prompt request,
because they just lack the understanding
of how to build
software that lasts.
And at the same time,
the whole world is, is,
or the whole security industry
is like putting their eyes on it,
which has been interesting
and also a little bit
frustrating because it misses some nuance.
Right?
For example, the, the web server
that I have that's meant for you.
Initially, I built it for debugging
and then I made it pretty,
but it's only meant to be accessible
in your network, in your trusted network.

[00:28]
But because it should also be
like a hacker’s
paradise, there's an option
how you can like, change that.
Because
like some people have weird setups.
Maybe they use like Ngrok,
maybe to use reverse proxies.
So there is a reason
why I didn't want to like
limit that.
But now you have like, people that
put it on the open internet, even though
I'm screaming in a secret document,
please don't do that.
That's not,
that's not what it’s intended for.
And then I have the security people
that point out that,
oh yeah, it doesn't have login
limitations, you know, like it, it doesn't
have all the things that you need
when it's on the public internet.
I'm like, yeah, I didn't build it for that
with that intention.
But because it is configurable,
it totally counts as a, as a CVSS 10.0.
So yeah, I, I,
I struggled a little bit with that.
But now I,
I brought on actually a security expert.
That's the main focus.
I, I realize I cannot stop people
from using it in ways it was not intended.
So my, my big focus now is to like,

[00:29]
support all these use cases and help
people not shoot themselves in the foot.
Right.
That's the beauty of open source.
People can embrace it
and like come up with ideas
that you didn't even think about.
Yeah,
that's the beauty and the madness of it.
Zooming out,
maybe for a second beyond OpenClaw.
Like, I've talked to a bunch of developers
this week.
We knew you were coming to the Codex
Hackathon.
They told me, like, how many?
Like, how come does like, Peter,
come up with all these great ideas?
Like, how does Peter come up
with so much creativity?
I don't know
if you have any answer to that,
or if it's more like your own curiosity
that you're following.
It's more like this realization that
stuff's easy now.
So even if I find an open source thing
that maybe solves my problem to 70%,
I just build it myself,
which would have been absolutely
impossible a year ago even.
And now it's just like
I just prompt it and it's on a second
screen and, and Codex works.
We’re both from Europe.
When I travel outside of SF
and I go back to Europe,
I'm sure you feel the same way,
like many developers and engineers

[00:30]
have not embraced Codex
and agentic tools just yet.
What would be your advice for them?
Like as they get started
and like should rethink the way they work
and their workflow.
My first advice always is like,
approach it in a playful way.
Build
something that you always wanted to build.
I'm, if you are at least
a little bit of a builder, there has to be
something on the back of your mind that
you want to build, like just, just play.
You just have to approach
this, this, this, this in playful
because like, I think the Nvidia, Nvidia
CEO said that in the near term
you're not going to be replaced by AI,
you're going to be replaced
by someone who uses AI.
Who uses it better than you, yeah.
But if your identity is, I want to,
I want to create things.
I want to solve problems.
If you are high-agency, if you're smart,
you will be in more demand than ever.
Yeah.
It's such a great time for builders
who embrace these tools,
shape their curiosity, and really can
bring any ideas to life the exact same way
you've done with all of these
great projects and OpenClaw.

[00:31]
I think in a year this is going to,
this is going to explode.
Yeah, 2026 will be an interesting one.
I think it's a fantastic way to end.
Thank you so, so much, Peter,
for your time. Thanks for having me.
Wonderful to spend time with you.
We all at OpenAI love your work.
We love supporting builders like yourself.
And honestly, you're a true inspiration
for the broader developer community.
Thanks again
and we can't wait to see what you're going
to work on next.
some adjustments with formatting and line
designation here
@graham.lewis@c-openai.com
can you check this line?
Is he saying "easier to talk" or "easier
to give code in"?
I think the latter but want to make sure.

</details>
