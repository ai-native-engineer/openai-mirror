---
title: "Build Hour: Prompt Caching"
channel: openai
url: https://www.youtube.com/watch?v=tECAkJAI_Vk
youtube_id: tECAkJAI_Vk
published: 2026-02-18
duration: "56:03"
captions: en-orig
---

# Build Hour: Prompt Caching

[![Build Hour: Prompt Caching](https://img.youtube.com/vi/tECAkJAI_Vk/hqdefault.jpg)](https://www.youtube.com/watch?v=tECAkJAI_Vk)

<details>
<summary>자막: Build Hour: Prompt Caching (56:03)</summary>

[00:00]
Hey everyone, welcome back to OpenAI
Build Hours. I'm Christine. I'm on the
startup marketing team and today I'm
here with Erica.
>> Hi, I'm a solutions engineer at OpenAI.
>> So today's session is about prompt
caching. Um, and this is one of the
fastest ways to cut latency and reduce
costs. So I'm really excited we're
diving deep into this topic today. So
quick context on what build hours are
all about. Um, it's really to empower
you with the best practices, tools, and
AI expertise to scale your company using
OpenAI's APIs and models. Um, everything
that we're covering today is really
designed to be immediately actionable.
So, you're going to see a lot of live
demos, um, as well as a customer
spotlight today to show how we actually
do this in practice. And if you want to
follow along and share this with your
team afterwards, you can always find
builds at our homepage webinar.
/build hours. Okay, so let's jump in and
give you a preview of everything we're
going to be talking about today.

[00:01]
So, here is the agenda. Um, and it's
really structured to show both the
foundation and practical tools to start
using prompt caching effectively. So,
first we're going to go um with prompt
caching concepts. So, this is going to
be 10 minutes. It's going to focus on
the foundation, the mechanics behind how
caching works, and then a quick API walk
through to understand what's happening
under the hood.
And of course, we're going to bring this
into practice. Uh, today's live demo is
extra fun. It's going to be on an AI
styling assistant. Um, but we're really
going to show you how to use um, batch
image processing, branching chat, and
then longunning compaction in action.
Um, and so this is like a real workflow
and whether you're a startup, a
developer, you can see how that applies.
So then as we're going through this
demo, we're really going to show you um
this like developer playbook. And this
shows you the tips on how to maximize
cache hit rates and things like um the
pro prompt cache key, context
engineering, endpoint selection, tool

[00:02]
usage um and so on. [snorts] And then
I'm really excited. We have um a
customer spotlight today on warp. Um and
this is going to be a realworld example
and they'll show you actual impact and
metrics on how they've used prompt
caching and how that's really changed
their workflows. And finally Q&A. Uh we
do have some time for Q&A, but
throughout the session feel free to
submit these via the text box so that we
can answer them live and then save a few
for um answering on on air with the last
few minutes that we have. So with that,
I will turn it over to Erica. Thanks,
Christine.
Okay, why prompt caching? I will say I
love deep diving on prompt caching
because in my role as a solutions
engineer at OpenAI, there's really three
things that I talk about with customers.
It's intelligence, latency, and cost.
So, how can I make things faster,
cheaper, smarter? And prom caching is a
way that you can influence your latency
and your cost with no negative impact to

[00:03]
intelligence. So I think it's kind of a
no-brainer as you become more
sophisticated in architecting your AI
applications to think about prompt
caching. So I'm going to start with an
overview like what is prompt caching and
then talk about how it actually works at
OpenAI.
So essentially prompt caching is compute
reuse. When multiple requests share the
same prefix, we skip fully processing
those tokens and only spend compute on
what we haven't seen before. And you'll
hear me say prefix a lot today. By
prefix, I just mean the inputs you've
sent us before. So that's like your
system prompt, images, audio, messages,
etc. That's what we're calling prefix.
So I want to talk about like 101 basics
of caching. Essentially, caching starts
at 1024 tokens. If you send us a 900
token prompt, we're not caching. So,
once you send us 1024 tokens, we will
start caching blocks of 128 tokens. And
cachits require a contiguous prefix. So,

[00:04]
we have to see everything in the exact
same order as you sent us before. Like,
that is the number one key here of
caching is send us the exact same stuff
in the exact same order. um eligibility.
It's on check completions, it's on
responses, and it's multimodal. So, we
will cache audio, text, images, and it
happens automatically. It's what we call
implicit prompt caching. Um you don't
have to do anything. There's no uh
changes to your code. Um and there's no
cost. Um by default, our cache is
ephemeral in memory, 5 to 10 minutes,
but we have a new extended prompt
caching. So you can pass us a parameter
and we will store your cash for up to 24
hours. And then there's a ton of
optimization. Right? These are the
basics, but we're going to spend the
rest of the build hour talking about how
you can maximize for your cash hit rate.
[snorts] And like I said, there's two
main things that we care about. Like
there's two main impacts of prompt
caching. The first is pricing. So when

[00:05]
we introduced prom caching with the 40
model family we gave a 50% discount with
41 a 75% discount and then with the five
model family and on it's 90% discount.
[snorts] I like to throw GBD realtime on
here because um audio caching on our
speechtospech model is almost 99%
of a discount on cash tokens. So the
more you can increase your cash hit rate
and have those cached input tokens, the
more you can save. This is a huge
incentive to focus here. And then the
other piece is latency. Um so this chart
I ran 2300 prompts variable length
between 1024 and 200,000 tokens. You can
see on the left hand side um there's
kind of like a smattering of green and
red dots. time to first tokens like
roughly the same about a 7% difference
for those cached prompts. Whereas if we

[00:06]
look on the right hand side and you can
see this sharp increase for the uncashed
requests, it's like 67% faster for these
super long prompts. The longer your
input, the bigger impact of caching on
time to first token. So you can kind of
see that green line is roughly flat
because caching keeps latency roughly
proportional to the generated output
length rather than the total
conversation length.
Okay. In order to understand the
optimizations and the developer tips
that we're going to cover, I think it's
really important to take just a few
minutes to talk about what attention is.
What is in this cache? Like what is the
cache?
So attention is the mechanism that lets
a model selectively focus on the most
relevant parts of the input when
processing a token. Right? This is kind

[00:07]
of like the heart of the transformer
model. Attention is all you need. Its
purpose is to build the best possible
representation of the current token by
integrating all the prior context since
that representation is what's driving
the next token prediction. And each
block and this is like the most
simplified possible version of inference
here on the right. But each block
contains two main components. There's
the self- attention layer and the feed
forward network. That's like the
multi-layer perceptron. And in self-
attention tokens are determining what
they need to know about the other
tokens. In the feed forward network,
each token's representation is going to
get refined through linear and nonlinear
transformations, but like that's out of
scope for prompt caching. We just care
about attention today. So, as tokens
move through these stacked layers, like
a model might have 32 or 64 layers, the
representations become progressively
richer. And this is all parallelized
matrix math. Like this is why we need
GPUs.
Um to perform self attention, each token

[00:08]
embedding is projected into three
vectors. A query, a key, and a value.
And the query represents the information
the token is looking for. Basically like
what do I need to know about all the
previous tokens to contextualize myself
best. The key represents uh what the
token contains like who am I? What do I
represent? Am I a verb? Am I a color?
And the value represents the information
that it can contribute if it's relevant.
And these projections are learned linear
transformations parameterized by weights
and biases that are optimized during
pre-training. And these are specific to
each model. And when we think about
model parameters like this is what we're
talking about. So the model's computing
similarity scores between the query, the
query, and the key like how relevant is
that previous token. And that way the
model can pull in the most relevant
signals from earlier words instead of
treating all prior words equally. And
that's how context disambiguates
meaning. For example, when we're

[00:09]
thinking about the word river, it's
going to shift the internal
representation of bank like riverbank
towards its geog geographic sense rather
than the financial one.
And without caching, we're basically
redoing all this matrix math that we
need all these GPUs for. Like we don't
want to do that. We want to reuse that
work that's already been done. Um, and
essentially what's in the cache, it's
basically just a giant pile of floating
point numbers. Like we're not storing
tokens, we're not storing embeddings.
Um, this is what's actually in the
cache. So I want to talk about what
happens when you actually send OpenAI an
API request. We think this is key to how
we're thinking about what optimizations
to make. So here's the flow that
actually happens when you're making a
request to the responses API. Um so
first we're going to compute and hash
the prefix um and and check that hash in
our routers. So what does that actually
mean? Like are we storing the tokens?

[00:10]
Are we looking at your first prefix like
that first part of your prefix? No.
We're hashing that first 256 tokens and
we're using that and optionally the
prompt cache key which is an optional
parameter you can pass us to actually
route to the right machine.
We're going to select an engine. So, as
you might imagine, you can't send 10 or
100,000 requests to be processed on a
single GPU. Each engine can only handle
about 15 requests per minute. And this
is really key when we're thinking about
some of these optimizations. We're
always going to prioritize engine
health. Um so we will sacrifice some
cash hit ratio by distributing traffic
and that's what's really going to get
everybody the best time between token um
for that balanced utilization. Okay. So
we've selected our engine. If we've seen
your prefix before, we're going to fetch
that and then we're going to look at
those future chunks. So, we looked at
your first 256 tokens, the hash of that,
and now we're going to look in those 128

[00:11]
token chunks to see um how much have we
already seen before. So, right, we you
we could have 100,000 tokens in the
cache. We're going to keep looking until
we see that first mismatched token.
Everything after that is going to be
considered uncashed. So, the engine is
going to say, "Okay, what have I seen
before? Oh, I see this is my cache it
hit it. Here's my new content." And then
it's going to do inference over
everything that it hasn't seen yet. So
my super highlevel inference TLTR at the
top. We're going to tokenize. We're
going to go through embeddings. We're
going to go through attention, the MLP
blocks, linear projection, softmax, and
then we're going to get our predicted
next token, which is the whole point
here. What's that next token? And then
lastly, we're going to update the cache
to include the outputs that the model
just generated. So the next time you
make a request, it has everything
everything you've sent us and everything
the model generated in the cache ready
for your next request.
Okay, awesome. Before we get into

[00:12]
developer tips, um I want to do a quick
demo just to highlight the difference
between no cache and cache. So I have an
AI styling assistant uh this retail tech
startup I've just started. One of the
things I need to do is process a super
high volume of images in bulk. Same
prompts over and over again. It's just
the images that are going to change.
Okay, super um small uh diagram I hear I
have here. Essentially, when we're
thinking about caching, it's like what
is static? What is dynamic? In this
case, what is static is my standard
image processing prompt. It's like about
2,000 tokens. And then what's dynamic?
gets all the images I'm passing in.
So, I'm going to pop over to this demo I
built. There's a lot to look at here.
So, we're going to walk through it.
Essentially, what are we doing? We are
analyzing all of my images at scale. We
can see my input schema. Essentially, I
have the system prompt so that I can
pull all the information I need out of
my images. And then I have this long

[00:13]
response format schema that I'm going to
pull back. I'm going to click on run
comparison so we can let it run while
I'm talking. But essentially, we have
three variants here. We've got a cache
break scenario where I'm actually
preventing caching by inserting a
timestamp. And that might sound kind of
like arbitrary and obvious, but we've
actually had customers who accidentally
were including spaces, including dynamic
content, including a timestamp, which
meant it that they're breaking the cache
on every single request because the
start of your prompt is new on every
request. And then the other two things I
have here are cache. So I'm allowing
implicit caching. I'm not doing anything
different, but I have prompt key on or
prompt key off. And we're going to get
more into this parameter, but uh what
you need to know about this is it's
helping us route to the right engine.
Okay, great. So, looks like we're still
running. Let's pull up the cards. Cash
break is almost done, but you can see
immediately off the bat that including

[00:14]
this prompt cache key like key auto, we
can see we have a higher percentage of
our cash. So just normal implicit
caching, I'm not doing anything, just
making requests and not purposely
breaking my cache. I've got a 75% input.
And then if I have a cache key, I'm
getting an 83% input. And then as
expected, if I'm breaking the cache by
inserting a timestamp, I am at a 0%
cash. So we can see just immediately the
difference between the cost. We have 35
cents to process these images, just no
cash. We've got 22 almost 23 cents for
the cash with no key and then we have 21
cents for the cash with a key. So a huge
cost difference between no cash and cash
and honestly a significant difference at
scale between including a prompt cache
key and not including it. And as we can
see like my time to first token is
roughly the same because when we're
thinking about that latency chart 2,000
tokens is pretty small. So latency isn't

[00:15]
the impact here. It's really cost.
Okay, let's get into it. Um, we're going
to talk about some of the key tips that
I have that we've been working with with
customers on actually enhancing your
cache rates. Um, so five main things
we'll talk about. The prompt cache key,
that's super important. context
engineering. What do you need to think
about when you're doing context
engineering? Truncation, summarization,
AP endpoints, API endpoints, tool use,
and then the extended prompt caching
parameter. So, let's start with prompt
cache key.
Essentially, this is an optional
parameter you can pass into requests.
We're always going to cache
automatically, like you don't have to do
anything, but prompt cache key helps
when you have a lot of similar requests.
Remember, caching only works if a
request shares the same prefix and lands
on the same machine. So, we're going to
hash the first 256 tokens. That's where
we're going to identify what engine to

[00:16]
land your request on. But, if you send
thousands of requests with the same
prefix, we're going to have to spread
those across machines for load
balancing. So, your uh cache key hit
rate is going to drop. If you pass us a
prompt cache key, we're going to hash
the prefix plus that key. So you can
kind of intentionally group related
requests so they route to the same
engine. We had a coding customer who
started using prompt cache key and their
cash hit rate jumped by from 60 to 87%.
So a huge increase by starting to
leverage prompt cache key. Now reminder
here, we're going to combine it combine
it with the prefix hash. And I think
this is especially helpful because you
might have uh 256 tokens in common with
a lot of requests. But what happens when
you have variable content after that
initial hash? That's what we're going to
look at in this next uh demo. So when I
say branching chat, what am I thinking
about here? Well, let's pop back over to

[00:17]
Excal.
Now, I have as part of my a AI styling
bot a live chat so that I can offer
support to all of my users. I have a
static standard prompt that I'm going to
be using. Uh that's just like
information about my brand. That's going
to be in every single chat request. I'm
going to provide that to my uh customer
service agent. But then there's two
options, right? Users can go into
support. They can go into styling. And I
have dynamic prompts given where a
customer is going. Are they going to
support? Are they going into styling?
I'm gonna have like 5,000 tokens that
are different for those two flows. But
if we're only hashing the first 256
tokens, like that's going to get those
are going to get mashed together. So I'm
going to actually only really be getting
that 3K in common. So I'm going to pop
back into
our demo and I'm going to choose my

[00:18]
standard chat here. So, what are we
simulating? I'm simulating that I have
30 users. They're going into my live
chat. 15 of them are going to be going
into support. 15 are going to be going
into styling. And then we have five
turns each like they're, you know,
chatting about their order, etc. So, I'm
going to run the comparison on these.
And the variants we have today are uh
cache break, cached with a key, and
cached with no key. So, I'm adding a
key. I've got two prompt keys. I've got
one for my support and one for my
styling. And then cached, right? I'm not
breaking my cache, but I'm not doing
anything with the key. It's off. And
then our cash break scenario tragically
continues to have a 0% input. Very
expensive. So, we can see here it's a 31
cent cost for these users to go through.
And then we have a difference of 7% by
including my cash key. So a 7% increase
corresponds from 11 to 9 cents to

[00:19]
process this. Again, roughly similar
time to first token. These aren't super
long prompts, but you can see that if
you can think about how your application
has branching more than that first hash
branch branching amounts of dynamic
content, how important it's going to be
to think about your prompt cache key
carefully. And let's get back more into
prompt cache keys. There's more than
just that initial um kind of uh thought.
I want to talk about coding customers
because I think this is really
important. You're going to have huge
codebase contexts, tool schemas,
instructions, and you might have users
asking a ton of questions about the same
codebase or maybe you have users that
are working across a ton of different
code bases. So variable context that
you'd be providing to the model. When
we're thinking about how you might
leverage a prompt cache key in that
scenario, there's kind of two options.
One might be a per user key. So if you
have a reuse across codebased

[00:20]
conversations, you might want to think
about a per user key. Whereas per
conversation key scales better if you
have users who are in unrelated threads.
And um like I said, we have a coding
customer who increased their cache hit
rate by 27% by being intentional about
how they were using prompt cache key
here.
One thing that might be helpful and if
this is not helpful you know ignore but
it it can be helpful to think about a
prom cache key like a shard key in a
database because uh fundamentally it's
about controlling distribution and
locality.
Remember engines can only handle 15
requests per minute. So if you're
exceeding a common prefix and prompt
cache key we're going to spill over to
new machines. So think about how you're
choosing that granularity to maximize
knowing that this is a kind of
restriction um kind of like a basic
restriction of our inference. But even
if that happens, you're just going to
get that single cache mix miss. So every

[00:21]
time you go to a new engine, you'll have
that first request be uncashed and then
subsequent requests will be cached.
Again, if you have a coding workflow or
other kind of related long context use
case, think about how you want to define
that prompt cache key. Is it per user?
Is it per conversation? Or maybe you
want to group users by keys. Like maybe
users don't have that super high volume
of requests per minute. You want to max
out that 15 RPM. So maybe you group
users and figure out how you want to
bucket um kind of like by that grouping.
Okay, cool. Context engineering. The
longer we get uh these 24hour running
agents, the more important dealing with
super long running contexts is. Um so we
want to balance the optimization of the
cache and cost against how you're
thinking about doing context
engineering. Context engineering is

[00:22]
fundamentally about dynamically shaping
and curating what the model is seeing.
Whereas prom caching is really about
keeping everything the exact same as
what the model has seen before. So I
think it's kind of funny because context
engineering and prom caching are sort of
like inherently at odds. Um
>> very low. Um, so we want to think about
uh how big of an intelligence boost or a
token savings are you getting to make
the cash invalidation worthwhile?
Okay, context engineering versus versus
cache preservation. Every model has a
context window. Maybe it's uh 400,000
tokens, maybe it's a million. right now
uh kind of naively the responses API
will either truncate or fail the request
based on the parameter you're passing
in. So it's either going to just uh kind
of naively cut as many turns as much
context as it needs in order to stay
under the context window or it can just
fail. Um but hitting the context window

[00:23]
isn't the only reason that you would
want to manage your context. Like
fundamentally the more context you
provide to a model the less accurate it
might be. The more more tools you
provide, the harder it is for the model
to choose the right tool. So careful
context engineering is really important
to keep your agents reliable.
And we now actually at OpenAI have two
new ways to manage compaction. We have
serverside compaction where you can tell
us exactly when you want us to
automatically summarize to compact the
context that's happened in your um
session that far. And if you're using
codeex, you're probably already familiar
with this. We also have a standalone
compaction endpoint. So you can make
requests to responses/compact
and we'll return back an encrypted
compaction.
So kind of two ways two highle buckets
to think about context engineering. The
first is trimming or truncation which is
basically let's just completely get rid
of older terms. Um, and with this we

[00:24]
want to think about how much do you want
to drop in order to make that cash
invalidation worthwhile? Like how much
of that history are we just cutting out?
And then the other way is summarization
or compaction. So we're not just getting
rid of the terms, we're summarizing and
providing that as context in the next
response. So a little bit more
sophisticated. And again, we want to
think how often and how much do we want
to compress to make that cache
invalidation worthwhile.
I think a helpful example here is with
the real-time API. Our speech to speech
model has a really short context window
right now. It's 32,000 tokens. Um, and
uh because of that, we really want to be
careful about context management. We
have this new parameter, newish
parameter retention ratio, which if you
set it, it can make a bigger cut. Um,
when you say 7 retention ratio, you're

[00:25]
basically saying every time we get close
to our context window, cut, cut it so
that there's 30% gone, retain 70% of the
information. So, you can think about it
this like you're making big cuts less
frequently because what's the
alternative? Essentially, it's cutting
every time you're getting close to the
context window, which in practice means
you're invalidating your cache on every
request. Right? This is similar to the
timestamp thing or adding a space in
your prefix. If you're invalidating the
cache on every single request, it's
going to be really expensive.
when we introduce retention ratio um
instead of that naive truncation every
single turn you're going to get see this
like step you're going to get a bigger
cut less frequently and on 30 minute
sessions you can save 70% um remember
audio tokens are almost 99% off so this
is a huge savings if you can be a little
bit more sophisticated with your
truncation
I want to show us a demo to think about

[00:26]
compaction now the point here in
compaction I'm going to start this is
really to think about um not prompt
cache key. We're just thinking about the
impact of compaction on uh costs. Um so
this is like a controlled multi-turn
staircase benchmark. So each turn is
adding a deterministic context. So we
can really isolate how compaction
thresholds will change the prompt growth
over time. So it forces stable model
behavior like all of these have the same
uh 15 turns and we're just comparing
compaction modes. Um this is arbitrarily
low like you're never really going to
have a 20k compaction. But you might
think about doing context engineering
and changing your prompt every 20,000
tokens. So I have that I have 100,000
tokens and then I have no compaction.
I'm just like letting the model go,
letting the cache build. In practice you
probably want a compaction strategy
about 80% of your context window. Um,
but for demo purposes, let's see what

[00:27]
we've got. Um, okay, compaction off.
Maybe let's look at the matrix and
drawer here. So, compaction off, we can
see a total of 245,000
tokens. And that kind of makes sense
because we're letting it grow. We're not
doing any compacting. And that's 21
cents here. And we can see with a low
compaction rate um, at 20K, we can see
that we have the lowest cash. It's 45%.
And that's because we're invalidating
the cache more frequently. However, our
input tokens are only 82,000 because
we're doing this frequent cache. We're
not letting our input tokens grow. So,
it's actually significantly cheaper even
though our cash rate is lower. And then
we can see with high compaction, we're
not making that many cuts. So, we have a
pretty similar input as we do for the
compaction off. Um, but it's more
expensive. So, here it's not that I want
to tell you, okay, this is how often you
should be compacting or not. It's more
consider caching and consider the cost
of your input tokens when you're

[00:28]
designing how you actually want to
architect for compaction for truncation.
So not this is the right way to do it.
You know your traffic best. You need to
look at your eval to determine where is
the intelligence boost worth it to do
compaction or to do summarization or to
do truncation. And that's really what I
want you to think about.
Okay. Uh, a few more quick tips. Um, API
endpoints,
responses API. If you're using reasoning
models, the chain of thought tokens that
are hidden, uh, only get passed if
you're using the responses API. Check
completions will drop them. And so,
that's inherently breaking your cache
because we're missing those chain of
thought tokens. So, if you're using a
reasoning model, use the responses API.
Just switching from chat completions to
responses with reasoning models can
increase your cache from 40 to 80%. And
responses is not just about caching. Um,
it passes those reasoning tokens. So

[00:29]
there's also a huge intelligence boost.
So not only are you getting improvements
in latency, improvements of cost because
your cache increase, you're also getting
getting improvements in intelligence.
So use the responses API please.
batch API versus flex processing. Um,
when we think about our first demo,
which with this batch image processing
use case, um, if you have these kinds of
latency and sensitive workflows, like
maybe you're batch processing images
every night, you might be using the
batch API. Um, fairly new is flex
processing. So, essentially, you're just
passing us a parameter on service tier
equals flex. um we're going to give you
the same discount as you see on the
batch API 50%. But instead of this being
an endpoint uh that you're hitting, this
is on a per request basis. So you can
control how many requests per minute
you're sending us, you can add extended
prompt caching and you can also include
a prompt cache key with requests. So you
can have way more flexibility about

[00:30]
hitting um the cache rate that you
should um be getting with the responses
API outside of a batch scenario. So, I
ran 10,000 requests. I used the batch
API. I used flex processing with 24-hour
extended cache. Now, flex isn't like a a
guaranteed SLA on throughput. So, having
that extended cache really helps. So,
here you can see I I had 8.5% increase
in cash hit rates when I used Flex. Um,
that's a 23% decrease in my input token
cost. So it's not relevant for every
single use case, but think about using
flex processing or testing flex
processing with your kind of
asynchronous workloads. Two more quick
tips, tool use. Um, so when we're
thinking about context engineering, u
providing the right set of tools to a
model is really important to make it
easier for the model to choose that
tool. However, if you change your tools,

[00:31]
uh, that's going to invalidate your
cache. that's part of what's hashed in
your prefix. So we allow you to use this
new parameter allowed tools um that
actually lets you specify a curated set
of tools on that request for the model
without invalidating your cache. Right?
So tools are injected before developer
instructions. So those are part of the
prefix but this allowed tools is not. So
you can actually adjust tool access
dynamically while preserving your cache
hits. And then lastly, extended prompt
cache. Prompt caching. So this um pushes
your cache from five or 10 minutes to 24
hours.
You pass us a parameter prompt cache
retention 24 hours and then we will
offload your cache from in-memory to GPU
local storage. Um so that this will give
you this 24-hour cache. And if you think
about a scenario where you really care
about that first time to token latency
for a long request, you can think about
just keeping your cash warm all the

[00:32]
time. Every day just sending us a
request so that when you have a super
time-sensitive maybe user query with a
200,000 token, you're going to get that
70% latency in improvement for that
request. So leverage extended prompt
caching carefully. Um you know your
traffic best.
Um, with extended prompt caching, we
have seen coding customers save up to
20% on input tokens. A huge benefit.
Okay. Pricing and latency. We already
talked about how uh pricing uh discounts
have gotten more uh have gotten deeper
since we've gotten a more efficient
inference stack. So, we're just passing
that on to you. So, if you're using
older models, think about switching to
newer models so that you can leverage
that 90% discount on the five model
family. And if you're using the
real-time API, caching is even more
important.
Two easy ways to track usage. You can
look in our dashboard to see input uh um
cached input and um uncashed tokens. And

[00:33]
then we'll also give you this field uh
in every response so that you can see
total tokens, input um cache tokens and
and uncashed tokens.
A call out for ZDR uh for anybody on the
call who cares about zero data
retention. Um, we can think about
in-memory versus extended PROM caching a
little differently because inmemory is
ephemeral. It is ZDR eligible. We're not
storing anything. However, with extended
PROM caching, because we are putting
that in GPU local storage, it's not
eligible for CDR because we are actually
storing those prompts. I do want to just
remind everyone, we're not storing your
uh raw text or images or audio. We're
not storing tokens. We're storing the
key value tensors that are these like
intermediate states.
Okay, cache miss checklist. If you just
think about these like key reasons that
you might be missing your cache and
improvements you can make. We've got um
input content mismatch. So, are you

[00:34]
changing your tools? Are you changing
your prefix? Um all of these things that
might change in the in that original
hash.
Has too much time passed? Um are you not
using extended prompt caching and it's
been half an hour? Like you probably
won't have a cache. Are you sending too
many requests? You're spilling over to
other machines. you'll probably see a
little bit lower cache rate. Is your
prompt under 1,024 tokens? We're not
going to cache it. Um, if you're using
the batch API with preGPT5 models, it's
not eligible for caching. Um, flex
processing is. So, just think about that
as another reason to try out flex. Um,
also chat completions without a
reasoning or with a reasoning model,
you're going to see a lower cash hit.
And a reminder that the theoretical
ceiling for your cash hit is always
going to be higher than what you're
actually going to see in practice. Um,
cash hits aren't guaranteed. Engine
health, there's all sorts of reasons you
might miss a cash when you technically
are eligible for one.
And I want to pass it over to Warp and

[00:35]
Surj.
>> Awesome. Um, yeah. So, thank you so much
for explaining all of those concepts. um
and really loved the demo and showing
that live. Um but now I want to welcome
Siraj on um who will actually walk
through the improvement business on
Warp.
>> Hey Siraj, how's it going?
>> Hey thanks for the intro Christine
[clears throat] and um awesome
presentation Erica. Um and hello to
everyone tuning in live. I'm Siraj. I'm
the technical lead at Warp. Sorry if my
voice sounds a little raspy. Um I woke
up feeling a little sick today so bear
with me. Um give me a second to share my
screen here. Um, oh, uh, Christine, I
think you might need to stop sharing.
[snorts]
Sweet. Thank you. Um, let me go ahead
and share here.
Cool. Um,
yeah. Uh, again, thank you everyone for

[00:36]
tuning in. I'm Sar. I'm one of the
technical leads at Warp. Um, for those
who aren't familiar with us, Warp is an
agentic development environment. Um, in
our early years, we started off building
a terminal, but today the primary way
developers use Warp is by using our
agent orchestration platform called Oz.
Um, you can launch coding agents locally
or in the cloud um, and orchestrate them
together to handle real development
work. Um, today over uh, 700,000
developers use Warp to do work across
the entire development stack. So um
whether you're uh just starting to like
architect your project scaffold it build
features on top of it on on existing
projects um debug issues with with
existing projects deploy monitoring
really warp warp helps with all that um
and it works with all the
state-of-the-art models um and supports
all of the standard extensibility
primitives that you're used to like MCP
scales agents.mmd etc. Um okay so why am
I here? So um my team's job is to make
these agents smarter faster and more
efficient. Um, and today I want to focus
on the faster and more efficient part.

[00:37]
Um, because effective prompt caching is
one of the biggest levers we have to to
achieve that.
Um, cool. So, Erica went into a lot of
important detail on how um, prompt
caching works once a request lands in
OpenAI's back end. And I want to focus
on the perspective from those of us who
are building on top of OpenAI's API. Um,
what can we do to optimize our our
prompt cache hit rates? So uh before we
even talk about how um like or why prom
caching matters and and how to take
advantage of it um it helps to take a
look at how a coding agent like warp
actually operates. So um agent
interactions uh in warp naturally form
what we call agentic loops which um grow
turn by turn. So oftent times the user
will start by giving the agent some sort
of task uh let's say like in this case
fixed compiler error um and then the
agent will usually make a tool call
maybe reading some files maybe running a
shell command. um the model reasons over
that tool output and decides what to do
next. Um and that and that loop
continues um until the user's task is
complete. Um and that and that also
means that the prompt is growing

[00:38]
incrementally with each turn. Um which
makes our use case very conducive to
benefiting from from prompt caching. Um
so so this is kind of like uh the uh the
context window building up. So you start
with your system prompt, your tools, um,
and then you have user query and and all
the following turns until the until the
model is done. Okay. Um, Erica went over
a lot of this already, but just to
recap, why does it matter? Why does
prompt caching matter? Well, inference
can be slow and expensive. Um, these
models do a lot of work every time they
generate um, a response. And fortunately
um we can use prompt caching to to cut
down on a lot of repetitive work um by
caching um intermediate computations
from previous requests and using these
cache values um so the model doesn't
have to redo the same work over and over
um like you saw in that agent loop um
the conversation was growing and the
model had already performed inference on
on proper prefixes. So it um it would be
a lot of redundant and wasted work to
redo all of those inference
computations. Um so that's where prom
caching comes in. Um, when used
effectively, prom caching can reduce

[00:39]
your cost by up to 90% and improve
latency by as much as 80%, which is
huge. Um, and at warp, we get to pass
those savings directly onto our users.
Um, so they can iterate faster and get
more done with warp. Um, so yeah, prom
caching is one of the most important
tools we have for making agents both
faster and efficient. Um, again,
efficiency means less bend for our
users. Speed means tighter iteration
loops, so you can ship more quickly. Um,
both of which are really important to
serving a great user experience. Okay,
cool. So, I want to talk about a few
different um things that we do at warp
uh to make prom caching effective. So,
like Erica talked about, you need to use
consistent prefixes and that this is
like the number one rule to making prom
caching effective. Um Erica talked a lot
about these prefixes in terms of tokens
and I'm going to zoom out and talk about
um for those of us using the API what
we're familiar with which are um you
know your system prompt instructions,
your your tool definitions, your um your
user and assistant turns. Um
so what this means is that um from turn
to turn you need to render consistent

[00:40]
requests to the model and avoid any sort
of differences between these turns. Um
so in practice what this means is um
having your system prompt be as static
as can be. Um you want to avoid any
dynamic content in that system prompt.
Um and you uh similarly you want your
tools to be consistent from request to
request. Um and like Erica talked about
um while you might need to change which
tools the model can use at a particular
point in the life cycle of the agent um
you can use the allowed uh tools
parameter for that. Um so also
importantly we don't want to invalidate
the the cache. So um once the model has
seen some some prefix um if if you go
back and change what the model has seen
um you will basically invalidate that
cache from then on. So in this example
here, I have um on the left uh a request
that um contained a user query and a
bunch of tool call and tool call results
after that. Um but let's say that the
user changed their uh intent of the of
the task and the way we implemented it
um naively was to just change the

[00:41]
initial user query. Um well well that's
pretty bad because that means that every
subsequent tool call and tool call
result is no longer going to be
allegible to be cached um until the next
time it is cached. uh which which
ultimately means more cost and latency
for for your end users. Um so instead
what you might consider doing in in a
case like this is uh adding a message
instead to the end of the to the end of
the trace so far. Um letting the model
know that the user's intent has changed
and that will preserve your prom cache.
Um
cool. Um
next slide here. Uh the the other um
thing we do in terms of prom caching is
thinking about our our prompt cache in
terms of scopes. So at the first layer
we we like to think about like global
caching. So what that means is um we
want every request uh from any user to
benefit from some sort of cach it on
your first request. And what and what
that often means in practice is the
system prompt and tools. Because of our
volume we're constantly caching these
across the platform. Um and in practice
this usually means like roughly 15,000

[00:42]
cache tokens on your first request. Um
to make this possible we remove all
dynamic content from the system prompt.
anything user specific but still like
static or configuration like let's say
your rules or your um MCP servers um
that's moved into a separate context
message that comes after the system
prompt and tools um which is the next
scope so at the user level um
[clears throat] any given user in warp
is often launching multiple agents in
parallel um and oftent times they're
they're going to have MCP servers rules
code bases other parts of their
configuration that are going to stay
stable across those tasks and so that
means we we want to be able to take
advantage of prompt caching at the user
scope. And to do that, we like I said,
we insert a a like an additional context
message which is meant to be like user
scope dynamic context that comes right
after the system prompted tools. So that
way if you launch one agent in warp and
then another, you will benefit from from
prompt caching from a greater prompt
cache fit than than just like um what
you get at the global layer. And then
finally task level caching. So um w

[00:43]
within a single task, the prompt is
growing turn by turn. And like you saw
for a coding agent, um often times there
will be many turns and and these will be
long um long traces. And so this is
where we get the strongest cache reuse
because most of the the prompt remains
unchanged between consecutive agent
turns. Um and this is what we optimize
for because for a given task, there are
going to be many turns happening in
quick su succession for a coding agent.
Um there's going to be lots of tool
calls reading files into into context,
editing files and so on. So we want to
be very efficient uh at the task scope.
Um and again for for different domains
and products the scopes will look
different and and consequently the the
efficacy of prom caching but these are
the scopes that we care about.
Um and finally uh prompt cache key. So
Erica talked a lot about this. Um the
prompt cache key is very very very
important. Um depending on which model
provider you're using caching might be
explicit or implicit. When it's explicit
you get to decide what to cache when to
cach it and for how long. And you get
some guarantees about data being in the
cache but it usually costs more. Um with

[00:44]
OpenAI you get implicit prom caching
which means that caching is done
automatically and you don't have to even
think about it. Um and that means it's
also best effort and so cache hits
depend on on where your requests get
routed. Um and two if two requests land
on different backends that were like sub
that were um that that were part of the
same conversation. The cache won't be
reused in that case. Um but luckily
OpenAI provides a mechanism to influence
how your requests are routed so that you
can still optimize your prompt cache hit
rates and that's a prom cache key. Um
when we uh implemented the prom cache
key effectively, you can see that our
cache hit rate um more than doubled um
back in August of last year. Um we've
since made a more improvements to prom
caching, but just literally uh adding a
prompt cache key that was task scoped um
made our prom cache hit rate um much
much much more effective. So that was
awesome. Um and [clears throat] I'll
also mention that um you know you should
put effort into optimizing that that
cache key. You want it to be stable
enough to maximize your use but not so

[00:45]
granular that you overflow the cache or
fragment it unnecessarily um leading to
to cash overflow. Um cool. Uh I I will
show a quick demo here. Um let me
reshare.
Give me a second here.
Get my warp instance up here. Okay.
Sweet. Um, cool. Okay. So, with with um
with warp, uh, you can uh you can really
do anything in the software development
life cycle. Um, in this case, I have a
compiler error um that I run into, and I
want to get um to help me fix it. So,
I'm just going to ask Warp here um help
me with this um compiler error.

[00:46]
And I'm using GPT53 codeex here. Let me
just So, um what you see here is our
like internal debugging tool for looking
at um requests, outbound LM requests
that we make. Um and so, you'll notice
that if I scroll all the way down here,
um we started off with with some amount
of of a prompt cache hit. Um in this
case, it was roughly 2500 tokens on the
first request. Um but as you uh as you
kind of see as the conversation
progresses here um the prompt cache hit
uh or the number of tokens that are that
are read um from the cache increase. So
in this case um again prom caching is
best effort. So often like you might not
always see it but if I kind of keep
going you'll notice that um as the
conversation progresses we start seeing
more and more um hits to the prom cache
um like you see here.
Uh, cool. Um, and yeah, warp kind of
fixed my compiler error for me. I can
accept that. Let me reshare again back
to the presentation.
Okay, cool. Um, so prompt caching is

[00:47]
important um because you save you get to
save a lot of money and get get to pass
those savings on to users. So, um, going
back to that example I had initially, if
you put some simple numbers to it, um,
so let's say we had 10,000 tokens in the
system prompt, 5,000 for your tools, and
100 for the user's prompt. Um, without
prom caching, uh, the user would be
spending roughly 2 and a half cents for
that request. Um, and with prom caching,
um, we're down to to just a fraction of
that cost, onetenth of the cost of, um,
210 of a cent.
Um and that cost compounds um once you
once you have more and more requests uh
that are building up for a given trace
um [clears throat] you're using more
tokens and of and that will just mean
that like you um you're spending more
and so uh the costs really compound and
it becomes really important to prom
cache effectively.
Cool. Um and finally uh I I'll just
mention some exceptions. So, uh, Erica
touched on this a little bit, but, um,

[00:48]
using consistent prefix prefixes is not
a hard and fast rule. Sometimes you need
to edit the context window. There might
be situations where you, um, see,
uh, the that a model read in a file that
was, uh, that was irrelevant to the
user's task and it's just polluting the
context window. So, um, in those cases,
you might want to manicure the context
window and edit that that tool call
result out of it. um which might break
uh prompt caching um which is going to
depend on your use case and uh and this
is something that you need to evaluate
but sometimes that could lead to greater
performance and cheaper cost in the long
run um by by just breaking the cache
once.
Um cool that's that was mostly
everything I wanted to share today. Uh
yeah I'll just say that um prompt
caching is something that that you need
to think about upfront. It's it really
changes um the the way users interact
with your with your AI applications,
especially um where cost and latency is
really important.
Cool. I'll pass it back to you,
Christine.

[00:49]
>> Awesome. Thanks so much for sharing. Um
we do have some really good questions
coming in through the chat and wanted to
see if you had some time to join us back
on stage and help us answer some of
these.
>> Yeah, for sure. Sorry.
>> Awesome. Okay. Um, so let's jump back
into the slides, Erica, so we can show
everyone uh these questions and then get
started.
Perfect. Okay, so the first one is for
you. It is what are best practices for
applying caching when the system prompt
the first message in the conversation
includes dynamic components.
I mean, I think Siraj covered this,
which is essentially if you have dynamic
parts of your prompt, try to put them as
uh as far at the at the end of your
prefix, like keep as much static content
first. So, it sounds like Warp actually
puts that in a separate message as
opposed to even including that in the
system prompt. But I think like anything

[00:50]
you can to put dynamic content further
toward the end of the prefix that you're
sending us, the better.
Cool. Okay, let's go to the next one.
Um, this one was a follow-up question.
So, what message type is used for
dynamic contacts, system, developer,
assistant, something else?
>> It sounds like warp is using like a
separate message. And I think this is uh
I don't know, we're fairly agnostic to
that. If you put at the end of your
prefix, like that's fine. If you put it
in a new message, that's fine. I'd say
experiment with uh what works best. And
like SJ said, like your evals will
determine um where you're getting the
best performance from maybe putting it
in the prompt, putting it in a message.
>> Yeah, exactly. We we we tried a few
different things and and ultimately we
found from our metrics that that um the
approach we ended up sticking with was
was the most effective.
>> Cool. Okay. Um and let's see our next
one. Um when does prompt caching trigger

[00:51]
automatically? Right. So, this is at
1024 tokens. And I think it's really
important. I've had customers who want
to have really short um prefixes, really
short prompts because they're like,
"Well, I'm going to save money from
having a 500 or a 900 token prompt." Um,
but I was doing some testing. If you
increase a 900 token prompt to a,024
token prompt, you will get cash hits,
right? you're never going to get cash
hit on 99 on a 900 token prompt. So if
you start getting cash hits, even if you
only have a 50% cash hit, you would save
33% on your token costs by increasing
the length of your prompt over that
1024. Um, so you could save a huge
amount of money just by increasing your
prompt a little bit. And again, this
will depend on your eval, but I would
say if you're at that kind of far end,
close to 1024, but you're under it, like

[00:52]
really consider uh getting to the point
where your prompts are going to start
getting cached.
Let's see what's next.
Tradeoffs. There's really no trade-offs.
That's why prompt [laughter] caching is
so awesome. There's no trade-offs.
There's no hit to intelligence. Um when
we think about model parameters, like
they're basically deterministic. those
are part of pre that's like what
pre-training is for and so if you give
us an identical identical prefix um that
KV cache is going to be the exact same
so there is no difference in outputs
from using a KV cache that um is from
your previous request to the one that
you're doing right now like literally
the only difference is uh that we're
burning GPUs when we shouldn't have to
but there is literally no intelligence
difference no output difference there's
literally no trade-off for prompt
caching. Like when can you say that?
>> Yeah, we actually saw this question come
in a lot during the chat. So I wanted to
double click on it because it always
seemed like it was too good to be true.

[00:53]
It's not
>> love that. Um and then to specify what
about like with the real with real time
is any trade-offs there?
>> There's there is literally never a
trade-off. The only trade-off is when
you're thinking about how am I
architecting to maximize for cache hit
versus not. Cuz if you're over
maximizing for prompt caching, you might
be getting an intelligence hit because
you're not doing that kind of context
curation. But like literally just
caching, no intelligence difference.
There is no trade-off. It's only the
trade-off in architecture. Got it. Okay.
So one takeaway from this whole build
hour, no trade-offs. Definitely
definitely be broadcasting. [laughter]
Okay, next question here. Um,
are there differences with prompt
caching on the completions versus
responses API? We saw some activity in
the chat asking about completion
specifically. Um, so I wanted to double
click on that since you did mention um
the differences there.

[00:54]
>> So the only difference is if you are
using a reasoning model because
reasoning models have hidden chain of
thought tokens, right? we're not
exposing the full chain of thought and
because that's not persisted like track
completions is inherently stateless
that's not persisted and so there's
going to be a difference between turns
because the model generated these hidden
chain of thought tokens and then isn't
seeing them on the next request. So
that's the reason why there is prompt
caching difference because you're not
persisting those. So um it's not if
you're not using a reasoning model it's
going to be the exact same but if you
are using a reasoning model you're going
to see lower cash hit rates on check
completions.
>> Awesome. Okay so that is our last
question but our next slide is on
resources. So if you do have additional
questions um feel free to check these
out. So the first one is prompt caching
uh doc where you can find everything
that we covered. Um and then two
cookbooks. So we have prom caching 101
and then prom caching 2011 which Erica
didn't wasn't this just published

[00:55]
literally this morning
>> it was just published let me see if I
click into this tab you can see I just
launched prom caching 2011 so we had a
101 from last year but I included this
2011 cookbook. It has a ton of the
information we covered today. Um so you
can review this um check check it out.
Um it's live um in our developer site
right now
>> right now. So build hour is also when we
launch things. Um so definitely look at
these links. Um after this um after
we're done going live, I will send all
of these emails um all of these
resources out in an email. And of course
it's there's also the code repo. Um, so
that will show um everything that we've
done in past build hours as well as this
one if you're interested and want to
check out the amazing demo that Erica
showed uh during the session. And then I
will wrap up with our next build hour.
March 24th is all about agent
capabilities. Please register via the
link and we will see you next time.

[00:56]
Thanks so much for tuning in.

</details>
