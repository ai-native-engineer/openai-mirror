<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/create/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

# Create an agent session

POST/agents/sessions

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

##### Body ParametersJSONExpand Collapse

environment: [EnvironmentParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20environment_param%20%3E%20(schema))

An inline execution environment or a reference to an environment template.

None object { type }

Runs the agent without an execution environment.

type: "none"

The type of the object. Always `none`.

OpenAIHosted object { type, capability\_directories, env, 7 more }

An OpenAI-hosted environment, optionally based on a reusable template.

type: "openai\_hosted"

The type of the object. Always `openai_hosted`.

capability\_directories: optional array of string or null

Directories that contain capabilities exposed to the agent. Defaults to an empty list.

env: optional map[string] or null

Environment variables made available to the agent.

environment\_template\_id: optional string

A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

maxLength64

files: optional array of [HostedEnvironmentFileParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_environment_file_param%20%3E%20(schema)) or null

Files available before the agent starts. Defaults to an empty list.

FileID object { file\_id, path, type }

A file previously uploaded through the OpenAI Files API.

file\_id: string

The ID of the uploaded file.

minLength1

maxLength256

path: string

The absolute destination path inside `/workspace`.

minLength1

maxLength4096

type: "file\_id"

The type of the object. Always `file_id`.

Inline object { data, path, type }

A file supplied directly as standard-base64 data.

data: string

The standard-base64-encoded file contents.

maxLength6990508

path: string

The absolute destination path inside `/workspace`.

minLength1

maxLength4096

type: "inline"

The type of the object. Always `inline`.

network: optional object { access, allowed\_domains }  or null

Network access for an OpenAI-hosted environment.

access: "enabled" or "disabled" or "restricted"

The environment’s network access mode.

"enabled"

Allows unrestricted network access, matching an omitted network policy.

"disabled"

Disables network access.

"restricted"

Allows access only to configured domains.

allowed\_domains: optional array of string or null

Domains the environment may access when network access is restricted.

packages: optional object { npm, python, system }  or null

Packages to install in an OpenAI-hosted environment.

npm: optional array of string or null

npm packages to install globally. Defaults to an empty list.

python: optional array of string or null

Python packages to install. Defaults to an empty list.

system: optional array of string or null

System packages to install. Defaults to an empty list.

plugins: optional array of [HostedPluginParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_plugin_param%20%3E%20(schema)) { description, name, source, type }  or null

Plugins provided as inline ZIP archives. Defaults to an empty list.

description: string

The plugin description declared in `.codex-plugin/plugin.json`.

The plugin name declared in `.codex-plugin/plugin.json`.

minLength1

maxLength64

source: [InlineCapabilitySourceParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20inline_capability_source_param%20%3E%20(schema)) { data, media\_type, type }

Provides ZIP bytes encoded with standard base64.

data: string

Standard-base64 encoded ZIP archive bytes.

minLength1

maxLength70254592

media\_type: "application/zip"

The archive media type, always `application/zip`.

type: "base64"

The type of the object. Always `base64`.

type: "inline"

The type of the object. Always `inline`.

setup\_commands: optional array of [SetupCommandParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20setup_command_param%20%3E%20(schema)) { command, cwd }  or null

Ordered, confidential setup commands. Command bodies are never returned.

command: string

The shell command to execute.

maxLength65536

cwd: optional string or null

The absolute working directory. Defaults to `/workspace`.

maxLength4096

skills: optional array of [HostedSkillParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_skill_param%20%3E%20(schema)) or null

Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

SkillReference object { skill\_id, type, version }

References a skill uploaded through the Skills API.

skill\_id: string

The ID of the skill created through `/v1/skills`.

minLength1

maxLength64

type: "skill\_reference"

The type of the object. Always `skill_reference`.

version: optional string or null

The skill version, a positive integer or `latest`; omission selects the default.

Inline object { description, name, source, type }

Supplies a skill ZIP directly in the session request.

description: string

The skill description declared in `SKILL.md`.

The skill name declared in `SKILL.md`.

minLength1

maxLength64

source: [InlineCapabilitySourceParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20inline_capability_source_param%20%3E%20(schema)) { data, media\_type, type }

Provides ZIP bytes encoded with standard base64.

data: string

Standard-base64 encoded ZIP archive bytes.

minLength1

maxLength70254592

media\_type: "application/zip"

The archive media type, always `application/zip`.

type: "base64"

The type of the object. Always `base64`.

type: "inline"

The type of the object. Always `inline`.

