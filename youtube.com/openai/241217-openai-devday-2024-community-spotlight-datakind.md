---
title: "OpenAI DevDay 2024 | Community Spotlight | DataKind"
channel: openai
url: https://www.youtube.com/watch?v=_Zo_s9klKP0
youtube_id: _Zo_s9klKP0
published: 2024-12-17
duration: "10:34"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | DataKind

[![OpenAI DevDay 2024 | Community Spotlight | DataKind](https://img.youtube.com/vi/_Zo_s9klKP0/hqdefault.jpg)](https://www.youtube.com/watch?v=_Zo_s9klKP0)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | DataKind (10:34)</summary>

[00:00]
hi everyone I'm Caitlyn Augustine I'm
the vice president of product and
programs at datakind we're a global
nonprofit organization focused on using
data and technology in the service of
humanity and I'm joined by my colleague
Ted who leads our humanitarian um
efforts and Partnerships and we're going
to talk to you about the this enormous
need in the humanitarian space for
timely and highquality data and to put
that in context for you right now there
are 300 million people in the world in
need of humanitarian assistance there
are 40 coordinated Global appeals and
the uh Gap in funding is $46
billion um so it is clear that we have
to innovate to figure out solutions that
can get us to having these timely
responses these efficient uses of
resources and from data kind side we've
seen examples of when this has gone

[00:01]
incredibly well this is an example from
un Ocha in their response in Afghanistan
for natural disasters this is a uh
interactive dashboard that is uh put up
and maintained by the UN and it has data
from multiple resources it has it from
the local government it has it from uh
NOS it has it from the UN teams and it
allows the responders to identify where
a disaster has occurred and send the
right teams with the right interventions
in place in a very rapid fashion um but
this is unfortunately the exception it's
not the rule and we know that uh having
high quality data can help us save lives
so data kind uh went through a number of
interviews with humanitarian
organizations over two dozen of them to
say what are your pain points in
actually accessing and using this data
if you know it will help you in your
response and we heard a number of pain
points and identified places where

[00:02]
generative AI could be a meaningful part
of that solution while still keeping a
human in the loop to help solve those
problems and the problem I'm going to
dig into here is metadata prediction so
why metadata prediction well
humanitarians love spreadsheets they're
their preferred data sets uh it's how
they share data uh the humanitarian data
exchange which is one of the major
repositories of humanitarian data in
2023 had over
150,000 tabul data sets and even though
those data sets contain information that
can save lives they don't interoperate
and this is despite the fact that 20
years ago hexel a uh metadata standard
was Community created and approved for
use um it is a a tool that helps you
like this uh table here says put the
label and the description of the data on
each of your Columns of your data sets
and it's super easy to use the example
running there is how you would put a

[00:03]
line in your spreadsheet but hexel
hasn't really achieved adoption it
hasn't had its impact um its time
consuming to handleable data it's Error
prone what that ultimately means is that
about half of humanitarian data does not
have metadata on it at all and of the
half that does have uh metadata tagging
about half of it is wrong uh it's data
that isn't standard it's not in the the
common Corpus so that data is not fit
for purpose We Believe that generative
AI could help us in this uh labeling
this tags and attributes in this data
there was previous work about 5 years
ago that showed this as a proof of
concept but have a lot of friction in
implementation and we saw with uh using
uh gbt that we could actually do this
tagging for a more expansive uh body of
knowledge and get it to implementation
with far less friction uh we started
this work in 2023 and we've now expanded
it in 2024 completing the last round in
August testing three different models

[00:04]
and prompting approaches so how did we
actually come to this question well if
only about
25% of uh data sets have accurate
metadata we heard from our stakeholders
that they almost didn't care they were
like make it more right than wrong and
we will be happy uh we went to the
literature and we saw that in in
different contexts but for a similar
challenge uh 70% accuracy yielded
meaningful results in in those spaces so
we set as accuracy Target of 70% um this
is something that we are asking
humanitarians nonprofit organizations to
use they don't have a budget line for it
so we wanted to ensure that the weekly
cost was around $5 and that would allow
them to process around a 100 tables
which is sort of the load of generation
on a weekly basis and this was going
into an existing workflow we wanted it
to be as fast as possible our previous
work suggested about 1 second processing
time per table made sense and we wanted
the total time to take about an hour

[00:05]
from our prep to our processing um
because we are still having humans be a
part of this they're just now moving
from that manual correction of all that
metadata and that trying to piece
together information to actually just
checking the tagging that that has
happened and with those goals in mind we
started off on our work so first receive
the data right so we pulled the data
from the humanitarian data exchange um
and we did a lot of data prep and I just
want to highlight two pieces of this
data prep for you because they were
helpful learnings for our team uh as we
went through um using llms so the first
was Data enrichment so if you're a human
doing your metadata tagging you have to
read a number of rows to get the context
for what you're actually going to label
it right your your system has to do that
too so we used GPT 3.5 turbo to create
table summaries and we enriched our data
set in that way um the second was
creating our test and train set so
standard machine learning uh flows right

[00:06]
uh we will do a random assignment
between train and test uh to produce
those data sets um but in this case we
would have had the same organizations
data in both train and test because the
same organizations are doing all this
metadata tagging they do it all in the
same way having that random split could
have actually led us to sort of
artificially positive results so we
created our train and test sets based on
organization so an organization's
metadata could only occur in one or the
other of those sets um and then
ultimately we created our our test files
um uh and uh moved forward into uh
actually testing that fine-tuned GPT 4.0
um 40 Mini model and the first thing to
say is it worked really well for the
most common metadata um over 95%
accuracy for locations and dates and
since this is the thing that is most
crucial to get right we were thrilled at
these results it worked well for predict

[00:07]
predicting just the hexel tags those
just those uh labels things like
population like location like date but
it only worked okay for predicting the
tags and the attributes those
descriptors and when we dug into it it
was kind of interesting to figure out
why did this not work so well why were
we only getting around 60% accuracy and
the first thing was we actually found
situations where the model and the human
were both right um there are synonyms in
the hexal standard so something like
location can also be called admin so
human was labeling it one thing model
was labeling the other they're both
correct what was more interesting was we
found situations where the model was
right uh or more right than a human so
the model would actually add more
descriptors than the human did so uh
human might have said this is a
population the model might have said
this is a population of women 15 years
or younger giving us more valuable

[00:08]
information and then finally we had
situations where the human label data
was wrong um even though it was the
correct standard um it was still
describing the wrong things and the
model was actually correct and that
actually made us think maybe this
fine-tuning wasn't the best approach and
given the economies of scale with these
prompts could we avoid fine-tuning all
together instead directly prompt for
these hexel tags and attributes and the
answer is sort of right you know all of
us have been doing these zero shot
prompts out of the box our answer looked
right you know we we got this answer
that that seemed like it made sense but
it actually doesn't follow hexel
standard at all the answer looks a lot
like what those human labeled tags were
with the let me figure out what I think
the right answers are so we needed to
add instructions into our prompting um
we needed to change that to include only
the hexal data standard and we need to
put some rules in place for the order of
information that would come out that we

[00:09]
needed the tag then we needed the
attribute and once we did that it was
great um so our stakeholders were
thrilled because we had multiple
approaches that hit our accuracy targets
um in our time constraints and in our
cost Target and all of this allowed us
to unlock thousands of more variables
for humanitarian use and uh we're only
getting better right today exciting
announcements around distilling around
ongoing improvements that's what we're
taking now into phase two because
ultimately metadata prediction is one
part of our overall humanitarian data
project system it's just this one box
here uh in Gold um there are many other
pieces that feed into a tool that we are
using and we are making accessible to
humanitarians to give them that rapid
access to that timely highquality data
what you now actually see the behind me
is our humanitarian AI assistant that is

[00:10]
now pulling all of that harmonized
interoperable data together to allow a
humanitarian to interact uh with a chat
to get ground truth verified information
out to allow them to do a rapid response
um this has all been co-created with
humanitarians this was a Whistle Stop
tour I know I'm at my time uh please uh
follow us connect with us uh we look
forward to talking you with you uh in
the future so

</details>
