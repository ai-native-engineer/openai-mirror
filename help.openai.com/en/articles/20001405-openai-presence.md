<!-- source: https://help.openai.com/en/articles/20001405-openai-presence -->

# OpenAI Presence

Learn what OpenAI Presence is, how managed deployments work, and what availability, safeguards, and support to expect.

Updated: 18 days ago

OpenAI Presence is a managed enterprise platform for building, deploying, operating, and continuously improving governed AI agents for high-volume, high-stakes workflows.

Presence combines OpenAI models with the tools organizations need to define policies and permissions, connect business systems, test agent behavior, monitor production outcomes, and involve people when human judgment is needed.

This article provides a general overview. Exact features, models, channels, capacity, data handling, pricing, and service commitments are defined for each deployment.

# Who is OpenAI Presence for?

OpenAI Presence is designed for organizations with high scale, repeatable workflows that require strong governance, reliability, and operational oversight. Customer support and voice are strong early use cases, but Presence can support both customer-facing and internal workflows.

Presence is currently available through limited general availability (limited GA) as a managed deployment (see below). It is not a self-serve product. Access depends on workflow fit, implementation readiness, and available delivery capacity. Contact your OpenAI account representative for more information.

## What can a Presence agent do?

A Presence agent can be configured to:

* Follow approved instructions, standard operating procedures (SOPs), and organizational policies.
* Use approved knowledge and connect to business systems through APIs and tools with scoped permissions.
* Retrieve information, update systems, and complete approved actions.
* Communicate through supported voice or chat experiences, depending on the deployment.
* Escalate to a person or another support path when a policy, risk, or workflow requires human judgment.

Exact capabilities and integrations are confirmed during technical scoping.

## How is a Presence agent governed?

Presence includes controls for testing and operating agents in production. Depending on the deployment, these can include:

* Simulations and evaluations that test common workflows and edge cases before release.
* Guardrails, permissions, and approval steps that define what the agent can do.
* Session records, action histories, and quality signals that teams can review to improve the agent.
* Human escalation paths with structured context for the receiving team.
* Controlled rollout, monitoring, and rollback processes for new versions.

These controls help organizations evaluate changes before release and improve the agent using production evidence while keeping the organization in control.

## How does deployment work?

OpenAI Forward Deployed Engineers, select deployment partners, or both work with the customer through a managed process that typically includes:

1. Defining business outcomes, success criteria, and the initial workflows.
2. Connecting required systems and encoding policies, permissions, and escalation paths.
3. Completing security, privacy, and legal review for the deployment.
4. Running simulations, evaluations, and acceptance testing.
5. Staging a controlled production rollout and monitoring outcomes.
6. Reviewing evidence and making tested improvements over time.

A Presence agent does not become production-ready simply by ingesting documents. Each deployment requires scoping, integration, testing, review, and approval before launch.

## Which channels does OpenAI Presence support?

During limited GA, Presence supports conversational workflows through voice or chat. The available channel, contact-center integration, routing, authentication, and human-handoff design are confirmed for each deployment.

## What OpenAI models does Presence use?

Presence uses OpenAI models. The model configuration is selected for the workflow and may combine real-time interaction with deeper reasoning or tool execution. The exact configuration is validated for each deployment and may change as the workflow evolves.

## How are data, privacy, and security handled?

Data handling is defined and reviewed for each deployment. This includes which data the agent can access, what is logged, how sensitive information is removed or masked, how long data is retained, where data is stored, and who can access it.

Refer to the approved architecture, security documentation, and contract for your deployment. Configuration can differ across Presence deployments, so your deployment documentation is the definitive source for these details.

## How is OpenAI Presence different from ChatGPT Workspace Agents?

OpenAI Presence is a separate, managed enterprise product for production workflows that require integrations, testing, guardrails, monitoring, and deployment support.

[ChatGPT Workspace Agents for Enterprise and Business](/en/articles/20001143) are created, used, shared, and managed within supported ChatGPT and Slack workspace experiences. Presence agents are scoped and deployed with OpenAI, a select deployment partner, or both and are not created through the ChatGPT workspace agent interface.

## How do I get access to OpenAI Presence?

Contact your OpenAI account team to discuss eligibility, workflow fit, implementation readiness, and delivery capacity. Pricing and implementation scope are specific to each customer and deployment.
