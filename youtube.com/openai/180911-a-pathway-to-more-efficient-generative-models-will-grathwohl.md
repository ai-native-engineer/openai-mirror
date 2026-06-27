---
title: "A pathway to more efficient generative models | Will Grathwohl | 2018 Summer Intern Open House"
channel: openai
url: https://www.youtube.com/watch?v=zG7KqhtQzQo
youtube_id: zG7KqhtQzQo
published: 2018-09-11
duration: "10:02"
captions: en-orig
---

# A pathway to more efficient generative models | Will Grathwohl | 2018 Summer Intern Open House

[![A pathway to more efficient generative models | Will Grathwohl | 2018 Summer Intern Open House](https://img.youtube.com/vi/zG7KqhtQzQo/hqdefault.jpg)](https://www.youtube.com/watch?v=zG7KqhtQzQo)

<details>
<summary>자막: A pathway to more efficient generative models | Will Grathwohl | 2018 Summer Intern Open House (10:02)</summary>

[00:00]
already yeah so I'm going to talk to you
about some of the work I've been doing
here with Sonic and alia on sort of an
Avenue that we think might be a
promising way to make invertible
generative models potentially more
efficient and more expressive and so as
I mentioned when you're defining or
designing an invertible generative model
you have two main constraints when when
doing this you need the model to be
invertible and you also need the model
you need the to be able to compute the
log determinant of the Jacobian of the
model and those are two pretty big
constraints and because of that we
typically restrict ourselves to simpler
architectures where those things are
easier to compute and because of that we
are using these simple transformations
we must compose a whole bunch of them
together to build an expressive model
and as you as Sayaka mentioned is the
case with the gloww model and if we

[00:01]
could potentially use more expressive
transformations at every step of our
flow then there might be a step for us
to to build invertible models that are
more expressive use less parameters and
potentially use less computations so in
some of the work we've been doing we
took kind of a different a different
look at these types of models and if you
look at them in a different way
something the math changes in a way that
provides an avenue for for maybe
improving the models so you can think of
a flow based model as parameterizing a
discrete-time dynamics process where you
start at time 0 at the data and then to
get your next time step you just apply
every step of the flow and then you you
encode your data by moving along all the
way from time 0 to the finish time and
then you can compute the likelihood of
your data simply by the likelihood of
the final sample under the prior plus

[00:02]
the sum of the log determinants along
the way and if we kind of take the limit
of time to infinity then this basically
looks like a continuous time dynamics
process where instead instead of having
individual flow models parameterize the
derivative at every single time step we
can throw all of that into one model
that's going to take in the current data
point and time as well and then
parameter i's the gradient exactly and
then what this gives us is the exact
parameter a ssin of an ordinary
differential equation initial value
problem and the coolest thing here is
that if we look at the log probability
from the change of variables formula now
in the continuous case we have a
difference a different term here instead
of the sum of the log determinants we
actually have the integral of the
divergence of the function that defines
the gradient and just looking at those

[00:03]
two things next to each other
the form is very similar except now we
have this integral of the divergence
instead of the sum of the log
determinants and that's a very
interesting dichotomy there because the
determinant has a lot of different
properties than the divergence and
specifically in general if we have an
arbitrary function that goes from RN to
RN then computing the log determinant of
the Jacobian is going to is going to
work in n cubed time once we have the
Jacobian which is also challenging to
compute and there's really no efficient
way to get a to estimate this and there
is no like efficient unbiased estimator
but with the divergence we can actually
produce an efficient unbiased estimator
just using automatic differentiation and
and that estimator basically just works
by sampling like a Gaussian probe vector
and then pre and post multiplying the

[00:04]
Jacobian Phi that vector and then in
expectation that's going to give us the
divergence of the vector field and then
we can similarly use this in the
integral form of the log-likelihood to
get an unbiased estimate for the
log-likelihood which is not something we
can do in the in the discrete-time sits
situation and here's just a little three
line kind of tensorflow implementation
of how you would implement this
estimator and the cool thing here is
that using this now we have a way to
parameterize these invertible generative
models using an arbitrary neural network
and we also have a way to efficiently
train them just using back propagation
or standard automatic differentiation
tools which are you know very common
today so there are some problems here
because we have alleviated a source of
complexity but we have added another one
because now instead of a very simple
like known computation process where we

[00:05]
just apply the you know n flows that
we've defined we must now integrate
actually this OD e and that is
potentially challenging and it's kind of
been the the main area of of work that
we've been doing trying to make these
models actually tractable and training
them around the same scale of time that
we could before and an even more
challenging we have to now back
propagate through the solution of an OD
and get the gradients of the outputs
with respect to its inputs and the
parameters that define the flow function
thankfully there was some recent work
from the University of Toronto that
presented a method that to do this and
we've been building upon that method in
this work and the basic way that works
is you can actually get the gradients of
everything you need just by solving an
Augmented system of ordinary
differential equations and while this is
kind of out of left field from the deep

[00:06]
learning kind of a type of work that we
do there's actually been quite a number
of decades of history on numerical
methods for solving au des so there's
decades of work that we can draw upon to
a to help us out with that part of the
problem and and so here's a somewhat of
an example of some of the results I've
gotten so here is the continuous
normalizing flow on the left here and on
the right we have the glow model and so
in general I have not quite beaten the
results of the glue model yet and I
think that is mainly because the models
currently take too long to train so I
haven't been able to make them as large
as I would like to but I have noticed
that I have been able to get competitive
results with
real MVP and in some datasets I have
beaten the glue model and so I think
it's a very promising Avenue and I just
think there's a couple kind of little
issues that we need to solve before we
can really get these models to to
deliver the goods and I guess just

[00:07]
here's a little kind of visualization of
one of these models in the working and
basically we've started from the prior
distribution there and that was the the
continuous normalizing flow model
actually integrating samples from the
the prior distribution to match the
target distribution and so that was just
in a simple two dimensional problem but
this also works quite well on some
higher dimensional data so here is M
this and as you can see over here these
are actually going to be the digits that
are being warped by this is the gradient
field here that is being applied to them
and then that is being integrated and
actually warping them into what should
look like Gaussian noise and once this
finishes it will go backwards and it's
pretty fun to look at yeah and the cool
thing about this model is that this is
just like one one neural network that
kind of has like an auto encoder type
architecture and that neural network

[00:08]
just takes in these the images at every
time step that they've been warped and -
the time itself and it just
parameterised the gradient and all we
need to do to apply this transformation
is integrated and and yes that's most of
what I've been working on here and if
you anyone is interested feel free to
reach out to me there's my email and you
have any questions
[Applause]
oh that's typically just to got a
standard isotropic distribution yeah
yeah I mean yeah that's the standard
stuff I mean I've tried some other like
more structured prior distributions and
that like I did some earlier work here

[00:09]
where I was working on using these
models for like semi-supervised learning
so you could put like a mixture of
gaussians on some of the you know some
of the vectors and that has an
interesting effect of modeling you know
class conditional probabilities pretty
well but for all this work it was just
standard Gaussian distributions just log
like we herded the data yeah like that
was the if you go well if we could go
back a couple slides the bits per
dimension is typically what what people
do which is sort of like like you know
log probability would be typically for
you know written in Nats and then you
just compute that from that's two bits
and then average it over the dimensions
that's the standard metric people use in
the density estimation space

</details>
