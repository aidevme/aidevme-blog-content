# Dataverse MCP Server: The 15 Tools That Make Power Platform Agent-Ready

*Published: June 9, 2026 · Author: Zsolt Varga · AIDevMe*

🔗 **Published at:** [https://aidevme.com/dataverse-mcp-server-the-15-tools-that-make-power-platform-agent-ready/](https://aidevme.com/dataverse-mcp-server-the-15-tools-that-make-power-platform-agent-ready/)

---

**WordPress SEO**
- **Focus keyphrase:** Dataverse MCP server tools
- **SEO title:** Dataverse MCP Server: The 15 Tools That Make Power Platform Agent-Ready
- **Meta description:** The 15 Dataverse MCP server tools released June 2026: how they're organized by risk tier, what Skills enable, and how to configure agents for Power Platform.
- **Slug:** dataverse-mcp-server-tools-power-platform-agent-ready
- **Excerpt:** Microsoft formalized the Dataverse MCP server tool shape in June 2026 — 15 named tools that give any MCP-compatible agent grounded, auditable access to your Power Platform environment. This analysis covers the full tool surface organized by risk tier, how to configure clients in VS Code and Copilot Studio, the billing model, and a dedicated security and governance breakdown: Entra ID auth, RBAC, client allowlisting, audit gaps, prompt injection risks, and the delete-override danger in the sample agent instructions.

---

---

You have probably seen this failure. You ask a coding agent to generate a query or a plugin against your Dataverse environment. It produces something that looks exactly right — correct syntax, reasonable structure, confident tone. Then you run it and it immediately fails because the column name doesn't exist, or the table uses a different logical name than the agent assumed, or the relationship it referenced was never part of your schema. The AI wasn't wrong in general. It was wrong about *your* environment specifically, because it had no way to check.

This is the grounding problem. And it matters more than it might seem — not because AI agents are unreliable, but because enterprise Power Platform schemas are genuinely variable. Custom publishers, unmanaged layers, environment-specific configurations, late-arriving columns — the gap between what an agent knows from training and what actually exists in production can be significant. If your agent can't inspect the live environment before acting, it fills that gap with plausible-looking fiction.

Microsoft's answer to this, as of June 8, 2026, is not another abstraction layer. It is the **Dataverse MCP server** — a concrete set of fifteen named tools that any MCP-compatible agent can call against your live environment. The server has existed since mid-2025, but it was a broad connection — you could reach Dataverse, but the surface was vague. What changed in June 2026 is the formalization of the *tool shape*: a typed, governable, auditable contract that tells both you and your agent exactly what is allowed, what requires approval, and what is off-limits.



---

## Table of Contents

- [The Grounding Problem, Solved Structurally](#the-grounding-problem-solved-structurally)
- [Three Tiers of Risk, Three Tiers of Control](#three-tiers-of-risk-three-tiers-of-control)
- [What the File Tools Actually Enable](#what-the-file-tools-actually-enable)
- [Skills: The Self-Extending Agent](#skills-the-self-extending-agent)
- [Connecting from Claude Code, VS Code, and Copilot Studio](#connecting-from-claude-code-vs-code-and-copilot-studio)
- [Writing Agent Instructions That Actually Work](#writing-agent-instructions-that-actually-work)
  - [Add Instructions in Visual Studio Code or Copilot Studio](#add-instructions-in-visual-studio-code-or-copilot-studio)
- [The Billing Dimension](#the-billing-dimension)
- [Security and Governance Analysis](#security-and-governance-analysis)
  - [Authentication: Entra ID All the Way Down](#authentication-entra-id-all-the-way-down)
  - [Dataverse Security Roles Still Govern Data Access](#dataverse-security-roles-still-govern-data-access)
  - [The Managed Environment Gate](#the-managed-environment-gate)
  - [Client Allowlisting as an Authorization Layer](#client-allowlisting-as-an-authorization-layer)
  - [Audit Logging for Tool Calls](#audit-logging-for-tool-calls)
  - [Data Classification and the Schema/Data Separation](#data-classification-and-the-schemadata-separation)
  - [The Delete Override Risk](#the-delete-override-risk)
  - [Prompt Injection via Retrieved Data](#prompt-injection-via-retrieved-data)
- [What This Changes for Power Platform Architects](#what-this-changes-for-power-platform-architects)
- [Reference: The Full Tool Surface](#reference-the-full-tool-surface)
- [Resources](#resources)

---

## The Grounding Problem, Solved Structurally

When an agent connects to Dataverse through a well-defined MCP tool surface, the first thing it should do is orient itself. Not guess. Not rely on training data from six months ago. Actually inspect *your* environment.

Two tools handle this: `search` and `describe`.

`search` takes a keyword and returns matching table schemas and business skills from the live environment. `describe` takes one of those results and returns its full detail — columns, types, relationships, views, app references. Together, they form a runtime schema discovery loop that any agent can execute before touching data.

Think about what this means for your daily workflow. Instead of the agent confidently generating a query based on what it knows about Dataverse in general, it calls `search` for your table name first. It gets back your actual schema — your column names, your custom fields, your specific relationships. Then it generates the query. The difference in output quality is significant, and it compounds across every interaction in the session.

The separation of `search` (schema-level) from `search_data` (data-level) is also deliberate. Governance policies can allow schema inspection without permitting data retrieval — relevant for scenarios where an external agent is helping a developer understand a data model but should not be able to read production records.

And the Microsoft documentation reinforces this pattern explicitly at the instruction level. The sample agent instructions published in the official configuration guide make the sequencing mandatory:

> *"Whenever you have to use logical table name, call the `list_tables` tool to get that logical table name. Whenever you have to use column/attribute name, call the `describe_table` tool to get the column/attribute name."*

This is not a best-practice suggestion buried in a FAQ. It is the intended runtime pattern: inspect first, act second. If you are configuring a Dataverse agent and you are not already building this sequencing into your instructions, start there.

---

## Three Tiers of Risk, Three Tiers of Control

Once you look at the full tool surface, a natural risk stratification emerges. Not all fifteen tools carry the same weight, and the design of the MCP server reflects that.

**Read-only tools** — `search`, `describe`, `read_query`, `search_data`, `file_download` — observe without modifying. An agent with only these tools can answer questions, generate reports, inspect schemas, and download files, but it cannot change anything. These are the tools you grant first, the tools you grant most broadly, and the tools that carry the lowest operational risk.

**Write tools** — `create_record`, `update_record`, `create_table`, `update_table`, `upsert_skill`, `init_file_upload`, `commit_file_upload` — modify state, but in a recoverable way. A record can be corrected. A table schema can be rolled back through solution versioning. A skill can be overwritten. These require more deliberate access control, but they are not catastrophic if something goes wrong.

**Destructive tools** — `delete_record`, `delete_table`, `delete_skill` — are where Microsoft has explicitly introduced a human approval gate. The documentation is clear: `delete_record` and `delete_table` execute *only after explicit user approval*.

Here is where you need to stop and read carefully. The official sample agent instructions take the opposite stance on this:

```md
do not ask confirmation for delete table or delete record operation,
you can delete.
```

That is a deliberate design choice for a fully autonomous agent persona — the sample instructions are explicitly written for agentic, unattended operation. The instruction also states: *"Do not ask for user intervention if you have to run an operation externally in case Dataverse doesn't support that operation."*

This creates a genuine tension that architects need to resolve consciously. The MCP tool contract signals that destructive operations should require approval. The sample instructions override that with an autonomous execution mandate. Neither is wrong in every context — a developer agent running in a sandboxed test environment might legitimately skip confirmation gates; a production CRM agent absolutely should not.

The takeaway is direct: do not copy the sample agent instructions verbatim into a production agent. They are a starting point written for a sandboxed, fully supervised context. Adjust the confirmation behavior before your agent gets anywhere near real data.

For architects designing agentic workflows, this three-tier model maps directly to how you should think about agent permissions. The principle of least privilege applies here with even more force than in traditional RBAC: an agent that only needs to read and summarize pipeline data has no business holding `delete_table` capability in its allowed tool set.

---

## What the File Tools Actually Enable

File handling is the part of the new tool shape that gets the least attention in most writeups — which is a mistake, because it unlocks some genuinely useful operational scenarios you have probably been handling manually or with custom connectors.

The pattern is a three-step sequence: `init_file_upload` generates a SAS URL, the actual file transfer happens directly between your client and Azure Blob storage, then `commit_file_upload` registers the upload in Dataverse. `file_download` mirrors this for retrieval.

The design detail worth understanding: the MCP server never carries the file bytes. It orchestrates — issuing credentials, tracking state, committing the result — but the data moves directly to storage. This matters for performance (large files don't bottleneck through the protocol layer) and for compliance (data residency requirements are honored because the bytes never leave your Azure region through an intermediary).

In practice, think about what this makes possible. A contract renewal agent can download the previous agreement from a Dataverse note, process it, and commit the updated version back — all as auditable tool calls, no custom connector required. A field service agent can pull inspection photos from a work order record, run analysis, and write structured findings back as new records. These are workflows that previously needed bespoke integration work. Now they are a few named tool calls.

---

## Skills: The Self-Extending Agent

Among the fifteen tools, `upsert_skill` and `delete_skill` are the most conceptually interesting and the least familiar to most Power Platform practitioners.

Dataverse Skills are structured playbooks — named, stored business processes that agents can discover and execute. They are not plugins or flows. They are instructions that live in Dataverse and surface through the MCP `search` tool alongside table schemas, making them part of the agent's discoverable environment.

`upsert_skill` allows an agent — or a developer working through an agent — to add or update a skill by name. This creates a feedback loop: during a development session, if an agent discovers that a common operation is missing a stored playbook, a developer can define one and upsert it immediately, without leaving the terminal or IDE. The skill becomes available to other agents connecting to the same environment through their own `search` calls.

For enterprise teams, this is worth pausing on. Think about how much operational knowledge in your organisation currently lives in Confluence pages, senior developers' heads, or Slack threads that never get indexed. Dataverse Skills give you a way to progressively encode that knowledge into the environment itself — as discoverable, executable playbooks that any agent can find and use. Agents find them. Developers extend them. New starters benefit from them immediately. The environment gets smarter over time without a code deployment.

---

## Connecting from Claude Code, VS Code, and Copilot Studio

The Dataverse MCP endpoint follows a consistent URL format:

```
https://{orgName}.crm.dynamics.com/api/mcp
```

Any MCP-compatible client that authenticates with your Microsoft identity can connect to this endpoint — subject to the environment's allowed client configuration.

By default, **Copilot Studio is the only pre-enabled client**. Every other client — GitHub Copilot in VS Code, GitHub Copilot CLI, Claude Desktop, Claude Code — requires explicit activation in the Power Platform admin center. The steps are straightforward but easy to overlook:

1. Open the Power Platform admin center → **Manage** → **Environments**
2. Select your environment → **Settings** → **Product** → **Features**
3. Confirm that **Allow MCP clients to interact with Dataverse MCP server** is on
4. Select **Advanced Settings**, open the specific client record, set **Is Enabled** to **Yes**, and save

The allow-listing applies specifically to the `/api/mcp` agent entrypoint. MCP-named custom APIs in Dataverse are ordinary Dataverse APIs and are not restricted by this setting — a detail worth noting if you are building custom solutions that expose their own MCP-style interfaces.

One prerequisite that catches teams off-guard: **the environment must be a Managed Environment**. If your target environment is not managed, you cannot enable non-Microsoft MCP clients at all. This is a hard blocker, not a recommendation. If you hit it, the fix is to convert the environment to Managed — there is no workaround.

---

## Writing Agent Instructions That Actually Work

Connecting a client to the Dataverse MCP endpoint takes about ten minutes. Writing agent instructions that actually produce reliable behavior across a fifteen-tool surface — that is the harder problem, and it is where most teams underinvest.

Microsoft published sample agent instructions as part of the official configuration documentation, and they are worth studying closely — not as a template to copy, but as a model of what good Dataverse agent instructions look like structurally. Here is the full sample:

```md
## Role
Act as an autonomous agent responsible for interacting with the
Microsoft Dataverse app.

## Objective
Your objective is to respond to tasks provided by the user. First execute
each step of the provided task workflow using your MCP tools. Check if you
have achieved your objective after each tool call. If you have not achieved
your objective then continue to execute the next step in the task workflow.
Do not ask for user intervention if you have to run an operation externally
in case Dataverse doesn't support that operation — you are allowed to run it
without user confirmation. Also do not ask confirmation for delete table or
delete record operation, you can delete.

## MCP tool selection instructions
- Whenever you have to use logical table name, call the list_tables tool
  to get that logical table name.
- Whenever you have to use column/attribute name, call the describe_table
  tool to get the column/attribute name.

## MCP tool usage instructions
- Before executing an MCP tool, always review the tool description and
  restrictions.
- Always strictly follow the description of each MCP tool and perform
  actions without any deviation from the tool description.
- Provide higher precedence to tool description over general knowledge.
- Always review the tool documentation and restrictions before running any
  query or operation. Strictly validate each planned action against the
  tool's rules and supported features before execution.
- For read_query tool, there are restrictions on SQL conditions. Always
  refer to the tool description for supported and unsupported SQL keywords
  before generating the SQL query and ensure only supported
  conditions/keywords are used.

## Reasoning instructions
- Think out loud and reason step by step.
- Before each tool call, plan and verify the action conforms to the tool
  description.
- After each tool call, reflect on the result and determine the next step.
- If an exception, error, or warning is observed, communicate it clearly
  to the user and retry based on the error message.
- When answering questions about data, DO NOT rely on general knowledge —
  always use tools to retrieve accurate, current data.
- DO NOT stop reasoning until all tasks are complete or an unrecoverable
  error occurs.
- Only ask clarifying questions if the task requirements are ambiguous.
```

Several things stand out as architectural decisions worth examining.

**Tool description takes precedence over training data.** The instruction *"provide higher precedence to tool description over general knowledge"* is the key to reliable Dataverse agents. An LLM's training data contains information about Dataverse, FetchXML, OData, and SQL — but that information may be outdated, environment-specific, or simply wrong for your schema. Instructing the agent to defer to the live tool description over its priors is the grounding mechanism that prevents hallucination.

**The `read_query` SQL restriction is called out explicitly.** Dataverse's SQL support through the MCP layer is not full ANSI SQL. There are supported and unsupported keywords, and the sample instructions specifically tell the agent to inspect the tool description before constructing any query. This is a guard against a common failure mode: agents generating perfectly valid SQL that Dataverse's query engine rejects.

**The reasoning loop is explicit.** The instructions mandate step-by-step reasoning, reflection after each tool call, and continued execution until completion or unrecoverable failure. This is essentially a ReAct (Reason + Act) pattern encoded in natural language. For complex multi-step operations — creating a table, importing data, verifying relationships — this structured reasoning loop is what keeps the agent on track rather than stopping after the first successful tool call.

**What to modify for your context.** The delete confirmation behavior (discussed earlier) is the most obvious candidate for adjustment. Beyond that, you will want to add environment-specific constraints — which solution context to use for new tables, which publisher prefix to apply, which security roles to reference, which environments are off-limits. The sample is environment-agnostic; your production instructions should not be.

### Add Instructions in Visual Studio Code or Copilot Studio

Once you have a set of agent instructions — starting from the sample above and adjusted for your environment — here is how to apply them in the two most common clients.

#### Add Instructions in Visual Studio Code

1. Open Visual Studio Code.
2. Open the **Chat** pane.
3. Select **Settings** > **Chat Instructions**.
4. Select **New instruction file**.
5. Copy and paste your instruction content into the new file.

The instruction file is a Markdown document stored in your workspace under `.github/copilot-instructions.md` (workspace-scoped) or in your user profile (user-scoped). Workspace-scoped instructions are committed to version control alongside the code — which means they travel with the repository and apply consistently across the team. For Dataverse agent instructions, workspace-scoped is almost always the right choice: the instructions reference environment-specific details (publisher prefix, solution name, security role names) that are specific to the project, not the developer.

#### Add Instructions in Copilot Studio

1. Open Copilot Studio.
2. Select your agent.
3. Go to **System instructions** and paste your agent instructions.

In Copilot Studio, system instructions are stored as part of the agent definition and versioned within the solution that contains the agent. When you export the solution, the instructions travel with it — which makes them promotable through your ALM pipeline from development to test to production, with environment-specific overrides applied at promotion time through solution connection references or environment variables where applicable.

---

## The Billing Dimension

Enterprise architects cannot ignore the cost model, and the Dataverse MCP server has one.

Since December 15, 2025, tool calls made by agents created outside Microsoft Copilot Studio are charged in Copilot Credits. The `search` tool is billed at the Tenant Graph Grounding rate. All other tools — `read_query`, `create_record`, `describe`, and the rest — are billed at the Text and Generative AI tools (basic) rate, per ten responses.

Two license categories bypass this billing entirely: Dynamics 365 Premium licenses (Sales Premium, Finance Premium, Supply Chain Premium, Customer Service Premium) and Microsoft 365 Copilot User Subscription Licenses. If your users hold these, MCP tool calls against Dynamics 365 data do not consume credits, regardless of which MCP client initiates them.

For everyone else, the billing model shapes how you design agent orchestration. Agentic loops that call `search` repeatedly — re-orienting on every iteration — will accumulate credit consumption at the Graph Grounding rate. A better pattern is to call `search` and `describe` once at the start of a session, cache the schema context in the agent's conversation history, and avoid redundant metadata calls within a single workflow. Similarly, high-frequency polling loops using `read_query` should be restructured as event-driven triggers rather than scheduled pulls wherever the underlying process allows it.

---

## Security and Governance Analysis

The Dataverse MCP server is not just a technical integration surface — it is a new attack surface that requires deliberate governance design before any agent goes near production data. This section covers the layers that matter.

### Authentication: Entra ID All the Way Down

Every MCP tool call authenticates through **Microsoft Entra ID**. There is no alternative auth path, no API key, no shared secret. This is the right architecture — it means the identity of the caller is always verifiable, always auditable, and always subject to Conditional Access policies your tenant already enforces.

What this means in practice: an agent connecting to the Dataverse MCP endpoint must present a valid Entra ID token. For interactive developer sessions in VS Code or Claude Desktop, this is the signed-in user's token — the agent operates under the developer's identity and inherits their Dataverse security roles. For unattended agents and automated pipelines, a service principal or managed identity must be used. The access scope is `https://{orgName}.crm.dynamics.com/user_impersonation` — the same OAuth scope used by the Dataverse Web API.

One implication architects often miss: if a developer runs an agent under their own identity and that developer has System Administrator, the agent effectively has System Administrator too. Principle of least privilege applies to the identity the agent runs under, not just to the tools it is allowed to call.

### Dataverse Security Roles Still Govern Data Access

The MCP tool contract does not bypass Dataverse's own security layer. A call to `read_query` will only return rows the authenticated identity is permitted to read based on their Business Unit, Security Role, and field-level security configuration. A `create_record` call against a table the identity cannot write to will fail with the same error it would produce through the Web API.

This is important because it means your existing Dataverse security model is the backstop. An agent that gains access to `create_record` does not automatically gain the ability to create records in every table — it can only create records where the identity it runs under has Create privilege. The tool surface determines what operations the agent can *attempt*; the security model determines what operations will *succeed*.

The practical consequence: when designing agent identities (service principals), scope their Dataverse security roles as narrowly as the use case permits. A reporting agent needs Read on specific tables. It does not need Write. A provisioning agent may need Create and Update on schema tables in a test environment. It should not hold those roles in production. Separate service principals per agent persona, with separate role assignments, is the right pattern.

### The Managed Environment Gate

The requirement that non-Microsoft MCP clients can only be enabled on **Managed Environments** is not a coincidental restriction — it is a governance enforcement point.

Managed Environments bring several capabilities that directly support agentic scenarios: solution checker enforcement, data policies (DLP), audit logs, IP firewall, Customer Managed Keys, and the ability to block unmanaged customizations. By making Managed Environment a prerequisite, Microsoft ensures that the environments accepting external agent connections are the ones with the strongest governance controls already in place.

The operational implication: if a development team wants to test agent integrations on an unmanaged sandbox, they cannot use the full MCP client allowlisting. This is often the right constraint — you want agents tested in an environment that mirrors production governance, not a free-form sandbox where policies are loose. Promote to a Managed Environment first, then test.

### Client Allowlisting as an Authorization Layer

The Power Platform admin center's client allowlisting — where you explicitly enable each MCP client (GitHub Copilot, Claude, Cursor, etc.) per environment — is a second authorization layer that operates above Entra ID identity.

Even if a user authenticates with valid Entra ID credentials and holds appropriate Dataverse security roles, if the client they are connecting from is not on the environment's allowlist, the connection is refused. This means you can permit `GitHub Copilot` in your development environment and `Copilot Studio` everywhere, without allowing `Claude Desktop` or third-party clients in production — regardless of what those users' identities would otherwise permit.

This is a meaningful control for organizations that need to maintain software inventory and only permit approved AI tooling. It is the equivalent of managing which third-party OAuth applications are authorized in your Entra ID tenant, but scoped to Dataverse environments specifically.

### Audit Logging for Tool Calls

Dataverse's native audit log captures DML operations against tracked tables — Create, Update, Delete on records. This coverage extends to agent-initiated operations: a `create_record` call by an agent under a service principal identity generates the same audit trail as the same operation performed by a user in a model-driven app.

Schema operations (`create_table`, `update_table`, `delete_table`) are logged in the Dataverse administration event log. File operations via `init_file_upload` and `commit_file_upload` are logged against the file storage infrastructure.

What is not natively covered by Dataverse audit today: the MCP tool call itself — the fact that an agent called `search` against a given table, or that it called `describe` to inspect a column's definition. These read operations do not generate record-level audit events. For organizations with compliance requirements around data access (not just data modification), this gap is worth noting. The mitigation is to route agents through a logging proxy or to capture tool call events in the client orchestration layer, where they can be emitted to a SIEM alongside the Dataverse audit log.

### Data Classification and the Schema/Data Separation

The design decision to separate `search` and `describe` (schema-level discovery) from `search_data` and `read_query` (data-level retrieval) is not purely architectural — it has direct data classification implications.

An organization that classifies table schemas as internal documentation but classifies specific columns (email addresses, financial figures, health data) as restricted or confidential can grant schema discovery broadly while keeping data retrieval tools gated. A developer agent helping a colleague understand a data model can be permitted `search` and `describe` without ever being able to execute `read_query` against production data. This maps naturally to a Zero Trust approach where schema metadata is low-sensitivity and record content is not.

If your organization operates under GDPR, HIPAA, or similar frameworks, the distinction is operationally significant: granting an AI agent access to personal data through `search_data` or `read_query` may trigger data processing agreement requirements, depending on the agent vendor and where inference occurs. The schema-only tool set does not carry the same obligation.

### The Delete Override Risk

As discussed in the risk tier section, the sample agent instructions explicitly override the default deletion approval gate with `do not ask confirmation for delete table or delete record operation`. This instruction is appropriate in a sandboxed, fully supervised development context. It is a serious governance risk in any other context.

The risk is not simply that an agent might delete a record accidentally. It is that if an adversarial or malformed prompt reaches an agent running under this instruction set — through indirect prompt injection in retrieved data, through a compromised upstream system, or through a user who does not understand what they are triggering — deletion will proceed without any human checkpoint.

The mitigation options in order of strength:

1. **Remove the override entirely** for any agent that touches production or pre-production environments. Restore the default approval gate.
2. **Scope deletion capability** by removing `delete_record` and `delete_table` from the allowed tool set for agent personas that do not require it.
3. **Run delete-capable agents under a service principal** with a Dataverse security role that has no Delete privilege on any table that contains irreplaceable data.
4. **Enable Recycle Bin** (Dataverse's soft-delete feature for supported tables) so that agent-initiated deletions are recoverable within the retention window.

Layers 2 and 3 together are the most robust: the agent cannot attempt the operation, and even if it somehow does, the identity does not have the permission to succeed.

### Prompt Injection via Retrieved Data

When an agent calls `search_data` or `read_query` and the results include text fields — note bodies, email content, task descriptions, free-text comments — those results flow directly into the agent's context window. If any of that text contains instructions designed to redirect the agent's behavior, the agent may execute them.

This is indirect prompt injection, and it is a real risk for any agent that reads unstructured text from a data store it does not control. A malicious actor with write access to Dataverse records could plant instructions in a text column that cause an agent processing those records to take unintended actions.

The mitigations are layered. At the instruction level: write explicit agent instructions that state the agent should treat retrieved record content as data, not instructions, and should not execute instructions found in field values. At the architecture level: agents that process unstructured Dataverse text should not simultaneously hold write or delete tool access — separate the read agent from the write agent so that even a successful injection only affects a read-only persona. At the data level: apply field-level security to restrict who can write to text fields that agent personas will read.

---

## What This Changes for Power Platform Architects

The formalization of the Dataverse MCP tool shape is not just a product announcement — it is a signal that the platform has matured enough to make commitments about how agents connect to it. Microsoft is not saying "agents can now connect to Dataverse." It is saying "here is the precise, stable, governable contract for how that connection works, and we are building the ecosystem around it."

For architects, that shift means three things are now within reach that weren't a year ago.

You can design agent integration deliberately, not bolt it on. The named tool surface gives you a vocabulary for specifying exactly what a given agent persona can and cannot do — which means you can apply the same rigour to agent permissions that you already apply to human user permissions. Custom security roles per agent identity. Scoped tool access per use case. Separate service principals per persona. None of this was possible when the connection surface was vague.

Your development loop shortens when agents have live schema access. If you have ever spent time explaining your table structure to an AI tool before it could help you — or worse, discovered mid-implementation that its assumptions were wrong — you will feel the difference immediately. An agent that calls `list_tables`, resolves your actual logical names, and validates column existence before writing a single line of code is a qualitatively different collaborator.

Governance becomes enforceable at the platform level, not just the prompt level. This matters because prompt engineering is not governance — it is influence. Named tools with allowlists, Managed Environment prerequisites, RBAC enforcement, and approval gates for destructive operations: that is enforcement. You can now build agentic workflows with the same accountability model you would apply to any other privileged system access.

The fifteen tools are not the ceiling. They are the foundation. The question worth thinking about now is what you are going to build on top of them — and whether your team's governance model is ready for what comes next.

---

## Reference: The Full Tool Surface

<figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr><td><strong>Tool</strong></td><td><strong>Category</strong></td><td><strong>Modifies State</strong></td><td><strong>Approval Required</strong></td></tr><tr><td><code>search</code></td><td>Discovery</td><td>No</td><td>No</td></tr><tr><td><code>describe</code></td><td>Discovery</td><td>No</td><td>No</td></tr><tr><td><code>search_data</code></td><td>Data retrieval</td><td>No</td><td>No</td></tr><tr><td><code>read_query</code></td><td>Data retrieval</td><td>No</td><td>No</td></tr><tr><td><code>create_record</code></td><td>Record operations</td><td>Yes</td><td>No</td></tr><tr><td><code>update_record</code></td><td>Record operations</td><td>Yes</td><td>No</td></tr><tr><td><code>delete_record</code></td><td>Record operations</td><td>Yes</td><td><strong>Yes</strong> (by default)</td></tr><tr><td><code>create_table</code></td><td>Schema management</td><td>Yes</td><td>No</td></tr><tr><td><code>update_table</code></td><td>Schema management</td><td>Yes</td><td>No</td></tr><tr><td><code>delete_table</code></td><td>Schema management</td><td>Yes</td><td><strong>Yes</strong> (by default)</td></tr><tr><td><code>upsert_skill</code></td><td>Skills / Playbooks</td><td>Yes</td><td>No</td></tr><tr><td><code>delete_skill</code></td><td>Skills / Playbooks</td><td>Yes</td><td>No</td></tr><tr><td><code>init_file_upload</code></td><td>File handling</td><td>No</td><td>No</td></tr><tr><td><code>commit_file_upload</code></td><td>File handling</td><td>Yes</td><td>No</td></tr><tr><td><code>file_download</code></td><td>File handling</td><td>No</td><td>No</td></tr></tbody></table></figure>

---

## Resources

- [Dataverse MCP Server: Understanding the New Tool Shape](https://www.microsoft.com/en-us/power-platform/blog/2026/06/08/dataverse-mcp-server-understanding-the-new-tool-shape/) — Kent Weare, Power Platform Blog, June 8, 2026
- [Connect to Dataverse with Model Context Protocol](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp) — Microsoft Learn
- [Configure the Dataverse MCP server for an environment](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp-disable) — Microsoft Learn (includes sample agent instructions)
- [Microsoft Dataverse Plugin: Unleashing Coding Agents on the Enterprise — Build 2026](https://www.microsoft.com/en-us/power-platform/blog/2026/06/04/microsoft-dataverse-plugin-unleashing-coding-agents-on-the-enterprise-microsoft-build-2026/) — Kent Weare, Power Platform Blog, June 4, 2026

---

*Part of the AIDevMe series on agentic AI and Power Platform architecture. Subscribe on [Substack](https://aidevme.substack.com) for new posts.*
