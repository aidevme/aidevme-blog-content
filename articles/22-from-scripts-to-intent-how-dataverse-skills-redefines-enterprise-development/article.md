# From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development

> **Series:** Dataverse Skills Deep Dive · Part 1 of 4  
> **Audience:** Power Platform developers & solution architects  
> **Level:** Intermediate to advanced  
> **Published:** April 2026

---

## WordPress Metadata

**Categories:**
- Power Platform
- AI & Copilot
- Microsoft Dataverse
- Developer Tools

**Tags:**
- Dataverse Skills
- GitHub Copilot
- Claude Code
- Power Platform CLI
- AI-Assisted Development
- Intent-Driven Development
- MCP Server
- Dataverse Python SDK
- Power Platform Development
- Low-Code Development
- Enterprise Development
- Microsoft Power Platform

**SEO Title:** Dataverse Skills: How AI Agents Redefine Power Platform Development | Intent-Driven Coding

**Meta Description:** Discover how Microsoft's Dataverse Skills transforms Power Platform development from manual scripting to AI-driven intent. Learn how GitHub Copilot and Claude Code build complete Dataverse solutions from natural language prompts.

**Excerpt:**
Microsoft's Dataverse Skills represents a paradigm shift in Power Platform development—from manual tool orchestration to intent-driven AI coding. This open-source plugin for GitHub Copilot and Claude Code eliminates the developer tax of context-switching between PAC CLI, maker portal, and API documentation. Instead of writing scripts, developers describe their intent in natural language, and AI agents build complete Dataverse solutions automatically. Learn how this changes enterprise development workflows, why it matters for solution architects, and what skills-based development means for the future of low-code platforms.

---

## Table of Contents

