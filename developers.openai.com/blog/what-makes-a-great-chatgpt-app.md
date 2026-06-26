<!-- source: https://developers.openai.com/blog/what-makes-a-great-chatgpt-app/ -->

## Search the blog

![What makes a great ChatGPT app](/images/blog/apps-blog-visual.png)

At DevDay we introduced [ChatGPT Apps](https://openai.com/index/introducing-apps-in-chatgpt/) — a new way to bring your product directly into ChatGPT conversations. This post builds on that launch with practical guidance for developers, PMs, and designers on how to choose the right use case and design an app that’s actually useful once it’s live. We’ll focus on how to translate your product’s strengths into clear, well-scoped capabilities the model can apply across many different conversations and user intents. If you’re looking for the technical details, you can jump straight into the [Apps SDK quickstart](https://developers.openai.com/apps-sdk/quickstart) and [developer docs](https://developers.openai.com/apps-sdk).

We’ll cover:

* What a ChatGPT app really is (and isn’t)
* The three ways an app can genuinely add value
* How to design for conversation and discovery
* How to know whether your app is actually helping
* Concrete examples and suggestions for screenshots

## What a ChatGPT app actually is

When teams build their first ChatGPT app, the starting point is often:

*“We already have a product. Let’s bring it into ChatGPT.”*

This often starts with taking an existing web or mobile experience — screens, menus, flows — and trying to reshape it for chat. It’s a reasonable instinct; for years, “software” has meant pages, navigation, and UI scaffolding.

However, building apps for ChatGPT is a different environment. Users aren’t “opening” your app and starting on the home page. They’re having a conversation about something and the model can decide when to bring an app into that conversation. They’re entering at a point in time.
In that world, the best apps look surprisingly small from the outside. They don’t try to recreate the entire product. Instead, they allow users to access a few **specific powers** while using the app in ChatGPT: the concrete things your product does best that the model can reuse in any conversation.

Outside of ChatGPT, your app is often the destination. Users:

1. Tap your icon
2. Enter your environment
3. Learn your navigation and UI patterns

Most product decisions flow from that assumption: “We own the screen.” You can invest heavily in layout, onboarding, and information architecture because users are committing to your space.

Inside ChatGPT, your app plays a different role:

* It’s a **capability** the model can call - for both context and visual engagement.
* It shows up **inside** an ongoing conversation.
* It’s one of several tools the model may orchestrate.

That means the “unit of value” is less your overall experience and more the specific things you can help the model and user accomplish at the right moment.

A practical definition:

**A ChatGPT app is a set of well defined tools that can perform tasks, trigger interactions, or access data.**

This has a few implications:

* You don’t need to port every feature.
* You don’t need a full navigation hierarchy.
* You *do* need a clear, compact API: a handful of operations that are easy to invoke and easy to build on.

You can think of it this way: your ChatGPT app is a toolkit the model reaches for when the user runs into a specific type of problem. The more precisely that toolkit is defined, the easier it is to use in the flow of conversation.

Once you see your app as “capabilities the model can orchestrate,” rather than “a mini version of our product,” design decisions get clearer. You start asking “What can we help with here?” instead of “Where should the user go next?”

## The three ways to add real value

A simple filter for any app idea:

* **Know:** Does it let the user work with new context or data they couldn’t see otherwise in ChatGPT?
* **Do:** Does the app take real actions on the user’s behalf?
* **Show:** Does the app present information in a clearer, more actionable UI than plain text?

This applies to **“serious”** productivity apps and to **“just for fun”** apps like games. A game might not help someone ship a report faster, but it still does something the base model can’t do well on its own: maintain stateful game logic, track progress, enforce rules, or render interesting views of the game world. The value is delight and engagement, but the underlying pattern is the same.

### 1) New things to know

Your app makes new context available within a ChatGPT conversation:

* Live prices, availability, inventory
* Internal metrics, logs, analytics
* Specialized, subscription-gated, or niche datasets
* User-specific data (accounts, history, preferences, entitlements)
* Sensor data, live video streams

In practice, this often means bridging into systems where data is correct, current, and permissioned. The app becomes the “eyes and ears” of the model in your domain, and can answer questions with more authority.

### 2) New things to *do*

Your app takes actions on the user’s behalf:

* Create or update records in internal tools
* Send messages, tickets, approvals, notifications
* Schedule, book, order, or configure things
* Trigger workflows (deploy, escalate, sync data)
* Play interactive games (apply rules, advance turns, track state)
* Take actions in the physical world (IoT, robotics control, etc.)

Here, the app is less a source of truth and more a pair of hands. It takes the user’s intent and turns it into concrete changes in the systems your team already lives in—or, in the case of games, concrete changes in the game state that make the experience feel consistent and fair. This is where your app shifts to an agent in a meaningful way.

### 3) Better ways to show

An app can present information in a GUI in a ChatGPT conversation, that makes the information more digestible or more actionable:

* Shortlists, comparisons, rankings
* Tables, timelines, charts
* Role-specific or decision-specific summaries
* Visual or structured views of game state (boards, inventories, scores)

This is especially valuable when users are making choices or trade-offs. Apps can give the model a language for structure: widgets that have columns, rows, scores, and visuals that match how people actually decide—or, in games, how they understand “where they are” in the world.

If an app doesn’t clearly move the needle on at least one of **know/do/show**, it tends to feel like it’s not adding value beyond what users can already do in ChatGPT. Users may not complain explicitly, but it’s a missed opportunity to provide more meaningful value to the user, whether the app is meant for work or play.

Here you can see an example of an experience enhanced by an app:

An example answer from ChatGPT

This answer is helpful, however, the user may want to use an app with additional capabilities to directly browse real properties without changing context or leaving the conversation.

![find-homes](/images/blog/find-homes-expanded.png)
Answer with the Zillow app

With the Zillow app, the user has the additional ability to search live property listings, filter by criteria, and view rich property details — all without leaving the chat.

![find-homes-zillow](/images/blog/find-homes-zillow.png)

Fullscreen mode for enriched discovery

![find-homes-fs](/images/blog/find-homes-fs.png)
