# GitHub Copilot Agentic Memory Power Platform

Estimated reading time: 19 minutes

GitHub Copilot just launched a persistent, repository-scoped agentic memory system in public preview. Instead of starting from scratch every session, Copilot now learns your codebase conventions over time and shares that knowledge across the coding agent, code review, and CLI. In this article, we explore how it works under the hood — and walk through three concrete Power Platform scenarios (PCF control development, Power Automate solution management, and Dataverse architecture patterns) where this changes the daily developer experience significantly.

## Table of contents

-   [The Stateless AI Problem Every Developer Knows](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-the-stateless-ai-problem-every-developer-knows)

-   [How Agentic Memory Works](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-how-agentic-memory-works)
-   [Under the Hood: JIT Verification and Citation-Based Storage](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-under-the-hood-jit-verification-and-citation-based-storage)

-   [Security and Privacy Model](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-security-and-privacy-model)
-   [Agentic Memory vs. Instruction Files: Full Comparison](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-agentic-memory-vs-instruction-files-full-comparison)
    -   [The Recommended Approach: Use Both Together](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-the-recommended-approach-use-both-together)
-   [Availability, Current Limits, and What’s Coming](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-availability-current-limits-and-what-s-coming)
    -   [What’s Available Now (Public Preview, January 2026)](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-what-s-available-now-public-preview-january-2026)
    -   [Current Limits to Be Aware Of](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-current-limits-to-be-aware-of)
    -   [What’s on the Roadmap](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-what-s-on-the-roadmap)
-   [The Four Learning Phases: How to Test and Validate the Impact](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-the-four-learning-phases-how-to-test-and-validate-the-impact)
    -   [Phase 1 — Baseline: Document Your Current Pain Points](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-phase-1-baseline-document-your-current-pain-points)
    -   [Phase 2 — Accumulation: Enable Memory and Work Normally](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-phase-2-accumulation-enable-memory-and-work-normally)
    -   [Phase 3 — Inspection: Read the Stored Memories Directly](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-phase-3-inspection-read-the-stored-memories-directly)
    -   [Phase 4 — Validation: Re-run Baselines and Controlled Violation Tests](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-phase-4-validation-re-run-baselines-and-controlled-violation-tests)
-   [Use Cases](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-use-cases)
    -   [Use Case 1 — PCF Control Development: Teaching Copilot Your Component Architecture](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-use-case-1-pcf-control-development-teaching-copilot-your-component-architecture)
    -   [Use Case 2 — Dataverse Plugin Development: Learning Your Plugin Architecture Patterns](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-use-case-2-dataverse-plugin-development-learning-your-plugin-architecture-patterns)
    -   [Use Case 3 — Solution Source Control: Teaching Copilot Your Unpacked Solution Conventions](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-use-case-3-solution-source-control-teaching-copilot-your-unpacked-solution-conventions)
-   [How to Enable Agentic Memory Right Now](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-how-to-enable-agentic-memory-right-now)

-   [What Comes Next: The Road Toward Knowledge Graphs](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-what-comes-next-the-road-toward-knowledge-graphs)
-   [Closing Thoughts](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-closing-thoughts)