SelfHosted object { type, workspace\_directory, capability\_directories }

An application-hosted environment configured inline.

type: "self\_hosted"

The type of the object. Always `self_hosted`.

workspace\_directory: string

Absolute project directory inside the self-hosted environment.

capability\_directories: optional array of string or null

Directories that contain capabilities exposed to the agent. Defaults to an empty list.

agent: optional object { instructions, model, multi\_agent, 4 more }

Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

instructions: optional string or null

Additional instructions appended to the agent’s default base instructions. Omit to leave unchanged.

model: optional string

The model to use for the agent. The requested model name is preserved.

multi\_agent: optional [MultiAgentConfigParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20multi_agent_config_param%20%3E%20(schema)) { enabled, max\_concurrent\_subagents }  or null

Explicit configuration for creating and coordinating subagents.

enabled: boolean

Whether subagent tools are enabled.

max\_concurrent\_subagents: optional number

Maximum number of subagents that may run concurrently. Defaults to 6.

minimum1

maximum4294967295

reasoning: optional [AgentReasoningParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_reasoning_param%20%3E%20(schema)) { effort, summary }  or null

Reasoning configuration for the agent.

effort: optional "none" or "minimal" or "low" or 4 more or null

The amount of reasoning effort the model should use.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

"max"

summary: optional "concise" or "detailed" or "auto" or null

The reasoning summary format requested from the model.

"concise"

Returns a concise reasoning summary when supported.

"detailed"

Returns a detailed reasoning summary when supported.

"auto"

Automatically selects the most detailed summary supported by the model.

service\_tier: optional "auto" or "default" or "flex" or 2 more or null

The service tier used for model requests.

"auto"

Selects the service tier automatically.

"default"

Uses the default service tier.

"flex"

Uses the flex service tier.

"priority"

Uses the priority service tier.

"fast"

Uses the fast service tier.

text: optional [AgentTextParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_text_param%20%3E%20(schema)) { format, verbosity }  or null

Configuration for text generated by the agent.

format: optional [TextFormatParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20text_format_param%20%3E%20(schema)) or null

The output format for generated text.

Text object { type }

Generates ordinary text without a structured-output constraint.

type: "text"

The type of the object. Always `text`.

JSONSchema object { schema, type }

Constrains generated text to a JSON Schema.

schema: map[unknown]

The JSON Schema that generated text must match.

type: "json\_schema"

The type of the object. Always `json_schema`.

verbosity: optional "low" or "medium" or "high" or null

The amount of text the model should produce.

"low"

Produces less text.

"medium"

Uses the default amount of text.

"high"

Produces more text.

tools: optional array of [AgentToolParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_tool_param%20%3E%20(schema)) or null

Tools available to the agent. Omit to inherit, or pass null to clear them.

Function object { description, name, parameters, 2 more }

A function defined by the application.

description: string

A description of what the function does.

The name of the function.

parameters: map[unknown]

A JSON Schema object describing the function’s arguments.

type: "function"

The type of the object. Always `function`.

defer\_loading: optional boolean

Whether this function is deferred and discovered through tool search. Defaults to `false`.

ToolSearch object { type }

Discovers deferred function tools and loads them into the model context.

type: "tool\_search"

The type of the object. Always `tool_search`.

ProgrammaticToolCalling object { type, enabled }

Enables calling tools from model-generated code.

type: "programmatic\_tool\_calling"

The type of the object. Always `programmatic_tool_calling`.

enabled: optional boolean

Whether tools can be called from model-generated code. Defaults to `true`.

Mcp object { server\_label, transport, type, 5 more }

Tools provided by a remote MCP server.

server\_label: string

A label used to identify the MCP server in tool calls.

transport: [McpTransportParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20mcp_transport_param%20%3E%20(schema))

The transport used to connect to the MCP server.

HTTP object { server\_url, type, authorization, headers }

Connects to an MCP server over HTTP.

server\_url: string

The URL of the MCP server.

type: "http"

The type of the object. Always `http`.

authorization: optional string or null

The authorization value sent to the MCP server, if any.

headers: optional map[string] or null

Additional HTTP headers sent to the MCP server.

Stdio object { command, cwd, type, 3 more }

Starts an MCP server as a local process.

command: string

The command used to start the MCP server.

cwd: string

The working directory used to start the MCP server.

type: "stdio"

The type of the object. Always `stdio`.

args: optional array of string or null

Arguments passed to the MCP server command.

env: optional map[string] or null

Environment variables set for the MCP server process.

