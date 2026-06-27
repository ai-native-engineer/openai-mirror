---
title: "Learning Dexterity | Alex Ray | 2018 Summer Intern Open House"
channel: openai
url: https://www.youtube.com/watch?v=lmyU2VF_MGo
youtube_id: lmyU2VF_MGo
published: 2018-09-11
duration: "15:36"
captions: en-orig
---

# Learning Dexterity | Alex Ray | 2018 Summer Intern Open House

[![Learning Dexterity | Alex Ray | 2018 Summer Intern Open House](https://img.youtube.com/vi/lmyU2VF_MGo/hqdefault.jpg)](https://www.youtube.com/watch?v=lmyU2VF_MGo)

<details>
<summary>자막: Learning Dexterity | Alex Ray | 2018 Summer Intern Open House (15:36)</summary>

[00:00]
last hi folks I'm Alex Rey I'm on the
robotics team here and this is gonna be
a different sort of talk this is an
overview of a recent large team result
and instead of being these like really
great in turn projects unfortunately
they're they're limited on people and
limited on time this is about 12 months
worth of work for about 12 people so
there's a lot to get through I'm only
going to scratch the surface of it if
you want to learn more we have a really
well produced three-minute video it's on
YouTube in our website it's really cool
overview we have a blog post that's a
nice like human readable format as well
as like a longer research paper on it so
lots of different levels of detail but
for now I'm gonna give you an overview
of what we did and sort of like a peek
into the inside of it so quick outline
of like I'm gonna break down my tiny
amount of time is describe the task the

[00:01]
sort of problem we try to solve the
research process itself sort of like
what solving it looked like the systems
we built which were actually very very
simple and what results we got from them
so our task we have this five finger
dexterous robot hand it's under actuated
it's got 20 degrees of control and 24
degrees of freedom for reinforcement
learning folks that deal with continuous
control that is an awful lot and we have
objects in the hand that we would like
it to be able to manipulate and for us
manipulate means achieve arbitrary
rotations so if you imagine holding a
small object in your hand can you point
it in arbitrary direction without
dropping it so our primary goal this was
sort of our North Star we want to
manipulate this object of the robot hand
and specifically we want a sequence of
50 independent randomly drawn rotations
some secondary goals that we wanted to

[00:02]
hit but weren't exactly necessary where
we would like to solve it from vision
which means you don't need a specialized
object you can just drop the object in
the hand and like as long as your vision
model can see it you'll be able to
related we want to manipulate diverse
objects so not just cubes that say the
letters have opening on them and we want
to Train using a physics simulator
without any real data and so again our
North Star is a primary task the rest of
it or things that are sort of reach
goals so here like fish demonstrated
here's an example of our physical setup
there's this giant cage with a robot
hand in it and on the other side is our
simulation rendered with our simulation
renderer the robot is a giant bag of
unmodeled effects it has backlash it has
transmission problems it has creep and
stretch in the tendons and the simulator
has none of that here's our secondary

[00:03]
goal of the the cameras is just sort of
showing where the cameras are in the
cage our secondary goal of diverse
objects this is manipulating a
octahedral prison which is kind of cool
and then trading purely in simulated
data so this is all the stuff we have
during training is we both have a
renderer that simulates our vision data
and a physic simulator that simulates
our physics data and sort of the process
that we want to do it is a lot of
dealing with robot hands it's not all
training models but it starts with
training models so we really just over
and over for 12 months did this
iterative cycle that got faster and
faster as we got better at it it used to
take you no more than a month and now
we're able to do this in like a few days
we train a totally new model with
reinforcement learning that controls the
policy of the robot and a totally new
model for vision that is able to
localize the object inside the hand we

[00:04]
try running it on the real robot we
observe that it fails and we observe how
it fails and then try to improve it and
repeat so with all of these systems like
reinforcement learning with robotics
with deep neural networks with physics
emulation all of these are sources of
complexity so in all cases largely we
are trying to focus on building the
simplest thing Network
in the simplest possible solution so one
of the things we did was we started very
ambitiously and then eventually had to
break it down to a much much simpler
task we initially started with trying to
achieve six degrees of freedom on the
object so not only where is it not only
what direction is appointed but where is
it like lifted up off the palm and
things like that we simplified that to
be just rotation we simplified that to
be just major axis aligned rotation just
like get the x axis to be up then we
just tried spinning it around Z and then

[00:05]
when we had trouble doing that we just
tried reaching the fingertips to
arbitrary positions in space um
eventually we were able to climb back up
this ramp but this was a big part in
like unlocking a bunch of research
project progress quickly earlier in the
project another sort of thing we learned
along the way is that you have to try
lots of things at once in the blog post
and the the paper we describe two of our
vision tracking systems but we don't
really describe all the ones that we
tried that didn't work here's just some
I'm probably missing some we tried opto
optic tract like retro-reflective
infrared tracking dots these are common
in the motion picture industry we tried
depth cameras like a real sense or
Kinect we tried magnetic treat field
tracking like Palomas or like the sort
of early virtual reality controller
setups we tried active illumination
targets the face base those are those
red dots that you see on the fingertips
that actually did work we tried fiducial
and barcode tracking like a ruku and and

[00:06]
finally we tried the vision cameras and
while the paper sort of like is here's
the simplest thing that worked there's
quite a lot of things that didn't work
ahead of that and the final research
ingredient for like how we were able to
solve this task was lots and lots of
domain randomizations
we found that like instead of trying to
accurately model the robot simulating
the robot with with all of its basically
bagramon model defects would have been
effectively impossible and definitely
would have run much much slower than
real time and we want a fast simulator
so we added lots of domain
randomizations where instead of
accurately modeling the world you just
have to model the noise of the world and
some
the noise the world is more efficient to
sample from so for example we don't know
the exact friction on the hand we had
actually we didn't even really know what
units of friction were or what same
values were so additionally there are
things on the hand that might
approximate themselves as friction like
ridges due to machining or a little
screw holes that objects could get

[00:07]
caught in so additionally there's
different types of materials so instead
of like trying to accurately model these
we just took all the parts of the hand
which visually you saw sort of like
being different colors and we assign
them all very different frictions during
this time so somewhere along the project
we actually started we contracted a
professional roboticist to come in and
fix the hand whenever it broke because
we were breaking it so often and when we
told them what values of friction we
were using they were surprised it worked
at all but again these these these
simple systems are able to learn very
robust policies we also tried adding a
glove to the road trying to solve it the
other side so instead of solving it with
the AI solve it with the physical world
and it turns out gloves didn't end up
working which is sort of surprising to
us but the domain randomization did so
here's a quick overview of the system we
built a bigger graphic sort of from from

[00:08]
the one you saw from fish earlier we
have on the top left we have our policy
which is a very very simple recurrent
model and then in the middle we have our
vision model we trained both of them
separately they're not actually trained
together we tried that once and it
turned out to not help so it's
computationally cheaper to train them
both we did that and then when they're
rolled out on the real world we just
sort of like slap them both together we
take camera images from the camera we
pass them to the vision model it
generates observations for the position
of the object we add that to the sort of
observations to the robot give it to the
policy act and repeat for the neural
network nerds out there here is a rough
diagram of the vision model it's very
simple we like we're sort of surprised
this worked sort of like fish described
three combinational towers
that that all shared parameters you slap
them together and then you guess the
position from and rotation off them and
fishes work did a bunch to like improve
this result it turns out that we were

[00:09]
able to just use this and get it to work
on the real robot the policy
architecture is also very simple like
normal actor critic setup we have noise
observations and a goal that are given
to the actor the actor is the
interesting one the one on the left
because that's the one that actually
runs on the real robot
it's a Floyd connect layer and hose to
him and the output actions that's all it
took to achieve something that the field
of Robotics hadn't been able to achieve
before and then the value network has
more observation that's not noise so it
has basically more things going on but
mostly it's used to calculate advantages
during training so it's not actually
used on the real robot and we don't care
that it doesn't have to model the domain
randomization noise as much so this the
training architecture is like an
interesting part of the paper most of
what's involved in this is this is how
you get to training a simulated robotics

[00:10]
policy on more than 6000 CPUs and eight
GPUs
most of this is in support of just being
able to do that training this turned out
to be the simplest thing that worked and
not only was it the simplest thing that
worked for us we actually sort of
inherited it from a different team at
open AI a system we call a rapid and
it's the same system that powers the
dota bots so they have a lot of things
in common in in our paper we compare
both software actor critic and PPO but
the PPO is basically the same PPO that's
playing very very well against really
good players that dota 2 and then for
our robotic specific system we have our
robotic specific things and for the dota
specific system and they have their data
specific things sort of alright results
what we found out I guess the most
important result is that yes we are able
to do this task we were able to do

[00:11]
simple object manipulation we can learn
a policy from a division model purely
from simulated
data which transfers to the real robot
hand and then sort of our sub results of
other things we talked about is site
volt earlier we're able to act from
sparse observations so the actor again
the policy networks that thing on the
left is the one that runs on the real
robot that little X with note 4 is
interesting it's listed in the paper we
meant to include this we didn't as a
software bug and it still worked so I
was kind of surprising it turns out that
the we talked about some of the
surprising findings in the blog post
there's a lot of things that like are
counterintuitive to what traditional
roboticists would think that we are able
to figure out I'm going to go through
these real quick we are able to track
objects from cameras we have a very low
positional and rotational error lower
than real images part of it is that
gathering real data is really really
really hard and unstable if you like

[00:12]
bump something in a set up where you
change the how it curtain is hanging
your real data gets old fast but
simulator keeps on going we're able to
manipulate different objects we were
able to manipulate this octagonal prism
we tried a couple other objects that
around large round objects it has
trouble manipulating we're still trying
to understand that we're able to train
in a simple simulator even with all of
our innovations it still trains we're
able to show that the randomizations
that we added improved performance in
the real world I'm just going to skip
this because I'm out of time having an
LS TM is better than having a confident
is better than just being fully
connected running with more GPUs gives
you better performance yeah
[Applause]

[00:13]
oh man there's lots and lot
yeah they're all enumerated in the paper
the short answer is as many things as we
could for the visual we actually used
unity which is a video game renderer
instead of the default render because
video game render is give you lots like
in in pursuit of being more
photorealistic they give you many more
dials they you can adjust the metallic
nasur glossiness or like the the color
of the reflectance we randomized
everything we could on the physics side
we randomized as much as we that was a
more manual process it turns out physics
emulators mostly want to be accurate
they don't want to be inaccurate um and
a bunch of the effects were expensive to
model so we tried to simulate backlash
and we explained a little this in the
paper we don't get it exactly right
modeling backlash is a really really
hard problem but we can sort of randomly
move motors in the opposite direction
and that's close enough sometimes and so

[00:14]
the face base dots the dots on the
fingertips if you curl them all the way
in they can't be seen by the vision
system and they go away and it's hard to
model exactly which states those dots
disappear in but we can just have them
disappear for 25% of the time and it
roughly approximates it so yeah many of
it is is the things that we can figure
out that are easy to randomized we just
randomized by default and for things
that we think would help them that we
noticed on the robot and have hypotheses
about will you manually add every single
one does that sort of answer your
question
some so some randomizations help some
randomizations hurt some randomizations
sort of break-even in basically every
case were able to solve the task in
simulation this is something that's sort
of different than like normal academic

[00:15]
reinforcement learning in like mature or
simulated physics worlds is they care
that they can solve in simulation
basically everything we did we were able
to solve in simulation the only thing
that counted is if it worked on the real
robot and we're very very limited by how
many runs we can for every trial we
would have to run our baseline policy so
a policy with known performance just to
make sure the robot wasn't broken in was
behaving the correct way for a bunch of
times and then we'd have to run our
experimental policy a bunch of times
there's a bunch of domain randomizations
we're not sure if they improved because
we added them all at once and they
helped so we kept them all

</details>