-   [References and Further Reading](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/#h-references-and-further-reading)

## The Stateless AI Problem Every Developer Knows

If you have been using GitHub Copilot, you have experienced this frustration. You spend ten minutes explaining your project architecture, naming conventions, and preferred patterns to the AI. It generates great code. You close the editor. The next day you open a new file, and you are back to square one — Copilot has no idea what you explained yesterday.

This is not a Copilot-specific issue. It is a fundamental limitation of stateless AI systems. Every interaction is isolated. There is no continuity, no accumulated understanding of your codebase, and no knowledge transfer between different AI agents working on the same repository.

**GitHub’s answer to this is agentic memory — and it launched in public preview on January 15, 2026.**

## How Agentic Memory Works

The core idea is simple but powerful: as Copilot agents work on your repository, they extract and store small, tightly scoped facts called *memories*. These memories persist across sessions and are shared across different Copilot agents working on the same repository.

Think of a concrete example. Copilot’s coding agent is fixing a security vulnerability and in the process notices that your database connections always use a specific pattern — connection pooling with a custom retry policy. It stores this as a memory. From that point forward, every time Copilot code review looks at a pull request touching database code, it can flag deviations from that pattern automatically. No custom instruction files required.

Another practical scenario: Copilot code review notices during a PR that two configuration files must always stay synchronized — for instance, your appsettings.json and a Dataverse environment variable manifest. It stores that relationship as a memory. The coding agent will now automatically update both files together when generating new code that touches either one.

This is what GitHub means by *cross-agent memory*: knowledge discovered by one agent becomes available to all other agents working on the same repository.

## Under the Hood: JIT Verification and Citation-Based Storage

The most interesting engineering decision in GitHub’s implementation is what they deliberately chose *not* to build. The obvious approach for a memory system would be an offline curation service — a background process that manages, deduplicates, and expires old memories. GitHub rejected this architecture because maintaining a separate “truth database” synchronized with a rapidly changing codebase is a maintenance nightmare at scale.

Instead, they went with a Just-In-Time (JIT) verification model built on citations.

Every memory is stored together with citations — references to specific code locations in the repository that support the memory. When an agent retrieves a memory at the start of a new session, it does not trust it blindly. It checks the cited code locations against the current state of the branch:

-   If the code still matches the memory, the memory is valid and gets used (and its timestamp is refreshed).

-   If the code contradicts the memory or the cited locations no longer exist, the agent stores a corrected version reflecting the new evidence.
-   Memories that are never validated again are automatically deleted after 28 days.

This approach elegantly eliminates the need for any background curation. The verification happens inline, is limited to a small number of read operations, and adds negligible latency to agent sessions.

Memory creation itself is implemented as a tool call. The agent invokes it only when it discovers something with long-term, actionable value — not every time it reads a line of code. This keeps the memory store lean and signal-rich rather than noisy.

## Security and Privacy Model

Memory is scoped strictly to repositories, mirroring GitHub’s existing permission model:

-   Memories can only be **created** from activity initiated by users with write permissions.

-   Memories can only be **used** for tasks in the same repository by users with read permissions.
-   No memory crosses repository boundaries — knowledge about Repository A never leaks into Repository B.

-   Repository owners can view and delete all stored memories from repository settings.
-   Automatic 28-day expiry prevents stale knowledge from persisting indefinitely.

**Tip:** Memory is opt-in and off by default. Individual users on Copilot Pro or Pro+ enable it in personal settings. Organizations and enterprises enable it through policy settings in the organization or enterprise admin panel.

## Agentic Memory vs. Instruction Files: Full Comparison

Before agentic memory existed, the recommended way to give Copilot persistent context was a manually maintained instruction file — typically .*github/copilot-instructions.md*. Both approaches solve the same underlying problem (stateless AI), but they solve it in fundamentally different ways. Understanding the tradeoffs helps you decide when to use each one, and when to combine them.

The mental model that helps most: think of instruction files as your **team wiki** — intentional, structured, human-curated. Think of agentic memory as the **institutional knowledge a senior developer absorbs** from years of working on a codebase — implicit, self-updating, and shared automatically with everyone on the team.

| **Dimension** | **Instruction Files** | **Agentic Memory** |
| **How knowledge is created** | You write it manually | Copilot discovers it automatically during agent sessions |
| **How it stays current** | You update it manually — goes stale if you don’t | Self-updates via JIT citation verification; auto-corrects when code changes |
| **Maintenance burden** | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Medium — requires regular manual updates | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) None — fully automatic |
| **Available from day one** | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes — works immediately after you write it | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No — requires weeks of real Copilot activity to accumulate |
| **Knows things you forgot to document** | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No — only knows what you explicitly wrote | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes — learns implicit patterns you never thought to document |
| **Scope** | Repository (read by all agents working on that repo) | Repository only (public preview); personal + org scope planned |
| **Shared across agents** | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes — all Copilot agents read the same file | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes — cross-agent: coding agent memories inform code review and vice versa |
| **Handles contradictions** | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No — you have to manually remove outdated content | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes — if memory contradicts current code, it stores a corrected version |
| **Expiry / staleness risk** | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) High — stays forever regardless of relevance | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Low — auto-expires after 28 days unless actively used and verified |
| **Granularity** | Coarse — document-level, human-authored paragraphs | Fine — atomic facts tied to specific code locations |
| **Auditability** | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) High — it’s a Git-tracked file, fully visible | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Medium — viewable in repo settings, but not Git-tracked |
| **Best for** | Non-negotiable standards, onboarding rules, architectural decisions you want enforced from day one | Emergent conventions, file synchronization rules, patterns discovered through real development activity |
| **Works on low-activity repos** | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No — needs frequent Copilot interactions to generate memories |

### The Recommended Approach: Use Both Together

Instruction files and agentic memory are not competing alternatives — they’re complementary layers. The practical recommendation is:

-   Use **instruction files** for the rules you already know: publisher prefix conventions, forbidden patterns, required code review checklist items, deployment pipeline constraints. These are facts you can document on day one and that should never be violated.

-   Let **agentic memory** handle the rest: the patterns that emerge organically from your team’s actual development activity, the subtle synchronization requirements between files, the architectural habits that are easier to demonstrate than to document.

**Power Platform tip:** Start with an instruction file that documents your publisher prefix, solution naming convention, and connection reference pattern. Let agentic memory layer on top over time with the more nuanced knowledge — like which Dataverse tables must be updated together, or which PCF controls share a common utility library.

## Availability, Current Limits, and What’s Coming

### **What’s Available Now (Public Preview, January 2026)**

-   **Supported Copilot Features**
    -   Copilot Coding Agent
    -   Copilot Code Review
    -   Copilot CLI
-   **Eligible Plans**
    -   Copilot Pro
    -   Copilot Pro+
    -   Copilot Business
    -   Copilot Enterprise
