<!-- source: https://developers.openai.com/api/reference/java/resources/realtime/subresources/calls/methods/hangup/ -->

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

# Hang up call

realtime().calls().hangup(CallHangupParamsparams = CallHangupParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/realtime/calls/{call\_id}/hangup

End an active Realtime API call, whether it was initiated over SIP or
WebRTC.

##### ParametersExpand Collapse

CallHangupParams params

Optional<String> callId

### Hang up call

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
import com.openai.models.realtime.calls.CallHangupParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        client.realtime().calls().hangup("call_id");

##### Returns Examples
