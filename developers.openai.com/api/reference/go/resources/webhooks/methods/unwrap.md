<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/methods/unwrap/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Webhooks](/api/reference/go/resources/webhooks)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Unwrap

client.Webhooks.Unwrap(ctx) error

Function

Validates that the given payload was sent by OpenAI and parses the payload.

### Unwrap

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  err := client.Webhooks.Unwrap(context.TODO())
  if err != nil {
    panic(err.Error())

##### Returns Examples
