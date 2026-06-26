<!-- source: https://openai.com/index/gpt-4-research/ -->

March 14, 2023

[Milestone](/research/index/milestone/)

# GPT‑4

[Read paper(opens in a new window)](https://arxiv.org/abs/2303.08774)[View system card(opens in a new window)](https://cdn.openai.com/papers/gpt-4-system-card.pdf)[Try on ChatGPT Plus(opens in a new window)](https://chatgpt.com/chat)

More Resources

[Try in Playground(opens in a new window)](https://platform.openai.com/playground)[Rewatch demo livestream(opens in a new window)](https://youtube.com/live/outcGtbnMuQ?feature=share)[Contribute to OpenAI Evals(opens in a new window)](https://github.com/openai/evals)

<!-- yt-inline:outcGtbnMuQ -->
[![GPT-4 Developer Livestream](https://img.youtube.com/vi/outcGtbnMuQ/hqdefault.jpg)](https://www.youtube.com/watch?v=outcGtbnMuQ)

<details>
<summary>자막: GPT-4 Developer Livestream (24:28)</summary>

[00:00]
to the GPD4 developer demo live stream.
Honestly, it's kind of hard for me to
believe that this day is here. OpenAI
has been building this technology really
since we started the company, but for
the past two years, we've been really
focused on delivering GPT4.
That started with rebuilding our entire
training stack, actually training the
model, and then seeing what it was
capable of, trying to figure out its
capabilities, its risks, working with
partners in order to test it in real
world scenarios, really tuning its
behavior, optimizing the model, getting
it available so that you can use it. And
so today, our goal is to show you a
little bit of how to make GP24 shine,
how to really get the most out of it,
you know, where it's kind of, you know,
weaknesses are, where it's we're still
working on it, and just how to really
use it as a good tool, a good partner.
Um, so if you're interested in
participating in the stream, uh, that if

[00:01]
you go to our Discord, so that's
discord.gg/openai,
there's comments in there, and we'll
take a couple of audience suggestions.
So the first thing I want to show you is
the first task that GPD4 could do that
we never really got 3.5 to do. And the
way to think about this is all
throughout training that you know you're
constantly doing all this work. It's 2
a.m. the pager goes off. You fix the
model and you're always wondering is it
going to work?
Is all this effort actually going to pan
out? And so we all had a pet task that
we really liked and that we would all
individually be trying to see is the
model capable of it now. And I'm going
to show you the first one that we had a
success for four but never really got
there for 3.5. So I'm just going to copy
the top of our blog post from today.
Going to paste it into our playground.
Now this is our new chat completions
playground that came out two weeks ago.
I'm going to show you first with GPT 3.5
4 has the same API to it, the same
playground. The way that it works is you

[00:02]
have a system message where you explain
to the model what it's supposed to do
and we've made these models very
steerable. So you can provide it with
really any instruction you want,
whatever you dream up and the model will
adhere to it pretty well and in the
future it will get increasingly
increasingly powerful at at steering the
model very reliably.
You can then paste whatever you want as
a user. the model will return messages
as an assistant. And the way to think of
it is that we're moving away from sort
of just raw text in raw text out where
you can't tell where different parts of
the conversation come from, but towards
this much more structured format that
gives the model the opportunity to know,
well, this is the user asking me to do
something that the developer didn't
intend. I should listen to the developer
here. All right, so now time to actually
show you the task that I'm referring to.
So, everyone's familiar with summarize
this. Let's say article into a sentence.
Okay, getting a little more specific.
Uh, but where every word begins with G.
So, this is 3.5. Let's see what it does.

[00:03]
Yeah, it kind of didn't even try. Just
gave up on the task. This is pretty
typical for 3.5 trying to do this
particular kind of task. If it's, you
know, sort of a very kind of stilted
article or something like that, maybe it
can succeed. But for the most part, 3.5
just gives up. But let's try the exact
same prompt,
the exact same system message
in GPT4.
So, kind of borderline whether you want
to count AI or not. Uh, but so let's say
AI doesn't count. That's cheating.
So, fair enough. The model happily
accepts my feedback. So, now to make
sure it's not just good for G's, I'd
like to turn this over to the audience.
I'll take a suggestion on what letter to
try next. In the meanwhile, while I'm
waiting for our moderators to pick the
the lucky lucky letter, I will give a
try with A.

[00:04]
Um, but in this case, I'll say GP4 is
fine. Why not?
also pretty good summary. So, I'll hop
over to our Discord. All right. Wow. Uh
people are are being a little ambitious
here. I'm really trying to put the model
through the paces. We're going to try Q.
Uh which if you think about this for a
moment, I want the audience to really
think about how would you do a summary
of this article that all starts with Q.
It's not easy.
It's pretty good. That's pretty good.
All right. So, I've shown you
summarizing an existing article. I want
to show you how you can flexibly combine
ideas between different articles. So,
I'm going to take this article that was
on Hacker News yesterday,
copy paste it into the same
conversation, so it has all the context
of what we were just doing. I'm going to

[00:05]
say uh find one common theme between
this article and the GP4 blog.
So this is an article about Pine Cone
which is a Python web app development
framework and it's making the technology
more accessible, userfriendly. If you
don't think that was insightful enough,
you can always give some feedback and
say that was not insightful
enough. Please, no, I'll just even just
leave it there. Leave it up to the model
to decide. So, bridging the gap between
powerful technologies and practical
applications. Seems not bad. Um, and of
course, you can ask for any other kind
of task you want using its flexible
language understanding um and synthesis.
You can ask for something like now turn
the GT4 blog post into a rhyming poem.
picked up on picked up on open evals
open source for all helping to guide

[00:06]
answering the call which by the way if
you'd like to contribute to this model
please give us evals we have an open
source evaluation framework that will
help us guide and all of our users
understand what the model's capable of
and to take it to the next level. So
there we go. This is consuming existing
content using GPT4 with a little bit of
creativity on top.
But next, I want to show you how to
build with GPT4, what it's like to
create with it as a partner.
And so the thing we're going to do is
we're going to actually build a Discord
bot.
I'll build it live and show you the
process, show you debugging, show you
what the model can do, where its
limitations are, and how to work with
with them in order to sort of achieve
new heights. So the first thing I'll do
is tell the model that this time it's
supposed to be an AI programming
assistant. Its job is to write things
out in pseudo code first and then
actually write the code. And this
approach is very helpful to let the
model break down the problem into

[00:07]
smaller pieces. And then that way you're
not kind of asking it to just come up
with a super hard solution to a problem
all in one go. It also makes it very
interpretable because you can see
exactly what the model was thinking and
you can even provide corrections if
you'd like. So uh here is the prompt
that we're going to ask it. Uh this is
the kind of thing that 3.5 would totally
choke on if you if you've tried anything
like it. Um but so we're going to ask
for a Discord bot that uses the GPD4 API
to uh read images and text. Now there's
one problem here which is this model's
training cutoff is in 2021 which means
it has not seen our new chat completions
format. So I literally just went to the
blog post from two weeks ago copy pasted
from the blog post including the
response format. it has not seen the new
image extension to that and so I just
kind of wrote that up in you know just
very minimal detail about how to include
images and now the model can actually
leverage that doc that documentation
that it did not have memorized that it

[00:08]
does not know
and in general these models are very
good at using information that it's been
trained on in new ways and synthesizing
new content And you can see that right
here that it actually wrote an entirely
new bot.
Now, let's actually see if this bot is
going to work in practice. So, you
should always look through the code to
get a sense of what it does. Don't run
untrusted code from humans or from AIS.
Um, and one thing to note is that the
Discord API has changed a lot over time
and particularly that there's one
feature that has changed a lot since
this model was trained.
give it a try. In fact, yes, we are
missing the intents keyword. This is
something that came out in 2020. So, the
model does know it exists, but it
doesn't know which version of the
Discord API we're using. So, are we out
of luck? Well, not quite. We can just

[00:09]
simply paste to the model exactly the
error message. Not even going to say,
"Hey, this is from running your code.
Could you please fix it?" We'll just let
it run.
And the model says, "Oh, yeah. Whoops.
The intense argument. Here's the correct
Here's the correct code.
Now, let's give this a try. Once again,
kind of making sure that we understand
what the code is doing.
Now, a second issue that can come up is
it doesn't know what environment I'm
running in. And if you notice, it says,
"Hey, here's this inscrutable error
message." Which, if you've not used
Jupyter Notebook a lot with Asyncio
before, you probably have no idea what
this means.
But fortunately
once again you can just sort of say to
the model hey I I'm using Jupiter
and would like to make this work
and you fix it
and the specific problem is that there's

[00:10]
already an event loop running. So you
need to use this nest async IO library
you need to call nest async io.apply
apply the model knows all of this
correctly instantiates all of these
these pieces into the bot. It even helps
you helpfully tells you, oh, you're
running in Jupiter. Well, you can do
this bang pip install in order to
install the package if you don't already
have it. That was very helpful.
So, now we'll run. And it looks like
something happened. So, the first thing
I'll do is
go over to our Discord and I will paste
in a screenshot of our Discord itself.
So, remember GPT4 is not just a language
model. It's also a vision model. In
fact, it can flexibly accept inputs that
intersperse images and text arbitrarily,
kind of like a document. Now, the image
feature is in preview. So, this is going
to be a little sneak peek. It's not yet
publicly available. It's something we're
working with one partner called Be My

[00:11]
Eyes in order to really start to develop
it and get it ready for prime time. But,
you can ask anything you like. For
example, I can't, you know, I'll say
GP4,
hello world.
Can you describe this image in
painstaking detail?
All right, which first of all, think of
how you would do this yourself. Uh
there's a lot of different things you
could latch on to, a lot of different
pieces of the system you could describe.
And we can go over to the actual code
and we can see that yep, we in fact
received the message, have formatted an
appropriate request for our API.
And now we wait um because you know, one
of the things we have to do is we have
to make the system faster. That's one of
the things that we're working on
optimizing. Um in the meanwhile, I just
want to say to the audience that's
watching, we'll take an audience request
next. So, if you have an image and a
task you'd like to accomplish, please
submit that to the Discord. Our
moderators will pick one that that we'll
run.

[00:12]
So, we can see that the Discord Oh,
looks like we have a response. Perfect.
So, it's a screenshot of a Discord
application interface. Pretty good. Did
not even describe it. It knows that that
it's Discord. There's probably Discord
written there somewhere where it just
kind of knows this from from prior
experience. um server icon label GPD4
describes the interface in great detail.
Talks about uh all the people telling me
that I'm supposed to do Q. Uh very very
kind audience. Uh and describes a bunch
of the uh the notification messages and
the users that are in the channel. And
so there you go. That's some that's some
pretty good understanding. Now this next
one, if you notice, first of all, we got
a post, but the model did not actually
see the message. So is this a failure of
the model or of the system around the
model? Well, we can take a look and if
you notice here, content is an empty
string. We received a blank message
contents.
The reason for this is a dirty trick
that we played on the AI. So, if you go

[00:13]
to the Discord documentation
and you scroll through it all the way
down to uh it's hard for me to even find
honestly to the message content intent,
you'll see this was added as of
September 2022 as a required field. So,
in order to receive a message that does
not explicitly tag you, you now have to
include this new intent in your code.
Remember, I said intents have changed a
lot over time. This is much newer than
the model is possible is possibly able
to know. So maybe we're out of luck. We
have to debug this by hand. But once
again, we can try to use GPD4's language
understanding capabilities
to solve this. Now keep in mind this is
a document of like I think this is like
10,000 15,000 words something like that.
It's not formatted very well. This is
literally a command a copy paste. Like
this is what it's supposed to parse
through to find in the middle of that
document that oh yeah message contents
that's required now. But let's see if it
can do it. So we will ask for I I am

[00:14]
receiving blank message contents.
Can you Why could this be happening?
How do I fix it?
So one thing that's new about GPD4 is
context length. 32,000 tokens is kind of
the upper limit that we support right
now. uh in the model is able to flexibly
use long documents. Uh it's something
we're still optimizing. So we we
recommend trying it out um but not
necessarily sort of really really
scaling it up just yet um unless you
have an application that really benefits
from it. So if you're really interested
in long context, please let us know. We
want to see what kinds of applications
it unlocks. But if you see it says, oh
yeah, me message messages content intent
was not enabled. And so you could either
ask the model to write some code for you
or you could uh actually just you know
do it the oldfashioned way. Either way
is fine.

[00:15]
I think that this is a augmenting tool
makes you much more productive. Um but
it's still important that you are in the
driver's seat and are the manager and
knows what's what's going on. So now
we're connected once again. And uh
Boris, would you like to rerun the
message?
Once again, we can see that we have
received it even though the bot was not
explicitly tagged.
Seems like a pretty good
pretty good description. Interesting.
This is an interesting image actually.
Looks like it's a dolly generated one.
Um, and let's actually try this one as
well.
So, what's funny about this image? Oh,
it's already been submitted.
So, once again, we can verify that it's
making the right API calls.

[00:16]
Squirrels do typically eat nuts. We
don't expect them to use a camera or act
like a human. So, I think that's that's
a pretty good explanation of why that
image is funny. So, I'm going to show
you one more example of what you can do
with this model.
So, I have here a nice hand-drawn mockup
of a joke website. Uh, definitely worthy
of being put up on my refrigerator.
So, I'm just going to take out my phone,
literally take a photo
of this mockup,
and then I'm going to send it to our
Discord.
All right. Going to send it to our
Discord.

[00:17]
This is of course the rockiest part.
Making sure that we actually send it to
the right channel,
which in fact I think maybe I did not
sent it to the wrong channel. It's
funny. It's always the uh the sort of
nonI parts of these demos that are the
hardest part to do.
And here we go.
Technology is now solved.
And now we wait.
So the thing that's amazing in my mind
is that what's going on here is we're
talking to a neural network and this
neural network was trained to predict
what comes next, right? It played this
this game of sort being shown a partial
document and then predicted what comes
next across an unimaginably large amount
of content. And from there it learns all
of these skills that you can apply in

[00:18]
all these very flexible ways. And so we
can actually take now this output. So
literally we just said to output the
HTML from that picture
and here we go.
actual working JavaScript
filled in the jokes for comparison.
This was the original
of our mockup.
And so there you go. Going from
handdrawn, beautiful art, if I do say so
myself, to working website. And this is
all just potential, right? We you can
see lots of different applications. We
ourselves are still figuring out new
ways to use this. Um, so we're going to
work with our partner. We're going to
scale up from there. But please be
patient because it's going to take us
some time to really make this available
for everyone.
So I have one last thing to show you.
I've shown you reading existing content.
I've shown you how to build with the

[00:19]
system as a partner. The last thing I'm
going to show is how to work with the
system to accomplish a task that none of
us like to do, but we all have to.
So, you may have guessed the thing we're
going to do is taxes.
Now, note that GPT is not a certified
tax professional, nor am I. So, you
should always check with your your tax
adviser. Um, but it can be helpful to
understand some dense content to just be
able to empower yourself to to be able
to sort of solve problems and get a get
a handle on what's happening uh when you
could not otherwise. So, once again,
I'll do a system message. In this case,
I'm going to tell it that it's tax GPT,
uh, which is not a specific thing that
we've trained into this model. You can
be very creative if you want with the
system message to really get the model
in the mood of what is your job? What
are you supposed to do? So, I pasted in
the tax code. This is about 16 pages
worth of of tax code. Um, and there's
this question about Alice and Bob. They
got married at one point. Uh, and that
here are their their incomes and they

[00:20]
take a standard deduction. They're
filing jointly. So first question, what
is their standard deduction for 2018?
So while the model is chugging, I'm
going to solve this problem by hand to
show you what's involved. So the
standard deduction uh is the basic
standard deduction plus the additional.
The basic one is 200% uh for joint
return of sub paragraph C, which is
here. Okay, so additional doesn't apply.
The limitation doesn't apply. Um okay,
none of these apply. Oh, wait. special
rules for taxable year 2018, which is
the one we care about, through 2025, you
have to substitute 12,000 for 3,000. So
200% of 12,000, 24,000 is the final
answer.
If you notice, the model got to the same
conclusion and you can actually read
through its
explanation. And to tell you the truth,
the first time I tried to appro approach
this problem myself, I could not figure
it out. I spent half an hour reading
through the tax code trying to figure
out this like back reference and why

[00:21]
there's subpar program like just what's
even going on. It was only by asking the
model to spell out its reasoning and
then I followed along that I was like oh
I get it now. I understand how this
works. And so that I think is where the
power of the system lies. It's not
perfect but neither are you. And
together is this amplifying tool that
lets you just reach new heights. And you
can go further. You can say okay now
calculate their total liability
and here we go it's doing the
calculation
honestly I every time it does it. It's
just it's amazing. Uh this model's so
good at mental math. Uh it's way way
better than I am at mental math. It's
not hooked up to a calculator. Like

[00:22]
that's another way that you could really
try to enhance these systems. But it has
these raw capabilities that are so
flexible. It doesn't care if it's code.
It doesn't care if it's language. It
doesn't care if it's tax. All of these
capabilities in one system that can be
applied towards the problem that you
care about, towards your application,
towards whatever you build. And so to
end it, the final thing that I will show
is I a little other dose of creativity,
which is now summarize this problem into
a rhyming poem.
And there we go. A beautiful, beautiful
poem about doing your taxes. So, thank
you everyone for tuning in. I hope you
learn something about what the model can
do, how to work with it, and honestly,
we're just really excited to see what
you're going to build. I I've talked
about OpenAI evals. Please contribute.
We think that this model, improving it,
bringing it to the next level, is
something that everyone can contribute
to and that we think it can really

[00:23]
benefit a lot of people and we want your
help to do that. So, thank you very
much. We're so excited to see what
you're going to build.

</details>


We’ve created GPT‑4, the latest milestone in OpenAI’s effort in scaling up deep learning. GPT‑4 is a large multimodal model (accepting image and text inputs, emitting text outputs) that, while less capable than humans in many real-world scenarios, exhibits human-level performance on various professional and academic benchmarks. For example, it passes a simulated bar exam with a score around the top 10% of test takers; in contrast, GPT‑3.5’s score was around the bottom 10%. We’ve spent 6 months iteratively [aligning⁠](/index/instruction-following/) GPT‑4 using lessons from our adversarial testing program as well as ChatGPT, resulting in our best-ever results (though far from perfect) on factuality, steerability, and refusing to go outside of guardrails.

Over the past two years, we rebuilt our entire deep learning stack and, together with Azure, co-designed a supercomputer from the ground up for our workload. A year ago, we trained GPT‑3.5 as a first “test run” of the system. We found and fixed some bugs and improved our theoretical foundations. As a result, our GPT‑4 training run was (for us at least!) unprecedentedly stable, becoming our first large model whose training performance we were able to accurately predict ahead of time. As we continue to focus on reliable scaling, we aim to hone our methodology to help us predict and prepare for future capabilities increasingly far in advance—something we view as critical for safety.

We are releasing GPT‑4’s text input capability via ChatGPT and the API (with a [waitlist⁠](/waitlist/gpt-4-api/)). To prepare the image input capability for wider availability, we’re collaborating closely with a [single partner⁠(opens in a new window)](https://www.bemyeyes.com/) to start. We’re also open-sourcing [OpenAI Evals⁠(opens in a new window)](https://github.com/openai/evals), our framework for automated evaluation of AI model performance, to allow anyone to report shortcomings in our models to help guide further improvements.

## Capabilities

In a casual conversation, the distinction between GPT‑3.5 and GPT‑4 can be subtle. The difference comes out when the complexity of the task reaches a sufficient threshold—GPT‑4 is more reliable, creative, and able to handle much more nuanced instructions than GPT‑3.5.

To understand the difference between the two models, we tested on a variety of benchmarks, including simulating exams that were originally designed for humans. We proceeded by using the most recent publicly-available tests (in the case of the Olympiads and AP free response questions) or by purchasing 2022–2023 editions of practice exams. We did no specific training for these exams. A minority of the problems in the exams were seen by the model during training, but we believe the results to be representative—see our [technical report⁠(opens in a new window)](https://arxiv.org/abs/2303.08774) for details.

internal reference [1](#citation-bottom-1)

Loading...

Loading...

We also evaluated GPT‑4 on traditional benchmarks designed for machine learning models. GPT‑4 considerably outperforms existing large language models, alongside most state-of-the-art (SOTA) models which may include benchmark-specific crafting or additional training protocols:

Loading...

Many existing ML benchmarks are written in English. To get an initial sense of capability in other languages, we translated the MMLU benchmark—a suite of 14,000 multiple-choice problems spanning 57 subjects—into a variety of languages using Azure Translate (see [Appendix⁠](#appendix)). In the 24 of 26 languages tested, GPT‑4 outperforms the English-language performance of GPT‑3.5 and other LLMs (Chinchilla, PaLM), including for low-resource languages such as Latvian, Welsh, and Swahili:

Loading...

We’ve also been using GPT‑4 internally, with great impact on functions like support, sales, content moderation, and programming. We also are using it to assist humans in evaluating AI outputs, starting the second phase in our [alignment strategy⁠](/index/our-approach-to-alignment-research/).

### Visual inputs

GPT‑4 can accept a prompt of text and images, which—parallel to the text-only setting—lets the user specify any vision or language task. Specifically, it generates text outputs (natural language, code, etc.) given inputs consisting of interspersed text and images. Over a range of domains—including documents with text and photographs, diagrams, or screenshots—GPT‑4 exhibits similar capabilities as it does on text-only inputs. Furthermore, it can be augmented with test-time techniques that were developed for text-only language models, including few-shot and [chain-of-thought⁠(opens in a new window)](https://arxiv.org/abs/2201.11903) prompting. Image inputs are still a research preview and not publicly available.

Loading...

We preview GPT‑4’s performance by evaluating it on a narrow suite of standard academic vision benchmarks. However, these numbers do not fully represent the extent of its capabilities as we are constantly discovering new and exciting tasks that the model is able to tackle. We plan to release further analyses and evaluation numbers as well as thorough investigation of the effect of test-time techniques soon.

internal footnote[A](#citation-bottom-A)

Loading...

### Steerability

We’ve been working on each aspect of the plan outlined in our post about [defining the behavior of AIs⁠](/index/how-should-ai-systems-behave/), including steerability. Rather than the classic ChatGPT personality with a fixed verbosity, tone, and style, developers (and soon ChatGPT users) can now prescribe their AI’s style and task by describing those directions in the “system” message. System messages allow API users to significantly customize their users’ experience [within bounds⁠(opens in a new window)](https://platform.openai.com/docs/usage-policies). We will keep making improvements here (and particularly know that system messages are the easiest way to “jailbreak” the current model, i.e., the adherence to the bounds is not perfect), but we encourage you to try it out and let us know what you think.

Loading...

## Limitations

Despite its capabilities, GPT‑4 has similar limitations as earlier GPT models. Most importantly, it still is not fully reliable (it “hallucinates” facts and makes reasoning errors). Great care should be taken when using language model outputs, particularly in high-stakes contexts, with the exact protocol (such as human review, grounding with additional context, or avoiding high-stakes uses altogether) matching the needs of a specific use-case.

While still a real issue, GPT‑4 significantly reduces hallucinations relative to previous models (which have themselves been improving with each iteration). GPT‑4 scores 40% higher than our latest GPT‑3.5 on our internal adversarial factuality evaluations:

Loading...

We have made progress on external benchmarks like TruthfulQA, which tests the model’s ability to separate fact from an adversarially-selected set of incorrect statements. These questions are paired with factually incorrect answers that are statistically appealing.

Loading...

The GPT‑4 base model is only slightly better at this task than GPT‑3.5; however, after [RLHF⁠](/index/learning-from-human-preferences/) post-training (applying the same process we used with [GPT‑3.5⁠](/index/chatgpt/)) there is a large gap. Examining some examples below, GPT‑4 resists selecting common sayings (you can’t teach an old dog new tricks), however it still can miss subtle details (Elvis Presley was not the son of an actor).

Loading...

The model can have various biases in its outputs—we have made progress on these but there’s still more to do. Per our [recent blog post⁠](/index/how-should-ai-systems-behave/), we aim to make AI systems we build have reasonable default behaviors that reflect a wide swathe of users’ values, allow those systems to be customized within broad bounds, and get public input on what those bounds should be.

GPT‑4 generally lacks knowledge of events that have occurred after the vast majority of its data cuts off (September 2021), and does not learn from its experience. It can sometimes make simple reasoning errors which do not seem to comport with competence across so many domains, or be overly gullible in accepting obvious false statements from a user. And sometimes it can fail at hard problems the same way humans do, such as introducing security vulnerabilities into code it produces.

GPT‑4 can also be confidently wrong in its predictions, not taking care to double-check work when it’s likely to make a mistake. Interestingly, the base pre-trained model is highly calibrated (its predicted confidence in an answer generally matches the probability of being correct). However, through our current post-training process, the calibration is reduced.

Loading...

## Risks & mitigations

We’ve been iterating on GPT‑4 to make it safer and more aligned from the beginning of training, with efforts including selection and filtering of the pretraining data, evaluations and expert engagement, model safety improvements, and monitoring and enforcement.

GPT‑4 poses similar risks as previous models, such as generating harmful advice, buggy code, or inaccurate information. However, the additional capabilities of GPT‑4 lead to new risk surfaces. To understand the extent of these risks, we engaged over 50 experts from domains such as AI alignment risks, cybersecurity, biorisk, trust and safety, and international security to adversarially test the model. Their findings specifically enabled us to test model behavior in high-risk areas which require expertise to evaluate. Feedback and data from these experts fed into our mitigations and improvements for the model; for example, we’ve collected additional data to improve GPT‑4’s ability to refuse requests on how to synthesize dangerous chemicals.

GPT‑4 incorporates an additional safety reward signal during RLHF training to reduce harmful outputs (as defined by our [usage guidelines⁠(opens in a new window)](https://platform.openai.com/docs/usage-policies/disallowed-usage)) by training the model to refuse requests for such content. The reward is provided by a GPT‑4 zero-shot classifier judging safety boundaries and completion style on safety-related prompts. To prevent the model from refusing valid requests, we collect a diverse dataset from various sources (e.g., labeled production data, human red-teaming, model-generated prompts) and apply the safety reward signal (with a positive or negative value) on both allowed and disallowed categories. 

Our mitigations have significantly improved many of GPT‑4’s safety properties compared to GPT‑3.5. We’ve decreased the model’s tendency to respond to requests for disallowed content by 82% compared to GPT‑3.5, and GPT‑4 responds to sensitive requests (e.g., medical advice and self-harm) in accordance with our policies 29% more often.

Loading...

Loading...

Overall, our model-level interventions increase the difficulty of eliciting bad behavior but doing so is still possible. Additionally, there still exist “jailbreaks” to generate content which violate our [usage guidelines⁠](/policies/usage-policies/). As the “risk per token” of AI systems increases, it will become critical to achieve extremely high degrees of reliability in these interventions; for now it’s important to complement these limitations with deployment-time safety techniques like monitoring for abuse.

GPT‑4 and successor models have the potential to significantly influence society in both beneficial and harmful ways. We are collaborating with external researchers to improve how we understand and assess potential impacts, as well as to build evaluations for dangerous capabilities that may emerge in future systems. We will soon share more of our thinking on the potential social and economic impacts of GPT‑4 and other AI systems.

## Training process

Like previous GPT models, the GPT‑4 base model was trained to predict the next word in a document, and was trained using publicly available data (such as internet data) as well as data we’ve licensed. The data is a web-scale corpus of data including correct and incorrect solutions to math problems, weak and strong reasoning, self-contradictory and consistent statements, and representing a great variety of ideologies and ideas.

So when prompted with a question, the base model can respond in a wide variety of ways that might be far from a user’s intent. To align it with the user’s intent within guardrails, we fine-tune the model’s behavior using reinforcement learning with human feedback ([RLHF⁠](/index/learning-from-human-preferences/)).

Note that the model’s capabilities seem to come primarily from the pre-training process—RLHF does not improve exam performance (without active effort, it actually degrades it). But steering of the model comes from the post-training process—the base model requires prompt engineering to even know that it should answer the questions.

### Predictable scaling

A large focus of the GPT‑4 project has been building a deep learning stack that scales predictably. The primary reason is that, for very large training runs like GPT‑4, it is not feasible to do extensive model-specific tuning. We developed infrastructure and optimization that have very predictable behavior across multiple scales. To verify this scalability, we accurately predicted in advance GPT‑4’s final loss on our internal codebase (not part of the training set) by extrapolating from models trained using the same methodology but using 10,000x less compute:

Loading...

Now that we can accurately predict the metric we optimize during training (loss), we’re starting to develop methodology to predict more interpretable metrics. For example, we successfully predicted the pass rate on a subset of the [HumanEval⁠(opens in a new window)](https://github.com/openai/human-eval) dataset, extrapolating from models with 1,000x less compute:

Loading...

Some capabilities are still hard to predict. For example, the Inverse Scaling Prize was a competition to find a metric that gets worse as model compute increases, and [hindsight neglect⁠(opens in a new window)](https://www.alignmentforum.org/posts/iznohbCPFkeB9kAJL/inverse-scaling-prize-round-1-winners#_The_Floating_Droid___for_hindsight_neglect_10shot) was one of the winners. Just like with another recent [result,⁠(opens in a new window)](https://arxiv.org/abs/2211.02011) GPT‑4 reverses the trend:

Loading...

We believe that accurately predicting future machine learning capabilities is an important part of safety that doesn’t get nearly enough attention relative to its potential impact (though we’ve been encouraged by efforts across several institutions). We are scaling up our efforts to develop methods that provide society with better guidance about what to expect from future systems, and we hope this becomes a common goal in the field.

## OpenAI Evals

We’re open-sourcing [OpenAI Evals⁠(opens in a new window)](https://github.com/openai/evals), our software framework for creating and running benchmarks for evaluating models like GPT‑4, while inspecting their performance sample by sample. We use Evals to guide development of our models (both identifying shortcomings and preventing regressions), and our users can apply it for tracking performance across model versions (which will now be coming out regularly) and evolving product integrations. For example, Stripe has used Evals to complement their human evaluations to measure the accuracy of their GPT‑powered documentation tool.

Because the code is all open-source, Evals supports writing new classes to implement [custom evaluation logic⁠(opens in a new window)](https://github.com/openai/evals/blob/main/docs/custom-eval.md). In our own experience, however, many benchmarks follow one of a few “templates,” so we have also [included the templates⁠(opens in a new window)](https://github.com/openai/evals/blob/main/docs/eval-templates.md) that have been most useful internally (including a template for “model-graded evals”—we’ve found that GPT‑4 is surprisingly capable of checking its own work). Generally the most effective way to [build a new eval⁠(opens in a new window)](https://github.com/openai/evals/blob/main/docs/build-eval.md) will be to instantiate one of these templates along with providing data. We’re excited to see what others can build with these templates and with Evals more generally.

We are hoping Evals becomes a vehicle to share and crowdsource benchmarks, representing a maximally wide set of failure modes and difficult tasks. As an example to follow, we’ve created a [logic puzzles⁠(opens in a new window)](https://github.com/openai/evals/blob/main/evals/registry/evals/logic.yaml) eval which contains ten prompts where GPT‑4 fails. Evals is also compatible with implementing existing benchmarks; we’ve included several [notebooks⁠(opens in a new window)](https://github.com/openai/evals/tree/main/examples) implementing academic benchmarks and a few variations of integrating (small subsets of) [CoQA⁠(opens in a new window)](https://github.com/openai/evals/blob/main/evals/registry/evals/coqa-ex.yaml) as an example.

We invite everyone to use Evals to test our models and submit the most interesting examples. We believe that Evals will be an integral part of the process for using and building on top of our models, and we welcome [direct contributions, questions, and feedback⁠(opens in a new window)](https://github.com/openai/evals).

## ChatGPT Plus

ChatGPT Plus subscribers will get GPT‑4 access on [chatgpt.com⁠(opens in a new window)](https://chatgpt.com) with a usage cap. We will adjust the exact usage cap depending on demand and system performance in practice, but we expect to be severely capacity constrained (though we will scale up and optimize over upcoming months).

Depending on the traffic patterns we see, we may introduce a new subscription level for higher-volume GPT‑4 usage; we also hope at some point to offer some amount of free GPT‑4 queries so those without a subscription can try it too.

## API

To get access to the GPT‑4 API (which uses the same [ChatCompletions API⁠(opens in a new window)](https://platform.openai.com/docs/guides/chat/chat-vs-completions) as gpt-3.5-turbo), please [sign up for our waitlist⁠](/waitlist/gpt-4/). We will start inviting some developers today, and scale up gradually to balance capacity with demand. If you are a researcher studying the societal impact of AI or AI alignment issues, you can also apply for subsidized access via our [Researcher Access Program⁠](/form/researcher-access-program/).

Once you have access, you can make text-only requests to the gpt-4 model (image inputs are still in limited alpha), which we will automatically update to our recommended stable model as we make new versions over time (you can pin the current version by calling gpt-4-0314, which we’ll support until June 14). Pricing is $0.03 per 1k prompt tokens and $0.06 per 1k completion tokens. Default rate limits are 40k tokens per minute and 200 requests per minute.

gpt-4 has a context length of 8,192 tokens. We are also providing limited access to our 32,768–context (about 50 pages of text) version, gpt-4-32k, which will also be updated automatically over time (current version gpt-4-32k-0314, also supported until June 14). Pricing is $0.06 per 1K prompt tokens and $0.12 per 1k completion tokens. We are still improving model quality for long context and would love feedback on how it performs for your use-case. We are processing requests for the 8K and 32K engines at different rates based on capacity, so you may receive access to them at different times.

## Conclusion

We look forward to GPT‑4 becoming a valuable tool in improving people’s lives by powering many applications. There’s still a lot of work to do, and we look forward to improving this model through the collective efforts of the community building on top of, exploring, and contributing to the model.

For more: [Read paper⁠(opens in a new window)](https://arxiv.org/abs/2303.08774) / [View system card⁠(opens in a new window)](https://cdn.openai.com/papers/gpt-4-system-card.pdf) / [Try on ChatGPT Plus⁠(opens in a new window)](https://chat.openai.com/chat) / [Try in Playground⁠(opens in a new window)](https://platform.openai.com/playground) / [Rewatch demo livestream⁠(opens in a new window)](https://youtube.com/live/outcGtbnMuQ?feature=share) / [Contribute to OpenAI Evals⁠(opens in a new window)](https://github.com/openai/evals)

## Appendix

Example of MMLU questions, translated into other languages. Note, we use consistent choice tokens (A–D):

Loading...

* [GPT](/research/index/?tags=gpt)
* [Language](/research/index/?tags=language)
* [Multi-agent](/research/index/?tags=multi-agent)
* [Transformers](/research/index/?tags=transformers)
* [Compute Scaling](/research/index/?tags=compute-scaling)

## Footnotes

1. A

   We evaluate this benchmark using Chain-Of-Thought prompting with 4 examples from the training set in-context. The specific prompt was tuned on the validation set.

## References

1. 1

   P. Arredondo (Casetext/Stanford CodeX), D. Katz (Stanford CodeX), M. Bommarito (Stanford CodeX), S. Gao (Casetext). Further analysis is available [in the paper⁠(opens in a new window)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233).

## Author

## Acknowledgments

[View GPT-4 contributions⁠](/contributions/gpt-4/)

## Related articles

![Three farmers using a mobile app outside](https://images.ctfassets.net/kftzwdyauwt9/7b26cc3b-46d8-45b0-f67f6de0c8f8/8bc94d083a5a147609cddad159243ef7/digital_green.png?w=3840&q=90&fm=webp)

[Building agricultural database for farmers

Jan 12, 2024](/index/digital-green/)

![Wix cover image](https://images.ctfassets.net/kftzwdyauwt9/6E3QyNLzuWwK3EGBHPw7nQ/fbd0c5a34cc4f4ba096028adbdda8934/oai_Wix_1x1.png?w=3840&q=90&fm=webp)

[Creating websites in minutes with AI Website Builder

May 29, 2025](/index/wix/)

![WHOOP Coach HIIT](https://images.ctfassets.net/kftzwdyauwt9/163d4817-6436-4d20-83e0963f68f1/ef4bec09f31b32f8ca8a953a09da5897/whoop.png?w=3840&q=90&fm=webp)

[Delivering LLM-powered health solutions

Jan 4, 2024](/index/whoop/)
