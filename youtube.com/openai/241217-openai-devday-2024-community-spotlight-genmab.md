---
title: "OpenAI DevDay 2024 | Community Spotlight | Genmab"
channel: openai
url: https://www.youtube.com/watch?v=be3hAgGGyKo
youtube_id: be3hAgGGyKo
published: 2024-12-17
duration: "8:59"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | Genmab

[![OpenAI DevDay 2024 | Community Spotlight | Genmab](https://img.youtube.com/vi/be3hAgGGyKo/hqdefault.jpg)](https://www.youtube.com/watch?v=be3hAgGGyKo)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Genmab (8:59)</summary>

[00:00]
-We are so excited
to be here today to talk about
how we used AI agents
to help the clinical trial
process get a lot faster.
I'm Scott.
I lead our AI innovation team
at Genmab.
And the only reason
I got the time
to come here is
because my five-year-old was
super excited I got to meet
ChatGPT in person.
Because he tells way
better stories than daddy does.
So Sam?
-I'm Sam Wagner.
Scott, maybe after the talk
we can meet Mr. ChatGPT.
-Well, I think we should.
So Genmab,
we are a biotech company.
We are an innovation company,
but focused on biology.
But that culture has permeated.
And now Genmab is committed
to not only
being the best
at biology and antibodies.
But also to not just adopt AI,
but try to push it forward.

[00:01]
So this is where our framework
comes in to help something
we think is really important.
The clinical trial process,
for those who don't know,
is super long
and super expensive.
Eight years or more,
billions of dollars
for one medicine in one disease.
Something has to give
to scale this.
And we think that AI is
well-positioned to help here.
So we're going to tell
you a story about
how we did this
for a very specific use case
for document generation.
Regulatory documents
that you have to submit
to the government.
One of these things you can
think of as the patient's story.
So for every patient
on every trial, you have to --
for every day
that they're on your trial,
you have to generate a
very specific clinical document,
that takes a skilled workforce
a significant amount
of time to triangulate.
They have to go to hundreds
of different documents,
or hundreds
of different pages of documents,

[00:02]
thousands of data points.
Compile that all together
with their skills as clinicians,
right, and generate
this summary.
This is one of many,
many documents, by the way.
We can go into more if you want.
For thousands of patients.
This takes a significant amount
of time.
And often it's not
just your internal stakeholders,
and company, and data,
but it's external partners too
that you have to work with.
And, you know, GPT-4o just
prompting can't get you that --
for a regulatory document,
you need to be 100% accurate.
Ninety-nine percent is
not good enough.
So we're going to talk about
how our framework,
which we call CELI, can get
us that last mile to do this.
So our high-level architecture
here sort of explains how --
and Sam's going to show
you this in a minute.
Our language model takes in,
sort of, real-world,
real -- natural language,
the user story of the task,

[00:03]
plans out the future in context.
Knows what Step 10's going to be
when it's executing Step 1.
Can self-correct,
has a guideline.
Has a way of evaluating how
each step executes and performs.
And sort of is able to tailor
and customize the plan
going forward.
Now it takes that,
and everything it does,
all the tools
that it calls in Step 1,
is the input, is
the Step zero of the next step.
And we can, sort of,
iterate this kind of ad nauseam.
And we show that you can
converge on that 100% accuracy
that we're looking for.
We've also shown, and this
is going to be published soon,
that it can solve
generic problems
where you know
how to evaluate the solution.
But we can go into that later.
But I think right now,
I'm super excited
to hand the floor to Sam
to show us CELI in action.
Sam?
-Thanks, Scott. All right.

[00:04]
So I'm going to kick
off CELI here.
As it's loading,
what I'm going to show you here
is the points
that Scott was talking about.
Which are...
that we're able to learn
the patient as we go along.
That it's drafting step by step,
section by section.
And as it's doing that,
it has a retrieval process
to get the information
that it needs.
So the first thing that it does
is give us a system message
here.
The way that we initialize this
is that we have a series
of prompts specifying the job,
right?
So the first thing
that we do is --
and this is a compilation
of the job description,
which you write beforehand.
So the first thing that we do is
we set up a role and objective
to say that you're going to
draft this particular document.
We set some criteria
for what the tasks are.
So this is a list of tasks that
need to be done sequentially.
So you can think of this
as a checklist, right?
So it's going to complete
the first task,
then move on to the second,
third, and so on.

[00:05]
And as it's doing that,
if it's not able to do a task,
then it's able to solve that.
The medical writers
and the clinicians
give us guidelines to
how these things are supposed
to be drafted.
So that's included in the
instructions, in the prompts.
We also have some prompt
completion mechanics,
which is an essential part
of CELI.
This is really part
of the secret sauce.
So what we tell it
is that as it progresses,
that it needs to tell
us what's been completed,
what it's working on, and
what it's going to work on next.
So the first thing
that happens here
is we sent this system message
to GPT.
It responds.
It knows that the first thing
that it does,
needs to do here,
is do a function call for
the particular identifier
for the clinical trial.
What's interesting here
is that any kind of IDs or keys
that you retrieve,
it's going to stay in context.
So you can do any kind of
key value pair lookups
in your function
calls at any time.
So we sent that to GPT.
It responds.

[00:06]
Tells us that the first task
has been completed.
It's working on Task 2.
Proceed to Task 2.
So it's going to instruct
itself the next time
that a call is made.
So it knows to keep going here.
So it does a function call.
It retrieves the table here.
Those results are appended
to the context.
So the context keep
building up here.
Now we have two tasks
that are done.
So the interesting points here
is that it has
a revolving narrative here.
It tells us
what kind of information
that it's gleaning
from the particular retrievals.
And the other part of this too,
is that it knows
how this information
is going to be used later on.
So this is Task 2 right now,
and it's telling us later,
it needs this information
for drafting.
So it can see ahead to Task 10
because all of that information
is inside of the system
prompt altogether.
So just as a reminder,
every time that this is done,
sent to GPT,
the system message comes
along with that.
So it has that blueprint
the entire way.
So we're going to skip ahead to
where it starts to draft.

[00:07]
At this point, it has all
of the tables that it needs.
So it starts to write.
Here's the background section.
Here, it writes about Day 1.
And it keeps doing this.
Keeps writing every section
until it's done with that
and it's time to compile it.
It's compiled it all together.
And one of the reasons
that we do that
is that we're very accurate
when we cut this up into
smaller sections that it writes.
And it's able to glean
all the information
that it needs from the context.
So here we save that.
There is a monitoring agent
at the end of the process
that confirms
that it's been saved.
Everything's been done
up to that point in sequence
like it's supposed to.
And then we have a complete
draft, which looks like this.
All right, back to you, Scott.
-Cool.
So as I'm pulling this up, what
Sam showed could take hours.
But his process takes minutes.

[00:08]
And we're talking
about thousands of patients
on many different trials,
for many different days.
Lots of other documents too.
And if you think about it,
like, the ultimate goal here is
if you shave a month off of
a trial, let's just say a month,
that's literally
hundreds or thousands of people
with serious disease that
can have access to our drug,
that would not have been able to
because of
how serious the disease is.
So that's what like,
gets us up in the morning
to come into work,
right, is that problem.
And if you're interested
in working on those problems
with us,
like QR codes, open source.
CELI as a problem solver,
as a document generator is
generic, we think.
Also on the right,
if you're interested of helping
people with serious disease,
that's for you.
So thank you very much.
We've been so excited
to be here today.
Thank you.

</details>
