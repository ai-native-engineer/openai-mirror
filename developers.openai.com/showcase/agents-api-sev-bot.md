<!-- source: https://developers.openai.com/showcase/agents-api-sev-bot/ -->

## Showcase projects

[![Build an AI teammate for Slack](/showcase/agents-api-slack-bot.webp)

### Build an AI teammate for Slack

Search your workplace, analyze data, and complete real work without...](/showcase/agents-api-slack-bot)[![Bulk invoice and contract review](/showcase/agents-api-document-review.webp)

### Bulk invoice and contract review

Apply reusable policy skills to document batches with specialist agents.](/showcase/agents-api-document-review)[![Data agent](/showcase/agents-api-data-agent.webp)

### Data agent

Connect your warehouse and investigate business questions with context and...](/showcase/agents-api-data-analyst)[![GitHub issue investigation agent](/showcase/agents-api-github-issues.webp)

### GitHub issue investigation agent

Turn a new bug report into a clear root-cause analysis and suggested fix.](/showcase/agents-api-github-issues)[![SRE agent for incident response](/showcase/agents-api-sev-bot.webp)

### SRE agent for incident response

Investigate incidents in Slack using GitHub, AWS, and incident memory.](/showcase/agents-api-sev-bot)[![Photobooth Demo](/images/api/models/gpt-image-2.jpg)

### Photobooth Demo

Image API demo for capturing or uploading a portrait and generating...](/showcase/openai-imagegen-demo)[![OpenAI.fm](/showcase/tts-1.jpg)

### OpenAI.fm

Interactive Speech API demo for trying OpenAI text-to-speech voices.](https://openai.fm/)[![Realtime Solar System](/showcase/gpt-realtime.jpg)

### Realtime Solar System

Realtime API demo that lets you talk to a 3D solar system.](/showcase/solar-system-demo)[![Chatkit.world](/showcase/gpt-5-1.jpg)

### Chatkit.world

Map-based chat experience to explore the world through conversation.](/showcase/chatkit-world)

