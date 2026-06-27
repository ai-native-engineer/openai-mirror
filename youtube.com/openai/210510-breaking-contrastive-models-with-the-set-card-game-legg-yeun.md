---
title: "Breaking Contrastive Models with the SET Card Game | Legg Yeung | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=AKg0tzunYP0
youtube_id: AKg0tzunYP0
published: 2021-05-10
duration: "15:45"
captions: en-orig
---

# Breaking Contrastive Models with the SET Card Game | Legg Yeung | OpenAI Scholars Demo Day 2021

[![Breaking Contrastive Models with the SET Card Game | Legg Yeung | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/AKg0tzunYP0/hqdefault.jpg)](https://www.youtube.com/watch?v=AKg0tzunYP0)

<details>
<summary>자막: Breaking Contrastive Models with the SET Card Game | Legg Yeung | OpenAI Scholars Demo Day 2021 (15:45)</summary>

[00:00]
um hi my name is lake um
i'll be talking about breaking contrast
models with the sets card game
this project is motivated by a
particular failure mode of clip
consider this text prompt which asks for
a red cube on top of a green cube
on top of a blue cube the image forms a
natural pairing with the text
if i shuffle the colors in both the
image and the text i get another pairing
if i continue this procedure to generate
all six pairings of texts and
images and feed them into clip i'd
expect
clip to predict a six by six logics
matrix with a strong diagonal
but the logits predicted are actually
quite even it seems that
when there are multiple entities
relations and attributes
clip struggles my intuition for why this
happens
has to do with the dot product retrieval
layer between query and key
representation vectors in standard
contrasted models

[00:01]
we can view this layer as performing
linear classification
in which a linear boundary q is encoded
to separate the key data points
under this perspective the vc dimension
limitation applies
for quotes we have six keys one query
may match with three of them as positive
ps
but there are actually two to the power
six number of ways to assign some keys
as positive
and others as negative as long as our
hypothesis class can throw all 2 to the
power 6 number of queries at the keys
this is the idea of shattering in
general
if our queries are limited by the vector
dimension d
the vc theory states that they cannot
match with all possible subsets of d
plus one keys in data sets like imagenet
there are only a thousand labels in the
contrasting model setup this corresponds
to a thousand static queries
for example match all the docs so
model performance is far from hitting

[00:02]
the limits imposed by the vector's vc
dimension
but on data sets like clever many
dynamic queries can be formed
such as identifying all the scenes with
one or more blue objects
here we need to subset the scenes in
many dynamic ways
so we may hit the limit imposed by the
vector's vc dimension
i also have a secondary intuition that's
related to the poor approximation of
full rank
query key matrices using vectors that
are shorter than the rank
feel free to ask me about it to validate
my intuitions
i set up two architectures one is a
contrastive model which i encode
queries and keys separately and score
the compatibility using the dot product
retrieval layer
the other is a non-contrastive model
which scores each query key pair as a
continuous sequence
the contrasted model uses an eight layer
transformer to encode the query symbols
and an embedding lookup to encode the

[00:03]
key symbols
while the non-contrasting model uses a
four layer transformer to encode the
concatenated query key symbols
the contrastive model has 17 million
parameters while the non-contrastive
model has only half of that
my experiment goal is to show that
contrasting models with limited vector
representation dimensions
are worse than non-contrasted models
that uses half the parameters
task wise i borrowed the well-known sex
card game
it suits my purpose because of some nice
extendable properties
each card has multiple attributes and
possible values for attributes
these dimensions are scalable any pairs
of cards can form a query that evaluates
to a key card
in a complete set of three cards on any
attribute the cards either have to
be the same or all different
this query key matrix has a regular
pattern but it is still full rank

[00:04]
to extend this game i introduced the
star
regular expressions such that queries
can evaluate to subsets of key cards
in addition i introduced a set union and
symmetric difference operators
to make the queries and return subsets
even more dynamic i'm going to show an
example game
and how the models would play it here's
a deck of 27 cards
each with 3 attributes and three
possible values per attribute
each query has eight pairs of cards and
set union operators between them
depending on the query the matching
subset of keys and its size
vary this particular query returns 13
matching positive keys
a different query may return a different
smaller or larger subset of keys
such as 3 or 21. a training example is a
tuple of query symbols
and a key symbol sampled from the
matching positive key
we can sample different queries and

[00:05]
their keys this way to make a batch
the contrasted model uses the info nce
training objective which normalizes the
dot product
over all the query key pairings in this
batch size by batch size query
key matrix the scores are penalized
across
both columns and rows the
non-contrasting model uses a
conventional cross-entropy objective
the scores are penalized across keys in
the support
at test time the models are given
queries such as this one
and they score the compatibility of this
query with each of the 27 keys
there are 13 ground truth keys for this
query so one crude metric is to measure
how much your top 13 predictions overlap
with the
13 round trip keys i call this metric
the top k prediction ground truth
overlap for now
a more sensitive metric is to compare
the kl diversions
between the normalized predicted scores

[00:06]
and a ground truth distribution
constructed from dividing one among all
the ground truth keys evenly
putting all of this together i have
seven contrasted models with vector
representation dimension from 512 down
to four
they all have 17 million parameters and
a non-contrastive model with half the
size
i have five different games that are
based on a 27 card deck
from the sets game in its original form
to the afford mentioned extensions and a
final game of shattering 27 numbers
they have increasing levels of
difficulties characterized by the
respective total number of unique key
subsets the queries
should separate we tried each game on
all the models
here's a results plot on the y-axis we
have kl
divergence loss on the x-axis we have
those five games ordered from left to
right with increasing levels of
difficulty
measured by the total number of key

[00:07]
subsets the craze should separate
in powers of two the first game is the
original set
it requires the queries to separate 2 to
the power 4.57 subsets of keys
all the models did very well the second
game
includes a star regular expression and
requires the queries to separate
2 to the power 6 number subsets of keys
so the contrastive model with vector
dimension 4 starts to do poorly
as we introduce a set union and
symmetric
difference operators the models need to
separate between
2 to the power 21 and 23 subsets of keys
so the contrastive models with vector
dimension 8 to 20
also do worse and worse finally
on shattering 27 numbers the model needs
to satisfy a vc dimension of at least 27
so all the models with vector dimensions
less than 27
fails to varying extents

[00:08]
notice that throughout these schemes the
contrasting model
models with vector dimension 5 12 27
and the non-contrasted model with half
the parameters performed
consistently well the top k overlap
metric
shows a similar agreeing trend here
higher is better so the plot looks like
the kl
loss plot flipped upside down to
understand why the models with shorter
vector representations are worse i
zoomed into one game for some analysis
this is a representative query from
erroneous predictions
it matches with 13 ground truth positive
keys
and 14 round trip negative keys
the perfect model normalizes the dot
products and distribute the probability
mass
evenly among the positive keys and
nothing among the negative keys
the contrasted model with vector
representation dimension
5 12 and 27 are not far from perfect
but if we drop the dimension to 20 or

[00:09]
below we start to see
mass moving to the negative keys until
the dimension 4
which performs about the same as a
completely even distribution
it seems that as we drop the vector
representation dimension
the model becomes lessly able to develop
a preference
among the keys using entropy of
predictions as a measure of this
phenomenon
what we saw from a previous example can
generalize to all the queries that
matches with
10 to positive ground through positive
key cards
the entropy of predictions increases as
vector dimension decreases
notice that queries in this game return
to
return up to 2 to the power 21 subsets
of keys
and starting with dimension 20 entropy
grows more dramatically
this trend is also reflected in the
aggregate of all queries in the test
sets
these entropies are increasingly or
monotonically as vector dimension

[00:10]
decreases
in addition to this 27 card version i
also trained an 81 card
version of this particular game the
setup is similar
the contrastive models range from vector
representation dimension
512 down to 16 or around
17 million parameters the
non-contrastive model is half the size
here are the plots the trends are
similar
kl loss decreases as the vector
dimension increases and top k overlap
metric increases with the vector
dimension
notice that the game has 81 cards so in
theory with a vector dimension of 81
or above we should be able to solve this
game perfectly
and we do see some agreeing trends here
here are a few things i learned from
training these models
more difficult games require more gentle
learning rate schedules

[00:11]
cosign schedules help to unstructured
models from local
minima in some cases efficiency of
conversions
depends on initialization schemes
using dot products instead of cosign
similarity
and temperature works better for this
data
overall i think these observations are
more specific to the nature of this
synthetic game
than contrastive models
besides what i just told you i also
worked on some adjacent topics
during the past six months they include
a variable binding
in which i did some literature reviews
on tensor products
and a study of dolly and eclipse failure
modes
and then i looked at a point mutual
information for classification
specifically comparing the info mce
versus the cross-entropy objective for
zero shot classification on toy problems
and i looked at a various uh versions of
game rules and operators
and observed that their ranks

[00:12]
the rank of their query key distribution
measures these changes
finally i want to uh thank you for
listening
and also uh thank my mentor gabe for
giving me a lot of valuable guidances
and
and feedback in these six months
um and and i'll be update i'll be
updating my blog
over the weekend um with the uh with the
final with the final blog post so feel
free to
check it out next week also feel free to
contact me for
uh further questions so now i look over
to the q a for for questions
um
so there is a question on uh on the
intuition
behind entropy going up
as the embedding dimension goes down
and so
let's see let me go

[00:13]
to the
so uh from the error analysis that i saw
i saw that um
as the vector dimension goes down the
the vector size the vectors themselves
become less able to
encode enough signals that allow them to
uh kind of separate the the different
keys
um but i would be curious to do more
investigation on that front but in
general the observation is that as the
vector dimension goes down
the models become less and less able to
develop a preference among the keys
and then so there's a question on the
intuition on rank
let me also go to the corresponding
slide
so the intuition is that if our query

[00:14]
key matrix it has
rank uh has a is full rank
so in this case if i have uh if i have
less keys than my queries this full rank
matrix would have the rank equal to
the support of the keys i'll let's say
and if my um if my
vector representation sizes are less
than 27
when i take dot products between my
queries and keys
it's mathematically equivalent to doing
a matrix multiplication
of the keys matrix that has size
support keys by by a number that's less
than support size of keys
with the query matrix that
has a dimension that on the on one
dimension that's less than
support of keys and other being the
support of queries
so these vectors are shorter than the

[00:15]
than the full rank
27 and so um so when we do a matrix
multiplication between these two
matrices
the the m prime matrix is not going to
be
full rank it would have at at most the
rank of
the whatever the the vector
representation
dimension is um and then there is also a
question of
if the non-contrastive uh oh
so i i see that my time is up so i'm
gonna uh
uh hand the time over to sam and uh look
at the
look at the the third q a question of
line and make a reply

</details>
