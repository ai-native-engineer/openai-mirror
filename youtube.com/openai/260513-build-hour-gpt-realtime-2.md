---
title: "Build Hour: GPT-Realtime-2"
channel: openai
url: https://www.youtube.com/watch?v=qGS9Ghnq1RU
youtube_id: qGS9Ghnq1RU
published: 2026-05-13
duration: "43:00"
captions: en-orig
---

# Build Hour: GPT-Realtime-2

[![Build Hour: GPT-Realtime-2](https://img.youtube.com/vi/qGS9Ghnq1RU/hqdefault.jpg)](https://www.youtube.com/watch?v=qGS9Ghnq1RU)

<details>
<summary>자막: Build Hour: GPT-Realtime-2 (43:00)</summary>

[00:00]
Hi everyone, welcome back for another
build hour. We're so excited to have you
here today. My name is Sarah Urbonas. I
lead startup marketing here at OpenAI. I
am joined by two absolute legends who
internally need no introduction, but
Terry, Erica, can you introduce
yourselves and share what you've been up
to this past week?
>> Absolutely. So, I'm Terry. I am
a multimodal API PM here.
>> And I'm a solutions engineer on our
technical success org helping our
largest digital native customers scale
on our API platform.
>> And so today, everything is about GPT
real-time two, which we just released
last week. So, the goal of build hours
is really to empower you with the best
practices, tools, and AI expertise to
scale your company using OpenAI APIs and
models. Whether you're a founder or an
engineer at a larger company, we hope
what you learn today can actually take
these products and put them into
production, help you scale faster. You
can sign up for all of our build hours
at the link below. Um, and also find

[00:01]
them on YouTube. So, there's lots of
great content that we have, and we're
going to jump right into it because we
have a packed hour. So, today we're
going to go through kind of just an
overview of what we released last week,
um, share a little bit more about what
you can specifically build with and
where you should focus on, as well as
going through a couple of specific
demos. So, we're first going to go
through voice-powered search agents,
then product analytics dashboard. As
always with build hours, we're going to
build these live, so pray to the voice
demo gods that everything works out. And
then, we are really excited to be joined
by the team at Sierra. They're going to
share how they're building with
real-time two, and also some tips from
the pros with building with voice agents
in general. As always, we will save some
time for Q&A at the end. There's a Q&A
button that you'll see on your screen.
As we're going through the session
today, feel free to ask questions there.
We have folks in the studio who will
answer them live, and then at the end,
we'll always save some time to answer
questions both with Terry, Erica, and
the Sierra team.

[00:02]
So, with that, let's kick it off.
>> Amazing.
>> Awesome. So, we had a big audio drop
last Thursday with three new models.
Uh so, we'll go through them today.
Here's just a quick very uh quick view
of everything going on. Um but, we
wanted to actually show you
uh and immerse you in the experience.
So, we're going to go through some
demos.
Um so, then for the next slide, we're
going to make sure to
uh we want to know where everyone's
from. And so, if you could just drop a
flag for where you're calling from or
where you're dialing in from, uh we want
to show you potential translation model
in this
um potential language. So,
yeah.
>> Looks like we have We always have a lot
of Spanish speakers in the room, so
let's choose that for translation. I'm
going to pop over to our translation
demo.
And Terry, I'd love you to give this a
spin.
>> Cool. So, when I wake up this early, I'm

[00:03]
I'm really
Uh so, because I'm hungry, I'm going to
talk about some breakfast items.
>> Ooh, great idea, Terry.
>> An acai bowl.
What's better than breakfast is
potentially a new OpenAI
>> Okay, so I'm going to stop with the
translation
>> [laughter]
[clears throat]
>> Okay, so I'm estoy emocionado.
Let's see.
>> So, you can see here on the left is our
transcript, and then the output
translation transcript.
>> Absolutely. So, number one, you're
already seeing in action, which is the
real-time translate model. So, it
conversations that feel like language
barriers disappear. It supports over 70
input and 13 output languages with low
latency streaming translation.

[00:04]
And it's really great for video calls,
live streams, customer service.
And then also you're seeing number two,
which is our GBT real-time whisper
model.
That's secretly powering this experience
as well, where you can see streaming
capability with tunable latency as low
as 200 milliseconds with 80 input
languages. And so, that means you can
have earlier function calling, better
instruction following, and live products
will feel faster, more responsive for
captions, meeting notes, ambient agentic
context. And then we have our third
model that we released as well that is
GBT real-time two.
So, you'll see here it is our most
intelligent voice model.
It brings GBT 5 class reasoning into
voice.
And it's very strong at prompt
adherence, talk tool calling,
multilingual performance, which are all
critical to voice production workflows.
And so, you now have these three
different ways that you can build. So,
you have voice to action like hands-free
voice driven apps. You have your systems

[00:05]
to voice, which is like a voice chief of
staff, but it's organized into spoken
voice. And then you have voice to voice
like customer service calls. Companies
like T-Mobile use it all around the
world.
>> And someone commented in the chat in
Spanish and said, "Wow, that's good."
So, I'm assuming that it translated.
I'll say you both and oat milk latte was
>> I was I was worried about that.
>> [laughter]
>> It actually hopefully everybody could
hear.
We have dynamic voice cloning as part of
this. So, we can have multiple speakers
and you can actually tell the different
people are speaking, which I think is
really cool.
>> tone matching is really great for sure.
Cool. And then for real-time two,
there's a bunch of new capabilities. So,
beyond just like the emotion matching
that you get from voice to voice,
there's also things like preambles where
you can say, "Let me check on that."
Like a real human would before
reasoning.
There's also increased context windows.
This was a major request that we had. It
increased 4x to 128k now.

[00:06]
And so that roughly translates to
>> Like almost an hour which is also
coincidentally our session.
>> [laughter]
>> So it really increases the instruction
following the intelligence because we
don't have to truncate.
>> Yes, exactly. And then there's also
parallel tool calls. So you no longer
have to like waterfall the tool calls.
There's also better domain vocabulary
and understanding like healthcare or AI
terms. And then there's context over
turns which means better agentic
behavior. And then controllable
expressiveness. So you can try telling
it to whisper, be excited, jealous, you
try different things. We're excited to
see what you come up with. And on
benchmarks you'll see major jumps in
both intelligence, instruction following
and tool calling.
And so yeah, I'm very excited about the
next wave of AGI that'll be more global,
hands-free,
more accessible to everyone around the
world. But now we're going to have Erica
actually show us what the it's like
under the hood.
>> I'm really excited to show off our first
demo today which is an e-commerce site

[00:07]
with a voice powered search agent.
In this demo the real-time API is
powering search that's not just chatting
but actually operating the UI through
through tool use. And I think this
really highlights the power of our
reasoning models and parallel tool
calling. So let me pop over.
So I have been planning this trip to the
Pacific Northwest. I'm going hiking. I
have already bought a few things from my
favorite trail supply company. And I
need to keep shopping. So I want to use
the Supply Co shopping assistant to help
me make some more purchases.
Hey, can you remind me where did we
leave off? What do I still need to buy
for this trip?
>> I'll pull up your shopping plan and see
what's still missing. You still need a
tent and hiking shoes. Your daypack,
trail socks, and insulated bottle are
already covered. Which one do you want
to look for first?

[00:08]
>> Um let's start with tents, and I want to
see tents under $450 that would fit
three to four people.
>> I'll search tents and narrow to options
under your budget.
Two good options are highlighted. One is
a higher-rated three-to-four-person tent
at $419.85
with free shipping tomorrow.
The other is a quicker open style at
$357,
but it's not marked as full stock.
Do you want to open
>> Okay. Actually, can you tell me about
any one- or two-star reviews on the more
expensive tent?
>> I'll scan the low-rated reviews for that
tent.
The low-star reviews mainly say setup
can be slower than expected the first
time, and it's not a great pick for
heavy storms or strong wind and
downpour.
For a typical Pacific Northwest weekend,
those complaints aren't dealbreakers if
you expect light to moderate rain, but
I'd switch to a more storm-ready tent if
you expect rough weather.

[00:09]
>> You know, I actually haven't checked the
weather in a while. Would you mind
looking up the forecast for the Seattle
area the weekend after next for me?
>> I'll check the Seattle forecast for that
weekend and weigh the storm risk. Storm
risk looks moderate. Some rain and a
breezy spell, but not a clear storm.
That tent is probably fine for a normal
rainy weekend, but I'd use a footprint
and solid stakes.
>> Okay, that's good advice. Um okay, add
that to my cart, and then let's move on
and look at some waterproof hiking
boots.
>> I'll add the tent to your cart, then
I'll check your safe size and find
waterproof boots.
I added the tent to your cart. For
waterproof boots in US 10 with free
shipping, I highlighted a higher rated

[00:10]
pair and a cheaper pair.
Do you want to open the higher rated one
or the lower priced one?
>> Um
let's look at the cheaper one first. Can
you show me the product page for that?
>> I'll open the cheaper boots product page
so you can review the details. This pair
is $224.85,
rated 4.5 stars, and has free shipping.
US 10
>> Okay, well, I see a break-in takes a few
hikes. I've got to get busy in the next
2 weeks, but otherwise I kind of want to
save a little bit of money here. So, can
you add these ones to my cart and then
pull up my cart? I want to see my total.
>> I'll add these goods in US 10, then I'll
open your cart so you can see the total.
Your cart has the tent and the boots,
and the total is $644.70.
I can't check you out here.
>> Is there anything else? Like, tell me a
little bit about these optional add-ons.

[00:11]
>> Nice optional add-ons would be a rain
layer and a tent footprint stay kit,
since they help in wet breezy
conditions.
>> Yeah, maybe I'll come back for a rain
layer, but I think this is good for now.
Um thanks so much for helping me shop.
>> You're very welcome, Erica. Have an
awesome trip, and I'll be here when
you're ready for that rain layer.
>> Amazing. Okay, so the thing I think is
really exciting here is our model sounds
really good. It sounds really natural,
the voice is really steerable, but the
most exciting thing is this
intelligence. It's operating the UI
through tools. It can choose between I
think I'm passing it 15 or 20 tools
here, which is something that was way
beyond what we could expect or
um you know, would recommend for our
previous real-time models. So it can
choose between those tools, it can
inspect the current page and decide what
actions are needed. You could see it was
calling multiple tools in a row when
that was what was needed, including

[00:12]
external tools like weather, so that I
didn't have to leave the Supply Co site
in order to understand like what
purchase I should make. Um so I think
this just leads to a lot more natural
than our kind of speech in single action
out previous workflows. This is like an
actual shopping assistant that can
reason across all these tools and update
the visual experience as it talks.
Um so I think the next thing I want to
show you is really the other side of
this. So I was just a shopper on an
e-commerce website, Supply Co, but now I
want to demo as if I'm the product
manager of Supply Co, and I think this
is really interesting because I think
anybody who's used ChatGPT or other
maybe voice-to-voice solutions is kind
of like understands this. Um I talk, the
model talks back kind of experience, but
really we're thinking about voice to
action as this new kind of workflow
because the model's so good at tool

[00:13]
calling. And not everybody wants the
model to constantly be talking back. Um
so I'm going to swatch swap over to my
product analytics dashboard, right? So
I'm a product manager at Supply Co.
And actually
um there's a lot going on this
dashboard, but so I I kind of want help
with this. If only I had an AI assistant
that could help me with this. Um the
thing I've I've hearing is about Europe.
So let me open up my session and start
talking.
Um let's filter by Europe. That's what
I'm hearing issues about right now.
Cool. And let's look at the last 7 days
and compare that to the 7 days prior.
Okay, cool. Yeah, I can see a big drop
there.
Um looks like Safari is a problem. And

[00:14]
oh, I can see thanks for highlighting
this.
Um
can you point out any other filters that
you think
um
would be relevant here to this
investigation?
Okay, cool. Okay, so filter by voice
search, first-time shoppers, and
footwear. We'll start there.
Cool. Okay, yeah, I can see this is like
a huge activation drop-off.
Um
Okay, what's next? Actually, can you
kick off the root cause investigation
here?
And I think I just want to compare
mobile Safari to Chrome cuz that seems
like where a lot of these issues are
taking place.

[00:15]
Perfect.
Yeah, Safari is really the problem here.
Okay, let me expand this back open.
Metric Loop, can you give me a
two-sentence overview out loud um
explaining this root cause investigation
so I can explain it to my engineering
team.
>> The investigation shows a mobile Safari
specific regression where the product
detail page size selector validation
doesn't update correctly. So first-time
Europe footwear shoppers get stuck after
choosing a size and can't add to cart.
Chrome is near baseline, which points to
the PDP release behavior on Safari
rather than a broad traffic quality or
search issue.
>> Okay, amazing. This is super helpful.
I'm going to pass this on to my
engineering team in a ticket. Super
helpful. Thank you so much. Um okay,

[00:16]
cool. So
why do I think this is cool? The model's
good enough at instruction following
that it only talked when I asked it to.
Like I didn't need it to confirm with me
every time it did a filter. I just
wanted it to take that action so I
didn't have to go through and click
myself. And I can go in, click in and
see its reasoning at any time and see
the transcript so that I can interact it
with chat as well. Um this to me is a
huge step forward in intelligence, in
instruction following, and it means that
the model can behave like an analyst in
the loop. So like the e-commerce site,
I'm passing in a ton of tools. I also
asked the model to reason over a huge
amount of mock data, which I think is
really exciting because we have that um
reasoning, it can actually write code,
it can create dashboards, it can make
artifacts. Um our old models could
handle simple voice commands and call
some tools, but I hope this demo shows a
more durable pattern. Right, this is a
real-time agent that can actually route

[00:17]
across tools, um maintain investigation
state, and turn this live analytics
workflow into something conversational
without actually losing developer
control over the data or the UI.
And with that, I want to pass it back to
Terry to talk a little bit about some of
the use cases that we're seeing for
voice.
>> Yeah, so we're really excited for you to
build with voice interfaces across
agents, across apps. Here are just some
of the use cases that were
we'd love to show you. So, there's a lot
of smart device integrations that you
could potentially think about, different
coding assistants, and voice experiences
that make things fast, easy. There's
mobile apps you can add a voice box to
for any kind of voice experience.
There's the video game up and down and
jump experience that you could control
with voice. You have coaches, like
public speaking coaches, note-taking,
finance voice US, agentic voice video

[00:18]
calls. All this can be done with a voice
layer now. So,
really exciting time that we're in where
you know, in the future kids will learn
will speak to AI more than they will
even necessarily know how to type to AI.
So, we're ready to build for that wave.
And
the other just slight nod here is that
all these were created to with GBT image
too. So, if you're in a place where you
just want to ideate and you need more
brainstorming, GBT image 2 can do some
of this for you or some mocking as well
for different concepts. So,
Yeah. Amazing.
>> And I think next we're switching to our
customer spotlight. So, I think we're
really excited to have the Sierra team
here.
I know we have Ken and Soham. Are they
on the line?
Can we hear them?

[00:19]
>> Yes. Can you hear us?
>> Oh, sorry.
>> Hey guys.
>> Hi.
>> Hi. There we go.
>> Hello. Hey. Hey Soham, Ken Murphy. I'm
an engineer on the voice team at Sierra.
Uh so, Sierra helps businesses build
better, more human customer experiences
with AI.
So, in practice, we build AI agents that
can resolve real customer service issues
end-to-end, not just answer questions.
So, many of our customers are large
enterprises, including many Fortune 100
companies, which means these agents need
to work at high scale,
and integrate with complex systems, and
follow nuanced business policies. So,
you know, on the slide, here are a
couple examples of the incredible brands
that we work with and the scale that
we're operating at.
So, what makes this technically hard is
that the agent is not just generating a
response, it's deciding when to act,
what tools to call, what information to
use from a large knowledge database, and
whether a given action is allowed.
So, in a customer-facing environment,
small error rates quickly become real
business risk. So, an agent that

[00:20]
hallucinates a policy or takes the wrong
action even 0.1% of the time is just not
shippable.
So, the challenge is not just, can we
make the agent sound natural, it's
whether we can build, evaluate,
constrain, and operate agents that
businesses trust to represent them
directly with their customers.
So, now we're going to look into what we
built to operate agents at the scale and
how we're using the real-time API.
Oh, hello.
>> Hey Ken, this is Jade from Demo Lots.
We've got great news, but first I got to
say, you may verbally opt out at any
time. This call may be recorded for
quality.
Last time we chatted back in March, you
were eyeing Noe Valley. Has that shifted
at all?
>> Uh yeah, still
uh still looking in San Francisco, but
now in the Sunset.
>> Staying in San Francisco and shifting to
the Sunset makes sense for a lot of

[00:21]
buyers.
Are you looking for a single-family
home, condo, or
>> I'm looking for a single-family home.
>> Got it. Single-family homes in the
Sunset can be a nice fit.
What's your budget or max purchase
price?
>> About 350k.
>> Your licensed mortgage banker Sarah is
here to help. You're in great hands.
>> Well, so so that's an example of of one
of the demo agents that we've been
testing. Um so in general, we're very
excited about real-time too. You know,
directly goes after some of the biggest
production voice problems that we face.
So you know, latency, turn-taking,
reasoning, and speech quality. Like
voice is pretty unforgiving. You know, a
pause of even half a second can feel
awkward or broken.
And that's why the voice-to-voice
architecture is so compelling. So we
don't have to have this separate uh
speech-to-text transcription or
text-to-speech synthesis. Instead,
real-time can just cut out parts of the
traditional cascaded stack and make the
interaction feel faster, smoother, and

[00:22]
more human.
Uh but while real-time 2 gives us a
stronger foundation, like at Sierra, the
the model is just one piece. Around it,
we still run our agent harness,
which handles all of the additional
infrastructure needed to run agents
reliably and securely in production. So
with that harness, we define the
workflows needed for each individual
customer. Uh that includes the tools the
agent can use, language and branding it
should follow, guardrails it needs, and
the grounding required to keep it
aligned with the customer-specific
policies.
Uh we also use our own custom-tuned vad
models to decide when a user has stopped
speaking, which gives us a lot more
control over turn-taking. Uh we've found
that this performs better for our use
cases, where real-world audio is often
messy and includes a lot of background
noise, uh accents, interruptions, people
changing course mid-sentence.
And then this uh harness also handles
tracing, like redaction of sensitive
information, PCI-compliant payment
flows, uh and a range of other
production features that help ensure

[00:23]
that agents stay accurate, safe, and on
brand. And it's this production layer
that takes us from a strong base model,
like real-time 2, to a system that is
controllable, observable, and safe
enough for some of the world's largest
companies to to trust with their
customers.
So, um you know, impact so far is that
you know, mainly what we're looking for
is faster relevant audio, more natural
conversations, stronger tool execution,
and higher end-to-end task success.
Uh in some of our initial testing, we
have definitely seen latency gains. So,
we've seen calls that are roughly 30%
faster at P50 and up to 200% faster at
P90 compared to our cascaded system. So,
it does really help with naturalness
overall. Uh voice quality has been
strong. It's been competitive with some
of the dedicated synthesis providers
that we use, you know, based on our
internal evaluations.
Uh and you know,
speed and voice quality are not enough.
Like in a traditional stack, uh we have

[00:24]
to evaluate transcription, the agent
harness, and synthesis separately. With
voice-to-voice, we have to evaluate the
full call, you know, listening,
reasoning, acting, speaking.
Uh so, do to do that, we also use
simulations that replay realistic
customer calls customized to each
customer's workflow, which lets us
measure whether the agent actually
completes the task, not whether it
sounds good. So, that's kind of the the
real bar for production voice, not just
an agent that sounds human, but one that
can be trusted to do the work. So, going
to hand it off to Soham, uh who will
talk about how Voisi and how Sierra
evaluates voice models end to end.
>> Hello. Uh yeah, I'm Soham, and I
represent the voice research team at
Sierra.
Um I know Erica said that voice is her
favorite modality, and Ken said that
voice is really unforgiving. So,
it's really fun that both of them are
true at the same time.
Um okay. So,
I guess the first thing about voice
agents is that
they don't get to pick their audio.
Um,

[00:25]
customer service calls are
sophisticated, they're nuanced, and
everything can said, and
calls very rarely look like the ideal
calls we want them to. Ideal calls are
like often text like where there's like
clear turn boundaries, and it's easy to
disambiguate what's being said,
information is like conveyed crisply,
and it's not lossy. And production calls
almost never look like this, right? Like
there's always
interruptions, there's accents,
and the question we really ask ourselves
is
can an agent, can a voice agent handle a
call from a customer who's like on the
side of a highway or in a car with kids,
or can it handle a customer who is
really impatient and aggressive
interrupter, and
all doing all of this while trying to
like make progress on the task that
they're trying to accomplish at the same
time, and this is hard.

[00:26]
Um, and this brings us to like common
failure modes that we see with agents
like this, and
um, if we can move to the next slide,
that would be great.
Yes. Um, so
there are different forms of failure
modes. I think we have found that some
agents can be really good at the
conversation part of things, whereas
some agents are more are better with
just getting things done and like tool
calls, and when you bring both of them
together, the error modes really
compound, and we see a lot of
performance degradation in these
situations.
Um, some really common forms of error
are like with spelling out names and
numbers.
This can be quite tricky in that if you
get like one letter wrong,
are you able to recover from this
gracefully? If you do, do you keep that
in your memory or like
like when you make a tool call later
with my name,

[00:27]
do you get the spelling right or do you
use the incorrect spelling from the
beginning? And we see that agents
sometimes get mired in their own
mistakes and are unable to like move on
from there.
Um
and at the same time, there's different
forms of errors where like they're more
logical in the sense of
um oh, you wanted to cancel a flight,
but the agent misunderstood which flight
this was and
this like airline is quite high stakes,
right? So, like you can be really stuck
[laughter] in like dire situations where
you're in a city or country you don't
want to be in and you're stranded
because your voice agent canceled the
wrong flight and we don't want this.
Um there's also
parts of conversation that are hard to
work with. Um
like I think we don't realize that, but
humans often
backchannel with like mhm's and ah-ha's
and yes, that's right.
And a lot of our voice models are
trained to respond to everything that we
say
and humans are much better with being
selective with this.

[00:28]
It can be hard to
be like, okay, that's that's a signal I
should ignore versus that's a signal I
should respond to.
Um yeah, and we have found cascaded
models to really shine in this situation
because we can really overfit to these
conditions and customers are complex and
we want the brands to like we want our
agents to represent the brands.
And
it's been really fun to see that
like voice-to-voice models are now able
to absorb that complexity
and really improve their reasoning and
their communication
and that's been really exciting. So,
yeah, this brings us to thinking models,
which is what we're talking about today.
So, thinking models have been a real
step change in
voice-to-voice models. Our leaderboard
at Dialpad has been dominated by
thinking models, and it's

[00:29]
not that easy to think in voice
conversations. You can't just have a
buffering loop while you're thinking.
Like you have to say, "Okay, like give
me a moment." or "Let me think about
that." and you have to be okay with
being interrupted in these situations
and maintaining state. And not like
Yeah, we should be able to carry forward
even if you're interrupted during these
situations. And
all of these issues sort of expect like
expect load multilingually, and it's
been really fun to see that um OpenAI
has made like some really big strides
here in real time too significantly
better. Um there's a high ceiling, but
we are really getting there. And for
someone who's been like waiting for
voice-to-voice models for a while,
>> [snorts]
>> it is very exciting to see
voice-to-voice in the mainstream.
Yeah.
That is me. Thank you.
>> Sierra, thank you for being such an
amazing team to work with. You're one of

[00:30]
my favorite like companies ever. So, uh
yeah, it's been great to just see you
guys continue.
Thanks.
>> Great. And we're going to move into Q&A.
If you just exit or escape and refresh
the deck, I dropped in some questions.
We got a lot of great questions um
through the chat. There were a lot of
questions about interruptions and how
those are handled. Um so, wanted to kick
it off. Sierra, you shared a little bit
about how you kind of layer your own
barge and detection on top of real time
too. There were a few questions if
people should rely on built-in turn
detection versus adding app side
interruption logic and kind of what the
best practice is there.
>> Yeah, I think it depends on your
specific use case. So, I mean, out of
the box real-time too does come with
their own bad models, like you were
talking about both semantic and server.
And we we're finding they were working
pretty well. Uh we just have our own

[00:31]
customized bad model that is very
specific to uh customer service call
audio. So, like having very heavy
background noise. Yeah.
Kids in the background, a TV in the
background, that kind of thing.
>> Any recommendations from you both?
>> Yeah, um there are different like
padding recommendations um that we have
um
but also just it really depends on the
situation of like where your device what
kind of device you're calling in, what
kind of like environment you're in. Um
it does require often like tuning and
optimization um just to see what is
actually working um for you. Um but is
there anything uh that you want to share
beyond the semantic
versus
>> I think like not even just on that
piece, but I one thing that I think
people don't necessarily know is that
you can disable it on a turn-by-turn
basis. So, if you have something you
need the model to say like a disclaimer,
you can actually disable uh you know,
VAD on that turn. So, the model will

[00:32]
definitely say that, it won't be
interrupted, and then you can enable it
going forward. And so, I think that's
kind of a cool uh thing cuz it's not
just relying on like instruction
following, it's like actually preventing
the user from interrupting.
>> Yeah.
>> Which I think is kind of a cool feature.
Yeah.
>> That is cool.
>> The next question is also just like such
a tee up for the Sierra team. And a
question that we get all the time as
builders are starting to explore uh
real-time models and bring more voice
modalities into their products. What
actually separates a useful AI assistant
from an AI system that can actually
improve real-world business workflows? I
think reading between the lines of this
like for real time specifically,
um as the models are starting to become
more capable, um especially in like
those real world interactions.
>> Yeah, maybe I'll go first and then I can
pass it to the Sierra team.
Uh so, we're seeing a lot of um great
use cases in these like fast capture
fast intent um where it is easier to
drive things with voice and more

[00:33]
convenient than it necessarily is with
text. Um so, there's trade-offs when
you're building with either uh with text
obviously there's um more information
density um but with voice you can use it
when there you're driving, you can use
it on the go on mobile, you can use it
if you just have a generalized idea of
what you want but the model can
interpret it into something that's like
more um of a like coherent prompt. Um
so, different use cases we're seeing for
sure. Um I think in particular like
there's
uh like also
a younger uh demographics can like use
voice more than text in some cases. So,
um
definitely a lot of different use cases
but Sierra, I'll pass it to you.
>> Yeah, I think on the customer service
front um with our voice we try to like
bake in many things that we see in
production traffic with like
interruptions and noise and accents um
but
like it is a benchmark so it is it's not
production traffic and there are many

[00:34]
more complexities that go into that and
I think Ken is like much more familiar
with this.
>> Yeah, for production agents at least
with Sierra a lot of it goes into how do
you orchestrate the entire call. So, I
think real time is great at responding
within a turn and figuring out what to
do
but a lot of what goes into the Sierra
side is how do you define the different
workflows that an agent like can need to
work through. So, like we we work
directly with individual customers to
figure out you know, what does your
refund policy look like and then how do
we expose the right context to uh time
to at the right time.
>> I think fundamentally
the biggest difference between voice and
text is that you can speak like four
times faster than you can type. So, that
alone I think unlocks a lot of use cases
and to your point a lot of people feel
comfortable like stream of consciousness
speaking about maybe like a house that
they want to buy or a car. So, you can
think about it as a more intimate kind

[00:35]
of casual way for somebody to even
interact with an application and provide
more context than they might if they had
to actually type it out.
>> And since we are like doing a kind of
global live stream here, like there are
countries that are very voice first.
So, Brazil, India can be some of these
countries that might prefer to interact
with your app via voice.
So, just different considerations.
>> It's cool walking around our offices too
and hearing people talking to their
computers increasingly and even as we
were preparing for this, our production
team was sharing that they're using
Codex through the real time model so
that they're actually like talking to
Codex through their headset which is
just so cool. It's neat to see how we're
like drinking our own champagne with
these real time models internally.
All right,
we got some questions on like what if
audio sessions are more than one hour of
calls? What approaches should we try?
>> Yeah, I'm just going to answer.

[00:36]
I'm just impressed that you're able to
get the question out
and answer so quickly.
Um
Yeah, so I think there's different ways
that you could set it up. I mean, if you
could have multiple sessions
running at once, you could also stage
them such that you have different
sessions
like chained after one another.
Um
>> I think like the biggest thing and this
isn't not even just like oh my session's
more than an hour, but you might have
somebody call back or maybe you have
like a call drop for example, user hangs
up accidentally.
Actually saving that state of what's
been happening so you can rehydrate the
next session is probably the most
important thing. So if you are going
over an hour, like start a new session
and then hydrate that with all the
context from the previous hour and
because we have that extend extended
window now to 128,000 tokens, you can
provide way more context in that
session. So that's probably what I would
recommend is just like you're going to

[00:37]
have to start a new session and make
sure that you've saved all that state
from the first hour.
>> And when do you escalate to GPT-55
via an advisory pattern?
>> Based on your evals, I think this year
our team could probably talk about that.
In our old real-time models, we kind of
recommended that for basically anything
with reasoning because they just
fundamentally didn't have that
intelligence. So let the real-time model
handle this kind of maybe small easier
to handle set of tools and then escalate
out to a frontier model for anything
else, but it's always going to be based
on your evals. So you maybe maybe I'll
pass it to the Sierra team to talk about
how you think about evaluating the model
for handling certain kinds of
complexity.
>> Yeah, I think
um
like I'm assuming by advisory pattern
you mean like something like okay, in
this case maybe we more solid reasoning
or something and

[00:38]
I think for a while we thought about
and so I'm on the research side, maybe
Ken you can talk about what we do in
production, but on the like on the
research side for a while we thought
about okay, maybe let's sort of
put this conversation on hold for a
second and think about this using a text
model and get back to us, but I think
with real-time too and thinking models,
it's been real cool to see this the
model does it itself. The model says
that, you know, give me a minute. It
thinks about it and then it comes back
to you with an answer.
Um
and
what do we do?
>> Yeah, we we have two approaches on the
production side. Uh one, we have
supervisors within an agent that
asynchronously is reviewing the
conversation as it goes and deciding,
you know, like do we need to inject
additional information into the context
to kind of get it back on the rails.
Um the second approach honestly is that
like we support both real-time two and
just having everything go through
GPT-54.

[00:39]
Um
so depending on the complexity of the
agent, we'll
sometimes use real-time two if it's
something that we want to be really
fast. And for more complex agents, we'll
we'll stick with traditional uh
text-based models.
>> Yeah, love that. And I think you can
always inject context at any time
without even triggering a model response
with conversation item create. So, to
that point, you can have a background
uh you know, tool call running and the
model can keep talking. It's totally
fine with these kind of asynchronous
tool calls happening. So, then when that
background longer running process
happens, you can then just inject, you
know, whatever tool call results you had
back in so that the real-time model has
that and actually can create a response.
>> Yeah, I think in general, we do a lot of
orchestration and context management.
>> Yeah.
Especially important when you were
dealing with a smaller context window,
but even here this window is smaller
than frontier models. So, definitely
super important.

[00:40]
That's a great segue into our last
question that we'll answer live, which
is how do you real-time agents maintain
that context and decision consistency
while interacting with multiple tools?
>> Um I think one of the resources that we
have,
uh, on our blog is about perplexity
using, uh, context management to kind of
get to this production state.
Um,
yeah, we definitely recommend, like
reading that, but there's a lot of,
like, truncation optimization on the and
when they had the real-time 1.5 set up.
Now with real-time 2 and the larger
context window, there's a lot more
possible, for sure.
>> Yeah, absolutely. I think just I want to
call out, like, this is a reasoning
model. So, if you're familiar with
reasoning models from, you know, just
like our normal main line models, like,
this model has chain of thought. This
model, operates a little differently in
that it kind of has like this idea of
preambles, but you it's going to provide
you, kind of, it's reasoning the same

[00:41]
way our frontier models are. So, it's
not losing context as it's making those
parallel tool calls, it's just calling
tools like our any of our other frontier
models. So, I think it's actually
bringing it up to par with what you your
experience would be of our existing
models as opposed to like some other
kind of context or decision consistency.
I The only call it, I guess, I would
have is that you don't have to maintain
the state turn over turn. You can
dynamically, you know, context engineer
it, but we will, by default, pass all of
that turn to turn, so that, you know,
we're kind of automatically maintaining
that state and context.
>> Yeah, absolutely. And yeah, the thing I
want to stress with this model is how
good it is at the instruction following
piece. So, if, uh, you have any
conflicting instructions in your prompt,
um, it will, uh,
you know, try to do both. And so, one
thing we found really helpful is just
to, um, basically ask models themselves,
like, what is there any,
kind of, conflicting advice or,
um, better ways to optimize this prompt?
And it's pretty good at, like, giving

[00:42]
you that, uh, more optimized version of
it.
>> Great. So, um, Ken, thank you so much
for joining us. Um, we got some really
great questions and we've been answering
them in the chat. We're going to send
out some resources after this, the blog
that Terry mentioned where you can
actually see some of those use cases,
best practices, docs, playground, and as
always the Build Hour repo where we will
share um some code snippets with you to
start playing around with.
So, our next Build Hour is going to be
on May 28th. It's going to be on the
Agents SDK which we also recently
launched. And as always, you can find
all of our upcoming Build Hours at the
link below as well as the recorded
sessions on YouTube. So, thank you for
joining us today. You will get a survey
after this just asking for any feedback
on topics that you want to learn more
about. We really try to base these
sessions on what's interesting, what
would be most impactful for you to build
with. So, let us know what you want us
to cover next. Thanks for tuning in.

</details>
