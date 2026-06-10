# Medium Article — Article 71

*This is a Medium republication. The original article was published at:*
*https://aidevme.com/dataverse-mcp-server-the-15-tools-that-make-power-platform-agent-ready/*

---

# The Dataverse MCP Server Now Has 15 Named Tools. Here's What That Actually Means for Enterprise Developers.

Microsoft formalized the Dataverse MCP server tool shape on June 8, 2026. Most coverage summarized the announcement. This piece analyzes what the fifteen tools mean in practice — organized by risk, not by feature list.

---

## The Problem They're Solving

AI coding agents working with Dataverse have a structural problem: they cannot see your schema. They generate FetchXML, column references, and plugin code based on training data — which means they produce code that looks right but fails the moment it touches your actual environment, where column names differ, logical names don't match the display names, and custom publishers have shaped everything.

This is the grounding problem. The Dataverse MCP server's fifteen tools are the structural answer: a typed, named, governable interface that lets any MCP-compatible agent inspect your live environment before it generates anything.

---

## The Two Tools That Matter Most

Before anything else, understand `search` and `describe`.

`search` takes a keyword and returns matching table schemas and Dataverse Skills from your live environment. `describe` takes a result and returns full detail — column names, types, relationships, views, app references. Together they form a schema discovery loop that an agent can execute at the start of every session.

Microsoft's official sample agent instructions make this sequencing mandatory rather than optional:

> *"Whenever you have to use logical table name, call the list_tables tool to get that logical table name. Whenever you have to use column/attribute name, call the describe_table tool to get the column/attribute name."*

This is the grounding mechanism. If you are building a Dataverse agent and this is not in your instructions, it is the first gap to close.

The deliberate separation of `search` (schema-level) from `search_data` and `read_query` (data-level) also has governance implications worth understanding — more on that below.

---

## Three Tiers, One Risk Model

The fifteen tools organize into three risk tiers, and this taxonomy is how you design sensible agent permissions:

**Read-only** — `search`, `describe`, `read_query`, `search_data`, `file_download`
No writes. An agent with only these tools can answer questions, inspect schemas, run queries, and retrieve files. Grant broadly.

**Write** — `create_record`, `update_record`, `create_table`, `update_table`, `upsert_skill`, `init_file_upload`, `commit_file_upload`
Modifies state, but recoverable. Records can be corrected. Schemas roll back through solution versioning. Needs deliberate access control.

**Destructive** — `delete_record`, `delete_table`, `delete_skill`
Microsoft built an explicit approval gate here. `delete_record` and `delete_table` require user confirmation by default.

There is a wrinkle: the official sample agent instructions override that approval gate. The sample explicitly includes `do not ask confirmation for delete table or delete record operation, you can delete` — designed for fully autonomous, unattended operation. That is appropriate in a sandboxed dev environment. In production, it is a governance risk. The single most important modification before using the sample instructions in any real environment is to remove that override.

---

## File Handling: The Underrated Tier

The `init_file_upload`, `commit_file_upload`, and `file_download` tools get the least attention, but they enable something genuinely useful.

The architecture is worth understanding: the MCP server never carries file bytes. It issues a SAS URL (`init_file_upload`), the file transfers directly between the client and Azure Blob storage, then the upload is registered in Dataverse (`commit_file_upload`). The server orchestrates; the data path bypasses it entirely.

