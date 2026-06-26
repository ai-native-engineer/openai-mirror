<!-- source: https://developers.openai.com/api/reference/java/resources/realtime/subresources/calls/methods/reject/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Realtime](/api/reference/java/resources/realtime)

[Calls](/api/reference/java/resources/realtime/subresources/calls)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Reject call

realtime().calls().reject(CallRejectParamsparams = CallRejectParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/realtime/calls/{call\_id}/reject

Decline an incoming SIP call by returning a SIP status code to the caller.

##### ParametersExpand Collapse

CallRejectParams params

Optional<String> callId

Optional<Long> statusCode

SIP response code to send back to the caller. Defaults to `603` (Decline)
when omitted.

### Reject call

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.realtime.calls.CallRejectParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        client.realtime().calls().reject("call_id");

##### Returns Examples
