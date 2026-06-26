<!-- source: https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals/ -->

## Search the cookbook

Mar 21, 2024

# Getting Started with OpenAI Evals

This recipe is archived and may reference outdated models or APIs.

[![Roy Ziv](https://avatars.githubusercontent.com/u/103690170?v=4)  RZ](https://www.linkedin.com/in/roy-ziv-a46001149/)  [![Shyamal Anadkat](https://pbs.twimg.com/profile_images/1590564338682560512/3bbZJqxZ_400x400.jpg)  SA](https://twitter.com/shyamalanadkat)

[Roy Ziv 
(OpenAI)
 ,](https://www.linkedin.com/in/roy-ziv-a46001149/)  [Shyamal Anadkat 
(OpenAI)](https://twitter.com/shyamalanadkat)

[View on GitHub](https://github.com/openai/openai-cookbook/blob/main/examples/evaluation/Getting_Started_with_OpenAI_Evals.ipynb) [Download raw](https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/evaluation/Getting_Started_with_OpenAI_Evals.ipynb)

**Note: OpenAI now has a hosted evals product with an API! We recommend you use this instead.
See [Evals](https://platform.openai.com/docs/guides/evals)**

The [OpenAI Evals](https://github.com/openai/evals/tree/main) framework consists of

1. A framework to evaluate an LLM (large language model) or a system built on top of an LLM.
2. An open-source registry of challenging evals

This notebook will cover:

* Introduction to Evaluation and the [OpenAI Evals](https://github.com/openai/evals/tree/main) library
* Building an Eval
* Running an Eval

#### What are evaluations/ `evals`?

Evaluation is the process of validating and testing the outputs that your LLM applications are producing. Having strong evaluations (“evals”) will mean a more stable, reliable application that is resilient to code and model changes. An eval is a task used to measure the quality of the output of an LLM or LLM system. Given an input prompt, an output is generated. We evaluate this output with a set of ideal answers and find the quality of the LLM system.

#### Importance of Evaluations

If you are building with foundational models like `GPT-4`, creating high quality evals is one of the most impactful things you can do. Developing AI solutions involves an iterative design process. [Without evals, it can be very difficult and time intensive to understand](https://youtu.be/XGJNo8TpuVA?feature=shared&t=1089) how different model versions and prompts might affect your use case.

<!-- yt-inline:XGJNo8TpuVA -->
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


With OpenAI’s [continuous model upgrades](https://platform.openai.com/docs/models/continuous-model-upgrades), evals allow you to efficiently test model performance for your use cases in a standardized way. Developing a suite of evals customized to your objectives will help you quickly and effectively understand how new models may perform for your use cases. You can also make evals a part of your CI/CD pipeline to make sure you achieve the desired accuracy before deploying.

#### Types of evals

There are two main ways we can evaluate/grade completions: writing some validation logic in code
or using the model itself to inspect the answer. We’ll introduce each with some examples.

**Writing logic for answer checking**

The simplest and most common type of eval has an input and an ideal response or answer. For example,
we can have an eval sample where the input is “What year was Obama elected president for the first
time?” and the ideal answer is “2008”. We feed the input to a model and get the completion. If the model
says “2008”, it is then graded as correct. We can write a string match to check if the completion includes the phrase “2008”. If it does, we consider it correct.

Consider another eval where the input is to generate valid JSON: We can write some code that
attempts to parse the completion as JSON and then considers the completion correct if it is
parsable.

**Model grading: A two stage process where the model first answers the question, then we ask a
model to look at the response to check if it’s correct.**

Consider an input that asks the model to write a funny joke. The model then generates a
completion. We then create a new input to the model to answer the question: “Is this following
joke funny? First reason step by step, then answer yes or no” that includes the completion.” We
finally consider the original completion correct if the new model completion ends with “yes”.

Model grading works best with the latest, most powerful models like `GPT-4` and if we give them the ability
to reason before making a judgment. Model grading will have an error rate, so it is important to validate
the performance with human evaluation before running the evals at scale. For best results, it makes
sense to use a different model to do grading from the one that did the completion, like using `GPT-4` to
grade `GPT-3.5` answers.

#### OpenAI Eval Templates

In using evals, we have discovered several “templates” that accommodate many different benchmarks. We have implemented these templates in the OpenAI Evals library to simplify the development of new evals. For example, we have defined 2 types of eval templates that can be used out of the box:

* **Basic Eval Templates**: These contain deterministic functions to compare the output to the ideal\_answers. In cases where the desired model response has very little variation, such as answering multiple choice questions or simple questions with a straightforward answer, we have found this following templates to be useful.
* **Model-Graded Templates**: These contain functions where an LLM compares the output to the ideal\_answers and attempts to judge the accuracy. In cases where the desired model response can contain significant variation, such as answering an open-ended question, we have found that using the model to grade itself is a viable strategy for automated evaluation.

### Getting Setup

First, go to [github.com/openai/evals](https://github.com/openai/evals), clone the repository with `git clone git@github.com:openai/evals.git` and go through the [setup instructions](https://github.com/openai/evals).

To run evals later in this notebook, you will need to set up and specify your OpenAI API key. After you obtain an API key, specify it using the `OPENAI_API_KEY` environment variable.

Please be aware of the costs associated with using the API when running evals.

from openai import OpenAI
import pandas as pd

client = OpenAI()

## Building an evaluation for OpenAI Evals framework

At its core, an eval is a dataset and an eval class that is defined in a YAML file. To start creating an eval, we need

1. The test dataset in the `jsonl` format.
2. The eval template to be used

### Creating the eval dataset

Lets create a dataset for a use case where we are evaluating the model’s ability to generate syntactically correct SQL. In this use case, we have a series of tables that are related to car manufacturing

First we will need to create a system prompt that we would like to evaluate. We will pass in instructions for the model as well as an overview of the table structure:

"TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]"

For this prompt, we can ask a specific question:

"Q: how many car makers are their in germany?"

And we have an expected answer:

"A: SELECT count ( * )  FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country   =   T2.CountryId WHERE T2.CountryName   =   'germany'"

The dataset needs to be in the following format:

"input": [{"role": "system", "content": "<input prompt>"}, {"role": "user", "content": <user input>}, "ideal": "correct answer"]

Putting it all together, we get:

{"input": [{"role": "system", "content": "TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]\n"}, {"role": "system", "content": "Q: how many car makers are their in germany"}, "ideal": ["A: SELECT count ( * )  FROM CAR_MAKERS AS T1 JOIN COUNTRIES AS T2 ON T1.Country   =   T2.CountryId WHERE T2.CountryName   =   'germany'"]}

One way to speed up the process of building eval datasets, is to use `GPT-4` to generate synthetic data

## Use GPT-4 to generate synthetic data
# Define the system prompt and user input (these should be filled as per the specific use case)
system_prompt = """You are a helpful assistant that can ask questions about a database table and write SQL queries to answer the question.
    A user will pass in a table schema and your job is to return a question answer pairing. The question should relevant to the schema of the table,
    and you can speculate on its contents. You will then have to generate a SQL query to answer the question. Below are some examples of what this should look like.

    Example 1
    ```````````
    User input: Table museum, columns = [*,Museum_ID,Name,Num_of_Staff,Open_Year]\nTable visit, columns = [*,Museum_ID,visitor_ID,Num_of_Ticket,Total_spent]\nTable visitor, columns = [*,ID,Name,Level_of_membership,Age]\nForeign_keys = [visit.visitor_ID = visitor.ID,visit.Museum_ID = museum.Museum_ID]\n
    Assistant Response:
    Q: How many visitors have visited the museum with the most staff?
    A: SELECT count ( * )  FROM VISIT AS T1 JOIN MUSEUM AS T2 ON T1.Museum_ID   =   T2.Museum_ID WHERE T2.Num_of_Staff   =   ( SELECT max ( Num_of_Staff )  FROM MUSEUM ) 
    ```````````

    Example 2
    ```````````
    User input: Table museum, columns = [*,Museum_ID,Name,Num_of_Staff,Open_Year]\nTable visit, columns = [*,Museum_ID,visitor_ID,Num_of_Ticket,Total_spent]\nTable visitor, columns = [*,ID,Name,Level_of_membership,Age]\nForeign_keys = [visit.visitor_ID = visitor.ID,visit.Museum_ID = museum.Museum_ID]\n
    Assistant Response:
    Q: What are the names who have a membership level higher than 4?
    A: SELECT Name   FROM VISITOR AS T1 WHERE T1.Level_of_membership   >   4 
    ```````````

    Example 3
    ```````````
    User input: Table museum, columns = [*,Museum_ID,Name,Num_of_Staff,Open_Year]\nTable visit, columns = [*,Museum_ID,visitor_ID,Num_of_Ticket,Total_spent]\nTable visitor, columns = [*,ID,Name,Level_of_membership,Age]\nForeign_keys = [visit.visitor_ID = visitor.ID,visit.Museum_ID = museum.Museum_ID]\n
    Assistant Response:
    Q: How many tickets of customer id 5?
    A: SELECT count ( * )  FROM VISIT AS T1 JOIN VISITOR AS T2 ON T1.visitor_ID   =   T2.ID WHERE T2.ID   =   5 
    ```````````
    """

user_input = "Table car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]"

messages = [{
        "role": "system",
        "content": system_prompt
        "role": "user",
        "content": user_input
]

completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=messages,
    temperature=0.7,
    n=5

for choice in completion.choices:
    print(choice.message.content + "\n")

Q: What is the average horsepower for cars made in Europe?
A: SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE continents.Continent = 'Europe'

Q: What is the average horsepower for cars made in the USA?
A: SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN car_makers ON car_names.MakeId = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.CountryName = 'USA'

Q: What is the average horsepower for cars produced in countries from the continent with the id '3'?
A: SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE continents.ContId = '3'

Q: What is the average horsepower for cars made by makers from Europe?
A: SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE continents.Continent = 'Europe'

Q: What is the average horsepower for cars made in the USA?

A: SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN car_makers ON car_names.MakeId = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.CountryName = 'USA'

Once we have the synthetic data, we need to convert it to match the format of the eval dataset.

eval_data = []
input_prompt = "TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]"

for choice in completion.choices:
    question = choice.message.content.split("Q: ")[1].split("\n")[0]  # Extracting the question
    answer = choice.message.content.split("\nA: ")[1].split("\n")[0]  # Extracting the answer
    eval_data.append({
        "input": [
            {"role": "system", "content": input_prompt},
            {"role": "user", "content": question},
        ],
        "ideal": answer
    })

for item in eval_data:
    print(item)

{'input': [{'role': 'system', 'content': 'TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]'}, {'role': 'user', 'content': 'What is the average horsepower for cars made in Europe?'}], 'ideal': "SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE continents.Continent = 'Europe'"}
{'input': [{'role': 'system', 'content': 'TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]'}, {'role': 'user', 'content': 'What is the average horsepower for cars made in the USA?'}], 'ideal': "SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN car_makers ON car_names.MakeId = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.CountryName = 'USA'"}
{'input': [{'role': 'system', 'content': 'TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]'}, {'role': 'user', 'content': "What is the average horsepower for cars produced in countries from the continent with the id '3'?"}], 'ideal': "SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE continents.ContId = '3'"}
{'input': [{'role': 'system', 'content': 'TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]'}, {'role': 'user', 'content': 'What is the average horsepower for cars made by makers from Europe?'}], 'ideal': "SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE continents.Continent = 'Europe'"}
{'input': [{'role': 'system', 'content': 'TASK: Answer the following question with syntactically correct SQLite SQL. The SQL should be correct and be in context of the previous question-answer pairs.\nTable car_makers, columns = [*,Id,Maker,FullName,Country]\nTable car_names, columns = [*,MakeId,Model,Make]\nTable cars_data, columns = [*,Id,MPG,Cylinders,Edispl,Horsepower,Weight,Accelerate,Year]\nTable continents, columns = [*,ContId,Continent]\nTable countries, columns = [*,CountryId,CountryName,Continent]\nTable model_list, columns = [*,ModelId,Maker,Model]\nForeign_keys = [countries.Continent = continents.ContId,car_makers.Country = countries.CountryId,model_list.Maker = car_makers.Id,car_names.Model = model_list.Model,cars_data.Id = car_names.MakeId]'}, {'role': 'user', 'content': 'What is the average horsepower for cars made in the USA?'}], 'ideal': "SELECT AVG(cars_data.Horsepower) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN car_makers ON car_names.MakeId = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId WHERE countries.CountryName = 'USA'"}

Next we need to create the eval registry to run it in the framework.

The evals framework requires a `.yaml` file structured with the following properties:

* `id` - An identifier for your eval
* `description` - A short description of your eval
* `disclaimer` - An additional notes about your eval
* `metrics` - There are three types of eval metrics we can choose from: match, includes, fuzzyMatch

For our eval, we will configure the following:

"""
spider-sql:
  id: spider-sql.dev.v0
  metrics: [accuracy]
  description: Eval that scores SQL code from 194 examples in the Spider Text-to-SQL test dataset. The problems are selected by taking the first 10 problems for each database that appears in the test set.
    Yu, Tao, et al. \"Spider; A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task.\" Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, 2018, https://doi.org/10.18653/v1/d18-1425.
  disclaimer: Problems are solved zero-shot with no prompting other than the schema; performance may improve with training examples, fine tuning, or a different schema format. Evaluation is currently done through model-grading, where SQL code is not actually executed; the model may judge correct SQL to be incorrect, or vice-versa.
spider-sql.dev.v0:
  class: evals.elsuite.modelgraded.classify:ModelBasedClassify
  args:
    samples_jsonl: sql/spider_sql.jsonl
    eval_type: cot_classify
    modelgraded_spec: sql
  """""

'\nspider-sql:\n  id: spider-sql.dev.v0\n  metrics: [accuracy]\n  description: Eval that scores SQL code from 194 examples in the Spider Text-to-SQL test dataset. The problems are selected by taking the first 10 problems for each database that appears in the test set.\n    Yu, Tao, et al. "Spider; A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task." Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, 2018, https://doi.org/10.18653/v1/d18-1425.\n  disclaimer: Problems are solved zero-shot with no prompting other than the schema; performance may improve with training examples, fine tuning, or a different schema format. Evaluation is currently done through model-grading, where SQL code is not actually executed; the model may judge correct SQL to be incorrect, or vice-versa.\nspider-sql.dev.v0:\n  class: evals.elsuite.modelgraded.classify:ModelBasedClassify\n  args:\n    samples_jsonl: sql/spider_sql.jsonl\n    eval_type: cot_classify\n    modelgraded_spec: sql\n  '

## Running an evaluation

We can run this eval using the `oaieval` CLI. To get setup, install the library: `pip install .` (if you are running the [OpenAI Evals library](github.com/openai/evals) locally) or `pip install oaieval` if you are running an existing eval.

Then, run the eval using the CLI: `oaieval gpt-3.5-turbo spider-sql`

This command expects a model name and an eval set name. Note that we provide two command line interfaces (CLIs): `oaieval` for running a single eval and `oaievalset` for running a set of evals. The valid eval names are specified in the YAML files under `evals/registry/evals` and their corresponding implementations can be found in `evals/elsuite`.

!pip install evals --quiet

The `oaieval` CLI can accept various flags to modify the default behavior. You can run `oaieval --help` to see a full list of CLI options.

After running that command, you’ll see the final report of accuracy printed to the console, as well as a file path to a temporary file that contains the full report.

`oaieval` will search for the `spider-sql` eval YAML file in the `evals/registry/evals` directory, following the format specified in cell 4 above. The path to the eval dataset is specified in the eval YAML file under the args: parameter as `samples_jsonl: sql/spider_sql.jsonl`, with the file content in JSONL format (as generated in step 3 above).

After running that command, you’ll see the final report of accuracy printed to the console, as well as a file path to a temporary file that contains the full report.

!oaieval gpt-3.5-turbo spider-sql --max_samples 25

[2024-03-26 19:44:39,836] [registry.py:257] Loading registry from /Users/shyamal/.virtualenvs/openai/lib/python3.11/site-packages/evals/registry/evals
[2024-03-26 19:44:43,623] [registry.py:257] Loading registry from /Users/shyamal/.evals/evals
[2024-03-26 19:44:43,635] [oaieval.py:189] [1;35mRun started: 240327024443FACXGMKA[0m
[2024-03-26 19:44:43,663] [registry.py:257] Loading registry from /Users/shyamal/.virtualenvs/openai/lib/python3.11/site-packages/evals/registry/modelgraded
[2024-03-26 19:44:43,851] [registry.py:257] Loading registry from /Users/shyamal/.evals/modelgraded
[2024-03-26 19:44:43,853] [data.py:90] Fetching /Users/shyamal/.virtualenvs/openai/lib/python3.11/site-packages/evals/registry/data/sql/spider_sql.jsonl
[2024-03-26 19:44:43,878] [eval.py:36] Evaluating 25 samples
[2024-03-26 19:44:43,952] [eval.py:144] Running in threaded mode with 10 threads!
  0%|                                                    | 0/25 [00:00<?, ?it/s][2024-03-26 19:44:44,810] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:44,829] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:44,991] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:45,090] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:45,145] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:45,971] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:46,040] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:46,069] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:46,378] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:46,587] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:47,412] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
  4%|█▊                                          | 1/25 [00:03<01:23,  3.46s/it][2024-03-26 19:44:47,714] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
  8%|███▌                                        | 2/25 [00:03<00:36,  1.60s/it][2024-03-26 19:44:47,947] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 12%|█████▎                                      | 3/25 [00:03<00:21,  1.02it/s][2024-03-26 19:44:48,413] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:48,643] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 16%|███████                                     | 4/25 [00:04<00:18,  1.15it/s][2024-03-26 19:44:48,909] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 20%|████████▊                                   | 5/25 [00:04<00:12,  1.54it/s][2024-03-26 19:44:49,131] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:49,500] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:49,530] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 24%|██████████▌                                 | 6/25 [00:05<00:12,  1.56it/s][2024-03-26 19:44:49,962] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:49,964] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:49,967] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 28%|████████████▎                               | 7/25 [00:06<00:10,  1.73it/s][2024-03-26 19:44:50,577] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:50,602] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:50,634] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:50,862] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:51,503] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:51,608] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 40%|█████████████████▏                         | 10/25 [00:07<00:08,  1.79it/s][2024-03-26 19:44:51,801] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 44%|██████████████████▉                        | 11/25 [00:07<00:06,  2.09it/s][2024-03-26 19:44:51,856] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:51,969] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:52,227] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 52%|██████████████████████▎                    | 13/25 [00:08<00:04,  2.65it/s][2024-03-26 19:44:52,450] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:52,526] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:52,615] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 56%|████████████████████████                   | 14/25 [00:08<00:04,  2.64it/s][2024-03-26 19:44:52,625] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:52,777] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:53,653] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 60%|█████████████████████████▊                 | 15/25 [00:09<00:05,  1.87it/s][2024-03-26 19:44:53,670] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:54,028] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 68%|█████████████████████████████▏             | 17/25 [00:10<00:03,  2.54it/s][2024-03-26 19:44:54,388] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:54,396] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 72%|██████████████████████████████▉            | 18/25 [00:10<00:02,  2.58it/s][2024-03-26 19:44:54,529] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
