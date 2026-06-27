---
title: "OpenAI DevDay 2024 | Community Spotlight | DataKind"
channel: openai
url: https://www.youtube.com/watch?v=FBd-BXXEyCw
youtube_id: FBd-BXXEyCw
published: 2024-12-17
duration: "10:34"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | DataKind

[![OpenAI DevDay 2024 | Community Spotlight | DataKind](https://img.youtube.com/vi/FBd-BXXEyCw/hqdefault.jpg)](https://www.youtube.com/watch?v=FBd-BXXEyCw)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | DataKind (10:34)</summary>

[00:00]
-Hi everyone.
I'm Caitlin Augustin.
I'm the Vice President
of Product and Programs
at DataKind.
We're a global
nonprofit organization focused
on using data and technology
in the service of humanity.
And I'm joined by my colleague,
Mitali,
who leads our humanitarian
efforts and partnerships.
And we're going to talk to you
about this enormous need
in the humanitarian space
for timely
and high-quality data.
And to put that in context
for you,
right now there are
300 million people in the world
in need
of humanitarian assistance.
There are 40 coordinated
global appeals
and the gap in funding
is $46 billion.
So it is clear that we have to
innovate to figure out solutions
that can get us to having
these timely responses,
these efficient uses
of resources.
And from DataKind's side,
we've seen examples of when
this has gone incredibly well.

[00:01]
This is an example from UN OCHA
and their response
in Afghanistan
for natural disasters.
This is a interactive dashboard
that is put up
and maintained by the UN.
And it has data
from multiple resources.
It has it from
the local government.
It has it from NGOs.
It has it from the UN teams.
And it allows
the responders to identify
where a disaster has occurred
and send the right teams
with the right interventions
in place,
in a very rapid fashion.
But this is unfortunately
the exception.
It's not the rule.
And we know
that having high quality data
can help us save lives.
So DataKind went through
a number of interviews
with humanitarian organizations,
over two dozen of them,
to say,
what are your pain points
in actually accessing
and using this data?
If you know, it will help you
in your response.
And we heard a number
of pain points
and identified places

[00:02]
where generative AI
could be a meaningful part
of that solution,
while still keeping a human
in the loop
to help solve those problems.
And the problem
I'm going to dig into here
is metadata prediction.
So why metadata prediction?
Well, humanitarians
love spreadsheets.
Their preferred data sets,
it's how they share data.
The Humanitarian Data Exchange,
which is one
of the major repositories
of humanitarian data in 2023 had
over 150,000 tabular data sets.
And even though those data
sets contain information
that can save lives,
they don't interoperate.
And this is despite the fact
that 20 years ago,
HXL, a metadata standard,
was community created
and approved for use.
It is a tool that helps you,
like this table here says,
put the label
and the description of the data
on each of your columns
of your data sets.
And it's super easy to use.
The example running there is
how you would put a line
in your spreadsheet.

[00:03]
But HXL hasn't really
achieved adoption.
It hasn't had its impact.
It's time consuming
to hand label data.
It's error prone.
What that ultimately means is
that about half
of humanitarian data does
not have metadata on it at all.
And of the half
that does have metadata tagging,
about half of it is wrong.
It's data that isn't standard.
It's not in the common corpus.
So that data is not fit
for purpose.
We believe that generative AI
could help us in this labeling,
this tags and attributes
in this data.
There was previous work
about five years ago
that showed this
as a proof of concept,
but had a lot of friction
in implementation.
And we saw with using GPT
that we could actually do
this tagging
for a more expansive
body of knowledge
and get it to implementation
with far less friction.
We started this work in 2023,
and we've now expanded it
in 2024.
Completing the last round
in August,
testing three different models
and prompting approaches.

[00:04]
So how did we actually come
to this question?
Well, if only about 25% of
datasets have accurate metadata,
we heard from our stakeholders
that they almost didn't care.
They were like,
make it more right than wrong
and we will be happy.
We went to the literature and we
saw that in different contexts,
but for a similar challenge,
70% accuracy yielded meaningful
results in those spaces.
So we set an accuracy target
of 70%.
This is something that
we are asking humanitarians,
nonprofit organizations to use.
They don't have a budget line
for it,
so we wanted to ensure that the
weekly cost was around $5 US.
And that would allow them
to process around 100 tables,
which is sort of the load
of generation on a weekly basis.
And this was going into
an existing workflow.
We wanted it to be as fast
as possible.
Our previous work suggested
about one second processing time
per table made sense.
And we wanted the total time

[00:05]
to take about an hour
from our prep to our processing.
Because we are still having
humans be a part of this.
They're just now moving
from that manual correction
of all that metadata
and that trying
to piece together information,
to actually just checking
the tagging that has happened.
And with those goals in mind,
we started off on our work.
So first, receive the data,
right?
So we pulled the data from
the Humanitarian Data Exchange,
and we did a lot of data prep.
And I just want to highlight
two pieces
of this data prep for you,
because they were
helpful learnings for our team
as we went through using LLMs.
So the first was
data enrichment.
So if you're a human
doing your metadata tagging,
you have to read a number
of rows to get the context
for what you're actually
going to label it, right?
Your system has to do that too.
So we used GPT-3.
5 Turbo
to create table summaries,
and we enriched our data set
in that way.
The second was creating
our test and train set.
So standard machine
learning flows, right?

[00:06]
We will do a random assignment
between train and test
to produce those data sets.
But in this case,
we would have had
the same organization's data
in both train and test.
Because the same organizations
are doing all
this metadata tagging.
They do it all in the same way.
Having that random split
could have actually led us to
sort of artificially positive
results.
So we created our train and test
sets based on organizations.
So an organization's metadata
could only occur in one
or the other of those sets.
And then ultimately,
we created our test files
and moved forward into
actually testing that fine-tuned
GPT 4.0, 4o-mini model.
And the first thing to say is
it worked really well
for the most common metadata.
Over 95% accuracy
for locations and dates.
And since this is the thing that
is most crucial to get right,
we were thrilled
at these results.
And it worked well for
predicting just the HXL tags,

[00:07]
just those labels.
Things like population,
like location, like date.
But it only worked okay
for predicting the tags
and the attributes,
those descriptors.
And when we dug into it,
it was kind of interesting
to figure out
why did this not work so well?
Why were we only
getting around 60% accuracy?
And the first thing was
we actually found situations
where the model
and the human were both right.
There are synonyms
in the HXL standard.
So something like location
can also be called admin.
So human was labeling
it one thing,
model was labeling it the other.
They're both correct.
What was more interesting
was we found situations
where the model was right,
or more right than a human.
So the model would
actually add more descriptors
than the human did.
So human might have said
this is a population.
The model might have said,
this is a population
of women 15 years or younger.
Giving us
more valuable information.

[00:08]
And then finally,
we had situations
where the human
labeled data was wrong.
Even though it was
the correct standard,
it was still describing
the wrong things
and the model was
actually correct.
And that actually made us think
maybe this fine-tuning
wasn't the best approach.
And given the economies of scale
with these prompts,
could we avoid fine-tuning
altogether,
instead directly prompt for
these HXL tags and attributes?
And the answer is sort of,
right?
You know, all of us have been
doing these zero-shot prompts.
Out of the box,
our answer looked right.
You know, we got this answer
that seemed like it made sense,
but it actually doesn't follow
HXL standard at all.
The answer looks a lot like what
those human-labeled tags were.
The let me figure out what
I think the right answers are.
So we needed to add
instructions into our prompting.
We needed to change that
to include only
the HXL data standard.
And we needed to put
some rules in place
for the order of information
that would come out.

[00:09]
That we needed the tag,
then we needed the attribute.
And once we did that,
it was great.
So our stakeholders
were thrilled
because we had
multiple approaches
that hit our accuracy targets
in our time constraints
and in our cost target.
And all of this
allowed us to unlock thousands
of more variables
for humanitarian use.
And we're only getting better,
right?
Today's exciting announcements
around distilling,
around ongoing improvements.
That's what we're taking now
into Phase 2.
Because ultimately,
metadata prediction is
one part of our overall
humanitarian data project
system.
It's just this one box here
in gold.
There are many other pieces
that feed into a tool
that we are using
and we are making accessible
to humanitarians,
to give them that rapid access
to that timely,
high-quality data.
What you now actually see
behind me
is our Humanitarian
AI Assistant

[00:10]
that is now pulling all
of that harmonized,
interoperable data together,
to allow a humanitarian
to interact with a chat
to get ground-truthed,
verified information out
to allow them to do
a rapid response.
This has all been co-created
with humanitarians.
This was a whistle-stop tour.
I know I'm at my time.
Please follow us,
connect with us.
We look forward to talking
with you in the future, so...
[ Applause ]

</details>
