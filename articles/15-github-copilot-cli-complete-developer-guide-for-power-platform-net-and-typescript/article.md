# GitHub Copilot CLI Developer Guide: Install, Skills & Workflows

Estimated reading time: 19 minutes

**Target audience:** Power Platform developers, .NET developers, and TypeScript/React developers who want to start using GitHub Copilot CLI as their primary terminal-native AI coding agent.

**What you’ll learn:** How to install and configure Copilot CLI, how to work with its agentic modes, how to extend it with Agent Skills and MCP servers, and how to integrate it into your Power Platform ALM workflow — with practical examples at every step.

**Prerequisites:** A paid GitHub Copilot subscription (Pro, Pro+, Business, or Enterprise). Node.js 18+ installed. Basic familiarity with the command line.

---

## Table of contents

-   [Understanding GitHub Copilot CLI](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-understanding-github-copilot-cli)

-   [Installation and First Launch](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-installation-and-first-launch)
-   [Core Concepts: How the Agent Works](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-core-concepts-how-the-agent-works)

-   [Agentic Modes: Interactive, Plan, and Autopilot](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-agentic-modes-interactive-plan-and-autopilot)
-   [Essential Commands Reference](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-essential-commands-reference)

-   [Choosing Your AI Model](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-choosing-your-ai-model)
-   [Configuring Your Project](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-configuring-your-project)

-   [Working with Agent Skills](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-working-with-agent-skills)
    -   [Skill storage locations](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-skill-storage-locations)
    -   [Writing your first skill](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-writing-your-first-skill)
-   [Installing Skills for Your Developer Profile](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-installing-skills-for-your-developer-profile)
    -   [Install commands](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-install-commands)
    -   [Power Platform Developers](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-power-platform-developers)
    -   [.NET Developers](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-net-developers)
    -   [React / TypeScript Developers](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-react-typescript-developers)
    -   [Azure / DevOps Developers / Engineers](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-azure-devops-developers-engineers)
    -   [MCP Server Builders](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-mcp-server-builders)
    -   [Cross-Role Productivity (Useful for Everyone)](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-cross-role-productivity-useful-for-everyone)
-   [Extending with MCP Servers](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-extending-with-mcp-servers)
    -   [Adding a custom MCP server](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-adding-a-custom-mcp-server)
    -   [What a Dataverse MCP server enables](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-what-a-dataverse-mcp-server-enables)
    -   [Available community MCP servers for Power Platform](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-available-community-mcp-servers-for-power-platform)
-   [Power Platform Integration: Step-by-Step](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-power-platform-integration-step-by-step)
    -   [Step 2: Navigate to your Power Platform repo and initialize](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-step-2-navigate-to-your-power-platform-repo-and-initialize)
    -   [Step 3: Add the Power Platform Skills marketplace](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-step-3-add-the-power-platform-skills-marketplace)
    -   [Step 5: Add Power Platform-specific skills](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-step-5-add-power-platform-specific-skills)
    -   [Step 6: Configure your Dataverse MCP server (optional but recommended)](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-step-6-configure-your-dataverse-mcp-server-optional-but-recommended)
    -   [Step 7: Try your first Power Platform prompt](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-step-7-try-your-first-power-platform-prompt)
    -   [Practical Workflows with Code Examples](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-practical-workflows-with-code-examples)
    -   [Workflow 1: Scaffold a new PAC CLI Power Platform repository](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-workflow-1-scaffold-a-new-pac-cli-power-platform-repository)
    -   [Workflow 2: Scaffold a PCF control](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-workflow-2-scaffold-a-pcf-control)
    -   [Workflow 3: Debug a failing GitHub Actions pipeline](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-workflow-3-debug-a-failing-github-actions-pipeline)
    -   [Workflow 4: Write integration tests for a Power Automate flow](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-workflow-4-write-integration-tests-for-a-power-automate-flow)
    -   [Workflow 5: Use Dataverse MCP for live environment queries](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-workflow-5-use-dataverse-mcp-for-live-environment-queries)
-   [Copilot CLI vs Claude Code](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-copilot-cli-vs-claude-code)

-   [Enterprise Setup for Administrators](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-enterprise-setup-for-administrators)
    -   [Do I need a paid GitHub Copilot subscription to use Copilot CLI?](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-do-i-need-a-paid-github-copilot-subscription-to-use-copilot-cli)
    -   [Can I use GitHub Copilot CLI alongside Claude Code, or do I have to choose one?](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-can-i-use-github-copilot-cli-alongside-claude-code-or-do-i-have-to-choose-one)
    -   [How does PAC CLI authentication work locally vs in GitHub Actions?](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-how-does-pac-cli-authentication-work-locally-vs-in-github-actions)
    -   [How many skills should I install per project?](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-how-many-skills-should-i-install-per-project)
    -   [Do Agent Skills work in VS Code stable?](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-do-agent-skills-work-in-vs-code-stable)
-   [What’s Next — And How to Stay Sharp](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-what-s-next-and-how-to-stay-sharp)

