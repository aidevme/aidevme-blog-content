# Work IQ APIs: Microsoft Just Replaced the Graph Approach for Agent Builds

*Microsoft's new intelligence layer goes GA June 16. If you've ever watched an agent burn through a context window reading email metadata to find three useful facts, this is the direct fix for that.*

---

If you've built agents on Microsoft Graph, you know the pattern. One user question. Five API calls. Context window fills with message IDs, file record strings, and app identifiers the agent doesn't need. Token costs compound. Reliability drops because the agent now has to reason through noise to get to signal.

Work IQ is Microsoft's answer to that problem — and it goes generally available on **June 16, 2026**.

It's the intelligence layer that's been running underneath Microsoft Scout, Copilot Cowork, and M365 Copilot itself. Now open to anyone building agents. There's also an open-source MCP server and CLI you can install right now.

## What Work IQ actually does differently

Graph returns data. Work IQ returns context.

An agent asking "what's the status of Project Alpha?" doesn't get a list of emails to parse. It gets a synthesised answer grounded in the aggregate of everything that's happened across email, Teams, calendar, and files. Work IQ's internal LLMs do that pre-processing before the result reaches your agent.

Three numbers that make this concrete:

- **2x faster** than traditional Graph-based API calls
- **80% fewer tokens** consumed in agent coding harnesses (Microsoft internal testing)
- **10 MCP tools** instead of the hundreds of endpoints a full Graph integration requires

The token reduction is the one that changes your economics most directly. The processing happens server-side in the Work IQ runtime — your context window gets business context, not raw data. That 80% gap is the difference between an agent that fits its reasoning into one turn and one that spirals through three just to establish what it's looking at.

The tool count reduction matters for reliability. Every tool in a context window is a decision point for the model. Fewer tools means less overhead on selection and more capacity for actual work.

## The architecture: four domains

Work IQ is organised into four domains, each covering a different thing an agent needs to do:

**Chat** — Programmatic access to M365 Copilot's full intelligence. Pass a query, get back the synthesised answer with citations. Right for when you want the intelligence layer to do the reasoning.

**Context** — The same source material Copilot would use, returned in agent-consumable format rather than as a finished response. Right for when your agent needs to reason over the raw input itself.

**Tools** — Send emails, schedule meetings, upload documents. A small stable set of verbs, intentionally kept narrow so the API contract doesn't shift under your agent as data changes.

**Workspaces** — This is the one worth understanding deeply if you're building enterprise agents. It's intermediate state storage inside the M365 tenant boundary. Long-running agents need somewhere to stash partial outputs and progress between steps — somewhere that isn't a separate database you have to govern independently. Workspaces solve that problem. Scout and Copilot Cowork both depend on it. As Work IQ rolls out, expect this to become the standard pattern for multi-step agents across the M365 and Power Platform stack.

## Getting started today

The MCP server and CLI are in public preview now. You don't have to wait for June 16.

```bash
npm install -g @microsoft/workiq
workiq accept-eula
workiq ask -q "What meetings do I have tomorrow?"
```

Or via GitHub Copilot CLI:

```bash
/plugin marketplace add microsoft/work-iq
/plugin install workiq@work-iq
/plugin install workiq-preview@work-iq
```

There are four plugins: `workiq` for natural language M365 queries, `workiq-preview` for structured read/write entity access, `microsoft-365-agents-toolkit` for declarative agent scaffolding and eval, and `workiq-productivity` for read-only org insights. The preview plugin is worth installing alongside the standard one — it adds fetch, create, update, delete, schema discovery, and blob operations. That's a full read/write M365 surface via MCP.

One practical note: Work IQ requires admin consent on first access. If you're not a tenant admin, you'll need someone to grant it before any of this works.

## What this means for Power Platform developers

Work IQ is where Microsoft wants you to move for M365 context in agent architectures — away from custom Graph connectors, toward this surface. The 10-tool MCP interface improves agent reliability in ways that a direct Graph integration just can't match structurally.

If you're currently building Graph API custom connectors for email, calendar, or Teams data in Copilot Studio or Power Automate: compare that path against `workiq-preview` before you commit. The capabilities overlap significantly, and the token economics don't.

The Workspaces domain also closes a real gap in enterprise agent design. The question of where long-running agents store intermediate state without introducing a separately governed data store has always been awkward. Workspaces are the answer Microsoft is standardising on — and it's the kind of thing worth understanding before it becomes the expected pattern in client engagements.

---

I wrote the full breakdown on AIDevMe — all five advantages with the numbers behind them, the complete API architecture, pricing on Copilot Credits, full getting-started guide, and what it means specifically for Power Platform developers.

**[Read the full article →](https://aidevme.com/work-iq-apis-microsoft-365-intelligence-layer-enterprise-agents/)**

---

*Building agents on M365 or evaluating Work IQ for a client engagement? Reply and let me know what you're working on — always interested in what enterprise teams are running into in practice.*
