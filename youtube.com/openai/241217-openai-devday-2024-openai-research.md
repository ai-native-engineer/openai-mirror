---
title: "OpenAI DevDay 2024 | OpenAI Research"
channel: openai
url: https://www.youtube.com/watch?v=vlqEwE2wVr4
youtube_id: vlqEwE2wVr4
published: 2024-12-17
duration: "9:02"
captions: en
---

# OpenAI DevDay 2024 | OpenAI Research

[![OpenAI DevDay 2024 | OpenAI Research](https://img.youtube.com/vi/vlqEwE2wVr4/hqdefault.jpg)](https://www.youtube.com/watch?v=vlqEwE2wVr4)

<details>
<summary>자막: OpenAI DevDay 2024 | OpenAI Research (9:02)</summary>

[00:00]
-Hello, my name is Hung Won.
Today, with Jason,
we're happy to share
our thoughts on
how you can build with o1.
So o1 is a reasoning model
and we train o1 to think
with reinforcement learning.
And during the training phase
it learns, among other things,
to refine the thinking
strategies and recognize
and correct its mistakes.
So when o1 attempts to solve
a very difficult problem,
it may not get to
the working strategy in one go.
But just by trying on
a strategy,
even if it's unsuccessful,
can give some cues as
to what to try next.
And so o1 does this
and then eventually it gets to
the better strategy and so on.
So it's very patient and it's
a very different type of model.
And so last month,
when we released o1 preview,

[00:01]
we had showed
some of the examples
of actual chain of thought
going on.
So in this particular example,
we have the cipher text
that auto is trying to decipher
in some kind of a text.
And I'll show you
some reasoning patterns.
So in this case the model says,
hmm,
so probably it's
like recognizing
that this current thinking
strategy is not really leading
to anywhere and probably
trying something different.
In this case
the model tries something out
and then says, wait a minute.
So it's probably realizing
slightly better approach,
and then trying that next.
And then in this case,
the model has
more concrete idea to try out.
So it says,
let's test this theory.
And if after a while
the model gets to a
more correct situation,
correct like a strategy,
and says, it's perfect.
So the model behavior is very,
very different,
and in fact it's so different
that we believe
o1 represents a new paradigm.

[00:02]
A new paradigm changes
so many things
that I think we should think
about having a new perspective.
So what really changes?
I think a good starting point
to think about this question is
where we were,
and then, where we are now,
and where we're heading towards.
And so I invite you to think
about questions like these.
What just became possible with
o1 that wasn't really possible
with the previous generations
of the model?
And what will become possible
with the future versions of o1?
And obviously the answers
to these questions
will be very different depending
on the specific domain,
but just thinking about
these questions
will put you into a mode
of thinking where, okay,
now we're building
with the future models in mind,
instead of thinking
that the current generations
of the model will stay as is.
So you might say, okay,
I'm not building o1 myself,

[00:03]
so how do I know
what future generations
of the o1 might look like?
Unlike the previous paradigms,
o1 paradigm is much simpler
in that it's a reasoning model,
so its reasonings
will be just better,
meaning that it will be
able to think better
in pretty much anything
that requires thinking.
So with that,
I think it's useful
to think about
when you're building something
considering questions like this.
What would you want to build
if reasoning is 50% better
than what we have now?
What would you want to do
differently?
And then maybe more importantly,
what would you not want to build
if reasoning is 50% better?
And we have seen in many cases
that as the model gets
generally smarter,
some of the problems that we
think are difficult in the past
just became trivially possible.
So if we believe
that the reasoning will
just continually get better,
we should think about what
problems to not solve as well.

[00:04]
So with this new paradigm
I have been working for a while,
but I'm still really having
some trouble
because I'm so used to
the previous paradigm.
And so I think this
will be really useful.
I hope this sparked
some interest in thinking about
how to build with
this new reasoning paradigm.
With that,
I'll pass it on to Jason.
-Thanks, Hung Won.
I wanted to talk
a little more specifically...
[ Applause ]
I wanted to talk a little more
specifically about a few evals
that we've shown
in the blog post
that might guide you for
when you might want to use
o1 and o1-preview,
compared to GPT-4o.
So I think one of the best use
cases for models in o1 paradigm
are for extremely hard
math and code problems.
So you'll see in these bar
charts we have on the left AIME,
which is competition math,
and on the right Codeforces.

[00:05]
And there's these three bars,
so GPT-4o in teal,
o1-preview, and then o1.
And the thing to note here
is that GPT-4o and o1-preview
are barely solving a few
questions in these benchmarks.
And then you could see
o1-preview can solve
more than half,
and o1 can solve the majority
of problems in this data set.
So the point is there's
some subset of tasks
where GPT-4o is
really struggling
and o1 can solve the majority
of problems.
Here's a broader
evaluation suite
that we published
in the blog post,
and I'll highlight
a few things here.
So first,
if you look at the performance
on some of the math benchmarks,
so math from Hendrix,
Physics, College Math, LSAT.
There's a huge performance gain
when you use o1-preview
compared to GPT-4o.

[00:06]
And then conversely,
you don't get a huge
performance gain for every task,
so there's some tasks
like AP English Language,
Literature, SAT,
Public Relations,
where we actually don't see
o1-preview doing
a lot better than GPT-4o.
And so I made this table
that sort of summarizes
when you might want to use
models
from the o1 paradigm
versus GPT-4o.
So I would say the pros of using
models from o1-preview and o1
is if you're trying to do tasks
that are
extremely challenging prompts,
and in their domains of science,
math, and coding.
And the other use case would be
if you don't care about
any other constraints
and you just want
the best answer,
then o1 will likely be the
most performant model generally.
The cons here are obviously that
because as Hung Won mentioned,
o1-preview and o1
require time to think,
it's going to be
a lot more expensive,
and there's going to be
a much higher latency
when you use these models.
And then for GPT-4o,

[00:07]
I would say that's still great
for the majority of use cases
that people are
currently using the API for.
Obviously it's less expensive
and lower latency
than o1-preview and o1.
And I guess the con would be
that it's weaker than o1
on prompts
that require reasoning
or strong coding or math.
And then there's the question of
when should you use
o1-preview versus o1-mini?
And this plot here
shows the inference cost
versus performance
of a few of these models.
So you could see the
inference cost on the X axis,
and then on the Y axis
is performance on AIME,
which is competition math.
And interestingly,
we see that o1-mini is actually
strictly better than o1-preview,
and this is because we really
specialized o1-mini to be a fast
but performant model
on things like math and coding.
And I would say,
you should use o1-mini
if you're doing math or coding,

[00:08]
or if you want the answer
more quickly or cheaply.
But I would say in other cases,
o1-preview is a good choice.
Finally, I wanted to highlight
a few use cases
in the API of o1-preview
and o1-mini.
So I like this one from
the opening at Cookbook here.
It's basically a medical
and accuracy detection.
So you've given a bunch
of information and diagnosis,
and then o1-preview
tries to detect
whether it's a correct diagnosis
or not.
Obviously coding is
another great example
of o1-preview shining.
So for use cases like Cursor,
I think o1-preview
would do a great job.
Hard sciences research is
another great use case
that o1-preview is
particularly strong at.
And we've also heard
that these models have been good
as a brainstorming partner
on math problems
or on legal domain reasoning.
So I'll end here, and enjoy
using o1-preview and o1-mini.
Thank you.

</details>
