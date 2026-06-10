# Substack Article — Article 71

*Canonical URL: https://aidevme.com/dataverse-mcp-server-the-15-tools-that-make-power-platform-agent-ready/*

---

# Your Dataverse Agent Has Been Flying Blind. That Changed in June 2026.

You have probably experienced this. You ask an AI agent to write a plugin or a query against your Dataverse environment. It produces something that looks completely reasonable — correct syntax, right general shape, confident tone. Then you run it and it breaks immediately, because the column name it used doesn't exist in your schema, or the table has a different logical name than the agent assumed.

The AI wasn't hallucinating randomly. It was filling a gap. It had no way to actually inspect your environment, so it substituted training data for ground truth. In a generic scenario that works fine. In an enterprise Power Platform deployment — where custom publishers, unmanaged layers, and environment-specific configurations create significant schema drift — it fails in ways that are hard to debug and easy to misattribute.

Microsoft addressed this directly on June 8, 2026, with the formalization of the Dataverse MCP server tool shape. Not a new product. A named, typed, governable contract: fifteen specific tools that any MCP-compatible agent can call against your live Dataverse environment.

---

## The Two Tools That Solve the Grounding Problem

The most important tools in the set are the first two: `search` and `describe`.

Before your agent writes a single line of code or generates a single query, it should call `search` with a keyword. It gets back matching table schemas and business skills from your live environment — your actual column names, your specific relationships, your real logical names. Then it calls `describe` to get the full detail on whatever it found. Only then does it start generating.

This changes the output quality in a way that compounds across a session. Every subsequent tool call is grounded in what actually exists rather than what the model learned from generic documentation. For complex enterprise schemas the difference is significant.

Microsoft's official sample agent instructions make this mandatory, not optional:

> *"Whenever you have to use logical table name, call the list_tables tool to get that logical table name. Whenever you have to use column/attribute name, call the describe_table tool to get the column/attribute name."*

If you are building a Dataverse agent today and this sequencing is not in your instructions, that is the first thing to fix.

---

## Three Tiers, One Risk Model

The fifteen tools organize naturally into three risk tiers, and understanding this structure is how you design sensible agent permissions.

**Read-only** (`search`, `describe`, `read_query`, `search_data`, `file_download`): these observe without modifying anything. Grant these broadly. An agent with only these tools can answer questions, inspect schemas, run queries, and download files — but it cannot change your data or your schema.

**Write** (`create_record`, `update_record`, `create_table`, `update_table`, `upsert_skill`, file upload tools): these modify state but in ways that are recoverable. Records can be corrected. Schemas can be rolled back through solution versioning.

**Destructive** (`delete_record`, `delete_table`, `delete_skill`): these are where Microsoft built in an explicit approval gate. By default, `delete_record` and `delete_table` require explicit user confirmation before executing.

Here is the thing worth knowing: the official sample agent instructions override that approval gate. The sample explicitly says to delete without asking for confirmation — it is designed for fully autonomous, sandboxed operation. That is appropriate for a dev environment. It is a governance risk in production. If you are adapting the sample instructions for real use, changing the deletion behavior is the most important modification to make.

---

## The Skills Loop Nobody Is Talking About

`upsert_skill` is the tool most Power Platform practitioners haven't thought about yet, and it might be the most strategically interesting one.

Dataverse Skills are named, stored playbooks — business process instructions that live in Dataverse and surface through the `search` tool alongside table schemas. When an agent calls `search`, it doesn't just get table metadata. It gets the operational playbooks your team has encoded into the environment.

`upsert_skill` lets you add or update one of those playbooks in real time. In a development session: a developer identifies a missing playbook, defines it, upserts it immediately without leaving the terminal, and it becomes available to every other agent connecting to the same environment from that moment forward.

Think about what this means at scale. Operational knowledge that currently lives in Confluence pages and senior developers' heads can be progressively encoded as discoverable skills. The environment gets smarter over time without a deployment pipeline. New team members and new agents benefit from it immediately.

