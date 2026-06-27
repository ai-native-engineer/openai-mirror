---
title: "OpenAI DevDay 2024 | Community Spotlight | Parloa"
channel: openai
url: https://www.youtube.com/watch?v=xZc0YQbIyWE
youtube_id: xZc0YQbIyWE
published: 2024-12-17
duration: "14:58"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Parloa

[![OpenAI DevDay 2024 | Community Spotlight | Parloa](https://img.youtube.com/vi/xZc0YQbIyWE/hqdefault.jpg)](https://www.youtube.com/watch?v=xZc0YQbIyWE)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Parloa (14:58)</summary>

[00:00]
So, my name is Mike with AI and I work
for a company called Palwa. We are doing
contact center automation and just
imagine you're calling into a telephone
hotline how it sounds nowadays. It's
usually press one for insurance, press
two for contract
and that's not a great experience,
right? So, today I want to talk about
how the contact center industry is uh
being transformed, how it's being shaped
in the near-term future by using open AI
technology, especially GPT-4 with
multi-agent crews and the human in the
loop integration to make sure we can use
it safely.
We at Palwa, we believe that every
customer interaction should be as easy
as talking to a friend. So, just imagine
you're calling in, you want to have it
natural, you want it to be trustable,
you want it to be safe. And this is what
we call a personal AI agent. So, every
conversation is unique. It's not just

[00:01]
deflecting the calls, it's actually
making sure that we resolve the issues.
If you look in nowadays world, we do
have contact centers all around the
globe, all around the world. There are
human agents and customer care
representatives that is being called
working on different levels. These are
all human agents who work day in, day
out in a call center and that's actually
not an easy job. I've been visiting call
centers in Malaga, in Cairo, talking to
the agents there. It's a really hard job
to do. If we look into the future, we
want to support that kind of work by
introducing
AI agents to the workforce of human
agents that are working in contact
centers. And this does not mean that we
are replacing human agents doing that
job. We will complement it because you
saw it in the demo from Romain. He was
ordering pies, but it wasn't him who was
doing the call. He instructed his
assistant to do it on his behalf. Now
imagine your personal assistant that you
have in your pocket, your Siri, your
Alexa. They all doing phone calls, not

[00:02]
only to one place, but maybe negotiating
a pie price with 10 different vendors.
Who's picking up the call on the other
side?
It can be human agents. It won't be
possible. We cannot cover the whole
market. We won't be able to manage that
inflow of call volume and this is where
AI agents can be a solution to also be
able to pick up these calls on the other
side.
The challenge that comes with it is we
do have actual customer interactions.
We're talking to our customers and we
care about our customers. So, we need to
come up with new solutions in how to put
this technology safely and responsible
into production. And this is where the
AI agent life cycle comes into play.
It's not just about building a hello
world example or putting it into
production without caring about the
performance. It's actually making sure
the whole life cycle is supported. And
this is where we earlier this year in
September launched our AI agent
management platform which we were
working on for 1 and 1/2 years. It was
quite tricky not to talk about it. So,

[00:03]
we needed to keep our mouth shut and we
then launched it in September and
finally we are able to talk about it. We
try to cover all the parts that you need
to have to properly put it into
production. This comes with design and
integration. Design and integration
means I'm building an AI agent. I prompt
it with natural language briefing and I
also integrate it to third-party tools
because I need to interact with the
outside world, fetching information and
putting data back to the systems where
they belong to. And making sure that we
test it properly. Testing changed. So,
we were coming from an IVR world. This
is like intent classification, natural
language processing. We are trying to
take a word, put it into an intent and
then try to navigate along the path,
very fixed, very easy to test a happy
path. But now we are dealing with a
world that is non-deterministic. So, we
need to change the approach and the
approach that we are choosing is
simulation and evaluation, making sure
that we can actually test it. And the
first two parts will be the key focus of
the session today, but for sure we also
need to make sure that we deploy and

[00:04]
scale it. Why? In contact centers and in
customer service, we usually see large
spikes of call volume. So, one day you
could have thousands of calls more than
on the other day and you need to make
sure that using large language models
can deal with the amount of calls that
are coming in. And on the other side, we
want to derive KPIs and data,
quantifiable data of what's working, how
many people are calling in. And this is
the last step, monitor and improve and
then the whole process starts again in
order to make sure we increase the
autonomy rate of the AI agents that we
are using.
Coming to the first part, the design and
integrate part. This is how it looks
like when we are building this this AI
agent. It's a natural language briefing.
You can compare it to the way
how a human agent starts their job when
they are on the first day. Like they are
being told, "What company are you
working for? What products do you
support? How do you handle the cases
when somebody is calling in?" And you're
prompting that with natural language.
So, the whole way on how we build these

[00:05]
kind of experiences changes as well. We
are using natural language. We are no
longer programming. It becomes much
easier also for subject matter experts
to actually
work on AI agents. The thing is
it's hard.
You all know prompt engineering is a
science for itself and it won't become
easier in the near-term future. So, at
Palwa, we set out to support especially
the initial stage of getting from zero
to one when you are having a use case
that you want to support. And this is
where a multi-agent prompt engineering
crew comes into play
where we are trying to support our
conversational designers. How it works
is we are replicating the roles that we
usually have in our teams
and are trying to do the whole process
with autonomous GPT-4 based agents. So,
we have vice president customer success
with a lot of experience making sure to
navigate the different work streams and
we have two people collaborating, the
solution engineer which is focused on

[00:06]
the integration part, how do I get
systems connected and a CX designer who
is focused on how to make the best
conversational strategy overall. This
crew is working collaboratively and the
manager make sure that it meets the
goals that we set out with best
practices, with prompt examples and all
the best practices that we see in the
field that we always incorporate back
and in the end we are generating a JSON
configuration that is being used by our
M Studio. The thing is this is a
recursive loop in itself. So, the the
agent designer at the conversational
designer also needs to potentially
instruct back about improvements, about
things that have been missed out or
about a use case that we didn't
that we didn't consider in the
beginning. And then in the end, if we
are happy with the first draft, with the
first design our crew came up with, we
need to simulate and evaluate it. To go
a bit into technical details, our
configuration structure is a bit
different to the traditional prompt that
you are seeing when you are plainly
prompting. Why? We need to support
specific parts for telephony. Classical

[00:07]
use cases for example handovers,
telephony handovers where we want to
handover to human agents for specific
use cases and this is where a SIP tool
for example comes into play. We are also
structuring the prompt between the
persona,
the different kind of
descriptions that we need to pass for
the parameters where we want to pass
meter information to third-party tools
and all of that needs to be considered.
So, it's much more complex than just
the normal text your prompt. And then we
have the roles, the role descriptions
where we opted for the YAML way of
describing it to make sure that also our
solution engineers themselves can easily
collaborate. All of this is based on the
crew AI framework. Crew AI primarily
because of the usability and the
developer experience so that we can loop
in more people from CX or from our own
solution engineering to
help with that process. And now we end
up with a prompt. The challenge is how
do we know that a briefing that we
generated and a briefing that we came up
with actually does what it is supposed

[00:08]
to do. This is where simulation and
evaluation comes into play where we need
to test the reliability of the prompt.
So, we have the conversational designer,
we have a configured AI agent
configuration and on the other side we
have actual customer conversations. So,
we are working with call centers
together. So, we have sample data from
actual use cases in the field and we are
taking these to derive customer persona.
So, just imagine we have an angry caller
you have a child that is calling in, an
elderly person. It's completely
different personas that are calling in
and we need to make sure that we
simulate all the different variants in
order to make sure that our AI agent is
simulated with the different customers
and can handle these cases according to
the briefing that we provided in the
agent configuration. All of these
conversations are being evaluated with
contact center specific evaluation
criteria and in the end this generates
insights for the conversational designer
to make sure that we improve over time

[00:09]
the whole configuration and we make sure
we are compliant with the goals that
have been set out
by the company. This is how it looks
like in the UI. So, we have a we
abstracted all the complexity away for
our customers themselves.
They have an easy way to run
simulations, to configure the personas
that they want to test, how many
iterations you want to do, how many
simulations you want to run. So, you can
think about it like running thousands
and thousands of conversations so that
we can properly quantify the reliability
of the large language model and make
sure that it's safe to use also for
production use cases. And the evaluation
criteria in itself is a mixture of the
technical accuracy. It's essentially
like an end-to-end integration test like
we know it from software engineering
where we can also test for API errors
because sometimes it's not even the AI
agent who is at fault. Sometimes it's
the API from the customer who is sending
a bad response or or that is not
reacting properly. And on the other
side, we have the language behavior

[00:10]
itself. How do we handle the
conversation? Do we properly act, for
example, with the corporate wording? Do
we recommend a competitor if you're
asking specifically all of the things
that we need to have for compliance? We
can make sure that we either pass or
fail that criteria.
The thing is, in real life,
not every customer interaction can be
handled autonomously. This is is This is
how it is nowadays. So, we need to come
up with a solution and how we handle
conversations that cannot be fully
automated. Um and at Palovera, we build
a solution for that where we incorporate
the concept of an AI agent with a human
agent. How that works is, we hand over
that call to a human agent, but the
customer and the human agent, they don't
hear each other. The human agent sees
this interface you're seeing right now.
The whole conversation is being
transcribed in real time, and
the AI agent proposes proper responses
to the human agent. You saw these little
blue buttons? The human agent can just
select a proposed response. If the human

[00:11]
agent is not happy with the proposed
response,
they can just still speak to the phone,
and everything the human agent says is
also being transcribed and then put back
into the ChatML context that we use for
the AI agent. So, the human can chime
in, control the conversation if need be,
and the AI agent will adopt that kind of
guidance or how the conversation flows
in the next turn and propose, for
example, a better suggestion next time.
Um this way, the agent is um supported
in their job, um and the good side
effect that we have by making sure that
the human agent and the consumer, they
are not connecting directly to each
other, we can even bridge the language
barrier at the same time. So, this is
completely language agnostic. So, a
Swedish caller can call in and a German
human agent can support them, and we can
make sure that we use large language
model to accelerate the whole process
and still make sure that the latency is
as low as possible. And this is also
super interesting for customers who are

[00:12]
a bit
objective against generative AI usage or
who have concerns. This way, we can make
sure it's safe to use and it's always
being supervised by human agents who
have the experience on how to handle
these kind of cases.
Why is this important? Um if you look
into the past, um this is how the world
looked like. We have a lot of IVR
systems, press number one, press number
two, and a lot of human agents, junior
agents, senior agents working on the
different levels.
Um with the emerge of AI, we are
entering we entered the AI transition
phase where we came up with rule-based
AI agents, mostly based on natural
language processing, intent
classification in parts, but we still
had a lot of IVR and junior agents and
senior agents who have to handle that.
Right now, we are entering an era where
we have autonomous AI agents um who are
taking over more and more jobs, who can
complement for now the rule-based
systems and who will make sure that we
are slowly but steadily getting rid of

[00:13]
the IVR solutions with the bad customer
journey in itself. If you look into the
future, we will enter an era where it's
called the AI first contact center. And
um funnily enough, it was in one of the
podcasts where Sam Altman was uh talking
to Lex Fridman, and he estimated round
about a year ago that potentially
contact centers might be one of the
first industries being completely
disrupted.
He was right. Um this is currently
happening. So, we are rolling out that
solution with call centers and contact
centers around the world. And if you
look into the future, when we have more
capable models, more autonomy, um and
more ways to connect to third-party
system, more instruction following, um
we will have autonomous agents dealing
with the cases where the customers are
calling in and fully autonomously
resolving them end to end, even
integrating to the systems and
automating the whole process. The
important part is, we still will have
human agents. And the difference to how
they work nowadays and how they work in

[00:14]
the future is they will be promoted,
essentially, to become senior agents and
AI coaches or supervisors. So, the
future that we envision is that contact
centers of the future will
help AI agents to do a good job, and the
human agents will become the supervisors
for all of these AI agents.
That's the future that we envision, and
um at Palovera, we believe that the
leaders of this era, the companies who
try to do good contact uh and customer
service,
um they will provide a personal AI agent
for every customer. Um and um my last
take for that round here, let's prove to
the world that uh large language models
can have a good benefit um to society,
to humanity, and also consider
um the organizational changes that are
about to happen in the past and help
everyone adopt to it. Um thank you for
taking the time.
Thank you.
[Applause]

</details>
