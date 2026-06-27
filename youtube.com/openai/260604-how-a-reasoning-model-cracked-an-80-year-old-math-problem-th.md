---
title: "How a reasoning model cracked an 80-year-old math problem — the OpenAI Podcast Ep. 20"
channel: openai
url: https://www.youtube.com/watch?v=wNWz5Hbh5VQ
youtube_id: wNWz5Hbh5VQ
published: 2026-06-04
duration: "41:17"
captions: en
---

# How a reasoning model cracked an 80-year-old math problem — the OpenAI Podcast Ep. 20

[![How a reasoning model cracked an 80-year-old math problem — the OpenAI Podcast Ep. 20](https://img.youtube.com/vi/wNWz5Hbh5VQ/hqdefault.jpg)](https://www.youtube.com/watch?v=wNWz5Hbh5VQ)

<details>
<summary>자막: How a reasoning model cracked an 80-year-old math problem — the OpenAI Podcast Ep. 20 (41:17)</summary>

[00:00]
Hello, I'm Andrew Mayne, and welcome to
the OpenAI Podcast.
On today's episode, we're speaking with
Alexander Wei, Hongxun Wu, and Lijie Chen
from the reasoning research team behind a
recent math breakthrough from an OpenAI
model.
They'll tell us the story behind the
discovery and what stood out to them about
the reaction.
Everyone had a hard time sleeping because
it's so, so exciting.
Okay, this model is something that's
really amazing.
I mean, this is something that can be
published in the best journal of math.
Maybe this is one in a hundred times where
it's too good to be true, but it's
actually true.
Lijie, tell me what you work on.
Oh, I work on reasoning with Alex.
Okay.
How did you find your way into reasoning?
Last summer, Alex had this breakthrough in
like IOI and IMO.
You know, I used to be a participant in
IOI.
Okay.
And then I was like, oh, that's crazy.
You know, model can already win medals,
gold medals.
At that time, I was an assistant professor
at UC Berkeley.

[00:01]
But then I'm thinking maybe I should try
to rethink my career.
It seems like making the model smarter
will maybe have some bigger impact on the
world.
And then I just kind of had a conversation
with Alex back in last October.
And then I got super excited about this
thing.
And eventually I just joined OpenAI.
We hear IOI and IMO come up a lot.
Alex, you want to unpack those for
everybody?
So IMO and IOI are these two competitions
for high schoolers.
They stand for the International Math
Olympiad and International Olympiad of
Informatics, respectively.
And these are just devilishly hard math
problems.
You get two sessions for each of these
exams that are like four and a half to
five hours, and you just have to do three
problems.
And so for a long time, these were sort of
an implicit grand challenge in AI.
When would we be able to get models that
could perform as well as the best humans

[00:02]
on these exams?
That was a pretty interesting starting
point, I think, for measuring the success
of the model.
And we're here to talk about how far
things have gone since then, which is
pretty incredible.
But how did you find your way into
reasoning?
So I did my PhD in ML.
Towards the end of my PhD, I got excited
about this idea of spending more compute
at inference time to solve harder and
harder reasoning problems.
At the time, I was playing with GPT-3.5
Turbo in the API, and I didn't really get
any interesting results.
But there was this team at OpenAI that
seemed to be doing something pretty
similar.
And so I got super excited about it and
was lucky enough to be able to join.
So probably the simplest way to describe
that is like letting it inference time is
basically letting the model think longer
about it.
Yes, that's right.
So basically, before this era of test time
compute, models sort of answered

[00:03]
immediately without, like right off the
cuff, without thinking.
And what inference time compute, test time
compute does is you now give the model a
chance to think and improve its answer and
try different things before having to
finally output something.
That obviously just helps make the model
smarter, lets them do things that they
wouldn't otherwise be able to do
instantly.
When you started to work on reasoning, did
you have an idea of where you wanted to
see this go?
Like what your expectations were?
Were you looking at it purely from, hey,
this is very cool from an academic point
of view?
Or did you have some sort of other vision?
I think for me, the draw of reasoning when
I first got excited about it was that
this was something that, you know, models
just obviously can't do right now.
So this was like end of 2023, start of
2024.
Models were, you know, struggling with
grade school math problems.
And so at that time, it was just like, can
we just get these models to do something

[00:04]
reasonable on math at all, let alone have
them be much, much better than I am at it.
I remember my first day at OpenAI, Nolan
Brown asked me when I thought models would
get IMO gold.
That was just a benchmark we talked about.
I think at the time, a lot of people even
within research thought that IMO gold was
out of reach this year, but maybe like
2026.
I felt like I had an idea that if we just
pushed for it, maybe I thought we could do
it by April.
It took until June to get a really good
model.
And then IMO rolled around and we were
able to get gold.
And I think zooming out, I think this
happened a lot faster than I expected.
And it's crazy to me that progress since
then has kept up at this same sort of

[00:05]
blistering pace.
It was just 10 months ago, but it feels
like the IMO level of problem feels far in
the rearview mirror of AI today.
Nolan asked me the same question.
I mean, not about IMO gold, but about
whether a model can solve P versus NP.
I think P versus NP might be something
quite hard.
Because I think the reason is that I think
for solving P versus NP, you would need
to build a new theory.
Maybe you have to write many books of new
ideas to get there.
So currently, it seems we are still far
from that.
But, you know, maybe who knows what will
happen in the future. So, yeah.
Hongxun, what do you work on?
Oh, I was working on theoretical computer
science.
I was collaborating a lot with Lijie in my
PhD.
I was at Berkeley.
And I remember when o1 came out, I was
talking to my advisor saying, "Oh, there's

[00:06]
no barrier in models solving math problems
anymore."
I think he just smiles.
And he knew that he was going to lose a
student. Oh, wow.
So let's talk a bit about that, because
it's an interesting point.
Because as you said, it went from the
model would just have a moment to try to
figure out the answer.
Then all of a sudden, you've given it the
ability to spend longer and to think about
it, reasoning.
And the results have come pretty quickly,
and I think surprising to a lot of people.
You had a model that was able to basically
disprove one of the Erdős conjectures.
Could you explain that just a little bit?
So our models last week, they were able to
produce a proof of the, or a disproof
rather, of the unit distance conjecture
due to Erdős.
And this was an 80-year-old open problem
in the field of combinatorial geometry,
where basically the question concerns if
you have endpoints, let's say on a piece

[00:07]
of paper, how many of them can be one inch
apart exactly?
And how many pairs can be one-inch apart
exactly?
And how does this number grow
asymptotically with the number of points
on the piece of paper?
This wasn't a trivial problem.
When Erdős put this together, the idea was
to say that it could, you know, I think
ideally it had to be only done on a plane
or something like this.
But there was, you know, the idea that
maybe there was no better way.
And this has been out there because it's a
very interesting problem.
And the fact that a model solved this is
pretty profound.
And also, this model was a general purpose
model, correct?
Yes, that's right.
So Erdős's original conjecture was
essentially that the optimal solution to
having as many distance one points on the
plane was to arrange them in a square
grid.

[00:08]
And what the model proved was that the
square grid was not actually close to
optimal at all.
and that you can do much better with a
different construction using a lot of
high-powered number theory.
Hongxun, how did you choose these
problems?
I guess we didn't really choose the
problem.
What happened was we wanted to test the
upper bound of our model's capability.
So we just used a selected subset of Erdős
problems and to test the capability of
the model.
I would love to know, one, who is the one
that hit Enter and asked the model the
question.
I guess both of us, like Hongxun and I.
You guys at the same time, like, press--
Yeah, maybe.
I think what happened was actually we were
testing like two side different internal
models.
And we both saw some correct solutions.
It was really, really exciting for us.
How did you know that it worked?
Of course, you first asked the model to
check it.

[00:09]
Okay.
But of course, you know, models sometimes
are not reliable.
I got it. It's good. Don't worry about it.
Yeah, so then we just, after we checked
with the model, it seems plausible.
Then we just asked a bunch of, you know,
our mathematics friends in the company,
you know, Mehtaab and Mark Sellke.
And at first they were like, oh, there's
no way this can be true.
It's a major open problem.
But after, you know, just they think about
it for a day, they couldn't figure out
any mistake.
Then they become more convinced.
Then eventually they're like, actually,
this may be correct.
Yeah, then everyone had a hard time
sleeping because it's so exciting.
What was the conversation like when you
started getting people saying that this
was accurate?
For me, I was not that surprised because I
guess when Mehtaab first said, okay, what
happened was first Mehtaab said, this is
definitely wrong.
But I actually knew that he probably just
spent like five minutes, 10 minutes
looking at it.
So in my heart, I don't really believe
that.

[00:10]
But later he told me it's 50%.
I was thinking, okay, if we extrapolate
the trend, then maybe next night it will
be 100%.
So yeah, it's a little bit dreamlike, but
also it feels a little bit natural that
this model would do something amazing.
Later, it just become more and more real
that this might actually be correct.
might actually be a big deal the first
time they can publish something that would
get into
top math journals.
We knew this day was going to come, but
never knew that it's going to become
reality so fast. It's like living a dream.
I mean, this is something that can be
published in the
best journal of math. It is way beyond IMO
level.
So I would expect something to happen at
some time, but at some point.

[00:11]
But maybe not just this may.
Yeah.
One of the things I think that we've seen
emphasized at OpenAI is that OpenAI
doesn't try to train two specific
benchmarks and stuff.
That OpenAI tries to build really good
general overall models.
And I think sometimes people say, well, we
just try to build a generally smart
model, and we find these things a lot
away.
And when it comes to reasoning, it's the
same thing.
Something that's really good reasoning
overall, you find these capabilities.
Does that ring true for you?
Yeah.
I think for this model in particular, I
think it's one that I think all of us have
also just used in lieu of the current
model in Codex.
And it works quite well as just a general
purpose model.
Having the capabilities to do this Erdős
unit distance result, I think people will
be able to do this at home in the near
future.
It's been exciting to see people react to
this and pay attention to this.

[00:12]
We went from just a very short period of
time ago where people said models weren't
good at math, and now models are doing
this.
What have been some of the more fun things
you've seen online or reactions from
people?
Ever since we announced the results, my
friend in TCS started to ask me to try
their open problems, including my advisor
gave me like two, three open problems to
try on.
I think the reaction was very positive.
I think people really get a sense that the
frontier of AI today can really come up
with research output that I think many
human mathematicians would be proud to
achieve.
And I think it's really great that we're
able to communicate this, that this is the
frontier of progress to the rest of the
world.
I've seen people make these designs of
trying to sketch out the model's
construction.

[00:13]
If you plot it on a grid, it's actually
this very pretty, symmetric, geometric
design.
Yeah, I guess we are thinking maybe try to
make one of the designs, put them in a
frame and put them on a desk or something
to celebrate this moment.
Yeah, I think it's going to be fun when we
start seeing things like tiling problems
and other stuff where we can actually just
look at the artifacts that we need.
So we've been hearing more about Erdős
problems lately.
And some seem like they weren't as
challenging to solve as perhaps as people
thought.
They just needed some attention.
Yet this one seems to be a little bit more
complicated.
Where would you rank this?
I think he proposed like a thousand
questions or more, right?
So like he, you know, Erdős problem is
this collection of all the problems he has
asked.
There's some problems where he has offered
some money for a solution.
Some problems he just noted.
And this problem he offered, I think,
$500, which is from last century.

[00:14]
So it was a little bit.
And also, this is one of the central
questions in this field of discrete
geometry.
And this has been heavily discussed by
mathematicians in many discrete geometry
papers.
And so it's kind of one of the questions
people have thought about a lot and really
want to see the answer.
So I would say this is more like a major
open problem in a concrete field of
mathematics instead of some just like, you
know, many other Erdős questions, which
may be just some, you know, something
Erdős asked after lunch or something.
So how do you collect that $500?
Did it disappear when he passed away?
I think there's a special agency for that.
But you usually just frame the check.
Yeah.
So maybe we'll just frame the check in
Sam's office. I don't know.
How do you feel this proves that reasoning
is effective?

[00:15]
Well, I think the biggest proof is that if
you look at the plot in the official
blog, if you give the model more time to
think, the accuracy on this problem grows
faster.
Like if you give it a lot of time, it can
get almost 50% correct.
So more thinking, more correctness.
I think that's really a proof of reasoning
being effective.
But Alex, to go back to this, this isn't a
math model.
This is a model that can do many different
things.
Do you see a correlation between as these
get better at solving things like
mathematics that it works with other
general problems?
That's the hypothesis at least is that
this model was not trained specifically
for math.
And so, and we just wanted to, you know,
like we had this new model, how we came
about this.
We wanted to take it on a test drive,
essentially.
And so we evaluated it on some, you know,
very challenging math problems and to just
see like, what can it do?
When you go through the proof and you look
at what it came up with, were the things
that surprised you, things that you would
describe as creative?

[00:16]
So for some context, like the proof is
like well above my own mathematical pay
grade.
But just at a high level, my understanding
was that this idea of taking class field
theory and applying it to problems in
combinatorial geometry hadn't really been
done before.
Though some people knew that there could
be this bridge between these two fields.
Being able to do that and execute it
requires, first of all, to make the
connection requires quite a bit of insight
and creativity.
And then to execute the proof is also a
very delicate, careful affair that very
few people would be able to do.
I think the most surprising thing for me
is you tell the model to do something and
you want to have a lunch.
And when you come back, you'll see that it
actually does much better than you
thought.

[00:17]
And at that moment, you feel like, Okay,
this model is something that's really
amazing.
So going back to GPT-3.5 Turbo and working
with that and looking at a model that was
doing automatically instant sort of
inference and figuring these things out to
now a model that's able to do incredible
mathematical proofs.
Is it using tools? Is it using Lean?
Is it using some other things like that?
Or is this doing purely inside the model?
In the case, the model basically is like
Codex.
It can code, it can look at the website
and find information.
So it's basically a general ChatGPT setup.
You can also write Python and execute it.
But I don't think the model writes
anything.
I think Lijie has a story about the
Cambridge dictionary.
Oh, Okay.
So the first thing the model do when it
gets to the website is to check what unit
means in the Cambridge dictionary.
It's a little bit ridiculous.

[00:18]
So it looked up the word unit?
Yeah, you also make sure it has the
absolute correct understanding of what is
unit.
Have you seen it do other things like
that, where you're saying, oh, it's trying
to ground itself to make sure it
understands the question?
I think definitely.
A lot of time in the model answer, it will
actually explain the definition again.
Yeah.
To show that it actually grounded the
definitions.
As people who are very knowledgeable about
computer science, people who know a lot
about mathematics, is it intimidating to
all of us and see this happen?
I think it should not be intimidating.
I think it should be empowering.
Okay.
After the proof actually come out, like
mathematician has improved, first improved
the bound it proved.
And second, they use the motivation of the
construction to knock down other open
problems as well.
So I think the trend is going to continue.
Model can make good breakthrough on some
very hard questions we don't know how to

[00:19]
solve.
But then how to digest that idea, how to
use that method for other good things, I
think human still has a role in this.
So what do you think the role of somebody
working in mathematics is going to be like
five years from now?
I think there will be a lot of AI and
human collaboration.
Because AI, and now AI, they know a lot,
right?
They can connect distant ideas.
But humans can also think for longer.
Currently, it seems AI cannot build a new
theory for math, for example.
But I guess humans, once they have the
help of AI, they can just grab all the
ideas from distinct fields of math.
I think they can empower humans way more.
Do you see this working into other fields?
Are we going to see discoveries in
physics?
So, I mean, I can't speak for physics, but
I mean, I guess like we're all
researchers in AI.
And I think definitely for me, like my day
to day looks completely different than

[00:20]
when I first started doing research in
this field.
I think so much of my work is now done by
coding agents.
I can just do so much more.
And I think that's been a sort of magical
feeling that with AI, you're really
starting now to feel like you can use AI
to build AI faster.
How much has AI changed the way you do
these sorts of things?
I think changing completely.
Even when I just joined half a year ago, I
was hand coding the codes, looking up the
select channels for directions.
But now the default is just ask Codex.
And I ask Codex to do a lot of things.
And then I just go to lunch.
I just go to talk to people.
The work completely changes.
And now you use Codex on your phone and
you can check on it.
Yeah.

[00:21]
It's interesting how much more I want to
do things now that you have this sort of
tool that can work all the time and do
stuff.
Lijie, how do you explain this to your
friends who are sort of trying to
understand what this means and how it's
going to impact other fields?
So, I mean, I have some mathematician
friends and I have some, you know, friends
in other fields.
Yeah.
So I think the way I want to tell them is
that I feel like, you know, some may be
afraid that AI will replace them.
You know, AI will just replace
mathematicians.
Yeah, but I think it's really about
empowering every theoretical researcher.
Because AI really has this advantage of
knowing so many stuff and connections.
Currently, it seems like the problem had
for a human may not be had for AI.
And that's a really great thing.
We can use AI to solve those problems, get
new ideas, and then we can digest them
and make new discoveries, just like
Hongxun said.
So I think some of them get very excited
about this.
And of course, one thing is that, you
know, currently it's only on math, but I

[00:22]
believe that because it's a general
reasoning model, like all the at least
theoretical researchers, they can benefit
a lot from that.
Like, I think the dream world will be like
everyone have some access to the top
level reasoning ability.
So other researchers can use them to
discover whatever they want to discover.
And then basically, OpenAI will accelerate
science a lot, because you are empowering
every scientist to accelerate the science
worldwide.
And then that's our mission.
So if I was a researcher, how would I get
started?
What advice would you have to say, Okay,
try this first?
We'll start with you, Hongxun.
Get a ChatGPT Pro subscription.
Of course.
It's really, really much better than
thinking without Pro and because they
think longer.
and try to ask the boldest question you
can ask.
I had an experience that sometimes I try
to decompose a problem into a smaller
problem and ask the model.
And it turns out that it was not as good
as just directly ask the question, because

[00:23]
my decomposition was not the best way.
Why do you think that was?
I think because as humans, we have all
kinds of priors on how problems should be
solved.
And they are very helpful in reducing the
thinking time.
But very often, the prior are wrong, and
there are blind spots.
And AI models, they sometimes just can
surprise us with discovering these hidden
things.
When I spoke to Alex Lupsasca, he talked
about how kind of treating it like a
graduate student.
Not talking down too low, but not too
high, but at the right level so you could
just understand that it knew the terms and
worked for you.
Alex, how about for you?
What advice would you give somebody who's
a researcher who wants to try to figure
out how to be more effective with this?
Yeah, I think a lot of it is actually
like, I think these days learning to trust
the model and like figuring out like, you
know, how far you can go in trusting the
model and also learning like, you know,
what's beyond what the model can do.

[00:24]
Because if you don't have a sense of that,
you don't like, you know, maximally use
the full capabilities of the model.
I think Lijie has taught me a lot about
how to use these tools better.
I feel like I'm sort of a dinosaur in some
respects in terms of adoption.
Because I think I started working at
OpenAI well before these tools existed.
And so I think I have a lot of old bad
habits where I don't trust the models
enough.
I still think it's like the models of six
months ago or something.
That's an interesting paradigm.
Okay.
So, Lijie, what advice would you give?
Oh, I have this method of every time you
double your trust on a model.
and see when it fails.
And if it fails, you just go back.
And you do this every month.
Then you can quickly get to the point
where you can maximally trust the model,
but also not breaking your stuff.
And apparently, for the last five months,
it's going really exponentially.

[00:25]
Back in the GPT-3 days, I had a list of
tests and things like this I would do.
And I'd watch them incrementally get
better, then GPT-4, And then by the time
o1 came out, I had to throw it out because
that was just toy problems at that point.
And I feel like I have to continuously
sort of adjust and kind of keep trying
bigger and more complicated things to do
that with.
Do you think that for somebody who's in
mathematics or in a related field right
now who's feeling a little bit concerned
by this, do you think that they should be
taking a more optimistic approach?
I think it's legit to feel concerned,
especially when a lot of the field is
problem-solving oriented, because models
are going to be really good at
problem-solving.
But mathematics is really, really much
more than problem-solving.
It's more about understanding the
structure and building new theories, like
Lijie said.

[00:26]
And I think we should try to figure out
how to better use the model to help us in
solving the problems that we met and then
try to accelerate the speed that we build
new theory and come up with new
understandings.
I think that's the more optimistic view.
When Codex becomes much better, it can do
so much more things for you.
You would expect you will work less
because Codex is good.
somehow you actually work more because
that's way more thing you can do.
So I actually hope this can happen for
math as well.
The model becomes so good, I must imagine
you have 10 ideas.
You can ask 10 models to try them and see
one of them succeed.
And they don't have to do tedious
calculation by themselves.
So I would imagine maybe what happened
with coding can happen to mathematicians.
It's interesting too because when we talk
about the Erdős problems, Paul was a very
interesting person who found a lot of
things curious and said, oh, this is neat.

[00:27]
And we have this category of problems he
put together, but there's not a lot of
rhyme or reason to them.
They were just things that he found
curious or worked with other people on.
And I think that's kind of a big thing
that's neat about science in general is
often we think that there are these real
specific hierarchies, but literally it can
just be things we're curious about.
That being said, how long before there are
no more unsolved Erdős problems?
Some of them are very, very hard.
Yeah.
Yeah. So, yeah, I don't know.
Do you foresee us, maybe Alex, needing to
come up with a new category of problems?
I think probably the hardest problems on
that list, I think that list includes the
Collatz conjecture.
These are problems that feel very, very
far out of reach of the mathematical
technology of today, even though many of
them are quite simple to state.
So we'll still have some more things to
work on and continuously move things
through. That's good to know.
It's exciting, though, too, to think about
what happens when you do start applying
this to other areas in physics and
astronomy and start looking at data sets

[00:28]
and stuff and what kind of discoveries are
going to be in store.
Do you have any particular area that
you're hoping to see?
Oh, I hope it just solves P versus NP.
Okay.
How about you, Alex?
I think the next milestone in my head is
really like AI that can do AI research.
I think there are so many unsolved
problems here.
We are, in a sense, in many ways, limited
by all the limitations of just our own
intelligences.
I'm optimistic about just having AI
broadly available as a technology because
there's just so much more demand for
intelligence in the world that humans can
supply.
Oh, I wanted to say P versus NP too, but
Hongxun said it.
Yeah.
So I guess beyond that, like one concrete
thing I'm very interested in is like, no,
like it currently assumes AI is trying to
combine ideas from different fields.

[00:29]
And of course, in a very novel and, you
know, sophisticated way, but like, can AI
actually generate completely new ideas
from scratch?
I mean, that's something like we haven't
really seen concretely in AI.
And that's something I maybe want to see
next happening.
And that can be very cool.
Have you seen traces of that yet?
I think so.
Like, you know, even in this problem, I
mean, I think some-- if you look at the
chain of thought, which is like 125 pages,
I think some of the thoughts are pretty
creative, although they didn't work out.
Yeah.
I mean, the final idea is more like
combining all the stuff.
But somehow it has some creative thoughts.
But it is interesting.
Early on, arguments were like, these
models But you could give it two ideas
that have never been connected before and
say, what's the relationship?
And that would be something very, very
new.
It felt like something different.
And I feel like we'll probably be seeing
more of that.
Do you see us coming up with new forms of
mathematics?

[00:30]
I think that actually will be a shorter
way down the line.
Next year.
Maybe.
I think because models now are very, very
good at coming up with some idea to solve
a problem.
but it's not good at proposing a
completely new different kind of math or
proposing new theory.
How to get a model to do that is still
very, very open.
How I would think about it is we see this
like Moore's law for the time horizon at
which these models are effective.
And I think you sort of feel that in math
where, you know, there's like every few
months, the amount of time these models
can like sort of work independently for
doubles, at least the amount of human
equivalent time.
And so, you know, for solving problems, if
you're really, really good at it, maybe
some problems like you actually have
pretty short paths for the solution.

[00:31]
You don't need to take that long.
But I think for inventing new ways of
doing mathematics, that's much more like a
years or decades long process.
And so I think it'll still take a bit of
time for that exponential to get there.
This was done by an internal model that
you guys worked on.
And since then, GPT-5.5 has been able to
do the same thing.
And we've seen other labs have said that
they've been able to do this as well.
But this was several weeks ago, which is
now ancient history.
What have we seen since then?
I think one difference between the
original result and I think what the
follow-up findings have been is that
actually for the original model, there was
no scaffolding needed.
You sort of just asked it to do the
problem and then it gave you the answer.
And so actually this is all, you can read
the original prompt and response in the
note we uploaded on the blog.
Whereas I think the follow-up efforts have
had a little bit more structure or

[00:32]
steering of the models.
I think one interesting data point here is
that it's really all about test time
compute scaling.
After we initially solved the problem,
this is a plot Lijie brought up earlier,
is that with enough test time compute
budget,
the model is able to solve the problem
around 50% of the time.
So it's not surprising that you can get
there with other methods.
You can find this with other methods as
well.
But I think what's really important here
is just that as you pour in more test time
compute, you get better results.
It seems like it's kind of a virtuous
cycle where you take today's model, give
it more compute, let it solve for that,
and you understand how these problems can
be solved.
Next generation models can learn from that
and just get more and more efficient.
And you just have this, basically, it
seems like it just scales forever, right?

[00:33]
What do you think we're going to see by
the end of the year?
What I want to see is people use our model
to discover lots of new stuff.
And not only in math, but also in all of
science.
Of course, OpenAI wants to do some cool
math stuff.
But I think it would be better if everyone
can use the model to discover their own
science.
And I would expect like many
mathematicians will use the model.
I mean, maybe not completely on the model,
but collaborate with the model to
discover a lot of more math results.
I think that would be really cool.
Hongxun, I've talked to some
mathematicians who know others or who are
very reticent to even try using AI in
mathematics.
What is the best argument you can give?
I think I'll just show them the proof of
the conjecture.
I think just about productivity, right?
Like we do math not just to enjoy the
pleasure of the problem solving, but also
to advance a field and to understand the
truth that we're looking for.

[00:34]
And using AI is going to speed up that by
a lot.
It's going to tell us what we are really
struggling to find, and it will be hard to
resist using it at some point.
You could be an astronomer and not use a
telescope, but you kind of have to ask
why.
Yeah, exactly.
I know one of the researchers here likes
to watch computers play chess against each
other, and it feels like he sometimes
learns things from that.
Do you think that we'll learn to be better
mathematicians or researchers or
scientists or just thinkers in general by
watching the solutions the models come up
with?
Looking at 125 pages of thinking is
probably not very helpful for a
mathematician.
But just by looking at the answer, you
actually do learn some idea that you

[00:35]
didn't know before.
And that inspires later mathematical works
that knock down other problems.
So I definitely think people learn
something, like mathematicians learn
something from AI solutions.
Yeah, so some of the mathematicians that
we asked to review the proof together with
collaborators, they actually use the idea
to disprove some product conjecture, but
for real numbers.
I think that's one very good example.
AI can crack down important questions and
give us ideas that we can apply elsewhere.
Yeah, I think it's remarkable that this
group of mathematicians has already, just
in the span of a week, already used it to
disprove this result that I think is maybe
of similar importance to the unit distance
conjecture.
So I think this is a wonderful example of
mathematicians seeing this and using it as

[00:36]
inspiration and bringing the ideas to bear
on a different problem.
What does this mean for the mathematical
community?
I think for us, like when we do these
experiments, I think we want to like make
sure we like,
like empower the academic communities we
interact with, where we don't just like go
to some community and like, you know, from
the outside, try to like solve a bunch of
their problems and like give them a bunch
of like AI slop.
But what we really want to do is we want
to make these tools available to
researchers and let them direct, you know,
this like all this like AI test time
compute at the problems they think are
important.
And I think it's not, I think it's like it
really shouldn't be viewed as a race to
like, you know, solve as many Erdős
problems as we can.

[00:37]
But more like, you know, we want to like
make people aware that the technology is
out there. This is what it can do.
You're not trying to solve every Erdős
problem.
Yeah, I would not say that as our goal.
I think this has just happened to be a
particularly significant result that we
thought would be important to, you know,
share with the world.
that this is the capability level of
models today.
But this is like, it's really not the goal
to like, you know, just like go through
the list as if it were a race.
- Do you foresee things applying to like
cryptography?
And there's also some debate too about, do
these models get so good that we kind of
surpass even where quantum computing goes,
which sounds kind of crazy.
- Yeah, I think cryptography is really an
important topic these days because, you
know, the foundation of cryptography is
really about some problems like factoring.
It's hard to solve by computers, right?
But basically, we only have conjecture.

[00:38]
There's no mathematical proof of this
fact.
And suppose the model gets really good at
algorithms.
Maybe they will prove some of the
cryptography conjecture and say, "Okay,
those protocols are actually secure.
We don't have to conjecture them to be
secure."
Or maybe they'll find some loophole.
And that's also very important.
I think we need to make sure the
foundation of our security is good.
So the model can stress test the
foundation of the cryptography to make
sure we have better security.
What about quantum computing?
I think that's a very different territory.
Quantum computing, actually I used to
study quantum computing.
My first paper is on quantum advantage,
which shows like for some tasks quantum
computers can do better than classical
computers, but so far I think the models.
I mean that is classical computers.
I mean that they do what human can do I
mean maybe a bit better because I'm with

[00:39]
that we can sometimes do like more fancy
stuff like simulating some quantum
effect in chemistry, which we probably
not.
I'm not an expert on that, but that might
not.
It's unclear. It is just two different
paradigms.
So I'm not super sure how they compare to
each other.
But I think AI is going to greatly
accelerate the pace that we develop
quantum computers. In recent years,
there's improvement in error correcting.
You have quantum error correcting codes
that only uses simpler type of operations
and that really speed up the physical
implementation.
So I expect more of these to come from
collaboration with AI, that AI can propose
new quantum error correction algorithms
and then we can develop the quantum
computers much faster.
Once you ask the model to solve a
question, you can of course follow up with

[00:40]
how did you solve it?
can you explain this part of the proof to
me?
And then the model will patiently try to
teach you how everything goes line by
line. So it's actually not just one-shot
problem solving.
You can ask a follow-up question to learn
how the proof works.
And I really like that.
One thing you learn very quickly as a
researcher is that if your results are too
good to be true, you probably have a bug
somewhere.
I think every researcher has had an
experience where they see amazing numbers
from their experiments and it turns out
the experiment was actually wrong, the
numbers were wrong.
When I first heard about this from Lijie
and Hongxun, that was my prior.
I was like, "Oh, I'll wait for them to
find the bug."
But then I think as the days went on um is
you sort of like have this like growing

[00:41]
like optimism that oh like you know maybe
this is the one in a hundred times where
it's like it's like too good to be true
but it's it's actually true.
Well, gentlemen, thank you very much.
Yeah, thanks so much. Thank you so much.

</details>
