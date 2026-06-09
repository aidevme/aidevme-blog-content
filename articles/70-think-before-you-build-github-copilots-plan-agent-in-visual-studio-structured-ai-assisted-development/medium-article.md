# Think Before You Build: GitHub Copilot's Plan Agent in Visual Studio

> *Originally published at [aidevme.com](https://aidevme.com/think-before-you-build-github-copilots-plan-agent-in-visual-studio-structured-ai-assisted-development/). The full version with code examples and references is available there.*

---

You fire up GitHub Copilot in Agent mode, describe a feature, and watch it start modifying files across your solution. Ten minutes later you're staring at a cascade of changes that technically compile — but head in entirely the wrong direction.

The AI wasn't wrong. *You* just weren't aligned with it before it started.

This is the structural limitation of how agentic AI coding has worked up to now. Agent mode is optimised for *doing*. The moment you describe a task, the model starts gathering context and generating changes. For small, well-bounded tasks that's exactly the right behaviour. For anything larger — a multi-file refactor, a new integration layer, a significant architecture change — the absence of an explicit alignment step is where things go sideways.

Microsoft shipped the **Plan agent** in Visual Studio in May 2026 to address exactly this. It inserts a structured planning phase *before* any code generation happens.

---

## What the Plan Agent Actually Does

From the agent picker in the Copilot Chat panel, you select **Plan** instead of **Agent**, then describe your task. Here's what follows:

**1. Describe your intent** — Your prompt starts the process. Precise prompts produce better plans with fewer clarifying rounds. Vague prompts trigger more questions.

**2. Read-only codebase scan** — Copilot reads your solution before proposing anything. Project structure, service registrations, interface definitions, config files, NuGet references. No writes, no changes. The plan it produces will be grounded in *your* codebase, not a generic template.

**3. Targeted clarifying questions** — Where it finds ambiguity, it asks. Which project should this apply to? Should the existing authentication layer be left untouched? Each answer narrows the scope.

**4. Markdown plan drafted** — A detailed step-by-step plan is saved to `.copilot/plans/plan-{title}.md`. You get a structured document listing the goal, affected files, numbered steps, out-of-scope items, and open questions.

**5. You edit the plan** — Open it in the editor and treat it like any other file. Add constraints as inline comments. Remove steps you don't want. Change file paths. Commit it to your PR as a design decision record.

**6. Implement** — When you're satisfied, click **Implement plan**. Agent mode executes the approved plan step by step. You're not discovering the design mid-flight — you're executing a decision you already made.

---

## The Key Insight

Think of the difference between an architect showing you blueprints versus a contractor arriving with half the walls already framed. The end result might be technically sound either way. But one of those conversations is much easier to have.

The Plan agent makes misalignment *visible and cheap to fix* — before the cost of changing direction becomes non-trivial.

---

## A Concrete Example: Dataverse Plugin Refactor

For those building on Power Platform or Dynamics 365, here's a prompt that produces a genuinely useful plan:

```
Refactor AccountSyncPlugin.cs to extract business logic into
a testable AccountSyncService. Introduce IAccountSyncService
and a constructor-injected factory so we can unit test without
live Dataverse calls. Follow the "poor man's DI" pattern standard
for Dataverse plugins. Create unit tests using Moq.
```

The Plan agent scans your plugin project, identifies the monolithic `IPlugin.Execute` method, and produces a plan with:

- `IOrganizationServiceFactory` interface to create
- `IAccountSyncService` interface to define
- `AccountSyncService` with all business logic extracted
- Refactored plugin as a thin orchestrator
- Unit tests using Moq — no live Dataverse required

The plan is reviewable, editable, and committable. Your colleague can review a Markdown document before the first file changes. That's a fundamentally different kind of collaboration than reviewing a 12-file diff after the fact.

---

## Prompts That Work Well

A few patterns that consistently produce better plans:

**Scope explicitly** — "Add in-memory caching to `AccountRepository` only. Do not modify the service layer." The more you specify what to leave alone, the tighter the plan scope.

**Reference existing patterns** — "Follow the same repository pattern used in `OrderService`." Copilot will scan your existing implementation and use it as the template.

**State test expectations upfront** — "Include unit tests covering the happy path and one failure scenario." Without this, tests tend to be an afterthought in the plan.

**Protect sensitive areas** — "Do not modify `WebhookController` — it is under active development in a parallel branch." Inline constraints in the plan are also respected during implementation.

---

## The `.copilot/plans/` Folder as a Decision Log

One underappreciated aspect: over time, your `.copilot/plans/` folder becomes a lightweight architectural decision log.

```
.copilot/
  plans/
    plan-accountsync-refactor.md       ← completed, committed
    plan-jwt-auth-middleware.md        ← completed, committed
    plan-bulk-import-pipeline.md       ← in progress
```

Add a simple frontmatter convention (`status`, `author`, `pr`) and these files tell a story about *why* the code is structured the way it is — not just what it does. Future developers (including you, six months from now) get context that normally lives only in people's heads or gets buried in PR descriptions.

---

## Where It Fits in the Development Pipeline

The Plan agent lives at the *design* end of the pipeline:

```
Plan agent        ← design & scope alignment
Agent mode        ← implementation
Solution Checker  ← static analysis
Unit Tests / CI   ← automated verification
PR Review         ← human review of diffs
PAC CLI Deploy    ← promotion to environment
```

It doesn't replace any downstream checks. A plan won't catch a runtime bug or a missing managed property. But it dramatically increases the likelihood that what gets built is what was intended — which reduces the cost of everything downstream.

---

## Worth Trying

The Plan agent is available now in Visual Studio with a GitHub Copilot subscription. Try it on your next refactoring task: write a precise prompt, let Copilot scan, push back on the first draft, edit the Markdown, then implement. The extra five minutes at the planning stage will save you a longer cleanup later.

The full article — including complete before/after code for the Dataverse plugin scenario, all four prompt patterns with detailed examples, and links to the official Microsoft documentation — is at:

👉 **[aidevme.com — Think Before You Build: GitHub Copilot's Plan Agent in Visual Studio](https://aidevme.com/think-before-you-build-github-copilots-plan-agent-in-visual-studio-structured-ai-assisted-development/)**

---

*Zsolt Zombik writes about Power Platform architecture, agentic AI patterns, and developer tooling for enterprise teams at [aidevme.com](https://aidevme.com).*