[2024-03-26 19:44:54,585] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 76%|████████████████████████████████▋          | 19/25 [00:10<00:02,  2.94it/s][2024-03-26 19:44:54,980] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 80%|██████████████████████████████████▍        | 20/25 [00:11<00:01,  2.82it/s][2024-03-26 19:44:55,152] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 84%|████████████████████████████████████       | 21/25 [00:11<00:01,  3.27it/s][2024-03-26 19:44:56,420] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 88%|█████████████████████████████████████▊     | 22/25 [00:12<00:01,  1.75it/s][2024-03-26 19:44:56,984] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 92%|███████████████████████████████████████▌   | 23/25 [00:13<00:01,  1.76it/s][2024-03-26 19:44:57,370] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
 96%|█████████████████████████████████████████▎ | 24/25 [00:13<00:00,  1.94it/s][2024-03-26 19:44:59,589] [_client.py:1026] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
100%|███████████████████████████████████████████| 25/25 [00:15<00:00,  1.60it/s]
[2024-03-26 19:44:59,607] [record.py:360] Final report: {'counts/Correct': 20, 'counts/Incorrect': 5, 'score': 0.8}. Logged to /tmp/evallogs/240327024443FACXGMKA_gpt-3.5-turbo_spider-sql.jsonl
[2024-03-26 19:44:59,608] [oaieval.py:229] Final report:
[2024-03-26 19:44:59,608] [oaieval.py:231] counts/Correct: 20
[2024-03-26 19:44:59,608] [oaieval.py:231] counts/Incorrect: 5
[2024-03-26 19:44:59,608] [oaieval.py:231] score: 0.8
[2024-03-26 19:44:59,640] [record.py:349] Logged 75 rows of events to /tmp/evallogs/240327024443FACXGMKA_gpt-3.5-turbo_spider-sql.jsonl: insert_time=27.915ms