- [Introduction](#introduction)
- [The Old Way: Tool Juggling as a Developer Tax](#the-old-way-tool-juggling-as-a-developer-tax)
- [The Paradigm Shift: Intent-Driven Development](#the-paradigm-shift-intent-driven-development)
- [What Are Dataverse Skills Exactly?](#what-are-dataverse-skills-exactly)
- [Why This Matters for Enterprise Platforms](#why-this-matters-for-enterprise-platforms)
- [The Broader Ecosystem This Unlocks](#the-broader-ecosystem-this-unlocks)
- [What This Means for You as a Developer or Architect](#what-this-means-for-you-as-a-developer-or-architect)
- [FAQ](#faq)
- [References & Further Reading](#references--further-reading)

---

## Introduction

On April 1, 2026, Microsoft's Dataverse team shipped something that, quietly, changes the developer experience on Power Platform more than anything since the introduction of the Power Platform CLI.

Specifically, it is called **Dataverse Skills** — an open-source plugin for coding agents like GitHub Copilot and Claude Code that gives them deep, structured knowledge of how to build and manage Dataverse solutions from end to end.

However, to understand why this matters, you have to first understand the problem it solves.

---

## The Old Way: Tool Juggling as a Developer Tax

Anyone who has built non-trivial Dataverse solutions knows the pattern. Indeed, a typical session looks something like this:

1. First, you open the Power Platform CLI to authenticate and select an environment.
2. Next, you switch to the maker portal to visually inspect an existing table schema.
3. Then, you open the official OData Web API docs to look up the correct request format for creating a lookup column.
4. Subsequently, you write a Python or PowerShell script to bulk-load sample data, get the column logical names wrong on the first attempt, fix them, run it again.
5. Afterwards, you switch back to the CLI to export the solution.
6. Finally, you realise you forgot to add the new table to the solution. You go back.

This constant context-switching — between CLI, browser, API docs, and scripts — is what I call the **developer tax** on enterprise platforms. Clearly, the knowledge exists. Similarly, the tools exist. However, the orchestration is manual, error-prone, and slow.

Moreover, the cognitive load is especially high for architects who are context-switching across multiple projects and environments simultaneously.

### The Traditional Toolchain

| Task | Tool |
|------|------|
| Authentication & environment management | PAC CLI (`pac auth create`, `pac org select`) |
| Schema inspection | Maker portal or direct OData API calls |
| Solution ALM | PAC CLI (`pac solution export/import`) |
| Bulk data operations | Custom Python/PowerShell scripts |
| FetchXML / OData queries | Query builder or hand-crafted requests |
| Table/column creation | Maker portal or Web API calls |

Each tool has its own authentication model, its own syntax, and its own documentation set. As a result, bringing a new developer onto a project means teaching all of them. Furthermore, this onboarding overhead compounds as teams grow.

---

## The Paradigm Shift: Intent-Driven Development

The shift happening right now in enterprise software is from **writing code** to **directing agents**. Instead of stitching together APIs, CLIs, and scripts, developers describe intent and let agents execute.

Furthermore, for enterprise platforms like Dataverse, this creates a specific requirement: **they must be operable by agents, not just by humans**.

Indeed, this is precisely what Dataverse Skills addresses.

For example, consider the recruiting system example from the official release blog:

```
"I'm building a recruiting system for Zava Construction. I need tables for 
Positions, Candidates, Interviewers, Interviews, and Feedback — with lookups, 
a many-to-many between Candidates and Positions, and a self-referential 
interview chain. Create everything in a ZavaRecruiting solution, load sample 
data, and show me which candidates are currently interviewing."
```

From that single natural language prompt, the agent:

1. First, discovers the Dataverse environment and configures the MCP connection
2. Then, creates the solution using PAC CLI
3. Next, builds five tables with choice columns, lookups, and a M:N relationship
4. Subsequently, generates and executes a Python script to bulk-load realistic sample data
5. Finally, queries across tables and returns the business answer

Notably, no skill names are invoked manually. No tool flags. No context switching. Instead, the agent handles the full orchestration.

### The Key Insight

Ultimately, the most important design decision in Dataverse Skills is this: **the user never invokes a skill directly**. Instead, you describe your intent, and the agent determines which skills to load, in what order, using which tools.

In other words, skills are the agent's knowledge. Natural language is the interface.

Consequently, this is a fundamentally different mental model from traditional CLI-based automation, where you have to know the exact command, flags, and sequence. In contrast, with Skills, you describe *what you want to achieve*, and the agent figures out *how to achieve it*.

---

## What Are Dataverse Skills Exactly?

Dataverse Skills is an open-source GitHub repository (`microsoft/Dataverse-skills`) that contains a structured collection of Markdown files. Specifically, each file is a "skill" — a self-contained unit of knowledge about how to perform a specific Dataverse operation.

Moreover, the skills are organized into three phases:

### Phase 1: Connect

The agent discovers your environments, authenticates via PAC CLI or Azure CLI, registers the Dataverse MCP server, and initializes a consistent project structure. Essentially, you configure nothing — the agent handles discovery and setup.

Key operations covered:
- `pac auth create` and environment discovery
- Dataverse MCP server registration (`/api/mcp` endpoint)
- Project structure initialization

### Phase 2: Build

Next, the agent creates solutions, tables, columns, lookups, many-to-many relationships, forms, and views. Importantly, it knows which tool is right for each operation:

- **MCP server** for quick reads and metadata operations
- **Dataverse Python SDK** for bulk operations
- **Web API** for schema modifications

Notably, every component is automatically added to the active solution.

### Phase 3: Operate

Finally, the agent loads data, runs analytical queries, bulk-imports from CSV, and profiles data quality using the official Dataverse Python SDK.

### Technical Format

Each skill is a Markdown file with YAML frontmatter. Significantly, this design choice has important implications:

```yaml
---
name: dataverse-create-table
description: Creates a new Dataverse table with the specified schema
allowed-tools: [bash, file, web_fetch]
---
```

No compiled code. No proprietary formats. Consequently, every skill can be read, understood, modified, and contributed to by any developer. Additionally, the project is MIT-licensed.

---

## Why This Matters for Enterprise Platforms

Dataverse Skills represents a broader architectural principle that Microsoft is applying across the Power Platform: **platforms must expose their capabilities as agent-consumable knowledge**, not just human-consumable UIs.

Indeed, this is why the release is accompanied by three other major developments:

### 1. The Dataverse MCP Server

The Model Context Protocol (MCP) server built into Dataverse provides standardized, agent-accessible endpoints for reading and writing Dataverse data. As one of its primary tools for the Connect and Build phases, the Skills plugin leverages this server extensively.

Access to the MCP server is available at:
```
https://{your-org}.crm.dynamics.com/api/mcp
```

Specifically, it exposes tools like `list_tables`, `describe_table`, `read_query`, `create_record`, and `update_record` that agents can call directly.

### 2. The Dataverse Python SDK

The `PowerPlatform-Dataverse-Client` Python package (currently v0.1.0b7, in public preview since Microsoft Ignite 2025) provides a high-level, Pythonic interface for Dataverse operations. Importantly, the Skills plugin uses this heavily for the Operate phase.

```python
from PowerPlatform.Dataverse.client import DataverseClient
from azure.identity import AzureCliCredential

client = DataverseClient("https://yourorg.crm.dynamics.com", AzureCliCredential())

# Bulk create with native Dataverse CreateMultiple
client.records.create("new_candidate", [
    {"new_firstname": "Anna", "new_lastname": "Mueller", "new_status": 1},
    {"new_firstname": "Thomas", "new_lastname": "Berger", "new_status": 1},
])
```

### 3. Power Platform 2026 Release Wave 1

The 2026 Release Wave 1 (April–September 2026) explicitly includes enhancements to agent programmability with Dataverse APIs, MCP servers, and the Python SDK. Therefore, Dataverse Skills is the developer-facing entry point into this broader platform direction.

---

## The Broader Ecosystem This Unlocks

At this point, it is worth distinguishing **Dataverse Skills** (the developer plugin) from **Business Skills** (a separate, but related concept in Copilot Studio).

**Business Skills** are reusable, natural-language-described process instructions stored as Dataverse table records. They can be created by makers in Copilot Studio and used by agents to execute business processes — like logging a call transcript or looking up order status.

Nevertheless, the two concepts are complementary:
- **Dataverse Skills** (developer plugin): teaches coding agents how to *build and manage* Dataverse solutions
- **Business Skills** (Copilot Studio): teaches agents how to *execute business processes* stored in Dataverse

Ultimately, as a developer or architect, you will likely work with both.

---

## What This Means for You as a Developer or Architect

### For Developers

- **Onboarding acceleration:** New developers on a project can describe what they want to build and have the agent scaffold the correct Dataverse schema, without needing to memorize PAC CLI command sequences.
- **Prototyping speed:** Furthermore, a full data model with sample data can be stood up in minutes from a single prompt.
- **Reduced documentation dependency:** Additionally, the knowledge is embedded in the agent, not in a wiki you have to maintain.

### Architectural Impact

- **Consistent patterns:** The skills encode best practices (publisher prefixes, solution structure, ALM hygiene) that propagate automatically across projects.
- **Governance by default:** Moreover, because the agent uses the same tools and patterns every time, architectural standards are easier to enforce.
- **Focus shift:** Most importantly, you move from explaining *how* to do things to defining *what* should be done and *why* — which is where architectural value actually lies.

### Team-Wide Benefits

- **Tool standardization:** One plugin investment covers both GitHub Copilot and Claude Code users. Teams that haven't standardized on a single coding agent get consistent Dataverse capabilities regardless.

---

## FAQ

**Q: Is Dataverse Skills the same as the Business Skills feature in Copilot Studio?**

No. These are two distinct features. Dataverse Skills is a developer plugin for coding agents (GitHub Copilot, Claude Code) that teaches them how to build Dataverse solutions. Business Skills is a Copilot Studio feature for storing and executing business process instructions. They are complementary.

**Q: Do I need to pay for anything to use Dataverse Skills?**

The plugin itself is MIT-licensed and free. However, using the Dataverse MCP server from non-Copilot Studio clients (such as GitHub Copilot or Claude Code) does incur Copilot credit charges as of December 15, 2025. That said, If you have Dynamics 365 Premium or Microsoft 365 Copilot User Subscription Licenses, Dynamics 365 data access may not be charged additionally.

**Q: Which Dataverse environments are supported?**

The Dataverse MCP server requires a Managed Environment. Business Skills also require Managed Environments. Standard environments work with PAC CLI and the Python SDK directly.

**Q: Is the Python SDK production-ready?**

As of April 2026, the `PowerPlatform-Dataverse-Client` package is in public preview (v0.1.0b7). Therefore, it is not recommended for production use yet, as breaking changes are possible. Nevertheless, you should monitor the PyPI page and the GitHub repository for GA announcements.

**Q: Can I write my own Dataverse Skills?**

Yes. The project is open source and accepts contributions via pull request. Specifically, each skill is a Markdown file with YAML frontmatter — no programming knowledge beyond Markdown is required to contribute a new skill.

**Q: Does this work with on-premises Dataverse installations?**

The MCP server and Python SDK require cloud-hosted Dataverse environments. On-premises or hybrid scenarios are not currently covered by Dataverse Skills.

---

## References & Further Reading

### Official Announcements
- [Dataverse Skills: Your Coding Agent Now Speaks Dataverse — Power Platform Developer Blog](https://devblogs.microsoft.com/powerplatform/dataverse-skills-your-coding-agent-now-speaks-dataverse/)
- [Dataverse MCP Server — Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2025/07/07/dataverse-mcp/)
- [Introducing the Dataverse SDK for Python — Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2025/12/03/dataverse-sdk-python/)

### GitHub Repositories
- [microsoft/Dataverse-skills](https://github.com/microsoft/Dataverse-skills) — The plugin source
- [microsoft/PowerPlatform-DataverseClient-Python](https://github.com/microsoft/PowerPlatform-DataverseClient-Python) — Python SDK source

### Microsoft Learn Documentation
- [Connect to Dataverse with MCP](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp)
- [Configure the Dataverse MCP server](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp-disable)
- [Dataverse SDK for Python overview](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/sdk-python/overview)
- [Create and use Business Skills](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-business-skills)
- [Power Platform CLI reference](https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction)
- [Power Platform 2026 Release Wave 1](https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/)

### Package Registry
- [PowerPlatform-Dataverse-Client on PyPI](https://pypi.org/project/PowerPlatform-Dataverse-Client/)

---

*Next in this series → [Part 2: Getting Started — Installing Dataverse Skills and Running Your First Agent-Built Solution](#)*