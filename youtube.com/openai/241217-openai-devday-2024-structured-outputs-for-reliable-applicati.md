---
title: "OpenAI DevDay 2024 | Structured outputs for reliable applications"
channel: openai
url: https://www.youtube.com/watch?v=kE4BkATIl9c
youtube_id: kE4BkATIl9c
published: 2024-12-17
duration: "40:39"
captions: en
---

# OpenAI DevDay 2024 | Structured outputs for reliable applications

[![OpenAI DevDay 2024 | Structured outputs for reliable applications](https://img.youtube.com/vi/kE4BkATIl9c/hqdefault.jpg)](https://www.youtube.com/watch?v=kE4BkATIl9c)

<details>
<summary>자막: OpenAI DevDay 2024 | Structured outputs for reliable applications (40:39)</summary>

[00:00]
♪♪
[ Applause ]
-Hi there.
-Hello everyone.
We're here to talk about
structured outputs,
an exciting new future
we shared in OpenAI API
in August this year.
It's been a huge unlock for
developers, working with LLMs.
And in just a few short weeks,
hundreds of thousands
of developers
have integrated it
into their applications.
My name is Atty Eleti
and I lead API design at OpenAI.
-And I'm Michelle Pokrass
and I'm the Tech Lead here
for the API.
Today we're going to talk
about three things.
First, we're going to tell you
why you need structured outputs
and we'll talk about
how the feature works
and finally we'll tell you
how we built it under the hood.
So, let's get right into it.
-Let's start at the beginning.
The year is 2020 and OpenAI
has just launched GPT-3.

[00:01]
GPT-3 can write emails,
draft blog posts
and generate movie scripts.
It was great
for text generation.
Quickly, developers, all of you,
started to find
some exciting new applications
for this technology.
From generating
end game scripts like AI Dungeon
or drafting marketing materials
like copy.ai.
Fast forward three years,
in 2023, we launched GPT-4.
A new breakthrough
in LLM intelligence.
For the first time, models were
capably of advanced reasoning,
following complex instructions,
extracting information
from long documents
and taking action
on behalf of users.
Developers took it
to the next level,
from building AI powered
productivity tools like CURSOR.
Customer service agents
like Klarna and language
learning apps like Duolingo.
All of these products
had one thing in common,
they were connecting LLMs
to the outside world.

[00:02]
From your code base, to external
APIs or on device actions.
To do this,
they needed outputs to
be structured, typically JSON.
Here's an example,
let's say you're building
a personal assistant
and you want to convert the
users message into an API call.
The user might say,
play the Beatles.
Here's what you expect,
you want a JSON object,
that says play music for the API
and the Beatles for the artist.
But too often here's
what you get.
The middle begins
with a preamble saying, sure,
hers the JSON,
to call the play music API.
Now this isn't particularly
helpful for developers,
since we need just the JSON,
not the text surrounding it.
This is a problem.
LLM outputs are
not always reliable,
making it hard to integrate
them into your acts.
Now as developers
we're tried all kinds
of tricks to solve this.

[00:03]
Some of you may have
written prompts like this.
Or even this.
Now, sometimes it works
and sometimes you have to go
all the way
and write a custom
markdown parser.
That's obviously not
how it should work.
So, to solve this problem
in June last year,
we launched function calling.
It lead the way to define tools
the model can call
using JSON schema.
You define the schema
of the function
and the model outputs JSON
adhering to it.
Unfortunately function calling
wasn't perfect.
Sometimes the model
would output invalid JSON,
such as
by adding a trailing comma.
We've all done that before.
So in November at DevDay
last year we launched JSON mode.
JSON mode ensures
valid JSON outputs.
So you never see
another pressing error.
But this still wasn't enough.
The model could output
the wrong type,

[00:04]
like a string instead of
a float, as you see here.
Or hallucinate a parameter
entirely.
This cat and mouse
game to get reliable outputs
can be really frustrating.
Fundamentally, AI applications
need reliable outputs.
So, to solve these problems once
and for all,
we introduced structured outputs
to the API in August.
Here's Michelle
to tell you more.
-So structured outputs is
a new feature designed to ensure
that middle generated outputs
will exactly match
JSON schemas supplied by you,
developers.
You can think
of structured outputs
as the difference
between suggesting to the model
to use your schema
and to constraining.
You don't have to ask
nicely anymore
and you can just supply
the JSON schema that you need.
And you might be wondering,
if this is the right solution
that finally solves the problem,
why did it take us so long
to get here?
And the answer is twofold.

[00:05]
First, we still believe
that function calling
is often the right abstraction
for this functionality
and then finally,
it actually took us a
little while to build a solution
that is performant
for inference at scale,
while constraining your outputs.
So we're going to talk
a little bit more later
about the engineering
and research
we undertook to make this work,
but for now, let's talk about
how you can use it.
So structured outputs is
available
in two modes in the API.
The first is function calling,
as Atty just showed you.
And you're probably
already familiar with it.
This feature always our models
to generate parameters
for your tool calls
and it allows developers
to connect LLMs
with functionality
in their applications.
The second mode is
the response format parameter.
This parameter is useful when
the model is responding directly
to a user, rather than emitting
a function call.
So let's start
with function calling.
If you've use it before,
you're probably pretty familiar
with the format of a request

[00:06]
that you see here.
You can see we're supplying a
JSON schema in the tool section,
and there's parameters
for the function.
This tells the model how to call
our tool and in our case,
the function is called
get weather
and it has two parameters,
location and unit.
So location is a string type
and so is unit,
but it's actually limited
to just a few fields
with the enum parameter.
When you supply a function
like this in our API,
our systems will show the model,
this spec,
and it will use that information
to generate tool calls
when it's appropriate.
Enabling structured outputs here
is really easy.
With just one like of code
I can set strict to true,
and this will enable
structured outputs.
This will use
the supplied schema
and always make sure the model's
response will follow it.
So, that's structured outputs
in function calling.
Now let's look at a quick
example in the playground.

[00:07]
And before we get into it,
I'll tell you a little bit
about a startup I'm building.
So, I'm actually building
an AI glasses product.
They're pretty hot right now.
They're really futuristic
and they're built
on the Open AI API.
These glasses have
a speaker in the stem
to read the answers
out from the assistant
and there's actually a little
AR screen for the glasses.
I actually want to make
an internal admin dashboard
to help my team answer questions
about orders that we've received
and you know,
what their shipping status is.
So I actually already have a
database with order information
and I want to connect this
assistant to that information.
So, let's get started
in the playground.
So I've actually
already created a query function
to tell the assistant
how to query my SQL database.
Let's take a quick look.
So, here's my function,
it's called query.
And it has kind of the
properties that you'd except.

[00:08]
So the first is table name
and we only had one table name,
orders, that's all
we support so far.
Then we have all
of the columns of my table.
So these are just straight
from my database.
And then you know, the meat
of this is the conditions
that we support for querying.
So, you'll notice here
that we have some operators.
My database supports equals,
greater than,
less than, and nonequals.
And then we have like
an order by.
So just stuff
you'd expect for a database.
When I use the assistant
I'll set the system message
to tell it today's date,
so it can be useful
and then a user comes in
and they're asking
to find all of the orders
shipped September 1st or later.
So let's give this a quick go.
Alright, you can see
we've got a function call back
and it looks pretty good.
I mean, the logic is right.
We're checking that shipped at
is greater than
or equal to September 1st.
But the discerning developer
will notice
that this will likely cause
your application to blow up.

[00:09]
And the reason for that is that
we're using the greater than
or equal to operator.
However, our ORM for some reason
only supports these operators
and so the greater than
or equal to will just not work.
With structured outputs,
we can set strict to true
and this will constrain
the model to only use
what you've provided.
So let's save that and retry.
Awesome!
You can see this time
we've actually used the greater
than operator and the models
done in the logic to determine,
we actually need to check
that we're greater
than the last day of August,
and not greater than or equal
to the first day of September.
So through this you can see
how structured outputs will
just eliminate a whole class
of errors for your application.
Now, let's get back to
response formats.
So in the past when you wanted
the model to respond using JSON,
you would be using JSON mode.
So, back to my
AI glasses startup.

[00:10]
Since they've got a speaker
in the stem,
I want them to read some of
the assistants response out loud
and I want to show a summarized
version in the lenses.
Before structures outputs,
I would actually just put
these instructions
into the system message
and use JSON mode.
This is pretty nice,
I would always get back JSON.
But, sometimes if the user
asked for something specific,
I would get back an extra key
or the model will,
you know, use the wrong type.
With structured outputs,
I can move these instructions
into the response format
parameter,
like you see here.
I'm going to use
the description to explain
to the model how to respond,
with the voiceover and display
parameters.
So this way the model
will always follow the format
and use these two keys.
So, let's give this
a quick go as well.
Alright, I have another tab here
and I've actually created
that schema,
so let's take a quick look.
So voiceover is our
first string property

[00:11]
and we're telling the assistant,
this will be read aloud via TTS.
And to write
out numbers and acronyms fully.
Then we have the display
property and this is,
you know, we don't have a ton
of room on the glasses,
so we're going to keep
this tight, just five words.
So I'm going to put this
into the playground,
you can see on the right here we
have the response format option.
I'm going to paste in my schema
and you'll see
that strict is set to true,
so structured outputs is on.
Now I'm going to test out
the glasses with a,
you know, typical query.
I might ask something like,
how tall is a giraffe?
When I run this,
you see that I get the output
in the form I've asked for.
So we have
the voiceover parameter,
which has spelled
out the words to make it easier
for our TTS models
to read them out.
We also have the display field,
which is just four words,
which should fit right
on the glasses.
So there you have structured
outputs with response formats.
This is just a
really quick demo,
but Atty's get into something
a little more interesting.

[00:12]
-Okay.
So, that showed us the feature,
but let's get into
some more interesting demos
and how you might use structured
outputs in your applications.
Let's imagine we're building
a fictitious company
called Convex.
Convex is an AI powered
recruiting tool.
It lets recruiters create
job postings,
submit referrals
and schedule interviews.
Behind the scenes,
Convex is a node and react app,
that uses response formats to
extract information from resumes
and uses function calling
to perform queries
over the candidate data.
Let's see it in action.
So, I've gone ahead
and created a job posting
here for an ML Engineer role
that we're hiring at Open AI.
And you can see
the job description,
the hiring manager
and someone of the candidates
that have already applied.
Now before I came on stage,
a promising candidate reached
out to me and shared his rSum.
Let's take a look.

[00:13]
Okay, Greg seems
to have a good Stripe
and has a little bit
over experience working in AI.
He has a whole bunch of skills
including coding and Python,
so seems like
a promising candidate.
Let's put it in a folder.
So, I'm going to go click in
the add candidate button here.
And select Greg's rSum
and you can see
that we're outputting the fields
from the rSum in real time.
The model is use
structured outputs
to extract this information from
the text that's within the PDF.
Let's take a look at the models
response behind the scenes.
So we see a JSON object,
with name, title, location,
contact information,
work experience,
all of this has been
extract from the rSum.
Now, let's take a look at the
code to see how this all works.
So, behind the scenes
we're using the response
format called, resume.

[00:14]
It has the fields we just saw,
like name, title,
location and so on.
And particular
for work experience,
you'll notice
that I'm using an array.
So, structured outputs supposed
to say wise subset
of JSON schema,
including arrays.
That allows the model to output
more than one work experience.
Now, some
of the JavaScript developers
in the room might also notice
that I'm using the library Zod,
to define my schema.
Zod is great.
It lets me define my schemas
in code
and get run time type safety.
The Open AI node SDK has
native support for Zod.
You can define your schemas
in it
and when the model starts
responding,
we parse the response back
into the Zod object as well,
and it supports streaming.
Very similarly the OpenAI Python
SDK supports Pydantic natively.
Okay, so let's add one
more field to the format here.
Let's add the GitHub user name.
So I'm going to go save that,

[00:15]
refresh my page, and
let's add it for one more time.
Great, the models responding
and you can see
that the GitHub user name
was also extracted.
Okay, so that was the
first feature I wanted to demo,
which is extracting information
from unstructured data
using response formats.
Next, let's see how
we can use structured outputs
in function calling.
So I'm going to go
click view all here
to open my candidate
analysis screen
and I have a helpful
AI assistant here
that I can ask questions
to analyze my data.
Now we'll see
that candidates have applied
from all over the country
in San Francisco and
New York and Austin,
but for this role
we're hiring in the SF office,
so let's filter
the candidates down.
I'm going to say filter
the candidates to those based
in San Francisco,
let's press enter.
And we see that the model called
the find candidates function,

[00:16]
with a criteria field.
The field is location
and the value is San Francisco.
And this hit our back in API
and it returned a list
of candidates that were filtered
and are based in SF.
We also noticed
that the UI on the left
has been updated
to reflect these candidates.
In this way
you can use function calling
to control the UI
of your application.
Let's look at this
behind the scenes.
So in our code
I've defined a tool
or a function called,
find candidates.
Find candidates has a schema
that includes a list of criteria
and each criteria has a field,
so that can be title,
location and so on and a value,
which is the value to filter on.
So that was a quick one
on one example
of using structured outputs
with function calling.
Let's try something harder.
Let's say graph these candidates
by years of experience.

[00:17]
You'll notice
that the model is generating UI,
a card with a header
and a bar graph
that shows all the candidates
and their years of experience,
a table with the rows as well.
Now this is not a prebuilt UI.
This is actually
the model composing a set
of react components dynamically.
We can look at the schema here
as well.
We see that the
top level properties component
and it says card and card
has a list of children,
that includes a header,
a bar chart and so on.
Here's how the schema
is defined behind the scenes.
We have a tool called
generate UI.
And generate UI has
one property called, component.
Component is an any of --
of card, header,
bar chart and so on.
And each of these schemas
is defined later on
in the defs parameter.
Now this is a really interesting
feature of structured outputs,
where you can actually use
defs to define your schemas
in one place
and use them multiple times
and you can use recursive
schema definitions as well.

[00:18]
So you'll notice that the card
schema here has a children,
which then references
component again.
So in this way a component
can have a list of children
that are components
and structured outputs
handles this
with no problem at all.
Great, so now that we have
candidates sorted
by years of experience,
let's go ahead
and schedule some interviews.
So I'm going to say,
schedule interviews
for the candidates with,
let's say for the top
three candidates,
by years of experience
with Michelle and Olivier.
So what this is going to do
is first go
and check the availability
of Michelle and Olivier
on their calendars.
Once it picks out
a few good slots
it's going to schedule
those interviews
and finally it's
going to email the candidates
that their interviews
have been booked.
So let's press enter. Awesome.
So we see
that the models calling
the fetch availability API
and got some data back,
it's now calling
the scheduled interviews API

[00:19]
and that succeeded.
And finally it's called
send emails,
with custom emails
for each candidate
and that succeeded as well.
So that's an example
of a multistep workflow,
using function calling.
Where each step benefits
from structured outputs.
Before this feature,
if any one of these steps
failed,
the whole workflow would fail.
And in production,
if one of these
had let's say a 1% error rate,
the workflow would have
an approximately 3% error rate.
You can see how important
structured outputs is
for reliability
of agentic workflows.
Okay, so that's a little demo of
how you can use
structured outputs
and real world applications.
You can use response formats
to extract information
from unstructured data.
You can use function calling
to generate UI.
And finally,
you can build agentic workflows
with 100% reliability.
To tell you about
how all of this
works under the hood,
here's Michelle.
[ Applause ]
-Thanks, Atty.
Super cool, and can't wait
to interview Greg later.

[00:20]
Let's get into how structured
outputs works under the hood.
We're going to talk
about three things.
We're going to talk about
the engineering implementation,
the research we undertook to
make our models better at format
following, and then finally some
of the interesting API
design decisions
we made to ship this feature.
To ship this,
we actually decided to take
an approach that combined
both research and engineering,
to create a holistic solution.
Doing just one of these would
make a pretty good product,
but together they are greater
than the sum of their parts.
There's actually more
to structured outputs
than just prompting
our models differently.
It creates some interesting
tradeoffs for developers,
so we thought it would be useful
to take you under the hood,
under those choices.
On the engineering side,
we decided to take an approach
known as constrained decoding,
to ensure that our models
would also follow schemas
supplied by developers.
And there's three components
of constrained decoding

[00:21]
that we're about to talk about.
The first is LLM inference,
how that works.
Then we're going to get into
token masking
and finally, we're going to talk
about the subset of JSON schema
that we support,
all of those grammars.
So let's start
with LLM inference.
LLMs operate on tokens,
which is the vocabulary
of a large language model.
This is all of the labels that
the model can output or produce.
So, let's get into
a simple example of a model
to show a small vocabulary.
This is the classic example
of an AI model.
So it's a digit recognition
model.
I want to train a model to
recognize this handwritten three
and determine what digit it is.
So the vocab of this model
is just going to be 10 labels,
the digits zero through nine.
And this is actually what a
model like that would look like.
So first we convert
our input into some sort of
computer representation
and in this case,
we're going to take every pixel
from my handwritten three
and feed that into the model.

[00:22]
Then we have the inner layers
of the model,
and then finally at the end,
the model is producing 10 values
and these are the predictions
of our labels from zero to nine.
You can actually see here
that the digit three
has a 97% probability, so
this digit is probably a three.
This is also how large language
models work for inference
in pretty broad strokes.
Rather than predicting
the digits zero through nine,
large language models predict,
you know, language.
In order to do this
they use labels
that represent language,
and one of the best ways
we found for doing this
is to use tokens.
Tokens are like words or word
fragments.
And here we have some English
text broken up into its tokens.
This is actually the text
from our blog post
and you can see
that the taken boundaries vary.
Sometimes they're an entire word
like the word "the"
or sometimes they're
a word fragment like "struct."

[00:23]
These tokens make up
the vocabulary
of large language models
and at any point the model
can product any of these,
they're all valid.
So this is
unconstrained decoding,
where there's no constraints
on what can be produced.
What you see on the screen
are actually some
of the real tokens
in the GPT-4 tokenizer.
So, there's all kinds
of parts of speech,
like individual characters,
so the exclamation point,
to full words like
"conveyer" at the bottom here.
Now let's say we're using
structured outputs
to generate an output
with this schema.
So, this schema has
a single property, value,
and that's a number type.
And we're part way
through our generation already,
so we've produced a curly brace,
some white space,
and then value.
By default,
when we sample, any token
from the vocab can be chosen.
So that can be a string
or a Boolean.
But if we did produce a Boolean
that would not match the schema,

[00:24]
so and a number like 42
would be valid.
So this tells us
that we actually need to limit
which tokens can
be produced next
and we can't just have
the entire vocab of the model.
To do this we will use a
technique known as token masking
and this constrains the tokens,
which can be picked
at the very end of sampling.
So, back to our digit example.
Here's an example
of taken masking,
let's say I have some side info
about these numbers.
I know that they're
all prime for some reason
and so I wouldn't
want to decode, you know, zero,
one, four, six,
any of the non-prime numbers.
So this is actually
what I would do.
I would kind of mask out
any of those predictions.
So what we do after
we generate their probabilities
with a for pass,
is then remove any labels
that are not supplied,
so that we will only sample
from a valid token.
This is known as masking
and we're effectively
ignoring any values

[00:25]
that we don't want to
be produced.
Large language models are
autoregressive
and that means they produce
output one token at a time.
Each time we sample a token,
that output is fed back in right
as input,
for the next inference step.
This means when sampling JSON
for your schemas,
we actually need to update
the masked tokens
at every step of inference
and we can't just do it once
at the beginning of the request.
And if that's not making sense,
look at this example.
So you can see, first, we're
allowing the curly brace token
and then once we sample it,
in step two,
you actually no longer see
the curly brace in the mask.
So you can see
that from step to step
we need to update these masks.
Because this is happening
at every inference step,
we need this operation
to be super, super fast.
At the scale that some
of your apps run,
you know, we need to make
things lightning fast
and keep inferences as fast
as possible.

[00:26]
So, you probably
already know this,
but token sampling happens
on a GPU.
And we actually do it
one batch at a time.
For each batch,
we calculate probabilities
for everything in that batch
and then we'll apply
any token masks
and then we'll sample from that
final probability distribution.
And that sampling is right here
in the orange segments.
So as you can see here,
we can actually calculate
the probabilities
and determine the masks
in parallel
and this frees up
precious GPU resources,
because we can do
the mask determination on CPU.
This is very helpful
for us to keep things fast.
You'll also notice
that we need the mask to happen
at about the same amount of time
as calculating
the probabilities.
And this is also known
as the time between tokens
and it varies based
on the size of the model.
And so we need to keep this
under even something
like 10 milliseconds.
So a naive solution
to this problem
would involve determining
these valid tokens

[00:27]
from the current state,
at every step of inference.
But like we said,
we have 10 milliseconds
so we're not super likely
to meet that budget.
So we want it to pre-compute
as much work as possible
and then reuse it when sampling
to make mass computation
more like a lookup
and less like a lot of work.
And just like you can build
an index in your SQL database
to speed up queries,
we can actually
build up an index
with the specific JSON schema
that you supply
to make fetching these masks
very fast during inference.
There's actually a lot of work
that goes into producing
this index from the JSON schema.
First, we convert
the JSON schema into a grammar.
And a grammar is actually
a formal specification
of a language.
Once we have the grammar,
we can create a parser.
And a parser is a program
that can check strings
and see if they're part
of this language.
You can think of the parser
as a program

[00:28]
that takes in a JSON blob
and tells you,
does that match the schema
or not?
Finally, once we have a parser,
we can iterate over all
of the tokens in our vocabulary
and all of the states
that are possible in the parser,
and this will determine
which tokens are valid.
This work lets us build
an index.
Our index is actually a tree,
which is a prefixed base
data structure
that allows for
O(1) lookups.
So, during inference
we're running our parser,
building up some states
and then every time
we'll traverse this tree
to find the leaf.
The leaf node will tell us what
the mask is for the next step.
Generating this index is pretty
computationally expensive.
We have to go over all
of the possible states.
So we do it just once
and then we cache it
later for fast look ups.
This is why the first query
to structured outputs
can take a little time,
usually under 10 seconds.

[00:29]
And then the following
queries are just as fast
as you normally expect.
Finally, let's talk about
the kinds of grammars
we support with
structured outputs.
A common approach
in the open source community
is using regular expressions
for determining token masks.
And this approach works
quite well for simple
or depth limited schemas.
So, for example, you
can imagine a regular expression
for our value schema
from before.
It's actually a
pretty tractable implement
with a regular expression,
which we have here.
And this regular expression has
about what you'd expect.
First we have the curly brace
and then we have
some white space, then value
and then finally a regular
expression for number types.
However you actually
can't implement all
of the expressiveness with JSON
schema with regular expressions.
They're missing basically
the memory needed to store
information about pass lookups.
So let's talk about
why that's important.

[00:30]
Here's an example of a recursive
schema from our blog post.
So this schema is useful
for generative UI
and it's kind of like what Atty
showed you just now as well.
Each component can have
a list of children
and those must also
themselves match the schema
at the top level.
So you can see the schema here
uses the ref paren
to reference the parent.
And there's actually no way
to implement a regular
expression to validate this,
because of the potential
of recursive nesting.
This is just
a fundamental limitation
of regular expressions,
because they don't have
arbitrary memory
to encode information
about past outputs.
To make this easier to grok,
here's a really simple example
of a language.
Our language is defined
as all of the strings
that have matching open
and close parens
and you can see we have
a quick example here
where all parentheses are
matches.
This is something
that's so easy to explain,
but it's not possible
to implement

[00:31]
with a regular expression.
And to show you why,
there's actually two attempts
we have here to do so.
So the first one is very simple,
we just allow arbitrary open
and closed parens.
But it's pretty clear
why this won't work,
you can have one open
and two closed parens.
So it doesn't validate
our language,
we're kind of missing the memory
of what happened before.
Our other attempt here is much
more complicated and it works,
but only up to three layers
of nesting.
We go further than that,
the regular expression
doesn't behave properly.
This is just a toy example,
but we believe that recursive
and deeply nested
schemas are often critical
for developers,
so we really wanted to find
a way to support them.
We can do so by adding
in a stack
and this gives us the memory
we need to encode information
about past outputs.
So this stack will let us
keep track of things like,
how many open parens
have I seen before?
This approach is known
as the CFG,

[00:32]
or context free grammar
approach.
It's a little trickier
to implement
but it allows
for far more expressiveness.
This is the approach
that we went with and it's
why it takes a little bit
of time
to build up this tree
for inference.
It's also why we support
recursion in deep nesting.
So, that's the engineering side
of structured outputs.
We just talked about
how LLM inference works,
why token masking is
a useful building block
and how this all comes
together in the extensive subset
of JSON schema that we support.
We believe
that this implementation results
in the greatest set
of trade outs for developers.
We've kept inferences
as fast as possible
and we supported a very wide
subset of JSON schema.
And we believe the tradeoff
of waiting a little longer,
that first request
while you're developing,
is worth it for most developers.
So now let's get into
how we've actually improved
our models with research

[00:33]
to work with structured outputs.
-Awesome.
[ Applause ]
Thank you, Michelle.
So that was a little bit
of the engineering
behind structured outputs.
Next let's talk about
the research side.
On the research side
we wanted to ship a model
that was much better at
following formats as specified.
It's not enough
to just constrain the model
to a valid output,
if those outputs are
out of distribution
or low probability
for the model.
Because the model
will often behave erratically.
Some of you may have seen this
as the infinite
new line problem before.
This happened with some
of our older models
that weren't trained
on response formats.
The models natural
inclination was to generate text
that works in JSON,
but because it was
being forced to output JSON,
the only valid
sufficiently probably token
was the new line character.
So the model would distribute
the new line token,
one after another, all the way
until it hits max tokens.
So, we wanted to avoid
this problem

[00:34]
so we specifically trained the
models to understand JSON schema
and in particular,
complex schemas better.
It's also not enough
for the model
to just understand the schema,
it needs to know what
the quality of that field is.
There's a semantic meaning
behind the keys.
For example, consider
this action item schema.
Each action item has
a description,
a due date and an owner.
To produce a good output,
it's not enough to know
that a description is a string
and the owner is a string.
The model needs to know
what kind of string
goes into a description and what
kind of string goes into owner.
So, to ensure
the models are good at this,
we train them with a whole bunch
of complex schemas,
including nested schemas.
So here are the results
from our training process.
This graph shows our models
on the x-axis
and their accuracy on one
of our evals on the y-axis.
The first three bars
from the left are GPT-4,
GPT-4 turbo
and the original GPT-4o.

[00:35]
You can see that accuracy
improved from about 26% to 86%
over the last year.
Now at the very end here,
you see the results
for our latest model.
The orange bar shows the models
results with just prompting
and it has an accuracy of 85%.
When you add in the
newly trained response format,
we see that the yellow bar,
the accuracy improves to 93%.
This is much better,
but still not 100%.
So to get to 100%, we can enable
constrained decoding,
as Michelle shared earlier,
giving us a perfect score
on the green bar.
So in this way, combining
research to improve the model,
with engineering to implement
constrained decoding,
brings out the
best possible results.
Okay, finally let's get into
some interesting design
tradeoffs we made
when creating this feature.
We'll talk about three things,
additional properties,
required properties
and the order of properties.
Let's start
with additional properties.
So one of the controversial API
design decision we had to make,

[00:36]
was deciding what
to do with properties
that were not defined
in the schema.
By default, JSON schema
always extra properties,
so all additional properties
are always allowed.
Now this is generally
not the behavior
we as developers expect.
You can imagine errors
like this,
where we have a function,
get weather,
that accepts two arguments.
If the LLM produces
an extra argument,
we get a run-time error.
So, we decided to disallow
additional properties
by default in the OpenAI API.
That said, this meant
the default in our API
was different
than the default in JSON schema,
that's not great especially
if the developer
already has a predefined schema
from elsewhere
in their application.
In general one
of our API design principles
is we prefer to explicit
rather than implicit.
So we decided to require
that developers have to parse
in additional properties false
in their schemas.
This makes the API
a little bit harder to use,
it means you have to set
this property every time,

[00:37]
but it sets expectations
better with developers.
Okay, let's talk about
required properties.
By default, in JSON schema,
all properties are optional.
This is, again, not what we
as developers expect.
To go back
to our earlier example
of the get weather function,
if the LLM decided
to skip one of the promoters,
we would again get
a run-time error.
So to make this feature
more intuitive,
we decided that all properties
were required by default
and once again to set
expectations,
we require developers
to parse this in,
in the required directive.
Now, we do have a workaround
for optional parameters,
which is to make them nullable.
This gives us the best
of both worlds.
You get optionality,
would the performance tradeoffs.
Okay, finally let's talk about
the order of properties.
My default JSON schema has
no ordering constraints,
which mean the LLM can
produce properties in any order.
But in the context
of LLMs order really matters.

[00:38]
Having the strict ordering of
properties can be really useful.
For example,
you can use an earlier field
in your schema
to condition the value
of a later field.
Such as adding a chain
of thought field to your schema.
The model will first
generate the chain of thought,
explain its thinking,
and then generate the answer.
This often improves the quality
of the answer significantly.
So to support this use case
we decided to generate
fields in the same order
that you define them in schema.
So that API design.
We wanted to make sure
that the API had good defaults,
while making the constraints
transparent to the developers.
Okay, so to bring it
all home here's Michelle.
-Awesome.
So you can see that
the engineering and research
paths of this product result
in a meaningful improvement,
but only when combined they
offer the best possible results.

[00:39]
This is actually our ethos
behind the work in
the OpenAI API.
We want to do the engineering
and research work on our end,
to make the easiest to use API
for developers.
We want to solve problems
like structured outputs for you,
so you can spend time
working on what matters most,
your application.
We think structured outputs was
the final puzzle piece
for unlocking the full power
of AI applications.
Data extraction is now reliable.
Function calls have
the required parameters.
And finally, a agentic
flows can work 100% of the time.
Since we launched
structured outputs in August,
developers like you, from
big companies to small startups,
have been building amazing apps!
We've seen customers like
Shopify use structured outputs
to reduce hallucinations
and improved the reliability
of their applications.
We've also heard
the excitement from all of you.
It's been so great
to see structured outputs solve

[00:40]
so many problems for developers.
And this is
why we do what we do.
Our mission at OpenAI is
to build safe AGI for everyone.
We build the API because we
think working with developers,
you all, is just critical
to achieving that mission.
You see the future before
anyone else, and together,
we can spread this technology
to the furthest reaches
of the world.
As follow engineers,
we feel so lucky to serve you.
So thank you for building us
and we're so excited
to see what you do.
Thank you.
[ Cheers and applause ]

</details>
