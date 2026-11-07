<!-- source: https://help.openai.com/en/articles/20001607-using-daybreak-in-codex-cli -->

# Using Daybreak in Codex CLI

Use this guide to enable Daybreak in Codex CLI, configure it for automated workflows and SDK integrations, and troubleshoot access or refusal issues.

Updated: 10 days ago

Note that to access these changes, you’ll need to upgrade to Codex CLI 0.163.0 or later. CLI upgrades are opt-in: existing installations retain their current behavior until you update them.

* If your automation installs `@openai/codex@latest`, it can pick up this change on its next install or update. If you installed Codex CLI globally with npm, run `npm install -g @openai/codex@latest`, then run `codex --version` to confirm the upgrade.
* To defer the change, pin `@openai/codex@0.162.0`. A one-time installation using `@latest` does not update itself. Workflows pinned to older versions retain their previous behavior.
* For TypeScript integrations, update `@openai/codex-sdk` and its bundled runtime. For Python integrations, update `openai-codex` and its Codex runtime. Updating the global CLI alone may not update an SDK's runtime. If you configure a custom executable path, update that executable too.

Manually configured model IDs absent from an otherwise available catalog will retain their previous automatic treatment in CLI and Codex Desktop, even when Daybreak is ON. Their absence from the catalog alone does not prevent a request from succeeding.

Cyber model availability in the model picker may roll out separately. Once enabled, users already on a supported release do not need another download to see the newly available models. Reopen the model picker or restart Codex to refresh the list.

# Enable Daybreak in interactive CLI

1. Start Codex with your usual authentication.
2. To turn Daybreak ON, enter `/daybreak`.
3. Codex will report `Daybreak on. Applies to new turns.`
4. This will apply to the active thread and be saved as the default for new sessions.
5. To turn Daybreak OFF, run the same command (`/daybreak`) again.

# Enable Daybreak in headless CLI

Headless workflows run without an interactive UI, commonly through `codex exec` in scripts, scheduled jobs, or CI. There is no interactive “Enable Daybreak” (`/daybreak`) prompt here. Instead, you can:

1. **Add Daybreak to a specific CLI run** by adding `-c daybreak=true` to each command that should use reduced refusals. As an example, you might enter:

`codex exec -c daybreak=true "Review the changes in this repository."`

1. Keep your existing prompt and other command options. Add this setting to each invocation that should use Daybreak, including commands in scripts, scheduled jobs, and CI configuration.
2. **Make Daybreak the default for new CLI sessions and runs** by adding `daybreak=true` to the configuration file loaded by Codex.
3. The default user configuration is `~/.codex/config.toml`. If your automation sets `CODEX_HOME`, use `$CODEX_HOME/config.toml` instead. Place the setting at the top level, outside sections such as `[features]`.
4. Make the change in the environment where the automation actually runs. Updating your laptop's configuration does not update a CI runner or remote machine.
5. The setting also applies to new interactive sessions that use the same configuration. Resumed and forked sessions retain their saved Daybreak choice; a new configuration default does not replace it.
6. Note that a command-line setting overrides the saved configuration for that invocation. You can therefore keep `daybreak = true` in your configuration and use `-c daybreak=false` for an individual run.

# Enable Daybreak via TypeScript SDK

Pass the Daybreak setting through the client configuration:

> `import { Codex } from "@openai/codex-sdk";`
>
> `const codex = new Codex({`
>
> `config: { daybreak: true },`
>
> `});`
>
> `const thread = codex.startThread();`
>
> `const result = await thread.run("Review the changes in this repository.");`
>
> `console.log(result.finalResponse);`

Use `daybreak: false` to turn Daybreak off and use the normal refusal behavior. Keep your existing authentication configuration.

# Enable Daybreak via the app server or Python SDK

1. Read the selected model’s `availableAccessPrograms.cyber` values from `model/list`, then set `cyberAccessProgram` in the `turn/start` parameters.

a. For a mainline model and account with Daybreak Blue access:

`{ "cyberAccessProgram": "daybreakBlue" }`

b. For a cyber model and account with Daybreak Red access:

`{ "cyberAccessProgram": "daybreakRed" }`

c. For normal refusal behavior:

`{ "cyberAccessProgram": "standard" }`

2. Include the selection on every turn that should use it; do not assume that omitting the parameter turns Daybreak off. Direct app-server clients must enable the `experimentalApi` capability during initialization to use this parameter.

3. The Python SDK's low-level CodexClient can pass the same parameter:

> `from openai_codex.client import CodexClient`
>
> `with CodexClient() as client:`
>
> `client.initialize()`
>
> `thread = client.thread_start()`
>
> `turn = client.turn_start(`
>
> `thread.thread.id,`
>
> `"Review the changes in this repository.",`
>
> `params={"cyberAccessProgram": "daybreakBlue"},`
>
> `)`
>
> `client.wait_for_turn_completed(turn.turn.id)`

4. This example assumes Daybreak Blue is available for the selected model. The Python client enables the experimental API capability by default. A saved thread preference alone does not select a program for an app-server turn.

# If you added a local model catalog prior to these changes

If signing in with an API key previously didn’t show the models you expected, you may have added a local catalog using `model_catalog_json` in `config.toml`. Codex uses that local file instead of the automatic catalog, so your model list can become outdated. Once automatic catalog support is available for your environment, follow these steps to switch back:

1. Open `config.toml`. For Codex CLI, open `~/.codex/config.toml` (or `$CODEX_HOME/config.toml` if you set `CODEX_HOME`). In Codex Desktop, go to **Settings > Configuration**, then select **Open config.toml**.
2. Temporarily disable the local catalog. Add # at the beginning of the `model_catalog_json` line, save the file, and restart Codex with the same account or API key. Leave any catalog URL your organization requires in place.
3. Verify your access. In CLI, start `codex`, then enter `/daybreak` inside the session. In Desktop, open the Advanced model picker and turn on Daybreak. If you have Daybreak Red access, confirm that an expected cyber model appears and that you can send a request using it.
4. Keep the working configuration. If the check succeeds, delete the line you disabled and save the file. If it fails, remove the `#`, save, and restart Codex to restore your previous setup.

# Troubleshoot refusals in CLI

* Run a representative job with the same credentials, model, and configuration used by your automation.
* If Daybreak is unavailable, confirm that:

  + Your account or API project has Daybreak access.
  + The selected model supports Daybreak.
* In interactive CLI, check that Daybreak is On. Interactive CLI can show a refusal message when Daybreak is available but OFF: `Daybreak is currently off. If you’re doing authorized security work, turn it on and try your request again.`

  + The prompt asks `Turn on Daybreak for your next request?` and offers `Enable Daybreak` or `Not now`.
  + Select **Enable Daybreak** to turn it on for your next request, then try the request again. Note that the refused request is not retried automatically; you must request again. Some requests may still be refused with Daybreak ON.
  + Select **Not now** to leave Daybreak OFF.
* For automations, confirm that `daybreak=true` reaches the actual Codex process and is not overridden by another command-line setting.
