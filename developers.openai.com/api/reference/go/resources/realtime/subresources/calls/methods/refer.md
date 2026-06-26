<!-- source: https://developers.openai.com/api/reference/go/resources/realtime/subresources/calls/methods/refer/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Realtime](/api/reference/go/resources/realtime)

[Calls](/api/reference/go/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Refer call

client.Realtime.Calls.Refer(ctx, callID, body) error

POST/realtime/calls/{call\_id}/refer

Transfer an active SIP call to a new destination using the SIP REFER verb.

##### ParametersExpand Collapse

callID string

body CallReferParams

TargetUri param.Field[string]

URI that should appear in the SIP Refer-To header. Supports values like
`tel:+14155550123` or `sip:agent@example.com`.

### Refer call

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
  "github.com/openai/openai-go/realtime"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  err := client.Realtime.Calls.Refer(
    context.TODO(),
    "call_id",
    realtime.CallReferParams{
      TargetUri: "tel:+14155550123",
  if err != nil {
    panic(err.Error())

##### Returns Examples
