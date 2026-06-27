---
title: "Large Scale Reward Modeling | Jonathan Ward | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=EUZxw2VZUBA
youtube_id: EUZxw2VZUBA
published: 2021-05-10
duration: "14:49"
captions: en-orig
---

# Large Scale Reward Modeling | Jonathan Ward | OpenAI Scholars Demo Day 2021

[![Large Scale Reward Modeling | Jonathan Ward | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/EUZxw2VZUBA/hqdefault.jpg)](https://www.youtube.com/watch?v=EUZxw2VZUBA)

<details>
<summary>자막: Large Scale Reward Modeling | Jonathan Ward | OpenAI Scholars Demo Day 2021 (14:49)</summary>

[00:00]
Hey everyone, I'm Jonathan Ward and I've
been mentored by John Schulman.
Over the past six months at months I've
explored the possibility for large-scale
reward modeling.
So what this means in practice is how do
we learn what people want
and then build models that are better
able to do that.
So this this question really starts with
what should models do. So there are a
couple of domains we can think about.
There's the formal domain in which
specifying the task is really clear and
very simple.
This would include game playing, board
games, video games. So a lot of the
recent results in machine learning
around
beating Atari or various video various
other video games or chess or go have
really centered on these domains where
it's
really easy to provide clear feedback to
the model about what to do next.
But a lot of life is actually really
much more informal where specifying what
correct behavior looks like is much

[00:01]
harder to deal.
And this is really the area that I'm
going to be focusing on today.
So there's really a couple ways to
proceed
and I'll in particular contrast these
two. There's the idea of formalizing
what's informal. So this means trying to
write a function that somehow captures
the nuances of the problem at hand. So
this would include
things like Rouge or blue if you're
familiar with those terms in machine
learning. These are functions that are
essentially trying to measure
how good a summary is or how good a
translation is. But then there's this
other approach which is what I'll focus
on which essentially aims to understand
what's good by simply asking people
to compare two things or to rate
something. So this is the setting of
learning human preferences.
So the tricky part here is actually
getting these preferences, getting
feedback.
So there's a couple of ways of
proceeding and a lot of excellent work
has been done at Open AI um and DeepMind

[00:02]
as well on this setting of understanding
um how to use feedback and to train
systems to to incorporate that feedback
and improve their performance. Um, this
prior work has really focused on
interactive feedback. So, feedback where
you hire contractors and then the
researchers work with those contractors
to make sure there's a common
understanding and prior work has
demonstrated they can build accurate
models of human preferences using this
type of feedback.
This is however expensive.
Um,
but
one potential way forward is to use
feedback that's directly available on
the internet. And this is potentially
much less expensive,
can potentially
uh gather more of this data, and you can
potentially gather across various tasks.
So,
that's what I'm really going to be
focusing on. So, the operative question
is essentially, can we train an accurate
model of human preferences from feedback

[00:03]
that's gathered on the internet?
And so, just to reflect on that a little
bit more. So, with interactive feedback,
you get some benefits, right? Um, you
can make sure the contractors or
whoever's providing the feedback has a
similar sense of preferences that you or
the researchers or whatever the gold
standard you are for the true
preferences um
is So, you can make sure there's a close
match there. So, in some sense, those
are much closer. But, internet feedback,
you kind of get what's already out
there, right? So, if there's a lot of
ratings of one thing being better than
another, better stories, um
better
uh better question answers, then that
sort of model of what exists and what's
preferred
is is what you're is what you're capable
of learning from.
Um,
so then with this in mind,
um I really wanted to focus on more
structured, task-oriented
uh feedback. So, a lot of feedback in

[00:04]
the internet is generic, where it's sort
of scattered across various tasks. So,
like like on Twitter or YouTube, it's
not really responding to a specific task
performance on a specific task. It just
says that comment or that video was
good. Um
but for these task-oriented domains, you
can actually get a clear answer whether
a certain explanation or certain answer
to a question was good. So, uh there's a
very clear sense of input and output.
In particular, I'll be focusing on
Reddit. So, Reddit is the seventh most
popular site in the US, um
and it's organized into subreddits that
have particular tasks and particular
sort of uh
structures in the way that they give
feedback. So, they might value certain
things as a community.
And I'll focus on the community of
r/writingprompts in particular. So, this
is a community of short story writers,
um
and
it's structured in the form of a writing
prompt. So, you get a writing prompt if
you're if you're trying to respond to

[00:05]
one of these things. And it looks like
this. Uh a small dragon must defend his
hoard a single coin, and then people
will provide various responses to that
writing prompt. And each response will
get some number of
uh upvotes, downvotes, and together
they'll produce a resulting score.
So, these scores actually reflect some
measure of the aggregate preferences of
the people on r/writingprompts.
So, we can try to learn a model
of those preferences
uh using these scores.
And in particular,
there's a few models that I want to
train. So, the first model is
essentially the generative model. This
is the model that takes writing prompt
as input and produces a response. So,
this is somewhat analogous to someone
who's browsing the subreddit and writing
um
And then the next
model is the evaluative model. So, this
would be analogous to someone who's
lurking and provides like an upvote or

[00:06]
downvote
um on these stories. So, the evaluative
model gets the prompt, it gets uh two
responses to that prompt, and simply
outputs which of the two responses is
better.
And then the last model in this sort of
system that I'm considering is the
gameplay model, the the agent model. So,
this agent model starts off from the
generative model. So, it's just
something that learns to produce stories
that are similar to the stories that
it's seen.
Um but it's further trained using the
feedback it gets from the evaluative
model. Um so, the the evaluator
essentially provides feedback to
um one of two agents that are playing
against each other.
Um
And it provides that indication in the
form of saying which one of the stories
is better.
So, there's a sequence of models that I
trained here. I start with pre-trained
models. Um these are widely available
and provide a great starting point for
doing experiments.
Um I trained the generative model. Uh I

[00:07]
trained the evaluative model, and I
combined the generative model and
evaluative model to produce the agent.
And then ultimately, um
I can take those outputs, and I can make
them available to the public to you all
um for example, at rewardmodeling.com,
which is a a website I built for this
project. Um where I can actually gather
um some of your feedback on whether the
the output of this model actually
matches your preferences.
So, the um the most important result is
really how well does this reward model
generalize, or how well does it actually
capture
um
our preferences, our model preferences.
So, in order to assess this, we
essentially train this large model
on some number of comparisons, and then
we test it on a set of comparisons that
it hasn't seen before.
And then in particular for this project,
I wanted to make sure that the model

[00:08]
wasn't learning anything spurious,
wasn't learning
how preferences based on how long the
responses were, wasn't learning these
preferences based on how quickly they
were made. So, I removed several
confounders and I filtered down to a
hard test set of roughly similar
responses that were made at roughly the
same time.
And
with this, I actually received a final
accuracy model accuracy of 74.2%.
So, to place this number in some
context, right? It's worth thinking
about there's some inherent sort of
noise
in in sort of preferences. These are
preferences from a lot of people. These
are preferences that are gathered across
10 years of Reddit data. They might vary
over time.
Um, and to understand this closer, let's
take a look at this graph, which looks
at how this accuracy changes as we
increase or decrease the model size and
as we increase or decrease the number of
examples that seen. So, this on the
x-axis, this is the number of samples in

[00:09]
the training set. So, this is the number
of examples that basically sees before
it does the test, right?
And then on the left, you can see the
accuracy, which is its performance on
this test set. So,
I'll draw your attention to the
performance of GPT-2 Excel, which in
particular is the largest model that I
trained. Um, so, you can see here that
it actually learns the fastest of all
the models, but then it essentially
saturates at this performance of around
74.2%.
And there's a couple things that we can
think draw from there. Um, one is that
larger models simply learn faster. They
can just extract more meaning from the
data that's given to them.
Um
two, that there are continued gains from
from increasing the number of samples
that the model sees.
Um but this is most pronounced for the
smaller model sets.
Um
and then with this in mind, it's really

[00:10]
interesting to think about what happens
if we combine data sets um across
different subreddits. What happens
uh when we start to explore things like
transfer? And this is really where I
want to take this project next.
Um
so I think the the basic idea is um
what if we trained this reward model on
a lot of different subreddits, a lot of
different tasks, basically, and then
tested its performance on a task that it
hadn't seen before.
Um so in many ways this more closely
captures what we want out of a model in
reality.
Um
For a lot of tasks, we won't have the
vast amount of feedback that comes from
uh Reddit.
Um
For a lot of tasks, we won't be able to
actually gather um expensive human
feedback.
Um So what we really want is a reward
model that's been trained on
pre-existing
uh signals and then it actually performs
well on some evaluation that it hasn't

[00:11]
been prepared for.
And along these lines, uh you can think
of
like a a long-term direction for this
field is sort of being like gathering
feedback from the internet is almost
analogous to pre-training um
in the common sort of language modeling
setup. And then this interactive
feedback that people gather is analogous
to fine-tuning.
Um
in the sense that we can more carefully
construct this set of feedback.
Uh we can hire contractors with
particular expertise, or we can make
sure that they have what we have a broad
uh reflection of all the feedback uh
from different people groups that we
care about. Um and that way we can make
sure that the true preferences are more
accurately captured while also receiving
some performance benefit from using um
this internet feedback.
And with that I'll end on a bit of
caution or a note that um so like what
processes have we learned? So Red-

[00:12]
Reddit isn't really representative of
the globe, right? It's a it's skewed in
many ways, right? So if we actually
wanted a model that maybe represents
um
a very general sense of what we mean for
or something to be a good story or not,
we're going to have to balance out this
uh this data set, right? Um
and that will be important going
forward. We're going to want people with
more expertise in writing, and we're
going to want people with a whole lot of
different um influences.
Um so with that I'd like to thank my
mentor. I'd like to thank the other
scholars, especially Sam and Danielle
who donated a lots of computes.
Um I'd like to thank the organizers for
making this all possible.
Uh and then I will answer questions.
All right, so
how do you get rid of any concern of
bias on Reddit? So

[00:13]
um
I'll answer this one live. So
the I think the issue is you simply
can't. Um
I think the the way to approach that is
to actually balance it with
getting other data sets.
Um
like one one thing that I did to was I I
filtered out explicit explicit text. Um
but I think there's a lot uh
there are a lot of issues there. So,
I think the future of this is probably
balancing
the
the internet feedback with a more
curated data set of feedback.
Do I think the 75% accuracy ceiling is
due to the noise in the labels or
weakness of the models? Um, I'd say it's
it's potentially
a bit of
both, right? Um,
I would be very interested in seeing if
uh
if a
larger model with more capacity can move

[00:14]
past that, but it does look like a lot
of the models, like the various size
models, were converging around the 75%
accuracy. Um, so I I actually think it's
probably mostly noise in the labels. Um,
and I did notice that when I actually
uh added the the data of um
of when the response was made, the delay
between the submission and the response
to the uh to the language model input,
that the language model was actually
able to further increase its its
accuracy. So, it was able to take into
account both the text itself and the
speed of the response.
Um,
and with that, I think I'm at time. I
would love to answer any other
questions in the future, but um that's
it for me.

</details>
