---
title: "Semantic Parsing English to GraphQL | Andre Carerra | OpenAI Scholars Demo Day 2020"
channel: openai
url: https://www.youtube.com/watch?v=liMJS5DrnlQ
youtube_id: liMJS5DrnlQ
published: 2020-07-09
duration: "23:29"
captions: en-orig
---

# Semantic Parsing English to GraphQL | Andre Carerra | OpenAI Scholars Demo Day 2020

[![Semantic Parsing English to GraphQL | Andre Carerra | OpenAI Scholars Demo Day 2020](https://img.youtube.com/vi/liMJS5DrnlQ/hqdefault.jpg)](https://www.youtube.com/watch?v=liMJS5DrnlQ)

<details>
<summary>자막: Semantic Parsing English to GraphQL | Andre Carerra | OpenAI Scholars Demo Day 2020 (23:29)</summary>

[00:00]
So, I'd like to talk about semantic
parsing of English to GraphQL.
So, first of all, a little bit about
GraphQL for those that don't have too
much of a background.
GraphQL is basically a query language
for your API.
This compare This can be compared to
SQL, which is a query language to to
databases.
GraphQL can cover a whole API, which
means it can cover a broad set of
business logic, databases, and data
types.
Um one of one of the strengths of
GraphQL is its ease of developer use.
It lends itself well to nested
relations. It provides a schema, which
serves as an API contract, and and it
makes It can make the the development
experience for for software engineers a
little bit easier.
So, here,
we can see a little bit about what
GraphQL looks like.
Um GraphQL lets you describe your data

[00:01]
in a schema. So, and here you have a
small example of that. It can show you
the relationships between different
types of data.
With that schema, we can send a query,
and that query
can give us a predictable result of
exactly what we expect to receive from
from this interface.
Semantic parsing is the task of
converting a natural language utterance
to a logical logical form,
the machine understandable
representation of its meaning.
In this case, we're converting English
natural language
to
GraphQL, which is the logical form or
the machine understandable machine
understandable representation of its
meaning.
So, here, we can see a little bit more
of what this looks like. So, for
example, if you have some English
prompt, and I
natural language, such as what is the
name and date of the song released most

[00:02]
recently?
And some GraphQL schema that defines
that data,
we can find the corresponding GraphQL
query
such as this.
So, why did I want to go through this
project? Um there's a few reasons.
The first of which is I wanted to
understand the limits of general
language models for semantic parsing. Uh
this task is a little bit similar to
machine translation where and we take
some
um input language and output a target
language. In our case, we're inputting
English and outputting uh GraphQL.
Uh I wanted to see how it could
potentially ease the learning curve for
developers. So, if a developer has the
ability to interact with a
with a model that generates queries for
them so that they can see what these
queries how these queries are
structured, it might make it easier for
them.
And finally,
the this could be a potential tooling
for non-technical data users. Uh so, an

[00:03]
example of this would be a a manager
that uses Salesforce. Um instead of
reaching out to an engineer to for them
to generate a custom query, uh they
could type it out in natural
English and
uh they would be able to get a response.
So, previously there has been some work
into semantic parsing um over a broad
range of languages and domains.
Um
for my specific use case, I was really
interested to see what the SQL um data
sets looked like.
Um as you can see here, there's several
SQL data sets uh that have a broad range
of different domains and different uh
query complexities.
Of these, the one that stood out the
most and I'll cover why in a second is
Spider.
The The The was that there is no GraphQL
data sets. So, I wanted to train a model
to to learn and to to create GraphQL.

[00:04]
Um and that would be very difficult
without a GraphQL data set.
So, I looked into Spider specifically.
So, Spider is semantic parsing of of
natural language text to SQL.
It has In the data set, it has 10,000
questions, around 5,000 unique complex
SQL queries.
Uh covering 200 different databases with
138 different domains.
So, these
each of these um queries
in the Sorry, in the corpus between the
train and test or validation data sets,
there are different queries and
different databases. So, for a system to
perform well, it must generalize to new
queries and new database schemas and new
questions. Um which is a difficult task
to cover.
This specific uh task uh has been
tackled for the last few years and has
achieved pretty good results. So, here

[00:05]
on this slide, you can see what the top
five um ranking leaders in the exact
match accuracy look like.
And so, on the testing set, um
we can see there's around 60% accuracy
on this SQL Spider task.
So, for my task, uh
I had to be able to create a GraphQL
data set. And so, this Spider data set
served as a great starting point.
Uh first off was
being able to convert SQL to GraphQL. I
started out not even being able to know
if I could if this was possible. Um and
so, it was
it took a little bit of time to just
understand what the tools were and what
I could use to accomplish this this
first task.
The two two very important tools that I
used were Hasura and PG Loader. Hasura
just generates a GraphQL schema based

[00:06]
off of a database and PG Loader
converted SQLite to Postgres
and that allowed me to use Hasura on top
of it.
Then the bulk of the work was converting
SQL abstract syntax trees to GraphQL
abstract syntax trees.
Um and I'll cover what that is right
now.
So, here's a simple example of a SQL
abstract syntax tree to a GraphQL
abstract syntax tree.
On the left side we see SQL. So, the
query right here is select count star
from songs.
So, we have we take this query, we parse
it into a tree and like I said before
this is a very simple example. Then this
tree is then converted to a GraphQL tree
as you can see on the right side.
Then that tree is just converted to a
raw GraphQL query.
Part of generating the data sets um
required the use of validation scripts
and so there was a few things I looked
out for in these validation scripts. So,

[00:07]
when I was verifying this data sets, I
covered the syntax um making sure that
the queries that were formed were actual
GraphQL queries. Uh also
covered validated the syntax against the
schema so making sure that the keywords
that were used in the queries itself um
were valid for the schema that we were
looking at.
And then I executed those queries
against endpoints and make sure that
they um
were valid.
So,
what this resulted in this whole process
resulted in is that um
half of the queries were transferred
around half of the queries.
So, the big problem here the big
obstacle was that Hasura doesn't include
a group by clause. So, group by is a is
a clause that's used very often in SQL,
and the server didn't have a good way to
transfer that over. I mean, this could
have been done manually, but I wouldn't
have been able to do that within the
limit the time limits of the program.
Um but in the end, I was very confident

[00:08]
because of the validation script and
data set.
Um so,
diving into the details, this looks like
160 schemas across 138 different
domains,
uh around 4,300 unique English prompts,
and around 2,400
unique GraphQL queries.
So, after that, the next step was
um experimenting on the data set and
seeing what kind of results I could get.
Uh I experimented with a few different
models. The ones that stood out the most
were BART and T5.
So, these are um two different models
where um that other researchers from
different research groups have come up
with. Both of them are encoder-decoder
um transformer models.
And they're very similar.
Where they vary though is that BART is a
bidirectional encoder,
um but both of them are encoder-decoder
models.
And lend themselves very well to
translation tasks. So, I thought they
could lend themselves well to my task as

[00:09]
well.
So,
as I mentioned before, it the the
process looks a little bit like this.
So, we input a
an English prompt. So, in this case,
what is the name and date of the song
released most recently,
concatenated with the
GraphQL schema. So, it would look a
little bit like the what you see on the
left here.
That is passed through to our model T5,
and then
our output {slash} target
um is this GraphQL query we see on the
right here. And this is just done with
an auto-regressive objective.
Part of this uh required the use of a
validation metric to make sure that my
results looked what I like what I
expected them to look like. So, in this
case our I wanted my outputs to look
like my targets. Um the validation
metric that I came up with was exactly
matching exact set matching accuracy.
What this means is that since I could

[00:10]
parse my GraphQL queries, the the target
and the output into abstract syntax
tree, I could compare those two queries
to see how accurate they were.
Um and so since in in these abstract
syntax trees, the order of the of the
children's the children nodes don't
matter.
Um so two trees with a different order
of child nodes could be equivalent. So,
for example, um
we see these these two little trees
right here where on the left side we
have a green um a green child node and
then on the right side we have a right
green child node. And these two are
equivalent queries and so we want I
wanted to make sure that this validation
um metric could be able to handle for
that.
And so a good example of this would be
in this in this query here, um the song
name and release date could be switched,
but the query would still be equivalent.
So, what did the results look like? Um

[00:11]
I with these two models uh specifically
using T5, which performed the best, I
got 46 to 50% exact set matching
accuracy
on the GraphQL validation data data set.
Um this is in comparison to the 20% uh
SQL exact set matching accuracy that I
got with this with these same models. Uh
and this is an interesting result for a
couple of reasons. Um this range of 46
to 50%
is actually the same model, but the 46%
model
um was just trained on the graph QL
queries. The 50% model was trained on
the graph QL queries and the SQL
queries, and for some reason it was able
to perform better. Um my guess is that
that was able to happen because the
model learned what's important what
keywords were important between schemas.
And as I mentioned before, this uh the
existing spider um

[00:12]
uh
best models um got around 65%
exact match accuracy, as we can see
here.
So, why did my model perform worse on
these?
Um and this is because these models
that are in the leaderboard here
uh used specific architecture that was
specific only to SQL. So, these models
here can only produce SQL. They wouldn't
be able to produce graph QL as well.
Uh whereas my model was also able able
to produce SQL and graph QL.
And so, this sets it up for future work
where um we could see potential uses
where we could find a way to increase
the accuracy of both of them.
Um
and maybe even across different query
languages as well.
As I mentioned before, the data set
since this data set was based on the
spider data set, the for a model to
perform well, um it must be able to
generalize well over new schemas and new

[00:13]
questions and queries.
And so, to me a 50% uh accuracy
says that the model is able to
generalize these results pretty well.
Um what I forgot to mention a little bit
earlier is that this exact set matching
accuracy is more of a lower bound
because there are multiple queries that
could um display the same information,
um but it's a little bit more difficult
to be able to parse those trees as well.
So, what does this look like? It'll be
helpful to see it working action.
So, here
we have
a database that we're using. So, this
database is called music one, which has
information about different music genres
and artists.
And we can ask a question such as, "What
is the country of the artist named
Enrique?"
So, here we generate a GraphQL query
as we can see below
on the left side, and then we can send
that query to server
and get a response. And so, here we see

[00:14]
that our response looks like this. And
the answer to the question is the
country is USA.
Here's another example. Um
and this shows that the model is able to
generalize to a different database. So,
here there's the 160 different
databases.
Um and instead of selecting music one,
we're going to look at flight two, which
has information about uh different
airlines and flights.
So, now we ask a new question, "Give the
airline with the abbreviation UAL."
We generate a GraphQL query,
and we send that query and get a
response. And this case it says, "United
Airlines."
Um and so, this is just a small example
of of what it can do.
Um
In the future, um
the the next in the next couple of days,
I want to release these models and code
so that everybody's free to use them and
improve them.

[00:15]
Um I've been working on a paper
constantly to submit to archive, and
within this next week I'll I'll be
submitting that as well.
And then, uh a little bit longer term, a
couple more tasks. So, one of them is to
add more examples to take advantage of
GraphQL. Um
these examples only take advantage of
the more simple aspects of GraphQL, but
um it wouldn't be too difficult to add
more complex examples.
And um
another another task is to test on an
enterprise schema.
Um so Salesforce and GitHub both have
GraphQL APIs.
And so I'd like to see what kind of
results I could get by um
um semantic parsing English to these
GraphQL endpoints.
And so I just wanted to say thanks um
specifically to a few communities and
people. So um I want to thank OpenAI for
the opportunity to be part of the
Scholars Program. I've learned a lot and
I've and from from the people at OpenAI

[00:16]
and I and I enjoyed having the
flexibility to work on on this project
as well.
Um also thanks to Hugging Face and
PyTorch Lightning communities. Uh they
made themselves very available to me to
ask any questions on how to use their
tooling.
And then I wanted to think think my
mentor Melanie uh for taking the time to
work with me. And as Sam said um
it did feel more like somebody working
with me and and getting through the more
difficult parts of of getting into the
field.
Wanted to thank also Christina and
Mariah. They they were in charge of of
the Scholars Program and and were very
helpful and made themselves very
available to to all of the the Scholars
um whenever we needed any help. And also
just wanted to thank uh my wife Noel
who has been very
supportive throughout this whole
program.
And now I'll open it up for any
questions
that um

[00:17]
I can see here on the Q&A.
So first results or first question, are
your results using models trained from
scratch or using fine-tuned
uh or using fine-tuning pre-trained
models? Also, what are the model sizes?
So yeah, good question. So, the models
that I was using
um were pre-trained on large corpuses
and and and and the case of T5, for
example,
um it was trained on a corpus that was
uh generated from the internet. Um and
so, it learned a lot about language in
general. Uh so,
what I did is fine-tuned those specific
models um
for my specific task um
in a couple of different ways, but the
main one was converting English to
GraphQL.
And the model sizes, um
so, these models weren't extremely big.
I was able to fit both models onto the

[00:18]
GPUs that I could um run on Google
Colab. So, Google Colab gives around 16
GB of memory for these models.
So, I was able to run those perfectly
fine on there um with some smaller batch
sizes. Um so, anybody should be able to
do that with a Google with a Google
account using Google Colab.
And
the second question is how often does
this model generate syntactically
invalid outputs? That's a good question,
as well. So,
um
from the So, as I mentioned before, in
the validation metric, that validation
metric also covers metric or also covers
examples that are not valid. And so, any
example that is invalid would be counted
as wrong, right? And so, 50% means that
50% were valid and um
the correct query that I expected. And
so, 50% And that also means that 50%
were probably not. Um but that's So, the

[00:19]
the upper bound of how many
um
syntactically invalid outputs would be
50%, but in practice, when I looked at
it, it tended to be a lot smaller than
that. It was
I would say something like
5% of the outputs were syntactically
invalid. Um
and that's because this model has the
flexibility to output different types of
query languages.
And next question by Mariah is, "What is
the most challenging What was the most
challenging part of the project?" And I
think most challenging part was
definitely converting those uh SQL
queries to GraphQL queries. Um
it was a lot So, it was a lot of
parsing. It was a lot of using trees and
graphs to figure out what the right
GraphQL query would be. So, all in all
that that process probably took a month
by itself to to work out. Um and at the
very beginning, I didn't even know if it
was possible, but it as we realized

[00:20]
about half of the queries were possible
to transfer over.
See,
there's a any more.
Yes, okay, I have another question from
Alec Radford.
"Do you think general-purpose
architectures like T5 are sufficient, or
is there still a need for
domain-specific architectures like the
specific SQL-specific ones you
mentioned?" Yeah, I've been thinking
about this question, actually, and I
think um
I think it depends on on the difficulty
um because
there is a difference between a model
that is
where the whole model architecture is
specifically tied to SQL,
and a model where just the output heads
are tied to SQL.
So, if we could um and this could be
future future work, obviously, if we
could
replace the SQL head just and just the
SQL head and and put a GraphQL head on

[00:21]
there, that would be that would be
great. Um but obviously this is this
lends itself to to the time required to
to create those heads. Um but I think we
need to do we probably need to explore
both a little bit better
um and compare them. And so I think
that's a good
place to look in the future.
See.
And the next question is how often is
the model generate syntactically invalid
outputs? I already covered that um
probably around 5% of the time.
And what's the main metric you've used
for evaluating your model?
Um yeah, that's the the metric I
mentioned previously, which is the exact
set matching accuracy. So I would
the I would basically work work this way
and convert the GraphQL queries into

[00:22]
um abstract syntax trees and then
compare two trees to each other and that
way I could evaluate my model throughout
every epic.
And then from Christina,
uh
really cool work. How do you imagine the
model architecture to differ for GraphQL
as opposed to SQL?
Is the problem space different in any
way?
So
yes, the
the model architecture I feel like most
of the model could remain the same
because the these general um
architectures that we as we seen with
other examples, they're able to
we can use them for translation tasks,
for task generation, for classification,
different things like that. Um so I I
feel like my intuition is that well
where the will work will go is in
preparing the right types of heads.
And what that requires is is just

[00:23]
somebody who understands um
how to um basically output these
abstract syntax trees directly.
Um
So, I think I I think that though that
these general models will be able to
if as long as the general architecture
or in other words the the middle part of
the model is able to understand the
English that the these models will be
able to perform well.

</details>
