<!-- source: https://academy.openai.com/public/clubs/champions-ecqup/videos/workflow-clip-proactively-monitor-accounts-with-codex-2026-06-12 -->

[Champions](/en/public/clubs/champions-ecqup/overview)

[navigation.content](/en/public/clubs/champions-ecqup/content)

Sign in or Join the community to continue

Get Started

# Workflow clip: Proactively monitor accounts with Codex

Posted Jun 12, 2026 | Views 79

# Codex for Work

# Activators

# Use Cases

Share

## SUMMARY

Yash Pahade (AI Success Engineer, OpenAI) demonstrates a Codex-powered account briefing workflow that brings daily account context, recent activity, next touches, approved sources, and metrics into one reviewable page for the team. The clip shows both the workflow output and the Codex automation approach behind it.

+ Read More

## TRANSCRIPT

00:00:00-00:00:53 | Yash Pahade:
So what you're looking at right here is kind of a demo version of the pages for my customers that I have. So you can see right here, I call it a command center, where the customer name, let's just call it Acme for today.
Usually I start by wanting to get a good understanding of what's changed in the last day since I last refreshed this page. So really getting a good understanding of what the state of the account is, if there are any support items, like if our customers had any feedback for us on any of our channels, or if they've written any tickets, if there's anything related to scheduling, upcoming meetings, or recent meetings.
And then also metrics as well too, in terms of where they are with usage of our AI tooling like ChatGPT, how many weekly active users they have, what's changed, etc. Now you can see right here, I'm starting to kind of build up a lot of this context on our Notion page. So I have things like recent activity, kind of going deeper into the higher-level stuff.

00:00:56-00:01:03 | Kenna Valdez:
One moment, Yash, before you dive in. Is it possible to get your screen share and the text a little bit bigger, just so folks can see a little more clearly?

00:01:03-00:01:06 | Yash Pahade:
Oh, of course. Sorry about that. Is this clear?

00:01:06-00:01:13 | Kenna Valdez:
Thank you. Let us know in chat with a thumbs up.

00:01:13-00:06:07 | Yash Pahade:
Okay, great. So yeah, you can see right here, I'm keeping track of things like recent activity with the customer, so some of the most latest touch points with them. Some of the points that are just all of this is generated with Codex.

I'm also looking at things like next touch points, right? Based off of recent meetings we've had, based off of recent conversations, what are the next things that I need to do? I'm also keeping track of things like meetings, so which ones I have upcoming for the week or that have already happened. So something that happened earlier this week, for example, on June 10, I have information like if this was an internal meeting or external meeting, what the meeting title was, and then just some notes that came out of that session. All of this populated with Codex.

And then the interesting part is metrics as well too. So I'm keeping track of things like total ARR, how they're using our API, what that trend has looked like as well, weekly active users, seats filled, etc.
One thing I did want to point out that I think was pretty interesting is that when you're using tools like Codex, there are limitations with what Codex has access to based off of the tooling that they're interacting with. For example, Notion doesn't really give you access to their API for charting. So Codex actually intuitively knew this and built out some very, very basic charting using things like ASCII. So you can see right here, it's a simple visualization. It's nothing too crazy, but gives me a really good idea in terms of trends. You can see a growing trend right here. Here's one too.

So it intuitively knows a lot of these things and picks it up, of course with some prompting of mine as well too, but I got a lot of this to work pretty much off the first iteration of this command center. You can see right here, we're scrolling down, there's some more metrics here as well. And it will also share some of the data that it's using to help put this together, which I've linked here. It looks like it's not here for this specific one, but you can get a good idea.

Again, going deeper into some of these metrics and some of the things it's visualizing on a weekly snapshot basis. And a lot of these things it's actually pulling from some of our own internal data sources. So as an AI success engineer, I don't have to spend a lot of time writing complex SQL queries, running them every day. This just happens automatically.
I'm just going to go through some of these. Something else interesting as well is recent cases. Codex is basically able to pull some of the ongoing cases, like tickets, into this dashboard as well too, so it has full access to read that once you've hooked it up. And it can be a really useful way for me to keep track of what tickets are in progress, what are some blockers, what's been closed recently, and kind of avoids having me context switch between multiple tools.

Yeah, even something as simple as a to-do, this can get automatically updated based off of Slack activity, emails, documentation, call transcripts, etc. Something I can manually change as well too. And you can even have it remove certain to-do items if I change it from status in progress to done, for example.

Something else that I find really interesting and particularly helpful is news around some of my accounts, especially when you work with products that are maybe a little bit more in the public eye or more consumer-facing. There are a lot of useful information that I would want to be aware of and would have to maybe go through some news websites, sources like CNBC, Reddit, etc. All this is pulled automatically using Codex, and it just searches the web and can pull whatever information it thinks is relevant for me. So if there's a newer initiative, I can talk to my customers about that, talk about how they're thinking about building new products that they've talked about publicly, and how I can help support that.

And finally, I just have all of my different sources of data kind of aggregated right here. So like docs, Gong calls, things like what use cases they're building towards, some of the stakeholders as well so that I'm aware of who's on our side, who's on their side, operating sources, and then just backstage data as well too.

So you can see right here a pretty simple snapshot. Gives me a really good idea and something I can just quickly scan through every day to know where things are at. And this will get automatically updated every day. And I can kind of switch gears and show you how we're doing that. Before I do that, did we want to stop for questions?

