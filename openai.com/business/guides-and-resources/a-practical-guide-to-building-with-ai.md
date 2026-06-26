<!-- source: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-with-ai/ -->

# A practical guide to building with GPT‑5

Proven startup strategies to migrate, prompt, and scale with OpenAI’s newest frontier model.

[Try ChatGPT(opens in a new window)](https://chat.openai.com/)[Contact sales](/contact-sales/)

## Meet GPT‑5: our most powerful, most steerable model yet.

Built for the full spectrum of coding and agentic tasks, GPT‑5 is faster, smarter, and more adaptable than anything we’ve released before. Its greatest strength is how responsive it is to your direction, making it easier than ever to shape behavior for your specific use case.

But here’s the catch: every new model ‘thinks’ a little differently. Prompts that worked with GPT‑4.1 or other models won’t always translate directly. To unlock GPT‑5’s full potential, you’ll need to refine your prompts and tailor them to its unique behaviors and personality.

Our newest flagship model represents a major leap forward in what startups can accomplish, both due to its state-of-the-art performance (74.9% on SWE-bench Verified) and the controls developers have to steer and shape behavior. GPT‑5 excels at agentic and multi-step reasoning tasks where reliability, depth, and control matter: parsing complex inputs, orchestrating tool use, or managing multi-stage workflows. Beyond agentic use cases, whether you’re refining natural language interfaces, powering developer tools, generating structured outputs, or automating complex business processes, GPT‑5 delivers higher accuracy, better consistency, and more predictable behavior than any previous model.

---

### What we’ll cover in this guide

In this guide, we’ll share proven techniques to get the most out of GPT‑5 based on our work with leading startups with technical resources and actionable steps to get started.

1. **Migrate:** Steps to migrate to the Responses API, designed for long-term scale, speed, and new reasoning capabilities.
2. **Optimize:** Techniques to develop strong prompting that help you move faster and reduce engineering overhead.
3. **Steer:** New controls let you guide how the model reasons and communicates to match effort and output based on task complexity.
4. **Troubleshoot:** Resources to avoid common pitfalls like overthinking or overly verbose answers.

By the end of this guide, you should understand how to leverage GPT‑5 to its full potential to unlock more consistent, predictable, and accurate behavior while optimizing costs.

---

## Step 01: Migrate to the Responses API

Your first step to unlocking GPT‑5’s full intelligence is to build on the infrastructure designed for it. Only the Responses API allows the model to persist its chains of thought (reasoning items) across turns and tool calls, either with OpenAI managing state or by passing back encrypted reasoning items.

This means every request to the model has access to its complete internal context, significantly boosting performance and improving caching to lower costs—capabilities the Chat Completions API simply doesn’t support.

##### Velocity

Smarter tool use and built-in state management reduce glue code and orchestration. You ship faster with fewer engineers and focus more time on your product and customers.

##### Scale without drag

Full-context reasoning plus faster performance and higher cache-hit rates lower infrastructure costs and latency as you grow. With zero-data retention (ZDR) compatibility, you’re not locked into today’s deployment pattern—you’re ready for the agentic workflows that will define tomorrow’s applications.

##### Future-proofing

The Responses API is the path forward for new reasoning capabilities. Building here keeps you off legacy APIs when the most powerful features ship and aligns your codebase with where OpenAI is investing most heavily, giving you long-term stability as the ecosystem evolves.

The Responses API is the unified surface for working with GPT‑5. To maximize performance and future-proof your startup, we highly recommend moving workflows to the Responses API today.

![Screenshot of a tweet by Greg Brockman (@gdb), verified, that says “try using Responses API with gpt-5:” and quotes a tweet from Shen Zhuoran (@CMS_Flash), verified, dated Aug 18. The quoted tweet reads: “Man it’s crazy how BIG a difference it makes for GPT-5 just by switching from Completions API to Responses API. We’re cooking @augmentcode.” The tweet shows a timestamp of 10:04 AM · Aug 19, 2025.](https://images.ctfassets.net/kftzwdyauwt9/DESfDyAgvsjMjmQBLKkaj/0148090e354cc9f5cb737f274a3b6ce7/Twitter.png?w=3840&q=90&fm=webp)

###### Getting started with Responses API

[### Responses API

Why we build the Responses API.

Learn more](https://developers.openai.com/blog/responses-api)

[### Reasoning Models on the Responses API

Instructions on passing reasoning tokens, caching, and unlocking more intelligence.

Learn more](https://cookbook.openai.com/examples/responses_api/reasoning_items)

[### Migration Guide

Step-by-step instructions to move from Completions to Responses.

Learn more](https://platform.openai.com/docs/guides/migrate-to-responses#page-top)

[### Codex CLI Toolkit

Open-sourced tools to automate and streamline migration.

Learn more](https://github.com/openai/completions-responses-migration-pack)

[### Build Hour Demo

See GPT-5 in action on the Responses API.

Learn more](https://www.youtube.com/watch?feature=shared&t=304&v=ITMouQ_EuXI&themeRefresh=1)

---

## Step 02: Optimize prompting

Moving to GPT‑5 isn’t just about adopting a new model – it’s about mastering how to optimize it. Startups that develop strong prompting practices move faster, spend less on engineering overhead, and create products that feel meaningfully better to users.

![Screenshot of a tweet by alex duffy (@alxai_), verified. The tweet says that good prompting is more important with GPT-5 because it is highly steerable: mediocre prompts give worse results, great prompts give better ones. It notes a performance gap for GPT-5 with minimal reasoning, with optimized prompts shown in red and baseline in gray. Below the text is a dark-themed box-and-whisker chart titled “Model Performance as France,” showing multiple model configurations along the x-axis and game score on the y-axis. Red (optimized) distributions generally appear higher than gray (baseline), highlighting performance differences, with some model groups outlined for emphasis.](https://images.ctfassets.net/kftzwdyauwt9/76Jw7jCUMiZ2dLaQGm70Nw/fb792962120058aaf1c5fed4d2292d6d/Twitter_Alex_Duffy.png?w=3840&q=90&fm=webp)

##### Start with evals

Begin by running your existing prompts as is against your evals to establish a baseline and see where outputs diverge from expectations.

##### Inspect the model’s reasoning

For specific failure cases, loop the eval again and stream reasoning summaries with GPT‑5 in the Responses API. Watching the model reason helps you pinpoint where it needs more steering.

##### Metaprompt and simplify

GPT‑5 is skilled at metaprompting—use the model to improve its own prompts as you iterate. Often, it requires less scaffolding than older models; shorter, clearer instructions can perform better.

##### Template and document

When prompts work reliably, lock them into reusable templates or a prompt library. Document what good vs. bad outputs look like so the team can build consistently, and revisit periodically as techniques evolve.

###### Getting started with prompt optimization

[### GPT-5 Prompting Guide

Best practices for crafting powerful prompts

Learn more](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)

[### Building Hour Demo

Live example of GPT-5 in action

Learn more](https://www.youtube.com/watch?v=ITMouQ_EuXI&t=1528s)

<!-- yt-inline:ITMouQ_EuXI -->
[![Build Hour: GPT-5](https://img.youtube.com/vi/ITMouQ_EuXI/hqdefault.jpg)](https://www.youtube.com/watch?v=ITMouQ_EuXI)

<details>
<summary>자막: Build Hour: GPT-5 (58:35)</summary>

[00:00]
Welcome to the GPT5 build hour. I'm
Christine. I'm on the startup marketing
team. And you might recognize Bill from
our image gen build hour.
>> Hi. Uh yeah, it's good to be back again.
>> So, Bill had so much fun last time that
he brought a few of his friends.
>> Hi, I'm Eric. Uh I'm from the posting
research team.
Um, so if you're new to build hour, the
goal of build hour is to empower you
with the best practices, tools, and AI
expertise to scale scale your company
using open AI APIs and models. Next
slide.
Below you can see our homepage. So feel
free to visit this for any upcoming
build hours. We have one on September
3rd that's going to be all about codecs.
But for this one, we are going to be
talking about our smartest, most
steerable model yet. I dropped these two
links in the chat for you uh to open up
and feel free to test these out as
you're following along. Um highly
recommend looking through the the prompt

[00:01]
optimization cookbook as well as the as
the prompt optimizer.
We want to help you build better with
GPD5. Um you might be looking a little
bit like this with some bad prompting
and our goal is after this hour for you
to look a little bit more like this.
Um so feel free to use any of the um
questions in our chat um as we go
through because we'll be answering them
live. Next slide. Um so here's a
snapshot of what this next hour will
entail. First we'll be talking through
the GPT5 new capabilities. So we're
going to touch on coding agentic tasks
and some new features. We won't spend
too much time on this because then we'll
be diving straight into demos
specifically using GPT5 in the responses
API. And then we'll spend 10 minutes on
prompting covering best practices um as
well as metaprompting and walking
through what that looks like. And then
we will welcome Riley, the founder of
Charlie Labs on stage to share how he
built an autonomous coding agent with

[00:02]
GBD5. And then as I mentioned Q&A, um
this is your chance to get your
questions answered. We have our team
here in the room with us um answering
these as we go along and then we'll also
select a few to address live. um towards
the end of the session. So, I will pass
it off to to Bill and Eric.
>> Awesome. Uh thank you, Christine. It's
good to be back again. We have a lot of
content prepared. Uh and so u a lot of
those things I'll touch up on in a demo.
So, I'm just going to run through uh the
deck really quickly just to show you
what the GPD5's capabilities are. Um5 is
a true coding collaborator. Um I think
that there's no question about it. I
think there's already a lot of uh news
and hype in the media these days and I'm
happy to confirm that these are true.
This model does show is is a step
function in increase in code quality u
in its ability to uh create good-looking
front-end UI. It's also incredibly
collaborative. It's also really
steerable as well. So, you can tell it

[00:03]
what to do and it'll be able to do
things for you. Um couple of benchmarks
since people seem to really care about
benchmarks. Um but bigger number is
always better and I'm happy to say that
indeed uh we have like bigger numbers uh
on uh important benchmarks and like
Sweetbench as well as Ador Polyglot
multilanguage code editing.
Not only is GP5 good at coding related
tasks, it's also very good at long
running agentic tasks as well. So what I
mean by that is aentic tasks that
involve longchains uh tool calls. So if
you want the models to be able to do
things end to end by itself by calling
tools, GP5 is going to be able to do
that also with uh instruction following
as well. So it does exactly what it's
told to do when conditions arise. And it
also provides pretty good explanations
of its actions up front through its
preamles and also proactively corrects
itself if it finds itself going down the
wrong path as well.

[00:04]
Couple of other new features. Um we also
with the GPD5 introduced a reasoning a
new reasoning uh parameter called
minimal. Uh so this GBD5 is a reasoning
model uh but with minimal reasoning uh
GBD5 essentially does the least amount
of reasoning it it needs to do and so at
the end of the day you get the
intelligence of GB5 alongside the uh the
the increased model intelligence with
the latency profile of a non-reasoning
model like that that you're familiar
with like GD41
custom tools as well so you don't have
to worry about uh escaping JSON so what
this allows you to do is make tool calls
in plain text. Uh so if you're building
something uh in the agent coding space,
you don't have to worry about escaping
finicky adjustments anymore. Robocity
parameter pretty self-explanatory. Um it
steers how much of a final output you
want out of the model, but I'll also
talk a little bit more on the tips and

[00:05]
tricks on how you can use this for
function calls as well. Without further
ado, uh let's take a closer look at GBD5
inside of the responses API and how you
can use it. So here I have a um uh my
cursor um pulled up with the uh OpenAI
build hours repo. And just to give you
guys a quick show of like its improved
front-end capabilities, I ran a one shot
uh inside of cursor uh using GPD5 before
right before this uh build hour. This is
a create another folder named landing
page and generate a landing page of a AI
coding product called vibe coder. Very
very simple um prompt and you you're
able to see that it has generated a
fully functioning website alongside of
tabs that just works. So this is pretty
much a tangent here. I just wanted to
show you the things cool things that
you're able to build out of the box. Now
you might be wondering how are you able
to build something like uh cursor u with

[00:06]
GD5. Uh now this is what I'll be getting
into like how you can use GP5 inside of
the API. So um inside of API to use GBD5
very simple all you have to do is change
out the slug. You can see here in the in
the responses API, I have the model that
says GPD5 and all of a sudden like this
response is this request is hitting the
GPD5 model and this comes from the GP5
uh model. And just to show you the
minimal uh reasoning effort as well here
I have two identical requests um that's
been sent to the model. One of them
finished in 0.9 seconds, the other one
finished in 6.9 seconds. Uh on the first
we use minimal response. The second we
use high uh high high reasoning effort
uh for the response and as you can see
there is a difference in how long it
takes for those two things to come back.
And also on the second part I also
turned on reasoning summary as well. So
you can see exactly how the model

[00:07]
reasons.
>> Yeah. So Bill like you've been talking a
lot there's this like responses thing
here. Can you tell us more about that?
>> Oh yes. uh responses API allows you to
um to to uh really uh use GPD5 to its
fullest extent. If you are familiar with
our uh let me just run a couple of cells
here so you can see to generate things
that I'll be talking about shortly. uh
if you are familiar uh with our API in
the early days back in the GBD3.5 turbo
days uh we created this thing called
completions API uh which is uh what most
of you guys might be already familiar
with uh so as you can see here we're
using the completions API sing hello
world and here we're using responses API
to do the same thing those two APIs
responses API is essentially kind of a
v2 version of the completions API it's a
better uh and and more featurerich uh
version of the API that really allows
you to take advantage of the full
capabilities of reasoning models GP5. On

[00:08]
the surface level, they look kind of
similar um just with additional u
developer experience affordances out
there. So putting things like output
text is a lot easier than choices square
bracket zero.content
that you have to get into with
completions API.
>> But there is one thing here that I would
love to you to to take note. If we dig
into the response that it can output. So
there are two differences here. This one
I didn't pass in the parameter store
equals to false. Here I have by default
store equals to true. So the responses
API by default is a stateful API as
well. And you can turn that state off by
uh passing in store equals to false. And
you can use something called
reasoning.enencrypted content to get the
same benefits. And what I mean by
benefit here is this thing the reasoning
item that it's passing back. If we look
into the response.output,
we see that we have a reasoning item.
One is encrypted here. If we use store

[00:09]
equals to false, one is not encrypted.
I'll just talk briefly about what this
is and how we can leverage this. So for
the reasoning models like GPD5, it emits
something called chain of thought
reasoning tokens when it's reasoning and
calling it the tools. Those are
basically the intermediate steps while
it's thinking things like, oh, what tool
should I be calling at this moment? Why
I should be calling these things? And
this is useful because uh for you if you
pass those things back after a tool call
the the model will have access to the
reasons why it's called the tools in the
first place. So it's able to uh
continuous train of thought much more
coherently. And to demonstrate this a
little bit more concretely here uh when
is reasoning items really necessary for
uh model intelligence. So if you just
imagine the user you sending a message
like a user message like like I have
here uh like what is the weather in
Paris today? Um uh the the API might
might start to think that hey I don't
have all of the context and therefore

[00:10]
I'm going to give you a tool call for
you to run on your side as well. But
because um because I'm a reasoning model
I have all those reasoning steps that I
have performed. I also want to know why
I have called this tool after you have
provided the response. So I'm going to
give you that reasoning item so that for
you to be able to pass it back to me and
and when you finished with a tool call
the user you pass back the reasoning
item as well as a tool call result
directly to the responses API which then
continues its train of thought uh in
deciding whether or not it has enough
context or needs to call another tool as
well. And so as you can see here, we
have a a tool cut weather mocked up and
I have the user asking what the weather
is like in Paris today. And we can just
take a quick look at the response. We're
using encrypted uh chain of thought
tokens here. So for ZDR orgs that cannot
uh use the statefulness of responses
API, we give you the chain of thought
tokens encrypted uh inside of this
encrypted content. As you can see here

[00:11]
in responses, we see that all of this is
present. And as we see also here this
tool call is mitt uh with the arguments
of longitude and latitude of Paris. And
uh as a user here what we can do here
all we have to do is add this whole
thing to the context. You don't have to
worry about parsing out uh the encrypted
content or as a reasoning item. And then
we can mock up a response uh to how how
how much Paris like is actually hot or
cold today. And you can see here this
gets back to us with an answer. This is
a very simple toy example. So it might
not like uh inside of completions you
will probably get the same answer. But
for a long running agentic task where
you have 20 to 50 tool calls uh
backtoback this can really mean the
difference between uh two to 4% uh
difference in benchmarks like sweet
bench.
>> Yeah. So, so Bill, just like to
summarize here, um the model is going to
perform better over longunning rollouts

[00:12]
because it's going to remember its
previous thoughts. Like it won't have
amnesia and forget the things that it
did before.
>> Yes.
>> Um at least in the train of thought as
it was thinking.
>> Exactly.
>> You got that exactly right. In addition,
one thing that I almost forgot to
mention, uh because of prompt caching,
prompt caching for us depends on the
prefix. So the prefix being the same
between requests, the reasoning items
are actually what part of that input
into the prefix. So in addition, you
actually get better caching performance.
So it's cheaper, more intelligence, and
faster.
>> Awesome. So more cost efficient, too.
>> Exactly. Um, and just to show you guys
the verosity uh parameter how it works,
we can just run those two requests here.
No any difference between the two, Eric?
Uh maybe I think the second one is
longer.
>> Oh yes, absolutely. Erica, you're right
on the money here. Um as you can see
here, focity steers the the final uh
output of the um of the of the model as

[00:13]
well. Um so in addition to final output
there is it also affects the tool call
as well. So here I have uh something
mocked up. This is a custom tool which
allows you uh allows the model to call
the tool in plain text. So as you can
see here, this is defined a very simple
way. This is sort of a standin for an
applied patch tool. Let's say if you're
uh cursor making uh an aenta coding
tool, right? And here I have a prompt
and I'm going to run these this prompt
in uh in low as well as high. And what
we can see here is a little bit of a
difference between uh how how the the
tool call is also emitted. So those are
two different code snippets that's
emitted. It's a little bit hard to tell
uh between the two, but you can see here
that um that verbosity high produces um
a little bit a code that's a little bit
easier to read, a code that has better
error handling as well as just overall a

[00:14]
little bit more readable uh for
developers. And while the first one low
verbosity is still readable uh as well
as um correct, it's a little bit less um
like so uh le less readable. So in a
case where code readability is important
to you, we discovered that verbosity
high is actually um you know really
conducive to that. So my best advice to
you would be experiment for your use
case on what sort of a velocity level
works best for you and and and and go
from there. And for code agent coding
use case we found that verbosity high
works really well and cool and then just
oh and I have a fun snippet that also
ran here. Uh but before like getting
into this I would just love to reiterate
on the things that I've talked about the
differences between switching to
completions responses API is really
really huge. Uh so I would just love to
reiterate on that. If there's one thing
I would like you to take away from this
entire build hour. Sorry Eric, sorry

[00:15]
Anoo, sorry Riley is the use responses
API. Please, please, please use the
responses API to use the model in this
unhand handicapped way. So pass back the
reasoning items for maximal
intelligence. Other things are minimal
reasoning for latency sensitive task
free form function calling as well as
verosity parameter for your desired
length. And here I have this pretty
funny prompt that I just thought would
be kind of cool. Um, like I copy and so
this has already generated the code and
I've copy and pasted this code right
here. And let's see what it generates.
It's Wow. What What is that, Eric?
>> Uh, so if I'm seeing this correctly, it
looks kind of like a creeper, which is a
um an entity like a a mob from from
Minecraft. A game that I played a lot as
a kid.
>> Oh, wow. Okay. Well, great. I I've
played that game a lot as a kid as well.
I wonder why this is showing up here. Um
maybe uh you have something. All right.
>> For us, Eric.
>> Yeah. So, hey guys again. Uh, I'm Eric.
Uh, today I'll be talking a bit about
like what we're excited about for um

[00:16]
from the research side, like to improve
in the next iteration of the model. But
first, I kind of want to give like a
visual demonstration of where the model
really shines. Um, so first, uh, we'll
be building a Minecraft clone in codeex.
So, for context, um, so I'm in my
Minecraft folder, which you can see is
empty. Um for context codeex is part of
our coding suite of products. Um one
particular product that we have is
codeex cli which is a terminal tool
where you can do prompts um write
prompts and it'll just output code. Um
so I have a prompt for Minecraft that I
will paste in.
So this is going to be writing the whole
application from scratch.
Um, so as we can see, like they're using
OpenI Codeex in terminal. Um, we're in
our Minecraft folder. Codeex is going to
have access to all of the files and
folders um in the folder that we start

[00:17]
in. Uh, right now there's nothing in
there, so it's just starting from
scratch. We have some commands here. Uh,
we're not going to use those today. Um,
so, uh, Codeex by default uses GPD5
today.
>> And as you can see, GP5 is going to tell
us first what it's going to do before it
actually goes and does it. Um so it's
thinking it gives us like some highle
plan
>> and u
>> so this is GPD5 inside of codeex.
>> Yes.
>> How how might u an audience member here
try it out by themselves?
>> Yeah. Um so go online and look for the
codeex docs. Um you can find this like
on Google or if you like GPD for it. Um
it's a pretty easy like npm install. Uh
then like as I did here like you just
type in codeex like it'll give you a
nice like little terminal command and
then you get this really nice interface
where you can just type in like a chat
box um and it'll show you as it runs. So
great. Um so we gave a high level plan
and now it's giving uh GPD5 is giving a

[00:18]
bunch of checkboxes which it'll run
through and now it's going to run for
about maybe like three to five minutes.
Um so we'll let it run.
>> Yeah. While it's running, Eric, I have a
couple of questions on top of my mind. I
imagine probably you guys have as well.
What are you most excited about GPD5
since I think you've been the one
training it?
>> Yeah. Um, I think there's a couple
things that you touched on earlier,
Bill.
>> Yeah.
>> Um, I think a big focus was agenticness.
Um, we want the model to be more
coherent over like bigger tasks, tasks
that take longer, like longer time
horizon tasks. Um, so this is something
that we really dialed in. Um, I think
something else that we really focused on
is front-end and web development. Um, so
previous models were already quite
functional. Like they thought hard. Um,
they can build like very functional
applications, but they often didn't have
as much of an idea of like taste and an
understanding of like what makes a web
application beautiful. And so, um, GBD5
today is, uh, in my opinion like one of

[00:19]
the best, if not the best model for
building like really beautiful
applications and websites. It's also
very steerable, um, as we mentioned
before. Um, so it'll adhere very closely
to your prompts. Um, so if you want to
change like the way that your website
looks, uh, you can do that and just like
vibe code and build, uh, whatever you
like.
>> That's awesome. Uh, that that's awesome,
man. I see that this is the codeex is
running through certain things and it's
almost like finishing up here. It's like
checking
>> that's quite fast actually. Yeah. So, so
kind of as we can see um, it's giving us
so yeah, we start out with this plan.
It's checking off things on the plan as
it goes and explaining what it's doing.
Um, so the visibility into what it's
doing is really good.
>> I see.
>> And it's showing us the patches that
it's making. Um, and Wow, nice. Um,
>> wow. Is it done?
>> It's already done.
>> I Okay.
>> Shall we play it?
>> Yeah, let's let's play it. So, um, what
I'm going to do is I'm going to go into
my other terminal, which is in the same
folder. I can do an ls just to show that
now there's files in here, whereas
before there weren't. Um, we have some

[00:20]
instructions here for how to do this.
Um, but we can npm install which will
install some dependencies.
Great. And then we can npm rundev
to try it. So let's try it.
So we'll go into our browser here.
Cool. Um,
>> wow. This is
>> so Okay. Interesting.
So we have a world here. We can break
blocks.
H.
All right. So, we can make some updates
to this. I think that there's a couple
of things that we can do. First, um I
want to customize this a bit to make the
world is a little too green for my
tastes. Like, it added borders like I
wanted it to, but I think it could be a
bit more pink.
>> Yeah.
>> Um I think there's also some rendering
here. So, let's just prompt that. Like
the beauty of Codeex is that NGP5 and
Codex is that it understands your
intent. Um and it just builds. So, let's
give it a pretty meaty prompt, actually.

[00:21]
Um, maybe I want to add pink flowers
onto all the blocks.
>> I also want it as a sun.
>> Okay, let's let's do that. And make make
the sun a pink flower, too.
>> Yeah.
>> Um, also improve the
rendering of the blocks.
>> Um,
>> awesome.
>> Cool. And this should run for a little
bit. So, while it's running, I also want
to talk about what we're excited about
um for future iterations of our models.
Um there's a couple things here. I think
one is continuing to push hard on web
development. I think this is like a
really like big use case and people care
a lot about it. Um so making like
additionally like more beautiful and
complex web apps that are just super
functional. I think something I'm
personally very excited about is models
that can work in a loop to iterate on
your app because right now models are
kind of they're confined to just
building your app like we're doing here
but they have no real visibility into
the application that you're building um

[00:22]
outside of like some small cases where
it writes some tests. Um I think the
future is models just in a loop
iterating with you building testing
building testing. Um, and I think that
this is something that like the whole
community is going to work on like
connecting models to testing
environments and we'll work hard as well
to make the models better at this. Um, I
think the final thing is just improved
agentness. I think over like the medium
to long time horizon. Um, in the future
the models are just going to get more
and more coherent over longer like
horizon tasks. Um,
and I kind of see a world where there's
this like agent slider. I'm kind of
shamelessly stealing this from Andre,
but um Corpathi that where like the
models can do very long horizon tasks
like maybe an hour, a day, a week. Um
but sometimes you want them working
together with you like in the loop. Um
and I want the models to kind of just
understand from context uh like what you
want like do you want this to be like a

[00:23]
quick small thing like a minimal
implementation like in the coding
example or do we want this to be like a
very longunning thing? Um,
>> Eric, you're really painting a picture
of the the future here. Um, so if I'm
understanding it correctly, the future
models will be able to better understand
if this task is simple or if it's hard,
if it needs to think longer, if it's
thinking shorter. And in addition, it's
just going to be smarter and for the
longer running task, it can just be so
much more agentic. It's be able to do
things hours, maybe days on end, if I'm
correct here.
>> Yeah. Yeah. Yeah. Cool. I think this is
done. So, let's uh we already have our
server here. So, as the code changes
come in, we can just kind of see how
things go. Oh, wow. Okay, that's
>> has a lot of flowers.
>> That is pretty cool. They actually added
the flowers like on top of the blocks.
>> Wow.
>> And we can actually
>> jump
>> kind of run around and jump.
>> Oh, wow. That's amazing.
>> Um, where is a sun?
[Music]
>> Cool. But nice. So, that's like
basically you can continue customizing

[00:24]
this. You can add like mobs or other
mobs are short for mobile entities, I
think. So um different things that you
can interact with. Uh okay. So to end
this I think I will just
jump off the side.
>> That's uh wow that's that
>> cool.
>> Okay.
>> All right.
>> Also one one last thing before uh before
we we end on this is that uh in order I
think Eric how like when we improve on
the future models we also want to hear
uh your feedback as well. Um, so we've
created a very um like simple Google
form just for you to drop any thoughts
that you might have and this should show
up inside of the chat. So feel free to
take a look at it, fill it out and we'd
really appreciate anything. And Eric
actually
>> So I personally I think the thing that
the team really wants um more than
anything else is your feedback. like we
want to understand your use cases
because um I think we try to understand
as best as we can like what everyone's
doing but there's like so many different
use cases. Um so yeah, we'll send a

[00:25]
form. Um I'm personally going to read
everything and uh yeah, you know, we'll
we'll improve on we can only improve on
stuff that you tell us that is like
important to you. So please send us your
feedback.
>> Cool. Thank you. Um I love the pink
flowers. I think you guys were inspired
from my my Barbie GIF. Um definitely
steerable. Uh so on that note um welcome
Anoop.
>> He actually wrote the prompting guide.
So he's an expert on prompting. As I
mentioned GBD5 is really steerable. And
so Anoo is going to help you get the
most out of GBD5 with really good
prompting.
>> Yeah. Uh thanks Christine and thanks
Bill and uh Eric for the awesome demos.
Hopefully we can get you guys to build
demos as good as they did um with with
the prompting tips that we're giving
today.
Sweet. Um, maybe just like a tangible
example of where we've seen prompting
actually provide a big lift to GT5
performance. Um, here's one where Alex
tweeted, "Hey, we were previously just
took our old prompts and put them into

[00:26]
Gd5 and didn't really notice much
results and maybe even worse results."
Um, but then realizing there's some
nuances to prompting GD5. And once you
realize those nuances, you can get a lot
better performance that's statistically
a lot more significant than what they've
been seeing in the past. And if you see
the little quote tweet at the bottom,
um, Eric mentions that, hey, Gift5
interprets your words literally and very
very well, like follows instructions. So
like be make sure to be specific and
make sure the model will understand what
what you're trying to mention to it in
the prompt. Um, and then now we're just
going to go over a few different
examples actually of how to think about
like a prompting cheat sheet. So these
are like maybe six snippets that we
think will be helpful, but obviously
there's a lot more that's important when
you're working on prompts. And hopefully
this is just a starting place to get you
to that 80% and then that final 20% um
hopefully you can tweak pretty quickly
with the the intuitive tips that we're
giving now.
>> Cool. So I think the first thing is
maybe the most important part for
getting the most out of GT5 in terms of

[00:27]
prompting. We've seen in the past um
that when folks are using o older models
that if you give conflicting
instructions or information that's maybe
a bit imprecise, the models will sort of
vibe and infer their way to an answer
that kind of does what you want it to do
most of the time and you're generally
pretty happy with it. But the thing
we've noticed with GT5 is if you also
have those same imprecise like maybe
viby answers that you're looking for. Uh
GT5 really interprets those like super
effectively and maybe to the detriment
of performance. And what happens if you
read over the reasoning summaries that
Bill mentioned with the responses API is
you'll see that the model's actually
conflicted there. They there one part
saying like oh what's going on in this
instruction and then the other part's
like okay maybe it's working as
expected. Um, so this is the place where
we want you to make sure that you don't
have any of these conflicting
instructions and you have very precise
pieces of information that you're giving
GP5 and that's where we see pretty big
step uh function improvements across any
previous models that you may be using.
Um, so that's the first tip. The second

[00:28]
one is using the right reasoning effort.
We recommend starting with medium, but
as Bill mentioned in previous slides,
it's probably useful if you want like a
low latency task to start with low
reasoning effort. Or maybe you're
running like a super long agenda task
like building Minecraft for example.
Then maybe you want a lot longer
reasoning effort and maybe you want to
turn that to high. Um and maybe you want
to turn up verbosity as well to high for
that. Um this is actually we ran some
tests when we were doing the the
prompting guide and we were we were
wondering like what's maybe the best
structure to structure your prompts. Is
it XML? Is it Markdown? Is it JSON? Is
it YAML? Um or is it something else? Um
from our tests we've seen that XML
performed the best. But as always, I
will always caveat this. There's maybe
some things that work well for your use
case that might not work for others. So
just know that we've seen XML perform
the best for our tests.
Um the fourth one is maybe a meta point
uh which is metaprompting. Um the
>> I I see what you did there.
>> Thank you.
Um, the way to think about metaprompting

[00:29]
for GV5 and maybe just as a whole for
how to improve prompts is generally
we've seen people in the past say like,
"Okay, X thing is broken in our prompt.
Can you please fix it?" Um, and maybe
the model does okay there. But the
pattern we've seen actually do the best
and we'll we'll show an example of this
is actually asking the model why it's
doing something and then once you ask
the model why it did a certain behavior,
then the model will maybe give back some
response. So GP5 will say maybe I did
this incorrect thing because of X Y and
Z reasons. And then once you have that
then you can ask the model to fix it
based on those reasons. So it's a lot
more uh precise in the actions you're
taking versus maybe making those like
single one-off changes initially are
very overfit to the specific prompt
where where you might not want to do
that.
Cool. Um I think the next thing you you
kind of saw in Eric's codeex demo,
right, is give room for planning and
self-reflection. The model does this
really well out of the box already. Um,
but making sure you have some sort of
planning or uh some sort of setup step

[00:30]
for the model gives it a lot of room and
we kind of saw that with the to-do list
uh in codecs.
And then the final thing uh we've kind
of mentioned this a couple times, right?
The controlling the agenticness of the
model can be a bit tricky. So maybe
there's some points where the model is
maybe doing too much and you want it to
actually defer to the user to give input
or maybe sometimes it's not doing enough
and it's asking the user for input too
often. There's this like fine balance
you want to you want to find and we have
some tips here to help you do that in in
a demo coming up. Sweet. Maybe let's hop
into the demos.
>> Great. Ah the Minecraft
>> Yes.
>> Creeper is staring at us.
>> Yeah, you can build that.
Um, so for the first one, let's actually
chat through like controlling agentic
eagerness. So right here, I'm going to
plan on building two websites. One
website where I'm just going to give a a
default prompt with a bunch of different
examples. So you'll see them here.
There's like 15 different elements that

[00:31]
I want for this website. Um, and then
I'm going to do the exact same thing um
with more eagerness. And the way you'll
see this is
if it
I'm going to scroll past it. Um, but the
way you'll see this is we'll add a
little persistence check to the model
and then that persistence check will
make it go a little bit further for its
next steps. So if we want to see how
this actually might look if we run this.
So these are just some boiler plate
code. Let's run it. And then once it's
running we can see the outputs that we
ran. So this is with less persistence.
So we didn't ask the model to keep going
and go through all 15 steps. We have a
website generated here. It has some
frequently asked questions. Kind of did
the task as expected.
Um, and then here we have the same
thing. It's a little bit more structured
and well put together. Um, we have a few
different items here. It looks pretty
similar, right? All the all the key
parts are there. Uh the main thing I
want to call out here if I go back to

[00:32]
the prompt actually
is one of the things we ask for in the
FAQ section is add at least three common
questions in a class flow accordion
format. So there's a lot of small minute
instructions here, right? There's three
at least three. Um if we go back, it
looks like there's at least three in the
FAQ for both of them. Um, but the
collapsible accordion, this I don't know
if a plus sign counts as a collapsible
accordion, but those are like the small
nuances where if you add persistence,
this this is the icon you would kind of
expect for a collapsible accordion
folder.
>> Yeah, in my book, that's an accordion.
The other one is not.
>> Okay,
>> that's that's a fake accordion.
>> Belch approved, so we'll take it.
>> Um, so that's that's one example of
maybe adding persistence to your prompts
to actually get better performance out
of the model. So the next thing maybe
before we get there is maybe how do you
control having less eagerness in the
model. Um for that maybe one thing you
can do is actually control the search
depth for example. So here is an example

[00:33]
where we say actually want the search
depth to be very low initially when
you're like searching for a bunch of
things maybe in a codebase and this
these are some actions you want to do of
maybe you only want to go two tool calls
to search maybe not do eight of them and
eight different graps. Uh, Bill, I know
you're a big vibe coder, right? Like
>> Oh, yes.
>> Have you have you played around with
this and seen it perform well?
>> Oh, yeah. No, I definitely have. Um, I
think the the the the issue a lot of
times that I've seen with um like the
folks is that like JD5 would love to get
the answer correct. And so at times um
it sort of takes it has its own agency.
So it does a lot of exploration to make
sure that the answer is absolutely
correct. But for sometimes you actually
don't need that much. you don't need all
of that like you know context you you
also don't need things to be 100%
correct so in those case u having a
prompt like this was really helpful in
sort of steering down turning down that
uh the exploration eagerness in the very
beginning um yeah so I have seen a lot
of success with this so I I guess I have
a question for you like how how does

[00:34]
like eagerness compare to the the stuff
about persistence how do the two two
concepts differ
>> yeah so maybe you want more eagerness or
like more persistence if you want like
these longer task to be completed end to
end without any user input and then
maybe the user will then change things
as they go. But maybe you want less
eagerness. For example, if you want the
user to say okay, you want them more
brought along in the process and you
want them to give input as it's going
along. So you want the model to be more
of like a pair programmers.
>> I see. I see. So so instances where uh
you want the model to be more agentic or
like the other part could be like a
trade-off between collaboriveness.
>> Yeah. Exactly. Sweet. So that's like
maybe one prompting tip we have. The
next one is maybe how you would prompt
for preamble. So this is a new feature
that we added for GP5 where you can
actually prompt the model to give
explanations for the tool calls it's
doing. And you can do something very
trit right of in your prompt just say
before every tool call explain why
you're doing the tool call and then it
will do that. But we found that there's
a nice UX you can gather from actually

[00:35]
controlling this behavior. And since GP5
is a very steerable model, this is a
prompt that we typically like. Um, but
obviously change it for whatever use
case you're working on is all we kind of
like putting up an upfront plan. Uh, so
before the model calls any tools, give
it a plan. And then as it's calling
tools, maybe grouping them together or
summarizing them as you're working on
each distinct task. So we can actually
see this if we go to the playground real
quick. And I have uh a prompt here where
it's we're planning a picnic actually
and we've added this tool preamble and
we've added a bunch of MCP servers of
different stores for planning this
picnic. And then here I want to actually
plan a picnic for all of us in the room
here to somewhere in SF. Um and we want
to use all the items from these stores.
So let's give it a shot and see what it
does.
So as this is running, maybe I'll just
like walk through this preamble prompt,
right? Um we kind of always start with
always begin with like stating the
user's goal in a friendly manner. Um and
then once we do that we want to like

[00:36]
outline the structured plan and like
some detailed logical step and then as
you see your searches maybe like do some
additional lookups and narrate each step
for the user. So right now you see the
model's initially just reasoning and
thinking through the prompt as it's
given and then once it's thinking
through the prompt it will will start
reasoning through and maybe give this
upfront plan. So right now it's like
understanding the cart requirements and
like seeing that oh we've given a bunch
of MCP servers to the model and see what
it does.
>> So so how are you providing all of those
tools that like you mentioned MCP
servers can you tell me a little bit
more about those?
>> Yeah. Yeah. So as you can see in the
response API we can add a bunch of
separate tools. So obviously we support
all our hosted tools like web search
code interpreter etc. and also custom
tools. But now you can also add MCP
servers or your own custom functions
that you'd like.
Yeah. So maybe as this is going and
reasoning about its plan, um are there
places where you guys have seen like
preamles do pretty well or like helped

[00:37]
you guys?
>> Oh yeah, absolutely. As as you said, I
am a big coder. I almost forgot. I don't
think I can write code myself like from
scratch anymore. I don't even think I
can write a for loop anymore. Uh and so
like it's really helpful to be able to
have a model here that tells you walk
you through the different steps on when
it's building something just like Eric
has showed uh using codeex what exactly
it's building why it's building it and
sometimes actually if you have done
something wrong in the prompt you can
also catch uh sort of the mistaken uh
reasoning path that's going along go
going down uh using the preamles and you
can also correct your prompt accordingly
as well. That's what I've seen. What
about you Eric? Yeah, I think this is a
really good and like important UX to
have um like in your favorite coding
assistant whether that's like you know
Codex, Cursor, Windsurf um
it's really useful just to see like what
is going to happen before it happens. Um
and it means that like kind of as we
talked about the models are kind of
running longer and longer and so it's
really important to be able to monitor

[00:38]
what they're doing as they go and uh
people can just like stop or pause
workflows as as they you know go down
the wrong path. So it's like that
monitoring is really really important
and I found that very useful.
>> Cool. So yeah, as you see here, it gave
the plan and then gave it's thinking of
like why it's calling certain tools each
time and then as we see this will keep
running. But I think the final thing we
wanted to quickly show you is how you'd
use how you'd optimize your prompts
pretty quickly in the playground itself.
So the final example, let's make it
pretty quick, is we have this
instruction following example here. This
example actually has a bit of
conflicting instructions um which we'll
notice when we put it in to this tool.
I'm just going to ask
can you fix
the conflicting instructions?
Um, and maybe to briefly explain maybe
where the conflicting instructions are
is you'll see this section right here
where it says always look up the patient

[00:39]
profile before taking any actions to
ensure that they're an existing patient.
Um, but then we have this section here
which is for high acuity orange cases
auto assign the same day. Um, if
explicit consent is on file proceed to
book and notify the patient if consent
is unknown just like book it
immediately. So the change we made if we
click it is clarified the high acuity
use cases and the assistant must
tenatively state at the earliest day
time slot. So this is an example of
using metarmpting and using our tools to
hopefully help improve your prompts
pretty quickly. Obviously this is a very
short example but we've seen this work
pretty effectively for a lot of
customers we've been working with. Um
and yeah at with that maybe I'll pass it
off to Christine.
>> Awesome. Thanks Nuke. Um, so up until
this point you've heard a lot about
coding, tool calling, the responses API.
Um, so I'm really excited to bring this
to a real world application. A lot of,
um, you guys tuning in are founders
yourselves. So would love to welcome
Riley, the founder and CEO of Charlie

[00:40]
Labs, um, on stage with us.
>> Hey Christine,
>> how's it going?
>> Thank you very much for having me. Uh,
I'm excited to be here about how Charlie
is using GBG5.
of course. Um, so I'll let you take it
away.
>> Perfect. I'll jump into a screen share
here. Um,
quick intro on myself. Uh, just in case
you were concerned, I wasn't a technical
co-founder and you shouldn't trust me.
Um, this is my GitHub profile. Uh what's
most interesting here is uh this period
here which is where we got early access
to GVD5 and my productivity personally
increased so much that it washed out the
rest of this chart which is pretty wild.
And then one other quick note here is if
you look at code review verse other over
time and you go back a couple years
you'll see how much programming is
changing. Um so what is Charlie? Uh
Charlie is a Typescript focused coding

[00:41]
agent. Um but he's not an IDE uh or a
CLI tool that runs locally on your
machine. Um you interact with him via
GitHub, Linear, and Slack just like you
would with any humans on your team. Um,
the normal workflow looks something like
chatting with Charlie in Slack to
brainstorm, moving that into a linear
issue, maybe polishing it up, and then
asking for a PR and then reviewing and
iterating uh in GitHub until it's ready
to merge. Um, I'm going to do a quick
demo as part of this. Uh, this is a a
demo repo of the apply patch tool. So,
this is our implementation of the apply
patch tool that we'll talk about more.
Um, this is a Slack or it's hooked up to
that repo. Um, as well as a linear
workspace. And you can see I seated it
here with a couple of questions. I asked
Charlie, read the read me and see if
there's anything that's wrong or could
be improved. Um, search the repo for
bugs and let me know what you find and
look for outdated comments. Um, these

[00:42]
are just kind of simple demos so that we
can do this in time. Um, if you jump
into one of these, you'll see. So, this
is one where I asked Charlie to look for
bugs. He searched through a whole bunch
of stuff. Um, interestingly, he also ran
the tests and types and was like,
"That's all good." Uh, and then had a
list of things that we may want to fix.
Um, so I said open a linear issue for
the normalize method suggestion and
another one to handle the case only file
renames that he pointed out. Um, so he
did that. Uh, this is the issue. One of
the nice things about making issues from
Charlie is that they look very nice and
they're fully written, which I don't I'm
sure most of you have never seen an
issue from an engineer that looked
anything like this. Um,
so those messages resulted in these five
issues which I'm going to quickly assign

[00:43]
to Charlie. Um, and then so he's going
to get started on all five of these
while we jump into
explanation of how Charlie works. Um,
so this is GitHub, Slack, and Linear.
Um, Charlie receives web hook events for
all kinds of actions. Um, and then he
also has the ability to write back to
those platforms. uh and when he gets
that um he's going to start uh talking
to GBD5 as the main driver of the agent
loop. Um we are using the responses API
uh which has worked very well. Um one of
the other nice things about that is that
we're using the built-in web search tool
uh which is also fantastic. Like that is
such a simple ad and increases results
uh a lot in a lot of different ways. Um,
so then once Charlie's running, Charlie
really only has one tool um in his agent
loop other than the web search tool,
which is run a bash command. Um, so he
spins up a VM uh powered by run loop

[00:44]
that is set up specifically for writing
TypeScript code. Um, so it has a bunch
of the dependencies, the tools, and then
a normal flow would look something like
using rip grip instead. If you guys have
run bash commands, you've probably seen
how much GB5 loves using said. Um,
that's going to gather some context. And
then we use the apply patch tool, which
is a really smart way to edit code
efficiently. Um, it works far better
than search and replace or rewriting
entire files. Um, and then running some
tests. Uh something where GP5 really
stands out here is if these tests fail,
um that historically could be quite
problematic for models to get thrown off
track and being able to backtrack to
actually fix it. Um GBT5 is really good
at kind of recovering from both being
smart enough to run the commands and
then also to recover from them. Um and
then he'll make a commit and open a PR.

[00:45]
Um,
a couple of the things that GBT5 really
stands out for here is the ability to
work with a wide range of platforms. Um,
because we're like sometimes he's
opening PR, sometimes he's creating
linear issues, sometimes sending Slack
messages. So, there's actually a lot of
different commands that can be run here
depending on what the user asked for and
where the event came from. And GVD does
a really good job with that.
Um, quick emails for comparison. Uh so
this is our internal PR creation eval
which is like Sweetbench but uh actually
creates a real GitHub issue and the
agent has to create a PR not just a
diff. Um we saw 16% improvement from 03
uh using exactly the same prompt. Um and
then after we optimized it we got up to
a 29% improvement from 03 which is
pretty awesome because when we switched
to 03 we switched from sonnet and saw a
similar size improvement. um when we

[00:46]
made that change and then PR review evo.
So this is we have a way to evaluate the
model's ability to find bugs and also
not uh leave comments that are incorrect
or noisy. Um we saw 5% improvement over
03 which 03 is already pretty good. Um,
and kind of to balance that, we ran the
evals with a claude obus 41 and it was
46% worse um than five.
Um, and because we kind of had to do it,
um, we ran a head-to-head of Charlie
versus Cloud Code where we used Charlie,
we got 10 issues from open source
projects, um, ran Charlie on them and
then set up Cloud Code with the GitHub
action so it could generate PRs from
those issues as well. Um, and then we
use this series of LLM as a judge. You
can go to the um link here. It's
research.tchylabs.ai
for more information, but uh Charlie won
10 out of 10 of the comparisons um and

[00:47]
scored better in aggregate for
testability and quality and description.
We've had some challenges with the
veracity. That's been our biggest battle
with five. Um, but overall really good
results. Um, we've been really happy
with uh how Charlie has been working
with five. Um, we can quickly look back
and see where we're at here. Okay, so
these five issues, it looks like we have
four PRs already. Um, we can jump into
one of them. Um, so this is Charlie will
open a PR under his account. uh context
on what was changed, how it changed. Uh
he's really good about running
verification to prove whether the
changes actually work. One of the nice
things about Charlie is you should be
able to oneshot a lot of PR is like I
don't actually open an editor or a
terminal very often anymore because
Charlie is so good about making sure

[00:48]
that this PR will pass. Um and then he
also will review his own PRs. So he had
some advice here. We're not going to
have time to see it, but um I can say
yes, please to that advice. Um and then
what's going to happen is Charlie is
going to go he's going to get this. He's
going to go read this and he'll push a
commit to this PR to fix um the issue
that he pointed out.
Um and then this is so there's four
other PRs that came out of this. Um it's
pretty amazing being able to work in
parallel like this. It's like I'll often
if I have a bunch of meetings come up
just coming up queue these up and fire
them off and then when I come back I
have a whole bunch of PRs waiting to be
reviewed and merged.
>> Awesome. Thanks so much for sharing this
Riley. Um I'm going to drop um Charlie
uh in the chat so you guys can give it a
try. Um really appreciate your time.

[00:49]
Thanks a lot.
>> Perfect. Thank you.
>> Thanks Riley.
>> Thank you Riley.
Okay, so now we have 10 minutes left for
some Q&A. Let's get into it.
>> Let me uh actually share my screen once
again.
Okay, hopefully everyone can see my
screen. And here we have the questions
that y'all have put up. Uh so the first
one is what are your best practices for
context engineering uh especially in the
space of coding? Wow, this is a very
good question and I I frankly don't
think we can, you know, answer it fully
u in the 10 minutes that we have and we
also want to answer other questions as
well. But I think I I'll just I have
something on top of my mind. I think
perhaps you two can dig into it as well.
Um but for context engineering
especially in the space of coding, this
is um like definitely uh a really
interesting topic. uh GPD5 while it

[00:50]
performs pretty well across the long
context, it still has a fixed context
window of 400,000 right now, input plus
output. So being able to figure out what
parts of um what thing what are the
things you want to throw in that context
is very very important as well. So we've
seen successes with people using uh
summary models that compacts uh the the
the past parts of the conversation as a
conversation goes longer. So the model
can focus on the the newer and more
relevant information. We've seen a lot
of success with that. The other part
that we've also seen a lot of success
with is for like the simpler tasks
actually like our recommendation is just
that you can also just toss a lot of
like sometimes entire repo in there.
That's fine. But for context engineering
uh when the things get too long uh
summarizing the older parts of the
context compacting it is the recommended
way of going forward as well.
>> Yeah. My thought here is the models are

[00:51]
very good at using tools like
particularly like even very simple tools
like the terminal tool um which is very
generic. So
I another recommendation I have is if
you have like a full context and like
well a large repo um you can give an
outline of the file structure or um
interesting like things that you should
look at and then the model can decide on
its own to call tools to find that
context. Um and in combination with like
summary models or compaction I think
this is very powerful um for reducing
like for using the most effective
context that you need. Yeah, I think
plus one on the the tools piece of and
also it's like helpful to have a section
in your prompt probably around like tool
decision boundaries so you can be clear
of when you want to grab certain pieces
of information for the model.
>> Yeah. And on that piece just to double
click on that that GPD5 is very
steerable. So it should respect the tool
boundaries that you outlined very
carefully. And then the other part is
GD5 also excels at parallel function

[00:52]
call calling. So for a lot of those
exploration context gathering parts uh
make sure that you also put in the
correct infrastructure in place to take
advantage of the parallel uh context
gathering capabilities.
Uh the next question is how does
verbosity affect the instruction I
provide? For example, if I ask for a
1,00word essay and set verbosity low,
will it not follow the instructions?
That is a also a good question here.
Eric, I'm wondering if you might have
some thoughts here.
>> Yeah. Yeah. Um
this is a challenging question actually.
My my intuition I actually haven't
tested this myself. Um
my intuition is that a thousand words is
probably short enough that verbosity
won't matter too much. Um I think it's
some longer lengths like say you want
like a 10,000word essay or even like an
100,000word essay. um verbosity will
take precedence. I think overall like

[00:53]
the hierarchy looks like like roughly
how I think about it is like at
verbosity high there's no limit um and
so the model will just like follow
whatever instruction but at verbosity
low um the verbosity like has an
increasing effect as like the essay that
you ask for gets longer and the
verbosity kind of takes precedence
although it's sort of a soft um impact
on the model. So I'd recommend if you
want this kind of like steerability, set
verbosity to high and then say what
instruction you want for how long
something should be.
>> Yes. So verbosity is uh is a library in
the API that you can use. But also at
the end of the day, it sounds like the
prompting is is also highly effective
even if you just set verosity to high.
>> Yes.
>> Cool. Let's move on to the next one. Any
tips for generating code while
minimizing slop? Wow. Swap is is a
common word.
>> I love the word swap.
>> Yeah. What does that what does that word
mean? Like I think Well, I'm a bit of a
a like previous generation folks. I'm

[00:54]
kind of getting old these days. I think
a noob. You're the youngest person here.
Like what does that mean?
>> Yeah, I guess it just means not not good
code quality. Um maybe like the tips for
generating good code. I think our uh
general advice here is having some sort
of style guide in your prompts help the
most for minimizing the slop. uh as the
Gen Z people say I guess or or tech
debt. Um that's the main one. Maybe Eric
or Bill, do you have anything else? But
I feel like that's the main one, right?
>> Yeah. Um I think that's a big one. Um I
think something I do while working with
GPD5 is um like give it the feature list
that you want and then just say like be
minimal. Otherwise, the model's pretty
good at doing this, but I think like
that extra little reminder does help. um
depending on the kind of application
that you're working on. This doesn't
this isn't always true. Um saying like
build minimal tests and like run them um
that also helps a lot and like makes the
code that it writes like usually like
more correct like more

[00:55]
well structured um and just generally
improves things.
>> Yeah. And I think on my part, I I've I
don't think I'm the most uh qualified to
comment on this because I kind of
embrace as a slop uh because a lot of
the things I build that's also another
way to go. So uh one thing is the models
will keep getting better and uh like
these days you call it slop. I think
like tomorrow like the models that Eric
has mentioned like the super agentic
models that can take task from end to
end that can handle vagueness. Well,
maybe it's going to generate that like
slop slop that it like should not be
called slop anymore. And I think I look
forward to that day.
Um, but like even today, I think GPD5 is
uh really good as in in the sense of
following the instructions you give it
so that if you actually just say things
like, hey, I want this to be minimal. I
want this to be maintainable, it will
actually respect a lot of that to write
maintainable, readable, uh, correct
code. Yes,

[00:56]
>> it's crazy how much of a difference a
little bit of a prompt makes, right?
It's really calling back to like your
point on prompt really makes a
difference in
>> how is GPD5 better for MCP tasks. So,
yeah.
>> Yeah, I I I can take this first. Um, the
model is much better at function
calling. Um, we spent like quite a lot
of time on this. it should be better at
both novel functions that you give it as
well as sort of the like bless set of
functions that everyone uses like
terminal and and such. Um so without
going like too granularly into it I
think it's just it is better is is the
top line.
>> Well I don't think there's anything else
to add to it. I guess like GPD5 is just
just
>> make your MCP um Yeah. Oh yeah. Okay.
Like I think the point and steer ability
is also big. Um, I think it's important
to like tune the decision boundaries on
your tools um, pretty carefully. Like
the model will get pretty close um, to
what you want, but because it's so
steerable, it's easy to really dial in

[00:57]
that like last bit on on MCP and tool
uh, decision boundaries.
>> Yeah. So, a lot of times I I like double
click on the decision boundary part. Uh
a lot of times when folks are thinking
that the wrong tools are getting called,
uh it also goes back to the the
prompting stuff is that you're actually
not really specifying the decision
boundaries well. And so sometimes a
model's default prior behavior is a
little bit different from what you think
is a best case scenario. It's worthwhile
to spend a little time uh optimizing for
it.
>> Awesome. Uh I think that's all that we
have time for for this build hour. We
tried to get to everyone's questions,
but um if your question wasn't answered,
highly recommend you check out our new
developers.ai.com
um page. We really consolidated all of
these resources that you see. I just
highlighted a few um over here on the
right for you. Um but I will be sending
out a follow-up email with the recording
um and links. So don't worry about
writing all of these down. Um, and then

[00:58]
also the the code repo. Uh, so you guys
can try everything that we did today.
Um, last slide is just to share our
upcoming build hours. September 3rd is
all is going to be all about codecs. You
got a little bit of a preview today with
with the Eric's building um, Minecraft,
but um, we'll dive a little bit deeper
uh, into this and then definitely
bookmark our our homepage because we're
constantly adding new build hours. Um,
and definitely send us your feedback. So
with that, thank you everyone for
joining and we'll see you September 3rd.
>> Thank you all.
>> Thank you.

</details>


[### Prompt Optimization Tool

Interactive playground to refine prompts

Learn more](https://platform.openai.com/chat/edit?models=gpt-5&optimize=true)

---

## Step 03: Steer GPT‑5 with reasoning, verbosity, and new capabilities

GPT‑5 introduces new controls that let you fine-tune how the model reasons and communicates. These capabilities help startups match model effort and output to the unique complexity of their products.

##### Reasoning effort

`reasoning_effort` controls how much the model thinks (and how readily it calls tools). The default is `medium;` options are `minimal`, `low`, `medium`, and `high`. Experiment to right-size effort to the complexity of your task and measure against your evals using the [prompting guide⁠(opens in a new window)](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide).

##### Verbosity

`verbosity` influences the length of the model’s output. Options are `low`, `medium`, and `high`. You can also add prompt instructions for scenarios where you want the model to override the default.

##### Experimentation guidance

GPT‑5 is highly steerable. These parameters give you more control over model behavior. There’s no single deterministic best configuration - systematically experiment and evaluate to identify what works best for your use case.

###### New & enhanced capabilities

[### GPT-5 Build Hour

Live coding session showcasing GPT-5 capabilities.

Learn more](https://youtu.be/ITMouQ_EuXI?feature=shared&t=151)

[### Using GPT-5

Quick guide to get started and build effectively.

Learn more](https://platform.openai.com/docs/guides/latest-model#page-top)

[### New parameters and tools

Overview of the latest features and settings.

Learn more](https://cookbook.openai.com/examples/gpt-5/gpt-5_new_params_and_tools)

[### Preambles

Tips for setting strong context in prompts.

Learn more](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide#tool-preambles)

[### Latency optimization

Techniques to speed up responses.

Learn more](https://platform.openai.com/docs/guides/latency-optimization#page-top)

[### Cost optimization

Strategies to reduce usage costs.

Learn more](https://platform.openai.com/docs/guides/cost-optimization#page-top)

---

## Step 04: Troubleshoot using common patterns

From working closely with hundreds of startups, we see recurring issues such as overthinking, underthinking, over-deference, overly verbose outputs, latency problems (see [Latency Optimization⁠(opens in a new window)](https://platform.openai.com/docs/guides/latency-optimization#page-top)), tool overuse, and malformed tool calls. Because GPT‑5 is highly steerable and eager to follow instructions, careful prompt tuning—paired with solid evals and metaprompting—resolves most of these quickly. For deeper guidance on diagnosing and correcting each pattern, explore the [GPT‑5 Troubleshooting Cookbook⁠(opens in a new window)](https://cookbook.openai.com/examples/gpt-5/gpt-5_troubleshooting_guide).

---

### About the authors

This guide was developed by [Hillary Bush⁠(opens in a new window)](https://www.linkedin.com/in/hillarybush/), Startups Account Director, and [Prashant Mital⁠(opens in a new window)](https://www.linkedin.com/in/pmital/), Startup Solutions Architect, based on their experience working with top startups leveraging GPT‑5.

They created this guide after helping dozens of early-stage and growth-stage startups adopt GPT‑5 in production, seeing consistent patterns in how the most successful teams migrated APIs, tuned prompts, and used new reasoning controls to ship faster and build stronger products.

The goal of the OpenAI Startups Team is to share these best practices broadly so any startup, whether pre-seed or scaling globally, can accelerate its journey from idea to impact with GPT‑5. We hope you found this guide useful – happy building!

## Interested in bringing AI to your business?

Learn how we help companies build scalable, responsible AI strategies.

[Try ChatGPT](https://chatgpt.com/)[Contact sales](/contact-sales/)

## Sources cited

* [Greg Brockman @gdb, X⁠(opens in a new window)](https://x.com/gdb/status/1957851156564042012)
* [Alex Duffy @alxai\_, X⁠(opens in a new window)](https://x.com/alxai_/status/1955082871426748638)

## Keep reading

![How agents are transforming work > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7hmtkjKv0DxS4Yt8mQZju2/c168bfa2010da64bcc9dd60d6b5491e8/Art_Card__1_.png?w=3840&q=90&fm=webp)

[How agents are transforming work

CompanyJun 25, 2026](/index/how-agents-are-transforming-work/)

![OpenAI and Broadcom Jalapeño inference chip card image](https://images.ctfassets.net/kftzwdyauwt9/21KcazqOHUF7Cq71Hpfcnc/81ad98a1978845b441ab14e008168c75/openai-broadcom-jalapeno-inference-chip-image-1_1.png?w=3840&q=90&fm=webp)

[OpenAI and Broadcom unveil LLM-optimized inference chip

CompanyJun 24, 2026](/index/openai-broadcom-jalapeno-inference-chip/)

![Helping build shared standards for advanced AI - card image](https://images.ctfassets.net/kftzwdyauwt9/3tqr0Vb3JnK38uBRBw7FAF/a3989888ee148ba286b834076aaa289b/helping-build-shared-standards-for-advanced-ai-1_1.png?w=3840&q=90&fm=webp)

[Helping build shared standards for advanced AI

Global AffairsJun 23, 2026](/index/helping-build-shared-standards-for-advanced-ai/)
