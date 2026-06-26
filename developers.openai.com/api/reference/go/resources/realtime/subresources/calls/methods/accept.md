<!-- source: https://developers.openai.com/api/reference/go/resources/realtime/subresources/calls/methods/accept/ -->

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

# Accept call

client.Realtime.Calls.Accept(ctx, callID, body) error

POST/realtime/calls/{call\_id}/accept

Accept an incoming SIP call and configure the realtime session that will
handle it.

##### ParametersExpand Collapse

callID string

body CallAcceptParams

RealtimeSessionCreateRequest param.Field[[RealtimeSessionCreateRequest](/api/reference/go/resources/realtime#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema))]

Realtime session object configuration.

### Accept call

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
  err := client.Realtime.Calls.Accept(
    context.TODO(),
    "call_id",
    realtime.CallAcceptParams{
      RealtimeSessionCreateRequest: realtime.RealtimeSessionCreateRequestParam{

  if err != nil {
    panic(err.Error())

##### Returns Examples
