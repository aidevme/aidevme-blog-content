# GitHub Copilot CLI GA: What Power Platform Developers Need to Know

Estimated reading time: 12 minutes

## Table of contents

-   [Introduction: The Terminal Just Got a Lot Smarter — Even for Low-Code Developers](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-introduction-the-terminal-just-got-a-lot-smarter-even-for-low-code-developers)

-   [What Is GitHub Copilot CLI?](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-what-is-github-copilot-cli)
-   [Key Features of GitHub Copilot CLI GA](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-key-features-of-github-copilot-cli-ga)
    -   [Background Delegation with & Prefix](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-background-delegation-with-amp-prefix)
-   [How to Install GitHub Copilot CLI](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-how-to-install-github-copilot-cli)

-   [Power Platform Skills Plugin — Microsoft’s Official Integration](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-power-platform-skills-plugin-microsoft-s-official-integration)
-   [5 Real-World Scenarios for Power Platform Developers](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-5-real-world-scenarios-for-power-platform-developers)
    -   [Scenario 1: Scaffolding a PAC CLI Power Platform Project](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-scenario-1-scaffolding-a-pac-cli-power-platform-project)
    -   [Scenario 2: PCF Control Development — Scaffolding and TypeScript Assistance](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-scenario-2-pcf-control-development-scaffolding-and-typescript-assistance)
    -   [Scenario 3: Debugging a Failing GitHub Actions Power Platform Pipeline](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-scenario-3-debugging-a-failing-github-actions-power-platform-pipeline)
    -   [Scenario 4: Using a Custom MCP Server for Dataverse Operations](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-scenario-4-using-a-custom-mcp-server-for-dataverse-operations)
    -   [Scenario 5: Writing and Running Integration Tests for Power Automate Flows](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-scenario-5-writing-and-running-integration-tests-for-power-automate-flows)
-   [Extending with Agent Skills](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-extending-with-agent-skills)

-   [GitHub Copilot CLI vs Claude Code: A Quick Comparison](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-github-copilot-cli-vs-claude-code-a-quick-comparison)
-   [The Skills Ecosystem: What’s Available by Developer Profile](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-the-skills-ecosystem-what-s-available-by-developer-profile)

-   [Quick Start for Power Platform Developers](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-quick-start-for-power-platform-developers)
    -   [Do I need a paid GitHub Copilot subscription?](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-do-i-need-a-paid-github-copilot-subscription)
    -   [Can I use Copilot CLI alongside Claude Code, or do I have to choose?](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-can-i-use-copilot-cli-alongside-claude-code-or-do-i-have-to-choose)
    -   [How many Agent Skills should I install per project?](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-how-many-agent-skills-should-i-install-per-project)
-   [Join the Conversation](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-join-the-conversation)

