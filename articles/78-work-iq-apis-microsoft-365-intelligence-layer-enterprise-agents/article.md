# Work IQ APIs: Microsoft's New Intelligence Layer for Enterprise Agents Is Now Generally Available

**WordPress SEO**
- **Focus keyphrase:** Work IQ APIs Microsoft 365
- **SEO title:** Work IQ APIs: Microsoft's M365 Intelligence Layer for Enterprise Agents
- **Meta description:** Microsoft's Work IQ APIs go GA on June 16, 2026 — bringing 2x faster retrieval, 80% fewer tokens, and a 10-tool MCP surface for building agents on top of M365 data. Here's what developers need to know.
- **Slug:** work-iq-apis-microsoft-365-intelligence-layer-enterprise-agents
- **Excerpt:** Work IQ is Microsoft's new intelligence layer for Microsoft 365, announced at Build 2026 and going generally available June 16, 2026. It gives agents — and the developers building them — a way to work with business context rather than raw data: 2x faster than traditional APIs, 80% fewer tokens, 10 MCP tools instead of hundreds, and full M365 tenant security. This post covers the architecture, the five core advantages, how to get started with the MCP server and CLI today, and what it means for Power Platform developers building on Dataverse and M365.
- **Categories:** AI & Copilot, Model Context Protocol, Power Platform
- **Tags:** Microsoft AI, AI Agents, Agentic AI, MCP Server, Model Context Protocol, GitHub Copilot CLI, Copilot Credits, Power Platform AI, Enterprise AI, Microsoft Copilot Studio, Enterprise Architecture, AI Agent Development

---

If you've built agents on Microsoft Graph, you know the problem. You make five API calls to pull context for one question. The agent's context window fills with message IDs, file record strings, and metadata it doesn't need. Token costs multiply. Reliability drops.

Work IQ is Microsoft's answer to that. It's a new API surface — generally available **June 16, 2026** — that returns business context instead of raw data. The intelligence layer already powering Microsoft Scout, Copilot Cowork, and M365 Copilot itself. Now open to developers.

There's also an open-source MCP server and CLI you can install today. This post covers what Work IQ is, how the architecture works, what the numbers mean in practice, and how to get started.

---

## Table of Contents

