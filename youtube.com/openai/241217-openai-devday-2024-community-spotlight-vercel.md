---
title: "OpenAI DevDay 2024 | Community Spotlight | Vercel"
channel: openai
url: https://www.youtube.com/watch?v=NA99SpQ--EA
youtube_id: NA99SpQ--EA
published: 2024-12-17
duration: "10:49"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | Vercel

[![OpenAI DevDay 2024 | Community Spotlight | Vercel](https://img.youtube.com/vi/NA99SpQ--EA/hqdefault.jpg)](https://www.youtube.com/watch?v=NA99SpQ--EA)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Vercel (10:49)</summary>

[00:00]
-I see a lot of friends here,
so we'll keep this
pretty casual.
I'm Jared.
I run the AI team at Vercel,
which includes v0
and the AI SDK,
which if you -- we're
not going to talk about today,
but you should check out.
We started Vercel to --
with kind of a simple mission,
which is to enable people
to ship amazing products.
And you'll note that the word
developer actually isn't
in that sentence anymore.
And that's going to be one
of the themes of today.
So if you don't know what v0 is,
it's a web development agent.
I guess that's the hotter way
of describing it.
It is also a
generative user interface AI.
So the generative UI,
if you will, system.
And it sits somewhere
in between a design tool,
and a coding tool,
and something that probably
hasn't been built before.

[00:01]
So today I want to
basically show you how it works,
but also talk about
the sort of shifts
that we're seeing
in the current landscape,
and how we are thinking about
this tool and where it's going.
So there's basically two themes
that we're going to talk
about today.
And the first one is a term
that I hope catches on,
which is the era
of personal software.
And this is, kind of,
an all-encompassing phrase.
But when you have sophisticated
enough code generation,
at the same time combined
with these new AI tools,
this allows anyone to create
anything just for them.
And that's just brand new.
And so it's kind of funny.
It's sometimes easier to create
software now than it is to,
like, go Google it, right?
You think about
those favicon generator
with all the ads,
or JSON preview, or all
these toy things that just suck.
Like, right,
like you don't want to use that.
You want to build
your own thing.
Well, now you
can actually do that.
And v0 actually helps that.

[00:02]
But it goes beyond just, like,
little toys.
You can imagine a situation
where what often would require,
let's say, tons and tons
of business analysts in Excel,
might be able to just like,
have an app
that gets generated instead.
I used to work at Goldman Sachs.
And so this rings --
this like, rings true for me.
Instead of having to go
build some like,
crazy discounted
cash flow model,
just have v0 generate
an app for it.
And we'll see some of that
today.
But at a deeper level,
personal software is
going to let us solve
higher level problems
by creating --
allowing us to create Meta tools
that we can use to solve them.
And so what I want to show
you today is
how we can use v0
to show off some of that.
And then take a sneak peek
of like,
some of the other --
the second theme,
which we'll get to in a moment.
So let's just
hop into some demos.
So I know realtime and
text-to-speech is like,
the big deal today, right,
which is an amazing thing.
An announcement
that OpenAI came up with.

[00:03]
So I'm super stoked about that.
But let's just show what
it would take to just do like,
a simple text-to-speech app.
Maybe I want to record a
greeting or something like that.
And v0 can help us there.
So it doesn't take much
to get started with v0.
I'm literally going to like --
I'm not even going to copy it.
I'm just going to take
some screenshots of this.
And this is, again,
the OpenAI documentation.
It doesn't really matter here.
I'll use CleanShot here.
And I can hop over to v0
and just say --
can we zoom in and see?
I think we can see.
Make a text-to-speech generator
using OpenAI in the browser.
And in this case,
let the user input
their OpenAI key directly.
And let's attach some images
of some docs.
Whoops.
Let's grab some docs there.

[00:04]
I just grabbed the wrong doc.
We'll take that there. Great.
And yeah,
let's see what happens there.
So v0 is now going to basically
generate an app for us.
And it is going to do that
as it streams.
It's super fun.
And when it's ready to render,
it's actually going to render
with real React code.
It's based off shadcn
and Tailwind.
And if it does use
external third-party libraries,
those work too.
Which is also really,
really useful,
as we'll see in a second.
So I'm going to --
so not only does, like,
v0 show me what it's building,
it's also explaining
how to use it, which is great.
So I'll enter in my API key.
And let's say, I love OpenAI,
and let's generate this.
And it looks like
it's not working.
Oh, well.
Demo gods are being annoying.
Let's see.
Make it work properly.

[00:05]
I don't even know
why it's not working.
Let's see.
So that's the right URL.
Let's try this one more time,
in which case
we'll go back to the fallback.
Ah! We screwed up,
but it's okay.
We had a working one.
Same prompt.
Let's see what the prompt was.
Make it text-to-speech
with OpenAI in the browser.
Make it figurable.
All right, it was clearly close.
Probabilistic code.
Still difficult.
My API key was --
Oh, that was the whole thing
the whole time?
All right. Here we go.

[00:06]
-I love OpenAI.
-There we go. Sick. It worked.
So yeah, it's a little toy app,
but I'll show you some more
realistic stuff that you can do.
At Vercel, we're very like,
v0-pilled.
So we've done stuff like --
I don't know,
if you ever need
the Vercel logo,
you can just grab it from this.
What's also neat about v0
is when I'm ready to like,
go live with this,
if I want to, I can publish
it directly and even get a URL.
So that's super fun.
And so now my site is live,
which is great.
And so now I have
a shareable URL.
So that's kind of great.
I can also fork existing ones.
But you can kind of go wild.
Like one of our engineers has
been like, cooking on this stuff
and built a full image.
Like, literally
an entire image generator.
So you can even -- all of this
is built with v0 and prompts.
So we can make memes here,
like Moo Deng got accepted to YC
by forking OpenAI.

[00:07]
I don't know. Let's see.
Did it do that?
Add text. Great. Fire.
What a sick meme. Amazing.
So people can create,
like, amazing stuff.
And you can fork this yourself
and even, like, keep going.
And so there's sort of
a TikTok-ification,
if you will, of code,
which has been fun and viral.
And people have done
some nuts -- pretty nutty stuff.
So it takes you
to the next point,
which is that while
this looks like a toy right now,
we're actually betting that it's
not going to be a toy forever.
And so we think about this
as like,
we're about to launch
these billboards in SF.
Which sort of play on words
about prompt engineering
and professional engineering,
and how these two things
are going to fuse together.
And so the rest of the demos
I'm about to show you are
actually pretty real world
and more material.
So we're about to have Next.js
Conf in a couple of weeks.
You should all come.
You're all invited.
And then one of the 3D artists
that we hired built
out this cool video animation.

[00:08]
And of course, the v0 team,
like, took that as a challenge.
Okay, how do we do this in v0?
And actually what is one
of our --
somebody from
the marketing department
actually cooked this one up.
And they did an amazing job.
They actually were
able to use React-three-fiber
to generate a pretty good
working clone prototype.
And what was also really fun is
that like, this is now forkable.
So I can go back here.
I can fork it -- --
if I wanted to.
And I can keep prompting
editing it.
And in the essence of time,
I'll show you what I did
before I got on stage here.
And I got -- let's see here.
Whoops.
My OpenAI.
Where's my fork?
Fork of CubeGenerator.
So I took that. I forked it.
And I made it for OpenAI demo
day with just like,
three prompts,
which is pretty awesome.

[00:09]
So I uploaded the OpenAI logos.
I then just prompted it to say,
like, make this for OpenAI.
And boom, like,
pretty much production grade
React-three-fiber
compatible code.
And what's really useful
is this code can be used
in your application
with just one command.
So if I'm working on Next.js
or any React application,
I can just copy this.
Pop open my editor,
paste this in,
and it will download
all the third party dependencies
and all of the React code
that I need to like,
ship this to production.
And so we envision this world --
and you'll see here
in components like,
here's the DevDay cube.
And we'd be ready to go here.
And so you can imagine
this world where
software is not just
personalized,
but also, like, democratized,
whereby every single person
in the organization
can work together.
And through prompting,
and code gen, and generative UI,
you can imagine that the --
what it means to be an engineer
or a developer is just like,
vastly different than what it
means to be a developer today.
You're no longer going to have
this like,

[00:10]
gatekeeping of who can code
and who can't code.
Of course, those who can code
will be God tier developers.
And those who can't code,
well, now they're going to be
able to be empowered to ship
and create amazing things.
And so I'm really,
really excited about
the other billboard
that we're about
to launch too in SF.
And that I'll read it
to you now,
which is that
everybody can cook.
And that's the second theme
that we hope --
that I wanted to talk
about today.
Which was that, this idea that,
through code gen,
through generative AI
and generative UI,
we're hoping that we can bring
and democratize creativity
throughout entire organizations.
So with that, I want to say
thank you to OpenAI
and thank you all for coming.
And check out v0.
Thanks so much.

</details>
