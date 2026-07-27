---
title: "GPT-4 Developer Livestream"
channel: openai
url: https://www.youtube.com/watch?v=outcGtbnMuQ
youtube_id: outcGtbnMuQ
published: 2023-03-14
duration: "24:28"
captions: en-orig
---

# GPT-4 Developer Livestream

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
