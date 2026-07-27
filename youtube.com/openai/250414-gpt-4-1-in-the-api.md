---
title: "GPT 4.1 in the API"
channel: openai
url: https://www.youtube.com/watch?v=kA-P9ood-cE
youtube_id: kA-P9ood-cE
published: 2025-04-14
duration: "23:12"
captions: en-orig
---

# GPT 4.1 in the API

[![GPT 4.1 in the API](https://img.youtube.com/vi/kA-P9ood-cE/hqdefault.jpg)](https://www.youtube.com/watch?v=kA-P9ood-cE)

<details>
<summary>자막: GPT 4.1 in the API (23:12)</summary>

[00:00]
Hey, I'm Kevin and I lead product at
OpenAI. Hi, I'm Michelle and I'm a
post-training research lead here at
OpenAI. Hi, I'm Ishan and I also work on
post training. All right, today we're
excited to announce GPT 4.1, which is a
family of models in the API that were
trained just for developers. And it's
three models. So, it's GPT 4.1, GPT 4.1
Mini, and for the first time, GPT 4.1
Nano, which is our smallest, fastest,
and cheapest model ever. Now, these
models are better than GPT40 on just
about every dimension. They're even they
even meet or beat GPT 4.5 in a bunch of
key ways. And for the first time, they
have long context. So, all three models,
even the nano model, can handle up to a
million tokens of context. We've also
got some fun pricing uh stuff to talk
about, but we'll save that for later.
And actually, the decision to name these

[00:01]
4.1 was intentional. I mean, it's not
just that we're bad at naming. It's not
just that. It's also that uh but these
models are better across the board.
They're great at coding. They're great
at complex instruction following.
They're fantastic for building agents.
So, let's dive in. Let's talk evals.
Let's do demos. You want to take us
away? Yeah, let's get started with a
little look at kind of the intelligence
by latency curves here. And the quaazar
or sorry the 4.1 series actually
improves a lot from 40. So you can see
40 and mini in here are in green and
then 4.1 we have these three new models
that kind of move that frontier upward
because they're much more intelligent.
You also can see that we have nano as a
new entrant in this area and it's much
faster but also you know really holds
its weight on intelligence. So that's
kind of the rough shape of the models
and you know when deciding when to use
them we recommend starting with 4.1 uh
and it's our kind of powerhouse for
these three dimensions coding
instruction following and long context.

[00:02]
Um but if you need something a little
faster you know for maybe a slightly
simpler use case I'd recommend 4.1 mini.
And then finally, nano is just an
absolute workhorse for, you know, tons
of applications like autocomplete or
classification or extracting, you know,
stuff from long documents. So that's
kind of when you should use each model.
Um, but let's get into coding first. So
you know, developers care a lot about
coding and we've been improving our
model's ability to write functional
code. Um, and so what does that mean?
We've been working on making it follow
diff formats better, explore repos,
write unit tests, and write code that
compiles. And actually uh SWEBench is a
really great eval for evaluating this
sort of performance. Kind of the model
is dropped into a Python repo. It's
given a task. It's got to explore, write
some code, write some tests. And we see
that GBT4.1 is a significant improvement
over our past models. It reaches 55%
accuracy, up from 33% from our previous
GPT40 model. And we think this is pretty

[00:03]
impressive for a non-reasoning model. It
even beats 01 and 03 mini. But uh
Swebench is all Python and we've also
improved this model's ability to code in
other languages and Ader polyglot is a
great benchmark for that specifically.
It's got a bunch of languages, but also
what's cool is that it's got a whole
diff format. Um so sometimes developers
want the model to rewrite the entire
file, but sometimes you want it to
produce diffs and that's useful when you
want a faster application. You know, you
save latency on the tokens that are not
changed. Also save money, right, on
Exactly. Um, and so here you can see
that we've really closed the gap on
whole and diff performance and we've
also doubled GBD4.1's diff performance
from 40. Um, you can also see that mini
is a really significant improvement over
GPT40 mini. So we think both of these
models will be a great uh great model
for any kind of coding tasks. Um, so
those are coding benchmarks, but there's
also kind of the intangibles of when
you're using a model. You know, when

[00:04]
you're creating a front end, is it
functional? Is it beautiful? Does it
nail the mark? And so for that, we have
uh a little example of a flashc card app
I've been making. You're learning Hindi.
Yeah, working on it. Uh and so I've got
uh you know a prompt here. It's pretty
complicated. I'm asking for this app
pretty specifically. I want a nice 3D
animation when you click on the flash
card. Um and so when I give this prompt
to GBT40, this is what I get. Um it
follows some of the instructions and and
some of the app is functional. Um, but
you know, we've really trained GBT4.1 to
do better. And that model, you can see
it looks way better. It's discovered
colors. Uh, it can also do the 3D
animation. Um, so we think you're really
going to like this improvement to
front-end coding. And this was just
based on that prompt that you gave it.
Just one prompt and you get back an
entire working application. It's pretty
cool. Um, but we've also been working on
instruction following. So, can you tell
us a bit about that? Yeah. So just like
coding, we have made the model way

[00:05]
better at instruction following. It now
strictly follows all the instructions
that you provided. So using all the
feedback that we received, we created
this internal instruction following eval
where it mimics all how an API developer
uses our model. So each sample in the
eval contains a complex set of
instructions where each instruction
belongs to one of several categories
like formatting, uh ranking, ordered
instructions, overconfidence and so on.
And collectively that sample is given a
difficulty rating from like easy, medium
and hard. And we see that this model
does really well across all those axis
and on difficulty levels as well. So
here you can see the hard subset eval
results. And this model is so much
better than the previous 40 model. So
what's an example of like a really hard
set of of instructions to follow? Yeah.
So let's say you're building a trip uh
planning application and you give it
instructions like make sure you receive
all the info from the user before
answering them. And when you answer with
the trip itinary, make sure it's in a
table format. It contains five rows,
three columns. The columns are formatted

[00:06]
in a certain way. Yeah. I I don't know
about you all. I remember all the times
that you have to you learn these tricks
in prompting where you're like, "No, no,
no. You really need to make this a
table, not a list. Trust me, my boss is
going to be super mad at me if you don't
get this right." So hopefully no more of
that. Yeah. And people actually were
doing that just so that they could get
the model to follow an instruction. None
of that is needed now. The model follows
all your instructions to the tea and
it's Yeah, it does really well. We also
have a new prompting guide now that
we'll publish on how to get the best out
of our models. Awesome. Um, and not just
internal evals, even on external
benchmarks like scales multi-challenge
eval that tests models instruction
following capabilities on multiple
turns. Uh, our model does really well.
So, for example, you might have an
instruction three turns ago and it tests
whether the model remembers that
instructions and continues to follow it.
So, it also tests models coherence and
memory. Um, these improvements also
scale well on long context data too. So
you could give it large corpus of data
and the be behavior that you're trying
to extract from the model, it'll
continue to follow that. Nice. Yeah.
Speaking of large corpuses, GBT4.1, Mini

[00:07]
and Nano are our first models to have 1
million of tokens in as the context.
This is up from 128K for our past
models. So it's a 8x improvement, which
is pretty big. But it's not enough to
just have the context. You want the
model to be able to use it effectively.
Um and so for that we're showing this uh
eval we created um which is a needle in
a haststack. We insert some kind of uh
text into a large corpus and we ask the
model to find it. Um and we see that the
model can find it across any depth. Uh
so maybe at the beginning, the middle or
the end of the the document and also
across the entire full length of the
context up to 1 million. This is a very
boring looking graph but it's boring in
a great way because it says every square
is actually working. Yeah, it's actually
boring through so much work, which is so
cool. Normally, you would expect to see
some of these be red, like you know, the
long context doesn't hold up to a
certain area, but the fact that all of
these is blue means that the model can
find what you're looking for. And this
is for all three models, all three
models, even nano. Um, so this is not,

[00:08]
you know, the end all beall of long
context. Uh, it's nice to find a
detractor in a in a long document, but
that's not exactly what all our
developers are doing. Um, so we've also
created an eval called OpenAI MRCR. Uh,
and this is a kind of more challenging
uh way of determining how well the model
does on long context. Um, so you can see
that GBT 4.1 in blue exceeds GBT40 in
green significantly up to 128K tokens.
Um, and it holds up quite well all the
way up to 1 million tokens. And this
this eval is actually really complex.
Can you explain a little bit more about
how it works? Yeah, it's pretty
complicated. So we basically create
these synthetic conversations where
there's a user and an assistant talking
back and forth and the user is asking
for things like give me a poem about
depear and then give me a poem about
frogs and then maybe give me a short
story about tiers and then we ask the
model uh find me the second short story
about peers and so you can find it's

[00:09]
pretty complicated. You have to not get
confused by the poems and the frogs and
find you know the second and not the
first one. Um, so we're really excited
about this improvement in performance,
but you can see that there's still some
work to do here. Um, and so as part of
that, we're publishing this eval on
hugging face today, uh, OpenAI MRC, and
we really want to spur on more work in
the kind of more difficult long context
uh, processing area. Yeah. Um, and then
more on multimodal long context. So
sometimes you're not just using text,
but you also want to upload a video. And
uh we found that on the video MME
benchmark, GPT4.1 reaches
state-of-the-art performance achieving
72%. Um so this benchmark is pretty
cool. You upload like a 30 to 60 minute
video without subtitles and the models
asked multiple choice questions. So
GBT4.1 is much better at understanding
this sorts of thing. All right. And then
one last hit on eval
uh on multimodal uh processing in

[00:10]
general. These models are a really
significant improvement, but the real
story is GBT4.1 mini. Um, this model,
you can see it really punches above its
weight uh on multimodal uh reasoning and
intelligence. And we think this is
probably the top model to be used uh if
you're doing any sort of multimodal or
image processing. Okay, amazing
benchmarks. But let's see some demos.
Let's do it.
So here we have the OpenAI playground
which is a really nice UI to iterate on
OpenAI's APIs. Um I've pre-selected the
latest 4.1 model and in the system
message I've given it a light identity.
The identity is it needs to produce a
single Python file code application uh
with very limited setup required. I also
told it that it has access to the latest
4.1 model which can handle up to 1
million tokens of input and 32K output.
So on the right we mimic a user query.
So the user is asking to make a website
that can take a large text file and
answer questions about it. We give it

[00:11]
very limited style guidance and we tell
it to use OpenAI's responses APIs to
answer questions about the doc.
So let's see it in action. So you're
having as part of the demo, you're
having it create a website and then
you'll use that website for the rest of
the demo. Exactly. Okay. Yeah. So now
it's producing like multiple hundreds of
lines of code. I've rerun this query
before and I have copied that the code
that it spits out into this app.py file.
So you can see it's a multiple hundred
line file. You see that the HTML has
been inlined in this file. Um if you
keep scrolling you would see there's the
upload code, the code to ask questions.
It's going to hit the responses API. So
the model did this just in one shot.
Yeah, it's doing that right now as
you're seeing it. Yeah. Just produce the
code. It tells you how to spin it up.
Cool. Yeah. Should we take it for a
spin? Let's do it. Yeah. Cool.
Okay. So, let's try.

[00:12]
Nice. What do you think? That looks
pretty cool. It's It's a little BDB
sassy, but I think it worked. I do like
that it uh advertises itself there at
the bottom. Powered by GPT 4.1. Yeah,
it's kind of neat. Just based on the
limited guidance that we gave it, it
produced this website. So to test the
log file that I'm about to upload, um
that file is NASA's server request
response log file from 1995 August. Let
me show you that file. You just have
this file lying around. Yeah, that's
don't you don't? I actually I prefer the
94. Oh, uh the 94 is a great version.
That's a good one. Yeah. So in this log
file, you can see the client name in the
left that made the request to NASA
servers. You see the time stamp, the
resource that was accessed, and the HTTP
response code. This is a long file that
contains a lot of log lines, and you can
see on the left that this is about
450,000 tokens of uh content here. Nice.
So, you just couldn't use this with our
past model. Yeah, this wasn't possible.

[00:13]
So, let's try uploading this
file. Now, what I've done is I've snuck
in a line that is not actually an HTTP
request response. Let's see if it can
find it. Very sneaky
view. Okay. So, it's a little needle in
the haststack except in this case you
don't even tell it what the needle looks
like. It's just figure out what's
different and tell me exactly. So, it's
going to sift through the whole file, do
some pattern matching to see how all the
log lines look like and then try to see
if there's one that does not look like
the others. Nice. And I really like this
thinking spinner. So this is just the
front end that we created uh in the demo
right before this one. Exactly. It's
like a nice actively going spinner. And
all the front end improvements also are
showing up here even in this like very
limited single page Python application
that we asked it to write. It doesn't
have access to like other additional

[00:14]
files that it could spit out for styling
or anything like that. So totally. Yeah.
I think this front end is is definitely
significantly better than what I can
make. So it meets my bar for sure. Yeah.
Yeah. And this spinning thing is kind of
neat.
Definitely taken a sec, but we're I
think we're almost there.
Any minute now.
Come on. 4.1. Live demos are awesome.
Okay, we made it.
Uh, okay. There is a line that it has
spit out that does not look like an HTTP
request line to me. It does not. Okay.
Uh, let's see if this line is indeed in
the log file that we uploaded. I'm going
to copy this keyword.
Nice. Here it is. Great. So, it was able

[00:15]
to find this line that has been snuck in
into this D4 450,000 token log file that
is like very hard to find. So, did
pretty well. Nice job, GBG4.1.
Let's look at another demo. Awesome.
Okay. So, here we are going to riff on
the previous demo that we saw, but this
one is going to be more focused on how
an API developer prompts our model. So,
I've again selected the 4.1 model here.
And here the the application's
personality is of a log analyst
assistant. We tell it how the input data
will be structured. So we tell it it
will be within these log data uh tags
and how the user's query would be
structured. So that would be in the
query tag. And then we have a set of
rules. So these are kind of the
instructions that a API developer would
provide to the model. So they are saying
that only answer questions about the
content within log data. Uh the question
should always be formatted within the
query tags. If any of those things are
not true, please respond with an error
message. The response should be in an
XML format. And I've given it some very
light guidance on how the XML format

[00:16]
should look like. So it should have some
tags like result, final answer,
references, and so on. Nice. Yeah, this
looks a lot like the system messages we
find developers use often. You know,
they're pretty meaty. Yeah. Um, and I've
preloaded the log file here. So this is
the trimmed version of the same log file
we saw earlier. Cool. So I first made a
request u saying how many requests were
made by fnal.gov of and it rejected it
because it was not formatted within the
query tags. Now I'm going to make the
same request within query tags and see
how it
does. Okay, now it was able to find the
two references that are within the log
file. So this is the kind of interaction
we see quite a bit with 40 where users
want a certain behavior and especially
certain behavior not to happen and the
model sometimes misses on it. So I have
an example. I made the same query to 40
and it answered the question instead of
saying that it needs to be wrapped in
query tax. Yeah, that's a key detail we
hear a lot from developers. You really
want it to follow negative instructions
and and do exactly as specified.

[00:17]
Exactly. Yeah. Super cool. Awesome. So,
great results on benchmarks. That was an
awesome set of live demos. I I know a
big amount of work has gone into just
making sure that this model is is really
good at the kind of day-to-day tasks
that developers face. and you and your
team have put a ton of time into that.
So maybe talk a bit about it. Yeah,
totally. Um, yeah, it's not an accident
that developers in the real world love
using these models. Um, to that end, we
kind of went with a data sharing program
last year where developers can opt in to
share their traffic with us. Uh, and in
exchange for free free credits and so
when that traffic comes in, we'll, you
know, scrub it for PII, remove any
identifying details, and then use that
to improve our models. And actually one
of the key things we do with that is
creating evals. Um and so the evals help
us tell like when we're creating a new
model, are we on the right track? Are
developers going to like this? And so
the eval Sean mentioned at the top
instruction following was directly
inspired by this. Um and so first I want
to say thank you to all of the
developers who've opted in. Thanks to

[00:18]
you opting in, we've been able to make a
much better model. And then what I'll
say for developers who haven't yet, uh,
if you want the models to get better for
you with no work on your part, I'd
recommend opting in. Yeah, it really
does help us build great models for you.
Now, we said we also would come back and
talk pricing. Uh, our mission is to
ensure that AGI benefits all of
humanity. And one of the things that
we've learned over and over is that the
more cost-effectively we can offer our
models, the more use cases you're able
to build, the more that you're able to
use AI to help people all over the
world. And so in particular, GPT 4.1
with all of the improvements that
Michelle and Isan have been talking
about is going to be 26% cheaper than
GPT40. And GPT4.1 Nano is our smallest,
fastest, cheapest model ever at just 12
cents blended per million tokens. And uh
going beyond what any of our competitors
offer, there is no pricing bump for long

[00:19]
context. So when you use our long
context models, you're just paying for
your tokens uh the same way that you pay
for a non-long context uh request. Now
uh one bit of uh you know, fun police
update here. Uh, we know GPUs are at a
premium. We want to make sure that we
can get GPT 4.1 out as broadly as
possible to all of you and we've just
been talking about how 4.1 beats even
4.5 on a lot of key benchmarks. So,
we're announcing that we're going to be
deprecating GPT 4.5 in the API. Not
today. It'll happen over the course of
the next 3 months or so, but we really
do need those GPUs back. Yeah, we're
really excited to get some back for
research. So, thank you. Yeah. And uh I
know we all love
GPT4.5. Uh a lot of the improvements
that we've made uh are going to continue
on in this model and in other models.
So, it has been a very successful
experiment. Now, we have one more

[00:20]
surprise for you. Uh I'm really excited
to invite Verun, who is the founder and
CEO of Windsurf, which is one of the
premier agentic coding uh idees out in
the market. Verun and his team have been
early testers of GPT4.1 and uh excited
to hear from you directly. How's it
been? Yeah, we got access to GPT 4.1. We
were super excited to sort of test it
out and we were very surprised with the
performance. Uh we have internal
benchmarks that are very similar to what
a SWEBench looks like that validates
endto-end software performance and we
found that it was a 60% improvement over
GPT40 which is a massive bump. Uh but
internal benchmarks only tell a part of
the story, right? Uh for our users, what
matters more than just getting to a
solution, it's actually the smoothness,
the interactivity when you're viating an
app or or modifying an app. Um and what
we actually found was GPT 4.1 has
substantially fewer cases of degenerate
behavior. And maybe a couple examples
here. We found the GPT4.1 reduces uh

[00:21]
kind of the number of times that it
needs to read unnecessary files uh by
40% compared to the other leading
models. And also it modifies unnecessary
files 70% less than the other leading
models. Um to top it all off, the model
is also surprisingly less verbose.
Right? These models sometimes tend to
blabber a lot and GBT 4.1 is 50% less
verbose than the other leading models as
well. Um, for all these reasons, we've
been super excited about the
performance. Uh, we decided to actually
go out and provide GPT 4.1 for free for
all of our free and paid users for the
week and also heavily discount the
product uh, immediately afterwards. So,
just to recap, in Windsurf, GPT4.1 will
be free, totally free for the next 7
days and then going forward will be
heavily discounted for a while. That's
exactly right. Awesome. Amazing. I will
say uh this weekend my 8-year-old
decided he wanted to start selling Legos
and so uh we opened up Wind Surf uh

[00:22]
opened GPT4.1 and we vibecoded a Lego
website for his uh his upcoming business
and it worked great. So uh you'll have
to send that over. Yeah, we'll we'll
post it with the live stream. I'm sure
everybody everybody is excited about it.
Um but thanks so much for joining us.
We're super excited to see what what
people build in Windsurf and beyond. So
that's today. We have a family of three
models, GPT 4.1, GPT 4.1 Mini, and GPT
4.1 Nano that are our smartest, fastest,
cheapest uh models that we have ever
built just in the API for developers. By
the way, you can also fine-tune GPT 4.1
and 4.1 Mini starting today, and Nano
will be uh available to fine-tune in the
near future. I want to say a huge thank
you to Michelle, to Isan, and to their
whole teams. These models are fantastic.
We're super excited to see what you all
build. So, uh, that's it for today. Uh,
these models are available now. Uh,

[00:23]
they're they're in the API. Please start
using them. We can't wait to see what
you build, and we look forward to
hearing your feedback. Thank you so
much.

</details>
