---
title: "OpenAI DevDay 2024 | Community Spotlight | Mindtrip"
channel: openai
url: https://www.youtube.com/watch?v=Xjl2SqqrA4s
youtube_id: Xjl2SqqrA4s
published: 2024-12-17
duration: "9:26"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | Mindtrip

[![OpenAI DevDay 2024 | Community Spotlight | Mindtrip](https://img.youtube.com/vi/Xjl2SqqrA4s/hqdefault.jpg)](https://www.youtube.com/watch?v=Xjl2SqqrA4s)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Mindtrip (9:26)</summary>

[00:00]
-So I am Garrick Toubassi,
I am a co-founder of Mindtrip.
And I think more importantly,
I'm standing
between you and lunch.
So I have just a tight
90 minutes,
and if we all cooperate,
we'll get out of here.
Just kidding.
I'm going to talk to you
a little bit about
what we're doing at Mindtrip
with regards
to multimodal inputs.
And spoiler alert,
I will not be talking much about
the cool new Realtime API.
We've been doing
some prototyping with that
and I'll comment on that
at the end,
but mainly I'm going
to talk about all
the great stuff you can
do with the API you already know
and love, Chat Complete.
All right, so let's dive in.
First of all,
what the heck is Mindtrip?
So Mindtrip is your
AI-powered travel platform,
and we have this ambitious goal
to help you with the
full travel life cycle,

[00:01]
whether it's inspiration
and discovery,
planning, collaborating
with other travelers,
booking, and then on the trip,
et cetera.
So this is a big
expansive vision.
And this is my one
marketing slide,
my CMO will be happy
that I included it.
It also represents
the peak production value
of the whole deck.
So it's all downhill from here
But what really
are we talking about?
When we started ideating
around travel, we started,
as many people did,
with ChatGPT.
And believe me, I love ChatGPT,
use it all the time.
But when you're doing
travel planning,
you're left with, you know,
inert text, you know,
kind of leaves you
right at the altar.
You can't really plan the trip,
you can't really action it.
And so I think, with a lot of
LLM-based applications,
the challenge is,
how do you take that inert text

[00:02]
and make it actionable
and alive?
And so with Mindtrip,
we're able to connect
entities in the conversation,
put it on a map, et cetera.
We've got photos, we've got
reviews, bada-boom, bada-bing.
By the way, does this look
a little familiar?
Right? That Wanderlust demo.
So just for the record,
we were there first,
they saw an early demo of this,
and then asked if we didn't mind
if they do a little thing
in DevDay a year ago.
So that's pretty cool.
So a lot of what we're doing is,
you know,
taking the text,
making it alive and actionable.
Okay, that's great.
We then looked a lot at
how when people start
the travel planning journey,
where they get
that inspiration from.
And it turns out there's lots
of great content on the Internet
that can kind of kick
start travel planning.
But again,
we see the same problem.
There's a lot of inert,
unactionable content.

[00:03]
So whether it's like a blog post
or a travel article,
or whether it's
a long form video
or short form social video,
or even just
an inspirational image,
we want to make it so any
of these
can be kind of
the seed crystal for, you know,
useful, vibrant travel planning.
And so now it's time to bust out
of the deck and do a quick demo.
So here I am in Mindtrip
with a blank conversation.
Let's say that I stumble on
this cool, like, blog post
where someone is talking about
this really interesting island.
It's part of Portugal, but it's
in the middle of the Atlantic.
And so I can just go to Mindtrip
and say,
hey, plan me a trip based on...
Chugga, chugga, chugga,
and what we'll get is
a faithful representation
of that itinerary
in that article,
kind of in a structured form.
We've got things on the map.

[00:04]
Let's see
where the cool cave is.
So there's the cool cave.
You can see we've got a trip
that we've drafted up for you,
so you can kind of
mess with that,
and it's all kind of ready
to rock.
So that's interesting,
but the observant
audience member will notice,
we haven't done anything
multimodal.
We're still in the wheelhouse
of the LLM text.
All right?
So let's try something
maybe a little more interesting.
Let's say, instead of having
this blog post,
let's say someone sent
me an image,
or I stumbled on an image
on the Internet,
and I'm just going to copy
and paste this.
You know, you could upload,
drag, drop.
But let's say I start with this,
and now I've got, again,
a fresh thing, and I say,
I want to go to there.
That is a "30 Rock" reference
for those of you
that are
in the right demographic.
And so here we're sending
the image straight to GPT-4o.
Did you know you can do that?
Just send it right over.

[00:05]
And no PhDs necessary.
I've now got out-of-the-box some
interpretation of that image
and I've got some cool,
some cool stuff cooking there.
So that's images. Cool.
What about videos?
So videos come in
different shapes and sizes,
and I think you can tell I'm
a pretty cool, hip, young guy,
and so I love me
some snack-sized social videos,
you know,
often heavily caption based
with like a boozy soundtrack
in the background.
So I've got one
of those right here for you.
So for example, here's some...
[ "Until I Found You"
by Stephen Sanchez plays ]
Yeah, that's putting me
in the mood to travel.
So this is some recommendations
around London.
So I can go in here and say,
plan me a trip based on recos.
And we will recognize
that it's London
and start plotting
those things on the map,

[00:06]
and again, we're putting
together a draft itinerary.
So that's all pretty,
pretty sweet.
And let's kind of maybe dive
under the hood
and talk about that,
go back to the deck.
So First off,
just to be super clear,
the Chat Complete API has
two data types, image and text.
And so if you have images
you're dealing with,
it's worth kind of asking
yourself,
what is the semantic value
of the image?
If it's visual, like
in the case of that cool cave,
then you probably just want to
send it straight into a GPT-4o.
If what you have is
text content in the image,
you may want to do
a separate pass,
like a side conversation
to kind of do the OCR,
and then send
that resulting text
for final answer generation.
Videos are a little trickier,
since videos are obviously
not a native type
supported directly by the model,
so you've got to do
some shenanigans.
You've got to decide, again,
what semantic value
can extract from the video?
If you have
a high value audio transcript,

[00:07]
you can get
that audio transcript,
maybe you strip it off the video
with FFmpeg
and you can use a speech
to text API,
like we use OpenAI's
Whisper model.
There's speech
to text API that works great.
Now you've got text
and now you can work with that.
You may also have a video that
just has purely visual content,
in which case
you've got to decide
how you want to sample frames.
You can extract those
with something like FFmpeg,
send those to the model.
Or in the case
of that social video,
if it's text captions,
now you've got to figure out
how to sample frames
and do OCR on it
and send it over to the,
the resulting text
over the model.
Operationally,
just some minor details
which may be self-evident.
When you send images
to the model,
you can either give it a URL
or you can do it in line
as kind of a data URL.
We host them on S3
and send in a URL.
And then if you're doing
any kind of post processing,
like speech to text or OCR,
you know, you can cache those,

[00:08]
which means
if you've got a piece of content
that's a little, you know, hot,
then you know,
you save a little money,
you reduce latency for users,
which of course,
you know, is win-win.
And then finally,
a couple thoughts.
So we have had a chance to play
with the new Realtime API,
which is pretty awesome,
and it's a very different shape
of API,
but that's because it's
really a different beast
because you want to support
that Realtime,
and in particular the semantics
around doing interruption,
which is kind of
an interesting challenge.
So that's pretty cool,
we're excited about that.
And maybe from the demo
you saw earlier,
you might imagine
the kinds of things
we would do in our product
around real time audio.
But for us using images
and kind of the existing
multimodal capabilities,
that helps us connect
inspiration
with action and booking.
And I think just in general,
it's worth thinking about,
whatever
your application domain is,

[00:09]
is there existing content
in the ecosystem
that you can leverage to kind of
get the conversation started?
So you aren't just
putting people
in either pre-canned prompts
or, you know,
kind of the blinking cursor,
the blank page phenomenon.
So those are
just a few thoughts.
Any questions,
feel free to reach out to me.
And thanks for your time
and attention.
[ Applause ]

</details>
