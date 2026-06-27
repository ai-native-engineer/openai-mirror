---
title: "Codex checks its work for you"
channel: openai
url: https://www.youtube.com/watch?v=dHCNpcNyoFM
youtube_id: dHCNpcNyoFM
published: 2026-02-11
duration: "2:24"
captions: en
---

# Codex checks its work for you

[![Codex checks its work for you](https://img.youtube.com/vi/dHCNpcNyoFM/hqdefault.jpg)](https://www.youtube.com/watch?v=dHCNpcNyoFM)

<details>
<summary>자막: Codex checks its work for you (2:24)</summary>

[00:00]
I've been a huge fan of Codex for a
lot of last year. Really dramatically
changed how I work, how I build
software, and the app has been another
step change, and it's made my job even
more fun. I trust that it's going to
make a lot more progress in one go
without, you know, babysitting or
handholding. And especially its
improved ability to validate the work
that it's done to write the code and
then, like, automatically run tests or
even launch the app and do checks like
that. It means that when I get back to
that session and it says that it's
done, a lot more of a time, you know,
it's not just, hey, I wrote a bunch of
code and now, you know, you have to
build compiler errors or whatever it
is. But actually, you know, this code
works and, you know, might need some
refactoring or polishing, but, you
know, I can immediately start testing
this thing that I asked to build. And
that's been just transformative for
all sorts of work. So this is a
task where I've been doing a little
refactoring related to logging. And
this is one of those tasks where Codex

[00:01]
can really excel because there is,
it's not a complicated task, but
it does, it did require modifying a
lot of files. And there was also a bit
of risk where you're modifying, you
know, sort of a crucial component of
the app where our regression in this
case would have meant our logs stop
working and, you know, our
observability pipeline breaks, right?
So our ability to see the logs in the
beta version of the app so we can
diagnose back reports would break. So
then the way that I would have done
this before Codex is, you know, I've
made a change. I'm going to compile
the app and run it and look if the
logs are there, right? So in this
case, I just told the model and we can
give that a try. I can see it using
our logs tool
and it's querying some logs. It ran
the app and then it tried
to find the session ID by
writing some Python code. It found
right here. Nice. And then now it's
using the old logs MCP to go
and query that. Yeah, so I just came

[00:02]
back to our conversation and the
model's telling me that it ran the
command that I told it, it found the
session ID and then it ran this and it
found some logs statement. So I can
tell that after our refactor, you
know, logs are still being piked. So
awesome. That's a piece of work that
it just takes to me. That's very cool.
Like 10 minutes on this task.

</details>