env\_vars: optional array of string or null

Environment variable names to inherit from the selected execution environment.

type: "mcp"

The type of the object. Always `mcp`.

allowed\_tools: optional array of string or null

The MCP tools the agent may call. All server tools are allowed when omitted.

connection\_origin: optional "service" or "environment" or null

Where outbound MCP HTTP connections originate.

"service"

Uses the Managed Agents service network.

"environment"

Uses the session’s execution environment.

credential\_id: optional string or null

The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

request\_metadata: optional map[unknown] or null

Metadata included with requests to this MCP server.

required: optional boolean

Whether this MCP server must initialize before the first turn. Defaults to `false`.

WebSearch object { type, allowed\_domains, context\_size, 2 more }

Web search.

type: "web\_search"

The type of the object. Always `web_search`.

allowed\_domains: optional array of string or null

Domains the search may include.

context\_size: optional "low" or "medium" or "high" or null

The amount of web search context made available to the model.

"low"

"medium"

"high"

location: optional object { city, country, region, timezone }  or null

Approximate user location used to localize web search results.

city: optional string or null

The city name.

country: optional string or null

The two-letter ISO country code, such as `US`.

region: optional string or null

The region or state name.

timezone: optional string or null

The IANA timezone, such as `America/Los_Angeles`.

mode: optional "disabled" or "cached" or "live" or null

The source used for web search results.

"disabled"

Disables web search.

"cached"

Uses cached search results.

"live"

Searches the live web.

agent\_id: optional string

The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

maxLength64

input: optional string or array of [AgentSessionInputMessageParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_session_input_message_param%20%3E%20(schema)) { content, role, type }  or null

Initial input submitted when creating a session.

string

array of [AgentSessionInputMessageParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_session_input_message_param%20%3E%20(schema)) { content, role, type }

content: array of [InputContentParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20input_content_param%20%3E%20(schema))

The content of the message.

InputText object { text, type }

Text input to the model.

text: string

The text sent to the model.

type: "input\_text"

The type of the object. Always `input_text`.

InputImage object { image\_url, type }

Image input to the model.

image\_url: string

The URL of the image sent to the model.

type: "input\_image"

The type of the object. Always `input_image`.

role: "user"

The role of the message author. Always `user`.

type: optional "message"

The type of the input item. Always `message`.

metadata: optional map[string] or null

Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

stream: optional boolean

Whether to stream session events as server-sent events. Defaults to `false`.

vault\_ids: optional array of string or null

The IDs of vaults made available to the session.

AgentSession object { id, agent, created\_at, 9 more }

A Managed Agents session.

The ID of the session.

agent: object { id, instructions, model, 6 more }

The agent running in the session.

The ID of the agent.

instructions: string or null

Custom instructions appended to the agent’s default base instructions.

model: string

The model used by the agent.

multi\_agent: [MultiAgentConfig](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20multi_agent_config%20%3E%20(schema)) { enabled, max\_concurrent\_subagents }

Configuration for creating and coordinating subagents.

enabled: boolean

Whether subagent tools are enabled. Defaults to false.

max\_concurrent\_subagents: number or null

Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

minimum1

maximum4294967295

name: string or null

The reusable agent’s name when the session was created, or null if no name was saved. Later changes to the agent’s name do not affect this value.

reasoning: [AgentReasoning](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_reasoning%20%3E%20(schema)) { effort, summary }

The agent’s reasoning configuration.

effort: "none" or "minimal" or "low" or 4 more or null

The amount of reasoning effort used by an agent.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

"max"

summary: "concise" or "detailed" or "auto" or null

The reasoning summary format requested from an agent.

"concise"

Returns a concise reasoning summary when supported.

"detailed"

Returns a detailed reasoning summary when supported.

"auto"

Automatically selects the most detailed summary supported by the model.

service\_tier: "auto" or "default" or "flex" or 2 more

The effective service-tier policy for model requests. Defaults to `auto`.

"auto"

"default"

"flex"

"priority"

"fast"

text: [AgentText](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_text%20%3E%20(schema)) { format, verbosity }

Configuration for text generated by the agent.

format: [TextFormat](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20text_format%20%3E%20(schema))

The effective output format. Defaults to ordinary text.

Text object { type }

Generates ordinary text without a structured-output constraint.

type: "text"

The type of the object. Always `text`.

JSONSchema object { schema, type }

Constrains generated text to a JSON Schema.

schema: map[unknown]

The JSON Schema that generated text must match.

type: "json\_schema"

The type of the object. Always `json_schema`.

