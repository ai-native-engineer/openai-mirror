---
title: "Codex in JetBrains IDEs"
channel: openai
url: https://www.youtube.com/watch?v=1XkVsE9-ZK4
youtube_id: 1XkVsE9-ZK4
published: 2026-01-22
duration: "9:48"
captions: en
---

# Codex in JetBrains IDEs

[![Codex in JetBrains IDEs](https://img.youtube.com/vi/1XkVsE9-ZK4/hqdefault.jpg)](https://www.youtube.com/watch?v=1XkVsE9-ZK4)

<details>
<summary>자막: Codex in JetBrains IDEs (9:48)</summary>

[00:00]
It's really important for us that Codex works anywhere you like to code.
For many of you, that place is your JetBrains IDE.
So we're super excited to announce that one of our most requested features is finally here.
Codex now works in JetBrains.
You can now collaborate with Codex directly within JetBrains IDEs
using your ChatGPT subscription, API key, or your JetBrains AI subscription.
And with me, I got Gleb from JetBrains,
who's going to give us a quick tour of Codex in JetBrains.
We know developers use our products on complex problems.
And that's where JetBrains and Codex really shine.
So I wanted to show you Codex's work on real projects inside my IDE.
It's a multi-platform Kotlin codebase for our conference.
It runs on mobile, web, and even desktop.
I'll show you how Codex helps with debugging and feature implementation
on that scale right within your IDE.
So let's start probably with the fact that you don't need to use JetBrains AI subscription to log into Codex.

[00:01]
You can use your ChatGPT account to log in or add the API key to do that.
So I'm going to log in in my Codex account, which is already done.
And then I want to, first of all, ask what this project is about, totally.
Totally, it makes sense.
Good way to start. So we can see Codex beginning to look at different files,
reading the file system. Exactly. Yeah. So it collects some context and understanding of what
does the project do. So as you can see, it's our Kotlin Conf app. By the way, you're welcome.
And so, yeah, it runs on Android, iOS, desktop, and web using the framework called Compose
multi-platform. So I will try to build this project right now to see how it actually looks like on iOS.
Cool. So this is compiling it for iOS and then

[00:02]
It compiles the project for iOS using Gradle technology. We're using the IntelliJ tools for
that. But as you can see, there are some errors, right? So, and I will probably need
to help of Codex to solve that.
So what I do is I'm just simply copy and pasting everything
that is read here and asking Codex to help me solving that.
So we can now see Codex is jumping through different tasks,
looking at the files that might be impacted based
on the stack trace.
Exactly.
And you see what exactly Codex does.
So it provides some reasoning on the certain actions that it does.
It shows the files that it's read and so on.
And this is the same Codex that I get when I run Codex CLI or if I use it in a different idea?
It is exactly the same Codex just because inside JetBrains we run evaluation to make sure the quality of CLI Codex is exactly the same as the one that users receive inside AI systems.

[00:03]
Amazing.
And it looks like it did some file changes here.
Yeah.
So actually, we can take a look on the exact changes
to make sure that they actually make sense.
You see the Codex has finished its work.
And we can try to build the project again, right?
Fingers crossed.
See if it builds.
These are just warnings, so it's not a problem.
And it builds.
All right.
Does it run?
Developers usually don't like dealing with the build issues,
and it's quite difficult to understand what exactly is happening
when the project is building.
So Codex does an amazing job understanding what exactly needs to be done here.
Yeah, we didn't really have to give it any guidance.

[00:04]
It just runs around and we figure things out.
We didn't even need to read through the errors that are here, right?
So, yeah, the app is working.
and now I guess it's time to give Codex a little bit more complex task, right?
We know that the biggest problem for all the mobile developers is localization, right?
So just because it's quite a mundane, complex task
that does not involve a lot of kind of visual changes,
but at the same time it is extremely important.
Probably the best task to give to an agent.
Sounds great.
I have a problem that I'm going to base here.
and I'm going to ask, create a localization to Spanish
for the conference app that we have.
Awesome. Let's fire it off.
While Codex is working, we still can oversee
what kind of files it looks at,

[00:05]
what kind of reasoning behind looking at these files.
When it runs the bash commands,
we can see what kind of commands it runs.
At the same time, so different developers have different tolerance towards what agent does, right?
And this is something that we consider inside our integration, where user can select different types of access modes to agent, right?
So we can restrict agent 2 from editing any file.
So it would be just read-only, extremely suitable for understanding complex code bases, or let's say search when a user just doesn't know where the certain file is located.
Agent mode allows to run commands, but at the same time it requires user approval for every command so that some quite sensitive commands would be user-reviewed.
And full access, which I currently have, actually allows agent to run any command they want, apart from the riskiest ones, and change the code files.

[00:06]
Awesome.
And then you can see, are you able to click on the actual files that it's checking out?
Yeah, so you can take a look at the file.
So it opens in IDE, so you can take a look at what exactly is written in this file
as the changes come.
That's awesome.
And I think one of the things that's interesting
is it looked like Codex was doing a lot of research
across the code base
so that if you have a complex code base,
it's going to go and first understand all the context
because we didn't give it any guidance, right?
We just sort of like say, here's the problem.
But now it's sort of like locked in
and it's just like hammering out code change after code change.
Exactly, exactly.
It's like you put a developer
that does not know a thing about this code base to a task.
So the first thing they do is to research the code.
That's right.
So agent here exactly mimics these actions.

[00:07]
Doing the research is not changing anything just because they don't know yet about the codebase.
But so once the research is done, the code changes are coming.
Amazing.
It feels like it's like everything is still very much right inside your IDE.
Exactly.
You don't have to change any of your behaviors that you're used to.
So it's just a sidebar, right?
So while agent is working, you can even close this tab and start a new conversation and asking about something else.
Or you can continue working on the files that you worked with.
So the work of an agent is paralleled with the work that developer does.
And it does not intervene with that.
So a developer does not need to wait for agent to finish working to continue their work.
They kind of coexist elegantly and parallel.
So now it's running a shell command here.
So it looks like it's running Gradle.
It tries to compile everything.

[00:08]
Yeah.
And this is like one of the interesting things about Codex.
Codex always tries to verify its own work.
So being able to then tap into the build tools and using them.
And that's an amazing part, right?
So just because just writing code is not enough.
You need to make sure that the code actually works and reiterate on that if it doesn't.
And as you can see, some of the commands are skipped.
and it's done.
You see?
So the Codex listed the files that were changed, right?
So we can take a look at the lines
that were actually updated or removed.
We can see them in a commit tool window
that they are uncommitted yet.
So we can push them to the repo.
But first of all, let's make sure that it actually works
and rerun the app to see whether the localization
actually takes place.
Cool.
And for that, we're just using the same tools
that we're used to in the IDE already.
Exactly, yeah.
So it's building, starting up the iOS simulator.

[00:09]
It starts the simulator, and I'd expect the app to be already in Spanish.
Cool. Let's see.
Oh, yeah, I can see your simulator is set to Spanish already.
It's set to Spanish just because the app is going to take the localization from the system.
So if everything went fine, the app would be already in Spanish.
And that's how Codex is natively integrated in our products.
What I showed you was all done in IntelliJ, but it also works in other JetBrains products like PyCharm, WebStorm, or Rider.
Thanks, Gleb.
These are just a few of the things that you can build with Codex inside JetBrains.
To get started, go to openai.com/codex or choose Codex inside the AI chat of your JetBrains IDE of choice.
Thank you, and we can't wait to see what you build.

</details>
