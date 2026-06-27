---
title: "Physics Net | Ifu Aniemeka | OpenAI Scholars Demo Day 2018"
channel: openai
url: https://www.youtube.com/watch?v=wSVwTszUrck
youtube_id: wSVwTszUrck
published: 2020-07-02
duration: "12:14"
captions: en-orig
---

# Physics Net | Ifu Aniemeka | OpenAI Scholars Demo Day 2018

[![Physics Net | Ifu Aniemeka | OpenAI Scholars Demo Day 2018](https://img.youtube.com/vi/wSVwTszUrck/hqdefault.jpg)](https://www.youtube.com/watch?v=wSVwTszUrck)

<details>
<summary>자막: Physics Net | Ifu Aniemeka | OpenAI Scholars Demo Day 2018 (12:14)</summary>

[00:00]
so hey everyone thanks for showing up
tonight
Thursday night Phyllis my name is equal
a new Mecca and I'm a software engineer
from Chicago and today I'll be talking
to you about physics net I couldn't come
up with a clever name for it so we're
still gonna call it and as you can see
it's it concerns training a model to be
able to predict the motion of objects in
a environment
so physics nerds prepare yourselves
alright so from a pretty early age human
beings are able to do some pretty
complex things right so within roughly a
year of being born you should have been
able to throw things you hopefully were
also able to track falling objects with
your eyes and within a year most
children can pick up objects and

[00:01]
unfortunately put them directly in their
mouths temper this this little super
smart doesn't do that kind of thing so
without being told at any point you sort
of gain beginning intuition that say for
example if you throw a ball into the air
it'll follow a roughly parabolic
trajectory you also know that if you
throw this ball at a wall or whatever
I'm sports not my thing you know that it
will it'll bounce off of that of that
wall so the purpose of my project was to
try to train a model to figure out how
objects move in space without explicitly
being given concepts like force or
momentum just to like to get it from the
same way that weekend in which is via

[00:02]
observation of course all of this is in
service of eventually constructing a
robot army because you know
they need to understand that you have to
aim where the target will be and not
where it is so to create the
environments
I used JavaScript physics engine called
meta jeaious so you can kind of see from
the way the circles are moving this
doesn't perfectly mimic the real world
all of these collisions are perfectly
elastic
there is no spin so there's no angular
momentum there's no air surface friction
so effectively if you keep the recording
going the balls just travel forever so
this is a fairly elementary thing to do
for a human being right so on the far
left you'll see circles at time let's

[00:03]
say like T equals zero right
that's position 1 the frame in the
middle that would be time like T equals
1 the outward circles are in a different
position in that last frame you can see
some vectors that are being drawn
between the initial position of the
circles and their final position right
so we kind of do this subconsciously and
because we're able to do this so easily
we can guess the next position of each
of these circles you see these the the
circles outlined in red or obviously
like the the final positions in the
third frame and this is basically what I
asked I asked my model to do I give it
two frames with circles in obviously
different positions and then I would
have it guess what's the third frame
where where will the circle be at the
next time step so the model wasn't given
images act exactly like these these are

[00:04]
rectangles and you know a white space
it's actually given samples like this
they're somewhat pixelated the actual
samples are 28 by 28 pixels so we can
blow them up they look like this
but that is actually enough information
for the model to be able to figure out
what it needs to figure out so this is
the architecture of my model it's a it's
a convolutional auto encoder so as you
can see at the top with the encoder I
what I did was I took two images and I
essentially you stacked them and I fed
them through several convolution layers
and at the end of that the decoder at
the bottom the decoder is the portion of
the network that actually essentially
like undoes the convolutions and
reconstructs the image so at the top I
give it two to the initial images and
then at the bottom it constructs that

[00:05]
third image I'm gonna give you a sort of
a quick rundown of what the model
produced during training but to start
with it's not really producing much of
anything right it's just a gray square
after about 2000 epochs it figures out
that it should generate generate walls
but as you can see the walls are not the
right color they're white and also
there's nothing inside of the box after
about 4000 epochs it actually has
figured out the color of the walls
they're gray which is awesome but still
nothing then it starts producing smudges
after about 6000 epochs you can see like
in the middle there just purplish
something going on and in the lower left
corner there's something greenish that's

[00:06]
kind of what we're looking for
over time it gets more accurate this is
pretty close
I constructed in animation just to give
you a better idea of what it predicts so
on the left is the target and on the
right is what the network predicts I
constructed the animation on the right
by taking the two input images that I
gave the network and then concatenating
it's prediction on the on the end of
that so you can see it's pretty good
with velocity position specifically
right after each time step but the
colors are a little off right like the
the circles are flickering so there's
some imperfections here that could be
fixed but I was I was pretty happy to
see that you know it's it's it has an
idea of where of where the circle should
be so next s right the point is is for a

[00:07]
model that generalizes to how the world
works using not not too many samples
right so one of the things I want to do
is essentially want to add complications
to this environment one would be to add
barriers or like walls inside of the
environment to see that it understands
that great wall means bounce off right
another thing I could do would be to
change the environment shape which is
another sort of generalization around
bouncing off walls adding friction
there's there was no friction in in the
original environment fixing the issue
around the colors in the frames keeping
them stable and another thing I don't
really mention here is adjusting the
framerate so how I chose the framerate
was a somewhat arbitrary but I don't
know if that was a noble thing

[00:08]
essentially I wanted to have a high
enough framerate that if a circle
bounced off a wall it wouldn't be such
that for example you know it's like a
little ways again from the wall at time
step one and then like pretty far away
from the wall at time step two I wanted
enough frames per second that
I would I would I would capture it
getting pretty close to the wall and you
know eventually bouncing off so I'd like
to see you know what happens when I when
I when I adjust the frame brakes either
higher or lower just like it's kind of
see what happens so yeah there's a lot I
could do with this and I'm really
excited to you know experiment some more
if you want to find me I'm on twitter at
ing Becca you can go to my personal site
at life is algorithm calm and you can
find me on github Larissa told me not to

[00:09]
say Terminator she called it the T word
so I I see I didn't Larissa I didn't say
it I just put it I didn't well I did its
we're fine we're safe everything's good
so yeah thanks for coming give any
questions you can feel free to ask them
now and so I'm not sure how to rephrase

[00:10]
your question but you're you're sort of
theorizing that maybe additional
computation would help deal with like
the color issue we should talk later
okay let's talk about this I don't yeah
I'll show you the code and you can fix
it for me any other any other questions
you ever because if we never trained it
on c3
oh um I'm not sure that it does I are
you are you commenting on I'm sorry so
the question is about how how would the

[00:11]
model dealt with the blurring like the
blurry pixels Oh ml magic eye yeah I
didn't do anything like special to get
that to happen it just like oh that's
your question okay so yeah you're the
question is around like how over time it
figured out that the balls are not like
smeared and actually sort of brought
them together into like a single link
central location um not sure we know how
to answer your questions
see no well yeah we'll talk about it

[00:12]
later
yes yeah thank you for coming don't be -
when we're back in play
[Applause]

</details>
