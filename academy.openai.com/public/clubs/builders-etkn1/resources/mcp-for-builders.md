<!-- source: https://academy.openai.com/public/clubs/builders-etkn1/resources/mcp-for-builders -->

[Builders](/public/clubs/builders-etkn1/overview)

[Content](/public/clubs/builders-etkn1/content)

Training

August 7, 2025 · Last updated on September 2, 2026

# MCP for Builders

![MCP for Builders](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Builder-Image-Template-for-OAI-Academy-YY-843f0e1a-dbde-4c62-a318-f6ed505c3430-1754605311815.jpeg?fit=scale-down&width=1200)

# Developers & Builders

# OpenAI API

# Advanced & Builder Skills

# Work

# Portfolio Company SDLC

## Connect your app to real‑world tools with a single, simple interface.

![MCP for Builders](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Builder-Image-Template-for-OAI-Academy-YY-843f0e1a-dbde-4c62-a318-f6ed505c3430-1754605311815.jpeg?fit=scale-down&width=1200)

## Start building with MCP

Think of MCP as the “universal adapter” for your AI-powered app. Instead of hand‑coding a new function call for every API, you point the model at an *MCP server* that exposes a tidy set of commands (things like “*search catalog*,” “*get customer*,” or “*create ticket*.”) This results in fewer moving parts, faster iteration, and easier maintenance as your toolset grows.

## Why builders like it

* **One connection, many tools:** Plug multiple services into one MCP server, then give the model clean, reusable commands.

* **Lower friction, faster loops:** Cut down on round‑trips and glue code in agentic workflows.

* **Reusable patterns:** Standardize actions your agents can take across projects/teams.

* **Grows with you:** Add or swap integrations without re‑prompting your whole app.

## Core resources

