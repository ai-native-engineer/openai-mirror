---
title: "OpenAI o3 & o4-mini"
channel: openai
url: https://www.youtube.com/watch?v=sq8GBPUb3rk
youtube_id: sq8GBPUb3rk
published: 2025-04-16
duration: "25:50"
captions: en-orig
---

# OpenAI o3 & o4-mini

[![OpenAI o3 & o4-mini](https://img.youtube.com/vi/sq8GBPUb3rk/hqdefault.jpg)](https://www.youtube.com/watch?v=sq8GBPUb3rk)

<details>
<summary>자막: OpenAI o3 & o4-mini (25:50)</summary>

[00:00]
Hello and welcome. I'm Greg Brockman.
I'm Mark Chen. I lead research at
OpenAI. There are some models that feel
like a qualitative step into the future.
GVD4 was one of those.
Today is also going to be one of those
days. We are going to be releasing two
models, 03 and 04 mini.
These are the first models where top
scientists tell us they produce
legitimately good and useful novel
ideas. We've seen great results in
law. Talking to one of my co-workers
yesterday, he said that 03 came up with
a great idea for system architecture.
It's like we we haven't really seen
anything like this.
And the thing that's really amazing
about these models is that they're not
just models. They're really AI systems.
We've trained them to use tools, which
is not something that we had done with

[00:01]
our previous reasoning models. They
actually use these tools in their chain
of thought as they're trying to solve a
hard problem. For example, we've seen 03
use like 600 tool calls in a row trying
to solve a really hard task.
And we're going to be making these
models incrementally uh available
starting today, rolling out as quickly
as we can in our API and chat GBT. And
one thing that's very near and dear to
to my heart is their ability in software
engineering and not just producing sort
of, you know, oneoff pieces of code, but
really working in real code bases. I I
found that these models are actually
better than I am at navigating through
our OpenAI codebase, which is really
useful. Definitely better than I am. has
sealed for me a long time ago. Yes. Yes.
But it just helps you get so much more
done. And so we're really excited to
bring these to the world and see what
you will all do with them.
The reason we're so excited about tool
use is that it makes our reasoning
models that much more useful and that
much
smarter. Just as you might use a

[00:02]
calculator to solve a difficult math
problem or you might use a map app to
navigate through unfamiliar streets, our
models, when paired with the right
tools, become that much more powerful.
With that in mind, we combined our O
series reasoning models with our full
suite of tools to achieve
state-of-the-art results across a bunch
of very hard benchmarks including Amy,
GPQA, Code Forces, and Sweetbench. And
just to illustrate the power of tools,
it can also give a lot of new
functionality. For instance, we now can
have the models think with images. And
what that means is that the model can
use Python to manipulate, crop and
transform images in service of the task
that you want to do. This means that
today you can upload complicated images.
You can upload blurry upside down images
and the model will handle that without
any problems. Now these advancements are
powered by continued algorithmic
advances in our RL paradigm. We've
continued to scale both train time

[00:03]
scaling and test time scaling. And one
thing that makes me so excited about
these models is just you know one or two
weeks ago I saw that there was a new
paper in condensed matter physics right
and it used 03 mini high to aid in the
proof of a new unsolved theorem and I
really do believe that with this suite
of models 03 and 04 mini we're going to
see more advances like that. So here we
have two of our researchers we have Eric
and Brandon and they're going to show us
a demo. Yep. Hi I'm Brandon McKenzie. I
work on multimodal reasoning at OpenAI.
Hi, I'm Eric Mitchell. I work on post
training along with lots of other folks
for our O series models. All right,
we're going to show you some things that
uh 03 can do. Uh I'll start with a
science example. So this will be a
physics poster. So I'm going to let uh
03 start thinking now so it can take its
time. Um what I'm going to feed it is a
poster of uh some physics internship
that I did in 2015, so 10 years ago. And
uh this poster or the project was

[00:04]
supposed to estimate a quantity called
the proton is vector scalar charge. It's
a beyond the standard model of particle
physics uh quantity that tells you how
short inter short range interactions uh
uh how strong they are. And what you'll
see is that the model 03 is is zooming
in. It's kind of like browsing around
here. I'll zoom out just so we get a
little bit better view. And it is it is
kind of looking for the right quantities
for uh for the question I asked it which
is to basically find this result that I
had and compare it to recent literature.
But there's a small twist. Uh the result
actually isn't in the poster. And that's
because I didn't have it yet. Uh so
although it's in like the final paper
for this project, it's not in this
poster. And uh I'm actually asking 03 to
do the rest of the project for me
essentially. He uses the same trick at
OpenAI. Yeah. It's true. It's true. Uh
great. So, it found the plot that I
wanted it to find. Uh, it's supposed to
figure out that it needs to like find
the slope of this plot, extrapolate down
to a specific like physical cork mass
and then like grab that quantity and

[00:05]
then actually apply another quantity to
normalize that value. Um, and I think it
is already kind of figured out that this
is what it should do, but it is just
spending a little bit more time
exploring the image. Okay, it's good.
It's it's it's now going to browse the
web for recent results. Yeah. Why is it
searching the web? Uh well I think I
actually did I did I ask it? I said oh
yeah find any recent findings that have
like updated estimates. So now it's like
just looking at like the literature and
seeing what people have done and how it
compares to the result that well that it
thinks that I eventually arrived at. And
how long do you think it would take you
to do this task? Uh quite a long time.
Uh yeah so I mean it took me a long time
just to remember uh what my poster even
meant in the first place. Uh and it also
I also didn't even realize that the
result wasn't wasn't there when I first
asked it this question. and it actually
told me that uh which was nice. So many
days just for me to even like onboard
myself back to my my project and then uh
a few days more probably to actually
like search through the literature and I
mean it it must have just read you know
at least like 10 different papers in a

[00:06]
few seconds for me. So that's that's a
huge time savings. Uh great. So it has
uh summarized my my result here and
these numbers look uh correct to me. So
it's figured out like there's like this
unnormalized value that it's like
estimated by extrapolating and that when
you multiply by this specific uh
constant that it will renormalize it and
it says okay you would have ended up uh
with this which is somewhat close. I
think it ended up around like 1.2 in my
my paper and uh then it compares with
the actual literature here. So there's a
few different estimates and uh looks a
little close I'd say. So let's see what
it says. Uh, it says my bare value looks
high because it needs to be reormalized.
That's correct. Uh, after you multiply
by that, you get something that's more
consistent with the state-of-the-art
results. That's great. Um, but it says
my precision isn't isn't as good as the
state-of-the-art, which is fine. Uh, you
know, it was an internship. Not bad.
Exactly.
I'll take it. I'll take it. So, it seems
like it's still a reasonable estimate

[00:07]
that maybe has a little bit more
uncertainty than uh recent results,
which is great. So, the field has made
progress uh which is awesome to see.
That's such a cool example. That's super
cool. Cool. Now I'll hand it off to Eric
for for his example. Cool.
Yeah, it's tough to go after uh a demo
like that, but uh I'm going to I'm going
to show another aspect of O3's
capabilities that I I also think is
super cool. Um as uh Mark and Greg have
said, um one of the the cool things
about these models is they can use all
of the tools that we have available in
CHIGBT. So I just turned on uh memory
for this model. So the the model knows a
few things about
me. Um and I'm gonna I'll get this one
started as well. And and so you know, as
people have said, models are super
smart, which is really really great, and
they can help us with, you know, even
cutting edge research in all sorts of
fields. But even if you're not literally
a researcher in particle physics, um
these this new intelligence and and
these these sort of you know more
agentic kind of abilities to use tools

[00:08]
is still useful and and it can still be
um you know very valuable um for for you
as well. And so what I've asked 03 here
is just based on what you know about me.
So you know it has access to memories
now um read the new read the news and
and teach me something that I probably
didn't know but that I would find really
cool in particular. Um, and so, you
know, this is going to involve, you
know, knowing something about me, but
also doing some of this agent, uh, you
know, thinking and and tool use to to
look up, um, some potentially relevant,
you know, interesting things. Um, and
and and here I've also asked it to
actually plot some, you know, some data
or information that I could put in a
blog post if I wanted to tell people
about this this cool new fact. Um, and
so what it what it's done here is, uh,
some of my interests are scuba diving
and and playing music. Um, and so it's
it's sort of combined these interests
and it's actually found um this this
line of research that was actually kind
of mind-blowing to me um which I didn't
know about until I like actually was
working on this demo where um
researchers actually make recordings of

[00:09]
healthy coral reefs and then they
literally play back those recordings
underwater with an underwater speaker
and that actually accelerates the
settlement of new coral and and even
fish to sort of heal that coral reef and
have it regenerate more quickly. And so,
um, this is like an actual line of
research in like coral reef
preservation. Um, and it and it it was a
very cool sort of synthesis of like
both, you know, like underwater like,
um, exploration and and also, uh, music.
And so, um, here we have a nice blog
post. So, the model is sort of smoothly
both browsing, it's using advanced data
analysis to show and plot some data for
me. It's using canvas to generate a blog
post. Um and it's you know summarizing
at the end with some citations you know
what it found and and where it got those
results from. So um again you know the
these models are super super smart which
is awesome and I'm really really excited
about it. Um and and and I think this
new intelligence and sort of ability to
use tools will be useful whether you are
you know literally at the frontiers of
some scientific field um or you are you
know integrating this model in your

[00:10]
everyday workflows. I wonder if like
what you can maybe play sound for a
physicist too and uh improve their
results. Yeah. What should we play at
work? We should sound a healthy healthy
healthy physicist. What does a healthy
physicist sound like, Brandon?
I'll look into that. I'll ask three.
Cool. Thank you guys both for showing
these really compelling demos. Uh, next
we'll have Wenda and we'll have Ana come
on and talk a little bit about how the
models are trained and also what the
evals are like. Great. Thanks a lot.
Thanks. Thank you both,
man. Super incredible.
knowledge work and also even if you're
just doing something that's highly
personalized, it's very useful. And to
me, the the magic is that under the
hood, it's still just next token
prediction, right? It's just a model
that's just thinking about what should
come next with sprinkles of RL. Exactly.
We've changed the objective. We trained
where the data come from and now we're
able to really hook it up to the world.
Hi, I'm Wenda. I'm a researcher at
OpenAI and I work on scanning RL

[00:11]
systems. I'm Ana. I'm a researcher at
OpenAI and I worked on some of the
algorithms for these models. Uh so we
wanted to start out by showing some
results on standard benchmarks for these
models in math, coding and science. So
in these plots, the dark yellow bars are
the new set of models and the light
yellow bars are the old set of models
and we see a pretty substantial boost.
So on AM which is a hard math contest 04
mini gets 99% accuracy with tools pretty
much saturating the eval on code forces
these models get over 2700 which place
them in the top 200 contestants in the
world and GPQA is a set of hard PhD
level questions and 03 gets over 83%.
Which is pretty incredible. It's pretty
good. We want to go beyond the eval
numbers which are incredible and show
you a little bit how our model uses
tools in order to solve those problems.
Uh so here for example we have a problem
from the AM math contest and the problem
here is uh asking you to look at this

[00:12]
grid of 2x2 squares and count the number
of conditions of coloring that verify
some constraint and let's see how the
model does it. Yeah. So the way the
model thinks is really cool. So it
starts out by producing a brute force
program and then runs it using a Python
interpreter and it gets the right answer
which is 82. But this is messy, right?
It's pretty inelegant. And the model
recognizes that and then simplifies its
solution and comes up with a smarter way
of doing things. It then also doublech
checkcks its answer to increase its
reliability, which is kind of
neat. Now these models are not just
trained to output the right answer.
They're also trained to be useful. So in
this case, it now gives the solution in
words to explain it to a human. What I
found really cool here was we didn't
train the model uh to use certain
strategies directly. We didn't say
simplify your solution or double check.
It just organically learns to do these

[00:13]
things which is pretty incredible. Yeah,
it's super cool that comes up with
essentially the intelligent solution
here that a human would be able to do
whereas the first brute force solution
of course um you would never have time
to do that in the actual
contest. So beyond uh math science we
also want to share you know a lot of you
I know use these models for coding I
want to share some practical coding
benchmarks. So on sweet answer and a
polydot we achieve state-of-the-art
results with the model when it's allowed
to use tools end to end without any
harness or any specific uh things like
this and to illustrate a bit more I want
to share a sweet bench example with all
of
you so for this example uh I'm running
it uh with 03 high in the API with
access to the container tool
unfortunately it will take us a couple
more weeks uh to put the final polish on
a tool running in the API and so you
won't be able to run this today but I
want to share this because I'm so
excited about how the model is using the
tool. So the problem the model is asked
to tackle is the following. Um it's uh
concerning a bug in this package called

[00:14]
senpai which is a python package which
is used to manipulate symbolic
mathematics and uh I'm prompting the
model with the question and I'm also
giving the model access to a container
which is a virtual machine and with the
simp repository pre-loaded. So the model
has access to a shell with all the code
already there and the model will have to
figure out the
bug. So the cool thing is that the model
starts by just double checking what I'm
saying and seeing whether you know it
observes the same thing you know like I
would do when someone bugs me about
something. I'm just going to check you
know you know is it actually a problem
and the model does see oh yeah it seems
to print out max of two x with the round
brackets and the square brackets. I bug
Wendo a lot and he does
that and he always has good questions
though.
Yeah. And then after this um just to
double check it will check that you know
sign is now rendering correctly. So this
is the square brackets is the internal
behavior and the bug we're trying to fix
essentially. And so the model will go
around and browse the code and try to
kind of get the lay of the land of the
repository. And to do this it just uses
a common terminal tools that we might

[00:15]
use in our day-to-day work. So like a
list of files. It opens the file we said
and it will kind of print out the
relevant files and try to find what it's
looking for. After some browsing,
eventually the model figures out that
maybe it can check this thing called the
MRO, which is a Python construct that
tells you about the inheritance of uh
the class. And then based on the
previous knowledge that the model has
acquired, it notices that that something
is wrong. And this uh class is not
inherit from function but from
application. And so the model browses
around a little bit more and eventually
figures out that there's a good solution
here. We can change this file to
implement this. So use apply patch
applies a patch and then um hopefully
this is the right solution.
Fi to confirm this the model runs a unit
test just like any good engine would to
double check that you know it has gotten
the right thing and sees that indeed now
it's printing with the square
brackets. So this was a really cool
route and it's really cool to see the
model kind of arranging this all by
itself own. This route was actually on
the shorter side of Sweet Bunch and
there were about 22 interactions and
16,000 tokens. uh in some cases the

[00:16]
model uses more than a 100 container
interactions and on average it uses 37.
So it's pretty cool that it can do these
long rollouts with so many container
interactions and get the right answer.
Yeah, doing a roll out that long with
reliability is not trivial at all. It's
really hard. Yeah. Uh we also wanted to
show some numbers for standard
multimodal benchmarks and uh these
numbers are just crazy on MMU, Math
Vista, Charive and Vstar. Uh so we
really hope these models are useful for
your multimodal tasks as well. Yeah,
this is really you know applying the
reasoning paradigm to multimodel which
was previously not possible and now as
Brandon demoed the model is able to
manipulate the image directly in the
chain of thought and that leads to a
huge increase in capability for
multimodel. Yeah finally want to share
another few evals that uh we run
externally. Uh so humanity tax exam as
you can see our 03 model is able to get
close to deep research uh but 03 will
run much faster and of course much fewer

[00:17]
rate limits in charge if you are using
it in charge. Uh so we think it's a very
cool model if you do not need a full
report like what deep research produces
but instead I still interested in some
agentic behavior uh to kind
information. So in these plots we show
the performance on the y-axis against
the estimated inference cost on the
x-axis and we see that 04 mini is quite
a bit better than 03 mini for any given
inference cost. Additionally uh one
thing that is not shown here is that 04
mini is a multimodel model and like 03
mini. So if you need a small and fast
multimodel reasoning model um yeah I'm
very excited for you guys to try out O4
mini.
The results for 03 are even more stark.
Um you can see that for uh it can get
the same performance with way less
inference cost and if you're willing to
pay the same amount as 01 then you get a
much higher score. Um so these are
pretty amazing models. Yeah. And this is
why we're going to replace the 01 models

[00:18]
with the new ones. Yes. Um one thing we
should mention quickly is that due to uh
of the optimizations we've done to make
the reason more cost efficient and also
the model more useful in general. Uh it
is not as benchmark optimized as the
numbers we shared for the 12 days of
Christmas. So there might be some small
disparities uh up and down. It generally
has gone up in multimodel for example.
Uh we still hope that we still think
that this is a much better model because
it's much more optimized for real world
use cases and you won't have to wait as
long when you're asking for an answer
which you know is a real thing with
these reasoning models. People are
impatient. I I am impatient.
So these models are a result of a lot of
rigorous science, ingenuity and
craftsmanship and we put in more than 10
times the training compute of 01 to
produce 03. Um, and it was a lot of hard
work by lots and lots of people, but the
end result was really beautiful to see.
As we scaled up compute on the x-axis,

[00:19]
the performance on eval like Amy just
kept going up. Yeah. So, this is really
us, you know, going and retracing our
steps through the GPT series, right,
which was this kind of predictable scing
and pre-training. And now the goal is
really we're trying to get through this
scaling in RL and showing that as we put
in more RL comput, we're also able to
get commentary gains.
Yeah. 04 look like. Yeah. I think if we
just draw the line, you know,
110% heard it here
first. Great. We're so excited for you
to try out the model. Thank you.
So, we've shown you the models, but we
have one more special surprise. Here to
show that to you are Fouad and Michael.
Hi, I'm Fouad on the agents research
team. I'm Michael, also on agents
research. You know, I remember seeing a
couple years ago the codeex demo and it
was just so wild to see how far we've
come with these new speedbench numbers.
Yeah, that that model in that demo was

[00:20]
kind of the first time that anyone had
seen what is now called vibe
coding. What a great term. I wish we had
it at the time.
And I you know we we called that model
codeex because I you know we it really
captures the fact that code is so so
integral to to what we were trying to
train the model to do. Um and so today
what we're going to show you is the
continuation of the codeex legacy. Um
we're going to be releasing a series of
applications that we think will define
what the future of programming looks
like. And today we're starting with the
first one. Great. Yeah. Today we're
excited to share codeex CLI. It's a
lightweight interface to connect our
models to our users and their computers.
You can think of it like a reference
implementation for how to safely deploy
code executing agents where you need
them. It's built on top of public APIs
like the responses API taking advantage
of new features like chain of thought
summaries in that API and our latest
models like 03 and 04 mini with
multimodal reasoning capabilities. But

[00:21]
enough talk let's actually see a demo.
Michael. Awesome. So, I went online to
see what people had built with 03 mini.
And so, I found this cool image to ask
you generator. Um, the author said that
they built it with 03, but I'm pretty
sure they meant 03 mini. So, unless they
were time travel. Yeah. Right. And so,
um, so I thought today we would
reimplement this using codeex and 04
mini just from the post. And so, I'll
start out actually by just by taking a
screenshot. And I'll take the screenshot
and I'll drag it to my
terminal. And so, give it to Codeex. And
so as you can see I've passed it in
using the image flag. And so codecs will
start using that multimodal reasoning uh
that we saw earlier from O for mini. And
one amazing thing about using these
models directly on your computers. You
can take any file any codebase that
you're working in. Just go and grab
that, put it into codeex. And um here we
can actually see um some of that chain
of thought that we were talking about
earlier. Um you know it's asking for
some clarifying questions. It's thinking
about things and then it actually looked
at the image and even suggested a few
things that we might want to do with it.
What did you do you have in mind? Uh, I
mean, I thought we would just

[00:22]
reimplement what we what we saw in the
post. Yeah. But I mean, since we're
live, maybe we'll make it a little bit
more fun. Let's uh add the web camera
API. And just for the folks watching on
the live stream, maybe let's make sure
we keep it in the 16 by9. I don't want,
you know, some uh some some really small
uh um little video, but you want to go
and try that? Uh, that sounds bold, but
I like it.
All right. So while it's thinking, I
think one of the amazing things about
codeex is that you can actually see it
both think and also run the tools
directly on your machine. So like what
they mentioned earlier with function
calling in the API, you can actually
expose any of the existing functions
that you would use and in the future
we'll have the full suite of tools
you'll be able to use in the API. And
while it's thinking, do you want to
maybe talk a little bit about how it
actually runs the commands? We can start
to see it actually running some commands
now. Yeah. So by default, Codex runs in
what we call suggest mode. And so it's
as it's running it suggests commands to
edit or uh commands to run or files to
edit and you get to approve each one. Um
but that can get a bit tedious. And so
for the sake of the demo I ran it in
what we call full auto mode. Yeah. And a

[00:23]
little bit about full auto mode. It's a
mode where you can allow the agent to go
off and do its work but still stay safe
and secure. So it's able to run commands
network disabled and limit the edits
that it makes to the directory that you
ran it in. So it gives you the peace of
mind of actually having something that
can go off and do things but without the
risks that come with just letting it run
whatever command it wants. And it looks
like it's already it's pretty fast. So
it's already done. It's already done.
You want to pull it up? Yeah. So it said
it created this ASKI uh HTML file. So
let's go pull that up. Uh got to give it
some permissions. Always need some
permissions. And let's see. Oh, nice.
Oh, it even has a little width slider.
Uh not quite what I thought a width
slider would do. Oh, but it's low res
us. I I love I do love the low res
version. You want say hi? There we go.
Hi. Nice. Amazing. Um so as you can see,
it's it's so fun to use codecs. We've
been using Codex, actually build Codeex,
and we're incredibly excited to see what
you do with it now that it's fully
available. And not only is the tool
available, but we're also open sourcing
all the code. So, you can go up as of a
few minutes ago to our GitHub,
OpenAI/Codex, and go check it out. You

[00:24]
can even use Codex to explain the repo
to you. We're incredibly excited to see
what you do. Alongside Codex CLI, we're
also announcing a $1 million open source
initiative to support projects with API
credits using our latest models using
Codeex CLI to accelerate the frontier of
open source. We'll have a link in our
research blog post for more information.
But with that, I'm going to hand it back
over to Mark. Thank you both. Thank you
both so much. Um, I want to talk a
little bit more about chat GPT
availability. So starting today, if you
are a pro plus team subscriber, you're
going to we're going to start rolling
out access to 03, 04 mini, and 04 mini
high. And as you saw from Ana's post,
these are strictly better than the
previous generation of models. So they
will be replacing the 01 and 03 mini
series of models that we had before.
You're going to have to wait a week if
you are enterprise or edu. And if you
use 01 Pro today and you love it, we are
going to roll out 03 Pro, but it will
take us some time to make sure all of

[00:25]
the you know last remaining features are
tied up. We are also releasing these
models in the API. Um in upcoming weeks
we will release tool usage in the API as
well. So uh that will be really exciting
to see what people do with them. Um
these models huge huge amount of work
making them available um from the entire
team. Uh, and so it's been a real labor
of love to bring these to the world and
we really view them as a major step
forward in our mission of bringing AGI
to benefit all of humanity. And so
they're very useful for scientific
applications, but we also think that
they will be useful in your daily life.
And so please use them, explore what
they're capable of, and we're just so
excited to see what you'll do with them.
Thank you. Thank you to the team.

</details>
