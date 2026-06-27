---
title: "The New Stack and Ops for AI"
channel: openai
url: https://www.youtube.com/watch?v=XGJNo8TpuVA
youtube_id: XGJNo8TpuVA
published: 2023-11-13
duration: "34:09"
captions: en
---

# The New Stack and Ops for AI

[![The New Stack and Ops for AI](https://img.youtube.com/vi/XGJNo8TpuVA/hqdefault.jpg)](https://www.youtube.com/watch?v=XGJNo8TpuVA)

<details>
<summary>자막: The New Stack and Ops for AI (34:09)</summary>

[00:00]
[music]
-Hi, everyone.
Welcome to the new Stack
and Ops for AI,
going from prototype
to production.
My name is Sherwin,
and I lead the Engineering team
for the OpenAI Developer Platform,
the team that builds and maintains
the APIs that over 2 million developers,
including hopefully many of you,
have used to build products on top of our models.
-I'm Shyamal,
I'm part of the Applied team where I've worked
with hundreds of startups
and enterprises
to help them build great products
and experiences on our platform.
-Today, we're really excited to talk
to you all about the process
of taking your applications
and bringing them
from the prototype stage into production.
First, I wanted to put things
into perspective for a little bit.
While it might seem
like it's been a very long time
since ChatGPT
has entered our lives
and transformed the world,
it actually hasn't even been a full calendar year
since it was launched.
ChatGPT was actually launched
in late November 2022,

[00:01]
and it hasn't even been
a full 12 months yet.
Similarly, GPT-4
was only launched in March 2023,
and it hasn't even been eight months
since people have experienced
our flagship model
and tried to use it into their products.
In this time, GPT has gone
from being a toy for us
to play around with and share on social media
into a tool for us
to use in our day-to-day lives
and our workplaces
into now a capability that enterprises,
startups, and developers
everywhere are trying
to bake into their own products.
Oftentimes, the first step
is to build a prototype.
As many of you probably know,
it's quite simple and easy
to set up a really cool prototype
using one of our models.
It's really cool to come up with a demo
and show it to all of our friends.
However, oftentimes there's a really big gap
in going from there into production,
and oftentimes it's hard
to get things into production.
A large part of this is due
to the nondeterministic nature of these models.
Scaling non-deterministic apps
from prototype
into production can oftentimes
feel quite difficult
without a guiding framework.

[00:02]
Oftentimes,
you might feel something like this
where you have a lot of tools
out there for you to use.
The field is moving very quickly.
There's a lot of different possibilities,
but you don't really know
where to go and what to start with.
For this talk, we wanted
to give you all a framework to use
to help guide you moving your app
from prototype into production.
This framework we wanted to provide to you
is in the form of a stack diagram
that is influenced
by a lot of the challenges
that our customers have brought to us
in scaling their apps.
We'll be talking
about how to build a delightful
user experience on top of these LLMs.
We'll be talking about handling
model inconsistency
via grounding the model
with Knowledge Store and Tools.
We'll be talking about how
to iterate on your applications
in confidence using Evaluations.
Finally, we'll be talking about
how to manage scale
for your applications and thinking about cost
and latency using orchestration.
For each one of these,
we'll be talking about
a couple of strategies
that hopefully you all can bring back
and use in your own different products.
Oftentimes first,
we just have a simple prototype.
At this point,
there isn't a whole stack like what I just showed.

[00:03]
There's usually just
a very simple setup here
where you have your application
and it's talking directly with their API.
While this works great initially,
very quickly you'll realize that it's not enough.
Shyamal: Let's talk about
the first layer of this framework.
Technology is as useful
as the user experience surrounding it.
While the goal
is to build a trustworthy, defensive,
and delightful user experience,
AI-assisted copilots
and assistants present a different set
of human-computer interaction
and UX challenges.
The unique considerations
of scaling applications built
with our models
makes it even more important
to drive better
and safe outcomes for users.
We're going to talk
about two strategies here
to navigate some
of the challenges that come
with building apps on top of our models,
which are inherently probabilistic in nature.
Controlling for uncertainty
and building guardrails
for steerability and safety.
Controlling
for uncertainty refers to proactively
optimizing the user experience

[00:04]
by managing how the model interacts
and responds to the users.
Until now, a lot of products
have been deterministic
where interactions can happen
in repeatable and precise ways.
This has been challenging with the shift
towards building language user interfaces.
It has become important
to design for human centricity
by having the AI enhance
and augment human capabilities
rather than replacing human judgment.
When designing ChatGPT,
for example, we baked in a few UX elements
to help guide the users and control
for this inherent uncertainty
that comes with building apps
powered by models.
The first one,
depending on the use case, the first strategy here
is to keep human in the loop and understand
that the first artifact created
with generative AI
might not be
the final artifact that the user wants.
Giving the users
an opportunity to iterate
and improve the quality
over time is important
for navigating uncertainty
and building a robust UX.

[00:05]
The feedback controls,
on the other hand,
also provide affordances for fixing mistakes
and are useful signals
to build a solid data flywheel.
Another important aspect
of building transparent UX
is to communicate the system's capabilities
and limitations to the users.
The user can understand
what the AI can or cannot do.
You can take this further by explaining
to the user how the AI
can make mistakes.
In ChatGPT's case,
this takes the form of an AI notice at the bottom.
This sets the right expectations
with the user.
Finally, a well-designed user interface
can guide user interaction
with AI to get the most helpful
and safer responses
and the best out of the interaction.
This can take the form
of suggestive prompts in ChatGPT,
which not only help onboard
the users to this experience,
but also provide the user an opportunity
to ask better questions,

[00:06]
suggest alternative ways
of solving a problem, inspire,
and probe deeper.
All three of these strategies
really put the users
in the center and at the control
of the experience by designing a UX
that brings the best out of working
with AI products
and creating a collaborative
and human-centric experience.
To establish a foundation
of trust and for you
to build more confidence in deploying
your GPT-powered applications,
it's not only important
to build a human-centric UX
but also to build guardrails
for both steerability and safety.
You can think of guardrails
as essentially constraints
or preventative controls that sit between
the user experience and the model.
They aim to prevent harmful and unwanted
content getting to your applications,
to your users, and also adding steerability
to the models in production.
Some of the best interaction paradigms
that we've seen developers
build have built safety

[00:07]
and security at the core of the experience.
Some of our best models are the ones
that are most aligned with human values.
We believe some
of the most useful and capable UX
brings the best out of safety
and steerability for better, safer outcomes.
To demonstrate an example of this,
let's start with a simple prompt in DALL·E.
Very timely for Christmas,
to create an abstract oil painting
of a Christmas tree.
DALL·E uses the model to enhance
the prompt by adding more details
and specificity around the hues,
the shape of the tree,
the colors and brush strokes,
and so on.
Now, I'm not an artist,
so I wouldn't have done
a better job at this,
but in this case,
I'm using DALL·E as a partner
to bring my ideas to imagination.
Now, you might be wondering,
how is this a safety guardrail?
Well, the same prompt enrichment
used to create better artifacts
also functions as a safety guardrail.
If the model in this case detects
a problematic prompt

[00:08]
that violates the privacy
or rights of individuals,
it'll suggest a different prompt
rather than refusing it outright.
In this case, instead of generating
an image of a real person,
it captures the essence and then creates
an image of a fictional person.
We shared one example
of a guardrail that can help
with both steerability and safety,
but guardrails can take many other forms.
Some examples of this
are compliance guardrails,
security guardrails,
and guardrails to ensure
that the model outputs
are syntactically and semantically correct.
Guardrails become essentially important
when you're building interfaces
for highly regulated industries
where there's low tolerance
for errors and hallucination
and where you have to prioritize security
and compliance.
We built a great user experience
with both steerability and safety,
but our journey doesn't end there.

[00:09]
-At this point, you've built
a delightful user experience
for all of your users that can manage around some
of the uncertainty of these models.
While this works really great as a prototype,
when the types of queries
that you'll be getting from your users
are pretty constrained,
as you scale this into production,
you'll very quickly start running
into consistency issues
because as you scale out your application,
the types of queries and inputs
that you'll get will start varying quite a lot.
With this, we want to talk
about model consistency,
which introduces the second part
of our stack involving grounding the model
with the knowledge store and tools.
Two strategies that we've seen
in our customers adopt pretty well here
to manage around the inherent inconsistency
of these models include one,
constraining the model behavior
at the model level itself,
and then two, grounding the model
with some real-world knowledge using something
like a knowledge store or your own tools.
The first one of these is constraining
the model behavior itself.
This is an issue
because oftentimes it's difficult
to manage around
the inherent probabilistic nature of LLMs

[00:10]
and especially
as a customer of our API
where you don't have really
low-level access to the model,
it's really difficult to manage
around some of this inconsistency.
Today, we actually introduced
two new model-level features
that help you constrain model behavior,
and wanted to talk to you about this today.
The first one of these is JSON mode
which if toggled on will constrain
the output of the model
to be within the JSON grammar.
The second one is reproducible outputs
using a new parameter named C
that we're introducing into chat completions.
The first one of these, JSON mode,
has been a really commonly asked
feature from a lot of people.
It allows you to force the model
to output within the JSON grammar.
Often times this is really important to developers
because you're taking the output
from an LLM
and feeding it into
a downstream software system.
A lot of times, in order to do that you'll need
a common data format
and JSON is one of the most popular of these.
While this is great, one big downfall
of inconsistency here
is when the model outputs invalid JSON
it will actually break your system
and throw an exception

[00:11]
which is not a great experience
for your customers.
JSON mode that we introduce today
should significantly
reduce the likelihood of this.
The way it works is something
like this where in chat completions,
we've added a new argument known
as JSON Schema.
If you pass and type object into that parameter
and you pass it into our API,
the output that you'll be getting
from our system
or from the API will be constrained
to within the JSON grammar.
The content field there
will be constrained to the JSON grammar.
While this doesn't remove 100%
of all JSON errors in our evals
that we've seen internally,
it does significantly reduce the error rate
for JSON being output
by this model.
The second thing is getting significantly
more reproducible outputs
via a C parameter in chat completions.
A lot of our models
are non-deterministic
but if you look under the hood,
they're actually three main contributors
to a lot of the inconsistent behavior
happening behind the scenes.
One of these
is how the model samples its tokens based off
of the probability that it gets.

[00:12]
That's controlled by the temperature
and the top P parameters
that we already have.
The second one is the C parameter
which is the random number
that the model uses
to start its calculations and base it off of.
The third one is this thing
called system fingerprint
which describes the state
of our engines that are running
in the backend and the code
that we have deployed on those.
As those change, there will be some inherent
non-determinants when that happens.
As of today, we only give people access
to temperature and top P.
Starting today,
we'll actually be giving developers access
to the C parameter as in input
and giving developers visibility
into system fingerprint in the responses
of the chat completions model.
In practice, it looks something like this
where in chat completions there
will now be a seed parameter
that you can pass in which is an integer.
If you're passing a seed
like one, two, three, four, five,
and you're controlling the temperature setting it
to something like zero,
your output will be significantly
more consistent over time.
If you send this particular
request over to us five times,
the output that you will be getting
under choices

[00:13]
will be significantly more consistent.
Additionally, we're giving you access
to the system fingerprint parameter
which on every response
from the model
will tell you a fingerprint about
our engine system under the hood.
If you're getting the exact
same system fingerprint back
from earlier responses,
and you passed in the same seed
and temperature zero you're almost certainly
going to get the same response.
Cool, so those are model-level behaviors
that you can actually very quickly pick up
and just try with even today.
A more involved technique
is called grounding the model
which helps reduce the inconsistency
of the model behavior
by giving it additional facts
to base its answer off of.
The root of this
is that when it's on its own a model
can often hallucinate information
as you all are aware of.
A lot of this is due to the fact
that we're forcing the model
to speak
and if it doesn't really know anything
it will have to try
and say something and a lot of the times
it will make something up.
The idea behind this
is to ground the model
and give it a bunch of facts
so that it doesn't have nothing to go off of.

[00:14]
Concretely, what we'd be doing here
is in the input context explicitly giving
the model some grounded facts
to reduce the likelihood
of hallucinations from the model.
This is actually quite a broad sentiment.
The way this might look
in a system diagram is like this
where a query will come in
from your user,
hits our servers and instead
of first passing it over to our API,
we're first going to do a round trip
to some type of grounded fact source.
Let's say we pass the query in there.
Then in our grounded fact source,
it will ideally return some type
of grounded fact for us
and then we will then take
the grounded fact
and the query itself and pass it over to our API.
Then ideally the API takes that information
and synthesizes some type of response
using the grounded fact here.
To make this a little bit more concrete,
one way that this might be
implemented is using RAG
or vector databases which is a very common
and popular technique today.
In this example, let's say I'm building
a customer server spot
and a user asks, how do I delete my account?
This might be specific to my own application
or my own product
so the API by itself won't really know this.

[00:15]
Let's say, I have a retrieval service
like a vector database
that I've used to index a bunch
of my internal documents
and a bunch of my FAQs about support
and it knows about how to delete documents.
What I would do here first is do
a query to the retrieval service
with how do I delete my account.
Let's say it finds a relevant snippet
for me here that says,
in the account deletion FAQ,
you go to settings,
you scroll down and click here, whatever.
We would then pass that along
with the original query to our API
and then the API would use that fact
to ground some response back to the user.
In this case, it would say,
to delete your account,
go to settings, scroll down, click here.
This is one implementation,
but actually, this can be quite broad
and with OpenAI function calling in the API,
you can actually use your own services
and we've seen this used
to great effect by our customers.
In this case, instead of having
a vector database,
we might use our own API
or own microservice here.
In this case, let's say a customer is asking
for what the current mortgage rates
are which of course,
even our LMS don't know immediately
because this changes all the time.
Let's say we have a microservice
that's doing some daily sync job
that's downloading

[00:16]
and keeping track
of the current mortgage rates.
In this case,
we would use function calling.
We would tell our model
that has it access to this function known
as get_mortgage_rates(),
which is within our microservice.
We'd first send a request over to the API
and it would express its intent to call
this get_mortgage_rates() function.
We would then fulfill that intent by calling
our API with get_mortgage_rates().
Let's say it returns something
like 8% mortgage rates
for a 30-year fixed mortgage
and then the rest looks very similar
where you're passing that into the API
with the original query
and the model is then responding
with a ground response,
saying something like, not great.
Current 30-year fixed rates are actually at 8% already.
At a very broad level, you're using
this grounded fact source in a generic way,
to help ground the model
and help reduce model inconsistency.
I just wrote two different examples of this,
but the grounded fact source
can also be other things
like a search index even elastics earch
or some type of more general search index.
It can be something like a database.
It could even be something
like browsing the internet
or trying some smart mechanism
that grab additional facts.

[00:17]
The main idea is to give something
for the model to work.
One thing I wanted to call out
is that the OpenAI Assistants API
that we just announced today,
actually offers
an out-of-the-box retrieval setup for you
to use and build on top of
with retrieval built right in
in a first-class experience.
I'd recommend checking it out.
Shyamal: So far we talked
about building a transparent
human-centric user experience.
Then we talked about
how do you consistently deliver
that user experience
through some of the model-level features
we released today and then
by grounding the model.
Now we're going
to talk about how do we deliver
that experience consistently
without regressions.
This is where evaluating
the performance of the model
becomes really important.
We're going to talk about
two strategies here
that will help evaluate performance
for applications built with our models.
The first one is to create evaluation suites
for your specific use cases.

[00:18]
Working with many orgs,
we hear time and time again
that evaluating the model
and the performance
and testing progressions is hard,
often slowing down development velocity.
Part of that problem is for developers
to not think
about a systematic process
for evaluating the performance
of these models
and also doing evaluations too late.
Evaluations are really
the key to success here.
In measuring the performance
of the models
on real product scenarios
is really essential
to prevent regressions
and for you to build confidence
as you deploy these models at scale.
You can think of evals
as essentially unit tests
for the large language models.
People often think of prompting
as a philosophy,
but it is more of a science.
When you pair it
with evaluations,
you can treat it like
a software product or delivery.
Evals can really transform ambiguous dialogues
into quantifiable experiments.

[00:19]
They also make model governance,
model upgrades,
much easier setting expectations
around what's good or bad.
Capabilities, evaluations,
and performance really go hand-in-hand
and they should be the place where
you begin your AI engineering journey.
In order to build evals,
let's say we start simple
and have human annotators
evaluate the outputs
of an application as you're testing.
A typical approach in this case
is where you have an application
with different sets of prompts
or retrieval approaches
and so on and you'd want to start
by building a golden test data set
of evals by looking
at these responses
and then manually grading them.
As you annotate this over time,
you end up with a test suite
that you can then run in online
or offline fashion or part
of your CICD pipelines.
Due to the nature
of large language models,
they can make mistakes,
so do humans.
Depending on your use case,
you might want to consider
building evals to test for things

[00:20]
like bad output formatting
or hallucinations,
agents going off the rails,
bad tone, and so on.
Let's talk about how to build an Eval.
Earlier this year,
we open-sourced the evals framework,
which has been an inspiration
for many developers.
This library contains a registry
of really challenging evals
for different specific
use cases and verticals,
and a lot of templates,
which can come in handy
and can be a solid starting point
for a lot of you
to understand the kind of evaluations
and tests you should be building
for your specific use cases.
After you've built an eval suite,
a good practice
and hygiene here is to log
and track your eval runs.
In this case, for example,
we have five different eval runs,
each scored against
our golden test dataset,
along with the annotation feedback
and audit of changes.
The audit of changes could include things
like changes to your prompt,

[00:21]
to your retrieval strategy,
few short examples,
or even upgrade
to model snapshots.
You don't need complicated tooling to start
with tracking something like this.
A lot of our customers start
with just a spreadsheet,
but the point is each run
should be stored
at a very granular level
so you can track it accordingly.
Although human feedback and user evals
are the highest signal in quality,
it's often expensive
or not always practical,
for example, when you cannot use
real customer data for evals.
This is where automated evals
can help developers monitor progress
and test for regressions quickly.
Let's talk about model-graded evals
or essentially using AI to grade AI.
GPT-4 can be a strong evaluator.
In fact, in a lot of natural language
generation tasks,
we've seen GPT-4 evaluations to be well
correlated with human judgment

[00:22]
with some additional prompting methods.
The benefit of model-graded evals here
is that by reducing human involvement
in parts of the evaluation process
that can be handled by language models,
humans can be more focused on addressing
some of the complex edge cases
that are needed for refining
the evaluation methods.
Let's look at an example
of what this could look like in practice.
In this case, we have an input query
and two pairs of completions.
One that is the ground truth and one
that is sampled from the model.
The evaluation here is a very simple
prompt that asks GPT-4
to compare the factual content
of the submitted answer with the expert answer.
This is passed to GPT-4
to grade, and in this case,
GPT-4's observation is there's a disparity
between the submitted answer
and the expert answer.
We can take this further by improving
our evaluation prompt
with some additional prompt engineering techniques
like chain of thought and so on.

[00:23]
In the previous example,
the eval was pretty binary.
Either the answer matched
the ground truth or it did not.
In a lot of cases,
you'd want to think about eval metrics,
which are closely correlated
with what your users would expect
or the outcomes that you're trying to derive.
For example, going back to Sherwin's example
of a customer service assistant,
we'd want to eval for custom metrics
like the relevancy of the response,
the credibility of the response, and so on,
and have the model essentially score
against those different metrics
or the criteria that we decide.
Here's an example of what that criteria
or scorecard would look like.
Here we have provided GPT-4 essentially
this criteria for relevance, credibility,
and correctness, and then use GPT-4
to score the candidate outputs.
A good tip here is a show rather than tell,
which basically including examples

[00:24]
of what a score of one
or a FI could look like,
would really help in this evaluation process
so that model would really appreciate
the spread of the criteria.
In this case, GPT-4 has effectively learned
an internal model of language quality,
which helps it to differentiate
between relevant text and low-quality text.
Harnessing this internal scoring
mechanism allows us
to do auto valuation
of new candidate outputs.
When GPT-4 is expensive
or slow for evals,
even after today's price drops,
you can fine-tune a 3.5 turbo model,
which essentially distills GPT-4's outputs
to become really good
at evaluating your use cases.
In practice, what this means
is you can use GPT-4
to curate high-quality data
for evaluations,
then fine-tune a 3.5 judge model
that gets really good at evaluating those outputs,
and then use that fine-tuned model to valuate
the performance of your application.
This also helps reduce some
of the biases that come

[00:25]
with just using GPT-4 for evaluations.
The key here is to adopt
evaluation-driven development.
Good evaluations are the ones
which are well correlated
to the outcomes that you're trying
to derive or the user metrics
that you care about.
They have really high end-to-end
coverage in the case of RAG
and they're scalable to compute.
This is where automated evaluations really help.
-At this point,
you've built a delightful user experience,
you're able to deliver it
consistently to your users
and you're also able to iterate on the product
in confidence using evaluations.
If you do all this right,
oftentimes you'll find yourselves
with a product that's blowing up
and really, really popular.
If the last year has shown us anything,
it's that the consumer appetite
and even the internal employee appetite
for AI is quite insatiable.
Oftentimes, you'll now start thinking
about how to manage scale.
Oftentimes, managing scale
means managing around latency
and managing around cost.
With this, we introduce
the final part of our stack,

[00:26]
known as orchestration,
where you can manage around scale
by adding a couple of additional mechanisms
and forks into your application.
Two strategies that we've seen
in managing costs
and latency involve
using semantic caching
to reduce the number
of round trips that you're taking
to our API as well as routing
to the cheaper models.
The first one of these is known
as semantic caching.
What semantic caching looks like
in practice from a systems perspective,
it you're going to be adding
a new layer in your logic
to sit between us and your application.
In this case, if a query comes in
asking when was GPT-4 released,
you would first go to your semantic cache
and do a lookup there
and see if you have anything in your cache.
In this case, we don't and then you would
just pass this request over to our API.
Then the API would respond
to something like March 14th, 2023,
and then you'd save this
within your semantic cache,
which might be a vector database
or some other type of store.

[00:27]
The main point here is you're saving
the March 14th, 2023 response
and keying it with that query
of when was GPT-4 released
and then you pass this back
over to your users.
This is fine, but let's say,
a month or a week from now,
another request comes in where
a user asks GPT-4 release date?
Now, this isn't the exact same query
that you had before,
but it is very semantically similar
and can be answered
by the exact same response.
In this case, you would do
a semantic lookup in your cache,
realize that you have this already
and you'd just return back to the user
with March 14th, 2023.
With this setup,
you've actually saved latency
because you're no longer doing
a round trip to our API
and you've saved costs
because you're no longer hitting
and paying for additional tokens.
While this works great,
oftentimes, it might be a little bit
difficult to manage
and there are often even more capable ways
of managing cost and latency.
This is where we start thinking
about routing to cheaper models
and where orchestration really comes into play.

[00:28]
When I talk about routing
to cheaper models,
oftentimes the first thing to think about
is to go from GPT-4 into 3.5 Turbo,
which sounds great
because GPT-3.5 Turbo is so cheap, so fast,
however, it's obviously not nearly
as smart as GPT-4.
If you were to just drag
and drop 3.5 Turbo into your application,
you'll very quickly realize
that you're not delivering
as great of a customer experience.
However, the GPT-3.5 Turbo Finetuning API
that we released only two months ago
has already become a huge hit
with our customers and it's been
a really great way for customers
to reduce costs by fine-tuning a custom
version of GPT-3.5 Turbo
for their own particular use case,
and get all the benefits
of the lower latency and the lower cost.
There's obviously
a full talk about fine-tuning earlier,
but just in a nutshell, the main idea here
is to take your own curated dataset.
This might be something like hundreds
or even thousands of examples at times,
describing the model on how to act
in your particular use case.
You'd pass in that curated dataset
into our fine-tuning API maybe tweak
a parameter or two here

[00:29]
and then the main output here is a custom
fine-tuned version of 3.5 Turbo specific
to you and your organization
based off of your dataset.
While this is great, oftentimes actually,
there's a huge activation energy
associated with doing this
and it's because it can be quite expensive
to generate this curated data set.
Like I mentioned,
you might need hundreds, thousands,
sometimes even tens of thousands
of examples for your use case,
and oftentimes you'll be manually
creating these yourself
or hiring some contractors
to do this manually as well.
However, one really cool method
that we've seen a lot of customers adopt
is you can actually use GPT-4
to create the training dataset
to fine-tune 3.5 Turbo.
It's starting to look very similar
to what Shyamal just mentioned
around evals as well,
but GPT-4 is at an intelligence level
where you can actually
just give it a bunch of prompts,
it'll output a bunch
of outputs for you here,
and that output
can just be your training set.
You don't need any human
manual intervention here.
What you're effectively doing here
is you're distilling the outputs
from GPT-4

[00:30]
and feeding that into 3.5 Turbo
so it can learn.
Oftentimes, what this does
is that in your specific narrow domain,
it helps this fine-tuned version
of 3.5 Turbo be almost as good as GPT-4.
If you do take the effort in doing all of this,
the dividends that you get down
the line are actually quite significant,
not only from a latency perspective,
because GPT-3.5 Turbo is obviously a lot faster,
but also from a cost perspective.
Just to illustrate this a little bit more concretely,
if you look at the table,
even after today's GPT-4 price drops,
a fine-tuned version of 3.5 Turbo
is still 70% to 80% cheaper.
While it's not as cheap
as the vanilla 3.5 Turbo,
you can see it's still quite a bit off from GPT-4,
and if you switch over
to fine-tuned 3.5 Turbo,
you'll be saving on a lot of cost.
-All right, so we talked about a framework
that can help you navigate
the unique considerations
and challenges that come
with scaling applications built with our models,

[00:31]
going from prototype to production.
Let's recap.
We talked about how
to build a useful, delightful,
and human-centric user experience
by controlling for uncertainty
and adding guardrails.
Then we talked
about how do we deliver
that experience consistently
through grounding the model
and through some of the model-level features.
Then we talked about consistently
delivering that experience
without regressions
by implementing evaluations.
Then finally, we talked about considerations
that come with scale,
which is managing latency and costs.
As we've seen,
building with our models increases
surface area for what's possible,
but it has also increased
the footprint of challenges.
All of these strategies we talked about,
including the orchestration part
of the stack,
have been converging into
this new discipline called LLM Ops
or Large Language Model Operations.
Just as DevOps emerged
in the early 2000s
to streamline the software development process,

[00:32]
LLM Ops has recently emerged
in response to the unique challenges
that are posed by building applications with LLMs
and they've become a core component
of many enterprise architecture and stacks.
You can think of LLM Ops
as basically the practice, tooling,
and infrastructure that is required
for the operational management
of LLMs end-to-end.
It's a vast and evolving field,
and we're still scratching the surface.
While we won't go into details,
here's a preview of what this could look like.
LLM Ops capabilities help address
challenges like monitoring,
optimizing performance,
helping with security compliance,
managing your data and embeddings,
increasing development velocity,
and really accelerating the process
of reliable testing
and evaluation at scale.
Here, observability and tracing
become especially important
to identify and debug failures
with your prompt chains and assistants
and handle issues in production faster,

[00:33]
making just collaboration
between different teams easier.
Gateways, for example,
are important to simplify integrations,
can help with centralized management
of security, API keys, and so on.
LLM Ops really enable scaling
to thousands of applications
and millions of users,
and with the right foundations here,
organizations can really
accelerate their adoption.
Rather than one-off tools,
the focus should be really developing
these long-term platforms
and expertise.
Just like this young explorer
standing at the threshold,
we have a set of wide field
of opportunities in front of us
to build the infrastructure
and primitives
that stretch beyond
the framework we talked about today.
We're really excited to help you
build the next-generation assistants
and ecosystem for generations to come.
There's so much to build and discover,
and we can only do it together.
Thank you.
[applause]

[00:34]
[music]

</details>