`oaievalset` expects a model name and an eval set name, for which the valid options are specified in the YAML files under `evals/registry/eval_sets`.

### Going through eval logs

The eval logs are located at `/tmp/evallogs` and different log files are created for each evaluation run.

log_name = '240327024443FACXGMKA_gpt-3.5-turbo_spider-sql.jsonl' # "EDIT THIS" - copy from above
events = f"/tmp/evallogs/{log_name}"
display(pd.read_json(events, lines=True).head(5))

|  | spec | final\_report | run\_id | event\_id | sample\_id | type | data | created\_by | created\_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | {'completion\_fns': ['gpt-3.5-turbo'], 'eval\_name': 'spider-sql.dev.v0', 'base\_eval': 'spider-sql', 'split': 'dev', 'run\_config': {'completion\_fns': ['gpt-3.5-turbo'], 'eval\_spec': {'cls': 'evals.elsuite.modelgraded.classify:ModelBasedClassify', 'registry\_path': '/Users/shyamal/.virtualenvs/openai/lib/python3.11/site-packages/evals/registry', 'args': {'samples\_jsonl': 'sql/spider\_sql.jsonl', 'eval\_type': 'cot\_classify', 'modelgraded\_spec': 'sql'}, 'key': 'spider-sql.dev.v0', 'group': 'sql'}, 'seed': 20220722, 'max\_samples': 25, 'command': '/Users/shyamal/.virtualenvs/openai/bin/oaieval gpt-3.5-turbo spider-sql --max\_samples 25', 'initial\_settings': {'visible': False}}, 'created\_by': '', 'run\_id': '240327024443FACXGMKA', 'created\_at': '2024-03-27 02:44:43.626043'} | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaT |
| 1 | NaN | {'counts/Correct': 20, 'counts/Incorrect': 5, 'score': 0.8} | NaN | NaN | NaN | NaN | NaN | NaN | NaT |
| 2 | NaN | NaN | 240327024443FACXGMKA | 0.0 | spider-sql.dev.88 | sampling | {'prompt': [{'content': 'Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct. Use only the following tables and columns: Table: players. Columns: player\_id (number), first\_name (text), last\_name (text), hand (text), birth\_date (time), country\_code (text) Table: matches. Columns: best\_of (number), draw\_size (number), loser\_age (number), loser\_entry (text), loser\_hand (text), loser\_ht (number), loser\_id (number), loser\_ioc (text), loser\_name (text), loser\_rank (number), loser\_rank\_points (number), loser\_seed (number), match\_num (number), minutes (number), round (text), score (text), surface (text), tourney\_date (time), tourney\_id (text), tourney\_level (text), tourney\_name (text), winner\_age (number), winner\_entry (text), winner\_hand (text), winner\_ht (number), winner\_id (number), winner\_ioc (text), winner\_name (text), winner\_rank (number), winner\_rank\_points (number), winner\_seed (number), year (number) Table: rankings. Columns: ranking\_date (time), ranking (number), player\_id (number), ranking\_points (number), tours (number) Question: Find the average rank of winners in all matches. ’, ‘role’: ‘system’}], ‘sampled’: [‘SELECT AVG(winner\_rank) AS average\_rank\_of\_winners FROM matches;’]} |  | 2024-03-27 02:44:44.821110+00:00 |
| 3 | NaN | NaN | 240327024443FACXGMKA | 1.0 | spider-sql.dev.82 | sampling | {‘prompt’: [{‘content’: ‘Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct. Use only the following tables and columns: Table: players. Columns: player\_id (number), first\_name (text), last\_name (text), hand (text), birth\_date (time), country\_code (text) Table: matches. Columns: best\_of (number), draw\_size (number), loser\_age (number), loser\_entry (text), loser\_hand (text), loser\_ht (number), loser\_id (number), loser\_ioc (text), loser\_name (text), loser\_rank (number), loser\_rank\_points (number), loser\_seed (number), match\_num (number), minutes (number), round (text), score (text), surface (text), tourney\_date (time), tourney\_id (text), tourney\_level (text), tourney\_name (text), winner\_age (number), winner\_entry (text), winner\_hand (text), winner\_ht (number), winner\_id (number), winner\_ioc (text), winner\_name (text), winner\_rank (number), winner\_rank\_points (number), winner\_seed (number), year (number) Table: rankings. Columns: ranking\_date (time), ranking (number), player\_id (number), ranking\_points (number), tours (number)   Question: Find the total number of matches. ’, ‘role’: ‘system’}], ‘sampled’: [‘SELECT COUNT(\*) AS total\_matches FROM matches;’]} |  | 2024-03-27 02:44:44.831848+00:00 |
| 4 | NaN | NaN | 240327024443FACXGMKA | 2.0 | spider-sql.dev.25 | sampling | {‘prompt’: [{‘content’: ‘Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct. Use only the following tables and columns: Table: continents. Columns: ContId (number), Continent (text) Table: countries. Columns: CountryId (number), CountryName (text), Continent (number) Table: car\_makers. Columns: Id (number), Maker (text), FullName (text), Country (text) Table: model\_list. Columns: ModelId (number), Maker (number), Model (text) Table: car\_names. Columns: MakeId (number), Model (text), Make (text) Table: cars\_data. Columns: Id (number), MPG (text), Cylinders (number), Edispl (number), Horsepower (text), Weight (number), Accelerate (number), Year (number)   Question: How many countries exist? ’, ‘role’: ‘system’}], ‘sampled’: [‘SELECT COUNT(\*) AS TotalCountries FROM countries;’]} |  | 2024-03-27 02:44:44.996647+00:00 |

# processing the log events generated by oaieval

with open(events, "r") as f:
    events_df = pd.read_json(f, lines=True)

This file will contain structured logs of the evaluation. The first entry provides a detailed specification of the evaluation, including the completion functions, evaluation name, run configuration, creator’s name, run ID, and creation timestamp.

display(events_df.iloc[0].spec)

{'completion_fns': ['gpt-3.5-turbo'],
 'eval_name': 'spider-sql.dev.v0',
 'base_eval': 'spider-sql',
 'split': 'dev',
 'run_config': {'completion_fns': ['gpt-3.5-turbo'],
  'eval_spec': {'cls': 'evals.elsuite.modelgraded.classify:ModelBasedClassify',
   'registry_path': '/Users/shyamal/.virtualenvs/openai/lib/python3.11/site-packages/evals/registry',
   'args': {'samples_jsonl': 'sql/spider_sql.jsonl',
    'eval_type': 'cot_classify',
    'modelgraded_spec': 'sql'},
   'key': 'spider-sql.dev.v0',
   'group': 'sql'},
  'seed': 20220722,
  'max_samples': 25,
  'command': '/Users/shyamal/.virtualenvs/openai/bin/oaieval gpt-3.5-turbo spider-sql --max_samples 25',
  'initial_settings': {'visible': False}},
 'created_by': '',
 'run_id': '240327024443FACXGMKA',
 'created_at': '2024-03-27 02:44:43.626043'}

Let’s also look at the entry which provides the final report of the evaluation.

display(events_df.dropna(subset=['final_report']).iloc[0]['final_report'])

{'counts/Correct': 20, 'counts/Incorrect': 5, 'score': 0.8}

We can also review individual evaluation events that provide specific samples (`sample_id`), results, event types, and metadata.

pd.set_option('display.max_colwidth', None)  # None means no truncation
display(events_df.iloc[2][['run_id', 'event_id', 'sample_id', 'type', 'data', 'created_at']])

run_id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                240327024443FACXGMKA
event_id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               0.0
sample_id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                spider-sql.dev.88
type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              sampling
data          {'prompt': [{'content': 'Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct.
Use only the following tables and columns:
Table: players. Columns: player_id (number), first_name (text), last_name (text), hand (text), birth_date (time), country_code (text)
Table: matches. Columns: best_of (number), draw_size (number), loser_age (number), loser_entry (text), loser_hand (text), loser_ht (number), loser_id (number), loser_ioc (text), loser_name (text), loser_rank (number), loser_rank_points (number), loser_seed (number), match_num (number), minutes (number), round (text), score (text), surface (text), tourney_date (time), tourney_id (text), tourney_level (text), tourney_name (text), winner_age (number), winner_entry (text), winner_hand (text), winner_ht (number), winner_id (number), winner_ioc (text), winner_name (text), winner_rank (number), winner_rank_points (number), winner_seed (number), year (number)
Table: rankings. Columns: ranking_date (time), ranking (number), player_id (number), ranking_points (number), tours (number)

Question: Find the average rank of winners in all matches.
', 'role': 'system'}], 'sampled': ['SELECT AVG(winner_rank) AS average_rank_of_winners
FROM matches;']}
created_at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                2024-03-27 02:44:44.821110+00:00
Name: 2, dtype: object

# Inspect samples
for i, row in events_df[events_df['type'] == 'sampling'].head(5).iterrows():
    data = pd.json_normalize(row['data'])
    print(f"Prompt: {data['prompt'].iloc[0]}")
    print(f"Sampled: {data['sampled'].iloc[0]}")
    print("-" * 10)

Prompt: [{'content': 'Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct.\nUse only the following tables and columns:\nTable: players. Columns: player_id (number), first_name (text), last_name (text), hand (text), birth_date (time), country_code (text)\nTable: matches. Columns: best_of (number), draw_size (number), loser_age (number), loser_entry (text), loser_hand (text), loser_ht (number), loser_id (number), loser_ioc (text), loser_name (text), loser_rank (number), loser_rank_points (number), loser_seed (number), match_num (number), minutes (number), round (text), score (text), surface (text), tourney_date (time), tourney_id (text), tourney_level (text), tourney_name (text), winner_age (number), winner_entry (text), winner_hand (text), winner_ht (number), winner_id (number), winner_ioc (text), winner_name (text), winner_rank (number), winner_rank_points (number), winner_seed (number), year (number)\nTable: rankings. Columns: ranking_date (time), ranking (number), player_id (number), ranking_points (number), tours (number)\n\nQuestion: Find the average rank of winners in all matches.\n', 'role': 'system'}]
Sampled: ['SELECT AVG(winner_rank) AS average_rank_of_winners\nFROM matches;']
----------
Prompt: [{'content': 'Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct.\nUse only the following tables and columns:\nTable: players. Columns: player_id (number), first_name (text), last_name (text), hand (text), birth_date (time), country_code (text)\nTable: matches. Columns: best_of (number), draw_size (number), loser_age (number), loser_entry (text), loser_hand (text), loser_ht (number), loser_id (number), loser_ioc (text), loser_name (text), loser_rank (number), loser_rank_points (number), loser_seed (number), match_num (number), minutes (number), round (text), score (text), surface (text), tourney_date (time), tourney_id (text), tourney_level (text), tourney_name (text), winner_age (number), winner_entry (text), winner_hand (text), winner_ht (number), winner_id (number), winner_ioc (text), winner_name (text), winner_rank (number), winner_rank_points (number), winner_seed (number), year (number)\nTable: rankings. Columns: ranking_date (time), ranking (number), player_id (number), ranking_points (number), tours (number)\n\nQuestion: Find the total number of matches.\n', 'role': 'system'}]
Sampled: ['SELECT COUNT(*) AS total_matches\nFROM matches;']
----------
Prompt: [{'content': 'Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct.\nUse only the following tables and columns:\nTable: continents. Columns: ContId (number), Continent (text)\nTable: countries. Columns: CountryId (number), CountryName (text), Continent (number)\nTable: car_makers. Columns: Id (number), Maker (text), FullName (text), Country (text)\nTable: model_list. Columns: ModelId (number), Maker (number), Model (text)\nTable: car_names. Columns: MakeId (number), Model (text), Make (text)\nTable: cars_data. Columns: Id (number), MPG (text), Cylinders (number), Edispl (number), Horsepower (text), Weight (number), Accelerate (number), Year (number)\n\nQuestion: How many countries exist?\n', 'role': 'system'}]
Sampled: ['SELECT COUNT(*) AS TotalCountries\nFROM countries;']
----------
Prompt: [{'content': 'Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct.\nUse only the following tables and columns:\nTable: TV_Channel. Columns: id (text), series_name (text), Country (text), Language (text), Content (text), Pixel_aspect_ratio_PAR (text), Hight_definition_TV (text), Pay_per_view_PPV (text), Package_Option (text)\nTable: TV_series. Columns: id (number), Episode (text), Air_Date (text), Rating (text), Share (number), 18_49_Rating_Share (text), Viewers_m (text), Weekly_Rank (number), Channel (text)\nTable: Cartoon. Columns: id (number), Title (text), Directed_by (text), Written_by (text), Original_air_date (text), Production_code (number), Channel (text)\n\nQuestion: What is the name and directors of all the cartoons that are ordered by air date?\n', 'role': 'system'}]
Sampled: ['SELECT Title, Directed_by\nFROM Cartoon\nORDER BY Original_air_date;']
----------
Prompt: [{'content': 'Answer the following question with syntactically correct SQLite SQL. Be creative but the SQL must be correct.\nUse only the following tables and columns:\nTable: stadium. Columns: Stadium_ID (number), Location (text), Name (text), Capacity (number), Highest (number), Lowest (number), Average (number)\nTable: singer. Columns: Singer_ID (number), Name (text), Country (text), Song_Name (text), Song_release_year (text), Age (number), Is_male (others)\nTable: concert. Columns: concert_ID (number), concert_Name (text), Theme (text), Stadium_ID (text), Year (text)\nTable: singer_in_concert. Columns: concert_ID (number), Singer_ID (text)\n\nQuestion: Show the name and the release year of the song by the youngest singer.\n', 'role': 'system'}]
Sampled: ['```sql\nSELECT s.Name, s.Song_release_year\nFROM singer s\nWHERE s.Age = (SELECT MIN(Age) FROM singer)\n```']
----------

Let’s review our failures to understand which tests did not succeed.

def pretty_print_text(prompt):
    # Define markers for the sections
    markers = {
        "question": "[Question]:",
        "expert": "[Expert]:",
        "submission": "[Submission]:",
        "end": "[END DATA]"
    
    # Function to extract text between markers
    def extract_text(start_marker, end_marker):
        start = prompt.find(start_marker) + len(start_marker)
        end = prompt.find(end_marker)
        text = prompt[start:end].strip()
        if start_marker == markers["question"]:
            text = text.split("\n\nQuestion:")[-1].strip() if "\n\nQuestion:" in text else text
        elif start_marker == markers["submission"]:
            text = text.replace("```sql", "").replace("```", "").strip()
        return text
    
    # Extracting text for each section
    question_text = extract_text(markers["question"], markers["expert"])
    expert_text = extract_text(markers["expert"], markers["submission"])
    submission_text = extract_text(markers["submission"], markers["end"])
    
    # HTML color codes and formatting
    colors = {
        "question": '<span style="color: #0000FF;">QUESTION:<br>', 
        "expert": '<span style="color: #008000;">EXPECTED:<br>',  
        "submission": '<span style="color: #FFA500;">SUBMISSION:<br>' 
    color_end = '</span>'
    
    # Display each section with color
    from IPython.display import display, HTML
    display(HTML(f"{colors['question']}{question_text}{color_end}"))
    display(HTML(f"{colors['expert']}{expert_text}{color_end}"))
    display(HTML(f"{colors['submission']}{submission_text}{color_end}"))

# Inspect metrics where choice is made and print only the prompt, result, and expected result if the choice is incorrect
for i, row in events_df[events_df['type'] == 'metrics'].iterrows():
    if row['data']['choice'] == 'Incorrect':
        # Get the previous row's data, which contains the prompt and the expected result
        prev_row = events_df.iloc[i-1]
        prompt = prev_row['data']['prompt'][0]['content'] if 'prompt' in prev_row['data'] and len(prev_row['data']['prompt']) > 0 else "Prompt not available"
        expected_result = prev_row['data'].get('ideal', 'Expected result not provided')
        
        # Current row's data will be the actual result
        result = row['data'].get('result', 'Actual result not provided')
        
        pretty_print_text(prompt)
        print("-" * 40)

QUESTION:  
How many countries have a republic as their form of government?

\*\*\*\*\*\*\*\*\*\*\*\*

EXPECTED:  
SELECT count(\*) FROM country WHERE GovernmentForm = “Republic”
\*\*\*\*\*\*\*\*\*\*\*\*

SUBMISSION:  
SELECT COUNT(\*)
FROM country
WHERE GovernmentForm LIKE ‘%Republic%’

\*\*\*\*\*\*\*\*\*\*\*\*

----------------------------------------

QUESTION:  
Return the document id, template id, and description for the document with the name Robbin CV.

\*\*\*\*\*\*\*\*\*\*\*\*

EXPECTED:  
SELECT document\_id , template\_id , Document\_Description FROM Documents WHERE document\_name = “Robbin CV”
\*\*\*\*\*\*\*\*\*\*\*\*

SUBMISSION:  
SELECT Documents.Document\_ID, Documents.Template\_ID, Documents.Document\_Description
FROM Documents
JOIN Templates ON Documents.Template\_ID = Templates.Template\_ID
WHERE Documents.Document\_Name = ‘Robbin CV’;

\*\*\*\*\*\*\*\*\*\*\*\*

----------------------------------------

QUESTION:  
Which professionals live in the state of Indiana or have done treatment on more than 2 treatments? List his or her id, last name and cell phone.

\*\*\*\*\*\*\*\*\*\*\*\*

EXPECTED:  
SELECT professional\_id , last\_name , cell\_number FROM Professionals WHERE state = ‘Indiana’ UNION SELECT T1.professional\_id , T1.last\_name , T1.cell\_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional\_id = T2.professional\_id GROUP BY T1.professional\_id HAVING count(\*) > 2
\*\*\*\*\*\*\*\*\*\*\*\*

SUBMISSION:  
SELECT professional\_id, last\_name, cell\_number
FROM Professionals
WHERE state = ‘Indiana’
OR professional\_id IN (
SELECT professional\_id
FROM Treatments
GROUP BY professional\_id
HAVING COUNT(\*) > 2
);
\*\*\*\*\*\*\*\*\*\*\*\*

----------------------------------------

QUESTION:  
What is the continent name which Anguilla belongs to?

\*\*\*\*\*\*\*\*\*\*\*\*

EXPECTED:  
SELECT Continent FROM country WHERE Name = “Anguilla”
\*\*\*\*\*\*\*\*\*\*\*\*

SUBMISSION:  
SELECT c.Continent
FROM country c
WHERE c.Code = ‘AIA’;

\*\*\*\*\*\*\*\*\*\*\*\*

----------------------------------------

QUESTION:  
How many airlines do we have?

\*\*\*\*\*\*\*\*\*\*\*\*

EXPECTED:  
SELECT count(\*) FROM AIRLINES
\*\*\*\*\*\*\*\*\*\*\*\*

SUBMISSION:  
SELECT COUNT(DISTINCT Airline) AS TotalAirlines
FROM airlines;
\*\*\*\*\*\*\*\*\*\*\*\*

----------------------------------------

Reviewing some of the failures we see the following:

* The second incorrect answer had an unnecessary join with the ‘Templates’ table. Our eval was able to accurately identify this and flag this as incorrect.
* Few other answers have minor syntax differences that caused the answers to get flagged.
  + In situations like this, it would be worthwhile exploring whether we should continue iterating on the prompt to ensure certain stylistic choices, or if we should modify the evaluation suite to capture this variation.
  + This type of failure hints at the potential need for model-graded evals as a way to ensure accuracy in grading the results

# Conclusion

Building out effective evals is a core part of the development cycle of LLM-based applications. The OpenAI Evals framework provides the core structure of building evals out of the box, and allows you to quickly spin up new tests for your various use cases. In this guide, we demonstrated step-by-step how to create an eval, run it, and analyze the results.

The example shown in this guide represent a straightfoward use case for evals. As you continue to explore this framework, we recommend you explore creating more complex model-graded evals for actual production use cases. Happy evaluating!
