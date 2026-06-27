---
title: "Debug web apps with browser use in Codex"
channel: openai
url: https://www.youtube.com/watch?v=bhgYFRZLyKI
youtube_id: bhgYFRZLyKI
published: 2026-06-12
duration: "1:28"
captions: en
---

# Debug web apps with browser use in Codex

[![Debug web apps with browser use in Codex](https://img.youtube.com/vi/bhgYFRZLyKI/hqdefault.jpg)](https://www.youtube.com/watch?v=bhgYFRZLyKI)

<details>
<summary>자막: Debug web apps with browser use in Codex (1:28)</summary>

[00:00]
Codex can now better debug and test the
web applications that you're building.
We've added support for the Chrome
DevTools Protocol, or CDP, to the
Browser Use functionality in Codex.
This way, Codex has access to more
advanced functionality like performance
profiling and inspecting network
traffic, as well as the ability to
inspect console logs, runtime errors,
local storage, and the applied styling.
To use this functionality, you'll have
to enable Developer Mode in the browser
settings of your Codex app.
And since this mode gives Codex more
insight into the application it is
controlling, you'll have to explicitly
approve when Codex starts using CDP to
inspect a website.
I've been working on this little chat
app and noticed that it recently slowed
down quite significantly, especially as
the list of conversations grows.
It takes a while to load, and typing
overall is quite delayed.
I can ask Codex to debug this using
Browser Use. This way, it is not just
doing a code pass, but actually
inspecting the network traffic and
profiling the application.
This way, it can get a better
understanding of your app and the true

[00:01]
bottlenecks by profiling specific
interactions in your app or looking at
the network requests your app is making
before diving into fixing it.
You can see it found a couple of
issues, fixed them, and supported those
fixes with clear measurements showing
the improvements. This is just one
example of how Codex can use CDP to
have more in-depth Browser Use
capabilities when building applications.
Give it a try and let us know
what you think.

</details>
