<!-- source: https://developers.openai.com/api/docs/guides/trace-grading/ -->

Trace grading is the process of assigning structured scores or labels to an agent’s trace—the end-to-end log of decisions, tool calls, and reasoning steps—to assess correctness, quality, or adherence to expectations. These annotations help identify where the agent did well or made mistakes, enabling targeted improvements in orchestration or behavior.

Trace evals use those graded traces to systematically evaluate agent performance across many examples, helping to benchmark changes, identify regressions, or validate improvements. Unlike black-box evaluations, trace evals provide more data to better understand why an agent succeeds or fails.

Use both features to track, analyze, and optimize the performance of groups of agents.

## Get started with traces

1. In the dashboard, navigate to Logs > [Traces](https://platform.openai.com/logs?api=traces).
2. Select a workflow. You’ll see traces from SDK-based apps, and from existing [Agent Builder](/api/docs/guides/agent-builder) workflows during the transition window.
3. Select a trace to inspect your workflow.
4. Create a grader, and run it to grade your agents’ performance against grader criteria.

Trace grading is a valuable tool for error identification at scale, which is critical for building resilience into your AI applications. Learn more about our recommended process in our [cookbook](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel).

## Evaluate traces with runs

1. Select **Grade all**. This takes you to the evaluation dashboard.
2. In the evaluation dashboard, add and edit test criteria.
3. Add a run to evaluate outputs. You can configure run options like model, date range, and tool calls to get more specificity in your eval.

Learn more about how you can use evals [here](/api/docs/guides/evals).
