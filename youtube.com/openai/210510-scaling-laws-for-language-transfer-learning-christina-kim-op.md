---
title: "Scaling Laws for Language Transfer Learning | Christina Kim | OpenAI Scholars Demo Day 2021"
channel: openai
url: https://www.youtube.com/watch?v=lpe5Gwuqa-k
youtube_id: lpe5Gwuqa-k
published: 2021-05-10
duration: "15:03"
captions: en-orig
---

# Scaling Laws for Language Transfer Learning | Christina Kim | OpenAI Scholars Demo Day 2021

[![Scaling Laws for Language Transfer Learning | Christina Kim | OpenAI Scholars Demo Day 2021](https://img.youtube.com/vi/lpe5Gwuqa-k/hqdefault.jpg)](https://www.youtube.com/watch?v=lpe5Gwuqa-k)

<details>
<summary>자막: Scaling Laws for Language Transfer Learning | Christina Kim | OpenAI Scholars Demo Day 2021 (15:03)</summary>

[00:00]
Hi everyone.
I'm Kristina Kim and I'm really excited
to present my scholars project on the
scaling laws for language transfer
learning.
Um so throughout the Open AI scholars
program, I was really interested in
questions around data. Um what
characteristics and attributes are there
um and how does that impact model
performance? So for my project, I looked
at how do the scaling laws look for
pre-trained English language models as
we transfer to other languages.
So historically, the advancement of deep
learning capabilities has been centered
around three different levers. So that's
better algorithms, faster and cheaper
compute, and larger high-quality data
sets.
Given machine learning's potential
significant impact in society, deepening
our general understanding of machine
learning and how certain factors improve
models is critical for making better
predictions of which capabilities are
going to develop next and when.
Further, the exploration of scaling laws
um evidenced across these three factors
has created a way to measure the impact
of these three as they interact and
limit each other.
So my project framework is inspired by

[00:01]
the work on scaling laws, which was
published by Open AI in the past year.
Um scaling laws predict machine learning
performance, as I said, as a function of
model size, data set size, and the
amount of compute used for training. So
you can think of compute, data set size,
and model size as different limiting
factors um that you can be uh changing
to get better performance. And recently,
scaling relationships were found for
transfer learning from pre-trained
English text models to Python.
So scaling laws for transfer are
important because the scaling
relationships can help explain how to
work in a limited data regime. So in an
ideal world, you're going to have an
infinite amount of data for your models
to be learning from. Um and by that, I
mean that you're only limited by the
other two factors, compute and model
size.
But getting a large quantity of
high-quality data is a non-trivial task
and it's oftentimes uh near impossible.
As a result, most problems that we want
to study are actually in this low data
regime.
Uh before the scholars program, I was a
machine learning engineer and I saw

[00:02]
firsthand how costly it is in both time
and money to get good quality data.
Um evaluating these tradeoffs is a
pretty important and practical question
uh that many researchers and
practitioners have to handle.
So building upon the work from scaling
laws for transfer, my experiments try to
answer the question, how much does
pre-training actually help when we're
transferring across different languages
um being Chinese, Spanish, and German,
and what does that look like as we vary
the data set size and model size?
So for my experiments, I first had to
pre-train English language models um and
I pre-trained decoder-only transformers
of size 124 million non-embedding
parameters to the my smallest model
size, which was 3.3 million
non-embedding parameters. Um I trained
this all on OpenWebText2, which is an
open-source version of WebText, which
was used to train um GPT-2.
I used the same hyperparameters from the
original scaling laws for neural
languages paper, except I used a
500-step warm-up with a cosine decay to

[00:03]
10% of the max learning rate here.
Um the text is encoded with the same
GPT-2 tokenizer, um which is a
byte-level byte pair encoding with a
vocab size of 50,000. And all the models
were trained to about 26 billion tokens.
And as you can see here, um my models
exhibit scaling laws similar to what was
found in the scaling laws for neural
languages, except this line isn't quite
linear here. Um and that kind of
indicates that maybe my largest models
are under-trained a bit here.
After getting my pre-trained models, um
I next set up my fine-tuning
experiments. So for my fine-tuning
experiments, I wanted to focus on
changing the number of tokens in the
data while holding performance, which in
our case was cross-entropy loss and
model size constant.
So for these experiments, the data set
size spanned six orders of magnitude,
while the model sizes spanned two orders
of magnitude. And I trained this on
three different languages, which were
Chinese, Spanish, and German. So for the

[00:04]
Chinese data set, I used this data set
called CommunityQA, which um is similar
to the WebText corpus.
And then for German and Spanish, I got
it from Oscar, which is a multilingual
corpus um got by classifying the Common
Crawl corpus.
So in my experiments, the thing that I
really wanted to measure was the
effective data transfer. So what does
that look like when we are training from
English text to Chinese, Spanish, and
German text? And so the effective data
transfer um can be measured as
this is the amount of fine-tuning data
needed to get to this loss when we're um
using a pre-trained model, and then this
purple dotted line is the amount of
additional data that we would need to
get to that same loss when we're
training from scratch on the um this
data set size.
So it's important to note here that as
you can see, the amount of data
transferred from pre-training gets
smaller as we increase the number of
tokens in the data set size that we're
looking at. Um and eventually, for this
model, it converges around uh 10 million

[00:05]
tokens for the data set size.
So I wanted to show you what it looks
like when we actually compare these
three languages. So
this is like the exciting bit here. And
so you can see that for the pre-trained
English models, they help the most when
we're learning um German versus Spanish
and Chinese.
And that kind of makes sense because I
think these results reflect a lot about
the linguistic similarities between
English and these other languages. So
English and German are both derived from
Proto-Germanic and are linguistically
most similar. And although Spanish um
shares many of the same symbols as the
English alphabet, it's actually in a
different family of languages. And then
obviously, Chinese has a very, very
different alphabet than the English
alphabet um and is very distinct there.
Um another thing I want to highlight
here is a bit about the shape of the
lines and the distance between them.
So as you can see, the effective data
transfer for Spanish and Chinese is not
too different at this initial point here

[00:06]
um for data set size of 8,000 tokens.
However, as we increase the data set
size, we can see that pre-training
continues to help for another order of
magnitude um compared uh to Chinese
here.
Another way to think about um the amount
of data, how much data is actually
useful from pre-training, is to think
about the
fraction of effective data of
fine-tuning. So the smaller this
fraction is, it means more pre-training
uh means pre-training has helped us
more. So as you can see these graphs
here, as the model size increases, um
this fraction decreases all languages,
which means that pre-training has become
more effective.
Um but as we
increase the data set size, um
this fraction increases across model
sizes, and that means pre-training has
become less effective here. Um a lot of
these results here on this graph show
um
the same point that I brought up on the
previous slide about how far apart are

[00:07]
maybe these distributions are from each
other. Um and as you can see that the
German graph here has steeper curves
compared to the Spanish and Chinese, and
I think that indicates
um that there's more transfer uh
happening for German compared to the
other two languages.
Another interesting thing that we found
was that pre-training helps most in low
data regimes. So in a low data regime,
pre-training is most helpful across the
data size uh across model sizes, but
especially in the smaller model sizes.
And you can see here as I increase the
model size with the fixed data set size
um of Chinese text to find uh
to fine-tune it on, models trained from
scratch on Chinese did not improve,
while the models were
the models pre-trained on English
continued to achieve um better
performance. So you can see here that
these flat lines here are where we're
data-limited um in this setup um versus
when we start to see an increase um in
the slope, we're now parameter-limited.

[00:08]
Another important thing to note is that
pre-training and using pre-trained
models is way more compute-efficient
than uh using uh training from scratch.
And you can see this here um for this
one model size um for this one data set
size.
I want to talk about some limitations
that some of my experiments had. And so
the first one is that I used the same
tokenizer for all languages. So this is
an issue cuz as I mentioned before, the
tokenizer had a 50K vocab size, and
Chinese um has over 50,000 characters in
its uh
uh language. So
that means a lot of the tokenization is
probably quite inefficient. Um and so
this could impact model performance
quite a bit. So I think for future work,
uh you would want to train your own
tokenizers um
and then transfer to learn from there.
Another point is that uh it looks like
from my original uh plots for the
pre-training, that maybe I could have
been pre-training for longer. Um and
then I think I could have gotten more

[00:09]
linear line for some of the scaling laws
that I saw for the OpenWebText models.
Another thing um that I would want to do
is do a more thorough hyperparameter
sweep and learning rate sweep. Um as I
believe that both of these uh
limitations uh would cause a very, very
different results. Um I believe the
numbers that I've gotten in the previous
slides would be very different had I
found the ideal optimum learning rates
for the different data set sizes and
model sizes.
Um one other note is that my data the
languages that I got are from different
sources, and so I think this experiment
could be more
thorough if I had used the same um data
set source for all three of the
languages.
I want to talk about some future work
that I'm really excited about after this
project. So I think one thing that could
be really interesting is to compare the
effective data transfer as we use
pre-trained models of a different
language back to English. Um
then you can maybe create some kind of
mapping of how far apart are

[00:10]
distributions from each other. Is there
some kind of symmetry in the data
transfer there? Um, and what does that
actually look like?
Um, another obvious next steps would be
uh to actually use this setup to do uh
work in low-resource languages or other
tasks and distributions that are quite
different from English.
Um,
another thing that'd be really cool to
do based on this work would be to
predict the ideal ratio for pre-train
versus fine-tune for any given problem
for some compute uh for some budget that
you would have.
Um, another thing that I think would be
interesting in the same format of
experimentation would be studying the
forgetting problem in transfer learning
and see what that effective data
transfer looks like as we um
are approaching this problem.
Before I answer questions, I wanted to
give some thanks to folks. Um, I want to
thank JT for sharing his wisdom with me
throughout the program and keeping our
project on track. Um, and for staying up
late now from Poland to hear this. Uh,
my fellow scholars, especially Janelle
and Kujo for sharing compute with me.
Um, and everyone that gave me feedback
throughout the process and program. Um,
especially Danny and Mo and a shout-out

[00:11]
to OpenAI for making all of this
possible.
Great. So, now I'll answer some
questions that I have here.
Uh, I have a question that says uh which
model architecture was used to transfer
learning across models? Um, and also
which one was trained from scratch? So,
the model architecture that I used is
the same like GPT GPT uh transformer.
So, which is a decoder-only uh
transformer.
Um,
see.
Um, I have a question that says how
would you extrapolate what kinds of
gains from pre-training you'd get for
models smaller or larger than you've
been training or from smaller and larger
data sets?
Um, so I think you would just be able to

[00:12]
can see the similar trends um that we
saw in my previous slides uh for the
different uh data set sizes. And I think
as you as I saw, the main takeaway is
that if you have a large uh pre-training
data uh fine-tuning data set, um it may
uh
uh you're not going to get as many gains
as you would get from a much smaller
fine-tuning data set.
Um, another question is
how is my setup related to the scaling
laws for transfer paper by Danny
Hernandez from earlier this year? Um, so
a lot of my work is super inspired by uh
Danny's experiments there. Uh, so I did
the same type of uh experimentation
where I was changing the data set size
as I was varying the model sizes um and
as I was comparing for uh the loss
between those.

[00:13]
Um, I had a question this last question
that says uh did you consider transfer
between other types of languages, say
programming languages? Um, and I would
actually say that you should check out
the uh scaling laws for transfer paper
because that actually does look into how
does English transfer to Python. Um,
um
So, I got another question that says uh
did you get a chance to study
performance on metrics other than loss?
Um, and I didn't, but I'd be kind of
curious to see how you could
characterize this on uh downstream tasks
and I think that's like a pretty big
thing to uh look at for transfer
learning in particular.

[00:14]
Uh, there was a question that says would
you like to use a different tokenizer in
the future? And uh yeah, definitely. I
think being using the train tokenizer on
the specific languages would get you
much better results um and therefore
probably much cleaner uh graphs.
Um, another question that says was there
any reason you decided not to train
models smaller than 2 million
parameters? Um, not particularly. Uh,
just thought much much smaller models
than that would result in uh
losses that weren't maybe that
interesting to look at since we'd be
parameter limited um very quickly.
Awesome. So, I think that's all my time.
Um, so I'm going to pass it off to
Danielle who's going to be presenting
her project.

</details>
