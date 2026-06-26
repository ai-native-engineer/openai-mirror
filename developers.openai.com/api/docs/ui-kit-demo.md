<!-- source: https://developers.openai.com/api/docs/ui-kit-demo/ -->

# UI Kit Demo

### DocsTip

Use DocsTip for helpful callouts inside guides or references.

### DocCardGroup

[![API reference](/open-graph.png)

API reference

Browse endpoints, parameters, and responses.](/docs)[![Resources](/resources_bg.png)

Resources

Find guides, best practices, and examples.](/learn)[![Local anchor](/blog_bg.png)

Local anchor

Jump to a section on the page.](#local-section)

### DocsMarkdownContent

# DocsMarkdownContent

Use **Markdown** content here to validate styles and link handling.

* Bullet one
* Bullet two

[Internal link](/docs) and [external link](https://openai.com).

### ContentModeSwitch

Responses sample

curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY"

### CodeSample

Examples

javascript

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await client.responses.create({
  model: "gpt-4.1-mini",
  input: "Say hello",

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
  model="gpt-4.1-mini",
  input="Say hello",

var client = new OpenAIClient(Environment.GetEnvironmentVariable("OPENAI_API_KEY"));

var response = await client.Responses.CreateAsync(
  model: "gpt-4.1-mini",
  input: "Say hello"
);

Examples

javascript

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await client.responses.create({
  model: "gpt-4.1-mini",
  input: "Say hello",

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
  model="gpt-4.1-mini",
  input="Say hello",

var client = new OpenAIClient(Environment.GetEnvironmentVariable("OPENAI_API_KEY"));

var response = await client.Responses.CreateAsync(
  model: "gpt-4.1-mini",
  input: "Say hello"
);

## hello

### CodeSample

Examples

javascript

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await client.responses.create({
  model: "gpt-4.1-mini",
  input: "Say hello",

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
  model="gpt-4.1-mini",
  input="Say hello",

var client = new OpenAIClient(Environment.GetEnvironmentVariable("OPENAI_API_KEY"));

var response = await client.Responses.CreateAsync(
  model: "gpt-4.1-mini",
  input: "Say hello"
);

Examples

javascript

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await client.responses.create({
  model: "gpt-4.1-mini",
  input: "Say hello",

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.responses.create(
  model="gpt-4.1-mini",
  input="Say hello",

var client = new OpenAIClient(Environment.GetEnvironmentVariable("OPENAI_API_KEY"));

var response = await client.Responses.CreateAsync(
  model: "gpt-4.1-mini",
  input: "Say hello"
);

### CodeComparison

Before

curl https://api.openai.com/v1/responses

After

curl https://api.openai.com/v1/responses

### ContentSwitcher

NodePython

Node

Node SDK

import OpenAI from "openai";

const client = new OpenAI();

Python

Python SDK

from openai import OpenAI

client = OpenAI()

### DeepDive

Deep dive

Why streaming matters

### LatencyExample

Network

End user to API latency

Server

Time to process prompt tokens

Server

Time to sample/generate tokens

Network

API to end user latency

### WaveformComponent

### Expander

Expandable section

Use Expander to hide long details behind a toggle.

### Image

![OpenAI Open Graph](/open-graph.png)

### Icon

### IconItem

Realtime quickstart

Launch a realtime session and inspect events.

### GalleryDocs

[![Input 1](/blog_bg.png)](/blog_bg.png)[![Input 2](/resources_bg.png)](/resources_bg.png)[![Input 3](/api_bg.webp)](/api_bg.webp)[![Input 4](/open-graph.png)](/open-graph.png)

![Result](/apps-og-card.png)

### CodeGallery

Explore

[![](https://cdn.openai.com/devhub/gpt5prompts/ocean-wave-simulation-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/brutalist-dev-landing-page-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/solar-system-explorer-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/customer-journey-flow-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/asteroid-game-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/employee-skills-matrix-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/virtual-drum-kit-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/camping-gear-checklist-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/weather-theatre-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/typing-rain-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/holiday-card-for-kids-5.2.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/cloud-painter.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/audio-step-sequencer.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/farewell-message-board.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/csv-to-charts.png)](#)[![](https://cdn.openai.com/devhub/gpt5prompts/espresso.png)](#)

### ImageGallery

Explore

[![](https://cdn.openai.com/API/docs/images/images-gallery-2/sci-fi-hangar.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/mechanical-bouquet.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/mechanical-watch.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/botanical-perfume-output.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/lavender-sunrise.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/moon-control-room-1969.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/mountain-map.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/shipyard-welding-documentary.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/coral-reef.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/smart-home-dashboard.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/abstract-orbit.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/airport-departure-kiosk-ui.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/icons-poster.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/3d-city.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/ink-wash-temple.png)](#)[![](https://cdn.openai.com/API/docs/images/images-gallery-2/cliffside-portrait.png)](#)

### VideoGallery

Explore

[![](https://cdn.openai.com/API/docs/video-gallery/posters/Space-Race.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/maui.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/Upside-Down-City.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/fox-walk.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/zebra-chase.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/mushroom-network.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/90s-TV-Ad.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/chameleon.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/cozy-coffee-shop-interior.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/coloring.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/Sleeping-Otters.jpg)](#)[![](https://cdn.openai.com/API/docs/video-gallery/posters/indie-cafe-rainy-window.jpg)](#)