- [What Is Work IQ?](#what-is-work-iq)
- [The Five Core Advantages](#the-five-core-advantages)
  - [Intelligence](#intelligence)
  - [Speed](#speed)
  - [Efficiency](#efficiency)
  - [Scale](#scale)
  - [Security](#security)
- [The API Architecture: Four Domains](#the-api-architecture-four-domains)
- [Pricing: Copilot Credits and the New Cost Dashboard](#pricing-copilot-credits-and-the-new-cost-dashboard)
- [Getting Started: The MCP Server and CLI](#getting-started-the-mcp-server-and-cli)
  - [Quick Start with GitHub Copilot CLI](#quick-start-with-github-copilot-cli)
  - [Standalone MCP Server in VS Code](#standalone-mcp-server-in-vs-code)
  - [Available Plugins](#available-plugins)
  - [Admin Consent Requirement](#admin-consent-requirement)
- [What This Means for Power Platform Developers](#what-this-means-for-power-platform-developers)
- [Key Takeaways](#key-takeaways)
- [References](#references)

---

## What Is Work IQ?

Work IQ continuously processes content from email, calendar, meetings, chats, files, people, collaboration patterns, and line-of-business systems to build a semantic understanding of how your organisation operates. Not a search index. Not a document store. A real-time model of how work actually gets done.

The difference from Microsoft Graph is what gets returned. Graph returns data. Work IQ returns context. An agent asking "what's the status of Project Alpha?" doesn't get a list of emails to read through — it gets a synthesised answer grounded in the aggregate of everything that's happened across email, Teams, calendar, and files. Work IQ's internal LLMs and agents do that pre-processing before the result reaches your agent.

Microsoft Scout, Copilot Cowork, and M365 Copilot itself all run on this layer. The GA announcement makes that same layer available to anyone building agents.

For context on the scale involved: Microsoft's internal data from May 2026 puts the average Work IQ data footprint across Fortune 500 organisations at **over 600 terabytes**. That's not stored data — that's the live semantic index being continuously maintained.

---

## The Five Core Advantages

Microsoft benchmarks Work IQ against Microsoft Graph and direct REST endpoints. Each advantage comes with a specific number — here's what those numbers actually mean for your agent builds.

### Intelligence

Work IQ is built on a semantic index with ultra-low latency, personal memory, personal and organisational skills, structured schema on top of files, and business-specific knowledge tuning. Agents get the most relevant, continuously updated context — not just content matches, but a full understanding of people, roles, org structure, and collaboration patterns.

That last part is what Graph can't give you. Graph can tell you who sent an email. Work IQ can tell you who actually makes the decisions on a project, based on the full pattern of who's in meetings, who's cc'd on what, and whose input gets acted on.

### Speed

**2x faster run time** than traditional APIs. The mechanism is straightforward: Work IQ aggregates context server-side so your agent makes fewer round trips. But the more important gain for developers is the tool count. Work IQ exposes M365 data through **10 generic tools with progressive disclosure** via MCP — not the hundreds of data-specific endpoints that Graph-based integration requires.

Fewer tools means your agent spends less context budget describing what tools are available and more time actually using them. That's a reliability improvement, not just a speed one.

### Efficiency

**80% fewer tokens** than traditional APIs in coding harnesses (Microsoft internal testing). Work IQ's internal LLMs pre-process content before it reaches your agent — trimming file record strings, message IDs, and app IDs that your agent would otherwise have to read and discard. The processing happens in the Work IQ runtime, not in your context window.

If you've built Graph-based agents and watched the token meter run while your agent reads through pages of metadata to extract three relevant facts, this is the direct fix for that problem.

### Scale

Human software usage is intermittent and shallow. Agent usage is continuous, high-frequency, and systematic — and it's going to get much heavier. Microsoft is explicitly designing Work IQ for the throughput of "hundreds of millions of agents" coming online over the next few years. The M365 infrastructure is being rebuilt to handle that load.

For now this matters mainly as a signal: Microsoft is treating agents as first-class API consumers, not afterthoughts bolted onto a human-facing platform.

### Security

All data, context, and insights stay within the M365 tenant trust boundary. Agent operations are auditable and discoverable. You can build enterprise agents without adding a separate governance layer — the security controls are in the API surface itself, not a wrapper you have to build around it.

---

## The API Architecture: Four Domains

Work IQ is organised into four domains. Think of them as the four things an agent needs to do its job: get a synthesised answer, get raw context to reason over, take actions, and store state between steps.

**Chat** — Programmatic access to M365 Copilot's full intelligence. Pass a query, get back the response (with citations) that Copilot would return to a user. This is the right domain when your agent needs a synthesised answer and you want the intelligence layer to do the reasoning.

**Context** — Agent-ready context without the synthesis. The Context API returns what Copilot would use to answer a query — but in a format your agent consumes directly, rather than as a finished response. Use this when your agent needs to do its own reasoning over the source material.

**Tools** — Actions on M365 entities: send emails, schedule meetings, upload documents, and more. The surface is a small set of verbs with resource paths, intentionally kept stable so your agent can work across new data and changing scenarios without the API contract shifting underneath it.

**Workspaces** — Intermediate state storage inside the M365 tenant boundary. Long-running agents need somewhere to stash partial outputs, memory, and progress between steps — somewhere that isn't an external database you have to govern separately. Workspaces solve that. Microsoft built Scout and Copilot Cowork on top of this domain; it's the enabler that makes multi-hour agentic work actually feasible inside an enterprise boundary.

---

## Pricing: Copilot Credits and the New Cost Dashboard

Work IQ APIs are priced on consumption, denominated in **Copilot Credits**:

- **Tools**: fixed component per operation
- **Chat and Context**: variable component based on usage

Alongside the GA, Microsoft is launching a new **cost management dashboard in the M365 admin center** — and Work IQ APIs are the first product it covers. From there, IT admins can review AI credit usage, switch between prepaid and pay-as-you-go billing, set spending limits at tenant, group, and user level, and monitor credit requests from users. Copilot Studio will follow.

If you're evaluating Work IQ for a client engagement, this is the governance story: consumption billing with tenant-level spending controls built in from day one. Details at [aka.ms/WorkIQ/licensing](https://aka.ms/WorkIQ/licensing).

---

## Getting Started: The MCP Server and CLI

You don't have to wait for June 16. The MCP server and CLI are in public preview now at [github.com/microsoft/work-iq](https://github.com/microsoft/work-iq). The npm package is `@microsoft/workiq`.

**Prerequisite**: Node.js 18+ (npm and npx included).

### Quick Start with GitHub Copilot CLI

```bash
# 1. Open GitHub Copilot CLI
copilot

# 2. Add the Work IQ plugin marketplace (one-time setup)
/plugin marketplace add microsoft/work-iq

# 3. Install plugins
/plugin install workiq@work-iq
/plugin install workiq-preview@work-iq
/plugin install workiq-productivity@work-iq
/plugin install microsoft-365-agents-toolkit@work-iq
```

After restarting Copilot CLI, you can immediately ask questions like:

- "What are my upcoming meetings this week?"
- "Summarise emails from Sarah about the budget"
- "Find documents I worked on yesterday"
- "What did John say about the proposal?"
- "Summarise today's messages in the Engineering channel"

### Standalone MCP Server in VS Code

Click to install directly in VS Code:

```
https://vscode.dev/redirect/mcp/install?name=workiq&config={"command":"npx","args":["-y","@microsoft/workiq","mcp"]}
```

Or add manually to your MCP configuration:

```json
{
  "workiq": {
    "command": "npx",
    "args": ["-y", "@microsoft/workiq@latest", "mcp"],
    "tools": ["*"]
  }
}
```

Or install globally and run as a CLI:

```bash
npm install -g @microsoft/workiq

# Accept EULA (required on first use)
workiq accept-eula

# Interactive mode
workiq ask

# Single question
workiq ask -q "What meetings do I have tomorrow?"

# With a specific tenant
workiq ask -t "your-tenant-id" -q "Show my emails"

# Start MCP server
workiq mcp
```

Platform support: Windows (x64, arm64), Linux (x64, arm64), macOS (x64, arm64).

### Available Plugins

| Plugin | Description |
|---|---|
| `workiq` | Natural language queries over M365 data — emails, meetings, documents, Teams messages, people |
| `workiq-preview` | Same as workiq plus broader entity tools: fetch, create, update, delete, do-action, call-function, blob upload/download, schema discovery |
| `microsoft-365-agents-toolkit` | Toolkit for building and evaluating M365 Copilot declarative agents — scaffolding, manifest authoring, capability configuration, eval workflows |
| `workiq-productivity` | Read-only productivity insights — email triage, meeting costs, org charts, channel audits |

The full plugin catalog with skill listings, example prompts, and installation instructions is in [PLUGINS.md](https://github.com/microsoft/work-iq/blob/main/PLUGINS.md).

### Admin Consent Requirement

Work IQ needs permissions that require administrative rights on the tenant. On first access, a consent dialog appears. If you're not a tenant admin, you'll need your admin to grant consent.

For tenant admins: the [Tenant Administrator Enablement Guide](https://github.com/microsoft/work-iq/blob/main/ADMIN-INSTRUCTIONS.md) covers granting admin consent, including a one-click consent URL.

---

## What This Means for Power Platform Developers

**Work IQ is the Graph replacement for M365 context in agent architectures.** If you're building Copilot Studio agents, Power Automate flows, or custom connectors that call Graph endpoints to retrieve email, calendar, or Teams data, this is where Microsoft wants you to move. Fewer tools, 80% fewer tokens, better context. The 10-tool MCP surface isn't just an ergonomic improvement — it directly improves agent reliability by reducing how much decision-making overhead goes into tool selection.

**The `workiq-preview` plugin is worth installing today.** The standard `workiq` plugin gives you natural language queries. The preview plugin adds structured entity tools — fetch, create, update, delete, do-action, call-function, blob upload/download, schema discovery. That's a read/write M365 surface via MCP. If you're currently building Graph API custom connectors for M365 data access, compare that path against `workiq-preview` before you commit.

**The `microsoft-365-agents-toolkit` plugin is the Copilot Studio eval story.** Scaffolding, manifest authoring, capability configuration, and eval workflows for M365 declarative agents, all accessible from Copilot CLI. If you're shipping declarative agents to enterprise clients and you don't have a structured evaluation step in your build process, this closes that gap.

The Workspaces domain deserves a separate call-out. Long-running enterprise agents have always had an awkward problem: where do you store intermediate state between steps without introducing a separate governed data store? Workspaces put that storage inside the M365 tenant boundary, under the same controls as the rest of your data. Scout and Copilot Cowork both depend on it. As Work IQ rolls out, you'll see this show up as the standard pattern for multi-step agents across the M365 and Power Platform stack — and it's worth understanding how it works before that becomes the expectation in client engagements.

---

## Key Takeaways

- **Work IQ APIs go GA on June 16, 2026** — announced at Build 2026 by Charles Lamanna (EVP, Copilot, Agents, and Platform).
- Work IQ is the intelligence layer already powering **Microsoft Scout**, **Copilot Cowork**, and **Microsoft 365 Copilot** — now available to developers.
- **5 advantages over traditional APIs**: intelligence (semantic index, not search), speed (2x faster, 10 MCP tools vs. hundreds), efficiency (80% fewer tokens), scale (designed for agent-frequency usage), security (M365 tenant boundary, auditable).
- **4 API domains**: Chat (M365 Copilot programmatic access), Context (agent-ready context), Tools (M365 entity actions), Workspaces (intermediate state for long-running agents).
- **Pricing**: consumption-based in Copilot Credits; new cost management dashboard in M365 admin center with spending limits at tenant/group/user level.
- **MCP server and CLI available now**: `npm install -g @microsoft/workiq` or `npx -y @microsoft/workiq mcp`. GitHub repo: [microsoft/work-iq](https://github.com/microsoft/work-iq).
- **4 plugins**: `workiq`, `workiq-preview` (read/write entity tools), `microsoft-365-agents-toolkit` (declarative agent scaffolding + eval), `workiq-productivity` (read-only insights).
- **Admin consent required** before first use. See [ADMIN-INSTRUCTIONS.md](https://github.com/microsoft/work-iq/blob/main/ADMIN-INSTRUCTIONS.md).

---

## References

- [Work IQ APIs: The Future of Business Context](https://aidevme.com/work-iq-apis-microsoft-365-intelligence-layer-enterprise-agents/) — aidevme.com
- [Announcing the new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/) — Charles Lamanna, Microsoft 365 Blog (June 2, 2026)
- [microsoft/work-iq — MCP Server and CLI for accessing Work IQ](https://github.com/microsoft/work-iq) — GitHub
- [Work IQ pricing](https://aka.ms/WorkIQ/licensing) — Microsoft
- [Tenant Administrator Enablement Guide](https://github.com/microsoft/work-iq/blob/main/ADMIN-INSTRUCTIONS.md) — microsoft/work-iq on GitHub
- [PLUGINS.md — Full plugin catalog](https://github.com/microsoft/work-iq/blob/main/PLUGINS.md) — microsoft/work-iq on GitHub
- [Introducing Microsoft Scout: Your always-on personal agent](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) — Omar Shahine, Microsoft 365 Blog (June 2, 2026)
