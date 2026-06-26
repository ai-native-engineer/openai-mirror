<!-- source: https://developers.openai.com/apps-sdk/changelog/ -->

## Search the ChatGPT docs

## June 2026

* 2026-06-12

  ### App permission controls in ChatGPT

  #### Fixes & improvements

  + ChatGPT users can now choose when connected apps ask for permission: always, before making changes, or only before important changes. Personal accounts can set global and per-app preferences, while Business and Enterprise admins control workspace and per-app defaults.

## May 2026

* 2026-05-28

  ### MCP Apps host style variables

  #### Fixes & improvements

  + ChatGPT now provides standardized MCP Apps host CSS variables through `hostContext.styles.variables` during initialization and updates them through `ui/notifications/host-context-changed` when the host theme changes, helping apps match ChatGPT’s light and dark appearance without hardcoded host-specific colors.
* 2026-05-27

  ### MCP Apps tool lifecycle updates

  #### Fixes & improvements

  + `window.openai.toolResponseMetadata` now preserves the canonical MCP tool result envelope, including hidden `_meta`, when ChatGPT launches widgets.
  + For tools that need user approval, ChatGPT now delivers widget tool input through the MCP Apps `ui/notifications/tool-input` lifecycle after approval instead of preloading it into the initial widget globals.
* 2026-05-26

  ### MCP server instructions

  #### Fixes & improvements

  + ChatGPT now reads MCP server instructions returned during initialization and uses them alongside tool metadata to understand cross-tool workflows, constraints, and server-wide guidance.
* 2026-05-06

  ### Output schema examples

  #### Fixes & improvements

  + Apps SDK and MCP server docs now show `outputSchema` in tool examples and recommend declaring one for tools that return structured content.

## March 2026

* 2026-03-25

  ### Plugin distribution guidance

  #### Fixes & improvements

  + Apps SDK docs now explain that OpenAI turns approved apps into plugins for Codex distribution, and that for now plugins are only available in Codex.
* 2026-03-24

  ### File library helpers in window.openai

  #### Fixes & improvements

  + `window.openai.selectFiles()` lets widgets pick existing files from the user’s ChatGPT file library when that library is available.
  + `window.openai.uploadFile(file, { library: true })` lets widgets save uploads into the user’s ChatGPT file library when that library is available.
* 2026-03-09

  ### Non-image file uploads

  #### Fixes & improvements

  + `window.openai.uploadFile` now supports non-image file types.

## February 2026

* 2026-02-22

  ### MCP Apps compatibility

  #### Fixes & improvements

  + ChatGPT is now fully compatible with the [MCP Apps spec](https://apps.extensions.modelcontextprotocol.io/api/).
* 2026-02-02

  ### Apps SDK updates for redirects, widget descriptions, and follow-up scrolling

  #### Fixes & improvements

  + `window.openai.openExternal({ href, redirectUrl })` supports `redirectUrl: false`, which prevents the host from appending `?redirectUrl=...` to external links.
  + `window.openai.setOpenInAppUrl({ href })` is the supported way to override the fullscreen “Open in ” destination; if you do not call it, ChatGPT keeps opening the widget’s current iframe path.
  + `openai/widgetDescription` is honored during resource construction and takes precedence over `resource.description` when present.
  + `window.openai.sendFollowUpMessage` supports a `scrollToBottom` parameter; it defaults to `true`, and you can pass `false` to opt out.

## January 2026

* 2026-01-21

  ### Company knowledge compatibility guidance

  #### Fixes & improvements

  + Added [company knowledge in ChatGPT](https://openai.com/index/introducing-company-knowledge/) compatibility guidance for the `search`/`fetch` tools. [Click here to learn more](/apps-sdk/build/mcp-server#company-knowledge-compatibility).
* 2026-01-15

  ### Session metadata for tool calls & requestModal template switching

  #### Fixes & improvements

  + Tool calls now include `_meta["openai/session"]`, an anonymized conversation id you can use to correlate requests within a ChatGPT session.
  + `window.openai.requestModal({ template })` now supports opening a different registered UI template by passing the template URI from `registerResource`.

## November 2025

* 2025-11-04

  ### Resources updates

  #### Fixes & improvements

  + Published a new [Apps SDK state management](/apps-sdk/build/state-management) guide.
  + Added copy functionality to all code snippets.
  + Launched a unified developers [changelog](/changelog).
