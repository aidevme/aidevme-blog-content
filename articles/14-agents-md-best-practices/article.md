# agents.md Best Practices: The Complete Developer Playbook

Estimated reading time: 14 minutes

Your AI agent just pushed a commit that touched three files it was never supposed to touch. Sound familiar?

The problem isn’t GitHub Copilot. It isn’t the model. It’s the missing operating manual — and following `agents.md` best practices is the fastest way to fix it. After analyzing over 2,500 public repositories, GitHub found a stark divide: agents with structured configuration files consistently outperform those running on vague, one-line personas. The difference between an agent that works and one that guesses isn’t intelligence. It’s instructions.

This guide breaks down exactly what those high-performing configurations look like — the six structural pillars that separate reliable agents from unpredictable ones, a ready-to-use Dataverse plugin agent template for Power Platform developers, and the one maintenance habit that keeps your agent sharp as your codebase evolves.

If you’ve ever thought *“this agent should know better by now”* — this is the article you needed six months ago.

## Table of contents

-   [The Problem Nobody Talks About: Your AI Agent Is Flying Blind](https://aidevme.com/agents-md-best-practices/#h-the-problem-nobody-talks-about-your-ai-agent-is-flying-blind)

-   [What Is agents.md — And Why Does It Exist?](https://aidevme.com/agents-md-best-practices/#h-what-is-agents-md-and-why-does-it-exist)
-   [The Six Pillars of a High-Performing agents.md File](https://aidevme.com/agents-md-best-practices/#h-the-six-pillars-of-a-high-performing-agents-md-file)
    -   [1\. Executable Commands — Put Them First](https://aidevme.com/agents-md-best-practices/#h-1-executable-commands-put-them-first)
    -   [2\. Code Examples Over Written Explanations](https://aidevme.com/agents-md-best-practices/#h-2-code-examples-over-written-explanations)
    -   [3\. Three-Tier Boundaries: Always / Ask First / Never](https://aidevme.com/agents-md-best-practices/#h-3-three-tier-boundaries-always-ask-first-never)
    -   [4\. Specific Stack Information With Versions](https://aidevme.com/agents-md-best-practices/#h-4-specific-stack-information-with-versions)
    -   [5\. Project Structure — With Purpose, Not Just Paths](https://aidevme.com/agents-md-best-practices/#h-5-project-structure-with-purpose-not-just-paths)
    -   [6\. Git Workflow and Commit Standards](https://aidevme.com/agents-md-best-practices/#h-6-git-workflow-and-commit-standards)
-   [Building Your First Specialist Agent: A Practical Walkthrough](https://aidevme.com/agents-md-best-practices/#h-building-your-first-specialist-agent-a-practical-walkthrough)

-   [The agents.md Ecosystem: Which File Should You Use?](https://aidevme.com/agents-md-best-practices/#h-the-agents-md-ecosystem-which-file-should-you-use)
-   [The Five Agents Worth Building Right Now](https://aidevme.com/agents-md-best-practices/#h-the-five-agents-worth-building-right-now)

-   [The Hidden Benefit: agents.md Forces Better Documentation](https://aidevme.com/agents-md-best-practices/#h-the-hidden-benefit-agents-md-forces-better-documentation)
-   [Maintenance: The Part Most Guides Skip](https://aidevme.com/agents-md-best-practices/#h-maintenance-the-part-most-guides-skip)

-   [Quick-Start Template: Dataverse Plugin Agent](https://aidevme.com/agents-md-best-practices/#h-quick-start-template-dataverse-plugin-agent)
-   [Key Takeaways](https://aidevme.com/agents-md-best-practices/#h-key-takeaways)
    -   [What is the difference between agents.md and copilot-instructions.md?](https://aidevme.com/agents-md-best-practices/#h-what-is-the-difference-between-agents-md-and-copilot-instructions-md)
    -   [Does Claude Code support AGENTS.md?](https://aidevme.com/agents-md-best-practices/#h-does-claude-code-support-agents-md)
    -   [Where exactly do I place agents.md files in my repository?](https://aidevme.com/agents-md-best-practices/#h-where-exactly-do-i-place-agents-md-files-in-my-repository)
    -   [How often should I update my agents.md file?](https://aidevme.com/agents-md-best-practices/#h-how-often-should-i-update-my-agents-md-file)
    -   [Is the AGENTS.md open standard officially endorsed by Microsoft?](https://aidevme.com/agents-md-best-practices/#h-is-the-agents-md-open-standard-officially-endorsed-by-microsoft)
-   [References](https://aidevme.com/agents-md-best-practices/#h-references)

-   [Your Turn — Let’s Talk About It](https://aidevme.com/agents-md-best-practices/#h-your-turn-let-s-talk-about-it)

## The Problem Nobody Talks About: Your AI Agent Is Flying Blind

You’ve integrated GitHub Copilot into your workflow. You’ve assigned tasks, watched it spin up pull requests, and marveled at how far agentic AI has come. But somewhere along the way, results got inconsistent. The agent touched files it shouldn’t have, missed your coding conventions, and produced output that looked technically correct but felt wrong for your project.

The culprit, more often than not, isn’t the model. It’s the missing operating manual.

GitHub’s analysis of over 2,500 public repositories carrying `agents.md` files reveals a pattern that’s hard to ignore: the repositories producing the best agentic results aren’t relying on better prompts at task time. They’re doing the hard work up front, encoding their project’s DNA into a structured configuration file that every AI coding agent can read before touching a single line of code.

This guide walks through everything you need to know to build agents that actually work — from the anatomy of a high-performing `agents.md` file to the emerging open standard that’s reshaping how AI tools interact with your codebase.

## What Is agents.md — And Why Does It Exist?

At its core, an `agents.md` file is exactly what it sounds like: a README written for AI agents rather than human developers. Understanding `agents.md` best practices starts here. Where your `README.md` explains what the project does to a person cloning the repo for the first time, `agents.md` explains *how to work on it* to an AI that’s about to autonomously modify it.

The concept emerged from a real fragmentation problem. Every major AI coding assistant wanted its own configuration file. GitHub Copilot expected `.github/copilot-instructions.md`. Claude Code used `CLAUDE.md`. Cursor read `.cursorrules`. Windsurf had `.windsurfrules`. Teams maintaining more than one AI tool in their workflow were duplicating the same instructions in three or four formats, each one gradually drifting out of sync with the actual codebase.

AGENTS.md was conceived as a collaborative open standard — initially driven by Sourcegraph, then adopted by OpenAI, Google, and a growing ecosystem of AI coding platforms — to serve as a single instruction file that all tools can understand. GitHub Copilot’s coding agent added formal support in August 2025, and today the standard is recognized by Cursor, Amp, Windsurf, Gemini CLI, RooCode, Warp, Zed, and dozens of others.

Think of AGENTS.md as a README for agents: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project. README.md files are for humans. AGENTS.md complements this by containing the extra, sometimes detailed context coding agents need — build steps, tests, and conventions that might clutter a README or aren’t relevant to human contributors.

## The Six Pillars of a High-Performing agents.md File

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/02/stop-writing-vague-ai-prompts-the-developers-playbook-for-mastering-agents-6-pillars.png?resize=1536%2C1024&ssl=1)

GitHub’s analysis of over 2,500 repositories identified a clear divide between agent configurations that produce reliable, high-quality output and those that don’t. The top-performing files consistently hit six areas. Miss more than two, and your agent is guessing.

### 1\. Executable Commands — Put Them First

The single most impactful thing you can add to your `agents.md` is a list of the commands your agent should actually run. Not “run tests.” Not “build the project.” The exact commands with flags and options:

Bash

```
npm test -- --coverage
npm run build
npx markdownlint docs/
pytest -v --tb=short
```

Agents reference these constantly. Putting them in an early section means they’re loaded into context before anything else. An agent that can’t validate its own work — can’t run the test suite, can’t check if the TypeScript compiles — is an agent flying blind after every change.

### 2\. Code Examples Over Written Explanations

One real snippet showing your conventions beats three paragraphs describing them. If your team uses a specific pattern for error handling, show it. If you have a naming standard for React hooks, illustrate it with an actual example from the codebase. Agents are remarkably good at inferring style from examples; they’re less reliable at interpreting abstract descriptions.

### 3\. Three-Tier Boundaries: Always / Ask First / Never

This is the safety layer that prevents your agent from doing something irreversible. GitHub’s research found that “never commit secrets” was the single most common boundary across successful agent files — which tells you how often agents get this wrong when not explicitly constrained.

A three-tier boundary model gives agents graduated guidance:

-   **Always do:** Write to `docs/`, run linting before commits, follow naming conventions**.**

-   **Ask first:** Major changes to existing documents, adding new dependencies, modifying CI/CD config**.**
-   **Never do:** Modify source code from the docs agent, touch `node_modules/`, commit API keys or secrets

### 4\. Specific Stack Information With Versions

“React project” tells your agent almost nothing. “React 18 with TypeScript 5.2, Vite 5, and Tailwind CSS 3.4” tells it exactly which APIs are available, which deprecations to avoid, and which idioms to prefer. Include your key dependencies and their versions. Agents use this to make decisions about everything from import paths to which test utilities to reach for.

### 5\. Project Structure — With Purpose, Not Just Paths

Rather than a flat directory listing, explain what each directory *does* and which ones the agent should read from versus write to. This is especially critical for specialized agents. A docs agent should know that `src/` is read-only context and `docs/` is its workspace. A test agent needs to know where tests live and whether integration tests are separate from unit tests.

For large codebases, be cautious about documenting file paths directly. File paths change constantly. If your AGENTS.md says “authentication logic lives in src/auth/handlers.ts” and that file gets renamed or moved, the agent will confidently look in the wrong place. Instead of documenting structure, describe capabilities and let the agent navigate.

### 6\. Git Workflow and Commit Standards

Does your team use conventional commits? Do you require a specific PR description format? Are there branch naming conventions? An agent that pushes a commit with the message “fix stuff” in a repo that enforces `feat(auth): add OAuth2 support` is going to cause friction, even if the code itself is correct.

## Building Your First Specialist Agent: A Practical Walkthrough

The most common mistake developers make when creating their first `agents.md` is trying to build a general-purpose helper. The data from GitHub’s repository analysis is clear: specialist agents outperform generalists. Pick one job.

Here’s a minimal but production-ready `docs-agent.md` placed at `.github/agents/docs-agent.md`:

Markdown

```
---
name: docs_agent
description: Expert technical writer for this project
---

You are an expert technical writer for this project.

## Your role
- You are fluent in Markdown and can read TypeScript code

- You write for a developer audience, focusing on clarity and practical examples
- Your task: read code from `src/` and generate or update documentation in `docs/`

## Project knowledge
- **Tech Stack:** React 18, TypeScript, Vite, Tailwind CSS

- **File Structure:**
  - `src/` – Application source code (you READ from here)
  - `docs/` – All documentation (you WRITE to here)

## Commands you can use
Build docs: `npm run docs:build`
Lint markdown: `npx markdownlint docs/`

## Boundaries
- Always do: Write to `docs/`, run markdownlint after changes

- Ask first: Major restructuring of existing documents
- Never do: Modify code in `src/`, edit config files, commit secrets
```

Notice what this file does well: it states a clear persona, gives the agent runnable commands for self-validation, distinguishes read-only from write-allowed directories, and sets explicit boundaries. There’s no ambiguity about what this agent is supposed to do or where it’s allowed to operate.

## The agents.md Ecosystem: Which File Should You Use?

If you’re working with multiple AI tools — which most professional developers are — you’ll quickly encounter the question of whether to maintain separate configuration files for each tool or consolidate into AGENTS.md.

VS Code’s guidance is practical: start with a single `.github/copilot-instructions.md` file for project-wide coding standards, add `.instructions.md` files when you need different rules for different file types or frameworks, and use AGENTS.md if you work with multiple AI agents in your workspace.

For teams using both Claude Code and GitHub Copilot, the recommended approach is to use both files together: create your main instructions in AGENTS.md for universal compatibility, then have CLAUDE.md reference it with a single import line. This pattern gives you the best of both worlds — universal compatibility via AGENTS.md, plus Claude-specific features via CLAUDE.md.

GitHub Copilot’s coding agent supports AGENTS.md alongside `.github/copilot-instructions.md`, `.github/instructions/**.instructions.md`, `CLAUDE.md`, and `GEMINI.md` — so existing configurations are not disrupted by adopting the standard.

## The Five Agents Worth Building Right Now

Based on GitHub’s research into what teams are actually building, these five agent types deliver the highest return on configuration investment:

**@docs-agent** reads your source code and writes documentation to a dedicated `docs/` directory. Give it `npm run docs:build` and `markdownlint` commands so it can validate its own output. Never let it touch `src/`.

**@test-agent** writes and extends the test suite. It needs to know your test framework (Jest, PyTest, Playwright, Vitest), the command to run tests, and most importantly: it can never delete a failing test. It can only write new tests or fix broken ones.

**@lint-agent** handles code style and formatting. This is one of the safest agents to deploy because linters are designed to be deterministic. Give it `eslint --fix` and `prettier --write`, and constrain it to style changes only — never logic.

**@api-agent** builds REST endpoints and GraphQL resolvers. It needs to know your framework (Express, FastAPI, NestJS), where routes live, and the command to start the dev server for manual verification. Critical boundary: it can modify routes but must ask before touching database schemas.

**@security-agent** audits code for common vulnerabilities, checks for hardcoded secrets, and reviews dependency versions. This one should have read-only access to the entire codebase and write access only to a `security-reports/` directory.

Here’s something the GitHub research surfaced that’s worth sitting with: what early AGENTS.md adopters discovered is that the content of a good AGENTS.md file looks exactly like the documentation that should have been in the README all along. After explaining project context to AI agents repeatedly, developers finally wrote the comprehensive documentation they’d been avoiding for years.

This isn’t a side effect. It’s the mechanism. What’s framed as “for the AI” ends up being good for engineering too: the same structure that improves AI assistants also reduces duplication, saving teams from copy-pasting the same instructions across tools. Instead of documentation being a chore with a distant or uncertain reward, AGENTS.md makes it a direct productivity boost.

The discipline of writing precise, executable instructions for an AI agent — instructions that will be tested automatically every time the agent runs — creates accountability that optional human documentation never had. If your `agents.md` says “run `npm test` and all tests should pass before committing,” that instruction gets verified constantly. Your README saying “make sure tests pass” gets read once by each new developer and then ignored.

## Maintenance: The Part Most Guides Skip

Creating an `agents.md` file is straightforward. Keeping it accurate as your codebase evolves is where most teams fail.

The hard part isn’t writing these files. It’s keeping them accurate as the codebase evolves. Bootstrapping documentation is trivial — ask Claude Code to run `/init` and you get a `CLAUDE.md` file in seconds. But this creates an illusion of completeness. The file exists, it has content, it looks professional. Meanwhile, the codebase moves on.

Common drift patterns to watch for:

-   Node.js version requirements in your config that don’t match your current `package.json`.

-   File paths pointing to modules that have been renamed or moved.
-   Build commands that have changed as your toolchain evolved.

-   Test framework references after migrating from Jest to Vitest (or vice versa)

Treat your `agents.md` as living code, not documentation. Subject it to code review when you make architectural changes. When a new framework is introduced, update the stack section. When a directory is reorganized, update the file structure section. The agent will only be as reliable as the operating manual you maintain for it.

## Quick-Start Template: Dataverse Plugin Agent

For those of us working in the Microsoft Power Platform ecosystem, here’s a production-ready template that accounts for the specific tooling and conventions of enterprise Dataverse plugin development:

Markdown

```
---
name: dataverse_plugin_agent
description: Dataverse Plugin developer — writes, registers, and tests IPlugin implementations for this solution
---

You are a senior Dataverse Plugin developer with deep knowledge of the Microsoft.Xrm.Sdk framework,
the Plugin Registration Tool, and enterprise-grade C# development practices for Power Platform.

## Your role
- Write IPlugin implementations that are stateless, exception-safe, and solution-aware

- Generate unit tests using FakeXrmEasy or the Microsoft.Xrm.Sdk.Fakes test harness
- Assist with plugin step registration metadata (message, entity, stage, mode)

- Identify and fix common plugin anti-patterns: static fields, blocking calls, missing null checks

## Tech stack
- .NET 4.6.2 / .NET 6 (NuGet: Microsoft.CrmSdk.CoreAssemblies 9.x)

- FakeXrmEasy 2.x for unit testing
- PAC CLI for solution export/import

- Plugin Registration Tool (PRT) for step registration

## Commands
Build:      `dotnet build --configuration Release`
Test:       `dotnet test --logger trx --results-directory TestResults/`
Pack:       `dotnet publish -c Release -o ./dist`
Deploy:     `pac plugin push --solution-zip ./dist/MyPlugin.zip`
Export sol: `pac solution export --name MySolution --path ./solutions/ --managed false`

## Code style example

Correct — stateless, early exit, typed service usage:
```csharp
public class AccountPreValidatePlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)
            serviceProvider.GetService(typeof(IPluginExecutionContext));

        if (context.MessageName != "Create" || context.Stage != 10) return;

        var tracingService = (ITracingService)
            serviceProvider.GetService(typeof(ITracingService));

        if (!context.InputParameters.TryGetValue("Target", out var raw)
            || raw is not Entity target)
        {
            tracingService.Trace("Target missing or wrong type — aborting.");
            return;
        }

        var name = target.GetAttributeValue<string>("name");
        if (string.IsNullOrWhiteSpace(name))
            throw new InvalidPluginExecutionException("Account name is required.");

        tracingService.Trace($"Pre-validate passed for account: {name}");
    }
}
```

Wrong — static state, missing null checks, swallowed exceptions:
```csharp
public class BadPlugin : IPlugin
{
    private static IOrganizationService _service; // never use static fields

    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)
            serviceProvider.GetService(typeof(IPluginExecutionContext));
        var target = (Entity)context.InputParameters["Target"]; // no null check
        try { /* ... */ } catch (Exception) { } // never swallow exceptions
    }
}
```

## File structure
- `src/Plugins/`         – IPlugin implementations (you WRITE here)

- `src/Plugins.Tests/`   – FakeXrmEasy unit tests (you WRITE here)
- `solutions/`           – Exported solution ZIPs (READ ONLY — never edit manually)

- `docs/plugin-steps.md` – Step registration reference (READ ONLY)

## Plugin step registration conventions
| Message     | Entity        | Stage         | Mode        | Use case                        |
|-------------|---------------|---------------|-------------|---------------------------------|
| Create/Update | account, contact | PreValidation (10) | Synchronous | Field validation                |
| Create/Update | account       | PreOperation (20) | Synchronous | Default value injection         |
| Create       | opportunity   | PostOperation (40) | Asynchronous | Fire-and-forget side effects   |

## Boundaries
- Always: Keep plugins stateless, add ITracingService tracing, write a matching unit test per plugin class

- Always: Throw InvalidPluginExecutionException for business rule violations (never Exception)
- Ask first: Changing plugin isolation mode, adding new NuGet dependencies, modifying solution structure

- Never: Use static fields or properties, perform synchronous HTTP calls inside plugin execution, touch the `solutions/` folder directly
- Never: Hardcode organization URLs, user IDs, or connection strings anywhere in plugin code
```

## Key Takeaways

The shift from general-purpose AI assistants to configured specialist agents is one of the most impactful workflow changes available to developers right now. The configuration overhead is low — a well-structured `agents.md` takes an afternoon to write and months to pay dividends.

Start with one agent. Make it a specialist. Give it commands it can actually run, show it what good output looks like with real examples, set explicit boundaries, and specify your tech stack with versions. Test it. Then iterate.

The best `agents.md` files in GitHub’s analysis didn’t arrive fully formed. They grew through iteration — developers noticing where agents made mistakes, adding constraints, and gradually building a configuration that matched how their team actually works.

That’s the process. Not upfront perfection, but continuous refinement of a living document that makes your AI collaborators progressively more reliable.

## Frequently Asked Questions

### What is the difference between agents.md and copilot-instructions.md?

`copilot-instructions.md` (placed at `.github/copilot-instructions.md`) is an always-on file that sets project-wide norms for *all* Copilot interactions — chat, code review, and the coding agent. `agents.md` is the emerging cross-tool open standard that works across GitHub Copilot, Cursor, Windsurf, Gemini CLI, and others. If you only use GitHub Copilot, either file works. If you use multiple AI tools, `AGENTS.md` is the better choice because you maintain one file instead of several. GitHub Copilot’s coding agent reads both.

### Does Claude Code support AGENTS.md?

Not natively as of early 2026 — Claude Code uses `CLAUDE.md` as its primary configuration file. The recommended workaround is to maintain your full instructions in `AGENTS.md` and have `CLAUDE.md` reference it with a single import line (`See AGENTS.md for detailed project instructions`). This gives you universal compatibility via AGENTS.md while keeping Claude-specific extensions in CLAUDE.md.

### Where exactly do I place agents.md files in my repository?

There are two main scopes. For repository-level agents, place the file at `.github/agents/YOUR-AGENT-NAME.md`. For organization or enterprise-wide agents available across all repositories, place it at `/agents/YOUR-AGENT-NAME.md` inside your org’s `.github` or `.github-private` repository. A root-level `AGENTS.md` (capital letters) at the repository root is also recognized by the open standard and acts as always-on project context for any compatible tool.

### How often should I update my agents.md file?

Treat it like code, not documentation. The practical rule: review and update your `agents.md` whenever you make an architectural change, introduce a new framework or library, rename or reorganize directories, or change your build and test commands. Stale context is worse than no context — an agent that confidently navigates to a file path that no longer exists will fail silently and waste tokens on every task.

### Is the AGENTS.md open standard officially endorsed by Microsoft?

Microsoft has not formally endorsed AGENTS.md as a standard, but GitHub (a Microsoft subsidiary) added support for it in the Copilot coding agent in August 2025 — alongside their own `.github/copilot-instructions.md` format. VS Code’s documentation explicitly recommends AGENTS.md for developers working with multiple AI agents. The standard is gaining broad industry support: OpenAI, Google, Sourcegraph, Cursor, and dozens of other platforms have all added compatibility.

## References

**Primary Sources**

-   **GitHub Blog** — [*How to write a great agents.md: Lessons from over 2,500 repositories* (Matt Nigh, November 2025)](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)

-   **GitHub Changelog** — [*Custom agents for GitHub Copilot* (October 2025)](https://github.blog/changelog/2025-10-28-custom-agents-for-github-copilot/)
-   **GitHub Changelog** — [*Copilot coding agent now supports AGENTS.md custom instructions* (August 2025)](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)

-   **GitHub Blog** — [*Your stack, your rules: Introducing custom agents in GitHub Copilot* (December 2025)](https://github.blog/news-insights/product-news/your-stack-your-rules-introducing-custom-agents-in-github-copilot-for-observability-iac-and-security/)

**Official Documentation**

-   **GitHub Docs** — *[About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)*

-   **GitHub Docs** — *[Creating custom agents for Copilot coding agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)*
-   **GitHub Docs** — *[Best practices for using GitHub Copilot to work on tasks](https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/best-practices-for-using-copilot-to-work-on-tasks)*

-   **VS Code Docs** — *[Use custom instructions in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)*

**Open Standard & Community**

-   **AGENTS.md [*Open Standard*](https://agents.md/)**

-   **Substratia** — [*AGENTS.md vs CLAUDE.md: Complete Guide to AI Agent Configuration* (January 2026)](https://substratia.io/blog/agents-md-vs-claude-md/)
-   **AI Hero** — *[Complete Guide to AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md)*

-   **Tessl.io** — [*The Rise of AGENTS.md: An Open Standard and Single Source of Truth for AI Coding Agents* (September 2025)](https://tessl.io/blog/the-rise-of-agents-md-an-open-standard-and-single-source-of-truth-for-ai-coding-agents/)
-   **Packmind** — [*Writing AI coding agent context files is easy. Keeping them accurate isn’t.* (February 2026)](https://packmind.com/evaluate-context-ai-coding-agent/)

-   **Upsun Developer Center** — [*AGENTS.md: Why your README matters more than AI configuration files* (August 2025)](https://devcenter.upsun.com/posts/why-your-readme-matters-more-than-ai-configuration-files/)
-   **Layer5** — *[AGENTS.md: One File to Guide Them All](agents.md: One File to Guide Them All)*[https://layer5.io/blog/ai/agentsmd-one-file-to-guide-them-all/](https://layer5.io/blog/ai/agentsmd-one-file-to-guide-them-all/)

-   **GitHub Community Discussion** — *[What differentiates Custom Agents, Agent Skills and Custom Instructions in Copilot CLI](https://github.com/orgs/community/discussions/183962)*

## Your Turn — Let’s Talk About It

I’ve shared what GitHub’s data says and what works in my own Power Platform projects. But the real gold is always in the trenches — the edge cases, the anti-patterns, the configurations that surprised you.

**A few questions I’d genuinely love to hear your take on:**

-   Have you already started using `agents.md` or `copilot-instructions.md` in your projects? What was your biggest “aha moment” — or your biggest frustration?

-   Which of the six pillars made the most immediate difference when you added it? My bet is on executable commands, but I’ve been wrong before.
-   Are you managing multiple AI tools (Copilot + Claude Code + Cursor) in the same repo? How are you handling the fragmentation — one `AGENTS.md` to rule them all, or separate files per tool?

-   For those of you building on Dataverse and Power Platform — are you using the Copilot coding agent for plugin work yet, or does the sandboxed execution environment still feel too risky for production plugin changes?
-   What’s the worst thing an unconfigured agent has done to your codebase? No judgment — we’ve all been there.

Drop your answers in the comments below. If you’ve built an `agents.md` setup you’re particularly proud of — or one that spectacularly failed — share it. The community learns fastest from real examples, not polished demos.

And if this article saved you from a bad agent experience (or gave you the push to finally write that configuration file), share it with a colleague who’s still letting their agent fly blind. They’ll thank you later.

### *Related*

[![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform-featured.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/ "The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform")

#### [The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/ "The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform")

GitHub Copilot CLI Autopilot mode reached GA in February 2026 — but for Power Platform, autonomous PAC CLI execution carries real risk. This article builds a scored Risk Decision Matrix mapping every PAC CLI operation to one of four zones: full Autopilot, conditional, Plan Mode only, or human-only. Includes a…

March 10, 2026

In "AI & Copilot"

---
> **Note:** This page contains 3 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [Stop Writing Vague AI Prompts: The Developer’s Playbook for Mastering agents.md in 2026](https://aidevme.com/agents-md-best-practices/)