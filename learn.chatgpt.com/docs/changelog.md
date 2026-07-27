<!-- source: https://learn.chatgpt.com/docs/changelog -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionOverview

[All updates](/codex/changelog)  [General](/codex/changelog?type=general)  [ChatGPT desktop app](/codex/changelog?type=codex-app)  [Remote](/codex/changelog?type=codex-mobile)  [Codex CLI](/codex/changelog?type=codex-cli)

[July 2026](#month-2026-07)  [June 2026](#month-2026-06)  [May 2026](#month-2026-05)  [April 2026](#month-2026-04)  [March 2026](#month-2026-03)  [February 2026](#month-2026-02)  [January 2026](#month-2026-01)  [December 2025](#month-2025-12)  [November 2025](#month-2025-11)  [October 2025](#month-2025-10)  [September 2025](#month-2025-09)  [August 2025](#month-2025-08)  [June 2025](#month-2025-06)  [May 2025](#month-2025-05)

## July 2026

* 2026-07-23

  ### ChatGPT Voice and multi-folder projects 26.715

  Powered by GPT-Live, ChatGPT Voice lets you talk through work and coordinate
  tasks in Chat, Work, and Codex in the ChatGPT desktop app.

  Start a new chat or task in voice mode, then ask ChatGPT to start, check, or
  steer work in other threads. On macOS, turn on **Screen context** to share an
  [appshot](/codex/appshots) of your frontmost window.

  Voice is available with Plus, Pro, Business, Edu, and Enterprise plans in the
  desktop app and through [Remote on iOS](/codex/remote-connections#set-up-mobile-access).

  Local projects in the ChatGPT desktop app can now include multiple related
  folders. From a project’s menu, select **Edit project** to add folders and choose
  the primary folder. New chats, Git operations, and automatic discovery of
  `AGENTS.md`, skills, and `config.toml` use the primary folder. Secondary
  folders remain available for file search, reading, and editing.

  Get started with [ChatGPT Voice](/codex/features/voice) and [multi-folder local
  projects](/codex/projects#use-local-projects-for-folders-and-codebases).
* 2026-07-21

  ### Codex CLI 0.145.0

  ```
  $ npm install -g @openai/codex@0.145.0
  ```

    View details 

  ## New Features

  + Added experimental paginated thread history with efficient resume, search, persisted names, sub-agent support, and memories. ([#33364](https://github.com/openai/codex/pull/33364), [#33907](https://github.com/openai/codex/pull/33907), [#34085](https://github.com/openai/codex/pull/34085), [#34229](https://github.com/openai/codex/pull/34229), [#34386](https://github.com/openai/codex/pull/34386))
  + Expanded `/import` to migrate Cursor and Claude Code settings, MCP servers, plugins, sessions, commands, and project-scoped memories. ([#31672](https://github.com/openai/codex/pull/31672), [#33411](https://github.com/openai/codex/pull/33411), [#33426](https://github.com/openai/codex/pull/33426), [#33444](https://github.com/openai/codex/pull/33444))
  + Added experimental Amazon Bedrock login, custom endpoint and authentication support, and GPT-5.6 Sol as the default Bedrock model. ([#31327](https://github.com/openai/codex/pull/31327), [#33170](https://github.com/openai/codex/pull/33170), [#33175](https://github.com/openai/codex/pull/33175), [#32288](https://github.com/openai/codex/pull/32288), [#33695](https://github.com/openai/codex/pull/33695))
  + Added audio inputs and tool outputs, including common local audio formats, and introduced streaming realtime V3 conversations. ([#33261](https://github.com/openai/codex/pull/33261), [#33856](https://github.com/openai/codex/pull/33856), [#33932](https://github.com/openai/codex/pull/33932), [#34080](https://github.com/openai/codex/pull/34080), [#34385](https://github.com/openai/codex/pull/34385))
  + Stabilized the opt-in multi-agent V2 experience with configurable sub-agent models, reasoning levels, concurrency, restored roles, and improved agent navigation. ([#33550](https://github.com/openai/codex/pull/33550), [#33631](https://github.com/openai/codex/pull/33631), [#33657](https://github.com/openai/codex/pull/33657), [#33841](https://github.com/openai/codex/pull/33841), [#34383](https://github.com/openai/codex/pull/34383))
  + Added secure, clickable inline visualization links in the terminal UI. ([#33925](https://github.com/openai/codex/pull/33925), [#34217](https://github.com/openai/codex/pull/34217), [#34346](https://github.com/openai/codex/pull/34346))

  ## Bug Fixes

  + Editing an earlier prompt or retrying a safety-buffered turn now creates a contextual branch, preserving the original conversation, attachments, and mention bindings. ([#33201](https://github.com/openai/codex/pull/33201), [#33207](https://github.com/openai/codex/pull/33207), [#33211](https://github.com/openai/codex/pull/33211))
  + Improved terminal responsiveness for long conversations and streamed output through incremental Markdown rendering, fewer redraws, caching, and bounded command output. ([#34045](https://github.com/openai/codex/pull/34045), [#34049](https://github.com/openai/codex/pull/34049), [#34216](https://github.com/openai/codex/pull/34216), [#34223](https://github.com/openai/codex/pull/34223), [#34359](https://github.com/openai/codex/pull/34359))
  + Prevented slow or conflicting MCP startup and authentication flows by enforcing startup timeouts, avoiding blocking OAuth discovery, serializing refreshes, and reusing tool catalogs safely. ([#32229](https://github.com/openai/codex/pull/32229), [#32781](https://github.com/openai/codex/pull/32781), [#32825](https://github.com/openai/codex/pull/32825), [#33184](https://github.com/openai/codex/pull/33184), [#33297](https://github.com/openai/codex/pull/33297))
  + Improved Windows execution and sandbox reliability, including native exec-server sandboxing, network-proxy enforcement, hidden helper consoles, and correctly quoted hook commands. ([#32849](https://github.com/openai/codex/pull/32849), [#32857](https://github.com/openai/codex/pull/32857), [#33926](https://github.com/openai/codex/pull/33926), [#34423](https://github.com/openai/codex/pull/34423))
  + Fixed compact release-metadata parsing and macOS code-mode installation, with an in-process fallback when the external code-mode host is unavailable. ([#31667](https://github.com/openai/codex/pull/31667), [#31876](https://github.com/openai/codex/pull/31876), [#31899](https://github.com/openai/codex/pull/31899))
  + Strengthened safety and approval handling with better forced-`rm` detection, consistent full-access confirmation, and preserved rejection reasons across tools. ([#32989](https://github.com/openai/codex/pull/32989), [#33464](https://github.com/openai/codex/pull/33464), [#34400](https://github.com/openai/codex/pull/34400))

  ## Documentation

  + Updated the bundled OpenAI Docs skill with current GPT-5.6 model resolution, prompting, and migration guidance across macOS, Linux, and Windows. ([#31842](https://github.com/openai/codex/pull/31842), [#33121](https://github.com/openai/codex/pull/33121))

  ## Chores

  + Migrated bundled GPT-5.4 selections and internal uses to the corresponding GPT-5.6 Terra and Luna variants. ([#33173](https://github.com/openai/codex/pull/33173))
  + Reduced startup and large-context overhead with concurrent skill/plugin discovery and more efficient remote compaction. ([#31566](https://github.com/openai/codex/pull/31566), [#33369](https://github.com/openai/codex/pull/33369), [#33423](https://github.com/openai/codex/pull/33423), [#34431](https://github.com/openai/codex/pull/34431))
  + Updated the packaged ripgrep binary to 15.2.0. ([#34384](https://github.com/openai/codex/pull/34384))

  ## Changelog

  Full Changelog: [rust-v0.144.0...rust-v0.145.0](https://github.com/openai/codex/compare/rust-v0.144.0...rust-v0.145.0)

  + [#31667](https://github.com/openai/codex/pull/31667) fix: parse compact release metadata in installer [@efrazer-oai](https://github.com/efrazer-oai)
  + [#31362](https://github.com/openai/codex/pull/31362) core: route realtime and memories through HTTP client factory [@bolinfest](https://github.com/bolinfest)
  + [#31566](https://github.com/openai/codex/pull/31566) perf(skills): reuse walk inventory for host loading [@jif-oai](https://github.com/jif-oai)
  + [#31576](https://github.com/openai/codex/pull/31576) Bound exec-server process event reordering [@jif-oai](https://github.com/jif-oai)
  + [#31756](https://github.com/openai/codex/pull/31756) test(skills): assert symlinked metadata loading [@jif-oai](https://github.com/jif-oai)
  + [#31581](https://github.com/openai/codex/pull/31581) Resolve selected capability roots without starting executors [@jif-oai](https://github.com/jif-oai)
  + [#31789](https://github.com/openai/codex/pull/31789) Stop persisting RMCP service traces [@jif-oai](https://github.com/jif-oai)
  + [#31792](https://github.com/openai/codex/pull/31792) Summarize streamed response item logs [@jif-oai](https://github.com/jif-oai)
  + [#31791](https://github.com/openai/codex/pull/31791) Filter routine Hyper logs from SQLite [@jif-oai](https://github.com/jif-oai)
  + [#31790](https://github.com/openai/codex/pull/31790) Reduce MCP tool-list trace volume [@jif-oai](https://github.com/jif-oai)
  + [#31804](https://github.com/openai/codex/pull/31804) Stabilize the memories feature flag [@jif-oai](https://github.com/jif-oai)
  + [#31803](https://github.com/openai/codex/pull/31803) fix(mcp): default Apps product SKU to codex [@alecbarber-oai](https://github.com/alecbarber-oai)
  + [#31745](https://github.com/openai/codex/pull/31745) code-mode: retain shared MCP types for deferred tools [@sayan-oai](https://github.com/sayan-oai)
  + [#31672](https://github.com/openai/codex/pull/31672) Import enabled plugins from known marketplaces [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#31652](https://github.com/openai/codex/pull/31652) fix(tui): hide empty reasoning summaries [@fcoury-oai](https://github.com/fcoury-oai)
  + [#31767](https://github.com/openai/codex/pull/31767) Remove the network proxy config wrapper [@jif-oai](https://github.com/jif-oai)
  + [#31481](https://github.com/openai/codex/pull/31481) fix: forward originator to Codex Apps MCP [@raquel-openai](https://github.com/raquel-openai)
  + [#31363](https://github.com/openai/codex/pull/31363) codex-api: route file uploads through HTTP client factory [@bolinfest](https://github.com/bolinfest)
  + [#31813](https://github.com/openai/codex/pull/31813) tui: update safety buffering copy [@etraut-openai](https://github.com/etraut-openai)
  + [#31830](https://github.com/openai/codex/pull/31830) fix(sandboxing): initialize network proxy config inline [@fcoury-oai](https://github.com/fcoury-oai)
  + [#31431](https://github.com/openai/codex/pull/31431) build: ratchet direct reqwest dependencies [@bolinfest](https://github.com/bolinfest)
  + [#31876](https://github.com/openai/codex/pull/31876) code-mode: fix installation on darwin [@cconger](https://github.com/cconger)
  + [#31842](https://github.com/openai/codex/pull/31842) Update bundled OpenAI Docs skill for GPT-5.6 [@kkahadze-oai](https://github.com/kkahadze-oai)
  + [#31637](https://github.com/openai/codex/pull/31637) login: route raw auth flows through HTTP client [@bolinfest](https://github.com/bolinfest)
  + [#31686](https://github.com/openai/codex/pull/31686) [codex-apps] Filter optional file fields by tool schema [@tsarlandie-oai](https://github.com/tsarlandie-oai)
  + [#31899](https://github.com/openai/codex/pull/31899) code-mode: fall back to using in process v8 if we fail to resolve external process [@cconger](https://github.com/cconger)
  + [#31805](https://github.com/openai/codex/pull/31805) Bound remote MCP stdio lines [@jif-oai](https://github.com/jif-oai)
  + [#30293](https://github.com/openai/codex/pull/30293) Resolve and pin MCP OAuth credential stores [@stevenlee-oai](https://github.com/stevenlee-oai)
  + [#31892](https://github.com/openai/codex/pull/31892) exec-server: materialize filesystem workspace roots [@pakrym-oai](https://github.com/pakrym-oai)
  + [#31327](https://github.com/openai/codex/pull/31327) feat: add managed Bedrock login API [@celia-oai](https://github.com/celia-oai)
  + [#31295](https://github.com/openai/codex/pull/31295) bench: add codex help e2e macrobenchmark [@anp-oai](https://github.com/anp-oai)
  + [#31428](https://github.com/openai/codex/pull/31428) bench: add e2e benchmark entrypoints [@anp-oai](https://github.com/anp-oai)
  + [#31937](https://github.com/openai/codex/pull/31937) exec-server: expose process helper to outer sandbox [@pakrym-oai](https://github.com/pakrym-oai)
  + [#32093](https://github.com/openai/codex/pull/32093) Remove the legacy exec policy engine [@copyberry](https://github.com/copyberry)
  + [#32106](https://github.com/openai/codex/pull/32106) Reduce startup latency for ancestor discovery [@copyberry](https://github.com/copyberry)
  + [#32112](https://github.com/openai/codex/pull/32112) Bound streamed exec-server HTTP response bodies [@copyberry](https://github.com/copyberry)
  + [#32122](https://github.com/openai/codex/pull/32122) Test the shared exec-server HTTP response byte budget [@copyberry](https://github.com/copyberry)
  + [#32123](https://github.com/openai/codex/pull/32123) Bound exec-server stdio JSON-RPC messages [@copyberry](https://github.com/copyberry)
  + [#32126](https://github.com/openai/codex/pull/32126) Test bounded concurrency in ancestor discovery [@copyberry](https://github.com/copyberry)
  + [#32134](https://github.com/openai/codex/pull/32134) Test stdio JSON-RPC size limits with LF and CRLF [@copyberry](https://github.com/copyberry)
  + [#32135](https://github.com/openai/codex/pull/32135) Propagate tracing subscribers to exec start tasks [@copyberry](https://github.com/copyberry)
  + [#32150](https://github.com/openai/codex/pull/32150) Keep unified exec output collection bounded [@copyberry](https://github.com/copyberry)
  + [#32193](https://github.com/openai/codex/pull/32193) Validate memory consolidation artifacts before succeeding [@copyberry](https://github.com/copyberry)
  + [#32197](https://github.com/openai/codex/pull/32197) Rebind memory consolidation workspace roots [@copyberry](https://github.com/copyberry)
  + [#32200](https://github.com/openai/codex/pull/32200) Add a skill invocation extension contributor [@copyberry](https://github.com/copyberry)
  + [#32206](https://github.com/openai/codex/pull/32206) Always send reasoning parameters in Responses requests [@copyberry](https://github.com/copyberry)
  + [#32213](https://github.com/openai/codex/pull/32213) Generate unique IDs for review rollout messages [@copyberry](https://github.com/copyberry)
  + [#32214](https://github.com/openai/codex/pull/32214) Propagate workspace roots to exec-server sandboxes [@copyberry](https://github.com/copyberry)
  + [#32229](https://github.com/openai/codex/pull/32229) Serialize MCP OAuth credential refreshes [@copyberry](https://github.com/copyberry)
  + [#32231](https://github.com/openai/codex/pull/32231) Support pending remote environment registration [@copyberry](https://github.com/copyberry)
  + [#32232](https://github.com/openai/codex/pull/32232) Let permission hooks resolve strict auto-review requests [@copyberry](https://github.com/copyberry)
  + [#32234](https://github.com/openai/codex/pull/32234) Add dedicated storage for paginated thread history [@copyberry](https://github.com/copyberry)
  + [#32246](https://github.com/openai/codex/pull/32246) Extract reverse JSONL scanning from session indexing [@copyberry](https://github.com/copyberry)
  + [#32256](https://github.com/openai/codex/pull/32256) Improve Responses WebSocket timing telemetry [@copyberry](https://github.com/copyberry)
  + [#32261](https://github.com/openai/codex/pull/32261) Preserve local path conventions in automatic approvals [@copyberry](https://github.com/copyberry)
  + [#32263](https://github.com/openai/codex/pull/32263) Include start times in terminal turn events [@copyberry](https://github.com/copyberry)
  + [#32272](https://github.com/openai/codex/pull/32272) Expose scheduled tasks in plugin details [@copyberry](https://github.com/copyberry)
  + [#32274](https://github.com/openai/codex/pull/32274) Remove the personality migration [@copyberry](https://github.com/copyberry)
  + [#32276](https://github.com/openai/codex/pull/32276) Repair unterminated rollout files before appending [@copyberry](https://github.com/copyberry)
  + [#32277](https://github.com/openai/codex/pull/32277) Honor `personality = "none"` in model instructions [@copyberry](https://github.com/copyberry)
  + [#32280](https://github.com/openai/codex/pull/32280) Include terminal errors in turn completion events [@copyberry](https://github.com/copyberry)
  + [#32286](https://github.com/openai/codex/pull/32286) Clarify waiting behavior in safety buffering prompts [@copyberry](https://github.com/copyberry)
  + [#32288](https://github.com/openai/codex/pull/32288) Make GPT-5.6 Sol the default Bedrock model [@copyberry](https://github.com/copyberry)
  + [#32289](https://github.com/openai/codex/pull/32289) Persist paginated items in the local thread store [@copyberry](https://github.com/copyberry)
  + [#32290](https://github.com/openai/codex/pull/32290) Respect model support for reasoning summaries [@copyberry](https://github.com/copyberry)
  + [#32301](https://github.com/openai/codex/pull/32301) Trust hooks from materialized workspace plugins [@copyberry](https://github.com/copyberry)
  + [#32302](https://github.com/openai/codex/pull/32302) Prefer the Codex home socket for Unix IDE context [@copyberry](https://github.com/copyberry)
  + [#32305](https://github.com/openai/codex/pull/32305) Improve file blob upload diagnostics [@copyberry](https://github.com/copyberry)
  + [#32312](https://github.com/openai/codex/pull/32312) Require prefixes for outbound response item IDs [@copyberry](https://github.com/copyberry)
  + [#32316](https://github.com/openai/codex/pull/32316) Stop falling back to older model availability announcements [@copyberry](https://github.com/copyberry)
  + [#32326](https://github.com/openai/codex/pull/32326) Use canonical links in the moved config notice [@copyberry](https://github.com/copyberry)
  + [#32332](https://github.com/openai/codex/pull/32332) Add ordinals to paginated rollout records [@copyberry](https://github.com/copyberry)
  + [#32441](https://github.com/openai/codex/pull/32441) Preserve parent sandbox enforcement for memory consolidation [@copyberry](https://github.com/copyberry)
  + [#32460](https://github.com/openai/codex/pull/32460) Emit thread-idle lifecycle after guardian interrupts [@copyberry](https://github.com/copyberry)
  + [#32461](https://github.com/openai/codex/pull/32461) Expand tabs when rendering TUI diffs [@copyberry](https://github.com/copyberry)
  + [#32485](https://github.com/openai/codex/pull/32485) Use available width for skill names in the toggle view [@copyberry](https://github.com/copyberry)
  + [#32628](https://github.com/openai/codex/pull/32628) Improve composer completion target resolution [@copyberry](https://github.com/copyberry)
  + [#32698](https://github.com/openai/codex/pull/32698) Extract connector runtime snapshot management [@copyberry](https://github.com/copyberry)
  + [#32744](https://github.com/openai/codex/pull/32744) Log missing personality messages at trace level [@copyberry](https://github.com/copyberry)
  + [#32746](https://github.com/openai/codex/pull/32746) Make advanced reasoning selection explicit in the TUI [@copyberry](https://github.com/copyberry)
  + [#32747](https://github.com/openai/codex/pull/32747) Align Guardian reviews with session configuration [@copyberry](https://github.com/copyberry)
  + [#32749](https://github.com/openai/codex/pull/32749) Expose model overrides for multi-agent v2 spawns [@copyberry](https://github.com/copyberry)
  + [#32751](https://github.com/openai/codex/pull/32751) Restrict spawned-agent models to the active backend [@copyberry](https://github.com/copyberry)
  + [#32761](https://github.com/openai/codex/pull/32761) Add shadow metrics for lexical skill selection [@copyberry](https://github.com/copyberry)
  + [#32768](https://github.com/openai/codex/pull/32768) Align shadow skill selection with observable sources [@copyberry](https://github.com/copyberry)
  + [#32780](https://github.com/openai/codex/pull/32780) Enable skill search shadow selection by default [@copyberry](https://github.com/copyberry)
  + [#32781](https://github.com/openai/codex/pull/32781) Apply MCP startup timeouts during client creation [@copyberry](https://github.com/copyberry)
  + [#32801](https://github.com/openai/codex/pull/32801) Refactor OAuth store lock contention tests [@copyberry](https://github.com/copyberry)
  + [#32822](https://github.com/openai/codex/pull/32822) Make explicit multi-agent mode override proactive delegation [@copyberry](https://github.com/copyberry)
  + [#32825](https://github.com/openai/codex/pull/32825) Avoid blocking thread startup on MCP OAuth discovery [@copyberry](https://github.com/copyberry)
  + [#32835](https://github.com/openai/codex/pull/32835) Forward turn metadata in standalone web search [@copyberry](https://github.com/copyberry)
  + [#32837](https://github.com/openai/codex/pull/32837) Restore V2 agent identities on root thread resume [@copyberry](https://github.com/copyberry)
  + [#32838](https://github.com/openai/codex/pull/32838) Reap exited PID-managed app-server children [@copyberry](https://github.com/copyberry)
  + [#32844](https://github.com/openai/codex/pull/32844) Expand millisecond duration histogram boundaries [@copyberry](https://github.com/copyberry)
  + [#32849](https://github.com/openai/codex/pull/32849) Hide Windows filesystem helper console windows [@copyberry](https://github.com/copyberry)
  + [#32857](https://github.com/openai/codex/pull/32857) Require the elevated Windows sandbox for network proxies [@copyberry](https://github.com/copyberry)
  + [#32858](https://github.com/openai/codex/pull/32858) Persist slash-command popup dismissal [@copyberry](https://github.com/copyberry)
  + [#32864](https://github.com/openai/codex/pull/32864) Coalesce concurrent Windows sandbox setup requests [@copyberry](https://github.com/copyberry)
  + [#32866](https://github.com/openai/codex/pull/32866) Allow responses after image generation [@copyberry](https://github.com/copyberry)
  + [#32867](https://github.com/openai/codex/pull/32867) Include connector IDs in MCP tool call analytics [@copyberry](https://github.com/copyberry)
  + [#32875](https://github.com/openai/codex/pull/32875) Use model catalog policies for Guardian auto review [@copyberry](https://github.com/copyberry)
  + [#32881](https://github.com/openai/codex/pull/32881) Broaden remote compaction model fallback [@copyberry](https://github.com/copyberry)
  + [#32884](https://github.com/openai/codex/pull/32884) Prepare external agent migration for source adapters [@copyberry](https://github.com/copyberry)
  + [#32887](https://github.com/openai/codex/pull/32887) Tag shell tool telemetry by command category [@copyberry](https://github.com/copyberry)
  + [#32891](https://github.com/openai/codex/pull/32891) Attach connector caches to diagnostic uploads [@copyberry](https://github.com/copyberry)
  + [#32894](https://github.com/openai/codex/pull/32894) Serialize plugin install requests [@copyberry](https://github.com/copyberry)
  + [#32896](https://github.com/openai/codex/pull/32896) Load model context from a bounded rollout suffix [@copyberry](https://github.com/copyberry)
  + [#32897](https://github.com/openai/codex/pull/32897) Route blocked network requests to their owning calls [@copyberry](https://github.com/copyberry)
  + [#32898](https://github.com/openai/codex/pull/32898) Expose structured standalone web search results [@copyberry](https://github.com/copyberry)
  + [#32899](https://github.com/openai/codex/pull/32899) Add exec-server environment status checks [@copyberry](https://github.com/copyberry)
  + [#32900](https://github.com/openai/codex/pull/32900) Derive collaboration settings from turn context [@copyberry](https://github.com/copyberry)
  + [#32903](https://github.com/openai/codex/pull/32903) Include session IDs in tool item analytics events [@copyberry](https://github.com/copyberry)
  + [#32905](https://github.com/openai/codex/pull/32905) Timestamp app-server notifications at emission [@copyberry](https://github.com/copyberry)
  + [#32911](https://github.com/openai/codex/pull/32911) Allow injecting the models manager into `ThreadManager` [@copyberry](https://github.com/copyberry)
  + [#32920](https://github.com/openai/codex/pull/32920) Expose environment status through app-server [@copyberry](https://github.com/copyberry)
  + [#32923](https://github.com/openai/codex/pull/32923) Materialize paginated thread history in SQLite [@copyberry](https://github.com/copyberry)
  + [#32928](https://github.com/openai/codex/pull/32928) Resume thread history projection from its SQLite checkpoint [@copyberry](https://github.com/copyberry)
  + [#32945](https://github.com/openai/codex/pull/32945) Restrict Guardian reviewer tools [@copyberry](https://github.com/copyberry)
  + [#32949](https://github.com/openai/codex/pull/32949) Tighten recommended plugin install suggestions [@copyberry](https://github.com/copyberry)
  + [#32952](https://github.com/openai/codex/pull/32952) Scope runtime workspace roots to execution environments [@copyberry](https://github.com/copyberry)
  + [#32985](https://github.com/openai/codex/pull/32985) Expose exact per-response usage in raw app-server events [@copyberry](https://github.com/copyberry)
  + [#32989](https://github.com/openai/codex/pull/32989) Always confirm before enabling full access [@copyberry](https://github.com/copyberry)
  + [#33013](https://github.com/openai/codex/pull/33013) Bound exec-server JSON-RPC decoding complexity [@copyberry](https://github.com/copyberry)
  + [#33026](https://github.com/openai/codex/pull/33026) Include raw response completions in TypeScript envelopes [@copyberry](https://github.com/copyberry)
  + [#33030](https://github.com/openai/codex/pull/33030) Remove task messages from `list_agents` output [@copyberry](https://github.com/copyberry)
  + [#33031](https://github.com/openai/codex/pull/33031) Preserve JSON number precision in exec-server RPC messages [@copyberry](https://github.com/copyberry)
  + [#33035](https://github.com/openai/codex/pull/33035) Use session IDs for prompt cache keys [@copyberry](https://github.com/copyberry)
  + [#33040](https://github.com/openai/codex/pull/33040) Send plugin analytics with API key authentication [@copyberry](https://github.com/copyberry)
  + [#33076](https://github.com/openai/codex/pull/33076) Add an agent extension runner [@copyberry](https://github.com/copyberry)
  + [#33093](https://github.com/openai/codex/pull/33093) Preserve streamed output during capped history replay [@copyberry](https://github.com/copyberry)
  + [#33105](https://github.com/openai/codex/pull/33105) Fix TUI status visibility around streamed output [@copyberry](https://github.com/copyberry)
  + [#33107](https://github.com/openai/codex/pull/33107) Preserve special filesystem subpaths as wire strings [@copyberry](https://github.com/copyberry)
  + [#33109](https://github.com/openai/codex/pull/33109) Reject forks of paginated threads [@copyberry](https://github.com/copyberry)
  + [#33113](https://github.com/openai/codex/pull/33113) Allow injecting the Codex Apps tools cache [@copyberry](https://github.com/copyberry)
  + [#33121](https://github.com/openai/codex/pull/33121) Refine GPT-5.6 prompting and migration guidance [@copyberry](https://github.com/copyberry)
  + [#33147](https://github.com/openai/codex/pull/33147) Support model catalog permission messages [@copyberry](https://github.com/copyberry)
  + [#33149](https://github.com/openai/codex/pull/33149) Build MCP tool runtimes before router planning [@copyberry](https://github.com/copyberry)
  + [#33150](https://github.com/openai/codex/pull/33150) Clarify exec yield timing on Windows [@copyberry](https://github.com/copyberry)
  + [#33152](https://github.com/openai/codex/pull/33152) Support paginated thread history in app-server list APIs [@copyberry](https://github.com/copyberry)
  + [#33155](https://github.com/openai/codex/pull/33155) Trace startup prewarm tasks [@copyberry](https://github.com/copyberry)
  + [#33156](https://github.com/openai/codex/pull/33156) Run detached reviews as review-agent turns [@copyberry](https://github.com/copyberry)
  + [#33159](https://github.com/openai/codex/pull/33159) Move sleep items to the extension-owned lifecycle path [@copyberry](https://github.com/copyberry)
  + [#33166](https://github.com/openai/codex/pull/33166) Defer Noise environment connections until registration [@copyberry](https://github.com/copyberry)
  + [#33167](https://github.com/openai/codex/pull/33167) Document the Windows exec yield time range [@copyberry](https://github.com/copyberry)
  + [#33170](https://github.com/openai/codex/pull/33170) Support Amazon Bedrock login in the app server [@copyberry](https://github.com/copyberry)
  + [#33173](https://github.com/openai/codex/pull/33173) Migrate GPT-5.4 uses to GPT-5.6 variants [@copyberry](https://github.com/copyberry)
  + [#33175](https://github.com/openai/codex/pull/33175) Handle Amazon Bedrock credentials during logout [@copyberry](https://github.com/copyberry)
  + [#33177](https://github.com/openai/codex/pull/33177) Support model catalog templates for Guardian policy prompts [@copyberry](https://github.com/copyberry)
  + [#33180](https://github.com/openai/codex/pull/33180) Serialize concurrent MCP stdin writes [@copyberry](https://github.com/copyberry)
  + [#33182](https://github.com/openai/codex/pull/33182) Preserve plugin install failure subtypes during imports [@copyberry](https://github.com/copyberry)
  + [#33184](https://github.com/openai/codex/pull/33184) Reuse MCP tool catalogs across sessions [@copyberry](https://github.com/copyberry)
  + [#33185](https://github.com/openai/codex/pull/33185) Keep approval test targets in the temporary home [@copyberry](https://github.com/copyberry)
  + [#33187](https://github.com/openai/codex/pull/33187) Honor workspace spend controls in rate-limit handling [@copyberry](https://github.com/copyberry)
  + [#33198](https://github.com/openai/codex/pull/33198) Keep interrupted prompts in conversation history [@copyberry](https://github.com/copyberry)
  + [#33200](https://github.com/openai/codex/pull/33200) Separate exec permission paths from core models [@copyberry](https://github.com/copyberry)
  + [#33201](https://github.com/openai/codex/pull/33201) Branch conversations when editing earlier TUI prompts [@copyberry](https://github.com/copyberry)
  + [#33203](https://github.com/openai/codex/pull/33203) Preserve in-flight state when restoring thread input [@copyberry](https://github.com/copyberry)
  + [#33207](https://github.com/openai/codex/pull/33207) Retry safety-buffered turns on a forked thread [@copyberry](https://github.com/copyberry)
  + [#33209](https://github.com/openai/codex/pull/33209) Separate session state from session I/O [@copyberry](https://github.com/copyberry)
  + [#33211](https://github.com/openai/codex/pull/33211) Preserve thread context when retrying or editing turns [@copyberry](https://github.com/copyberry)
  + [#33213](https://github.com/openai/codex/pull/33213) Prepare Python SDK 0.144.4 stable release [@copyberry](https://github.com/copyberry)
  + [#33223](https://github.com/openai/codex/pull/33223) Instrument environment and plugin resolution paths [@copyberry](https://github.com/copyberry)
  + [#33232](https://github.com/openai/codex/pull/33232) Disambiguate skill mentions from shell parameters [@copyberry](https://github.com/copyberry)
  + [#33237](https://github.com/openai/codex/pull/33237) Fix skill completion around bound mentions with suffixes [@copyberry](https://github.com/copyberry)
  + [#33239](https://github.com/openai/codex/pull/33239) Render TUI composer tabs as single-column spaces [@copyberry](https://github.com/copyberry)
  + [#33243](https://github.com/openai/codex/pull/33243) Add auto-compaction fallback token-budget settings [@copyberry](https://github.com/copyberry)
  + [#33251](https://github.com/openai/codex/pull/33251) Report selected environment connection transitions [@copyberry](https://github.com/copyberry)
  + [#33255](https://github.com/openai/codex/pull/33255) Add a fallback phase before automatic context rollover [@copyberry](https://github.com/copyberry)
  + [#33261](https://github.com/openai/codex/pull/33261) Add Frameless Bidi support for realtime conversations [@copyberry](https://github.com/copyberry)
  + [#33297](https://github.com/openai/codex/pull/33297) Allow MCP servers to opt out of tool catalog caching [@copyberry](https://github.com/copyberry)
  + [#33308](https://github.com/openai/codex/pull/33308) Expand MCP tool catalog cache regression coverage [@copyberry](https://github.com/copyberry)
  + [#33364](https://github.com/openai/codex/pull/33364) Enable paginated thread history in app-server [@copyberry](https://github.com/copyberry)
  + [#33367](https://github.com/openai/codex/pull/33367) Respect final-answer boundaries for queued agent mail [@copyberry](https://github.com/copyberry)
  + [#33369](https://github.com/openai/codex/pull/33369) Scan skill roots concurrently [@copyberry](https://github.com/copyberry)
  + [#33373](https://github.com/openai/codex/pull/33373) Render TUI prompts before submitting user turns [@copyberry](https://github.com/copyberry)
  + [#33411](https://github.com/openai/codex/pull/33411) Migrate plugin commands into skills on install [@copyberry](https://github.com/copyberry)
  + [#33412](https://github.com/openai/codex/pull/33412) Refactor world-state rendering tests into snapshots [@copyberry](https://github.com/copyberry)
  + [#33414](https://github.com/openai/codex/pull/33414) Expose connector candidates from imported sessions [@copyberry](https://github.com/copyberry)
  + [#33421](https://github.com/openai/codex/pull/33421) Fetch workspace connectors concurrently [@copyberry](https://github.com/copyberry)
  + [#33423](https://github.com/openai/codex/pull/33423) Load executor plugin declarations concurrently [@copyberry](https://github.com/copyberry)
  + [#33424](https://github.com/openai/codex/pull/33424) Attribute OpenAI docs MCP requests to Codex [@copyberry](https://github.com/copyberry)
  + [#33425](https://github.com/openai/codex/pull/33425) Refresh host skill catalogs through world state [@copyberry](https://github.com/copyberry)
  + [#33426](https://github.com/openai/codex/pull/33426) Add Cursor support to setup import [@copyberry](https://github.com/copyberry)
  + [#33427](https://github.com/openai/codex/pull/33427) Propagate deferred environment capability roots to MCP [@copyberry](https://github.com/copyberry)
  + [#33430](https://github.com/openai/codex/pull/33430) Avoid creating metadata paths in the Windows sandbox [@copyberry](https://github.com/copyberry)
  + [#33432](https://github.com/openai/codex/pull/33432) Preserve paginated history for spawned subagents [@copyberry](https://github.com/copyberry)
  + [#33435](https://github.com/openai/codex/pull/33435) Warn on conflicting capability root locations [@copyberry](https://github.com/copyberry)
  + [#33441](https://github.com/openai/codex/pull/33441) Shut down Codex threads after approval scenarios [@copyberry](https://github.com/copyberry)
  + [#33444](https://github.com/openai/codex/pull/33444) Add external agent memory migration [@copyberry](https://github.com/copyberry)
  + [#33445](https://github.com/openai/codex/pull/33445) Select the elevated Windows sandbox for network proxies [@copyberry](https://github.com/copyberry)
  + [#33446](https://github.com/openai/codex/pull/33446) Remove the unused network proxy loader [@copyberry](https://github.com/copyberry)
  + [#33454](https://github.com/openai/codex/pull/33454) Track prompt cache write token usage [@copyberry](https://github.com/copyberry)
  + [#33456](https://github.com/openai/codex/pull/33456) Move external agent migration into its crate [@copyberry](https://github.com/copyberry)
  + [#33457](https://github.com/openai/codex/pull/33457) Use final answers in turn history summaries [@copyberry](https://github.com/copyberry)
  + [#33459](https://github.com/openai/codex/pull/33459) Allow more time for image generation in code mode [@copyberry](https://github.com/copyberry)
  + [#33464](https://github.com/openai/codex/pull/33464) Strengthen forced `rm` command detection [@copyberry](https://github.com/copyberry)
  + [#33467](https://github.com/openai/codex/pull/33467) Remove template IDs from MCP tool call metadata [@copyberry](https://github.com/copyberry)
  + [#33500](https://github.com/openai/codex/pull/33500) Add cache-write tokens to the raw response schema [@copyberry](https://github.com/copyberry)
  + [#33509](https://github.com/openai/codex/pull/33509) Preserve encrypted content in MCP tool outputs [@copyberry](https://github.com/copyberry)
  + [#33550](https://github.com/openai/codex/pull/33550) Unify multi-agent settings under `agents` [@copyberry](https://github.com/copyberry)
  + [#33572](https://github.com/openai/codex/pull/33572) Expose spawn agent types only when roles are configured [@copyberry](https://github.com/copyberry)
  + [#33605](https://github.com/openai/codex/pull/33605) Add fielded BM25 to shadow skill selection [@copyberry](https://github.com/copyberry)
  + [#33613](https://github.com/openai/codex/pull/33613) Add character n-gram skill selection [@copyberry](https://github.com/copyberry)
  + [#33614](https://github.com/openai/codex/pull/33614) Add multi-query lexical skill selection [@copyberry](https://github.com/copyberry)
  + [#33631](https://github.com/openai/codex/pull/33631) Honor configured model defaults for spawned agents [@copyberry](https://github.com/copyberry)
  + [#33632](https://github.com/openai/codex/pull/33632) Remove generated-default filesystem path variants [@copyberry](https://github.com/copyberry)
  + [#33633](https://github.com/openai/codex/pull/33633) Clarify when to wait for starting environments [@copyberry](https://github.com/copyberry)
  + [#33636](https://github.com/openai/codex/pull/33636) Clarify when to wait for starting environments [@copyberry](https://github.com/copyberry)
  + [#33639](https://github.com/openai/codex/pull/33639) Remove the unused realtime WebRTC crate [@copyberry](https://github.com/copyberry)
  + [#33640](https://github.com/openai/codex/pull/33640) Avoid duplicate cached app list update notifications [@copyberry](https://github.com/copyberry)
  + [#33645](https://github.com/openai/codex/pull/33645) Run `write_stdin` concurrently across terminal sessions [@copyberry](https://github.com/copyberry)
  + [#33651](https://github.com/openai/codex/pull/33651) Add an app-server API for reading app metadata [@copyberry](https://github.com/copyberry)
  + [#33656](https://github.com/openai/codex/pull/33656) Validate reasoning effort after applying spawn roles [@copyberry](https://github.com/copyberry)
  + [#33657](https://github.com/openai/codex/pull/33657) Restore agent roles when reloading v2 sub-agents [@copyberry](https://github.com/copyberry)
  + [#33658](https://github.com/openai/codex/pull/33658) Keep active-turn environments stable across settings updates [@copyberry](https://github.com/copyberry)
  + [#33659](https://github.com/openai/codex/pull/33659) Require data URLs for code-mode image output [@copyberry](https://github.com/copyberry)
  + [#33665](https://github.com/openai/codex/pull/33665) Refresh step world state for all sessions [@copyberry](https://github.com/copyberry)
  + [#33677](https://github.com/openai/codex/pull/33677) Forward thread originators from standalone extensions [@copyberry](https://github.com/copyberry)
  + [#33680](https://github.com/openai/codex/pull/33680) Reword the apply\_patch tool description [@copyberry](https://github.com/copyberry)
  + [#33683](https://github.com/openai/codex/pull/33683) Preserve scope and provenance for imported agent memory [@copyberry](https://github.com/copyberry)
  + [#33684](https://github.com/openai/codex/pull/33684) Extract TUI approval request payloads into structs [@copyberry](https://github.com/copyberry)
  + [#33687](https://github.com/openai/codex/pull/33687) Avoid unnecessary writes during migration repair [@copyberry](https://github.com/copyberry)
  + [#33695](https://github.com/openai/codex/pull/33695) Support custom transports for Amazon Bedrock [@copyberry](https://github.com/copyberry)
  + [#33841](https://github.com/openai/codex/pull/33841) Make parent-owned sub-agent threads read-only in the TUI [@copyberry](https://github.com/copyberry)
  + [#33842](https://github.com/openai/codex/pull/33842) Give the zsh fork decline test more execution time [@copyberry](https://github.com/copyberry)
  + [#33843](https://github.com/openai/codex/pull/33843) Add an API for reading installed app runtime state [@copyberry](https://github.com/copyberry)
  + [#33845](https://github.com/openai/codex/pull/33845) Confirm usage-limit resets before redemption [@copyberry](https://github.com/copyberry)
  + [#33848](https://github.com/openai/codex/pull/33848) Fix the managed Bedrock logout test assertion [@copyberry](https://github.com/copyberry)
  + [#33851](https://github.com/openai/codex/pull/33851) Record web search result payload sizes [@copyberry](https://github.com/copyberry)
  + [#33852](https://github.com/openai/codex/pull/33852) Add batched executor capability discovery [@copyberry](https://github.com/copyberry)
  + [#33855](https://github.com/openai/codex/pull/33855) Tag realtime transcript tail flush delegations [@copyberry](https://github.com/copyberry)
  + [#33856](https://github.com/openai/codex/pull/33856) Stream realtime V3 Codex handoff output [@copyberry](https://github.com/copyberry)
  + [#33858](https://github.com/openai/codex/pull/33858) Isolate core tests from shell and rollout persistence [@copyberry](https://github.com/copyberry)
  + [#33861](https://github.com/openai/codex/pull/33861) Test workspace write isolation across exec servers [@copyberry](https://github.com/copyberry)
  + [#33862](https://github.com/openai/codex/pull/33862) Suppress empty multi-agent mode messages [@copyberry](https://github.com/copyberry)
  + [#33863](https://github.com/openai/codex/pull/33863) Report detailed session import error types [@copyberry](https://github.com/copyberry)
  + [#33864](https://github.com/openai/codex/pull/33864) Keep feature tests focused on behavior [@copyberry](https://github.com/copyberry)
  + [#33866](https://github.com/openai/codex/pull/33866) Remove the redundant tool dispatch wrapper [@copyberry](https://github.com/copyberry)
  + [#33867](https://github.com/openai/codex/pull/33867) Add grace period to code-mode yield timeouts [@copyberry](https://github.com/copyberry)
  + [#33868](https://github.com/openai/codex/pull/33868) Remove stale ignored core tests [@copyberry](https://github.com/copyberry)
  + [#33870](https://github.com/openai/codex/pull/33870) Remove the redundant borrowed line wrapping helper [@copyberry](https://github.com/copyberry)
  + [#33872](https://github.com/openai/codex/pull/33872) Remove unused TUI collaboration mode indicators [@copyberry](https://github.com/copyberry)
  + [#33876](https://github.com/openai/codex/pull/33876) Track collaboration mode instructions in world state [@copyberry](https://github.com/copyberry)
  + [#33883](https://github.com/openai/codex/pull/33883) Report CLI as the external agent config import source [@copyberry](https://github.com/copyberry)
  + [#33889](https://github.com/openai/codex/pull/33889) Centralize thread MCP connections in `McpRuntime` [@copyberry](https://github.com/copyberry)
  + [#33892](https://github.com/openai/codex/pull/33892) Limit rollout metadata reads to headers [@copyberry](https://github.com/copyberry)
  + [#33893](https://github.com/openai/codex/pull/33893) Track realtime conversation state in world state [@copyberry](https://github.com/copyberry)
  + [#33895](https://github.com/openai/codex/pull/33895) Add SessionEnd hooks for thread teardown [@copyberry](https://github.com/copyberry)
  + [#33896](https://github.com/openai/codex/pull/33896) Expose plugin installation interstitial requirements [@copyberry](https://github.com/copyberry)
  + [#33901](https://github.com/openai/codex/pull/33901) Support ChatGPT-branded Desktop app builds [@copyberry](https://github.com/copyberry)
  + [#33902](https://github.com/openai/codex/pull/33902) Add bounded batch lookups for message history [@copyberry](https://github.com/copyberry)
  + [#33903](https://github.com/openai/codex/pull/33903) Route realtime V3 handoffs by response channel [@copyberry](https://github.com/copyberry)
  + [#33905](https://github.com/openai/codex/pull/33905) Batch persistent history reads during reverse search [@copyberry](https://github.com/copyberry)
  + [#33906](https://github.com/openai/codex/pull/33906) Launch managed network proxies on remote executors [@copyberry](https://github.com/copyberry)
  + [#33907](https://github.com/openai/codex/pull/33907) Add occurrence search for paginated threads [@copyberry](https://github.com/copyberry)
  + [#33908](https://github.com/openai/codex/pull/33908) Allow publishing plugins through share updates [@copyberry](https://github.com/copyberry)
  + [#33921](https://github.com/openai/codex/pull/33921) Preserve sub-agent liveness in the agent picker [@copyberry](https://github.com/copyberry)
  + [#33922](https://github.com/openai/codex/pull/33922) Allow selecting path-backed agents in the TUI picker [@copyberry](https://github.com/copyberry)
  + [#33923](https://github.com/openai/codex/pull/33923) Add audio variants to user input protocols [@copyberry](https://github.com/copyberry)
  + [#33925](https://github.com/openai/codex/pull/33925) Render inline visualization links in the TUI [@copyberry](https://github.com/copyberry)
  + [#33926](https://github.com/openai/codex/pull/33926) Fix quoted hook commands on Windows [@copyberry](https://github.com/copyberry)
  + [#33929](https://github.com/openai/codex/pull/33929) Handle audio inputs and Bazel unit test arguments [@copyberry](https://github.com/copyberry)
  + [#33930](https://github.com/openai/codex/pull/33930) Track inherited paginated rollout prefixes [@copyberry](https://github.com/copyberry)
  + [#33932](https://github.com/openai/codex/pull/33932) Forward audio inputs to the Responses API [@copyberry](https://github.com/copyberry)
  + [#33938](https://github.com/openai/codex/pull/33938) Centralize SQLite connection configuration [@copyberry](https://github.com/copyberry)
  + [#33944](https://github.com/openai/codex/pull/33944) Track permission instructions in world state [@copyberry](https://github.com/copyberry)
  + [#33950](https://github.com/openai/codex/pull/33950) Let users remember the working directory for resumed sessions [@copyberry](https://github.com/copyberry)
  + [#33961](https://github.com/openai/codex/pull/33961) Refresh bundled model metadata [@copyberry](https://github.com/copyberry)
  + [#33963](https://github.com/openai/codex/pull/33963) Add context to sampling retry logs [@copyberry](https://github.com/copyberry)
  + [#33982](https://github.com/openai/codex/pull/33982) Gate audio history by model input modalities [@copyberry](https://github.com/copyberry)
  + [#34038](https://github.com/openai/codex/pull/34038) Handle compressed rollouts in doctor thread inventory [@copyberry](https://github.com/copyberry)
  + [#34045](https://github.com/openai/codex/pull/34045) Render streamed Markdown incrementally [@copyberry](https://github.com/copyberry)
  + [#34047](https://github.com/openai/codex/pull/34047) Avoid resending the model for reasoning shortcuts [@copyberry](https://github.com/copyberry)
  + [#34049](https://github.com/openai/codex/pull/34049) Avoid redundant TUI redraws while streaming [@copyberry](https://github.com/copyberry)
  + [#34067](https://github.com/openai/codex/pull/34067) Seed realtime V3 sessions with initial text items [@copyberry](https://github.com/copyberry)
  + [#34080](https://github.com/openai/codex/pull/34080) Add audio output support to dynamic tools and code mode [@copyberry](https://github.com/copyberry)
  + [#34085](https://github.com/openai/codex/pull/34085) Support legacy views for paginated thread history [@copyberry](https://github.com/copyberry)
  + [#34194](https://github.com/openai/codex/pull/34194) Avoid cloning thread data when rendering transcripts [@copyberry](https://github.com/copyberry)
  + [#34197](https://github.com/openai/codex/pull/34197) Use the Markdown collector as the streaming source of truth [@copyberry](https://github.com/copyberry)
  + [#34198](https://github.com/openai/codex/pull/34198) Start side conversations without replaying inherited turns [@copyberry](https://github.com/copyberry)
  + [#34199](https://github.com/openai/codex/pull/34199) Avoid liveness races when starting side conversations [@copyberry](https://github.com/copyberry)
  + [#34204](https://github.com/openai/codex/pull/34204) Avoid cloning buffered TUI history lines [@copyberry](https://github.com/copyberry)
  + [#34206](https://github.com/openai/codex/pull/34206) Avoid retaining decoded MCP images in history cells [@copyberry](https://github.com/copyberry)
  + [#34216](https://github.com/openai/codex/pull/34216) Speed up TUI Markdown layout [@copyberry](https://github.com/copyberry)
  + [#34217](https://github.com/openai/codex/pull/34217) Keep incremental rendering with visualization context [@copyberry](https://github.com/copyberry)
  + [#34218](https://github.com/openai/codex/pull/34218) Track TUI command completion separately from output [@copyberry](https://github.com/copyberry)
  + [#34222](https://github.com/openai/codex/pull/34222) Avoid buffering replay-irrelevant thread notifications [@copyberry](https://github.com/copyberry)
  + [#34223](https://github.com/openai/codex/pull/34223) Cache finalized Markdown history rendering [@copyberry](https://github.com/copyberry)
  + [#34224](https://github.com/openai/codex/pull/34224) Avoid cloning file changes in TUI diff rendering [@copyberry](https://github.com/copyberry)
  + [#34226](https://github.com/openai/codex/pull/34226) Backfill completion items only for the active exec turn [@copyberry](https://github.com/copyberry)
  + [#34229](https://github.com/openai/codex/pull/34229) Persist names for paginated threads [@copyberry](https://github.com/copyberry)
  + [#34232](https://github.com/openai/codex/pull/34232) Remeasure dynamic cells in the transcript overlay [@copyberry](https://github.com/copyberry)
  + [#34234](https://github.com/openai/codex/pull/34234) Avoid redundant TUI subagent metadata requests [@copyberry](https://github.com/copyberry)
  + [#34271](https://github.com/openai/codex/pull/34271) Migrate legacy exec policy allow rules [@copyberry](https://github.com/copyberry)
  + [#34293](https://github.com/openai/codex/pull/34293) Preserve zsh tied PATH exports in shell snapshots [@copyberry](https://github.com/copyberry)
  + [#34344](https://github.com/openai/codex/pull/34344) Reject unsupported history modes when loading rollouts [@copyberry](https://github.com/copyberry)
  + [#34345](https://github.com/openai/codex/pull/34345) Remove unused Rust helpers [@copyberry](https://github.com/copyberry)
  + [#34346](https://github.com/openai/codex/pull/34346) Track inline visualization directives during streaming [@copyberry](https://github.com/copyberry)
  + [#34347](https://github.com/openai/codex/pull/34347) Avoid cloning deferred TUI lifecycle payloads [@copyberry](https://github.com/copyberry)
  + [#34348](https://github.com/openai/codex/pull/34348) Cache TUI flex heights across frame passes [@copyberry](https://github.com/copyberry)
  + [#34355](https://github.com/openai/codex/pull/34355) Parallelize TUI bootstrap requests [@copyberry](https://github.com/copyberry)
  + [#34357](https://github.com/openai/codex/pull/34357) Render streamed command output through preview iterators [@copyberry](https://github.com/copyberry)
  + [#34359](https://github.com/openai/codex/pull/34359) Keep streamed command output bounded in the TUI [@copyberry](https://github.com/copyberry)
  + [#34361](https://github.com/openai/codex/pull/34361) Avoid cloning thread history for token usage replay [@copyberry](https://github.com/copyberry)
  + [#34365](https://github.com/openai/codex/pull/34365) Animate Max and Ultra reasoning effort changes [@copyberry](https://github.com/copyberry)
  + [#34366](https://github.com/openai/codex/pull/34366) Avoid cloning hyperlink text during TUI rendering [@copyberry](https://github.com/copyberry)
  + [#34368](https://github.com/openai/codex/pull/34368) Use app-server skill metadata directly in the TUI [@copyberry](https://github.com/copyberry)
  + [#34371](https://github.com/openai/codex/pull/34371) Clear stale Guardian reviews when turns end [@copyberry](https://github.com/copyberry)
  + [#34375](https://github.com/openai/codex/pull/34375) Extend second-based latency histogram buckets [@copyberry](https://github.com/copyberry)
  + [#34378](https://github.com/openai/codex/pull/34378) Avoid rendering generated images twice [@copyberry](https://github.com/copyberry)
  + [#34380](https://github.com/openai/codex/pull/34380) Stop retrying turns with invalid tool images [@copyberry](https://github.com/copyberry)
  + [#34381](https://github.com/openai/codex/pull/34381) Avoid cloning Responses WebSocket payloads [@copyberry](https://github.com/copyberry)
  + [#34382](https://github.com/openai/codex/pull/34382) Keep paginated thread Git metadata in SQLite [@copyberry](https://github.com/copyberry)
  + [#34383](https://github.com/openai/codex/pull/34383) Mark multi-agent v2 as stable [@copyberry](https://github.com/copyberry)
  + [#34384](https://github.com/openai/codex/pull/34384) Update packaged ripgrep to 15.2.0 [@copyberry](https://github.com/copyberry)
  + [#34385](https://github.com/openai/codex/pull/34385) Preserve audio across history and tool outputs [@copyberry](https://github.com/copyberry)
  + [#34386](https://github.com/openai/codex/pull/34386) Enable memories for paginated threads [@copyberry](https://github.com/copyberry)
  + [#34387](https://github.com/openai/codex/pull/34387) Refresh bundled model metadata [@copyberry](https://github.com/copyberry)
  + [#34389](https://github.com/openai/codex/pull/34389) Route Codex Apps MCP through plugin service [@copyberry](https://github.com/copyberry)
  + [#34390](https://github.com/openai/codex/pull/34390) Use copy-on-write storage for history snapshots [@copyberry](https://github.com/copyberry)
  + [#34392](https://github.com/openai/codex/pull/34392) Ignore inherited ACEs when refreshing Windows write roots [@copyberry](https://github.com/copyberry)
  + [#34393](https://github.com/openai/codex/pull/34393) Add configurable hook context spill limits [@copyberry](https://github.com/copyberry)
  + [#34396](https://github.com/openai/codex/pull/34396) Run compact session-start hooks before turn continuation [@copyberry](https://github.com/copyberry)
  + [#34400](https://github.com/openai/codex/pull/34400) Propagate approval rejection reasons [@copyberry](https://github.com/copyberry)
  + [#34403](https://github.com/openai/codex/pull/34403) Update tests for history and hook API changes [@copyberry](https://github.com/copyberry)
  + [#34407](https://github.com/openai/codex/pull/34407) Resolve paginated rollout lineages [@copyberry](https://github.com/copyberry)
  + [#34408](https://github.com/openai/codex/pull/34408) Support threadless MCP connections without event channels [@copyberry](https://github.com/copyberry)
  + [#34409](https://github.com/openai/codex/pull/34409) Limit the Linux `/proc` preflight filesystem view [@copyberry](https://github.com/copyberry)
  + [#34411](https://github.com/openai/codex/pull/34411) Require absolute paths for test SQLite configuration [@copyberry](https://github.com/copyberry)
  + [#34413](https://github.com/openai/codex/pull/34413) Remove CSV-backed agent jobs [@copyberry](https://github.com/copyberry)
  + [#34416](https://github.com/openai/codex/pull/34416) Show completed hook warnings in TUI headers [@copyberry](https://github.com/copyberry)
  + [#34417](https://github.com/openai/codex/pull/34417) Enrich app/read connector metadata [@copyberry](https://github.com/copyberry)
  + [#34423](https://github.com/openai/codex/pull/34423) Support Windows sandboxing in the exec server [@copyberry](https://github.com/copyberry)
  + [#34429](https://github.com/openai/codex/pull/34429) Move shared skill models into `codex-skills` [@copyberry](https://github.com/copyberry)
  + [#34431](https://github.com/openai/codex/pull/34431) Optimize remote compaction history handling [@copyberry](https://github.com/copyberry)
  + [#34434](https://github.com/openai/codex/pull/34434) Support catalog messages for non-request approval policies [@copyberry](https://github.com/copyberry)
  + [#34435](https://github.com/openai/codex/pull/34435) Resolve outbound proxy routes explicitly [@copyberry](https://github.com/copyberry)
  + [#34436](https://github.com/openai/codex/pull/34436) Honor managed permission profiles in network proxy resolution [@copyberry](https://github.com/copyberry)
  + [#34438](https://github.com/openai/codex/pull/34438) Increase the patch approval test timeout [@copyberry](https://github.com/copyberry)
  + [#34441](https://github.com/openai/codex/pull/34441) Add buffered code-mode exec yields [@copyberry](https://github.com/copyberry)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.145.0)
* 2026-07-20

  ### ChatGPT for iOS 1.2026.195

  ### New features

  + Added support for rendering Mermaid diagrams inline in task transcripts.
  + Added support for interactive forms in Codex tasks.
  + Added support for restoring unsent prompts when switching between tasks,
    hosts, and workspaces.

  ### Improvements and bug fixes

  + Improved task lists to sort by recent activity and show unavailable hosts when
    creating a task.
  + Improved the composer with selected-text previews and smoother new-task
    transitions.
  + Improved goals with support for resuming blocked or usage-limited runs.
  + Improved plan progress, Fast controls, and inline dictation.
  + Improved Remote onboarding, composer guidance, and iPad navigation.
  + Fixed an issue that could close the app when duplicate task-list entries
    appeared while starting a task.
  + Fixed iOS 18 task actions and task-list styling.
  + Fixed composer spacing, attachment menu padding, and duplicate transcription
    indicators.
* 2026-07-18

  ### Codex CLI 0.144.6

  ```
  $ npm install -g @openai/codex@0.144.6
  ```

    View details 

  ## Bug Fixes

  + Refreshed bundled instructions for GPT-5.6 Sol, Terra, and Luna, and corrected their context windows to 272,000 tokens. ([#33972](https://github.com/openai/codex/pull/33972), [#34009](https://github.com/openai/codex/pull/34009))

  ## Changelog

  Full Changelog: [rust-v0.144.5...rust-v0.144.6](https://github.com/openai/codex/compare/rust-v0.144.5...rust-v0.144.6)

  + [#33972](https://github.com/openai/codex/pull/33972) Backport refreshed bundled model metadata to 0.144 [@sayan-oai](https://github.com/sayan-oai)
  + [#34009](https://github.com/openai/codex/pull/34009) Narrow 0.144 hotfix to GPT-5.6 prompts and context [@sayan-oai](https://github.com/sayan-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.144.6)
* 2026-07-16

  ### Codex CLI 0.144.5

  ```
  $ npm install -g @openai/codex@0.144.5
  ```

    View details 

  ## Bug Fixes

  + Improved dangerous-command detection, including more forced `rm` forms, and provides clearer rejection reasons when commands are denied. ([#33455](https://github.com/openai/codex/pull/33455))

  ## Changelog

  Full Changelog: [rust-v0.144.4...rust-v0.144.5](https://github.com/openai/codex/compare/rust-v0.144.4...rust-v0.144.5)

  + [#33455](https://github.com/openai/codex/pull/33455) [release/0.144] fix(core) expand is\_dangerous\_command [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.144.5)
* 2026-07-14

  ### Codex CLI 0.144.4

  ```
  $ npm install -g @openai/codex@0.144.4
  ```

    View details 

  ## Chores

  + No user-facing changes in this patch release.

  ## Changelog

  Full Changelog: [rust-v0.144.3...rust-v0.144.4](https://github.com/openai/codex/compare/rust-v0.144.3...rust-v0.144.4)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.144.4)
* 2026-07-13

  ### ChatGPT for iOS 1.2026.188

  ### New features

  + Added support for inline visualizations in Codex tasks.

  ### Improvements and bug fixes

  + Improved creating and managing tasks from conversations, with reliable links
    to newly created tasks.
  + Improved tool activity styling and progress indicators.
  + Improved file-opening feedback.
  + Improved the composer so controls remain visible above the keyboard for long
    prompts and larger text sizes.
  + Fixed Fast mode selection and restoration for each task.
  + Fixed initial prompts ignoring the selected approval preset.
  + Fixed autocomplete backgrounds and task rows becoming unresponsive during
    swipe gestures.
* 2026-07-13

  ### Codex CLI 0.144.3

  ```
  $ npm install -g @openai/codex@0.144.3
  ```

    View details 

  ## Chores

  + Published a version-only release with no merged pull request changes since `rust-v0.144.2`.

  ## Changelog

  Full Changelog: [rust-v0.144.2...rust-v0.144.3](https://github.com/openai/codex/compare/rust-v0.144.2...rust-v0.144.3)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.144.3)
* 2026-07-13

  ### Codex CLI 0.144.2

  ```
  $ npm install -g @openai/codex@0.144.2
  ```

    View details 

  ## Bug Fixes

  + Restored the previous Guardian auto-review policy, request format, and tool behavior after rolling back a prompting regression. ([#32672](https://github.com/openai/codex/pull/32672))

  ## Changelog

  Full Changelog: [rust-v0.144.1...rust-v0.144.2](https://github.com/openai/codex/compare/rust-v0.144.1...rust-v0.144.2)

  + [#32672](https://github.com/openai/codex/pull/32672) [release/0.144] Revert "Update auto review prompting" [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.144.2)
* 2026-07-09

  ### Codex joins the ChatGPT desktop app 26.707

  Codex is now part of the ChatGPT desktop app on macOS and Windows. Existing
  Codex app users can update as usual and keep their projects, settings, and
  workflows. You can make Codex the default view and, on macOS, keep the Codex
  app icon.

  ### New features

  + Edit Markdown and code directly in the app, use inline annotations, and ask
    Codex to revise selected content.
  + Use PR Chat to review GitHub pull requests and ask Codex about changes in
    context. Send inline review feedback, inspect proposed patches, and edit,
    accept, or reject them without leaving the app.
  + Connect custom domains to published Sites.

  ### Performance improvements and bug fixes

  + Made Computer Use faster with GPT-5.6.
  + Made task and subagent activity easier to follow while Codex works.
  + Simplified plugin management by moving it into Settings.
  + Improved permission handling when resuming tasks or sending follow-ups.
  + Added clearer Full access warnings and dialog when combinging Full access with Ultra.
  + Improved macOS and Windows setup, including macOS installation, Git-backed
    workflows, and Computer Use on Windows.
  + Fixed task resumption for local projects and onboarding retry loops.
  + Fixed scrolling in pull request reviews and expanded Mermaid diagram labels.
  + Improved mobile connection reliability and fixed video rendering for SSH
    projects.
  + Additional performance improvements and bug fixes.
* 2026-07-09

  ### Codex CLI 0.144.1

  ```
  $ npm install -g @openai/codex@0.144.1
  ```

    View details 

  ## Bug Fixes

  + Fixed standalone installs failing when GitHub returns compact or reordered release metadata. ([#31913](https://github.com/openai/codex/pull/31913))
  + Ensured macOS package installs expose the code-mode host alongside the `codex` executable. ([#31913](https://github.com/openai/codex/pull/31913))
  + Kept code mode working when the companion host binary is unavailable by falling back to the embedded runtime. ([#31913](https://github.com/openai/codex/pull/31913))

  ## Changelog

  Full Changelog: [rust-v0.144.0...rust-v0.144.1](https://github.com/openai/codex/compare/rust-v0.144.0...rust-v0.144.1)

  + [#31913](https://github.com/openai/codex/pull/31913) [0.144] Backport installer and code-mode reliability fixes [@bolinfest](https://github.com/bolinfest)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.144.1)
* 2026-07-09

  ### Codex CLI 0.144.0

  ```
  $ npm install -g @openai/codex@0.144.0
  ```

    View details 

  ## New Features

  + Usage-limit reset credits now show their type and expiration, and let you choose which credit to redeem. ([#30488](https://github.com/openai/codex/pull/30488))
  + Added a `writes` app-approval mode that allows declared read-only actions while prompting for writes. ([#30482](https://github.com/openai/codex/pull/30482))
  + MCP tools can now request authentication interactively without an experimental opt-in. ([#28772](https://github.com/openai/codex/pull/28772))
  + App-server hosts can provide Codex authentication at runtime and redirect successful logins to a hosted page. ([#28745](https://github.com/openai/codex/pull/28745), [#31274](https://github.com/openai/codex/pull/31274))
  + Global pnunen installs are now detected so diagnostics and updates use the correct package manager. ([#31503](https://github.com/openai/codex/pull/31503))
  + Selecting Ultra reasoning now warns when high multi-agent concurrency could increase usage quickly. ([#31621](https://github.com/openai/codex/pull/31621))

  ## Bug Fixes

  + Resumed ChatGPT threads recover when compaction references a retired model by retrying with the currently selected model. ([#30319](https://github.com/openai/codex/pull/30319))
  + Fixed Code Mode crashes in Intel macOS release binaries. ([#30953](https://github.com/openai/codex/pull/30953))
  + Windows sandbox sessions can delete files in writable roots and access the managed primary runtime. ([#31138](https://github.com/openai/codex/pull/31138), [#31574](https://github.com/openai/codex/pull/31574))
  + Pasted terminal control sequences can no longer corrupt TUI rendering or resumed conversation history. ([#31494](https://github.com/openai/codex/pull/31494))
  + Long-running app sessions now refresh expired authentication for the hosted `codex_apps` connector. ([#31486](https://github.com/openai/codex/pull/31486))
  + Responses WebSockets continue using the low-latency transport while respecting system proxies and custom certificate authorities. ([#31441](https://github.com/openai/codex/pull/31441), [#31622](https://github.com/openai/codex/pull/31622))

  ## Documentation

  + Device-code login warnings now explain how to recognize and stop phishing attempts. ([#31648](https://github.com/openai/codex/pull/31648))

  ## Chores

  + Reduced plugin skill-loading time on remote executors by resolving namespaces once per root. ([#31348](https://github.com/openai/codex/pull/31348))
  + Made the `/review` branch picker faster and more reliable in large repositories. ([#31464](https://github.com/openai/codex/pull/31464))
  + Improved automatic review behavior with clearer instructions and a focused tool set. ([#31480](https://github.com/openai/codex/pull/31480))
  + Made Amazon Bedrock model names clearly identify their GPT-5.6 family and variant. ([#31636](https://github.com/openai/codex/pull/31636))

  ## Changelog

  Full Changelog: [rust-v0.143.0...rust-v0.144.0](https://github.com/openai/codex/compare/rust-v0.143.0...rust-v0.144.0)

  + [#30292](https://github.com/openai/codex/pull/30292) Serialize shared MCP OAuth credential stores [@stevenlee-oai](https://github.com/stevenlee-oai)
  + [#30488](https://github.com/openai/codex/pull/30488) [codex-cli] Show reset details in redemption picker [@jayp-oai](https://github.com/jayp-oai)
  + [#31297](https://github.com/openai/codex/pull/31297) feat(core): emit canonical command execution items [@owenlin0](https://github.com/owenlin0)
  + [#31298](https://github.com/openai/codex/pull/31298) feat(core): emit canonical dynamic tool call items [@owenlin0](https://github.com/owenlin0)
  + [#31369](https://github.com/openai/codex/pull/31369) test(skills): cover plugin namespace loading [@anp-oai](https://github.com/anp-oai)
  + [#30953](https://github.com/openai/codex/pull/30953) fix(release): add missing Intel V8 signing entitlement [@malsamiri-oai](https://github.com/malsamiri-oai)
  + [#31355](https://github.com/openai/codex/pull/31355) refactor: make ExternalAuth return CodexAuth [@lt-oai](https://github.com/lt-oai)
  + [#31352](https://github.com/openai/codex/pull/31352) ci: increase Windows Bazel local test jobs [@anp-oai](https://github.com/anp-oai)
  + [#30482](https://github.com/openai/codex/pull/30482) [codex-rs] Add writes app approval mode [@zamoshchin-openai](https://github.com/zamoshchin-openai)
  + [#31439](https://github.com/openai/codex/pull/31439) Handle bio policy errors in Codex [@fc-oai](https://github.com/fc-oai)
  + [#31319](https://github.com/openai/codex/pull/31319) [codex] add connector runtime latency metrics [@mzeng-openai](https://github.com/mzeng-openai)
  + [#31312](https://github.com/openai/codex/pull/31312) Use model catalog approval messages [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)
  + [#31422](https://github.com/openai/codex/pull/31422) test: generalize exec-server fixture [@anp-oai](https://github.com/anp-oai)
  + [#28772](https://github.com/openai/codex/pull/28772) [codex] Enable auth elicitation by default [@mzeng-openai](https://github.com/mzeng-openai)
  + [#28745](https://github.com/openai/codex/pull/28745) [login] support hosted success redirects [@rafael-jac](https://github.com/rafael-jac)
  + [#31316](https://github.com/openai/codex/pull/31316) chore: extract remote compaction request attempts [@celia-oai](https://github.com/celia-oai)
  + [#31299](https://github.com/openai/codex/pull/31299) feat(core): emit canonical sub-agent activity items [@owenlin0](https://github.com/owenlin0)
  + [#31285](https://github.com/openai/codex/pull/31285) [1/5] [codex] sync managed-layer bundle schema [@hefuc-oai](https://github.com/hefuc-oai)
  + [#31300](https://github.com/openai/codex/pull/31300) feat(core): emit canonical collab tool call items [@owenlin0](https://github.com/owenlin0)
  + [#31301](https://github.com/openai/codex/pull/31301) feat(core): emit canonical collab wait items [@owenlin0](https://github.com/owenlin0)
  + [#30319](https://github.com/openai/codex/pull/30319) fix: retry rejected previous-model compaction with selected model [@celia-oai](https://github.com/celia-oai)
  + [#30879](https://github.com/openai/codex/pull/30879) Handle mixed-case URLs in Windows command safety [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#31191](https://github.com/openai/codex/pull/31191) Handle completion separators and popup dismissal [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#31425](https://github.com/openai/codex/pull/31425) test: add TestAppServer builder [@anp-oai](https://github.com/anp-oai)
  + [#31342](https://github.com/openai/codex/pull/31342) http-client: expose WebSocket proxy prerequisites [@bolinfest](https://github.com/bolinfest)
  + [#31348](https://github.com/openai/codex/pull/31348) perf(skills): resolve plugin namespaces per root [@anp-oai](https://github.com/anp-oai)
  + [#31289](https://github.com/openai/codex/pull/31289) Use canonical indexed web access field [@winston-openai](https://github.com/winston-openai)
  + [#31464](https://github.com/openai/codex/pull/31464) Speed up review branch picker via `for-each-ref` [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#31332](https://github.com/openai/codex/pull/31332) ci: parameterize Cargo target paths [@anp-oai](https://github.com/anp-oai)
  + [#31421](https://github.com/openai/codex/pull/31421) refactor: unify external auth resolution [@pakrym-oai](https://github.com/pakrym-oai)
  + [#31451](https://github.com/openai/codex/pull/31451) test: migrate TestAppServer callers to builder [@anp-oai](https://github.com/anp-oai)
  + [#31274](https://github.com/openai/codex/pull/31274) [codex] Add externally provided Codex auth [@lt-oai](https://github.com/lt-oai)
  + [#31501](https://github.com/openai/codex/pull/31501) trace hook command execution [@wiltzius-openai](https://github.com/wiltzius-openai)
  + [#31356](https://github.com/openai/codex/pull/31356) ci: run V8 source builds on Windows 2025 [@anp-oai](https://github.com/anp-oai)
  + [#31283](https://github.com/openai/codex/pull/31283) core: support extension-owned turn items [@owenlin0](https://github.com/owenlin0)
  + [#31570](https://github.com/openai/codex/pull/31570) fs: support pruning hidden directories during walks [@jif-oai](https://github.com/jif-oai)
  + [#31465](https://github.com/openai/codex/pull/31465) Align empty branch list message with search [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#31586](https://github.com/openai/codex/pull/31586) Stabilize encrypted MAv2 spawn request test [@jif-oai](https://github.com/jif-oai)
  + [#31585](https://github.com/openai/codex/pull/31585) Stabilize remote compaction parity against dynamic skill catalogs [@jif-oai](https://github.com/jif-oai)
  + [#31518](https://github.com/openai/codex/pull/31518) Log plugin install failure subtypes [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#31587](https://github.com/openai/codex/pull/31587) Stabilize shared rollout budget test [@jif-oai](https://github.com/jif-oai)
  + [#31503](https://github.com/openai/codex/pull/31503) Detect Codex installs managed by pnpm [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#31525](https://github.com/openai/codex/pull/31525) core: migrate standalone web search to extension-owned turn items [@owenlin0](https://github.com/owenlin0)
  + [#31473](https://github.com/openai/codex/pull/31473) feat(core): emit canonical review mode items [@owenlin0](https://github.com/owenlin0)
  + [#31452](https://github.com/openai/codex/pull/31452) test: remove TestAppServer constructors [@anp-oai](https://github.com/anp-oai)
  + [#31612](https://github.com/openai/codex/pull/31612) Round MCP timeout durations in error messages [@jif-oai](https://github.com/jif-oai)
  + [#31138](https://github.com/openai/codex/pull/31138) fix(windows-sandbox): allow deletion in writable roots [@fcoury-oai](https://github.com/fcoury-oai)
  + [#31500](https://github.com/openai/codex/pull/31500) code-mode: move to hosted mode by default [@cconger](https://github.com/cconger)
  + [#31494](https://github.com/openai/codex/pull/31494) tui: sanitize terminal controls in user messages [@etraut-openai](https://github.com/etraut-openai)
  + [#31524](https://github.com/openai/codex/pull/31524) chore(protocol): use UUIDv7 for generated item IDs [@owenlin0](https://github.com/owenlin0)
  + [#31496](https://github.com/openai/codex/pull/31496) Fall back to HTTP when Apple Git is unavailable [@fc-oai](https://github.com/fc-oai)
  + [#31578](https://github.com/openai/codex/pull/31578) Bound exec-server pending RPCs [@jif-oai](https://github.com/jif-oai)
  + [#29875](https://github.com/openai/codex/pull/29875) [codex] Sanitize imported session fallback titles [@stefanstokic-oai](https://github.com/stefanstokic-oai)
  + [#31621](https://github.com/openai/codex/pull/31621) tui: warn on Ultra with high multi-agent concurrency [@shijie-oai](https://github.com/shijie-oai)
  + [#31622](https://github.com/openai/codex/pull/31622) websocket-client: add proxy-aware connector [@bolinfest](https://github.com/bolinfest)
  + [#31574](https://github.com/openai/codex/pull/31574) [codex] Grant Windows sandbox access to primary runtime [@abhinav-oai](https://github.com/abhinav-oai)
  + [#31292](https://github.com/openai/codex/pull/31292) Reuse MCP tool snapshot within a sampling request [@sayan-oai](https://github.com/sayan-oai)
  + [#31630](https://github.com/openai/codex/pull/31630) feat(core): emit canonical hook prompt items [@owenlin0](https://github.com/owenlin0)
  + [#31636](https://github.com/openai/codex/pull/31636) feat: change amazon Bedrock GPT-5.6 display names [@celia-oai](https://github.com/celia-oai)
  + [#31629](https://github.com/openai/codex/pull/31629) core: stop emitting legacy command events directly [@owenlin0](https://github.com/owenlin0)
  + [#31441](https://github.com/openai/codex/pull/31441) core: preserve Responses WebSockets with system proxy [@bolinfest](https://github.com/bolinfest)
  + [#31357](https://github.com/openai/codex/pull/31357) ci: route build IO through Dev Drives [@anp-oai](https://github.com/anp-oai)
  + [#31461](https://github.com/openai/codex/pull/31461) chore: remove inert cargo audit workflow [@anp-oai](https://github.com/anp-oai)
  + [#31614](https://github.com/openai/codex/pull/31614) test: migrate app-server v2 starts to auto env [@anp-oai](https://github.com/anp-oai)
  + [#31497](https://github.com/openai/codex/pull/31497) [codex] increase tool schema compaction threshold [@fbauer33](https://github.com/fbauer33)
  + [#31650](https://github.com/openai/codex/pull/31650) code-mode: make all approvals trigger elicitation pause [@cconger](https://github.com/cconger)
  + [#31648](https://github.com/openai/codex/pull/31648) Clarify device-code phishing warning [@etraut-openai](https://github.com/etraut-openai)
  + [#31663](https://github.com/openai/codex/pull/31663) test(app-server): use native rollout fixture paths [@fcoury-oai](https://github.com/fcoury-oai)
  + [#31330](https://github.com/openai/codex/pull/31330) [codex-apps] Omit internal fields from file payloads [@jacobzhou-oai](https://github.com/jacobzhou-oai)
  + [#31480](https://github.com/openai/codex/pull/31480) Update auto review prompting [@olliem-oai](https://github.com/olliem-oai)
  + [#21818](https://github.com/openai/codex/pull/21818) Update models.json @github-actions
  + [#31427](https://github.com/openai/codex/pull/31427) test: add delayed exec-server transport [@anp-oai](https://github.com/anp-oai)
  + [#30278](https://github.com/openai/codex/pull/30278) [codex] Preserve reviewer when resuming threads [@viyatb-oai](https://github.com/viyatb-oai)
  + [#31675](https://github.com/openai/codex/pull/31675) Expand agent core ownership [@pakrym-oai](https://github.com/pakrym-oai)
  + [#31486](https://github.com/openai/codex/pull/31486) [connectors] Refresh codex\_apps /ps/mcp auth [@stevenlee-oai](https://github.com/stevenlee-oai)
  + [#31361](https://github.com/openai/codex/pull/31361) model-provider: route model discovery through HTTP client factory [@bolinfest](https://github.com/bolinfest)
  + [#30188](https://github.com/openai/codex/pull/30188) feat(rollout): persist TurnItems for paginated thread rollouts [@owenlin0](https://github.com/owenlin0)
  + [#31596](https://github.com/openai/codex/pull/31596) Use the image generation extension by default [@won-openai](https://github.com/won-openai)
  + [#31684](https://github.com/openai/codex/pull/31684) Update models.json @github-actions

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.144.0)
* 2026-07-08

  ### Codex CLI 0.143.0

  ```
  $ npm install -g @openai/codex@0.143.0
  ```

    View details 

  ## New Features

  + Remote plugins are now enabled by default, with richer catalog rows, npm marketplace sources, and visible remote/local versions. ([#30297](https://github.com/openai/codex/pull/30297), [#26705](https://github.com/openai/codex/pull/26705), [#29375](https://github.com/openai/codex/pull/29375), [#30981](https://github.com/openai/codex/pull/30981))
  + Codex can route authentication and Responses API traffic through macOS and Windows system proxies, including PAC and WPAD configurations. ([#26708](https://github.com/openai/codex/pull/26708), [#26709](https://github.com/openai/codex/pull/26709), [#31335](https://github.com/openai/codex/pull/31335))
  + Added `codex remote-control pair` for generating manual pairing codes from a running daemon. ([#29913](https://github.com/openai/codex/pull/29913))
  + Added Amazon Bedrock GPT-5.6 Sol, Terra, and Luna models, with first-class support for `max` reasoning effort. ([#30285](https://github.com/openai/codex/pull/30285), [#30467](https://github.com/openai/codex/pull/30467))
  + MCP tools now use tool search by default, and ChatGPT-hosted MCP servers can explicitly use session authentication. ([#29486](https://github.com/openai/codex/pull/29486), [#29733](https://github.com/openai/codex/pull/29733))
  + App-server clients can inspect environments, list descendant threads, and fork history through a specific turn. ([#30291](https://github.com/openai/codex/pull/30291), [#29591](https://github.com/openai/codex/pull/29591), [#30277](https://github.com/openai/codex/pull/30277))

  ## Bug Fixes

  + Fixed Windows ConPTY input handling for line endings and backspace, plus sandbox credential retry edge cases. ([#29734](https://github.com/openai/codex/pull/29734), [#29624](https://github.com/openai/codex/pull/29624), [#29637](https://github.com/openai/codex/pull/29637))
  + Fixed stale TUI safety prompts and cancelled reviews that could leave MCP startup appearing busy. ([#30490](https://github.com/openai/codex/pull/30490), [#31189](https://github.com/openai/codex/pull/31189))
  + Improved recovery when exec servers are temporarily offline and prevented remote-control token refresh retry storms. ([#30098](https://github.com/openai/codex/pull/30098), [#30201](https://github.com/openai/codex/pull/30201))
  + Preserved trailing realtime transcript text and terminal rollout events during shutdown. ([#29918](https://github.com/openai/codex/pull/29918), [#30144](https://github.com/openai/codex/pull/30144))
  + Improved incremental WebSocket request success by ignoring response metadata during comparisons. ([#30770](https://github.com/openai/codex/pull/30770))
  + Reduced installer failures from GitHub API rate limits by reusing release metadata. ([#31056](https://github.com/openai/codex/pull/31056))

  ## Documentation

  + Documented UUID7 thread and turn IDs, plus recommended remote-executor integration-test workflows. ([#27714](https://github.com/openai/codex/pull/27714), [#29790](https://github.com/openai/codex/pull/29790))

  ## Chores

  + Updated OpenSSL, Hono, fast-uri, quick-xml, and crossbeam-epoch to address security advisories. ([#29487](https://github.com/openai/codex/pull/29487), [#29650](https://github.com/openai/codex/pull/29650), [#30941](https://github.com/openai/codex/pull/30941), [#31308](https://github.com/openai/codex/pull/31308))

  ## Changelog

  Full Changelog: [rust-v0.142.0...rust-v0.143.0](https://github.com/openai/codex/compare/rust-v0.142.0...rust-v0.143.0)

  + [#26708](https://github.com/openai/codex/pull/26708) PAC 3 - Add Windows system proxy resolver [@canvrno-oai](https://github.com/canvrno-oai)
  + [#28769](https://github.com/openai/codex/pull/28769) Register full CDP requirements feature [@syuan-oai](https://github.com/syuan-oai)
  + [#29485](https://github.com/openai/codex/pull/29485) [codex] fetch featured IDs for remote plugins [@ericning-o](https://github.com/ericning-o)
  + [#29487](https://github.com/openai/codex/pull/29487) Upgrade bundled OpenSSL to 3.6.3 [@jif-oai](https://github.com/jif-oai)
  + [#29489](https://github.com/openai/codex/pull/29489) [codex] Update esbuild to 0.28.1 [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29488](https://github.com/openai/codex/pull/29488) [plugins] Add dark-mode logo metadata [@drewschuster-openai](https://github.com/drewschuster-openai)
  + [#29249](https://github.com/openai/codex/pull/29249) [codex] migrate environment context to model world state [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29494](https://github.com/openai/codex/pull/29494) core: wrap token budget window context [@bolinfest](https://github.com/bolinfest)
  + [#29417](https://github.com/openai/codex/pull/29417) [codex] replace remote images with model-visible error text [@rka-oai](https://github.com/rka-oai)
  + [#28360](https://github.com/openai/codex/pull/28360) feat(core): store turn\_id on ResponseItem metadata [@owenlin0](https://github.com/owenlin0)
  + [#29486](https://github.com/openai/codex/pull/29486) [codex] Use tool search for MCP tools by default [@sayan-oai](https://github.com/sayan-oai)
  + [#29501](https://github.com/openai/codex/pull/29501) path-uri: clarify host-native path conversion [@anp-oai](https://github.com/anp-oai)
  + [#29504](https://github.com/openai/codex/pull/29504) fix: world state response item test [@celia-oai](https://github.com/celia-oai)
  + [#26704](https://github.com/openai/codex/pull/26704) TUI Plugin Sharing 4 - cover remote plugin catalog flows [@canvrno-oai](https://github.com/canvrno-oai)
  + [#29419](https://github.com/openai/codex/pull/29419) [codex] reject remote images at app-server ingress [@rka-oai](https://github.com/rka-oai)
  + [#28992](https://github.com/openai/codex/pull/28992) chore: improve expired Bedrock credential errors [@celia-oai](https://github.com/celia-oai)
  + [#29467](https://github.com/openai/codex/pull/29467) Make formatter output quiet on success [@anp-oai](https://github.com/anp-oai)
  + [#26709](https://github.com/openai/codex/pull/26709) PAC 4 - Add macOS system proxy resolver [@canvrno-oai](https://github.com/canvrno-oai)
  + [#29490](https://github.com/openai/codex/pull/29490) chore: warn when Code Mode lacks model metadata [@celia-oai](https://github.com/celia-oai)
  + [#29493](https://github.com/openai/codex/pull/29493) mcp: accept foreign absolute cwd for remote stdio [@anp-oai](https://github.com/anp-oai)
  + [#29473](https://github.com/openai/codex/pull/29473) Propagate safety buffering treatment metadata [@fc-oai](https://github.com/fc-oai)
  + [#24092](https://github.com/openai/codex/pull/24092) [codex] Reject unlowered PowerShell AST regions [@bookholt-oai](https://github.com/bookholt-oai)
  + [#29155](https://github.com/openai/codex/pull/29155) [codex] Expose service tier and reasoning effort in OTEL [@daniel-oai](https://github.com/daniel-oai)
  + [#29068](https://github.com/openai/codex/pull/29068) [codex] stylistic changes [@rka-oai](https://github.com/rka-oai)
  + [#29518](https://github.com/openai/codex/pull/29518) Remove redundant Codex Apps manager flag [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#27946](https://github.com/openai/codex/pull/27946) [codex] Use input items for Responses Lite tools [@rka-oai](https://github.com/rka-oai)
  + [#29528](https://github.com/openai/codex/pull/29528) Centralize Codex Apps client handling [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#29577](https://github.com/openai/codex/pull/29577) Handle additional tools in image URL validation [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#29575](https://github.com/openai/codex/pull/29575) Remove redundant Codex Apps cache guard [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#29583](https://github.com/openai/codex/pull/29583) Group Codex Apps client setup [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#29358](https://github.com/openai/codex/pull/29358) Allow codex sandbox to consume MCP sandbox state [@jif-oai](https://github.com/jif-oai)
  + [#29599](https://github.com/openai/codex/pull/29599) Stop persisting bridged log events [@jif-oai](https://github.com/jif-oai)
  + [#29615](https://github.com/openai/codex/pull/29615) Fix Codex Apps auth elicitation hang [@jif-oai](https://github.com/jif-oai)
  + [#29067](https://github.com/openai/codex/pull/29067) Namespace multi-agent v2 tools under collaboration [@jif-oai](https://github.com/jif-oai)
  + [#29614](https://github.com/openai/codex/pull/29614) path-uri: add lexical containment [@jif-oai](https://github.com/jif-oai)
  + [#28426](https://github.com/openai/codex/pull/28426) Share resumed rollout history [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#29634](https://github.com/openai/codex/pull/29634) Update rmcp to 1.8.0 [@jif-oai](https://github.com/jif-oai)
  + [#29650](https://github.com/openai/codex/pull/29650) Update vulnerable Hono and fast-uri dependencies [@jif-oai](https://github.com/jif-oai)
  + [#29498](https://github.com/openai/codex/pull/29498) [codex] Instrument rollout persistence bytes [@wiltzius-openai](https://github.com/wiltzius-openai)
  + [#29659](https://github.com/openai/codex/pull/29659) [core] debounce current-time reminders by elapsed time [@rka-oai](https://github.com/rka-oai)
  + [#29608](https://github.com/openai/codex/pull/29608) Shut down superseded MCP managers on refresh [@jif-oai](https://github.com/jif-oai)
  + [#29527](https://github.com/openai/codex/pull/29527) core: use turn-owned world state for inline compaction [@sayan-oai](https://github.com/sayan-oai)
  + [#29672](https://github.com/openai/codex/pull/29672) [codex] Handle additional tools in rollout persistence metrics [@rka-oai](https://github.com/rka-oai)
  + [#29669](https://github.com/openai/codex/pull/29669) Handle additional tools in rollout persistence metrics [@winston-openai](https://github.com/winston-openai)
  + [#29680](https://github.com/openai/codex/pull/29680) Revert "Handle additional tools in rollout persistence metrics" [@rasmusrygaard](https://github.com/rasmusrygaard)
  + [#27714](https://github.com/openai/codex/pull/27714) app-server: document thread and turn IDs are UUID7 [@owenlin0](https://github.com/owenlin0)
  + [#29456](https://github.com/openai/codex/pull/29456) Prepare managed network sandbox context [@jif-oai](https://github.com/jif-oai)
  + [#28418](https://github.com/openai/codex/pull/28418) chore(core) rm AskForApproval::OnFailure [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)
  + [#29675](https://github.com/openai/codex/pull/29675) core: add extra metadata field to Thread struct [@kumquatexpress](https://github.com/kumquatexpress)
  + [#29013](https://github.com/openai/codex/pull/29013) Keep managed MITM CA private keys in proxy memory [@winston-openai](https://github.com/winston-openai)
  + [#29495](https://github.com/openai/codex/pull/29495) Separate local and remote plugin analytics IDs [@jameswt-oai](https://github.com/jameswt-oai)
  + [#29671](https://github.com/openai/codex/pull/29671) [codex] Preserve proxy state for filesystem sandbox helpers [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#29513](https://github.com/openai/codex/pull/29513) [codex] allow image generation with provider auth [@richardopenai](https://github.com/richardopenai)
  + [#29526](https://github.com/openai/codex/pull/29526) core: resolve view\_image paths in selected environment [@anp-oai](https://github.com/anp-oai)
  + [#29696](https://github.com/openai/codex/pull/29696) [codex] Fix stale approval policy in MCP test [@sayan-oai](https://github.com/sayan-oai)
  + [#29704](https://github.com/openai/codex/pull/29704) [codex] Fix stale approval policy in MCP test [@kumquatexpress](https://github.com/kumquatexpress)
  + [#29547](https://github.com/openai/codex/pull/29547) core: use current step environments for tools [@sayan-oai](https://github.com/sayan-oai)
  + [#28976](https://github.com/openai/codex/pull/28976) Add MCP tool call error metrics [@stevenlee-oai](https://github.com/stevenlee-oai)
  + [#27045](https://github.com/openai/codex/pull/27045) feat(guardian): include connected account email in app reviews [@viyatb-oai](https://github.com/viyatb-oai)
  + [#29620](https://github.com/openai/codex/pull/29620) Decouple plugin manifest path resolution [@jif-oai](https://github.com/jif-oai)
  + [#29666](https://github.com/openai/codex/pull/29666) [codex] Report the exec-server working directory [@rasmusrygaard](https://github.com/rasmusrygaard)
  + [#29705](https://github.com/openai/codex/pull/29705) feat(app-server): thread/turns/items/list -> thread/items/list [@owenlin0](https://github.com/owenlin0)
  + [#29716](https://github.com/openai/codex/pull/29716) code-mode: Rename codex\_code\_mode::CodeModeService [@cconger](https://github.com/cconger)
  + [#29712](https://github.com/openai/codex/pull/29712) test: branch on target OS instead of runner flavor [@anp-oai](https://github.com/anp-oai)
  + [#29728](https://github.com/openai/codex/pull/29728) core tests: rename automatic environment builder [@anp-oai](https://github.com/anp-oai)
  + [#29158](https://github.com/openai/codex/pull/29158) path-uri: remove legacy path deserialization [@anp-oai](https://github.com/anp-oai)
  + [#29519](https://github.com/openai/codex/pull/29519) core: persist initial context window metadata [@bolinfest](https://github.com/bolinfest)
  + [#28918](https://github.com/openai/codex/pull/28918) Make selected plugin roots URI-native [@jif-oai](https://github.com/jif-oai)
  + [#29515](https://github.com/openai/codex/pull/29515) [codex] define code mode host handshake protocol [@cconger](https://github.com/cconger)
  + [#29715](https://github.com/openai/codex/pull/29715) [codex] surface rollout budget exhaustion [@rka-oai](https://github.com/rka-oai)
  + [#29732](https://github.com/openai/codex/pull/29732) code-mode: Remove Session::is\_alive() [@cconger](https://github.com/cconger)
  + [#29626](https://github.com/openai/codex/pull/29626) Load executor skills without host path conversion [@jif-oai](https://github.com/jif-oai)
  + [#29714](https://github.com/openai/codex/pull/29714) protocol: separate app and exec RPC ownership [@anp-oai](https://github.com/anp-oai)
  + [#29664](https://github.com/openai/codex/pull/29664) refactor: extract context window token status [@bolinfest](https://github.com/bolinfest)
  + [#29665](https://github.com/openai/codex/pull/29665) fix: scope context remaining to body window [@bolinfest](https://github.com/bolinfest)
  + [#29744](https://github.com/openai/codex/pull/29744) [codex] rename rollout budget error to session budget error [@rka-oai](https://github.com/rka-oai)
  + [#29739](https://github.com/openai/codex/pull/29739) Update new\_context\_window instructions [@andmis](https://github.com/andmis)
  + [#29743](https://github.com/openai/codex/pull/29743) core: reset context for token budget compaction [@bolinfest](https://github.com/bolinfest)
  + [#29477](https://github.com/openai/codex/pull/29477) Support thread-level originator overrides [@alexsong-oai](https://github.com/alexsong-oai)
  + [#29745](https://github.com/openai/codex/pull/29745) core: add wait\_for\_environment for starting environments [@sayan-oai](https://github.com/sayan-oai)
  + [#28630](https://github.com/openai/codex/pull/28630) [codex] trace MCP startup latency [@rphilizaire-openai](https://github.com/rphilizaire-openai)
  + [#29750](https://github.com/openai/codex/pull/29750) chore: assign `amsg_` IDs to agent messages [@bolinfest](https://github.com/bolinfest)
  + [#29746](https://github.com/openai/codex/pull/29746) test: add app-server auto environment helper [@anp-oai](https://github.com/anp-oai)
  + [#29711](https://github.com/openai/codex/pull/29711) Let image generation extension hosts control output persistence [@won-openai](https://github.com/won-openai)
  + [#29762](https://github.com/openai/codex/pull/29762) [codex] Reuse compacted history replacement for new context windows [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29768](https://github.com/openai/codex/pull/29768) [codex] Update bundled skill installer guidance [@sayan-oai](https://github.com/sayan-oai)
  + [#29690](https://github.com/openai/codex/pull/29690) [plugins] Add marketplace source requirements [@xl-openai](https://github.com/xl-openai)
  + [#29765](https://github.com/openai/codex/pull/29765) [codex] Ignore local curated plugins when remote catalog is active [@xl-openai](https://github.com/xl-openai)
  + [#29767](https://github.com/openai/codex/pull/29767) [codex] Assign response item IDs in forked history [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29721](https://github.com/openai/codex/pull/29721) auth: move domain mode below app wire types [@anp-oai](https://github.com/anp-oai)
  + [#29753](https://github.com/openai/codex/pull/29753) [plugins] Enforce marketplace source admission requirements [@xl-openai](https://github.com/xl-openai)
  + [#29722](https://github.com/openai/codex/pull/29722) config: own layer provenance types [@anp-oai](https://github.com/anp-oai)
  + [#29723](https://github.com/openai/codex/pull/29723) connectors: own app metadata types [@anp-oai](https://github.com/anp-oai)
  + [#29788](https://github.com/openai/codex/pull/29788) test: run app-server integration tests under Wine [@anp-oai](https://github.com/anp-oai)
  + [#29789](https://github.com/openai/codex/pull/29789) test: use automatic environments in app-server integration tests [@anp-oai](https://github.com/anp-oai)
  + [#29790](https://github.com/openai/codex/pull/29790) docs: document remote executor integration testing [@anp-oai](https://github.com/anp-oai)
  + [#29815](https://github.com/openai/codex/pull/29815) [codex] Remove auto-compaction opt-out [@rhan-oai](https://github.com/rhan-oai)
  + [#29628](https://github.com/openai/codex/pull/29628) Keep executor plugin MCP paths URI-native [@jif-oai](https://github.com/jif-oai)
  + [#29731](https://github.com/openai/codex/pull/29731) [codex] Emit implicit skill usage for support reads [@alexsong-oai](https://github.com/alexsong-oai)
  + [#29829](https://github.com/openai/codex/pull/29829) Persist agent messages as response items [@jif-oai](https://github.com/jif-oai)
  + [#29841](https://github.com/openai/codex/pull/29841) Add a bounded filesystem walk RPC [@jif-oai](https://github.com/jif-oai)
  + [#29842](https://github.com/openai/codex/pull/29842) Use fs/walk for environment skill discovery [@jif-oai](https://github.com/jif-oai)
  + [#29567](https://github.com/openai/codex/pull/29567) [codex] show external import result counts [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#29831](https://github.com/openai/codex/pull/29831) Cache plugin namespace during executor skill discovery [@jif-oai](https://github.com/jif-oai)
  + [#29720](https://github.com/openai/codex/pull/29720) ci: fail jobs that dirty the worktree [@anp-oai](https://github.com/anp-oai)
  + [#29887](https://github.com/openai/codex/pull/29887) Fix environment skill discovery after merge [@jif-oai](https://github.com/jif-oai)
  + [#29734](https://github.com/openai/codex/pull/29734) [codex] fix Windows ConPTY input handling [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#28593](https://github.com/openai/codex/pull/28593) [codex] suppress low usage remaining warnings when credits are available [@brooks-oai](https://github.com/brooks-oai)
  + [#29624](https://github.com/openai/codex/pull/29624) Preserve Windows sandbox identity during credential retry [@jif-oai](https://github.com/jif-oai)
  + [#27466](https://github.com/openai/codex/pull/27466) [codex] Trace exec-server JSON-RPC requests [@richardopenai](https://github.com/richardopenai)
  + [#29844](https://github.com/openai/codex/pull/29844) Follow directory symlinks in filesystem walks [@jif-oai](https://github.com/jif-oai)
  + [#29637](https://github.com/openai/codex/pull/29637) Skip credential refresh for WindowsApps launch failures [@jif-oai](https://github.com/jif-oai)
  + [#29591](https://github.com/openai/codex/pull/29591) feat(app-server): list descendant threads by ancestor [@btraut-openai](https://github.com/btraut-openai)
  + [#28034](https://github.com/openai/codex/pull/28034) feat(network-proxy): experimental local credential broker [@winston-openai](https://github.com/winston-openai)
  + [#29736](https://github.com/openai/codex/pull/29736) [codex] Inject agent graph store into ThreadManager [@wiltzius-openai](https://github.com/wiltzius-openai)
  + [#29889](https://github.com/openai/codex/pull/29889) [apps] Thread structured icon assets through app list [@drewschuster-openai](https://github.com/drewschuster-openai)
  + [#29724](https://github.com/openai/codex/pull/29724) mcp: keep elicitation requests below app wire types [@anp-oai](https://github.com/anp-oai)
  + [#29684](https://github.com/openai/codex/pull/29684) [plugins] Track plugin install requests by ID [@adaley-openai](https://github.com/adaley-openai)
  + [#29870](https://github.com/openai/codex/pull/29870) Pipeline bounded AGENTS.md and Git root probes [@jif-oai](https://github.com/jif-oai)
  + [#29893](https://github.com/openai/codex/pull/29893) [codex] dedupe remote control account header [@shuo-openai](https://github.com/shuo-openai)
  + [#29851](https://github.com/openai/codex/pull/29851) Add a connector declaration snapshot [@jif-oai](https://github.com/jif-oai)
  + [#29903](https://github.com/openai/codex/pull/29903) path-uri: normalize parent segments in absolute joins [@anp-oai](https://github.com/anp-oai)
  + [#29852](https://github.com/openai/codex/pull/29852) Read connector declarations from executor plugins [@jif-oai](https://github.com/jif-oai)
  + [#29785](https://github.com/openai/codex/pull/29785) Isolate curated plugin sync Git environment [@etraut-openai](https://github.com/etraut-openai)
  + [#29907](https://github.com/openai/codex/pull/29907) [codex] namespace sleep under clock [@rka-oai](https://github.com/rka-oai)
  + [#29910](https://github.com/openai/codex/pull/29910) [codex] nest sleep config under current time reminder [@rka-oai](https://github.com/rka-oai)
  + [#29913](https://github.com/openai/codex/pull/29913) feat(remote-control): add daemon pairing command [@apanasenko-oai](https://github.com/apanasenko-oai)
  + [#29936](https://github.com/openai/codex/pull/29936) core: add configurable <context\_window\_guidance> message [@bolinfest](https://github.com/bolinfest)
  + [#26705](https://github.com/openai/codex/pull/26705) TUI Plugin Sharing 5 - polish remote plugin catalog rows [@canvrno-oai](https://github.com/canvrno-oai)
  + [#29733](https://github.com/openai/codex/pull/29733) Allow ChatGPT-hosted MCP servers to use session auth [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#29833](https://github.com/openai/codex/pull/29833) [1/3] core: make world state snapshots serializable [@sayan-oai](https://github.com/sayan-oai)
  + [#29919](https://github.com/openai/codex/pull/29919) TUI support for buffer experience [@etraut-openai](https://github.com/etraut-openai)
  + [#29924](https://github.com/openai/codex/pull/29924) Represent MCP authentication with an enum [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#29804](https://github.com/openai/codex/pull/29804) code-mode: define process host wire protocol [@cconger](https://github.com/cconger)
  + [#29956](https://github.com/openai/codex/pull/29956) [codex] Populate remote plugin local versions [@abhinav-oai](https://github.com/abhinav-oai)
  + [#29835](https://github.com/openai/codex/pull/29835) [2/3] core: persist world state in rollouts [@sayan-oai](https://github.com/sayan-oai)
  + [#29899](https://github.com/openai/codex/pull/29899) [codex] Update reasoning effort [@shijie-oai](https://github.com/shijie-oai)
  + [#29837](https://github.com/openai/codex/pull/29837) [3/3] core: replay persisted world state [@sayan-oai](https://github.com/sayan-oai)
  + [#29969](https://github.com/openai/codex/pull/29969) Report MCP error codes with server attribution [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#29970](https://github.com/openai/codex/pull/29970) core: raise token budget message limits [@bolinfest](https://github.com/bolinfest)
  + [#29973](https://github.com/openai/codex/pull/29973) [codex] route sleep through time providers [@rka-oai](https://github.com/rka-oai)
  + [#19051](https://github.com/openai/codex/pull/19051) feat: use run agent task auth for inference [@adrian-openai](https://github.com/adrian-openai)
  + [#29810](https://github.com/openai/codex/pull/29810) core: make AGENTS.md react to environment changes [@sayan-oai](https://github.com/sayan-oai)
  + [#29997](https://github.com/openai/codex/pull/29997) core: reconcile legacy WorldState sections [@sayan-oai](https://github.com/sayan-oai)
  + [#29990](https://github.com/openai/codex/pull/29990) Parallelize environment skill loading [@anp-oai](https://github.com/anp-oai)
  + [#28522](https://github.com/openai/codex/pull/28522) Support HTTP MCP servers from selected executor plugins [@jif-oai](https://github.com/jif-oai)
  + [#28529](https://github.com/openai/codex/pull/28529) Support OAuth for HTTP MCP servers from selected executor plugins [@jif-oai](https://github.com/jif-oai)
  + [#29656](https://github.com/openai/codex/pull/29656) Test executor-routed MCP OAuth token exchange [@jif-oai](https://github.com/jif-oai)
  + [#29928](https://github.com/openai/codex/pull/29928) chore(app-server): mark thread/rollback as deprecated [@owenlin0](https://github.com/owenlin0)
  + [#29856](https://github.com/openai/codex/pull/29856) Persist selected capability roots and resolve availability per model step [@jif-oai](https://github.com/jif-oai)
  + [#27467](https://github.com/openai/codex/pull/27467) [codex] Record exec-server lifecycle metrics [@richardopenai](https://github.com/richardopenai)
  + [#29942](https://github.com/openai/codex/pull/29942) feat: add provider-aware model fallback to thread start [@celia-oai](https://github.com/celia-oai)
  + [#30095](https://github.com/openai/codex/pull/30095) cli: rename sandbox permission profile flag [@bolinfest](https://github.com/bolinfest)
  + [#30029](https://github.com/openai/codex/pull/30029) [codex] current time reminder interval to be set to 0 [@rka-oai](https://github.com/rka-oai)
  + [#29941](https://github.com/openai/codex/pull/29941) core: expose permission profile to shell tools [@bolinfest](https://github.com/bolinfest)
  + [#30031](https://github.com/openai/codex/pull/30031) [codex] add current time reminder delivery mode config [@rka-oai](https://github.com/rka-oai)
  + [#30098](https://github.com/openai/codex/pull/30098) [codex] Retry temporarily offline exec-server recovery [@richardopenai](https://github.com/richardopenai)
  + [#30033](https://github.com/openai/codex/pull/30033) [codex] impl delivery\_mode: current time reminders on response boundaries [@rka-oai](https://github.com/rka-oai)
  + [#30108](https://github.com/openai/codex/pull/30108) [codex] extend code-mode host IPC transport [@cconger](https://github.com/cconger)
  + [#27470](https://github.com/openai/codex/pull/27470) [codex] Observe remote exec-server lifecycle [@richardopenai](https://github.com/richardopenai)
  + [#30113](https://github.com/openai/codex/pull/30113) [codex] poll external clock during sleep [@rka-oai](https://github.com/rka-oai)
  + [#29003](https://github.com/openai/codex/pull/29003) feat(core, mcp): cache codex\_apps tools in memory [@owenlin0](https://github.com/owenlin0)
  + [#30114](https://github.com/openai/codex/pull/30114) release: publish standalone zsh artifacts [@bolinfest](https://github.com/bolinfest)
  + [#30116](https://github.com/openai/codex/pull/30116) release: consume standalone zsh artifacts [@bolinfest](https://github.com/bolinfest)
  + [#29648](https://github.com/openai/codex/pull/29648) [codex] Add managed MCP server matchers [@felixxia-oai](https://github.com/felixxia-oai)
  + [#30100](https://github.com/openai/codex/pull/30100) Let extensions contribute World State sections [@jif-oai](https://github.com/jif-oai)
  + [#30124](https://github.com/openai/codex/pull/30124) fix(app-server): suppress TUI rollback warning [@fcoury-oai](https://github.com/fcoury-oai)
  + [#29877](https://github.com/openai/codex/pull/29877) [codex] Surface MCP reauthentication-required startup failures [@felixxia-oai](https://github.com/felixxia-oai)
  + [#29988](https://github.com/openai/codex/pull/29988) Recognize Work web and mobile thread originators [@chiam-oai](https://github.com/chiam-oai)
  + [#30110](https://github.com/openai/codex/pull/30110) [codex] add code-mode host failure supervision hooks [@cconger](https://github.com/cconger)
  + [#30088](https://github.com/openai/codex/pull/30088) Project executor skills through World State [@jif-oai](https://github.com/jif-oai)
  + [#30117](https://github.com/openai/codex/pull/30117) [codex] Propagate traces through exec-server HTTP [@wiltzius-openai](https://github.com/wiltzius-openai)
  + [#30101](https://github.com/openai/codex/pull/30101) Pin MCP runtimes to model steps [@jif-oai](https://github.com/jif-oai)
  + [#30134](https://github.com/openai/codex/pull/30134) ci: narrow Windows test skips [@anp-oai](https://github.com/anp-oai)
  + [#30093](https://github.com/openai/codex/pull/30093) Project selected plugin runtime by environment availability [@jif-oai](https://github.com/jif-oai)
  + [#30145](https://github.com/openai/codex/pull/30145) Reuse walk inventory for environment skill metadata [@jif-oai](https://github.com/jif-oai)
  + [#30111](https://github.com/openai/codex/pull/30111) [codex] implement standalone code-mode process host [@cconger](https://github.com/cconger)
  + [#29935](https://github.com/openai/codex/pull/29935) [codex] Attribute app-server analytics by thread originator [@alexsong-oai](https://github.com/alexsong-oai)
  + [#30152](https://github.com/openai/codex/pull/30152) Reinject missing World State fragments on resume [@jif-oai](https://github.com/jif-oai)
  + [#30127](https://github.com/openai/codex/pull/30127) Keep MCP elicitation routable across runtime refreshes [@jif-oai](https://github.com/jif-oai)
  + [#29934](https://github.com/openai/codex/pull/29934) Expose MCP app identity in app context [@martinauyeung-oai](https://github.com/martinauyeung-oai)
  + [#29909](https://github.com/openai/codex/pull/29909) [codex] allow CCA image generation and web search extensions [@won-openai](https://github.com/won-openai)
  + [#30157](https://github.com/openai/codex/pull/30157) Test selected capabilities across availability and resume [@jif-oai](https://github.com/jif-oai)
  + [#30144](https://github.com/openai/codex/pull/30144) [codex] fix terminal rollout event durability [@wiltzius-openai](https://github.com/wiltzius-openai)
  + [#29920](https://github.com/openai/codex/pull/29920) Retry failed Codex Apps MCP startup [@kbazzi](https://github.com/kbazzi)
  + [#29516](https://github.com/openai/codex/pull/29516) Persist Cloudflare affinity cookies for MCP HTTP [@stevenlee-oai](https://github.com/stevenlee-oai)
  + [#30112](https://github.com/openai/codex/pull/30112) [codex] add process-owned code-mode session client [@cconger](https://github.com/cconger)
  + [#30142](https://github.com/openai/codex/pull/30142) [codex] wire process-owned code mode host into core [@cconger](https://github.com/cconger)
  + [#30198](https://github.com/openai/codex/pull/30198) [codex] fix CreateThreadParams test initializer [@anp-oai](https://github.com/anp-oai)
  + [#30148](https://github.com/openai/codex/pull/30148) Reuse MCP runtimes when selected availability changes nothing [@jif-oai](https://github.com/jif-oai)
  + [#30215](https://github.com/openai/codex/pull/30215) Test selected capabilities across unavailable resume [@jif-oai](https://github.com/jif-oai)
  + [#29991](https://github.com/openai/codex/pull/29991) [codex] narrow unused skills intro export [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#30229](https://github.com/openai/codex/pull/30229) Relax hooks.json top-level metadata validation [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#29927](https://github.com/openai/codex/pull/29927) feat(app-server): add history\_mode to thread [@owenlin0](https://github.com/owenlin0)
  + [#30276](https://github.com/openai/codex/pull/30276) fix main [@owenlin0](https://github.com/owenlin0)
  + [#29683](https://github.com/openai/codex/pull/29683) [codex] Add managed new-thread model settings [@hefuc-oai](https://github.com/hefuc-oai)
  + [#30225](https://github.com/openai/codex/pull/30225) Overlap executor skill reads with namespace discovery [@jif-oai](https://github.com/jif-oai)
  + [#30274](https://github.com/openai/codex/pull/30274) [codex] allow AGENTS.md and skills to authorize delegation [@charlesdu-openai](https://github.com/charlesdu-openai)
  + [#30147](https://github.com/openai/codex/pull/30147) [codex] Use managed defaults for TUI threads [@hefuc-oai](https://github.com/hefuc-oai)
  + [#30261](https://github.com/openai/codex/pull/30261) ensure thread.history\_mode is immutable [@owenlin0](https://github.com/owenlin0)
  + [#30277](https://github.com/openai/codex/pull/30277) feat(app-server): add optional turn\_id to thread/fork [@owenlin0](https://github.com/owenlin0)
  + [#30143](https://github.com/openai/codex/pull/30143) Let Codex consult user-level code-review-\* skills. [@anp-oai](https://github.com/anp-oai)
  + [#30285](https://github.com/openai/codex/pull/30285) feat: add GPT-5.6 variants to Bedrock catalog [@celia-oai](https://github.com/celia-oai)
  + [#30173](https://github.com/openai/codex/pull/30173) Close thread persistence when submission channel closes [@alfozan](https://github.com/alfozan)
  + [#30257](https://github.com/openai/codex/pull/30257) [codex] Classify nested MCP authentication startup errors [@felixxia-oai](https://github.com/felixxia-oai)
  + [#29375](https://github.com/openai/codex/pull/29375) [codex] Support npm marketplace plugin sources [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#30146](https://github.com/openai/codex/pull/30146) [codex] group blocking and postmerge CI workflows [@anp-oai](https://github.com/anp-oai)
  + [#30282](https://github.com/openai/codex/pull/30282) feat(protocol): define missing rollout turn items [@owenlin0](https://github.com/owenlin0)
  + [#30201](https://github.com/openai/codex/pull/30201) fix(remote-control): avoid server token refresh retry storms [@apanasenko-oai](https://github.com/apanasenko-oai)
  + [#30273](https://github.com/openai/codex/pull/30273) [codex] consume pushed exec-server process events [@richardopenai](https://github.com/richardopenai)
  + [#30286](https://github.com/openai/codex/pull/30286) core: overlap diff root discovery with world state [@anp-oai](https://github.com/anp-oai)
  + [#30314](https://github.com/openai/codex/pull/30314) app-server: structure and test JSON shutdown logs [@bolinfest](https://github.com/bolinfest)
  + [#30317](https://github.com/openai/codex/pull/30317) Update security check wording [@etraut-openai](https://github.com/etraut-openai)
  + [#30302](https://github.com/openai/codex/pull/30302) Preserve namespaces on custom tool calls [@nhamidi-oai](https://github.com/nhamidi-oai)
  + [#30327](https://github.com/openai/codex/pull/30327) core: stabilize synthesized call output IDs [@bolinfest](https://github.com/bolinfest)
  + [#30291](https://github.com/openai/codex/pull/30291) [app-server] expose environment info RPC [@maxj-oai](https://github.com/maxj-oai)
  + [#29691](https://github.com/openai/codex/pull/29691) [plugins] Enforce marketplace source policy at runtime [@xl-openai](https://github.com/xl-openai)
  + [#30384](https://github.com/openai/codex/pull/30384) [app-server] increase currentTime/read timeout [@rka-oai](https://github.com/rka-oai)
  + [#30297](https://github.com/openai/codex/pull/30297) [codex] Enable remote plugins by default [@xl-openai](https://github.com/xl-openai)
  + [#30490](https://github.com/openai/codex/pull/30490) fix(tui): clear completed safety buffering prompt [@fcoury-oai](https://github.com/fcoury-oai)
  + [#29740](https://github.com/openai/codex/pull/29740) [codex] Use model metadata for skills usage instructions [@ani-oai](https://github.com/ani-oai)
  + [#30511](https://github.com/openai/codex/pull/30511) [codex] Restore v1 delegation guidance [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#30508](https://github.com/openai/codex/pull/30508) Revert "Make auto-review on-request prompt more proactive" [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)
  + [#30467](https://github.com/openai/codex/pull/30467) [codex] Treat max as a first-class reasoning effort [@shijie-oai](https://github.com/shijie-oai)
  + [#30491](https://github.com/openai/codex/pull/30491) Update safety check links [@etraut-openai](https://github.com/etraut-openai)
  + [#30607](https://github.com/openai/codex/pull/30607) [codex] auto-label AWS Bedrock issues [@etraut-openai](https://github.com/etraut-openai)
  + [#30269](https://github.com/openai/codex/pull/30269) [codex] disable Nagle on Rendezvous WebSockets [@richardopenai](https://github.com/richardopenai)
  + [#30645](https://github.com/openai/codex/pull/30645) [codex] Update safety notice wording [@etraut-openai](https://github.com/etraut-openai)
  + [#30757](https://github.com/openai/codex/pull/30757) fix(core) Remove full text websocket trace [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)
  + [#30851](https://github.com/openai/codex/pull/30851) docs: add tag to fenced code block [@bolinfest](https://github.com/bolinfest)
  + [#30643](https://github.com/openai/codex/pull/30643) [codex] bound Rendezvous WebSocket liveness [@richardopenai](https://github.com/richardopenai)
  + [#30867](https://github.com/openai/codex/pull/30867) Consolidate multi-agent v2 communication sends [@bolinfest](https://github.com/bolinfest)
  + [#30872](https://github.com/openai/codex/pull/30872) Log multi-agent communication lifecycle [@bolinfest](https://github.com/bolinfest)
  + [#30883](https://github.com/openai/codex/pull/30883) [codex] emit per-request TTFT completion telemetry [@xli-oai](https://github.com/xli-oai)
  + [#30897](https://github.com/openai/codex/pull/30897) Fix inherited availability metadata for Bedrock models [@shijie-oai](https://github.com/shijie-oai)
  + [#30941](https://github.com/openai/codex/pull/30941) fix: address quick-xml security advisories [@bolinfest](https://github.com/bolinfest)
  + [#30770](https://github.com/openai/codex/pull/30770) fix(websockets) ignore metadata for incremental requests [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)
  + [#30334](https://github.com/openai/codex/pull/30334) telemetry: log structured direct tool-call timing [@bolinfest](https://github.com/bolinfest)
  + [#30493](https://github.com/openai/codex/pull/30493) [codex] Add configurable multi-agent mode hint text [@shijie-oai](https://github.com/shijie-oai)
  + [#30796](https://github.com/openai/codex/pull/30796) Fix MIME types for path-backed feedback attachments [@btraut-openai](https://github.com/btraut-openai)
  + [#31056](https://github.com/openai/codex/pull/31056) fix(install): reuse GitHub release metadata [@bolinfest](https://github.com/bolinfest)
  + [#30981](https://github.com/openai/codex/pull/30981) [codex] expose remote plugin versions [@ericning-o](https://github.com/ericning-o)
  + [#31066](https://github.com/openai/codex/pull/31066) chore: remove unused git-cliff configuration [@bolinfest](https://github.com/bolinfest)
  + [#31064](https://github.com/openai/codex/pull/31064) [codex] Read buffering metadata from response events [@fc-oai](https://github.com/fc-oai)
  + [#30223](https://github.com/openai/codex/pull/30223) Make plugin guidance react to environment readiness [@sayan-oai](https://github.com/sayan-oai)
  + [#31189](https://github.com/openai/codex/pull/31189) Fix cancelled review leaving MCP startup busy [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#30876](https://github.com/openai/codex/pull/30876) [core] Support interleaved response items [@alexi-openai](https://github.com/alexi-openai)
  + [#31262](https://github.com/openai/codex/pull/31262) [codex] Read retry model from buffering events [@fc-oai](https://github.com/fc-oai)
  + [#31261](https://github.com/openai/codex/pull/31261) Revert "[core] Support interleaved response items" [@alexi-openai](https://github.com/alexi-openai)
  + [#31253](https://github.com/openai/codex/pull/31253) Emit exec-policy warnings for freshly loaded thread config [@etraut-openai](https://github.com/etraut-openai)
  + [#31179](https://github.com/openai/codex/pull/31179) Remove TUI exec-policy core exports [@etraut-openai](https://github.com/etraut-openai)
  + [#29959](https://github.com/openai/codex/pull/29959) Conditional codex\_home dotenv [@canvrno-oai](https://github.com/canvrno-oai)
  + [#30627](https://github.com/openai/codex/pull/30627) elicitations: Move to shared ElicitationService [@cconger](https://github.com/cconger)
  + [#30318](https://github.com/openai/codex/pull/30318) core: trace executor skill discovery [@anp-oai](https://github.com/anp-oai)
  + [#31276](https://github.com/openai/codex/pull/31276) Revert "Conditional codex\_home dotenv" [@canvrno-oai](https://github.com/canvrno-oai)
  + [#30956](https://github.com/openai/codex/pull/30956) refactor(protocol): isolate legacy item fanout [@owenlin0](https://github.com/owenlin0)
  + [#30395](https://github.com/openai/codex/pull/30395) [app-server] Include reset-credit details in rate limits [@jayp-oai](https://github.com/jayp-oai)
  + [#31267](https://github.com/openai/codex/pull/31267) chore(approvals) consolidate guardian calls for shell tools [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)
  + [#31252](https://github.com/openai/codex/pull/31252) [tui] Truncate hook context in conversation history [@abhinav-oai](https://github.com/abhinav-oai)
  + [#29918](https://github.com/openai/codex/pull/29918) [codex] Flush trailing realtime transcript tail [@guinness-oai](https://github.com/guinness-oai)
  + [#30226](https://github.com/openai/codex/pull/30226) Make Apps guidance react to MCP availability [@sayan-oai](https://github.com/sayan-oai)
  + [#31190](https://github.com/openai/codex/pull/31190) Use popup token ranges for autocomplete insertion [@charliemarsh-oai](https://github.com/charliemarsh-oai)
  + [#29697](https://github.com/openai/codex/pull/29697) fix: attribut network requests to the exact exec on linux [@jif-oai](https://github.com/jif-oai)
  + [#31303](https://github.com/openai/codex/pull/31303) feat(code-mode): allow disabling V8 JIT [@cconger](https://github.com/cconger)
  + [#31271](https://github.com/openai/codex/pull/31271) chore: use .worktreeinclude for user Bazel config [@anp-oai](https://github.com/anp-oai)
  + [#31308](https://github.com/openai/codex/pull/31308) fix: update crossbeam-epoch for RUSTSEC-2026-0204 [@cconger](https://github.com/cconger)
  + [#30202](https://github.com/openai/codex/pull/30202) [codex] bundle code mode host in release packages [@cconger](https://github.com/cconger)
  + [#31293](https://github.com/openai/codex/pull/31293) [codex] app-server: expose plugin install policy source [@ericning-o](https://github.com/ericning-o)
  + [#31318](https://github.com/openai/codex/pull/31318) ci: share common workflow setup [@anp-oai](https://github.com/anp-oai)
  + [#29992](https://github.com/openai/codex/pull/29992) app-server: cover selected environments in integration tests [@anp-oai](https://github.com/anp-oai)
  + [#31284](https://github.com/openai/codex/pull/31284) Warn when configured service tiers are unsupported [@etraut-openai](https://github.com/etraut-openai)
  + [#31323](https://github.com/openai/codex/pull/31323) Extract shared HTTP transport into codex-http-client [@bolinfest](https://github.com/bolinfest)
  + [#31331](https://github.com/openai/codex/pull/31331) Migrate direct HTTP consumers to codex-http-client [@bolinfest](https://github.com/bolinfest)
  + [#31337](https://github.com/openai/codex/pull/31337) fix: restore Codex environment setup table [@anp-oai](https://github.com/anp-oai)
  + [#31188](https://github.com/openai/codex/pull/31188) Preserve managed exec policy after rules parse errors [@etraut-openai](https://github.com/etraut-openai)
  + [#31306](https://github.com/openai/codex/pull/31306) [codex] Support sequential cutoff reasoning summaries [@ashwinnathan-openai](https://github.com/ashwinnathan-openai)
  + [#31344](https://github.com/openai/codex/pull/31344) exec-server: use virtual time in Noise relay test [@bolinfest](https://github.com/bolinfest)
  + [#31296](https://github.com/openai/codex/pull/31296) refactor(protocol): map canonical tool items to legacy events [@owenlin0](https://github.com/owenlin0)
  + [#31335](https://github.com/openai/codex/pull/31335) core: route Responses API through system proxy [@bolinfest](https://github.com/bolinfest)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.143.0)
* 2026-07-06

  ### ChatGPT for iOS 1.2026.181

  ### New features

  + Added support for creating, searching, opening, forking, and managing Codex
    tasks directly from a conversation.
  + Added filters for staged, unstaged, branch, and last-turn changes, with controls
    for comparing branches.
  + Added support for adding selected transcript text directly to the composer.
  + Added previews for image and file attachments before sending.
  + Added inline Photos and Camera pickers to the attachment menu.
  + Added a connection shortcut and support for SSH hosts using private keys or no
    credentials.
  + Added usage limits and credit details to the task menu.

  ### Improvements and bug fixes

  + Improved the task list with consistent task terminology, clearer delegated
    task titles, and a Needs input status.
  + Improved initial task loading and foreground recovery.
  + Improved autocomplete by selecting the first result automatically and
    accepting it with Return.
  + Improved model, reasoning, and Fast settings so changes remain scoped to the
    current task.
  + Improved task-management and dynamic tool activity presentation.
  + Improved side chats to open directly when only one conversation is available.
  + Improved plugin autocomplete with installed plugins and their icons.
  + Improved workspace diff accuracy and expand-and-collapse navigation.
  + Improved recovery by preserving thread state across reconnects and host
    pairings across sign-out.
  + Fixed stuck thread-list loading, prompt mode deadlocks, stale images, and
    microphone permission alerts.
  + Fixed shake to undo and keyboard refocusing after sending a prompt.
* 2026-07-01

  ### Codex CLI 0.142.5

  ```
  $ npm install -g @openai/codex@0.142.5
  ```

    View details 

  ## Bug Fixes

  + Prevented full Responses WebSocket request payloads from being written to trace logs. ([#30771](https://github.com/openai/codex/pull/30771))

  ## Changelog

  Full Changelog: [rust-v0.142.4...rust-v0.142.5](https://github.com/openai/codex/compare/rust-v0.142.4...rust-v0.142.5)

  + [#30771](https://github.com/openai/codex/pull/30771) [codex] Backport websocket trace fix to release/0.142 [@dylan-hurd-oai](https://github.com/dylan-hurd-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.142.5)

## June 2026

* 2026-06-29

  ### Codex CLI 0.142.4

  ```
  $ npm install -g @openai/codex@0.142.4
  ```

    View details 

  ## Chores

  + No user-facing changes were identified for this release.

  ## Changelog

  Full Changelog: [rust-v0.142.3...rust-v0.142.4](https://github.com/openai/codex/compare/rust-v0.142.3...rust-v0.142.4)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.142.4)
* 2026-06-26

  ### Codex CLI 0.142.3

  ```
  $ npm install -g @openai/codex@0.142.3
  ```

    View details 

  ## Chores

  + Maintenance-only patch release with no user-facing changes since 0.142.2.

  ## Changelog

  Full Changelog: [rust-v0.142.2...rust-v0.142.3](https://github.com/openai/codex/compare/rust-v0.142.2...rust-v0.142.3)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.142.3)
* 2026-06-25

  ### Codex Remote reaches general availability

  Codex Remote has reached general availability. Use Codex from the ChatGPT mobile
  app to start or continue work on a connected Mac or Windows host, review
  progress, and approve actions from your phone.

  Remote Control now uses authenticated one-to-one QR pairing between each iOS or
  Android device and each host. Update the ChatGPT mobile app and Codex App to the
  latest versions before connecting. Connections used since June 8, 2026, remain
  paired; older inactive connections need to pair again.

  The new [DigitalOcean plugin](https://chatgpt.com/plugins/share/5dc672c7116c44ff92595d48e72df522)
  lets Codex provision a DigitalOcean Droplet, configure SSH access, and connect
  it to the Codex App as a remote workspace.

  See [Remote connections](/codex/remote-connections) for setup and
  troubleshooting.
* 2026-06-25

  ### Codex CLI 0.142.2

  ```
  $ npm install -g @openai/codex@0.142.2
  ```

    View details 

  ## New Features

  + MCP tools now use tool search by default when supported, improving tool discovery while preserving compatibility with older models and providers. ([#29486](https://github.com/openai/codex/pull/29486))
  + macOS authentication clients can honor system proxy, PAC, and WPAD settings when `respect_system_proxy` is enabled. ([#26709](https://github.com/openai/codex/pull/26709))
  + Plugins can provide dedicated dark-mode logos through local manifests and remote catalogs. ([#29488](https://github.com/openai/codex/pull/29488))
  + Apps can display richer safety-buffering UI using server-provided visibility and faster-model metadata. ([#29473](https://github.com/openai/codex/pull/29473))

  ## Bug Fixes

  + Remote plugin catalogs now return curated featured-plugin rankings. ([#29485](https://github.com/openai/codex/pull/29485))
  + Expired Amazon Bedrock credentials now produce actionable recovery guidance instead of a generic authorization error. ([#28992](https://github.com/openai/codex/pull/28992))
  + Remote stdio MCP servers now accept absolute working directories written in the remote platform’s path format. ([#29493](https://github.com/openai/codex/pull/29493))
  + Remote HTTP(S) image inputs now return clear model-visible validation errors; inline data URLs and local images remain supported. ([#29417](https://github.com/openai/codex/pull/29417), [#29419](https://github.com/openai/codex/pull/29419))
  + PowerShell commands containing executable AST regions the safety classifier cannot inspect now require approval. ([#24092](https://github.com/openai/codex/pull/24092))
  + Code Mode now warns when the selected model lacks the required metadata. ([#29490](https://github.com/openai/codex/pull/29490))

  ## Chores

  + Updated bundled OpenSSL and esbuild dependencies to patched releases. ([#29487](https://github.com/openai/codex/pull/29487), [#29489](https://github.com/openai/codex/pull/29489))
  + Successful formatter runs are now quiet while failures still show diagnostics. ([#29467](https://github.com/openai/codex/pull/29467))

  ## Changelog

  Full Changelog: [rust-v0.142.1...rust-v0.142.2](https://github.com/openai/codex/compare/rust-v0.142.1...rust-v0.142.2)

  + [#28769](https://github.com/openai/codex/pull/28769) Register full CDP requirements feature [@syuan-oai](https://github.com/syuan-oai)
  + [#29485](https://github.com/openai/codex/pull/29485) [codex] fetch featured IDs for remote plugins [@ericning-o](https://github.com/ericning-o)
  + [#29487](https://github.com/openai/codex/pull/29487) Upgrade bundled OpenSSL to 3.6.3 [@jif-oai](https://github.com/jif-oai)
  + [#29489](https://github.com/openai/codex/pull/29489) [codex] Update esbuild to 0.28.1 [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29488](https://github.com/openai/codex/pull/29488) [plugins] Add dark-mode logo metadata [@drewschuster-openai](https://github.com/drewschuster-openai)
  + [#29249](https://github.com/openai/codex/pull/29249) [codex] migrate environment context to model world state [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29494](https://github.com/openai/codex/pull/29494) core: wrap token budget window context [@bolinfest](https://github.com/bolinfest)
  + [#29417](https://github.com/openai/codex/pull/29417) [codex] replace remote images with model-visible error text [@rka-oai](https://github.com/rka-oai)
  + [#28360](https://github.com/openai/codex/pull/28360) feat(core): store turn\_id on ResponseItem metadata [@owenlin0](https://github.com/owenlin0)
  + [#29486](https://github.com/openai/codex/pull/29486) [codex] Use tool search for MCP tools by default [@sayan-oai](https://github.com/sayan-oai)
  + [#29501](https://github.com/openai/codex/pull/29501) path-uri: clarify host-native path conversion [@anp-oai](https://github.com/anp-oai)
  + [#29504](https://github.com/openai/codex/pull/29504) fix: world state response item test [@celia-oai](https://github.com/celia-oai)
  + [#26704](https://github.com/openai/codex/pull/26704) TUI Plugin Sharing 4 - cover remote plugin catalog flows [@canvrno-oai](https://github.com/canvrno-oai)
  + [#29419](https://github.com/openai/codex/pull/29419) [codex] reject remote images at app-server ingress [@rka-oai](https://github.com/rka-oai)
  + [#28992](https://github.com/openai/codex/pull/28992) chore: improve expired Bedrock credential errors [@celia-oai](https://github.com/celia-oai)
  + [#29467](https://github.com/openai/codex/pull/29467) Make formatter output quiet on success [@anp-oai](https://github.com/anp-oai)
  + [#26709](https://github.com/openai/codex/pull/26709) PAC 4 - Add macOS system proxy resolver [@canvrno-oai](https://github.com/canvrno-oai)
  + [#29490](https://github.com/openai/codex/pull/29490) chore: warn when Code Mode lacks model metadata [@celia-oai](https://github.com/celia-oai)
  + [#29493](https://github.com/openai/codex/pull/29493) mcp: accept foreign absolute cwd for remote stdio [@anp-oai](https://github.com/anp-oai)
  + [#29473](https://github.com/openai/codex/pull/29473) Propagate safety buffering treatment metadata [@fc-oai](https://github.com/fc-oai)
  + [#24092](https://github.com/openai/codex/pull/24092) [codex] Reject unlowered PowerShell AST regions [@bookholt-oai](https://github.com/bookholt-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.142.2)
* 2026-06-25

  ### Codex CLI 0.142.1

  ```
  $ npm install -g @openai/codex@0.142.1
  ```

    View details 

  ## New Features

  + Added opt-in Windows system proxy support for authentication, including PAC, WPAD, static proxies, and bypass rules. ([#26708](https://github.com/openai/codex/pull/26708))

  ## Changelog

  Full Changelog: [rust-v0.142.0...rust-v0.142.1](https://github.com/openai/codex/compare/rust-v0.142.0...rust-v0.142.1)

  + [#26708](https://github.com/openai/codex/pull/26708) PAC 3 - Add Windows system proxy resolver [@canvrno-oai](https://github.com/canvrno-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.142.1)
* 2026-06-22

  ### ChatGPT for iOS 1.2026.167

  ### New features

  + Added per-host personality settings with Friendly and Pragmatic options.
  + Added support for editing goals directly in the composer.
  + Added a link from forked conversations back to the original thread.

  ### Improvements and bug fixes

  + Improved side chat visibility with separate conversations above the composer.
  + Improved composer autocomplete for commands, skills, and plugins from any
    prefix.
  + Improved progress visibility for subagents, tasks, and worktree creation.
  + Fixed long threads loading.
  + Improved workspace file search, code review drafts, steering, and host setup
    and recovery.
  + Fixed Face ID unlocking, stopping responses, collapsed sections, and dark-mode
    host indicators.
* 2026-06-22

  ### Codex CLI 0.142.0

  ```
  $ npm install -g @openai/codex@0.142.0
  ```

    View details 

  ## New Features

  + `/usage` can now show and redeem earned usage-limit reset credits, with confirmation, retry, and refreshed availability states. ([#28154](https://github.com/openai/codex/pull/28154), [#28793](https://github.com/openai/codex/pull/28793))
  + `/plugins` now organizes remote plugins into OpenAI Curated, Workspace, and Shared with me sections, while eligible turns can recommend and install relevant plugins. ([#26703](https://github.com/openai/codex/pull/26703), [#28399](https://github.com/openai/codex/pull/28399), [#28400](https://github.com/openai/codex/pull/28400), [#27704](https://github.com/openai/codex/pull/27704), [#28403](https://github.com/openai/codex/pull/28403))
  + Configurable rollout token budgets track usage across agent threads, provide remaining-budget reminders, and abort turns when exhausted. ([#28746](https://github.com/openai/codex/pull/28746), [#28494](https://github.com/openai/codex/pull/28494), [#28707](https://github.com/openai/codex/pull/28707), [#29423](https://github.com/openai/codex/pull/29423))
  + App-server clients can configure multi-agent delegation as disabled, explicit-request-only, or proactive at the thread and turn level. ([#28685](https://github.com/openai/codex/pull/28685), [#28792](https://github.com/openai/codex/pull/28792), [#29324](https://github.com/openai/codex/pull/29324))
  + Added an indexed web-search mode that permits live searches while restricting direct page access to server-approved URLs. ([#28489](https://github.com/openai/codex/pull/28489))
  + Codex can now receive scheduled UTC time reminders and query the current time directly, including through client-provided app-server clocks. ([#28822](https://github.com/openai/codex/pull/28822), [#28824](https://github.com/openai/codex/pull/28824), [#28835](https://github.com/openai/codex/pull/28835), [#29011](https://github.com/openai/codex/pull/29011))

  ## Bug Fixes

  + Restored reliable Linux TUI rendering after suspending with `Ctrl+Z` and resuming with `fg`. ([#28342](https://github.com/openai/codex/pull/28342))
  + Exec-server processes and stdio MCP sessions now survive transient disconnects, including signed-URL refresh and retry-safe stdin writes. ([#28512](https://github.com/openai/codex/pull/28512), [#28374](https://github.com/openai/codex/pull/28374), [#28546](https://github.com/openai/codex/pull/28546), [#28895](https://github.com/openai/codex/pull/28895))
  + Remote environments now preserve executor-native paths, shells, `AGENTS.md` discovery, and sandbox behavior across operating systems. ([#28146](https://github.com/openai/codex/pull/28146), [#28152](https://github.com/openai/codex/pull/28152), [#28958](https://github.com/openai/codex/pull/28958), [#28983](https://github.com/openai/codex/pull/28983), [#29099](https://github.com/openai/codex/pull/29099), [#29108](https://github.com/openai/codex/pull/29108), [#29113](https://github.com/openai/codex/pull/29113), [#29424](https://github.com/openai/codex/pull/29424))
  + Plugin loading and installation now handle root marketplace layouts, manifest fallbacks, multiple skill paths, actionable download errors, and immediate tool refreshes. ([#28771](https://github.com/openai/codex/pull/28771), [#28789](https://github.com/openai/codex/pull/28789), [#28790](https://github.com/openai/codex/pull/28790), [#28863](https://github.com/openai/codex/pull/28863), [#28951](https://github.com/openai/codex/pull/28951))
  + Parent agents now receive terminal subagent errors instead of seeing failed work as an empty successful completion. ([#28375](https://github.com/openai/codex/pull/28375))
  + Goal-first threads are once again persisted and returned by `thread/list` and `thread/search`. ([#28808](https://github.com/openai/codex/pull/28808))

  ## Chores

  + Reduced startup and session latency by deferring unnecessary DNS work, warming the model cache, reusing parsed plugin skills, parallelizing skill metadata reads, and skipping redundant catalog synchronization. ([#28542](https://github.com/openai/codex/pull/28542), [#28699](https://github.com/openai/codex/pull/28699), [#28844](https://github.com/openai/codex/pull/28844), [#29326](https://github.com/openai/codex/pull/29326), [#29005](https://github.com/openai/codex/pull/29005))
  + Reduced persistent-log churn by removing per-event WebSocket payload logging and filtering duplicated telemetry records. ([#29432](https://github.com/openai/codex/pull/29432), [#29457](https://github.com/openai/codex/pull/29457))

  ## Changelog

  Full Changelog: [rust-v0.141.0...rust-v0.142.0](https://github.com/openai/codex/compare/rust-v0.141.0...rust-v0.142.0)

  + [#28396](https://github.com/openai/codex/pull/28396) [codex] Record external agent import results [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#27751](https://github.com/openai/codex/pull/27751) [codex] expose Bedrock credential source in account/read [@celia-oai](https://github.com/celia-oai)
  + [#28338](https://github.com/openai/codex/pull/28338) [codex] Compress cold active rollouts [@jif-oai](https://github.com/jif-oai)
  + [#28368](https://github.com/openai/codex/pull/28368) feat: render typed envelopes for multi-agent v2 messages [@jif-oai](https://github.com/jif-oai)
  + [#28508](https://github.com/openai/codex/pull/28508) [tests] Keep Apps out of generic core test harness [@jif-oai](https://github.com/jif-oai)
  + [#28472](https://github.com/openai/codex/pull/28472) [codex] Clarify plugin load and runtime capability stages [@xl-openai](https://github.com/xl-openai)
  + [#28375](https://github.com/openai/codex/pull/28375) core: surface terminal subagent errors to parent agents [@jif-oai](https://github.com/jif-oai)
  + [#28542](https://github.com/openai/codex/pull/28542) perf(config): defer remote sandbox hostname lookup [@fcoury-oai](https://github.com/fcoury-oai)
  + [#28473](https://github.com/openai/codex/pull/28473) path-uri: clarify invalid host path errors [@anp-oai](https://github.com/anp-oai)
  + [#28342](https://github.com/openai/codex/pull/28342) fix(tui): restore TUI after suspend [@fcoury-oai](https://github.com/fcoury-oai)
  + [#28354](https://github.com/openai/codex/pull/28354) [codex] exec-server: stream files in chunks [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28553](https://github.com/openai/codex/pull/28553) chore: side prompt [@jif-oai](https://github.com/jif-oai)
  + [#27099](https://github.com/openai/codex/pull/27099) [codex-app-server-test-client & codex-app-server] Plugin Usage Analytics Smoke Test [@jameswt-oai](https://github.com/jameswt-oai)
  + [#28554](https://github.com/openai/codex/pull/28554) fix(tui): highlight C++ module files [@fcoury-oai](https://github.com/fcoury-oai)
  + [#28467](https://github.com/openai/codex/pull/28467) [codex] Warn clearly when code mode output is truncated [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#27750](https://github.com/openai/codex/pull/27750) [codex] Add incremental thread history changes [@wiltzius-openai](https://github.com/wiltzius-openai)
  + [#28154](https://github.com/openai/codex/pull/28154) feat(tui): add rate-limit reset redemption to /usage [@jayp-oai](https://github.com/jayp-oai)
  + [#28562](https://github.com/openai/codex/pull/28562) ci: run code-mode unit tests on all bazel targets [@cconger](https://github.com/cconger)
  + [#27923](https://github.com/openai/codex/pull/27923) [codex] Route MCP file uploads through environment filesystem [@pakrym-oai](https://github.com/pakrym-oai)
  + [#27100](https://github.com/openai/codex/pull/27100) [codex-app-server-test-client] Plugin Install/Uninstall Analytics Smoke Test [@jameswt-oai](https://github.com/jameswt-oai)
  + [#28581](https://github.com/openai/codex/pull/28581) [codex] re-enable absolute workdir integration test [@anp-oai](https://github.com/anp-oai)
  + [#28468](https://github.com/openai/codex/pull/28468) code-mode: extend test coverage to lock in cell lifecycle [@cconger](https://github.com/cconger)
  + [#28587](https://github.com/openai/codex/pull/28587) [codex] test exec relative additional permissions [@anp-oai](https://github.com/anp-oai)
  + [#28577](https://github.com/openai/codex/pull/28577) Clarify model-generated and legacy app path types [@anp-oai](https://github.com/anp-oai)
  + [#28589](https://github.com/openai/codex/pull/28589) Record invariants for path migration. [@anp-oai](https://github.com/anp-oai)
  + [#28146](https://github.com/openai/codex/pull/28146) app-server: preserve target-native environment cwd [@anp-oai](https://github.com/anp-oai)
  + [#28595](https://github.com/openai/codex/pull/28595) Tell codex about PathUri serde compat. [@anp-oai](https://github.com/anp-oai)
  + [#28399](https://github.com/openai/codex/pull/28399) [codex] [1/4] Add recommended plugin endpoint cache [@adaley-openai](https://github.com/adaley-openai)
  + [#28400](https://github.com/openai/codex/pull/28400) [codex] [2/4] Generalize plugin suggestion presentation [@adaley-openai](https://github.com/adaley-openai)
  + [#27704](https://github.com/openai/codex/pull/27704) [codex] [3/4] Activate endpoint plugin recommendations [@adaley-openai](https://github.com/adaley-openai)
  + [#28152](https://github.com/openai/codex/pull/28152) core: render remote environment cwd natively [@anp-oai](https://github.com/anp-oai)
  + [#28403](https://github.com/openai/codex/pull/28403) [codex] [4/4] Simplify recommended plugin install schema [@adaley-openai](https://github.com/adaley-openai)
  + [#26706](https://github.com/openai/codex/pull/26706) PAC 1 - Add system proxy feature config surface [@canvrno-oai](https://github.com/canvrno-oai)
  + [#27910](https://github.com/openai/codex/pull/27910) Add thread recencyAt for sidebar ordering [@nornagon-openai](https://github.com/nornagon-openai)
  + [#28627](https://github.com/openai/codex/pull/28627) Revert "Tell codex about PathUri serde compat. ([#28595](https://github.com/openai/codex/pull/28595))" [@anp-oai](https://github.com/anp-oai)
  + [#28625](https://github.com/openai/codex/pull/28625) [codex] Gate remote plugin catalog by auth [@xl-openai](https://github.com/xl-openai)
  + [#28629](https://github.com/openai/codex/pull/28629) [codex] core: restore absolute turn context cwd [@anp-oai](https://github.com/anp-oai)
  + [#28642](https://github.com/openai/codex/pull/28642) thread-store: fix response fixture compilation [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28580](https://github.com/openai/codex/pull/28580) [codex] Support object-valued plugin MCP manifests [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#28599](https://github.com/openai/codex/pull/28599) code-mode: move cell state into library actor [@cconger](https://github.com/cconger)
  + [#28471](https://github.com/openai/codex/pull/28471) [codex] Test code-mode variable truncation [@aibrahim-oai](https://github.com/aibrahim-oai)
  + [#28655](https://github.com/openai/codex/pull/28655) Revert thread recencyAt for sidebar ordering [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28638](https://github.com/openai/codex/pull/28638) core: remove redundant TurnContext and Prompt fields [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28656](https://github.com/openai/codex/pull/28656) [codex] Persist built-in image results reported as generating [@won-openai](https://github.com/won-openai)
  + [#28512](https://github.com/openai/codex/pull/28512) Resume exec-server sessions after disconnect [@jif-oai](https://github.com/jif-oai)
  + [#28546](https://github.com/openai/codex/pull/28546) Back off registry retries during exec recovery [@jif-oai](https://github.com/jif-oai)
  + [#28561](https://github.com/openai/codex/pull/28561) Add join key for MAv2 inter-agent messages [@jif-oai](https://github.com/jif-oai)
  + [#28699](https://github.com/openai/codex/pull/28699) app-server: keep the model cache warm [@jif-oai](https://github.com/jif-oai)
  + [#28705](https://github.com/openai/codex/pull/28705) Replace SkillsManager with SkillsService [@jif-oai](https://github.com/jif-oai)
  + [#27965](https://github.com/openai/codex/pull/27965) [ez][codex-rs] Support apps.\_default.default\_tools\_approval\_mode [@zamoshchin-openai](https://github.com/zamoshchin-openai)
  + [#28359](https://github.com/openai/codex/pull/28359) Run fs helper through Windows sandbox wrapper [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#28628](https://github.com/openai/codex/pull/28628) [codex] Repair invalid skill frontmatter scalars [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#28632](https://github.com/openai/codex/pull/28632) Tell codex to avoid changing rollout format. [@anp-oai](https://github.com/anp-oai)
  + [#28738](https://github.com/openai/codex/pull/28738) Scope command approvals by execution environment [@jif-oai](https://github.com/jif-oai)
  + [#19047](https://github.com/openai/codex/pull/19047) feat: add run task identity primitives [@adrian-openai](https://github.com/adrian-openai)
  + [#28671](https://github.com/openai/codex/pull/28671) [codex] Restore thread recency with compatible migration history [@nornagon-openai](https://github.com/nornagon-openai)
  + [#28768](https://github.com/openai/codex/pull/28768) Extract TUI plugin catalog rendering [@canvrno-oai](https://github.com/canvrno-oai)
  + [#28389](https://github.com/openai/codex/pull/28389) [codex] Use compact OpenAI docs search queries [@kkahadze-oai](https://github.com/kkahadze-oai)
  + [#28681](https://github.com/openai/codex/pull/28681) unified-exec: preserve PathUri through exec-server [@anp-oai](https://github.com/anp-oai)
  + [#28731](https://github.com/openai/codex/pull/28731) [codex] Track plugin install and import telemetry failures [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#28651](https://github.com/openai/codex/pull/28651) exec-server: expose environment registry payloads [@viyatb-oai](https://github.com/viyatb-oai)
  + [#28771](https://github.com/openai/codex/pull/28771) fix(plugins): support root local marketplace plugins [@caseychow-oai](https://github.com/caseychow-oai)
  + [#28791](https://github.com/openai/codex/pull/28791) bazel: refresh expired macOS SDK pin [@anp-oai](https://github.com/anp-oai)
  + [#28782](https://github.com/openai/codex/pull/28782) [codex] trace tools build latency [@owenlin0](https://github.com/owenlin0)
  + [#28778](https://github.com/openai/codex/pull/28778) path-uri: decouple native path parsing [@anp-oai](https://github.com/anp-oai)
  + [#28774](https://github.com/openai/codex/pull/28774) feat(exec-server): add Noise rendezvous environment [@apanasenko-oai](https://github.com/apanasenko-oai)
  + [#28812](https://github.com/openai/codex/pull/28812) [codex] Add optional IDs to response items [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28784](https://github.com/openai/codex/pull/28784) fix(install): support older awk checksum parsing [@fcoury-oai](https://github.com/fcoury-oai)
  + [#28826](https://github.com/openai/codex/pull/28826) [codex] Use unique IDs for realtime-routed turns [@guinness-oai](https://github.com/guinness-oai)
  + [#27986](https://github.com/openai/codex/pull/27986) [codex] control automatic realtime handoff delivery [@jiayuhuang-openai](https://github.com/jiayuhuang-openai)
  + [#28836](https://github.com/openai/codex/pull/28836) [codex] Support assistant realtime append text [@guinness-oai](https://github.com/guinness-oai)
  + [#28374](https://github.com/openai/codex/pull/28374) Refresh signed exec-server URLs on reconnect [@apanasenko-oai](https://github.com/apanasenko-oai)
  + [#28825](https://github.com/openai/codex/pull/28825) Expose selecte namespaces as direct model tools [@won-openai](https://github.com/won-openai)
  + [#28790](https://github.com/openai/codex/pull/28790) [codex] Support plugin manifest path lists [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#28851](https://github.com/openai/codex/pull/28851) Record more path migration guidance for codex. [@anp-oai](https://github.com/anp-oai)
  + [#28780](https://github.com/openai/codex/pull/28780) unified-exec: retain PathUri in command events [@anp-oai](https://github.com/anp-oai)
  + [#28605](https://github.com/openai/codex/pull/28605) [codex] Split plugin and skill warmup tracing [@mzeng-openai](https://github.com/mzeng-openai)
  + [#28608](https://github.com/openai/codex/pull/28608) [codex] Pass plugin namespace into skill loading [@mzeng-openai](https://github.com/mzeng-openai)
  + [#28746](https://github.com/openai/codex/pull/28746) [codex] add rollout token budget configuration (1/N) [@rka-oai](https://github.com/rka-oai)
  + [#28766](https://github.com/openai/codex/pull/28766) Add network environment ID plumbing [@jif-oai](https://github.com/jif-oai)
  + [#28915](https://github.com/openai/codex/pull/28915) Avoid sandbox helper in apply\_patch approval tests [@jif-oai](https://github.com/jif-oai)
  + [#28813](https://github.com/openai/codex/pull/28813) Pause active goals before TUI interrupts [@etraut-openai](https://github.com/etraut-openai)
  + [#28895](https://github.com/openai/codex/pull/28895) Recover exec process stdin writes [@jif-oai](https://github.com/jif-oai)
  + [#28940](https://github.com/openai/codex/pull/28940) Pin Windows argument lint to Windows 2022 [@rka-oai](https://github.com/rka-oai)
  + [#28914](https://github.com/openai/codex/pull/28914) Scope MCP sandbox metadata to server environment [@jif-oai](https://github.com/jif-oai)
  + [#28911](https://github.com/openai/codex/pull/28911) Add turn-scoped context contributions [@jif-oai](https://github.com/jif-oai)
  + [#28808](https://github.com/openai/codex/pull/28808) Fix goal-first live threads missing from thread/list [@etraut-openai](https://github.com/etraut-openai)
  + [#25019](https://github.com/openai/codex/pull/25019) [codex] Initialize exec-server OpenTelemetry at startup [@starr-openai](https://github.com/starr-openai)
  + [#28943](https://github.com/openai/codex/pull/28943) [codex] Fix Windows sandbox runtime ACL refresh [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#28946](https://github.com/openai/codex/pull/28946) Synchronize realtime notification test requests [@rka-oai](https://github.com/rka-oai)
  + [#28822](https://github.com/openai/codex/pull/28822) Add Config for Time Reminders (1/n) [@rka-oai](https://github.com/rka-oai)
  + [#28494](https://github.com/openai/codex/pull/28494) [codex] rollout budget implementation (2/N) [@rka-oai](https://github.com/rka-oai)
  + [#27500](https://github.com/openai/codex/pull/27500) Support `openai/form` extended form elicitations [@gpeal](https://github.com/gpeal)
  + [#28949](https://github.com/openai/codex/pull/28949) [codex] Make thread store turn filter optional [@wiltzius-openai](https://github.com/wiltzius-openai)
  + [#28824](https://github.com/openai/codex/pull/28824) current time reminders impl for system clock (2/n) [@rka-oai](https://github.com/rka-oai)
  + [#27812](https://github.com/openai/codex/pull/27812) [codex] Cache plugin metadata for tool suggestions [@mzeng-openai](https://github.com/mzeng-openai)
  + [#28854](https://github.com/openai/codex/pull/28854) apply-patch: carry paths as PathUri [@anp-oai](https://github.com/anp-oai)
  + [#28835](https://github.com/openai/codex/pull/28835) Add app-server current-time impl (3/n) [@rka-oai](https://github.com/rka-oai)
  + [#26496](https://github.com/openai/codex/pull/26496) Make auto-review on-request prompt more proactive [@maja-openai](https://github.com/maja-openai)
  + [#28947](https://github.com/openai/codex/pull/28947) [codex] Remove hardcoded app ID filters [@ericning-o](https://github.com/ericning-o)
  + [#28959](https://github.com/openai/codex/pull/28959) TUI: improve unified mention selection visibility [@canvrno-oai](https://github.com/canvrno-oai)
  + [#27132](https://github.com/openai/codex/pull/27132) Emit Trusted MCP App Identity on Tool-Call Items [@martinauyeung-oai](https://github.com/martinauyeung-oai)
  + [#19049](https://github.com/openai/codex/pull/19049) feat: opt ChatGPT auth into agent identity [@adrian-openai](https://github.com/adrian-openai)
  + [#28770](https://github.com/openai/codex/pull/28770) [connectors] Ignore synthetic links for app accessibility [@adaley-openai](https://github.com/adaley-openai)
  + [#28863](https://github.com/openai/codex/pull/28863) [codex] Preserve remote plugin download status errors [@xl-openai](https://github.com/xl-openai)
  + [#28958](https://github.com/openai/codex/pull/28958) core: load AGENTS.md from foreign environments [@anp-oai](https://github.com/anp-oai)
  + [#28789](https://github.com/openai/codex/pull/28789) [codex] Support marketplace plugin manifest fallback [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#28993](https://github.com/openai/codex/pull/28993) [codex] Remove child AGENTS.md prompt experiment [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28989](https://github.com/openai/codex/pull/28989) core: log AGENTS.md paths as URIs [@anp-oai](https://github.com/anp-oai)
  + [#28983](https://github.com/openai/codex/pull/28983) core: keep remote exec on reported shell [@anp-oai](https://github.com/anp-oai)
  + [#28844](https://github.com/openai/codex/pull/28844) [codex] Reuse parsed plugin skills during session startup [@xl-openai](https://github.com/xl-openai)
  + [#28953](https://github.com/openai/codex/pull/28953) core: add UUIDv7 context window IDs [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28951](https://github.com/openai/codex/pull/28951) [plugins] Refresh plugin and tool caches after remote install [@adaley-openai](https://github.com/adaley-openai)
  + [#28856](https://github.com/openai/codex/pull/28856) Always use AVAS for realtime WebRTC calls [@bakks](https://github.com/bakks)
  + [#28814](https://github.com/openai/codex/pull/28814) [codex] Assign response item IDs when recording history [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29005](https://github.com/openai/codex/pull/29005) [codex] Skip curated repo sync for remote plugins [@xl-openai](https://github.com/xl-openai)
  + [#29011](https://github.com/openai/codex/pull/29011) [codex] add clock current-time tool [@rka-oai](https://github.com/rka-oai)
  + [#29012](https://github.com/openai/codex/pull/29012) core: assign item IDs to compacted replacement history [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29022](https://github.com/openai/codex/pull/29022) [codex] Support protected resource OAuth discovery [@xl-openai](https://github.com/xl-openai)
  + [#28674](https://github.com/openai/codex/pull/28674) [1/3] core: add remote environment connection lifecycle [@sayan-oai](https://github.com/sayan-oai)
  + [#28683](https://github.com/openai/codex/pull/28683) [2/3] core: track starting environments in snapshots [@sayan-oai](https://github.com/sayan-oai)
  + [#29025](https://github.com/openai/codex/pull/29025) [3/3] app-server: configure environment connection timeout [@sayan-oai](https://github.com/sayan-oai)
  + [#28685](https://github.com/openai/codex/pull/28685) Add per-turn multi-agent mode [@shijie-oai](https://github.com/shijie-oai)
  + [#28792](https://github.com/openai/codex/pull/28792) Expose thread-level multi-agent mode [@shijie-oai](https://github.com/shijie-oai)
  + [#28707](https://github.com/openai/codex/pull/28707) [codex] abort turns when rollout budgets expire (token budget 3/3) [@rka-oai](https://github.com/rka-oai)
  + [#28899](https://github.com/openai/codex/pull/28899) Scope network approvals by environment [@jif-oai](https://github.com/jif-oai)
  + [#29086](https://github.com/openai/codex/pull/29086) Document raw response item compatibility [@jif-oai](https://github.com/jif-oai)
  + [#28489](https://github.com/openai/codex/pull/28489) Add indexed web search mode [@winston-openai](https://github.com/winston-openai)
  + [#28942](https://github.com/openai/codex/pull/28942) Add config toggles for orchestrator skills and MCP [@jif-oai](https://github.com/jif-oai)
  + [#29099](https://github.com/openai/codex/pull/29099) Keep remote exec commands native to the executor [@jif-oai](https://github.com/jif-oai)
  + [#29095](https://github.com/openai/codex/pull/29095) Use cached and live web access terminology [@winston-openai](https://github.com/winston-openai)
  + [#29042](https://github.com/openai/codex/pull/29042) [codex] trace pre-sampling skill and persistence latency [@rphilizaire-openai](https://github.com/rphilizaire-openai)
  + [#29132](https://github.com/openai/codex/pull/29132) chore(deps): advance tokio-tungstenite [@apanasenko-oai](https://github.com/apanasenko-oai)
  + [#29006](https://github.com/openai/codex/pull/29006) [codex] Preserve skill descriptions outside model context [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#29154](https://github.com/openai/codex/pull/29154) Allow resume and settings commands during tasks and MCP startup [@etraut-openai](https://github.com/etraut-openai)
  + [#29256](https://github.com/openai/codex/pull/29256) core: add context window lineage IDs [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29259](https://github.com/openai/codex/pull/29259) [codex] prototype mcp\_history thread hint injection [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29255](https://github.com/openai/codex/pull/29255) [codex] add configurable token budget compaction reminder [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29295](https://github.com/openai/codex/pull/29295) [codex] simplify token budget context [@pakrym-oai](https://github.com/pakrym-oai)
  + [#29108](https://github.com/openai/codex/pull/29108) Carry sandbox intent to remote exec servers [@jif-oai](https://github.com/jif-oai)
  + [#29325](https://github.com/openai/codex/pull/29325) Test pipelined scalar exec-server requests [@jif-oai](https://github.com/jif-oai)
  + [#29326](https://github.com/openai/codex/pull/29326) Parallelize skill metadata stats [@jif-oai](https://github.com/jif-oai)
  + [#29329](https://github.com/openai/codex/pull/29329) Use controlled time for remote initialization timeout test [@jif-oai](https://github.com/jif-oai)
  + [#29170](https://github.com/openai/codex/pull/29170) code-mode: define transport-neutral runtime types [@cconger](https://github.com/cconger)
  + [#29285](https://github.com/openai/codex/pull/29285) code-mode: move session ownership into runtime [@cconger](https://github.com/cconger)
  + [#29286](https://github.com/openai/codex/pull/29286) code-mode: linearize cell terminal state [@cconger](https://github.com/cconger)
  + [#29287](https://github.com/openai/codex/pull/29287) code-mode: make session shutdown authoritative [@cconger](https://github.com/cconger)
  + [#29301](https://github.com/openai/codex/pull/29301) [prompting] updated plan mode prompt [@rhan-oai](https://github.com/rhan-oai)
  + [#29288](https://github.com/openai/codex/pull/29288) code-mode: preserve dropped observation output [@cconger](https://github.com/cconger)
  + [#29289](https://github.com/openai/codex/pull/29289) code-mode: preserve initial yield at completion [@cconger](https://github.com/cconger)
  + [#28260](https://github.com/openai/codex/pull/28260) [codex] Add internal auto-compaction opt-out [@rhan-oai](https://github.com/rhan-oai)
  + [#29371](https://github.com/openai/codex/pull/29371) Propagate safety buffering events to app-server clients [@fc-oai](https://github.com/fc-oai)
  + [#29393](https://github.com/openai/codex/pull/29393) chore: fix merge race (auto-compaction feature access) [@sayan-oai](https://github.com/sayan-oai)
  + [#29327](https://github.com/openai/codex/pull/29327) Persist session IDs across thread resume [@jif-oai](https://github.com/jif-oai)
  + [#29324](https://github.com/openai/codex/pull/29324) Simplify multi-agent mode controls [@jif-oai](https://github.com/jif-oai)
  + [#29113](https://github.com/openai/codex/pull/29113) Apply sandbox intent inside remote exec servers [@jif-oai](https://github.com/jif-oai)
  + [#29001](https://github.com/openai/codex/pull/29001) Add workspace messages app-server API [@xli-oai](https://github.com/xli-oai)
  + [#29432](https://github.com/openai/codex/pull/29432) Stop logging every Responses WebSocket event [@jif-oai](https://github.com/jif-oai)
  + [#29073](https://github.com/openai/codex/pull/29073) core: refresh environment context before sampling [@sayan-oai](https://github.com/sayan-oai)
  + [#29455](https://github.com/openai/codex/pull/29455) fix(core): restore thread\_source in x-codex-turn-metadata [@owenlin0](https://github.com/owenlin0)
  + [#29457](https://github.com/openai/codex/pull/29457) Filter noisy targets from persistent logs [@jif-oai](https://github.com/jif-oai)
  + [#29429](https://github.com/openai/codex/pull/29429) remove flag for image preparation [@rka-oai](https://github.com/rka-oai)
  + [#29143](https://github.com/openai/codex/pull/29143) ci: restore custom Windows runner with hermetic LLVM 0.7.9 [@anp-oai](https://github.com/anp-oai)
  + [#27102](https://github.com/openai/codex/pull/27102) [codex] Centralize Plugin Analytics Metadata [@jameswt-oai](https://github.com/jameswt-oai)
  + [#26703](https://github.com/openai/codex/pull/26703) TUI Plugin Sharing 3 - render remote plugin catalog sections [@canvrno-oai](https://github.com/canvrno-oai)
  + [#29424](https://github.com/openai/codex/pull/29424) Report remote sandbox denials semantically [@jif-oai](https://github.com/jif-oai)
  + [#28968](https://github.com/openai/codex/pull/28968) core: rename metadata -> internal\_chat\_message\_metadata\_passthrough [@owenlin0](https://github.com/owenlin0)
  + [#29464](https://github.com/openai/codex/pull/29464) [sdk/python] Stop advertising HTTP image URLs [@rka-oai](https://github.com/rka-oai)
  + [#28793](https://github.com/openai/codex/pull/28793) [codex] Fix usage-limit reset copy and state [@jayp-oai](https://github.com/jayp-oai)
  + [#27982](https://github.com/openai/codex/pull/27982) [codex] Start the guardian child session when parent session is started [@jgershen-oai](https://github.com/jgershen-oai)
  + [#29468](https://github.com/openai/codex/pull/29468) core: remove unused permissions cwd plumbing [@bolinfest](https://github.com/bolinfest)
  + [#26707](https://github.com/openai/codex/pull/26707) PAC 2 - Add shared auth system proxy contract [@canvrno-oai](https://github.com/canvrno-oai)
  + [#28991](https://github.com/openai/codex/pull/28991) Allow ChatGPT accounts without email [@efrazer-oai](https://github.com/efrazer-oai)
  + [#29423](https://github.com/openai/codex/pull/29423) [codex] configure rollout budget reminder thresholds [@rka-oai](https://github.com/rka-oai)
  + [#26678](https://github.com/openai/codex/pull/26678) permission profiles: expose availability to clients [@viyatb-oai](https://github.com/viyatb-oai)
  + [#29476](https://github.com/openai/codex/pull/29476) [codex] handle request\_user\_input in app-server test client [@celia-oai](https://github.com/celia-oai)
  + [#29479](https://github.com/openai/codex/pull/29479) fix(config): address permission profile review follow-ups [@viyatb-oai](https://github.com/viyatb-oai)
  + [#29014](https://github.com/openai/codex/pull/29014) Honor startup custom CA bundles with managed MITM [@winston-openai](https://github.com/winston-openai)
  + [#29480](https://github.com/openai/codex/pull/29480) chore: advance tungstenite fork pins [@apanasenko-oai](https://github.com/apanasenko-oai)
  + [#27669](https://github.com/openai/codex/pull/27669) [codex-core-plugins] Remote Plugin ID Persisted to File [@jameswt-oai](https://github.com/jameswt-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.142.0)
* 2026-06-18

  ### Codex app 26.616

  ### New features

  + Added [Record & Replay](/codex/extend/record-and-replay), a macOS feature that turns
    a demonstrated workflow into a reusable skill. Initial availability excludes
    the European Economic Area, the United Kingdom, and Switzerland. You or your
    administrator must also enable Computer Use.
  + Added bulk actions to [automation](/codex/automations) run history so you
    can mark every run as read or archive eligible runs.
  + Added [thread handoff between local and remote hosts](/codex/remote-connections#hand-off-a-task-between-hosts),
    so you can move a thread to a matching project on a connected host and
    continue it there. Codex can also coordinate the handoff for you.

  ### Performance improvements and bug fixes

  + Added new [deep links](/codex/app/commands#settings) to manage SSH connections.
  + Improved Browser Use so visible-tab routing and annotations persist when a
    draft browser session moves to the server.
  + Additional performance improvements and bug fixes.
* 2026-06-18

  ### Codex CLI 0.141.0

  ```
  $ npm install -g @openai/codex@0.141.0
  ```

    View details 

  ## New Features

  + Remote executors now use authenticated, end-to-end encrypted Noise relay channels. ([#26242](https://github.com/openai/codex/pull/26242), [#26245](https://github.com/openai/codex/pull/26245))
  + Cross-platform remote execution now preserves executor-native working directories and shells, including filesystem permission paths across app-server and exec-server boundaries. ([#27819](https://github.com/openai/codex/pull/27819), [#27995](https://github.com/openai/codex/pull/27995), [#28032](https://github.com/openai/codex/pull/28032), [#28122](https://github.com/openai/codex/pull/28122), [#28165](https://github.com/openai/codex/pull/28165), [#28367](https://github.com/openai/codex/pull/28367))
  + Selected executor plugins can activate their stdio MCP servers per thread; plugin discovery also adds a created-by-me marketplace and auth-specific curated catalogs. ([#27870](https://github.com/openai/codex/pull/27870), [#27884](https://github.com/openai/codex/pull/27884), [#27893](https://github.com/openai/codex/pull/27893), [#28203](https://github.com/openai/codex/pull/28203), [#28383](https://github.com/openai/codex/pull/28383))
  + App-server clients can list immediate child threads, correlate external-agent imports with detailed results, and read or redeem rate-limit reset credits. ([#26662](https://github.com/openai/codex/pull/26662), [#28008](https://github.com/openai/codex/pull/28008), [#28143](https://github.com/openai/codex/pull/28143))
  + Realtime clients can explicitly append speech, control how Codex responses enter conversations, and omit startup context. ([#27917](https://github.com/openai/codex/pull/27917), [#28405](https://github.com/openai/codex/pull/28405))
  + TUI input prompts can auto-resolve after inactivity, with a countdown that pauses on interaction. ([#28235](https://github.com/openai/codex/pull/28235))

  ## Bug Fixes

  + Hook trust bypass now persists through `codex exec` thread start and resume, while blocking `PostToolUse` hooks correctly reject code-mode tool calls. ([#26434](https://github.com/openai/codex/pull/26434), [#28365](https://github.com/openai/codex/pull/28365))
  + Plugin capabilities now route consistently by authentication mode, deduplicate conflicting App/MCP declarations, and preserve remote marketplace ordering. ([#27461](https://github.com/openai/codex/pull/27461), [#27602](https://github.com/openai/codex/pull/27602), [#27607](https://github.com/openai/codex/pull/27607), [#27902](https://github.com/openai/codex/pull/27902), [#27958](https://github.com/openai/codex/pull/27958), [#28395](https://github.com/openai/codex/pull/28395))
  + Windows sandbox execution repairs stale credentials automatically and gives PowerShell commands more time before backgrounding. ([#27086](https://github.com/openai/codex/pull/27086), [#27944](https://github.com/openai/codex/pull/27944))
  + Idle exec-server relays remain connected, and steered user input immediately interrupts `wait_agent`. ([#28286](https://github.com/openai/codex/pull/28286), [#28341](https://github.com/openai/codex/pull/28341))
  + Bundled SQLite is pinned to a version containing the WAL-reset corruption fix. ([#27992](https://github.com/openai/codex/pull/27992))
  + TLS connections now support P-521 certificate signatures commonly used by enterprise proxies. ([#27706](https://github.com/openai/codex/pull/27706))

  ## Chores

  + Reduced latency and memory use in large, tool-heavy sessions by caching tool search and eliminating repeated request and history copies. ([#27258](https://github.com/openai/codex/pull/27258), [#27813](https://github.com/openai/codex/pull/27813), [#28306](https://github.com/openai/codex/pull/28306), [#28309](https://github.com/openai/codex/pull/28309), [#28313](https://github.com/openai/codex/pull/28313), [#28323](https://github.com/openai/codex/pull/28323), [#28327](https://github.com/openai/codex/pull/28327))
  + Bounded prompt-image caching to 64 MiB and feedback uploads to eight related threads. ([#28294](https://github.com/openai/codex/pull/28294), [#28332](https://github.com/openai/codex/pull/28332))
  + Terminal resize reflow is now always enabled, ignoring obsolete disabled settings. ([#27794](https://github.com/openai/codex/pull/27794))

  ## Changelog

  Full Changelog: [rust-v0.140.0...rust-v0.141.0](https://github.com/openai/codex/compare/rust-v0.140.0...rust-v0.141.0)

  + [#28001](https://github.com/openai/codex/pull/28001) [codex] package Windows ARM64 on x64 [@tamird](https://github.com/tamird)
  + [#28032](https://github.com/openai/codex/pull/28032) [codex] Carry exec-server cwd as PathUri [@anp-oai](https://github.com/anp-oai)
  + [#27607](https://github.com/openai/codex/pull/27607) [codex] Dedupe plugin MCPs by app declaration name [@felixxia-oai](https://github.com/felixxia-oai)
  + [#27992](https://github.com/openai/codex/pull/27992) [codex] Pin bundled SQLite to fixed WAL-reset version [@gpeal](https://github.com/gpeal)
  + [#28125](https://github.com/openai/codex/pull/28125) build: run buildifier from just fmt [@anp-oai](https://github.com/anp-oai)
  + [#28120](https://github.com/openai/codex/pull/28120) bazel: add PowerShell to Wine test harness [@anp-oai](https://github.com/anp-oai)
  + [#27819](https://github.com/openai/codex/pull/27819) path-uri: render native paths across platforms [@anp-oai](https://github.com/anp-oai)
  + [#28122](https://github.com/openai/codex/pull/28122) [codex] exec-server honors remote environment cwd and shell [@anp-oai](https://github.com/anp-oai)
  + [#26662](https://github.com/openai/codex/pull/26662) feat(app-server): filter threads by parent [@btraut-openai](https://github.com/btraut-openai)
  + [#27884](https://github.com/openai/codex/pull/27884) Add selected-plugin precedence and attribution to the MCP catalog [@jif-oai](https://github.com/jif-oai)
  + [#27870](https://github.com/openai/codex/pull/27870) Discover stdio MCP servers from selected executor plugins [@jif-oai](https://github.com/jif-oai)
  + [#28283](https://github.com/openai/codex/pull/28283) [codex] update multi-agent v2 prompts [@jif-oai](https://github.com/jif-oai)
  + [#27602](https://github.com/openai/codex/pull/27602) [codex] Preserve plugin apps in connector listings [@felixxia-oai](https://github.com/felixxia-oai)
  + [#27461](https://github.com/openai/codex/pull/27461) [codex] Skip plugin MCP OAuth for matching app routes [@felixxia-oai](https://github.com/felixxia-oai)
  + [#27893](https://github.com/openai/codex/pull/27893) Activate selected executor plugin MCPs in app-server [@jif-oai](https://github.com/jif-oai)
  + [#28332](https://github.com/openai/codex/pull/28332) [codex] Cap feedback upload subtrees [@jif-oai](https://github.com/jif-oai)
  + [#27365](https://github.com/openai/codex/pull/27365) Represent dynamic tools with explicit namespaces internally [@sayan-oai](https://github.com/sayan-oai)
  + [#28333](https://github.com/openai/codex/pull/28333) skills: hide orchestrator skills with a local executor [@jif-oai](https://github.com/jif-oai)
  + [#27756](https://github.com/openai/codex/pull/27756) [codex] simplify shell snapshot ownership [@pakrym-oai](https://github.com/pakrym-oai)
  + [#27794](https://github.com/openai/codex/pull/27794) Remove terminal resize reflow flag gates [@etraut-openai](https://github.com/etraut-openai)
  + [#28286](https://github.com/openai/codex/pull/28286) chore: restore exec-server relay keepalives [@jif-oai](https://github.com/jif-oai)
  + [#28164](https://github.com/openai/codex/pull/28164) [codex] simplify memory read metrics [@pakrym-oai](https://github.com/pakrym-oai)
  + [#27371](https://github.com/openai/codex/pull/27371) Expose explicit dynamic tool namespaces in thread start [@sayan-oai](https://github.com/sayan-oai)
  + [#28309](https://github.com/openai/codex/pull/28309) linearize history output normalization [@jif-oai](https://github.com/jif-oai)
  + [#28306](https://github.com/openai/codex/pull/28306) avoid cloning sampling request input [@jif-oai](https://github.com/jif-oai)
  + [#28323](https://github.com/openai/codex/pull/28323) serialize websocket requests directly [@jif-oai](https://github.com/jif-oai)
  + [#28313](https://github.com/openai/codex/pull/28313) avoid cloning websocket request history [@jif-oai](https://github.com/jif-oai)
  + [#28344](https://github.com/openai/codex/pull/28344) [codex] remove stale PathExt import [@pakrym-oai](https://github.com/pakrym-oai)
  + [#27059](https://github.com/openai/codex/pull/27059) [codex] Cover OTLP HTTP log and trace event export [@richardopenai](https://github.com/richardopenai)
  + [#28327](https://github.com/openai/codex/pull/28327) reuse encoded Responses request bodies [@jif-oai](https://github.com/jif-oai)
  + [#27995](https://github.com/openai/codex/pull/27995) [codex] preserve explicit environment cwd [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28285](https://github.com/openai/codex/pull/28285) guardian: isolate review context from skills and memories [@jif-oai](https://github.com/jif-oai)
  + [#26702](https://github.com/openai/codex/pull/26702) TUI Plugin Sharing 2 - add remote plugin section plumbing [@canvrno-oai](https://github.com/canvrno-oai)
  + [#28294](https://github.com/openai/codex/pull/28294) bound prompt image cache retention [@jif-oai](https://github.com/jif-oai)
  + [#28257](https://github.com/openai/codex/pull/28257) Support staging OAuth client ID overrides [@apanasenko-oai](https://github.com/apanasenko-oai)
  + [#28341](https://github.com/openai/codex/pull/28341) core: let steer interrupt wait\_agent [@jif-oai](https://github.com/jif-oai)
  + [#28336](https://github.com/openai/codex/pull/28336) skills: cache orchestrator resources per thread [@jif-oai](https://github.com/jif-oai)
  + [#28357](https://github.com/openai/codex/pull/28357) Extract shared Windows sandbox session runner [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#27706](https://github.com/openai/codex/pull/27706) Use aws-lc-rs for rustls crypto provider [@malsamiri-oai](https://github.com/malsamiri-oai)
  + [#28347](https://github.com/openai/codex/pull/28347) [codex] add path-types skill [@anp-oai](https://github.com/anp-oai)
  + [#28235](https://github.com/openai/codex/pull/28235) Add request user input auto-resolution timer [@shijie-oai](https://github.com/shijie-oai)
  + [#28234](https://github.com/openai/codex/pull/28234) [mcp] Increase default tool timeout to 300 seconds [@adaley-openai](https://github.com/adaley-openai)
  + [#28008](https://github.com/openai/codex/pull/28008) [codex] Add external agent import result accounting [@charlesgong-openai](https://github.com/charlesgong-openai)
  + [#27944](https://github.com/openai/codex/pull/27944) recover stale Windows sandbox credentials [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#27086](https://github.com/openai/codex/pull/27086) Add Windows unified exec yield floor [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#28358](https://github.com/openai/codex/pull/28358) Add hidden Windows sandbox wrapper entrypoint [@iceweasel-oai](https://github.com/iceweasel-oai)
  + [#27258](https://github.com/openai/codex/pull/27258) core: cache the tool search handler per session [@mchen-oai](https://github.com/mchen-oai)
  + [#28143](https://github.com/openai/codex/pull/28143) feat(app-server): expose rate-limit reset credits [@jayp-oai](https://github.com/jayp-oai)
  + [#28355](https://github.com/openai/codex/pull/28355) feat(core): add metadata field to ResponseItem [@owenlin0](https://github.com/owenlin0)
  + [#28203](https://github.com/openai/codex/pull/28203) [codex] Add created-by-me remote plugin marketplace [@ericning-o](https://github.com/ericning-o)
  + [#28365](https://github.com/openai/codex/pull/28365) Respect blocking PostToolUse hooks in code mode [@abhinav-oai](https://github.com/abhinav-oai)
  + [#27813](https://github.com/openai/codex/pull/27813) [codex] Reuse Apps policy evaluation across MCP tool exposure [@mzeng-openai](https://github.com/mzeng-openai)
  + [#28300](https://github.com/openai/codex/pull/28300) Deflake realtime handoff steering test [@felixxia-oai](https://github.com/felixxia-oai)
  + [#28395](https://github.com/openai/codex/pull/28395) [codex] Preserve remote plugin directory order [@jameswt-oai](https://github.com/jameswt-oai)
  + [#27955](https://github.com/openai/codex/pull/27955) [codex] retain resolved environments across turns [@pakrym-oai](https://github.com/pakrym-oai)
  + [#27917](https://github.com/openai/codex/pull/27917) Add realtime speech append control [@guinness-oai](https://github.com/guinness-oai)
  + [#27093](https://github.com/openai/codex/pull/27093) [codex-analytics] Analytics Capture to File in Debug Builds [@jameswt-oai](https://github.com/jameswt-oai)
  + [#26242](https://github.com/openai/codex/pull/26242) exec-server: add Noise relay transport [@viyatb-oai](https://github.com/viyatb-oai)
  + [#28165](https://github.com/openai/codex/pull/28165) Use PathUri in filesystem permission paths for exec-server [@anp-oai](https://github.com/anp-oai)
  + [#28415](https://github.com/openai/codex/pull/28415) [codex] Fix missing response item metadata in tests [@adaley-openai](https://github.com/adaley-openai)
  + [#27058](https://github.com/openai/codex/pull/27058) [codex] Add second-based OTEL duration histograms [@richardopenai](https://github.com/richardopenai)
  + [#27902](https://github.com/openai/codex/pull/27902) [codex] Centralize plugin auth capability filtering [@felixxia-oai](https://github.com/felixxia-oai)
  + [#28405](https://github.com/openai/codex/pull/28405) Add a toggle for realtime startup context [@guinness-oai](https://github.com/guinness-oai)
  + [#26434](https://github.com/openai/codex/pull/26434) Preserve hook trust bypass in codex exec threads [@abhinav-oai](https://github.com/abhinav-oai)
  + [#26245](https://github.com/openai/codex/pull/26245) exec-server: default remote transport to Noise [@viyatb-oai](https://github.com/viyatb-oai)
  + [#28383](https://github.com/openai/codex/pull/28383) [codex] Load API curated marketplace by auth [@felixxia-oai](https://github.com/felixxia-oai)
  + [#27958](https://github.com/openai/codex/pull/27958) [codex] Make plugin details capability aware [@felixxia-oai](https://github.com/felixxia-oai)
  + [#28367](https://github.com/openai/codex/pull/28367) Use ApiPathString in app-server filesystem permission paths [@anp-oai](https://github.com/anp-oai)
  + [#28421](https://github.com/openai/codex/pull/28421) [codex] Bind shell snapshots to retained thread environments [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28429](https://github.com/openai/codex/pull/28429) [codex] Add interruptible sleep tool [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28441](https://github.com/openai/codex/pull/28441) [codex] Use expect in integration tests [@pakrym-oai](https://github.com/pakrym-oai)
  + [#28163](https://github.com/openai/codex/pull/28163) [codex] Use local environment for user shell commands [@pakrym-oai](https://github.com/pakrym-oai)

  [Full release on Github](https://github.com/openai/codex/releases/tag/rust-v0.141.0)
* 2026-06-16

  ### Codex app features are available in the EEA, UK, and Switzerland

  More Codex app capabilities are rolling out to users in the European Economic
  Area, the United Kingdom, and Switzerland:

  + [Computer Use](/codex/computer-use) is available on macOS and Windows in
    these regions, so Codex can operate desktop apps by seeing, clicking, and
    typing.
  + The [Codex Chrome extension](/codex/chrome-extension) is available for
    browser tasks that need signed-in Chrome context, working across tabs in the
    background without taking over your browser.
  + [Memories](/codex/customization/memories) can remember useful preferences, recurring
    workflows, tech stacks, and repository conventions when enabled. Memories are
    off by default in the European Economic Area, the United Kingdom, and
    Switzerland.
  + [Chronicle](/codex/customization/chronicle) is available as an opt-in research
    preview for ChatGPT Pro subscribers on macOS, helping Codex build memories
    from recent screen context.
* 2026-06-15

  ### ChatGPT for iOS 1.2026.160

  ### New features

  + Added a workspace file browser for previewing files and linking workspace paths
    into prompts.
  + Added a directory picker for choosing a workspace folder when starting a new
    thread.
  + Added controls to expand or collapse all diffs while reviewing changed files.
  + Added MCP approval choices for allowing requested actions in the current chat
    or across chats.
  + Added LaTeX rendering in Codex messages and plans.

  ### Improvements and bug fixes

  + Improved status indicators for running threads, queued prompts, side chats,
    and subagents.
  + Improved pairing and onboarding with clearer errors, manual pairing-code
    support, and more reliable host selection after pairing.
  + Improved task-list recovery, reconnect state, host-specific refresh, and
    thread performance.
  + Improved Codex profile sharing, activity history, and settings layout.
  + Improved goal workflows with a composer shortcut, desktop-aligned goal message
    actions, and better resumed question handling.
  + Improved assistant message actions, transcript layout, and public rate-limit
    names.
  + Fixed stuck thread-list swipe actions, duplicate messages when reopening a new
    thread, spawned subagents appearing as top-level task rows, and misleading
    connection errors when sending prompts.
* 2026-06-11

  ### Codex app 26.609

  ### New features

  + Added rate-limit reset banking for Plus and Pro users, including one free
    reset at launch and
    [referral invitations](/codex/pricing#invite-friends-and-coworkers) for
    earning more during the current promotion. Eligible Business members can
    invite coworkers to earn shared workspace credits through a separate
    referral program.
  + Added [Developer mode](/codex/browser?surface=app#app-developer-mode) for Browser use in
    Chrome and the Codex in-app browser. It gives Codex controlled Chrome
    DevTools Protocol (CDP) access for performance profiling and deeper debugging
    of network traffic, console output, runtime errors, and page state.
  + Added the `/init` command to the app composer for creating project
    instructions with the same initialization workflow as the Codex CLI.
  + Added customizable macOS Dock icons with light and dark Codex variants.
  + Added Computer Use for Enterprise users outside the European Economic Area,
    the United Kingdom, and Switzerland.
  + Added support for configuring per-app access controls for Computer Use on
    Windows.
  + Added an **Unread chats** section to the command menu, with the most recently
    updated unread chat selected by default.

  ### Performance improvements and bug fixes

  + Made Browser use up to 2x faster through CDP and DOM snapshot optimizations
    that reduce browser round trips.
  + Made command, browser, integration, and source activity summaries easier to
    understand, and improved how completed chats present files, automations, and
    other durable output.
  + Improved plugin management by including workspace plugins, refreshing plugin
    state more reliably after installation or removal, and letting you upload a
    new version of an already-shared plugin without changing its access.
  + Improved usage-limit errors with inline plan and workspace guidance,
    including reset timing when available.
  + Added `Cmd`+`Enter` and `Ctrl`+`Enter` as
    shortcuts for submitting custom approval feedback.
  + Fixed Browser use download handling and improved Developer mode recovery and
    diagnostics.
  + Fixed scheduled automations so they honor the selected approval mode, and
    fixed manual project ordering, Browser tab dragging, MCP app sizing after
    right-pane transitions, and clickable ChatGPT thread mentions.
  + Fixed issues affecting background agent tab restoration, commit and pull
    request message generation, sidebar pull request status updates, Codex Mobile
    QR pairing, remote-control MFA, remote SSH installation and connection,
    updater prompts, and overlay positioning at non-default zoom levels.
  + Additional performance improvements and bug fixes.
* 2026-06-09

  ### Codex app 26.608

  ### New features

  + Added [Import to Codex](/codex/import) flows for importing supported setup
    from Claude Code and Claude Cowork, including during onboarding.
  + Revamped plugins screen with separate tabs, marketplace and
    category filters, keyboard navigation, and clearer install actions.
  + Expanded Settings search to find options from more panels, including Git and
    pets.

  ### Performance improvements and bug fixes

  + Fixed goal timer overlap in narrow layouts.
  + Reduced unread notifications while an active goal continues running.
  + Kept review diff ordering consistent with the file tree.
  + Improved window rendering on systems that don’t support translucent
    backdrops, including Windows 10.
  + Additional performance improvements and bug fixes.
* 2026-06-09

  ### ChatGPT for iOS 1.2026.153

  ### New features

  + Added support for choosing a branch, creating a worktree, and running an
    environment setup script for new threads.
  + Added a Codex profile screen with usage stats and token activity charts.
  + Added `/goal` support for creating and managing goals from Codex Mobile.
  + Added inline review comments when viewing changed files.
  + Added support for asking in side chat from selected transcript text.
  + Added support for editing the latest sent prompt.

  ### Improvements and bug fixes

  + Improved attachment support on Windows hosts.
  + Skills and plugins now appear directly inline in the composer.
  + Improved side chat and queued prompt visibility while a thread is running.
  + Improved message styling, navigation, tool activity, Face ID behavior,
    archived-thread browsing, and thread UI polish.
* 2026-06-04

  ### Codex app updates 26.602

  ### New features

  + Added activity insights and share cards to the
    [Profile section](/codex/app/settings#profile). You can review Codex usage
    highlights and save a profile card; sharing is available on consumer ChatGPT
    plans.

  ### Performance improvements and bug fixes

  + Improved Computer Use startup readiness and appshot error reporting.
  + Fixed browser and review UI issues, including fullscreen browser composer
    controls, hex color swatches, terminal scrollbar alignment, and animated diff
    stat alignment.
  + Expanded onboarding with more role choices so Codex can tailor first-run
    suggestions more accurately.
  + Fixed configuration writes after plugin installation.
  + Additional performance improvements and bug fixes.
* 2026-06-02

  ### Build and deploy websites with Sites

  [**Sites**](/codex/sites) is now available in preview in the Codex app. Use the
  Sites plugin to create, save, deploy, and inspect websites, dashboards, internal
  tools, web apps, and games hosted by OpenAI.

  Open **Sites** in the app sidebar to return to your projects and manage hosted
  environment variables and secrets.

  ChatGPT Business workspaces include Sites by default. ChatGPT Enterprise admins
  can enable Sites for the appropriate roles through role-based access control
  (RBAC).
* 2026-06-02

  ### ChatGPT for iOS 1.2026.146

  ### New features

  + Added an optional Face ID or passcode lock for Codex.
  + Added a new settings screen for choosing Queue or Steer as the default
    follow-up behavior and toggling line wrapping for code diffs.
  + Added support for connecting to Windows machines over SSH.

  ### Improvements and bug fixes

  + Added support for `/side <prompt>` to start a side
    conversation with an initial question.
  + Improved follow-up prompts, the Codex home screen, and viewing changed files.
  + Fixed issues with reconnecting, archiving threads, loading tasks, and
    connecting to hosts.
* 2026-06-01

  ### Use Codex with Amazon Bedrock

  Codex can now use supported OpenAI models available through Amazon Bedrock.
  Configure [Amazon Bedrock as your model provider](/codex/amazon-bedrock) to run
  Codex locally with AWS-managed authentication, account controls, and billing.
* 2026-06-01

  ### Terminal placement controls 26.601

  ### New features

  + Added **Default terminal location** in [General settings](/codex/app/settings#general).
    When the bottom panel is enabled, choose whether the terminal shortcut and
    environment actions open terminal tabs in the bottom panel or the right panel.

  ### Performance improvements and bug fixes

  + Additional performance improvements and bug fixes.

## May 2026

* 2026-05-29

  ### Computer use and mobile access on Windows 26.527

  ### New features

  + [Computer Use](/codex/computer-use) now works on Windows. Codex can
    operate Windows desktop apps by seeing, clicking, and typing in the
    foreground while it works.
  + [Remote control](/codex/remote-connections) now supports Windows devices. You
    can start Codex work on a Windows device from ChatGPT on iOS or Android, or
    from a Mac running Codex, and check its progress remotely.
  + The [Profile section](/codex/app/settings#profile) now shows your profile
    details, usage stats, and token activity.
  + Added thread coordination for local projects and worktrees, including
    separate background threads when explicitly requested.
  + Expanded search for past Codex app threads to include conversation content
    and Git branch names.
  + Added stable identicons for background subagents across the app.
  + Improved keyboard shortcut settings with keypress search and a reset-all
    action.
  + Improved Chrome context capture for Google Docs, Sheets, and Slides tabs.

  ### Performance improvements and bug fixes

  + Additional performance improvements and bug fixes.
* 2026-05-26

  ### GPT-5.3-Codex and GPT-5.2 deprecated

  GPT-5.3-Codex and GPT-5.2 are now deprecated as user-selectable models in Codex
  for users signed in with ChatGPT. API-key workflows aren’t affected.

  Use a current Codex model, such as GPT-5.5, GPT-5.4, or GPT-5.4 mini. See
  [Codex models](/codex/models#deprecated-codex-models) for model availability
  and [Codex pricing](/codex/pricing#credits-overview) for credit rates.
* 2026-05-25

  ### ChatGPT for iOS 1.2026.139

  ### New features

  + Added Spotlight and Shortcuts support for opening Codex Mobile directly.
  + Added browsing for archived Codex threads.
  + Added `/side` for opening a side conversation.
  + Added options to save or copy rendered images.

  ### Improvements and bug fixes

  + Improved iPad keyboard shortcuts.
  + Improved setup and relaunch reliability.
  + Fixed issues with task progress, loading archived threads, previewing code
    changes, and switching hosts.
* 2026-05-21

  ### Appshots, goal mode, and more 26.519

  [Appshots](/codex/appshots) are now available in the Codex app on macOS. Press
  both Command keys to send the frontmost app window to Codex with a screenshot
  and available text, so Codex can work from context in another app without you
  copying, pasting, or describing it manually.

  This launch also includes:

  + [Goal mode](/codex/prompting#goal-mode) is no longer an experimental feature
    and is available in the Codex app, IDE extension, and CLI. With Goal mode, you
    can have Codex drive toward a specific objective for hours or even days.
  + [Remote computer use](/codex/computer-use#locked-use), so Codex can use
    desktop apps after your Mac locks, including remotely via Codex Mobile. Codex
    scopes locked use to active, trusted computer use turns and includes
    safeguards such as short-lived authorization, covered displays, relock on
    local input, and manual-unlock fallback.
  + [Plugin sharing](/plugins/build/plugins#share-a-local-plugin-with-your-workspace)
    through marketplace sources is available for ChatGPT Business. Enterprise
    support is coming soon. Teams can distribute reusable plugin bundles that
    include skills, MCP servers, and lifecycle hooks.
  + [Advanced in-app browser annotations](/codex/browser?surface=app#app-styling-feedback)
    let you tweak styling such as font size, colors, and spacing directly using
    annotations. This gives Codex a clearer signal for changes.
  + Browser-use improvements across in-app browser & Chrome:
    - Codex can now download and extract all image assets from a page much more
      quickly.
    - Codex can now extract structured data from pages more effectively and find
      information more quickly with a read-only JS sandbox.
  + Chrome extension will create less clutter when using it. Codex will no longer
    create tab groups when taking over existing tabs, and at the end of a task for
    handoff. Instead, it uses tab icons to indicate status.
  + Significantly improved reliability for browser use. We fixed bugs on Windows,
    flaky availability of the plugin to non geo-blocked regions, and many other
    issues impacting performance.
* 2026-05-18

  ### ChatGPT for iOS 1.2026.132

  ### New features

  + Added support for opening completed Codex tasks directly from iOS
    notifications.
  + Added the ability to open changed files directly while reviewing a task.

  ### Improvements and bug fixes

  + Improved task resume, reconnection, and foreground reliability.
  + Improved task progress updates, code review, and message composition.
* 2026-05-14

  ### Work with Codex from anywhere

  You can now use Codex from the ChatGPT mobile app by connecting it to a Mac
  running the Codex app. Codex runs from the connected host, so the same projects,
  files, credentials, plugins, skills, and configuration are available from your
  phone.

  See [Remote connections](/codex/remote-connections) for mobile setup, choosing
  a host, what comes from the connected machine, and SSH hosts. This launch also
  includes [Hooks](/codex/hooks) general availability,
  [Codex access tokens](/codex/enterprise/access-tokens) for trusted automation,
  and [Enterprise admin setup](/codex/enterprise/admin-setup) guidance.
* 2026-05-11

  ### Expanded Auto-review documentation

  Added a dedicated
  [Auto-review](/codex/sandboxing/auto-review) page covering the
  reviewer lifecycle, trigger conditions, failure behavior, and local or managed
  configuration.

  Also updated the [Agent approvals & security](/codex/agent-approvals-security)
  and [Sandbox](/codex/sandboxing) docs so they explain more clearly how
  Auto-review relates to the sandbox boundary.
* 2026-05-08

  ### Codex app 26.506

  ### New features

  + Added an in-app trust review flow for hooks and kept Hooks settings reachable even before hooks are fully configured.

  ### Performance improvements and bug fixes

  + Restored tooltip-wrapped dropdowns that could stop opening after the tooltip rewrite.
  + Preserved in-progress message edits across thread switches.
  + Fixed several desktop workflow regressions, including `Ctrl+V` paste in the Windows terminal, opening modified external links outside the in-app browser, and keeping feedback slash commands attached to the right thread.
  + Improved loading and panel polish by showing model loading while a thread resumes, hiding unavailable model controls during load, and bundling summary-panel layout and hover fixes.
  + Kept the Computer Use settings control visible even when uninstalled and disabled problematic extension hover panels.
  + Additional performance improvements and bug fixes.
* 2026-05-07

  ### Codex for Chrome

  With the new extension for Chrome, Codex is even better at working with apps
  and websites in your browser. It works in parallel across tabs in the
  background without taking over your browser, and you stay in control of which
  websites Codex can use.

  Learn more in the [Codex Chrome extension documentation](/codex/chrome-extension).
* 2026-05-06

  ### Codex analytics governance docs update

  Updated the Codex enterprise governance guide with more detailed coverage of the
  Analytics dashboard charts, data export options, and enterprise Analytics API
  endpoints.
* 2026-05-05

  ### Create Codex access tokens

  ChatGPT Enterprise workspace owners and admins can allow permitted members to
  create Codex access tokens for trusted, non-interactive Codex local workflows.
  Members can use access tokens to run Codex from scripts, schedulers, and private
  CI runners with their ChatGPT workspace identity.

  Learn more in [Access tokens](/codex/enterprise/access-tokens).
* 2026-05-05

  ### Codex app 26.429

  ### New features

  + Added dictation cleanup plus a configurable dictation dictionary for names, file paths, and code symbols.
  + Added zoom and download controls to the image lightbox.

  ### Performance improvements and bug fixes

  + Improved voice and dictation error messages for microphone, connection, and quota failures.
  + Fixed in-app browser comment markers so they stay aligned across scrolling, zoom, and responsive layout changes.
  + Made pull request creation and recovery flows more reliable by preserving newly created pull request state, classifying more app-server failures as restart-required, and stopping exhausted remote reconnect loops.
  + Additional performance improvements and bug fixes.

## April 2026

* 2026-04-24

  ### Codex app 26.423

  ### New features

  + Added a tooltip on realtime delegation messages to clarify that Codex uses the surrounding voice conversation as context.

  ### Performance improvements and bug fixes

  + Fixed search in long review files so next and previous results reliably jump to off-screen matches.
  + Kept embedded MCP app panels from restarting or losing state during fullscreen changes and thread reloads.
  + Fixed several desktop regressions, including tray crashes when the local connection is missing, duplicate macOS fullscreen menu entries, and broken global dictation hotkeys on older macOS versions.
  + Additional performance improvements and bug fixes.
* 2026-04-23

  ### GPT-5.5 and Codex app updates

  [GPT-5.5 is now available in Codex](https://openai.com/index/introducing-gpt-5-5/)
  as OpenAI’s newest frontier model for complex coding, computer use, knowledge
  work, and research workflows.

  #### GPT-5.5 in Codex

  GPT-5.5 is the recommended choice for most Codex tasks when it appears in your
  model picker. It’s especially useful for implementation, refactors, debugging,
  testing, validation, and knowledge-work artifacts.

  To switch to GPT-5.5:

  + In the CLI, start a new thread with:

    ```
    codex --model gpt-5.5
    ```

    Or use `/model` during a session.
  + In the IDE extension, choose GPT-5.5 from the model selector in the composer.
  + In the Codex app, choose GPT-5.5 from the model selector in the composer.

  If you don’t see GPT-5.5 yet, update the CLI, IDE extension, or Codex app to
  the latest version. During the rollout, continue using GPT-5.4 if GPT-5.5 is
  not yet available.

  #### Browser use in the Codex app

  The Codex app can now let Codex operate the in-app browser for local
  development servers and file-backed pages. Ask Codex to use the browser when it
  needs to click through a rendered UI, reproduce a visual bug, or verify a local
  fix inside the app.

  Browser use runs through the bundled Browser plugin. In settings, you can
  manage the plugin and review allowed or blocked websites.

  #### Automatic approval reviews

  Codex can route eligible approval prompts through an automatic reviewer agent
  before the request runs. When configured, the Codex app shows an automatic
  review item with the review status and risk level, so you can see whether the
  reviewer approved, denied, stopped, or timed out before deciding.
* 2026-04-20

  ### Codex app 26.417

  ### New features

  + Added local branch search and non-image file pasting in the composer.
  + Added collapsible sidebar sections, tray usage-limit surfacing, and a command-palette theme switcher.

  ### Performance improvements and bug fixes

  + Made review faster and more stable with better diff batching and preserved diff and search state.
  + Fixed projectless cwd and permissions handling, default file opening, spreadsheet suggestions, and remote-control reconnect issues.
  + Additional performance improvements and bug fixes.
* 2026-04-16

  ### Codex can now help with more of your work 26.415

  Codex is becoming a broader workspace for getting work done with AI. This
  update makes it easier to start work with less setup, verify what Codex is
  building, create richer outputs, and keep momentum across longer-running tasks.

  #### Verify more of your work

  The Codex app now includes an early [**in-app browser**](/codex/browser?surface=app). You
  can open local or public pages that don’t require sign-in, comment directly on
  the rendered page, and ask Codex to address page-level feedback.

  ![Codex app showing a browser comment on a local web app preview](/images/codex/app/in-app-browser-light.webp) ![Codex app showing a browser comment on a local web app preview](/images/codex/app/in-app-browser-dark.webp) 

  ![Codex app showing a browser comment on a local web app preview](/images/codex/app/in-app-browser-light.webp) ![Codex app showing a browser comment on a local web app preview](/images/codex/app/in-app-browser-dark.webp)

  [**Computer use**](/codex/computer-use) lets Codex operate macOS apps by seeing,
  clicking, and typing, which helps with native app testing, simulator flows,
  low-risk app settings, and GUI-only bugs.

  The feature isn’t available in the European Economic Area, the United Kingdom, or
  Switzerland at launch.

  #### Start, follow, and steer work

  [**Chats**](/codex/projects#start-without-a-project) are threads you can start
  without choosing a project folder first. They’re useful for research, writing,
  planning, analysis, source gathering, and tool-driven work that doesn’t begin in
  a codebase.

  For work that needs a later check-in,
  [**thread automations**](/codex/automations#schedule-work-from-a-task) can wake up
  the same thread on a schedule while preserving the conversation context. Use
  them to check a long-running process, watch for updates, or continue a
  follow-up loop without starting from scratch.

  [**The task sidebar**](/codex/artifacts-viewer#follow-artifact-work) makes plans, sources,
  generated artifacts, and summaries easier to follow while Codex works.
  [**Context-aware suggestions**](/codex/app/settings#context-aware-suggestions)
  can also help you pick up relevant follow-ups when you start or return to Codex.

  #### Stronger for software development

  Codex now brings more of the **pull request workflow** into the app. You can
  inspect [**GitHub pull requests**](/codex/code-review?surface=app#app-pull-request-reviews) in the
  sidebar, review comments in the diff, review changed files, then ask Codex to
  explain feedback, make changes, check them, and keep the review moving.

  #### Review richer outputs

  The [**artifact viewer**](/codex/artifacts-viewer) can preview
  generated files such as PDF files, spreadsheets, documents, and presentations in
  the sidebar before you commit or share them. [**Memories**](/codex/customization/memories),
  where available, can also carry useful context from past tasks into future
  threads, including stable preferences, project conventions, and recurring work
  patterns.

  #### Other features

  + [Remote connections](/codex/remote-connections) - We’re gradually rolling out SSH remote connections in alpha
  + Support for [multiple terminals](/codex/integrated-terminal)
  + macOS menu bar and [Windows system tray](/codex/windows/windows-app) support
  + [Multi-window support](/codex/reference/settings#keep-a-task-near-your-work)
  + [Intel Mac support](/codex/app)
  + [New plugins](/codex/plugins)
  + Improved thread and tool rendering
* 2026-04-12

  ### Codex app 26.410

  ### New features

  + Added command-menu file search, including `Cmd+P` routing into workspace file search.
  + Added rich previews in the sidebar file viewer for images, PDFs, and Markdown.
  + Added terminal tabs per thread, a selected-text Ask Codex overlay, and a Help menu feedback entry.

  ### Performance improvements and bug fixes

  + Improved review diff whitespace handling and search highlighting.
  + Fixed in-app browser address bar and external-open issues, plus several file viewer and side-panel bugs.
  + Additional performance improvements and bug fixes.
* 2026-04-10

  ### Codex app 26.409

  ### New features

  + Added Windows Store updater support.
  + Expanded pull request workflows with an activity timeline, PR-page commenting, and push choices in the push modal.
  + Added workspace file tabs in the thread side panel, drag-and-drop tab reordering, run action editing, and a logout confirmation dialog.

  ### Performance improvements and bug fixes

  + Improved pull request board performance and comment flyouts.
  + Improved update and navigation resilience, and fixed projectless visibility, unread-state, and pinned-row edge cases.
  + Additional performance improvements and bug fixes.
* 2026-04-09

  ### Codex app 26.406

  ### New features

  + Added collapsible inline review comments and inline or detached review modes.
  + Added a Git summary and Sources section in the thread side panel.
  + Added a New Quick Chat command and local video embeds in the app.

  ### Performance improvements and bug fixes

  + Preserved thread scroll position per conversation and unread state across windows.
  + Improved review refresh reliability, and fixed dictation loss, right-panel reset, and GitHub reconnect messaging.
  + Additional performance improvements and bug fixes.
* 2026-04-07

  ### Codex model availability update

  We’re updating model availability for users who sign in with ChatGPT. Starting
  April 7, the model picker no longer shows `gpt-5.2-codex`,
  `gpt-5.1-codex-mini`, `gpt-5.1-codex-max`, `gpt-5.1-codex`, `gpt-5.1`, or
  `gpt-5`. On April 14, we’ll remove those models from Codex for ChatGPT sign-in.

  Users can still choose from `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.3-codex`, and
  `gpt-5.2`. ChatGPT Pro users can also choose `gpt-5.3-codex-spark`.

  To use another API-supported model in Codex, sign in with an API key or
  configure a model provider.
* 2026-04-01

  ### Codex app 26.325, 26.331, 26.401

  ### New features

  + Added workspace settings to the app.
  + Added “Don’t ask again” handling and polish for custom MCP approval panels.
  + Added native Windows updater support, including MSIX support, plus a Windows system tray menu so Codex can stay resident after the last window closes.
  + Added app and file `@` mentions in the automation composer, surfaced subagent diff stats in the composer, and added artifact cards for generated file citations.
  + Added a Quick Chat app-menu shortcut, a review file tree open menu, early heartbeat automation affordances in threads, and image support for remote connections.

  ### Performance improvements and bug fixes

  + Fixed review panel scroll jumps and PR status actions while a conversation is still running.
  + Fixed several multi-window issues, plus `@`-mention results, duplicate project labeling, Windows `runGit` behavior, and revert, unstage, and stage-all actions.
  + Improved remote-thread and sidebar polish, Windows update recovery, unsupported-version guidance, and overall thread search speed.
  + Fixed sticky review issues such as diff hunk expansion, header overlap, archive-thread crashes, and window-zoom shell sizing.
  + Additional performance improvements and bug fixes.

## March 2026

* 2026-03-25

  ### Build and install plugins in Codex

  Codex now supports **plugins**: installable bundles that package skills, app
  integrations, and MCP server configuration for reusable workflows.

  Plugins are available in the Codex app, CLI, and IDE extensions.

  You can install curated plugins from the plugin directory, or scaffold a local
  plugin with `@plugin-creator` and test it with workspace-scoped or home-scoped
  marketplaces.

  Learn more in the [plugins documentation](/codex/plugins).

  ![](/images/codex/plugins/directory.png)

  #### Plugin structure

  Every plugin is a folder with a required `.codex-plugin/plugin.json` manifest
  and optional supporting files:

  ```
  my-plugin/
    .codex-plugin/
      plugin.json   # Required: plugin manifest
    skills/         # Optional: packaged skills
    .app.json       # Optional: app or connector mappings
    .mcp.json       # Optional: MCP server configuration
    assets/         # Optional: icons, logos, screenshots
  ```

  #### Install plugins per-user or per-repo

  You can install plugins for just yourself with
  `~/.agents/plugins/marketplace.json` and `~/.codex/plugins/`, or for everyone
  on a project with `.agents/plugins/marketplace.json` and a repo-local plugin
  directory such as `./plugins/`.

  #### Curated plugins and local development

  Codex surfaces curated public plugins in the plugin directory. Codex also ships
  with the built-in `@plugin-creator` skill to help you scaffold a plugin, add a
  local marketplace entry, and test it before sharing it with teammates.
* 2026-03-25

  ### Codex app 26.324

  ### New features

  + Redesigned the skills and plugins browse and manage pages.
  + Added per-window zoom and a clearer edited-files state in review.
  + Added automation titles and icons in the sidebar, plus bundled Raycast themes.

  ### Performance improvements and bug fixes

  + Kept loaded threads and projects visible during reconnects and made navigation feel faster.
  + Fixed archive freezes, markdown wrapping, hotkey-window regressions, and several permissions, terminal, and worktree issues.
  + Additional performance improvements and bug fixes.
* 2026-03-24

  ### Codex app 26.323

  ### New features

  + Added search for past Codex app threads, including a sidebar shortcut and keyboard shortcuts for jumping to recent threads.
  + Added a one-click option to archive all local threads in a project.
  + Synced key settings between the Codex app and the VS Code extension, and added a settings entry point in the extension.

  ### Performance improvements and bug fixes

  + Additional performance improvements and bug fixes.
* 2026-03-20

  ### Codex app 26.320

  ### New features

  + Added Floating Composer v2.
  + Added terminal shortcuts for jumping by word and line.
  + Improved plugin discovery surfaces and file-path rendering for saved images.

  ### Performance improvements and bug fixes

  + Fixed sidebar crashes when subagent turn items are missing.
  + Fixed pop-out thread routing and preserved local paths for composer image attachments.
  + Additional performance improvements and bug fixes.
* 2026-03-19

  ### Codex app 26.318, 26.319

  ### New features

  + Added skills to the `@` menu so you can insert them from the composer alongside other mentions.
  + `Cmd/Ctrl+F` now starts with your current text selection, which makes searching reviews and diffs faster, alongside broader review navigation improvements such as a refreshed file tree and percentage-based file tree resizing.
  + Added a branded loading shimmer while the app starts.

  ### Performance improvements and bug fixes

  + Improved collapsed diff summaries in review.
  + Fixed slash-command focus and composer alignment issues, and polished plugin cards and step details.
  + Additional performance improvements and bug fixes.
* 2026-03-18

  ### Codex app 26.317

  ### New features

  + You can now fork a conversation from an earlier message, not just the latest turn.
  + Added slash commands for switching models and reasoning levels, and made slash commands work in the middle of a draft prompt.
  + Added notifications for plan mode questions so it’s easier to notice when Codex needs input.

  ### Performance improvements and bug fixes

  + Fixed thread handoff and subagent navigation issues across worktrees and the VS Code extension.
  + Additional performance improvements and bug fixes.
* 2026-03-17

  ### Introducing GPT-5.4 mini in Codex

  GPT-5.4 mini is now available in Codex as a fast, efficient model for lighter
  coding tasks and subagents.

  It improves over GPT-5 mini across coding, reasoning, image understanding, and
  tool use while running more than 2x faster. In Codex, GPT-5.4 mini uses 30% as
  much of your included limits as GPT-5.4, so comparable tasks can last about
  3.3x longer before you hit those limits.

  GPT-5.4 mini is available in the Codex app, the CLI, the IDE extension, and
  Codex on the web. GPT-5.4 mini is also available in the API.

  Use GPT-5.4 mini for codebase exploration, large-file review, processing
  supporting documents, and other less reasoning-intensive subagent work. For
  more complex planning, coordination, and final judgment, start with GPT-5.4.

  To switch to GPT-5.4 mini:

  + In the CLI, start a new thread with:

    ```
    codex --model gpt-5.4-mini
    ```

    Or use `/model` during a session.
  + In the IDE extension, choose GPT-5.4 mini from the model selector in the
    composer.
  + In the Codex app, choose GPT-5.4 mini from the model selector in the
    composer.

  If you don’t see GPT-5.4 mini yet, update the CLI, IDE extension, or Codex app
  to the latest version.
* 2026-03-16

  ### Codex app 26.313

  ### New features

  + Added back and forward buttons in the header so you can move between recent screens more quickly.
  + Added an **Open in Finder**, **Open in Explorer**, or **Open in File Manager** action from thread menus to jump straight to a thread’s project folder.

  ### Performance improvements and bug fixes

  + Improved resume and thread error toasts with clearer details when something goes wrong.
  + Additional performance improvements and bug fixes.
* 2026-03-12

  ### Codex app 26.312

  ### Themes

  Change the Codex app appearance in **Settings** by choosing a base theme,
  adjusting accent, background, and foreground colors, and changing the UI and
  code fonts. You can also share your custom theme with friends.

  ![Codex app theme settings showing custom themes, color controls, and font settings](/images/codex/app/themes-side-by-side.webp) ![Codex app theme settings showing custom themes, color controls, and font settings](/images/codex/app/themes-side-by-side.webp) 

  ![Codex app theme settings showing custom themes, color controls, and font settings](/images/codex/app/themes-side-by-side.webp) ![Codex app theme settings showing custom themes, color controls, and font settings](/images/codex/app/themes-side-by-side.webp)

  ### Revamped Automations

  You can now choose whether automations run locally or on a worktree, define
  custom reasoning levels and models, and use templates to find inspiration for
  new automations.

  ![Automations settings showing local and worktree options alongside scheduling controls](/images/codex/app/codex-automations-light.webp) ![Automations settings showing local and worktree options alongside scheduling controls](/images/codex/app/codex-automations-dark.webp) 

  ![Automations settings showing local and worktree options alongside scheduling controls](/images/codex/app/codex-automations-light.webp) ![Automations settings showing local and worktree options alongside scheduling controls](/images/codex/app/codex-automations-dark.webp)

  ### Performance improvements and bug fixes

  Various bug fixes and performance improvements.
* 2026-03-11

  ### Codex app 26.311

  ### New features

  + Codex can now read the integrated terminal for the current thread, so it can check the status of a running development server or refer back to failed build output while it works with you.

  ### Performance improvements and bug fixes

  + Additional performance improvements and bug fixes.
* 2026-03-05

  ### Introducing GPT-5.4 in Codex

  GPT-5.4 is now available in Codex as OpenAI’s most capable and efficient
  frontier model for professional work.

  It combines recent advances in reasoning, coding, and agentic workflows in one
  model, and it’s the recommended choice for most Codex tasks.

  In Codex, GPT-5.4 is the first general-purpose model with native computer-use
  capabilities. GPT-5.4 in Codex includes experimental support for the 1M
  context window. It supports complex workflows across applications and
  long-horizon tasks, with stronger tool use and tool search that help agents
  find and use the right tools more efficiently.

  GPT-5.4 is available everywhere you can use Codex: the Codex app, the CLI, the
  IDE extension, and Codex Cloud on the web. GPT-5.4 is also available in the
  API.

  To switch to GPT-5.4:

  + In the CLI, start a new thread with:

    ```
    codex --model gpt-5.4
    ```

    Or use `/model` during a session.
  + In the IDE extension, choose GPT-5.4 from the model selector in the
    composer.
  + In the Codex app, choose GPT-5.4 from the model selector in the composer.

  If you don’t see GPT-5.4 yet, update the CLI, IDE extension, or Codex app to
  the latest version.
* 2026-03-05

  ### Codex app 26.305

  ### Performance improvements and bug fixes

  + Improved remote connections with clearer connection errors, better status updates, and clearer host labels in thread and settings views.
  + Fixed copy and paste shortcuts in the integrated terminal on Windows.
  + Fixed an issue where archived pinned threads could reappear in the sidebar.
  + Fixed an issue where repeated `codex://new` links could stop prefilling a new conversation when the app was already open.
  + Additional performance improvements and bug fixes.
* 2026-03-04

  ### Codex app 26.304

  #### Codex app for Windows

  ![Codex app for Windows showing a project sidebar, active thread, and review pane](/images/codex/windows/codex-windows-light.webp) ![Codex app for Windows showing a project sidebar, active thread, and review pane](/images/codex/windows/codex-windows-dark.webp) 

  ![Codex app for Windows showing a project sidebar, active thread, and review pane](/images/codex/windows/codex-windows-light.webp) ![Codex app for Windows showing a project sidebar, active thread, and review pane](/images/codex/windows/codex-windows-dark.webp)

  The Codex app is now available on Windows. The app gives you one interface
  for working across projects, running parallel agent threads, and reviewing
  results in one place.

  The Codex app runs natively on Windows using PowerShell and a native Windows
  sandbox for bounded permissions, so you can use Codex on Windows without
  moving your workflow into WSL, onto a virtual machine, or by deactivating the
  sandbox.

  The Windows app includes the same core features as the rest of the Codex app:

  + [Skills](/codex/build-skills) to discover and extend Codex
    capabilities.
  + [Automations](/codex/automations) to run work in the background.
  + [Worktrees](/codex/environments/git-worktrees) to handle independent tasks in the same
    project.

  If you prefer to develop in WSL, you can also switch the Codex agent and the
  integrated terminal to run there.

  Download it from the
  [Microsoft Store](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)
  and sign in with your ChatGPT account or an API key. For setup and
  configuration details, see [Setup](/codex/windows/windows-app#download-the-chatgpt-desktop-app), [Use WSL with the
  Codex app](/codex/windows/windows-app#windows-subsystem-for-linux-wsl), and [Customize the
  app for your development setup](/codex/windows/windows-app#customize-for-your-dev-setup).
* 2026-03-03

  ### Codex app 26.303

  ### New features

  + Added a Worktrees setting to turn automatic cleanup of Codex-managed worktrees on or off.
  + Added Handoff support for moving a thread between Local and [Worktree](/codex/environments/git-worktrees).
  + Added an explicit English option in the language menu.

  ### Performance improvements and bug fixes

  + Improved GitHub and pull request workflows.
  + Improved approval prompts and app connection sign-in flows.
  + Additional performance improvements and bug fixes.

## February 2026

* 2026-02-28

  ### Codex app 26.228

  ### Performance improvements and bug fixes

  + Fixed a regression where conversation and task views could stop updating while Codex was streaming a response.
  + Additional performance improvements and bug fixes.
* 2026-02-27

  ### Codex app 26.227

  ### New features

  + Added pull request status badges in task rows and PR buttons, including draft, open, merged, and closed states.
  + Added a Worktrees setting to choose how many Codex-managed worktrees to keep before older ones are cleaned up.

  ### Performance improvements and bug fixes

  + Improved scrolling and navigation in long conversations and code review, including fixes for thread jumpiness, sidebar jitter, and diff scrolling.
  + Improved app startup reliability and keyboard zoom behavior.
  + Additional performance improvements and bug fixes.
* 2026-02-26

  ### Codex app 26.226

  ### New features

  + Added new MCP shortcuts in the composer, including install keyword suggestions and an MCP server submenu in **Add context**.
  + Added support for `@mentions` and skill mentions in inline review comments.

  ### Performance improvements and bug fixes

  + Improved rendering of MCP tool calls and Mermaid diagram error handling.
  + Fixed an issue where stopped terminal commands could continue appearing as running.
  + Additional performance improvements and bug fixes.
* 2026-02-17

  ### Codex app 26.217

  ### New features

  + Added drag-and-drop support to reorder queued messages.
  + Added a warning when the selected model is downgraded.

  ### Improvements and bug fixes

  + Improved file workflows with fuzzy file search and better attachment recovery after restart.
  + Additional performance improvements and bug fixes.
* 2026-02-12

  ### Introducing GPT-5.3-Codex-Spark

  [Today, we’re releasing a research preview of GPT-5.3-Codex-Spark](https://openai.com/index/introducing-gpt-5-3-codex-spark/),
  a smaller version of GPT-5.3-Codex and our first model designed for real-time
  coding. Codex-Spark is optimized to feel near-instant, delivering more than 1000 tokens per second while remaining highly capable for real-world coding tasks.

  Codex-Spark is available in research preview for ChatGPT Pro users in
  the latest Codex app, CLI, and IDE extension. This release also marks the first
  milestone in our partnership with Cerebras.

  At launch, Codex-Spark is text-only with a 128k context window. During
  the research preview, usage has separate model-specific limits and doesn’t
  count against standard Codex limits. During high demand, access may slow down
  or queue while we balance reliability across users.

  To switch to GPT-5.3-Codex-Spark:

  + In the CLI, start a new thread with:

    ```
    codex --model gpt-5.3-codex-spark
    ```

    Or use `/model` during a session.
  + In the IDE extension, choose GPT-5.3-Codex-Spark from the model selector in
    the composer.
  + In the Codex app, choose GPT-5.3-Codex-Spark from the model selector in the
    composer.

  If you don’t see GPT-5.3-Codex-Spark yet, update the CLI, IDE extension, or
  Codex app to the latest version.

  GPT-5.3-Codex-Spark isn’t available in the API at launch.
  For API-key workflows, continue using `gpt-5.2-codex`.
* 2026-02-12

  ### Codex app 26.212

  ### New features

  + Support for GPT-5.3-Codex-Spark
  + Added conversation forking
  + Added [floating pop-out window](/codex/reference/settings#keep-a-task-near-your-work) to take a conversation with you

  ### Bug fixes

  + Improved performance and bug fixes

  Alpha testing for the Codex app on Windows is also starting. [Sign up here](https://openai.com/form/codex-app/) to be a potential alpha tester.
* 2026-02-10

  ### Codex app 26.210

  ### New features

  + Added branch search in the branch picker.
  + Added clearer guidance for entering plan mode when you type `plan` in the composer.
  + Added support for parallel approvals.

  ### Improvements and bug fixes

  + Additional performance improvements and bug fixes.
* 2026-02-09

  ### GPT-5.3-Codex in Cursor and VS Code

  Starting today, GPT-5.3-Codex is available natively in Cursor and VS Code.

  API access is starting with a small set of customers as part of a phased
  release.

  This is the first model treated as a high security capability under the
  Preparedness Framework.

  Safety controls will continue to scale, and API access will expand over the
  next few weeks.
* 2026-02-08

  ### Codex app 26.208

  ### New features

  + Added MCP and personality actions to the command palette.
  + Updated follow-up behavior to queue by default.

  ### Improvements and bug fixes

  + Additional performance improvements and bug fixes.
* 2026-02-06

  ### Codex app 26.206

  ### New features

  + Added a file-reference action to reveal files directly in your OS file manager.

  ### Improvements and bug fixes

  + Improved handling of large reviews by removing the overall diff-size cap in the review pane.
  + Additional performance improvements and bug fixes.
* 2026-02-05

  ### Introducing GPT-5.3-Codex

  [Today we’re releasing GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/),
  the most capable agentic coding model to date for complex, real-world software
  engineering.

  GPT-5.3-Codex combines the frontier coding performance of GPT-5.2-Codex with
  stronger reasoning and professional knowledge capabilities, and runs 25% faster
  for Codex users. It’s also better at collaboration while the agent is
  working—delivering more frequent progress updates and responding to steering in
  real time.

  GPT-5.3-Codex is available with paid ChatGPT plans everywhere you can use
  Codex: the Codex app, the CLI, the IDE extension, and Codex Cloud on the web.
  API access for the model will come soon.

  To switch to GPT-5.3-Codex:

  + In the CLI, start a new thread with:

    ```
    codex --model gpt-5.3-codex
    ```

    Or use `/model` during a session.
  + In the IDE extension, make sure you are signed in with ChatGPT, then choose
    GPT-5.3-Codex from the model selector in the composer.
  + In the Codex app, make sure you are signed in with ChatGPT, then choose
    GPT-5.3-Codex from the model selector in the composer.
  + If you don’t see GPT-5.3-Codex, update the CLI, IDE extension, or Codex app
    to the latest version.

  For API-key workflows, continue using `gpt-5.2-codex` while API support rolls
  out.
* 2026-02-05

  ### Codex app 26.205

  ### New features

  + Support for **[GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/)**.
  + Added mid-turn steering. Submit a message while Codex is working to direct its behavior.
  + Attach or drop any file type.

  ### Bug fixes

  + Fix flickering of the app.
* 2026-02-04

  ### Codex app 26.204

  ### New features

  + Added **Zed** and **Textmate** as options to open files and folders.
  + Added PDF preview in the review panel.

  ### Bug fixes

  + Performance improvements.
* 2026-02-03

  ### Codex app 26.203

  ### New features

  + Added thread renaming on double-click in the thread list.

  ### Improvements and bug fixes

  + Renamed **Sync** to **Handoff** and added clearer source/destination stats in the handoff UI.
  + Additional performance improvements and bug fixes.
* 2026-02-02

  ### Introducing the Codex app

  #### Codex app

  ![Codex app showing a project sidebar, thread list, and review pane](/images/codex/app/codex-app-basic-light.webp) ![Codex app showing a project sidebar, thread list, and review pane](/images/codex/app/codex-app-basic-dark.webp) 

  ![Codex app showing a project sidebar, thread list, and review pane](/images/codex/app/codex-app-basic-light.webp) ![Codex app showing a project sidebar, thread list, and review pane](/images/codex/app/codex-app-basic-dark.webp)

  The Codex app for macOS is a desktop interface for running agent threads in parallel and collaborating with agents on long-running tasks. It includes a project sidebar, thread list, and review pane for tracking work across projects.

  Key features:

  + [Multitask across projects](/codex/projects)
  + [Built-in worktree support](/codex/environments/git-worktrees)
  + [Voice dictation](/codex/prompting#use-voice-dictation)
  + [Built-in Git tooling](/codex/environments/local-environment#use-built-in-git-tools)
  + [Skills](/codex/build-skills)
  + [Automations](/codex/automations)

  For a limited time, **ChatGPT Free and Go include Codex**, and **Plus, Pro, Business, Enterprise, and Edu** plans get **double rate limits**. Those higher limits apply in the app, the CLI, your IDE, and the cloud.

  Learn more in the [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/) blog post.

  Check out the [Codex app documentation](/codex/app) for more.

  [Get started with the Codex app](https://persistent.oaistatic.com/codex-app-prod/Codex.dmg)

## January 2026

* 2026-01-28

  ### Web search is now enabled by default

  Codex now enables web search for local tasks in the Codex CLI and IDE Extension.
  By default, Codex uses a web search cache, which is an OpenAI-maintained index of web results. Cached mode returns pre-indexed results instead of fetching live pages, while live mode fetches the most recent data from the web. If you are using `--yolo` or another [full access sandbox setting](/codex/agent-approvals-security), web search defaults to live results. To disable this behavior or switch modes, use the `web_search` configuration option:

  + `web_search = "cached"` (default; serves results from the web search cache)
  + `web_search = "live"` (fetches the most recent data from the web; same as `--search`)
  + `web_search = "disabled"` to remove the tool

  To learn more, check out the [configuration documentation](/codex/config-file/config-basic).
* 2026-01-23

  ### Team Config for shared configuration

  Team Config groups the files teams use to standardize Codex across repositories and machines. Use it to share:

  + `config.toml` defaults
  + `rules/` for command controls outside the sandbox
  + `skills/` for reusable workflows

  Codex loads these layers from `.codex/` folders in the current working directory, parent folders, and the repo root, plus user (`~/.codex/`) and system (`/etc/codex/`) locations. Higher-precedence locations override lower-precedence ones.

  Admins can still enforce constraints with `requirements.toml`, which overrides defaults regardless of location.

  Learn more in [Team Config](/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config).
* 2026-01-22

  ### Custom prompts deprecated

  Custom prompts are now deprecated. Use [skills](/codex/build-skills) for reusable instructions and workflows instead.
* 2026-01-14

  ### GPT-5.2-Codex API availability

  GPT-5.2-Codex is now available in the API and for users who sign into Codex with the API.

  To learn more about using GPT-5.2-Codex check out our [API documentation](https://platform.openai.com/docs/models/gpt-5.2-codex).

## December 2025

* 2025-12-19

  ### Agent skills in Codex

  Codex now supports **agent skills**: reusable bundles of instructions (plus optional scripts and resources) that help Codex reliably complete specific tasks.

  Skills are available in both the Codex CLI and IDE extensions.

  You can invoke a skill explicitly by typing `$skill-name` (for example, `$skill-installer` or the experimental `$create-plan` skill after installing it), or let Codex select a skill automatically based on your prompt.

  Learn more in the [skills documentation](/codex/build-skills).

  ![](/images/codex/skills/skills-selector-cli-light.webp)![](/images/codex/skills/skills-selector-cli-dark.webp)

  ![](/images/codex/skills/skills-selector-ide-light.webp)![](/images/codex/skills/skills-selector-ide-dark.webp)

  #### Folder-based standard (agentskills.io)

  Following the open [agent skills specification](https://agentskills.io/specification), a skill is a folder with a required `SKILL.md` and optional supporting files:

  ```
  my-skill/
    SKILL.md       # Required: instructions + metadata
    scripts/       # Optional: executable code
    references/    # Optional: documentation
    assets/        # Optional: templates, resources
  ```

  #### Install skills per-user or per-repo

  You can install skills for just yourself in `~/.codex/skills`, or for everyone on a project by checking them into `.codex/skills` in the repository.

  Codex also ships with a few built-in system skills to get started, including `$skill-creator` and `$skill-installer`. The `$create-plan` skill is experimental and needs to be installed (for example: `$skill-installer install the create-plan skill from the .experimental folder`).

  #### Curated skills directory

  Codex ships with a [small curated set of skills](https://github.com/openai/skills) inspired by popular workflows at OpenAI. Install them with `$skill-installer`, and expect more over time.
* 2025-12-18

  ### Introducing GPT-5.2-Codex

  [Today we are releasing GPT-5.2-Codex](https://openai.com/index/gpt-5-2-codex), the most advanced agentic coding model yet for complex, real-world software engineering.

  GPT-5.2-Codex is a version of [GPT-5.2](https://openai.com/index/introducing-gpt-5-2/) further optimized for agentic coding in Codex, including improvements on long-horizon work through context compaction, stronger performance on large code changes like refactors and migrations, improved performance in Windows environments, and significantly stronger cybersecurity capabilities.

  Starting today, the CLI and IDE Extension will default to `gpt-5.2-codex` for users who are signed in with ChatGPT. API access for the model will come soon.

  If you have a model specified in your [`config.toml` configuration file](/codex/local-config), you can instead try out `gpt-5.2-codex` for a new Codex CLI session using:

  ```
  codex --model gpt-5.2-codex
  ```

  You can also use the `/model` slash command in the CLI. In the Codex IDE Extension you can select GPT-5.2-Codex from the dropdown menu.

  If you want to switch for all sessions, you can change your default model to `gpt-5.2-codex` by updating your `config.toml` [configuration file](/codex/local-config):

  ```
  model = "gpt-5.2-codex”
  ```
* 2025-12-04

  ### Introducing Codex for Linear

  Assign or mention @Codex in an issue to kick-off a Codex cloud task. As Codex works, it posts updates back to Linear, providing a link to the completed task so you can review, open a PR, or keep working.

  ![Screenshot of a successful Codex task started in Linear](/images/codex/integrations/linear-codex-example.png)

  To learn more about how to connect Codex to Linear both locally through MCP and through the new integration, check out the [Codex for Linear documentation](/codex/third-party/linear).

## November 2025

* 2025-11-24

  ### Usage and credits fixes

  Minor updates to address a few issues with Codex usage and credits:

  + Adjusted all usage dashboards to show “limits remaining” for consistency. The CLI previously displayed “limits used.”
  + Fixed an issue preventing users from buying credits if their ChatGPT subscription was purchased via iOS or Google Play.
  + Fixed an issue where the CLI could display stale usage information; it now refreshes without needing to send a message first.
  + Optimized the backend to help smooth out usage throughout the day, irrespective of overall Codex load or how traffic is routed. Before, users could get unlucky and hit a few cache misses in a row, leading to much less usage.
* 2025-11-18

  ### Introducing GPT-5.1-Codex-Max

  [Today we are releasing GPT-5.1-Codex-Max](https://openai.com/index/gpt-5-1-codex-max), our new frontier agentic coding model.

  GPT‑5.1-Codex-Max is built on an update to our foundational reasoning model, which is trained on agentic tasks across software engineering, math, research, and more. GPT‑5.1-Codex-Max is faster, more intelligent, and more token-efficient at every stage of the development cycle–and a new step towards becoming a reliable coding partner.

  Starting today, the CLI and IDE Extension will default to `gpt-5.1-codex-max` for users that are signed in with ChatGPT. API access for the model will come soon.

  For non-latency-sensitive tasks, we’ve also added a new Extra High (`xhigh`) reasoning effort, which lets the model think for an even longer period of time for a better answer. We still recommend medium as your daily driver for most tasks.

  If you have a model specified in your [`config.toml` configuration file](/codex/local-config), you can instead try out `gpt-5.1-codex-max` for a new Codex CLI session using:

  ```
  codex --model gpt-5.1-codex-max
  ```

  You can also use the `/model` slash command in the CLI. In the Codex IDE Extension you can select GPT-5.1-Codex from the dropdown menu.

  If you want to switch for all sessions, you can change your default model to `gpt-5.1-codex-max` by updating your `config.toml` [configuration file](/codex/local-config):

  ```
  model = "gpt-5.1-codex-max”
  ```
* 2025-11-13

  ### Introducing GPT-5.1-Codex and GPT-5.1-Codex-Mini

  Along with the [GPT-5.1 launch in the API](https://openai.com/index/gpt-5-1-for-developers/), we are introducing new `gpt-5.1-codex-mini` and `gpt-5.1-codex` model options in Codex, a version of GPT-5.1 optimized for long-running, agentic coding tasks and use in coding agent harnesses in Codex or Codex-like harnesses.

  Starting today, the CLI and IDE Extension will default to `gpt-5.1-codex` on macOS and Linux and `gpt-5.1` on Windows.

  If you have a model specified in your [`config.toml` configuration file](/codex/local-config), you can instead try out `gpt-5.1-codex` for a new Codex CLI session using:

  ```
  codex --model gpt-5.1-codex
  ```

  You can also use the `/model` slash command in the CLI. In the Codex IDE Extension you can select GPT-5.1-Codex from the dropdown menu.

  If you want to switch for all sessions, you can change your default model to `gpt-5.1-codex` by updating your `config.toml` [configuration file](/codex/local-config):

  ```
  model = "gpt-5.1-codex”
  ```
* 2025-11-07

  ### Introducing GPT-5-Codex-Mini

  Today we are introducing a new `gpt-5-codex-mini` model option to Codex CLI and the IDE Extension. The model is a smaller, more cost-effective, but less capable version of `gpt-5-codex` that provides approximately 4x more usage as part of your ChatGPT subscription.

  Starting today, the CLI and IDE Extension will automatically suggest switching to `gpt-5-codex-mini` when you reach 90% of your 5-hour usage limit, to help you work longer without interruptions.

  You can try the model for a new Codex CLI session using:

  ```
  codex --model gpt-5-codex-mini
  ```

  You can also use the `/model` slash command in the CLI. In the Codex IDE Extension you can select GPT-5-Codex-Mini from the dropdown menu.

  Alternatively, you can change your default model to `gpt-5-codex-mini` by updating your `config.toml` [configuration file](/codex/local-config):

  ```
  model = "gpt-5-codex-mini”
  ```
* 2025-11-06

  ### GPT-5-Codex model update

  We’ve shipped a minor update to GPT-5-Codex:

  + More reliable file edits with `apply_patch`.
  + Fewer destructive actions such as `git reset`.
  + More collaborative behavior when encountering user edits in files.
  + 3% more efficient in time and usage.

## October 2025

* 2025-10-30

  ### Credits on ChatGPT Pro and Plus

  Codex users on ChatGPT Plus and Pro can now use on-demand credits for more Codex usage beyond what’s included in your plan. [Learn more.](/codex/pricing)
* 2025-10-22

  ### Tag @Codex on GitHub Issues and PRs

  You can now tag `@codex` on a teammate’s pull request to ask clarifying questions, request a follow-up, or ask Codex to make changes. GitHub Issues now also support `@codex` mentions, so you can kick off tasks from any issue, without leaving your workflow.

  ![Codex responding to a GitHub pull request and issue after an @Codex mention.](/images/codex/integrations/github-example.png)
* 2025-10-06

  ### Codex is now GA

  Codex is now generally available with 3 new features — @Codex in Slack, Codex SDK, and new admin tools.

  #### @Codex in Slack

  ![](/images/codex/integrations/slack-example.png)

  You can now questions and assign tasks to Codex directly from Slack. See the [Slack guide](/codex/third-party/slack) to get started.

  #### Codex SDK

  Integrate the same agent that powers the Codex CLI inside your own tools and workflows with the Codex SDK in Typescript. With the new Codex GitHub Action, you can easily add Codex to CI/CD workflows. See the [Codex SDK guide](/codex/codex-sdk) to get started.

  ```
  import { Codex } from "@openai/codex-sdk";

  const agent = new Codex();
  const thread = await agent.startThread();

  const result = await thread.run("Explore this repo");
  console.log(result);

  const result2 = await thread.run("Propose changes");
  console.log(result2);
  ```

  #### New admin controls and analytics

  ![](/images/codex/enterprise/analytics.png)

  ChatGPT workspace admins can now edit or delete Codex Cloud environments. With managed config files, they can set safe defaults for CLI and IDE usage and monitor how Codex uses commands locally. New analytics dashboards help you track Codex usage and code review feedback. Learn more in the [enterprise admin guide.](/codex/enterprise/admin-setup)

  #### Availability and pricing updates

  The Slack integration and Codex SDK are available to developers on ChatGPT Plus, Pro, Business, Edu, and Enterprise plans starting today, while the new admin features will be available to Business, Edu, and Enterprise.
  Beginning October 20, Codex Cloud tasks will count toward your Codex usage. Review the [Codex pricing guide](/codex/pricing) for plan-specific details.

## September 2025

* 2025-09-23

  ### GPT-5-Codex in the API

  GPT-5-Codex is now available in the Responses API, and you can also use it with your API Key in the Codex CLI.
  We plan on regularly updating this model snapshot.
  It is available at the same price as GPT-5. You can learn more about pricing and rate limits for this model on our [model page](https://platform.openai.com/docs/models/gpt-5-codex).
* 2025-09-15

  ### Introducing GPT-5-Codex

  #### New model: GPT-5-Codex

  ![codex-switch-model](https://cdn.openai.com/devhub/docs/codex-switch-model.png)

  GPT-5-Codex is a version of GPT-5 further optimized for agentic coding in Codex.
  It’s available in the IDE extension and CLI when you sign in with your ChatGPT account.
  It also powers the cloud agent and Code Review in GitHub.

  To learn more about GPT-5-Codex and how it performs compared to GPT-5 on software engineering tasks, see our [announcement blog post](https://openai.com/index/introducing-upgrades-to-codex/).

  #### Image outputs

  ![codex-image-outputs](https://cdn.openai.com/devhub/docs/codex-image-output.png)

  When working in the cloud on front-end engineering tasks, GPT-5-Codex can now display screenshots of the UI in Codex web for you to review. With image output, you can iterate on the design without needing to check out the branch locally.

  #### New in Codex CLI

  + You can now resume sessions where you left off with `codex resume`.
  + Context compaction automatically summarizes the session as it approaches the context window limit.

  Learn more in the [latest release notes](https://github.com/openai/codex/releases/tag/rust-v0.36.0)

## August 2025

* 2025-08-27

  ### Late August update

  #### IDE extension (Compatible with VS Code, Cursor, Windsurf)

  ![](/images/codex/changelog/local_task.gif)

  Codex now runs in your IDE with an interactive UI for fast local iteration. Easily switch between modes and reasoning efforts.

  #### Sign in with ChatGPT (IDE & CLI)

  ![](/images/codex/changelog/sign-in-with-chat.gif)

  One-click authentication that removes API keys and uses ChatGPT Enterprise credits.

  #### Move work between local ↔ cloud

  ![](/images/codex/changelog/cloud_task.gif)

  Hand off tasks to Codex web from the IDE with the ability to apply changes locally so you can delegate jobs without leaving your editor.

  #### Code Reviews

  ![](/images/codex/changelog/codex_review.gif)

  Codex goes beyond static analysis. It checks a PR against its intent, reasons across the codebase and dependencies, and can run code to validate the behavior of changes.
* 2025-08-21

  ### Mid August update

  #### Image inputs

  ![](/images/codex/changelog/image_input.png)

  You can now attach images to your prompts in Codex web. This is great for asking Codex to implement frontend changes or follow up on whiteboarding sessions.

  #### Container caching

  ![](/images/codex/changelog/container_caching.png)

  Codex now caches containers to start new tasks and followups 90% faster, dropping the median start time from 48 seconds to 5 seconds. You can optionally configure a maintenance script to update the environment from its cached state to prepare for new tasks. See the docs for more.

  #### Automatic environment setup

  Now, environments without manual setup scripts automatically run the standard installation commands for common package managers like yarn, pnpm, npm, go mod, gradle, pip, poetry, uv, and cargo. This reduces test failures for new environments by 40%.

## June 2025

* 2025-06-13

  ### Best of N

  ![](/images/codex/changelog/best-of-n.png)

  Codex can now generate multiple responses simultaneously for a single task, helping you quickly explore possible solutions to pick the best approach.

  #### Fixes & improvements

  + Added some keyboard shortcuts and a page to explore them. Open it by pressing ⌘-/ on macOS and Ctrl+/ on other platforms.
  + Added a “branch” query parameter in addition to the existing “environment”, “prompt” and “tab=archived” parameters.
  + Added a loading indicator when downloading a repo during container setup.
  + Added support for cancelling tasks.
  + Fixed issues causing tasks to fail during setup.
  + Fixed issues running followups in environments where the setup script changes files that are gitignored.
  + Improved how the agent understands and reacts to network access restrictions.
  + Increased the update rate of text describing what Codex is doing.
  + Increased the limit for setup script duration to 20 minutes for Pro and Business users.
  + Polished code diffs: You can now option-click a code diff header to expand/collapse all of them.
* 2025-06-03

  ### June update

  #### Agent internet access

  ![](/images/codex/changelog/internet_access.png)

  Now you can give Codex access to the internet during task execution to install dependencies, upgrade packages, run tests that need external resources, and more.

  Internet access is off by default. Plus, Pro, and Business users can enable it for specific environments, with granular control of which domains and HTTP methods Codex can access. Internet access for Enterprise users is coming soon.

  Learn more about usage and risks in the [docs](/codex/cloud/agent-internet).

  #### Update existing PRs

  ![](/images/codex/changelog/update_prs.png)

  Now you can update existing pull requests when following up on a task.

  #### Voice dictation

  ![](/images/codex/changelog/voice_dictation.gif)

  Now you can dictate tasks to Codex.

  #### Fixes & improvements

  + Added a link to this changelog from the profile menu.
  + Added support for binary files: When applying patches, all file operations are supported. When using PRs, only deleting or renaming binary files is supported for now.
  + Fixed an issue on iOS where follow up tasks where shown duplicated in the task list.
  + Fixed an issue on iOS where pull request statuses were out of date.
  + Fixed an issue with follow ups where the environments were incorrectly started with the state from the first turn, rather than the most recent state.
  + Fixed internationalization of task events and logs.
  + Improved error messages for setup scripts.
  + Increased the limit on task diffs from 1 MB to 5 MB.
  + Increased the limit for setup script duration from 5 to 10 minutes.
  + Polished GitHub connection flow.
  + Re-enabled Live Activities on iOS after resolving an issue with missed notifications.
  + Removed the mandatory two-factor authentication requirement for users using SSO or social logins.

## May 2025

* 2025-05-22

  ### Reworked environment page

  It’s now easier and faster to set up code execution.

  ![](/images/codex/changelog/environment_setup.png)

  #### Fixes & improvements

  + Added a button to retry failed tasks
  + Added indicators to show that the agent runs without network access after setup
  + Added options to copy git patches after pushing a PR
  + Added support for unicode branch names
  + Fixed a bug where secrets were not piped to the setup script
  + Fixed creating branches when there’s a branch name conflict.
  + Fixed rendering diffs with multi-character emojis.
  + Improved error messages when starting tasks, running setup scripts, pushing PRs, or disconnected from GitHub to be more specific and indicate how to resolve the error.
  + Improved onboarding for teams.
  + Polished how new tasks look while loading.
  + Polished the followup composer.
  + Reduced GitHub disconnects by 90%.
  + Reduced PR creation latency by 35%.
  + Reduced tool call latency by 50%.
  + Reduced task completion latency by 20%.
  + Started setting page titles to task names so Codex tabs are easier to tell apart.
  + Tweaked the system prompt so that agent knows it’s working without network, and can suggest that the user set up dependencies.
  + Updated the docs.
* 2025-05-19

  ### Codex in the ChatGPT iOS app

  Start tasks, view diffs, and push PRs—while you’re away from your desk.

  ![](/images/codex/changelog/mobile_support.png)
