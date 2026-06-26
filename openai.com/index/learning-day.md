<!-- source: https://openai.com/index/learning-day/ -->

August 1, 2019

[Company](/news/company-announcements/)

# Learning Day

At OpenAI, each Thursday is Learning Day: a day where employees have the option to self-study technical skills that will make them better at their job but which aren’t being learned from daily work.

![Learning Day](https://images.ctfassets.net/kftzwdyauwt9/f3ffe702-1fd9-465a-da2a2c7e1ce6/4766e0572304b9a506d0955b36fe5a6a/learning-day.jpg?w=3840&q=90&fm=webp)

Illustration: Ben Barry

We’ve found that the biggest contributions at OpenAI come from cross-functional experts, so we either need to hire them or grow them here. Before Learning Day, we very rarely saw people grow cross-functionally—for example, employees coming from a software background rarely picked up machine learning (something equally rare in other organizations except academia). Since Learning Day, this kind of growth has become very common.

On a typical learning day, people do things like:

* Reimplement papers.
* Follow deep learning tutorials.
* Play with new tools in cluster management, compilation, virtual world generation, or coding paradigms.
* Learn how to do research on bite-sized problems.
* Read about new developments in seemingly unrelated areas of AI.

We think Learning Day might be useful for other organizations, so we’d like to share how it started and works at OpenAI.

## Backstory

We first tried out Learning Day on our Robotics team. Here’s how our Head of Robotics, Wojciech Zaremba (Woj), came up with the idea:

Loading...

## How it works

Learning Day happens each Thursday. Woj wrote the following guidelines for the Robotics team, but we’ve adapted these principles across each team that has adopted Learning Day:

Loading...

To keep people accountable, we ask everyone to post in Slack what they learned that day.

## What we learn on Learning Day

The following are examples of what people learn on a single Learning Day.

#### **Deep learning reading**

* “[Population Based Augmentation: Efficient Learning of Augmentation Policy Schedules⁠(opens in a new window)](https://arxiv.org/abs/1905.05393)”
* “[Learning Domain Randomization Distributions for Transfer of Locomotion Policies⁠(opens in a new window)](https://arxiv.org/abs/1906.00410)”
* “[Neural Graph Evolution: Towards Efficient Automatic Robot DesignLearning to Learn with Probabilistic Task Embeddings⁠(opens in a new window)](https://bair.berkeley.edu/blog/2019/06/10/pearl/)”
* “[Mid-Level Visual Representations Improve Generalization and Sample Efficiency for Learning Visuomotor Policies⁠(opens in a new window)](http://perceptual.actor/assets/main_paper.pdf)”
* “[Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables⁠(opens in a new window)](https://arxiv.org/abs/1903.08254)”
* “[Does computer vision matter for action?⁠(opens in a new window)](https://arxiv.org/pdf/1905.12887.pdf)”
* “[WAIC, but Why? Generative Ensembles for Robust Anomaly Detection⁠(opens in a new window)](https://arxiv.org/abs/1810.01392)”
* “[Weight Agnostic Neural Networks⁠(opens in a new window)](https://arxiv.org/abs/1906.04358)”
* “[Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations⁠(opens in a new window)](https://arxiv.org/abs/1811.12359)”
* [Deep unsupervised learning⁠(opens in a new window)](https://sites.google.com/view/berkeley-cs294-158-sp19/home)
* [Deep RL Bootcamp⁠(opens in a new window)](https://sites.google.com/view/deep-rl-bootcamp/lectures)

#### **Deep learning coding**

* [Reptile⁠](/index/reptile/) and [MAML⁠(opens in a new window)](https://arxiv.org/abs/1803.02999)
* Play with code in [JAX⁠(opens in a new window)](https://github.com/google/jax)
* Apply [Sparse Transformers⁠(opens in a new window)](https://github.com/openai/sparse_attention) to vision tasks
* Implement LSTM and transformer from scratch; train them on Penn treebank
* Train a neural net to reproduce the behavior of a physical motor

#### **Math and statistics**

* [Time Series Analysis⁠(opens in a new window)](https://www.youtube.com/watch?v=uBeM1FUk4Ps&t=1606s)

<!-- yt-inline:uBeM1FUk4Ps -->
[![8. Time Series Analysis I](https://img.youtube.com/vi/uBeM1FUk4Ps/hqdefault.jpg)](https://www.youtube.com/watch?v=uBeM1FUk4Ps)

<details>
<summary>자막: 8. Time Series Analysis I (1:16:19)</summary>

[00:00]
The following content is provided under
a Creative Common License. Your support
will help MIT Open Courseware continue
to offer high-quality educational
resources for free. To make a donation
or view additional materials from
hundreds of MIT courses, visit MIT Open
Courseware at ocw.mmit.edu.
Okay. Well, last time I was lecturing uh
we were talk we're uh talking about
regression analysis and we finished up
talking about estimation methods for
fitting regression models. Um I want to
recap the method of maximum likelihood
because this is really the primary
estimation method in statistical
modeling that you start with. And uh so
let me just review uh where we were. We
have a normal linear regression model. A
dependent variable Y is explained by a
linear combination of independent
variables uh given by a regression
parameter beta. And we assume that there

[00:01]
are errors about all the cases which are
independent and identically distributed
normal random variables. So uh because
of that relationship the dependent
variable vector Y which is an N vector
for N cases is a multivariate normal
random variable.
Now um the likelihood function is equal
to the density function for the data and
there's you know some ambiguity really
about how one manipulates the likelihood
function. The likelihood function
becomes defined once we've observed a
sample of data. So in this uh expression
for the likelihood function as a
function of beta and sigma squared we're
considering evaluating the probability
density function for the data
conditional on the unknown
parameters. So if this were simply a
univariant normal distribution with some

[00:02]
unknown mean and variance then what we
would have is just a sort of bell curve
uh for mu centered around a single
observation y if you look at the
likelihood function and how how it
varies with with the underlying mean and
of the uh normal distribution. Um so
this likelihood function uh is uh well
the challenge really in maximum
likelihood estimation is really
uh uh calculating and computing the
likelihood function um and with normal
linear regression models is very easy.
Now uh the maximum likelihood estimates
are those values that maximize this
function and the question is why are
those good estimates of the underlying
parameters? Um well what those estimates
do is they are the parameter
values for which the observed data is

[00:03]
most likely.
So we're able to scale the unknown
parameters by how likely those
parameters could have generated these
data values. So let's look
at the likelihood function for this
normal linear regression model. Okay,
these first two lines
here are highlighting the first line is
highlighting that our response variable
values are
independent. They're conditionally
independent given the unknown
parameters. And so the density of the
full vector of y's is simply the product
of the density functions for those uh
components. And because this is a normal
linear regression model, each of the yis
is normally distributed. So what's in
there is simply the density function of
a normal random variable with mean given

[00:04]
by the beta sum of independent variables
for each I uh case I uh given by the
regression parameters.
And that
expression basically can be expressed in
matrix form this
way. And what we have
is the likelihood
function is ends up being a function of
our Q of beta which was our le squares
criterion.
So le squares
estimation is equivalent to maximum
likelihood estimation for the regression
parameters if we have a normal linear
regression model. Um, and there's this
extra term minus n. Well, actually, if
we're going to maximize the likelihood
function, we can also maximize the log
of the likelihood function because
that's just a monotone function of the

[00:05]
likelihood. And it's easier to maximize
the log of the likelihood function which
is expressed here. And so, uh, we're
able to maximize over beta by minimizing
q of beta. And then we can maximize over
sigma squared given our estimate for
beta. And that's achieved by taking the
derivative of the log likelihood with
respect to sigma
squar. So we basically have this first
order condition that finds the maximum
because things are appropriately uh
convex. And taking that
derivative we uh and solving for zero we
basically get this expression. So this
is just taking the derivative of the log
likelihood with respect to sigma
squared. And you'll notice here I'm
taking the derivative with respect to
sigma squar as a parameter not sigma.

[00:06]
And that gives us that the maximum
likelihood estimate of the error
variance is Q of beta hat over N. So
this is the sum of the squared residuals
divided by N. Now I you know emphasize
here that that's biased. Who can tell
me why that's biased or why it ought to
be biased?
Okay. Well, it should be n minus
one if we're actually estimating one
parameter. So, you know, if we were
estimating uh and if the independent
variables were say a a constant one, so
we're just estimating a a sample from a
normal with mean beta one corresponding
to the units vector of the x. Then uh we

[00:07]
would have a onederee correction for one
uh sort of one degree of freedom
correction to the residuals to get an
unbiased estimator. But what if we have
p parameters? Well, let me ask you this.
What if we had n parameters in our
regression model? What would happen if
we had a uh you know a full rank n
independent variable matrix and n
independent observations?
Yes, you'd have an exact fit to the
data. So there would be this estimate
would be zero. Okay. And so u clearly if
the data do arise from a normal linear
regression model zero is not unbiased
right and you need to have some
correction. It turns out you need to uh
divide by n minus the rank of the x

[00:08]
matrix the degrees of freedom in the
model to get a biased estimate. So so
this is uh an important issue. Well, it
highlights how the more parameters you
add in the model, the more precise your
fitted values are. In a sense, there's
dangers of curve fitting, which you
know, you want to avoid. Uh, but the uh
maximum likelihood uh estimates in fact
are biased and you just have to be be
aware of that and when you're using
different software fitting different
models, you need to know whether there
are various corrections being made for
unbiasedness or not. Um, but
um, okay. So, so this uh solves the
estimation problem for normal linear
regression models. And when we have
normal linear regression models, the
theorem we went through last time is
very important. Let me just go back and
highlight that for you.

[00:09]
Um okay, this theorem right here. Okay,
this is this is really the important
uh a very important theorem indicating
what is the distribution of the le
squares. Now the maximum likelihood
estimates of our regression model. Okay,
they are normally distributed and uh the
residuals sums of squares have a kai
squared distribution with degrees of
freedom given by n minus p. And we can
look at how uh how much sort of signal
to noise there is in estimating our
regression parameters by calculating a
tstistic which is take away from an
estimate its expected value its mean and
divide through by an estimate of the
variability in standard deviation units
and that will have a t distribution. So
that that's a critical uh uh way to
assess the relevance of different
explanatory variables in our model and

[00:10]
and this uh approach will apply in max
with maximum likelihood estimation in
all kinds of models apart from normal
linear regression models. It turns out
maximum likelihood estimates generally
are asmmptoically normally distributed
and so these properties here will apply
uh for those models as well. So let's uh
finish up these notes on estimation by
talking about generalized M estimation.
Um so what we want to consider is
estimating unknown
parameters
by minimizing some function Q of beta
which is a sum of evaluations of another
function H evaluated for each of the
individual cases.
and choosing h to take on different
uh functional forms will define

[00:11]
different kinds of estimators. Um and
we've seen how when h is simply uh the
square of the case minus its regression
prediction. Um that leads to least
squares and in fact maximum likelihood
estimation. Um, as we saw
before, rather than taking the square of
the sort of residual, the fitted
residual, we could take simply
the the modulus of that and uh so that
would be the mean absolute deviation. So
rather than summing the squared
deviations from the mean, we could sum
the absolute deviations from the mean.
Now from a mathematical standpoint, if
we want to solve for those
estimates, how would you go about doing
that? Right? What methodology would you
use
to maximize this function?

[00:12]
Well, we'd try and apply basically the
same principles of if this is a convex
function, then uh we just want to take
derivatives of that and solve for that
being equal to zero. So what happens
when you take the derivative of the
modulus of y - x i beta with respect to
beta?
What did you say?
Yeah, I I I don't It's It's not Yeah,
it's not the first second dive is not
continuous. Okay. Well, this is a not a
smooth function, but it's if we let me
just plot xi beta here. Um and

[00:13]
uh y minus that. Um basically this is
going to
be a function that has slope one when
it's positive and slope minus one when
it's negative. And so that will be true
um component-wise or for the y. So what
we end up wanting to do is find the
value of the regression estimate that
minimizes
uh the sum
of predictions that are below the
estimate plus the sum of the predictions
that are above the estimate given by the
regression line and and that solves the
problem. Now um with the maximum
likelihood
estimation one can plug in minus log the
density of yi given beta x and sigma i^
2 and that function is simply sums to

[00:14]
the log of the joint density for all the
data. So that works as well. um with
robust M estimators we can consider
another function kai which can be
defined to have good properties with
estimates and there's a whole theory of
robust estimation that's very rich which
talks about how best to uh specify this
kai function now
um one of the problems with le squares
estimation is that the squares of very
large values are very very large in
magnitude. So there's perhaps an undue
influence of very large values uh very
large residuals in under le squares
estimation and maxim market estimation.
So robust estimators allow you to
control that uh by uh defining the
function differently.
Finally there are quantile estimators

[00:15]
which extend
uh the sort of mean absolute deviation
criterion. And so if we consider the H
function to be basically a multiple of
the
deviation if the residual
is positive and a different multiple
sort of a complimentary multiple if the
deviation the residual is less than zero
then by varying tow you end up getting
quantile estimators where what you're
doing is minimizing an estimate
of the tal
quantile. So the
uh so so this general class of m
estimators is uh encompasses most most
estimators that we will uh encounter in
in fitting
models. All right. So that finishes the

[00:16]
technical or the mathematical discussion
of regression analysis. Let me
uh
highlight for you.
Um let's
see. Let's see. There's there's a case
study that was dragged to the desktop
here and I wanted to find that. Okay,
let me find
that. All
right. Okay. Um there's a case study
that's been
uh added to the course website and this
first one is on uh linear regression
models for asset pricing and I want you

[00:17]
to read through that just to see how uh
it applies fitting various simple linear
regression models
and let's see here's your full
screen okay with
This okay this this case study begins by
introducing the capital asset pricing
model which basically suggests that if
you look at the returns on any stocks in
an efficient market then those should uh
depend on the return of the overall
market but scaled by how risky the stock
is. And so if one looks at how risk you
know basically what the return is on the
stock on the right scale u you should
have a simple linear regression model.
So here we just look at uh time series
for a GE stock in the S&P 500 and the
case study goes through how you can
actually collect this data on the web

[00:18]
using R. And so uh you know the uh case
notes you know provide those details.
Um there's also uh the three-month
treasury rate which is uh collected. And
so if you're thinking about return on
the stock versus return on the index,
well what's really of interest is the
excess return over a risk-free rate. And
in the efficient markets models uh
basically the excess return of a stock
is related to the excess is related to
the uh excess return of the market as
given by a linear regression model. So
we can fit this model and uh here's a
plot of the excess returns on a daily
basis for GE stock versus the market. So
that looks like a nice sort of point
cloud for which a linear model might fit
well and it does.
Um the uh there are reg well there are
regression diagnostics which I'll get to

[00:19]
in a well there are regression
diagnostics which are detailed in the
problem set where we're looking at you
know how influential are individual
observations what's their impact on
regression parameters.
Um this uh display here basically
highlights with a very simple linear
regression model what are the
influential obs data points and so I've
highlighted in red those values which
are influential. Now if you look at the
definition of leverage in a linear model
it's very simple uh simple linear model
is just those observations that are very
far from the mean have large leverage.
And so you can confirm that uh with your
answers to to the problem set. Um okay
this X indicates a significant orly
influential point in terms of the
regression parameters uh given by Cook's
distance and that uh definition is is
also given in the case notes

[00:20]
um by computing the individual leverages
with a function that's given here and by
uh selecting out those that exceed a
given magnitude.
Okay. Now with uh this very very simple
model of stocks depending on one unknown
factor uh risk factor given the market
in in modeling equity returns the uh
there are many different factors that
can can have an impact on on returns. So
um what I've done in the case study is
to look at adding another factor which
is
um just the oil uh let's see the return
on crude oil and
so let's see I need to go down

[00:21]
here. So, let
me let me highlight something for you
here. Okay. With with GE stock, what
would you expect the impact of a return
say a high return on crude oil to be on
on the return of GE stock? Would you
expect it to be positively related or
negatively related?
Okay.
Um, well, GE is a stock that's, you
know, just a broad stock, you know,
invested in many different industries
and really reflects sort of the overall
market to some extent. But many years
ago, probably 10, 15 years ago, it was
GE represented maybe sort of 3% of the
GMP of the US market. So it was really
highly related to how well the market
does. Now crude
oil is a commodity and oil is used to

[00:22]
drive cars to you know fuel uh energy
production. So if you have an increase
in oil prices then the cost of
essentially doing business goes up. So
uh is so is associated with like an
inflation factor. Prices are rising. So
um if you can see here the uh regression
estimate if we add in the factor of the
uh return on crude oil it's
negative.03 and it has a t value of
minus3.561. So in fact there you know
the market in a sense over this period
for this analysis you know was not
efficient in explaining the return on
GE. um crude oil is another independent
factor that helps explain returns. So
you know that's useful to know and if
you are clever about defining and
identifying uh and evaluating different

[00:23]
factors you can build uh factor uh asset
pricing models that are very very useful
uh for investing and trading. Now as as
a comparison to this, this case study
uh also uh applied the
same analysis to Exxon Mobile. Now Exon
Mobile is an oil company. So um let me
highlight this
here. We basically are fitting this
model now that's
highlighted and
Here if we consider this two factor
model the regression parameter
corresponding to the crude oil factor is
plus.13 with a t value of 16. So crude
oil definitely has an impact on the

[00:24]
value of the return of Exxon Mobile. It
basically goes up and down with oil
prices.
Um
now let's see let's see this this case
study closes with a uh scatter plot of
the independent variables and
highlighting where the influential
values
are. And so just in the same way that
with a simple linear regression it was
those that were far away from the mean
of the
data were
influential in a multivariate setting
here it's bariate the influential
observations are those that are very far
away from the centroidid and if you look
at uh one of the problems in the problem
set it actually goes through and you can
see uh where this these leverage values
are and how it indicates sort of
influences associated with the
mahalenobus distance of cases. is from
the centrid of the independent
variables. So if you're a sort of a
visual type mathematician as opposed to

[00:25]
an algebraic type mathematician, you
know, I think these kinds of graphs are
very helpful in understanding what is
really going on and uh the uh degree of
influence is associated with the fact
that we're basically taking leaf squares
estimates and uh so we have the
quadratic form associated with the
overall process. All right.
There's there's another case study that
uh I'll be happy to discuss
uh after class or during office hours. I
don't think we have time today during
the lecture, but it concerns exchange
rate regimes. And the second case study
uh looks at um the Chinese yuan, which
was basically pegged to the dollar uh
for many years. And then uh I guess
through political influence from other

[00:26]
countries they uh started to let the uh
yuan vary from the dollar but have
perhaps pegged it to some basket of
security of of currencies. And so how
would you determine what that basket of
currencies is? Well, there are
regression methods that have been
developed by economists that help you do
that. And that case study goes through
the analysis of that. So check that out
to see how you can get immediate access
to currency data and be fitting these
regression models and looking at the
different results and trying to evaluate
those.
Okay. So let's turn
now to the main
topic. Let's see
here which is time series
analysis. Okay, today I in the rest of

[00:27]
the lecture I want to talk about
univariate time series analysis. Um and
so we're thinking of u basically a
random variable that's observed over
time and it's a discrete time process
and we'll uh introduce you to the wool
representation theorem and definitions
of st stationerity and its relationship
there. then look at the classic models
of uh auto reggressive moving average
models
um and then extending those to
non-stationerity with integrated uh auto
reggressive moving average models and
then finally talk about estimating
stationary models and how we test for
stationerity. So
let's begin with you know from basically
first principles uh we have a
stochcastic process
uh a discrete time stochcastic process x

[00:28]
which is is consists of random variables
indexed by time and we're thinking now
discrete
time the stochcastic behavior of this
sequence is determined by specifying the
density or probability mass functions
for all finite collections of time
indexes. And uh so if we could specify
all finite dimensional distributions of
this process, we would
specify this probability model for the
stochcastic
process. Um now this stochastic process
is strictly stationary.
If the density function for any
collection of
times t1 through
tm is equal to the density function with
for a tow translation of that. So the
density function for any finite

[00:29]
dimensional
distribution is stationary is constant
under arbitrary translations.
So, uh, you know, that's, uh, a very
strong property, but, um, it's a
reasonable property to ask for if you're
doing statistical modeling. And what do
you want to do when you're estimating
models? You want to estimate things that
are constant. Constants are nice things
to estimate. And, uh, parameters of
models are constant. So, we really want
uh, the underlying structure of the
distributions to be uh, the same.
All
right. The uh okay that was strict
stationerity which requires knowledge of
the entire distribution of the
stochastic process. Um we're now going
to introduce a weaker definition which
is coariant stationerity.
And a coarent stationary process has a

[00:30]
constant mean mu, a constant variance
sigma squar and a
co-variance at um over increments towo
given by a function gamma of tao that is
also constant and it's not gamma is
isn't a constant function but the
basically for all t uh coariance of xt
xt plus toao is to this gamma of tao
function. Um and uh we also have can
introduce the autocorrelation function
of the stochastic process row of toao.
And so
um the correlation of two random
variables is the covariance of those
random variables divided by the square
root of the product of the variances. Um
and Chungboom I think introduced that a
bit in one of his lectures where we were

[00:31]
talking about uh the correlation
function. Um but um essentially the
correlation function
is if you standardize the data or the
random variables to have mean zero. So
subtract off the means and then divide
through by their standard deviations. So
those translated variables have mean
zero and variance one. then the
correlation coefficient is the coariance
between those standardized random
variables.
Um so this is going to come up again and
again in time series analysis. Now the w
representation theorem is a very very
powerful theorem about coariant
stationary processes.
Um it basically states that if we have a
zero mean coariant stationary time
series then it can be decomposed into

[00:32]
two components that have very nice
structure. Okay. Uh basically XT can be
decomposed into VT plus ST. VT is going
to be a linearly
deterministic
process, meaning that past values of
VT perfectly predict what VT is going to
be. So this could be like a linear trend
or some fixed function of past values.
It's basically a deterministic process.
So there's nothing random in VT. It's
it's something that's it's uh it's fixed
uh without randomness. And
ST
is a sum of coefficients pi times ADA T
minus
I where the ADA T minus I or the ADA T's
are linearly unpredictable white noise.
So what we have is ST is a weighted

[00:33]
average of white noise with coefficients
given by the
SI and the coefficients SI are such that
SI zero is
one and the sum of the squared SI is
finite and the white noise A to T. Okay,
what's white noise? It has expectation
zero. It has
variance given by sigma squar that's
constant and it has co-variance across
different white noise elements that's
zero for all t and s. So a to t are
uncorrelated with themselves and of
course they are uncorrelated with the
deterministic process.
So you know this is really a very very
powerful uh concept. You know if if you
are modeling a process and it has

[00:34]
coariant stationerity then there exists
a representation like this of the
function. So it's
uh a very compelling uh structure um
which uh we'll see how how it applies in
different
circumstances. Now uh before getting
into the definition of autogressive
moving average models um I just want to
uh give you an
intuitive understanding of what's going
on with the world decomposition. Um, and
this I think will help motivate why the
wall decomposition should exist from a
mathematical
standpoint. Um, so
consider just some univariate stochastic
process sometime series XT that we want
to model and we believe that it's
coariant
stationary and so we want to specify

[00:35]
essentially the W decomposition of that.
Well, what we could do is initialize a
parameter P, the number of past
observations in the linearly
deterministic
term
and
then estimate the linear projection of
XT on the last P lag values. And
so what I want to do is consider
estimating uh that relationship using a
sample of size n with some ending point
t less than or equal to
t. And
so we can consider
um y values like a response variable
being given by the successive values of
our
uh time
series. And so our response variables yj

[00:36]
can be considered to be xt knus n + j.
um and define a Y
vector and a Z
matrix as
follows. So we have values of
our stochastic process in Y and then our
Zmatrix which is essentially a matrix of
independent variables is just the lagged
values of the sta of this process. So
let's apply ordinary le squares to
specify the projection. Okay, this
projection matrix is should be familiar
now and that basically gives us a p a
prediction of yhat depending on p lags
and we can compute the projection
residual from that
fit. Well, we can conduct time series

[00:37]
methods to analyze these residuals which
we'll be introducing here uh in a few
minutes.
um to specify a moving average model. We
can then have estimates of the
underlying coefficients SI and estimates
of the these residuals A to T and then
we can evaluate whether this is a good
model or not. Okay, what does it mean to
be an appropriate model? Well, the
residual should be orthogonal to longer
lags than t minus s or longer lags than
p. So we basically shouldn't have any
dependence of our residuals
on lags of the uh stochastic process
that weren't included in the model.
Those should be orthogonal.
um and the A to T hats should be
consistent with white

[00:38]
noise. So those those issues can be
evaluated and if there's evidence
otherwise then we can change the
specification of the model. We can add
additional lags. We can add additional
deterministic variables if we you know
deter can identify uh what those might
be and proceed with this process. But
essentially that is uh how the world
decomposition would be could be
implemented. And theoretically as our
sample gets large, if we're observing
this time
series for a long time, then the limit
uh well certainly the limit of the
projections as P the number of lags we
include gets large should be essentially
the projection of our data on its
history. And that in fact is the uh
projection corresponding to defining the

[00:39]
coefficients of SI. And so in the limit
those will uh that projection will
converge and it will converge in the
sense that the coefficients on the of
the projection definition correspond to
the
si and uh now um if uh p goes to
infinity is
required now p means that there's
basically a long-term dependence in the
process. I mean it does depend on
basically it doesn't stop at a given
lag. It just the dependence uh uh it
persists over time then we may require
that p goes to
infinity. Now what happens when p goes
to infinity? Well and if you let p go to
infinity too quickly you run out of
degrees of freedom to estimate your
models. And so uh from an implementation
standpoint you need to let p over n go
to zero so that you have

[00:40]
essentially more data per observ than
obser more data than parameters that
you're estimating and uh so that that
becomes required and um in time series
modeling what we look for are models
where finite numbers of val finite
values of P are
required. Uh so we're only estimating a
finite number of parameters. Or if we
have a moving average model which has
coefficients that are infinite number,
perhaps those can be defined by a small
number of
parameters. So uh we'll be looking for
for that kind of feature in different
models. All right, let's turn to talking
about the lag operator. uh the lag
operator is you know a fundamental tool
in time series models. Um we uh consider

[00:41]
the operator L that shifts the time
series back by one time
increment. And applying this operator
recursively we get if it's operating
zero times there's no lag. One time
there's one lag. Two times two lags.
Doing that iteratively. And in thinking
of these, you know, what we're dealing
with is like a a transformation on
infinite dimensional space where it's
like the identity matrix sort of shifted
by one element or not the identity but
you know an element. Uh well yeah it's
like the identity matrix shifted by one
column or two columns. Um so anyway
inverses of these operators are well
defined in terms of what we get from
them.
So uh if we we can represent the W
representation in terms of uh these lag
operators by saying that our stochastic

[00:42]
process
XT is equal to VT
plus this S of L function. basically a
uh functional of the lag operator which
is a potentially infinite order polomial
of the
lags. So so this notation is something
that you need to get very familiar with
if you are going to be comfortable with
the different models that are introduced
with ARMA uh and ARMA
models. Any questions about that?
Okay. All right. Okay. Um, now relating
to this, let me just introduce now
because this will come up uh somewhat
later, but there's the impulse response
function of the coariant stationary
process. Okay, if we have a stochcastic
process
XT which is given by this W
representation, then you can ask

[00:43]
yourself what happens when
there's what what happens to the
innovation at time t which is a to t how
does that affect the
process over time and so okay if you
know pretend that you are you know
chairman of the Federal Reserve Bank and
uh you're interested in uh
GMPP or you know basically economic
growth and uh you're considering
changing interest rates to help the
economy. Well, you'd like to know what
an impact is of your change in this
factors how that's going to affect the
uh variable of interest perhaps GMP. Now
in this case we're thinking of just a
simple coarian stationary stochcastic
process. There's no uh it's it's
basically a process that is a random a
weighted sum a moving average of

[00:44]
innovations a to t. But the question is
basically any coariant stationary
process can be represented in this form
and the impulse response uh function
relates to what is the impact of a to t
what's it impact over time basically it
it affects the process at time t that
because of the moving average process
affects it at t plus one affects at t
plus2 and so this impulse response is uh
basically Basically the derivative of
the value of the process with
the J previous innovation is given by J.
So the different innovations have an
impact on the current value given by
this impulse response function. So
looking backward that definition is
pretty well defined. But you can also
think about how does an impact of the
innovation affect the process going
forward. And the long run cumulative

[00:45]
response is essentially what is the
impact of that innovation in the process
ultimately and eventually it's it's it's
it's not going to change the value of
the process but you know what is the
value to which the the process is moving
because of that one innovation. And so
the long run cumulative response is
given by basically the sum of these
individual ones and it's given by the
sum of the sis. Um so that's the
polomial of s with lag operator where we
replace the lag operator by
one. Okay. We'll we'll we'll see this
again when we uh talk about uh vector
auto reggressive processes. um with
multivariate time
series. All
right. Now the walled representation
which is a infinite order moving average

[00:46]
possibly infinite order u can have an
auto
reggressive
representation.
Um suppose
that there is
uh
another polomial pi star of the lags
which is which we're going to call pi
inverse of l which
satisfies the fact that if you multiply
that with p of l you get the identity
like zero then this s inverse if that
exists
um is basically the inversion of this
uh p of l oper or the yeah is the
inverse of the p of l. So if we start
with P of L if that's invertible then
there exists a SI inverse of L with
coefficients P SI
star and one
can basically take our original

[00:47]
expression for the stochcastic process
which is as this moving average of the
ADAS and express it as this
uh essentially moving averages of the
X's and so we've essentially inverted
the process
um and show that the stochastic
process has can be expressed
as an infinite order
autogressive representation. And so this
infinite order autogressive
representation corresponds to that
intuitive understanding of how the world
representation exists. And it actually
uh works with the uh or the regression
coefficients and that projection several
slides back corresponds to this inverse
operator. All right. So let's turn to

[00:48]
some
uh specific time series models that are
that are widely used. Um the class of
auto reggressive moving average
processes has this mathematical uh
definition.
We define the
XT to be equal to a linear combination
of lags of X going back P
lags with with coefficients 51 through
5P and then there are
residuals which um
are expressed in terms of a cuth order
moving average. So um in this framework
the ad t's are white noise and white
noise to reiterate is mean zero constant
variance zero co-variance between
those in
this

[00:49]
representation I've simplified things a
little bit by subtracting off the mean
from all of the
x's and uh that just makes the formulas
a little bit more simpler. Now with lag
operators we can write this ARMA model
as f of l a pith order polomial of lag l
given with
coefficients 1 f1 up to
fp and theta of l uh given by uh one
theta 1 theta 2 up to theta
q and the wall
decomposition as this
uh well okay the wall decomposition okay
this is basically a representation of
the ARMA time series model all right
basically we're taking a set of lags of

[00:50]
the independent of of the values of the
stochcastic process up to order P and
that's equal to a weighted average of
the ADA T's
If we multiply by the inverse of f of l
if that
exists then we get this representation
here which is simply the w
decomposition. So the arma models
uh basically have a w decomposition.
um if this f of l is
invertible
and we'll explore these by looking at
simpler cases of the arma models by just
focusing on auto reggressive models
first and then moving average processes
second so that you'll get a better feel
for how how these things are manipulated
and interpreted. So, so let's move on to

[00:51]
the pee order auto reggressive process.
So, we're going to consider ARMA models
that are just which just have auto
reggressive terms in them.
And
so, so we have f of l xt minus mu is
equal to a t which is white noise. So, a
linear combination of the series is
white noise.
Um and XT follows then a linear
regression model on explanatory
variables which are lags of the uh
process X. And this can be expressed as
XT equal to C plus the sum from 1 to P
of FJ X t minus J which is a linear
regression model with regression
parameters FJ and C the constant
term is equal to mu * V of 1. Now if you

[00:52]
uh basically take
expectations of the uh of the process um
you basically have coefficients of mu
coming in from all the terms and uh f of
one times mu is the uh regression
coefficient
there. All right. So with this auto
reggressive model we now want to go over
what are the stationerity conditions. Um
certainly
uh this auto reggressive model is
uh one where well a simple random walk
is follows an auto reggressive model but
it's not
stationary. We'll highlight that in a
minute as well. But if you think about
it that's true. And so uh stationerity
is is something to be uh understood and
evaluated.
the

[00:53]
uh okay this this uh polomial function
fee where if we replace the lag operator
L by Z a complex variable
um the uh equation f of z equal to
zero is the characteristic equation
associated with this auto reggressive
And
um it turns out that we'll be interested
in the roots of this characteristic
equation. Now if we consider writing f
of l as a function of the roots of the
equation, we get this expression where
you'll notice if you multiply all those
terms out, the ones all multiply out
together and you get one.
And with the lag operator L to the p
power that would be the product of 1

[00:54]
over lambda 1 * 1 over lambda 2 or
actually negative 1 over lambda 1 times
negative 1 over lambda 2 and so forth
out to negative 1 over lambda p. But um
you know basically if there are p roots
to this equation this is this is how it
would be written
out. And uh the covariance that the the
matri or the process x t is coariant
stationary if and only if all the roots
of this characteristic equation lie
outside the unit
circle. So um what does that mean? That
means that the norm modulus of the
complex Z is uh greater than one. So
they're outside the unit circle where
it's less than or equal to one.
and the roots if they um are outside the
unit circle
um then the modulus of the lambda j's is

[00:55]
greater than
one and if we then
consider taking a complex number lambda
basically the root and have an
expression for 1 - 1 / lambda l
inverse we can get this
series expression for that inverse and
that
series will exist and sort of be bounded
if the
lambda are greater than one in
magnitude. So we can
actually compute an inverse of f of l by
taking the inverse of each of the
component products in that polomial. So
u you know the and in introductory time
series courses they talk about
stationerity and unit roots but they

[00:56]
don't really get into it because people
don't know complex math don't know about
roots. uh so anyway but this is just you
know very simply how that uh framework
is applied. So so we have a polomial
uh equation for the characteristic
equation whose roots we're looking for
and those roots have to be outside the
unit circle for stationerity of the
process. Well, okay. It's it's basically
the conditions for invertability of the
process of the auto reggressive process
and that
invertability renders the process an
infinite order moving average process.
So let's go through these
results for the auto reggressive process
of order one where things you know
always start with the simplest cases to
understand things. Okay the uh
characteristic equation for this model

[00:57]
is just 1 minus vz the root is 1 over
v. So lambda is greater than one.
uh if the modulus of lambda is greater
than one meaning the root is outside the
unit circle then f is less than one. So
for coariant stationerity of this auto
reggressive process we need the
magnitude of fee to be less than one in
magnitude. Um okay the expected value of
x is mu. The variance of X is uh sigma^
2 X. This has this form sigma square
over 1 minus V. That
expression is is basically obtained by
looking at the infinite order moving
average
representation. Um but notice that
if
positive then the variance of X is

[00:58]
actually
less is actually greater than the
variance of the
innovations and if f is uh less than
zero then it's going to be smaller. So
the innovation variance basically um is
is sort of scaled up a bit in in the
auto reggressive process. The coariance
matrix is f times sigma squ x. You'll be
going through this in the uh problem set
and the uh covariance of of x is f to
the j power sigma^ 2
x and these expressions can all be
easily evaluated by simply writing out
the definition of these coariances in
terms of the original model and looking
at what terms are independent cancel out
and that proceeds.
All
right. So

[00:59]
let's let's just go through these cases.
We'll just show it all here. All right.
So we have
um if fe is between zero and one then
the process experiences exponential mean
reversion to mu. So an auto reggressive
process with fee between zero and one
corresponds to a mean reverting process.
Um this process is actually one that has
been used theoretically for interest
rate models and a lot of theoretical
work in finance. The vasich model is
actually an an example of the orstein
ulbeck process which is basically a mean
reverting brownian
motion. Um and uh any variables that
exhibit or could be thought of as
exhibiting mean reversion um can be
uh this model can be applied to those

[01:00]
processes such as uh interest rate
spreads or real exchange rates variables
where one can expect that things never
get too large or too small they come
back to some meat. Now the challenge is
that usually may be true over short
periods of time but over very long
periods of time the point to which
you're reverting to changes. So these
models tend to not have broad
application over long time ranges. We
need to adapt them. Anyway with the AR
process we can also have negative values
of fee which results in exponential mean
reversion. uh that's oscillating in time
because the reg the auto reggressive
coefficient uh basically is a negative
value and okay for fe equal to one well
the world de composition doesn't exist
and the process is the simple random
walk so uh basically if f is equal to

[01:01]
one that means that basically just
changes in value of the process are
independent and identically distributed
white noise and that's the random walk
process and that process is was covered
in earlier lectures you know is
non-stationary. If f is greater than one
then you have an explosive process
because uh basically the the values are
scaling up every every time increment.
So um so those are features of the AR1
model.
um for a general uh auto reggressive
process of order P
um there's a method well we can look at
the second order moments of that process
which have a very nice structure and
then use those to solve for estimates of
the ARMA parameters or auto reggressive
parameters and uh those happen to be

[01:02]
specified by what are called the U
walker
equations. So u Walker equations is a
standard topic in time series
analysis. What is it? What does it
correspond to? Well, we take our
original auto reggressive process of
order P and we write out the formulas
for the
co-variance at lag j between two
observations. So what's the coariance
between xt and xt minus j?
And that
expression is given by this equation.
And so this equation for gamma of J is
determined simply by evaluating the
expectations where we're taking the
expectation of XT in the auto
reggressive process times the fixed XT
minus J minus mu. So just evaluating
each of those terms, you can validate
that this is the equation.

[01:03]
If we look at the equations
corresponding to J equals 1. So lag one
up through lag P. This is what those
equations look
like. Basically the left hand side is
gamma 1 through gamma P. the coariance
to lag one up to lag p is equal
to basically fun linear functions given
by the fee of the other
covariances.
Um who can tell me uh you know what the
structure is of this matrix? It's not a
diagonal matrix. What kind of matrix is
this? Sort of a math trivia question
here. But it it has a special
name.
Anyone? It's a toplitz matrix. Okay,
it's where the off diagonals are all the
same value. And in fact, because of the

[01:04]
symmetry of the
coariance basically the gamma of one is
equal to gamma of minus1, gamma of
minus2 is equal to gamma of plus2.
Because of the coariant stationerity,
it's actually also symmetric. So, so
these equations allow us to solve for
the fees so long as we have estimates of
these
coariances. So, if we have a system of
estimates,
uh we can plug these in and attempt to
solve this. Um if they're consistent
estimates of the coariances, then there
will be a solution. And then the zeroth
equation which was not part of this
series of equations. If you go back and
look at the zeroth equation that allows
you to get an estimate for the sigma
squared. So so these u walker equations
are the way in which uh many arma models
are specified in different uh statistics
packages and uh the

[01:05]
uh in terms of you know what principles
are being applied. Well, if if we're
using unbiased estimates of these
parameters, then this is applying what's
called the method of moments principle
for statistical estimation. And with
complicated models where sometimes the
likelihood functions are very hard to
estimate or specify and compute um and
then to do optimization over those is
even harder. Um it it can turn out that
there are relationships between the
moments of the random variables which
are functions of the unknown parameters
and you can solve for basically the
sample moments equaling the theoretical
moments and you apply the method of
moments uh estimation method.
Econometrics is uh you know rich with
many uh applications of that
principle. Uh okay, the next section
goes through the uh moving average

[01:06]
model.
Um let me
uh highlight this. Okay, so with an
order Q moving
average, we basically have a polomial in
the lag operator L which is operated
upon the ADA T's. And if you write out
the expectations of XT, you get mu. The
variance of XT is just gamma is sigma
squar * 1 plus the squares of the uh
coefficients in the polomial. And so
this feature or this property here is
due to the fact that we have
uncorrelated innovations in the uh ads.
The ads are white noise. So the only
thing that comes through in the square
of xt and the expectation of that is the
squared powers of the
uh adas which have coefficients given by

[01:07]
the theta squared. So these properties
are you know left I'll leave you just to
to verify very straightforward.
uh but let's now turn to the final
minutes of the lecture today to
accommodating non-stationary
behavior in time series. Um the
uh original approaches with time series
was to focus on estimation methodologies
for coariant stationary processes. So if
a series is not coariant stationary then
we would want to do some uh
transformation of the data of the series
into uh a
stationary uh so so that the result the
resulting process is stationary and um
with the differencing operators delta
um box and genkins advocated removing

[01:08]
non-stationary trending behavior which
is exhibited often in economic time
series by using a first difference maybe
a second difference or a kth order
difference. So um the uh uh these
operators you know are defined in this
way um basically with the kith order
operator uh having this expression here.
This is sort of the binomial expansion
of uh you know a kith power which um can
be useful. Um anyway it comes up all the
time in probability theory.
And if if a process has a linear time
trend, then delta xt is going to have no
time trend at all because if you you're
basically taking out that linear
component by taking successive
differences. Sometimes if you have a
real series and you look at the
difference it appears non-station you
look at first differences that can still

[01:09]
have not appear to be growing over time
in which case sometimes the second
difference uh will result in a process
with no trend.
So these are uh sort of convenient
tricks techniques to to render the
series stationary and
um let's see there's sort of examples
here of linear trend reversion models
which are rendered uh coar coariant
stationary under first differencing. So
if you okay in this case this is an
example where you have a deterministic
time trend but then you have reversion
to the time trend over time. So we
basically have a tot error about the
deterministic trend is a first order
auto reggressor
process and the moments here can be
derived this way. Um leave that as an

[01:10]
exercise.
Um, one can also consider uh the pure
integrated
process and talk about uh
stochastic trends and uh basically
random walk processes are are often
referred to in econ econometrics as
stochcastic trends and you may want to
try and eliminate those from from uh
remove those from the data or
accommodate them. And so uh but the
stochcastic trend
process is
uh basically given
by the first difference xt is just equal
to uh a to t. And so we have essentially
this random walk from a given starting
point. And it's easy to verify that if
you knew the zeroth point, then the

[01:11]
variance of the tth time point would be
t sigma squar because we're summing t
independent
innovations. And the co-variance of uh
between uh t and like t minus j is
simply t minus j sigma squar and the
correlation between those has this form.
What you can see is that this definitely
depends on time. So it's not a
stationary process. Um so uh this first
differencing
um results in stationerity and the
undifferenced process has has those
features. The
uh okay final
uh let's see where we
are. Okay final topic for today.
um is just how you incorporate

[01:12]
uh non-stationary processes into armor
processes. Well um if you take first
differences or second differences and
the resulting process is coariant
stationary then uh we can just
incorporate that differencing into the
model specification itself and define
ARMA models auto reggressive integrated
moving average
processes. And so to specify these
models, we need to determine the order
of the differencing required to move
trends deterministic or stata
stochcastic and then estimating the
unknown parameters and then applying
model selection criteria. So let me go
very quickly through
this and
um come back to it the beginning of next
time. But in specify in the parameters
of these models we can apply maximum
likelihood again if we assume normality
of these innovations a to
t and we can express the arma model in

[01:13]
state space form which results in a form
for the likelihood function which we'll
see in a few lectures ahead. Um but then
we can apply uh limited information
maximum likelihood where we just
condition on the first few observations
of the data and maximize the
likelihood
or not condition on the first few
observations but also use their
information as well and look at their uh
density functions incorporating those
into the likelihood relative to the
stationary distribution for their
values.
And then the issue becomes how do we
choose amongst different models. Now you
know last time we talked about linear
regression models how you'd specify a
given model. Here we're talking about
auto reggressive moving average and even
integrated moving average processes. And
how do we specify those? Well, with the
method of um maximum

[01:14]
likelihood, there are procedures which
uh there there are measures of um how
effectively a a fitted model is given by
an information criterion
um that you would want to minimize for a
given fitted model. So we can consider
different sets of models, different
numbers of explanatory variables,
different orders of uh auto reggressive
parameters, moving average parameters
and compute say the AI information
criterion or the B information criterion
or the H and Quinn criterion as
different ways of judging how good
different models are. And let me just
finish today by pointing out that what
these information criteria are is
basically a function of the log
likelihood
function which is something we're trying
to maximize with maximum likelihood

[01:15]
estimates and then adding some penalty
for how many parameters we're
estimating. And so what I'd like you to
think about for next time is you know
what kind of a penalty is appropriate
for adding an extra parameter like what
evidence is required to incorporate
extra parameters extra variables in the
model you know would it be t statistics
that are that exceed some threshold or
some other criterion turns out that
these are all related to those issues
and uh it's very interesting how how
those play out and Um, I'll say uh that
if for those of you who've actually seen
these before, uh, the Bay information
criterion corresponds to an assumption
that there is some finite number of
variables in the model and you know what
those
are. The Hen Quinn criterion says maybe
there's an infinite number of variables

[01:16]
in the
model, but um, you want to uh, be able
to identify those. And so um anyway,
it's it's a very challenging problem
with model selection and these criteria
c can be used to specify those. So we'll
go through that next time.

</details>

* [*The Book of Why: The New Science of Cause and Effect*⁠(opens in a new window)](https://www.amazon.com/Book-Why-Science-Cause-Effect/dp/046509760X)

#### **Management**

* [*Thanks for the Feedback: The Science and Art of Receiving Feedback Well*⁠(opens in a new window)](https://www.amazon.com/Thanks-Feedback-Science-Receiving-Well/dp/0670014664)
* [*Change Your Questions, Change Your Life: 10 Powerful Tools for Life and Work*⁠(opens in a new window)](https://www.amazon.com/Change-Your-Questions-Life-Institute/dp/1576756009)

#### **Historical context on powerful technologies**

* [*Dark Territory: The Secret History of Cyber War*⁠(opens in a new window)](https://www.amazon.com/Dark-Territory-Secret-History-Cyber/dp/1476763267)
* [*The Hacked World Order: How Nations Fight, Trade, Maneuver, and Manipulate in the Digital Age*⁠(opens in a new window)](https://www.amazon.com/Hacked-World-Order-Maneuver-Manipulate/dp/1469065894)
* [*Technology Transfer to the USSR, 1928–1937 and 1966–1975: The Role of Western Technology in Soviet Economic Development*⁠(opens in a new window)](https://www.amazon.com/Technology-Transfer-USSR-1928-1937-1966-1975-ebook/dp/B07TKDR9Q2)
* [*The Turing Test: Verbal Behavior as the Hallmark of Intelligence*⁠(opens in a new window)](https://www.amazon.com/Turing-Test-Behavior-Hallmark-Intelligence/dp/0262692937)
* [*The Information: A History, A Theory, A Flood*⁠(opens in a new window)](https://www.amazon.com/Information-History-Theory-Flood/dp/1400096235)
* [*Radical Markets: Uprooting Capitalism and Democracy for a Just Society*⁠(opens in a new window)](http://radicalmarkets.com/)

We also reimburse reasonable self-studying expenses such as books and tutors, used mostly to learn fundamentals in mathematics. These costs are very worthwhile investments!

## How we sustain it

Learning Day’s impact comes from being rigorous about how people use it. It’s not a day for leisure, but instead a day for a specific kind of hard work. We see and try to counteract the following failure modes so that we can sustain it long term:

**Learning Day could be used for work**. Learning Day could turn into a normal working day because people may want to accomplish their main project faster (due to internal or external pressure). We prevent this by having Learning Day on the same day for every team. This creates positive peer pressure and encourages everyone to take advantage of Learning Day.

**Learning Day could expand in scope to non–Learning Days**. We actually haven’t yet observed this happen. Based on what we’ve seen with other organizations, we think this would most likely indicate that the person isn’t excited enough about their main project, and would be a sign to their manager that the person should switch teams or projects.

**Learning Day could be used for leisure**. Our solution is for every team member to share their progress on Slack via [Geekbot⁠(opens in a new window)](https://geekbot.com/). This keeps the excitement high and provides an accountability mechanism.

![Learning Day Slack](https://images.ctfassets.net/kftzwdyauwt9/02121261-cd23-4da7-0f8f0076eccb/85bd37362eaf877d98f7dcda496cdfce/learning-day-slack.jpg?w=3840&q=90&fm=webp)

## Learning Day beyond Robotics

We’ve recently expanded Learning Day from a subset of our technical teams to the entire company. It’s become a cultural staple—on our most recent internal survey, Learning Day was the aspect of our culture that people talked about the most. We’re excited to see its impact as we continue to evolve and support Learning Day in the future.

* [Events](/news/?tags=events)
* [Culture & Careers](/news/?tags=culture-careers)
* [2019](/news/?tags=2019)

## Author

## Related articles

![city](https://images.ctfassets.net/kftzwdyauwt9/5Wm11GSMw6U7lLDKdcyuUY/3180687ca07ba934009f3c2b9219c10c/city.webp?w=3840&q=90&fm=webp)

[Introducing OpenAI London

CompanyJun 28, 2023](/index/introducing-openai-london/)

![Person sitting on a couch in front of a red coffee table in a plant-filled room](https://images.ctfassets.net/kftzwdyauwt9/e3357d5a-b177-4b3a-1edf79a7f2dc/ca1f3418cd72b4eb84c9d1a09dfffc7f/stangel-2022-0421.jpg?w=3840&q=90&fm=webp)

[The power of continuous learning

CompanyDec 23, 2022](/index/the-power-of-continuous-learning/)

![Person gazing across the room with an optimistic expression](https://images.ctfassets.net/kftzwdyauwt9/21098b49-868d-4515-ca433071d782/838b1914602aaba2e3d935b70d1fa11b/stangel-2022-0795.jpg?w=3840&q=90&fm=webp)

[Discovering the minutiae of backend systems

CompanyDec 8, 2022](/index/discovering-the-minutiae-of-backend-systems/)