verbosity: "low" or "medium" or "high"

The amount of text produced by the agent. Defaults to `medium`.

"low"

"medium"

"high"

tools: array of [AgentTool](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_tool%20%3E%20(schema))

Tools available to the agent.

Function object { defer\_loading, description, name, 2 more }

A function defined by the application.

defer\_loading: boolean

Whether the function is deferred and discovered through tool search.

description: string

A description of what the function does.

The name of the function.

parameters: map[unknown]

A JSON Schema object describing the function’s arguments.

type: "function"

The type of the object. Always `function`.

ProgrammaticToolCalling object { enabled, type }

Enables calling tools from model-generated code.

enabled: boolean

Whether tools can be called from model-generated code.

type: "programmatic\_tool\_calling"

The type of the object. Always `programmatic_tool_calling`.

Mcp object { allowed\_tools, connection\_origin, credential\_id, 5 more }

Tools provided by a remote MCP server.

allowed\_tools: array of string or null

The MCP tools the agent may call.

connection\_origin: "service" or "environment"

Where outbound MCP HTTP connections originate.

"service"

"environment"

credential\_id: string or null

The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

request\_metadata: map[unknown]

Metadata included with requests to this MCP server.

required: boolean

Whether this MCP server must initialize before the first turn.

server\_label: string

A label used to identify the MCP server in tool calls.

transport: [McpTransport](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20mcp_transport%20%3E%20(schema))

The transport used to connect to the MCP server.

HTTP object { server\_url, type }

Connects to an MCP server over HTTP.

server\_url: string

The URL of the MCP server.

type: "http"

The type of the object. Always `http`.

Stdio object { args, command, cwd, 2 more }

Starts an MCP server as a local process.

args: array of string

Arguments passed to the MCP server command.

command: string

The command used to start the MCP server.

cwd: string

The working directory used to start the MCP server.

env\_vars: array of string

Environment variable names inherited from the execution environment.

type: "stdio"

The type of the object. Always `stdio`.

type: "mcp"

The type of the object. Always `mcp`.

WebSearch object { allowed\_domains, context\_size, location, 2 more }

Web search.

allowed\_domains: array of string or null

Allowed search domains, or `null` when the search is unrestricted.

context\_size: "low" or "medium" or "high"

The amount of search context made available to the model. Defaults to `medium`.

"low"

"medium"

"high"

location: object { city, country, region, timezone }  or null

Approximate user location used to localize web search results.

city: string or null

The city name.

country: string or null

The two-letter ISO country code, such as `US`.

region: string or null

The region or state name.

timezone: string or null

The IANA timezone, such as `America/Los_Angeles`.

mode: "disabled" or "cached" or "live"

The source used for web search results.

"disabled"

"cached"

"live"

type: "web\_search"

The type of the object. Always `web_search`.

The Unix timestamp, in seconds, when the session was created.

environment: [Environment](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20environment%20%3E%20(schema))

The execution environment for the session.

None object { type }

The session talks to CCA without selecting or provisioning an execution environment.

type: "none"

The type of the object. Always `none`.

OpenAIHosted object { id, capability\_directories, files, 5 more }

An environment hosted by OpenAI.

The public ID of the environment.

capability\_directories: array of string

Directories that contain capabilities exposed to the agent.

files: array of [HostedEnvironmentFile](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_environment_file%20%3E%20(schema))

Files available in the environment, excluding their contents.

HostedEnvironmentFileID object { id, file\_id, path, 2 more }

A file copied from the OpenAI Files API.

The session-scoped ID of the file in the execution environment.

file\_id: string

The ID of the uploaded file.

path: string

The file’s absolute path inside the environment.

size\_bytes: number

The decoded file size in bytes.

minimum0

type: "file\_id"

The type of the object. Always `file_id`.

Inline object { id, path, size\_bytes, type }

A file supplied inline when the session was created.

The session-scoped ID of the file in the execution environment.

path: string

The file’s absolute path inside the environment.

size\_bytes: number

The decoded file size in bytes.

minimum0

type: "inline"

The type of the object. Always `inline`.

network: object { access, allowed\_domains }

The effective network access policy for the environment.

access: "enabled" or "disabled" or "restricted"

The environment’s network access mode.

"enabled"

Allows unrestricted network access.

"disabled"

Disables network access.

"restricted"

Allows access only to configured domains.

allowed\_domains: array of string

Domains the environment may access when network access is restricted.

packages: object { npm, python, system }

Packages installed in the environment.

npm: array of string

npm packages installed globally in the environment.