-   [References and Further Reading](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-references-and-further-reading)
-   [Related Reading](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#h-related-reading)

## Introduction: The Terminal Just Got a Lot Smarter — Even for Low-Code Developers

On February 25, 2026, GitHub announced the general availability of **GitHub Copilot CLI** for all paid Copilot subscribers — marking the graduation of what started as a terminal assistant into a full-blown autonomous coding agent. It plans, builds, reviews code, and remembers context across sessions, all without you ever leaving your terminal window.

But here’s the question most Power Platform developers are probably asking: *“I build Canvas Apps, Model-Driven Apps, and Copilot Studio solutions — why would a terminal tool matter to me?”*

The answer is: **more than you think.**

Power Platform development has quietly grown a significant CLI surface area. The **Power Platform CLI (PAC CLI)** is the backbone of ALM pipelines, solution packaging, environment management, and PCF control deployment. If you use GitHub Actions for your Power Platform CI/CD pipelines, you’re already living in the terminal — you just haven’t had an AI agent helping you there yet. Beyond that, Microsoft has officially published a **Power Platform Skills plugin for GitHub Copilot CLI** (`microsoft/power-platform-skills`), with support for Power Pages today and Power Apps generative pages coming soon. This means the ecosystem is already converging.

Whether you’re a senior architect managing multi-environment Dataverse pipelines, a PCF developer scaffolding TypeScript controls, or a consultant automating solution deployments for enterprise clients — GitHub Copilot CLI GA is a milestone worth understanding deeply.

**Before you read on — quick question:** *Where does most of your Power Platform work happen today?*

-   Mostly in the browser (Power Apps Studio, make.powerapps.com)

-   Mixed — browser for low-code, terminal for ALM and CI/CD
-   Heavily in the terminal — PAC CLI, GitHub Actions, PCF dev

Drop your answer in the comments. It’ll be interesting to see how the community splits — and it shapes what I cover next on AIDevMe.

## What Is GitHub Copilot CLI?

GitHub Copilot CLI is a **terminal-native AI coding agent** that brings the full power of GitHub Copilot directly to your command line. It went into public preview in September 2025 and has received hundreds of updates since then. As of February 25, 2026, it is production-ready and available across all paid tiers: **Copilot Pro ($10/mo), Pro+ ($39/mo), Business ($19/user/mo), and Enterprise ($39/user/mo)**.

Unlike the older `gh copilot suggest` command (which gave you a single command suggestion), the new Copilot CLI is an autonomous agent capable of:

-   Planning multi-step tasks before execution.

-   Editing files, running commands, and iterating on results.
-   Delegating to specialized sub-agents in parallel.

-   Remembering your codebase across sessions.
-   Connecting to external services via MCP servers

It is not just a chatbot in a terminal. It is closer to having a senior developer pair-programming with you at the command line.

## Key Features of GitHub Copilot CLI GA

### Agentic Plan Mode and Autopilot Mode

Copilot CLI ships with two complementary execution modes that give you full control over how autonomous the agent operates.

**Plan Mode** (activated with `Shift+Tab`) turns the agent into a thoughtful collaborator. Before writing a single line of code or running a single command, it analyzes your request, asks clarifying questions, and produces a structured implementation plan for your review. You approve the plan, then it executes.

**Autopilot Mode** goes hands-free. For well-defined, trust-worthy tasks — writing unit tests, refactoring files, fixing CI failures — you hand the wheel over entirely. The agent executes tools, runs shell commands, and iterates until the job is done.

### Specialized Built-In Agents

Rather than a monolithic assistant, Copilot CLI delegates to specialized sub-agents automatically:

-   **Explore** — Fast codebase analysis without polluting your main context**.**

-   **Task** — Runs builds, tests, and shell commands.
-   **Code Review** — Analyzes staged or unstaged changes before you commit.

-   **Plan** — Dedicated implementation planning agent

Multiple agents can run in **parallel**, dramatically shortening feedback loops on complex tasks.

### Background Delegation with `&` Prefix

Prefix any prompt with `&` to delegate work to the cloud-based Copilot coding agent while you keep your terminal free for other tasks. Use `/resume` to switch between local and remote sessions. This is particularly powerful for long-running Power Platform solution exports or deployment pipelines.

### MCP Extensibility: The Game Changer

Copilot CLI ships with **GitHub’s own MCP server built in** and supports any custom MCP server. This is where the story for Power Platform professionals gets genuinely exciting — we’ll cover the specifics in a dedicated scenario section below.

### Multi-Model Choice

You can choose your AI engine mid-session with the `/model` command:

| **Model** | **Premium Request Multiplier** |
| **Claude Opus 4.6** | 3x |
| **Claude Sonnet 4.6** | 1x |
| **GPT-5.3-Codex** | 1x |
| **Claude Haiku 4.5** | 0.33x |
| **GPT-5 mini / GPT-4.1** | 0x (included free) |

For quick scaffolding tasks, Claude Haiku 4.5 or GPT-5 mini will burn almost no premium request budget. For architectural deep-dives, Claude Sonnet 4.6 hits the sweet spot of capability and cost.

**Infinite Sessions with Auto-Compaction and Repository Memory**

When your session approaches 95% of the context window, Copilot automatically compresses history in the background. Sessions can run as long as your task requires. Across sessions, the agent builds **repository memory** — learning your codebase conventions, naming patterns, and preferences so future sessions are immediately productive.

**`/diff`, `/review`, and Undo**

-   `/diff` — Review all file changes made during the session with syntax-highlighted inline diffs, add line-level comments, toggle between session changes and branch diffs.

-   `/review` — Quick sanity check on staged or unstaged changes before committing.
-   `Esc+Esc` — Rewind all file changes back to any previous snapshot in the session

## How to Install GitHub Copilot CLI

Bash

```
npm install -g @github/copilot   # or: brew install github/tap/copilot  |  winget install GitHub.Copilot
copilot                           # authenticate and launch
/init                             # initialize for your repo
```

Homebrew and WinGet both auto-update. Copilot CLI is also included in the default GitHub Codespaces image. For full install options, prerequisites, and first-launch walkthrough, see the in [GitHub Copilot CLI: Complete Developer Guide for Power Platform, .NET, and TypeScript.](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/)

## Power Platform Skills Plugin — Microsoft’s Official Integration

One of the most significant discoveries for Power Platform developers is the **`microsoft/power-platform-skills`** repository — an officially maintained plugin marketplace for GitHub Copilot CLI (and Claude Code) that provides Power Platform development plugins.

### Installing the Power Platform Skills Plugin

Bash

```


# Quick install via curl (Mac/Linux/Windows cmd)
curl -fsSL https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js | node

# Or install manually inside a Copilot CLI session
/plugin marketplace add microsoft/power-platform-skills
/plugin install power-pages@power-platform-skills
```

### What’s Available Today

**Power Pages Plugin** supports creating and deploying Power Pages Code Sites (Single Page Applications) using modern frontend stacks: React, Angular, Vue, or Astro — deployed via PAC CLI.

**Power Apps Plugin** (coming soon) will support building and deploying Power Apps generative pages for model-driven apps using React + TypeScript + Fluent UI.

This is Microsoft signaling clearly: **the future of Power Platform professional development runs through the terminal and agentic AI**.

## 5 Real-World Scenarios for Power Platform Developers

### Scenario 1: Scaffolding a PAC CLI Power Platform Project

You’re starting a new Power Platform solution repository from scratch. Instead of manually creating the folder structure, environment configuration, and GitHub Actions workflow, you describe the intent to Copilot CLI:

Bash

```
copilot
> Set up a Power Platform ALM repository for a Dataverse solution named "CustomerPortal". 
> Include PAC CLI commands for solution export/import, a GitHub Actions workflow for CI/CD, 
> and a .env.example file with environment variables for dev, test, and prod.
```

Copilot CLI switches to **Plan Mode**, proposes the full structure for your review, then executes — creating the folder hierarchy, scaffolding the workflow YAML, and writing the PAC CLI helper scripts.

**Sample generated GitHub Actions workflow snippet:**

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
        run: |
          npm install -g @microsoft/powerplatform-cli

      - name: Authenticate to Power Platform
        run: |
          pac auth create \
            --url ${{ secrets.DATAVERSE_URL }} \
            --applicationId ${{ secrets.CLIENT_ID }} \
            --clientSecret ${{ secrets.CLIENT_SECRET }} \
            --tenant ${{ secrets.TENANT_ID }}

      - name: Export solution (unmanaged)
        run: |
          pac solution export \
            --name ${{ github.event.inputs.solution_name }} \
            --path ./solutions/${{ github.event.inputs.solution_name }}.zip \
            --managed false \
            --overwrite true

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

### Scenario 2: PCF Control Development — Scaffolding and TypeScript Assistance

You’re building a new PCF control — say, a **Stakeholder Map** visualization for Model-Driven Apps. Copilot CLI can scaffold the entire control, write the TypeScript manifest, and help you debug TypeScript compilation errors iteratively.

Bash

```
copilot --allow-tool 'shell(pac *)' --allow-tool 'shell(npm *)'
> Scaffold a new PCF control named "StakeholderMap" using pac pcf init. 
> It should be a TypeScript field control targeting Dataverse. 
> After scaffolding, install dependencies and confirm it builds cleanly.
```

Copilot CLI runs the PAC CLI commands, installs dependencies, runs `npm run build`, interprets the output, and iterates if there are TypeScript errors.

**Sample PCF manifest snippet the agent would produce:**

XML

```
<!-- ControlManifest.Input.xml -->
<?xml version="1.0" encoding="utf-8"?>
<manifest>
  <control namespace="AIDevMe" constructor="StakeholderMap" 
           version="1.0.0" display-name-key="StakeholderMap_DisplayName" 
           description-key="StakeholderMap_Desc" control-type="standard">
    
    <property name="stakeholderData" display-name-key="stakeholderData_Display_Name" 
              description-key="stakeholderData_Desc" of-type="Multiple" usage="bound" required="true"/>
    
    <property name="selectedColor" display-name-key="selectedColor_Display_Name"
              description-key="selectedColor_Desc" of-type="SingleLine.Text" usage="input" required="false"/>

    <resources>
      <code path="index.ts" order="1"/>
      <css path="css/StakeholderMap.css" order="1"/>
    </resources>
  </control>
</manifest>
```

TypeScript

```
// index.ts — generated by Copilot CLI
import { IInputs, IOutputs } from "./generated/ManifestTypes";

export class StakeholderMap implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  private container: HTMLDivElement;
  private context: ComponentFramework.Context<IInputs>;

  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ): void {
    this.container = container;
    this.context = context;
    this.renderMap();
  }

  private renderMap(): void {
    const data = this.context.parameters.stakeholderData.raw ?? "";
    // Render 2D quadrant visualization
    this.container.innerHTML = `
      <div class="stakeholder-map">
        <div class="quadrant high-influence high-interest">Champions</div>
        <div class="quadrant high-influence low-interest">Keep Satisfied</div>
        <div class="quadrant low-influence high-interest">Keep Informed</div>
        <div class="quadrant low-influence low-interest">Monitor</div>
      </div>
    `;
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    this.context = context;
    this.renderMap();
  }

  public getOutputs(): IOutputs {
    return {};
  }

  public destroy(): void {
    this.container.innerHTML = "";
  }
}
```

### Scenario 3: Debugging a Failing GitHub Actions Power Platform Pipeline

Your Power Platform solution export pipeline is failing with a cryptic PAC CLI error. Instead of digging through logs manually, you paste the error into Copilot CLI:

Bash

```
copilot
> My GitHub Actions workflow is failing with this error on the 'pac solution export' step:
> "Error: Solution with name 'MyApp' was not found in the target environment."
> The solution definitely exists in our dev environment. The workflow uses a Service Principal. 
> Here's the workflow file: [paste or /add-file workflow.yml]
```

Copilot CLI reads the workflow, identifies that the `pac auth create` step is pointing at the wrong environment URL (a common mistake where `DATAVERSE_URL` resolves to the production environment secret instead of dev), proposes a fix, and shows you a `/diff` before applying it.

**Key PAC CLI environment variable pattern to always verify:**

### Scenario 4: Using a Custom MCP Server for Dataverse Operations

One of the most powerful capabilities for Power Platform architects is combining Copilot CLI with a **custom Dataverse MCP server**. This allows the agent to query your actual Dataverse environment — reading entity metadata, checking solution components, or validating data — as part of its planning and execution.

Here’s how you configure a local Dataverse MCP server inside Copilot CLI:

JSON

```
// ~/.copilot/config.json
{
  "mcpServers": {
    "dataverse": {
      "command": "node",
      "args": ["/path/to/dataverse-mcp-server/dist/index.js"],
      "env": {
        "DATAVERSE_URL": "https://yourorg.crm.dynamics.com",
        "CLIENT_ID": "<your-app-registration-client-id>",
        "TENANT_ID": "<your-tenant-id>",
        "CLIENT_SECRET": "<your-client-secret>"
      }
    }
  }
}
```

Once configured, you can prompt Copilot CLI with natural language against your live Dataverse:

Bash

```
copilot
> Check the 'Contact' entity in our Dataverse environment and list all custom fields 
> added in the last 30 days. Then generate a PAC CLI command to export only 
> the solution containing those components.
```

The agent calls the Dataverse MCP server, retrieves metadata, synthesizes the component list, and generates the scoped `pac solution export` command — all in one session.

### Scenario 5: Writing and Running Integration Tests for Power Automate Flows

Power Automate flows are notoriously hard to test automatically. Using Copilot CLI with the background delegation (`&`) pattern, you can ask the agent to generate a test harness while you continue working:

Bash

```
copilot
& Write a Node.js integration test suite using Jest for our 'LeadQualification' Power Automate 
flow. The flow accepts a JSON body with {firstName, lastName, email, company} and 
calls an HTTP trigger. Use the endpoint from our .env file. Mock the external CRM call 
but actually invoke the flow via HTTP. Include happy path, missing field, and invalid email tests.
```

**While the test suite is being written in the background, you switch to another terminal. Later:**

Bash

```
/resume
```

**The agent has finished. You review the generated test file with `/diff`, approve it, and run it:**

JavaScript

```
// Generated: lead-qualification.test.js
const axios = require("axios");
require("dotenv").config();

const FLOW_URL = process.env.LEAD_QUALIFICATION_FLOW_URL;

describe("LeadQualification Power Automate Flow", () => {
  
  test("Happy path: valid lead submits successfully", async () => {
    const response = await axios.post(FLOW_URL, {
      firstName: "Anna",
      lastName: "Kovacs",
      email: "anna.kovacs@example.com",
      company: "Contoso Ltd"
    });
    expect(response.status).toBe(202);
    expect(response.data).toHaveProperty("leadId");
  });

  test("Missing required field returns 400", async () => {
    await expect(
      axios.post(FLOW_URL, {
        firstName: "Anna",
        // lastName missing
        email: "anna.kovacs@example.com",
        company: "Contoso Ltd"
      })
    ).rejects.toMatchObject({ response: { status: 400 } });
  });

  test("Invalid email format returns 400", async () => {
    await expect(
      axios.post(FLOW_URL, {
        firstName: "Anna",
        lastName: "Kovacs",
        email: "not-an-email",
        company: "Contoso Ltd"
      })
    ).rejects.toMatchObject({ response: { status: 400 } });
  });
});
```

**Have you tried any of these scenarios yet?** These five workflows cover the most common entry points for Power Platform developers. But everyone’s stack is different — maybe you’re deep in Dataverse plugins, or you’re managing a 50-solution tenant, or you’re building PCF controls with React 18 and Fluent UI v9.

**Which scenario is most relevant to your work right now?** And is there one we didn’t cover that you’d like to see? Tell us in the comments — the most-requested scenario becomes the next deep-dive article on AIDevMe.

## Extending with Agent Skills

One of the most powerful customization mechanisms is **Agent Skills** — markdown files committed to `.github/skills/` that teach the agent your team’s specific workflows. A Power Platform skill might encode your deployment checklist, environment naming conventions, and PAC CLI authentication patterns — so every team member’s Copilot session has that institutional knowledge baked in automatically.

Markdown

```
<!-- .github/skills/pac-cli-deploy/SKILL.md -->
---
name: pac-cli-deploy
description: Deploy Power Platform solutions using PAC CLI. Use when the user asks to
  export, import, or publish a Dataverse solution, or manage PAC CLI authentication.
---
Always authenticate via Service Principal. Run `pac solution check` before import.
Use `--async` for solutions > 50MB. Environments: DEV / TEST / PROD.
```

Skills work across Copilot CLI, Claude Code, and VS Code agent mode — write once, use everywhere. For a complete guide to writing, structuring, and sharing skills, see **[GitHub Copilot CLI: Complete Developer Guide for Power Platform, .NET, and TypeScript](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/)**.

## GitHub Copilot CLI vs Claude Code: A Quick Comparison

Both tools are terminal-native AI coding agents. Here’s how they compare for Power Platform professionals:

| **Feature** | **GitHub Copilot CLI** | **Claude Code** |
| **Native GitHub integration** | Deep (issues, PRs, Actions) | Via MCP only |
| **Power Platform Skills plugin** | `microsoft/power-platform-skills` | Same plugin supports both |
| **Multi-model support** | Claude, GPT, Gemini | Anthropic models only |
| **Context window** | ~200K (mediated) | 200K (native) |
| **Repository memory** | Cross-session | Cross-session |
| **MCP extensibility** | Full support | Full support |
| **Fleet/parallel agents** | `/fleet` command | Sub-agents |
| **Enterprise policies** | Via GitHub org settings | Via Anthropic console |

If your workflow is **deeply embedded in GitHub** — Issues, PRs, GitHub Actions, Codespaces — Copilot CLI’s native context is a significant productivity advantage. If you prefer **maximum context window and direct model access**, Claude Code retains an edge on raw capability.

For most Power Platform enterprise architects: **both tools are worth keeping in your toolkit.** The Microsoft Power Platform Skills plugin explicitly supports both.

## The Skills Ecosystem: What’s Available by Developer Profile

The Agent Skills standard (`agentskills.io`) is supported across GitHub Copilot CLI, Claude Code, and VS Code agent mode. Four major repositories cover the Power Platform space:

| **Repository** | **Stars** | **What it covers** |
| `**microsoft/power-platform-skills**` | — | Power Pages, Model Apps (official Microsoft plugins) |
| `**microsoft/skills**` | 1.2k | 132 Azure SDK skills — .NET, Python, TypeScript, Java |
| `**github/awesome-copilot**` | 14.6k | Community skills, instructions, collections across all stacks |
| `**anthropics/skills**` | 69k | Document skills, frontend design, skill-creator |

**Quick install:**

Bash

```
/plugin marketplace add microsoft/power-platform-skills
/plugin marketplace add github/awesome-copilot
/plugin install power-pages@power-platform-skills
```

**No PCF plugin exists in `microsoft/power-platform-skills` today.** PCF coverage comes from `github/awesome-copilot` as the `pcf-api-reference` instruction and the PCF Development collection (17 items) — not a standalone Agent Skill.

For the full curated breakdown by developer profile — Power Platform, .NET, React/TypeScript, Azure/DevOps, MCP builders, and cross-role productivity — see **[GitHub Copilot CLI: Complete Developer Guide for Power Platform, .NET, and TypeScript](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/)**.

## Quick Start for Power Platform Developers

Five minutes to your first agentic PAC CLI session:

Bash

```
npm install -g @github/copilot                          # 1. Install
copilot && /init                                        # 2. Authenticate and initialize repo
/plugin marketplace add microsoft/power-platform-skills # 3. Add Power Platform Skills
/plugin install power-pages@power-platform-skills       # 4. Install the plugin
> List all solutions in my Dataverse dev environment    # 5. First prompt
```

For a complete 7-step walkthrough including AGENTS.md configuration, Dataverse MCP setup, and recommended skill selection, see [GitHub Copilot CLI: Complete Developer Guide for Power Platform, .NET, and TypeScript](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/)

## Frequently Asked Questions

### Do I need a paid GitHub Copilot subscription?

Yes — Copilot CLI is included with all paid plans (Pro, Pro+, Business, Enterprise). There is no free tier. Each agent interaction draws from your premium request allowance; autopilot and fleet sessions consume more quota than simple questions.

### Can I use Copilot CLI alongside Claude Code, or do I have to choose?

Both. They share the same Agent Skills standard and the same `microsoft/power-platform-skills` plugin. A skill in `.github/skills/` works in both tools simultaneously. Use Copilot CLI when you need deep GitHub integration (issues, PRs, Actions); use Claude Code when you want direct model control or a larger raw context window.

### How many Agent Skills should I install per project?

4–8. The agent loads all skill metadata at session start — too many skills causes “context rot” where metadata eats the context window instead of your actual task. Choose skills matched to what you’re actively building.

## Join the Conversation

GitHub Copilot CLI GA is one of those releases that looks incremental on the surface but quietly shifts how professional Power Platform development works. The combination of agentic autonomy, PAC CLI native support, Agent Skills extensibility, and the official `microsoft/power-platform-skills` plugin means the gap between “low-code developer” and “terminal-native architect” just got a lot narrower.

**A few things I’d love to hear from you:**

-   **Have you migrated any manual PAC CLI steps to Copilot CLI yet?** What did you automate first?

-   **Are you building custom Agent Skills for your team?** Share what problem you’re solving — or drop a link to your repo if it’s public.
-   **Copilot CLI or Claude Code — or both?** Where do you see each one fitting in your workflow?

-   **What’s missing?** Is there a Power Platform workflow you wish Copilot CLI could handle that it can’t yet?

Leave a comment below, or find me on LinkedIn — I read and respond to everything. If this article was useful, sharing it with one other Power Platform developer in your network makes a real difference for the AIDevMe community.

**Not subscribed yet?** The AIDevMe newsletter covers exactly this kind of deep-dive, practical content — Power Platform architecture, agentic AI patterns, and the tools that are actually changing how we build. [Subscribe here](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/#) and get the next article directly in your inbox.

## References and Further Reading

-   [GitHub Changelog: Copilot CLI is now generally available](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/) — Official GA announcement, February 25, 2026.

-   [GitHub Copilot CLI Documentation](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli) — Full reference documentation.
-   [Copilot CLI Best Practices Guide](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices) — GitHub’s official recommendations.

-   [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) — Official Microsoft plugin for Copilot CLI and Claude Code.
-   [GitHub Copilot CLI Changelog: Enhanced agents and context management](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/) — January 2026 update notes.

-   [Enterprise AI Controls & Agent Control Plane GA](https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available) — Enterprise governance capabilities.
-   [PAC CLI Reference](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference) — Microsoft Learn.

-   [Copilot CLI Public Repository](https://github.com/github/copilot-cli) — Release notes and community discussions

If this article gave you a solid overview and you want to go deeper, the companion **Developer Guide** covers the same ecosystem as a progressive, hands-on reference — starting from installation through to enterprise configuration, with a full command reference, AGENTS.md templates, and step-by-step Power Platform integration walkthrough.

**[GitHub Copilot CLI: Developer Guide](https://aidevme.com/github-copilot-cli-complete-developer-guide-for-power-platform-net-and-typescript/)** — Structured learning path with practical examples for Power Platform, .NET, and TypeScript developers.

### *Related*

[![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform-featured.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/ "The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform")

#### [The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform](https://aidevme.com/the-risk-decision-matrix-for-github-copilot-cli-autopilot-mode-in-power-platform/ "The Risk Decision Matrix for GitHub Copilot CLI Autopilot Mode in Power Platform")

GitHub Copilot CLI Autopilot mode reached GA in February 2026 — but for Power Platform, autonomous PAC CLI execution carries real risk. This article builds a scored Risk Decision Matrix mapping every PAC CLI operation to one of four zones: full Autopilot, conditional, Plan Mode only, or human-only. Includes a…

March 10, 2026

In "AI & Copilot"

[![GitHub Copilot Agentic Memory vs Stateless AI](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/02/github-copilot-agentic-memory-what-it-is-how-it-works-featured.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/ "GitHub Copilot Agentic Memory: What It Is, How It Works?")

#### [GitHub Copilot Agentic Memory: What It Is, How It Works?](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/ "GitHub Copilot Agentic Memory: What It Is, How It Works?")

GitHub Copilot just launched a persistent, repository-scoped agentic memory system in public preview. Instead of starting from scratch every session, Copilot now learns your codebase conventions over time and shares that knowledge across the coding agent, code review, and CLI. In this article, we explore how it works under the…

February 24, 2026

In "AI & Copilot"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [GitHub Copilot CLI Is Now Generally Available — And Power Platform Developers Should Pay Attention](https://aidevme.com/github-copilot-cli-is-now-generally-available-and-power-platform-developers-should-pay-attention/)