-   [References and Further Reading](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#h-references-and-further-reading)

---

## Understanding GitHub Copilot CLI

GitHub Copilot CLI reached **General Availability on February 25, 2026**, graduating from its September 2025 public preview into a production-ready tool for all paid Copilot subscribers.

It is not a chatbot in a terminal. It is an **autonomous coding agent** — meaning it can plan multi-step tasks, edit files, run shell commands, delegate to specialized sub-agents in parallel, and remember your codebase across sessions, all without leaving the command line.

The key difference from the older `gh copilot suggest` command:

| **Old `gh copilot suggest`** | **GitHub Copilot CLI (new)** |
| **Single command suggestion** | Multi-step autonomous agent |
| **One-shot, no iteration** | Plans, executes, reviews, iterates |
| **No memory** | Cross-session repository memory |
| **No file editing** | Full read/write access to your project |
| **No MCP / plugin support** | Full MCP extensibility, plugin marketplace |

For Power Platform developers specifically, this matters because PAC CLI, solution export/import pipelines, and PCF control toolchains all live at the terminal. Having an agent that understands your Dataverse environment, reads your GitHub Actions workflows, and executes PAC CLI commands on your behalf changes what “developer productivity” means.

## Installation and First Launch

**Install via your preferred package manager**

Bash

```


# npm (all platforms — most portable)
npm install -g @github/copilot

# macOS — Homebrew (auto-updates)
brew install github/tap/copilot

# Windows — WinGet (auto-updates)
winget install GitHub.Copilot

# Linux / CI — shell script (auto-updates)
curl -fsSL https://cli.github.com/packages/copilot/install.sh | sh
```

**Auto-update note:** Homebrew, WinGet, and the shell script installations auto-update. npm requires `npm update -g @github/copilot` to get new versions. Copilot CLI ships frequent updates — staying current matters.

Copilot CLI is also **pre-installed in GitHub Codespaces** and available as a Dev Container Feature if you use container-based development.

**Authenticate and launch**

Bash

```


# Launch Copilot CLI — this triggers browser-based GitHub authentication on first run
copilot
```

On first launch, you will be asked to confirm you trust the files in the current directory. This is a security check — Copilot CLI has read/write/execute access to files in the folder you launched from.

**Verify your installation**

Bash

```


# Check version
copilot --version

# Check available models (confirms authentication worked)
/model

# View your current session context
/context
```

## Core Concepts: How the Agent Works

Before diving into workflows, three concepts are worth internalizing.

**Context window and auto-compaction**

Copilot CLI maintains a rolling context window across your session. When it reaches approximately 95% capacity, it **auto-compacts** — summarizing older history while preserving the most relevant recent context. Sessions can run as long as your task requires, without you manually resetting anything.

**Repository memory (cross-session)**

As you work in a repository over time, Copilot CLI learns and stores facts about your codebase: naming conventions, frequently used patterns, your preferred solution names, environment URLs, team standards. This memory persists when you close the terminal and is loaded automatically the next time you open a session in the same repository. You can inspect it with `/memory show`.

**Progressive tool trust**

By default, Copilot CLI asks for approval before running shell commands and editing files. You can adjust trust levels per session or per project. The recommended approach is to **pre-approve specific tools** rather than granting blanket trust — this keeps you in control while reducing friction for known-safe operations like `pac *` or `npm *`.

## Agentic Modes: Interactive, Plan, and Autopilot

Copilot CLI has three distinct operating modes. Choosing the right one for each task significantly affects quality and safety.

### Interactive mode (default)

The default. You type a prompt, the agent responds with a plan or action, you approve or push back, it continues. Good for most day-to-day work.

Bash

```
copilot
> List all solutions in my dev environment and show their version numbers
```

### Plan mode — `Shift+Tab`

Before writing a single line or running a single command, the agent produces a **structured implementation plan** for your review. You see every step before anything happens.

Bash

```
copilot
> [Press Shift+Tab to enter plan mode]
> Set up a new PCF control named CustomerTimeline for model-driven apps
```

Copilot presents: “Here’s what I plan to do: 1. Run pac pcf init… 2. Install npm dependencies… 3. Build to verify… Approve?” You review and approve before execution begins. Use this for anything irreversible or complex.

### Autopilot mode — `Shift+Tab` twice

Full autonomous execution. The agent plans, executes tools, iterates on errors, and reports back when done. No per-step approval.

Bash

```
copilot
> [Press Shift+Tab twice to enter autopilot mode]
> Write Jest integration tests for our LeadQualification Power Automate flow
```

Use autopilot for well-scoped, lower-risk tasks like writing tests, generating documentation, or refactoring a single file. Reserve it for tasks where the blast radius of a mistake is limited.

### Background delegation — `&` prefix

Prefix any prompt with `&` to delegate the task to GitHub’s cloud coding agent, freeing your local terminal immediately.

Bash

```
> & Export the CustomerPortal solution and create a PR with the unpacked components
```

Later, use `/resume` to pick up the session and review what was done.

## Essential Commands Reference

These are the commands you’ll use most often. All slash commands are available in any active session.

### Navigation and context

| **Command** | **What it does** |
| `**/init**` | Analyze the current repo and generate an `AGENTS.md` file with project context |
| `**/context**` | Show what context (files, memory, skills) is currently loaded |
| `**/memory show**` | Display what Copilot has learned about your repository across past sessions |
| `**/resume**` | Resume a previous session or pick up a background (`&`) task |

### File management and review

| **Command** | **What it does** |
| `**/diff**` | Show all file changes made this session with syntax-highlighted inline diffs |
| `**/review**` | Sanity-check staged or unstaged git changes before committing |
| `**Esc+Esc**` | Undo — rewind all file changes back to a previous session snapshot |
| `**/add-file <path>**` | Add a specific file to the current session context |

### Model and configuration

| **Command** | **What it does** |
| `**/model**` | View and switch AI models mid-session |
| `**/settings**` | View and edit session settings |
| `**/experimental show**` | Preview features currently in development |
| `**/changelog**` | See what’s new in the current version |

### Plugins and skills

| **Command** | **What it does** |
| `**/plugin marketplace add <owner/repo>**` | Register a plugin marketplace |
| `**/plugin install <name>@<marketplace>**` | Install a plugin from a registered marketplace |
| `**/plugin list**` | List installed plugins |
| `/**skills**` | View available Agent Skills for the current project |

### Agents and parallel work

| **Command** | **What it does** |
| `**/fleet <prompt>**` | Run the same task across multiple sub-agents in parallel |
| `**& <prompt>**` | Delegate to cloud coding agent in the background |
| `**/agents**` | Show available custom agent profiles |

## Choosing Your AI Model

Use `/model` at any point in a session to switch models. Different models suit different task types.

| **Model** | **Premium Request Cost** | **Best for** |
| **GPT-5 mini / GPT-4.1** | 0× (free, included) | Quick questions, orientation, cheap exploration |
| **Claude Haiku 4.5** | 0.33× | Fast analysis, file reading, understanding codebases |
| **Claude Sonnet 4.6** | 1× | Most coding tasks — the recommended daily driver |
| **GPT-5.3-Codex** | 1× | Strong for pure code generation, especially Python/JS |
| **Claude Opus 4.6** | 3× | Architecture decisions, complex multi-step reasoning |

**Practical model strategy:**

1.  Start sessions with **Haiku 4.5** for exploration — reading files, understanding the codebase, asking questions.
2.  Switch to **Sonnet 4.6** for generation tasks — writing code, creating workflows, refactoring.
3.  Reach for **Opus 4.6** when you need deeper reasoning — architecture review, complex debugging, designing multi-agent systems

Bash

```
copilot
> [explore the repo first with Haiku]
/model claude-haiku-4-5
> Summarize the solution structure in this repo and list all PAC CLI scripts

> [then switch to Sonnet for the real work]
/model claude-sonnet-4-6
> Now generate a GitHub Actions workflow for automated solution export based on what you found
```

## Configuring Your Project

Two configuration files make every subsequent session in your repository smarter: `AGENTS.md` and `.github/copilot/config.json`.

`AGENTS.md` — project context loaded on every session start

This file tells the agent what kind of project it is working in, every time it starts. Generate a baseline with `/init`, then customize it.

Markdown

```


# AGENTS.md

## Project Overview
Power Platform solution repository for CustomerPortal — a Dynamics 365 Customer Service
customization including model-driven apps, PCF controls, and Power Automate flows.

## Technology Stack
- Power Platform CLI (PAC CLI) for ALM operations

- TypeScript + React for PCF controls (Fluent UI v9 component library)
- GitHub Actions for CI/CD pipelines

- Dataverse as the data platform
- Node.js 20 for scripts and tests

## Environment Naming
- Development: DEV-CustomerPortal (https://devenv.crm.dynamics.com)

- Test: TEST-CustomerPortal (https://testenv.crm.dynamics.com)
- Production: PROD-CustomerPortal (https://prodenv.crm.dynamics.com)

## Branching Strategy
- `main` → triggers export from DEV and commits unpacked solution

- `release/*` → triggers import to TEST with Solution Checker gate
- Tags `v*` → triggers production import (manual approval required)

## Conventions
- Solution unique name: CustomerPortal

- PCF controls namespace: ELCA.CustomerPortal
- Always run `pac solution check` before importing to TEST or PROD

- Use `--async` flag for solution imports to avoid timeouts
```

`.github/copilot/config.json` — pre-approved tools and marketplace registration

JSON

```
{
  "marketplaces": [
    "microsoft/power-platform-skills",
    "github/awesome-copilot"
  ],
  "allowedTools": [
    "shell(pac *)",
    "shell(npm *)",
    "shell(dotnet *)",
    "shell(git *)",
    "shell(bash scripts/*)"
  ],
  "launchMessage": "CustomerPortal Power Platform project. PAC CLI, npm, dotnet, and git are pre-approved. Run /skills to see available Power Platform skills."
}
```

**Security note:** Only pre-approve tools with a limited blast radius. `shell(pac *)` is safe — PAC CLI cannot damage files outside your Dataverse environment. Avoid `shell(rm *)` or `shell(curl *)` in shared config files.

## Working with Agent Skills

Agent Skills are the most powerful customization mechanism in Copilot CLI. A skill is a folder containing a `SKILL.md` file that packages domain knowledge, workflow instructions, and optional scripts into a reusable unit the agent loads automatically when relevant.

### How skills are discovered and loaded

The agent always reads skill names and descriptions from YAML frontmatter — this is lightweight and happens on every session. The full skill body is only loaded when the agent decides it is relevant to your current task. This means you can have many skills installed without paying context cost for all of them at once.

Bash

```
Session start → Load skill metadata (name + description for all installed skills)
               ↓
User prompt → Agent matches prompt to relevant skills
               ↓
Relevant skill → Full SKILL.md body loaded into context
               ↓
Agent follows skill instructions for the task
```

### Skill storage locations

| **Location** | **Scope** |
| `**.github/skills//SKILL.md**` | Project-level — committed to repo, shared with team |
| `**~/.copilot/skills//SKILL.md**` | Personal — available across all your repos |
| `**~/.claude/skills//SKILL.md**` | Personal — also works with Claude Code |

### Writing your first skill

The minimum viable skill is a folder with a `SKILL.md` file:

Bash

```
.github/skills/
└── pac-cli-deploy/
    └── SKILL.md
```

Markdown

```
---
name: pac-cli-deploy
description: Deploy Power Platform solutions using PAC CLI. Use when the user asks to
  export, import, pack, unpack, or publish a Dataverse solution, or when working with
  PAC CLI authentication and environment management.
---

# PAC CLI Deployment Skill

## Authentication
Always use the service principal profile:
```bash
pac auth create --url $DATAVERSE_URL --applicationId $CLIENT_ID \
  --clientSecret $CLIENT_SECRET --tenant $TENANT_ID
```

## Pre-import checklist
1. Run `pac solution check --solutionFile <path>` — block on Critical issues
2. For TEST/PROD: confirm version bump in solution.xml
3. Use `--async` flag for solutions > 50MB

## Environment URLs
- DEV: https://devenv.crm.dynamics.com

- TEST: https://testenv.crm.dynamics.com
- PROD: https://prodenv.crm.dynamics.com (requires approval workflow)
```

The description field is critical — it is the primary mechanism by which the agent decides whether to load the skill for a given prompt. Write it to be specific and include trigger phrases.

### Invoking skills explicitly

You can also manually trigger a skill with a slash command:

Bash

```
> /pac-cli-deploy Export the latest CustomerPortal solution to the solutions/ folder
```

## Installing Skills for Your Developer Profile

The Agent Skills standard (`agentskills.io`) is supported across GitHub Copilot CLI, Claude Code, VS Code agent mode, and several other tools. Skills you install work in all of them simultaneously. Below is a curated selection by developer role.

**Install rule:** Aim for 4–8 skills per project. Installing too many causes “context rot” — the agent uses context on loading skill metadata instead of your actual task.

### Install commands

Bash

```


# Register marketplaces
/plugin marketplace add microsoft/power-platform-skills
/plugin marketplace add github/awesome-copilot
/plugin marketplace add microsoft/skills

# Install specific plugins
/plugin install power-pages@power-platform-skills
/plugin install model-apps@power-platform-skills

# For microsoft/skills (uses npm wizard)
npx skills add microsoft/skills


# → interactive selector lets you choose exactly which skills to install
```

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript-power_platform_developers.png?resize=512%2C512&ssl=1)

### Power Platform Developers

 **![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Important:** `microsoft/power-platform-skills` currently ships **only two plugins** — `power-pages` and `model-apps`. There is **no PCF plugin** in this repository. PCF coverage exists in `github/awesome-copilot` but as *instructions* and *collections*, not Agent Skills. See the distinction in the table below.

#### From `microsoft/power-platform-skills` (Agent Skills / Plugins):

| **Plugin** | **What it does** |
| **power-pages** | Create and deploy Power Pages Code Sites (React, Angular, Vue, Astro) via PAC CLI — local dev, build, and deployment workflows. |
| **model-apps** | Build and deploy Power Apps generative pages for model-driven apps. Stack: React + TypeScript + Fluent UI, deployed via PAC CLI. (Preview) |

#### From `github/awesome-copilot` — Agent Skills:

| **Skill** | **What it does** |
| **dataverse-mcp** | Configure a Dataverse MCP server for your Copilot CLI session and generate the correct connection config. |
| **copilot-studio-mcp-server** | Generate a complete MCP server optimized for Copilot Studio — streamable HTTP, correct schema constraints. |
| **dataverse-python-sdk** | Generate production-ready Python code using the Dataverse SDK with error handling and best practices. |

#### From `github/awesome-copilot` — Instructions (`.instructions.md`, always-on pattern-matched context):

Instructions load differently from skills. They are pattern-matched against file types or folder paths and injected automatically — they don’t require a description-triggered invocation like skills do.

| **Instruction** | **What it does** |
| **power-apps-code-apps** | Standards and best practices for Power Apps Code Apps (TypeScript + React + Power Platform integration). |
| **pcf-api-reference** | Complete PCF API reference — all interfaces, availability in model-driven and canvas apps. **This is the primary PCF coverage available; there is no standalone PCF Agent Skill.** |
| **power-automate-logic-apps** | Best practices for Power Automate and Azure Logic Apps workflows, WDL patterns, enterprise automation. |
| **power-bi-dax** | DAX best practices for efficient, maintainable formulas. |
| **power-bi-data-modeling** | Star schema and data modeling guidance. |
| **power-bi-devops-alm** | CI/CD pipelines, deployment automation, and ALM for Power BI solutions. |
| **power-bi-custom-visuals** | React + D3.js for Power BI custom visuals with TypeScript patterns and testing. |

#### From `github/awesome-copilot` — Collections (curated multi-item toolkits):

| **Collection** | **Type** | **What it includes** |
| **Power Apps Code Apps Development** | Collection | TypeScript, React, Dataverse, connector patterns — 12 items |
| **Power Apps Component Framework (PCF) Development** | Collection | 17-item toolkit for PCF TypeScript dev (model-driven + canvas). **No standalone PCF skill exists; this collection bundles instructions and prompts.** |
| **Power BI Development** | Collection | 14 items: DAX, modeling, performance, visualization, security, DevOps/ALM |
| **Power Platform MCP Connector Development** | Collection | Custom connectors with MCP integration for Copilot Studio |

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript-dotnet_developers.png?resize=512%2C512&ssl=1)

Microsoft’s `microsoft/skills` repository has **29 .NET-specific skills**, all with test coverage and acceptance criteria.

#### From `microsoft/skills`:

| **Skill** | **What it does** |
| **azure-ai-openai-dotnet** | Azure OpenAI SDK: chat completions, embeddings, image generation, audio, DALL-E, Whisper. |
| **azure-ai-agents-persistent-dotnet** | AI Agents SDK: threads, runs, function calling, file search. |
| **azure-ai-projects-dotnet** | AI Foundry SDK: Foundry project management, versioned agents, evaluations. |
| **azure-ai-document-intelligence-dotnet** | Document Intelligence: extract text and tables from invoices, receipts, IDs. |
| **azure-ai-voicelive-dotnet** | Voice Live SDK: real-time voice AI with bidirectional WebSocket. |
| **azure-servicebus-dotnet** | Service Bus: queues, topics, sessions, dead-letter handling. |
| **m365-agents-sdk-dotnet** | M365 Agents SDK: ASP.NET Core hosting, AgentApplication routing, Copilot Studio client. |
| **azure-entra-authentication-events-dotnet** | Entra auth extensions: Azure Functions triggers, token enrichment. |

#### From `github/awesome-copilot` skills:

| **Skill** | **What it does** |
| **dotnet-upgrade** | Agent-guided .NET version upgrades — dependency analysis, multi-repo validation, deployment readiness. |
| **nuget-package-manager** | Manage NuGet packages with CLI-first discipline; handles version updates correctly. |

#### **Available collections:**  

| **Collection** | **What it includes** |
| **C# .NET Development** | Testing, documentation, best practices — prompts, instructions, chat modes |
| **MCP servers in C#** | Build MCP servers using the official Microsoft MCP SDK |

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript-react_typescript_developers.png?resize=512%2C512&ssl=1)

### React / TypeScript Developers

#### From `anthropics/skills`:

| **Skill** | **What it does** |
| **frontend-design** | Production-grade frontend interfaces — avoids generic AI aesthetics. Triggers on any web component, dashboard, or React component request. |

#### From `microsoft/skills`:

| **Skill** | **What it does** |
| **react-flow-nodes** | Custom React Flow nodes with TypeScript, handles, Zustand. |
| **zustand-stores** | Zustand stores: TypeScript, `subscribeWithSelector`, state/action separation. |
| **azure-ai-projects-ts** | AI Projects SDK for TypeScript: agents, connections, evaluations. |
| **azure-cosmos-ts** | Cosmos DB TypeScript SDK: CRUD, queries, bulk operations. |
| **azure-ai-document-intelligence-ts** | Document Intelligence REST SDK for TypeScript. |
| **azure-ai-voicelive-ts** | Voice Live SDK for Node.js/browser environments. |

#### **Available collections:**  

| **Collection** | What it includes |
| **Frontend Web Development** | React, Angular, Vue, TypeScript, CSS frameworks — prompts, instructions, chat modes |
| **Azure Static Web Apps** | Deploy React/Vite/Next.js to Azure SWA with the correct CLI — framework-aware golden path |

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript-azure_devops_developers.png?resize=512%2C512&ssl=1)

### Azure / DevOps Developers / Engineers

#### From `microsoft/skills`:

| **Skill** | **What it does** |
| **microsoft-foundry** | Full AI Foundry lifecycle: model deployment, agent dev, evals, RBAC, quota management. |
| **azure-cosmos-db-py** | Cosmos DB with Python/FastAPI: dual auth, service layer, CRUD, TDD patterns. |
| **azure-ai-search-\*** | AI Search: full-text, vector, semantic, hybrid search (Python / TypeScript). |
| **m365-agents-sdk-\*** | M365 Agents SDK across .NET, Python, TypeScript for multi-channel agents. |
| **azure-resource-manager-\*** | ARM SDKs for Fabric, Cosmos DB, SQL, Redis, MySQL, PostgreSQL, Service Bus, Event Hubs. |

#### From `github/awesome-copilot` skills:

| **Skill** | **What it does** |
| **terraform-azurerm** | Analyze Terraform plan JSON for AzureRM — distinguishes false-positive diffs from real changes. |
| **rollout-plan-generator** | Generate rollout plans: preflight checks, step-by-step deployment, rollback procedures, comms plans. |
| **devops-incident-triage** | Specialized runbooks for incident response: pipeline failures, deployment rollbacks, on-call triage. |

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript-mcp_server_builders.png?resize=512%2C512&ssl=1)

### MCP Server Builders

#### From `microsoft/skills`:

| **Skill** | **What it does** |
| **build-mcp-server** | Cross-language MCP server guide: Python (FastMCP), Node/TypeScript (MCP SDK), C#/.NET (Microsoft MCP SDK). |

#### From `github/awesome-copilot` collections (one per language):

| **Collection** | **Language / SDK** |
| **MCP servers in TypeScript/Node.js** | Official `@modelcontextprotocol/sdk` |
| **MCP servers in Python** | FastMCP |
| **MCP servers in C#** | Microsoft MCP SDK |
| **MCP servers in Go** | Official `go-sdk` |
| **MCP servers in Java** | MCP Java SDK + reactive streams + Spring Boot |
| **MCP servers in Kotlin** | io.modelcontextprotocol:kotlin-sdk |
| **MCP servers in Rust** | `rmcp` SDK with async/await and procedural macros |
| **MCP servers in Ruby** | Official Ruby MCP SDK + Rails integration |

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript-cross_role_productivity.png?resize=512%2C512&ssl=1)

### Cross-Role Productivity (Useful for Everyone)

#### From `anthropics/skills`:

| **Skill** | **What it does** |
| **skill-creator** | Create, benchmark, and iteratively improve new Agent Skills with evals. |
| **docx** | Create and edit Word documents with complex formatting. |
| **pdf** | Read, extract, merge, split, fill, and watermark PDF files. |
| **pptx** | Create and edit PowerPoint presentations. |
| **xlsx** | Create and manipulate Excel spreadsheets. |

#### From `github/awesome-copilot` skills:

| **Skill** | **What it does** |
| **make-skill-template** | Scaffold new Agent Skills with correct frontmatter and directory structure. |
| **microsoft-skill-creator** | Generate skills for any Microsoft technology using the Learn MCP — stores knowledge locally. |
| **10x-engineer** | Interpret shorthand, quasi-code, and natural language into production-quality code. |
| **readme-generator** | Scan project documentation and produce a comprehensive `README.md`. |
| **diataxis-documentation** | Expert technical writing following the Diátaxis framework. |
| **copilot-skill-suggester** | Analyze your repo context and suggest relevant skills you may be missing. |
| **excalidraw-diagrams** | Generate Excalidraw diagrams from natural language descriptions. |
| **meeting-minutes** | Generate concise meeting minutes with decisions, action items, and owners. |

## Extending with MCP Servers

MCP (Model Context Protocol) servers allow Copilot CLI to interact with external systems — reading live Dataverse metadata, querying your database, calling APIs — as part of its reasoning and execution.

Copilot CLI ships with **GitHub’s own MCP server pre-configured**, enabling native operations against your repositories, issues, pull requests, and Actions workflows.

### Adding a custom MCP server

**Edit `~/.copilot/mcp-config.json` (or use `/settings` → MCP in the interactive UI):**

JSON

```
{
  "mcpServers": {
    "dataverse": {
      "command": "node",
      "args": ["/path/to/dataverse-mcp-server/dist/index.js"],
      "env": {
        "DATAVERSE_URL": "https://yourorg.crm.dynamics.com",
        "CLIENT_ID": "your-app-registration-client-id",
        "TENANT_ID": "your-tenant-id",
        "CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

### What a Dataverse MCP server enables

**Once configured, natural language queries against your live environment become possible:**

Bash

```
> Check the Contact entity and list all custom fields added in the last 30 days.
  Then generate a PAC CLI command to export only the solution containing those components.
```

**The agent calls the MCP server, retrieves live entity metadata, cross-references solution components, and generates a scoped `pac solution export` command — in one session.**

### Available community MCP servers for Power Platform

-   **Dataverse MCP server** — Entity metadata, OData queries, solution component inspection

-   **Copilot Studio MCP server** — Agent definition management, topic inspection (use the `copilot-studio-mcp-server` skill to scaffold this)
-   **GitHub MCP server** (built-in) — Issues, PRs, branches, Actions workflows, code search

## Power Platform Integration: Step-by-Step

This is the complete setup sequence for a Power Platform developer starting fresh with a Dataverse project repository.

### Step 1: Install Copilot CLI and authenticate

Bash

```
npm install -g @github/copilot
copilot


# → Browser-based GitHub auth on first run
```

### Step 2: Navigate to your Power Platform repo and initialize

Bash

```
cd ~/repos/CustomerPortal
copilot
/init


# → Generates AGENTS.md with repo context analysis
```

Inspect the generated `AGENTS.md` and add your environment URLs, branching strategy, and PAC CLI conventions.

### Step 3: Add the Power Platform Skills marketplace

Bash

```
/plugin marketplace add microsoft/power-platform-skills
/plugin install power-pages@power-platform-skills
```

**For model-driven app development:**

Bash

```
/plugin install model-apps@power-platform-skills
```

### Step 4: Create your project config file

Create `.github/copilot/config.json` in your repository:

JSON

```
{
  "marketplaces": ["microsoft/power-platform-skills"],
  "allowedTools": [
    "shell(pac *)",
    "shell(npm *)",
    "shell(dotnet *)",
    "shell(git *)"
  ],
  "launchMessage": "CustomerPortal Power Platform project loaded. PAC CLI pre-approved."
}
```

### Step 5: Add Power Platform-specific skills

Bash

```


# Create the skills folder
mkdir -p .github/skills/pac-cli-deploy

# Create your first skill (see the template in section 8)


# Then verify it is discovered
/skills
```

You should see your `pac-cli-deploy` skill listed with its description.

### Step 6: Configure your Dataverse MCP server (optional but recommended)

If you have a Dataverse MCP server available, configure it in `~/.copilot/mcp-config.json` as shown in section 10. This unlocks live environment queries during your sessions.

### Step 7: Try your first Power Platform prompt

Bash

```
> List all solutions in our dev environment, show their versions, 
  and flag any that are more than 2 minor versions behind main
```

With the MCP server configured, Copilot CLI calls Dataverse directly. Without it, it works from the files in your repository.

### Practical Workflows with Code Examples

### Workflow 1: Scaffold a new PAC CLI Power Platform repository

Bash

```
copilot
> Set up a Power Platform ALM repository for a Dataverse solution named "CustomerPortal".
> Include:
> - PAC CLI commands for solution export and import
> - GitHub Actions workflows for CI/CD across dev, test, and prod environments
> - A .env.example file with all required variables
> - An AGENTS.md with Power Platform project context
```

Copilot switches to Plan Mode, proposes the full structure for review, then executes. The generated export workflow:

YAML

```


# .github/workflows/export-solution.yml
name: Export Power Platform Solution

on:
  workflow_dispatch:
    inputs:
      solution_name:
        description: 'Solution unique name'
        required: true
        default: 'CustomerPortal'

jobs:
  export-solution:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install PAC CLI
        run: npm install -g @microsoft/powerplatform-cli

      - name: Authenticate to Power Platform
        run: |
          pac auth create \
            --url ${{ secrets.DEV_DATAVERSE_URL }} \
            --applicationId ${{ secrets.CLIENT_ID }} \
            --clientSecret ${{ secrets.CLIENT_SECRET }} \
            --tenant ${{ secrets.TENANT_ID }}

      - name: Export solution (unmanaged)
        run: |
          pac solution export \
            --name ${{ github.event.inputs.solution_name }} \
            --path ./solutions/${{ github.event.inputs.solution_name }}.zip \
            --managed false --overwrite true

      - name: Unpack solution
        run: |
          pac solution unpack \
            --zipfile ./solutions/${{ github.event.inputs.solution_name }}.zip \
            --folder ./solutions/${{ github.event.inputs.solution_name }} \
            --processCanvasApps true

      - name: Commit unpacked solution
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add ./solutions/
          git commit -m "chore: export ${{ github.event.inputs.solution_name }}" || echo "No changes"
          git push
```

### Workflow 2: Scaffold a PCF control

Bash

```
copilot --allow-tool 'shell(pac *)' --allow-tool 'shell(npm *)'
> Scaffold a new PCF control named "StakeholderMap" using pac pcf init.
> It should be a TypeScript field control for Dataverse.
> After scaffolding, install dependencies and confirm it builds cleanly.
```

Copilot CLI runs the PAC CLI commands, installs dependencies, runs `npm run build`, interprets TypeScript compiler output, and iterates on any errors before handing back to you.

**Sample manifest produced:**

XML

```
<!-- ControlManifest.Input.xml -->
<manifest>
  <control namespace="AIDevMe" constructor="StakeholderMap"
           version="1.0.0" display-name-key="StakeholderMap_DisplayName"
           control-type="standard">
    <property name="stakeholderData" of-type="Multiple" usage="bound" required="true"/>
    <resources>
      <code path="index.ts" order="1"/>
      <css path="css/StakeholderMap.css" order="1"/>
    </resources>
  </control>
</manifest>
```

### Workflow 3: Debug a failing GitHub Actions pipeline

Bash

```
copilot
> My GitHub Actions workflow is failing on the 'pac solution export' step with:
> "Error: Solution with name 'MyApp' was not found in the target environment."
> The solution definitely exists. The workflow uses a Service Principal.
> Here's the workflow: [paste content or use /add-file .github/workflows/export.yml]
```

Copilot reads the workflow and identifies the most common cause — the `DATAVERSE_URL` secret resolving to the wrong environment. It proposes a fix and shows a `/diff` before applying:

YAML

```


#  Common mistake: ambiguous secret name can resolve to wrong environment
- run: pac auth create --url ${{ secrets.DATAVERSE_URL }}

#  Fix: use environment-scoped secrets
- run: pac auth create --url ${{ secrets.DEV_DATAVERSE_URL }}
```

### Workflow 4: Write integration tests for a Power Automate flow

Bash

```


# Use background delegation — write tests while you keep working
> & Write a Node.js Jest integration test suite for our LeadQualification 
  Power Automate HTTP trigger flow. Include happy path, missing field validation,
  and invalid email tests. Use the FLOW_URL from .env.

# Continue working in the terminal, then later:
/resume
```

**Sample generated test:**

JavaScript

```
// lead-qualification.test.js
const axios = require("axios");
require("dotenv").config();

const FLOW_URL = process.env.LEAD_QUALIFICATION_FLOW_URL;

describe("LeadQualification Power Automate Flow", () => {

  test("Valid payload returns 202 with leadId", async () => {
    const response = await axios.post(FLOW_URL, {
      firstName: "Anna", lastName: "Kovacs",
      email: "anna.kovacs@example.com", company: "Contoso Ltd"
    });
    expect(response.status).toBe(202);
    expect(response.data).toHaveProperty("leadId");
  });

  test("Missing lastName returns 400", async () => {
    await expect(
      axios.post(FLOW_URL, { firstName: "Anna", email: "a@b.com", company: "Contoso" })
    ).rejects.toMatchObject({ response: { status: 400 } });
  });

  test("Invalid email format returns 400", async () => {
    await expect(
      axios.post(FLOW_URL, {
        firstName: "Anna", lastName: "Kovacs",
        email: "not-an-email", company: "Contoso"
      })
    ).rejects.toMatchObject({ response: { status: 400 } });
  });
});
```

### Workflow 5: Use Dataverse MCP for live environment queries

**With a Dataverse MCP server configured (Extending with MCP Servers):**

Bash

```
> Check the Contact entity in our dev environment and list all custom fields
  added in the last 30 days. Generate a PAC CLI command to export only
  the solution containing those components.
```

The agent calls Dataverse, retrieves metadata, cross-references solution components, and produces:

Bash

```
pac solution export \
  --name ContactCustomizations_20260205 \
  --path ./solutions/ContactCustomizations_20260205.zip \
  --managed false
```

## Copilot CLI vs Claude Code

Both are terminal-native AI coding agents that share the same Agent Skills standard and plugin ecosystem. Here is how they compare for Power Platform professionals.

| **Feature** | **GitHub Copilot CLI** | **Claude Code** |
| **Native GitHub integration** | Deep — issues, PRs, Actions, code search | Via MCP only |
| **Power Platform Skills plugin** | `microsoft/power-platform-skills` | Same plugin supports both |
| **Multi-model support** | Claude, GPT, Gemini | Anthropic models only |
| **Context window** | ~200K (session-managed) | 200K (native) |
| **Repository memory** | Cross-session | Cross-session |
| **MCP extensibility** | Full support | Full support |
| **Fleet / parallel agents** | `/fleet command` | Sub-agents |
| **Background delegation** | `&` prefix → cloud agent | Not directly equivalent |
| **Enterprise policies** | Via GitHub org settings | Via Anthropic console |
| **Agent Skills standard** | .github/skills/ | `.claude/skills/` (also reads `.github/skills/`) |
| **Bundled document skills** | Via plugin | Built-in (`/docx`, `/pdf`, `/pptx`, `/xlsx`) |

**When to choose Copilot CLI:** Your workflow is deeply embedded in GitHub — assigning issues to agents, reviewing PRs, triggering Actions. You want multi-model flexibility within one tool. Your organization manages everything through GitHub org policies.

**When to choose Claude Code:** You want the largest raw context window. You prefer direct Anthropic model access. You value the built-in document creation skills without any plugin setup.

**For most Power Platform enterprise architects:** use both. They share the same skills and plugins — a skill you write today works in both tools without modification.

## Enterprise Setup for Administrators

### Enabling Copilot CLI for your organization

For Copilot Business and Enterprise plans, an administrator must explicitly enable Copilot CLI from the GitHub organization settings page before users can access it.

Path: **GitHub Organization Settings → Copilot → Features→ Enable Copilot CLI**

**Enterprise controls available at GA**

| **Control** | **What it does** |
| **Agent Control Plane** | Full visibility into which models are being used, tools invoked, and premium request consumption per session across the org |
| **Organization Policies** | Restrict model availability — e.g., allow only Sonnet and GPT-5 mini, block Opus for cost control |
| **Hooks for policy enforcement** | `preToolUse` hooks can approve/deny specific shell commands, enforce file access restrictions, implement compliance workflows |
| **Audit logs** | All agent sessions are logged — addresses shadow AI governance concerns for regulated industries |
| **HTTPS proxy support** | Route all agent traffic through a corporate proxy |

**Recommended enterprise configuration for Power Platform teams**

1.  **Enable Copilot CLI at the org level** with Copilot Business or Enterprise.
2.  **Allow PAC CLI, npm, and git** in the organization policy default tool list.
3.  **Register `microsoft/power-platform-skills`** as the default marketplace in a shared `.github/copilot/config.json` committed to all Power Platform repos.
4.  **Set model policy** to Sonnet 4.6 as the default, with Opus 4.6 available on request — this balances capability and cost.
5.  **Enable audit logging** before rolling out to large teams — you want session data from the start.
6.  **For GCC / on-premise Dataverse:** confirm HTTPS proxy routes are configured for `api.github.com` and Anthropic/OpenAI endpoints before rollout

## Frequently Asked Questions

### Do I need a paid GitHub Copilot subscription to use Copilot CLI?

Yes. Copilot CLI is available on all paid plans — Pro ($10/mo), Pro+ ($39/mo), Business ($19/user/mo), and Enterprise ($39/user/mo). There is no free tier. Each agent interaction draws from your premium request allowance, with heavier agentic sessions (autopilot, fleet) consuming more quota than simple questions.

### Can I use GitHub Copilot CLI alongside Claude Code, or do I have to choose one?

You can use both — and arguably should. They share the same Agent Skills standard and plugin ecosystem, including `microsoft/power-platform-skills`. A skill installed in `.github/skills/` works in Copilot CLI, Claude Code, and VS Code agent mode simultaneously. Choose the tool that fits the session: Copilot CLI for GitHub-native tasks, Claude Code when you need maximum context or direct model control.

### How does PAC CLI authentication work locally vs in GitHub Actions?

Locally, Copilot CLI uses your existing `pac auth list` profile. In GitHub Actions, credentials are passed as environment variables (`DATAVERSE_URL`, `TENANT_ID`, `CLIENT_ID`, `CLIENT_SECRET`) using a Service Principal. The Copilot CLI session runs on your machine; PAC CLI tool calls execute in the pipeline context. Background delegation (`&` prefix) operates under your GitHub identity, not a Service Principal — keep that in mind for production pipeline access.

### How many skills should I install per project?

Microsoft’s guidance is **4 to 8 skills per project**. Installing all 130+ skills from a repository like `microsoft/skills` causes “context rot” — skill metadata consumes context window space that should go to your task. Progressive disclosure means only the full body of relevant skills loads, but even metadata at scale adds up. Select skills matched to what you are actually building in that repository.

### Do Agent Skills work in VS Code stable?

Yes — support for the VS Code stable channel landed in early 2026. If skills are not triggering, check that you are on the latest Copilot extension version and that your skills live in `.github/skills/` (the new standard location), not only in `.claude/skills/`.

## What’s Next — And How to Stay Sharp

This guide covers everything you need to get productive with Copilot CLI today. But the ecosystem is moving fast — new skills are being published weekly, MCP server support is expanding, and Microsoft is actively adding plugins to `microsoft/power-platform-skills`.

**Here’s how to keep up:**

-   ![⭐](https://s.w.org/images/core/emoji/17.0.2/svg/2b50.svg) **Star the repos** — `microsoft/power-platform-skills`, `github/awesome-copilot`, and `microsoft/skills` on GitHub. Watch for new releases.

-   **Subscribe to AIDevMe** — every deep-dive article on agentic Power Platform development, agent skills, and MCP patterns lands in your inbox before it’s shared anywhere else. [Subscribe here](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/#).
-   **Tell me what’s missing** — Is there a step in this guide that needs more detail? A workflow we didn’t cover? A skill that should be in the curated lists? Leave a comment on the companion article or open an issue — this guide is a living document.

-   **Share with your team** — If you’re the one who discovered this, you’re probably the one who’ll set it up for everyone else too. Forward this guide to the developers on your team who work with PAC CLI, PCF, or Dataverse — it’ll save them hours.

## References and Further Reading

### Companion Article

This guide is the hands-on companion to the AIDevMe blog article covering the GitHub Copilot CLI GA announcement. If you prefer a narrative overview — what changed, why it matters, enterprise readiness considerations, and a Copilot CLI vs Claude Code comparison — start there first.

→ [**GitHub Copilot CLI Is Now Generally Available — And Power Platform Developers Should Pay Attention**](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/) — Published on AIDevMe.com

-   [GitHub Changelog: Copilot CLI is now generally available](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/) — Official GA announcement, February 25, 2026

-   [GitHub Copilot CLI Documentation](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli) — Full reference documentation
-   [Copilot CLI Best Practices Guide](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices) — GitHub’s official recommendations

-   [About Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) — GitHub Docs
-   [Agent Skills specification](https://agentskills.io/specification) — The open standard

-   [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) — Official Microsoft plugin for Copilot CLI and Claude Code
-   [microsoft/skills](https://github.com/microsoft/skills) — 132 Azure SDK skills with 1-click install wizard

-   [github/awesome-copilot](https://github.com/github/awesome-copilot) — Community skills, agents, instructions, and plugins
-   [anthropics/skills](https://github.com/anthropics/skills) — Anthropic’s reference skills including document creation

-   [Enterprise AI Controls & Agent Control Plane GA](https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available) — Enterprise governance features
-   [PAC CLI Reference](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference) — Microsoft Learn

### *Related*

[![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform-featured.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/ "The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform")

#### [The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/ "The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform")

GitHub Copilot CLI Autopilot mode reached GA in February 2026 — but for Power Platform, autonomous PAC CLI execution carries real risk. This article builds a scored Risk Decision Matrix mapping every PAC CLI operation to one of four zones: full Autopilot, conditional, Plan Mode only, or human-only. Includes a…

March 10, 2026

In "AI & Copilot"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [GitHub Copilot CLI: Complete Developer Guide for Power Platform, .NET, and TypeScript](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/)