# Microsoft Scout: The Complete Guide to Microsoft's First Always-On Autopilot Agent

**WordPress SEO**
- **Focus keyphrase:** Microsoft Scout Autopilot agent
- **SEO title:** Microsoft Scout: Complete Guide to Microsoft's Always-On Autopilot Agent
- **Meta description:** Microsoft Scout is Microsoft's first Autopilot agent — a desktop AI app for Windows and macOS that acts on your files, shell, browser, and Microsoft 365 data autonomously. Here's everything you need to know.
- **Slug:** microsoft-scout-autopilot-agent-complete-guide
- **Excerpt:** Microsoft Scout is Microsoft's first Autopilot agent, announced at Build 2026. It's a desktop AI application for Windows and macOS that acts on your files, shell, browser, and Microsoft 365 data — with its own Entra identity, heartbeat background mode, automations, and sub-agent delegation. This guide covers everything: what it is, what it can do, how access works, enterprise governance, and what it means for Power Platform and enterprise developers.
- **Categories:** AI & Copilot, Power Platform
- **Tags:** Microsoft Scout, Autopilot Agent, AI Agents, Agentic AI, GitHub Copilot, Microsoft 365, Power Platform AI, Enterprise AI, Enterprise Architecture, OpenClaw, Entra Identity, Microsoft Build 2026, Playwright, Work IQ, Microsoft Purview
- **URL:** [Microsoft Scout Autopilot Agent: What to Know - Practical AI, Copilot & Modern Development Insights](https://aidevme.com/microsoft-scout-autopilot-agent-complete-guide/)

---

At Microsoft Build 2026, Omar Shahine — Corporate Vice President of Microsoft Scout — announced something that had been running quietly inside Microsoft for months: **Microsoft Scout**, the company's first **Autopilot agent**.

Copilot Chat answers questions. Scout takes action. It runs on your desktop, reads and writes your files, executes shell commands, automates a browser with Playwright, queries your entire Microsoft 365 account, and keeps working in the background on a schedule — all with its own Entra identity, under the permissions you set.

This isn't an incremental update to Copilot. It's a new product category, and understanding how it's built matters for anyone working in Power Platform, Dataverse, or enterprise architecture. Here's everything you need to know.

---

## Table of Contents

- [A New Category: Autopilot Agents](#a-new-category-autopilot-agents)
- [What Is Microsoft Scout?](#what-is-microsoft-scout)
- [What Microsoft Scout Can Do](#what-microsoft-scout-can-do)
  - [File System](#file-system)
  - [Shell Commands](#shell-commands)
  - [Browser Control](#browser-control)
  - [Microsoft 365 Integration](#microsoft-365-integration)
  - [Autonomous Background Modes](#autonomous-background-modes)
  - [Sub-Agent Delegation](#sub-agent-delegation)
  - [Memory and Session History](#memory-and-session-history)
  - [Sensitivity Labels](#sensitivity-labels)
  - [Skills System](#skills-system)
- [How It Works: The Approval Loop](#how-it-works-the-approval-loop)
- [Microsoft Scout vs Copilot Chat](#microsoft-scout-vs-copilot-chat)
- [Access and Licensing Requirements](#access-and-licensing-requirements)
- [Enterprise Security and Governance](#enterprise-security-and-governance)
- [Work IQ: The Intelligence Layer](#work-iq-the-intelligence-layer)
- [OpenClaw: The Open-Source Foundation](#openclaw-the-open-source-foundation)
- [Known Limitations](#known-limitations)
- [The "Addiction" Controversy and Marketing vs. Reality](#the-addiction-controversy-and-marketing-vs-reality)
- [What This Means for Power Platform and Enterprise Developers](#what-this-means-for-power-platform-and-enterprise-developers)
- [Key Takeaways](#key-takeaways)
- [References](#references)

---

## A New Category: Autopilot Agents

Microsoft is introducing a new product category alongside Scout: **Autopilots**.

> "Autopilots are always-on agents that work autonomously, with their own identity, and act on your behalf."

The distinction matters. Most AI tools are reactive — you prompt them, they respond, the work stops when you close the tab. Autopilots are different in three specific ways:

- They stay active in the background and work without being prompted each time
- They operate with **their own Entra identity** — not a shared anonymous service account. Everything they do is attributable to a known actor your directory already understands
- Their credentials are scoped to the task at hand, redacted from logs and diagnostics, and managed with the same rigour as any first-party Microsoft service

That identity model is architecturally significant. When Scout acts on your behalf, you know exactly whose authority it carried, and nothing sensitive leaked along the way. For enterprise architects who have spent years dealing with service accounts and shared credentials in Power Automate flows, this is a meaningful upgrade in the trust model.

---

## What Is Microsoft Scout?

**Microsoft Scout** is a desktop AI application for Windows and macOS. You describe what you need in a chat interface, and Scout carries out the work — reading and writing files, running shell commands, controlling a browser, querying your Microsoft 365 account, and working autonomously in the background.

It was announced June 2, 2026 at Microsoft Build by Omar Shahine and is currently in **Frontier private preview** (experimental release, prerelease documentation, subject to change). It is not generally available. Mobile is not supported. Desktop only: Windows 11 or later, macOS 12 Monterey or later.

Scout is powered by **OpenClaw**, Microsoft's open-source Autopilot technology. The internal codename was "Clawpilot" — some pre-release Intune screenshots still use it. Access requires Frontier enrollment, an Intune policy configuration, and an admin opt-in attestation. Users need both a Microsoft 365 Copilot licence and a GitHub Copilot Business or Enterprise licence.

The origin story is worth knowing. What became Scout started as Omar Shahine's personal project — a local OpenClaw deployment running on his MacBook at home, later extended into a [home automation integration](https://github.com/omarshahine/HomeClaw) that let an autonomous LLM agent observe and respond to physical sensors in his home office. That personal experiment, which Satya Nadella was an early follower of, became Microsoft's biggest bet on autonomous agents.

---

## What Microsoft Scout Can Do

### File System

Scout reads, writes, and searches files in your configured workspace directory. It creates fully formatted documents through bundled skills:

- **Word** (.docx) — reports, memos, proposals, letters
- **Excel** (.xlsx) — spreadsheets, data analysis, formatted tables, charts
- **PowerPoint** (.pptx) — slide decks, presentations, pitch materials
- **Web Artifacts Builder** — interactive HTML dashboards, data visualisations, org charts
- **Loop** — edits Microsoft Loop documents through browser automation

It handles a wide range of formats: Office documents, PDF, Markdown, images, code files, config files (.json, .yaml, .toml, .ini, .xml, .env), audio, video, and archives.

### Shell Commands

Scout executes shell commands on your machine — git, gh, curl, PowerShell, npm, docker, kubectl, and more. Every command is classified into one of three tiers:

| Tier | Behaviour | Examples |
|---|---|---|
| Auto-approve | Runs without prompting | `ls`, `cat`, `grep`, `git log`, `git diff`, `docker ps`, `npm list`, `gh pr list`, `kubectl get` |
| Prompt | Pauses for your approval | `npm install`, `git push`, `curl`, network requests, file writes |
| Deny | Blocked entirely | Destructive commands like `rm -rf /`, `format` |

You can customise which commands auto-approve and which are blocked from Settings > Permissions, and mark sensitive directories that always require explicit approval before access.

### Browser Control

Scout automates a browser using Playwright. It can navigate to any URL, click elements, type, fill forms, upload files, take full-page screenshots and snapshots, read console logs, inspect network requests, extract text content, and wait for elements to load. The bundled Loop skill uses this capability to edit Microsoft Loop documents.

### Microsoft 365 Integration

Scout connects directly to your M365 account with permissioned API access:

- **Email**: read, send, reply, forward, manage and move messages
- **Calendar**: view events, create meetings, find free/busy times across attendees, accept/decline invitations — it checks availability, respects out-of-office blocks, and resolves names to email addresses via your organisation's directory
- **Teams**: read chats, send messages
- **OneDrive**: browse, read, and upload files
- **People search**: resolve names, find contacts, look up reporting relationships

For questions that span multiple services — "What did John say about the product deadline across all channels?" — Scout uses **WorkIQ** to query across email, calendar, Teams, and documents simultaneously using AI reasoning.

### Autonomous Background Modes

This is where Scout diverges most sharply from any previous Copilot product. It can work while you're away.

**Heartbeat mode** runs a recurring prompt on a configurable schedule — every 15 minutes, 30 minutes, 1 hour, or 2 hours. You set the prompt (what Scout does on each check-in), the interval, the working days, and the working hours. Heartbeat has its own separate permission policy, more restrictive than interactive sessions: outbound messages use only generic content, never private data, and tentative calendar events are treated as busy. You can review a log of every check-in from the Heartbeat panel.

**Automations** are discrete tasks triggered on a schedule or by a condition you define. Unlike heartbeat — which uses a single repeating prompt — automations can be one-shot (run once and deactivate), condition-triggered (run when something becomes true), or recurring. You can even import automation definitions from GitHub repositories.

### Sub-Agent Delegation

For complex or parallelisable work, Scout launches specialised sub-agents that run in the background and report results when finished:

| Agent type | Best for |
|---|---|
| Explore | Fast codebase research across multiple files and modules |
| Task | Runs builds, tests, lints, installations |
| Code review | Analyses code changes for bugs and security issues |
| Research | Thorough web and repository searches with citations |
| General-purpose | Full toolset for complex multi-step work |

You can also request delegation explicitly: "Research how other teams implement caching, while you also start setting up the Redis configuration."

### Memory and Session History

Scout proactively saves important information as you work — you don't need to ask. Memories persist across sessions and track their provenance: session-inferred, imported, or external. Memories from external sources like emails and web pages are tagged as data, not instructions, protecting against prompt injection.

You can also search your past session history: "What did I work on last week?" or "How did I handle authentication in the previous project?" View and delete memories any time from Settings > Memory.

### Sensitivity Labels

Scout tracks Microsoft Information Protection (MIP) sensitivity labels on content you access during a session. When you read an email or file with a label like "Confidential," the session's sensitivity level elevates. Scout won't write labelled content to unprotected destinations — Teams channels, plain text files, external tools — and the current session sensitivity level is visible in the UI.

### Skills System

Skills extend what Scout knows how to do. There are three tiers:

| Tier | Location | Scope |
|---|---|---|
| Bundled | Shipped with the app | Always available, updated with app releases |
| Workspace | `~/.copilot/m-skills/` | Synced across devices via cloud sync |
| Global user | `~/.copilot/skills/` | Available on this machine in all conversations |

You can create custom skills by adding a folder with a `SKILL.md` file to `~/.copilot/skills/`. The file needs a YAML frontmatter block with a description, followed by instructions in Markdown. Scout discovers them automatically at the start of each conversation.

For Power Platform developers, this means you can write a skill that embeds your Dataverse conventions, solution ALM patterns, and pac CLI commands — and Scout will load it in every session without being prompted.

---

## How It Works: The Approval Loop

The interaction model is straightforward:

1. You describe what you want in the chat interface
2. Scout selects tools, works through the steps, and streams progress in real time — full markdown rendering with headings, tables, code blocks, Mermaid diagrams, and inline images
3. Before any sensitive action (sending email, running a command, writing files), Scout pauses and shows you exactly what it plans to do
4. You approve, always allow (adds to auto-approve list), or deny
5. Results appear in the conversation or are saved to your workspace

You can send follow-up messages at any time, even while Scout is still working. If your follow-up changes direction, Scout adjusts.

For shell commands specifically, Scout shows you the exact command before running it. You're never approving a black box.

Default settings on first install: WorkIQ connectivity is **on**, shell access is **on**, auto-approve is **off**. All actions require user confirmation until you explicitly enable auto-approve for specific capabilities.

---

## Microsoft Scout vs Copilot Chat

The simplest way to distinguish them:

| | Copilot Chat | Microsoft Scout |
|---|---|---|
| What it is | Cloud-based AI for drafting, summarising, answering questions | Desktop AI that acts on your files, shell, browser, and M365 |
| Best for | Fast, focused, single-task support | Multi-step workflows, local development, autonomous background tasks |
| Local file access | No | Yes — full workspace access |
| Shell commands | No | Yes — three-tier permissions |
| Browser control | No | Yes — Playwright automation |
| Autonomous background modes | No | Yes — heartbeat and automations |
| Works while you're away | No | Yes |

Copilot Chat is a tool you pick up and put down. Scout is infrastructure that keeps working.

---

## Access and Licensing Requirements

### What users need

- Windows 11 or macOS 12 Monterey or later
- A Microsoft 365 work or school account (personal accounts are not supported)
- An active **Microsoft 365 Copilot licence**
- A **GitHub Copilot Business or Enterprise licence** (billing for Scout runs through GitHub Copilot)
- Local Administrator permissions for installation

### What admins need to do first

Access requires two separate admin gates — both must be complete before any user can sign in. Installing the app grants nothing on its own.

**Gate 1: Enable Frontier in the M365 admin center**

1. M365 admin center → Copilot → Settings → View all → search "Frontier" → Copilot Frontier
2. Set access: No access / All users / Specific users
3. Allow approximately three hours to propagate

This makes Frontier available to assigned users but doesn't enable Scout sign-in on its own.

**Gate 2: Admin enablement — three required steps**

1. **Configure the Intune policy** — enables `AllowScoutFrontierAccess` on target devices. Download the ADMX/ADML templates for Windows and the `microsoft-scout.mobileconfig` for macOS from [github.com/microsoft/scout-resources](https://github.com/microsoft/scout-resources/tree/main/admins), import them in Intune admin center, create a configuration policy, enable the Frontier access setting, and assign to devices.

2. **Complete the admin attestation form** — required because Scout can route data outside M365 to GitHub Copilot's inference path. This is an additional gate beyond Frontier enrollment. Complete the [M365 Admin Frontier organisation sign-up form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRyKGkCGRU0tBnsDASQkbqxJUOUROWUI4SFc5MFI5TTZJSU5MWExFRDZDMC4u).

3. **Provision GitHub Copilot licences** for any users who don't already have them.

**Important**: If a user tries to sign in before both gates are complete, sign-in fails silently — there's no clear in-product error message. Confirm all gates are in place before troubleshooting on the client.

### User setup

Once admin gates are complete, users download from [https://aka.ms/msscout](https://aka.ms/msscout), sign in with M365 credentials, sign in with a GitHub account, configure a workspace directory, and optionally connect to Microsoft 365 for email, calendar, Teams, and OneDrive access.

---

## Enterprise Security and Governance

### The identity model

Every Scout agent operates with its own governed Entra identity — not a shared service account. Credentials are scoped to the task at hand and redacted from logs and diagnostics. When Scout acts on your behalf, the action is attributable to a known actor your directory already understands.

Access control is enforced before anything executes: agents can only reach resources and destinations you've approved. Data protection policies from **Microsoft Purview** — sensitivity labels, DLP — are enforced in the moment, before anything is sent or written. Scout operates within those controls; it doesn't bypass them.

### The data handling gap you need to know about

This is the detail that matters most for enterprise architects.

Scout's LLM interactions are processed through **GitHub Copilot**, which operates under separate terms. Prompts, content, and related data may be transmitted outside Microsoft 365, including to third-party model providers configured through GitHub Copilot. When data is processed through GitHub Copilot, several M365 protections **do not apply**: data residency commitments, retention policies, sensitivity label enforcement, eDiscovery, and other compliance controls.

Here's how the data splits:

- **Files created by Scout** → saved to your workspace directory on your local machine
- **Session and memory data** → stored in the user's OneDrive; covered by the Microsoft DPA and standard OneDrive controls per your Purview configuration
- **Automation instructions and MCP output** → stored locally on the end user's device; **not covered by the M365 DPA**; subject to your endpoint management and device controls

Scout does not use your data to train AI models.

If your organisation's M365 Copilot approval assumed full DPA coverage, Scout's GitHub Copilot processing path is a material change that warrants a review — the same category of concern as Claude Fable 5's data retention story.

---

## Work IQ: The Intelligence Layer

**Work IQ** (also written WorkIQ) is the cross-M365 intelligence engine that powers Scout's more complex queries. When you ask something that spans services — "Find everything related to the Q4 planning initiative" or "Summarise what happened in the Engineering channel this week" — Scout uses WorkIQ to query across email, calendar, Teams, and documents simultaneously using AI reasoning, then synthesises the results.

Work IQ also powers the "always-on" intelligence that builds over time: learning how you work, what you care about, and what needs to happen next. The more Scout is used, the more aligned it becomes to your priorities.

At Build 2026, Microsoft announced [new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/), making this intelligence layer available to third-party agents as well — not just Scout.

---

## OpenClaw: The Open-Source Foundation

Scout is built on OpenClaw, an open-source agentic framework that Microsoft adopted as the foundation for its Autopilot agent category. Microsoft is contributing policy conformance directly upstream to OpenClaw, meaning organisations running OpenClaw will be able to validate whether their environment is configured within their security and compliance requirements and get a verifiable, audit-ready answer.
This is the same open-source playbook Microsoft ran with VS Code and the editor ecosystem. Building on an open foundation means the enterprise governance tooling around Autopilot agents has a chance to become an ecosystem standard, not a Microsoft proprietary lock-in.

---

## The "Addiction" Controversy and Marketing vs. Reality

Before Scout was publicly available, [404 Media obtained an internal Microsoft strategy document](https://www.404media.co/microsoft-wants-to-make-people-addicted-to-scout-its-new-ai-assistant-internal-documents-reveal/) outlining how the team wanted to "make people addicted" to Scout before rolling out additional functionality. Satya Nadella's public response was blunt: *"Not sure what this document is or who is writing and leaking this nonsense! They may want to go work elsewhere."* The follow-up coverage from 404 Media ran with the headline: *"Satya Nadella 'Not Sure' Who Said Microsoft Wanted to Make Addictive AI, Is Looking for Guy Who Did This."*

The responsible AI angle here is genuine — Scout is designed to reach out to you proactively, live in the same chat interface as messages from real colleagues, and build context over time. The line between a useful always-on agent and one engineered for dependency is worth thinking about clearly before rolling it out broadly.

It's also worth being clear about what the current Frontier preview actually is versus the promotional video Microsoft released. The official announcement video uses a mock UI whose URL points to the consumer version of Copilot, not the M365 work version. As [Jukka Niiranen noted](https://www.perspectives.plus/p/scout-claw-cowork-tasks-opal-agent-365), most people watching won't have the technical ability to try the Frontier preview — so they won't immediately know it's aspirational rather than a shipping product. The docs themselves were revised multiple times in the first days after launch: the M365 Copilot licence requirement appeared, disappeared, and reappeared; the GitHub Copilot licence requirement was added after launch.

During preview testing, there's also been no apparent enforcement of the M365 Copilot licence gate — but Scout does burn **GitHub Copilot AI Credits**, not standard Copilot Credits. That's the actual billing unit to track if you're evaluating cost at scale.

---

## Known Limitations

Being clear about what Scout can't or won't do is as important as what it can:

- **Desktop only** — not available on mobile. Windows 11 or macOS 12 Monterey or later.
- **Workspace boundary** — Scout can't access files outside your configured workspace directory unless you explicitly grant permission.
- **Shell permissions apply** — dangerous commands are blocked by default. The three-tier system is enforced; you can't disable it entirely.
- **M365 authorisation boundary** — Scout can only access M365 data your account is already authorised to use.
- **Custom skills are unvalidated** — Microsoft does not validate user-authored skills. Review custom skill outputs carefully.
- **Background modes are more restricted** — heartbeat and automations run under a more conservative permission policy than interactive sessions.
- **Multi-step task reliability** — complex tasks with many dependencies may not always complete as expected. AI-generated content should be treated as drafts. Always review before sending, sharing, or deploying.
- **Not for high-stakes autonomous decisions** — Scout is not intended for legal filings, medical decisions, or financial transactions that bypass approval processes.

---

## What This Means for Power Platform and Enterprise Developers

Several things in Scout's architecture are directly relevant to Power Platform work.

**The Entra identity model is the right template for autonomous agents.** Power Automate flows running under service accounts or user context have always been a governance gap — you either share credentials or tie automation to a person's account. Scout demonstrates what a production-grade autonomous agent identity looks like: own Entra identity, scoped credentials, DLP enforcement in the moment, everything attributable. If you're designing autonomous agents for clients, this is the architecture to study.

**Scout is a practical productivity tool for Dataverse and Power Platform developers right now.** Write a custom skill at `~/.copilot/skills/` that embeds your Dataverse conventions, ALM patterns, pac CLI commands, and solution structure. Scout discovers it automatically. From that point you can ask it to scaffold solutions, run pac CLI commands, check Dataverse entity schemas, draft governance documentation, schedule follow-up meetings, and send status updates — all in one conversation. That's not a future vision; it's what the capability set supports today.

**The data handling boundary is the same conversation as Claude Fable 5.** LLM processing routes through GitHub Copilot, outside M365 DPA coverage. If your clients are in regulated industries or have strict data residency requirements, that processing path needs to be in your architecture review, not found later during a compliance audit.

**Work IQ as a platform matters.** The new Work IQ APIs announced at Build 2026 let you build agents that tap the same cross-M365 reasoning that powers Scout's intelligence layer. For Power Platform teams building agents that need to reason across M365 context — approvals, calendar, email, Teams — that's a significant capability unlock.

---

## Key Takeaways

- **Microsoft Scout** is Microsoft's first Autopilot agent — a new product category of always-on, identity-bearing, background-capable agents.
- It's a **desktop application** for Windows 11 and macOS 12+, currently in **Frontier private preview**.
- Scout acts on your **files, shell, browser, and Microsoft 365 data** with a tiered permission system and mandatory approval before sensitive actions.
- **Heartbeat mode** and **automations** let it work while you're away — on a schedule or triggered by conditions.
- **Sub-agent delegation** (5 types) enables parallel, isolated execution for complex work.
- **Each Scout agent has its own Entra identity** — not a shared service account. Actions are attributable and credentials are scoped.
- **LLM processing routes through GitHub Copilot**, outside M365 DPA coverage. Data residency, retention, and compliance controls from M365 do not apply to that processing path.
- **Custom skills** use the same `~/.copilot/skills/` pattern as GitHub Copilot — Power Platform/Dataverse developers can write skills that encode their domain conventions.
- **Access requires two admin gates** plus GitHub Copilot and M365 Copilot licences. Sign-in fails silently if gates aren't complete.
- Download at [https://aka.ms/msscout](https://aka.ms/msscout) after Frontier enrollment.

---

## References

- [Introducing Microsoft Scout: Your always-on personal agent](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) — Omar Shahine, Microsoft 365 Blog (June 2, 2026)
- [Microsoft Scout documentation](https://learn.microsoft.com/en-us/microsoft-scout/) — Microsoft Learn
- [Microsoft Scout (Frontier) overview](https://learn.microsoft.com/en-us/microsoft-scout/overview) — Microsoft Learn
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started) — Microsoft Learn
- [Use Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout) — Microsoft Learn
- [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview) — Microsoft Learn
- [Set up Microsoft Scout with Intune](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup) — Microsoft Learn
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq) — Microsoft Learn
- [Responsible AI overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview) — Microsoft Learn
- [Responsible AI FAQ for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq) — Microsoft Learn
- [Announcing the new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/) — Microsoft 365 Blog (June 2, 2026)
- [Work IQ APIs: The Future of Business Context](https://aidevme.com/work-iq-apis-microsoft-365-intelligence-layer-enterprise-agents/) — aidevme.com
- [Scout, Claw, Cowork, Tasks, Opal, Agent 365...](https://www.perspectives.plus/p/scout-claw-cowork-tasks-opal-agent-365) — Jukka Niiranen, Perspectives on Power Platform (June 12, 2026) *(paywalled after intro)*
- [Microsoft wants to make people "addicted" to Scout](https://www.404media.co/microsoft-wants-to-make-people-addicted-to-scout-its-new-ai-assistant-internal-documents-reveal/) — 404 Media

- [Article Angles to Consider](#article-angles-to-consider)

---

## Source URLs
- [Introducing Microsoft Scout: Your always-on personal agent](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) — Microsoft 365 Blog, Omar Shahine, June 2 2026
- [Microsoft Scout documentation](https://learn.microsoft.com/en-us/microsoft-scout/)
- [Microsoft Scout (Frontier) overview](https://learn.microsoft.com/en-us/microsoft-scout/overview)
- [Get started with Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/get-started)
- [Use Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout)
- [Admin access overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview)
- [Set up Microsoft Scout with Intune](https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup)
- [Microsoft Scout common questions](https://learn.microsoft.com/en-us/microsoft-scout/faq)
- [Responsible AI overview for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview)
- [Responsible AI FAQ for Microsoft Scout](https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq)

---

## What Is Microsoft Scout?

Microsoft Scout is a **desktop AI application** for Windows and macOS that takes action on your behalf across your files, shell, browser, and Microsoft 365 data. It was announced June 2, 2026 by Omar Shahine (CVP, Microsoft Scout) at Microsoft Build 2026.

It is Microsoft's **first Autopilot agent** — a new category Microsoft defines as "always-on agents that work autonomously, with their own identity, and act on your behalf."

It is currently in **Frontier private preview** (experimental release). Access requires Frontier enrollment, Intune policy configuration, and an admin opt-in attestation. Users must have a GitHub Copilot Business or Enterprise licence plus a Microsoft 365 Copilot licence.

It is **NOT generally available**. Not available on mobile. Desktop only (Windows 11 or later / macOS 12 Monterey or later).

**Internal codename**: The docs still reference "Clawpilot" in some pre-release Intune screenshots.

**Powered by**: OpenClaw open-source technology. Microsoft is contributing policy conformance upstream to OpenClaw.

---

## The "Autopilot" Category

This is a new product category Microsoft is introducing alongside Scout:

> "Autopilots are always-on agents that work autonomously, with their own identity, and act on your behalf."

Key properties of Autopilots:
- Stay active in the background
- Understand how work gets done across apps and systems
- Take action without needing to be prompted each time
- Operate with their **own Entra identity** (not a shared anonymous service account) — so everything they do is attributable
- Actions are attributable to a known actor your directory already understands

This is architecturally significant: each Scout agent has its own governed Entra identity. Scoped credentials. Redacted from logs. Managed like a first-party Microsoft service.

---

## What Scout Can Do: Full Capability List

### File system
- Read, write, search files in workspace directory
- Create Word (.docx), Excel (.xlsx), PowerPoint (.pptx) documents via bundled skills
- Web Artifacts Builder (interactive HTML dashboards, data visualizations, org charts)
- Edit Loop documents via browser automation
- Supported formats: Word, Excel, PowerPoint, PDF, Markdown, images (.png, .jpg, .gif, .webp, etc.), code files, config files (.json, .yaml, .toml, .ini, .xml, .env), audio, video, archives

### Shell
- Execute shell commands on your machine (git, gh, curl, PowerShell, npm, docker, kubectl, etc.)
- Three-tier permission system:
  - **Auto-approve**: ls, cat, grep, git log, git diff, docker ps, npm list, gh pr list, kubectl get
  - **Prompt** (pause for approval): npm install, git push, curl, network requests, file writes
  - **Deny** (always blocked): destructive commands like `rm -rf /`, `format`
- Customisable allow/deny patterns in Settings > Permissions
- Sensitive paths: require explicit approval before access

### Browser Control
- Playwright-based automation
- Navigate URLs, click, type, fill forms, upload files
- Take page snapshots and screenshots
- Read console logs and inspect network requests
- Extract text content
- Wait for elements to load
- Microsoft Loop integration (the bundled Loop skill uses browser control)

### Microsoft 365 Integration
- **Email**: read, send, reply, forward, manage/move emails
- **Calendar**: view events, create events, find free/busy times, accept/decline, automatically checks attendee availability, respects OOF blocks, resolves names to email via org directory
- **Teams**: read chats, send messages
- **OneDrive**: browse, read, upload files
- **People search**: resolve names, find contacts, look up reporting relationships
- **WorkIQ** (for complex cross-M365 queries): queries across email, calendar, Teams, documents using AI reasoning — e.g. "What did John say about the product deadline across all channels?"

### Autonomous Background Modes

**Heartbeat mode**:
- Periodic background check-ins (every 15 min, 30 min, 1 hour, or 2 hours)
- Configurable prompt, interval, work days, work hours
- Separate (more restrictive) permissions policy — since you're not present to approve
- Outbound messages use only generic content, never private data; tentative calendar events treated as busy
- Review log of recent check-ins in the Heartbeat panel

**Automations**:
- Independent tasks on a schedule or when a condition is met
- Schedule-triggered (e.g. "Every Monday at 9 AM") or Condition-triggered
- One-shot option (runs once and deactivates)
- Can import automation definitions from GitHub repositories
- Manage/enable/disable/edit/delete from Automations panel

### Sub-agent Delegation
Scout can launch specialised sub-agents that run in parallel:
| Agent type | Best for |
|---|---|
| Explore | Fast codebase research across multiple files and modules |
| Task | Runs builds, tests, lints, installations |
| Code review | Analyses code changes for bugs and security issues |
| Research | Thorough web + repository searches with citations |
| General-purpose | Full toolset for complex multi-step work |

### Memory and Session History
- Proactively saves important info as you work — no need to ask
- Memories persist across sessions
- Tracks provenance: session-inferred, imported, or external
- External-source memories (emails, web pages) tagged as data, not instructions
- Can search past session history: "What did I work on last week?" / "How did I handle auth in the previous project?"
- View and manage memories in Settings > Memory

### Sensitivity Labels (MIP)
- Tracks Microsoft Information Protection (MIP) sensitivity labels on accessed content
- Session sensitivity level elevates when you read labelled content
- Won't write labelled content to unprotected destinations
- Shows current session sensitivity level in the UI

### Skills System
Three tiers of skills:
| Tier | Location | Scope |
|---|---|---|
| Bundled | Shipped with app | Always available, updated with app releases |
| Workspace | `~/.copilot/m-skills/` | Synced across devices via cloud sync |
| Global user | `~/.copilot/skills/` | Available on this machine in all conversations |

Custom skills: create a folder under `~/.copilot/skills/`, add `SKILL.md` with YAML frontmatter description + instructions. Scout auto-discovers them.

Bundled skills: Word, Excel, PowerPoint, Loop, Web Artifacts Builder.

---

## How It Works (The Loop)

1. User describes task in natural language
2. Scout selects tools and works through steps, streaming progress in real time (full markdown: headings, tables, code blocks, Mermaid diagrams, inline images)
3. User approves sensitive actions (sending email, running commands, writing files) before execution
4. Results delivered in conversation or saved to workspace

**Action approval options**:
- Approve (one-time)
- Always allow (adds to auto-approve list)
- Deny (blocks the action)

For shell commands: exact command shown before approval.

---

## Scout vs Copilot Chat (Key Differences)

| | Copilot Chat | Microsoft Scout |
|---|---|---|
| What it is | Cloud-based AI for drafting, summarising, Q&A | Desktop AI that acts on files, shell, browser, M365 |
| Best for | Fast, focused single-task support | Multi-step workflows, local dev, autonomous background tasks |
| Local file access | No | Yes (full workspace access) |
| Shell commands | No | Yes (three-tier permissions) |
| Browser control | No | Yes (Playwright) |
| Autonomous modes | No | Yes (heartbeat + automations) |

---

## Access and Licensing Requirements

### User requirements
- Windows 11 or macOS 12 Monterey or later
- Microsoft 365 work/school account (no personal accounts)
- Active Microsoft 365 Copilot licence
- GitHub Copilot Business or Enterprise licence
- Local Administrator permissions for installation

### Admin gates (both must complete before users can sign in)

**Gate 1: Frontier access in M365 admin center**
1. M365 admin center → Copilot → Settings → View all → search "Frontier" → Copilot Frontier
2. Set access: No access / All users / Specific users
3. Allow ~3 hours to propagate

**Gate 2: Admin enablement (three steps — all required)**
1. Configure Intune policy (enables `AllowScoutFrontierAccess` on devices)
2. Complete the [M365 Admin Frontier organisation sign-up form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRyKGkCGRU0tBnsDASQkbqxJUOUROWUI4SFc5MFI5TTZJSU5MWExFRDZDMC4u) (admin attestation — required because Scout can route data outside M365)
3. Provision GitHub Copilot licences for users

**Then users**:
- Download from https://aka.ms/msscout
- Sign in with M365 credentials
- Sign in with GitHub account (billing runs through GitHub Copilot)
- Configure workspace directory
- Connect to Microsoft 365 (optional, for email/calendar/Teams/OneDrive)

**Important**: If users try to sign in before admin gates are complete, sign-in fails with no clear in-product error message. Admins must confirm all gates are in place before troubleshooting on the client.

### Intune setup (Windows)
- Download ADMX/ADML templates from https://github.com/microsoft/scout-resources/tree/main/admins
- Import `microsoft-scout.admx` and `microsoft-scout.adml` in Intune admin center
- Create configuration policy → Platform: Windows 10 and later → Templates → Imported Administrative Templates
- Enable "Allow Microsoft Scout Frontier access" (`AllowScoutFrontierAccess`)
- Assign to devices/groups

### Intune setup (macOS)
- Upload `microsoft-scout.mobileconfig` to a macOS Custom profile, Device channel
- Assign to devices/groups

---

## Enterprise Security and Governance

- **Entra identity**: Each Scout agent operates with its own governed Entra identity — not a shared service account. All actions are attributable.
- **Credentials**: Scoped to the task, redacted from logs/diagnostics, managed like a first-party Microsoft service.
- **Access control**: Agents can only reach resources and destinations you've approved. Sensitive actions require human sign-off.
- **Purview integration**: Data protection policies from Microsoft Purview (sensitivity labels, DLP) are enforced in-the-moment before anything is sent or written.
- **Authentication**: MSAL (Microsoft Authentication Library) with WAM (Web Account Manager) on Windows.
- **Tenant isolation**: M365 data is isolated to your organisation's tenant, subject to existing security, compliance, and governance controls.
- **Prompt injection protection**: External content (emails, web pages, Teams messages) is tagged as untrusted and treated as data, not instructions.

### Data handling notes (important for enterprise architects)
- **LLM interactions** are processed through GitHub Copilot, which operates under **separate terms**. Prompts, content, and related data may be transmitted outside Microsoft 365, including to third-party model providers through GitHub Copilot.
- When processed through GitHub Copilot, certain M365 protections **do NOT apply**: data residency commitments, retention policies, sensitivity label enforcement, eDiscovery, and other compliance controls.
- **Files** created by Scout → saved to workspace directory on local machine
- **Session and memory data** → stored in user's OneDrive; covered by Microsoft DPA and standard OneDrive controls per Purview configuration
- **Automation instructions and MCP output** → stored locally on the end user's device; NOT covered by M365 DPA; subject to endpoint management and device controls
- Scout does NOT use your data to train AI models.

---

## Work IQ

Scout uses **Work IQ** (sometimes written "WorkIQ") for complex cross-M365 queries and for its autonomous background intelligence:
- Queries across email, calendar, Teams, and documents using AI reasoning
- Powers the "always-on" intelligence that builds context over time
- Learning how you work, what you care about, what needs to happen next
- Microsoft also announced [new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/) at Build 2026 for third-party agent use

---

## OpenClaw Open Source

- Scout is powered by OpenClaw open-source technology
- Microsoft is contributing policy conformance upstream to OpenClaw
- Organisations running OpenClaw will be able to validate whether their environment is configured within security and compliance requirements (verifiable, audit-ready)

---

## Known Limitations

- Not available on mobile (desktop only)
- Cannot access files outside workspace directory unless explicitly granted
- Shell commands subject to three-tier permission system; dangerous commands blocked by default
- Browser control requires bundled Playwright
- Can only access M365 data your account is authorised to use
- Microsoft does NOT validate custom skills authored by users
- Background modes use a more restrictive permission policy than interactive conversations
- Complex, multi-step tasks with many dependencies may not always complete as expected
- May misinterpret ambiguous or overly broad instructions
- AI-generated content should be treated as drafts — always review before sending/sharing/deploying

---

## Default Settings on First Install

- WorkIQ connectivity: **ON**
- Shell access: **ON**
- Auto-approve: **OFF** (all actions require user confirmation; must explicitly enable per capability)

---

## Mini Mode

Compact, always-visible window for quick interactions. Configurable: start in mini mode, always-on-top behaviour, keyboard shortcut to toggle.

---

## Personality Presets

Scout offers personality presets that change conversational style. Default is helpful and professional. Switchable anytime via the application icon next to the prompt entry field.

---

## Intended Use Cases (Per Microsoft)

- Building and testing software projects
- Exploring and editing codebases
- Automating web workflows (filling forms, extracting data from portals)
- Managing Microsoft 365 data (emails, meetings, files)
- Running autonomous background tasks (inbox triage, schedule monitoring, recurring reports)
- Creating structured documents from unstructured input

**NOT intended for**: legal filings, medical decisions, financial transactions that bypass approval processes, or any use requiring guaranteed accuracy without human review.

---

## Responsible AI Safeguards

- Approval prompts before sensitive actions (send email, post in Teams, run commands)
- Pause, resume, cancel at any time
- External content tagged as untrusted (prompt injection protection)
- Sensitivity label tracking (MIP)
- Shell permission tiers (auto-approve, prompt, deny)
- Sensitive path protection
- Separate (more restrictive) permissions for background modes
- Admins can disable or restrict autonomous execution modes at the org level

---

## Key Dates and Context

- June 2, 2026: Announced at Microsoft Build 2026 by Omar Shahine (CVP, Microsoft Scout)
- Microsoft employees had an early desktop experience before the announcement
- Currently extending to a select group of customers in private preview and Frontier organisations
- Related announcements at Build 2026: Work IQ APIs GA, Frontier Tuning, Teams platform agent collaboration

---

## Article Angles to Consider

1. **Power Platform angle**: Scout has its own Entra identity — this changes the agent identity model. Power Platform developers building autonomous agents can learn from how Scout approaches permissioned identity, scoped credentials, and DLP enforcement. Compare to how Power Automate flows run under a service account vs. user context.

2. **Developer productivity angle**: Scout is GitHub Copilot + local file system + M365 + browser automation all in one agent. For Power Platform/Dataverse developers this means: scaffolding, running pac CLI commands, checking Dataverse solutions, sending status updates, scheduling meetings — all from one conversational interface.

3. **Enterprise governance angle**: The two-admin-gate model, Entra identity per agent, M365 DPA boundaries vs. GitHub Copilot processing, MIP label tracking — this is the governance story for IT decision-makers.

4. **Autopilot category angle**: What does "always-on, own identity, acts on your behalf" mean for the future of enterprise software? Scout is the first concrete product in this category. The heartbeat mode and automations are the mechanism. Work IQ is the intelligence layer.

5. **The data handling gap**: LLM interactions route through GitHub Copilot, outside M365 compliance boundaries. This is the key gotcha for enterprise architects — the same pattern as Claude Fable 5's data retention story. Worth naming explicitly.

6. **OpenClaw and open-source**: Microsoft contributing to an open-source foundation for Autopilot agents is strategically interesting — same playbook as VS Code and the editor ecosystem.

7. **Custom skills**: The `~/.copilot/skills/` pattern is the same pattern used by GitHub Copilot's custom skills system. Power Platform/Dataverse developers can write skills that know Dataverse conventions, solution ALM, pac CLI patterns — Scout discovers them automatically.