* ﻿ [**An Introduction to MCP**](https://vimeo.com/manage/videos/1105243308)**:** a quick, clear walkthrough of what MCP is and how it helps you tailor model behavior end‑to‑end.

* ﻿ [**Using the Responses API’s MCP Tool Cookbook**](https://cookbook.openai.com/examples/mcp/mcp_tool_guide)**:** step‑by‑step setup, how the tool works, example use cases, and best practices.

## Get started today

1. **Watch the intro video** to see how MCP fits into an agentic app.

2. **Follow the Cookbook** to spin up your first MCP tool and test it in a simple workflow.

3. **Add commands over time** as your app needs grow, no big refactors required.

[1:00:00](/public/clubs/builders-etkn1/videos/codex-for-software-engineers-2026-03-13)

Video

[Codex Fundamentals](/public/clubs/builders-etkn1/videos/codex-for-software-engineers-2026-03-13)

By Ryan Taylor

[Builder Bootcamp](/public/clubs/builders-etkn1/resources/builder-bootcamp-2026-04-22)

[Codex 101: Introduction and Onboarding](/public/clubs/builders-etkn1/resources/codex-101-introduction-and-onboarding-2026-03-18)

[GPT-5 for Builders](/public/clubs/builders-etkn1/resources/gpt-5-for-builders)

Aug 7th, 2025 • Views 65.9K

[Codex Bootcamp](/public/clubs/builders-etkn1/resources/codex-bootcamp-2026-09-23)

Aug 12th, 2026 • Views 8.1K

External Content

[Codex for SWEs](/public/clubs/builders-etkn1/externals/codex-for-swes-2026-03-18)

Mar 18th, 2026 • Views 2.4K

[59:20](/public/videos/builder-bootcamp-rag-2026-09-14)

Video

[Builder Bootcamp: RAG](/public/videos/builder-bootcamp-rag-2026-09-14)

Sep 14th, 2026 • Views 1.5K

[GPT-5 for Builders](/public/clubs/builders-etkn1/resources/gpt-5-for-builders)

Aug 7th, 2025 • Views 65.9K

External Content

[Codex for SWEs](/public/clubs/builders-etkn1/externals/codex-for-swes-2026-03-18)

Mar 18th, 2026 • Views 2.4K

[59:20](/public/videos/builder-bootcamp-rag-2026-09-14)

Video

[Builder Bootcamp: RAG](/public/videos/builder-bootcamp-rag-2026-09-14)

Sep 14th, 2026 • Views 1.5K

[Codex Bootcamp](/public/clubs/builders-etkn1/resources/codex-bootcamp-2026-09-23)

Aug 12th, 2026 • Views 8.1K

# An Introduction to MCP

<!-- vimeo: 1105243308 | track: English (auto-generated) -->

[▶ Watch on Vimeo](https://vimeo.com/1105243308)

<details>
<summary>자막: An Introduction to MCP</summary>

Hi everyone, my name is Nico Inch, and I'm a product manager on our API team. Hi, I'm Steven. I'm an engineer on the API team. Awesome. So about two months ago, we launched the responses API and since then, hundreds of thousands of users have started to use it. We've already processed trillions of to tokens on this API and today we are super excited to launch the next set of features for it. People are really liking the simplicity of the responses. API for someone who's just getting started building their first AI application. It's just three lines of code to get started by talking to any of our models. And for power users or enterprises that are looking for more of a batteries included approach, uh, they can use the file search tool for, uh, a built-in rack pipeline. They can use a web search tool to browse the web computer use to control their, their computers, and so much more. So today we are gonna launch six new features to responses, API, which is three new tools and three new features. So three new tools are gonna be support for remote MCP servers, code interpreter, and image generation. And the features that we are launching are background mode, reasoning summaries, and encrypted content. So let's just dive into seeing how all of this works. We are so excited to launch support today for model context protocol or MCP servers. Within the responses, API, you can now seamlessly connect to dozens of services like Stripe, Twilio, Shopify, and more without needing to manage each of these integrations yourself. One of the my favorite MCP use cases I've seen so far is from Shopify. So Shopify is rolling out a custom MCP server for every Shopify store on the web so that models can use it to search through product catalogs and get details on any products that are for sale. So, uh, let's jump in with a demo. Um, here we are in the, um, API playground and I'm gonna connect to a Shopify MCP server to help me do some shopping. So in my case, I just started doing yoga and I'd like to, uh, have some help finding a yoga mat. So what I can do is add a new tool, and in this case we're gonna add an MCP server and we'll add the MCP server for the aloe yoga store. This particular, um, remote MCP server is open, no authentication required, so I can just click connect. Yeah, you can access pretty much any, uh, Shopify store with m ccp, just the Shopify store domain name slash API slash cp. Yep. And so it exposes all of these tools like getting, um, policies and FAQs, product details and so forth. I'm just going to choose the shop catalog and update cart tools and add this to my request. So now, when I prompt the model, um, it will use tools from that MCP server to help fulfill the response. So for instance, I can say, find me at black yoga mat and add it to my cart. This will contact the Shopify, um, uh, server and do a search for, uh, black yoga mat. I can approve that by default, all, uh, MCP calls require approval. Um, but you can also turn this off. Uh, it seems to have found a yoga mat and is going to add it to the cart, and now it's summarizing what it found for me and also given me a link to check out, which is perfect, exactly what I wanted. So now I can check out and I'll have my new yoga mat, uh, within my hands within seconds. Nice. Wow. Incredible. Just what I needed. That's fast. All right. Um, so beyond MCP, we are also launching support for two new, two other hosted tools. First, we are launching code interpreter. So you can ask, you can now ask models like O three to analyze data and CSB files, generate graphs or work on hard math problems, all using Python, And also like, uh, images, right? So if you've seen the demos of putting an image into the context and then O three sort of crop, it zooms, inver, the images, whatnot, uh, all of that is powered by the code interpreter tool. Yeah, it's incredible. And in addition to image inputs with the code interpreter, we are launching as well an image generation tool. So this is the same image generation tool that recently went viral within chat GPT. And now models will have access to call it as part of their, um, uh, response within the responses. API. So each of these hosted tools is very exciting on their own, but I think the real power comes from combining multiple tools together. So let's try a couple of fun examples where we're combining multiple hosted tools. In this first one, I'm going to combine the web search tool and the image generation tool to create a visualization of the weather forecast for tomorrow in San Francisco. So I'll go ahead and add the web search tool to my request as well as the image generation tool, and I will ask it to create an image of the Golden Gate Bridge with tomorrow's forecast. Tomorrow's SF Forecast overlaid in a cloud above the bridge. Nice. So it started by searching the web. It's going to be looking for, uh, tomorrow's forecast that's very detailed, hour by hour forecast, um, stunning and warm as usual. That's why I love living here. And now it's generating an image. We just fast forward it a bit and we can see now that the, the weather is overlaid on a cloud above the Golden Gate Bridge. Um, incredible. Can You actually do this with, uh, MCP servers? How would we combine MCP server with image generation? Absolutely. Um, let's try with the Stripe MCP server. So Stripe has this MCP server that allows you to search their documentation. Um, I know you used to work at Stripe, um, but I didn't. So I find some of the concepts, uh, a little bit, uh, uh, new and confusing. So, uh, I'd like to create an image to help me understand some of, um, the stripes. API. So Stripe is actually one of our built-in defaults here, so I can go ahead and copy in my test. API key when I connect to the Stripe, it, a guy server will gimme all the tools that, um, Stripe makes available. This case, it's a lot. Um, we have things like searching through documentation, creating customers, listing prices, um, all sorts of things. Click Into one of them. Yeah. Yeah. So if you click into one, you'll see what the model will actually see. Um, these descriptions help, um, guide the model in which tool to call, and then also how to fill in the different parameters. Um, in this case, uh, I only want to make the search documentation tool available, so add that. So we've got the Stripe MCP server with the search documentation tool enabled and the image generation tool. So let's say search the Stripe docs and create an image to visualize how Stripe subscriptions work. Nice. And again, is the first step. Uh, it's going to get the list of tools. It will search, um, it's gonna search the documentation for subscriptions, and then it's going to generate an image. Um, and again, this takes a few seconds, so we'll just fast forward. Great. It's generated an image. I don't know how accurate it is. Maybe you could tell me. But, um, pretty neat way to, uh, search through documentation and, uh, create visualizations with the image generation tool. Looks Pretty neat. I think it's, it's pretty accurate. And they even have entitlements, which I think just launched, so it's pretty cool. Incredible. Okay, so let's dive into demo three. And this time let's use a more powerful model like O three. So O three has been trained using reinforcement learning to be able to use tools while it reasons, so it can think about which tools to use. It can use a tool and then decide that it's the wrong one, and take a step back and do something else. It's really, uh, e agentic in, in the pure sense of the word. Um, so let's try something much more complicated with this model. In this demo, let's give it three tools. And, and Steven, you wanna show us, uh, what we're gonna do? Yeah, so in this example, what I'm going to do is take a list of trip expenses, um, from a recent trip to Bali, and they're in multiple currencies. And what I'd like to do is sum up the total, uh, get the conversion rates, daily conversion rates from an MCP server to get everything into US dollars. And then from there, create a PayPal invoice to send to my friend. Nice. So, um, I've got already, uh, in response set up here with two tools. Uh, one is Zapier, which has my currency converter as, as a Zap. They have built in MT p servers and customized kinda which Zaps are available in each server. Um, and then I've got my PayPal account here so that we can create an invoice at the end, um, and then to actually do the calculations and so forth. I'll need to add the code interpreter tool, and I can give the code interpreter tool access to my CSV here, which contains all the expenses. All Right, so bring your own files to code interpreter. That's pretty neat. Yeah, bring your own files, obviously add a lot more files there, and it gives it all, um, to the Python, uh, to, uh, to read. Um, so my prompt here is to sum up the total expenses, convert to US dollars using today's exchange rate, and then create a PayPal invoice for that total with these details. Um, and what's really cool about this prompt is that it's an entirely end-to-end a Gentech workflow. Uh, that's all gonna happen within the chain of thought, uh, with these tool calls interspersed in, uh, previously this would've been multiple API calls, you know, integrations remote, remote, uh, API calls on your server. Now it's just one call to the responses API. So, um, let's give it a shot. Give You usually PayPal invoice your friends for expenses. Yeah, absolutely. Every single trip involves double entry accounting and invoices. Um, Right. So yeah, it's, it's gotten the tools from ZA PR, it's gotten the tools from, uh, PayPal. It's actually reasoning right now. Um, Let's see what, yeah, so if this works, which we're hoping it does, um, it will probably start by reading the file, uh, calculating up the expenses in different currencies. So looks like it's reading through the file, getting a sense of the different columns and so forth that are available on it. Um, and now it's getting, uh, the total in Euros as well as the total in USD, so it realizes it doesn't have the today's, um, Euro to USD exchange rate. So it's getting that from an MCP server, um, and once it has, has that exchange rate, um, it will then calculate the total in US dollars and hopefully create an invoice for me. That's amazing. Yeah, the euro, the euro to USD exchange rate hasn't been doing that great yet recently, but, um, at least we're getting to the latest one. Uh, perfect. So now it's running a little bit more Python to do that final conversion and getting my output here. Uh, it sees that the, um, total is, is about $3,000 getting today's date and fantastic. As the last step here, I've, I've said it to turn on approvals before it actually creates a PayPal invoice, but it, uh, has all the details for the requests to PayPal, um, and if I press approve, it will create the invoice and then I can send it to my friend. So that entire end-to-end agentic workflow, one call to responses API and no custom code that I needed to deploy. So, pretty remarkable. And we're excited to see what kinds of things that, uh, developers will build by combining multiple tools, MCP chain of thought and reasoning. So very, very powerful. Nice. Yeah. So remote MCP servers are just getting started. Uh, we've shown you, uh, a few today. Uh, there are about, uh, a dozen or couple dozen that exist out there today. Uh, and we expect the number of remote MCP servers, uh, in the coming weeks and months to grow really quickly. Uh, and I'm really excited to see what you can do with a single responses, API call when there are hundreds of remote MCP servers out there, uh, combined with our built-in tools. Uh, and so very excited about the future over here. Uh, before we wrap, let's just quickly touch on the three new features that we are launching. So first, we've got background mode. As you've seen in deep research or codex or operator, some of these, uh, tr model trajectories can take, you know, dozens of minutes to complete, 10 minutes, 20 minutes. And so far you had to do everything synchronously. You can now use background mode to create an asynchronous response. Um, it'll keep running in the background. You can check to see whether it's done or not. And you can even start a stream from an asynchronously running response, which is really cool. You can just like check in on where it is and catch up on it. Yeah. Um, Super exciting. Something that developers have been asking for, for a long time. Yeah, totally. Um, we also have reasoning summaries in the responses. API, now you've seen, uh, these concise need summaries of what the model is thinking about in chat GPT, and you can use those, uh, and, and get those in the responses, API with our reasoning models. And lastly, we have encrypted content. So with models like O three and O four, many, it's really important that you continue to reuse the reasoning tokens that are sent by the model, um, back in future API requests. So the model doesn't have to think from scratch if you're a zero data retention customer, or if you don't wanna store that data on open air servers because of some privacy reasons, uh, you can still use encrypted content so that open air never stores that data and you can, uh, sell, pass back those reasoning tokens to us. So that's it. Uh, those are the three, uh, new tools and three new features that we're launching today in the responses API and we can't wait to see what you build on top of the API. Thanks. Thank you.

</details>
