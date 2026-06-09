# Think Before You Build: GitHub Copilot's Plan Agent in Visual Studio — Structured AI-Assisted Development

Estimated reading time: 12 minutes

GitHub Copilot's Plan agent, introduced in Visual Studio in May 2026, adds a deliberate planning phase before any code generation happens. Instead of watching AI modify files in unpredictable directions, you review and approve a detailed Markdown plan grounded in your actual codebase — before a single file changes. This guide covers how the Plan agent works step by step, how to write prompts that produce genuinely useful plans, and how to apply it to a real Dataverse plugin refactoring scenario with working before-and-after code examples.

---

## Table of contents

- [The Problem With "Just Build It"](#the-problem-with-just-build-it)
- [How the Plan Agent Works: Step by Step](#how-the-plan-agent-works-step-by-step)
  - [Phase 1 — Describe Your Intent](#phase-1--describe-your-intent)
  - [Phase 2 — Copilot Scans Your Codebase (Read-Only)](#phase-2--copilot-scans-your-codebase-read-only)
  - [Phase 3 — The Plan Is Drafted](#phase-3--the-plan-is-drafted)
  - [Phase 4 — You Edit the Plan Directly](#phase-4--you-edit-the-plan-directly)
  - [Phase 5 — Implement](#phase-5--implement)
- [Writing Better Prompts for the Plan Agent](#writing-better-prompts-for-the-plan-agent)
- [A Real-World Scenario: Power Platform Plugin Refactor](#a-real-world-scenario-power-platform-plugin-refactor)
- [The Plan File as a Living Document](#the-plan-file-as-a-living-document)
- [Where This Fits in Your Development Loop](#where-this-fits-in-your-development-loop)
- [Summary](#summary)

---

We've all been there. You fire up GitHub Copilot in Agent mode, describe a feature, and watch it start modifying files across your solution. Ten minutes later you're staring at a cascade of changes that technically compile — but head in entirely the wrong direction. The AI wasn't wrong. *You* just weren't aligned with it before it started.

This isn't a criticism of agentic AI — it's a structural limitation of how it has worked up to now. Agent mode is optimised for *doing*. The moment you describe a task, the model starts gathering context and generating changes. For small, well-bounded tasks that's exactly the right behaviour. For anything larger — a multi-file refactor, a new integration layer, a significant architecture change — the absence of an explicit alignment step is where things go sideways.

Microsoft introduced the **Plan agent** in Visual Studio in May 2026 — a dedicated GitHub Copilot agent that puts a deliberate planning phase *before* any code generation happens. It scans your codebase in read-only mode, asks targeted clarifying questions, and produces a detailed step-by-step Markdown plan that you can review, edit, and approve before a single file is touched. Only after you explicitly trigger implementation does the agent mode take over and execute the plan.

For those of us building complex enterprise solutions on Power Platform, Dynamics 365, or .NET backends, this is a meaningful shift. Not because it makes the AI smarter — the underlying model is the same — but because it makes the *collaboration* smarter. You're not reviewing a diff after the fact and trying to reverse decisions you didn't make. You're reviewing a plan *before* the decisions are executed, while the cost of changing your mind is still zero.

Think of it as the difference between an architect showing you blueprints versus a contractor arriving with half the walls already framed. The end result might be technically sound either way. But one of those conversations is much easier to have.

In this article I'll walk through exactly how the Plan agent works — the five-phase workflow, what a real plan output looks like, how to write prompts that produce genuinely useful plans, and a complete before-and-after example from a Dataverse plugin refactoring scenario. If you've been using GitHub Copilot Agent mode and occasionally found yourself cleaning up after it, this feature is directly aimed at the problem you've been experiencing.

---

## The Problem With "Just Build It"

Agent mode has been a game-changer, but it has an inherent tension: the moment you describe something to Copilot, it wants to *build* it. That eagerness is great for small, well-scoped tasks. For larger features — refactoring a module, wiring up a new integration, redesigning a service layer — jumping straight to implementation is risky.

Consider this pattern that many of us have experienced:

```
You:     "Add retry logic to all Dataverse API calls in the service layer."
Copilot: [modifies 12 files, introduces Polly, changes interface signatures,
          updates DI registration, adds new config keys...]
You:     "Wait — we already use a custom HttpClient factory with retry built in.
          I just needed it applied to the OrganizationServiceProxy calls."
```

The AI wasn't wrong about *how* to add retry logic. It was wrong about *where* you needed it, because neither of you paused to agree on scope before acting.

The Plan agent inserts a structured **plan-first loop** that makes this kind of misalignment visible before a single file is touched.

---

## How the Plan Agent Works: Step by Step

The workflow lives inside the Copilot Chat panel. From the **agent picker**, you select **Plan** instead of **Agent**, then describe your task. Here's what happens next.

### Phase 1 — Describe Your Intent

Your prompt is the starting point. The Plan agent handles both vague and precise requests, but the specificity of your prompt affects how many clarifying questions it asks.

**Vague prompt** (expect more questions):
```
Add authentication to the portal API.
```

**Precise prompt** (faster to draft):
```
Add JWT bearer token validation to the ASP.NET Core middleware pipeline
in the CustomerPortal.Api project. Tokens are issued by our Entra ID
tenant. Use Microsoft.Identity.Web. Do not modify the existing
ClaimsTransformation logic.
```

For complex enterprise work, a precise prompt is almost always worth the extra 30 seconds to write. It dramatically reduces the number of clarifying rounds.

---

### Phase 2 — Copilot Scans Your Codebase (Read-Only)

Before asking anything, Copilot reads your solution using **read-only tools only** — no writes, no changes. It looks at:

- Project structure and solution layout
- Existing service registrations and DI configuration
- Interface definitions and existing implementations
- Relevant configuration files (e.g., `appsettings.json`, `*.csproj`)
- NuGet package references

This is important: the plan it produces will be grounded in *your* codebase, not a generic template. For Power Platform developers working with PAC CLI projects, plugin assemblies, or multi-solution repositories, this means Copilot will understand your actual project layout before it proposes anything.

After scanning, it asks clarifying questions where it finds ambiguity:

```
Copilot: I found two projects that expose API endpoints:
         - CustomerPortal.Api
         - InternalAdmin.Api

         Should JWT validation apply to both, or only CustomerPortal.Api?

         I also see that InternalAdmin.Api uses Windows Authentication.
         Do you want to leave that unchanged?
```

Answer these questions directly in chat. Each answer narrows the scope of the plan.

---

### Phase 3 — The Plan Is Drafted

Once Copilot has enough context, it generates a detailed step-by-step implementation plan. Here's an example of what a real plan looks like for a Dataverse plugin scenario.

**Prompt given:**
```
Refactor the AccountSyncPlugin to use a service class pattern.
Extract business logic out of the IPlugin.Execute method into a
testable AccountSyncService. Add constructor injection via a
factory interface so we can unit test without live Dataverse calls.
```

**Example plan output (saved to `.copilot/plans/plan-accountsync-refactor.md`):**

```markdown
# Plan: AccountSyncPlugin Service Class Refactor

## Goal
Extract business logic from AccountSyncPlugin.Execute() into a
testable AccountSyncService class, introducing a factory interface
for dependency injection in unit tests.

## Affected Files
- src/Plugins/AccountSyncPlugin.cs (modify)
- src/Services/AccountSyncService.cs (create)
- src/Services/IAccountSyncService.cs (create)
- src/Factories/IOrganizationServiceFactory.cs (create)
- src/Factories/OrganizationServiceFactory.cs (create)
- tests/Plugins/AccountSyncPluginTests.cs (create)
- tests/Services/AccountSyncServiceTests.cs (create)

## Steps

### Step 1 — Create IOrganizationServiceFactory
Define an interface that wraps IOrganizationService creation so
unit tests can inject a mock:

```csharp
public interface IOrganizationServiceFactory
{
    IOrganizationService CreateOrganizationService(Guid userId);
}
```

### Step 2 — Create IAccountSyncService
Define the service interface exposing the sync operation:

```csharp
public interface IAccountSyncService
{
    void SyncAccount(Entity account, IOrganizationService service);
}
```

### Step 3 — Implement AccountSyncService
Move all business logic from AccountSyncPlugin.Execute() into
AccountSyncService.SyncAccount(). The plugin becomes a thin
orchestrator.

### Step 4 — Refactor AccountSyncPlugin
Replace inline logic with a call to IAccountSyncService.
Use a factory constructor for production and a testable
constructor for unit tests (poor man's DI, standard plugin pattern).

### Step 5 — Write Unit Tests
Create AccountSyncServiceTests using Moq to mock
IOrganizationService. Verify sync logic without Dataverse dependency.

## Out of Scope
- IPlugin registration in plugin registration tool
- Changes to other plugins in the solution
- Shared service locator infrastructure

## Open Questions
- Should AccountSyncService be registered in a shared ServiceLocator,
  or remain self-contained per plugin?
```
```

This is a plan you can actually review in a pull request. You can push back on individual steps, ask Copilot to break "Step 3" into sub-steps, or ask it to reconsider the factory pattern if your team uses a different approach.

---

### Phase 4 — You Edit the Plan Directly

Every plan is persisted as a Markdown file at:

```
.copilot/
  plans/
    plan-accountsync-refactor.md
    plan-jwt-auth-middleware.md
```

This means you can:

**Edit in the editor** — Open the file and modify it like any other Markdown document. Add or remove steps, change file paths, add notes. Copilot reads your edits and keeps the chat context in sync.

**Commit to version control** — Add the plan to your PR as documentation of the design decision. Future developers (including you, six months from now) can see *why* the code is structured the way it is.

**Share for team review** — Send the plan to a colleague or architect before implementation begins. Getting sign-off on a Markdown plan is much faster than reviewing a 15-file diff.

**Add constraints as comments:**

```markdown
### Step 3 — Implement AccountSyncService
<!-- CONSTRAINT: Do not use static members. Plugin assembly is shared. -->
<!-- CONSTRAINT: Keep sync logic synchronous — no async/await in plugins. -->
Move all business logic from AccountSyncPlugin.Execute() into
AccountSyncService.SyncAccount().
```

Copilot will respect these inline comments when it implements.

---

### Phase 5 — Implement

When you're satisfied, click **Implement plan**. Agent mode takes over, works through the plan step by step, creates and modifies files, and shows you progress in real time.

The key difference from running Agent mode directly: **you approved the plan first**. The implementation phase is executing a decision you already made, not discovering the decision mid-flight.

---

## Writing Better Prompts for the Plan Agent

Not all prompts produce equally useful plans. Here are patterns that consistently work well.

### Pattern 1 — Scope by Layer, Not by Feature

Instead of:
```
Add caching to the app.
```

Try:
```
Add in-memory caching (IMemoryCache) to the AccountRepository class only.
Cache the GetByExternalId query with a 5-minute sliding expiration.
Do not modify the service layer or the plugin.
```

The more explicit you are about *what to leave alone*, the better the plan scope.

### Pattern 2 — Reference Existing Patterns

```
Refactor CustomerService to follow the same repository pattern
used in OrderService. Look at how OrderRepository uses the
UnitOfWork class and apply the same approach to CustomerRepository.
```

Copilot will scan `OrderService` and `OrderRepository` before drafting — your existing code becomes the template.

### Pattern 3 — Specify Test Coverage Expectations

```
Add a DataverseConnectionManager class that wraps
IOrganizationService initialization. Include unit tests using Moq.
Target at least the happy path and one connection failure scenario.
```

Without this, plans often treat testing as an afterthought. Stating it upfront puts it in the plan.

### Pattern 4 — Use Constraints to Protect Sensitive Areas

```
Add structured logging (Serilog) to the webhook processing pipeline.
Do not modify WebhookController — it is under active development
in a parallel branch. Only touch the WebhookProcessor and
WebhookDispatcher classes.
```

---

## A Real-World Scenario: Power Platform Plugin Refactor

Let me walk through a scenario relevant to most readers here — refactoring a Dataverse plugin for testability.

**Starting point:** A monolithic plugin that does too much.

```csharp
// Before: AccountSyncPlugin.cs — hard to test, business logic mixed with plumbing
public class AccountSyncPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)
            serviceProvider.GetService(typeof(IPluginExecutionContext));
        var serviceFactory = (IOrganizationServiceFactory)
            serviceProvider.GetService(typeof(IOrganizationServiceFactory));
        var service = serviceFactory.CreateOrganizationService(context.UserId);

        // 200 lines of business logic directly here
        var target = (Entity)context.InputParameters["Target"];
        var existingAccount = service.Retrieve("account", 
            target.GetAttributeValue<Guid>("accountid"), 
            new ColumnSet("name", "emailaddress1", "externalid"));

        // sync logic, validation, related record updates...
        // all tangled together with no way to unit test
    }
}
```

**Prompt to the Plan agent:**
```
Refactor AccountSyncPlugin.cs to extract business logic into
a testable AccountSyncService. Introduce IAccountSyncService
and a constructor-injected factory so we can unit test without
live Dataverse calls. Follow the "poor man's DI" pattern standard
for Dataverse plugins. Create unit tests using Moq.
```

**After implementation — the refactored plugin:**

```csharp
// After: AccountSyncPlugin.cs — thin orchestrator
public class AccountSyncPlugin : IPlugin
{
    private readonly IAccountSyncService _syncService;

    // Production constructor — called by Dataverse runtime
    public AccountSyncPlugin()
    {
        _syncService = new AccountSyncService(
            new DataverseOrganizationServiceFactory());
    }

    // Testable constructor — called by unit tests
    internal AccountSyncPlugin(IAccountSyncService syncService)
    {
        _syncService = syncService;
    }

    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)
            serviceProvider.GetService(typeof(IPluginExecutionContext));
        var serviceFactory = (IOrganizationServiceFactory)
            serviceProvider.GetService(typeof(IOrganizationServiceFactory));
        var service = serviceFactory.CreateOrganizationService(context.UserId);

        var target = (Entity)context.InputParameters["Target"];
        _syncService.SyncAccount(target, service);
    }
}
```

```csharp
// After: AccountSyncService.cs — all business logic, fully testable
public class AccountSyncService : IAccountSyncService
{
    private readonly IDataverseOrganizationServiceFactory _factory;

    public AccountSyncService(IDataverseOrganizationServiceFactory factory)
    {
        _factory = factory;
    }

    public void SyncAccount(Entity target, IOrganizationService service)
    {
        var accountId = target.GetAttributeValue<Guid>("accountid");
        var existing = service.Retrieve("account", accountId,
            new ColumnSet("name", "emailaddress1", "externalid"));

        ValidateExternalId(target, existing);
        UpdateRelatedContacts(target, service);
        ApplySyncStatus(target, service);
    }

    private void ValidateExternalId(Entity target, Entity existing) { /* ... */ }
    private void UpdateRelatedContacts(Entity target, IOrganizationService svc) { /* ... */ }
    private void ApplySyncStatus(Entity target, IOrganizationService svc) { /* ... */ }
}
```

```csharp
// After: AccountSyncServiceTests.cs — no live Dataverse needed
[TestClass]
public class AccountSyncServiceTests
{
    private Mock<IOrganizationService> _mockService;
    private Mock<IDataverseOrganizationServiceFactory> _mockFactory;
    private AccountSyncService _sut;

    [TestInitialize]
    public void Setup()
    {
        _mockService = new Mock<IOrganizationService>();
        _mockFactory = new Mock<IDataverseOrganizationServiceFactory>();
        _sut = new AccountSyncService(_mockFactory.Object);
    }

    [TestMethod]
    public void SyncAccount_WithValidExternalId_UpdatesRelatedContacts()
    {
        // Arrange
        var accountId = Guid.NewGuid();
        var target = new Entity("account") { Id = accountId };
        target["externalid"] = "EXT-001";

        var existing = new Entity("account") { Id = accountId };
        existing["externalid"] = "EXT-001";
        existing["name"] = "Contoso Ltd";

        _mockService
            .Setup(s => s.Retrieve("account", accountId, It.IsAny<ColumnSet>()))
            .Returns(existing);

        // Act
        _sut.SyncAccount(target, _mockService.Object);

        // Assert
        _mockService.Verify(
            s => s.Update(It.Is<Entity>(e => e.LogicalName == "contact")),
            Times.AtLeastOnce);
    }

    [TestMethod]
    [ExpectedException(typeof(InvalidPluginExecutionException))]
    public void SyncAccount_WithMismatchedExternalId_ThrowsException()
    {
        var accountId = Guid.NewGuid();
        var target = new Entity("account") { Id = accountId };
        target["externalid"] = "EXT-002"; // different

        var existing = new Entity("account") { Id = accountId };
        existing["externalid"] = "EXT-001"; // original

        _mockService
            .Setup(s => s.Retrieve("account", accountId, It.IsAny<ColumnSet>()))
            .Returns(existing);

        _sut.SyncAccount(target, _mockService.Object);
    }
}
```

The plan agent produced the structure. The implementation agent filled in the code. You reviewed and approved a Markdown plan before any of this landed in your solution.

---

## The Plan File as a Living Document

One underappreciated aspect of the Plan agent is what happens to the `.copilot/plans/` folder over time. Consider a team convention:

```
.copilot/
  plans/
    plan-accountsync-refactor.md       ← completed, committed
    plan-jwt-auth-middleware.md        ← completed, committed
    plan-bulk-import-pipeline.md       ← in progress
    plan-power-pages-auth-redesign.md  ← under review
```

These files become a lightweight **decision log** for your codebase. Add a frontmatter convention and they're even more useful:

```markdown
---
status: completed
implemented: 2026-06-01
author: zsolt
pr: #142
---

# Plan: AccountSync Plugin Refactor
...
```

This is something your team can standardize without any tooling overhead — it's just Markdown in a committed folder.

---

## Where This Fits in Your Development Loop

The Plan agent lives at the *design* end of the development pipeline. Here's how it relates to the other stages:

```
[Plan agent]           ← design & scope alignment
     ↓
[Agent mode / Copilot] ← implementation
     ↓
[Solution Checker]     ← static analysis (Power Platform)
[Unit Tests / CI]      ← automated verification
     ↓
[PR Review]            ← human review of diffs
     ↓
[ALM pipeline / PAC CLI deploy] ← promotion to environment
```

It's not a replacement for any of the downstream checks. A plan won't catch a runtime bug or a missing managed property. But it dramatically increases the likelihood that what gets built is what was intended — which reduces the cost of everything downstream.

---

## Summary

The Plan agent is a practical addition to the GitHub Copilot toolset that addresses a real gap in agentic workflows: the absence of a structured design phase before implementation begins.

For enterprise developers, the benefits are concrete:

- **Plans are editable Markdown** — you stay in control of the design, not just the code review
- **Read-only codebase scanning** — plans are grounded in your actual solution structure
- **No code changes until you approve** — the planning and implementation phases are explicitly separated
- **Plans persist in version control** — your `.copilot/plans/` folder becomes a lightweight decision log

Try it on your next refactoring task. Write a precise prompt, let Copilot scan, push back on the first draft, edit the Markdown directly, then implement. The extra five minutes at the planning stage will save you a much longer cleanup later.

---

*If this was useful, subscribe to the AIDevMe newsletter — I cover Power Platform architecture, agentic AI patterns, and developer tooling for enterprise teams. New articles every week.*

---

*Tags: GitHub Copilot · Visual Studio · Agentic AI · Dataverse · Power Platform · Plugin Development · Developer Tooling*
