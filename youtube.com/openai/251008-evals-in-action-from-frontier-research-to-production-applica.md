---
title: "Evals in Action: From Frontier Research to Production Applications"
channel: openai
url: https://www.youtube.com/watch?v=YEaKXjHENyQ
youtube_id: YEaKXjHENyQ
published: 2025-10-08
duration: "21:37"
captions: en-orig
---

# Evals in Action: From Frontier Research to Production Applications

[![Evals in Action: From Frontier Research to Production Applications](https://img.youtube.com/vi/YEaKXjHENyQ/hqdefault.jpg)](https://www.youtube.com/watch?v=YEaKXjHENyQ)

<details>
<summary>자막: Evals in Action: From Frontier Research to Production Applications (21:37)</summary>

[00:00]
Hi everyone.
I'm Tel. I'm a researcher on the
reinforcement learning team here at
OpenAI and I lead our Frontier Evals
efforts. And soon I'll be joined by
Henry who leads our EVALS product. We'll
be doing a Q&A at the end. So please
drop your questions in the Discord and
thanks so much for coming.
So here at OpenAI, we're training some
of the most powerful AI models in the
world. And to understand what these
models can do, we need to evaluate them.
Evals measure the capabilities of our
models so we can steer model training
towards good outcomes. So we're very
excited to share with you today first
how we evaluate frontier capability
progress here at OpenAI and second how
you can have practical tools to run your
own evaluations on your applications and
agents.
So why does evaluation matter? At
OpenAI, training runs are very expensive

[00:01]
in terms of compute and researcher time.
So we need signal to measure progress so
we know how the run is doing and we can
intervene and steer training
appropriately.
Historically we use classic academic
benchmarks like the SAT or the LSAT or
the AE which is a high school math
competition to push forward reasoning
capabilities. But these eval can only
measure so much. For example, when we
were starting to train 03, we didn't
know if we were making progress because
we'd already gotten so close to 100% on
all of these benchmarks. And yet, our
models weren't yet able to do real world
work. So, it was clear we needed a new
way to measure progress.
You can think of these classic
benchmarks like you'd think of hiring a
straight A student out of high school.
Sure, they're great at studying and
passing tests, but they're untested in
terms of work in the real world. And we
all know that can be a tough transition.
This is me in my first internship being
so behind at my work that I was coding
at the team drinks and my team made a
lot of fun of me for that.

[00:02]
So that's why we're transitioning from
tests to measuring work like a drop in
co-orker would actually do to understand
how models can support people in their
everyday work. To do this, we built GDP
val which is named GDP val because it
covers tasks relevant to GDP or gross
domestic product and it measures how our
models can do on economically valuable
real world tasks. It's available on the
OpenAI website as well as hugging face.
So when we launched GDP val in
September, it really took off. A lot of
people in the community were talking
about it and using it. But to understand
why, I'd love to show you a few examples
of what this eval is actually actually
measuring. All the tasks on GDP val were
made by experts with an average of 14
years of experience in their fields.
They're the best of the best. And we
wanted to measure how models can stack
up against these experts on real world
work. So here's an example. We have a
real estate agent that's taken some
pictures of a property they want to show
and they've done some research on that
property and then they want to make a
brochure to show that off. And we're
interested in how can our models do

[00:03]
compared to this agent. And you'll
notice that the tasks in GDP val are
very long horizon. They often take days
or even weeks to complete. And they're
very multimodal. So often involve a lot
of computer use, images, and tools.
Here's another example. Uh a
manufacturing engineer is creating a 3D
model of a cable reel stand. Again, very
multimodal. It involves an actual piece
of real world work someone had to do.
And final example, you have a film and
video editor that's creating a high
energy intro reel with audio and video.
So those are just a few examples. Uh we
actually cover a lot more. We started
with the top nine sectors that
contribute to US GDP as per the Federal
Reserve. So every industry that we
include here contributes over 5% to US
GDP. And then within each sector, we
selected the top five knowledgework
occupations that contribute the most to
overall wages as per the Bureau of Labor
Statistics. And then finally, within
each occupation, the government actually
tracks what what are the main tasks that
someone does in that job. So for
example, if you're an accountant, you

[00:04]
might be looking up external
information. You might be creating a
budget. You might talk to a client. And
for every occupation, we cover the
majority of work tasks in that
occupation.
So overall this yields over a thousand
real world tasks covering real estate,
CAD design, retail, really trying to
understand how models can do real world
work.
So those are some examples of the tasks
we test. The natural question is how
good are we at these? So first let me
explain how we grade our models. So we
use pairwise expert grading where we
compare a model's output to a human
expert's deliverable and then the
graders in the field are blinded so they
don't know which is which and they
select the one they prefer and we roll
these judgments into an overall win rate
which is the percent of times the
model's output is preferred and this
gives us a clear and unbiased
measurement of capability on real world
work that we can track over time. So
here's my favorite plot. So the y-axis
we have the win rate versus an industry
professional. And back in spring 2024, I
helped work on the GBT40 model, which at

[00:05]
the time we thought was like the
frontier best model we had ever
released. But actually on GDP val, it
scores less than 20% on win rate. So the
vast majority of times an expert would
not want to use GPT40 instead of just
having them do the work directly.
But already over the last 18 months with
GBT5, we're getting close to 40% win
rate on these tasks. Which means that in
half the times nearly experts would
prefer the model's output or think it's
just as good compared to something a
human could do. And if this trajectory
continues, you might just imagine where
would we be in a year or two? Maybe
we'll be actually at par. And in fact,
there's already some models in the
industry like Claude here that's already
getting really close. So these models
are going to be able to do the kinds of
applications you guys care about quite
quickly.
I'd love to do a little explainer. Um,
this is a very simplified task where we
have a nurse practitioner that's making
a deck to explain hypertension. And I'd
love to see how you all do in guessing
which one is the model versus the human.
Okay. So, raise your hand if you think
the example on the left is the human
expert.

[00:06]
Couple hands maybe like 10% of hands.
Raise your hand if you think the right
one is the expert.
So, if you turn if you like the left,
turns out that one's the model. the
right is actually the expert, but you
might notice they're pretty similar.
Like, you can't really tell the
difference. They both kind of get the
job done. And if you look into the time
and cost of getting this kind of output,
the models are significantly faster and
cheaper than humans. Where you see in
our paper, we have some more detail that
if you have a model in the loop when
completing these tasks, you can save a
lot of time and money compared to doing
the task unaided.
So, why did we build GDP? The first
reason is that understanding how AI can
impact labor is a very commonly asked
question. And the current methods used
by economists often involve looking at
usage data. So how are people using
these models in production? But the
problem with this is that it's very much
a lagging indicator. And for most large
technological shifts, it can take years
or decades for actual usage to show
through in GDP. So for example,
airplanes, electricity, the internet,

[00:07]
you know, the time from inventing an
airplane to most people using it to get
around for work took decades. And we
suspect AI will be the same due to, you
know, regulatory reasons, cultural
reasons, procedural reasons. And so
evaluations help us proactively track
and communicate how our models are doing
on real world work. And then also
internally on our research teams, we're
using this as a northstar to guide and
track model progress. So if you're
interested in this evaluation, you can
evaluate your own models at
eval.openai.com.
We've also open sourced the evalat on
hugging face um where it's already
reached number one and you can use any
of the data sets there. And then
finally, we provide a public grader
service so that you can iterate on your
own results.
So I'd like to caveat a lot of
limitations. I saw some discussion on
Twitter that was like OpenAI automated
all jobs. That is like not what this
eval is saying. It's measuring how
models can do on a set of wellsp
specified tasks that have a clear input
and output. And as you might imagine in
real work, there's like a lot more than
that. You know, you have to figure out
what even to work on. You have to
prioritize tasks. Your manager might
give you feedback and you might iterate.
And so we're working on making future

[00:08]
versions of GDP val that incorporate
this. But in the meantime, we're really
excited about GDP val making a lot more
progress than these academic tests to
understand how our models do on the same
kinds of tasks that many of you are
building for.
So that's how we evaluate Frontier
models at OpenAI as we build them
internally. But if you're building on
the OpenAI API, you might also want a
way to evaluate your models with the
same rigor for your own custom use
cases. And that's why Henry from Product
is here to show you how.
[Applause]
Thanks.
Teams that invest in evals, they build
consistently better products. And we see
this pretty much every day here at
OpenAI. Not just when building our
frontier models, but also from our work
with the some of the world's largest
enterprises, some of the world's most
sophisticated startups. We work with
these companies to help them deploy AI
to production every day. And from that
work, we've seen how critical eval are

[00:09]
and how crucial they are to get right.
I'm going to share today what we've
learned from this work and how we're
making those lessons available to
everyone through our product.
So why do evals matter for builders,
people who are building agents,
applications, not only people who are
making frontier models such as OpenAI?
It's because building high performing AI
applications, it's still really
challenging, right? It's not easy. LLMs,
they're infuriatingly nondeterministic.
New models keep dropping. With chat, the
edge cases are pretty much endless. It
gets even harder when you're building an
agent and error rates compound with
every call. Then you combine this with
user expectations. They're super high
and they're only getting higher over
time.
And errors, they can be really costly.
People are building agents in regul
regulated domains now. Think finance,
legal, health. Wanting to get these use
cases right is crucial. User
expectations through the roof and you
have no tolerance for failure.

[00:10]
So I think we can agree evaluation.
But today they're really hard to get
right. You have to spend what seems like
forever compiling representative data
sets of inputs. You have to create and
align graders that really capture your
business preferences. And it's so time
consuming some people just skip it all
together and ship straight to production
based on vibes.
We're working hard to improve this here
at OpenAI.
We have an eval product and today we've
shipped a whole bunch of new features
for it. This product, it aims to make
defining and running evals much easier
and increasingly automated. Today, we've
introduced a host of new functionality
to make it easy to build evals, to run
evals, and especially to run evals for
agents. First up, data sets. This is our
visual eval builder. Makes it easier

[00:11]
than ever to get started building your
first eval as well as the complete human
annotations in one easy surface.
Next up, traces. Traces are an
incredibly powerful tool when you're
building an agent or a multi- aent
system, but they're hard to interpret at
scale to find those faults when you've
completed many runs. Trace grading
allows you to run graders over those
completed traces, identify those
problems, and direct your debugging
efforts directly to those failing traces
and those problematic spans.
And then what do you do once you've
completed an eval run? you have a ton of
relevant information from a prompt, a
bunch of greater outputs, and
potentially human annotations, too.
Well, today you have to read through all
of that data, find patterns, maybe do
some prompt engineering. But a better
way is automated prompt optimization.
This is where we take all of those
inputs, the annotations, the greater
outputs, the original prompt, and we
rewrite that automatically to massively
accelerate your iteration time.
Next up, a really common request that

[00:12]
we've had throughout the lifespan of our
product, third party model support. So
when you're using our eval framework,
thank you. When you're using our evas
framework, you're not exclusively tied
to OpenAI models anymore. You can
evaluate across the ecosystem. And this
has been implemented by a partnership
with Open Router and bring your own key,
so you can support any custom endpoint.
And finally, our product's enterprise
ready. We're available to organizations
with zero data retention enabled and we
support enterprise key management as
well.
So that's enough talking. Let's get into
a demo. I want to talk you through an
example that Carlilele the leading
global investment fund built using agent
kit. This is a use case that is much
simplified but for for reasons that I
will not go into I wanted to make
something that was like simple and
easily visualizable. So the goal of this
is to take a company, provide analysis
from various perspectives, criticize
those perspectives, and then come up
with a final report that a professional
investor can use to inform their

[00:13]
workflows. So here you can see the
visual agent builder that was demoed on
stage earlier. You can see we take an
input, pass it through various agents,
and then write a report that gets
returned to the user. Now, building a
multi- aent system is complex and
challenging. Your agent is only as good
as the weakest link as any one of these
specific components. So initially you
want to evaluate each component. So if I
click on one of these nodes, I can see
an agent. This is a fundamental analyst
that is going to conduct financial
analysis into a provided company. Now we
could just run with this node, but a
better way would be to build a simple
eval for it. So if I click evaluate,
this is going to open that agent that
had been defined in the visual agent
builder and it's going to open that in
our new data sets product. It makes it
easier than ever to create that eval. So
here you can see the model that we had
used. We can see the variables and the
tool call has been passed through. We
can see the initial prompt and then we
can upload just a set of sample data

[00:14]
just really basic couple of rows.
So this is now a basic data set that we
can use to test this application with.
You can see I've got a couple of
companies that I feed into this prompt
and I've got a couple of columns here of
ground truth values so that we can make
sure that web search tool is pulling in
the correct context from around the web.
So this is going to run through and
complete generations here. And as those
generations are completing, we can click
in, we can read what the actual
generation has been, and we can do a
couple of things. First up, we can add
annotation columns. So this is a really
powerful tool to conduct manual subjana
expert annotations. So here, let me add
a rating column and then let me
additionally add a free text feedback
column so that I can attach those kind
of free text annotations to. So what I
can first do is I can read through
these. I could find some challenges. I
could rate, you know, maybe that one's
good, maybe that one's bad. I can add
free text feedback. You know, maybe this

[00:15]
is too long. I could also use this to
rewrite that generation and create a
golden response.
So subject runner expert annotations
super powerful technique when running
evals and really it's crucial to lean
into them but they're very expensive and
don't scale well. So a better solution
is to also use graders. So here we're
going to just create our first LLM
judge, a simple grader that's going to
run over those generations. And in this
example, I'm going to ask the judge to
just evaluate a financial analysis and
ensure that we see upside and downside
arguments, comparison against
competitors, and a clear buy, sell, hold
rating. I'm additionally going to ensure
that the quarterly revenue and income
figures that I pulled in are consistent
with those ground truth values that we
have in that reference data set. So now
I can save that grader and that's going
to take these generations, pass them
into that LLM judge, and then create a
response, which I'll be able to see
here. Now, running grading can take a
minute while the inference completes,
but like a good TV chef, I've got an

[00:16]
example of one that I made earlier. So,
here we can see this grader that's
completed and we can read through this
rubric and understand why a failure
might have occurred. And here, for
example, we can see that the response
does not compare the given company
against any of its peers. And there's a
couple of other failures, too. So, what
could we do here? There's a couple of
things. First, you could read through
all of those failures and then do some
manual prompt iteration and try and
iterate on that manually. A better way
is to optimize this prompt
automatically. So, I've clicked this
optimize button down here and a new tab
has opened up where it's rewriting the
prompt with an agent. This is going to
take that data, those annotations, the
greater outputs, and suggest an improved
prompt. Now, again, this is going to
take some time to come through. So,
we're going to click ahead to one that I
made earlier. And here we can see a diff
view. That original prompt which we were
using pretty simple couple of lines
didn't actually capture all of the

[00:17]
criteria that I wanted the the
generation to consider. And here we can
see this automatically rewritten prompt
which is significantly more thorough and
aligned with the preferences that I have
uh kind of encapsulated in that manual
annotation.
So that was that first step. That's how
I took that multi- aent system took a
single node and evaluated it. You also
want to look at the end to end. You want
to make sure that this whole system is
working as intended. To do that, traces
are a great tool. So here we can see a
set of traces that have been created
from this agent. We can then attach
graders. In fact, I'm just going to
delete these ones I made earlier. So we
can then attach graders and say as we've
been scrolling through these traces, we
find some problems. And let's say we
want to make sure that cited sources are
authoritative first party sources and
not news aggregators.
Let's say we scrolled further and we got
to the end of the we got to the end of
the generation and we found another
problem that the final output needs to
have a clear buy, sell rating. So the

[00:18]
workflow here is to build up a rubric, a
set of tests that you want to run over
these traces at scale. You create them
here as you're tabbing through many of
these traces. You can scope however many
you want to uh kind of test. And then
once you built that rubric up, you can
click to grade all and this will run
those graders over many traces at scale
so you can find the problematic examples
to dive into.
So that was a real quick overview of how
you can take actually let me just show
you what that looks like when it's run.
So obviously it takes a bit of time to
run one of these evals uh because a
trace is very large. So here you can see
this is coming through and you've got
the graders. But once that completes,
I'll go again to one that I made earlier
and you get a view like this where you
can see those greater outputs at scale.
And I can click through any one of these
traces and understand where there's been
problems so that I can accelerate that
trace review process rather than reading
through dozens of them at any one time.
So that was a real quick overview of how
Carlile can build an agent using our

[00:19]
agent builder but then crucially
evaluate a single node and then the
whole multi-agent system end to end
which allows you to be confident in the
performance which is obviously so
crucial if you're in a performance
sensitive domain.
So when you're deciding how to run evals
and what tooling to use, there's a
couple of things that we think are
really worth considering. The first is
integration with a kind of a a
horizontal set of tools that contain
everything you need in one place. We're
building that in the agent kit from the
product. This provides tight integration
from building an agent in the builder as
well as the agents SDK. Easy deployment
tools and now easy optimization tools so
you can complete that iteration loop all
in one place.
Next up, automation. I showed you today
how prompts optimization can accelerate
that journey of building a high
performing agent. We want to go further
and allow you to generate and align
graders and generate data sets based on
representative user inputs. So keep your
eyes peeled for those coming soon. And

[00:20]
then finally, we're really trying to
lean into ease of use, making it
straightforward to get your subject
matter experts in a tool capturing their
expert preference data in one place and
reducing the barrier of entry to running
evals, which today can be challenging,
somewhat intimidating.
So the final lessons that we've picked
up from working with lots of customers
over the last many years is starting
simple and building evals right at the
start of that development process. Don't
wait till the end and do a bit of ad hoc
testing. Define a simple set right at
the start and evolve it as you build out
your application. Next up, use real
human data. Don't come up with
hypothetical examples hoping they're
going to be representative of your real
users. Instead, sample real past user
inputs and use them as the basis of your
eval set. And then finally, annotate
with subject matter experts and spend
the time that you spend on eval making
sure that that preference data is being
captured by your graders, by your
prompts, and let some of that manual
repetitive work like prompt

[00:21]
optimization, greater alignment, let's
try and get that to be automated so you
can focus on the tasks that matter.
So we really see rigorous evals enabling
anyone to build high performing products
and they're a crucial part of that
development journey.
And today you've seen how we evaluate
our frontier models here at OpenAI and
how you can evaluate your applications
using the same rigor through our new
product.

</details>
