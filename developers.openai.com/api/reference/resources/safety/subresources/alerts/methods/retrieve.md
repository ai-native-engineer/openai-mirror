<!-- source: https://developers.openai.com/api/reference/resources/safety/subresources/alerts/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Safety](/api/reference/resources/safety)

[Alerts](/api/reference/resources/safety/subresources/alerts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve a safety alert

GET/safety/alerts/{id}

Get a safety alert belonging to the authenticated API project.

##### Path ParametersExpand Collapse

id: string

Project safety alert ID

maxLength38

##### ReturnsExpand Collapse

SafetyAlert object { id, created\_at, error\_type, 6 more }

id: string

created\_at: number

formatunixtime

error\_type: "potentially\_unintended\_data\_transfer" or "potentially\_unintended\_data\_access" or "potentially\_unintended\_destructive\_activity" or "other"

One of the following:

"potentially\_unintended\_data\_transfer"

"potentially\_unintended\_data\_access"

"potentially\_unintended\_destructive\_activity"

"other"

model: string

object: "safety.alert"

reason: string or null

A customer-safe description derived from error\_type, or null for zero data retention requests.

request\_id: string

request\_paused: boolean

Whether block registration succeeded for this request. This does not confirm that response execution stopped.

response\_id: string

### Retrieve a safety alert

HTTP

HTTPHTTP

PythonPython

TypeScriptTypeScript

GoGo

RubyRuby

JavaJava

CLI ToolCLI Tool

```
curl https://api.openai.com/v1/safety/alerts/alert_0123456789abcdef0123456789abcdef \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

```
{
  "id": "alert_0123456789abcdef0123456789abcdef",
  "object": "safety.alert",
  "created_at": 1787659200,
  "request_id": "req_123",
  "response_id": "resp_123",
  "model": "gpt-6-astra",
  "request_paused": true,
  "error_type": "potentially_unintended_data_access",
  "reason": "Potentially unintended data access."
}
```

##### Returns Examples

```
{
  "id": "alert_0123456789abcdef0123456789abcdef",
  "object": "safety.alert",
  "created_at": 1787659200,
  "request_id": "req_123",
  "response_id": "resp_123",
  "model": "gpt-6-astra",
  "request_paused": true,
  "error_type": "potentially_unintended_data_access",
  "reason": "Potentially unintended data access."
}
```
