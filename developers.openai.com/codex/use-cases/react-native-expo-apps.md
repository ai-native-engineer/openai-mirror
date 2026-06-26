<!-- source: https://developers.openai.com/codex/use-cases/react-native-expo-apps/ -->

## Search the Codex docs

Codex use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Build React Native apps with Expo

Go from a mobile-app idea to a working Expo app with the dedicated plugin.

Difficulty **Intermediate**

Time horizon **1h**

Use Codex with the Expo plugin to scaffold React Native apps, stay inside Expo Router and Expo-native package conventions, test quickly with Expo Go, and move to dev clients or EAS builds only when the app needs them.

## Best for

* Developers who want to prototype or ship a React Native app with Expo before reaching for native IDE workflows.
* Expo Router projects where Codex should follow Expo conventions for routing, UI, package installs, builds, and deployment.
* Developers that need to migrate a web app to a mobile app.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/react-native-expo-apps/?export=pdf)

Use Codex with the Expo plugin to scaffold React Native apps, stay inside Expo Router and Expo-native package conventions, test quickly with Expo Go, and move to dev clients or EAS builds only when the app needs them.

Intermediate

1h

Related links

[Expo plugin](https://docs.expo.dev/skills/)  [Expo MCP Server setup](https://docs.expo.dev/eas/ai/mcp/)

## Best for

* Developers who want to prototype or ship a React Native app with Expo before reaching for native IDE workflows.
* Expo Router projects where Codex should follow Expo conventions for routing, UI, package installs, builds, and deployment.
* Developers that need to migrate a web app to a mobile app.

## Skills & Plugins

* [Expo](https://docs.expo.dev/skills/)

  Use Expo-authored skills for Expo Router UI, native-feeling components, data fetching, dev clients, deployment, upgrades, modules, and Codex Run action wiring.

| Skill | Why use it |
| --- | --- |
| [Expo](https://docs.expo.dev/skills/) | Use Expo-authored skills for Expo Router UI, native-feeling components, data fetching, dev clients, deployment, upgrades, modules, and Codex Run action wiring. |

## Starter prompt

Use the Expo plugin to build a React Native app with Expo for this idea:
[describe the app idea, target users, and the main workflow]
Requirements:
- Start with Expo Router and Expo-native project conventions.
- Try `npx expo start` and Expo Go first before creating a custom build.
- Use `npx expo install` for Expo packages so dependencies stay compatible.
- Use native-feeling UI patterns for navigation, forms, lists, empty states, and loading states.
Deliver:
- the working app slice
- the run command
- the verification path you used, including Expo Go, device, simulator, dev client, or EAS

Open in the Codex app

Use the Expo plugin to build a React Native app with Expo for this idea:
[describe the app idea, target users, and the main workflow]
Requirements:
- Start with Expo Router and Expo-native project conventions.
- Try `npx expo start` and Expo Go first before creating a custom build.
- Use `npx expo install` for Expo packages so dependencies stay compatible.
- Use native-feeling UI patterns for navigation, forms, lists, empty states, and loading states.
Deliver:
- the working app slice
- the run command
- the verification path you used, including Expo Go, device, simulator, dev client, or EAS

## Start with Expo Go

Expo is a strong default when you want Codex to move from a mobile-app idea to a
tested React Native app. The useful loop is `expo start` first, Expo Go
on a device next, and then a dev client or EAS build only when the app needs
custom native code, store distribution, or a capability that Expo Go can’t run.

That keeps Codex focused on the app workflow instead of spending the first pass
on native IDE setup, simulator setup, provisioning, or build configuration.

## Use the Expo plugin

Expo published an [Expo plugin](https://docs.expo.dev/skills/) that gives Codex Expo-native guidance for Expo Router, native UI, forms,
navigation, animations, data fetching, NativeWind setup, Expo modules, dev
clients, deployment, upgrades, and Codex Run action wiring.

Use it when Codex is building new Expo screens, adding packages, wiring API
calls, preparing a dev client, or getting an app ready for TestFlight, App
Store, Play Store, or EAS Hosting.

Optionally, add the [Expo MCP Server](https://docs.expo.dev/eas/ai/mcp/) when the task needs current
Expo documentation lookup, compatible package installation, EAS build and
workflow operations, screenshots, simulator interaction, React Native DevTools,
or TestFlight data.

## Iteration process

1. Ask Codex to inspect the repo and confirm whether it is a new Expo app or an
   existing Expo project.
2. Start with Expo Router and Expo Go, and use `npx expo install` when adding
   Expo packages.
3. Ask Codex to build one complete workflow with native-feeling navigation,
   loading states, empty states, and error states.
4. Verify on the fastest available path, such as Expo Go on a device or a
   simulator, then move to a dev client or EAS only when needed.

## Suggested follow-up prompt

Use the Expo plugin to add the following [feature/screen/flow] to this app:
[describe one feature, screen or user flow]
Constraints:
- Keep Expo Router as the routing layer.
- Use Expo-compatible package installs.
- Test with Expo Go first.
- Move to dev client or EAS only if this feature requires it.
After implementing, tell me the exact run path you used and what you verified.

## Tech stack

Need

Default options

Why it's needed

Need

Mobile framework

Default options

[Expo](https://expo.dev/)  and  [React Native](https://reactnative.dev/)

Why it's needed

Expo gives Codex a managed React Native path with fast iteration, compatible packages, and deployment tooling.

Need

Routing

Default options

[Expo Router](https://docs.expo.dev/router/introduction/)

Why it's needed

Expo Router keeps navigation file-based and predictable, which helps Codex add screens and flows without inventing a custom routing layer.

| Need | Default options | Why it's needed |
| --- | --- | --- |
| Mobile framework | [Expo](https://expo.dev/)  and  [React Native](https://reactnative.dev/) | Expo gives Codex a managed React Native path with fast iteration, compatible packages, and deployment tooling. |
| Routing | [Expo Router](https://docs.expo.dev/router/introduction/) | Expo Router keeps navigation file-based and predictable, which helps Codex add screens and flows without inventing a custom routing layer. |

## Related use cases

[![](/codex/use-cases/idea-to-proof-of-concept.webp)

### Get from idea to proof of concept

Use Codex with ImageGen to turn a rough idea into a visual direction, implement the smallest...

Front-end  Engineering](/codex/use-cases/idea-to-proof-of-concept)[![](/codex/use-cases/browser-games.webp)

### Create browser-based games

Use Codex to turn a game brief into first a well-defined plan, and then a real browser-based...

Engineering  Code](/codex/use-cases/browser-games)[![](/codex/use-cases/ios-app-intents.webp)

### Add iOS app intents

Use Codex and the Build iOS Apps plugin to identify the actions and entities your app should...

iOS  Code](/codex/use-cases/ios-app-intents)
