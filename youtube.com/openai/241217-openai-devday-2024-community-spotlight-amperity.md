---
title: "OpenAI DevDay 2024 | Community Spotlight | Amperity"
channel: openai
url: https://www.youtube.com/watch?v=JCh30k5ZXzo
youtube_id: JCh30k5ZXzo
published: 2024-12-17
duration: "8:31"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | Amperity

[![OpenAI DevDay 2024 | Community Spotlight | Amperity](https://img.youtube.com/vi/JCh30k5ZXzo/hqdefault.jpg)](https://www.youtube.com/watch?v=JCh30k5ZXzo)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Amperity (8:31)</summary>

[00:00]
[ Applause ]
-Thanks so much, Kevin,
for the warm welcome.
We're Joyce and Camden
from Amperity.
Amperity is a
customer data cloud.
We unify and centralize
customer data for many
of the world's largest brands.
And today we're going to
be talking about
how we've built on top
of OpenAI's models
to help brands make sense
of their really complex
customer data.
We're going to start off today
with our friend Lauren,
who's a marketer at Acme Retail.
We're heading into the holidays.
It's a time of the year
where brands are really focused
on customer retention.
And Lauren has a
really simple question.
She wants to know how many
high-value customers do I have?
It turns out, though,
this question is
deceptively difficult to answer.
Why is this actually so hard?
There are a couple reasons.
The first one is data
is really siloed.
Acme Retail has a POS system.
It has a legacy POS system.
It has an e-comm system.

[00:01]
Each of those systems
has different customer IDs.
Customers might have used
different email addresses,
names, physical addresses.
It's really hard
to even figure out
how much a customer has spent
at Acme Retail.
This is somewhere
Amperity could help.
However,
even once the data is unified,
Acme Retail might have hundreds
of different database tables.
They could have
a loyalty database table,
a predicted value table,
a transaction table.
And unless Lauren is actually
in this data day in and day out,
it could be really hard
for her to know where to start.
And not on top of that,
but to be able to meaningfully
interact with your data,
you need to know SQL.
To solve this challenge,
we built AmpAI.
AmpAI is a natural language
to SQL tool specifically geared
towards non-technical users.
It enables brands
to build visualizations
and also customize the output
by encoding their unique rules
about their customers.
That's somewhere we'll spend
a little less time today.
But if you want to learn more,
please find us after.

[00:02]
If we were just building
AmpAI for Acme Retail,
it actually might
not be too hard.
Context windows are getting
larger and larger.
You could imagine we
might pull in all
of the schema information.
We might pull in table samples.
We might pull in example
questions and results
that we've returned.
And we might be
able to create this
pretty easily using
relatively naive methods
given the increased size
of context windows.
However, when you take
into account
that AmpAI has to work for
a financial institution
who wants to understand
who's signing up for home loans,
when it needs to work for
an airline
who's trying to learn more about
credit card sign-up trends,
when it needs to work for
a B2C brand
that wants to learn
about ad performance,
this becomes
a really challenging problem.
All in all, AmpAI needs to work
across hundreds of brands
that Amperity serves,
and more than five verticals.
The main challenge we encounter
here is one of context.

[00:03]
In order for AmpAI
to answer a user's question
and create the SQL
from natural language,
it needs to have information
around the database tables,
the fields,
the values within those fields.
And this is really hard
when you take into account
that there's hundreds
of different types
of non-standard schema AmpAI
must operate over.
And also the data
could be changing by the day.
I'm going to turn things
over to Camden
to dive into our approach
to context management
and some of our considerations
along the way.
-Thanks, Joyce.
When we started building AmpAI,
we knew we had to be resilient
to many different types
of schemas across our
different brands and verticals.
And so we needed --
we knew that we needed
a RAG approach
in order to make this work.
But instead of using
vector DBs or embeddings,
what we instead chose to do
was add two research steps
that happened prior to
the actual SQL generation step.
So we'll be using Lauren's
question,
how many high value customers
do I have,
as a guide to show
how we evolved our approach.

[00:04]
So the first step we took was,
sort of, a naive approach.
We take the user's
question in the database schema
and we pass it to a
SQL generation step with GPT-4o.
And then we pass that
to Amperity's
internal query engine
to run that SQL.
But for this specific user's
question,
how many high value customers
do I have?
We're not going to get
a great answer because
GPT-4o doesn't have the context
for what high value means
in the context of your business
or your brand.
So we needed --
knew we needed something more.
So our first approach here
was to say,
take an intermediate step
with GPT-4o
to rank the top five tables
and grab the samples
of those tables.
So this approach takes
the user's question
and the database schema,
passes it to GPT-4o
to rank the top five tables.
And which in this case will
include the Customer360 table
and the Unified Loyalty table.
Then we pass those to Amperity's
internal query engine
to get row samples
of those tables.
And we pass all of that context
to the generate and run SQL
steps that we had before.

[00:05]
But in this case, we're not
going to get the right answer.
And that's because
we want platinum and gold.
And in the samples
that we have above,
we only have bronze and gold
as part of the samples
that were passed
to the SQL generation step.
So this actually
isn't sufficient
for us to answer the question.
So we knew we needed
something more.
So we added another research
step on top of this,
which is to get
the distinct values
of the most important field.
So we pass the user's question
and the database schema
to another intermediate
GPT-4o step
that asks it to get
the most important field
across the entire
database schema.
This field should be "pclv tier"
in the table Customer360.
Then we pass that to Amperity's
internal query engine,
which gets the distinct values
for all that field
and samples them.
And then passes that along
with our previous research step
into the generate
and run SQL steps.
Now that we have
both platinum and gold
as part of the distinct values
that are passed to the final
generate and run SQL steps,
we have the final answer.

[00:06]
Which is that predicted customer
lifetime value tier should be
in gold and/or platinum.
And this is the right answer.
So here, as a summary,
is our full architecture.
We have two research steps
that we pass the user's
question and database schema to.
First, to rank the top
five tables
and get the row samples
from those tables.
Second, to get the
most important field
and sample distinct values
from those -- from that field.
And then pass all
of that context
onto the SQL generation step and
run that SQL inside of Amperity.
Now Joyce will do a demo of
how this looks inside
of the product.
-Okay.
Let's put a UI to a name.
We're going to ask
AmpAI two questions.
The first is, how many
high-value customers do I have?
And then the second is,
what products do they tend
to buy around holiday?
So under the hood here, there
are two tool calls running.
The distinct values tool call,
and also the tool call
to pull the row samples.
It's correctly pulled
in platinum and gold
from the predicted customer
lifetime value tier.
And we can see there are about
414,000 of these customers.
Next, I've asked what
the product revenue is.

[00:07]
This is challenging
because there's actually
10 different product taxonomies
that Acme Retail uses.
So it's pulling --
it's running the row samples
tool call under the hood.
And we can see
that it's correctly
pulled in product subcategory.
It's a little bit challenging
for me to parse these results.
So I'm now going to ask
another question,
which actually invokes
another tool call under the hood
to graph the results.
And soon we'll be able to see
that these high-value customers
tend to purchase shoes,
tops and tees,
and jeans around the holiday.
It's been absolutely incredible
to see the impact
that AmpAI has had on
our customers
and also Amperity's products.
The way we understand
product usage,
or one of the ways,
is by looking at the number
of queries
that customers run over
their data in Amperity.
Here, the yellow line represents
users who are using AmpAI.
The blue line represents those
who are not.
And over the last three months,
AmpAI has actually led
to 130% increase in the number

[00:08]
of queries run in Amperity.
So really dramatic impact
on our customers.
We covered one
technical challenge
we faced with AmpAI today,
which focused
on context management
and how we feed
the right context to GPT-4o.
There were many other challenges
we encountered as well.
Around evaluations,
around customization.
So if you would like to learn
more, please find us after.
Thank you so much.
[ Applause ]

</details>
