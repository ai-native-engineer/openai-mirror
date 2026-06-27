---
title: "How PMs use the Codex app"
channel: openai
url: https://www.youtube.com/watch?v=6OiE0jIY93c
youtube_id: 6OiE0jIY93c
published: 2026-02-09
duration: "2:20"
captions: en
---

# How PMs use the Codex app

[![How PMs use the Codex app](https://img.youtube.com/vi/6OiE0jIY93c/hqdefault.jpg)](https://www.youtube.com/watch?v=6OiE0jIY93c)

<details>
<summary>자막: How PMs use the Codex app (2:20)</summary>

[00:00]
As PM of the team, I don't code that
often, so I like rarely understand the
code that's being edited, like and the
code around the code that's being
edited. So I kind of want to read up
on that before I look stupid in front
of the team. I actually want to be
kind of careful, like when you decide
to tag any engineer or even when
you want to file a ticket. In this
case, I saw, you know, there was this
button and it was kind of confusing as
to what it did. So my gut, my
immediate thing is to say, okay,
what does this button even do? I'm
just asking a question. So then I
pinged the team and I was like, hey,
this is a strange behavior to me.
I just confirmed that we don't need
this button. You know, I don't want to
go around deleting people's buttons
for no reason. So like, oh, we don't
need it. Okay, great. So I told it to
delete it. And actually I got
distracted and I was working on some
other stuff. Saw the change. We went
back and forth. So I created PR and
I saw that my PR got approved, but
there was a test failure. And, you
know, I have become so lazy. Like the
moment I'm like, oh, I better go into
like build kite and like, look at the
test logs. You know, it's like, ah,
yeah, but the app has all these great
skills. And so I could just click into
the skills tab and I'd just be like,
build kite. Okay. Sick. Someone is

[00:01]
like already figured this out for me.
So I'd be like, okay, let's go back to
this thing and just be like build kite
fetch logs. Why failing? And it told
me, okay, you need to install the
build kite tokens. So I did that. So I
was like, okay, I ran the command to
get a token now fix my PR. So what I
immediately did is I went to our main,
the top level folder in the repo,
which is where all the skills are. And
I just asked it to fix this problem. I
had to ask you how to set the build
kite token. I don't want you to have
to do that next time. So, you know,
read the rollout, reflect on what
might fix it and like update the
skill. I probably could have just said
update the skill, but I feel like kind
of helping it, like know how to think
through it results in higher quality,
especially because I'm often using
codex on low, which I think is like an
under underrated technique.
And so basically we,
you know, we went, had a bit of a back
and forth, but ultimately made an
update to the thing that is in a PR
somewhere. Just to summarize, like we
went through this inductive journey
where I was looking at user feedback
and I saw a thing, I asked the
question, realized this probably

[00:02]
needed to be changed. So then I like
made the change in, and then in making
the change at a PR failure. So, so
I used a skill to fix the PR failure,
but in the mean, then improved two
skills kind of as I went. And so
over time, codex just gets like better
and better in working on a code base,
which is pretty fun.

</details>
