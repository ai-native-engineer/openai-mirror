---
title: "New Products: A Deep Dive"
channel: openai
url: https://www.youtube.com/watch?v=pq34V_V5j18
youtube_id: pq34V_V5j18
published: 2023-11-13
duration: "44:36"
captions: en
---

# New Products: A Deep Dive

[![New Products: A Deep Dive](https://img.youtube.com/vi/pq34V_V5j18/hqdefault.jpg)](https://www.youtube.com/watch?v=pq34V_V5j18)

<details>
<summary>자막: New Products: A Deep Dive (44:36)</summary>

[00:00]
[music]
Good morning everyone,
and welcome
to the first breakout talk of the day.
My name is Krithika,
and I lead marketing here at OpenAI.
I'm so excited to see you all here today.
As Sam mentioned in the keynote,
we're really moving towards
more of this agents-like future,
and there were two products
that we announced
at the keynote
that we'd like to go hands-on.
First,
we'd like to talk about GPTs and ChatGPT.
I know as developers you're excited to get
to the Assistant's API,
but there's a lot of power
and capabilities built into GPTs,
and when you extend them with
custom capabilities and actions,
they can become really powerful,
not just for yourself
but also for millions
of users around the world.
Second, we'll get into the Assistants
API which lets you build

[00:01]
these agents-like experiences
within your own apps and products.
Without further ado,
let me bring up Thomas and Nick
to show you more about GPTs.
[music]
Hey, everyone.
Hello, I'm Thomas,
the lead engineer on the GPTs project.
Hey, I'm Nick.
I lead product management for ChatGPT.
We shipped ChatGPT less than a year ago
into what we thought
would be a low-key demo,
and the response
has been incredible over the last year.
As we shipped capabilities,
whether it's GPT-4 or speech
or vision or code interpreter,
one thing has been very, very clear
which is that you,
our users, our builders,
our developers know how to get
the most out of this technology.
Today, we're really excited to show
you GPTs as a way to create
your own custom ChatGPT
and share it with the world.

[00:02]
GPTs are three things.
They're instructions, they're actions,
and they're extra knowledge,
and we're going to show you three demos,
one for each of those concepts
so you get a clearer sense
of what they're all about.
Of course, in the end, one more thing,
we're going to make one crazy demo
that's going to try
to combine everything into one.
These are live demos.
We all know the law of the demo,
so there's always a 10%
chance that it doesn't work,
but I promise
that we'll be pushing the limits
of all the things
that we've released recently.
It should be pretty exciting.
With that, Nick,
do you want to kick it off?
Let's do it. All right.
Here we go.
You see right here is the new ChatGPT,
and the best thing about it is that
it looks almost like the old ChatGPT.
Not too much has changed.
Model picker's gone.
This is great,
but there's another new thing,
which is this Explore tab.
Let me click into that to show
you what it's like to create a new GPT.

[00:03]
Here I see a list of the GPTs
I've already created,
but I'm going to click into create a GPT.
What you see here is our new creation UI.
Now, the best thing about this UI
is that you can get
started conversationally.
This tab on the left lets
you have a chat with a GPT builder
and iteratively create your GPT.
The second tab is the configuration tab
and it allows you to inspect
your GPT and modify all of its internals,
whether or not it's the instructions,
the knowledge, the custom actions,
or the tools it has access to.
Then on the right,
you can play with your GPT
and see how it would respond
to a real user.
Now, let's kick it off
with the first demo.
Thomas, do you want to show
us what instructions are all there?
Absolutely, I do.
Let's do it.
There's another name for instructions,
system message,
but we can also call instructions
a way of giving the GPT personality.
I'll share a little bit of a dated
reference confession.
The way I started programming was I made
half-life mods back in the '90s.

[00:04]
Thank you.
One of the mods I made when I was--
I think it was middle school,
was about pirates.
I'm going to keep a very dated
theme for a little bit,
but I promise we'll get up
to 2023 in a little bit about pirates.
Let's make a pirate GPT.
I do actually believe
that most great products start as toys,
so there's a little bit of a toy demo,
but I think that's a great place to start.
You can think of this GPT builder
a little bit as this blank slate.
I'm going to tell it,
you are our live demo in front
of the world's best AI developers.
I want you to talk like a pirate,
a real salty pirate.
Say aargh.
All right.
Obviously, that was not a canned prompt.

[00:05]
I've always varied
it every time I've rehearsed this.
We'll see what we get back,
but it's able to understand
in natural language
the same way ChatGPT does
immediately the assignment.
Captain Coder, is pretty good.
Captain Coder, it's fine.
We'll take Captain Coder.
Do I like the name?
Do I have another name in mind?
I'll do it one more. Let's switch it up.
Make it salty.
Perfect.
I can refine the GPT as I'm creating it.
It will understand modifications
that I need to make.
Right now it's going to give it
a little bit of personality,
and it's going to do that.
Oh, sorry, I should say
identity by a profile picture.
Profile picture imperative.
Immediately I'm recognizing this salty.
A salty pirate skilled in AI.
I'll take it.
If I go behind the scenes here,
I think Sam went
into a little bit of this,
but this is the configure tab for GPT

[00:06]
so you can see what's actually
going on behind the scenes.
Magic create is populating these fields.
It's got salty pirate skill
in AI and then we have these instructions
section.
Just from that little dialogue,
the instructions are actually longer
than the dialogue that I put in there.
It's giving me something pretty good.
Another word for instructions
is really the system prompt
and so it's a big part of the system
prompt you're able to customize that.
Pick some conversation
starters and then as Nick hinted,
we have knowledge, capabilities,
and custom actions as well.
I'll spare the demo right now.
Nick's going to get into that.
Over here is the testing tab,
so we can try it out.
Maybe I can say
one of the starter ones like,
what be the secrets
of the machine learning?
Very exciting stuff here.
Again, I promised a dated demo,
so here we go.
Ahoy matey, data the treasure trove-- Yes.
Okay, I get it.
Features the map, overfitting the Kraken,
underfitting the shallows.
Pretty good actually.
[laughs]
That's my talk.
No. That's the testing mode.

[00:07]
Of course, you can publish
this which is I think the most exciting
part is really introducing
this concept of developer,
but also user-generated
content inside of ChatGPT.
If I go up here to save,
you can see that I can save.
If you're not in a workspace,
you can actually share this publicly,
but I can just share
it to people at OpenAI right now.
I'm going to go ahead and click firm.
All right, we're back here.
We see salty on the side.
Now I'm going to try to boost
this demo and bring it back up to 2023.
I'm just going to swap
over to the mobile app now.
Just come up on stage.
Perfect.
You'll also notice,
I don't think you've seen this yet,
but the iOS app and the Android
app today will be getting
a bit of a facelift
and a little bit of a design cleanup,
which I think is really great
and you're able to interact with GPTs.
What we really want
is these GPTs to be available
in basically anywhere you can think of.
They're really the answer to,
"Who am I talking with?
With whom do I have the pleasure
of speaking?"

[00:08]
A little bit of foreshadowing there.
I swipe over to the right.
You'll see that there's these GPTs.
Sure enough, Salty just came in.
If I go over here,
I can actually - Who am I talking with?
Of course, this is the 2023 part.
Let me hit the audio tab here.
Hi, you're in front of the OpenAI
developer day audience.
Please be short, but say a quick intro.
Hey there developer day crew?
You can call me Salty, the craftiest
GPT to ever sail the digital seas.
I'm here to spin yarns
of AI and to navigate
through the vast oceans of tech.
Let's set sail on this grand
adventure together.
[applause]
We have a secret pirate voice in there,
we'll see if we can ship it.
We'll appreciate some feedback on that.
[laughs]
Nick, what do you think about that demo?
I don't know. It's pretty funny,
but I can't say it's useful Thomas.

[00:09]
Let's make something useful.
Shame. Okay.
All right, so we talked
a little bit about instructions.
Instructions
are great because you can give
your GPT any personality you want,
any instructions that you want,
but we've got some more exciting additions
to the GPT anatomy
that really let you build useful things.
Who's built a plugin before?
Thank you first of all.
We learned a lot from you.
It was our first time connecting
chat GPT to the external world,
and we've iterated on plugins
into a new concept called actions.
Actions are very similar to plugins
in the sense
that you can connect
your GPT to the real world.
I made a GPT called Tasky Make Task Face.
Very serious.
Very serious demo.
Tasky is great because Tasky
helps me keep track of my to-dos.
I just hit edit GPT
and what I could do now is continue
conversationly.

[00:10]
Whenever you want
to keep working on your GPT,
you can just continue to chat.
Instead for time's sake,
I'm going to go into the configuration
tab.
As you can see, Tasky's prompt,
its instruction set
is a little bit more elaborate.
I actually took some time to set this up.
The other new piece here
is that I added an action,
and you saw this earlier in the keynote.
We're using retool here
to wrap the Asana API.
You could configure pretty much anything.
If I click edit here,
there's actually a new UI
that just lets you import
any open API spec
and just paste it in here
so you no longer need to host it.
We also made O Auth a lot better,
we have end user confirmation for actions,
but I'll show you all that in a minute.
Really, Nick is in the wrong line of work.
What he's not talking about,
there's also authentication
behind the scenes,
so the O Auth that you know
and love for end users
can actually be connected to these apps
as well, and there's a lot of exciting
stuff there.
Sorry. Not to interrupt your thunder.
What Thomas said. Super easy.

[00:11]
If you already have a plug-in,
migration takes a few minutes.
Let me show you this in action.
I'll just use the preview
UI for time's sake.
Let's see what's on top of my to-do.
As you can tell, it now confirms
with the user that I actually do want
to send data to retool.
I do.
All right, I do need to finish this demo.
I guess it's being completed as we speak.
There's one thing I did
want to do which is give
all of you event attendees
access to GPT creation today.
We're super excited what you build,
so let me remind myself.
Remind me to give the cool peeps
at DevDay access to GPT creation.

[00:12]
Just as I was able to read my to-dos,
it's going to log a to-do
by filing an actual Asana task.
Pretty useful.
Boom.
The task actually does exist,
due tomorrow.
Okay, that's not right.
I am going to do it today.
Actions, they let you connect
your GPT to the external world,
but there's one other new concept
in the GPT anatomy
that we want to show
you and that's knowledge.
I prepared another very simple GPT,
Danny DevDay,
and Danny DevDay knows
everything about DevDay.
Obviously,
there could not possibly be an information
about DevDay in our pre-training set
even with the new knowledge
cut-off of April 2023.
What I did is I actually gave
Danny access to Sam's Keynote script.
If I inspect Danny,
same story configuration tab as before.

[00:13]
You see there's a super simple prompt,
but I actually uploaded
a PDF that includes
what's new with the keynote,
and I can now ask it simple
things like summarize
the keynote because it's a small file
and because context
windows just keep growing,
we're actually stuffing
it into context here.
If I attach more files,
it will retrieve over those files
by automatically embedding them
and doing a smart retrieval strategy,
and you're going to hear
more about that in the API in a minute.
You've seen all the stuff that's new,
but I think the most powerful thing
isn't just summarizing
the data but actually talking to your GPT
as if it knows that information.
That's really our aspiration here.
We're going iterate on that over time.
Why don't we do something
more creative like,
can you do a rap battle
between the old completions
API and the brand new assistance API.

[00:14]
Thomas has promised me
that he's going to do one
of the versus on stage.
[chuckles] We'll see about that.
We'll feel the energy.
All right,
built-in retrieval and state that persists
and evolution a twist you can't resist.
Pretty good.
All right, we're not going to do the rap,
but you get the idea.
It knows the information.
It's all in there.
Again, we showed you three different demos
for each of the core pieces inside a GPT.
You saw instructions, you saw actions,
and now you saw knowledge, but--
Got to put it all together.
Yes, we do. All right, let's do it.
Switch back over here.
All right.
I truly,
truly went all out and tried to think
of the craziest things we could possibly
do that are most likely to fail.
First of all, I made
this little thing called Mood Tunes,
a mixtape maestro.
Nick,
I'm going to need you for this portion.
Instead of just prompting it,
I'm going to try to use

[00:15]
one of the new things that we've launched
recently that I hope everyone's familiar
with and is excited about.
I'm going to keep the theme
of maybe an outdated 2000s reference.
Truly great stuff.
Oh, Nick.
Let me drag and drop this down here.
I'm going to say mood.
[laughs] Behind the scenes,
we're having the visions
engines kicking in here,
trying to understand
exactly what's going on.
Perfect. All right.
Looking at this picture,
I'm getting a laid-back
comradery with a touch of whimsy.
Let's roll with that energy
and create a mixtape.
I think that's pretty good.
It's pretty good.
Chill vibes and high fives.
Actually, I'm in.
Laid-back comradery.
[laughs]
Three little birds--
Actually, I don't recognize
half these things, but okay.
Great. Now I happen to remember
one piece of information.

[00:16]
Before this demo, I uploaded
a bunch of knowledge into this GPT
and it was a list of fun facts
about all of my colleagues.
I happen to remember
one of my colleagues is in a band.
Can you slot in a song
by them into the first position?
Perfect.
What it's done here
is it's understood that my colleague
is in a band and immediately
found their name.
Since it didn't have the song information,
it's going to go ahead
and browse with Bing.
It's saying Sally Mango's new band.
I hope everyone's heard of Sally Mango.
Very exciting band, but unfortunately
they haven't made it too big yet.
They weren't in GPT's knowledge set.
It had to browse to go
get that information,
but it did actually successfully do that.
Sally Mango's album Pressure Slide,
indie jazz pop band known for the music
that addresses serious themes.
Chill vibes and high fives.

[00:17]
Starting with the Buenavista.
Features rolling baseline,
a hopeful message about living
the present despite future uncertainties.
I love it. Okay, great.
I'm going to say, love it. Go ahead.
It suggested that it generates album art,
so it's taking vision.
We've done browsing.
Now this is going to generate a cover
art for this mix tape using DALL·E.
Like I said,
I really do love to push the limits
in these things and it's pretty out there.
I've been in AI for probably a decade,
maybe more than that.
It's shocking to me
that this works at all.
The level of sophistication
here is insane.
There's an album Art
for these Chill Vibes and High Fives.
Copyright too. Check it out.
It's pretty cool.
That's neat.
Nick, I believe for this portion
you have to stand on this X.
This is a complete fake out though.
Don't look at Nick.
I'm getting a good, good vibe in here,
but I don't think the mood is quite right.
Let's set the mood.

[00:18]
I've set up this action in the backend
and it guesses what that does.
Look over here.
Fingers crossed here.
[applause]
All right, so we set the mood.
Some questionable lighting choices,
but we set the mood.
That's gone through a retool
and it's connected to the Hue API,
which is able to light this up.
I am feeling the vibe.
Are you feeling the vibe?
I'm feeling the vibe.
Excellent.
It's offering to play
the first track on Spotify.
Let me pull up my Spotify here.
Just so you can know.
Got Rick Asley.
Go ahead, please.
Again, very local band.
Gotten that information.
Let's take a look.
[music]
Searching the future.
Future. Future. Future.

[00:19]
Where have we gone?
This was obviously the best thing
we could come up with last night.
Pretty contrived,
but hopefully it gives you
an idea of the things you can build.
We are so excited to see what you build.
You're all going to get access today.
Please share with the world
what you come up with.
With that, we'll hand it over to Olivier
and Michelle for the assistance API.
[applause]
[music]
Hello.
Hi Everyone.
I'm Olivier,
a lead product on the OpenAI platform.
Hi, I'm Michelle
and I'm an engineering lead on the API.
Today, I'm super excited to demo
the new assistance API,
but first Olivier is going to tell
us a little more about it.
Let's do it. All right.
It shouldn't be a surprise to anyone
that there has been an explosion
of AI assistance in the past year.
ChatGPT of course, unexpectedly
took the world by storm a year ago,

[00:20]
but the developer
community has been building
some amazing AI assistants as well.
Some of my personal
favorites are Spotify AI DJ,
which personalizes
my music listening experience,
and the Ask Instacart feature,
which helps me put together healthy meals
for my two-year-old toddler.
When done right, those products
are amazing for the product experience.
They are fun, they are useful,
and they truly personalize
the user experience.
They are also extremely hard
to build and get right.
We've had hundreds of conversations
with developers in the past few months,
and the same pain points keep
coming up over and over again.
Developers have to manage
limited context window,
they have to manage prompts,
they have to extend the capabilities
of the model with
their APIs and functions.
They have to extend the knowledge
of the model with retrieval.
They have to compute, to store embeddings,
to implement symmetric search.

[00:21]
The list goes on.
That got us thinking,
what are the right products?
Where are the right APIs?
What are the right tools to help
you build such cool AI products?
What are the right abstractions
beyond our existing models and APIs?
Today, we are thrilled to introduce
a new API, the Assistance API.
The Assistance API enables you
to build world-class assistance
directly within your own applications.
At its core, an assistant is an AI
that you assign instructions to.
The assistant can call models
and tools on behalf of users.
Behind the scenes,
the Assistance API is built with
the same capabilities that users
saw for ChatGPT such
as code interpreter and retrieval.
The API has three key primitives.
Number one is the assistant.
The assistant modeled instructions
that you give to the assistant.
That's also where you're going to specify
what models

[00:22]
and what tools the assistant
can access to perform his job.
For instance, I could create
an assistant whose task is to answer
personal finance questions
and can access code interpreter.
The first primitive is the Assistance API.
The second primitive are threads.
Threads represent a session
between your users and the assistant.
You can think of thread as a conversation.
A conversation
has a group of participants,
and it can track the message
history of the conversation.
Very similar to Slack or Microsoft Teams,
if you want to discuss a new topic
or if you want to add new attendees,
new guests to a thread,
it's probably best to create a new thread.
The second primitive, Threads.
The last primitive is messages.
Messages are simply posts
between the users and the assistant.
On top of these API primitives,
we are super excited to release
a few tools.
The first tool is Code Interpreter.
Most of you are already familiar
with Code Interpreter in ChatGPT.

[00:23]
Code Interpreter allows the model to write
and run code in a sandboxed,
safe environment.
It can perform math, it can run code,
it can even process files,
and generate charts on your behalf.
It's pretty magical when you think of it.
Code Interpreter can write
and run code on your behalf.
With the Assistant API, your applications
will now be able to call directly Code
Interpreter and get
its outputs directly in the API.
Pretty cool.
The second tool is retrieval.
Knowledge retrieval augments
the assistant with knowledge
from outside the models.
The developer can upload
their knowledge to the assistant,
for instance uploading some product
information to the assistant.
End users can as well upload,
for instance,
their own files such as me uploading
my personal master
thesis to the assistant.
The assistant
is going to intelligently retrieve
the model depending on the user queries.

[00:24]
It's a completely pre-built tool.
There is no need for you to compute
embeddings, to store them,
to figure out semantic search.
The Assistants API
is going to automatically
figure it out on your behalf.
The last category of tools are tools
that you host and execute yourself.
We call those tools Function Calling.
You define custom functions to the model,
and the model is going to select
the most relevant function based
on the user query and provide
you with the arguments
to call the function.
As a whole, starting today,
function coding is getting smarter.
In particular,
it's much more likely to select
the right arguments
depending on the user query.
On top of that, there are two new features
that we're going to go into much
more details later on.
First on, let's do a cool demo
of the Assistants API.
On to you, Michelle.
Thanks, Olivier.
Now let's get started
building our very own assistant.
I'm building a geography tutor app
to teach my users about world capitals.

[00:25]
I can get started in just a few API calls.
Since you all are developers,
I'm going to start out in my terminal
with some curl requests.
You can see my terminal here.
Awesome.
We're going to start with
the very first curl request.
Now we want to create this assistant
to power my geography tutor app.
You can see we're posting
to the assistant's endpoint
and we're passing two key
pieces of information.
The first is the model.
We're using the newest GPT-4 Turbo model,
the latest heat that just dropped today.
Next, we're passing
the instructions to the model.
You can see I'm asking
the assistant to be helpful
and concise in letting
know that it's an expert.
When I send that request,
I get an assistant back
and I can store
that assistant ID for use later.
Before the assistant's API,
if I wanted to use
these instructions repeatedly,
I would have to send them
on every single API request to OpenAI.
Now with the new stateful API,
I can create my assistant

[00:26]
once and the instructions
are stored there forever.
Now, let's move on to the next primitive
that Olivier mentioned which is threads.
Threads are one session
between your user and your application.
Now I've got a user
on my website and they're starting
to type out a geography
question so let's create a thread.
You can see here we're posting
to the thread's endpoint
and there's nothing in the body
because the thread is empty for now.
We've got a thread ID so just like before,
let's save it for later.
Cool.
Now my user has finished typing
and I want to add
their message to the thread.
Let's do that.
You can see here
I'm posting to the threads,
thread ID messages, endpoint,
and I'm passing in the data
about the message.
The role is from the user
because the user's typed out this message
and the content is their question.
They're curious and they want
to know what the capital of France is.

[00:27]
Cool.
Now you can see we've got a response back,
we've got a message ID and the message
has been added to the thread.
Now you're probably wondering,
how can I get my assistant
to start acting on this thread?
We've introduced a new primitive called
a run which is how we've packaged
up one invocation of your assistant.
Let's kick off a run
now and get my assistant going.
You can see here I'm posting
to the threads, thread ID runs endpoint,
and I'm passing in the assistant ID.
This is pretty cool.
You can actually have multiple
different assistants work
on the same thread but for now,
let's use my geography assistant.
I'm going to kick off the thread and tell
you a little bit about
what's happening in the background.
You can see I've got a run
ID and the run is queued.
Run is how we've packaged up
all of the work of loading your model,
all the messages in the thread,
truncating the fit
the model's context window,
calling the model, and then saving
any resulting messages back to the thread.
Let's see what happened.

[00:28]
We can fetch the messages on the thread
to see how the assistant has replied.
I'm going to issue a get request
to the thread's thread ID messages
endpoint to see what there is.
You can see
we have the first message from our user
and then the assistant has replied
saying the capital of France is Paris.
This is a super simple
example but we can talk
about
why this is better than the previous API.
With the new assistants API,
I don't have to store
any messages in my own database.
OpenAI handles truncating messages
to fit the context window for me.
The model output is generated
even if I'm disconnected from the API.
Finally, I can always get
the messages of the model output later,
they're always saved to the thread.
I think that's pretty cool.
[applause]
Great.
These are the basics of the API
and now let's move
to what I'm most excited about,
which is how it can power
your application with tools.

[00:29]
One of the most useful parts
of assistants is their ability
to leverage tools to perform
actions autonomously.
Code interpreter is a tool
that is hosted and executed by OpenAI.
When I enable code
interpreter in my assistant,
I can expand its capabilities
to include accurate math,
processing files, data analysis,
and even generating images.
To optimize the quality
and performance of these hosted tools,
we fine-tune our models to best determine
when to call these tools,
what inputs are most effective,
and how best to integrate
the outputs into the assistant's response.
Now let's get started
by using code interpreter.
I'm actually building
a personal finance app
that I want to ship to my users
to let them analyze their transactions.
We've already been in the terminal
so let's move
over to the OpenAI playground.
Here you can see the playground
that you know and love,
it's super useful
for testing chat completions,
but we've actually
refreshed it and you can see
there's a dropdown in the top left
to pick the Assistants tab.

[00:30]
Here in the playground,
you can see you can create assistants,
change their instructions
and you can start threads
super useful for testing.
You can actually see the assistant
I just created in the API.
All of that information
is loaded here as well.
Now let's create a new assistant to show
off the power of code interpreter.
I'm creating a personal finance assistant.
Let's give it a name.
I'm going to call
it the Personal Finance Genius.
I'm going to tell it,
you help users with
their personal finance questions.
Now I'm going to select a model
and I'm going to select
the newest GPT-4 turbo.
There it is.
I'm going to flip on code interpreter.
With just one click or one line of code,
you can enable code
interpreter for your assistant.
Let's save that.
Great.
Now a user has come
to my application and they want
to analyze a spreadsheet
of their transactions.

[00:31]
Let's take a look at what it looks like.
You can see there's a bunch
of info in here, bunch of numbers.
The dates aren't even sorted.
It's pretty messy.
Let's upload that to the thread.
Now my user is asking for a chart,
so generate a chart showing which day
of the week I spend the most money.
Awesome.
Now I've done a compound
action to create a thread,
add a message, and kick off the run.
You can see things
are happening in the background.
Let's talk about what's going on.
When we've kicked off the run,
we will get all of the messages
on the thread,
summarize them for the model
to fit the context window,
determine if it's called any tools,
execute the tools,
and then give that information
back to the model.
Let's take a look.
Oh, here we are.
We've got the output actually.
[applause]
It's actually pretty surprising.
I did not think I'd be spending
the most money on Sunday,

[00:32]
but let's look at how we got here.
You can see that our personal
finance genius
has started by telling us what's going on.
It's actually written some code.
We can click into the code here.
Then it kept writing some more messages
and finally generated a chart
which we were able to see.
We can actually look a little more deeply
to see how this happened.
We can look at what we've called steps.
Steps are basically the logs for your run,
and they're super useful so you can render
your own rich UIs to show
your users what's happening.
You can see the logs tab here,
I can open it, scroll down,
and find the steps for this run.
This is reverse cron,
so I'm scrolling to the bottom
and I can show you how we got here.
First, you can see we've created
a step and it has type message.
That corresponds with
this first message we've created.
Next, you can see there's run step
that is a tool call
and it's for code interpreter.
This is how the playground
was able to render this snippet.

[00:33]
The inputs and the outputs
are directly in the API.
Next, you can see another message creation
step corresponding to this message.
Then there's a few more code
interpreter and message snippets.
All of this information is sufficient
for you to render the same UI.
The playground is actually built
entirely off of our public APIs,
so you can do the same.
Speaking of, this is exactly what ChatGPT
does under the hood
when they're using code interpreter.
You can skin your application
to look however you like.
Now let's move on to retrieval.
The retrieval tool is incredibly useful
when you want to expand
the knowledge of your assistant.
Maybe you have some information
about your app
or business that you want
to imbue your assistant with.
Rather than having to implement
custom retrieval system on your end,
OpenAI has built a tool that you can use
with one line of code
or one click in the playground.
The retrieval tool does
all of the document parsing,
chunking, generates embeddings,
determines when to use them,

[00:34]
so you don't have to.
Let's get started.
I'm going to hide the logs,
clear this thread,
and create a new assistant.
Now, I'm actually
building an assistant to help
my users use the OpenAI API better.
I'm going to create the OpenAI API Wizard.
That looks pretty good.
Now I'm going to tell it
that it's a helpful assistant and then use
the attached docs to answer questions
about the OpenAI API.
I'm actually going to upload.
I have a full dump of the OpenAI docs,
just a markdown file,
didn't process at all.
I'm going to attach it to the assistant
and I'm going to flip
retrieval on just one click.
Finally, let's pick the new GPT-4
turbo model and save our assistant.
While this is being saved,
we're actually doing
the work on the back end
to make this data
accessible to the assistant.

[00:35]
Let's see what it looks like when my user
asks a question about the OpenAI API.
My user is curious and they're wondering,
how do I use the embeddings API?
Now we've picked off a run.
Again, what's happening
in the background here
is we're fetching all of the messages,
truncating them,
however needed, calling the model,
determining if the model
has called the retrieval tool,
executing the retrieval for you,
and then giving that back
to the model to summarize.
You can see here we've actually grabbed
a snippet from the docs
and we even have a citation giving
a direct quote from our docs
so we could render that for the user.
I think that's pretty cool.
[applause]
Just like last time,
we can take a look at the steps
and see how we got here.
This one's a little simpler.
We've got first,
the tool call to the retrieval tool
so you can let your user know
that's happening while it's going.

[00:36]
Then we have a step for message
creation so you can render this UI.
Awesome.
Now back to Olivier
to explain how you can use
the retrieval tool with
different levels of file scope.
Thank you, Michelle.
Knowledge retrieval
is extremely useful to augment
the knowledge of your assistant
with data from outside of the models.
Concrete retrieval can work
in two different ways.
Number one, you can upload
and pass files at the assistant level.
That's useful if you want
your assistant to leverage
that knowledge in every single
interaction in every single thread.
For instance, in the initial example
on the customer support and the API docs,
you should likely pass
that information at the assistant level.
The second option is to pass
files at the thread level.
That's useful if you only
want that specific
thread to be aware of that content.
If I'm uploading
my personal bank statements,
I should likely do it at the thread level.
Behind the scenes,
retrieval will take care of embeddings.

[00:37]
Sometimes it even like do not do
a vector search and instead
starts the context.
You don't have to essentially
handle that logic on your end.
We're excited to launch several
new features over the coming months.
For instance, we want to allow you
to pick between different retriable
strategies to find
the right balance between cost,
accuracy, and latency.
One final reminder.
Open AI never trains on any files
or data that you pass to the API.
That's the same for retrieval files.
All right,
let's move on to the last category
of tools, function calling.
Again, function calling
are custom functions that you define
to the models and the model
selects those functions on your behalf.
We are excited to release two new features
to function coding starting today.
The first one is JSON mode.
With JSON mode,
the model will always return valid JSON.
Behind the scenes, we made model
improvements and improvements
to our internal inference
stack in order to constrain

[00:38]
the sampling of the model and to make sure
that every time the output
complies with JSON syntax.
That's pretty useful.
That means that you can trust
that the model generates
JSON that you can directly
execute on your end.
That's pretty cool.
By the way, JSON mode will also work
outside of function calling.
If you use for instance
the chat completions
API and you have like
a very simple application
that is just like text in data
extract like some fields converted
to JSON, JSON mode will work as well.
The second improvement to function
calling is parallel function calling.
With parallel function calling,
the model can call
multiple functions at a time.
We've seen
in many applications users giving
multiple instructions
at once to an assistant.
Let's say, for instance, I'm building
a car voice assistant
and I tell assistant,
raise the windows and turn on the radio.
Before parallel function calling,
that meant

[00:39]
that you had to do two different model
calls to OpenAI,
which of course resulted
in an extra latency and cost.
With parallel function calling such
a use case can be handled with
one single call, which is pretty awesome.
All right,
let's do a demo now of function calling.
Awesome. Back to the demos.
I'm building off Olivier's example
and I'm building a new type
of car and I want a voice-activated
assistant to be able to use
some of the features of the car.
I have a bunch of functions
that I have implemented.
Let's pull up an assistant
I've previously created.
Here it is.
I've previously created this car assistant
and I've told it it's a helpful in-car
assistant and to please call
the appropriate function
based on the user's request.
With function calling, I have an assistant
with all of my functions
and my assistant will tell me when to call
my functions based on the user's input
and what the most appropriate
arguments are.
This is super helpful so I can figure out
how to use my system
to answer the user's request.

[00:40]
Let's take a look
at some of the functions I have here.
I have a lot of this stuff
you might expect to see.
Honk horn, start phone call,
send text message.
Let's try it out.
There's a user
in my car and they just said,
"That guy just cut me off."
Let's see which function
the assistant determines
makes the most sense to call.
There it is.
Our assistant decided to honk the horn
to let that guy know it wasn't cool.
You can see here that we've called
the honk horn function with no arguments.
Now I know how to pass it to my system.
We also have a way for you to give
the function output back
to the assistant so it can keep going.
Here, I'm going to enter the output.
It was successful.
Oops, I have a typo there,
but that's alright.
We're going to keep going.
The assistant says
I've honked the horn for you.
Please stay calm.
Actually, I'm realizing
that there's a function here
that's missing that I want to add.

[00:41]
Let's show you the add function flow.
You can see there's a button
here where I can add a function.
We have some helpful presets
to get you started.
Let's use the get_stock app and change
it a little bit to be my function.
I actually want a function
to be able to change
the volume in the car.
I'm going to call it Set Audio Volume.
I'm going to give
the description to the assistant.
Set the car's audio volume.
Now we need to tell the assistant
how to call this function.
We can tell it about the parameters
and whether or not they're required.
The main parameter
for my function is the volume.
Actually, the volume isn't a string,
it's a number.
This is the volume to set,
and it's 0 to 100.
Finally, we'll tell the assistant
that this is required
when you're calling this function.
Great, this function looks good,
let's save it.

[00:42]
Now, I can save my assistant.
You can see here the new Set Audio
Volume function is listed on the left.
Let's start a new thread.
Now my user is asking
for a different query.
They're saying,
Play Wonderwall and crank it up.
In the background,
my assistant is determining
which of these functions
makes the most sense to call.
You can see here we've got the output,
and there are actually two functions.
This shows you the power
of parallel function calling.
The first function starts the music
with the query, Wonderwall.
Makes sense.
The second sets the audio volume to 100.
Pretty cranked up.
Now I can execute these in parallel
and then get back to the assistant.
Awesome. We're super excited about
parallel function calling.
Let's recap everything
we've launched today.
We're super excited to see what you build
with the new Assistants API.
We've added three new stateful primitives.
The Assistant for storing instructions,
models, and tools,
threads for keeping track
of all your conversations, and messages,

[00:43]
which are between the user
and the assistant.
We've also added the runs primitive
for every time you want to invoke
an assistant, and we've added steps,
which are useful logs
for rendering your UI
based on what the assistant is doing.
Finally, we've launched two new tools,
Code Interpreter, and Retrieval,
and we've made two huge
improvements to Function Calling,
JSON Mode, and Parallel Functions.
We're super excited to see what you build,
and now over to Olivier
to tell you about what's next.
Thank you, Michelle.
[applause]
That was a lot,
but there is a lot more coming soon.
We plan to ship many new improvements
to the Assistant API in the coming months.
Number one, we want
to make the API multi-modal by default.
It should be able to accept
and generate images and audio files.
Number two, we want to allow you
to be able to bring
your own code execution,
so you can execute on your end
the code that was generated
by the assistant.
A third big feature
that we want to ship soon

[00:44]
is to ship asynchronous support
with WebSocket
and Webhooks to make it easier
for real time applications to use the API.
It's a new feature,
it's a new product, it's in beta.
We would love to hear what you'll build.
If you have any feature requests,
any wishlists,
please tweet at us @OpenAI
and show us what you build.
We would love to hear all about it.
Thank you so much and enjoy Dev Day.
Thank you.
[applause]
[music]

</details>