-   **Memory Scope**
    -   Per repository only
    -   Strict isolation — no cross-repo sharing
    -   Write permission required to create memories
    -   Read permission sufficient to use memories
-   **Management Controls**
    -   View all stored memories in repo settings
    -   Delete individual or all memories
    -   Org/enterprise policy toggle
    -   Off by default — fully opt-in

### **Current Limits to Be Aware Of**

Known Limitations in Public Preview:

-   **Repository scope only.** No organization-wide or personal memory yet. Each repository is an isolated silo.

-   **28-day expiry.** Memories that are not re-validated within 28 days are automatically deleted. Low-activity repositories may lose memories before they become useful.
-   **No retrieval search tool yet.** Currently, memories are retrieved by recency for the target repository. Semantic search and weighted prioritization are planned but not yet available.

-   **Closed-branch memories persist temporarily.** Memories can be created from code in PRs that were closed without merging — these will expire naturally but may temporarily affect suggestions.
-   **No memory between conflicting branches.** If two branches have contradictory patterns, Copilot verifies memories against the current branch at runtime — but the experience across branches can feel inconsistent.

-   **Requires active Copilot agent use.** The system only learns from activity initiated by users who have memory enabled. Passive IDE autocomplete does not generate memories.

### What’s on the Roadmap  

**GitHub has confirmed the following are planned for future releases:**

-   **Personal scope** — memory tied to you as a developer, carrying your preferences and patterns across all repositories you work in.

-   **Organizational scope** — shared knowledge available across all repositories in an organization, enabling cross-repo convention enforcement.
-   **Additional retrieval techniques** — semantic search tool and weighted prioritization to surface the most relevant memories rather than just the most recent ones.

-   **More Copilot agents** — memory support for agents beyond coding, code review, and CLI (security, deployment, and maintenance agents are expected to follow).

## The Four Learning Phases: How to Test and Validate the Impact

One of the most common questions after enabling agentic memory is: *“How do I know if it’s actually working?”* The answer requires a structured approach because the memory system does not produce instant results — it needs real development activity to learn from. Here is a proven four-phase validation framework.

### Phase 1 — Baseline: Document Your Current Pain Points

Before enabling memory, identify 3–5 situations where you currently have to re-explain context to Copilot every session. Run each as a cold prompt with no instruction file and no extra context, and save the outputs. Examples: *“Generate a new PCF control following our MobX pattern”*, *“Write a Power Automate flow that uses our connection reference naming convention”*, *“Create a Dataverse schema script with our publisher prefix and audit columns.”* These saved outputs become your before snapshots for comparison.

Day 0 — before enabling memory

### Phase 2 — Accumulation: Enable Memory and Work Normally

Turn on memory and simply continue your normal workflow for two to four weeks. Do not try to force or accelerate the learning — the system needs genuine PR activity, real code review cycles, and authentic coding agent tasks to extract meaningful patterns. Artificial interactions produce noise, not signal. The memory system is learning from the actual decisions your team makes, not from synthetic exercises. For Power Platform teams: keep using the coding agent for PCF scaffolding, running code review on solution PRs, and using Copilot CLI for schema work.

Weeks 1–4 — passive accumulation period

### Phase 3 — Inspection: Read the Stored Memories Directly

This is the step most developers skip, and it’s the most revealing. Navigate to your repository on GitHub → Settings → Copilot → Memory and review exactly what facts Copilot has stored. Ask yourself: do the stored memories reflect the conventions you actually care about? Are there memories about the right things (your MobX pattern, your naming conventions, your cascade behavior rules)? Are there any that capture noise rather than signal? This inspection tells you whether the system is learning correctly before you rely on it. If the stored memories look wrong or incomplete, that is diagnostic information about what your codebase needs to make patterns more explicit.

After week 2 — inspect and assess quality

### Phase 4 — Validation: Re-run Baselines and Controlled Violation Tests

After four weeks, re-run the exact same cold prompts from Phase 1 and compare outputs side by side. Did Copilot apply your naming conventions without prompting? Did it follow your architectural patterns automatically? Then run the most revealing test: intentionally submit a PR that *violates* a convention you expect the memory system to have learned — for example, a PCF control that calls notifyOutputChanged directly instead of through a MobX reaction, or a connection reference named outside your convention. If Copilot code review flags the violation without any human instruction, the memory system is working exactly as intended. If it does not flag it, the convention may not have been stored or the citation verification may have failed — both of which point back to making your code patterns more explicit.

Week 4+ — benchmark against your baseline

**Realistic expectations:** The 28-day expiry means memory only sticks if conventions are being regularly reinforced through active use. A repository that sees one or two PRs per month may not accumulate enough signal for the system to be meaningfully useful. Agentic memory delivers the most value on active codebases with frequent Copilot interactions — think at least 3–5 coding agent tasks or code review cycles per week.

## Use Cases

### Use Case 1 — PCF Control Development: Teaching Copilot Your Component Architecture

**The Problem**

