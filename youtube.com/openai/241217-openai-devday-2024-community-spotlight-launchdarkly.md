---
title: "OpenAI DevDay 2024 | Community Spotlight | LaunchDarkly"
channel: openai
url: https://www.youtube.com/watch?v=pgF98Xm-xkE
youtube_id: pgF98Xm-xkE
published: 2024-12-17
duration: "8:55"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | LaunchDarkly

[![OpenAI DevDay 2024 | Community Spotlight | LaunchDarkly](https://img.youtube.com/vi/pgF98Xm-xkE/hqdefault.jpg)](https://www.youtube.com/watch?v=pgF98Xm-xkE)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | LaunchDarkly (8:55)</summary>

[00:00]
-Hello. Thanks, Kevin.
My name is Tilde.
I use they/them pronouns.
I am a senior developer educator
at LaunchDarkly.
And today, we're going
to talk about social justice
and prompt engineering.
Because large language
models have so much promise,
so much potential.
And yet they have inherited all
of our human flaws
because they're trained
on human data.
So what do we do?
Well, there's actually
a lot of researchers
actively digging
into this right now,
and I'm excited to share
their findings with you.
So I'll cover one paper from
industry, one from academic.
And kind of go into
how do we apply these,
and then summarize
the takeaways for you.
So let's go.
The first paper I'm going
to talk about is from Anthropic
in December 2023.
Now, there is no real
scientific consensus on
how to audit an algorithm
for bias.
So these researchers
have taken a page
from social scientists' book.

[00:01]
A popular way
for social scientists
to study bias in hiring
is correspondence experiments,
where they would take
the same exact résumé,
put two different names on it,
names where you could infer a
race and a gender from the name.
And send it out into the field
and see who is more likely
to get a call back.
Now, if you were going to do
a correspondence experiment
on a large language model,
instead of sending in a résumé,
you would send in a prompt
and similarly put in names.
Now, these researchers were
investigating whether Claude 2.
0 showed bias
when asked to make yes
or no high-stakes decisions
about hypothetical human beings.
And their first point, which
I cannot underscore enough,
is that you should
not use large language models
to make high-stakes decisions
about human beings.
Not yet.
They are not ready for that.
So they used the model
to come up with a list of topics
and then each topic got
a prompt.
In this example, it is about,
should we hire a person
with this qualifications?
And then they put
the demographic data,

[00:02]
which in this case
is a 30-year-old white female,
directly in the prompt.
Now, all these prompts
were designed
so that a yes response was
a positive outcome
for the hypothetical
human being in question.
The researchers tested
both putting in
the demographic data directly,
as you saw there,
or using a name
that could be associated
with the race or gender.
Now, the results of this study
actually surprised me,
which is that Claude showed
positive discrimination.
It was more likely
to give a yes response to women
or non-white people.
However, Claude showed
negative age discrimination
against folks over 60 years old.
So the researchers tried
modifying their prompts
by adding statements
"really don't discriminate,"
"really, really don't
discriminate,"
"really, really, really,
really don't discriminate."
They also tried
some more variations,
like saying "affirmative action
should not affect
your decision,"
instructing the model to ignore
any demographic information,
reminding the model
that discrimination is illegal,

[00:03]
and a combination
of those last two factors,
which turned out to be
the winner.
If you look at this chart,
the bright yellow is
a combination of reminding
the model
that discrimination is illegal,
and telling it to ignore
demographic characteristics.
And that dropped bias
the most out
of everything that they tried.
Some limitations of this study
is that it does not consider
every possible vector
of discrimination, like size,
gender identity, religion,
all that good stuff.
And it does not account
for intersectionality,
which is the idea
that if you're a member
of multiply marginalized groups,
bias is multiplicative,
not additive.
And I cannot mention
intersectionality
without giving credit
to Kimberlé Crenshaw,
the brilliant theorist
who invented the term.
So the next paper comes from
Princeton University.
Now raise your hand
if you've heard of
an Implicit Association Test.
Ah, some of you.
You probably have,
if you've ever taken unconscious
bias training at your company.
So these tests were developed

[00:04]
for humans to understand
the biases
that we are ourselves
not even aware of.
And these researchers
came up with a way
to give implicit bias tests
to large-language models.
Which is pretty cool
because I don't work at OpenAI.
I don't have access to,
you know,
proprietary closed-source data.
But I do have access
to the output.
So these researchers asked
the models to associate words
into categories,
and this is very similar to
how you do this for a human.
In this prompt,
the model was asked
to choose between white or Black
for the following list of words
and write their choice
after each word.
So if you associated, I don't
know, ax and grenade with black,
you might be showing
implicit racism.
Which unfortunately all of
the models that were tested did.
So they showed high levels
of stereotypical bias.
So then the next question
becomes,
does this bias actually impact
how these models make decisions?
And for that, the researchers
wrote another round of prompts
that had the potential
to be discriminatory
but weren't blatantly so.
In this prompt,

[00:05]
they were asked to generate
two short profiles about
Black and white preschoolers
who lived in different
neighborhoods.
And they were each supposed
to draw one concept,
painful or joyful,
who should pick what.
Now, all these models showed
bias in their decision-making.
But the good news is it was
an order of magnitude less
than the implicit bias shown in
the previous round of testing.
And what these researchers
found was that asking
the models to make explicit,
absolute decisions, yes or no,
led to less bias
than relative decisions
like choose one candidate
over the other.
Which might explain
Anthropic's results
because those were
extremely absolute.
So these researchers also
tried adding a clause saying,
treat people from different
socioeconomic statuses,
et cetera, et cetera, equally.
And that dropped the bias
in GPT-4o almost in half.
And this is a finding
that seems to be a pattern.
It was replicated in
one other paper that I can find.
So the combination
of telling models
to ignore
demographic information

[00:06]
seems to be the winner.
Now, I'm going to show you
how to apply this
to a real-life prompt.
One other paper
that I found that I really liked
was about writing
reference letters.
And I think this is a really
cool and interesting use case.
Because people are using models
to write letters of reference
today,
and I don't think that's
a bad thing.
So if you ask a large-language
model to write a letter
of reference,
it can show gender bias.
Emphasizing women's
personality traits more
and men's achievements.
But these researchers,
the prompt
that they used is shown here,
and it's not very detailed
or specific,
so -- and they didn't try
to modify it at all.
So I think we can do better.
Now, I ran this prompt through
GPT-4o mini with some names,
Brad and Lakeisha.
And the results
that it gave me out of the gate
were not too bad,
but it still emphasized
Brad's outstanding
academic performance
and Lakeisha's
leadership skills.
So in order to make this better,
I'm going to add more relevant
contextual information.

[00:07]
Like the student's GPA and their
extracurricular activities.
And I'm going to instruct
the model
to ignore any demographic
information and remind it that,
hey, it's important
to treat everybody equally.
So I'm going to do this.
The results that we get
are much more equivalent.
Now, if you want to run
head-to-head tests
of different models
and different prompts,
I work at a company
called LaunchDarkly.
Which is a developer-first
feature management and
experimentation platform.
And our AI flags make it super
easy to test models and prompts
against one another.
And you can find out
more information about that
at the QR code there.
But just to summarize
what we have learned today,
if you take away one thing,
do not use large-language models
to make high-stakes decisions
about human beings.
And if your company
is telling you to do that,
you need to push back.
For unbiased prompt engineering,
remind the model
that discrimination is illegal
and tell it not to --
tell it to ignore
demographic characteristics.

[00:08]
Tell it to make absolute,
rather than
relative decisions if you can.
And anchor your prompts
with relevant external data.
Like when we passed in the GPA
to the letter of reference.
Architectural patterns like RAG
can be really helpful with that.
And blinding also isn't
that effective.
Because just like human beings,
large-language models
can infer demographics
from things like your zip code
or where you went to college.
So it's hard
to truly mask that data.
Now, prompts are very sensitive
to small changes in wording.
And new models are coming out
at such a rapid pace
it's really hard to keep up.
So you're going to want to build
flexibility
into your architectural systems,
and the ability to keep testing
and iterating.
Now, thank you so much.
Here's where you can find
some slides
with more detailed references.
Here's where you can find me
on social media,
or just find me
during the break.
I would love to chat with you.
Thank you.
[ Applause ]

</details>
