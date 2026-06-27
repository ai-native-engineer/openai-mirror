---
title: "OpenAI DevDay 2024 | Community Spotlight | Tortus"
channel: openai
url: https://www.youtube.com/watch?v=tUEqVOnxcnw
youtube_id: tUEqVOnxcnw
published: 2024-12-17
duration: "13:31"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Tortus

[![OpenAI DevDay 2024 | Community Spotlight | Tortus](https://img.youtube.com/vi/tUEqVOnxcnw/hqdefault.jpg)](https://www.youtube.com/watch?v=tUEqVOnxcnw)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Tortus (13:31)</summary>

[00:00]
hi everyone my name is Nina I'm a
research engineer at tauris and today
with s we're going to present our
journey of evaluating LMS in a clinical
application seven minutes every time a
clinician uses our llm powered
application called toris they get seven
minutes to be to do what they best out
which is being a doctor and today this
is really critical because um up to 60%
of clinician tasks uh time is spent on
computer tasks such as entering data and
um filling tests and making orders which
can average up to 4,000 clicks on a
typical
shift it's therefore of no surprise that
53% of clinicians report that they are
burnt out with uh computer use being one
of the uh leading causes of this
burnout let's see how toris works so hi
s why are you in today to see me hi yes

[00:01]
I've been really dialed in the last
couple days you know working on this
presentation for opening I Dev day you
know been up all night working on these
slides oh yeah what sort of symptoms are
you having yeah so anytime I open up
canva I get nauseous you know I've been
having nightmares about Sam ultman
heckling me during the presentation it's
it's been a tough couple days oh yeah
that's pretty bad so it seems like
you're really dialed in so I'm going to
prescribe you some dialysis and also
some
paracetamol so now we should see that uh
tortoise will take our consultation and
we can create some documentation which
can be filed into the electronic health
record which is where all the
documentation about your doctor visits
is stored so here we're generating the
documentation and let's now have a look
at this summary so as we can see it
captures pretty well that um Sal is
quite stressed because he's presenting
openi um and that he's uh nauseous and
he's stressed and we can also see that
my prescription for dialysis for being
so dialed in and uh ibuprofen is also
mentioned but one thing to note is that

[00:02]
I never said anything about giving salum
paracetamol um and this is a clinical
error and this can have an impact on our
patients so we have to be very careful
of how we use llms in
production the typical Mantra in Silicon
valy of move fast and break things
therefore doesn't necessarily always
apply to us because moving fast and
breaking things can lead to moving fast
and breaking
people it's therefore critical that we
Center clinicians which are our end
users and are the experts in this domain
uh to help us design and evaluate uh the
things that we push to
production Clans are the typical
ideators of um maybe some complex
workflows that take as the input the
consultation and then output a series of
documents and they communicate these
requirements to the developers who will
Implement these in code and together
they iterate together until they reach a
good solution that can be um pushed to
production however we have some quite
stringent compliance requirements so
obviously our outputs need to be
clinically safe and this means that this
person process is quite slow and labor

[00:03]
intensive we found that the thing that
would made our process the slowest was
this iterative loop with the developer
and at the time there were no outof thee
box solutions to put the clinician back
into the driver's seat so we decided to
uh make a platform which broke down
these complex workflows into smaller
steps called blocks uh to put the
clinician back into the driver's seat
let's see how we did
this yes so at the core of our
architecture we have the building blocks
of what make up an LM workflow and our
key aim here was to make sure that
clinicians and Engineering are all sort
of speaking the same language When
developing these workflows so when we
designed our designed our blocks we have
centered it around an LM call we decide
our inputs in most cases it's usually a
medical transcript and our outputs we
also SP uh specify extra model
configuration such as the model the prom
that was used whether it's a structured
output and then this is the general
interface that we use when creating
blocks in llm workflows and a key part
of this is that we want our clinicians
to share blocks with with each other and

[00:04]
reuse them so we don't have to reuse a
lot of work so we store this within our
database and what we do is we ingest all
of these parameters we create a hash and
this forms a block ID so this is a
unique representation of a block such
that if we change any of these
parameters it generates a new block ID
but if we want to share a block with a
with another clinician they can then
pull it from our database so now we've
got the skeleton of our blocks let's see
how we can get them to compos together
let's say we've got one block which
extracts some key facts from a medical
transcript and another block which
ingests those facts and uh shoots out a
referral letter we want a way of
specifying how these two blocks can uh
compose together right and we initially
thought okay let's just use the term
facts and that will be the connection
between the two blocks but facts can be
very high level you can have facts in
bullet points you can write them in
paragraphs and that can lead to
different outputs down the line so we
need to be very explicit here so we've
decided to actually use the block ID of
the previous block to be used as the
input into the next block so we know

[00:05]
exactly what's coming before
it and that way we know that these two
blocks can be composed when we've got
the IDS matched up and now we have our
llm
workflow let's say we iterate on our
info extraction block while still
maintaining our current fact a letter
block we'll now create a new say we
changed uh the model opening eyes releas
a shiny new model that we want to use we
might change the promp slightly this
will produce a new block ID and we still
got our old block ID here but now we
know that because the block IDs don't
match our blocks no longer can fit
together and while this can seem really
uh verose like when we get audited it
actually puts us in a great position
because we know that when we're um when
we're getting audited for a specific
workflow we know exactly what's
happening along the
way uh we created a UI to allow our
clinicians to create these blocks um so
that we can create function calling
blocks um so they can create structured
output without having to edit long Json
we can also so load in some blocks from

[00:06]
the Firebase so what we've got here is a
block which um extracts key problems
from a medical transcript in the format
which is used for an electronic
Healthcare record system called emis so
the clinicians can load up this block
feed in a couple of transcripts to see
how the output turns out and we can see
how it turns out there so this is a
structured output shoots out an array of
problems but let's say we want to add to
this uh workflow we can create a block
from within the UI we're going to create
a simple llm block here which will
ingest these problems and shoot out a
note in the soap note
format so it's important to note here
that when we're specifying the inputs
we're actually specifying that we want
the block of the emis problems to be fed
in here now we've got our block we can
add it to our chain uh and generate our
outputs and after some generation we can
see that our soap note should be coming
out in the correct
format and we also have our intermediate
outputs being displayed
so we can see what's being produced

[00:07]
along the way so this is our main space
where our clinicians will iterate and
share blocks and when they're happy they
can save these blocks as an experiment
so what is an experiment an experiment
is a way that we uh compare llm
workflows let's say our existing uh
transcript letter workflow um just
consists of one block which takes in the
transcript and shoots out the referral
letter and we want to iterate on this
workflow by first extracting the key
facts and then generating the letter
when designing our experiment we specify
a couple of things the number of data
points that are being generated how many
clinicians we'd like to review each data
point and a baseline to compare the
results to so this framing here is what
forms our experiment and in this example
this is our Baseline let's see how the
generation pipeline works so we start
with our experiment that we specify we
then generate our outputs from our bank
of uh consultations we then give this to
our clinicians um we' designed a data
labeling platform which allows them to
label hallucinations and Emissions where

[00:08]
hallucinations are pieces in the output
that are not represented in the input
and Emissions are things that the llm
step has missed out um here at taorus we
call this
halumi um and yes we would like to
trademark this very shortly so if anyone
wants to use that please uh refer to our
website once we uh collect our halumi we
analyze the results and unlike in
regular life we actually want to
minimize the amount of halumi that is
generated in the experiments so if we
can see that our experiment has less
halumi than the Baseline we actually go
back to the drawing board create a new
experiment and iterate from there if it
looks good we can go into the
product it's important to see here that
this piece of the of the pipeline is
actually the most important part where
we're actually Gathering that those
human labels of halumi because doctors
have key information that an llm really
can't uh do itself um we've tried doing
M EV vales back in 2023 and they weren't

[00:09]
up to par so we really needed to make
this piece important and it's really
important to note that this step is
quite time consuming for the clinicians
to be looking at the input and the
output labeling and we actually pay our
clinicians to incentivize them to do a
good job so we really need to make the
most of our resources here so there's a
couple of things that we do to S of
maximize the resources we have available
to us first thing we do is that we store
results at the Block Level so in
addition to getting those intermed
output store we can actually reuse
previous experiments let's say we've got
a really good info extraction block and
we want to build on that and create
other different workflows we don't have
to get that info extraction box labels
redone another thing we do is smart
sampling so this is where we share the
random seed between the experiment and
the Baseline such that when we're
sampling new data points for our
experiment we're actually re using the
same examples as our Baseline so we're
comparing apples with apples and a key
feature this allows us to do is we can
actually increase the number of data
points we collect over time without

[00:10]
greatly increasing the labeling effort
let's say our Baseline is 25 examples
and our new experiment want run 30 we'll
sample the same 25 and get an additional
five and those additional five are the
ones that get
labeled okay let's look at some results
of how we use this platform to evaluate
the clinical safety of our product so as
Sal mentioned we have hallucinations and
Emissions which are uh things that the
model generates which aren't present in
the original transcript and omissions
being things that are missed out by the
El them we also make the internal uh
classification of major errors and minor
errors where major errors will have an
impact on uh the clinical outcome for
the patient so we're really interested
in trying to minimize uh the major
errors here I'm going to show you a
little example of what a ma major error
looks like so at the top this is this
text is actually really small so I'm
just going to explain um this is a
consultation where a doctor uh is seeing
a patient and the patient has flu like
symptoms and the doctor recommends that
the patient just go home drink some
water mofen and

[00:11]
rest at the bottom we see an output that
was generated by our llm with one of our
workflows and in red is an error that
the llm made so in this case um the llm
said that we should discuss the use of
broadspectrum antibiotics and this is
something that was not said by the
clinician so we would uh categorize this
as a major hallucination as it will have
an impact on the patient broadly what we
see um with these plots of our
experiments over time is that the volume
of hallucinations and Emissions uh
decrease as we iterate but obviously
this is an iterative framework so things
don't always go as expected and just to
highlight um a point here in our graph
we saw a very major increase uh in major
H
stations this happened because our
original Baseline we were trying to
generate some letters uh from the
transcript directly and we thought to
make the uh the outputs more factual we
should just extract the facts and then
use those to generate the letter using
this platform allowed us to very very
quickly assess uh that the experiment

[00:12]
actually introduced a lot more major
hallucinations so we directly said we
cannot push push this to production and
therefore this would have never impacted
uh patients in a real clinical
setting overall using this framework has
really saved a lot of time at torsus
originally we had two developers that
were tasked with co-creating with
clinicians and designing the workflows
that they wanted to run and these two
developers could go on and do other
things that needed to be done of the
company instead of uh riding the
workflows as the clinicians uh could now
do it themselves through our
playground additionally this had the
impact of making our clinicians a lot
happier because they were back in the
driver's seat and they could design the
workflows at the speed that they wanted
to and run the experiments that they
were interested in and overall this had
the effect of increasing our shipping
time of uh new prompts new models new
architectures into
production additionally uh all our
labeled outputs have resulted in one of

[00:13]
the first uh large scale data sets of
hallucinations and Emissions uh from llm
generated clinical documentation and we
are planning on using this uh to try and
automate this error detection and
therefore make our product further safe
this will also allow us to do live
monitoring production and and help flag
to our users uh when errors are made so
that they can be wary of them when they
are sharing the
documentation thank you for listening
and we look forward to Shing to you
later

</details>