PCF (Power Apps Component Framework) controls follow strict structural conventions: the manifest defines property types, the index TypeScript file implements the IInputs/IOutputs interfaces, CSS modules follow a naming convention, and your team probably uses MobX for state management. Every time a new developer — or a new AI session — touches the component library, this context has to be re-explained.

**How Agentic Memory Helps**

Once the memory system sees enough PRs in your PCF repository, it learns and retains your patterns. A stored memory might look like: *“PCF controls in this repo use MobX observables for internal state. The `updateView` method should never trigger `notifyOutputChanged` unless the user has explicitly interacted with the control. See: `src/controls/DateRangePicker/index.ts`, line 87.”*

From that point on, when the coding agent generates a new PCF control scaffold, it automatically follows your MobX pattern without prompting.

**Sample: PCF Control with Explicit Architecture Comments for Memory Extraction**

Structure your code with rich, descriptive comments in logical boundaries. The memory system picks these patterns up during code review iterations:

TypeScript

```
// src/controls/StatusBadge/index.ts
// ARCHITECTURE: This control follows the MobX observable pattern used across
// all PCF controls in this repository. State is managed in a separate store class.
// notifyOutputChanged() is called ONLY from the MobX reaction, never directly.

import { IInputs, IOutputs } from "./generated/ManifestTypes";
import { makeObservable, observable, reaction } from "mobx";

interface IControlState {
  statusValue: string;
  colorCode: string;
}

class StatusStore {
  @observable state: IControlState = { statusValue: "", colorCode: "#0078d4" };

  constructor() {
    makeObservable(this);
  }

  updateStatus(value: string): void {
    this.state.statusValue = value;
    // Color mapping follows the convention defined in DesignTokens.ts
    this.state.colorCode = this.resolveColor(value);
  }

  private resolveColor(status: string): string {
    const colorMap: Record<string, string> = {
      Active: "#107c10",
      Inactive: "#a80000",
      Pending: "#ff8c00",
    };
    return colorMap[status] ?? "#0078d4";
  }
}

export class StatusBadge implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  private store: StatusStore;
  private notifyOutputChanged: () => void;
  private container: HTMLDivElement;

  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ): void {
    this.notifyOutputChanged = notifyOutputChanged;
    this.container = container;
    this.store = new StatusStore();

    // MobX reaction: the ONLY place where notifyOutputChanged is called
    reaction(
      () => this.store.state.statusValue,
      () => this.notifyOutputChanged()
    );
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    const newValue = context.parameters.statusField.raw ?? "";
    if (newValue !== this.store.state.statusValue) {
      this.store.updateStatus(newValue);
    }
    this.render();
  }

  private render(): void {
    this.container.innerHTML = `
      <div class="status-badge" style="background:${this.store.state.colorCode}">
        ${this.store.state.statusValue}
      </div>
    `;
  }

  public getOutputs(): IOutputs {
    return {};
  }

  public destroy(): void {}
}
```

**Why this helps with memory:** The explicit architecture comment at the top becomes a citation anchor for the memory system. When Copilot code review sees a new PCF control that calls notifyOutputChanged directly from updateView, it flags the violation automatically because it remembers the architectural rule.

### Use Case 2 — Dataverse Plugin Development: Learning Your Plugin Architecture Patterns

**Why This Is the Most Realistic Power Platform Use Case**

Dataverse plugins are the strongest fit for agentic memory in the entire Power Platform ecosystem. They are pure C# code, they live natively in a Git repository, and Copilot works with them exactly as it would with any .NET project. More importantly, plugin projects accumulate very specific, opinionated architectural patterns over time — how you obtain services from IServiceProvider, whether you use early-bound or late-bound entity access, how you structure pre/post image retrieval, how tracing and error handling are done, and whether business logic is centralised in a base class or duplicated per plugin. These are exactly the kinds of implicit conventions that are tedious to document manually and perfect for the memory system to discover automatically.

**The Problem Without Memory**

Every time a developer (or the coding agent) creates a new plugin step, they have to either look at an existing plugin for reference, consult an instruction file, or just guess — and guessing produces inconsistent code. A new plugin might skip null checks on pre-images, forget to wrap execution in a try/catch that logs to the tracing service, or use Entity directly instead of the team’s preferred early-bound generated classes. Code review catches some of this, but not always.

**How Agentic Memory Helps**

After a few weeks of PRs and coding agent activity on your plugin repository, the memory system learns: your base class pattern, how ITracingService is always obtained first, that pre-images are always null-checked before access, and that business logic never goes directly in Execute() but is delegated to a dedicated handler method. The next plugin the coding agent scaffolds will follow all of these conventions without a single prompt.

**Sample: Dataverse Plugin with Consistent Architecture for Memory Extraction**

The key is structural consistency across all plugins in the repository. The memory system learns from the pattern it sees repeated across multiple files and PRs:

C#