This matters for compliance (data residency is honored — bytes never leave your Azure region through an intermediary) and for performance (large files don't bottleneck through the protocol layer).

What it enables: agent-driven document workflows that previously required custom connectors. Contract renewal agents that read and write attachments. Field service agents that retrieve inspection photos, analyze them, and write structured findings back as records. These are now a few named tool calls rather than bespoke integration work.

---

## Skills: The Mechanism Nobody's Talking About

`upsert_skill` is the most strategically interesting tool in the set, and the least discussed.

Dataverse Skills are named, stored playbooks — business process instructions that live in Dataverse and surface through the `search` tool alongside table schemas. When an agent calls `search`, it discovers not just your data model but your team's encoded operational processes.

`upsert_skill` lets a developer add or update a skill in real time, without leaving the IDE. Once upserted, it is immediately discoverable by any agent connecting to the same environment.

The long-term implication: operational knowledge that currently lives in documentation and senior developers' heads can be progressively encoded as discoverable agent playbooks. New team members and new agents find them through `search`. The environment accumulates intelligence without a deployment pipeline.

---

## The Security Layer You Need to Get Right

This is the section most coverage skips. Before connecting any agent to production Dataverse data, these four layers need deliberate design.

**Entra ID authentication, end to end.** There is no alternative auth path — no API keys, no shared secrets. Every tool call presents an Entra ID token. The agent inherits the Dataverse security roles of the identity it runs under. If a developer runs an agent under their own identity and has System Administrator, the agent effectively has System Administrator. Least privilege applies to the identity, not just the tool list.

**Dataverse RBAC still applies.** The MCP tool contract does not bypass row-level security, field-level security, or Business Unit boundaries. A `create_record` call where the identity lacks Create privilege fails exactly as it would through the Web API. Your existing security model is the backstop — design agent service principal identities with the same rigor you apply to human user roles.

**Client allowlisting is a real authorization layer.** Even with valid credentials and appropriate Dataverse roles, a client not on the environment's allowlist cannot connect. You can permit GitHub Copilot in dev and Copilot Studio in production without allowing Claude or Cursor near production data — regardless of the user's identity.

**The audit gap is real.** Dataverse audits DML operations — creates, updates, deletes. Agent-initiated writes appear in the audit log. But read operations through `search`, `describe`, and `read_query` do not generate record-level audit events. For compliance requirements around data access, this needs to be closed in the orchestration layer, not assumed to be covered.

**Prompt injection through retrieved data.** When an agent calls `read_query` and the results include free-text fields — notes, task descriptions, email content — those values flow into the agent's context window. A text field can contain instructions that redirect the agent's behavior. The mitigation is architecture: separate read agents from write/delete agents so that even a successful injection only affects a read-only persona, and instruct agents explicitly to treat retrieved record content as data rather than instructions.

---

## The Managed Environment Prerequisite

One practical detail catches teams off-guard: non-Microsoft MCP clients can only be enabled on Managed Environments. If your target environment is not managed, you cannot allowlist GitHub Copilot, Claude, or Cursor. There is no workaround — convert the environment to Managed first.

Once you are on a Managed Environment, activation is in the Power Platform admin center under Settings → Product → Features → Advanced Settings, with a record per client to set `Is Enabled` to `Yes`.

The endpoint follows this format across all environments:

```
https://{orgName}.crm.dynamics.com/api/mcp
```

---

## Writing Instructions That Actually Work

Connecting a client takes minutes. Writing agent instructions that produce reliable behavior across fifteen tools is where most teams underinvest.

Microsoft published sample instructions alongside the configuration documentation. They are worth reading as a structural model: the four-section format (Role, Objective, MCP tool selection, Reasoning) covers the key behavioral directives, including the mandatory `list_tables`/`describe_table` sequencing and a ReAct-style reasoning loop that keeps complex multi-step operations on track.

The two modifications to make before any production use:

1. Remove the deletion approval override — restore the default confirmation gate for `delete_record` and `delete_table`
2. Add environment-specific constraints — publisher prefix, solution context, security role names, out-of-scope environments

The sample is intentionally environment-agnostic. Your instructions should not be.

---

## What Changes for Enterprise Architects

Three shifts are now within reach that weren't a year ago.

**Agent permissions can be designed deliberately.** The named tool surface gives you the vocabulary for specifying exactly what a given agent persona can and cannot do. Custom security roles per agent identity. Scoped tool access per use case. Separate service principals per persona.

**Development loops shorten with live schema access.** An agent that calls `list_tables`, resolves your actual logical names, and validates column existence before generating code is a qualitatively different collaborator than one working from training data assumptions.

**Governance becomes platform-enforceable, not just prompt-expressed.** Prompt instructions are influence. Managed Environment prerequisites, client allowlists, RBAC enforcement, and approval gates are enforcement. You can now build agentic Dataverse workflows with the same accountability model you apply to any other privileged system access.

---

## The Full Reference Table and More

The complete tool reference table, the full sample agent instructions with line-by-line commentary, billing details (including the Copilot Credits model and D365 Premium license exemptions), and the GDPR implications of the schema/data tool separation are all in the original article:

**[Dataverse MCP Server: The 15 Tools That Make Power Platform Agent-Ready](https://aidevme.com/dataverse-mcp-server-the-15-tools-that-make-power-platform-agent-ready/)**

*Published on AIDevMe — Power Platform architecture, agentic AI patterns, and developer tooling for enterprise teams.*