[View on GitHub](https://github.com/OpenAI-Early-Access/agents-api-python-preview/tree/main/examples/apps/sev_bot)

### Agents API features

* Function tools
* Skills
* Sandbox
* Webhooks
* Persistent sessions
* Streaming

### Why use the Agents API?

#### Incident-triggered execution

A PagerDuty, incident.io, or Alertmanager webhook starts the investigation automatically, without waiting for a responder to restate the symptoms.

#### Persistent incident memory

One agent session retains the current incident's findings and follow-ups; a separate incident-history tool brings relevant past outages and mitigations into the investigation.

#### Operational tools

Your application supplies service evidence and incident records. Service-connected MCP servers provide GitHub and AWS access, and the sandbox holds the runbook.

#### Human-approved changes

The agent posts its findings and proposed rollback to #oncall, but only a responder can approve a production change.

### What you need

* Python 3.14+ and uv.
* A sandbox: self-hosted Docker or a  [third-party provider](https://developers.openai.com/api/docs/guides/agents/sandboxes#sandbox-providers)
  .
* An OpenAI API key.
* A Slack app installed in #oncall, with a bot token, signing secret, and message event subscriptions.
* PagerDuty, incident.io, or an Alertmanager-compatible monitoring system.
* Read access to the affected GitHub repository.
* AWS DevOps Agent credentials or another read-only AWS integration.

### The workflow at a glance

1. PagerDuty / incident.io
   →
2. Slack #oncall
   →
3. Agents API session
   →
4. Sandbox + AWS skills
   →
5. GitHub / AWS / memory
   →
6. Approved recovery

### Build the application

1. 1

   #### Set up

   Clone the repository, configure your OpenAI API key and Slack app credentials, and build the incident sandbox image.

   git clone https://github.com/OpenAI-Early-Access/agents-api-python-preview.git
   cd agents-api-python-preview
   cp examples/apps/sev_bot/.env.example examples/apps/sev_bot/.env
   # Add OPENAI_API_KEY, SLACK_BOT_TOKEN, and SLACK_SIGNING_SECRET to .env.
   docker build -t agent-api-sev-sandbox:latest examples/apps/sev_bot

   Create the Slack app from examples/apps/sev\_bot/slack-app-manifest.yaml. Set its HTTPS URLs to your host, install it, and invite it to #oncall. The manifest routes message.channels and message.groups to /slack/events and approval buttons to /slack/actions.
2. 2

   #### Install AWS skills in the sandbox

   The sandbox image contains Python, the Codex CLI, and AWS Agent Toolkit skills. Install the skills once at build time so every incident starts with the same guidance.

   FROM python:3.14-slim

   RUN apt-get update \
       && apt-get install --yes --no-install-recommends ca-certificates git nodejs npm ripgrep \
       && npm install --global @openai/codex@alpha \
       && rm -rf /var/lib/apt/lists/*

   RUN mkdir -p /workspace /codex-home
   ENV CODEX_HOME=/codex-home
   WORKDIR /workspace

   RUN npx --yes skills add aws/agent-toolkit-for-aws/skills \
       --agent codex --copy --yes

   This copies all skills into /workspace/.agents/skills for automatic discovery.
3. 3

   #### Receive incident alerts

   Accept webhooks from PagerDuty, incident.io, or Alertmanager and normalize them into a common incident shape. Start the investigation in the background and reuse the alert fingerprint to avoid duplicate incidents.

   from fastapi import BackgroundTasks, Request

   @app.post("/webhooks/alerts")
   async def receive_alert(request: Request, tasks: BackgroundTasks):
       # Verify the sender at your ingress before forwarding the webhook.
       payload = await request.json()
       return queue_alerts(app.state.bot, payload, tasks)

   The complete example's queue\_alerts helper normalizes payloads, deduplicates active alerts, retries failed investigations, and handles resolved incidents.
4. 4

   #### Inspect the alert

   The normalized alert identifies the affected service, severity, and customer-visible symptom. Its fingerprint becomes the stable key for both the agent session and the Slack incident thread.

     "status": "firing",
     "alerts": [{
       "fingerprint": "checkout-api-high-error-rate",
       "labels": {
         "service": "checkout-api",
         "severity": "critical"
       },
       "annotations": {
         "summary": "Checkout API error rate reached 18.7%"
     }]
5. 5

   #### Open the Slack incident thread

   Post the incoming incident to #oncall and keep the returned thread timestamp. Investigation findings, follow-up questions, and rollback approvals all stay in this thread.

   from slack_sdk.web.async_client import AsyncWebClient

   slack = AsyncWebClient(token=os.environ["SLACK_BOT_TOKEN"])
   message = await slack.chat_postMessage(
       channel="#oncall",
       text=f"*{incident['severity']}* {incident['title']}",
   )
   incident["slack_thread_ts"] = message["ts"]
6. 6

   #### Define the application tools

   Combine metrics, logs, and deployments in get\_service\_evidence. Use recall\_incidents for past outages and propose\_rollback to request approval. Only the two read-only functions run automatically; GitHub and AWS use MCP.

   handlers = {
       "get_service_evidence": get_service_evidence,
       "recall_incidents": recall_incidents,

   tools = [
       # Declare all three function schemas, including propose_rollback.
       *operational_function_tools,
       {"type": "programmatic_tool_calling", "enabled": True},
   ]

   Keep propose\_rollback out of handlers so its call stays pending until Slack approval. The first run uses bundled sample telemetry; connect get\_service\_evidence to your monitoring system before diagnosing real incidents.
7. 7

   #### Connect GitHub MCP

   Set GITHUB\_TOKEN and GITHUB\_REPOSITORY in .env. Use a fine-grained token scoped to the affected repository, with read access to Contents and Pull requests. Agents API calls GitHub directly, without a custom handler or sandbox credentials.

   github_tool = {
       "type": "mcp",
       "server_label": "github",
       "connection_origin": "service",
       "required": True,
       "allowed_tools": [
           "list_commits",
           "get_commit",
           "list_pull_requests",
           "pull_request_read",
           "get_file_contents",
       ],
       "transport": {
           "type": "http",
           "server_url": "https://api.githubcopilot.com/mcp/readonly",
           "authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
       },
   tools.append(github_tool)

   The read-only endpoint and allowlist expose only repository inspection tools. GITHUB\_REPOSITORY tells the agent where to look; token permissions enforce access. Without GITHUB\_TOKEN, the runnable example skips MCP and includes bundled sample PRs and commits in get\_service\_evidence.
8. 8

   #### Connect the AWS DevOps Agent

   The AWS Agent Toolkit includes an incident-response MCP server. Configure it as a service-connected tool so the agent can investigate AWS infrastructure without moving cloud credentials into a sandbox.

   aws_tool = {
       "type": "mcp",
       "server_label": "aws_devops",
       "connection_origin": "service",
       "transport": {
           "type": "http",
           "server_url": "https://connect.aidevops.us-east-1.api.aws/mcp",
           "authorization": f"Bearer {aws_token}",
       },
   tools.append(aws_tool)

   Without AWS MCP configured, get\_service\_evidence includes bundled CloudWatch, ECS, and ElastiCache telemetry. Setting DEVOPS\_AGENT\_TOKEN omits that sample AWS data and enables the MCP server.
9. 9

   #### Create an incident session

   Create one self-hosted Agents API session per alert fingerprint. Have the agent correlate evidence and request approval before recovery.

   from agent_api_sdk import AgentAPISDK

   instructions = """\
   Investigate the incident using service evidence, GitHub, AWS, and past incidents.
   Consult /workspace/runbooks/<service>.md and explain impact, likely cause, and next steps.
   Use read-only tools; never install integrations or change infrastructure.
   Clearly separate sample data from live findings.
   If a rollout caused the incident, call propose_rollback once for the previous healthy version.
   Approval records a decision, not an executed rollback.
   """

   client = AgentAPISDK()
   session = await client.sessions.create(
       agent={
           "model": "gpt-6-astra",
           "instructions": instructions,
           "reasoning": {"effort": "high"},
           "multi_agent": {"enabled": True, "max_concurrent_subagents": 3},
           "tools": tools,
       },
       environment={"type": "self_hosted", "workspace_directory": "/workspace"},
   )
   incident["session_id"] = session.id
10. 10

    #### Connect the incident sandbox

    Mount examples/apps/sev\_bot/runbooks read-only at /workspace/runbooks. Start codex exec-server with the session's environment ID, then submit the investigation. Keep the container alive for follow-ups.

    import asyncio
    import os
    from pathlib import Path

    import docker

    container = await asyncio.to_thread(
        docker.from_env().containers.run,
        "agent-api-sev-sandbox:latest",
        [
            "codex", "exec-server",
            "--remote", "https://api.openai.com/v1/agents/api",
            "--environment-id", session.info.environment.environment_id,
        ],
        environment={"CODEX_API_KEY": os.environ["OPENAI_API_KEY"]},
        volumes={
            str(Path("examples/apps/sev_bot/runbooks").resolve()): {
                "bind": "/workspace/runbooks",
                "mode": "ro",
            },
        },
        working_dir="/workspace",
        detach=True,
    )
    incident["sandbox"] = container

    events = session.stream(
        input="Investigate the checkout-api error spike.",
        # Read-only handlers only; the webhook handles propose_rollback.
        tool_handlers=handlers,
    )

    Inject the same OpenAI API key as CODEX\_API\_KEY at runtime, never during the image build. The example keeps Slack, GitHub, and AWS credentials outside the sandbox.
11. 11

    #### Receive approval requests from Agents API

    Register /webhooks/openai in your OpenAI project's webhook settings, subscribe to agent.session.action\_required, and set OPENAI\_WEBHOOK\_SECRET. Retrieve the pending call before asking for a Slack decision.

    @app.post("/webhooks/openai")
    async def openai_webhook(request: Request):
        # Verify OpenAI's signature before reading the event.
        event = await request.json()
        if event["type"] == "agent.session.action_required":
            session = await client.sessions.retrieve(event["data"]["id"])
            for pending in session.info.required_actions:
                if pending.type != "function_call" or pending.name != "propose_rollback":
                    continue
                # Find the incident by session ID and deduplicate by call ID.
                incident["pending_action"] = {
                    "turn_id": pending.turn_id,
                    "call_id": pending.call_id,
                await post_approval_buttons(incident, pending.arguments)
        return {"status": "ok"}

    The runnable receiver verifies signatures, validates the proposed service and version, and handles repeated deliveries. Do not register an automatic handler for propose\_rollback: the function call must remain pending until a person decides.
12. 12

    #### Post findings to #oncall

    Save the session ID, track tool activity, and publish the completed investigation into the original Slack thread. The diagnosis can cite a pull request, commit, CloudWatch alarm, and related prior incident.

    findings = []
    async for event in events:
        incident["session_id"] = event.session_id

        if event.type == "session.turn.item.added" and event.function_call:
            incident["timeline"].append(event.function_call["name"])

        if event.output_text_delta:
            findings.append(event.output_text_delta)

    await slack.chat_postMessage(
        channel="#oncall",
        thread_ts=incident["slack_thread_ts"],
        text="".join(findings),
    )
13. 13

    #### Use incident memory

    The incident session retains its conversation. Across incidents, recall\_incidents searches history loaded from a local JSON file. On the first run, load the bundled sample history instead.

    import json
    from pathlib import Path

    memory_file = Path("examples/apps/sev_bot/incident_memory.json")
    source = memory_file if memory_file.exists() else memory_file.with_name("incident_history.json")
    incident_history = json.loads(source.read_text())

    session = await client.sessions.retrieve(incident["session_id"])

    async for event in session.stream(
        input="Did a similar Redis connection-pool failure happen before?",
        tool_handlers=handlers,
    ):
        if event.output_text_delta:
            print(event.output_text_delta, end="")

    Resolved-incident history survives restarts in incident\_memory.json, which is ignored by Git. Active Slack threads, approvals, session IDs, and sandbox handles still live in memory. Use one app process per file.
14. 14

    #### Return the human decision to the agent

    The Slack callback submits approval or rejection as the pending function's result. The agent continues the same turn and explains the next steps. No deployment is executed.

    @app.post("/slack/actions")
    async def approve_rollback(request: Request):
        # Verify the Slack signature and the responder's permissions.
        action = get_slack_action(request)
        pending = incident["pending_action"]
        session = await client.sessions.retrieve(incident["session_id"])
        await session.tool_result(
            turn_id=pending["turn_id"],
            call_id=pending["call_id"],
            success=True,
            output={
                "decision": "approved" if action["action_id"] == "approve_rollback" else "rejected",
                "executed": False,
            },
        )
        return {"text": "Decision sent to the agent."}

    The runnable callback acknowledges Slack immediately and submits the result in the background. Both OpenAI and Slack callbacks need reachable HTTPS URLs. The original stream stays open for progress and resumed output; approval is driven by the webhook.
15. 15

    #### Start the Slack incident bot

    Start the webhook receiver, then send the included alert from another terminal. Investigation updates, follow-ups, and approval buttons appear in #oncall.

    uv run examples/apps/sev_bot/main.py

    # From another terminal:
    curl -X POST http://127.0.0.1:8003/webhooks/alerts \
      -H 'Content-Type: application/json' \
      --data-binary @examples/apps/sev_bot/sample_alert.json
16. 16

    #### Connect your incident provider

    Forward authenticated incident events to the receiver. For PagerDuty, subscribe to incident.triggered and incident.resolved and match its service name to operations.json. For incident.io, subscribe to public incident-created and status-updated v2 events and set INCIDENT\_SERVICE for the subscription.

    receivers:
      - name: incident-bot
        webhook_configs:
          - url: https://your-app.example/webhooks/alerts
            http_config:
              authorization:
                credentials: your-shared-token

    Set ALERT\_WEBHOOK\_TOKEN to the same value. For PagerDuty or incident.io, your ingress must verify the provider's native signature and forward a bearer token; the example does not implement that signature verification.
17. 17

    #### Resolve the incident

    A resolved alert saves the findings, posts a final Slack update, and deletes the session and sandbox. Write a temporary file, then replace the saved history atomically. Approval alone does not mean a rollback ran.

    incident_history.append({
        "id": incident["id"],
        "service": incident["service"],
        "summary": incident["title"],
        "root_cause": incident["analysis"][:1200],
        "resolution": "Resolved; this app did not execute a rollback.",
    })
    session = await client.sessions.retrieve(incident["session_id"])
    try:
        temporary = memory_file.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(incident_history, indent=2) + "\n")
        temporary.replace(memory_file)
    finally:
        try:
            await session.delete()
        finally:
            await asyncio.to_thread(incident["sandbox"].remove, force=True)

    The runnable example also cleans up the sandbox after failed investigations and on application shutdown.

### What you built

The included checkout alert produces an investigation like this, using bundled telemetry and real Slack delivery.

SEV-1 Checkout API error rate reached 18.7%
Slack: #oncall
Evidence: bundled sample telemetry, not a live production diagnosis.

Customer impact: approximately 782 failed checkouts per minute.
GitHub: PR #418 / commit 8c41f2e reduced max_connections from 64 to 8.
AWS: CloudWatch alarm firing; ElastiCache has 143 waiting requests.
Memory: INC-0931 recorded the same Redis pool failure and recovery.
Action: Roll back checkout-api to 2026.08.26.3, pending approval.

### Make it your own

* Connect the Slack app to #oncall and configure incident notifications from PagerDuty, incident.io, or Alertmanager.
* Replace fixture-backed evidence with your GitHub repository, AWS resources, production telemetry, and historical incident store.
* Persist incident fingerprints, Slack thread IDs, agent session IDs, and approved remediation decisions.
* Verify responder identity and production access before executing an approved rollback.

### Related reading

* [Sandbox providers](https://developers.openai.com/api/docs/guides/agents/sandboxes#sandbox-providers)

  Replace local Docker with a third-party sandbox running the same image and executor.
* [GitHub MCP](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md)

  Configure GitHub's hosted MCP server, read-only mode, and tool selection.
* [AWS skills](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills)

  Skill instructions for AWS observability, compute, databases, and incident investigation.
* [AWS Agent Toolkit](https://github.com/aws/agent-toolkit-for-aws)

  Official AWS agent skills, MCP servers, and operational integrations.
* [AWS DevOps Agent integration](https://github.com/aws/agent-toolkit-for-aws/tree/main/plugins/aws-agents-for-devsecops)

  AWS incident investigation, service inspection, and remediation recommendations through MCP.
* [Slack chat.postMessage](https://docs.slack.dev/reference/methods/chat.postMessage/)

  Send incident updates and follow-up messages to a Slack thread.

## Related projects

[![GitHub issue investigation agent](/showcase/agents-api-github-issues.webp)

### GitHub issue investigation agent

An issue investigator that checks out the repository, reproduces reported...

GPT-6 Astra  Agents API  Python](/showcase/agents-api-github-issues)[![Build an AI teammate for Slack](/showcase/agents-api-slack-bot.webp)

### Build an AI teammate for Slack

A Slack teammate that searches connected workplace tools, investigates...

GPT-6 Astra  Agents API  Python](/showcase/agents-api-slack-bot)[![Bulk invoice and contract review](/showcase/agents-api-document-review.webp)

### Bulk invoice and contract review

A document reviewer that applies reusable policy skills, delegates work to...

gpt-5.6-luna  Agents API  Python](/showcase/agents-api-document-review)