```
// Plugins/Account/AccountUpdatePlugin.cs
//
// ARCHITECTURE CONVENTIONS (enforced across all plugins in this repo):
//   1. Always extend PluginBase — never implement IPlugin directly.
//   2. Obtain ITracingService FIRST before any other operation.
//   3. Pre/post images are ALWAYS null-checked — never assume they exist.
//   4. Business logic goes in a dedicated handler class, not in Execute().
//   5. Use early-bound generated types (contoso_project, etc.) — never late-bound strings.
//   6. All exceptions are caught, traced, and rethrown as InvalidPluginExecutionException.

using Microsoft.Xrm.Sdk;
using System;

namespace Contoso.Plugins.Account
{
    [CrmPluginRegistration(
        MessageNameEnum.Update,
        "account",
        StageEnum.PostOperation,
        ExecutionModeEnum.Synchronous,
        FilteringAttributes = "name,telephone1,contoso_accounttier",
        StepName = "Contoso: Post-Update Account — Sync Tier to Projects",
        Description = "Syncs account tier changes to all related contoso_project records.")]
    public class AccountUpdatePlugin : PluginBase
    {
        // CONVENTION: Constructor only sets plugin context — no logic here
        public AccountUpdatePlugin(string unsecureConfig, string secureConfig)
            : base(typeof(AccountUpdatePlugin)) { }

        protected override void ExecuteCrmPlugin(LocalPluginContext localContext)
        {
            // CONVENTION: Tracing service obtained first — always
            var tracingService = localContext.TracingService;
            tracingService.Trace("AccountUpdatePlugin: starting execution.");

            var context = localContext.PluginExecutionContext;
            var serviceFactory = localContext.OrganizationServiceFactory;
            var service = serviceFactory.CreateOrganizationService(context.UserId);

            // CONVENTION: Pre-image access is always null-checked
            // Pre-image alias registered as "PreImage" in plugin registration
            if (!context.PreEntityImages.TryGetValue("PreImage", out Entity preImage))
            {
                tracingService.Trace("PreImage not available — skipping sync.");
                return;
            }

            // CONVENTION: Target image retrieved via strong-typed helper
            var target = context.InputParameters["Target"] as Entity;
            if (target == null)
            {
                throw new InvalidPluginExecutionException("Target entity is null.");
            }

            try
            {
                // CONVENTION: Business logic always delegated to a handler — never inline
                var handler = new AccountTierSyncHandler(service, tracingService);
                handler.SyncTierToProjects(target, preImage);

                tracingService.Trace("AccountUpdatePlugin: completed successfully.");
            }
            catch (InvalidPluginExecutionException)
            {
                // Re-throw business exceptions as-is
                throw;
            }
            catch (Exception ex)
            {
                // CONVENTION: Unexpected exceptions are traced then wrapped
                tracingService.Trace($"Unexpected error: {ex.Message}\n{ex.StackTrace}");
                throw new InvalidPluginExecutionException(
                    $"AccountUpdatePlugin failed: {ex.Message}", ex);
            }
        }
    }
}
```

C#

```
// Plugins/Account/AccountTierSyncHandler.cs
//
// CONVENTION: Each plugin has a paired handler class for all business logic.
// Handler classes are unit-testable without IOrganizationService mocking overhead.

using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Query;
using System.Collections.Generic;

namespace Contoso.Plugins.Account
{
    internal class AccountTierSyncHandler
    {
        private readonly IOrganizationService _service;
        private readonly ITracingService _tracing;

        public AccountTierSyncHandler(IOrganizationService service, ITracingService tracing)
        {
            _service = service;
            _tracing = tracing;
        }

        public void SyncTierToProjects(Entity target, Entity preImage)
        {
            // Only proceed if the tier actually changed
            if (!target.Contains("contoso_accounttier")) return;

            var newTier = target.GetAttributeValue<OptionSetValue>("contoso_accounttier");
            var oldTier = preImage.GetAttributeValue<OptionSetValue>("contoso_accounttier");

            if (newTier?.Value == oldTier?.Value) return;

            _tracing.Trace($"Tier changed from {oldTier?.Value} to {newTier?.Value}. Syncing projects.");

            // Retrieve all active projects for this account
            var query = new QueryExpression("contoso_project")
            {
                ColumnSet = new ColumnSet("contoso_projectid", "contoso_accounttier"),
                Criteria = new FilterExpression
                {
                    Conditions =
                    {
                        new ConditionExpression("accountid", ConditionOperator.Equal, target.Id),
                        new ConditionExpression("statecode", ConditionOperator.Equal, 0)
                    }
                }
            };

            var projects = _service.RetrieveMultiple(query).Entities;
            _tracing.Trace($"Found {projects.Count} active projects to update.");

            foreach (var project in projects)
            {
                var update = new Entity("contoso_project", project.Id)
                {
                    ["contoso_accounttier"] = newTier
                };
                _service.Update(update);
            }
        }
    }
}
```

C#

