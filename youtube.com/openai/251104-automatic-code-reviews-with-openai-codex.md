---
title: "Automatic code reviews with OpenAI Codex"
channel: openai
url: https://www.youtube.com/watch?v=HwbSWVg5Ln4
youtube_id: HwbSWVg5Ln4
published: 2025-11-04
duration: "8:20"
captions: en-orig
---

# Automatic code reviews with OpenAI Codex

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
