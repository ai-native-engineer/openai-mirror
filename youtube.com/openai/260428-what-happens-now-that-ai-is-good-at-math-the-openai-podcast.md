---
title: "What happens now that AI is good at math? — the OpenAI Podcast Ep. 17"
channel: openai
url: https://www.youtube.com/watch?v=9-TVwv6wtGQ
youtube_id: 9-TVwv6wtGQ
published: 2026-04-28
duration: "43:29"
captions: en
---

# What happens now that AI is good at math? — the OpenAI Podcast Ep. 17

[![What happens now that AI is good at math? — the OpenAI Podcast Ep. 17](https://img.youtube.com/vi/9-TVwv6wtGQ/hqdefault.jpg)](https://www.youtube.com/watch?v=9-TVwv6wtGQ)

<details>
<summary>자막: What happens now that AI is good at math? — the OpenAI Podcast Ep. 17 (43:29)</summary>

[00:00]
Hello, I'm Andrew Mayne, and this is the
OpenAI podcast.
Today, our guests are researchers
Sebastian Bubeck and Ernest Ryu,
and we're going to talk about math,
how it went from almost laughable to
Olympiad level,
and why you need math to reach AGI.
The progress of the last few years has
been nothing short of miraculous.
We will be able to have LLMs be able to
solve problems
that require more than 50 pages of
thinking.
Mathematics was just the perfect benchmark
to see the model making progress during
the last four years.
Sebastian, Ernest, I'd love to know more
about you.
So how would you explain your roles?
Yeah, sure.
So I have been working in mathematics for
almost 20 years now.
I used to work in optimization and theory
of machine learning.
I was a professor at Princeton for a few
years before moving to Microsoft.
And now I'm a researcher at OpenAI.
And in the last few years,
I've been really trying to understand how
AI can help mathematics and to really

[00:01]
evaluate the progress that we're making in
terms of solving difficult math problems
with AI.
Ernest, how about you?
Yeah, so I've recently joined OpenAI as a
researcher.
But before that,
I was an applied mathematician working on
optimization and machine learning theory.
And in my previous job,
I worked as a professor of mathematics at
the UCLA math department.
So I think a lot of people have this
perception that these models aren't good
at math, literally called language models.
And how has that changed? What's gone on?
Yeah,
I think the progress of the last few years
has been nothing short of miraculous.
It's important to remember that two years
ago, we didn't even have reasoning models,
let alone models that could prove, you
know, difficult mathematical theorems.
Today, two years later,
the models are able to help Fields
Medalists in their day-to-day work.
So really the jump is just simply
astounding.

[00:02]
And maybe if I can build a little bit more
on that,
something which is important to understand
is that everybody has been surprised by
this progress, including us.
So to tell you a story, a year and a half
ago,
I was at a workshop at a conference with
other fellow mathematicians,
and there was a debate that I participated
in on whether LLMs, scaling LLMs,
will help us resolve major open problems.
So this was a debate, you know, a year and
a half ago.
And the room was very divided.
In fact, they did a poll at the beginning,
and I think it was like 80% said no,
impossible that this would happen.
So then the debate unfolded.
And by the end of the debate, it was more
like 50-50.
So pretty good progress during that hour.
This obviously was just so wrong in
hindsight.
Like just mere eight months later,
the model was starting to be able to do
research level mathematics.
What was the breakthrough moment for you
realizing that there was a really good
intersection between AI and mathematics?

[00:03]
So summer of '25,
the big news was ChatGPT was able to
achieve a top human level performance
at the International Math Olympiad, a gold
medal performance.
So that was amazing news. And that
demonstrated that, well, at least for the
competition level mathematics,
the models are
very highly capable, only on par with the
top human high school contestants.
But, well, competition
problems are canned problems.
They have relatively short solutions
because they are meant to be solved
within a few hours. And they're not novel
because, well, somebody came up with it,
there's a solution. So it's not
research-level math.
So then I got curious, and a lot of people
got curious, can ChatGPT do research-level
mathematics?
And there was a lot of debate
online. And then I thought to myself, I
should try it on my own problems.
Maybe I'll try it for
myself and make up my own mind as opposed
to listening to what other people say,
because
a mathematician myself.

[00:04]
So I took a classical open problem in
optimization theory, which is a
branch of applied mathematics that I work
in.
And the question specifically is there's a
famous
algorithm called the Nesterov accelerated
gradient method.
And does this have this convergent
behavior
or is it possible that in certain bad
cases,
can there be a certain divergent behavior?
This question was genuinely open in the
sense that people know that in most cases,
the algorithm
behaves well, it's convergent, but people
really did not know,
is there a bad instance?
Does it, in the worst case, could it
diverge? The answer turned out to be yes.
And the way I
discovered it is I remember it distinctly.
So my bedtime for my son is 8 p.m. and
then I try not
to stay awake after midnight.
So I had four hours of usually evening
hours to myself if I want to
focus on something.
So I decided, okay, I'm going to spend a
few days working on this. So over the

[00:05]
course of three days, so that's 12 hours
total,
I interacted with ChatGPT on this
question.
It wasn't as simple as me just putting in
the prompt and getting a solution.
I played the role
of the verifier. I told whenever the model
made a mistake, I corrected it.
I also tried to point
the conversation into areas that I felt,
approaches that I felt were novel.
And after a while,
the proof, there was a proof and I checked
it.
I also asked ChatGPT to double check it
and it was
correct. And that's how this 42-year-old
open problem got resolved.
And once I got this
solution, I thought to myself, what would
be the most fun thing for me,
fun way for me to
publicize this because I could just write
a paper and that would be,
but that'd be less fun.
So I decided, let me go to Twitter and
talk about this.

[00:06]
but, well, I had a lot of fun. Yeah.
So it was, I think one of the earliest
instances of a genuinely open problem,
mathematical open problem being solved by
AI and yeah,
I mean, people ate it up and it was a lot
of fun.
It is interesting as you brought that up
that we've seen sometimes people said,
hey, I found
something cool or novel.
And then sometimes it gets torn apart.
Sometimes it stands up.
And going into social media can be kind of
scary,
but it sounds like we do need these
kind of feedback cycles.
I think part of the challenge for a lot of
us is we hear terms, you know,
we hear like
the International Math Olympiad and we're
trying to figure out like, okay,
what does that mean
from like a scale of a problem?
You know, I can understand addition,
subtraction, multiplication.
Could you give me an example of
understanding, like, where we went from,
from, like, you know, first ChatGPT, which
could kind of sort of use it,
then it could do math, it could use a
tool,
but then the model sort of implicitly
understanding that.
When ChatGPT, you know, just entered the
scene in early '23,

[00:07]
I started testing them.
I was very curious about how the model
would perform fair on sort of common math
problems.
So these would include math problems that
you would see in the high school level,
but also day-to-day math-ish problems.
So for example,
imagine a scenario where the three of us
went camping together and then I paid for
this, I paid for this, and then Andrew,
you paid for whatever.
And then we want to clear the ledger and
we want to split things evenly at the end.
Can ChatGPT do the calculations for us?
And this is moderately complicated if you
have like 17 items that we've purchased.
In 23, 24, and also in early 25, I
remember, the models couldn't do this.
Another example would be, I'm in, let's
say, in Korea,
Seb's in Paris, Andrew, you're in
California,
and want to set up a Zoom meeting.
What would be a good hour to do so?
Again, in early 25, the models couldn't do
this.

[00:08]
But then just suddenly things just
changed.
And I wasn't in OpenAI at the time, so I'm
not at all,
I'm not quite privy to what exactly you
did,
but suddenly the models started solving
IMO problems.
And then furthermore, it started solving
research problems.
And the way I sort of calibrate this right
now is that unless you are a professional
mathematician trying to discover new
mathematics,
If you are somebody who's, let's say,
a physicist or a chemist who uses
relatively complicated mathematics,
like differential equations, differential
geometry, things like this,
but you're not inventing new math,
then ChatGPT can do all of the math that
you would need.
So any basically user of high-level
mathematics from STEM can now use ChatGPT
to basically have their math taken care
of.
You want to exercise some degree of
caution, you know,
check whether things are right, you know,
run simulations just to double check.

[00:09]
The models can make mistakes.
But now any math problem that you would
want to solve, most people,
for 99% of the population, the models can
do it.
When I worked on the release of GPT-4, I
used scheduling as one of those examples.
And I could put three people into a
schedule and have it figure out time
slots.
But pushing it beyond that, that was
really hard.
Why was there a change?
So Ernest just talked about noticing all
of a sudden it got better.
Now we know one thing was tool used.
You could let the model use a calculator.
But something else happened with the
models themselves.
So going back to the debate that I just
told you about,
the framing was really about can scaling
alone,
scaling of LLMs alone bring you to solving
research breakthroughs in mathematics.
And
this is a wrong framing.
What we do at OpenAI, we do a lot of
research, innovative research.
It's not just about scaling the model.
So when you ask what happened, or when
you're asking what
happened middle of last year when suddenly
the model were able to solve math

[00:10]
problems, well,
a lot of things happen.
We do a lot of research and all of this
has to progress at the same time.
So I can't really point to a single
element.
But it was able to do it itself, though,
without the tools.
Yeah.
So I think it's really,
really important to just double down on
what Ernest was saying
about the progress and the scheduling
problems that the model wasn't able to do
back then.
I said that two years ago, we didn't have
reasoning models.
Well, think about four years ago.
Four years ago, so this is pre-ChatGPT.
And I remember Google came out with a
mathematics model called Minerva at the
time.
And I fell from my chair.
I was so impressed.
What was I impressed by?
That the model, I could give it the
coordinates of points in the plane,
and it would give me
a line that goes through those points.
Like when I say that, you know, now it's
almost hard to understand.
What are you talking about?
Obviously, a model can do that.
So I think we have kind of forgotten how
quickly things have happened.

[00:11]
And now, yeah, you know,
Ernest was saying that it's basically at
the point where unless you're trying to
invent new mathematics, it's kind of at
the right level already.
I would say we're already seeing glimmers
that even to invent new mathematics,
it's getting there.
Could you break down, though,
aside from somebody who's interested in
developing new fields of mathematics or
just making new proofs, what does this
affect everything else?
What is the impact of this going to be on
science?
What is the impact of the rest of what
you're working on?
Why is this really important and not just,
oh, cool, it does math?
So I think the, oh, cool, it does math
part,
what did matter as we were developing
those
models as a good way to benchmark the
progress?
The nice thing about mathematics is that
the questions are very clear,
non-ambiguous.
You know, everybody agrees on what the
question is asking.
So that's point number one.
Point number two, you can verify the
answer.
So once a model can give an answer,
everybody will agree.
Was it correct or was it not correct?

[00:12]
Although you can put a pin on that because
we will talk about, you know,
in research level, it's not that simple
anymore to evaluate.
But before research level, it's very easy
to evaluate.
So mathematics was just the perfect
benchmark to see the model making progress
during the last four years.
Now, we'd say we have kind of saturated
that aspect.
And you can ask, okay, now, okay, fine.
The models do mathematics.
We have understood.
What about the next steps?
And for the next step,
I would say that having our models be good
at mathematics is going
to be good for many, many other things.
And let me explain why.
A key feature of mathematics is that to
resolve a problem,
you have to think for a long time,
be it days, weeks, sometimes years.
So this long thinking, not only do you
have to think for a long time,
but you also have
to think consistently for a long time.
If at some point in your chain of
reasoning, there is a mistake,
this will kill the entire
argument.
It doesn't matter if everything after that
is correct.
If there is one single failure point,

[00:13]
the entire argument is destroyed.
So this property makes it that
this is what you want out of reasoning
models,
that if they make mistakes,
they will be able to correct themselves.
So we are hoping that this property
that they acquire through mathematics
will generalize to other domain,
which by the way,
is exactly the same thing with human
beings.
Why do we train human beings in
mathematics?
I mean, it's a very fun topic.
I love it.
We did it professionally.
Maybe we still do some of it a little bit.
But why do we train humans in mathematics?
Exactly for the same reason.
It gives you this kind of very logical
thinking.
Do we need to think about new ways to talk
about these discoveries?
Yeah.
So I personally view it a little bit as
part of my role to try to educate the
research community about the recent
advances.
because I have this dual background
of both being a former mathematician
and now working on the frontier of AI.
And indeed, like Twitter and social media
is a great place to try to explain what is
the progress

[00:14]
in particular because this progress is so
fast.
So, you know, for example,
maybe we can talk a little bit about the
Erdos problems,
you know, and some of the controversies
that happen around that.
So there was a first example.
So there was first, you know, Ernest
example
And there were a few other problems that
were solved.
You just want to explain Paul Erdos though
too,
just so I think people would love to know
who he is and why his problems are sort of
interesting.
Yeah, of course.
So Paul Erdos is one of the most prolific
mathematicians of the last century.
He has written, I think, 1,500 research
paper.
He was a very iconoclastic figure.
You know, he didn't have a house or an
apartment.
He was just traveling from one university
to the next,
trying to find new collaborators.
And every time he would go to a place and
basically ask questions.
He was very, very, very gifted at asking
questions.
Not all the questions that he asked were
interesting.
Let me just say that right away.
But still, it was very productive.
And the research community wrote a lot of
papers with him.

[00:15]
There is even this concept of an Erdos
number,
which is how far away are you in the chain
of collaborators
from having also a paper with Erdos.
My Erdos number is two.
I have co-authored a paper with someone
who co-authored with Erdos.
Wow.
Yeah, I'm pretty happy about that.
My number's three.
The joke was, you know, you could be on a
train ride with him.
And then by the end of the train ride,
you'd maybe work on a paper with him and
have your name.
Absolutely.
I think the two versus three basically
says something about our respective age.
That's actually what it says.
So anyway, so Erdos has, you know, all of
this problem.
And there is a very nice website by Thomas
Bloom,
who is keeping track of all the Erdos
problems that are still open.
So I think there is like a thousand
problem or something like that on that
website.
And Thomas himself has done the work of
trying to find,
he's an expert in combinatorics.
So he can kind of say, okay, this is open.
This is resolved.
This has some complicated status for every
problem.

[00:16]
Of course, he doesn't necessarily know the
answer to all of them.
So if there is a paper which is marked
open,
it is not necessarily true that nobody
knows
how to solve it.
But it is also a very interactive website
where people can go on it and, you know,
add comments to every problem and explain
whether there is a solution, et cetera.
So it's a very dynamic, great website.
So, of course, once we started to have GPT
be able to solve research math problems,
this sounded like a treasure trove of
problems to try our models on.
And we tried a couple.
And to our great surprise,
the model came back with answers to some
of them that were marked as open.
So we got really excited about this.
The first one, you know, that I tweeted
about, I don't remember when it was,
maybe it was in October or something like
that last year.
It was a deep literature search result. So
let me explain what that means.
It means that what GPT did is that it did
a vast literature search, trying to scan,

[00:17]
you know, thousands of papers.
And it found in some unrelated field, the
answer to the question.
Now, it's really important to understand
that it's not like in that, you know,
unrelated field, the person said, okay,
I'm solving an Erdos problem.
It was written in a completely different
language. It was different mathematics.
You have to do work to connect the two
pieces and GPT did that.
So that was kind of amazing. And this was
very ad hoc.
Like, you know, we just tried by hand
basically in the ChatGPT interface.
Once we saw that, Mark Selke, who is in
our team also,
decided to have a more systematic
approach of trying all of the problems.
And he tried that, and the model came back
with solutions to 10 Erdos problems.
And this was, you have to remember, at
that point, there was still, I think,
a very dynamic
discussion about whether those models
could go beyond the state of the art and
discover,
invent new mathematics.
So I got very excited about this result
and I tweeted about it.

[00:18]
And, you know,
it's kind of an infamous tweet because
people misunderstood it as kind of saying
it really found the solution to 10 open
problems that are very hard.
And the solution is completely new and did
not exist in the literature.
But that's not what happened.
It was connected, of course,
to the previous case where it is a deep
literature search.
So there was some, you know, feud with
Google about, you know,
with Demis about whether, you know,
this is the right way to talk about such
results.
But now the punchline is kind of amazing,
which is a few months later.
So again,
I said 10 solutions to open problems and
these were solutions in the literature.
And then the question is, can you find
solutions that are not in the literature?
By now, we have more than 10 actual
solutions that are completely new,
that are publishable in top journals in
combinatorics, completely obtained by,
you know, some by ChatGPT and some by our
internal models.
So just within, again, this really speaks
to the acceleration.

[00:19]
In the span of just a few months, we went
to,
it's kind of a ridiculous statement to say
that there would be 10 solutions to Erdos
problems.
it's actually happening for real and it's
accelerating.
Yeah, it's interesting because it seems
like step one is have models be able to do
really
good literature research.
And there have been major papers and
awards done,
given to people who've just done
literature
searches and found the solution was solved
here and it actually applies elsewhere.
So it's neat that it does that as the
first step,
but now that it's actually doing original.
I mean, you know,
one thing that I really like about AI
research is that it forces us to
confront big questions about intelligence
and about, you know,
research and progress and how
do we discover new things.
In particular, there is this question of
whether the progress that we're
seeing in science, is it just putting
together different pieces and, you know,
doing a little
bit of reasoning on top of it?
Or are there those brilliant, you know,
sparks of insight? Everybody,

[00:20]
of course, points to Einstein's, you know,
relativity. I'm not even sure that really
counts, to be honest.
So I think the jury is still out on
whether this process of just recombination
and a little bit of thinking, whether you
can kind of increase, you know,
human knowledge with no
limit, or do you really need the sparks of
genius that would be somehow only human?
Well, even he credited, I forgot who it
was, but who came up with the, you know,
the analogy, the visualization
method, you know, he said it wasn't his,
we pointed out who did it,
and he kind of took it to the next
step further, obviously.
And I think that we sometimes, we love
these tiny little stories when
it's a lot more complex than that.
Yeah, absolutely.
What will it mean for scientists in
general
if we have better mathematical tools in
AI?
How does it affect other things,
biology, material science?
Yeah, so again,
how it affects the rest of science?
Well, the point is,
I think it's really important
for everybody to understand.
It's not like we're doing something
very, very special for mathematics.
Our techniques,
our training techniques are very general.

[00:21]
They are applied to everything.
So our expectation is that
we are seeing more progress
Well, one reason is because it's very easy
to benchmark.
It's very easy to see that progress.
But we have full expectation that this is
going to happen in all sciences.
It's not going to be limited to
mathematics.
Yeah, it seems like something that's very
good at going, if this is true,
and then this is true,
and going through a long sequence of those
kinds of statements has a lot of
applications elsewhere.
We've heard the term auto-researcher.
Do you want to unpack that a bit?
Right now, the way we work is exactly what
Ernest described.
which is really an interaction.
It's kind of a professor-student
interaction
where ChatGPT is a student
and the professor is kind of, you know,
giving a first problem
and the student comes back
and then they talk a little bit.
The student goes away for another week,
comes back.
One point, of course,
is that it's compressing those timelines
greatly.
In the story, you know,
of solving this problem in 12 hours.
I mean, I don't know,
without ChatGPT,
how long would it have taken you?

[00:22]
Well, I have spent more than 40 hours
failing without AI. And I don't know,
maybe a month.
Right. So exactly. So, you know, there is
this thing of just compressing timelines.
Now, when we talk about the automated
researcher,
that's a slightly different vision where
the
model or maybe a collection of model would
work autonomously for a long period of
time.
This is kind of needed if we want to go
beyond the current level.
The current level of interaction,
the professor-student interaction
where the student comes back after a week,
it's going to be very hard
with that mode of interaction
to do real breakthroughs,
to solve actually longstanding research
problems
or to make progress in very difficult
fields in biology
where you need to interact with the wet
lab
and do all kinds of experiments.
So once you want to go towards the real
breakthrough,
we will need to work over longer
timelines.
And this is where the automated researcher
comes in.
Maybe let me say it in a slightly
different way.

[00:23]
One concept that I'm a big fan of is this
concept of AGI time.
So you can have AGI seconds, minutes,
hours, days, and so on.
So that really means you have an AI and it
can mimic human thinking,
but for how long?
So as Ernest was saying, two years ago,
maybe models were mimicking a high school
student
who thinks for a few minutes on a problem.
Now we can mimic a researcher who can
think for hours, maybe a few days.
We really want to go towards, and this
progress has been going on for now,
very consistently
for four years, where we went literally
from seconds to minutes to hours to days.
And now we are roughly at days slash one
week.
We want to go to weeks, if not months.
This is open research.
I don't think anyone on the planet knows
exactly how to do it.
But this goes back to, we are doing a lot
of research, a lot of innovation.
And I think once everything will be put
together,

[00:24]
we're just seeing this arc of progress
where we keep making progress in AGI time.
But this is the direction of the automated
researcher.
So the people, the other mathematicians
that I talk to,
their mode of using AI is they open up
ChatGPT and then they talk to ChatGPT
within that context window.
And you can have multiple sessions, but
each session has a finite context length.
And roughly on the order of like 50 pages
of a math paper.
And that's not long enough to make true
deep math,
groundbreaking math breakthroughs,
because a lot of math papers are longer
than 50 pages.
And also, the human thought that went into
to produce, let's say, a 10 or 30 page
paper is usually, well,
much orders of magnitude longer
than the final output.
So there's a limitation with the limited
context window. But people who've
use Codex will know that you can actually
have very long work sessions with Codex.

[00:25]
So you just
keep giving instructions as to what kind
of code you want to write.
And then the code itself that
you're working on, the repository of your
code, which in the math sense,
the analogy would be
that would be analogous to like math notes
that you write down.
That can be very, very, very long.
But Codex is pretty good at dealing with
that.
Once in a while, it compactifies its
conversations
And it has its way of becoming this really
amazing agent that can do really complex
jobs over huge repositories of code over a
really long context of conversation.
And this, I believe, is going to happen
with mathematics research as well.
So we will be able to have LLMs be able to
solve problems that are longer than just,
you know, that require more than 50 pages
of thinking.
And that's what human mathematicians do.
People think for a day on a certain
problem,
and then we kind of summarize our ideas
and then put it into notes.

[00:26]
The next day or the next week, we come
back to it.
And then over several months, we've
thought for so long,
but it's sort of summarized,
it's sort of organized in a way that
becomes manageable. And in the end,
the final output becomes a 30-page paper
summarizing the thoughts over many,
many months or even years.
so yeah i think that's gonna happen i was
working on a very very laughable problem
to you guys over
the weekend and using an LLM to try to do
it to figure out like how to use a
really small LLM to
do math in the middle of it i needed a
benchmark and i came across easy math
which is a benchmark
for small LLMs and problems just a paper
on it there wasn't really like a lot of
data and I just
in the middle of codex ago can you create
my own benchmark here and just generate
the data for that
And five minutes later, I had it.
And that was magical to me because I'm in
the middle of working on the tool that
would have involved me all of a sudden,
okay, I got to spend a few hours, go do a
generator, go produce this sort of stuff.

[00:27]
Absolutely.
And it runs in the background.
I can't imagine what it's like for you
guys doing grown-up problems.
Yeah.
I mean, what you describe is really, you
know,
what we went after when we published the
paper whose title was early experiments in
science acceleration with GPT-5.
Like we, what you have experienced is
literal acceleration.
Like this is something that would have
taken you before,
I don't know, maybe a few days of work or
something.
I would have given up.
Yeah.
So that's actually a great point.
You know, I would have given up.
This really enables scientists everywhere.
Like for example, mathematicians to be
able to use code.
Most of our friends, they don't code, you
know?
And now suddenly they have codex.
They can do all the experiments that, you
know,
before they were trying to find the poor
grad student
do the experiment for them. Now they can
do all of these experiments very easily.
The
flip side is of course, like that
scientists in all the disciplines,
they can also use
more advanced mathematics now, thanks to
ChatGPT.

[00:28]
I sat down with Bob Metcalf and showed him
how to use Codex to do R because he was
working
on a project and R was new to him and he
wanted to learn that.
And that was kind of a fun
experience to take somebody who's got a
great mind and say, oh, here's,
instead of spending
a lot of time having to figure this out,
there's the tool for you.
But of course, now, as you alluded to
before,
we should talk about the role of the human
in all of this.
What is the place for the human?
Especially if we start to think about, you
know,
let's think a little bit about the future.
I'm not a big fan of trying to predict the
future.
I like to explain what other...
But what do you think will happen?
I think, you know, there is what my heart
tells me and there is the rational aspect.
So what my head tells me is, look,
the progress has been happening very
consistently for the last four years.
From being able to solve math problems
that would take you seconds, to minutes,
to hours, to days.
There is no reason.
Anybody would look at the situation would
say, okay, a year from now,

[00:29]
you will have systems that can think for
weeks.
Two years from now, systems that can think
for years.
Not only that, but already today, we're
finding that our models,
they are able to really surpass
humans in the sense that they can find
mistakes in papers.
You know, we had system,
we had agents internally that have been
able to come up with, to find
papers and say, hey, actually this is
wrong.
Here is the correct answer.
Not only that,
but people tend to think that AI is only
good at answering questions.
Actually, no, it's also pretty good at
asking questions.
Of course, you need to be, you know,
again,
you need some research innovation there,
which we had.
And now our models are very good at asking
questions.
So good, in fact, that humans are looking
at those questions and saying, hey,
maybe I should write a paper based on this
question.
So this is, you know, really, really
already happening now.
So I think what I'm trying to say is that
in a year, in two years, yes,

[00:30]
models could do basic, more or less
everything that human researchers do.
So now what?
What is the role of humans?
Well, why is it that we're doing science?
What's the point?
You know, the point is not to, I mean,
it shouldn't be to just solve problems for
the fun of solving problems.
We're solving problems because we're
trying to understand something.
The understanding piece is key.
We're not solving problems to write
papers, to show, to say that we can write,
you know, 10 times more papers than our
neighbor.
That's not the point.
You can do competitive chess if that's
your kind of deal.
We're trying to really understand deeper
things.
And why are we trying to understand deeper
things?
Because we want to have better control
over our environment.
We want to be able to cure diseases.
We want to be able to build things better,
faster, more robust, more solid,
all of those things.
So I think there is a chance that we're
looking at a very,

[00:31]
very bright future using those tools as
long as the human stays in control and
guides what are the problems that matters.
Problems that, you know, the AI doesn't
care about curing disease.
I mean, you know, they will not suffer
from the same disease as we do,
but we do care.
So we have to control them and to guide
them towards those problems.
At the time of the advent of the first
computers,
when the computer went from being a person
that did the math to an actual machine
that did it,
you saw some people looking at maybe we
all have to move from math to physics
because that's where the hard problems are
going to be.
And there's not going to be any more hard
problems in mathematics because computers
resolve that.
Now it was the 1940s and 1950s.
And it turned out that that's not the
case,
that computation opened up a whole new
branch of that.
And that's what's going to continue,
that we're just going to see that the
mathematician that's in high school today
is going to have a very exciting future 30
years from now because of what's
happening here.
I think math is going to be so much fun.

[00:32]
So, okay, so math is, so mathematicians
enjoy solving problems.
But, you know, pre-AI, you know, we would
think for months to solve a problem.
And that's, there's enjoyment in that, but
there's, it's quite grueling.
That is pain.
There is pain too.
There is a lot of pain.
And there is a huge,
like there is a surge of dopamine when you
actually find the solution.
That's going to be accelerated.
So, you know, more solutions, more fun.
But also,
I think math is going to become much more
richer because it's going to be much more
interconnected.
Because there is a lot of, at research
level, a lot of math is hyper niche.
And when you write the paper,
you know that there are only five living
humans right now that will care about this
paper.
But you like the results, so you put it
out,
and then the five other people appreciate
it, so they read it.
But then 20 years later, it's going to be
in the archive somewhere,
and nobody will read it.
But now that we have AI, the AI will have
read it.

[00:33]
And if there is a useful connection, as
Sebastian mentioned, it will surface it.
And then people 100 years down the line
will discover it and use it for whatever
they want to use.
So I would now have much more confidence
that my results that are just put out
there will be used if there is a use in
the future.
And also, I'm now able to access the
mathematics in a much broader way.
There are fields that I've not studied,
but if a result comes up,
then I would still have to study that
field to be able to use that particular
result in my research.
But there is no way I could have found
that result without the assistance of AI.
But now it's accessible.
The model tells me, hey, you can use this
to solve your problem.
And then, well, OK, I'll go and try to use
that.
So math is going to be a much more
interconnected enterprise.
And also, verifying correctness of
mathematics is actually quite non-trivial.
Because imagine there's a proof written by
somebody that's 300 pages long.

[00:34]
And it claims to solve a really important
problem.
And this person is a very reputable
person.
So like there's there and the paper at
surface looks plausible.
How do you know?
Well, I mean, this is a process that takes
years to verify.
And it's also not enough that one person
reads it.
Many people need to read it and then try
to extend it and then look into the
details.
This is a process that takes years.
And sometimes, like, fatally incorrect
proofs are published.
So that's also a very slow process where
the field initially accepts a result,
but later
on discovers that it's unsalvageable.
So then it needs to get filtered out.
This is going to be so much more
accelerated with AI.
So right now,
our chat GPT and our AI models are not
perfect at verifying mathematics,
but it's very good.
And also, it has much more patience than
humans.

[00:35]
Yes.
So the truth is so much of the published
mathematics have minor mistakes and a lot
of them do have major mistakes.
And we know because we have tested these
things with our models.
But now I think the more richer future of
mathematics is that this will be through
AI verification.
We will have much more certainty as to
which results are correct,
which results are incorrect.
And we'll have a much faster feedback on
this.
paper published, put out a week ago, we
could get a verification on that.
And then we could trust
and build on that as opposed to waiting
for five years to really ascertain the
correctness.
So overall, math is going to be much more
fun.
It's going to be much more interconnected.
We'll be able to trust the results more.
We'll be able to move faster.
And the mathematicians will solve harder
and more interesting problems.
So maybe one thing that I want to add, so
I totally
agree with everything that you just said.
It's going to be a lot of fun, but I want
also to

[00:36]
look about one potential danger of the
current progress,
which would be that we kind of hand
the keys to the castle, to the AIs,
and that humans just start to trust the
system a lot more,
and that they don't do the hard work that
we kind of did to own our skills and to
own our skills to
to be able to verify and to sit patiently
for hours,
many days in a row or many weeks in a row
to try to understand deeply a result.
And instead just kind of ask ChatGPT to
explain it to us
in simpler terms.
So basically I'm worried about potentially
having a shallower understanding of
things because we rely too much on the
tool.
So I think it's really important for the
audience,
for everyone listening to us to understand
that expertise is even more valuable than
it ever was.
The reason why we are able to squeeze out
those results from ChatGPT is because of
all of those
years of training and our deep
understanding of the subject.

[00:37]
If it wasn't for that, we would not
be able to push the state of the art. And
we're seeing it.
It's not like we're seeing thousands
of people, like non-mathematicians
suddenly being able to prove new results.
In fact, if anything,
We have seen recent examples in social
media where non-mathematicians have tried
to use those tools to prove theorem and
come up with,
you know, many tens of pages of proof.
And then it turns out to be just wrong.
So this is a danger that we have to
grapple with.
It seems like that's going to be a problem
in a lot of things.
You see people spend, you know,
using current models that often just
reinforce things you want to hear.
And that can be kind of, you know,
I'm going to come up with some sort of
unified theory or whatever.
Like, well, guess what?
That's going to be a lot harder.
Yeah, I mean, this sort of issue of mental
sort of atrophy, if you will, is also,
I think, very prominent in coding as well.
So, I mean, I'm not a, you know, I wasn't
a computer science major,
but I took some computer science courses
and I did, I coded myself.
I wrestled with the debugger and most
people of my age did.

[00:38]
But nowadays, you don't have to do that in
your university curriculum.
And I think that's very dangerous.
I've heard some people in the sciences who
look at the progress are very optimistic,
like, well, we're not going to need
scientists.
We're not going to need this anymore.
No.
Yeah, no.
Wow.
This is terrible.
So really, I want to make sure anybody
listening, please do not say that.
This is the opposite of what we need.
We need more scientists than ever.
Those scientists are going to be more
productive, more powerful.
They will do better things.
But we need them to be really, really good
at their craft.
And I think this is where, you know,
obviously, OpenAI cannot do everything,
you know, just to say it out loud.
And this is where the existing
institutions have a very big role to play.
So academia needs to both understand the
rate of progress and, you know,
how fast this is going, but also to kind
of reclaim their role in that process.
Yeah, my hope and expectations,
we're going to see more people go into the
sciences because if you decide later on
in life that you want to get into this,

[00:39]
it's easier to catch up if you're
dedicated because you have the greatest
tutor in the world.
OpenAI just added to the ChatGPT has a
visual explanation tool now that helps you
explain things.
And I think that people, you know,
just because all of a sudden an AI model
is able to, you know, completely top out,
you know, a benchmark doesn't mean you go,
OK, we're done.
We solved grade school math.
Congratulations, everybody.
AI is done.
It's like, no,
there's a next level and the next level
and you're going to need people.
No, I think it will help.
I mean,
the young generation to get up to speed in
science like so much more quickly.
That's for sure.
Like I cannot imagine if I had ChatGPT,
you know, as a teenager.
I mean, I remember looking at Maxwell
equation and being like,
what does it really mean?
How did they come up with this stuff?
Now you can just ask it and it will
explain it to you so beautifully.
It's a big deal, but you still need to do
the hard work on top of it.
Though with a lot more people trying to
create mathematical proofs who don't know
what they're doing and aren't really maybe
putting the right scholarship to make

[00:40]
sure of that.
We've seen areas of code repos and whatnot
and people contributing fixes that aren't
real fixes and things like this.
How do you solve for that?
If I'm somebody who's involved in
mathematics or a journal right now,
I'm a little bit terrified.
Yeah.
So I think what Ernest said is that, you
know, AI can help also for that.
So we can have on the other side of it, of
those systems,
to have AI agents that are also going over
everything,
trying to verify as much as possible.
And then, again,
we do not want to trust fully the AI to
verify and to accept a paper or to accept
a comment.
But we can have the AI agent flagging
specific potential issues.
So kind of bringing to the front, okay,
hey, maybe this part,
I'm not totally sure about it.
So that will accelerate, that will help
the human to have less to verify,
basically.
And I think the sort of social structure
of mathematics or code,
it has to change a little bit in a way
that the human doing the commit or human

[00:41]
controlling the agent takes
responsibility.
So in mathematics, there already is a
culture of, well,
if you put out an incorrect proof, then,
well, that hurts your reputation.
And you're putting your reputation on the
line when you put out a paper with your
name.
And that has to, I think we need more of
that.
If you're mathematically curious and
somebody is watching this or listening,
and they maybe have an interest in math,
but maybe they didn't feel they were a
math person,
but they're kind of curious to get
started, what would you tell them?
Go chat with ChatGPT.
If you are interested in learning, then
it's so helpful.
Even at the research level, when I need to
learn a new concept,
I would habitually go to Wikipedia, and
then it's just very dense.
I'm like, okay, well, after like 30
seconds, I go, okay, let me ask ChatGPT.
And then I ask it.
And then I also ask follow-up questions.
And when I do so,
it gives me so much more helpful
information that is tailored to the
parts of my knowledge that is missing
because I'm asking the questions tailored

[00:42]
towards that.
And you could imagine explaining to
ChatGPT your mathematical background,
the books that
you've read, the material that you've
learned,
and then ask you to come up with a
question that
would be open and also would be
understandable with your level of
expertise. Sebastian mentioned
this.
I don't think people yet appreciate that
these LLMs are able to come up with good
questions,
but I think they can.
So having this companion that you can talk
about math with and talk about
questions. You could ask the model to help
you solve it.
And once you have a solution, then you
could keep talking and come up with the
next question, variations of this.
It becomes a much
more, even though you're still in your
room alone,
it feels much less of a solitary process.
And
that's what really makes mathematics fun.
Because math, I think it really is a
social endeavor.

[00:43]
I think toy problems would be fun.
And I tell people, you can start with how
many M&Ms
can you fit in your bathtub?
It sounds silly.
And you start to ask,
then you go,
how many words did you read last year?
How would you figure this out?
And then you can start to have
this real wonderful conversation
and start asking these questions.
Next thing you know,
you're starting to do
more and more complex mathematics
and realize how it should affect you.
Gentlemen, this is great.
Sebastian, Ernest,
thank you very much.
Thank you.
Thank you for having us.

</details>
