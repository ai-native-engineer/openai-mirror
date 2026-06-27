---
title: "Robust Vision-Based State Estimation | Hsiao-Yu 'Fish' Tung | 2018 Summer Intern Open House"
channel: openai
url: https://www.youtube.com/watch?v=hyZ1sRfRbgM
youtube_id: hyZ1sRfRbgM
published: 2018-09-11
duration: "16:46"
captions: en-orig
---

# Robust Vision-Based State Estimation | Hsiao-Yu 'Fish' Tung | 2018 Summer Intern Open House

[![Robust Vision-Based State Estimation | Hsiao-Yu 'Fish' Tung | 2018 Summer Intern Open House](https://img.youtube.com/vi/hyZ1sRfRbgM/hqdefault.jpg)](https://www.youtube.com/watch?v=hyZ1sRfRbgM)

<details>
<summary>자막: Robust Vision-Based State Estimation | Hsiao-Yu 'Fish' Tung | 2018 Summer Intern Open House (16:46)</summary>

[00:00]
hi everyone my knight is fished home I'm
currently a PhD student in Carnegie
Mellon machine learning Department I'm
interning the robot II teams working
with Peter and watching today I'm going
to talk about robust vision based stated
estimator so the goal for the robot II
team is to actually build a very strong
robotic background such that we can use
it to solve real AGI you know we we are
focusing on develop in general learning
based algorithm such that it can works
on a diverse of robotic tasks in order
to make sure the algorithm we develop is
general enough we need to pick up like a
pretty hard task in order to make sure
this algorithm really work so the task
we pick here is to have a shadow hand

[00:01]
rotating object to a desired pose so a
shadow hand robot is a robot that looks
exactly like human hand it has five
fingers it has several joint it can do
very delegated posts this task is
particularly difficult because if you as
a human engineer to hard-code this high
dimensional control it is nearly
impossible but before the robot can
start moving his fingers and try to
solve this task the first question we
want to answer is how do then the robot
know where is the object and what is the
object is posing in other words how do
the robot know what is the position and
orientation of the object in robotics
and reinforcement learning we call these
two state to ask the main States you can
actually use a 3d tracker
to use a 3d tracker you need to attach
some markers on the object you are
interested in we put our robot in a huge

[00:02]
cage where we can surrounded our robot
with a bunch of 3d sensors this sensors
will read off signal from the trackers
and then tell you what is the street
location of this markers so as you can
see this method actually can give a
pretty accurate object state but it is
pretty expensive and it kind of restrict
the robot to only see object in this
cage and besides if today I have a new
object I need to ask somebody to label
the marker first for me
which is impractical so here we want to
use like a more biologically inspired
solution which is just use cameras so we
can set up three cameras on this cage
the cameras are looking at our robot and
our object and from there we try to
infer the state of the object
so there are several benefit of building

[00:03]
a vision based state estimator it can be
more flexible as cheaper is easy to set
up and it's really what we want to feel
on our robot
so to summarize our environment look
like this you have the cage you have the
robot in the center you set up some
camera that is looking at your robot and
your object and from this cameras you
captured three images that is looking at
the scenes from a different point of
view and then the question we want to
ask is how do we go from these three
images to the state we want to know so
now I introduce our method our model is
a tip neural network we say neural
network is super powerful because it can
generalize a lot of tasks achieving
state-of-the-art results and most
importantly it doesn't require the
engineer to hard-code the features so
before going into how to train this

[00:04]
neural network let's go into detail of
how this new an hour actually looks like
so our now we're taking three images as
input we will pass each of the image
into several convolution layers and
fully connect layers and then we
aggregate an output from this
convolutional towers to predict our
final object state to train such Network
you need aside from the network itself
you
two additional seen one is a large
amount of data that contains a lot of
example of what are the inputs and what
are outfits like for here our inputs are
the three images and our output is the
state of the object so so then the
question is how do we get this large
data set we say it is impossible to get
it in the real world although we are
able to get the images we are not able
to know where are the objects so in
order to solve this problem we actually
use a simulator in a simulator we build

[00:05]
a very similar robot a very similar
object and we also set up three very
similar cameras that is shooting from
right top and left and then from this
simulator we can actually also read off
ground true state of the object so our
training data actually looks like what
what is on the right hand side that we
have three images pair with the ground
true state of the object besides that we
can also because it's in the simulator
we can easily change the texture and
color of our robots we can change the
lightness we can also change the
background so in to if we do that we can
get like a very diverse data set that
can cover maybe all the situation agent
my my encounter in the real world so by
having this large amount of data and
this objective function that basically
minimized the distance between your

[00:06]
prediction and the ground truth we are
able to train the network in the
simulator and it works well in the real
world so it actually can predict super
accurate state of the object in the real
world and we are able to use it to
really solve something with with this
state estimator however there's still
some problem with our current vision
system the problem is our simulator
actually need a very carefully aligned
camera in in in the simulator
means your camera need to have exactly
the same position as the one you have in
the real world so how we get this value
is the engineer need to go into the
simulator slightly adjust this camera
until the images are super aligned so
this actually requires extra effort
because every time we change the camera

[00:07]
rotation we need an engineer to do this
again another thing is if during test
time someone accidentally touch one of
the camera on the cage then the vision
system break so here I want to emphasize
how serious is this problem so I show
some state prediction error on real
images using a calibrated environment
and not calibrated in problem and you
can see on the blue curve is with
calibrated cameras and the others are
with misaligned camera and the
performance degrades a lot so why this
is why this is happening
because our neural network is actually
trying to find out someone useful
pattern and from this useful pattern you
want to drag LIGO to you the output you
want you want it to be predict because
your only objective function is this
Euclidean distance between the branches
and your prediction so if we sit back
and think how people figure out this

[00:08]
problem is I have this hand here today I
want to ask you like what is the
position and orientation of this cube in
this 3d coordinate system given only
this image captures from some random
camera well what will you do you
probably will say oh yeah of course
today we focus on objects so I
definitely need to like focus on the
object and you probably will also say I
want to know where this images captured
from so you might also look at the arm
of the robot to figure out what is the
camera position combining your object
detection and your position of the
camera all together you figure out what
is the global state of this object so in
order to answer this
and actually human need geometry
knowledge and also human need attention
on the right object so then the question
is how do we tell the robot that these

[00:09]
tools are important and you need to
somehow encode this in your solution the
solution is because in the simulator we
can get a bunch of 3d information we can
get whatever branches we want so in
order we can actually extract more
information from the simulator and then
add these two to the neural net we're
trying to tell him so let me introduce
these two so the first one is we want to
force the network to learn about
geometry so we say when we are doing the
previous practice we're actually trying
to infer where the camera is shooting
from so on top of the output there of
each of the image I will add an optional
task to say oh please predict as well
the camera position orientation to make
sure that the robot really understand
where this image is captured for so
biting adding this accurate test we can
actually improve the prediction on

[00:10]
position of the object so you can see
the red line is without this actuary
task and the green line is with this
after a task so by adding this we are
actually forced in an hour general to
generate like a more reasonable solution
for this the other scene is we want to
cast right attention to to this task so
previously we say oh because we are
answering like what is the state of the
object so we definitely need to watch
the object instead of focusing on the
background so we circle the object and
we say if I want to answer what is the
position of the camera I probably need
to focus on the arm of the robot so
these tools are the same we we feel like
the robot should add this focus on so
here I asked the robot to further
predict bounding box for this to object
note that the
pounding bass can be obtained from the

[00:11]
simulators in a simulator we can get
like any kind of cultures we wanted and
then from this bounding box location we
extract localized features and
concatenate lists localized features for
our final prediction so by doing this
this kind of forced attention actually
the network can improve on orientation
prediction so the red line is a bad sign
without any attention the blue line is
with attention on the cue and in the
bottom line the orange one is actually
forcing attention on the cube and also
the art of the robot so here is some
conclusion and take away from me is we
are proposing like a learning-based
vision system that is very robust to the
camera position and we also hope it can
transfer transfer well to the real
setting so previously in our release we

[00:12]
proposed this domain randomization where
we randomized all kinds of like textures
lightness and background in the
simulator but here I want to emphasize
like in order for for our visual model
to really understand 3d to understand
geometry
maybe we can extract more supervision
from the simulator the first thing is we
can enforce in geometry learning by
adding actual tasks like predicting
camera bells and we can force in right
attention by asking the the vision
system to predict bounding box and also
use the attended feature thank you
we have like a 1 minute Q&A oh okay hi
oh please you'd still so so actually I

[00:13]
have tried to randomize the camera
position like crazy like the camera can
move all around in this space but then
this actually decreased a lot on the on
the prediction of overall even in a
simulator so that means if you just have
this naive model that fit in image
passing through some convolution it is
now going to figure out this answer and
also we try to randomize the camera
position in our preview release and it
kind of like heard the final final
performance on the real image so we kind
of remove it so the thing is or narrower

[00:14]
structure is not good enough so that
even if we randomize the camera so much
it cannot learn something useful so it
needs something else to help it thanks
oh one more question
Oh does anyone too
hi how do you think that your approach
would work when cameras not in the hand
because you know camera will have you
know you have the extra complexity of
the depth sensing and so wise
differences there are types of wines
differences are not necessarily always
reflective of real-world difference in
distance so yeah how do you think that
this would work when the object is
further away it's further away so if the
object is kind of like it has a
distribution that is not in the

[00:15]
distribution we train then it definitely
will diverge in the real like we cannot
make sure or do you mean if we have
extra at that sensor well they help so
my question is more like do you think
the methodology would also apply when
you have the object further away such
that you have right here is that you
want the robot to be able to point to
the object yes so it's the state I guess
would just be the position of the object
so if all the cameras are here and like
kind of enclosing the robot there were a
lot of hand in a cage and the object is

[00:16]
over here yeah sure you can have all the
camera positioning and stuff figured out
but you want this extra distance to
account for right that the depth
perception capabilities with the camera
yeah so do you think that I think it's
like it's more like how do you think
that this approach
so I think that extra complexity can be
solved if you have like an additional
camera that is looking at the side so
then you can make sure this dimension is
correct but the thing is if something is
super far away like even for human like
if you have a car that is super far away
like is cross the street for you you
cannot predict precisely like what is
the distance between you and the car

</details>
