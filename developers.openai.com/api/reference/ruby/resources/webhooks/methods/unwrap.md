<!-- source: https://developers.openai.com/api/reference/ruby/resources/webhooks/methods/unwrap/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Webhooks](/api/reference/ruby/resources/webhooks)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unwrap

webhooks.unwrap() -> void

Function

Validates that the given payload was sent by OpenAI and parses the payload.

### Unwrap

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.webhooks.unwrap

puts(result)

##### Returns Examples
