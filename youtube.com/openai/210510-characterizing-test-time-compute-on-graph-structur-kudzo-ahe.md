---
title: "Characterizing Test Time Compute on Graph Structur… | Kudzo Ahegbebu | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=8iz5v3Q0g9I
youtube_id: 8iz5v3Q0g9I
published: 2021-05-10
duration: "17:11"
captions: en-orig
---

# Characterizing Test Time Compute on Graph Structur… | Kudzo Ahegbebu | OpenAI Scholars Demo Day 2021

[![Characterizing Test Time Compute on Graph Structur… | Kudzo Ahegbebu | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/8iz5v3Q0g9I/hqdefault.jpg)](https://www.youtube.com/watch?v=8iz5v3Q0g9I)

<details>
<summary>자막: Characterizing Test Time Compute on Graph Structur… | Kudzo Ahegbebu | OpenAI Scholars Demo Day 2021 (17:11)</summary>

[00:00]
uh hi um my
talk is going to be about characterizing
test time compute on graph structured
problems
um most of my scholars project has been
spent thinking about
uh this question of whether we can uh
create models
that continuously improve their outputs
the more compute that we give them at
test time
this is something that i'll call the
test time compute dream
and i think there's much anthromorphic
motivation here after all as humans when
we're being evaluated our answers
tend to become better the longer we're
given to think
machine learning models for the most
part don't exhibit this ability which
seems a little weird so i tend to bucket
this test time compute stuff
into two general categories one is
generalization
improvement mechanisms which deal with
the question of how can we create models
that use test time compute to learn more
general algorithms instead of learning
simple statistical associations and data
ideally we'd like these models to use

[00:01]
the extra compute
to resolve ambiguity and to correct and
refine
their own answers the second side of
this coin
is efficiency stuff and this deals with
the question of how we can
decouple the amount of parameters that a
model has
from uh the amount of time that it takes
to run the model at inference with the
motivation
here being that if we can construct
models that are larger
but that don't incur a larger
computational cost for those extra
parameters than we would okay so how did
we
tackle this question
um the overwhelming vast majority of
this project was actually spent
on something i'll likely only spend a
single slide talking about
in the interest of time and that's the
shortest path task
the shortest path is a sequence to
sequence modeling task in which i give
the model a pair of
tokens representing pairs of u.s cities
and i expected to output

[00:02]
a sequence of target tokens that
represent the
shortest path between the destinations
the stuff i'll mostly be presenting on
only really took shape in the past three
or four weeks and it involved
investigating some of these test time
properties
on uh graph neural networks operating
over the game of sudoku
okay like i said most of my project was
spent on the shortest pathwork
in which we were trying to answer this
question if we control the
flop the total flop budget of um
our models is there ever a point where
the test time performance of models like
the one that you see on the left
which use this sort of top layer
occurrence
ever begins to approach or match the
performance of models that don't have
this recurrence but maybe are larger
have been trained for longer the way we
did this was by keeping the training
complete
budget in terms of flops fixed for all
the models and then training these
recurrent models
with a fixed number of time steps during

[00:03]
training with loss evaluated at every
single time step
and then during test time evaluating
them with more steps of recurrence
see if it ever reaches a point where the
extra compute
allows them to in some sense catch up to
the larger models that were trained
without this
recurrence long story short it largely
doesn't seem
to work we never really see this sort of
phase transition
recurrence alone doesn't seem to be
enough
to be clear if you run a linear probe on
the embedding space for these models
they actually seem to learn something
like the locations or something at least
isometric to the locations of the cities
fairly quickly which indicates that the
problem isn't actually learning where
the cities are
it seems to be that even with the extra
recurrence the extra compute
learning a general shortest path
algorithm
is difficult occurrence alone doesn't
seem to be enough
we need additional structure on top of
that
which is where the graph neural network

[00:04]
stuff comes in
so graph neural networks or networks
that operate on graph structured data
there are a few main parts the first
part is this input representation phase
where you pass in
your graph structured data x here
represents the nodes
in your graph which contain the features
that you care about
these could be the locations of u.s
cities or the values of cells on a
sudoku board
a represents the adjacencies which
encode some concept
of the edges of the graph in other words
what relationships
nodes have with each other the gnn
processes this graph by iteratively
performing a learned message passing
operation between the nodes where it
attempts to refine
its internal representation of those
nodes at the end
of this refinement phase we can then run
classification tasks on either the
individual nodes
or if we aggregate the nodes we can run
classification on the entire graph
okay a key feature of these gnns is this
graph refinement equation which i'll

[00:05]
come back to
at least twice in this presentation um
it looks wild in its general form but
all it really is is
just three parts um it says that the
hidden state
for a node i is updated by a function
that takes in
the node embedding for that node and all
pairs of that node's neighbors
passed through some function and then
aggregated using your favorite
aggregation function
cool okay so how do we do this for
sudoku
well every cell on the sudoku board
corresponds to a node
on the graph this node on the graph
the nodes on this graph refine their
representations by passing messages to
themselves or
or their neighbors using that graph
refinement equation we just saw
and now what's typically done is that
you run this graph refinement phase for
a fixed number of times let's say 10
time steps
and then at the very end you run your
linear projection and you make a
prediction
what we do a little differently here is
that we make a prediction at every point

[00:06]
along the graph refinement phase and we
evaluate the loss at every single point
as well
this allows the model to be more robust
to being evaluated during the graph for
fun
to being evaluated with more graph
refinement iterations at test time than
it was trained on
um at training
okay so how does this actually look like
in practice here's one solving sudoku
this is real data by the way what's cool
about this is that it appears to
prioritize spending the extra compute
resources
on attending to and refining tokens that
have assigned a
low probability high uncertainty to in
the previous time steps
the red things become more green and the
green things stay green
okay this is cool because it's a sign
that the test time computer dream is at
least in principle
possible if we look at this graph which
shows the gnn
operating over two data sets one is
normal and the other is hard
we see generalization in two different
senses
one as we increase the amount of

[00:07]
iterations or test time compute
we see that the accuracy of the network
improves in an almost
monotonically increasing way by the way
the accuracy here is measured on the
sequence level which means that
i only count it if it gets the entire
board correct
the other sense is that if we give the
network problems that are harder
than the ones it was trained on it still
performs well okay
so if the argument here is that more
test time compute more iterations is
good
what would happen if we could evaluate
this model at infinite depth
in other words could we do better in
order to answer this question we need to
steal the machinery of deep equilibrium
models
now i don't have a whole lot of time to
go into the details
of deep equilibrium models but i suggest
that you check out
the paper by xiao zubai or the europe's
workshop from this past year the gist is
that deep equilibrium models
are inspired by the observation that we
can often rewrite

[00:08]
a standard neural network as an implicit
function
that instead of specifying explicitly
how to compute
the layer's output as a function of its
input we instead specify the conditions
in which we would like the layer's
output to satisfy
after rewriting these layers as implicit
functions it turns out
that most of them converge to a fixed
point which allows us to
instead of keeping track of the
intermediaries that graph refinement
phase in our auto grad library we could
instead
use an arbitrary black box root finding
algorithm
and to evaluate this convergence point
this is equivalent to running an
infinite depth weight tied feed forward
network
but has the notable advantage that we
can analytically back
propagate through this equilibrium point
using something called the implicit
function theorem
cool um yeah how's this relevant to gnns
well if you take a look at that graph
refinement equation from earlier
it looks exactly like a fixed point
equation which means that we can apply

[00:09]
the machinery of deep equilibrium nuts
here if you try this out it actually
works really well with a big caveat that
i'll related to early stopping that i'll
get to in the next slide
these early training curves are
preliminary but kind of dramatic
the deep equilibrium sorry the deep
equilibrium
gnn trains a lot faster than the
traditional gnn
further because we're using the
machinery of d people agreements to save
us from having to keep
track of the intermediate steps of that
graph refinement phase
in our auto grad library the memory
usage of the dp equilibrium
is smaller than the regular one as well
okay so what's the caveat
well uh as far as i can tell every
single time i've been
uh i've run this i've run into this
weird collapse
that happens where it starts training
and it's doing really great
and then it dies and i haven't quite
been able to figure out why this happens
i suspect it has to do with the growth

[00:10]
of the spectral norm of the operators
inside the gnn
as it's being evaluated by the fixed
point iterator but it also
just could be a bug in my code um
stopping training early when this
degeneracy begins is proven to be fine
and i'm still investigating the problem
but i just wanted to point this out for
completeness
okay shifting gears a little bit can we
do better
still in another way gnns are fine as
we've seen they seem to do well
on these relational reasoning style
tasks but one potential oddity is that
we must be explicit about the network
the structure of the network of the
graph that is we must explicitly tell
the network which nodes are connected to
each other nodes
for sudoku for instance we must be
explicit about saying that things that
are in the same row
things that are in the same column
things that are in the same cell
are connected could we instead learn the
adjacencies from scratch from the raw
unstructured data here's the idea

[00:11]
okay transformers seem to be pretty good
at learning how
how relevant pairs of tokens are to each
other
on the other hand gnns are good at
operating over
structured data what if we could use the
tension head from a standard transformer
to extract an adjacency matrix which we
then feed into
the gnn here's how it works we first
feed
a small transformer our input with a
small modification that at the top
layer we use the probability scores to
categorically sample the top k
indices which are the most relevant to
that particular token
that extracts k neighborhoods for each
token which we can then feed into our
tnn
now sampling indices is a
non-differentiable operation
however we can compensate for this by
using the surrogate loss thing outlined
below
this is taken from a paper by john
shulman and
uh it just provides a general framework

[00:12]
for gradient estimation through
stochastic compute graphs
the formulism just gives us a way to
convert stochastic compute graphs into
deterministic compute graphs
and evaluate a surrogate loss using
standard back propagation that provides
an
unbiased estimator of the gradient
through the stochastic node
cool okay so if you try this out it
works kind of um the reality is that it
just
trains much slower than the standard gnn
and
you know vanilla policy gradients are
high variance they're kind of messy
but and the performance actually is
worse than the standard gnn but it does
show that in principle we could train a
gnn
from scratch that learns the adjacencies
from scratch as well which is
kind of cool okay
conclusion yeah so uh test time compute
mechanisms i think are largely
underexplored but hold much promise they
have the potential for improved
generalization mechanisms

[00:13]
potential for improved sample efficiency
i think
recurrence plus message passing seems to
be a really interesting combination
and if the methods of this presentation
seem
uh contrived that's because they are but
ultimately like i'm
while the specific methods are kind of
crude i'm bullish on the idea of test
time compute in general and i think that
the next few years we'll see
critical breakthroughs that make use of
ideas that have test time compute at
their core
that's it i'd like to thank my mentor
will gus and i'd also like to thank
uh the program organizers and my cohort
and uh all the people that um gave me
early feedback
on uh some of this stuff and thank you
and now i'll take questions
uh let's see let me stop sharing
okay so this first question here

[00:14]
is
how do i extend this gnn setting to
sequence modeling
like the language modeling loss in uh
gpt
yeah so um you could imagine that each
output token corresponds to either
uh yeah you could do this in a couple
ways like you could imagine like an auto
regressive type thing
where like you're at each point
evaluating the state of the entire graph
and outputting an output sequence and
then feeding that output sequence into
uh the sort of beginning of the model
and then running this again
doing this sort of auto aggressively is
one way um
and then yeah but i'm sure there are
other ways that i'm just not
familiar with but yeah so what type of
problems you expect test time to
compute to really shine in yeah this is
a great question i think
sorry my dog gets really excited here uh

[00:15]
i think ultimately
uh test time compute will shine in
problems that really have sort of these
relational reasoning style tasks where
we need to
relate our previous outputs to
things that we're currently processing
or problems where we need to condition
the amount of computes that we do on the
complexity of our inputs
okay uh does the stochastic compute
graph mean that gnns can be applied to
settings without inductive biases
that's the ultimate hope i think this is
just very crude early work that shows
that you could
potentially also just learn the
adjacencies without
hand uh baking the inductive bias though
i mean i think part of the appeal of
graph neural networks is that like
they're so easy to bake in inductive
biases that you just
feed in the graph as
it is and that is the inductive bias for
your data
so there's definitely a trade-off here
and it's not like super clear that doing

[00:16]
this is like
always the right thing to do okay last
question
what does it look like if you threshold
the learned adjacency
weights to produce a discrete graph
structure is
is this roughly right threshold the
learned adjacency weights
oh right so yeah that's that's a good
point
these are discrete that's the whole
point of the sampling thing
is that the adjacencies are the indices
for each token which correspond to the
other tokens that are
are um they're near it so this isn't
like a tension where we're doing like a
soft max over
over um over the other output tokens
like
we're using the transformers probability
scores
and then we're discretely sampling like
which we're using the transformers
attention
uh scores asks our weights
for our discrete sampling if that makes
sense

[00:17]
um but yeah cool
i think i'm over time so um
yeah i'll hand it back over to francis i
guess

</details>
