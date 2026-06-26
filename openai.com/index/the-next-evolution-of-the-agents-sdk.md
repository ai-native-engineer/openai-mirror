<!-- source: https://openai.com/index/the-next-evolution-of-the-agents-sdk/ -->

April 15, 2026

[Product](/news/product-releases/)

# The next evolution of the Agents SDK

The updated Agents SDK helps developers build agents that can inspect files, run commands, edit code, and work on long-horizon tasks within controlled sandbox environments.

We’re introducing new capabilities to the [Agents SDK⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/agents) that give developers standardized infrastructure that is easy to get started with and is built correctly for OpenAI models: a model-native harness that lets agents work across files and tools on a computer, plus native sandbox execution for running that work safely.

For example, developers can give an agent a controlled workspace, explicit instructions, and the tools it needs to inspect evidence:

#### Python

```` ```
1

# pip install "openai-agents>=0.14.0"

2

3

import asyncio

4

import tempfile

5

from pathlib import Path

6

7

from agents import Runner

8

from agents.run import RunConfig

9

from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig

10

from agents.sandbox.entries import LocalDir

11

from agents.sandbox.sandboxes import UnixLocalSandboxClient

12

13

14

async def main() -> None:

15

with tempfile.TemporaryDirectory() as tmp:

16

dataroom = Path(tmp) / "dataroom"

17

dataroom.mkdir()

18

(dataroom / "metrics.md").write_text(

19

"""# Annual metrics

20

21

| Year | Revenue | Operating income | Operating cash flow |

22

| --- | ---: | ---: | ---: |

23

| FY2025 | $124.3M | $18.6M | $24.1M |

24

| FY2024 | $98.7M | $12.4M | $17.9M |

25

""",

26

encoding="utf-8",

27

)

28

29

agent = SandboxAgent(

30

name="Dataroom Analyst",

31

model="gpt-5.4",

32

instructions="Answer using only files in data/. Cite source filenames.",

33

default_manifest=Manifest(entries={"data": LocalDir(src=dataroom)}),

34

)

35

36

result = await Runner.run(

37

agent,

38

"Compare FY2025 revenue, operating income, and operating cash flow with FY2024.",

39

run_config=RunConfig(

40

sandbox=SandboxRunConfig(client=UnixLocalSandboxClient()),

41

),

42

)

43

print(result.final_output)

44

45

46

if __name__ == "__main__":

47

asyncio.run(main())

48
``` ````

Developers need more than the best models to build useful agents—they need systems that support how agents inspect files, run commands, write code, and keep working across many steps.

The systems that exist today come with tradeoffs as teams move from prototypes to production. Model-agnostic frameworks are flexible but do not fully utilize frontier models capabilities ; model-provider SDKs can be closer to the model but often lack enough visibility into the harness; and managed agent APIs can simplify deployment but constrain where agents run and how they access sensitive data.

Here’s what some of the customers who tested the new SDK with us had to say:

> “The updated Agents SDK made it production-viable for us to automate a critical clinical records workflow that previous approaches couldn’t handle reliably enough. For us, the difference was not just extracting the right metadata, but correctly understanding the boundaries of each encounter in long, complex records. As a result, we can more quickly understand what's happening for each patient in a given visit, helping members with their care needs and improving their experience with us.”

— Rachael Burns, Staff Engineer & AI Tech Lead, Oscar Health

## A more capable harness for the agent loop

With today’s release, the Agents SDK harness becomes more capable for agents that work with documents, files, and systems. It now has configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, and standardized integrations with primitives that are becoming common in frontier agent systems.