00:06:07-00:06:10 | Kenna Valdez:
I think we do have one question, and I know that this was something that Codex sort of initiated a little bit unexpectedly.

00:06:10-00:06:15 | Yash Pahade:
Sure.

00:06:15-00:06:30 | Kenna Valdez:
In your first run-through of this. But it is about the visuals. So do you have any tips on guiding that formatting or the sort of end state of what those visuals could look like when Codex builds them?

00:06:30-00:07:48 | Yash Pahade:
Sure. Yeah, I'm assuming by visuals you're talking about some of the metrics right here. Generally, when it comes to prompting Codex, there's a little bit of feedback and a little bit of back and forth involved. Sometimes for me, it'll happen on the first shot. Otherwise I'll give it examples of what I would like for it to look like as well.

When it comes to charting, I could say, hey, I'd have a preference for bar charts or horizontal charts or pie charts. And it also depends on the tool as well too. I think with Notion, we don't have access to charting capability specifically, or Codex doesn't, because that's gated behind, I believe, an API endpoint.

But depending on the tool you're using, you might be able to get even more granular with the way you're describing it. Now for the overall core structure of this, this all comes down to really prompting and having a conversation with Codex back and forth. This is really an iterative process.

So once something gets outputted onto Notion, I can kind of go back and forth and say, hey, these are the sections I want. These are sections I don't want. I prefer this to be a table versus maybe just bullet points. And then also with some of the charting right here, I'd prefer for this to be a line graph or a horizontal bar chart like Ed mentioned before.

00:07:48-00:08:31 | Kenna Valdez:
Completely agree. I think you hit two really good points that have definitely been my experience as well, as the iteration is okay. So if you need to kind of take additional steps to describe your preferences, it's okay to have that back and forth with Codex to get to where you want to go, and sharing examples.

You mentioned a couple, but sometimes I'll just screenshot another example of a dashboard and sort of following what I want the format to look like. And Codex can be really great at using visual examples that you give it to create something more in alignment with what you want. And I know that iteration has been a big part of the build of this automation for you. So I want to let you go on to the build.

00:08:31-00:11:42 | Yash Pahade:
Yeah, definitely. And I think that is a pretty good segue to go into the build itself. Basically, when you're building out automations with Codex, there's different ways to do it. I think the easiest way, and the way that I found to be the most effective, is basically opening up a chat with Codex and describing the automation you want.

So I'll start with a really, really simple prompt saying, hey, here are all the different data sources I have, and I would like some sort of a command center view or a daily pulse on what's happening with these different accounts. As you're kind of going back and forth with it, Codex will actually iterate and build on top of this automation.

As you can see right here, we have this automations tab. This is the actual automation itself, and it's going to start populating these instructions. I haven't actually written any of these instructions myself. This is what Codex is gauging based off of the back-and-forth conversation between me and Codex on the actual chat window.

So you can see right here, it gets a good idea of, like, okay, update the Notion command center, and it's linked to that Notion page that was created. And then talking a little bit more about the actual section or structures of that page as well too. So daily pulse, recent activity, calendar, etc. Going a little bit deeper into what each of those different sections are as well, so going into the daily workflows as well.
So it basically takes a lot of the different points that I've given it and the instructions I've given it, saying things like, hey, make sure that you check my Google Drive, that you check all the last channels on the Slack channels as well, just to prevent hallucination and guardrails to it. I'll even have it check some specific Slack DMs. Sometimes we talk in groups. Sometimes it's with me and another team member or a customer. It'll make sure to read context from that as well too.

So really, it'll kind of formulate what the structure is, what the workflow is. And then, based off of that, I can either ask it a lot of questions if I see it making mistakes, like, hey, where are you getting this information from? Or I can actually read through the instructions myself and get a good understanding of what Codex has told it to do specifically and what adjustments I need to make accordingly.
So you can see right here, it's from the daily workflow itself, all of the different steps that it takes every day in order to basically build out that entire page. You can see it's a lot of instructions because I've had a lot of back and forth with it. But for the most part, it does a pretty good job of reading this document over and over again and making adjustments based off of the feedback, and just based off of some of the feedback that I've given in general.

And it's consistently evolving. It's an iterative process. So these things will continue to improve. I still think there's room for improvement with this, and I get a lot of feedback from my other team members as well, in terms of things that they would like to see in this, because it's a source of truth for the entire team that supports this account.

+ Read More

Sign in or Join the community

![OpenAI Academy](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/OpenAI-black-monoblossom-743de6c6-b680-4334-8cd5-fee30f7a2202-1739890376705.png?fit=scale-down&width=100)

Create an account

1

## Watch More

[30:00](/en/public/videos/make-work-flow-proactively-monitor-accounts-with-codex-2026-06-12)

[Make Work Flow: Proactively monitor accounts with Codex](/en/public/videos/make-work-flow-proactively-monitor-accounts-with-codex-2026-06-12)

Posted Jun 12, 2026 | Views 79

# Codex for Work

# Activators

# Use Cases

[13:00](/en/public/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

[Workflow clip: Automate CRM updates with Codex](/en/public/videos/httpsvimeocom1202596507sharecopyandflsvandfeci)

Posted Jun 18, 2026 | Views 56

# Codex for Work

# Use Cases

# Activators

[3:00](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

[Confidence scoring and skill hardening with Codex](/en/public/videos/confidence-scoring-and-skill-hardening-with-codex-2026-06-18)

Posted Jun 18, 2026 | Views 89

# Codex

# champions

# AI Techniques
