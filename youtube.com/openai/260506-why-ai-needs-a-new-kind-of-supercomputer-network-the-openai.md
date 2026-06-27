---
title: "Why AI needs a new kind of supercomputer network — the OpenAI Podcast Ep. 18"
channel: openai
url: https://www.youtube.com/watch?v=TiW96H5HmAw
youtube_id: TiW96H5HmAw
published: 2026-05-06
duration: "37:38"
captions: en
---

# Why AI needs a new kind of supercomputer network — the OpenAI Podcast Ep. 18

[![Why AI needs a new kind of supercomputer network — the OpenAI Podcast Ep. 18](https://img.youtube.com/vi/TiW96H5HmAw/hqdefault.jpg)](https://www.youtube.com/watch?v=TiW96H5HmAw)

<details>
<summary>자막: Why AI needs a new kind of supercomputer network — the OpenAI Podcast Ep. 18 (37:38)</summary>

[00:00]
Hello, I'm Andrew Mayne, and this is the
OpenAI Podcast. On today's episode, we're
discussing how
to make supercomputers better at training
models. Joining me are Mark Handley from
the core networking
team and Greg Steinbrecher from workload
systems. They'll discuss how a
breakthrough has made
training more efficient so everyone gets
smarter models faster.
This has really allowed us to remove one
of the key barriers to continuing to
scale.
We're talking about a lot of the world's
fastest GPUs and making them all work
together on a single task.
We know we've won when researchers stop
needing to know what network protocol this
particular cluster is using.
So tell me a bit about your background.
I started out doing physics and math in
undergrad, wanting to basically understand
how complex systems work. I always liked
the part of physics
that's about how do you take this thing
that is unknowably complicated and build a
simple model
that is a complete and utter lie but tells
you something about that system. And then
build your

[00:01]
intuition on that and kind of build more
complex models. I ended up doing a PhD
trying to build quantum computers.
Ambitious PhD.
You know, little things, little things.
Unfortunately, what I liked is big
complicated systems. And you'll note that
quantum computers
don't work and therefore they don't scale
yet. They will someday, but they don't yet
work. And so
I kind of took a look at the chips we were
designing to control light for quantum
computers.
And I went, huh, that kind of looks like a
network switch.
What if we use this as a network switch?
And what I found out pretty quickly was
that academia does not know a whole lot
about what
real data center workloads look like.
You get a whole bunch of kind of very toy
models, but they're not very informative.
And so I ended up kind of pitching an
industry company to get a fellowship.
They paid for the last two years of my
PhD.
I ended up working there for a while,
building out, kind of doing initial
network hardware
just to try to understand what is it that
we actually need from data center
networks.
What I found out was that there's a huge

[00:02]
amount of headroom on just conventional
data center
networking hardware and lots of room for
optimization. We did not need my little
optical
chip. We did not need to do anything fancy
like that. But there's all sorts of really
fun problems.
And then around that time, the whole AI
boom started to kick off. We decided we
needed to
build big GPU clusters. And in particular,
we needed to build networks for those GPU
clusters.
And so I got roped in on trying to build
kind of simulations of those so that we
can figure out what to build.
And then in the process of trying to build
a simulation of these systems, you learn a
lot about how they have to work.
And at some point I said, well, why don't
I just go build the actual thing?
And so I transitioned from writing
software to build simulations to just
writing the software that allows GPUs to
communicate with each other.
And then a little over a year ago, ended
up coming here to OpenAI to do some of the
same stuff, but to get even closer to the
actual model training.
So the team I'm on is responsible for more

[00:03]
or less making sure that we'd use the GPUs
efficiently.
So are the models training as quickly as
they can be?
Are we not bottlenecked on the network?
What do we do when something fails?
Are we restarting efficiently?
How do we kind of work around quirks in
the hardware?
and yeah now I get to play with some of
the most fun hardware in the world and
like try to make it —
try to kind of squeeze every last ounce of
performance out of it.
Mark you've had a considerable amount of
experience trying to get computers to talk
to each other and do meaningful
work tell me more
about your background.
So when I'm not at OpenAI I'm a professor
at the University College London and I've
been doing networking research for more
decades than I care
to think about. Originally, I started
working out on trying to make the internet
do video conferencing.
And back then, that was a really difficult
thing because the computers were so slow.
And then we came up with a way for doing
that that suddenly the rest of the world
got interested in.
And so the standards we wrote for doing

[00:04]
that are now the things that your phone
uses to communicate
with 4G and 5G networks. And so that was
the first part of my life, was trying to
standardize all of
that sort of stuff, that everybody could
actually take advantage of that.
And the problem with standardizing is
everybody needs to agree.
So it just, it takes a long time to
actually get everybody to agree on
anything.
A while back, I got interested in what was
happening in the data center world.
And it had the big advantage that you
could actually do something different
because you
only needed to agree with it while
building, not the whole world.
And so that was how I got into thinking,
well, this data center networking stuff is
a really interesting place to be.
Well, it's an interesting problem because
I think that just the idea that we'd be
scaling as many GPUs as we are now, it's
happened so fast, happened so quickly.
And often, we're still using GPUs, which
are graphical processing units.
We're just now starting to use next
generation chips to do this.
So how much has been the work regarding
just to update the way we think about it
and update the sort of the tools we're

[00:05]
using for this, which is what we're here
to talk about with.
Multipath Reliable Connection.
So from a network point of view,
the data centers that we traditionally
used to build,
they kind of got derived from what we used
to do in the internet.
And when you do communication in the
internet,
you have lots and lots of people
communicate.
It's like there's a lot of data moving
around,
but they're all doing their own separate
conversations.
And so generally speaking,
if the more communications you add onto
the same shared network,
the more things smooth out and become
even.
And so that's great. You can take
advantage of the statistics of large
numbers.
Unfortunately, when you look at what we're
doing when we're training things, it's
exactly the opposite from that.
We're talking about a lot of the world's
fastest GPUs and making them all work
together on a single task, which is why
this stuff gets hard.
That process of basically ingesting all of
this data and allowing the AI model to
learn from that data in parallel is what
allows us to build smarter, better models.

[00:06]
But let's say one GPU goes a little slow.
Well, now all the other GPUs have to wait
for it. That's all wasted time.
Or one of the GPUs, you know, a cosmic ray
hits it and some bits flip and it stops.
Well, OK, now that whole step is maybe not
useful and we have to maybe roll back or
kind
of stop and take stock of what has
happened.
And while we stop and take stock, all the
GPUs are not doing useful work.
Yeah, a key thing here is that the
communication between the GPUs is actually
part of the computation.
It's like they're doing one big
computation across all of them.
It's not they're doing different things.
We have to actually have them communicate
with each other in order to agree on what
the result of that step of computation is.
And that's just about the worst possible
workload you could think to put onto a
network.
And so the way the industry has evolved
over the last couple of decades has been
slowly coming up with improvements on how
we actually do that.
But until recently, the scale wasn't
enough that it really mattered.
You could get away with doing the same

[00:07]
sort of things we did on the internet,
just bigger.
But you can't get away with that anymore.
And that's why we tried to think of
different ways to actually solve these
problems,
to cope with these very synchronized
workloads as we scale things up.
AI has upended a lot of things in the
world.
It has definitely upended the way that
technology companies have to think about
the data centers that they're building.
conventional hyperscalers for kind of the
web era, the teams that built this were
very kind of
disconnected from the individual
workloads. The goal was to basically just
provide an ocean of
compute. AI has forced us to think very
differently. And OpenAI in particular has
been kind of at the
forefront of realizing that the systems
and the design of the systems is integral
to the training
of the models and that you can't just have
your infrastructure team sit over here in
one building
and kind of just deliver an ocean of
compute and your model team sit over here
and like try to make
the best you know model that they can on
that compute you really have to do kind of
a co-design

[00:08]
across these whole things um and so you
know we on my team sit literally next to
the researchers
and talk with them every day about you
know how they can best you know how their
workloads fit
best onto the existing servers. And in
doing that, we learn a lot about where the
pain points are.
And we are on call for the big training
runs. We get woken up in the middle of the
night if
something is broken and can't be fixed.
And so through that process, and you start
to go,
oh, well, what if in the next generation
we fix these problems? What if we didn't
build data
centers with the same properties as we did
for web scale workloads? What if we
instead fix this
piece or this piece or this piece. And I
think the network has been a real source
of pain for us.
Yeah. So when you're building a data
center network, all of these GPUs, because
they do
this computation and they all need to talk
at the same time, you need a lot of
bandwidth.
And the problem with that is you can't

[00:09]
build that with a single switch or even a
hierarchy of
switches. You have to build hierarchies of
hierarchies of switches. And so that means
that
when you communicate from one GPU to a
different GPU,
there are many different paths your
traffic could take through that network.
Thousands of different paths your traffic
could take
through the network because we build
so many different switches in there.
There's several thousand switches in one
of these buildings.
Now that gives us an interesting problem,
which is which path do you take from one
place to the other?
And if you basically have the requirement
that I want to be able to send from one
GPU
to another GPU as fast as possible,
and I choose, say, a random path through
the network,
if I get lucky and nobody else chooses the
same path, then great.
But if I get unlucky and two people choose
the same path, we go slow.
And if 10 people choose the same path, we
go really slow.
And so this statistical multiplexing that
we used to have when we designed the
internet
just doesn't work out very well when we're
trying to build these networks for our
data centers.
And so that's where we came in to try and
design things somewhat differently.
Maybe to put a fine point on that,

[00:10]
the synchronous nature of the workload
that we talked about earlier
is why this becomes such a problem.
It is not about how fast can the average
pair of GPUs talk to each other.
It's always what is the absolute worst
case that occurs.
So if you think about you've got thousands
of GPUs that are trying to talk to each
other.
So there's tens of thousands or hundreds
of thousands of network flows on tens of
thousands of links.
What you have to do is you have to look at
that entire network and go, what is the
link that got most bottlenecked here?
That one link is going to set how fast all
of your GPUs are able to work and how much
time it takes for you to move data through
this.
because everything is proceeding in
lockstep. And so whereas previously we
might have been
subject to or kind of taken advantage of
average statistics, we don't have that
luxury anymore.
We instead are subject to like the tail of
the tail, we call P100, the 100th
percentile statistics.
And that leads to very different systems
requirements than when you can kind of
rely
on the law of large numbers to take care
of you.
And so the other problem with this is that
when you build your networks, we build the

[00:11]
best possible networks we can. We go to
the best
equipment vendors, we use the best optics
and so forth. When you really scale things
really big,
things are always going to be failing.
Links will fail, switches will get
confused and will have to
be rebooted and so forth. Any one of these
failures is going to affect the traffic
running
over the network. And so if you've got
this problem where we only care about the
100th
percentile and then a link fails in the
network, what happens? Well, stuff will
fail. We may have
time before the routing reconverges and
then we move the traffic onto a different
path. We take a
glitch there. That can be quite a long
glitch that can cost us. Or worse, we can
actually cause one
of these communication transfers to fail.
A single transfer fails and you could end
up with the whole
job crashing. And so we really want to
avoid that kind of problem. We want to
build a way of using
these networks that is resilient to not
only the potential transient congestion we
might build in
the network, but also when things fail, we
just want to be able to carry on and
basically not notice.
But that requires that we actually design
the network protocols differently from the
start.

[00:12]
You can't retrofit this onto existing
network protocols.
Yeah, it's a very interesting problem as
you describe it,
because I can see that where you could say
like,
oh, well, if we have a thousand GPUs,
there's only one chance out of 10 that
they're going to fail or whatever.
And now I have a hundred thousand GPUs.
Well, guess what? I'm going to have a
failure all the time.
And that's what you have to sort of solve
for each time you scale it.
So where does this break? Everywhere.
There we go.
If you think about the meantime between
failure of the equipment,
for any particular range of equipment,
You've got some time between which
something will fail somewhere in your
building.
And of course, the bigger we get, with the
same cost of equipment, that time comes
down further and further.
And eventually you get to a point where
actually something is failing sufficiently
often that you don't get any work done on
a large synchronous workload.
And we can't have that happen.
So we have to do things differently to
make that work. Yeah.
So the very simple math here is you can
basically assume that if failures are
independent and you double the size of
your system,
you're going to have half the time between
failures, right?

[00:13]
Your mean time to failure goes down by
half.
The important thing to think about here
for the network is for every GPU,
we have tens if not hundreds of network
components.
So even just like, say you've got one GPU
connected to one network adapter.
In that network adapter, if it has an
optical transceiver in it,
maybe you'll have four lasers.
On the other end of that transceiver,
you'll have another four lasers.
And so already just connecting that one
GPU just to its first hop switch, you've
got an order of magnitude more lasers than
you have GPUs.
Now add in multiple layers of switching
and you start to get into several orders
of magnitude more components in the
network than you have kind of at the edge
of your network.
Because we need to have so much bandwidth
here.
So we have to build these networks.
We can't kind of taper them down and only
have a couple of components in the network
because then we'd be starving the GPUs.
They wouldn't be able to actually kind of
use their full capability to do math as
quickly as possible.
Instead, we would just be letting them sit
idle and wasting time, money, energy.

[00:14]
We would get trained models more slowly.
It would be bad.
And so we built a very big network.
But now you have many, many, many more
components in that network than you have
maybe at the edge of your network.
You have literally millions of optical
links within the same building.
So it's a huge scale. You mentioned the
data centers originally were.
I go do something to search the cloud, to
get my email, whatever.
I may be talking to one server, there
might be a backup there.
The idea that we would be having more
computers inside a data center talking to
each other than we did just a few years
ago, people trying to connect to it.
And so how have these protocols evolved?
One of the things that got me into
networking in the first place, I have a
very distinct memory of, I was at a
conference, OFC, it's an optical
communications conference back in 2017.
And they had a presenter from Facebook.
and he put a chart up that had a stacked
line chart of the traffic that they serve
to their
end users and the traffic that goes inside

[00:15]
of their data centers. And the traffic
inside of
their data centers was just exploding,
even while the kind of amount of traffic
that they were
sending to end users was staying constant.
And this is way before GPU clusters and
AI. So this is,
what AI does is it takes all of the
systems challenges that people were having
previously
and it cranks them up to 11.
So to address this,
you've been working on a method,
Multipath Reliable Connection.
The insight was basically that you have,
we try to manage congestion in networks.
And so there are several pieces
that you can pull together and do this.
And the first part of the insight was
if you spray the packets across many
paths,
you can low balance those paths
through the network really equally. And if
you do that
and you build a network topology that has
enough capacity,
then you don't cause hotspots in the
network.
It leaves you with just one place where
you have congestion,
which is if multiple people try to send to
the same destination at the same time.
But it also leaves you some problems
because the packets can get jumbled up in
transit

[00:16]
because they're taking different paths.
And so if you do manage to cause
congestion and cause loss,
it's a little bit difficult to figure out
whether you got lost
or whether you should still be waiting for
packets
because they got jumbled up in transit.
And so the second piece of this is a
technique we call packet trimming,
which is if you're causing congestion in
the network
and you would overflow a queue,
normally we'd just drop the packet.
And then we've got ambiguity. Did it get
lost? Did it get lost?
How long do I need to wait for it?
But what we do instead is we will trim off
the payload of the packet
and just forward the little tiny packet
header to the destination,
which can immediately request a
retransmission
and we can retransmit that packet.
And that totally removes the sense of
ambiguity
as to whether we lost packets due to
congestion
or whether we should still be waiting for
them because they got reordered.
Interesting. So just making sure that the
part saying, are you there, goes through,
and then you can figure that out and then
send the rest.
Yes, you really need to know
that you should still be waiting for it
or you should not still be waiting for it.
What does this mean for the end user?

[00:17]
The biggest thing that this means
is that you're going to get better models,
more intelligent models, faster from
OpenAI.
So MRC allows us to accelerate
every part of our research and deployment
pipeline.
It allows individual users to not worry
about their jobs failing, not worry about
how their job has gotten scheduled and
whether the performance of it is going to
be different because they're placed on the
same rack as someone else's job.
It allows us to train frontier models much
faster, more reliably, and really just to
turn the entire crank of that pipeline
much faster and much more reliably.
So you should expect to see an ever
increasingly exciting pipeline of releases
from us. The vibes are good?
The vibes are good. The vibes are very
good.
The idea came out of a lot of research
work that we've had over the last few
decades.
We're not fundamentally inventing anything
new.

[00:18]
We're just doing things that other people
have invented, but pulling the combination
together into a set of features.
So we formed this group of people who are
all interested in doing this.
And last year, we finally got to the point
where we were able to deploy this.
And we went from, in a few months, from
the first hardware available to actually
running
and training models and it actually all
operating.
So this has the result that we don't cause
that congestion that we talked about
before.
The second really nice property is that if
something fails in the network, every
single
one of these flows that go through there
will probably be affected by the failure.
But it'll only be affected a little bit.
And within a few round trip times across
the network, we stopped using a failed
link.
And so this problem of links failing,
bringing down the network just goes away.
All of the flows themselves from the
network interface at one side network
interface are
just avoiding those failures as we go
through the network.
It's like self-annealing. Exactly. Yes.

[00:19]
So I think Mark has mildly undersold this,
but maybe we should- Mark, come on, man.
So conventionally, when a link goes down
on a network, what happens is one side of
that link,
the switch at one side of that link, or
maybe both sides of that link notices.
But then it has to tell all of its
neighbors that that link went down.
And then they have to tell all of their
neighbors that that link went down.
And so you have a distributed systems
problem.
It's conventionally solved with a
technology called BGP, Border Gateway
Protocol,
which is basically just like a gossip
protocol that allows one link over here to
eventually tell
this switch all the way over here, maybe
through five or seven hops through the
network, then,
hey, you can't get to this destination if
you take this link. You have to use these
other links.
That's a distributed systems problem that
has a convergence time.
What MRC has done is it has taken that and
it has broken the need to coordinate.
Every endpoint
independently very quickly detects, hey, I

[00:20]
shouldn't use that path and just stops
using it.
And this is maybe counterintuitive because
you would think, oh, it's easier if I just
have some central authority that tells me
that this link is down and that central
authority can distribute that information.
Anybody who's waiting for a website to
update knows that. It's not going to work.
Right. Central authorities are, generally
speaking, also known as single points of
failure.
And so instead, what we've done here is we
no longer have to wait for this whole
convergence process to occur, which can
take seconds or in the tail, tens of
seconds.
Instead, everyone within, generally
speaking, milliseconds notices and just
stops using that link.
So this is a very big deal because
previously, you know, the link goes down
and the whole job stops for a few seconds
as we wait for kind of the network to
stabilize.
That's time, again, that the GPUs aren't
doing useful work.
And as you, again, scale up, you're going
to have more and more and more of those
individual little seconds.
And here now, what we've observed is that
we turned this on as the data center was
being built.

[00:21]
As Mark said, we were able to get jobs up
in training within months of hardware
arriving.
There's a lot of manual labor that goes
into building one of these buildings.
There's a lot of shared points where
fibers from one data hall are coming in
and technicians are trying to assemble
another data hall or things like that.
And so what we saw was that because of all
of this kind of manual effort that was
going on, links were going up and down all
the time, like even way more often than
you would kind of hope just due to natural
failures. We did not care.
We didn't even notice. MRC just took care
of it.
It just kind of would detect, hey, can't
use that path, move on to the next one.
Didn't care. It was incredible.
So the other thing this gives you beyond
just that is because once it's handling
that by itself, once MRC is already
working around the failures, traditionally
we would probably still have been running
a routing protocol in the network to find
the paths that actually work.
But routing protocols themselves are
complicated and switches are complicated
and switch software is complicated.

[00:22]
And these are all things that can fail.
And we realized that actually MRC itself
was able to figure out which paths were
still working.
And so actually, we just decided that we
would turn off the routing protocols.
We use completely static routing in the
switches at the largest possible scale.
And so some paths are broken. Who cares?
MRC will find the broken ones that still
work and keep going.
And that just removes a whole set of
complexity out of our network management
that we just don't need anymore.
We don't care about whether the switch
control plane has converged because it
doesn't need to. It's entirely static.
They have a configuration that they have
at boot time.
They boot up and they never change their
routing tables from then onwards.
So this is a very big effort working with
a bunch of people.
Care to talk about some of the partners?
Yeah, we've been working with Microsoft,
who build our Fairwater data centers for
us.
And then we've been working with NVIDIA,
Broadcom, AMD, and Intel to standardize
this specification.

[00:23]
And with all of these guys to actually
build our hardware for our new
supercomputers.
It's interesting because as a user of this
technology, and you listen to sort of the
way we sort of think about things where
people talk about like, well, when's the
next model coming out?
Like it's a software update that comes up
every year. But it's not.
Every model is essentially a research
project, and it's dependent upon what goes
on in the training.
And you try to have an estimate of how
long it's going to take, and we try to
predict where that's going to be.
But this kind of reliability sounds like
it's going to be an incredible advantage.
God, yeah. I would say from talking to the
people who
were here even earlier, I mean, you hear
just horror stories about what it was
like, how often they were getting woken
up.
I remember walking in the cafeteria and
seeing some of the people working on
networking and sort of sad faces because
they didn't know why something had stopped
in a run. And it was just. Yeah.
We have heard nothing but universally
positive feedback about how stable the
clusters with MRC are, how well they're

[00:24]
working, how basically the researchers
don't have to think about this anymore.
And then you look at the statistics and
you realize just how much stuff is
breaking all the time and they're not
noticing. Yeah.
To some degree, this is the ideal, right?
I know I said earlier, we are pushing the
limits of infrastructure.
And so there's never going to be a time
that you can just completely ignore infra.
you know the ideal world right is
researchers don't have to think about this
but that's never
going to be the case but every time we we
know we've won when researchers stop
saying you know
network or stops you know stop needing to
know what network protocol this particular
cluster is using
and yeah it's been it's been really nice
to basically be able to focus all of
because there's
don't get me wrong there's plenty of other
things that break there's plenty of other
work to do
but this has really allowed us to remove
one of the key barriers to continuing to
scale
and to being able to deliver newer and
better models on a much, you know,

[00:25]
we are trying to scale everywhere,
including our velocity.
And you have all decided to make this open
to everybody to use.
Yeah, so the specification is due out
through OCP as an open standard.
And we've, as you say, decided to open
this up for everybody to use.
We're big believers in open standards and
open source.
We're building all of our networks on top
of Ethernet, which is selfless and open
standard.
And we benefit when the industry has
velocity, when the industry can keep up
with the things that we're trying to do on
the challenging side of things.
And so it's in everybody's interest if
we're all trying to actually deploy what
we think are the best solutions in this
space.
There's no shortage of coverage of the
scale of the AI build out.
I think on a personal level, I think it
would be a real shame if that supply chain
was fractured.
You have people investing in totally
different technologies and underlying

[00:26]
hardware just because they're trying to
get some small advantage.
I'm really excited that this is going to
be an open standard.
I think it will really benefit other
people outside of OpenAI.
It also benefits all of us if we are kind
of all pushing in the same direction.
Infrastructure is kind of this shared fate
of the whole industry.
And I think it is a very good thing that
we are open sourcing this and kind of
bringing everyone along.
It seems like it's beneficial, too,
because everything is becoming very
collaborative.
And even, you know, you take a project
like Stargate, which is multiple
locations, many partners across the world,
and Microsoft, Fairwater, and sort of this
idea that compute is a thing that there's
never going to be enough of it.
and the more we kind of work with each
other
to figure out how to maximize it and
continue doing it,
probably the better it's going to be
for everybody involved than treating it
like,
I mean, it is a very limited resource, but
these protocols, like you said before,

[00:27]
you know, with Ethernet, whatnot,
that's really what gave us, you know, what
we have and things like the World Wide Web
and a lot of the cool things
we realize, oh, share this because what
we're going to benefit
is going to be so much better. Yeah, what
we're trying to do is hard enough
without everybody having to reinvent the
wheel all the time. We think this is,
the right way to go and we'd like
everybody else to go in the same direction
as us.
Where are the limits of this?
MRC is a flexible standard.
It builds on top of Ethernet.
So as Ethernet scales, so will MRC.
You can think of Ethernet as kind of the
protocol that individual devices use to
talk to each other.
MRC sits on top of that.
It incorporates kind of this static
routing that Mark is talking about.
It incorporates what we call congestion
control, which is basically if we do end
up in situations because of failed links
or choices that we make about how we send
traffic, how the endpoints should react to
that to make sure that we kind of use the
network fairly and efficiently.

[00:28]
My experience with networking is that
there will always be more work to do.
There's always going to be ways we can
improve that, make the network more fair.
There's fundamental limits on networks.
Specifically, the speed of light is a
known speed limit.
And so the amount of time that it takes
for light to get from one point to another
in a network has some lower limits on it.
But we're going to keep making each of
those links faster and faster.
And so that will always kind of change the
operating point of basically how much data
you have outstanding per connection at a
given time.
And that will always require kind of
ongoing engineering effort to make sure
that we're making the best use of the
hardware that we have in a given
generation.
But I think MRC gives us a very flexible
and strong base to build on as we continue
to push through the next few generations.
And the key thing is because, as you say,
it's Ethernet-based.
I mean, Ethernet now is not what Ethernet
was 10 years ago or 20 years ago or 30
years ago or even 40 years ago.
Ethernet itself has evolved so much over
the years.
And what we're doing is we're taking
advantage of all that development by the
whole world's networking industries.

[00:29]
And so we want to make sure we carry on
riding that wave of innovation that has
taken Ethernet
forward. So given that all of that's
happening anyway, MLC, because it takes
the intelligence
pushed at the edge of the network, we can
scale the cores of our networks as long as
Ethernet
keeps scaling. And there's no particularly
obvious reason why that's not going to
keep scaling for
at least the near future. And who knows,
maybe smarter people than me will figure
out how to
make it work for another 40 years. One of
the key things we're doing, though, is
trying to actually
move the complexity out of the network. So
as I mentioned, we turn off the routing
and each
packet is actually source-routed through
the network. We're using a technique
called IPv6
segment routing, which allows each
individual packet's address to list the
precise set of
switches the packet goes through as it
goes through the network. And that means
that the
switches themselves can be really dumb.
It's really nice to be able to sort of
simplify a

[00:30]
of the network. And as you're trying to
scale and make things scale reliably,
making the middle of the network as simple
as possible has huge benefits to us.
the network as simple as possible has huge
benefits to us. The other piece here is,
you mentioned
Ethernet has this rich, wonderful history.
We're still building on Ethernet. That's
because it's
an open standard. That's because the
entire industry has bought it and is
pushing in the
same direction. And that's exactly what we
want to see from MRC also, is we want to
see basically
the next layer get ready for the systems
challenges of AI and get widely adopted.
We don't think that this would do as well
if it was an OpenAI exclusive.
With OpenAI investing the time and energy
and the people into solving these
problems,
it does seem like even though you're
making MRC available to everybody by
having teams now working on this,
it's got to be providing a lot of benefits
and advantage.
I try to get a lot of benefits. So again,
my role is from the perspective
of like, how do we make the most use of
what we have?

[00:31]
Not literally in a conservationist sense,
but in some sense it is, right?
Like if we're going to be burning the
power on these things, we want it to be
used productively
and we want it to be used efficiently.
Another one of the advantages of MRC is
because it has this property of allowing
us to spray
over multiple paths, we can build much
simpler, much smaller networks that have
many fewer devices in it.
So this is not an obvious property, but
basically we're able to build networks
that are much
flatter and basically have many fewer
layers of switches and use much less
power. They also cost
a lot less. And the amount of useful work
you can do per watt goes up when you do
that because you're
not spending extra power on these extra
layers of switches. The power is more
generally going
directly to the GPUs and allowing them to
actually do work.
When you train models and start off with
text models and with certain context
windows, so there's a certain amount of
data that needed to go
about. And then as you go into multimodal
models, is there a difference between
training, let's say,

[00:32]
an image model or a video model
or just a multimodal model?
I probably can't get into the details of
model architecture, but I will say that as
our models get more advanced,
the demands that they place on the systems
get substantially harder. The amount of
data that
you have to move and the latency bound on
doing that.
So basically, the regret that you have if
your network goes a little bit too slowly
just
gets worse and worse and worse as the
training cluster size gets bigger and as
you continue
to optimize the rest of the stack.
Because obviously we have many, many very
smart people who are trying to push in the
same direction and make these models very,
very efficient.
We all want the next version of ChatGPT
faster. We want it to be smarter.
One of the big strengths of OpenAI is that
we have all of these incredibly smart
people pushing in one direction.

[00:33]
And you have the researchers and you have
the infrastructure people and everyone
kind of knows what our goal is.
And so we have very smart people who are
trying to make the work that happens on
the GPU go faster.
And all that means is that now we have a
tighter bound on how long the network has
to transfer things.
Because if we are the ones who are lagging
behind, their work doesn't matter.
And so our work never stops.
As these things get bigger, the variance
in whatever the slowest computation is
goes up.
We have to work on controlling that tail.
Similarly, on the network side of things,
you need to pull things in.
One piece that when Mark was talking about
this splitting over many network links,
one thing that's mildly not obvious about
this is that if you did this without MRC,
the tail statistics actually get much
worse.
So if you take the same amount of
bandwidth
and have more paths,

[00:34]
you end up basically having worse tail
statistics
because you're throwing the same number of
balls into more bins.
The ratio of the worst bin to the average
bin gets much worse.
And so that deterministic routing that
Mark talked about
where we can do this kind of very careful
load balancing
across these very huge number of links is
very important to avoid getting into a bad
situation
that we would then have to kind of have a
feedback loop to recover from.
And so kind of all of these pieces of the
stack are extremely tightly coupled
together, right?
It is extremely important that we have
kind of low-level network hardware people
who have
some understanding of what is happening at
the workload layer.
And we have people at the workload layer
who have some understanding of what the
heck is
going on inside a network switch.
We really wouldn't be able to push the
boundaries of how big
you can make these systems without that
kind of vertical
integration and everyone pushing in the
same direction.
When people talk about data centers--

[00:35]
and you mentioned this earlier--
there's what you use for training, there's
what you use for inference.
When I asked ChatGPT, I don't need to talk
to the whole data center, I
need a few GPUs who are going to answer
this question.
And there's been talk about, well, the
next step
is we're going to put things into space.
And my question's always been like,
I can get-- like, I have a satellite with
some GPUs. It's doing inference.
But when you're literally spreading things
out across thousands or hundreds of
thousands of miles on a big network, it
seems like you lose all of your advantage
for speed.
The speed of light is your enemy versus
being in one center.
It's hard to envisage doing the sort of
training that we do in our Stargate data
centers in space.
Just the latency would be a huge problem.
And just the background rate of failures
would be a problem.
We have technicians from Microsoft and
Oracle who have to go in and fix things
all the time every day. Hard to do that in
orbit.
Yeah. Yeah. I think you can make all sorts
of arguments. And I have
gotten, I've gone very deep on this. As I
said, I have a physics background. I'm
very interested in,
you know, I worked with people who
designed satellites. You know...

[00:36]
things like that. Yeah. But I think a lot
of smart people have had very reasonable
arguments both
ways on that dimension. The major
barriers, I think, are the rate of
failure. I mean,
every GPU, every generation of GPU, the
GPU itself gets more powerful and more
expensive
and more important. I think we are doing
incredible work here on earth to try to
kind
of route around failures automatically but
i think that you would find yourself with
a lot of hardware
that you couldn't use very quickly if
you're shipping these things into space
now is there a
world in which you can also put
technicians in space maybe you can do all
sorts of things the
dreamer side of me says that would be
really really cool yeah the practical side
of me says it's
really really hard to do this stuff on
earth yeah like every day we are trying to
push limits on all
sorts of dimensions even just spinning up
MRC was a huge effort that required very
close
collaboration with us and engineers at a

[00:37]
number of other companies and it required
in some cases
you know hands-on machines to fix things
to test things etc these systems are hard
enough to build
and make work and make perform here on
earth i think trying to push the
boundaries of that and
also adding additional complications, you
have to make a really strong case for why
it makes sense to do it in space.
So build more terrestrial
compute centers.
Please. I mean, that is what we are trying
to do here, is build a lot of compute so
that we can increase the net amount of
intelligence in the world.
That's awesome. Gentlemen, thank you very
much.

</details>
