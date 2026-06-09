# Think Before You Build: GitHub Copilot's Plan Agent in Visual Studio

*The missing alignment step between you and your AI coding agent — and why it matters for enterprise developers*

---

If you've been using GitHub Copilot in Agent mode for any serious development work, you've probably had this experience at least once.

You describe a task. Copilot starts working. Files change. More files change. Ten minutes later you're staring at a 15-file diff that technically compiles — but isn't what you meant. Not even close.

The frustrating part is that the AI wasn't wrong about *how* to solve the problem. It was wrong about *what* you wanted solved. And it was already halfway through building the wrong thing before you had a chance to course-correct.

This is the structural gap that Microsoft's new **Plan agent** in Visual Studio addresses. Shipped in May 2026, it inserts a deliberate planning phase *before* any code changes happen. Scan first. Plan. Get your approval. Then implement.

It sounds simple. In practice, it changes how you work with Copilot in a meaningful way.

---

## The problem with jumping straight to implementation

Agent mode is optimised for *doing*. That's its strength for small, well-bounded tasks — describe it, watch it happen, ship it. But for larger work — a service layer refactor, a new integration, a significant architecture change — that eagerness is a liability.

Consider this scenario that most of us have lived through:

> **You:** "Add retry logic to all Dataverse API calls in the service layer."
>
> **Copilot:** *(modifies 12 files, introduces Polly, changes interface signatures, updates DI registration, adds new config keys...)*
>
> **You:** "Wait — we already have retry built into our HttpClient factory. I just needed it applied to the OrganizationServiceProxy calls."

The misalignment wasn't in the AI's understanding of retry patterns. It was in the scope. Nobody paused to agree on what "service layer" meant, what was already in place, or what should be left alone.

The Plan agent makes that conversation happen *before* the first file changes.

---

## How it actually works

You select **Plan** from the agent picker in the Copilot Chat panel instead of **Agent**, then describe your task. Here's what follows:

**Copilot scans your codebase in read-only mode first.** It looks at your project structure, service registrations, interfaces, config files, and NuGet references — without touching anything. The plan it produces is grounded in *your* solution, not a generic template.

**It asks clarifying questions where it finds ambiguity.** Which project should this apply to? Should the existing authentication middleware be left alone? Each answer narrows the scope before anything is written.

**It drafts a detailed Markdown plan** — saved to `.copilot/plans/plan-{title}.md` — with the goal, affected files, numbered implementation steps, out-of-scope items, and open questions. You can read the whole thing before a single line of code is generated.

**You edit the plan directly.** Open it in the editor like any other file. Add constraints as inline comments (`<!-- CONSTRAINT: no async/await in plugins -->`). Remove steps you disagree with. Commit it to version control as a record of the design decision.

**Then you click Implement.** Agent mode takes over and executes the approved plan step by step. You're not discovering the design mid-flight anymore — you're executing a decision you already made and reviewed.

---

## A real example: Dataverse plugin refactoring

For those of us building on Power Platform or Dynamics 365, here's a prompt that produces a genuinely useful plan:

```
Refactor AccountSyncPlugin.cs to extract business logic into
a testable AccountSyncService. Introduce IAccountSyncService
and a constructor-injected factory so we can unit test without
live Dataverse calls. Follow the "poor man's DI" pattern standard
for Dataverse plugins. Create unit tests using Moq.
```

The Plan agent scans your plugin project, identifies the monolithic `IPlugin.Execute` method, and produces a structured plan: create the factory interface, define the service interface, implement the service class with all the business logic, refactor the plugin to a thin orchestrator, write Moq-based unit tests.

Each step is reviewable. You can push back on Step 3 and ask Copilot to break it into sub-steps. You can add a constraint to Step 2 protecting code that's being touched in a parallel branch. You can get architectural sign-off on the plan from a colleague before implementation begins.

The plan itself goes into your PR. Future developers reading the code six months from now can see not just *what* was built, but *why* it was structured that way.

---

## The `.copilot/plans/` folder as a decision log

This is the part that I think is most underestimated.

Over time, your plans folder accumulates a record of every significant design decision made with AI assistance:

```
.copilot/plans/
  plan-accountsync-refactor.md       ← completed
  plan-jwt-auth-middleware.md        ← completed
  plan-bulk-import-pipeline.md       ← in progress
  plan-power-pages-auth-redesign.md  ← under review
```

Add a simple frontmatter convention — `status`, `author`, `pr` — and these files tell a story about how your codebase evolved. No extra tooling required. It's just Markdown in a committed folder.

For teams that struggle with architecture documentation (which is most teams), this is a lightweight way to capture decisions in the moment rather than trying to reconstruct them after the fact.

---

## Where it fits in the enterprise development pipeline

The Plan agent sits at the design end:

```
Plan agent         ← scope alignment before any changes
Agent mode         ← implementation of the approved plan
Solution Checker   ← static analysis
Unit Tests / CI    ← automated verification
PR Review          ← human review of diffs
PAC CLI Deploy     ← promotion to environment
```

It doesn't replace the downstream checks. A plan won't catch a runtime bug or a missing managed property. But when the *design* is right before implementation begins, the downstream process has less to catch.

---

## Try it on your next refactoring task

The Plan agent is available now in Visual Studio with a GitHub Copilot subscription.

Pick a refactoring task you've been putting off — something with more than two or three files involved. Write a precise prompt (specify what to leave alone as much as what to change), let Copilot scan, push back on the first draft, edit the Markdown, then implement.

The extra five minutes at the planning stage consistently saves a longer cleanup later.

---

The full article — complete before/after code for the Dataverse plugin scenario, four detailed prompt patterns with examples, and links to all official Microsoft documentation — is at:

👉 **[Think Before You Build: GitHub Copilot's Plan Agent in Visual Studio — aidevme.com](https://aidevme.com/think-before-you-build-github-copilots-plan-agent-in-visual-studio-structured-ai-assisted-development/)**

---

*I write about Power Platform architecture, agentic AI patterns, and developer tooling for enterprise teams. If this was useful, consider sharing it with a colleague who's been burned by Agent mode going sideways.*
