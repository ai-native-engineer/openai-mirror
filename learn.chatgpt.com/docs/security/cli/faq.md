<!-- source: https://learn.chatgpt.com/docs/security/cli/faq -->

Find answers to common questions about scanning repositories and managing
security findings from the terminal. For installation and a first scan, start
with the [CLI quickstart](/codex/security/cli).

## Repository scans

### Who can use the CLI

The Codex Security CLI and SDK are in limited beta. Approved customers and
partners receive installation instructions with their access. Contact your
account team if you need access.

### How does bulk repository scanning work

Sign in with GitHub CLI:

Discover and select repositories from a GitHub account or organization:

For a prepared list, provide a repository CSV and an output directory:

See [Run bulk security scans](/codex/security/cli/bulk-scans) for GitHub
discovery, the CSV format, campaign results, and available options.

### Can an interrupted bulk scan resume

Yes. Run the same bulk-scan command with the original CSV and output directory.
Codex Security skips completed repositories when their recorded scan artifacts
remain intact.

Add `--max-attempts 3` to retry temporary repository or scan errors:

  --workers 4 \
  --max-attempts 3

### How can a scan use architecture and security policies

Pass architecture documents, threat models, or security policies with
`--knowledge-base`:

npx codex-security scan . \

Codex Security uses these documents as context for the current scan. For
supported file types and directory behavior, see [Add security
context](/codex/security/cli/reference#add-security-context).

## Findings and coverage

### Where can teams find earlier scan results

List saved scans for your repository:

npx codex-security scans list /path/to/repository

Use a scan ID from the results to inspect its findings:

Each completed scan keeps its report, findings, coverage, and supporting
artifacts together. See [Scan
artifacts](/codex/security/cli/reference#scan-artifacts) for the full layout.

### How do scans distinguish new and known findings

Match findings that share a root cause across the two scans:

Compare the matched findings:

The comparison identifies new, persisting, reopened, resolved, and unknown
findings. A finding counts as resolved only when the later scan covers its
original target and affected path without coverage gaps.

### How does false-positive feedback work

Inspect the saved scan to find the occurrence ID:

Record why that finding doesn’t apply:

npx codex-security findings mark-false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

Future scans of the same repository receive that explanation as context. They
still independently check the current source, controls, and reachability. A
dismissal doesn’t suppress a rule, path, or vulnerability class.

For command details, see the [findings
reference](/codex/security/cli/reference#codex-security-findings).

### Why can repeat scans return different findings

AI-assisted scans can vary, even with the same scan configuration. Start by
rerunning your baseline scan:

npx codex-security scans rerun BASELINE_SCAN_ID

Match the baseline findings to the new scan:

npx codex-security scans match BASELINE_SCAN_ID REPEAT_SCAN_ID

Compare the matched results:

npx codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

Provide shared architecture and security guidance when missing context may
contribute to the variation. Matching can identify the same underlying finding
across runs, but it doesn’t make scans deterministic. Directly recheck any
important finding that disappears.

### How can a team confirm that a fix worked

After applying a fix, rerun the original scan:

npx codex-security scans rerun BEFORE_SCAN_ID

Match the original findings to the new scan:

npx codex-security scans match BEFORE_SCAN_ID AFTER_SCAN_ID

Compare the matched findings:

npx codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

Confirm that the new scan covers the original target and affected path without
coverage gaps. Then directly recheck the original finding against the current
checkout:

npx codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

A missing finding or scan comparison alone doesn’t prove that a fix worked.

### What does incomplete coverage mean

Coverage can be `complete`, `partial`, or `unknown`. Review `coverage.json`
for excluded paths, deferred surfaces, and open questions before treating a
scan as evidence of review.

Scans with partial or unknown coverage return exit code `2`, even without a
severity policy. They still keep any available findings and coverage. A later
scan can’t establish that an earlier finding no longer exists when it doesn’t
cover that finding’s original path.

## Automation and cost

### How do scan cost limits work

Set an estimated cost limit in USD before starting the scan:

npx codex-security scan . --max-cost 5

The limit is an estimate, not a hard spending cap. Requests already in
progress can finish above the limit. Codex Security keeps available results
when the scan stops.

### Can scans check commits and pull requests

Install a pre-commit security check for staged and unstaged changes:

For pull-request checks, scan the committed changes and set a severity
threshold:

npx codex-security scan . \
  --fail-on-severity high

A complete scan returns exit code `1` when it finds an issue at or above the
selected severity. See [Run scans in CI](/codex/security/cli/ci) for the
complete GitHub Actions workflow, artifact handling, and SARIF export.

### Can another application run scans directly

Yes. Use the [TypeScript SDK](/codex/security/sdk) to start scans, select
targets, inspect findings and coverage, track progress, and apply cost controls
from an application or developer tool.
