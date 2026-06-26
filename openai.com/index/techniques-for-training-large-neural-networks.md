<!-- source: https://openai.com/index/techniques-for-training-large-neural-networks/ -->

June 9, 2022

[Publication](/research/index/publication/)

# Techniques for training large neural networks

![Techniques For Training Large Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/62793de4-0f01-42fc-539325d9af36/bc1ac82499fc1dc43f59accdd31d0195/image-9.webp?w=3840&q=90&fm=webp)

Large neural networks are at the core of many recent advances in AI, but training them is a difficult engineering and research challenge which requires orchestrating a cluster of GPUs to perform a single synchronized calculation.

Large neural networks are at the core of many recent advances in AI, but training them is a difficult engineering and research challenge which requires orchestrating a cluster of GPUs to perform a single synchronized calculation. As cluster and model sizes have grown, machine learning practitioners have developed an increasing variety of techniques to parallelize model training over many GPUs. At first glance, understanding these parallelism techniques may seem daunting, but with only a few assumptions about the structure of the computation these techniques become much more clear—at that point, you’re just shuttling around opaque bits from A to B like a network switch shuttles around packets.

## No parallelism

Loading...

Training a neural network is an iterative process. In every iteration, we do a pass forward through a model’s [layers⁠(opens in a new window)](https://developer.nvidia.com/blog/deep-learning-nutshell-core-concepts/#layer) to compute an output for each training example in a batch of data. Then another pass proceeds [backward⁠(opens in a new window)](https://youtu.be/Ilg3gGewQ5U) through the layers, propagating how much each parameter affects the final output by computing a [gradient⁠(opens in a new window)](https://youtu.be/IHZwWFHWa-w) with respect to each parameter. The average gradient for the batch, the parameters, and some per-parameter optimization state is passed to an optimization algorithm, such as [Adam⁠(opens in a new window)](https://arxiv.org/abs/1412.6980), which computes the next iteration’s parameters (which should have slightly better performance on your data) and new per-parameter optimization state. As the training iterates over batches of data, the model evolves to produce increasingly accurate outputs.

<!-- yt-inline:Ilg3gGewQ5U -->
[![Backpropagation, intuitively | Deep Learning Chapter 3](https://img.youtube.com/vi/Ilg3gGewQ5U/hqdefault.jpg)](https://www.youtube.com/watch?v=Ilg3gGewQ5U)

<details>
<summary>자막: Backpropagation, intuitively | Deep Learning Chapter 3 (12:47)</summary>

[00:00]
Here, we tackle backpropagation, the core algorithm behind how neural networks learn.
After a quick recap for where we are, the first thing I'll do is an intuitive walkthrough
for what the algorithm is actually doing, without any reference to the formulas.
Then, for those of you who do want to dive into the math,
the next video goes into the calculus underlying all this.
If you watched the last two videos, or if you're just jumping in with the appropriate
background, you know what a neural network is, and how it feeds forward information.
Here, we're doing the classic example of recognizing handwritten digits whose pixel
values get fed into the first layer of the network with 784 neurons,
and I've been showing a network with two hidden layers having just 16 neurons each,
and an output layer of 10 neurons, indicating which digit the network is choosing
as its answer.
I'm also expecting you to understand gradient descent,
as described in the last video, and how what we mean by learning is
that we want to find which weights and biases minimize a certain cost function.

[00:01]
As a quick reminder, for the cost of a single training example,
you take the output the network gives, along with the output you wanted it to give,
and add up the squares of the differences between each component.
Doing this for all of your tens of thousands of training examples and
averaging the results, this gives you the total cost of the network.
And as if that's not enough to think about, as described in the last video,
the thing that we're looking for is the negative gradient of this cost function,
which tells you how you need to change all of the weights and biases,
all of these connections, so as to most efficiently decrease the cost.
Backpropagation, the topic of this video, is an
algorithm for computing that crazy complicated gradient.
And the one idea from the last video that I really want you to hold firmly
in your mind right now is that because thinking of the gradient vector
as a direction in 13,000 dimensions is, to put it lightly,
beyond the scope of our imaginations, there's another way you can think about it.

[00:02]
The magnitude of each component here is telling you how
sensitive the cost function is to each weight and bias.
For example, let's say you go through the process I'm about to describe,
and you compute the negative gradient, and the component associated with the weight on
this edge here comes out to be 3.2, while the component associated with this edge here
comes out as 0.1.
The way you would interpret that is that the cost of the function is 32 times more
sensitive to changes in that first weight, so if you were to wiggle that value
just a little bit, it's going to cause some change to the cost,
and that change is 32 times greater than what the same wiggle to that second
weight would give.
Personally, when I was first learning about backpropagation,
I think the most confusing aspect was just the notation and the index chasing of it all.
But once you unwrap what each part of this algorithm is really doing,
each individual effect it's having is actually pretty intuitive,

[00:03]
it's just that there's a lot of little adjustments getting layered on top of each other.
So I'm going to start things off here with a complete disregard for the notation,
and just step through the effects each training example has on the weights and biases.
Because the cost function involves averaging a certain cost per example over all
the tens of thousands of training examples, the way we adjust the weights and
biases for a single gradient descent step also depends on every single example.
Or rather, in principle it should, but for computational efficiency we'll do a little
trick later to keep you from needing to hit every single example for every step.
In other cases, right now, all we're going to do is focus
our attention on one single example, this image of a 2.
What effect should this one training example have
on how the weights and biases get adjusted?
Let's say we're at a point where the network is not well trained yet,
so the activations in the output are going to look pretty random,
maybe something like 0.5, 0.8, 0.2, on and on.

[00:04]
We can't directly change those activations, we
only have influence on the weights and biases.
But it's helpful to keep track of which adjustments
we wish should take place to that output layer.
And since we want it to classify the image as a 2,
we want that third value to get nudged up while all the others get nudged down.
Moreover, the sizes of these nudges should be proportional
to how far away each current value is from its target value.
For example, the increase to that number 2 neuron's activation
is in a sense more important than the decrease to the number 8 neuron,
which is already pretty close to where it should be.
So zooming in further, let's focus just on this one neuron,
the one whose activation we wish to increase.
Remember, that activation is defined as a certain weighted sum of all the
activations in the previous layer, plus a bias,
which is all then plugged into something like the sigmoid squishification function,

[00:05]
or a ReLU.
So there are three different avenues that can team
up together to help increase that activation.
You can increase the bias, you can increase the weights,
and you can change the activations from the previous layer.
Focusing on how the weights should be adjusted,
notice how the weights actually have differing levels of influence.
The connections with the brightest neurons from the preceding layer have the
biggest effect since those weights are multiplied by larger activation values.
So if you were to increase one of those weights,
it actually has a stronger influence on the ultimate cost function than increasing
the weights of connections with dimmer neurons,
at least as far as this one training example is concerned.
Remember, when we talk about gradient descent,
we don't just care about whether each component should get nudged up or down,
we care about which ones give you the most bang for your buck.
This, by the way, is at least somewhat reminiscent of a theory in
neuroscience for how biological networks of neurons learn, Hebbian theory,

[00:06]
often summed up in the phrase, neurons that fire together wire together.
Here, the biggest increases to weights, the biggest strengthening of connections,
happens between neurons which are the most active,
and the ones which we wish to become more active.
In a sense, the neurons that are firing while seeing a 2 get
more strongly linked to those firing when thinking about a 2.
To be clear, I'm not in a position to make statements one way or another about
whether artificial networks of neurons behave anything like biological brains,
and this fires together wire together idea comes with a couple meaningful asterisks,
but taken as a very loose analogy, I find it interesting to note.
Anyway, the third way we can help increase this neuron's activation
is by changing all the activations in the previous layer.
Namely, if everything connected to that digit 2 neuron with a positive
weight got brighter, and if everything connected with a negative weight got dimmer,
then that digit 2 neuron would become more active.

[00:07]
And similar to the weight changes, you're going to get the most bang for your buck
by seeking changes that are proportional to the size of the corresponding weights.
Now of course, we cannot directly influence those activations,
we only have control over the weights and biases.
But just as with the last layer, it's helpful to
keep a note of what those desired changes are.
But keep in mind, zooming out one step here, this
is only what that digit 2 output neuron wants.
Remember, we also want all the other neurons in the last layer to become less active,
and each of those other output neurons has its own thoughts about
what should happen to that second to last layer.
So, the desire of this digit 2 neuron is added together with the desires
of all the other output neurons for what should happen to this second to last layer,
again in proportion to the corresponding weights,
and in proportion to how much each of those neurons needs to change.

[00:08]
This right here is where the idea of propagating backwards comes in.
By adding together all these desired effects, you basically get a
list of nudges that you want to happen to this second to last layer.
And once you have those, you can recursively apply the same process to the
relevant weights and biases that determine those values,
repeating the same process I just walked through and moving backwards
through the network.
And zooming out a bit further, remember that this is all just how a single
training example wishes to nudge each one of those weights and biases.
If we only listened to what that 2 wanted, the network would
ultimately be incentivized just to classify all images as a 2.
So what you do is go through this same backprop routine for every other training example,
recording how each of them would like to change the weights and biases,
and average together those desired changes.

[00:09]
This collection here of the averaged nudges to each weight and bias is,
loosely speaking, the negative gradient of the cost function referenced
in the last video, or at least something proportional to it.
I say loosely speaking only because I have yet to get quantitatively precise
about those nudges, but if you understood every change I just referenced,
why some are proportionally bigger than others,
and how they all need to be added together, you understand the mechanics for
what backpropagation is actually doing.
By the way, in practice, it takes computers an extremely long time to add
up the influence of every training example every gradient descent step.
So here's what's commonly done instead.
You randomly shuffle your training data and then divide it into a whole
bunch of mini-batches, let's say each one having 100 training examples.
Then you compute a step according to the mini-batch.
It's not going to be the actual gradient of the cost function,

[00:10]
which depends on all of the training data, not this tiny subset,
so it's not the most efficient step downhill,
but each mini-batch does give you a pretty good approximation, and more importantly,
it gives you a significant computational speedup.
If you were to plot the trajectory of your network under the relevant cost surface,
it would be a little more like a drunk man stumbling aimlessly down a hill but taking
quick steps, rather than a carefully calculating man determining the exact downhill
direction of each step before taking a very slow and careful step in that direction.
This technique is referred to as stochastic gradient descent.
There's a lot going on here, so let's just sum it up for ourselves, shall we?
Backpropagation is the algorithm for determining how a single training
example would like to nudge the weights and biases,
not just in terms of whether they should go up or down,
but in terms of what relative proportions to those changes cause the
most rapid decrease to the cost.
A true gradient descent step would involve doing this for all your tens of

[00:11]
thousands of training examples and averaging the desired changes you get.
But that's computationally slow, so instead you randomly subdivide the
data into mini-batches and compute each step with respect to a mini-batch.
Repeatedly going through all of the mini-batches and making these adjustments,
you will converge towards a local minimum of the cost function,
which is to say your network will end up doing a really good job on the training
examples.
So with all of that said, every line of code that would go into implementing backprop
actually corresponds with something you have now seen, at least in informal terms.
But sometimes knowing what the math does is only half the battle,
and just representing the damn thing is where it gets all muddled and confusing.
So for those of you who do want to go deeper, the next video goes through the same
ideas that were just presented here, but in terms of the underlying calculus,
which should hopefully make it a little more familiar as you see the topic in other
resources.
Before that, one thing worth emphasizing is that for this algorithm to work,

[00:12]
and this goes for all sorts of machine learning beyond just neural networks,
you need a lot of training data.
In our case, one thing that makes handwritten digits such a nice example is that there
exists the MNIST database, with so many examples that have been labeled by humans.
So a common challenge that those of you working in machine learning will be familiar with
is just getting the labeled training data you actually need,
whether that's having people label tens of thousands of images,
or whatever other data type you might be dealing with.

</details>


<!-- yt-inline:IHZwWFHWa-w -->
[![Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://img.youtube.com/vi/IHZwWFHWa-w/hqdefault.jpg)](https://www.youtube.com/watch?v=IHZwWFHWa-w)

<details>
<summary>자막: Gradient descent, how neural networks learn | Deep Learning Chapter 2 (20:33)</summary>

[00:00]
Last video I laid out the structure of a neural network.
I'll give a quick recap here so that it's fresh in our minds,
and then I have two main goals for this video.
The first is to introduce the idea of gradient descent,
which underlies not only how neural networks learn,
but how a lot of other machine learning works as well.
Then after that we'll dig in a little more into how this particular network performs,
and what those hidden layers of neurons end up looking for.
As a reminder, our goal here is the classic example of handwritten digit recognition,
the hello world of neural networks.
These digits are rendered on a 28x28 pixel grid,
each pixel with some grayscale value between 0 and 1.
Those are what determine the activations of 784 neurons in the input layer of the network.
And then the activation for each neuron in the following layers is based on a weighted
sum of all the activations in the previous layer, plus some special number called a bias.

[00:01]
Then you compose that sum with some other function,
like the sigmoid squishification, or a relu, the way I walked through last video.
In total, given the somewhat arbitrary choice of two hidden layers with 16 neurons each,
the network has about 13,000 weights and biases that we can adjust,
and it's these values that determine what exactly the network actually does.
Then what we mean when we say that this network classifies a given digit is that
the brightest of those 10 neurons in the final layer corresponds to that digit.
And remember, the motivation we had in mind here for the layered structure
was that maybe the second layer could pick up on the edges,
and the third layer might pick up on patterns like loops and lines,
and the last one could just piece together those patterns to recognize digits.
So here, we learn how the network learns.
What we want is an algorithm where you can show this network a whole bunch of
training data, which comes in the form of a bunch of different images of handwritten

[00:02]
digits, along with labels for what they're supposed to be,
and it'll adjust those 13,000 weights and biases so as to improve its performance
on the training data.
Hopefully, this layered structure will mean that what it
learns generalizes to images beyond that training data.
The way we test that is that after you train the network,
you show it more labeled data that it's never seen before,
and you see how accurately it classifies those new images.
Fortunately for us, and what makes this such a common example to start with,
is that the good people behind the MNIST database have put together a collection of tens
of thousands of handwritten digit images, each one labeled with the numbers they're
supposed to be.
And as provocative as it is to describe a machine as learning,
once you see how it works, it feels a lot less like some crazy sci-fi premise,
and a lot more like a calculus exercise.
I mean, basically it comes down to finding the minimum of a certain function.

[00:03]
Remember, conceptually, we're thinking of each neuron as being connected to all
the neurons in the previous layer, and the weights in the weighted sum defining
its activation are kind of like the strengths of those connections,
and the bias is some indication of whether that neuron tends to be active or inactive.
And to start things off, we're just going to initialize
all of those weights and biases totally randomly.
Needless to say, this network is going to perform pretty horribly on
a given training example, since it's just doing something random.
For example, you feed in this image of a 3, and the output layer just looks like a mess.
So what you do is define a cost function, a way of telling the computer,
no, bad computer, that output should have activations which are 0 for most neurons,
but 1 for this neuron, what you gave me is utter trash.
To say that a little more mathematically, you add up the squares of the differences
between each of those trash output activations and the value you want them to have,

[00:04]
and this is what we'll call the cost of a single training example.
Notice this sum is small when the network confidently classifies the image correctly,
but it's large when the network seems like it doesn't know what it's doing.
So then what you do is consider the average cost over all of
the tens of thousands of training examples at your disposal.
This average cost is our measure for how lousy the network is,
and how bad the computer should feel.
And that's a complicated thing.
Remember how the network itself was basically a function,
one that takes in 784 numbers as inputs, the pixel values,
and spits out 10 numbers as its output, and in a sense it's parameterized
by all these weights and biases?
Well the cost function is a layer of complexity on top of that.
It takes as its input those 13,000 or so weights and biases,
and spits out a single number describing how bad those weights and biases are,

[00:05]
and the way it's defined depends on the network's behavior over all the tens of
thousands of pieces of training data.
That's a lot to think about.
But just telling the computer what a crappy job it's doing isn't very helpful.
You want to tell it how to change those weights and biases so that it gets better.
To make it easier, rather than struggling to imagine a function with 13,000 inputs,
just imagine a simple function that has one number as an input and one number as an
output.
How do you find an input that minimizes the value of this function?
Calculus students will know that you can sometimes figure out that minimum explicitly,
but that's not always feasible for really complicated functions,
certainly not in the 13,000 input version of this situation for our crazy complicated
neural network cost function.
A more flexible tactic is to start at any input,
and figure out which direction you should step to make that output lower.

[00:06]
Specifically, if you can figure out the slope of the function where you are,
then shift to the left if that slope is positive,
and shift the input to the right if that slope is negative.
If you do this repeatedly, at each point checking the new slope and taking the
appropriate step, you're going to approach some local minimum of the function.
The image you might have in mind here is a ball rolling down a hill.
Notice, even for this really simplified single input function,
there are many possible valleys that you might land in,
depending on which random input you start at,
and there's no guarantee that the local minimum you land in is going to
be the smallest possible value of the cost function.
That will carry over to our neural network case as well.
And I also want you to notice how if you make your step sizes proportional to the slope,
then when the slope is flattening out towards the minimum,
your steps get smaller and smaller, and that kind of helps you from overshooting.
Bumping up the complexity a bit, imagine instead
a function with two inputs and one output.

[00:07]
You might think of the input space as the xy-plane,
and the cost function as being graphed as a surface above it.
Now instead of asking about the slope of the function,
you have to ask which direction you should step in this input
space so as to decrease the output of the function most quickly.
In other words, what's the downhill direction?
Again, it's helpful to think of a ball rolling down that hill.
Those of you familiar with multivariable calculus will know that the
gradient of a function gives you the direction of steepest ascent,
which direction should you step to increase the function most quickly.
Naturally enough, taking the negative of that gradient gives you
the direction to step that decreases the function most quickly.
Even more than that, the length of this gradient vector is
an indication for just how steep that steepest slope is.
If you're unfamiliar with multivariable calculus and want to learn more,
check out some of the work I did for Khan Academy on the topic.

[00:08]
Honestly though, all that matters for you and me right now is that
in principle there exists a way to compute this vector,
this vector that tells you what the downhill direction is and how steep it is.
You'll be okay if that's all you know and you're not rock solid on the details.
Cause If you can get that, the algorithm for minimizing the function is to compute this
gradient direction, then take a small step downhill, and repeat that over and over.
It's the same basic idea for a function that has 13,000 inputs instead of 2 inputs.
Imagine organizing all 13,000 weights and biases
of our network into a giant column vector.
The negative gradient of the cost function is just a vector,
it's some direction inside this insanely huge input space that tells you which
nudges to all of those numbers is going to cause the most rapid decrease to
the cost function.
And of course, with our specially designed cost function,
changing the weights and biases to decrease it means making the

[00:09]
output of the network on each piece of training data look less like
a random array of 10 values, and more like an actual decision we want it to make.
It's important to remember, this cost function involves an average over all of the
training data, so if you minimize it, it means it's a better performance on all of those
samples.
The algorithm for computing this gradient efficiently,
which is effectively the heart of how a neural network learns,
is called backpropagation, and it's what I'm going to be talking about next video.
There, I really want to take the time to walk through what exactly happens to
each weight and bias for a given piece of training data,
trying to give an intuitive feel for what's happening beyond the pile of relevant
calculus and formulas.
Right here, right now, the main thing I want you to know,
independent of implementation details, is that what we mean when we
talk about a network learning is that it's just minimizing a cost function.
And notice, one consequence of that is that it's important for this cost function to have

[00:10]
a nice smooth output, so that we can find a local minimum by taking little steps
downhill.
This is why, by the way, artificial neurons have continuously ranging activations,
rather than simply being active or inactive in a binary way,
the way biological neurons are.
This process of repeatedly nudging an input of a function by some
multiple of the negative gradient is called gradient descent.
It's a way to converge towards some local minimum of a cost function,
basically a valley in this graph.
I'm still showing the picture of a function with two inputs, of course,
because nudges in a 13,000 dimensional input space are a little hard to
wrap your mind around, but there is a nice non-spatial way to think about this.
Each component of the negative gradient tells us two things.
The sign, of course, tells us whether the corresponding
component of the input vector should be nudged up or down.
But importantly, the relative magnitudes of all these
components kind of tells you which changes matter more.

[00:11]
You see, in our network, an adjustment to one of the weights might have a much
greater impact on the cost function than the adjustment to some other weight.
Some of these connections just matter more for our training data.
So a way you can think about this gradient vector of our mind-warpingly massive
cost function is that it encodes the relative importance of each weight and bias,
that is, which of these changes is going to carry the most bang for your buck.
This really is just another way of thinking about direction.
To take a simpler example, if you have some function with two variables as an input,
and you compute that its gradient at some particular point comes out as 3,1,
then on the one hand you can interpret that as saying that when you're
standing at that input, moving along this direction increases the function most quickly,
that when you graph the function above the plane of input points,
that vector is what's giving you the straight uphill direction.

[00:12]
But another way to read that is to say that changes to this first variable have 3
times the importance as changes to the second variable,
that at least in the neighborhood of the relevant input,
nudging the x-value carries a lot more bang for your buck.
Let's zoom out and sum up where we are so far.
The network itself is this function with 784 inputs and 10 outputs,
defined in terms of all these weighted sums.
The cost function is a layer of complexity on top of that.
It takes the 13,000 weights and biases as inputs and spits out
a single measure of lousiness based on the training examples.
And the gradient of the cost function is one more layer of complexity still.
It tells us what nudges to all these weights and biases cause the
fastest change to the value of the cost function,
which you might interpret as saying which changes to which weights matter the most.

[00:13]
So, when you initialize the network with random weights and biases,
and adjust them many times based on this gradient descent process,
how well does it actually perform on images it's never seen before?
The one I've described here, with the two hidden layers of 16 neurons each,
chosen mostly for aesthetic reasons, is not bad,
classifying about 96% of the new images it sees correctly.
And honestly, if you look at some of the examples it messes up on,
you feel compelled to cut it a little slack.
Now if you play around with the hidden layer structure and make a couple tweaks,
you can get this up to 98%.
And that's pretty good!
It's not the best, you can certainly get better performance by getting more sophisticated
than this plain vanilla network, but given how daunting the initial task is,
I think there's something incredible about any network doing this well on images it's
never seen before, given that we never specifically told it what patterns to look for.

[00:14]
Originally, the way I motivated this structure was by describing a hope we might have,
that the second layer might pick up on little edges,
that the third layer would piece together those edges to recognize loops
and longer lines, and that those might be pieced together to recognize digits.
So is this what our network is actually doing?
Well, for this one at least, not at all.
Remember how last video we looked at how the weights of the connections from all
the neurons in the first layer to a given neuron in the second layer can be
visualized as a given pixel pattern that the second layer neuron is picking up on?
Well, when we actually do that for the weights associated with these transitions,
from the first layer to the next, instead of picking up on isolated little edges here
and there, they look, well, almost random, just with some very loose patterns in the
middle there.
It would seem that in the unfathomably large 13,000 dimensional space
of possible weights and biases, our network found itself a happy

[00:15]
little local minimum that, despite successfully classifying most images,
doesn't exactly pick up on the patterns we might have hoped for.
And to really drive this point home, watch what happens when you input a random image.
If the system was smart, you might expect it to feel uncertain,
maybe not really activating any of those 10 output neurons or activating them
all evenly, but instead it confidently gives you some nonsense answer,
as if it feels as sure that this random noise is a 5 as it does that an actual
image of a 5 is a 5.
Phrased differently, even if this network can recognize digits pretty well,
it has no idea how to draw them.
A lot of this is because it's such a tightly constrained training setup.
I mean, put yourself in the network's shoes here.
From its point of view, the entire universe consists of nothing but clearly
defined unmoving digits centered in a tiny grid,
and its cost function never gave it any incentive to be anything but utterly
confident in its decisions.

[00:16]
So with this as the image of what those second layer neurons are really doing,
you might wonder why I would introduce this network with the
motivation of picking up on edges and patterns.
I mean, that's just not at all what it ends up doing.
Well, this is not meant to be our end goal, but instead a starting point.
Frankly, this is old technology, the kind researched in the 80s and 90s,
and you do need to understand it before you can understand more detailed modern
variants, and it clearly is capable of solving some interesting problems,
but the more you dig into what those hidden layers are really doing,
the less intelligent it seems.
Shifting the focus for a moment from how networks learn to how you learn,
that'll only happen if you engage actively with the material here somehow.
One pretty simple thing I want you to do is just pause right now and think deeply
for a moment about what changes you might make to this system and how it perceives
images if you wanted it to better pick up on things like edges and patterns.

[00:17]
But better than that, to actually engage with the material,
I highly recommend the book by Michael Nielsen on deep learning and neural networks.
In it, you can find the code and the data to download and play with for this exact
example, and the book will walk you through step by step what that code is doing.
What's awesome is that this book is free and publicly available,
so if you do get something out of it, consider joining me in making a donation towards
Nielsen's efforts.
I've also linked a couple other resources I like a lot in the description,
including the phenomenal and beautiful blog post by Chris Ola and the articles in
Distill.
To close things off here for the last few minutes,
I want to jump back into a snippet of the interview I had with Leisha Lee.
You might remember her from the last video, she did her PhD work in deep learning.
In this little snippet she talks about two recent papers that really dig into
how some of the more modern image recognition networks are actually learning.
Just to set up where we were in the conversation,
the first paper took one of these particularly deep neural networks that's really good

[00:18]
at image recognition, and instead of training it on a properly labeled dataset,
shuffled all the labels around before training.
Obviously the testing accuracy here was going to be no better than random,
since everything's just randomly labeled. But it was still able to achieve
the same training accuracy as you would on a properly labeled dataset.
Basically, the millions of weights for this particular network were
enough for it to just memorize the random data,
which raises the question for whether minimizing this cost function
actually corresponds to any sort of structure in the image, or is it just memorization?
...to memorize the entire dataset of what the correct classification is.
And so half a year later at ICML this year, there was not exactly rebuttal paper,
but paper that addressed some aspects of like, hey,
actually these networks are doing something a little bit smarter than that.

[00:19]
If you look at that accuracy curve if you were just training on a random data set
that curve went down very slowly, almost in a linear fashion.
So you’re really struggling to find that local minimum of the right weights.
Whereas if you're actually training on a structured dataset,
one that has the right labels, you fiddle around a little bit in the beginning,
but then you kind of dropped very fast to get to that accuracy level,
and so in some sense it was easier to find that local maxima.
And so what was also interesting about that is it brings into light another paper from
actually a couple of years ago, which has a lot more simplifications about the network
layers, but one of the results was saying how if you look at the optimization landscape,
the local minima that these networks tend to learn are actually of equal quality,
so in some sense if your dataset is structured,
you should be able to find that much more easily.
My thanks, as always, to those of you supporting on Patreon.

[00:20]
I've said before just what a game changer Patreon is,
but these videos really would not be possible without you.
I also want to give a special thanks to the VC firm Amplify Partners
and their support of these initial videos in the series. Thank you.

</details>


Various parallelism techniques slice this training process across different dimensions, including:

* Data parallelism—run different subsets of the batch on different GPUs;
* Pipeline parallelism—run different layers of the model on different GPUs;
* Tensor parallelism—break up the math for a single operation such as a matrix multiplication to be split across GPUs;
* Mixture-of-Experts—process each example by only a fraction of each layer.

(In this post, we’ll assume that you are using GPUs to train your neural networks, but the same ideas apply to those using any other [neural network accelerator⁠(opens in a new window)](https://www.synopsys.com/ai/what-is-an-ai-accelerator.html).)

## Data parallelism

*Data Parallel* training means copying the same parameters to multiple GPUs (often called “workers”) and assigning different examples to each to be processed simultaneously. Data parallelism alone still requires that your model fits into a single GPU’s memory, but lets you utilize the compute of many GPUs at the cost of storing many duplicate copies of your parameters. That being said, there are strategies to increase the effective RAM available to your GPU, such as temporarily offloading parameters to CPU memory between usages.

As each data parallel worker updates its copy of the parameters, they need to coordinate to ensure that each worker continues to have similar parameters. The simplest approach is to introduce blocking communication between workers: (1) independently compute the gradient on each worker; (2) [average the gradients across workers⁠(opens in a new window)](https://tech.preferred.jp/en/blog/technologies-behind-distributed-deep-learning-allreduce/); and (3) independently compute the same new parameters on each worker. Step (2) is a blocking average which requires transferring quite a lot of data (proportional to the number of workers times the size of your parameters), which can hurt your training throughput. There are various [asynchronous synchronization schemes⁠(opens in a new window)](https://arxiv.org/abs/1106.5730) to remove this overhead, but they hurt learning efficiency; in practice, people generally stick with the synchronous approach.

## Pipeline parallelism

With *Pipeline Parallel* training, we partition sequential chunks of the model across GPUs. Each GPU holds only a fraction of parameters, and thus the same model consumes proportionally less memory per GPU.

It’s straightforward to split a large model into chunks of consecutive layers. However, there’s a sequential dependency between inputs and outputs of layers, so a naive implementation can lead to a large amount of idle time while a worker waits for outputs from the previous machine to be used as its inputs. These waiting time chunks are known as “bubbles,” wasting the computation that could be done by the idling machines.

Loading...

We can reuse the ideas from data parallelism to reduce the cost of the bubble by having each worker only process a subset of data elements at one time, allowing us to cleverly overlap new computation with wait time. The core idea is to split one batch into multiple microbatches; each microbatch should be proportionally faster to process and each worker begins working on the next microbatch as soon as it’s available, thus expediting the pipeline execution. With enough microbatches the workers can be utilized most of the time with a minimal bubble at the beginning and end of the step. Gradients are averaged across microbatches, and updates to the parameters happen only once all microbatches have been completed.

The number of workers that the model is split over is commonly known as *pipeline depth*.

During the forward pass, workers only need to send the output (called activations) of its chunk of layers to the next worker; during the backward pass, it only sends the gradients on those activations to the previous worker. There’s a big design space of how to schedule these passes and how to aggregate the gradients across microbatches. [GPipe⁠(opens in a new window)](https://arxiv.org/abs/1811.06965) has each worker process forward and backward passes consecutively and then aggregates gradients from multiple microbatches synchronously at the end. [PipeDream⁠(opens in a new window)](https://cs.stanford.edu/~matei/papers/2019/sosp_pipedream.pdf) instead schedules each worker to alternatively process forward and backward passes.

Loading...

## Tensor parallelism

Pipeline parallelism splits a model “vertically” by layer. It’s also possible to “horizontally” split certain operations within a layer, which is usually called *Tensor Parallel* training. For many modern models (such as the [Transformer⁠(opens in a new window)](https://jalammar.github.io/illustrated-transformer/)), the computation bottleneck is multiplying an activation batch matrix with a large weight matrix. [Matrix multiplication⁠(opens in a new window)](https://en.wikipedia.org/wiki/Matrix_multiplication) can be thought of as dot products between pairs of rows and columns; it’s possible to compute independent dot products on different GPUs, or to compute parts of each dot product on different GPUs and sum up the results. With either strategy, we can slice the weight matrix into even-sized “shards”, host each shard on a different GPU, and use that shard to compute the relevant part of the overall matrix product before later communicating to combine the results.

One example is [Megatron-LM⁠(opens in a new window)](https://nv-adlr.github.io/MegatronLM), which parallelizes matrix multiplications within the Transformer’s self-attention and MLP layers. [PTD-P⁠(opens in a new window)](https://arxiv.org/abs/2104.04473) uses tensor, data, and pipeline parallelism; its pipeline schedule assigns multiple non-consecutive layers to each device, reducing bubble overhead at the cost of more network communication.

Sometimes the input to the network can be parallelized across a dimension with a high degree of parallel computation relative to cross-communication. [Sequence parallelism⁠(opens in a new window)](https://arxiv.org/abs/2205.05198) is one such idea, where an input sequence is split across time into multiple sub-examples, proportionally decreasing peak memory consumption by allowing the computation to proceed with more granularly-sized examples.

## Mixture-of-Experts (MoE)

With the [Mixture-of-Experts (MoE)⁠(opens in a new window)](https://arxiv.org/abs/1701.06538) approach, only a fraction of the network is used to compute the output for any one input. One example approach is to have many sets of weights and the network can choose which set to use via a gating mechanism at inference time. This enables many more parameters without increased computation cost. Each set of weights is referred to as “experts,” in the hope that the network will learn to assign specialized computation and skills to each expert. Different experts can be hosted on different GPUs, providing a clear way to scale up the number of GPUs used for a model.

![Illustration of a mixture-of-experts (MoE) layer. Only 2 out of the n experts are selected by the gating network. (Image adapted from: Shazeer et al., 2017)](https://images.ctfassets.net/kftzwdyauwt9/cb1a6327-67de-4d07-408086e8e33b/e24e8be0f14f8285430ef975c2279c97/moe.svg?w=3840&q=90)

Illustration of a mixture-of-experts (MoE) layer. Only 2 out of the *n* experts are selected by the gating network. (Image adapted from: [Shazeer et al., 2017⁠(opens in a new window)](https://arxiv.org/abs/1701.06538))

[GShard⁠(opens in a new window)](https://arxiv.org/abs/2006.16668) scales an MoE Transformer up to 600 billion parameters with a scheme where only the MoE layers are split across multiple TPU devices and other layers are fully duplicated. [Switch Transformer⁠(opens in a new window)](https://arxiv.org/abs/2101.03961) scales model size to trillions of parameters with even higher sparsity by routing one input to a single expert.

## Other memory saving designs

There are many other computational strategies to make training increasingly large neural networks more tractable. For example:

* To compute the gradient, you need to have saved the original activations, which can consume a lot of device RAM. [*Checkpointing*⁠(opens in a new window)](https://arxiv.org/abs/1604.06174) (also known as activation recomputation) stores any subset of activations, and recomputes the intermediate ones just-in-time during the backward pass. This saves a lot of memory at the computational cost of at most one additional full forward pass. One can also continually trade off between compute and memory cost by [selective activation recomputation⁠(opens in a new window)](https://arxiv.org/abs/2205.05198), which is checkpointing subsets of the activations that are relatively more expensive to store but cheaper to compute.
* [*Mixed Precision Training*⁠(opens in a new window)](https://arxiv.org/abs/1710.03740) is to train models using lower-precision numbers (most commonly [FP16⁠(opens in a new window)](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)). Modern accelerators can reach much higher FLOP counts with lower-precision numbers, and you also save on device RAM. With proper care, the resulting model can lose almost no accuracy.
* *Offloading* is to temporarily offload unused data to the CPU or amongst different devices and later read it back when needed. Naive implementations will slow down training a lot, but sophisticated implementations will pre-fetch data so that the device never needs to wait on it. One implementation of this idea is [ZeRO⁠(opens in a new window)](https://arxiv.org/abs/1910.02054) which splits the parameters, gradients, and optimizer states across all available hardware and materializes them as needed.
* *Memory Efficient Optimizers* have been proposed to reduce the memory footprint of the running state maintained by the optimizer, such as [Adafactor⁠(opens in a new window)](https://arxiv.org/abs/1804.04235).
* *Compression* also can be used for storing intermediate results in the network. For example, [Gist⁠(opens in a new window)](https://www.microsoft.com/en-us/research/uploads/prod/2018/04/fiddle-gist-isca18.pdf) compresses activations that are saved for the backward pass; [DALL·E⁠](/index/dall-e/) compresses the gradients before synchronizing them.

At OpenAI, we are training and improving large models from the underlying infrastructure all the way to deploying them for real-world problems. If you’d like to put the ideas from this post into practice—especially relevant for our Scaling and Applied Research teams—we’re [hiring⁠](/careers/research-engineer/)!

* [Compute Scaling](/research/index/?tags=compute-scaling)
* [Software & Engineering](/research/index/?tags=software-engineering)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Lilian Weng, Greg Brockman

## Acknowledgments

Thanks to Nikolas Tezak, Sam Altman, Daniel Gackle, Ilya Sutskever, and Steven Adler for feedback on drafts. Thanks to Justin Jay Wang, Bianca Martin, and Steve Dowling for communications and design.

## Related articles

![Introducing Triton Open Source Gpu Programming For Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/cdce1ebd-19a2-4848-a08ec8c44e18/55b924fc6628318148b7c5c4902551e7/image-18.webp?w=3840&q=90&fm=webp)

[Introducing Triton: Open-source GPU programming for neural networks

ReleaseJul 28, 2021](/index/triton/)

![Scaling Kubernetes To 7 500 Nodes](https://images.ctfassets.net/kftzwdyauwt9/84745f0a-d786-4066-99f031ec2cb2/be1d8d7357f9f5bc35970e058f42c8d0/image-25.webp?w=3840&q=90&fm=webp)

[Scaling Kubernetes to 7,500 nodes

ConclusionJan 25, 2021](/index/scaling-kubernetes-to-7500-nodes/)

![AI And Efficiency](https://images.ctfassets.net/kftzwdyauwt9/e5cba1f8-883b-4961-dca6f726f936/be1a627ab2f509a68b91b8a7ef29f610/image_128.png?w=3840&q=90&fm=webp)

[AI and efficiency

PublicationMay 5, 2020](/index/ai-and-efficiency/)