```
// Plugins/PluginBase.cs
//
// CONVENTION: All plugins in this repo extend PluginBase.
// This ensures consistent service extraction, context validation,
// and tracing setup across the entire plugin assembly.

using Microsoft.Xrm.Sdk;
using System;

namespace Contoso.Plugins
{
    public abstract class PluginBase : IPlugin
    {
        private readonly string _pluginTypeName;

        protected PluginBase(Type pluginType)
        {
            _pluginTypeName = pluginType.FullName;
        }

        public void Execute(IServiceProvider serviceProvider)
        {
            if (serviceProvider == null)
                throw new ArgumentNullException(nameof(serviceProvider));

            var localContext = new LocalPluginContext(serviceProvider);
            localContext.TracingService.Trace($"[{_pluginTypeName}] Entered Execute().");

            ExecuteCrmPlugin(localContext);
        }

        // CONVENTION: Subclasses implement this method, not Execute()
        protected abstract void ExecuteCrmPlugin(LocalPluginContext localContext);
    }
}
```

**Why this feeds the memory system well:** When the coding agent works on a new plugin — say, a pre-create step for contoso\_project — it reads the existing plugin files and their architecture comments as context. After a few PRs following this pattern, Copilot code review starts flagging any new plugin that bypasses PluginBase, skips null checks on images, or puts logic directly in Execute(). The memory evolves from reading your code, not from a file you wrote.

### Use Case 3 — Solution Source Control: Teaching Copilot Your Unpacked Solution Conventions

**Why Solution Source Control Is a Realistic Fit**

When you use pac solution unpack to store your Power Platform solution in Git, what you get in source control is a folder tree of YAML and JSON files — workflow definitions, environment variable schemas, connection reference metadata, custom control manifests, and more. These files are text. Copilot code review reads them like any other code. This means the memory system can genuinely learn from PRs that modify these files, because the coding agent and code review agent are actually working with the content.

This is fundamentally different from the previous version of this use case (raw Dataverse REST API scripts), which was too abstract and too far from how real teams work. Solution source files in a solutions/ folder are how modern Power Platform ALM actually looks.

**The Problem Without Memory**

Every time someone adds a new environment variable definition, a new connection reference, or a new cloud flow to the solution, there is a risk they forget the team’s conventions: the publisher prefix, the correct connector reference format, whether the flow must include an error-handling scope, or which environment variables must appear together. These mistakes are invisible until deployment fails or a flow errors in production.

**How Agentic Memory Helps**

After the coding agent and code review agent process several PRs touching your unpacked solution files, the memory system starts learning: which connection references must appear together (SharePoint and Dataverse always co-exist in this solution), what environment variable naming looks like, that every flow must have a top-level error scope that sends an adaptive card to a Teams channel, and which tables are referenced across multiple flow definitions. Code review will start flagging flows that skip the error scope. The coding agent will add the correct connection reference format when scaffolding new flows.

**Sample: Unpacked Solution Structure with Consistent Conventions**

Here is what a well-structured, convention-rich unpacked solution looks like in source control. The consistent patterns across files are what the memory system learns from:

Markdown

```


# Solution folder structure after pac solution unpack


# solutions/CONTOSOCRM/src/


# ├── Other/


# │   └── Solution.xml


# ├── environmentvariabledefinitions/


# │   ├── contoso_SharePointSiteUrl.json


# │   └── contoso_DataverseEnvironmentUrl.json


# ├── connectionreferences/


# │   ├── contoso_sharedsharepointonline.json


# │   └── contoso_shareddataverse.json


# └── Workflows/


#     ├── contoso_OnProjectCreated-{guid}.json


#     └── contoso_OnAccountTierChanged-{guid}.json
```

JSON

```
// solutions/CONTOSOCRM/src/environmentvariabledefinitions/contoso_SharePointSiteUrl.json
// CONVENTION: All environment variable schema names use prefix contoso_ followed by PascalCase.
// Display names are human-readable. Type is always explicit. DefaultValue is never set
// in source — only in deployment pipelines via deployment settings files.
{
  "environmentvariabledefinition": {
    "schemaname": "contoso_SharePointSiteUrl",
    "displayname": "SharePoint Site URL",
    "description": "Root SharePoint site used by all flows in this solution. Set per environment in deployment settings.",
    "type": "String",
    "isrequired": true,
    "introducedversion": "1.0.0.0"
  }
}
```

JSON

```
// solutions/CONTOSOCRM/src/connectionreferences/contoso_sharedsharepointonline.json
// CONVENTION: Connection reference logical names follow pattern:
//   contoso_shared{ConnectorNameNormalized}
// DisplayName is "{SolutionDisplayName} - {ServiceName}"
// connectionprovider always references the canonical connector ID.
// IMPORTANT: SharePoint and Dataverse connection references always appear together
// in this solution — if one is present, both must be present.
{
  "connectionreference": {
    "connectionreferencelogicalname": "contoso_sharedsharedataverse",
    "connectorid": "/providers/Microsoft.PowerApps/apis/shared_commondataserviceforapps",
    "displayname": "Contoso CRM - Microsoft Dataverse",
    "iscustomizable": true,
    "introducedversion": "1.0.0.0"
  }
}
```

JSON