These primitives include tool use via [MCP⁠(opens in a new window)](https://modelcontextprotocol.io), progressive disclosure via [skills⁠(opens in a new window)](https://agentskills.io), custom instructions via [AGENTS.md⁠(opens in a new window)](https://agents.md), code execution using the [shell⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/tools-shell) tool, file edits using the [apply patch⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/tools-apply-patch) tool, and more. The harness will continue to incorporate new agentic patterns and primitives over time, so developers can spend less time on core infrastructure updates and more time on the domain-specific logic that makes their agents useful.

![Diagram showing how the Agent SDK connects user input, models, and tools to build AI agents.](https://images.ctfassets.net/kftzwdyauwt9/62VtxAHiyQDEZeIPR3jJRC/ccef350e099792d7d6a7d9b41b61ac32/AgentSDK_BuildingAgentsWithModels-LightMode-500px.svg?w=3840&q=90)

![Diagram showing how to build AI agents using the Agent SDK with models, tools, and orchestration.](https://images.ctfassets.net/kftzwdyauwt9/75glmB5ZouJGgoRiiALGct/c15cc514db014be5bc7b9dc19a087ea0/AgentSDK_BuildingWithAgentsSDK-LightMode-500px.svg?w=3840&q=90)

The harness also helps developers unlock more of a frontier model’s capability by aligning execution with the way those models perform best. That keeps agents closer to the model’s natural operating pattern, improving reliability and performance on complex tasks—particularly when work is long-running or coordinated across a diverse set of tools and systems.

In addition, we realize each product is unique and rarely fits neatly into a mold. We designed Agents SDK to support this diversity. Developers get a harness that’s turnkey yet flexible—making it easy to adapt it to their own stack—including tool use, memory, and sandbox environment.

## Native sandbox execution

The updated Agents SDK supports sandbox execution natively, so agents can run in controlled computer environments with the files, tools, and dependencies they need for a task.

Many useful agents need a workspace where they can read and write files, install dependencies, run code, and use tools safely. Native sandbox support gives developers that execution layer out of the box, instead of forcing them to piece it together themselves.

Developers can bring their own sandbox or use built-in support for Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, and Vercel.

To make those environments portable across providers, the SDK also introduces a Manifest abstraction for describing the agent’s workspace. Developers can mount local files, define output directories, and bring in data from storage providers including AWS S3, Google Cloud Storage, Azure Blob Storage, and Cloudflare R2.

This gives developers a consistent way to shape the agent’s environment from local prototype to production deployment. It also gives the model a predictable workspace: where to find inputs, where to write outputs, and how to keep work organized across a long-running task.

![Logos for Daytona, E2B, Modal, Cloudflare, Vercel, Blaxel, Runloop](https://images.ctfassets.net/kftzwdyauwt9/1Q9fzbRG0Lsfv8neHtwibW/749d6c2f06610c5cd8a81f1824ce9d34/logos-light.png?w=3840&q=90&fm=webp)

## Separating harness from compute for security, durability, and scale

Agent systems should be designed assuming prompt-injection and exfiltration attempts. Separating harness and compute helps keep credentials out of environments where model-generated code executes.

It also enables durable execution. When the agent’s state is externalized, losing a sandbox container does not mean losing the run. With built-in snapshotting and rehydration, the Agents SDK can restore the agent’s state in a fresh container and continue from the last checkpoint if the original environment fails or expires.

Finally, it makes agents more scalable. Agent runs can use one sandbox or many, invoke sandboxes only when needed, route subagents to isolated environments, and parallelize work across containers for faster execution.

![Flow diagram illustrating how the Agent SDK enables AI agents to use additional compute resources for more complex tasks.](https://images.ctfassets.net/kftzwdyauwt9/7B96BmwdCcPwlY5CfQT81V/b327a755f297609d1b37a57f83925ef1/AgentSDK_HarnessWithCompute-LightMode-500px.svg?w=3840&q=90)

![Diagram depicting how AI agents built with the Agent SDK can orchestrate separate compute systems, allowing workloads to run independently while supporting more advanced tasks.](https://images.ctfassets.net/kftzwdyauwt9/0CDmKna4q9MihFzOSA6x/1d84c545399ba4487a404beee8864ff3/AgentSDK_HarnessSeparate-LightMode-500px__1_.svg?w=3840&q=90)

## Pricing and availability

These new Agents SDK capabilities are generally available to all customers via the API and use standard API pricing, based on tokens and tool use.

## What’s next

As we continue to develop the Agents SDK, we’ll keep expanding what developers can build with it, making it easier to bring more capable agents into production with less custom infrastructure, while preserving the flexibility and control developers need to fit agents into their own environments.

The new harness and sandbox capabilities are launching first in Python, with TypeScript support planned for a future release. We’re also working to bring additional agent capabilities, including code mode and subagents, to both Python and TypeScript.

In addition, we want to help bring the broader agent ecosystem together over time, with support for more sandbox providers, more integrations, and more ways for developers to plug the SDK into the tools and systems they already use.

* [2026](/news/?tags=2026)
* [API Platform](/news/?tags=api-platform)

## Author

## Keep reading

![Spend Controls_Artcard.png](https://images.ctfassets.net/kftzwdyauwt9/3RkIKhLVsVWcJQ3czkTNMH/c63f9c43efd82ddf863f87d44edca201/Spend_Controls_Artcard.png?w=3840&q=90&fm=webp)

[New usage analytics and updated spend controls for enterprises

ProductJun 18, 2026](/index/chatgpt-enterprise-spend-controls/)

![1x1 Health Art 1](https://images.ctfassets.net/kftzwdyauwt9/25I93CBDfs6LgX4R4XCMBD/121ac551be0a9153314bf51fdbe91dae/1x1_Health_Art_1.png?w=3840&q=90&fm=webp)

[Improving health intelligence in ChatGPT

ProductJun 18, 2026](/index/improving-health-intelligence-in-chatgpt/)

![Intro-OAI-Partner-ArtCard](https://images.ctfassets.net/kftzwdyauwt9/U6bb3rlwvYyhf2q835WWx/d50f5492dded3c21aa6d69c07d3b2a44/Introducing_OAI_Partner_Network_artcard.png?w=3840&q=90&fm=webp)

[Introducing the OpenAI Partner Network

ProductJun 14, 2026](/index/introducing-openai-partner-network/)
