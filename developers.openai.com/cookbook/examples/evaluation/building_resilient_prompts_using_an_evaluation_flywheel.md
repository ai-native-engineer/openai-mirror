<!-- source: https://developers.openai.com/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel/ -->

## Search the cookbook

Oct 6, 2025

# Building resilient prompts using an evaluation flywheel

[![Neel Kapse](https://media.licdn.com/dms/image/v2/D4E03AQEegSR4W4Ylmg/profile-displayphoto-scale_400_400/B4EZkLjdrcIQAk-/0/1756835470622?e=1762387200&v=beta&t=HETTFnoh3nV_Yc84tHGkahKgOFdvnPlesfi3ki8mWFg)  NK](https://www.linkedin.com/in/neel-kapse/)  [![Hamel Husain](https://media.licdn.com/dms/image/v2/C5603AQGoyHYtA2QIXw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1572471557655?e=1762387200&v=beta&t=wZrq-Nfc8-4Xq-nJ5g2jt9gZ1KLTg23KOIBGHk2xkZ0)  HH](https://www.linkedin.com/in/hamelhusain/)

[Neel Kapse 
(OpenAI)
 ,](https://www.linkedin.com/in/neel-kapse/)  [Hamel Husain](https://www.linkedin.com/in/hamelhusain/)

[View on GitHub](https://github.com/openai/openai-cookbook/blob/main/examples/evaluation/Building_resilient_prompts_using_an_evaluation_flywheel.md) [Download raw](https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/evaluation/Building_resilient_prompts_using_an_evaluation_flywheel.md)

## Overview

### Purpose of this cookbook

This cookbook provides a practical guide on how to use the OpenAI Platform to easily build resilience into your prompts.

> A **resilient prompt** is one that provides high-quality responses across the full breadth of possible inputs.

Prompt resilience is an essential piece of deploying AI applications in production. Without this property, your prompts can produce unexpected results on edge cases, provide subpar responses in normal cases, and undermine the effectiveness of your AI application.

To build resilience into your prompts, we recommend the **evaluation flywheel** process — a methodology that enables builders to continuously refine their AI applications over time in a measurable way.

### Target audience

This cookbook is designed for subject-matter experts, solutions architects, data scientists, and AI engineers who are looking to improve the general consistency and quality of their prompts, or address specific edge cases in their AI applications.

## The evaluation flywheel

AI applications often feel brittle. A prompt that works well one day can produce unexpected and low-quality results the next. This happens because prompts can be sensitive to small changes in user input or context. To build reliable AI products, we need a systematic way to make prompts more resilient.

The solution is a continuous, iterative process called the **evaluation flywheel**. Instead of guessing what might improve a prompt (“prompt-and-pray”), this lifecycle provides a structured engineering discipline to diagnose, measure, and solve problems.

The flywheel consists of three phases:

1. **Analyze**:
   Understand how and why your system is failing through qualitative review. Manually examine and annotate examples where the model behaves incorrectly to identify recurring failure modes.
2. **Measure**:
   Quantify the identified failure modes and set a baseline. You can’t improve what you can’t measure. Create a test dataset and build automated evaluators (“graders”) to score your system’s performance at scale.
3. **Improve**:
   Make targeted improvements such as rewriting prompts, adding better examples, or adjusting system components. With measurement in place, you can immediately see the impact of changes and iterate until failure rates are acceptably low.

This is a continuous cycle. As you improve the system, new, subtler failure modes emerge — and the flywheel begins again. This process is the core methodology for building robust and reliable AI applications.

![Evaluation flywheel](/cookbook/assets/images/evaluation-flywheel.png)

> **Source:** Shankar, S., & Husain, H. (2025). *Application-Centric AI Evals for Engineers and Technical Product Managers*. AI Evals Course Reader.

## An Example

To illustrate the evaluation process, let’s use data from an **apartment leasing assistant** in production.

It answers questions from prospective renters, such as:

* “How large are the apartments?”
* “When can I come in for a tour?”

Suppose we have a specific prompt within our application that we’d like to analyze. We can get started in the OpenAI Platform by adding in our prompt and uploading our input and output data to our Dataset (learn more about how to do this in [our docs](https://platform.openai.com/docs/guides/evaluations-getting-started)).

![Leasing agent data](/cookbook/assets/images/dataset.png)

With our prompt and traces loaded in, we’re ready to analyze prompt effectiveness.

## Analyzing prompt effectiveness

To improve a system, you must first understand how it fails. While automated metrics are useful for tracking progress, they cannot reveal *why* a failure occurred. Manual analysis of model outputs is the most effective way to diagnose issues and gain insights for targeted improvements.

The core of this analysis is **annotation** — applying structured labels to text to categorize and understand failure modes. This turns unstructured failures into an actionable roadmap for improvement. We recommend a two-step method drawn from qualitative research: open coding and axial coding.

### 1. Open Coding: Discovering failure modes

The first step is to read through a sample of failing traces (we recommend starting with around 50) and apply descriptive labels to each error you find. In this phase, do not worry about creating a perfect, structured taxonomy. The goal is discovery.

On the OpenAI Platform, you can use annotation columns to open code your dataset. Here, we add a **Feedback**-type annotation column titled `open_coding` to capture our results.

![Creating a feedback column](/cookbook/assets/images/creating-feedback-column.png)

For our apartment leasing assistant, our initial open codes might look like this:

* “bot suggested a tour time that wasn’t available”
* “the list of amenities was a single block of text”
* “failed to cancel the original appointment when rescheduling”
* “the link to the floorplan was broken”

These specific, grounded-in-data labels become the raw material for the next step.

![Open coding](/cookbook/assets/images/open-coding.png)

Here’s our dataset after open coding.

### 2. Axial Coding: Structuring your insights

Once you have a set of open codes, the next step is to group them into higher-level categories. This is axial coding—the process of identifying relationships between your initial labels to build a structured understanding of the core problems.

We can group our open codes into predefined axial codes:

* **Tour scheduling/rescheduling issue:**
  + Bot suggested a tour time that wasn’t available
  + Failed to cancel the original appointment when rescheduling
* **Formatting error with output:**
  + The list of amenities was a single block of text
  + The link to the floorplan was broken

We will add a new **Label**-type annotation column titled `axial_coding` to our dataset to capture this.

![Axial coding](/cookbook/assets/images/axial-coding.png)

This simple taxonomy gives us a clear, quantitative picture of our system’s primary weaknesses. We might discover that 35% of failures are related to tour scheduling, while only 10% are formatting errors. This tells us exactly where to focus our improvement efforts. For more information on how to conduct error analysis, see [this walkthrough](https://youtu.be/qH1dZ8JLLdU?si=Sxczt-LpKVVnMEdG).

<!-- yt-inline:qH1dZ8JLLdU -->
[![Intro To Error Analysis: Creating Custom Data Annotation Apps (4k version)](https://img.youtube.com/vi/qH1dZ8JLLdU/hqdefault.jpg)](https://www.youtube.com/watch?v=qH1dZ8JLLdU)

<details>
<summary>자막: Intro To Error Analysis: Creating Custom Data Annotation Apps (4k version) (41:36)</summary>

[00:00]
And just a quick introduction, um, I'm
Hussein. I've been working on machine
learning and AI for over 20 years. Um,
I've worked at a lot of different
startups like Airbnb, GitHub. I've been
working on LM for a really long time.
Uh, I was really early at GitHub. Um,
you know, working on LLMs. I led
research that led up to GitHub co-pilot.
Um, so I've been working on AI products
for for a while. Uh, and I'm excited to
be here with Shrea talk about error
analysis.
Yeah. Hi guys. I'm Shrea. I am a PhD
student at UC Berkeley in the EES
department. But before that, I was an ML
engineer. So I did a lot of MLOps work,
a lot of evaluation and deployment and
monitoring um of large scale time series
production. And now in the age of Gen
AI, I'm super interested from a research
perspective of, you know, how do we
rethink how we do evals when we're not
training models, we're using
off-the-shelf foundation models, we
haven't explicitly encoded loss metrics

[00:01]
or have too much label data to go off
of. So what does it mean to kind of
build confidence in how we evaluate our
systems? Um, so I'm very excited to be
here with Hamill today to kind of give
you a preview of the curriculum we're
building around this. Um I will move to
the next slide.
Yeah, go ahead. Um so just the
motivation of this is okay a lot of
people they you know they jump straight
to frameworks tools like you know what
rag database should I use what agentic
framework should I use so on and so
forth and it's quite rare that people
are looking at data and this is uh what
everyone is stuck on and you know I'm
currently an independent consultant who
helps people with AI products
And I would say yeah the mo the pe the
thing that people are stuck on is the
reason they're stuck is they're not
looking at data. And so this is like
conventional wisdom in in machine

[00:02]
learning circles. This is a tweet by
Greg Greg Brockman. Uh you know manual
inspection of data is the highest value
to prestige ratio of any activity in
machine learning. I would go even
further than that. I would say it's the
highest ROI activity in machine learning
period. And it's probably or it is the
highest ROI
activity if you're building any AI
product period. Um it doesn't feel like
it would be. It feels like oh looking at
data is grunt work but actually when you
look at data you you get a lot of value
very fast.
Um so yeah that's just the motivation. I
think you know this is going to be time
well spent. Um so yeah let's get into
it. So today's agenda we're going to
learn a technique a structured technique
for looking at data. So like what do we
mean by looking at data and like how do
you look at data? Well there's a way to

[00:03]
do that. It's called error analysis.
It's not something we made up. It's been
something that's been around for a
really long time in machine learning. Um
you know in machine learning we've had
to deal with systems that have
stochastic errors or uh you know
stochastic outputs and stoastic errors.
Um and you know we've had to deal with
these kind of systems for a long time
and error analysis is kind of a time-t
tested technique that you can use to
quickly find what number one what should
you invest your time in. There's so many
different moving parts in AI. you know,
there's so many different components of
your AI like should you tune your rag
system? Should you um you know, should
you do prompt engineering? Should you
invest in a framework? You know, people
have these questions, but really like
error analysis will guide you and help
you know what to invest in and also what
to measure. So like what do you measure?

[00:04]
You can measure any everything. It's
infinite. And so uh it'll you know it
guides you and it almost like helps you
create your road map. Um and they
already talked about okay error analysis
is not new. It's not something we're
making up. This is something that a lot
of people don't know about especially if
you don't have a data science
background.
Cool. So we're not going to be able to
go through all of these steps of error
analysis today, but we're going to go
through the first and the second as much
as the third as we can. But we like to
think about error analysis as
multi-stage. How do you go from zero to
having some set of emails that are
custom for your product? First, you
start with literally looking at your
data and annotating it. What are example
inputs your system might have? What are
example outputs? Um, how do you what are
the vibes that you have? Can you write
those vibes down on an output byoutput
basis? Then the second step is to take
all of your free form notes and

[00:05]
categorize them into groups. Um so you
you can use LLMs to do this. We found
that that's somewhat effective
especially at a smaller scale and maybe
you can try really advanced clustering
techniques if you would like but some
way to kind of group these nodes
together. Then what HML likes to call um
turning your outputs into a pivot table.
But basically in lay that's which
outputs correspond to which categories
and how many errors you have per
category. Given this kind of view over
your data it becomes much easier to
figure out okay how do I ship
improvements to my pipeline maybe I
change my prompts maybe I fix other
parts of my system maybe that in turn
creates new metrics and then finally
I've got to iterate go back to the
beginning keep looking at data. We find
that people kind of do this entire
process several times even before kind
of deploying their system. Um, and at

[00:06]
some point you become a lot more your
system becomes a lot more robust. It
doesn't really change throughout cycles.
You get newer met you get fewer and
newer metrics over time.
So today's lesson, we're going to have a
case study um where you've kind of put
together an AI recruiter, a very basic
AI recruiter that has a position that is
trying to hire for great a bunch of
candidate résumés. Um we actually got
them off Kaggle and is trying to write
personalized emails for these candidates
um when applying basically inviting
these candidates to apply for positions.
Um, and the problem that we have when we
try to wrote write this pipeline, we
used Llama 370B to generate these
emails, we just weren't really satisfied
with the vibes. Um, and I think this is
really common in a lot of people's cases
when they want to build evals. Like they
they built something, but they kind of
feel like the vibes are off and they

[00:07]
don't know how to turn that into
something actionable. Um, and we did try
a few rounds of prompt engineering, but
it felt like we fixed one thing and we
broke another. We didn't quite fix all
the things we wanted to. We were just
kind of ad hoc iterating on it. And Haml
has this excellent meme here. Maybe I'll
let him uh briefly mention it in the
backstory. Yeah. So, this is my friend
Greg Sakarelli. And you know, he's
playing this game of whack-a-ole. And
this is
exactly what you are doing if you try to
build an AI product without evals or
especially without looking at data. you
know, like you see a problem, you're
like, "Oh, let me fix it with prompt
engineering." See another problem,
you're like, "Oh, let me fix that with
like some, you know, tuning my rag or
whatever." And you just see a you just
keep hammering your these different
problems. But when you fix one thing, a
lot of times you're breaking another
thing. You don't really have a way of
knowing if you're making any progress.
And so, you want to avoid this. You want
to avoid this endless cycle that goes

[00:08]
nowhere with whack-a-ole.
Cool. All right. So, back to our case
study. Um, so I mentioned I got a data
set from Kaggle for this lesson. And
we'll we'll um post these slides later
on so you can look at if you would like,
but it's simply a collection of résumés.
Each réé, think of it as a blob. It's a
text string. Um, the only field that we
really care about here is this ré
string. Um, and we take a bunch of HR
um, HR category resumeumés and try to
write the customized emails to encourage
these people to apply for a university
admin/hrcoordinator. Um, so when we
wrote our pipeline, the prompt is very
straightforward. Right. It just kind of
details the job description and asks the
AI to write a personalized email that

[00:09]
references experience that references
the candidates's experience. We get some
good examples like what's on the left
and we get some bad examples like what's
on the right. And I I want to emphasize
a point here that even this is
subjective. People write email AI
assistance all the time and they have
their own criteria. Um but you know I'm
a basic person. I just want to make sure
it doesn't sound bad, but maybe what's
on the left seems pretty good. Um, but
what's on the right like doesn't have
good vibes. I was reading it. Haml and I
were reading it and I was like, okay.
Uh, maybe it first pulled the wrong I
don't know why it pulled the flight
attendant part of their resume, if at
all. It's a flight attendant part. Um,
it says, you know, although your
background is mostly in management and
customer service, uh, that's already
that feels like bad vibes. Hamilton said
it felt like a rejection email already.
It's like Yeah. Yeah, it definitely
does. Um, this like although your
background, any email starts with

[00:10]
although your background, I'm like,
"Okay, I just got rejected from
something."
Uh, yeah, it's actually pretty funny
because Oh, go for it. No, I mean it's
like I feel like I get really bad emails
from recruiters all the time uh that are
just like maybe even worse than this.
So, this is very interesting. And sorry,
can I just ask, is it supposed to be to
the HR manager or from the HR manager as
well? It's going to be it's supposed to
be to an applicant. And another issue is
probably that it shouldn't say dear HR
manager. It should say dear that
person's name. Um, but a lot of these
réumés are they don't have the
candidates's name in them. So, I guess
the LLM just fills out some role there.
Honestly, I've I've noticed OpenAI is it
will switch recipient and sender quite a
bit. Gemini 3, sorry, Gemma 3 is a lot
better on this, I found. Interesting.
Well, that's a good failure mode to keep
in mind because when we look at the

[00:11]
data, I we're going to see that
switching the
roles. Um, cool. All right. So hopefully
this kind of illustrates the pipeline
that we're building and illustrates that
there can in fact be bad emails. Um and
and I don't have a great definition of
bad. That's another thing you should
keep in mind right now is we know we we
trust ourselves to identify bad vibes.
We cannot articulate what these vibes
are at this
moment. All right. So let's jump into
annotating some data.
Um, oops, I accidentally the slide. And
I
think one of the things that I want to
do first, I think I have to pull it up.
Maybe I can't. Oh, I I'm only sharing
the window. So, let me share my
um bigger screen al together.
Share
cursor.
Share. All right. So, I generated a

[00:12]
bunch of data and I could try to open
this in open
with don't know why it doesn't let me
open
it. Oh, I see zoom is in the
way with
numbers. Does that not
work? Guess
not. Okay. Well, I wanted to show that
just simply opening this in Excel
spreadsheet is not the right way to go,
which you can if you want. Um, there's
it's fine to totally just create new
columns to annotate your data on Excel,
but you know, a lot of this is just big
text blobs. Um, so I what I'm going to
try to do in this lesson is vibe code an
interface for us to label this data. So,
I hope it works. I've never vibecoded
live

[00:13]
before. Uh, but part of this is also
going to be me trying to come up with
the right prompt to give us a good
labeling interface. Um, I don't want to
show you all of the code that I used to
generate the outputs because I did
generate outputs with some known
books. Okay. So I want a
custom data labeling interface
uh for me to annotate my output of this
pipeline. I want there to be a view
with a single input
output on the
page. This
maybe the resumeé on the left and the
email in the
center and then an open ended text

[00:14]
feedback box on the right where I can
write any failure most I find in the
data. And then some other things that I
find when I like to build custom
interfaces are um I want there to be
some
shortcuts.
So have left and right hot keys to
quickly iterate through the rows.
Um, another thing that I really like is
have a table of
feedbacks
persistent maybe at the bottom right. I
typically find this helpful because
sometimes when I've written failure
modes for previous outputs, I just like
to see kind of a list of failure modes
at all times that I've generated so far.
Um, then what else do I want to have

[00:15]
generate this app in
Flask and HTML? I just don't really want
a whole React app generated at this
moment, but that makes sense. You could
do that if you want that. I It's just a
static app. It can be pretty chill. Um,
don't use
uh I do have like a old version of this
annotation app just to make sure that I
could have vibe coded this correctly.
Um, don't use any other don't use any
files from
annotation. This is pretty hacky because
I mean you probably won't have an
annotation at old. Oh, and the last
thing that I want is make sure that the
there should be a save
button. That's
important. Save export button to save
the
feedbacks along with the rows. Do you
have to tell it where do you want to
save it? Oh, does it usually I don't

[00:16]
know by coding. What do you What do you
tell it? Yeah. I think like before you
didn't have to. So maybe we Yeah, I
don't know. We'll see. I mean, I think
the key here if you're going to do this
yourself is to use uh Claw 3.7 or you
know, Sonnet 3.7 thinking mode in in
cursor. Make sure you have that turned
on. If you're going to vibe code it this
way.
Well, I don't know if I've never tried
it outside of Okay, so let's see. The
interface will display one res email in
the center, open-ended feedback box on
the right, arrow, navigation key. Yeah,
sounds
great. Oh, and I do have a custom system
prompt that like parrots back what I
said. I don't know how effective that
is, but I just like the idea. No, I like
it. Yeah, it's always good to have a
plan. So, yeah, make this. Why not? I'm

[00:17]
not in I'm not in the yolo phase yet of
my life where I can just out execute
arbitrary shell
commands right
I'm really excited I mean so the point
of doing vibe cod you might be wondering
like why are we vibe coding an app is to
drive home the point that like okay the
first step that you want to do is you
want to have a data uh your own custom
data viewer and we can talk about like
why that is but you're like you know
nowadays it's so easy to create your own
custom data viewer with AI assisted
coding and like probably more than half
of you already know that but some people
they they don't they're like oh like why
do you what do you mean like you know
create a custom data viewer well um yeah
it's just really straightforward like AI
is really really good at custom data

[00:18]
annotation apps and then you'll see like
why. Um, and then we'll I'll show you
some screenshots of actual data
annotation apps that I've built for
several other companies in a similar
amount of time that Shrea is going to do
it. So, Shrea is doing this like in
under probably like round trip spend
like significantly less than 10 minutes.
Um, I mean we'll we'll see. Maybe I
don't want to jinx it. Let's not jinx
it. Um, but we have some questions. All
right. So, we see why not use tools like
Label Studio or YOLO. This is an
excellent question. Um, I I used to try
to use tools or even Excel or Google
spreadsheets, but I found that I got to
a point where it just felt like a little
bit too much friction because when I see
say an email string in an Excel or like
in just thumb cell, I have to do the
mental work to view that like a email in

[00:19]
my head before I check the vibes. And
when you build your own annotation
interface, you can do small things like
have the email look like a email. Um you
could if say it's not email, say it's,
you know, code or you're generating
plots with AI, you could literally just
like render that um and then quickly
look at it. So I think it's it is
actually worth it to
um make your own custom interface and
it's just so easy right now with these
AI tools. Um, why custom HTML JS instead
of grado? I mean, you can use grado if
you want. I Yeah, use whatever you want.
Use whatever you want. Doesn't matter.
Use whatever you're familiar with,
whatever you want. It really doesn't
matter. You know, it's helpful if you
use what AI is familiar with. So, if you
use some kind of established, you know,
uh, design pattern or, you know,
frameworks or whatever, it does help. Go
ahead. Okay. So, it looks like you

[00:20]
already have something. So, something's
running. So let's see what it is folks.
So we are here with this custom email
annotation interface. Um and so
hopefully already you can kind of see oh
wow if I just gener like looking at this
like an email is better than looking at
this in some kind of crud viewer that is
pretty generic.
Um but maybe we can start by coding the
lives. Yeah. Yeah. Uh, let me make sure
that. Okay, so we got there. Oh, we we
didn't finish yet. All right, so we're
here. Um, so let's start by looking at
this. Okay, so already
um already Hugo mentioned a great point
here. We don't even know who this role
is. So maybe we should have instructed
the LLM
to fill in the recipient.
You just say greet greeting is
incorrect. for example, greeting is not

[00:21]
correct. And I think at least I like to
have somewhat more verbose feedbacks in
the beginning because it helps me reason
about what's going on. But greeting is
not correct, the
recipient could be um the name of the
person or
blank if the
resume does not have the name. And
another error is uh this salutation I
guess you call it or is that the best
regards your name the placeholder is
there?
Ah yeah um yeah we can say the
uh is it called salutation? I don't know
I don't know what it's called.
Closing the
uh best
regards. That's a ham. Have to look that
up.
pull that out of them.
All right. And then actually reading the
content. Um, let's take a moment to read

[00:22]
it. Oh, no. I think salutation is the
beginning.
Sorry. But whatever it is, the Yeah, the
goodby the end. Um, I think it's okay.
Yeah, it seems solves the challenge. Our
team is
supportive. I'd love to discuss. Please,
let's schedule a call. I do like the
fact that it said please let's schedule
a call. Um, sometimes I find that people
also mention things that they like
because then you could go back and find
common things you like and encode that
back into the prompt. But yeah, let's
save this. And then the hotkey worked by
the way. I just pressed my arrow. So
that's exciting. That's huge. Hot keys
are huge because you want to make it you
that it really reduces the pain if
you're doing this like thousands of
times. Totally. This is great. This is
exactly the issue that Hugo mentioned,
right? you're the LLM just like
understood the assignment wrong. It's
not that the candidate is trying to
apply for this role. It's that we are
the recruiter trying to get the
candidate to apply for this role. So, um

[00:23]
understood which then this one is
hilarious. This one is like there's so
many things going wrong. Just uh yeah,
this really got the assignment wrong. Um
I I can't wait to get an email like this
from a recruiter. the recruiter be
amazing like reply with something asking
the candidate to apply not the candidate
asking to
apply and then um
irrelevant background so so the thing I
want you to pay attention to here notice
that Shrea is adding notes free form
notes okay we don't know what the errors
are yet the most important thing is like
we're going through different examples
and we're writing these notes in free
form. Um, we're not trying to like apply
categories or no like we're not labeling
yet. It's too premature for that. So,
like we're doing error analysis

[00:24]
correctly, especially in the beginning.
You want to just observe what you see
and just write notes and then we're
going to talk about okay like what do we
do with those notes? Yeah, this was a
horribly irrelevant everything was wrong
with it. quantum physics. I don't even
need to mention that. Um, so note that
we're also going slowly and that's like
totally okay. We're gonna go slowly. You
should go slowly. Like people spend
minutes per output on the first several
outputs. Like think of this as like
spending an hour going slowly. It's
going to give you a huge pay payoff.
Um, okay. So with your extensive
interest in data analysis and software
development,
okay, so one of the things that I
realized that I would like to have is
the ability to search the resume for
things that the AI actually said. Um,
analysis. Yeah, I don't think this
person looks like an HR director,

[00:25]
so it kind of bungled the
Yeah, it could have inferred. Yeah,
they conferred the wrong experience.
Yeah. So, you have to think, okay,
you're not trying to root cause it just
yet. You're just writing down what's
wrong. Root causing can come later.
Right now, we're just Yeah, you're just
like writing down what's wrong. Okay.
Like, why did this happen? Why is it
thinking that this person has data
analysis, software uh development
experience? Maybe there's something
wrong with prompt construction or rag or
something. We don't know. We don't know
yet. We're just We're just recording
what's wrong at this point.
Yeah. Oh, interesting. Web page develop.
Okay. Sorry. I'm doing exactly what you
said, which is not Don't try to triage
why AI kind of infer the wrong thing.
Just say what happened, which is this.
Um, so we keep going.
We're excited to introduce you to this

[00:26]
customer service.
Okay. What does it say? We
believe clients and manage
conflicts. Um
I It's kind of weird vibes honestly, but
establish clients and manage conflicts.
I'll probably say at this point I would
change the data annotation. We're not
going to do it now, but I would also add
the job post in here for sure. Yes. Yes,
that's a good point. So searching the So
this is very common actually when I
generate a annotation interface like
finding out that there's new things that
I wanted after I generated it and then
going back and edited which now we can
vibe code having search functionality in
the resume as well as the job posting
here. Um I'm not going to put any
feedback on this honestly. I think it's
fineish for now. We can keep going.

[00:27]
Um, all right.
So, I was impressed. I was impressed
with your
background. I believe your skills are
helpful. But I do feel like since I've
seen Conflict Revolution twice, like
maybe this is just a smell of the
language model that I I just don't like.
Like, yeah, please don't infer skills
from their resume that are not listed. I
mean, to be honest, I don't like any of
these, but I didn't I wouldn't know
that. I mean, I would now I have a
really distinct
like recommendation I would make or I
have a really good idea like, okay, I
don't like all this BS like
introductions. I was impressed with your
experience. You would make a great
contra, you know, make contribution to a
role. Like, when you see that, you just
have PTSD from thousands of recruiters,
right? Like, you're free. You're hurt.
Okay. So like how do you make it good?
Okay, like I want something that like is

[00:28]
something very specific to that person,
you know? So I would based upon what I
see right now, I would say, okay, like
that's not maybe we don't want to have
that feedback just yet, but that's
something I would write down and say,
okay, I need to rethink this whole
application, you know, I want these like
recruiter emails to be like really good.
So hire him as your product engineer.
But you know AI recruiters are writing
emails like this. Yeah, you can you can
have your own vibes. The point is you
can encode your vibes into your
annotation and back into your pipeline.
I agree with that.
Yeah. Again, this annotation is really
important. Like you know writing notes,
the writing notes part forces you to
think about what is happening. And I
promise you that these notes are going
to turn into something extremely
valuable. Yeah. Um although your
background is mostly in HR and
administration, this is exactly what you
said.

[00:29]
Um it's not good vibes. And you could
say basic things like it's not good
vibes.
Yeah. I mean I would say it feels like a
rejection. Um came across your resume.
Impressed by experience like Yeah.
impressed by your experience.
Um, okay. And you don't like impressed
by experience? I don't like it. Yeah.
It's just overused. Don't
like anything.
Okay.
Yeah. Again, I know we are being on a
soap box here, but you can write your
own feedbacks
here. This is not Yeah. You can write
whatever you like here. But this is this
is how it looks like when people you're
like okay what is looking at your data
what does it mean? This is what it means
like this is actually what it looks
like. It's it looks mundane but if you I
promise you if you do this on your own
data for your AI product you're going to

[00:30]
in just half an hour or so you will come
away
with really significant you know
takeaways.
I guess it's fine. I don't have as high
bar for you as you do. I know you don't
like impressed by.
Yeah, you could be. Yeah.
Another thing I would like to do is
expand. I don't like one question is why
do we why do we start with a manual
audit instead of letting an LLM do
initial feedback and adjusting it as
needed. Don't do that. Do not use
question to do don't jump straight into
tools like you need to put your own eyes
on the data because the LLM is just
going to lead you astray. Honestly,
you're going to be grounded in what that

[00:31]
LLM is saying. Um, yeah. And you need to
kind of get an idea yourself. Yeah, I
see this a lot. It's people ask the LLM
to judge it without having read at least
10 outputs and then they look at the LLM
feedback and they're like, "Yeah, I
totally agree with it." And but if they
were to do this independently of the the
LLM as we are doing, the LLM is not
coming up with maybe it'll come up with
this irrelevance thing, but it's not
going to get our vibes down. Um, and
it's totally worth spending the hour
annotating. You're building a whole
company, a whole product out of this.
Um, it's worth looking at your data
100%. Now, after you do this, and we'll
talk about this in our course later of
how you can use LLM as judge to kind of
scale up the vibes that you're coding,
but when you start out, you got to look
at your data. Um, I think this is just
too verbose.
Yep. It's very verbose. Am I reading I
don't even want to read it. I'm going to
move on. But definitely, it's kind of

[00:32]
verbose. Yeah. And also, I don't like
the fact that it says the budget twice.
Yeah. And you don't have to nit you
don't have to nitpick it too much. Like
in the feedback, if there's one thing
that is just like the smoking gun of why
it's wrong. Like if it's too verbose,
that's totally fine just to do that. You
don't have to like identify every single
problem.
Oh, okay. This one is super interesting
to me because it it shows literally one
of the phenomena that I study as a
researcher, which is how your criteria
drifts over time. You know, previously I
said I did not like the fact that it
would mention irrelevant things.
However, I I feel like if that were
phrased in the right way, like a PS, I'm
also interested in blacksmithing and say
I was super into that, I would enjoy the
email. I don't know, maybe Haml, you
have a really high bar for the so you

[00:33]
wouldn't. I think it's interesting. Um,
yeah, the PS I also enjoy one that's a
little bit dangerous for AI to write. Uh
but uh that's a that's a good Yeah,
that's like an interesting direction
honestly. Yeah, I mean he could maybe
pull that from like the profile of the
recruiter or the hiring manager,
but that's the kind of Yeah, that's the
kind of thinking that you might even
though it's irrelevant, but the reason
but I only like it
mentioned
explicitly as
something as a hobby.
unrelated and and I highly recommend you
don't have to type in the feedback. M
Sher is going to type the feedback right
now, but use like a voice transcription
app like Mac Whisper, Whisper Flow,
whatever. Over time, it really reduces
the strain of you know providing the

[00:34]
feedback.
this. Well, okay. So, another thing that
we would vibe code again on this if we
had more time is so our feedback box
should not be like one line anyways. So,
so um we get a bunch of stuff. Yeah. So,
like one question is do you balance
affirmative and critical feedback? I
usually like in the very beginning I
actually focus on critical feedback. If
it's good I just skip it. Later on you
want to maybe get affirmative feedback
if you're trying to fashion an LLM as a
judge. Um but that's you know that's
beyond this like foundation level. So
my answer to that is in the very early
stages I would start with critical
feedback. Start with whatever is you
feel like is the better direction you
would tell a human. Um so if the LM is
like doing a lot of things well that you
didn't explicitly detail in your prompt
and you want to preserve that. Um that's
an affirmative feedback. But if like
most of your feedback when you look at

[00:35]
the data is the vibes are off, you can
focus on critical stuff. Um, all right.
So, I know we don't have that much time.
We're probably going to go 5 minutes
over to 11:55, but I want to move on to
the next part. Um, which is how we can
kind of take this and turn this into
eval criteria. Um, so I've done this
with like you can export your
annotations if you would like, but for
the sake of time I'm just going to copy
paste it into a chat
GBT. Um, so a good prompt that might be
here is I've been coding my data. So
coding is um a term used in qualitative
research. really what we're doing here
um kind of
systematically taking notes open-ended
notes on outputs um so I'll say coding
my data to identify things I don't like
in it here are some of the

[00:36]
feedbacks I've
given note that this is in order um
later
feedbacks represent my updated
thinking and then you could really ask
it things like what are the three most
common failure modes.
You can do that or you can just tell
give you categories and you can apply
them. Um you
know but you can do that too. I mean
whatever the idea is like look you don't
like so you have written all these notes
right and you can get AI to categorize
those notes into you
know failure modes that then you can
analyze and then you can count okay so
like you know you see you see these like
sort of ones that it's writing right now
like redundancy verbosity
u misrepresenting hobbies or interests

[00:37]
whatever and then you know
clean it up. Now, you could do more
programmatically generate like a list of
categories and then you would ask the
LLM to then go back with this list and
then categorize those notes. Okay. And
then you would basically classify those
notes into these various categories.
Um, you know, one note can have multiple
categories.
Um, okay. So, yeah. No, it's Yeah, for
the interest of time, we won't do that
today. I mean, it's a 50-minute lecture,
but sign up for our course or go to our
future lightning lessons and we're going
to kind of keep moving on this. Yeah.
So, I mean like you can categorize these
notes and we don't have time to show
that, but basically you can categorize
each of those notes and have a pivot
table even and just count like okay,
what errors are occurring the most and
you'll be very surprised. You'll see a
lot of patterns in your data. We already
saw some patterns in the data we were
looking at and that will help you

[00:38]
prioritize like what do you work on you
know like what you should go fix you
know should you go do you have a
retrieval problem do you have you know
is it clearly a prompting issue for X Y
and Z and then it also helps you focus
on what to measure you know instead of
all these generic metrics helpfulness
score conciseness score toxicity score
all this stuff which is frankly [ __ ]
and it hurts you if you applied those
generic metrics most of the time. It's
like now you have concrete things you
know are wrong and then you can sort of
go after that. Um okay so takeaways from
this lesson one you should build your
own data annotation tool. Shrea did it
in like five minutes in front of you
just to drive home the point that you
can do
it. Um
number two write free form notes and
categorize them. You know don't try to
categorize too early. Just write your
notes, observe the data. Number three,
you're like, "Okay, how many of these
should I do?" So, one thing that Treya

[00:39]
articulates, which I really like, is
keep doing it until you feel like you
aren't learning anything
new. And number four, like this is the
foundation of evals. This is at the very
ground level. Before you do anything
else, before you think about eval
measurements, all this experiments,
whatever, you need to do this step. If
you don't do this step, then your your
evalu process is not going to work. And
number five is this is the you'll get
immense value out of this part. Um you
can't skip it. Yeah. Um we had a
question around what if you had a really
large data set, it's a certain
percentage we should annotate or we just
try and improve. Um I Hugo mentioned
look at 20 and you'll get a sense.
Everyone has their own magic number. For
me, I just like to do 30. Um, but
sometimes if I will stop if I feel like
I'm not learning anything new. I think
that's the real stopping criteria. If
you feel like, you know, when you're
you've looked at five more examples, 10

[00:40]
more examples, and you didn't find any
failure modes that you had already
observed before, you can call it and
then iterate. And Shrea, I just said 20
because a number is forced. And I
honestly if you look at 20 you'll
probably then look at 30 and then you'll
be like oh this is interesting and I
want to look at more and you'll get
addicted to it and if you don't maybe
you want to build other things as well.
If you don't enjoy looking at data maybe
you're in the wrong game.
Yeah. Yeah. Looking at 20 is like a mind
like a Jedi mind trick to like just
begin.
That's what we want you to do. Then
what's the step after categorizing
emails? Go back to prompt engineering.
Yeah, we'll talk about that in our
course. You if you're really early, if
you haven't done much prompt
engineering, um if you're seeing so many
failure modes already in 20 examples,
yes, definitely go back to prompt
engineering. You don't want to shift
something where like in every example
output you see the vibes are off. Um go
back to prompt engineering and then or
you could try to write lm's judge

[00:41]
prompts around each eval which we'll
talk about how to do later and then run
that on more examples. Yeah. All right.
All right, in the interest of time,
we'll stop here. Think thanks everyone
for coming. Was super successful for
first lightning lesson. I mean, tell all
your friends we're teaching a course.
We'll hopefully do a couple of more even
before the course. Um, and maybe we'll
take a question before before dropping
off.
So, let's see.

</details>


## Adding robustness with automatic graders

Armed with our taxonomy and dataset, we’re now ready to start automating the evaluation flywheel. The OpenAI Platform supports [a variety of grader types](https://platform.openai.com/docs/guides/graders) (including Python graders and LLM graders) that can be run in bulk on our dataset (learn more [here](https://platform.openai.com/docs/guides/evaluation-getting-started#adding-graders)). For this example, we can build and run LLM graders for the following:

* **Formatting grader:** assess whether the model’s response matches the desired format
* **Availability accuracy grader:** compares the availability returned by the model to a ground truth value you specify in your dataset

Our formatting grader is a fairly straightforward directive.
![Creating formatting grader](/cookbook/assets/images/creating-formatting-grader.png)

Our availability accuracy grader will reference additional input columns we’ve added to our dataset to capture business hours and day availability.
![Creating availability grader](/cookbook/assets/images/creating-availability-grader.png)
![Ground truth columns](/cookbook/assets/images/ground-truth-columns.png)

With automated graders in place, we can easily evaluate our performance on any change to our system — an updated prompt, updated model parameters, or newly discovered edge cases.

For more detail on how to get graders right, see our section on “Aligning your LLM judge” below.

## Optimizing the prompt

We’ve now identified and classified our errors, and built out grading to automate our flywheel. At this stage, we could choose to use our data to inform manual changes to our prompt. However, the OpenAI Platform supports an automatic [prompt optimization tool](https://platform.openai.com/docs/guides/prompt-optimizer) that speeds up this process.

The prompt optimizer takes our generated output, our custom annotation columns, and our graders into consideration to construct an improved prompt. We’ve constructed a fairly small example here, but with a full-fledged dataset (say, with the 50 rows we recommended earlier), the optimizer will produce a new prompt that solves many of our identified errors.

We may find ourselves wanting to iterate further, by re-annotating new model outputs, adding or refining graders, and re-optimizing. Graders and annotation column specifications are preserved across tabs, so we can continue to create additional prompt versions in new tabs as we work. The tabs also allow us to compare performance across different models, so we can use our graders to measure which model parameter configuration performs best.

This process enables us to improve our prompt over time, proactively responding to new errors or new model releases.

## Advanced techniques

### Expanding datasets with synthetic data

The core evaluation flywheel is your primary tool for improving your system. However, there are times when you may need more test data than you can gather from production logs. Synthetic data generation is a powerful, additional technique for these situations. It is particularly useful if you want to more extensively explore a specific failure mode, if you haven’t shipped your product yet and need initial data, or if you have a hypothesis about a weakness but lack real-world examples to validate it.
Simply asking an LLM to “generate N examples” often produces a homogenous set of test cases. A more structured approach is to define key dimensions of a query and generate data across combinations of them, forming tuples. This ensures greater diversity and coverage in your test set.

For our leasing assistant, you could define dimensions such as:

* **Channel:** Voice, Chat, Text
* **Intent:** Tour Scheduling, Maintenance, General Info & Inquiries
* **Persona:** Prospective Resident, Agency

You can then combine these into a tuple like `(Text, Tour Scheduling, Prospective Resident)` and prompt an LLM to generate specific test cases that match this profile. This structured method creates challenging, realistic scenarios that a simpler generation process might miss.

In addition to varying the core components of the query, you can apply **perturbations** to make test cases harder and more realistic. This involves slightly altering your generated examples to test the system’s resilience. Common perturbations include adding irrelevant information, introducing mistakes, or using different slang.

For a deeper dive into this topic, see [this discussion](https://hamel.dev/blog/posts/evals-faq/#q-what-is-the-best-approach-for-generating-synthetic-data).

### Aligning your LLM judge

An automated LLM judge is only useful if its judgments are trustworthy. To ensure this, you must systematically measure its performance against a human subject-matter expert (SME) using a “gold standard” dataset.

However, most test sets are **imbalanced** — they contain far more “pass” examples than “fail” examples. This makes a simple accuracy score misleading. A judge that always guesses “pass” might be 95% accurate but will never find a single failure.

* **True Positive Rate (TPR):** How well does the judge correctly identify the *failures*?
* **True Negative Rate (TNR):** How well does the judge correctly identify the *passes*?

The goal is to achieve high scores on both TPR and TNR. This confirms the judge is effective at finding real problems without being overly critical. This measurement process uses a standard dataset split.

1. **Train Set (~20%)**
   This set’s only job is to provide the “few-shot” examples for your judge’s prompt. You will select a handful of clear pass/fail cases from this set and embed them directly into the prompt to give it a strong starting point.
2. **Validation Set (~40%)**
   This is where you will iteratively improve your judge. You run the judge against this set and analyze the cases where its decision differs from the expert’s. Tune the judge’s prompt instructions to improve both its TPR and TNR.
3. **Test Set (~40%)**
   This final, held-out set is your report card. After tuning, run the judge on this set one time. The final TPR and TNR scores confirm you haven’t overfit and give you a trustworthy measure of your judge’s performance.

For more guidance on how to align an LLM judge with your SMEs, see [this discussion](https://hamel.dev/blog/posts/llm-judge/). For more guidance on what model you should use for judging your AI, see [this post](https://hamel.dev/blog/posts/evals-faq/#q-can-i-use-the-same-model-for-both-the-main-task-and-evaluation).

## Next steps

This cookbook provides a foundational workflow for building resilient prompts, but the evaluation flywheel doesn’t stop after one cycle. The next step is to make this process a core part of your engineering practice by integrating your graders into a CI/CD pipeline and monitoring production data to discover new failure modes.

In addition, the world of AI evaluations is deep and full of challenges we couldn’t cover here. As you work to build out your eval strategy, you’ll likely encounter more complex questions, such as:

* How do I make the case for investing in evaluations to my team?
* Why is a binary (pass/fail) evaluation often better than a 1-5 rating scale?
* What is the best way to debug a complex, multi-turn conversation trace?
* How should I approach evaluating my RAG system?
* How does this workflow adapt to agentic systems?

We recommend exploring [this FAQ about Evals](https://hamel.dev/blog/posts/evals-faq/) for further study.
