# GitHub Copilot CLI Autopilot Risk Matrix for Power Platform - Practical AI, Copilot & Modern Development Insights

Estimated reading time: 19 minutes

A practical framework for Power Platform architects and developers navigating autonomous agentic workflows

## Table of contents

-   [Why This Question Matters Now](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-why-this-question-matters-now)

-   [What Autopilot Mode Actually Does](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-what-autopilot-mode-actually-does)
-   [The Core Governance Concepts You Need](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-the-core-governance-concepts-you-need)

-   [Calculating the Two Axes](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-calculating-the-two-axes)
    -   [Reversibility Score (R)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-reversibility-score-r)
    -   [Blast Radius Score (B)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-blast-radius-score-b)
    -   [Combined Autopilot Safety Score (S)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-combined-autopilot-safety-score-s)
    -   [Full PAC CLI Scoring Reference](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-full-pac-cli-scoring-reference)
-   [The Power Platform Risk Decision Matrix](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-the-power-platform-risk-decision-matrix)
    -   [Zone 1 — Green: Full Autopilot Permitted (S = 2.5–3.0)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-zone-1-green-full-autopilot-permitted-s-2-5-3-0)
    -   [Zone 2 — Yellow: Autopilot with Pre-Approved Scope (S = 1.8–2.4)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-zone-2-yellow-autopilot-with-pre-approved-scope-s-1-8-2-4)
    -   [Zone 3 — Orange: Plan Mode Required, No Autopilot (S = 1.2–1.7)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-zone-3-orange-plan-mode-required-no-autopilot-s-1-2-1-7)
    -   [Zone 4 — Red: No Agentic Execution — Human Only (S = 1.0–1.1)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-zone-4-red-no-agentic-execution-human-only-s-1-0-1-1)
-   [Building Your AGENTS.md for Power Platform Work](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-building-your-agents-md-for-power-platform-work)

-   [The Autonomy Spectrum in Practice](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-the-autonomy-spectrum-in-practice)
-   [Monitoring and Audit: The Log Problem](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-monitoring-and-audit-the-log-problem)

-   [When Autopilot Is Actually the Right Choice](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-when-autopilot-is-actually-the-right-choice)
-   [Practical Implementation Checklist](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-practical-implementation-checklist)
    -   [Making the Score Drive the Hook Logic](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-making-the-score-drive-the-hook-logic)
    -   [What is GitHub Copilot CLI Autopilot mode?](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-what-is-github-copilot-cli-autopilot-mode)
    -   [What is AGENTS.md and how does it govern Autopilot?](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-what-is-agents-md-and-how-does-it-govern-autopilot)
    -   [Why is Autopilot mode risky for Power Platform specifically?](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-why-is-autopilot-mode-risky-for-power-platform-specifically)
    -   [What is the Autopilot Safety Score (S)?](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-what-is-the-autopilot-safety-score-s)
    -   [Can preToolUse hooks block dangerous PAC CLI commands automatically?](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-can-pretooluse-hooks-block-dangerous-pac-cli-commands-automatically)
-   [Related AIDevMe Articles](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-related-aidevme-articles)

