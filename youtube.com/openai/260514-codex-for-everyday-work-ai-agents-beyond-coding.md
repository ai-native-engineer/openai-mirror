---
title: "Codex for Everyday Work: AI Agents Beyond Coding"
channel: openai
url: https://www.youtube.com/watch?v=DLP9CagE3dU
youtube_id: DLP9CagE3dU
published: 2026-05-14
duration: "43:03"
captions: en-orig
---

# Codex for Everyday Work: AI Agents Beyond Coding

[![Codex for Everyday Work: AI Agents Beyond Coding](https://img.youtube.com/vi/DLP9CagE3dU/hqdefault.jpg)](https://www.youtube.com/watch?v=DLP9CagE3dU)

<details>
<summary>자막: Codex for Everyday Work: AI Agents Beyond Coding (43:03)</summary>

[00:00]
Good afternoon.
Welcome to OpenAI forum. Uh my name's
Chris Nicholson. I'm with the Global
Affairs team and I'm glad to be here
with all of you.
So, the forum, as some of you know, is a
place where we talk with experts about
how AI is being [clears throat] used in
the world.
Today's conversation is about Codex and
why it matters beyond software
engineering.
So, more and more people are using Codex
to help with knowledge work and personal
work. They're using it to reduce
friction, to perform tedious tasks, or
just to understand a problem, organize
information, and plan a document that
they can share.
So, that makes Codex helpful for
researchers, educators, operators in
industry, small business owners,
leaders, knowledge workers of of all
kinds. Um and today I'm joined by
Thibault.

[00:01]
Thank you for coming. Of course. Uh
Thibault is the head of Codex at OpenAI
and he's going to help us understand
where Codex came from,
and what the team is learning from
people using this tool, especially
non-technical users, and how folks can
begin to use it outside of coding. So,
Thibault, great to have you here. Great
to be here. Yeah. Um well, let's get
started. So, to ground this, Codex was
created as a tool for developers. Um
maybe you could tell us when did Codex
first launch and what problems were you
and the team trying to solve at the
beginning? Yeah, so the journey started
a long time ago. At OpenAI, we've always
been fascinated with uh helping
just figuring out like how we can create
very useful models that would then in
turn help us, you know, also like
accelerate the development. And, you
know, one of the grand challenges for a
while has always been uh coding.
And being able to code at the level of a
prolific software engineer. That was
like a grand challenge um like roughly

[00:02]
like 2 years ago when we started on this
journey. The first public version of
Codex was something that we now refer to
as Codex web.
It was this idea that we would have
uh
an entity running in the cloud
accessible over a web interface. You
would put your task in there. It would
go and look at the repository like a
code repository that you have. It would
figure out what the right set of changes
were in order to fulfill the task and it
would open a pull request on uh GitHub.
So it was like fully isolated fully
packaged. You would just state your
intent and then you would receive like a
code change at the end. And that was
like the entire thing that we shipped.
That was like roughly a year ago. What
we found was um it was a little bit too
high friction. Um it was too hard to set
up. And then also a lot of developers
just have you know a beautiful setup on
their own computer. And you know you
need to do go and like reproduce all of
that on our own cloud environment setup.
So the friction was too high. Um the
models were also not at the level where

[00:03]
they would you know get it right all the
time. And so it was kind of like hard to
iterate there with the model. And we
shifted our approach after that which
I'm glad to go into. Yeah great. So so
you were building a tool for yourselves
and it sounds like there was a pivot to
where you realized it it should work on
everybody's machine. Locally. That's
right. We realized that doing this on
our own cloud machines and asking
everyone to just configure it there was
too difficult because the models were
not yet at the level where it was
reliable for long-term horizon tasks. It
was just not working. When did you first
see people using it for tasks outside of
coding?
Oh that's that's been um more of a
recent shift in the last last uh six six
uh months I would say ever since we
released GPT-5 we've had that step
change in like generality and
reliability for general-purpose tasks I
would say. Around 5.2 as well, where it
became more reliable for long horizon
tasks. And then, one thing to realize as
well is like even for software engineers

[00:04]
and technical people, like the majority
of the day is not actually coding. The
majority of the day is like looking at,
you know, tickets, prioritizing, having
discussions around, you know, what how
how we should actually solve problems,
>> Mhm.
deciding on like the architecture,
solving, um, you know, like bug reports,
investigating bug reports, and figuring
out, you know, whether it's actually
true, whether it's a user problem, where
the problem actually is, dealing with
outages, and you know, being on call,
and then, you know, just like general
like having an understanding of the
systems, and doing a lot of information
gathering. I would say like maybe, you
know, software engineers spend like 20,
30% of their time actually coding.
[clears throat]
Uh, and so, what we saw is like a lot of
the people who had adopted Codex were
already, you know, the technical ones
were just using it for their day-to-day
work.
>> Mhm. Uh, and then, you know, it was
obvious that this we were holding sort
of like a technology that was like much
more powerful, and that we wanted to,
you know, was yearning to be useful for,
you know, Mhm. at scale, you know, for

[00:05]
for the entirety of the society.
>> Mhm.
>> [clears throat]
>> So, it sounds like
to be a software engineer, you have to
do a lot of things that aren't coding.
>> That's right. And and people were
dogfooding. They were using their own
tool to do these to do these non-coding
tasks. And in order to be useful at
coding, we were, okay, you need access
to more context. Maybe if you have
access to, you know, all of the
information that we have in Notion, you
know, information that you have in
documents, um,
then actually we saw that the agent
would become more useful at solving the
task.
>> Yeah. And then, you know, we were trying
to just make that more and more reliable
up until the point where now like the
majority of the tasks that are being
performed in Codex are actually
non-coding tasks.
>> That's really interesting. So,
it First of all, Codex was searching
code, and then you realized
it's also super useful to search a bunch
of documents and come back with
information. And obviously that's
something that all of us doing knowledge
work have to do. That's right.
So
So maybe
What is Do you Do you remember the first
moment when you were like, "Oh, this is

[00:06]
actually
going to be for everybody."
Right? When when that when the ambition
changed.
Yes, we were in the middle of a launch
for Codex and
Alexander
Americus, who is like the the lead
product manager on Codex, was was using
Codex to keep track of the state of
all of the changes that we were trying
to land Mhm. um in in in in the run-up
to the launch.
>> Mhm. And I had I had never seen someone
be as productive as Alexander at that
moment where it seemed like he had many
little Codex agents, you know, doing his
work on his behalf and chasing people up
>> Mhm. and then updating a document with
the latest state of things of like, "Oh,
you know, it's like we actually still
need to polish like this specific
feature. We have this user feedback. We
have that." And it was So, it was
coalescing all of this information from
all the user feedback that we have, the
information from the developers, and
keeping like a plan, you know, neat and
up-to-date while Alex was having a
discussion with me. Um and you know, I

[00:07]
felt like, "Wow, you know, it's like
we're really changing everything here,
not just software engineering." So So,
in the world before Codex, Alexander
would be either himself digging through
Slack channels or documents or GitHub
PRs and just like everybody like spend
so much time with coordination and then
you saw he had somehow delegated that
really time-consuming work to these
tools and they're doing it while he's in
a meeting with you. That's right. Um
Our models are very good at genera-
gathering the right context and
summarizing as well. And so, that's a
strong use case that we see. And he was
doing that and then also using it to
chase up information. So, we have it
connected to Slack. It's able to send in
to send messages. The Codex agent can
send messages to people to, you know,
also ask like what's the latest status
on, you know, this thing and so doing
all the chasing on behalf of Alexander.
Chasing takes so much time. So so So
there's Alexander. He's one of the most
productive people you've ever seen. He's
using Codex in this way. What's the

[00:08]
ripple effect? Like what's the
in concentric circles around the people
around him, the team, what gets shipped?
The what The ripple effects that we've
seen is
engineers have been greatly accelerated
and are now building faster than ever.
Adjacent jobs are are changing like the
role of the designer is changing, the
role of like the product manager is
changing and then, you know, we looked
at how can we accelerate and and
um give them also the means to, you
know, just be more productive.
And then we saw bottlenecks shift to
communications and marketing
where
we were suddenly producing so much work.
Um and you know, it was a challenge to
sort of like
tell the world and, you know, keep the
story coherent and um so the bottleneck
was shifting to other departments at the
company. Hm.
>> [clears throat]
>> So OpenAI is shipping really fast. Do
you
would it be possible without Codex?
No, I don't think so. At this point
Codex is critical for us. Yes.

[00:09]
>> Do you think other companies
>> with 10 times more engineers. Hm. Do you
think other companies are similar enough
to OpenAI and like the problems they're
trying to solve for the world that they
can follow a similar playbook?
Yes, I think now we the state of the
technology is uh
at has reached a point where these
agents are capable of very general work.
Um there's really many things, you know,
that you can do behind your computer
that the agent isn't able to also help
with.
And so, you know,
a lot of like, you know, the work that
needs to go into like preparing a
presentation to, you know, align, you
know, stakeholders, for example,
gathering context on public perception,
doing some marketing research,
organizing it's used a lot in our
finance department. Sarah Friar talks
about this a lot that she organized the
latest fund raise with Codex with the
help of Codex and it was a great
accelerant there as well. And so there's
this beautiful generality to it.
And it's evolved like you know, much
more to like it's not for generating

[00:10]
code. It's just to perform general
purpose tasks really. Mhm. So you
mentioned that roles are changing.
What kind of changes do you see?
The change that I see is that
everyone has to deal with
things moving much more quickly
uh and adapt much more quickly as well.
Um hard hard problems, things that used
to take days now maybe take like a
couple of hours.
Across the field we're seeing this in
science, we're seeing this in
engineering, but we're also seeing this
of like
you know, I would have expected like
doing an in-depth marketing research or,
you know, analyzing the public sentiment
around a new feature, you know, that
would have taken a lot of time to go and
like find all the sources and summarize
and then
uh condense it in a way where, you know,
like different people could consume
that. Now that's that's just really
being compressed to like a couple of
hours of work and, you know, being

[00:11]
completely automated away.
It does mean that everything is slowly
like moving much faster as well and you
need to adapt to things, you know, just
the the the pace having picked up.
People are able to do much more by
themselves as well and, you know,
there's something delightful about that
too. It's like it's very empowering. And
so maybe before you're like, "Oh, I need
to go and talk to someone about this." I
don't know, you can just do it. Um we're
seeing this a lot on uh data questions,
you know, within within companies where
it's like you have a question about,
"Oh, you know, how successful are we in
this market?" Um you know, are we
growing uh in India? Um, you know, what
what's happening in Korea? And then now
everyone is just empowered to ask
critics the question of like, "Hey, can
you pull up the dashboard? I don't
really know where it is, but I go figure
that." And then you can go and like dig
into, um, you know, all the details of
the business. And you don't need to go
and talk to like data analyst teams.
Like you can leave them alone. They can
do more interesting stuff than answering
your, you know, little questions. Yeah,
I I remember the days when data analyst
teams had long queues cuz they're a
shared resource of things they owe to

[00:12]
all the other teams. And as long as
those other teams have access to the
underlying data, that's very often they
can extract insights by themselves. I
feel like we're in this historical
moment where it used to be that the
people who had problems and the people
who built solutions were two separate
groups of people and the conversation
they had about the product were really
long and you you eventually got to
something that was kind of okay, but you
couldn't push it further because nobody
had time. And now now like this the
person who has the problem can build the
solution very quickly and iterate
through the changes they need. Yeah,
that's why we have UX designers as well
on the team. They're pushing code.
Uh, they're making changes. They they're
in there with the developers, uh,
shaping the product as they want to
like, you know, to kind of bring the
best out of it and create an amazing
experience. They don't have to go and
like convince, you know, the engineering
team, you know, to prioritize like, you
know, what the engineering team probably
feels like, you know, fairly minor
changes, but, you know, for our amazing
designers, you know, they're like, "Oh,
no, this is this is like this really
elevating the craft and the experience,

[00:13]
you know, for millions of users out
there." And so it's very empowering to
them, too. It feels like we're kind of
in this era of home-cooked, personalized
software on so many levels.
Yes, it feels that this is the wave
that's coming where everyone will be
able to have their own personal software
and maintain [clears throat] it and it
just does exactly what you need it to
do. Yeah. You you were telling me before
we started about something you built for
yourself that visualizes some data. Do
you do you want to do you want to share
that with Yeah, sure. I just It's just
really a fun uh, exercise. So, I have it
on my screen here.
And [snorts] I'm in I'm in I live in San
Francisco. So do you, I think.
>> [laughter]
>> I think the price of bread is
uh outrageous in San Francisco. I moved
from Europe. Um and um so, I was like,
"Hey Codex, can you find like the best
loaves in the city and create me a
spreadsheet uh so that, you know, I can
understand like where are those loaves,
uh where should you buy them, and uh you
know, what's the associated price?"
And so, it went and it worked for 5
minutes and it created this uh this

[00:14]
spreadsheet, which you can see here. Can
we see that? Can everybody see that?
Great. Um and so, you can see you have
Jane the Bakery, you have Arsicault, you
have Tartine. It has found like the
different loaves, a little description,
and the price. So, it seems like if I
want to go and find a good loaf of
bread, the sourdough loaf, I should go
to Neighbor uh Big House, which is in
Dogpatch. Mhm. And then, I was like,
"Okay, it's great. I have the
spreadsheet." I could have It traded on
the spreadsheet and asked for more
information, but instead, I wanted to
consume it in a bit of a more of a
visual way. So, I said, "Hey, how about
you create me a webpage?"
Um and so, it did and it just put all of
these on uh on a map here so I can
uh just And this is just really personal
stuff that was created for me. This took
4 minutes for Codex to just generate.
>> I can go and I can now click around and
uh I could probably ask it to show me a
picture of these loaves of bread as
well.
And this is just
Yo, this was just done like in in in in
10 minutes. I didn't even look at it. It
was just a single prompt for me. And

[00:15]
then, the way that I like to engage uh
with Codex, I would like to
um you know, show you I can I do
everything over voice. So, "Hey, I'm in
San Francisco. I'm really into bread. Uh
I want like a map of all the loaves uh
the loaves that I can buy and um just
pre-structure it uh with a little
explanation of uh where I can buy it and
like the price of the loaf.
And then I don't even need to type
anymore and it's just going to go and do
that. Um
and then I can do go and and and and and
just like do other stuff on my computer.
So this is not a thing where, you know,
I'm even, you know, actively spending at
the attention on it.
>> Mhm. So you're saying anybody can do
that if they care about some data, they
can be and they have access to it, they
can basically make a website, analyze
it, visualize it, share with their
friends, family, coworkers.
>> Uh and and we used to talk about writing
code. It seems like such an anachronism
now. Now you're you're kind of speaking
code, right?
It's it's using code under the hood, but
it's more of a tool
>> Yeah. for the agent. You don't even need

[00:16]
to know about it. Um it it's just, you
know, it's editing and creating
spreadsheets and documents and slide
decks for you. It's creating websites
for you. You don't need to understand
what's, um, you know, how it how it
actually like performs its work under
the hood. It's just using code as a tool
and this is why there's this beautiful
generality to it.
>> Yeah. So So in the old days, if you had
the skills, this might have taken you a
weekend
to to create something at at college or
something like that.
>> quite a bit of time to go and find all
that information.
>> Yeah. Right. And and now it's just an
instant and then if you don't quite like
it, you can just tell it to change it,
right?
>> That's right. If I'm like, "Oh,
actually, you know, I wanted to
you know, do the same but for coffee."
Mhm. Um
"Hey, uh do the same analysis for
coffee, um, not just bread."
That's it. That's all I need to do. It
will go and work with it minutes and
it'll end up with like likely will end
up with, um, you know, a website just
about coffee in San Francisco. And
you're looking for you're optimizing for

[00:17]
price and quality, right? It's actually
more complex than just give me cheap
bread. Yes. Yes. So you you can express
your own preferences,
um, you know, Codex will just go and
like take that into account and, um,
just really work to satisfy, you know,
your your your prompt. Right. So it it
gets the data, it visualizes the data,
it gets you to an insight about the
world, then you can make a decision to
suit your needs, which is kind of like
the universal loop we're all in in our
lives. How do I actually decide, make a
better decision Yes.
>> to reach my goals. Yes. And this can be
very simple, this can be like as
complicated as, you know, like the same
process was used for the latest, you
know, fund raise at OpenAI. So, it's
it's
it's just Codex, it's just in
capable of like the smallest things and
then the most complicated things
>> as well. Yeah. Amazing. So, so are you
now using it like Alexander? Are you are
you kind of coordinating and
orchestrating things?
>> You can see here in my uh
sidebar is this is before we started to
talk. I fire uh off like uh you know,
little tasks like all the time like you

[00:18]
know, maybe over a hundred different
tasks like per day that I just like hand
off to Codex and it just goes and like
does it for me. This goes from like
organizing my desktop files, uh you
know, managing uh compu- the compute
fleet, um helping me understand
uh how the on-call rotation is doing and
like how the engineers are doing,
helping me understand, you know, the
launch schedule that's coming up uh and,
you know, flagging anything that's like
at risk that I maybe I need to look
into. Um I use it as a little chief of
staff where
uh and I I run this every day. So, for
example, you can do a little automation
and like go through Gmail,
uh Notion, calendar,
and uh flag um
and give me give me a summary
of my day
and flag anything uh that is at risk.
And then I can say, "Okay, like do this
daily.
Um
do this daily at uh 9:00 a.m."

[00:19]
And then, you know, I can just go and
schedule that and then it will run it
and then I will find it in my inbox um
you know, at 9:00 a.m. every day. So,
it's like you've got your own chief of
staff. Yeah. Hey,
do you don't forget to do these These
are It's It's even helping you
prioritize. And that's right. It's
helping me prioritize. It's helping me
spend my attention where it matters the
most. It's and it's helping me also by
you know, I don't have to go and like do
the small things.
You know, that would otherwise just take
me time and maybe I would never get to.
What were the things that annoyed you?
Like most hideous things
in the pre-Codex time that you spent
hours every week on?
Um the thing that annoyed me most was
like I would not do certain things
because I felt like oh, I don't have the
time to do it myself, but I need to go
and annoy someone.
You know, to ask for like you know, this
information. Um but you know, I felt
like it was you know, maybe not
important enough to go and you know, put
this on someone's desk and be like you
know, hey, can you can you help me with
this question? Um so now I feel like you

[00:20]
know, I can just you know, get the
information that I want, have the little
reports that I want. Um I can build all
sorts of personal software that you
know, I didn't have the time to do. So
you know, it's just like a really uh it
gives me joy because um it it is doing
all the little tedious, you know, things
that were like a very manual on my
computer before. And now I'm like okay,
I'm just in the Codex app and um it's
doing all these things for me and I can
just focus on you know, the things that
I feel I actually want to think about.
Yeah. Uh so I know people often talk
about it as like
this would have taken weeks, now it
takes seconds, but it actually feels
like this never would have happened. It
would have taken infinity time because
we never would have gotten to it. And
that And that was actually
>> of that. There's a lot of that. It also
sounds like
are you enjoying your job more because
these things are getting done that used
to annoy you? Yes. Yes, I am. There's
like so much that I don't um
you know, like for example,
every day I'm like oh, you know, what's
the latest news?

[00:21]
Um and there's like
it has very personal instructions for
the kind of news that I care about.
And so,
what that is an example like I would
have never
received such a report about the news.
Um
and it gives me great joy like to just
like
read this in the morning and, you know,
feel a little bit more informed.
A lot of things on um when it comes to
like investigating, for example, we have
like a bug report
uh from a user. I see it like on Twitter
and it's like, "Oh, you know, that that
is a bummer because I would have usually
put this as like this is like a low
priority thing. This is probably
affecting like three users on the
planet. Um [laughter] this doesn't feel
like a thing." Like now, I'm like, "Oh,
let's just put this in Codex and you
know, it will get it done." And, you
know, I can feel like, you know,
just much better because I don't feel
like, you know, things are falling
through the cracks anymore.
So, it's reducing the cognitive load for
me.
>> Yeah. I I
It makes me think that this is actually
a tool to address burnout and

[00:22]
over-information overwhelm. Like people
we we're all kind of surrounded by tools
that are supposed to help us, but in the
end we're kind of trapped within our
tools. And and this is a thing that's
kind of
liberating us as a tool. Um and and
maybe decre- like so many people,
teachers, doctors, so many people feel
burnout and overwhelmed because they're
trapped in those tools, manual data
entry, that sort of thing. And do do you
feel like
it almost feels like our relationship to
tools is changing. Is there a
fundamental shift in how we relate to
tools?
Yeah, to me that's the promise. The
promise is you have
a trustworthy partner almost that you
can go through and, you know, will do a
lot of work on your behalf to a level of
trustworthiness where you're like, "Hey,
it's like if I delegate something to
you,
um you know, you'll you'll get it done.
If you don't you don't get it done to
the level of satisfaction, you know,
you'll flag it to me, but I know that it
will be done well. I know that it will
done be done, you know, maybe to a level
of quality that's superior to like now

[00:23]
if I were doing it myself. I can also,
you know, trust this partner to
um shield me from like a lot of the
noise and you know, to flag important
things, you know, when in in a timely
fashion. And so, I don't have to go and
you know, consume like information in
like, you know, seven different apps and
be bombarded by things that, you know, I
don't actually care about. Um what I
imagine the future to be like is, you
know, I don't even have to read my
email.
Um
I maybe I just have, you know, I have
like my little personal agent that is
just like reading my inbox for me,
flagging me like whenever there's
something really important, asking me
for input, and then just you know, doing
the work. So, you don't have to search
for needles in a dozen different
haystacks. Needles are kind of arranged
in a newsletter. I can I can say like,
here are my goals for today.
Help me out, manage everything else.
And trust that that will happen. That's
amazing. You must have seen over the

[00:24]
past few months like the
what you can trust this tool with is
changing. It's like you mentioned time
horizon, like the time it takes to do a
complex task. That's that's changing.
Yes, so we we actually launched a a new
thing there that is like more of an
advanced feature, uh which is uh {slash}
goal. So, in in Codex you have {slash}
commands, uh which allow you to uh for
example, enter like different modes.
{slash} goal allows you to enter a mode
where you give a long-term to Codex, and
it goes and is really relentless at it.
And so, for example, you can give it the
goal of solving a very hard mathematical
problem, and it will go at it for hours,
maybe days, maybe weeks until um it has
decided that it has satisfied the goal.
Um we're seeing it being used to do like
amazing things on like improving the
performance of programs, rewriting
entire programs from one language to
another.

[00:25]
Um it's used in science problems as
well. I've seen like really cool
breakthroughs on uh mathematics and and
and physics breakthroughs with it.
Um
and uh this is fascinating to me because
maybe like a couple of months ago we
were oh you know we were this is
exciting it's working for 10 minutes.
Now we're talking about you know agents
working for like weeks on like the
hardest tasks. Right. Right. Sometimes I
think genius is just the ability to
think about the same thing longer.
Yes. I mean if you know if you have
infinite time like probably like
uh you know a sufficiently smart human
would be able to come up with everything
that we have done you know in humanity
so far. So I feel threatened to me. So
so goal you can use that in the in the
CLI can you use that in this Codex app
that you're showing us right now? Yeah
it it's it's it's um
it's coming. It's not yet uh launched
but it will be available. Okay. We'll
we'll let the community know when
[laughter] when goal is available on all
surfaces. Okay. Awesome. So so it's
running for days and it's just going
going going in the background and it

[00:26]
comes and then it comes back and reports
to you hey I'm I'm done or I'm I'm stuck
on something. Mhm. Yeah. That's right.
Um and where the future is headed I
think is where it just it's not going to
stop. Um where [clears throat] you're
just going to have an agent that runs
like 24/7 and you know does useful
things for you and gets [clears throat]
steered along the way.
>> Yeah. Right now it's like very
turn-based. Yep. Uh where you know you
go and you have a specific task and
you're like oh you know it's like I want
you to go and solve that task. Like go
find all the loaves you know in San
Francisco and like tell me the price.
That's great. Solving tasks is super
important. Um
goal-oriented task solving is also a big
unlock um in terms of like the value
that you it can create for you.
But the next step I think is just it
just runs continuously and it does
useful things whether you instructed or
not. And it may be at some point like
I've done all the things that I think
are useful. I'm just going to sleep for
a little bit until I talk to you. Um but
it's not like um it's not like it's just
working when you have like a very clear

[00:27]
instruction. Is there any trick to
specifying the goal you want it like how
do you make goals succeed?
Yeah. So, one of the one of the shifts
with agents
um
compared to
you know, maybe if if you haven't
experienced
you know, if you haven't installed the
Codex app and you know, it's like the
first time you're you're using it
just just explore a little bit. You can
engage um in a very chatty way about you
know, what it what it's capable of. Like
it it it is it understands its own
capabilities. So, you can just you know,
ask it like what it can do.
But a good trick is to be precise on
helping it evaluate its own success.
And so, if you're able to describe what
good looks like
and you know, what's solved looks like
and what you want to see you know, at
the end of the completion of the task
then you know, Codex will be able to
sort of like
understand whether it's doing well and
whether it has completed the task or
not. So, can you put can you put a

[00:28]
number on it? Can you be precise?
Yeah. So, if for example, you know, you
can say like hey, I want uh I'm
presenting
my work.
Um I would like a slide deck. You know,
I would like it to have like 10 slides.
The first two slides I want it to
contain this kind of information. The
next six slides I want it to you know,
just really go into the meat of the
problem and do a technical breakdown and
then I want you know, two slides at the
end with open questions and Q&A. And if
you're a clear about it and you know,
you're you're specific about what you
want as the output then it's much more
likely to succeed. So, very similar to
what you might do with an assistant or a
lieutenant.
>> That's right. Yeah.
>> That's right. Okay. So, we take
questions from the community
and I'm going to read some of those. So,
we've got one here um
from and excuse me if I mispronounce
this, Gal Gen Karya,
principal engineer in financial
services, um
is asking what would make non-coders
move away from ChatGPT to Codex?

[00:29]
I think it's going to be an evolution
and it's really
I I don't expect that
um
you know, everyone will want to move to
Codex, but it is a nice complimentary to
ChatGPT.
Um
what I recommend to use it for is to do
things for you.
Um so, anything that you know, where
it's like manipulation of files on your
computer,
um running things on like automation and
doing things in the background every
couple of hours, you know, you can do
that Codex,
um
you know, and and ChatGPT for me is
still I go to for like, you know, quick
answers.
>> Mhm. Yeah, I I remember the old days for
me, I would be copying and pasting code
from ChatGPT into a file or a terminal,
but you don't have to do that anymore.
The copy and paste era is over. Yes,
Codex can just like work on the code and
the data, right?

[00:30]
>> Yeah, and if you have you know, if you
have like a a file on your computer, you
have pictures on your computer, you
know, just tell Codex like, hey, you
know, use this file, read it and it can
just do it. You don't need to go and
like, you know, click on it manually and
yeah.
Okay, we've got one from Anastasia
Chueva.
What do you think becomes the biggest
bottleneck in enterprise adoption
uh and then the choices are model
capability, human trust, or
organizational process design?
I don't think it's a capability thing.
Uh the capability's there, that's not
what what's holding back adoption uh in
enterprise. I I it's primarily, um,
trust and
uh, for trust, it's it's about is it
safe and is it secure?
Um,
you know, if if you have an agent just
run around, uh, in in your in your in
your company and like, you know, maybe
delete sensitive files or, you know,
upload information and you know, send an

[00:31]
email that contains, um, you know, an
exfiltrates like information that it
shouldn't.
>> People are going to use it.
>> That's that's that's terrible. Um, so
we've been thinking a lot about that. By
default, agents run inside of sandbox
with like tight controls, you know,
exactly
that they are able to only access, um,
you know, a specific portion of the file
system. And so, you know, like you can
constrain it to a folder. You can
disable network access. We're giving a
lot of enterprise controls. I think this
is very key to continue to expand from
there. There's also investments that
we've done. It's on our alignment blog
post. Uh, we call this feature auto
review, where we have created an agent
that is capable of reviewing the actions
of the primary agent.
And the way it works is that it the
primary agent codex is incentivized to
do the work for you. At times, it might
take an action that is, you know, maybe
a little bit risky. And so, you have
another agent that sort of reviews every
action that it's taking and flags and
stops it if it's like a high risk thing.
And, you know, I expect like more
innovations like this will be necessary.

[00:32]
>> referee or an umpire. That's against the
rules. Yes, yes. And be like, "Hey, stop
right there. You know, this is like too
risky of an action. I would like you to
take like a less risky action."
>> So, just to help the non-engineers in
the audience, a sandbox, is that just
like a folder in like, in a file system?
Like, do you say, "Don't go outside of
this folder. Just do things within
this?" Yeah. So, that's that's right.
It's, um, it's similar to how, um, you
can think about, you know, if you're in
a company like,
oh, you know, maybe you only get access
to information for one part of the
organization that you're in.
Um, and you know, people have like
different silos. This is like the
equivalent of a sand sandbox for an
agent. You can sort of like restrict
what it can have have access to and like
the set of actions that you can take.
Yeah. And And so a rule might be you can
read this data that IT gave you access
to, but you can't write back to it. You
can't delete it. You can't like change
it. The data is preserved, but you can
kind of extract and analyze it. Yeah. So
yeah, for example, you could say, "Oh,
you can only have read access to
something." Yeah, [clears throat] cool.
Um okay, we got one uh
Jason DeLuca, owner and principal

[00:33]
consultant Crossing Point IT Solutions.
What are non-developers doing that makes
Codec Codec's work well for them? What
habits separate the people who are
getting results from the ones who feel
stuck?
Um
I think what I've seen is
engaging with creativity and talking to
others who have um seen success. It's
just I I
I am surprised myself at like some of
the use cases.
Um
So being part of the community. Being
part of the community is great.
Um the second thing is
trying to engage with it um with
precise instructions instead of uh you
know, being being quite vague about what
you want.
And so putting some effort into like
just really being like, "Hey, you know,
this is
this is um this is precisely the outcome
that I would like." We talked about this

[00:34]
a little bit, but I would just really
consider, you know, agents to be, you
know,
someone new who just joined the company
has like no context about you, doesn't
know what you like, doesn't know about
your preferences. Like how would you
engage with them? You would probably be
uh you know, quite uh
um
you you would probably give them quite a
bit of information about like where to
find things, how to think about, you
know, relevant documents to read. Mhm.
Uh and so often people like forget about
that. Uh and then the the third thing is
connect a lot of like different sources.
So, we have plugins for like almost
everything now. We have more than 100
different plugins. You can collect, you
know, your calendar, docs, you know,
notion. You can connect like your
favorite tools. The more you give it
access to your like tools and
information from your world like the
more useful it will be. Mhm. So, the
more and better context gives you more
and better results. And some of that
context is in your head. And so,
[snorts] it's your goals. It's things
you've experienced that are not in the
docs and you and and you you got to be a

[00:35]
good boss and actually share some of
these things. That's actually
interesting. So, I
I have taken now the habit of like
writing everything down.
Um so, a lot of like my own thoughts, my
goals, it's like it's it's actually in
files on my computer and uh Codex has
access to it as well so that it can like
align itself a little bit more. So,
obviously yes, if it doesn't have access
to, you know, it doesn't have access to
your brain so
it can't read your mind.
So, you have to verbalize it something.
>> Yeah. Neat. Okay, we've got one more
from the community. Daniel Green, uh
Kansas City AI Collective. What are your
favorite real-world uses of computer use
so far, especially outside traditional
coding?
Um
I I use it for shopping.
Um where it it will it will go and um
order stuff for me so
uh I use it What I do is on my personal
computer I have Codex do meal planning
and then um
and then it will go and actually like
order the ingredients. So, that's the

[00:36]
thing that I use it for um
another thing that I've seen uh people
use uh it for is uh it's all it's it's
almost impossible to find like which
settings
you know, which settings pop up to open
up, you know, like beta on Windows on or
Mac OS to to do something on your
computer. And so, it's just being like,
"Hey Codex, um I'm trying to
uh change this on my computer. Just Can
you show me how to get there?" And it
will go and you know, it will actually
like you know, take you around and like
you know, click on the right things. Um
and then you know, you learn something
about your computer.
Um sometimes as well, um
there's like something that you want to
kind of want to adjust, um
you know, some slides or integrate like
an image and then your computer uses
that for that as well. For technical
people, it is very, very useful for QA.
Um where, you know, you Codex can then
like open the app and click around and
test that it actually functions. Yeah,
amazing.
Um okay, let's see what we got. Sai Sri

[00:37]
Hamsini in at AI/ML engineer at
AdeptMind. What are the biggest mistakes
people make when prompting Codex? I want
to know the answer to that one.
>> [snorts]
>> Oh, um
As you progress in delegating to Codex,
it can be
at some point I see
it becoming very tempting to just
delegate everything including your own
understanding. Mhm. [clears throat]
And not
using Codex enough to
elevate
your own understanding of the problem.
Um
if you just if you're just like purely
like, oh, I'm going to delegate
everything, at some point, you know, you
might realize like you don't actually
understand, you know, what's happening
anymore. Um and then, you know, you've
kind of like, you know, you're not as
grounded and you're, you know, maybe
going to lose a little bit, um of your
your productivity and like that's not

[00:38]
good. So,
spending more time to also gather
information and have it like explain
things to you. It can draw diagrams like
images V2 is like amazing at this, um
because it's very good at rendering text
too. And so, I see people use it all the
time to go and read, um you know, read
like
um our plans for launches or, you know,
like
and things from marketing, or like parts
of the code base, and then create images
to like, you know, just explain a
concept to you if you're trying to learn
something. So, I would say like the
mistake I'm seeing is just like too much
delegation, and you know, not enough
like using it to just helping you
understand. I totally agree. Whoever
does the work does the learning,
basically. So, I I built myself a little
skill, a tutor skill, flips the tables,
and it asked me to give
it answers about what it's taught tried
to teach me already, so that I can force
myself to do that learning of active
recall. Yeah, super cool. Let's see,
what else do we have? Um
Why does Codex matter beyond software,
and and where do you see these use cases

[00:39]
going next? So, we're really talking
about the future. We've talked a lot
about how things are changing up till
now. I think we're the future for a lot
of people, but there's a future for us,
too, and for everybody together.
Yes.
So,
fundamentally, what we're building is a
very general and very powerful agent
that
if connected to the right sources of
information, and you know, with
increasing access to all the information
in the world, and given the ability to
take actions upon the world, we'll be
able to do pretty much anything that you
know, you allow it to do.
And so, the promise there is just
incredible value creation.
Um
A lot of things that, you know, would
have taken like prohibitive amounts of
of time, you would never have gotten to,
or like just like too hard to accomplish
for humans, will become possible.
Everyone we will distribute this
the the intention is to distribute this
as like a broadly broadly as possible,
and to give, you know, the entire world

[00:40]
access to these capabilities, and these
agents.
And so, it's just really about, you
know, just lifting, you know, the the
the amount of things that people can
just, you know, even dream about
accomplishing. Yeah. Yeah. I've spoken
everybody from
prize-winning physicists to
industry project managers, they've come
to me and said, "I had a stack of good
ideas and I've been able to start work
on them and they never would have been
realized in the world before. It feels
like we're entering a golden era." It
feels like it. Yes. Yeah, amazing. Okay,
well, Thibault, this was a great
session. Thank you.
>> Thank you. Um
I and I just want to follow up uh
Thibault mentioned that having a
community will help you learn how to use
Codex better and I just want to make the
point that Open AI Forum is a community
where people are using Codex and we can
teach each other and support each other
in learning that better and and I hope
everybody in the session today will
continue to engage because this is a
place where skills are modeled and
transferred uh so that you can bring
this tool into your life in new ways. Um

[00:41]
the question we tried to answer today is
is why um why should people who don't
code care about Codex? I hope we
answered that. I'd also like to make the
point that although the word code is in
Codex
Codex actually means book, which is
something we all are used to,
right? So so so Codex is a more general
word than just code. Um but I but I hope
this conversation um made that answer
concrete. Uh
Codex is uh useful for developers, um
also useful for people anybody knowledge
workers, people working with information
go you know, searching for the
information they need, the needles in
the haystacks, uh struggling to make
sense of it, data analysis, visualize it
with kind of instant visualization like
Thibault showed it showed us um and
prioritization [clears throat]
and performing complex tasks in in the
background of their lives. So, we think
that Codex is uh bringing those powers
those superpowers to lots more people
and we're really excited about what
that's going to mean for our economy and

[00:42]
society and their businesses. Um
as we close I'd like to ask everybody
listening to think of one workflow in
their life or in their organization
where code Codex might help. Um and that
could be a research brief or a plan or
an onboarding process or reporting or a
decision memo. And just give it a try
because uh you've heard a lot from us
today, but the the clearest message is
just going to be your experience with
the tool. Right? You don't have to trust
anybody else about it. You can just
experience that tool. It's there,
available to you.
So,
thank you again, everyone, for being
part of Open AI Forum. Uh we appreciate
your time and your curiosity and the
thought everybody brought here, and
especially the the folks who got their
questions in. Those were great
questions. So, thank you. Um we have an
upcoming event. It's
Tuesday, May 26th, "How AI Could Detect
and Prevent the Next Pandemic" with the
Gates Foundation. We're super excited
about that. So, thank you, everyone, and
thank you, Tegan.

</details>
