---
title: "Generative Modelling | Sadhika Malladi | 2018 Summer Intern Open House"
channel: openai
url: https://www.youtube.com/watch?v=0cQrZxMFDEM
youtube_id: 0cQrZxMFDEM
published: 2018-09-11
duration: "12:43"
captions: en-orig
---

# Generative Modelling | Sadhika Malladi | 2018 Summer Intern Open House

[![Generative Modelling | Sadhika Malladi | 2018 Summer Intern Open House](https://img.youtube.com/vi/0cQrZxMFDEM/hqdefault.jpg)](https://www.youtube.com/watch?v=0cQrZxMFDEM)

<details>
<summary>자막: Generative Modelling | Sadhika Malladi | 2018 Summer Intern Open House (12:43)</summary>

[00:00]
hi everyone I'm Satya I'm an undergrad
at MIT I'm doing my internship here at
open AI broadly my internship is about
generative modeling and so what are
generative models they are models that
generate data within some kind of
distribution so for example if you give
your model to train on dogs then you
want your model to generate images of
previously unseen dogs why is this
useful it's not an inherently clear from
my explanation but when you're able to
generate images of dogs you hope that
your model has learned something more
something more useful about exactly what
is in the images of these dogs and that
learned some kind of structure that's
important so there are many applications
for these types of models the first one
I'll be talking about is world modeling
and well modeling is useful for sample
efficient generalizable reinforcement
learning so what exactly is world
modeling well in our hopes and dreams we

[00:01]
want our agents to first learn basic
movements so for example when you're
learning how to walk you learn how to
put one foot in front of the other then
you learn how to turn directions without
falling and maybe even go backwards once
you learn these basic movements you no
longer need specific instructions on how
to get from the couch to the TV or from
your house to school because now you
have a sense for how basic movements
cause interactions in your world and so
the idea is if we can train our agents
this way then hopefully they're able to
do more complex tasks that they haven't
necessarily been trained to do and we
can train them a lot easier using
transfer so we want to use less data to
train our agents because it's expensive
to collect this data from our games
that's specifically like episodes and
things like that so in this example here
I have a basic game called car racing
and so in this game as you can imagine
when you're learning how to drive a car
you learn how to go forward faster how
to slow down how to turn and so you can
see in the video that the car is able to
go on this track and it's never actually

[00:02]
seen this track before and so it's
learning how to turn and when it messes
up it's able to recover because it knows
exactly how its its movements will
interact with its environment and so
this is why model based reinforcement
learning agents would be really cool and
these are our hopes and dreams for them
but alas there are some shortcomings so
first of all a lot of the
implementations out there right now for
model-based reinforcement learning are
game specific they're also difficult to
train kind of finicky and one of the
biggest problems is that if you have a
small artifact when you generate a frame
of a game when you keep rolling out and
trying different actions within that
particular world model you're just gonna
build up on your artifacts you're never
going to be able to fix that and correct
for it and so these small errors can
propagate really quickly and cause a lot
of problems when you're rolling out and
obviously for some number of these
reasons we're not able to get
model-based agents to do as well as
model free agents so in the example I
show on the right I'm showing the same
exact model that trained the car racing

[00:03]
video but now you can see in the ground
this is a game of pong you have two
paddles in the ball you want to keep the
ball and play but when you reconstruct
after encoding it you no longer see the
ball you no longer see the other paddle
and so what I mean by reconstruction
I'll explain in a second but key part
here is that you're not able to see the
important parts of the game so you're
not you don't know where the ball is and
so it's hard for the model to learn so
how exactly was that car racing video
trained while you take a frame and you
run it through a variational auto
encoder so you run a series of
convolutions to get some layton's which
I represent with Z here and then you run
a series of D convolutions to get a
reconstruction of your frame and you
compare that reconstruction to the
original frame in order to get some kind
of error that you train with you also
give these Layton's which you hope
provides some kind of context of time
dependent state in your game to an RNN
and your R and then is going to keep
track of things like where are you in
the game how far your obstacles what

[00:04]
exactly is your specific game state so
the key here is that you don't want your
Layton's to be wasted in encoding
something that's true of all game States
so for example if you're running through
a grassy meadow
you don't want your Layton's to only be
encoding grassy meadow you want them to
encode something like oh there is a rock
there that I could trip on or something
like that so in this video that I show
it's again the car racing game on the
left you can see a video of the ground
truth and on the right
you can see what the model actually
reconstructs you can see it's pretty
accurate it doesn't have those red
bumpers which aren't really that
important but the key part here to
notice is why this worked on car racing
and not on pong is because there's so
few elements in car racing there's only
the track and then there's this green
highway so if you can roughly model
those you're able to train your agent
pretty well but it's not generalizable
to more complex games or games where you
have multiple scales of components so

[00:05]
how do we seek to improve this well when
we pair our BAE
or our encoder with a strong decoder
then our Leighton's are forced to mean
only things that are dependent on the
time which is what we want so for
example in this case when they use a
pixel CNN and we condition our pixel CNN
on the time state of our game then we're
able to force our Leighton's to just be
something like oh there is an obstacle
at X Y what does that obstacle look like
well that's for the pixel CNN to
generate and so by doing this we're able
to create a more robust model of exactly
how learn and how we think because I
know that I could trip over this table
but I also know I could trip over that
couch and the details of what I'm
tripping over aren't that important it's
just that I shouldn't trip so we also
know that pixel CNN's can generate
really high resolution images and so we
hope that they can generalize to games
that look a lot richer than just the car
racing game or the pong game even so

[00:06]
this is the work that I've been doing
with world modeling now I'm going to
transition to talking about how I've
been using generative models in the
context of invertible flow models
invertible flow models are known for
being expressive models with efficient
sampling before I talk about the
architecture I'll show exactly what I
mean when something's expressive this is
a video of my friend Prafulla
but in those gonna be here but he's here
and basically basically what you can see
here is propolis face morphing into
different celebrities faces now why is
this impressive because in order for our
eye to look at that and say wow that's a
realistic morphing every single one of
the images that
generated on the way there has to look
like a like a person's face if something
looks grotesquely wrong we will notice
it right away and so this is telling us
is that when you use an invertible flow
model you learn the latent space so
richly that you can interpolate between
them coatings of different images and
still have a reasonable interpolation so

[00:07]
in my mind if I were to imagine prava
becoming neil degrasse tyson this is how
i would imagine it but i don't do that
often so what do we hope what our
expectations of flow based generative
models well what we want to do is take
some random noise as you can see in the
image on the far right you take some
noise that's sampled based on some prior
usually with the tractable density and
then you warp that via your model into
what you want to see so maybe it's faces
maybe it's cats and dogs so basically
what these equations are saying is you
sample a Z from your prior and then you
run that Z through your invertible
network in order to get basically a
generated output so now f needs to be
invertible our model needs to be
invertible and we can use the
statistical change of parameters formula
in order to write exactly how the
log-likelihood of the input can be
expressed in terms of this model and so

[00:08]
when we do generative modeling we always
want to maximize the likelihood of
generating whatever input we get because
that's our best bet at making something
realistic here what you have is you see
that that likelihood can be modeled as a
likelihood of generating whatever that
random noises person prior - the log
determinant of the transportation the
transformation between the latency and
the inputs reality stuff it takes a lot
of effort to design a fully invertible
model there are very specific components
that can be used and each of those
components tends not to be very
expressive so when you have when you
want to build an actual model that's
able to turn noise into phases you need
to use an extremely large model which
requires a lot of memory and so as you
can see I have placed this meme here to
demonstrate my frustrations in
which you build a large model and you
want it to be tractable but no matter

[00:09]
how much memory you have you always run
out of memory yes so the types of
transformations you can do our things
like affine transformations or
one-by-one convolutions and I can talk
more about that when I talk about the
specific architecture so the first flow
model was called real NVP and on top of
that people that open they I have
refined it to make what's called globe
there aren't that many differences
between the two but the basic idea is
you take an input and you have a multi
scale architecture which means that
because you're only able to do one by
one convolutions you're only able to
pick up features at a particular scale
so you need to warp your inputs and
reshape them so that you can pick up
features on different scales and so you
squeeze which means you just changed the
dimensions and then you go through a
step of flow which is shown on the left
and then the step of flow is just a
simple normalization convolution and
then there's a coupling layer where you
split again and you run half of it
through a deep network and you run the

[00:10]
and you just let the other half go
through this deep network in the
coupling layer is what takes up the most
memory in our flow models so when I
thought to work with these models I
shared the parameters across the
coupling layers across all of the
different steps of flow and you would
think that well that's a lot of
parameters that you're losing that's
probably like one out of every 32 flow
steps is going to be actually expressive
but what I found was you can generate
very realistic-looking samples and match
the bits per dimension using 3% of the
memory that you did before and it goes
33% faster in terms of wall clock time
and so these are just C far 10 samples
and as you can see on both sides they're
pretty realistic yeah so that's pretty
much it for my presentation will is
going to be coming up here to talk a bit
about the work we've been doing together
on improving flow models in other ways

[00:11]
oh yeah yes yeah yeah so in our and new
architecture we only encode so we only
go from the inputs to the Layton's and
then we use the Layton's as a
conditioning vector for the pixel CNN so
the raw input also goes to the pixel CNN
and that's why what comes out of the
pixel CNN is what you actually train in
comparison to the true inputs did that
kind of make sense any other questions

[00:12]
so there are actually some troubles that
come with invertible models so the
biggest Pro of using an invertible model
is that you can sample really
efficiently so to draw random noise is
easy and then to run it backwards
through the model is also easy however
because you are constrained by having
these invertible components you're
forced to have a different level of
expressivity and these can also be
finicky to train because you can go into
regions where it's no longer invertible
or you fourth you're like forcing it to
be invertible and it's not able to
express what it needs to and this is
part of what my work with Lille has been
addressing

</details>
