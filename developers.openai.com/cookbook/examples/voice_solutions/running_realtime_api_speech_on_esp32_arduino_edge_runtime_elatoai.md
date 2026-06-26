<!-- source: https://developers.openai.com/cookbook/examples/voice_solutions/running_realtime_api_speech_on_esp32_arduino_edge_runtime_elatoai/ -->

## Search the cookbook

May 1, 2025

# ElatoAI - Realtime Speech AI Agents for ESP32 on Arduino

This recipe is archived and may reference outdated models or APIs.

[![Akashdeep Deb](https://avatars.githubusercontent.com/u/20175219)  AD](https://github.com/akdeb)

[Akashdeep Deb](https://github.com/akdeb)

[View on GitHub](https://github.com/openai/openai-cookbook/blob/main/examples/voice_solutions/running_realtime_api_speech_on_esp32_arduino_edge_runtime_elatoai.md) [Download raw](https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/voice_solutions/running_realtime_api_speech_on_esp32_arduino_edge_runtime_elatoai.md)

![Elato Logo](https://raw.githubusercontent.com/openai/openai-cookbook/refs/heads/main/examples/voice_solutions/arduino_ai_speech_assets/elato-alien.png)

## 👾 ElatoAI: Running OpenAI Realtime API Speech on ESP32 on Arduino with Deno Edge Functions

This guide shows how to build a AI voice agent device with Realtime AI Speech powered by OpenAI Realtime API, ESP32, Secure WebSockets, and Deno Edge Functions for >10-minute uninterrupted global conversations.

An active version of this README is available at [ElatoAI](https://github.com/akdeb/ElatoAI).

[![Elato AI Demo Video](https://raw.githubusercontent.com/akdeb/ElatoAI/refs/heads/main/assets/thumbnail.png)](https://www.youtube.com/watch?v=o1eIAwVll5I)

<!-- yt-inline:o1eIAwVll5I -->
[![Open-source, Conversational OpenAI Realtime Speech on ESP32](https://img.youtube.com/vi/o1eIAwVll5I/hqdefault.jpg)](https://www.youtube.com/watch?v=o1eIAwVll5I)

<details>
<summary>자막: Open-source, Conversational OpenAI Realtime Speech on ESP32 (2:25)</summary>

[00:00]
So, we're going to start talking to
Paddington Bear. And I've added a
character I call Chad Brew Barkley. And
this is what the conversation sounds
like. Bro, what? That's cringe, my dude.
We're not here to get all serious about
carbon stuff. Let's keep it real. How
about we just chill and hit the pump for
some bruise and laugh? Come on. Let's
make tonight unforgettable. Let's go.
Hey Chad, can you say hi to the world?
Yo, what's up world? Chad Barkley here.
Just giving a big shout out to everyone
out there. Let's go make awesome vibes.
Okay, awesome. So, I'm going to turn
that off. Next, we're going to chat with
someone who loves surfing. Totally
stoked to hang out and chat with you.
How's your day going? Hey, Summer. I'm
going to be in Maui in two weeks. What
should I do there? Oh, that sounds epic.
M is going to be so amazing. Summer. No,

[00:01]
I was saying I'm going to be in Maui in
Kihei. Um, and maybe I'll stay in Wuku.
Oh, my bad. Maui is going to be totally
chill and awesome, too. You should
definitely check
out a drive along the Hana Highway. It's
like a super scenic adventure with
waterfalls and lush forests. And now
we're going to talk to a character whose
name is Julian Shakespeare. And this is
what the conversation is like. Ah, the
curtain rises once more. We find
ourselves at the heart of the scene.
Dear Akash, what is it that you seek
from this dramatic dialogue? Let us
proceed with fervor and passion.
Shakespeare. What should I do for a
Kickstarter?
Ah, the stage is set and the spotlight
falls upon your grand endeavor to create
a Kickstarter campaign worthy of first.
Craft a narrative as compelling as the

[00:02]
finest tragedy or comedy. Your story
should capture the hearts and minds of
your audience, painting a vivid picture
of your project's purpose and passion.
Second, assemble rewards that dazzle and
delight like treasures hidden in a
chest, unique and enticing. each one a
token of gratitude to your backers.

</details>


## ⚡️ DIY Hardware Design

The reference implementation uses an ESP32-S3 microcontroller with minimal additional components:

![Hardware Setup](https://raw.githubusercontent.com/openai/openai-cookbook/refs/heads/main/examples/voice_solutions/arduino_ai_speech_assets/pcb-design.png)

**Required Components:**

* ESP32-S3 development board
* I2S microphone (e.g., INMP441)
* I2S amplifier and speaker (e.g., MAX98357A)
* Push button to start/stop the conversation
* RGB LED for visual feedback
* Optional: touch sensor for alternative control

**Hardware options:**
A fully assembled PCB and device is available in the [ElatoAI store](https://www.elatoai.com/products).

## 📱 App Design

Control your ESP32 AI device from your phone with your own webapp.

![App Screenshots](https://raw.githubusercontent.com/openai/openai-cookbook/refs/heads/main/examples/voice_solutions/arduino_ai_speech_assets/mockups.png)

| Select from a list of AI characters | Talk to your AI with real-time responses | Create personalized AI characters |
| --- | --- | --- |

## ✨ Quick Start Tutorial

[![Watch Demo on YouTube](https://img.shields.io/badge/Quick%20start%20Tutorial-YouTube-yellow?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=bXrNRpGOJWw)

<!-- yt-inline:bXrNRpGOJWw -->
[![Running OpenAI Realtime Speech API on ESP32 Arduino with ElatoAI! (Complete tutorial)](https://img.youtube.com/vi/bXrNRpGOJWw/hqdefault.jpg)](https://www.youtube.com/watch?v=bXrNRpGOJWw)

<details>
<summary>자막: Running OpenAI Realtime Speech API on ESP32 Arduino with ElatoAI! (Complete tutorial) (6:28)</summary>

[00:00]
Hey everyone, my name is Akash and I
created Elato to make it really easy for
you to run real-time AI speech models on
your
ESP32 with an edge server like Dino or
Superbase Edge Functions. Um, so we
create a device that looks like this
that uses an
ESP32S3 and you can wrap it around toys
to give it a voice and a personality. In
this video, I'm going to show you how to
get us started and I'm going to walk you
through the readme um to get you up and
running in no time. Uh so let's get
let's get us started. Um so first let's
set up superbase. Um so you're going to
run brew install superbase tap
superbase. And then once you've done
that um you want to run superbase start.
So I'm going to do that right now. And I
get um a lot of these links. Just to
double check. I'm going to go into
studio URL and I'll just check that this
works. Um it looks like all my tables
are set up which is really good. Next
we're going to go and set up the nextJS
front end. So this makes it easy for you

[00:01]
to run um for you to create AI
characters and also you can you know set
device volume, set overtheair updates
and stuff like that. Um so here we're
going to run npm
install and so we'll let that run and
then we'll just copy this command so
that we can create our end.local. So
this is where our environment variables
would be. So if we go into the code and
um if we go
into local we should see that these are
um we want to fill in the superbase
add-on key. So we're just going to pick
that up from here. So let's copy that
and then we're going to paste that here.
So I already have an OpenAI API key
which I'm going to use. So I'll just
copy that and um I'll paste that in here
as well. So that looks pretty solid. Now
let's run npm rundev. Um so once that's
running, we can go and check if our

[00:02]
front end looks good. Um
so okay, so we're going to go into home
and I think this will be logged in for
you, but you can log in with the credits
that you see on the screen. And then
we're going we're going to go into
settings. And it looks like we don't
need to register the device, which is
good. Next step, we're going to set up
the Dino server. So, we have the Nex.js
server running on a different um
console. We're going to go here and then
we're going to go into server Dino um
and let's copy this so that we create a
new M file. And then um same thing,
we're going to copy the Superbase key
and OpenAI API key. So, we'll do the
same thing here. Um why don't we just
copy it from here?
So, I'll just copy paste
that.
Um, and then let's do the same with the
OpenAI API key. Just copy the full
thing. And looks like we're set here.

[00:03]
Perfect. So, next we're just going to
run Dino here. And it looks like it's
running at 8,000. Next step, we're going
to um basically flash the ESP32
firmware. Um, and to do that, let's
first go into
config.cpp.
config.cpp. Here, um, since dev mode,
the mac the dev mode macro is set at
true, we're going to find, um, what our
IP address is for this network. Um, so
let's go in here. We go into Wi-Fi
settings. This is like a quick and easy
way to do it. We're going to go into
details and then we'll find the IP
address here. So for me it's just
1021136. Um let's close that and um it
looks like this is already set up. So I
think we should be in good shape. Um
next we're going to build and upload it.

[00:04]
So I have my ESP32 right here. I'm going
to plug in my USB type-C. I'm going to
connect it to my laptop. Just like that.
and let's go ahead and click build here.
Um, so once that
builds so you can see this is what it
looks like. Um, let's upload this
firmware on to the
ESP32S3. Okay, so you should see
something like this. Next, we're going
to go into to set our Wi-Fi. So, let's
go into settings. Maybe on our phone.
Um, that would be easier. We'll find
Elato device here. And um let's go into
192.168
um.41. And so we'll see a page like this
where we want to set our Wi-Fi
credentials. Okay. So you should see
that this is saved. Now we're going to
turn our device off and on again. Okay.

[00:05]
So I have my device here and since this
is a portable device, I'm going to turn
it off and on again. Um and so if we
look at our instructions first we should
see that when we turn it on it should
first generate an O token which gets
saved um in nonvolatile storage on the
ESP32S3 and then it should directly
connect to our edge server with our
openi API key. So we'll see that here.
This is green. It's going to generate
the O token. It's going to
student. Have you ever thought about how
playing guitar could be like exploring a
new galaxy of
what's
new? Let's add
another constellation.
Hey El, can you say hi to the world of
awesome developers?
Absolutely. Hi there, awesome explorers.
You're all
shinled and fun.

[00:06]
So, here you can see the transcript and
all the data from this conversation. All
right. Bye now, Elato.
Hey, Karen. Have a great day.
Awesome. So, hope that helped and um try
it out and let me know what you think in
the comments below. Cheers. Thank you.

</details>


1. **Clone the repository**

Head over to the [ElatoAI GitHub repository](https://github.com/akdeb/ElatoAI) and clone the repository.

git clone https://github.com/akdeb/ElatoAI.git
cd ElatoAI

2. **Set your environment variables (OPENAI\_API\_KEY, SUPABASE\_ANON\_KEY)**

In the `frontend-nextjs` directory, create a `.env.local` file and set your environment variables.

cd frontend-nextjs
cp .env.example .env.local

# In .env.local, set your environment variables 
# NEXT_PUBLIC_SUPABASE_ANON_KEY=<your-supabase-anon-key>
# OPENAI_API_KEY=<your-openai-api-key>

In the `server-deno` directory, create a `.env` file and set your environment variables.

cd server-deno
cp .env.example .env

# In .env, set your environment variables 
# SUPABASE_KEY=<your-supabase-anon-key>
# OPENAI_API_KEY=<your-openai-api-key>

2. **Start Supabase**

Install [Supabase CLI](https://supabase.com/docs/guides/local-development/cli/getting-started) and set up your Local Supabase Backend. From the root directory, run:

brew install supabase/tap/supabase
supabase start # Starts your local Supabase server with the default migrations and seed data.

3. **Set up your NextJS Frontend**

([See the Frontend README](https://github.com/akdeb/ElatoAI/tree/main/frontend-nextjs/README.md))

From the `frontend-nextjs` directory, run the following commands. (**Login creds:** Email: `admin@elatoai.com`, Password: `admin`)

cd frontend-nextjs
npm install

# Run the development server
npm run dev

4. **Start the Deno server**

([See the Deno server README](https://github.com/akdeb/ElatoAI/tree/main/server-deno/README.md))

# Navigate to the server directory
cd server-deno

# Run the server at port 8000
deno run -A --env-file=.env main.ts

5. **Setup the ESP32 Device firmware**

([See the ESP32 Device README](https://github.com/akdeb/ElatoAI/tree/main/firmware-arduino/README.md))

In `Config.cpp` set `ws_server` and `backend_server` to your local IP address. Run `ifconfig` in your console and find `en0` -> `inet` -> `192.168.1.100` (it may be different for your Wifi network). This tells the ESP32 device to connect to your NextJS frontend and Deno server running on your local machine. All services should be on the same Wifi network.

6. **Setup the ESP32 Device Wifi**

Build and upload the firmware to your ESP32 device. The ESP32 should open an `ELATO-DEVICE` captive portal to connect to Wifi. Connect to it and go to `http://192.168.4.1` to configure the device wifi.

7. Once your Wifi credentials are configured, turn the device OFF and ON again and it should connect to your Wifi and your server.
8. Now you can talk to your AI Character!

## 🚀 Ready to Launch?

1. Register your device by adding your ESP32 Device’s MAC Address and a unique user code to the `devices` table in Supabase.

> **Pro Tip:** To find your ESP32-S3 Device’s MAC Address, build and upload `test/print_mac_address_test.cpp` using PlatformIO and view the serial monitor.

2. On your frontend client in the [Settings page](http://localhost:3000/home/settings), add the unique user code so that the device is linked to your account in Supabase.
3. If you’re testing locally, you can keep enabled the `DEV_MODE` macro in `firmware-arduino/Config.h` and the Deno server env variable to use your local IP addresses for testing.
4. Now you can register multiple devices to your account by repeating the process above.

## Project Architecture

ElatoAI consists of three main components:

1. **Frontend Client** (`Next.js` hosted on Vercel) - to create and talk to your AI agents and ‘send’ it to your ESP32 device
2. **Edge Server Functions** (`Deno` running on Deno/Supabase Edge) - to handle the websocket connections from the ESP32 device and the OpenAI API calls
3. **ESP32 IoT Client** (`PlatformIO/Arduino`) - to receive the websocket connections from the Edge Server Functions and send audio to the OpenAI API via the Deno edge server.

## 🌟 Key Features

1. **Realtime Speech-to-Speech**: Instant speech conversion powered by OpenAI’s Realtime APIs.
2. **Create Custom AI Agents**: Create custom agents with different personalities and voices.
3. **Customizable Voices**: Choose from a variety of voices and personalities.
4. **Secure WebSockets**: Reliable, encrypted WebSocket communication.
5. **Server VAD Turn Detection**: Intelligent conversation flow handling for smooth interactions.
6. **Opus Audio Compression**: High-quality audio streaming with minimal bandwidth.
7. **Global Edge Performance**: Low latency Deno Edge Functions ensuring seamless global conversations.
8. **ESP32 Arduino Framework**: Optimized and easy-to-use hardware integration.
9. **Conversation History**: View your conversation history.
10. **Device Management and Authentication**: Register and manage your devices.
11. **User Authentication**: Secure user authentication and authorization.
12. **Conversations with WebRTC and Websockets**: Talk to your AI with WebRTC on the NextJS webapp and with websockets on the ESP32.
13. **Volume Control**: Control the volume of the ESP32 speaker from the NextJS webapp.
14. **Realtime Transcripts**: The realtime transcripts of your conversations are stored in the Supabase DB.
15. **OTA Updates**: Over the Air Updates for the ESP32 firmware.
16. **Wifi Management with captive portal**: Connect to your Wifi network from the ESP32 device.
17. **Factory Reset**: Factory reset the ESP32 device from the NextJS webapp.
18. **Button and Touch Support**: Use the button OR touch sensor to control the ESP32 device.
19. **No PSRAM Required**: The ESP32 device does not require PSRAM to run the speech to speech AI.
20. **OAuth for Web client**: OAuth for your users to manage their AI characters and devices.

## 🛠 Tech Stack

| Component | Technology Used |
| --- | --- |
| Frontend | Next.js, Vercel |
| Backend | Supabase DB |
| Edge Functions | Edge Functions on Deno / Supabase Edge Runtime |
| IoT Client | PlatformIO, Arduino Framework, ESP32-S3 |
| Audio Codec | Opus |
| Communication | Secure WebSockets |
| Libraries | ArduinoJson, WebSockets, AsyncWebServer, ESP32\_Button, Arduino Audio Tools, ArduinoLibOpus |

## 📈 Core Use Cases

We have a [Usecases.md](https://github.com/akdeb/ElatoAI/tree/main/Usecases.md) file that outlines the core use cases for the [Elato AI device](https://www.elatoai.com/products) or any other custom conversational AI device.

## 🗺️ High-Level Flow

![App Screenshots](https://raw.githubusercontent.com/openai/openai-cookbook/refs/heads/main/examples/voice_solutions/arduino_ai_speech_assets/flowchart.png)

## Project Structure

![App Screenshots](https://raw.githubusercontent.com/openai/openai-cookbook/refs/heads/main/examples/voice_solutions/arduino_ai_speech_assets/structure.png)

## ⚙️ PlatformIO Config

[env:esp32-s3-devkitc-1]
platform = espressif32 @ 6.10.0
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200

lib_deps =
    bblanchon/ArduinoJson@^7.1.0
    links2004/WebSockets@^2.4.1
    ESP32Async/ESPAsyncWebServer@^3.7.6
    https://github.com/esp-arduino-libs/ESP32_Button.git#v0.0.1
    https://github.com/pschatzmann/arduino-audio-tools.git#v1.0.1
    https://github.com/pschatzmann/arduino-libopus.git#a1.1.0

## 📊 Important Stats

* ⚡️ **Latency**: <2s round-trip globally
* 🎧 **Audio Quality**: Opus codec at bitrate 12kbps (high clarity)
* ⏳ **Uninterrupted Conversations**: Up to 10 minutes continuous conversations
* 🌎 **Global Availability**: Optimized with edge computing with Deno

## 🛡 Security

* Secure WebSockets (WSS) for encrypted data transfers
* Optional: API Key encryption with 256-bit AES
* Supabase DB for secure authentication
* Supabase RLS for all tables

## 🚫 Limitations

* 3-4s Cold start time while connecting to edge server
* Limited to upto 10 minutes of uninterrupted conversations
* Edge server stops when wall clock time is exceeded
* No speech interruption detection on ESP32

## License

This project is licensed under the MIT License - see the <LICENSE> file for details.

---

**This example is part of the [OpenAI Cookbook](https://github.com/openai/openai-cookbook). For the full project and latest updates, check out [ElatoAI](https://github.com/akdeb/ElatoAI) and consider giving it a ⭐️ if you find it useful!**
