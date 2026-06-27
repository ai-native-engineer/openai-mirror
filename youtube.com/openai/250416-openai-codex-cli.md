---
title: "OpenAI Codex CLI"
channel: openai
url: https://www.youtube.com/watch?v=FUq9qRwrDrI
youtube_id: FUq9qRwrDrI
published: 2025-04-16
duration: "6:19"
captions: en-orig
---

# OpenAI Codex CLI

[![OpenAI Codex CLI](https://img.youtube.com/vi/FUq9qRwrDrI/hqdefault.jpg)](https://www.youtube.com/watch?v=FUq9qRwrDrI)

<details>
<summary>자막: OpenAI Codex CLI (6:19)</summary>

[00:00]
So what I'm thinking is maybe I can
start introducing codecs from here. Fuad
as always is like coding away in the
background and then he can join me for
the live demos. What do you think?
Sounds great. Cool. Let's do it.
Take one mark. Hey everyone, I'm Roma
and I work on developer experience at
OpenAI. What I love most is making sure
developers like you feel delighted and
inspired by the tools we build. Well,
today we're excited to give you a quick
look at something new. We've been
experimenting with the Codeex CLI.
Codeex is a lightweight coding agent
that can run directly from your command
line. It can read and edit files. It can
run commands securely and you can really
use it to build features or complete
apps from scratch. But enough talk to
see that in action. I'm gonna bring
Fouad over for some live demos.
Hey. Hey. Hey. How's it going? Great.
Hey everyone, I'm Philad. I'm on the
agents research team and I'm so excited
to share codeex with you all. Why don't

[00:01]
you uh kick us off with maybe like a
project that people might have seen
before. Let's say like open.fm that we
use as a quick demo lab for our voice
models. Yeah, let me go and pull up the
website openm I think it's an open
source repo, right? So I can just go
ahead and clone that locally and fire up
codeex. And so here we have codeex just
running on my machine. The cool part is
that it runs with any of our public
models. And since I'm not that familiar
with the codebase, I'm just going to go
and start off by asking it to explain
this codebase to me. And so what I'm
looking at here on the screen is that
you're using 03 that we just launched
today. Yeah, you can actually use
anything from 4.1 from a few days ago to
03 and 04 mini today. And I think one
really cool thing is as it's actually
calling these tools, it's running
commands. You can see it run the
commands directly on your machine. So
now we can see it put together this
whole description. I can see that it
described what open IFM is. It shows me
the code architecture that it's an X.js
application. And finally, here's how I
can actually run it. So, I'm going to go
ahead and run the development server.
And um did you have a use case in mind?

[00:02]
Yeah, I mean, why don't we do something
simple like dark mode for instance? Like
I know developers always love dark mode
and and maybe we can do something on top
of that. Sure. Let me go ahead and
codeex. This time I'm going to run it in
full auto mode. So, what does that mean
exactly? Full auto. Now, we can also
edit and run commands automatically. Got
it. An important point there to make
sure it still stays safe and secure is
that when you run it in full auto mode,
it's actually running network disabled
and sandbox the directory that you ran
it in. So, it's perfectly safe for you
to just be able to walk away. But, it's
really important for us to make sure
that our users stay in control when
you're actually running this on your own
computer. That's great. It sounds like
what we're talking it's changing all the
tailwind CSS uh and and making the
changes we want. Yeah. So one of the
nice things is that while I got this
high level overview in one step, I can
also had to go in and make very specific
changes without actually having the
context of where it's making those
changes. So I think the nice part is
that you know you as a developer can
actually use this to both understand the
code and actually make edits to it
pretty seamlessly. Now that it's done,
I'm going to go ahead and open up the

[00:03]
open FM. I can open it up locally and
boom, we can see it in dark mode. That's
amazing. You know, that's one example
where it's an existing codebase, but
maybe try something new. Well, now that
we've got we've gotten familiar with
with codeex with this one example, I
thought why don't we create something a
bit more fun uh from scratch this time.
A little bit like vibe coding complete
app from nothing. Sure. Uh is there one
that you like in particular on Mac OS
for instance? Okay. Yeah. Um you know
when I was a kid I used to go to the
Apple store and you know play with photo
booth. I don't know I don't often do
this but um so yeah let's actually pull
out maybe one of the filters in photo
booth. Okay. Yeah. How about how about
this page of filters? Yeah. So, are you
able to like screenshot the app and just
tell codeex that you want it like put on
the web? Exactly. So, I'm going to grab
a screenshot of photo booth and I'm just
going to pass it in.
So, this time I'm going to put it in
full auto mode
and it is a first reason about the
image. It's going to understand what
what is it even looking at. Okay, great.
It understands that it's a screenshot of

[00:04]
Mac OS. Yeah. Um, and now I'm going to
tell it reimplement this in a single
page HTML.
And maybe I want to say um, use the web
camera API and make sure it's in
landscape mode.
And so now it'll just go off and given
that context about the screenshot of
what I wanted. You know, this could be,
you know, a screenshot of photo booth.
It could be a screenshot of uh, Figma
design. It could be a lot of different
things. I've used it in different
contexts where I've drawn very low
fidelity mock-ups. Um and then just kind
of give in codeex uh here's this context
that I want and then go off and make the
changes. I don't have to give it any
additional context, any additional
direction. It'll just go off think for a
while. You can see its chain of thought
reasoning as it's thinking through the
problem. Both what commands it's running
and also what its thoughts are. And now
finally here we see the page. Now if I
go ahead and open that page in my
browser, I can go ahead and see that it
created this photo booth. And boom, we
have Oh my god, look how cool that is.
It's exactly the same. Is that amazing?

[00:05]
That's so cool. And I'm sure you could
have prompted your way to get such a
result, but just like one screenshot and
the model understood exactly what you
wanted to build. You didn't have to open
a code editor this entire time. It was
just all in our terminal. And sometimes
I'll kick off multiple of these in
parallel and just let them, you know,
one explaining the codebase to me, one
making some changes and it's just pretty
magical to see it all come together.
That's amazing. So it was just a quick
look at some of the features that we
have in Codeex. We've seen how it can
read and edit files directly. It can run
commands very securely and you have
different uh knobs in order to to pick
the mode that you're the most
comfortable with. But my personal
favorite feature is really that one like
the multimodal reasoning. That's really
the true magic of those reasoning
models. You just feed it a piece of
paper on a sketch or something and boom,
you have uh code being written for you.
Do you want to share anything about like
uh one more thing about this? Yeah,
there's always one more thing. We're
really excited to actually share codeex
with you. Fully open source. You can go
to our GitHub, you can see the Codex
repo, you can explore it, you can
actually use Codex to understand more
about the repo. And we're super excited

[00:06]
to hear what you think. Yeah. And Codex
works with GPT 4.1 launched on Monday
and with 03 and4 mini launching today.
So we really can't wait to see what you
build. Thank you. Thanks.
Okay, that was very good. Cool.

</details>