```
// solutions/CONTOSOCRM/src/Workflows/contoso_OnProjectCreated-{guid}.json (simplified excerpt)
// CONVENTION: Every cloud flow in this solution must:
//   1. Have a top-level Try/Catch scope named "Error Handling Scope"
//   2. On failure: send an adaptive card to Teams channel (id stored in contoso_TeamsAlertChannelId env var)
//   3. Use connection references — never hardcoded connections
//   4. Flow display name: "Contoso | {TriggerEntity} | {ActionDescription}"
{
  "properties": {
    "displayName": "Contoso | Project | Notify Team on Creation",
    "description": "Fires on creation of contoso_project. Notifies the project team channel via Teams.",
    "connectionReferences": {
      "shared_teams": {
        "connectionName": "shared_teams",
        "id": "/providers/Microsoft.PowerApps/apis/shared_teams",
        "connectionReferenceLogicalName": "contoso_sharedmicrosoftteams"
      },
      "shared_commondataserviceforapps": {
        "connectionName": "shared_commondataserviceforapps",
        "id": "/providers/Microsoft.PowerApps/apis/shared_commondataserviceforapps",
        "connectionReferenceLogicalName": "contoso_shareddataverse"
      }
    },
    "definition": {
      "triggers": {
        "When_a_row_is_added": {
          "type": "OpenApiConnectionWebhook",
          "inputs": {
            "host": { "connectionName": "shared_commondataserviceforapps" },
            "parameters": {
              "subscriptionRequest/entityname": "contoso_project",
              "subscriptionRequest/scope": 4
            }
          }
        }
      },
      "actions": {
        "Error_Handling_Scope": {
          "type": "Scope",
          "comment": "CONVENTION: Required on every flow. Contains all business logic. runAfter is always empty (first action).",
          "actions": {
            "Get_Project_Details": {
              "type": "OpenApiConnection",
              "inputs": {
                "host": { "connectionName": "shared_commondataserviceforapps" },
                "parameters": {
                  "entityName": "contoso_project",
                  "recordId": "@triggerOutputs()?['body/contoso_projectid']",
                  "selectColumns": "contoso_projectname,contoso_accounttier,_ownerid_value"
                }
              }
            },
            "Post_Teams_Notification": {
              "type": "OpenApiConnection",
              "inputs": {
                "host": { "connectionName": "shared_teams" },
                "parameters": {
                  "channelId": "@parameters('$connections')['contoso_TeamsAlertChannelId']",
                  "body/messageBody": "New project created: @{outputs('Get_Project_Details')?['body/contoso_projectname']}"
                }
              },
              "runAfter": { "Get_Project_Details": ["Succeeded"] }
            }
          },
          "runAfter": {}
        },
        "Handle_Errors": {
          "type": "Scope",
          "comment": "CONVENTION: Always named 'Handle_Errors'. Runs only when Error_Handling_Scope fails.",
          "actions": {
            "Post_Error_to_Teams": {
              "type": "OpenApiConnection",
              "inputs": {
                "host": { "connectionName": "shared_teams" },
                "parameters": {
                  "channelId": "@parameters('$connections')['contoso_TeamsAlertChannelId']",
                  "body/messageBody": "Flow error in @{workflow()?['name']}: @{actions('Error_Handling_Scope')?['error']?['message']}"
                }
              }
            }
          },
          "runAfter": { "Error_Handling_Scope": ["Failed", "TimedOut"] }
        }
      }
    }
  }
}
```

**What the memory system learns from this:** After Copilot code review processes a few PRs that add or modify flow JSON files, it stores memories like: *“Every flow in this solution must contain an Error\_Handling\_Scope action and a Handle\_Errors scope that runs on failure.”* and *“contoso\_sharedsharedataverse and contoso\_sharedsharedataverse connection references always appear together.”* The next PR that adds a flow without the error scope will be flagged automatically — no instruction file entry required.

**Important prerequisite:** This use case requires your team to be doing proper ALM — unpacking solutions with pac solution unpack and committing the source files to Git. If your solution files are stored only as managed/unmanaged ZIPs, Copilot has nothing to read and the memory system cannot learn from them.

## How to Enable Agentic Memory Right Now

Enabling memory is straightforward, but the experience differs slightly depending on your Copilot plan.

**Enabling Copilot Memory for an enterprise  
**Enterprise owners can define an enablement policy for the whole enterprise, or delegate the decision to individual organization owners.

1.  In the top-right corner of GitHub, click your profile picture.
2.  Depending on your environment, click Enterprise, or click Enterprises then click the enterprise you want to view.
3.  At the top of the page, click AI controls.
4.  In the sidebar, click Copilot.
5.  Under “Features”, scroll down to the Copilot Memory setting and select a policy from the dropdown.
    -   Let organizations decide devolves the decision of whether to enable Copilot Memory to organization owners.
    -   Enabled everywhere enables Copilot Memory for all members of organizations in this enterprise who have a Copilot license.
    -   Disabled everywhere disables Copilot Memory and prevents it being enabled by organizations in this enterprise.

  