---

## The Security Layer You Need to Design Deliberately

This is the part that most coverage skips, and it is the part that matters most before you put agents near production data.

**Authentication** is Entra ID all the way down — no API keys, no shared secrets. The agent presents an Entra ID token and inherits the Dataverse security roles of whatever identity it runs under. Which means: if a developer runs an agent under their own identity and they have System Administrator, the agent effectively has System Administrator. Principle of least privilege applies to the identity, not just the tool list.

**Dataverse security roles remain the backstop.** The MCP tool contract does not bypass row-level security, field-level security, or Business Unit boundaries. A `create_record` call where the identity lacks Create privilege fails with the same error as through the Web API. Your existing security model still applies — which is reassuring, but also means you need to design agent service principal identities as carefully as you design human user security roles.

**Client allowlisting** gives you a second authorization layer. Even with valid credentials and the right Dataverse roles, a client that isn't on the environment's allowlist can't connect. You can permit GitHub Copilot in development and Copilot Studio in production without allowing Claude or Cursor anywhere near production data — regardless of what the user's identity would otherwise permit.

**The audit gap is real.** Dataverse audits DML operations — creates, updates, deletes. Agent-initiated writes show up in the audit log. But read operations through `search`, `describe`, and `read_query` do not generate record-level audit events. For compliance requirements around data access, not just data modification, that gap needs to be closed in the client orchestration layer.

**Prompt injection through retrieved data** is the risk I haven't seen anyone else call out explicitly. When an agent calls `read_query` or `search_data` and the results include free-text fields — notes, task descriptions, email content — those values flow directly into the agent's context. A malicious actor with write access to Dataverse records can plant instructions in a text field that redirect the agent's behavior. The mitigation: separate your read agents from your write/delete agents, and write explicit instructions telling the agent to treat retrieved record content as data, not instructions.

---

## Before You Connect Your First Client

The setup is not complicated, but there are two things that catch teams off-guard.

First: every client except Copilot Studio requires explicit activation in the Power Platform admin center, under Settings → Product → Features → Advanced Settings. This is not on by default.

Second: **the environment must be a Managed Environment**. If it is not, you cannot enable non-Microsoft MCP clients at all. There is no workaround. Upgrade the environment to Managed before you test.

The MCP endpoint format is consistent across environments:

```
https://{orgName}.crm.dynamics.com/api/mcp
```

Once the client is allowlisted and the environment is Managed, connection takes minutes. Writing agent instructions that produce reliable behavior across all fifteen tools is where the real work is — and why the official sample instructions are worth reading as a structural model, even if you modify the delete behavior before you use them.

---

## What It Actually Changes

The practical impact is in three areas.

You can now specify agent permissions with the same precision you apply to human user permissions. Named tools, scoped service principal roles, client allowlisting — the vocabulary for deliberate agent permission design exists now in a way it didn't a year ago.

Development loops get shorter when agents can self-orient. An agent that calls `list_tables`, resolves your actual logical names, and validates column existence before generating code is a qualitatively different collaborator than one that guesses from training data.

Governance is enforceable at the platform level, not just expressed in prompts. This matters because prompt instructions can be overridden, forgotten, or injected against. Platform-level enforcement — Managed Environment prerequisites, client allowlists, RBAC, approval gates — cannot be. You can build agentic Dataverse workflows with the same accountability model you would apply to any other privileged system access.

---

The full analysis — including the complete reference table of all 15 tools, the full sample agent instructions with line-by-line commentary, billing details, and the GDPR implications of schema-vs-data tool separation — is on AIDevMe:

**[Dataverse MCP Server: The 15 Tools That Make Power Platform Agent-Ready →](https://aidevme.com/dataverse-mcp-server-the-15-tools-that-make-power-platform-agent-ready/)**

If this was useful, share it with someone building agentic Power Platform solutions. There is a lot of coverage of what MCP is in general and very little on what these specific tools mean for enterprise architects — which is the gap this article is trying to close.
