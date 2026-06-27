---
title: "Pre-Training GPT-4.5"
channel: openai
url: https://www.youtube.com/watch?v=6nJZopACRuQ
youtube_id: 6nJZopACRuQ
published: 2025-04-11
duration: "46:33"
captions: en-orig
---

# Pre-Training GPT-4.5

[![Pre-Training GPT-4.5](https://img.youtube.com/vi/6nJZopACRuQ/hqdefault.jpg)](https://www.youtube.com/watch?v=6nJZopACRuQ)

<details>
<summary>자막: Pre-Training GPT-4.5 (46:33)</summary>

[00:00]
How many parameters is it still or do we
not care? I think we should just Okay,
so usually when we do these, it's to
talk about a new product that we're
about to launch. Um, but we're gonna do
something a little bit different today,
which is to talk about the research that
went into our product. When we launched
GPT4.5, we thought people were going to
like it. We were very proud of the
model, but people liked it much more
than we thought. People would said all
kinds of things like, "I never thought I
was going to have this experience
talking about model. It's so different
than GPT4. It's way better in these ways
that are either obvious or hard to
explain or this or that." But uh there
was like a lot of interest about what
went into making GPT4.5. So today we
have some of the key team that made
GPT4.5 and we're going to talk about it.
Uh we're going to talk about sort of
like what went into it, what we learned
and just like what it takes to make a
giant model like this. Um actually maybe
we start with that. What does it take to
make a giant model like this? You go
first.
Uh a lot of people and a lot of time and
a lot of compute. Oh maybe you guys
should introduce yourselves. Alex, you
want to start? Sure. Uh yeah, hi I'm
Alex. Uh I work a lot on pre-tuning
data. I also led a pre-tuning ML for

[00:01]
GP4.5.
Uh I'm Amin Chian. I I'm open chief
system architect. I oversee systems and
networking broadly at OpenAI. I'm Dan. I
work on data efficiency and algorithms.
Yeah. Okay. So what what goes into it?
Um yeah, so I think we started this
project basically two years ago or or
so. Um and uh we kind of knew that we
had a big new cluster coming online. Uh
and we we kind of saw this on the
horizon and we started doing a bunch of
work to kind of convince ourselves uh of
the features that we wanted to include
in the run doing a lot of large
derisking runs building out a very long
plan for this um and kind of across the
full stack from systems ML everything.
Um and yeah it was it was a long story
of execution for uh d-risking it uh and
kind of preparing for the run um before
the run itself which you know itself was
a very large endeavor.
Yeah, I think it's a process that starts

[00:02]
at inception with a collaboration
between ML side and the system side and
goes all the way to the time that we
know what model precisely we want to
train and then it's starting the
uh run process in itself with the pace
that we are working at and especially
trying to make use of our most recent
computer that is made available to us it
becomes something that is difficult to
priority plan perfectly. Mhm. So we
almost always go into a launch with a
lot of unresolved issues
um and try to make forward progress
throughout the run despite all the
challenges. basically add more compute,
resolve all the issues that we probably
might not have anticipated despite all
the projections that we had both on the
ML side and the system side and try to
basically close the gap between what we
predicted should happen and what is
happening. uh I think that is at a very

[00:03]
high level uh and broadest stroke is the
entirety of the process and the tail end
of it is the execution which takes a lot
of people a lot of energy and momentum
for a prolonged period of time to go
through the training process
how how close do you feel like we were
to what we expected to happen to what
actually happened um on the usually at
the beginning uh I'm talking about the
system side of it. U we are usually far
away from where we expect it to be and
there is always a choice to delay the
launch and basically defer until more
and more issues are resolved or launch
early and try to basically figure it out
as we go. It's always a balance of
figuring out not to delay the process
unreasonably.
uh but almost always there are issues
that we don't necessarily know at the
inception that we are going to run into

[00:04]
and the entirety of the process is try
to uh handle the known to the extent
that we can and have a plan for what how
the run should
go and as we make progress just deal
with the unknowns which is the
variability on let's say if a run is
successful how long it would take and so
How far have they been? Well, yeah. I
think I guess one at the highest level,
I guess with this project, we set out to
do GPD4.5, which means like 10x smarter
than GPD4. So, that was sort of I think
the the initial goal starting like two
years ago that we had set our sights on.
Um, and then there's a lot that kind of,
you know, kind of happened along the way
of like, oh, we think, you know, can we
do better or worse? Um I think uh it was
a very complicated row but in the end we
got to a model that we feel hit this
mark of 10x smarter than 2P4 um in terms
of kind of the effective compute that we
we put into it. Yeah. On this execution
side of it of course initially it was

[00:05]
far far away from how uh long we thought
that is it did take longer than we
thought. Uh yes but I think the process
is to try to shorten it to basically
match what we would two two part
question about that. Why do why does
going from you know making up numbers
here 10,000 GPUs to 100,000 GPUs why
does that make the problem much harder?
Um a lot of issues it's I I do believe
that issues that you observe at the
scale if you have a very keen eye you
would observe them at a smaller scale.
It's not that they only manifest at
larger scale but something that is a
rare occurrence becomes something that
is catastrophic at a scale. uh
especially if you haven't anticipated it
being what are some of the kinds of
things that have become captured I mean
among those things is that I think is
quite well known is uh issues with uh
the infrastructure uh the failure rates
that you observe the the variety of
failures that you observe uh in both in

[00:06]
terms of the types of failures and also
the the count itself so we get to
observe something that I'm sure the
vendor hasn't observed because this is a
large pool of samples and we get to
observe the entirety of the statistical
distribution of uh a large pool of
resources that that we are executing on
the fabric the network fabric is always
part of it. the individual accelerators
part of it but at the end of the day
this is the beauty of it at at the same
time that almost everything needs to
work as expected for the result to hold
and the job is to basically minimize
that variance. Second part of the
question, obviously it's really hard,
this is for all of you, really hard to
do things at the edge of scale. Um, so
you know, even going as we go off and do
the next training run, even kind of
crazier. Um, but I've also noticed it
gets much easier to go do things that
are now no longer frontier. So it took
like hundreds of people, almost all of
OpenAI's effort to do GPT4.5.

[00:07]
If you guys could go pick whoever you
wanted, what is the smallest team from
OpenAI that could go retrain GPT4 from
scratch today with everything we know
and have and all the systems work? I
think to get to a GPT4 level model, it's
probably on the order of maybe five to
10 people. Yeah, we did it with that
type of that number of people with GBT4.
4.5 was different in the sense that a
lot of work history was a lot more
people come together and it was a very
different effort than before I would say
but now that we've done that work I
think like the stack we've improved a
lot and like if you were to retrain like
I mean we kind of did this a little bit
in the pro process of training GB 4.5 we
trained GBD40 which was a GP4 caliber
model that we retrained using a lot of
the same stuff coming out of the GP4.5
research program um and I think doing
that run itself actually took a a
smaller number of people, right?
What about from your perspective, Dan?

[00:08]
Or just sort of like why is why is
training big models hard? I think doing
anything new is hard. I think uh even
just finding out that someone else did
something, it becomes immensely easier
because the hard part is having the
conviction to do something in the first
place. I feel like just the fact that
something is possible is a huge cheat
code. That just makes it Yeah. Yeah. I
mean, we're always like we're scaling
10x beyond what we did before with these
GPT pre-training runs. And it's there's
always new things that you find that are
interesting that you couldn't have
anticipated necessarily. What do we need
for the next 10x or 100x in pre-training
scale? Data efficiency. What does that
mean? Easy answer. Obviously, I know,
but what does it mean? So, the the
transformer, the GPT is spectacular at
making productive use of of data. It it
absorbs information. And it it it
compresses and and generalizes to some
degree, but it's its defining character
its signature is absorbing the

[00:09]
information very efficiently with
compute. But there's a somewhat of a
ceiling to how deep of an insight it can
gain from the data. And so at some point
as the compute just keeps growing and
growing and growing and the data grows
much less quickly the data becomes the
bottleneck of this standard paradigm and
it requires some
algorithmic innovations to be able to
learn spend the compute more compute to
learn more from the same amount of
data. What do you guys think we need to
keep scaling in addition to that? I I
think this answer is system side. I
think even between different GPTs that
we have trained GPT 4.5
was the sheer
uh volume of work that was required to
basically the changes that were required
for us to make

[00:10]
uh was a byproduct of the model
specification the same we wouldn't have
been able to train uh GD4.5 on the
precise same stack as we did GP4. So
let's
say state management, our approach with
state management changed. We had to
scale to more compute and that compute
was not available as part of one
cluster. We had to go to multicluster
training. uh and imagine it's many many
different work streams like that that
have to come together in a short period
of time for us to be able to do this and
for making another 10x jump of course
and other issues that pri we previously
knew that they do exist it's just that
it's a choice for expediting execution
that we skip for this one for the next
one we have to do it there's no way
around it and it's always those choices
that basically make the timeline of do
building the perfect system take much
longer. Uh so we are always compromising

[00:11]
on what is the fastest way to get to
this result. The systems is not an end
in its own. the product that the thing
that it produces is so for the next 10x
for me it would be uh of course fall
tolerance not uh and a form of fall
tolerance that we can co-design with the
workload such that we don't have to
worry the operational burden of keeping
uh such a massive run going is not like
our prior system so I would argue that
with our prior stack 4.5 but at
edge of what we could keep up with. Do
you know what percent of steps failed in
the 4.5 run due to some component
somewhere? I actually don't have a
number off the top of my head, but it is
usually the way things work. This is a
fascinating thing.
Uh there are issues that are early on uh

[00:12]
in the lifetime of a new generation of
hardware is not necessarily well
understood or well studied. We
start the process and we want to make
forward progress in presence of such
issues. Of course the failure rates
are quite significant earlier in the
run. they're not necessarily
um it could very well be that once we
find the root cause and eliminate it the
total number of failures significantly
drops and this is often the case. It's
just that uh we learn more the infra
that is some would call it clean up of
the infra or understanding uh
fundamental issues about the infra uh
and the state improves significantly but
that earlier phase of execution is
almost always quite painful because we
are learning about what are the new
failure modes in the new uh uh and the
new infrastructure while making forward

[00:13]
progress. Of course later on um the
failure rates drop significantly the
uptime improves overall and so on but
it's just a matter of prior it is hard
to predict what this early phase of a
generation of infrastructures lifetime
failure risk would look like and
designing for the steady state might
result in very poor
um availability earlier on in the
process. Obviously, reasoning models are
a huge part of our future and you know,
but but if we were going to put this
aside for a second and think about just
how far we could go on classical
pre-trained models, assuming we had
unlimited GPUs and you know, unlimited
networking and unlimited power, but we
were stuck with all of our current
problems. The stuff still broke. We
didn't figure out fall tolerant
training. We only had the data we have
whatever else. How? and we kind of use
the convention of each major number of
GPT is 100x increment. Um how far could
we go like GPT what could we train with

[00:14]
what we know today?
I think on that we get to like a 5.5 ML
on the algorithm side I don't I don't
think there's like a clear limit that we
we found. I think um yeah I think we're
just kind of scratching the surface of
more data efficient algorithms uh and I
think better ways to leverage the data
that we have. Um it's very interesting
because I think up until this rough
point in time like if you look even
through GPD4 we were largely just in a
compute constrained environment. Um so
that was kind of where all the research
was going into but now we're you know in
a very different kind of regime. Um
starting with 4.5 for some aspects of
the data where we are much more data
bound. Um so there's now not a lot more
excitement about this research. It is a
crazy update that I don't think the
world has really groed yet. I should
pick a different one that the world has
understood yet. uh that we're no longer
compute constrained on the best models
we can produce. That's just like that
was so the world we lived in for so
long. What was the most interesting ML
thing we learned during the four five
training

[00:15]
that you want to share?
Oh
gosh.
Um or either of you. I don't know what I
could share. In general terms, I think
it is being off of the prediction and
trying to figure out why we're off of
the slope that we predicted to be on.
Yeah, I think that most surprising maybe
we can. Yeah, I think one of the more
surprising things that we found um was
just uh kind of how different aspects of
what we were working on on the ML side
and what we put into the run scaled and
and some things that did or didn't scale
well um that we we kind of discovered
through the process of training this
model. Um it was uh it it's yeah we've
learned a lot through this. I'd say the
the two defining characteristics of the
GPT paradigm has been that the law you
can predict the test loss and it scales
predictably and magically lower test
loss means greater intelligence in all
these intangible amazing mysterious

[00:16]
ways. Are you a maximalist on that? Do
you like fully believe that?
Well, I was going to say that one of the
interesting things we found from 4.5, we
tested it again and the model has all of
these incredibly nuanced abilities that
were not in in anyone's bingo card
specifically. We just like the
conviction was it's going to be more
intelligent in ways that are really hard
to characterize ahead of time. And then
you see in the deployment, you see in
the the user satisfaction
that it's smarter in all these very
subtle ways. It has more common sense
knowledge. It understands nuance and
context. And that's that's the magic
that came out of the few extra bits of
test laws. And I think that that part of
the scaling held up really well. What
was the most like positive moment of the
whole training run? What was like what's
like the favorite memory?
There's obviously lots of pain, but
hopefully that's somewhat fit. I I do
have one, but yeah. Um yeah, I can go.

[00:17]
Uh yeah, so one one that comes to mind
for me, um we uh kind of we've we worked
a lot on the ML of the run during the
run itself as well. And I think some of
the the changes that we made during the
run had a quite quite good impact. I
think uh maybe perhaps better than
anticipated. And this was a pretty
exciting moment for us. Yeah, I I think
for me this was probably the
biggest effort in terms of um I see time
during the run while we are building I
mean I mean running things we are
building things in parallel
um of
course to get there faster we are
parallelizing work aggressively
um and there is conviction that it will
pay off we will B passes performance
cliff that makes the model essentially
untrainable in terms of the time it
would take to to train. Um, and there is

[00:18]
a plan. Everybody's executing on it, but
it's taking long. It is a hard it's hard
work. Definitely harder than I imagined
it would be. My projections were off uh
by how long it would take to basically
get uh those issues resolved. and seeing
I think seeing the moment that the whole
team
once a few of those issues got resolved
we got a big performance boost after I
remember that everybody got I mean you
could sense that the energy changed it's
just that everybody feels excited and
now more motivated to push uh everything
through the end it's just it's
fascinating part of see the ETA on our
status tracker like yeah has constantly
shifted from let's say two years to uh
something uh tangible uh then the effect
it has on the morale of the team and
everything else is I think that was the
beauty of it the other part I would uh

[00:19]
call out is the ML side of it didn't
stop the ML code design part of this
didn't stop at the launch of uh at the
launch time and people tagged along
issues that were left to say we'll
figure it out later people were actively
working on it and shipping things that
helped
um with execution time. Uh and I think
that spirit of teamwork and basically
not having team boundaries of I did my
work I pass it on to you is something
very powerful. I was going to say
there's been a lot of focus on how the
run itself was challenging and
predictions were but this is despite a
tremendous amount of sophisticated
planning. Oh this is of course Do you
want to say more about it? By far the
most planning. Yeah, I think I mean like
I said, we we started basically working
on this project like a year before we um
even started training the run itself. Um
and through this we had a number of very
large de-risking runs. We we took a lot
of care to kind of very carefully

[00:20]
sequence all the changes that we wanted
to put into it starting from sort of
like very high confidence known good
config. You can think like GPD4, you
know, we really understand this this
setup um from an ML perspective and just
layering things in and being very
careful to very carefully study the the
scaling uh of all of the changes we're
making. So it's not just good enough
that we see some amount of wind. We also
want any any win from any new feature to
be like persistent across scale and not
to be tapering off. Lots of things look
good at small scale, don't look good at
large scale. Uh so we had to be very
very paranoid through this process. Um
and really I think we continue to
iterate on our scaling laws methodology.
We learned a lot on that front uh
through this de-risking process. Uh
that's continuing to guide us for future
GPGs. I I remember something I miss
about another very fun moment. Um
so there this is the torch sound. Uh but
imagine it is very unlikely that we

[00:21]
launch a run and it doesn't have bugs. I
mean all sorts of bugs. It is just a
given that uh but we need to make
forward progress and we need to be sure
that okay are we actually sure that this
is on track and these bugs are not super
negatively affecting the health of the
run. While we are absolutely sure we
were initially very sure that there are
bugs that are consequential. We do we
have built a lot of systems around
giving us visibility and ability to
distinguish
between is it a hardware fault, what
type of hardware fault it is, is it some
form of corruption or is it some ML
potentially an ML bug or something like
races in our code. Um what happened was
that we we of course had a few open
threads about all sorts of issues that
different symptoms uh all correctness
related issues. Um and at the end of the

[00:22]
day uh so so of course we have found
bugs fixed them and so on. We arrived at
this point that we have multiple open
threads and there's a lot of uh thought
around what is causing all these are
they different bugs or it's one bug and
causing all of these. Uh people went I
mean uh around the table and say
everybody vote which one do you think is
the most probable cause of this bug and
the one that turned out to be the bug
got the least votes. It's just that it
is a torch some bug a simple summation
and uh upstream pietorch and no what was
the bug? So the the bug is for the this
is funny because uh for this specific
code path we were triggering it and for
the for context remember that we are
mostly using triton kernels. It's just
that for some corner cases that let's
say the ops don't matter much we
basically fall back to I mean it is okay
to run torch ops uh and our specific

[00:23]
uh the specific code path I or data
triggered for uh in the torch sum
function uh was basically had a bug um
and it was only occurring very
infrequently. It's just that it's a it's
data distribution dependent and it was
triggering in in a good case illegal
memory accesses because it was computing
some offsets and some bit of memory. The
fun revelation at the end is that once
uh somebody fixed the bug I mean our
engineers figured out oh I found the bug
it is this line is torched some let's
ship a fix and see if it fixes
everything. uh it fixed all the way of
sanding bugs that where they had
seemingly distinct uh symptoms and it
was quite fun and everybody I think we
were renaming the slack channels of
multiple theory to single bug theory or
uh and um that was quite a lot of fun to

[00:24]
basically okay how when in the when did
that happen I can't remember now it was
live from very early days of the run up
until I I think good portion of the run
I would
um 40% in event. Do you guys remember
how someone found it? Uh I I do remember
that. I think it was in the list of so
imagine there there's a sequence of uh
kernel invocations and the um the second
one was the one that was triggering
illegal memory accesses and that was
some very complicated uh kernel that we
wrote. Um and of course our team would
suspect that there is a bug there.
Uh obviously there must be a bug there
and pe I mean several very clever people
just line by line everybody is looking
at it. A bug was found but we rolled it
out. Some of those issues disappeared
but not everything. And at some point

[00:25]
somebody was I mean in the list torch at
some was the one feeding inputs to this
kernel. One of the many inputs of this
kernel and somebody started uh one of
our engineers started looking through
the code and different code paths. I
said oh this very unlikely code path
that probably most people don't hit we
do hit. uh and he said okay this line is
buggy let's I mean of course the only
verification and validation we have for
it is ship the change observe if all the
crashes disappear and it did disappear I
think that was the validation we needed
so but uh it was
t I mean this is the thing it's just
that it's a crash at a very very I mean
a slow rate it's one every hundred step
one every thousand steps and it's
something very easy to dismiss
But it's just that we should not have
that in the run as a discipline that we
should we do have and it's just not
giving up on it is the the story.

[00:26]
Alex, I understand what your life is
like. I think most people can imagine it
like leading up to like pushing go on
the run, but after that happens like
what is your day-to-day like? Are you
just like sitting there watching loss
curves? Like how does it go? Definitely
a lot of watching lost curves. We all
did a lot of that. Um, no, I think uh
past that there's a variety of things
still trying to work with with systems
uh to uh kind of you know get out
improvements that we didn't get in um on
the code design front uh before launch
time. Um there's a lot of things that we
try to continuously monitor of the run
to see if anything is kind of trending
like we're not uh expecting. So this is
lost cursor but there's a bunch of other
statistics that we can look at. Um and
then yeah kind of uh working a bit
towards like any other kinds of
improvements we could we could do to the
run as well from an ML perspective. U so
on the data front it becomes less busy
immediately once you click go but uh
otherwise there's still plenty to be
done. I I think what we lean on for ML

[00:27]
is a lot of correctness. Imagine there's
a lot of noisy signal and you are at
times reading tea leaves. It's just is
this healthy or not. Of course if you
wait long enough you would know it was
it was it healthy or not. It's just that
the responsibility. And how often are
there false alarms there? Like how often
are you like, "Oh, this is looking
really bad." And then it's fine. Pretty
frequently I think probably about half
the time maybe because we're a paranoid
bunch. So I think yeah, if it wasn't
half the time we wouldn't be looking
closely enough. I have a short lightning
round of questions. Sure. If you could
have any one ML question answered before
the next big run, what would you most
like to know?
I think uh what we should what what
algorithms we should employ with uh for
for limited data in certain domains is
the main thing it's a kind of vague
question but big answer and if you could
have any change to current hardware you
could have like a new kind of network
invented or like a totally new chip
architecture what is the most what is
the limiter on systems at this point not

[00:28]
you don't get to like say like oh I want
yeah
so
where at this is a transport level
networking transport level change. It's
just that where there are faults that
uh could be worked around uh at a
different level than the application
level. I would rather
uh the transport the network transport
do its job and uh keep running and give
me the available bandwidth without me
worrying about it. Is there anything
promising on that front?
Uh yes, we can talk about Okay, that's
good. At least um two-part one for you,
Dan. Uh how so on the data efficiency
question? Humans, for whatever other
flaws we have about learning things, we
seem unbelievably data efficient. Yeah.
How far away is our very best algorithm
currently from human level data? Really
hard to measure apples to apples. I
think just like vibes
by in language astronomically far away

[00:29]
100,000 x00x
something in that in that range uh it
depends on whether you count every bit
of pixel information on the optical
nerve but but we don't know
algorithmically how to leverage that to
be human level at text so I think
algorithmically we're yeah quite quite
quite far away and it apples to apples.
And then part two is do you think with
our
current our like the direction of our
current approach we will get to human
level data efficiency or is that just
not going to happen and doesn't matter?
Well, I think for for decades deep
learning has been about compute
efficiency and what's what what's
magical besides the data and compute
growth is that the the algorithmic
changes stack so well. You've got
different people, different parts of the
world finding this little trick that
makes it 10% better and then 20% better
and they just keep stacking. There just

[00:30]
hasn't yet been that kind
of mobilization around data efficiency
because it hasn't been worth it because
when the data is there and your compute
limited, it's just not worth it. And so
now we're entering a a new stage of AI
research where we we'll be stacking data
efficiency wins 10% here 20% there. And
I think it would be a little foolish to
make predictions about it hitting walls
that we have no reason
to predict a wall. But but it's there
the brain certainly operates on
different algorithmic principles than
anything that's a small tweak around
what we're doing. So we have to hedge a
little bit there. But I think there's a
lot of reason for optimism. This next
one is the same question for all three
of you. Uh yes or no or you can add you
can add you can add explanation too.
Will humanity ever do a 10 million GPU
or greater synchronous pre-training run?

[00:31]
I don't know if it'll exactly be a
pre-training run, but I think there'll
probably be some kind of training run
that there will be 10 million GPU
training. Yeah. Yeah. Yeah. I don't know
if it'll look it'll probably look
totally different than what we're doing
today, but there will be something that
is kind of in the spirit of unsupervised
learning that is like at that scale. I
think I think so. I would call it
semi-synchronous. Uh and the scale of it
I hope so. I think it sounds very
interesting. You would call it
semi-synchronous you said? Yes. I think
not fully synchronous but it's just laws
of nature. Can't bend it.
completely.
I think it's likely to be more
decentralized than that. There'll
definitely be 10 million GPUs working
together on an AI system that is
learning and doing things, but it might
not all the parts of the brain won't
necessarily all be talking to each
other. That makes sense. Um, can you say
anything that we've learned or observed
about how uh smarter and bigger

[00:32]
pre-trained models correlate with how
good a model is at learning
reasoning? Um, yeah. So, I think what
we've kind of observed is uh it is
better pre-training and unsupervised
learning. just tends to lift kind of
broad-based intelligence of the model
and aid a lot in generalization
uh which we found to be like really
complimentary I think with reasoning
which can tend to be a little bit
spikier lumpier in terms of like where
it's increasing intelligence um so yeah
I think they're they found them to be
good compliments to go off on a little
bit of a tangent do any of you guys have
like a intuition of is it weird or is
there anything to take away from the
fact that pre-training seems to be so
general across everything and when we
teach a model reasoning, we can get it
so good only at one category of things.
Yeah, I don't I don't know if it's the
most Yeah, I think I think it's
interesting. I think it's kind of not
surprising to see this out of
pre-training when you're just look at
what you're what you're training with.
Um, you're when you construct like a
training data set for pre-training, it's

[00:33]
inherently very broad. We're we're
targeting breadth and diversity. Um, and
I think it's it's kind of difficult to
always get the same breadth when you
talk about doing RL and having like
environments that you can kind of
cleanly get uh good reward signal out of
and good good environments out of. I I I
agree. But I think there's another
factor that pre-training is
essentially it's compressing the data
and compressing the data is about seeing
connections between different things.
It's about analogies. It's about
uh abstractions.
And reasoning is on a particular
problem. It there's like there is a
skill and a craft to thinking
carefully. And thinking carefully can
unlock many different kinds of problem
solving in different domains. But
there's something uh more learning at a
more abstract level when you're
compressing across domains in the way
pre-training does.

[00:34]
That that makes Oh, that I'm going to
change my question for you in a second.
I just thought of something else. Um
what's going to limit us in terms of
systems progress chips, processors,
memory, network or power? Like what what
will be the bottleneck of continuing to
scale this up?
Um it is this is the beauty of systems
uh in that if you do code design the
workload is
adaptable to the infrastructure that you
built.
Um there is I think let's say there is
no statement that broadly network is a
bottleneck or memory bandwidth is a
bottleneck or computer is a bottleneck.
We have the option to basically shift
and even for the same specification of
the model we have the option of shifting
resource demands to basically create a
more balanced system. However, having
said that, I think let's say the
pre-training answer is different than
the inference answer and so on. But it
it never hurts to have more memory
bandwidth. Uh I would uh yes, I think

[00:35]
this is a hard question to answer and
without qualification. Speaking of that
earlier point, how much do your teams
work together on like the spec of the
model as we get ready for the four five
run? Like how much how much is it you're
just like this? Yeah, very closely. I
mean down to like the shapes of the the
map moles that we want to be doing. Um
making sure those are optimized well. Um
but for this project it was a much
deeper collaboration going back um to
like I guess six or nine months before
the launch of the run. Um trying to do
for some of the the functionality we
wanted to put into the run and like
aspects of what we needed to do to make
4.5 happen. we took on like a a specific
like very large d-risking run uh that
was specifically focused on co-design
with systems uh to make kind of the the
ML and the systems work together well at
scale. Um so there we I think it's the
first time we put like such a large
emphasis just on the codeesign aspect
was really key. Yeah, I think that was
the first big um scale effort that I I

[00:36]
remember that it is not just about
fine-tuning one aspect of it is that
fundamentally you want a property whole
to hold system side and that property
doesn't emerge out of nowhere. You
really need to steer the system to give
you that property. Uh so that code
design effort is something uh that uh
formed the architecture and
architectural elements that goes into
the model and somehow ties the system
and ML side together. It's probably a
property we would not prefer to have.
Yeah, I would ideally want everything to
be decoupled to basically give maximal
room to each other. But at times things
get tied together where you are really
catering to the requirements of your
infrastructure or how things should be.
I mean oftentimes it is you really want
to have a balanced system uh and
balanced communication and a very
symmetrical type of system and you have
the best knob we have at our disposal is

[00:37]
all code design. How close are we to the
idealized mean
system? Do you mean being like fully
happy we have all the hardware we want?
It works for what we know about ML. We
are nowhere near that. You think it is
we are nowhere near but it is fun. It is
the the practice of building systems is
always about that that you have an
idealized view of how things should work
and it's just about reconciling the
differences of that with what you have.
I think we are not doing theory for the
sake of let's say just talking about
what we want it to be. We just want to
make it happen and approximate that
ideal to the degree that we can. So to
be honest I think this
u is probably as exciting as it gets for
systems. you be get to really come up
with hypothesis of what is a good system
design uh and take it from there and
basically see the results in action very
quickly. Things that previously one

[00:38]
would say this is an elegant system
design and uh we have to just history
will tell us if this is the right thing
to do or the wrong thing to do. We have
a lot of compute, we have a problem, we
we we know the target and just we go and
see if our choices were correct or not.
How much is your team thinking about the
sort of constraints of system design
when they're trying to decide what
what's going to go into the run? Yeah, I
think it's it's a huge consideration for
just doing pre-training runs at large.
Um I think like since 4.5 a lot of the
work on the architecture side there
there's also kind of ongoing threads
around further code design further
places that we can design for future
hardware uh build together. I think
there's been a lot of promising uh work
already since then.
Okay. My changed question for you. Why
does unsupervised learning work
compression? So So the ideal
intelligence is called Solomon
induction.

[00:39]
Basically, it's it's uncertain about
what universe it's in. And it imagines
all possible un it considers all
possible universes with simple ones more
likely than less simple ones. And it's
it's fully
basil in head and up updates its views
as it progresses. And you can
approximate this by uh finding the the
shortest program that computes
everything you've seen so far. And what
we're doing with pre-training or one way
to think about what pre-training is
doing is it is compressing it is trying
to find the shortest program that
explains all of the data that humans
have produced so far as a way of
approximating
and why does looking at next token
prediction do that? It's actually a
subtle question there. There was a
paradox or somewhat of a paradox in
statistics for a long time. Why do deep
networks generalize when they don't seem

[00:40]
to compress? Normally in statistics, you
have lots of data and you got small
models. The models predict the data.
Therefore, you can the models must have
compressed and must have learned
something. In pre-training generally,
the models are pretty gigantic and they
scale roughly with the with the data. Uh
so it was always a question are they
actually compressing? Are they
generalizing? And of course there are
critics who have said well it's just
memorizing and interpolating and
superficial. Um but there's a way of
viewing
pre-training such that you do see that
it is a compressor in a in a different
unintuitive way. And basically the idea
is called prequential compression. And
the idea is that the fact that it learns
quickly during
training means you can turn it into a
great compressor. So even though the
weights are big, the binary doesn't need
to store the weights. The binary can
pre-train from scratch to decompress.

[00:41]
And so the fact that it's learning
really really quickly means that most of
that data you can encode with very very
few bits. So basically for a subtle
reason, it really is quite a good
compressor. And I think that
is a a pretty satisfying explanation for
why it really does lead to intelligence.
You guys have anything to add? No, it's
great. Thank you.
Uh, one one thing somewhat relatedly
that hasn't come up yet is the
discipline of
metrics. It's like the the
thing the thing you get when you do
these scaling laws and you you do all
the ML science is very dependent on the
metric that you choose. What do you
mean? What do you want to say? Oh, yeah.
just talking about the the what test
side you're you're evaluating your
perplexity on. So what you're referring
to even even looking primarily at
perplexity. Oh yes, there's

[00:42]
already some viewers might think we're
looking at college tests or something.
Oh
yeah. Um so yeah I mean do you want to
explain perplexity then? I think it's
worth it. Yeah. So it's very it's very
tempting to try to evaluate your model
for intelligence on things that are
legible to humans as tests. Uh but if if
you if you do this probably you're going
to be favoring changes that make
memorization easier at the cost of
making systems actually smarter because
almost every test that we have out
there's something similar online like if
you can actually train on the entire
internet tests become somewhat uh
degenerate compared to tests for humans
where they can't do that. And so the the
main approach in the field is to look at
how much it compresses some held out
data that's thought to be good data. And

[00:43]
e even then if you're not careful about
that held out data, it's too similar to
your training data. Training changes to
your training algorithm that make it
memorize better will seem to make it
smarter because it'll have already it'll
already know your test set. And we don't
want to just be measuring memorization.
after memorization, we're after
generalization and so out of
distribution generalization. So yeah,
this is why I guess yeah, maybe you're
alluding to so like the the key test
sets that we're looking at, we we care a
lot about them not being present in any
degree to the slightest degree uh in our
training set because that kind of throws
off all all the way that we do our
scaling laws. Um so yeah, this is a very
key point with what's our best thing for
that? Uh so our our internal codebase uh
which we know is not out there.
Um, yeah, it's a very good held out. Has
that held as our best thing across like
many. It's still the best thing. Yeah,
it's remarkable. I mean, we joke that a
model is its monor repo loss like
everything else there's some incredibly

[00:44]
meta recursive thing there.
Oh yeah,
somehow you you you pre-train the model.
It has a monor repo loss and somehow
this tells you so much about how it's
going to be behaved down. It's it tells
you a lot about how a philosophy grad
student is going to find the nuances of
its responses. But it's incredible. It
is incredible. related to that and sort
of last question in some sense this
whole effort which was hugely expensive
in terms of people and time and dollars
and everything else was an experiment to
further validate that the scaling laws
keep going. Yeah.
And why and turns out they do and they
probably keep going for a long time. Um,
I accept scaling laws like I accept
quantum mechanics or something, but they
still don't like I still don't know why.
Like why should that be a property of
the universe? So why are scaling laws a

[00:45]
property of the universe? You want I can
I can take a stab. Well, the the fact
that more compression will lead to more
intelligence that has this very strong
philosophical grounding. So the question
is why does training bigger models for
longer give you more compression?
And there are a lot of theories here.
There's the one I like is that the the
relevant concepts are sort of uh sparse
in the in the the data of the world. And
in particularly it's is a power law so
that the like the hundth uh most
important concept appears in one out of
a hundred of the documents or or
whatever. So there's long tales. Does
that mean that if we make a perfect data
set and figure out very data efficient
algorithms? I mean can go home. It it
means that there's potentially
exponential compute wins on the table to
be very s sophisticated about your
choice of data. But but basically when
you just scoop up data

[00:46]
passively, you're going to
require 10xing your compute and your
data to to get the next constant number
of things in that
tail. And there's just that tail keeps
going. It's long. you keep you can keep
uh mining it. Although, as you alluded
to, you can probably do a lot better.
I think that's a good place to leave it.
Thank you guys very much. That was fun.
Yeah. Thank you.

</details>