**Enabling Copilot Memory for an organization  
**Organization owners can enable or disable Copilot Memory for all members of the organization with a Copilot license.

If the organization belongs to an enterprise, the ability for organization owners to enable or disable Copilot Memory may be controlled by the enterprise-level policy.

1.  In the upper-right corner of GitHub, click your profile picture, then click Organizations.
2.  Next to the organization, click Settings.
3.  In the sidebar, under “Code, planning, and automation”, click Copilot, then click Policies.
4.  Under “Features”, scroll down to the setting for Copilot Memory.
5.  Click the dropdown button and select Enabled.

Copilot Memory is enabled for all members of the organization who have a Copilot license.

**Enabling Copilot Memory for an individual user  
**If you have an individual Copilot subscription, from a Copilot Pro or Copilot Pro+ plan, you can enable Copilot Memory in your personal Copilot settings on GitHub.

Once enabled, Copilot Memory will be used in any repository in which you use Copilot coding agent, Copilot code review, or Copilot CLI.

1.  In the upper-right corner of any page on GitHub, click your profile picture, then click Copilot settings.
2.  Under “Features”, scroll down to the setting for Copilot Memory.
3.  Click the dropdown button and select Enabled.

**Practical tip for Power Platform teams:** Enable memory on your PCF component library repository first — this is typically where the most consistent architectural patterns exist and where the memory system will produce the most immediate value. Give it two to four weeks of normal PR activity before evaluating the results.

## What Comes Next: The Road Toward Knowledge Graphs

The current memory system stores relatively flat structures — individual facts tied to specific code locations. GitHub has signaled that future implementations will extend this with more sophisticated retrieval techniques, weighted prioritization, and memory scoped beyond repositories to personal and organizational levels.

Architecturally, the next logical step is a knowledge graph layer that understands relationships between memories across different domains. Imagine Copilot knowing that the authentication pattern in your PCF security service is functionally related to the OAuth flow in your Power Automate custom connector — not because they share a repository, but because the memory system has learned the semantic relationship between the two.

For Power Platform professionals, this maps directly to where the ecosystem is heading anyway: autonomous Copilot Studio agents that understand your entire enterprise data model, your Dataverse schema history, and your team’s deployment conventions — all without ever needing a custom instructions file.

The GitHub Copilot SDK, launched in technical preview in January 2026, takes this further by making the same agentic loop programmatically embeddable. That opens the door to building custom internal tools that combine Copilot’s memory-aware reasoning with your own enterprise tooling — Power Platform CLI, PAC CLI, and Dataverse APIs included.

## Closing Thoughts

Agentic memory is not a flashy feature — it does not change what Copilot can do. It changes what Copilot *knows*. And in enterprise development environments like Power Platform, where conventions, schema decisions, and deployment patterns accumulate years of hard-won institutional knowledge, that distinction matters enormously.

The architectural choices GitHub made — JIT verification over offline curation, citations over raw fact storage, repository isolation over global memory — are smart and pragmatic. They produce a system that gets better with use without requiring any maintenance overhead from developers.

If you work with PCF controls, Dataverse plugins, or Power Platform solutions in source control daily, enabling memory in your repositories today is low-risk and potentially high-reward. The system learns quietly in the background and starts delivering value through better-targeted code review and more context-aware code generation within weeks.

## References and Further Reading

-   [Building an agentic memory system for GitHub Copilot — GitHub Blog (Jan 2026)](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)

-   [About agentic memory for GitHub Copilot — GitHub Docs](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)
-   [Agentic memory for GitHub Copilot is in public preview — GitHub Changelog](https://github.blog/changelog/2026-01-15-agentic-memory-for-github-copilot-is-in-public-preview/)

-   [Build an agent into any app with the GitHub Copilot SDK — GitHub Blog (Jan 2026)](https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/)
-   [Memory is an Action, Not a Database — DEV Community](https://dev.to/mosiddi/memory-is-an-action-not-a-database-reflections-on-github-copilots-new-agentic-system-hpa)

-   [Memory Bank System — Agentic Coding Handbook](https://tweag.github.io/agentic-coding-handbook/WORKFLOW_MEMORY_BANK/)
-   [GitHub Copilot’s Agentic Memory: Teaching AI to Remember Your Codebase — Arinco](https://arinco.com.au/blog/github-copilots-agentic-memory-teaching-ai-to-remember-and-learn-your-codebase/)

-   [What’s New in Copilot Studio: November 2025 Updates — Microsoft](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/whats-new-in-microsoft-copilot-studio-november-2025/)

*Drop your thoughts in the comments below. If you’ve run into edge cases, surprising memory entries, or conventions the system got completely wrong, I want to hear about those too — the honest experiences are the most useful ones.*

*And if this article was useful, consider **sharing it with a colleague** who is still re-explaining their codebase to Copilot every single session. That problem now has a solution — they just need to know it exists.*

---
> **Note:** This page contains 3 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [GitHub Copilot Agentic Memory: What It Is, How It Works?](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/)