-   [Conclusion](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-conclusion)
-   [References](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-references)
    -   [GitHub Copilot CLI — Official Documentation & Announcements](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-github-copilot-cli-official-documentation-amp-announcements)
    -   [Power Platform ALM & PAC CLI — Official Documentation](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-power-platform-alm-amp-pac-cli-official-documentation)
    -   [Agentic AI Governance Frameworks](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-agentic-ai-governance-frameworks)
    -   [Autonomy Spectrum & Risk Scoring Theory](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-autonomy-spectrum-amp-risk-scoring-theory)
    -   [Security & Compliance Context](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/#h-security-amp-compliance-context)

## Why This Question Matters Now

When [András Fördős](https://www.linkedin.com/in/andrasfordos/) dropped this question on a recent post, it hit the heart of something the entire Power Platform community is wrestling with right now:

> How should the risk decision matrix be created/managed for using the autopilot agentic mode, specifically in Power Platform context?

It’s not a theoretical concern. GitHub Copilot CLI reached General Availability on February 25, 2026, and with it came **Autopilot mode** — a hands-off execution model where Copilot carries a task forward from start to finish without waiting for your approval at each step. Press `Shift+Tab` to cycle in, and the agent executes tools, runs commands, modifies files, and iterates until it declares the job done — or until you press `Ctrl+C`.

For general software development, this is powerful and mostly safe. For **Power Platform**, it’s a different conversation entirely. The blast radius of a misconfigured `pac solution import` or an unintended environment deletion is orders of magnitude larger than a broken unit test or a reformatted TypeScript file.

This article builds a practical risk decision matrix specifically for Power Platform practitioners. It draws on the latest agentic governance frameworks (Singapore IMDA, UC Berkeley, AWS) and maps them to the actual PAC CLI operations, Dataverse concepts, and ALM patterns you work with every day.

---

## What Autopilot Mode Actually Does

Before designing a risk framework, we need to understand what we’re governing.

In standard interactive mode, Copilot CLI follows a request-response loop: you prompt, it responds, you approve or redirect. In **Autopilot mode**, this loop disappears. The agent:

-   Executes tools and terminal commands autonomously.

-   Self-heals errors by retrying with different approaches.
-   Chains multiple operations without surfacing intermediate results for approval.

-   Continues until a built-in **maximum continuation limit** is reached (configurable), or until it determines the task is complete

GitHub’s own documentation is clear about the intended use case: *“Autopilot is particularly suited for well-defined tasks like writing tests, refactoring files, or fixing CI failures.”* The `/allow-all` command (alias `/yolo`) grants full permission across all tool types during a session.

The cost dimension matters too. Each autonomous continuation step consumes premium requests based on the active model’s multiplier — without your direct involvement in triggering them.

For Power Platform work, the key technical implication is this: **PAC CLI operations can be irreversible.** A `pac solution import` into production, a `pac env delete`, or a `pac admin application list` followed by a permission grant — these are not the same as overwriting a TypeScript file. The Dataverse platform does not have a global undo.

---

## The Core Governance Concepts You Need

Three concepts from the emerging agentic AI governance literature map directly to the Power Platform problem:

**Agency vs. Autonomy**: Agency is *what* the agent can do — the tools and systems it can touch. Autonomy is *how independently* it acts. You can have high agency (full PAC CLI access, Dataverse admin rights) with low autonomy (approval required at each step), or the reverse. In Autopilot mode, you’re cranking up autonomy. The risk framework is about controlling agency as compensation.

**Action-Space Bounding**: Singapore’s Model AI Governance Framework for Agentic AI (released January 2026) makes this the first pillar of agentic risk management — *assess and bound the agent’s action-space before deployment*. In practice: what PAC CLI commands is the agent allowed to run? What environments can it reach? What Dataverse tables can it touch?

**Reversibility as the Primary Risk Axis**: The most operationally useful way to classify Power Platform operations isn’t by feature area or complexity — it’s by **whether the operation can be undone**. This becomes the primary dimension of the risk matrix.

---

## Calculating the Two Axes

The risk matrix rests on two scored dimensions. Rather than applying them as gut-feel labels, each can be calculated from four sub-factors scored 1–3, then combined into an **Autopilot Safety Score (S)**. This makes the classification repeatable, team-shareable, and auditable — a scored table in your repo rather than a judgment call in someone’s head.

### Reversibility Score (R)

**Rate each sub-factor 1–3, then take the average. Higher = more reversible = safer for autopilot.**

| **Sub-factor** | **1 — Hard to reverse** | **2 — Partial** | **3 — Easy to reverse** |
| **Data loss risk** | Permanent data deletion possible | Recoverable from backup only | No data touched |
| **Rollback path** | No rollback mechanism exists | Manual restore required (30–60 min) | Automated rollback / re-import (< 5 min) |
| **Time to recover** | Hours or days | 30–60 minutes | Under 5 minutes |
| **Scope of change** | Live schema change (tables/columns) | Config or settings change | Artifact only — local filesystem or source control |

**R = average of the 4 sub-factors → range 1.0–3.0**

---

### Blast Radius Score (B)

**Rate each sub-factor 1–3, then take the average. Higher = more contained = safer for autopilot.**

| **Sub-factor** | **1 — Wide impact** | **2 — Moderate** | **3 — Contained** |
| **Environments affected** | Production (live users) | Test / UAT | Dev or local only |
| **User count at risk** | Hundreds or more | Tens of users | Zero — developer only |
| **Business processes at risk** | Mission-critical flows or plugins | Supporting or non-critical processes | No business process dependency |
| **Security boundary crossed** | Tenant-level or security role change | Environment-level permission change | No permission change |

**B = average of the 4 sub-factors → range 1.0–3.0**

---

### Combined Autopilot Safety Score (S)

Markdown

```
S = (R × 0.6) + (B × 0.4)
```

Reversibility carries the higher weight because an unrecoverable action in a contained scope is worse than a recoverable action with wider reach. A broken production environment that cannot be restored in under an hour is a business incident regardless of how few users triggered it.

| **S range** | **Zone** | **Autopilot posture** |
| **2.5 – 3.0** | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) Green | Full Autopilot permitted |
| **1.8 – 2.4** | ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) Yellow | Autopilot with AGENTS.md scope constraints |
| **1.2 – 1.7** | ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg) Orange | Plan Mode only — no autonomous execution |
| **1.0 – 1.1** | ![🔴](https://s.w.org/images/core/emoji/17.0.2/svg/1f534.svg) Red | Human only — agent forbidden from executing |

---

### Full PAC CLI Scoring Reference

The table below scores every operation discussed in this article. Use it as a starting point; adjust R and B sub-factor scores to reflect your specific environment topology (for example, a TEST environment with 50 integration partners consuming it scores lower on B than a clean isolated sandbox).

| **Operation** | **R** | **B** | **S** | **Zone** |
| `pac solution pack` (local) | 3.0 | 3.0 | 3.0 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) |
| `pac solution unpack` (local) | 3.0 | 3.0 | 3.0 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) |
| `pac solution check` (read-only) | 3.0 | 3.0 | 3.0 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) |
| `pac solution list` / `pac env list` | 3.0 | 3.0 | 3.0 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) |
| `pac modelbuilder build` | 3.0 | 3.0 | 3.0 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) |
| `pac pcf init` / `npm run build` | 3.0 | 3.0 | 3.0 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) |
| `pac solution export` from DEV | 2.75 | 2.75 | 2.75 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) |
| `pac solution import` to DEV | 2.5 | 2.5 | 2.5 | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) / ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) |
| `pac solution import` to TEST | 2.25 | 2.0 | 2.15 | ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) |
| `pac solution upgrade` on TEST | 2.0 | 2.0 | 2.0 | ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) |
| `pac admin environment create` (sandbox) | 2.5 | 2.25 | 2.4 | ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) |
| `pac admin user assign-role` on TEST | 2.0 | 2.0 | 2.0 | ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) |
| `pac solution import` to PRODUCTION | 1.5 | 1.25 | 1.4 | ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg) |
| Schema-change solution (column delete) | 1.25 | 1.5 | 1.35 | ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg) |
| `pac admin environment reset` (sandbox) | 1.5 | 1.75 | 1.6 | ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg) |
| Modify connection references (prod) | 1.5 | 1.5 | 1.5 | ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg) |
| `pac admin user assign-role` on PROD | 1.5 | 1.25 | 1.4 | ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg) |
| Tenant-level DLP policy change | 1.25 | 1.0 | 1.15 | ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg) / ![🔴](https://s.w.org/images/core/emoji/17.0.2/svg/1f534.svg) |
| `pac admin environment delete` | 1.0 | 1.0 | 1.0 | ![🔴](https://s.w.org/images/core/emoji/17.0.2/svg/1f534.svg) |
| `pac solution delete` on PROD | 1.0 | 1.0 | 1.0 | ![🔴](https://s.w.org/images/core/emoji/17.0.2/svg/1f534.svg) |
| Dataverse audit/retention policy change | 1.0 | 1.0 | 1.0 | ![🔴](https://s.w.org/images/core/emoji/17.0.2/svg/1f534.svg) |
| Disable all flows in production | 1.0 | 1.0 | 1.0 | ![🔴](https://s.w.org/images/core/emoji/17.0.2/svg/1f534.svg) |

**How to use this table in practice**: Score at planning time, not runtime. When you add a new PAC CLI operation to a workflow, score it before you write the pipeline. This forces the conversation about blast radius early, not after something breaks. Re-score when context changes — a TEST environment with live integration partners drops in B score and may move from ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) to ![🟠](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e0.svg). Add the scored table to your wiki or directly to `AGENTS.md` so the hook logic and the documentation share a single source of truth.

---

## The Power Platform Risk Decision Matrix

With scores established, the four zones and their corresponding Autopilot postures follow directly:

### Zone 1 — Green: Full Autopilot Permitted (S = 2.5–3.0)

**Reversible + Contained Blast Radius**

These are operations you can confidently hand to Autopilot mode. Mistakes are recoverable, and the scope of impact is limited.

| **Operation** | **PAC CLI Command** | **Why It’s Safe** |
| Pack a solution from source | `pac solution pack` | Local filesystem only, no environment contact |
| Unpack solution to source control | `pac solution unpack` | Local filesystem, source control is the safety net |
| Export unmanaged solution from DEV | `pac solution export` | Read-only against DEV; artifact stored locally |
| Run Solution Checker | `pac solution check` | Read-only analysis, no mutations |
| Generate TypeScript definitions | `pac modelbuilder build` | Local codegen, no environment writes |
| PCF build and test loop | `pac pcf init`, `npm run build` | Local compilation only |
| List environments, solutions, auth profiles | `pac env list`, `pac solution list` | Read-only queries |
| Create/update AGENTS.md and agent skills | File system writes | Source-controlled, version history preserved |

**Autopilot Posture**: ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Permit — no approval gates required. These are the ideal tasks for Copilot CLI’s `--allow-all-tools` flag in scripted CI workflows.

---

### Zone 2 — Yellow: Autopilot with Pre-Approved Scope (S = 1.8–2.4)

**Reversible + Moderate Blast Radius (non-production environments)**

These operations mutate environment state, but in environments where rollback paths exist: you can re-import a previous solution version, restore from backup, or reset the environment.

| **Operation** | **PAC CLI Command** | **Condition for Autopilot** |
| Import managed solution to DEV/TEST | `pac solution import` | Target environment explicitly scoped in AGENTS.md |
| Apply solution upgrade | `pac solution upgrade` | Non-production only; backup verified |
| Create TEST or sandbox environment | `pac admin environment create` | Environment type = Sandbox, not Production |
| Assign security roles | `pac admin user assign-role` | Non-production only; role list pre-approved |
| Publish customizations | `pac solution publish` | Non-production only |
| Run Power Apps Checker with auto-fix | `pac solution check --fix` | Scoped to local files, not live environment |

**Autopilot Posture**: Conditional — define the permitted action-space explicitly in `AGENTS.md`. Example constraint:

Markdown

```


## Scope Constraints
- PAC CLI import operations are permitted ONLY against environments matching the pattern: `*-dev-*` or `*-test-*`

- Production environment URLs must never appear in any pac command
- All solution imports must use `--async` and `--activate-plugins false` on first pass
```

---

### Zone 3 — Orange: Plan Mode Required, No Autopilot (S = 1.2–1.7)

**Partially Reversible + High Blast Radius**

These operations affect production systems or have limited rollback paths. A mistake requires human-led recovery, not agent-led recovery. GitHub Copilot CLI’s **Plan mode** (`Shift+Tab` before autopilot) is the correct posture here — the agent outlines exactly what it will do, and you review the plan before any execution starts.

| **Operation** | **PAC CLI Command** | **Why Human Review Is Required** |
| Import managed solution to PRODUCTION | `pac solution import` (prod target) | Production user impact; rollback = complex solution restore |
| Delete a Dataverse table column | Schema change via solution | Data loss risk; irreversible once data is purged |
| Reset a sandbox environment | `pac admin environment reset` | Full data wipe; audit trail destroyed |
| Modify connection references | Post-import configuration | Can break all flows consuming the reference |
| Grant System Administrator role | `pac admin user assign-role` | Security boundary breach if misconfigured |
| Set tenant-level DLP policies | `pac admin connector` | Affects all environments in tenant |

**Autopilot Posture**: ![🛑](https://s.w.org/images/core/emoji/17.0.2/svg/1f6d1.svg) Block — enforce via `preToolUse` hook in Copilot CLI. When the agent attempts a PAC command targeting a production URL, the hook fires, denies the tool call, and surfaces a human approval request. Example hook pattern:

JavaScript

```
// preToolUse hook: block-prod-deploy.js
export function preToolUse({ tool, input }) {
  if (tool === 'shell' && input.command.includes('pac solution import')) {
    const isProd = /crm\.dynamics\.com/.test(input.command) &&
                   !/(dev|test|sandbox)/.test(input.command);
    if (isProd) {
      return { deny: true, reason: 'Production deployment requires human approval gate.' };
    }
  }
}
```

---

### Zone 4 — Red: No Agentic Execution — Human Only (S = 1.0–1.1)

**Irreversible + Maximum Blast Radius**

These are operations where the consequences of an agentic error are catastrophic and non-recoverable. No mode of Copilot CLI — autopilot or interactive — should be permitted to execute these directly. They require explicit human initiation with a separate approval chain.

| **Operation** | **PAC CLI Command** | **Why It’s Red** |
| Delete a production environment | `pac admin environment delete` | Permanent; all data, flows, apps gone |
| Delete a managed solution from production | `pac solution delete` | Cascading deletions across dependent components |
| Revoke system-wide app registrations | Azure AD / admin portal | Identity plane breach |
| Modify Dataverse auditing/retention policies | Admin API | Compliance and legal exposure |
| Disable all active flows in production | Power Automate admin | Business process disruption |
| Export with sensitive data to uncontrolled location | `pac solution export` (prod + sensitive tables) | Data exfiltration risk |

**Autopilot Posture**: ![🚫](https://s.w.org/images/core/emoji/17.0.2/svg/1f6ab.svg) Never — these should be absent from the agent’s tool permissions entirely. In `AGENTS.md`, explicitly exclude these commands:

Markdown

```


## Forbidden Operations
The agent must NEVER execute:
- `pac admin environment delete`

- `pac solution delete` against production environments
- Any command that includes `--environment` referencing a production URL

- Any command that modifies DLP policies or tenant settings
```

---

## Building Your AGENTS.md for Power Platform Work

The `AGENTS.md` file is Copilot CLI’s mechanism for defining agent-level instructions. It’s the primary lever for implementing the risk matrix above. Here’s a practical template for a Power Platform repository:

Markdown

```


# AGENTS.md — Power Platform ALM Agent Instructions

## Identity and Scope
This agent assists with Power Platform ALM tasks in this repository.
It operates against the following environments:
- DEV: https://org-dev.crm4.dynamics.com

- TEST: https://org-test.crm4.dynamics.com
- PRODUCTION: READ-ONLY — no deployments, no mutations

## Permitted Operations
- pac solution pack / unpack / check

- pac solution export from DEV only
- pac solution import to DEV or TEST only

- pac pcf init / build / push
- pac modelbuilder build

- pac env list / pac solution list (any environment, read-only)

## Forbidden Operations
- pac solution import targeting production

- pac admin environment delete / reset
- pac solution delete (any environment)

- pac admin user assign-role in production
- Any operation that modifies DLP or tenant settings

- The /yolo or /allow-all commands are not to be used

## Human Approval Required For
- Any import to TEST (notify team lead via GitHub issue comment)

- Any schema-change solution (tables/columns added or removed)
- Any security role assignment

## Error Handling
On import failure, do NOT auto-retry with different parameters.
Surface the error and await human instruction.

## Blast Radius Awareness
Before any pac solution import, state:
1. Target environment
2. Solution version being deployed
3. Whether this is a managed or unmanaged import
4. Estimated impact (apps, flows, plugins affected)
```

---

## The Autonomy Spectrum in Practice

The governance literature describes autonomy not as a binary switch but as a spectrum. Industry frameworks propose four bands that map cleanly to Power Platform work:

| **Band** | **Agent Behavior** | **Power Platform Example** |
| Observe | Monitors, logs, surfaces insights | Copilot CLI analyzes solution for checker violations, reports findings |
| Recommend | Proposes actions, explains trade-offs | Copilot CLI drafts the `pac solution import` command, explains flags, awaits approval |
| Decide | Selects action within policy bounds; human executes | Copilot CLI selects correct connection reference values, presents final command for human to run |
| Act | Decides and executes within defined thresholds | Copilot CLI runs full DEV export + unpack + commit pipeline autonomously |

The risk matrix above tells you which autonomy band is appropriate per operation type. Zone 1 operations can reach **Act**. Zone 2 can reach **Decide** (or **Act** with strong AGENTS.md constraints). Zone 3 should stay at **Recommend**. Zone 4 is **Observe** only — no execution authority whatsoever.

A mature Power Platform team will encode these band assignments in their `AGENTS.md` and evolve them over time as trust and tooling mature. Autonomy expands naturally as trust, controls, and outcomes mature.

---

## Monitoring and Audit: The Log Problem

The scariest failures are the ones you can’t reconstruct, because you didn’t log the workflow. McKinsey’s research on agentic risk makes this a first-principle concern.

For Power Platform + Copilot CLI, this means:

**Copilot CLI session logs**: Enable `postToolUse` hooks to write structured logs of every PAC CLI command executed during an agent session. Include timestamp, command, target environment URL, and success/failure status.

**Dataverse audit logs**: Ensure solution imports and environment changes are captured in the Power Platform Admin Center audit trail. This is separate from the agent’s own logs and provides an independent record.

**GitHub Actions integration**: When running Copilot CLI in CI/CD pipelines (headless mode: `copilot --allow-all-tools -p "Export DEV solution and commit"`), the GitHub Actions run log provides the authoritative record. Map session IDs between CLI logs and Actions runs.

**Solution version pinning**: Before any import, log the current solution version in the target environment. This creates a recovery baseline — if an automated import breaks something, you know exactly what version to roll back to.

---

## When Autopilot Is Actually the Right Choice

This article has focused heavily on constraints, but it’s worth stating clearly: **Autopilot mode is genuinely valuable for Power Platform work when scoped correctly.** The following scenarios are ideal:

**Full ALM pipeline automation (DEV only)**: “Export the current solution from DEV, unpack it to the `solutions/` folder, run Solution Checker, and open a PR with the results.” This is a four-step, well-defined, fully reversible workflow. Autopilot handles it without interruption, and the PR gives you human review before anything goes further.

**PCF control scaffolding and build loop**: “Initialize a new PCF control called `AgentBridge`, configure it for virtual dataset, add the React and Fluent UI dependencies, and run the initial build.” Entirely local, fast, and recoverable.

**AGENTS.md and agent skill generation**: “Analyze this repository’s solution structure and generate an AGENTS.md with appropriate scope constraints for our three-environment setup.” The output is a text file you review before committing — low risk, high value.

**Solution Checker automation in CI**: Running `pac solution check` and parsing results as part of a PR gate is a perfect headless autopilot use case. No environment mutations, deterministic output, CI log as audit trail.

The pattern: **Autopilot excels at well-scoped, read-heavy, or locally-scoped tasks where the worst outcome is a failed pipeline run, not a broken production environment.**

---

## Practical Implementation Checklist

Use this as your starting point when onboarding GitHub Copilot CLI Autopilot for a Power Platform project:

-   **Define environment URL allowlist** in `AGENTS.md` — production URLs explicitly excluded from mutation commands

-   **Classify every PAC CLI command** used in your project against the four-zone matrix above
-   **Implement `preToolUse` hooks** to enforce Zone 3 and Zone 4 boundaries programmatically

-   **Configure `--max-continuations`** to limit runaway autopilot sessions in CI (recommended: 20 for ALM tasks)
-   **Enable PAC CLI verbose logging** (`pac --log-level info`) and capture to session artifact in GitHub Actions

-   **Run Autopilot in Plan mode first** for any new workflow — review the plan, then execute
-   **Document your team’s autonomy band assignments** per operation type and review quarterly

-   **Test Autopilot in DEV before allowing it in TEST** — validate it respects AGENTS.md constraints
-   **Never use `/yolo` in shared or CI contexts** — it overrides all permission constraints for the session

---

### Making the Score Drive the Hook Logic

Once you have a scored operation table, your `preToolUse` hook can enforce boundaries dynamically rather than through hardcoded command lists. Store the scores in a JSON sidecar file (`pac-risk-scores.json`) and load it at hook evaluation time:

**Original design — not yet in official documentation.** The `preToolUse` and `postToolUse` hook mechanism is real and part of the GitHub Copilot CLI GA release. However, the specific pattern below — loading a JSON risk-score table at hook evaluation time to drive zone enforcement dynamically — is an original architecture proposed here. GitHub and Microsoft do not currently document this combination. Treat it as a validated starting point for your own implementation, not a prescribed practice. If you build on it, test thoroughly in a DEV-only context before applying to shared or CI environments.

**Where `pac-risk-scores.json` is the scored table from this article, serialised:**

JSON

```
[
  { "command": "pac solution pack",   "R": 3.0, "B": 3.0, "S": 3.0, "zone": "" },
  { "command": "pac solution import", "R": 1.5, "B": 1.25, "S": 1.4, "zone": "", "note": "prod — override R/B for DEV/TEST contexts" },
  { "command": "pac admin environment delete", "R": 1.0, "B": 1.0, "S": 1.0, "zone": "" }
]
```

This keeps the enforcement logic thin and the risk decisions in data — versioned in source control, reviewable in PRs, and adjustable without touching hook code.

---

## Frequently Asked Questions

### What is GitHub Copilot CLI Autopilot mode?

Autopilot mode is a fully autonomous execution mode in GitHub Copilot CLI (GA February 25, 2026). Once you submit an initial prompt, the agent executes tools, runs terminal commands, edits files, and iterates through errors without asking for your approval at each step. You switch into it by pressing `Shift+Tab` during an interactive session.

### What is AGENTS.md and how does it govern Autopilot?

`AGENTS.md` is a Markdown file placed in your repository that Copilot CLI reads as agent-level instructions. It defines which PAC CLI operations are permitted, which environments the agent can target, what requires human approval, and how to handle errors. It is the primary mechanism for bounding the agent’s action-space in a Power Platform ALM context.

### Why is Autopilot mode risky for Power Platform specifically?

Unlike general software development where a bad autonomous action overwrites a file you can restore from Git, many PAC CLI operations affect live Dataverse environments. A `pac solution import` to production, a `pac admin environment delete`, or a misconfigured security role assignment can cause data loss or business disruption with no automated rollback path.

### What is the Autopilot Safety Score (S)?

The Autopilot Safety Score is a numerical classification introduced in this article. It combines a Reversibility score (R) and a Blast Radius score (B) using the formula `S = (R × 0.6) + (B × 0.4)`, producing a value between 1.0 and 3.0. Scores above 2.5 permit full Autopilot; scores below 1.2 require human-only execution.

### Can preToolUse hooks block dangerous PAC CLI commands automatically?

**Yes** — Copilot CLI’s `preToolUse` hooks fire before any tool execution. A hook that detects a `pac solution import` targeting a production URL can deny the tool call and surface a human approval prompt. The hardcoded hook pattern in this article is fully supported by the GA release; the JSON sidecar scoring pattern is an original proposed architecture (see the callout in the checklist section).

## Related AIDevMe Articles

-   **[GitHub Copilot CLI: Complete Developer Guide for Power Platform, .NET, and TypeScript](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/)** — getting started guide, installation, and first ALM workflow

-   **[Stop Writing Vague AI Prompts: The Developer’s Playbook for Mastering agents.md in 2026](https://aidevme.com/agents-md-best-practices/)** — how to write agent instructions that actually work

---

## Conclusion

[András Fördős’s](https://www.linkedin.com/in/andrasfordos/) question points to one of the most important design decisions Power Platform teams will make in 2026: **how much decision-making authority do we hand to the agent, and where do we draw the hard lines?**

The answer isn’t “never use Autopilot” — that wastes the productivity gains the tooling was built to deliver. The answer is a deliberate risk decision matrix that maps the reversibility and blast radius of every operation type to an appropriate autonomy posture.

For Power Platform, the core principle is simple: **the agent’s autonomy ceiling must be inversely proportional to the operation’s irreversibility.** Pack, unpack, analyze, scaffold — full Autopilot. Deploy to production, delete environments, modify security boundaries — human only, always.

Encode this in `AGENTS.md`. Enforce it with `preToolUse` hooks. Log everything. And revisit the matrix as your team’s confidence and the tooling’s capabilities evolve together.

The practitioners who get this right early will have a significant edge — not because they’re moving faster, but because they’re moving faster *without breaking things*.

---

## References

The references below are annotated to be transparent about how each source was actually used.

### GitHub Copilot CLI — Official Documentation & Announcements

-   GitHub. *Allowing GitHub Copilot CLI to work autonomously (Autopilot mode).* GitHub Docs, 2026. **Directly cited** — source of the `Shift+Tab` cycle mechanic, `/allow-all` alias `/yolo`, the three permission options on entering autopilot, premium request cost behaviour, and the `--max-continuations` limit. [https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot)

-   GitHub. *GitHub Copilot CLI is now generally available.* GitHub Changelog, February 25, 2026. **Directly cited** — source of the GA date (February 25, 2026), the autopilot mode description, built-in specialised agents (Explore, Task, Code Review, Plan), background delegation with `&` prefix, and the `preToolUse`/`postToolUse` hooks existence. [https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/)
-   GitHub. *Using GitHub Copilot CLI.* GitHub Docs, 2026. **Directly cited** — source of the `AGENTS.md` custom instructions mechanism, custom agents, agent skills, and the `/resume` command for session continuity. [https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli)

-   GitHub. *GitHub Copilot CLI — Product page and FAQ.* GitHub Features, 2026. **Directly cited** — source for `Shift+Tab` cycling between Plan and Autopilot modes, `AGENTS.md` and Agent Skills descriptions, `/fleet` for subagent coordination, and the organisation policy inheritance statement. [https://github.com/features/copilot/cli](https://github.com/features/copilot/cli)
-   GitHub. *Power agentic workflows in your terminal with GitHub Copilot CLI.* GitHub Blog, January 29, 2026. **Background used** — confirmed the MCP server integration pattern and custom agent workflow described in the article; no unique claims drawn directly from it that are not also in refs 1–4. [https://github.blog/ai-and-ml/github-copilot/power-agentic-workflows-in-your-terminal-with-github-copilot-cli/](https://github.blog/ai-and-ml/github-copilot/power-agentic-workflows-in-your-terminal-with-github-copilot-cli/)

-   GitHub. *github/copilot-cli — Official repository and release notes.* GitHub, 2026. **Background used** — release notes confirmed autopilot behaviour details already covered by refs 1–2; no unique claims drawn from it. [https://github.com/github/copilot-cli](https://github.com/github/copilot-cli)
-   GitHub. *GitHub Copilot Introduces Agent Mode and Next Edit Suggestions.* GitHub Newsroom, February 6, 2025. **Background used** — provided historical context on the February 2025 Agent Mode announcement that preceded CLI GA; not explicitly cited in the article body. [https://github.com/newsroom/press-releases/agent-mode](https://github.com/newsroom/press-releases/agent-mode)

-   GitHub. *GitHub Copilot features overview.* GitHub Docs, 2026. **Background used** — cross-referenced feature descriptions for accuracy; no unique claims drawn from it that are not in refs 1–4. [https://docs.github.com/en/copilot/get-started/features](https://docs.github.com/en/copilot/get-started/features)

---

### Power Platform ALM & PAC CLI — Official Documentation

-   Microsoft. *PAC CLI — solution command group reference.* Microsoft Learn, 2026. **Directly cited** — authoritative source for every `pac solution` command name, flag syntax (`--async`, `--activate-plugins`, `--publish`), and behaviour described in the zone tables. [https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/solution](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/solution)

-   Microsoft. *GitHub Actions for Microsoft Power Platform.* Microsoft Learn, 2026. **Background used** — confirmed the GitHub Actions + PAC CLI ALM pattern context; the specific commands in the article come from the PAC CLI reference (ref 9) rather than this page. [https://learn.microsoft.com/en-us/power-platform/alm/devops-github-actions](https://learn.microsoft.com/en-us/power-platform/alm/devops-github-actions)
-   Microsoft. *Available GitHub Actions for Microsoft Power Platform.* Microsoft Learn, 2026. **Background used** — confirmed action names and deployment pipeline patterns; no unique claims drawn directly from it into the article body. [https://learn.microsoft.com/en-us/power-platform/alm/devops-github-available-actions](https://learn.microsoft.com/en-us/power-platform/alm/devops-github-available-actions)

-   Microsoft. *microsoft/powerplatform-actions — GitHub repository.* GitHub, 2026. **Background used** — cross-referenced action availability; not explicitly cited. [https://github.com/microsoft/powerplatform-actions](https://github.com/microsoft/powerplatform-actions)
-   Microsoft. *microsoft/power-platform-skills — Plugin marketplace for Claude Code / GitHub Copilot CLI.* GitHub, 2026. **Background used** — confirmed that Microsoft itself ships a Power Platform plugin for Copilot CLI with PAC CLI permission whitelisting (`Bash(pac *)`), validating the AGENTS.md and hook enforcement patterns proposed in this article. [https://github.com/microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)

---

### Agentic AI Governance Frameworks

-   Infocomm Media Development Authority (IMDA), Singapore. *Model AI Governance Framework for Agentic AI.* World Economic Forum, Davos, January 22, 2026. **Directly cited** — primary source for the action-space bounding concept, the four governance actions (assess/bound, human accountability, technical controls, gradual rollout), and the human-in-the-loop vs. human-on-the-loop distinction used in the article. [https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)

-   Davis Wright Tremaine LLP. *New Governance Frameworks Offer a Roadmap for Managing Risks Unique to Agentic AI.* AI Law Advisor Blog, January 2026. **Directly cited** — source for the agency vs. autonomy distinction as a governance concept, and the Singapore framework’s two key concepts (action-space and autonomy level) used in the Core Governance Concepts section. [https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/01/roadmap-for-managing-risks-unique-to-agentic-ai](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/01/roadmap-for-managing-risks-unique-to-agentic-ai)
-   Amazon Web Services. *The Agentic AI Security Scoping Matrix: A framework for securing autonomous AI systems.* AWS Security Blog, November 21, 2025. **Directly cited** — source for the formal definitions of agency (scope of permitted actions) vs. autonomy (degree of independent decision-making) used in the Core Governance Concepts section. [https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/)

-   Isenberg, R. & Rahilly, L. *Trust in the Age of Agents.* McKinsey Quarterly / The McKinsey Podcast, March 2026. **Directly cited** — source for the “scariest failures are the ones you can’t reconstruct because you didn’t log the workflow” framing in the Monitoring and Audit section, and the 80% risky behaviour statistic used in research (not quoted in article body but informed the audit section emphasis). [https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/trust-in-the-age-of-agents](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/trust-in-the-age-of-agents)
-   Madkour, N., Newman, J., Raman, D., Jackson, K., Murphy, E.R., Yuan, C. *Agentic AI Risk-Management Standards Profile.* UC Berkeley Center for Long-Term Cybersecurity, February 2026. **Background used** — confirmed the governance framing and reversibility-as-risk-axis thinking; the article cites Singapore IMDA and AWS as the primary framework sources rather than this document directly. [https://ppc.land/uc-berkeley-unveils-framework-as-ai-agents-threaten-to-outrun-oversight/](https://ppc.land/uc-berkeley-unveils-framework-as-ai-agents-threaten-to-outrun-oversight/)

-   Deloitte Insights. *Agentic AI Strategy.* Tech Trends 2026, December 2025. **Background used** — provided enterprise adoption context (only 11% in production) used during research to frame urgency; not explicitly cited in the article body. [https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html)

---

### Autonomy Spectrum & Risk Scoring Theory

-   Auf Fait Technologies. *AI Readiness in Industry 4.0: A 2026 AI Adoption Framework for Autonomous Work.* December 2, 2025. **Directly cited** — source for the four-band autonomy spectrum (Observe → Recommend → Decide → Act) used in The Autonomy Spectrum in Practice section. [https://aufaittechnologies.com/blog/ai-adoption-framework/](https://aufaittechnologies.com/blog/ai-adoption-framework/)

-   Kore.ai. *AI Agents in 2026: From Hype to Enterprise Reality.* February 2026. **Directly cited** — source for “autonomy expands naturally as trust, controls, and outcomes mature” and the risk-managed autonomy framing used in the Autonomy Spectrum section conclusion. [https://www.kore.ai/blog/ai-agents-in-2026-from-hype-to-enterprise-reality](https://www.kore.ai/blog/ai-agents-in-2026-from-hype-to-enterprise-reality)
-   Arsanjani, A. *AI in 2026: Predictions Mapped to the Agentic AI Maturity Model.* Medium, December 2025. **Background used** — provided maturity model framing that informed the zone progression concept; not explicitly cited in the article body. [https://dr-arsanjani.medium.com/ai-in-2026-predictions-mapped-to-the-agentic-ai-maturity-model-c6f851a40ef5](https://dr-arsanjani.medium.com/ai-in-2026-predictions-mapped-to-the-agentic-ai-maturity-model-c6f851a40ef5)

-   MachineLearningMastery.com / Chugani, V. *7 Agentic AI Trends to Watch in 2026.* January 5, 2026. **Background used** — “bounded autonomy architectures” framing confirmed the zone approach; not explicitly cited in the article body. [https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/](https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/)

---

### Security & Compliance Context

-   CSO Online. *Why 2025’s Agentic AI Boom Is a CISO’s Worst Nightmare.* February 2026. **Background used** — NIST AI RMF update with “circuit breaker” mandate informed the preToolUse hook enforcement concept; not explicitly cited in the article body. [https://www.csoonline.com/article/4132860/why-2025s-agentic-ai-boom-is-a-cisos-worst-nightmare.html](https://www.csoonline.com/article/4132860/why-2025s-agentic-ai-boom-is-a-cisos-worst-nightmare.html)

-   Palo Alto Networks. *2026 Predictions for Autonomous AI.* November 25, 2025. **Background used** — “autonomy with control” and insider threat framing informed the Zone 4 rationale; not explicitly cited in the article body. [https://www.paloaltonetworks.com/blog/2025/11/2026-predictions-for-autonomous-ai/](https://www.paloaltonetworks.com/blog/2025/11/2026-predictions-for-autonomous-ai/)

---

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/)