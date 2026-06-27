---
title: "Automate tasks with the Codex app"
channel: openai
url: https://www.youtube.com/watch?v=xHnlzAPD9QI
youtube_id: xHnlzAPD9QI
published: 2026-02-03
duration: "4:35"
captions: en
---

# Automate tasks with the Codex app

[![Automate tasks with the Codex app](https://img.youtube.com/vi/xHnlzAPD9QI/hqdefault.jpg)](https://www.youtube.com/watch?v=xHnlzAPD9QI)

<details>
<summary>자막: Automate tasks with the Codex app (4:35)</summary>

[00:00]
So there is a lot about the job
isn't actually that fun that I have
now automated away almost entirely.
And so I'll show you a few of those
here in our automations tab. And we've
got a bunch running now, but we can
run down a few of these because I kind
of have set up a few different types
of automation. And the first type is
just sort of information. I'm asking
Codex to look at the last day of
commits into this section of our
monorepo. And basically group them,
tell me who worked on what, what got
done, what do I need to know about.
And so I wake up in the morning with
almost like a, if you've used JotGPT
Pulse, it's like a personalized pulse
that I walk, I open the app in the
morning and sitting there is like,
here's what happened yesterday in the
code base, which is super,
super useful. So I have one called
Upskill. And what Upskill does is
it looks at the last day of skill
usage. So it says, hey, skills are
really useful, but sometimes they take
a little bit of tinkering to get
right. And so it looks at Codex usage

[00:01]
throughout the past day and detects if
any skills, like if Codex had any
trouble with skills or if any of the
scripts didn't work correctly or if
like something could be sped up. And
it makes improvements to the skills.
So it's upskilling like overnight.
Like I'm going to sleep, I wake up,
Codex is smarter in the morning based
on what we're trying to do here.
Similarly, update AgentsMD, like
this I just have run every, I don't
know, six hours. And it just looks at
what we've been doing. And if there's
any like disagreements or
misunderstandings that I've had with
Codex or things where things took
longer to communicate than, or I used
some shorthands that Codex wasn't
familiar with, it will just add that
to the personalization. So that next
time things can just be quicker.
I've got a few others that are
integrated deeply into our other
tools. And so one of them is Sentry.
This is kind of a different type of
automation where it's going to go
through on whatever schedule, whatever
cadence, and it picks off one of the
top Sentry issues. So that could be

[00:02]
like a performance regression or
a crash or an error that's being
thrown in the app. And it like goes
through all of the information that we
have about it, the logs, the maps,
everything that Sentry has, it looks
at the code base and it picks
something to fix basically. And
automations have memory. So it
remembers what it tried to solve last
time. And so you're not going to get a
PR like solving the number one issue
every hour, right? But it's really
good because what this, you know, what
this type of automation does is it
allows us to focus on what is going to
make the Codex app great to use and
useful and joyful and all of the
things that like, you know,
bugs and things that fall through
cracks that like aren't quite as
fun to figure out, at least for me.
I know some people love it.
That stuff can happen kind of behind
the scenes, right? And so it's really
common that you run into merge
conflicts when you try to merge your
thing. And like you find, you know,
you iterate on your approach and

[00:03]
you've got like different types of
people giving reviews and then you're
finally ready to merge something and
there's a conflict. Your CI is failing
for, you know, some small reason.
You got to kind of dive into that. And
so I don't like dealing with any of
that. Maybe, you know. Most people
probably don't. Some people love doing
that and they work on CI tools.
But I have a green PRs automation here
that uses some of our skills. So
we use BuildKai, we use GitHub. And so
what this does is it checks if I have
any open PRs and I usually have like
at any given time between 10 and
20 PRs these days open at a time
because of the Codex app. Separate
problem. And this is going to go
through and it's going to say like, do
any have CI failures because of like,
you know, something that like linted
wrong or like didn't get caught in the
pre -push? Or maybe it's going to
merge conflict because someone is like
also changing it because we're rushing
to, you know, finish up a project or

[00:04]
something like that. And this is going
to go through and it's going to make
sure that all my PRs are green. It's
going to update the base branch.
It's going to intelligently resolve
merge conflicts by looking at like
what have people been trying to do. So
it's not just a factual like, you
know, I'm going to clean up the like
conflict markers. It can look at,
oh, like Joey was putting in this
feature. So we changed this block for
this reason. I'm trying to do this.
I'm changing it and there's a conflict
and like kind of knows how to do that.
And so that's a very long way of
saying my PRs are always green.

</details>
