<!-- source: https://openai.com/index/datadog/ -->

January 9, 2026

# Datadog uses Codex for system-level code review

With Codex, Datadog brings system-wide context into every code review to prevent incidents and protect customer trust.

[Datadog⁠(opens in a new window)](https://www.datadoghq.com/) runs one of the world’s most widely-used observability platforms, helping companies monitor, troubleshoot, and secure complex distributed systems. When something breaks, customers depend on Datadog to surface issues fast, which means reliability has to be built in long before code ever reaches production.

For Datadog’s engineering teams, that makes code review a high-stakes moment. It’s not just about catching mistakes, but about understanding how changes ripple through interconnected systems—an area where traditional static analysis and rule-based tools often fall short.

To meet this challenge, Datadog’s AI Development Experience (AI DevX) team turned to Codex, the coding agent from OpenAI, which brings system-level reasoning into code review and surfaces risks humans can’t easily see at scale.

“Time savings are real and important,” says Brad Carter, who leads Datadog’s AI DevX team. “But preventing incidents is far more compelling at our scale.”

## Bringing system-level context to code review with Codex

Effective code review at Datadog traditionally relied heavily on senior engineers—the people who understand the codebase, its history, and the architectural tradeoffs well enough to spot systemic risk.

But that kind of deep context is hard to scale, and early AI code review tools didn’t solve this problem; many behaved like advanced linters, flagging surface-level issues while missing broader system nuances. Datadog’s engineers often found the suggestions too shallow or too noisy, and ignored them.

Datadog began piloting Codex, the coding agent from OpenAI, by integrating it into the live development workflows. In one of the company’s largest and most heavily used repositories, every pull request was automatically reviewed by Codex. Engineers reacted to comments from Codex with thumbs up or down and shared informal feedback across teams. Many noted that the Codex feedback was worth reading, unlike previous tools that produced noisy or shallow suggestions.

## Validating AI review against real incidents

To test whether AI‑assisted review could do more than point out style issues, Datadog built an incident replay harness.

Instead of using hypothetical scenarios, the team went back to historical incidents. They reconstructed pull requests that had contributed to incidents, ran Codex against each one as if it were part of the original review, then asked the engineers who owned those incidents whether feedback from Codex would have made a difference.

The result: Codex found more than 10 cases, or roughly **22%** **of the incidents** that Datadog examined, where engineers confirmed that the feedback Codex provided would have made a difference—more than any other tool evaluated.

Because these pull requests had already passed code review, the replay test showed that Codex surfaced risks reviewers hadn’t seen at the time, complementing human judgment rather than replacing it.

## Delivering consistent, high-signal feedback

Datadog’s analysis showed that Codex consistently flagged issues that aren’t obvious from the immediate diff alone and can’t be caught by deterministic rules.

Engineers described Codex comments as more than “bot noise”:

* Codex pointed out interactions with modules not touched in the diff
* It identified missing test coverage in areas of cross‑service coupling
* It highlighted API contract changes that carried downstream risk

> “For me, a Codex comment feels like the smartest engineer I’ve worked with and who has infinite time to find bugs. It sees connections my brain doesn’t hold all at once.”

—Brad Carter, Engineering Manager at Datadog

That ability to connect review feedback to real reliability outcomes was what made Codex stand out in Datadog’s evaluation. Unlike static analysis tools, Codex compares the intent of the pull request with submitted code changes, reasoning over the entire codebase and dependencies to execute code and tests to validate behavior.

“It was the first one that actually seemed to consider the diff in the larger context of the program,” says Carter. “That was novel and eye‑opening.”  
  
For many engineers, that shift changed how they engaged with AI review altogether. “I started treating Codex comments like real code review feedback,” says Ted Wexler, Senior Software Engineer at Datadog. “Not something I’d skim or ignore, but something worth paying attention to.”

## Focusing engineers on design over detection

Following the evaluation, Datadog deployed Codex more broadly across its engineering workforce. Today **more than 1,000 engineers** use it regularly.

Feedback is largely surfaced organically rather than through formal in‑tool metrics. Engineers post to Slack about useful insights, constructive comments, and moments where Codex helped them think differently about a problem.

While time savings are significant, teams consistently pointed to a more meaningful shift in how work got done.

> “Codex changed my mind for what code review should be. It’s not about replicating our best human reviewers. It's about finding critical flaws and edge cases that humans struggle to see when reviewing changes in isolation.”

—Brad Carter, Engineering Manager at Datadog

## Redefining code review around risk, not speed

The broader impact for Datadog was a change in how code review itself is defined. Rather than treating review as a checkpoint for catching errors or optimizing cycle time, the team now sees Codex as a core reliability system that acts as a partner:

* Surfacing risk beyond what individual reviewers can hold in context
* Highlighting cross-module and cross-service interactions
* Increasing confidence in shipping at scale
* Allowing human reviewers to focus on architecture and design

This shift aligns with how Datadog’s leaders frame engineering priorities, where reliability and trust matter as much as, if not more than, velocity.

“We are the platform companies rely on when everything else is breaking,” says Carter. “Preventing incidents strengthens the trust our customers place in us.”

## Keep reading

![How agents are transforming work > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7hmtkjKv0DxS4Yt8mQZju2/c168bfa2010da64bcc9dd60d6b5491e8/Art_Card__1_.png?w=3840&q=90&fm=webp)

[How agents are transforming work

CompanyJun 25, 2026](/index/how-agents-are-transforming-work/)

![OpenAI and Broadcom Jalapeño inference chip card image](https://images.ctfassets.net/kftzwdyauwt9/21KcazqOHUF7Cq71Hpfcnc/81ad98a1978845b441ab14e008168c75/openai-broadcom-jalapeno-inference-chip-image-1_1.png?w=3840&q=90&fm=webp)

[OpenAI and Broadcom unveil LLM-optimized inference chip

CompanyJun 24, 2026](/index/openai-broadcom-jalapeno-inference-chip/)

![Helping build shared standards for advanced AI - card image](https://images.ctfassets.net/kftzwdyauwt9/3tqr0Vb3JnK38uBRBw7FAF/a3989888ee148ba286b834076aaa289b/helping-build-shared-standards-for-advanced-ai-1_1.png?w=3840&q=90&fm=webp)

[Helping build shared standards for advanced AI

Global AffairsJun 23, 2026](/index/helping-build-shared-standards-for-advanced-ai/)