python: array of string

Python packages installed in the environment.

system: array of string

System packages installed in the environment.

plugins: array of [HostedPlugin](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_plugin%20%3E%20(schema)) { description, name, type }

Plugins installed in the environment, excluding their archive contents.

description: string

The installed plugin description.

The installed plugin name.

type: "inline"

The type of the object. Always `inline`.

skills: array of [HostedSkill](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20hosted_skill%20%3E%20(schema))

Skills installed in the environment, excluding their archive contents.

HostedSkillReference object { description, name, skill\_id, 2 more }

A skill installed from the Skills API.

description: string

The installed skill description.

The installed skill name.

skill\_id: string

The referenced skill ID.

type: "skill\_reference"

The type of the object. Always `skill_reference`.

version: string

The concrete skill version installed for this session.

Inline object { description, name, type }

A skill installed from an inline ZIP archive.

description: string

The installed skill description.

The installed skill name.

type: "inline"

The type of the object. Always `inline`.

type: "openai\_hosted"

The type of the object. Always `openai_hosted`.

SelfHosted object { id, capability\_directories, remote\_url, 2 more }

An environment hosted by the application.

The public ID of the environment.

capability\_directories: array of string

Directories that contain capabilities exposed to the agent.

remote\_url: string

Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

type: "self\_hosted"

The type of the object. Always `self_hosted`.

workspace\_directory: string

The absolute project directory inside the environment. Defaults to `/workspace`.

error: string or null

The error that caused the session to fail, if any.

last\_active\_at: number

The Unix timestamp, in seconds, when the session was last active.

metadata: map[string]

Custom string key-value pairs attached to the session.

object: "agent.session"

The object type. Always `agent.session`.

required\_actions: array of object { arguments, call\_id, name, 2 more }  or object { environment\_id, type }

Actions that must be completed before the session can continue.

FunctionCall object { arguments, call\_id, name, 2 more }

Run a function tool and submit its result.

arguments: unknown

The arguments supplied by the model.

call\_id: string

The ID to include when submitting the function result.

The function name.

turn\_id: string

The ID of the turn that requested the function call.

type: "function\_call"

The type of the object. Always `function_call`.

EnvironmentConnection object { environment\_id, type }

Reconnect a session environment.

environment\_id: string

The ID of the environment to reconnect.

type: "environment\_connection"

The type of the object. Always `environment_connection`.

status: "idle" or "in\_progress" or "requires\_action" or "failed"

The current status of the session.

"idle"

The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

"in\_progress"

The session is processing a turn.

"requires\_action"

The session is waiting for one or more required actions.

"failed"

The session failed.

usage: [TokenUsage](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20token_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }  or null

Recorded token usage for a session or turn. Usage is best effort and may change.

input\_tokens: number

The number of input tokens used by the agent.

input\_tokens\_details: object { cached\_tokens }

A breakdown of the agent’s input token usage.

cached\_tokens: number

The number of input tokens retrieved from the prompt cache.

output\_tokens: number

The number of output tokens generated by the agent.

output\_tokens\_details: object { reasoning\_tokens }

A breakdown of the agent’s output token usage.

reasoning\_tokens: number

The number of output tokens used for reasoning.

total\_tokens: number

The total number of input and output tokens used by the agent.

vault\_ids: array of string

The IDs of vaults made available to the session.

### Create an agent session

curl https://api.openai.com/v1/agents/sessions \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
          "environment": {
            "type": "none"
        }'

  "agent": {
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
    "reasoning": {
      "effort": "none",
      "summary": "concise"
    },
    "service_tier": "auto",
    "text": {
      "format": {
        "type": "text"
      },
      "verbosity": "low"
    },
    "tools": [
        "defer_loading": true,
        "description": "description",
        "name": "name",
        "parameters": {
          "foo": "bar"
        },
        "type": "function"
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
      "arguments": {},
      "call_id": "call_id",
      "name": "name",
      "turn_id": "turn_id",
      "type": "function_call"
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]

  "agent": {
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
    "reasoning": {
      "effort": "none",
      "summary": "concise"
    },
    "service_tier": "auto",
    "text": {
      "format": {
        "type": "text"
      },
      "verbosity": "low"
    },
    "tools": [
        "defer_loading": true,
        "description": "description",
        "name": "name",
        "parameters": {
          "foo": "bar"
        },
        "type": "function"
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
      "arguments": {},
      "call_id": "call_id",
      "name": "name",
      "turn_id": "turn_id",
      "type": "function_call"
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]
