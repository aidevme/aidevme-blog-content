# Under the Hood: How Dataverse Skills Work and How to Write Your Own - Practical AI, Copilot & Modern Development Insights

Estimated reading time: 4 minutes

Understand the engineering decisions behind Dataverse Skills and learn to build your own custom skills for organizational patterns. This advanced guide dissects both skill file formats (Microsoft’s table format and extended YAML frontmatter), explains how AI agents select and chain skills, and reveals the three-tool strategy (MCP Server, Python SDK, PAC CLI) that optimizes performance and cost. Includes production-tested examples for automating environment provisioning and integrating agent-built solutions into Azure DevOps ALM pipelines. Essential reading for solution architects extending Dataverse Skills for enterprise use.

## Table of contents

-   [Introduction](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-introduction)

-   [The Anatomy of a Skill File](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-the-anatomy-of-a-skill-file-0)
    -   [Microsoft’s Official Format: YAML Frontmatter](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#microsofts-official-format-yaml-frontmatter)
    -   [Extended Format: Additional Metadata Fields](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#extended-format-additional-metadata-fields)
    -   [Required vs. Optional YAML Fields](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#required-vs-optional-yaml-fields)
    -   [When to Use Extended Fields](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#when-to-use-extended-fields)
-   [How Agents Select and Chain Skills](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-how-agents-select-and-chain-skills-0)
    -   [Skill chaining in practice](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#skill-chaining-in-practice)
    -   [When skills conflict](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#when-skills-conflict)
-   [The Three-Tool Strategy](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-the-three-tool-strategy-0)
    -   [Tool 1: Dataverse MCP Server](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-tool-1-dataverse-mcp-server)
    -   [Tool 2: Dataverse Python SDK](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#tool-2-dataverse-python-sdk)
    -   [Tool 3: PAC CLI](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-tool-3-pac-cli)
    -   [Decision matrix](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-decision-matrix)
-   [Deep Dive: The Dataverse Python SDK in Skills](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-deep-dive-the-dataverse-python-sdk-in-skills-0)
    -   [Authentication](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#authentication)
    -   [CRUD operations](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-crud-operations)
    -   [Pandas integration](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#pandas-integration)
    -   [Current limitations (preview)](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#current-limitations-preview)
-   [Deep Dive: MCP Tools Available to Skills](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-deep-dive-mcp-tools-available-to-skills-0)
    -   [Calling MCP tools from a skill](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#calling-mcp-tools-from-a-skill)
-   [Deep Dive: PAC CLI Operations in Skills](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-deep-dive-pac-cli-operations-in-skills-0)
    -   [Solution management](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#solution-management)
    -   [Environment operations](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-environment-operations)
    -   [Important PAC CLI note for skill authors](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-important-pac-cli-note-for-skill-authors)
-   [Writing Your Own Custom Skills](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-writing-your-own-custom-skills-0)
    -   [Skill file structure template](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#skill-file-structure-template)
    -   [Naming conventions](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-naming-conventions)
-   [Testing and Validating Custom Skills](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-testing-and-validating-custom-skills-0)
    -   [Register your skill locally](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#register-your-skill-locally)
    -   [Test with explicit skill invocation](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#test-with-explicit-skill-invocation)
    -   [Debugging skill selection](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#debugging-skill-selection)
-   [Real-World Custom Skill Examples](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-real-world-custom-skill-examples)
    -   [Example 1: Dataverse Plugins Skill](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#example-1-dataverse-plugins-skill)
    -   [Example 2: Dataverse Web Resources Skill](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-example-2-dataverse-web-resources-skill)
    -   [Which skill format should I use — table or YAML frontmatter?](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-which-skill-format-should-i-use-table-or-yaml-frontmatter)
    -   [Do skill files need to be valid Markdown?](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-do-skill-files-need-to-be-valid-markdown)
    -   [Can I use Python in skill files?](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-can-i-use-python-in-skill-files)
    -   [How long should a skill file be?](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-how-long-should-a-skill-file-be)
    -   [Can I share custom skills across my team?](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-can-i-share-custom-skills-across-my-team)
-   [References & Further Reading](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#h-references-amp-further-reading)
    -   [Dataverse Skills Repository](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#dataverse-skills-repository)
    -   [Python SDK Deep Dive](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#python-sdk-deep-dive)
    -   [MCP Server Tools](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#mcp-server-tools)
    -   [PAC CLI Reference](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#pac-cli-reference)
    -   [Third-Party Skills Ecosystems](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/#third-party-skills-ecosystems)

## **Introduction**

In [Part 1 – From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development](https://aidevme.com/from-scripts-to-intent-how-dataverse-skills-redefines-enterprise-development/) and [Part 2 – Getting Started with Dataverse Skills: Install, Configure, and Build Your First Agent-Driven Solution](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/), we covered the paradigm shift and the practical setup. Now, however, we go a level deeper—into the engineering decisions that make Dataverse Skills work. More importantly, we’ll explore the design patterns that make it extensible.

Understanding *how* Dataverse Skills work internally — the skill file formats, how agents select tools, how the Python SDK and MCP server interact — gives you two strategic advantages:

1.  **Organizational customization:** You can write your own skills that encode your firm’s specific Dataverse patterns, naming conventions, and architectural standards—turning tribal knowledge into executable agent instructions
2.  **Diagnostic capability:** When an agent makes an unexpected decision (creating a table via Web API instead of PAC CLI, for example), you can trace the decision back to specific skill instructions and adjust accordingly

This article is deliberately technical. It assumes you’re comfortable reading Markdown and YAML, understand RESTful API design, and have debugged multi-step automation workflows before. The target reader is a senior Power Platform developer or solution architect who needs to either extend Dataverse Skills for enterprise use or evaluate its technical architecture for governance approval.

We will dissect actual skill file anatomy, decode the agent’s tool selection heuristics, and walk through building two production-grade custom skills: one for automating environment provisioning workflows, and one for integrating agent-built solutions into Azure DevOps ALM pipelines. By the end, you’ll understand not just *what* Dataverse Skills does, but *how*—and more importantly, how to make it do what your organization needs.

---

![Flowchart showing AI agent analyzing natural language prompt and selecting appropriate Dataverse skills in sequence, with dependency chain from dataverse-connect through dataverse-create-table](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-anatomy-of-skill-file-yaml-structure.png?resize=1024%2C683&ssl=1)

## **The Anatomy of a Skill File**

Every Dataverse skill is a Markdown file with YAML frontmatter and instructional content. This is intentional — the format is readable by humans, editable in any text editor, and interpretable by any coding agent without compilation.

### Microsoft’s Official Format: YAML Frontmatter

The official Microsoft Dataverse-skills repository uses YAML frontmatter at the top of each skill file. Here’s the actual format from the `dv-metadata` skill:

Markdown

```
---
name: dv-metadata
description: >
  Create and modify Dataverse tables, columns, relationships, forms, and views using the Python SDK and Web API.
  Use when: "add column", "create table", "add relationship", "lookup column", "create form",
  "create view", "modify form", "FormXml", "SavedQuery", "option set", "picklist",
  "MetadataService", "EntityDefinitions".
  Do not use when: reading/writing data records (use dv-python-sdk),
  exporting solutions (use dv-solution).
---

# Skill: Metadata — Making Changes

**Before the first metadata change in a session, confirm the target environment with the user.** See the Multi-Environment Rule in the overview skill for the full confirmation flow.

---

## How Changes Are Made: Environment-First

**Do not write solution XML by hand to create new tables, columns, forms, or views.**

The environment validates metadata far more reliably than an agent editing XML. The correct workflow is:

1. **Make the change in the environment** via the Dataverse MetadataService API (or `pac` commands where available)
2. **Pull the change into the repo** via `pac solution export` + `pac solution unpack`
3. **Commit the result**

The exported XML is generated by Dataverse itself and is always valid. Hand-written XML is fragile — a single incorrect attribute or missing element causes an import failure with an opaque error.

## Creating a Table

**ALWAYS use the SDK unless you need full control over OwnershipType, HasActivities, or other advanced properties.** Do NOT use `requests` or `urllib` for table creation when the SDK can handle it.

**SDK approach (use this by default):**

\```python
from auth import get_credential, load_env
from PowerPlatform.Dataverse.client import DataverseClient
import os

load_env()
client = DataverseClient(os.environ["DATAVERSE_URL"], get_credential())

info = client.tables.create(
    "new_ProjectBudget",
    {"new_Amount": "decimal", "new_Description": "string"},
    solution="MySolution",
    primary_column="new_Name",
)
print(f"Created: {info['table_schema_name']}")
\```
```

**Key characteristics of Microsoft’s format:**

-   **YAML frontmatter:** Uses standard YAML with `---` delimiters

-   **Multiline description:** The `>` character enables clean multiline descriptions
-   **Embedded triggers:** “Use when” patterns are quoted phrases the agent should recognize (e.g., `"add column"`, `"create table"`)

-   **Disambiguation guidance:** “Do not use when” directs agents to other skills, preventing incorrect skill selection
-   **Natural flow:** After the frontmatter, the skill body provides detailed instructions using standard Markdown

### Extended Format: Additional Metadata Fields

For organizational skills or when you need explicit security boundaries and tool restrictions, you can extend the YAML frontmatter with additional fields:

Markdown

```
---
name: aidevme-create-table
description: >
  Creates a new custom table in Dataverse with the specified schema.
  Use when: "create a table", "add an entity", "I need a new table for",
  "create custom table", "new Dataverse table".
  Do not use when: modifying existing tables (use dv-metadata),
  creating virtual tables (requires connector configuration).
version: 1.0.0
phase: build
allowed-tools:
  - bash
  - web_fetch
  - file
safety:
  - Verify the publisher prefix matches the active solution before creating
  - Check for existing tables with the same logical name
  - Never create tables in the default solution
  - Warn if table name conflicts with a system table
requires:
  - dataverse-connect
  - dataverse-create-solution
priority: normal
---

## Purpose

Creates a Dataverse table using the Web API. Handles all column types, 
ownership modes, and automatically adds the table to the active solution.

## When to use

Use this skill when the user describes needing a new data entity. 
You do not need to be asked to "use the create-table skill" — 
infer when a table is needed from context.

## Pre-conditions

1. Active PAC CLI auth profile exists (`pac org who` succeeds)
2. Target solution exists and is active
3. Publisher prefix is known (from solution metadata or user input)

## Steps

### 1. Validate publisher prefix

Run: `pac org who` to get the environment URL.
Check active solution via MCP: `describe_table("solution")`
Extract publisher prefix from solution metadata.

If publisher prefix is unknown, ask the user before proceeding.

### 2. Check for conflicts

Before creating, call:
- `list_tables` via MCP — scan for tables matching the intended logical name

- If a match exists, report it and ask the user whether to skip, update, or abort

### 3. Create the table via Web API

Use the Dataverse Web API endpoint:

POST https://{org}.crm.dynamics.com/api/data/v9.2/EntityDefinitions

Request body:
\```json
{
  "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",
  "SchemaName": "{PublisherPrefix}_{TableName}",
  "DisplayName": { "LocalizedLabels": [{ "Label": "{Display Name}", "LanguageCode": 1033 }] },
  "DisplayCollectionName": { "LocalizedLabels": [{ "Label": "{Plural Display Name}", "LanguageCode": 1033 }] },
  "OwnershipType": "UserOwned",
  "HasActivities": false,
  "IsActivity": false
}
\```

### 4. Add to solution

After creation:
\```bash
pac solution add-solution-component \
  --solutionUniqueName {SolutionName} \
  --component {LogicalName} \
  --componentType 1
\```

### 5. Confirm and report

Report the created table's:
- Schema name

- Logical name  
- Solution membership

- Next suggested actions (add columns, create relationships)

## Safety checks

- NEVER create tables without a publisher prefix

- NEVER add tables to the Default solution
- If HasActivities is set to true, warn the user this cannot be changed after creation

- Data type selection is PERMANENT — warn before creating columns if the user seems uncertain

## Error handling

| Error | Cause | Resolution |
|-------|-------|------------|
| 400 SchemaName exists | Table already exists | Skip or report to user |
| 403 Forbidden | Missing system customizer role | Check environment permissions |
| 400 Invalid publisher | Publisher not registered | Create publisher first or correct the prefix |
```

### Required vs. Optional YAML Fields

**Required fields (Microsoft’s base format):**

**`name`** — Unique identifier for the skill. Use kebab-case naming: `{publisher}-{action}-{subject}` (e.g., `dv-metadata`, `aidevme-create-environment`)

**`description`** — Multi-line description that includes:

-   **What the skill does** (first line, concise)

-   **“Use when:”** Pattern triggers with quoted examples (e.g., `"add column"`, `"create table"`)
-   **“Do not use when:”** Disambiguation guidance pointing to other skills

The description is what agents use to determine skill relevance. Write it from the agent’s perspective — what should trigger this skill vs. other skills?

**Optional fields (for organizational extensions):**

**`allowed-tools`** — **Critical security boundary.** Restricts which tools the agent can use for this skill. In traditional software, you control execution through code paths and privilege checks. With agent-driven development, you control execution through declarative tool restrictions.

This matters more than you might initially assume: a data-loading skill may legitimately allow `bash` (for running Python scripts) and `file` (for reading CSV imports), but allowing `web_fetch` opens the door to data exfiltration via external API calls. The `allowed-tools` field is your defense against prompt injection attacks that attempt to trick the agent into unauthorized operations.

**`safety`** — Explicit safety rules the agent must check before proceeding. These are not enforced programmatically — they are instructions the agent interprets. Well-written safety rules prevent destructive operations. Think of these as codified guardrails that encode your organization’s governance policies.

**`requires`** — Declares skill dependencies. The agent will load prerequisite skills before executing this one, ensuring the environment is in the right state. This creates a dependency graph that the agent traverses automatically.

**`phase`** — Categorizes the skill: `connect` (authentication/setup), `build` (schema changes), `operate` (data operations), or `custom` (organizational extensions).

**`priority`** — Controls skill selection when multiple skills match the same intent. Set to `high` to override built-in skills with your organization’s custom version.

**`version`** — Semantic version for tracking skill evolution. Useful when sharing skills across teams or publishing to internal marketplaces.

### When to Use Extended Fields

**Use the base format (name + description only) when:**

-   Creating skills that closely follow Microsoft’s patterns

-   You want maximum simplicity and maximum agent compatibility
-   Your skills don’t require explicit tool restrictions

-   You’re contributing back to the Microsoft repository

**Add extended fields when:**

-   You need explicit security boundaries (`allowed-tools`)

-   You’re building organizational skills with complex dependencies (`requires`)
-   You want semantic versioning and priority control

-   You need to override or enhance Microsoft’s built-in skills (`priority`)
-   You have strict governance requirements (`safety`)

All fields work with GitHub Copilot and Claude Code (via .agent.md files) and Claude Desktop (via MCP skills). The agent interprets the YAML metadata and follows the instructional content in the body.

---

![Decision matrix showing three Dataverse tools: MCP Server for fast metadata queries, Python SDK for bulk data operations, and PAC CLI for ALM and solution management](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-three-tool-strategy-mcp-python-pac.png?resize=1024%2C683&ssl=1)

## How Agents Select and Chain Skills

The selection logic is not rule-based in the traditional sense. The agent uses the `name`, `description`, and `triggers` fields across all installed skills to make a relevance judgment.

When you type a prompt like:

```
Create a table for tracking employee certifications
```

The agent:

1.  Scans all installed skills for relevance to the intent
2.  Identifies `dataverse-create-table` as the primary match
3.  Checks its `requires` field — loads `dataverse-connect` and `dataverse-create-solution` first
4.  Executes the skill steps in sequence
5.  Dynamically selects tools within each step based on the `allowed-tools` list

### Skill chaining in practice

For a complex prompt like the recruiting system example from Part 2, the agent chains skills in this order:

```
dataverse-connect
  └── dataverse-mcp-register
dataverse-create-solution
dataverse-create-table (× 5, in parallel where safe)
  └── dataverse-create-column (× N per table)
  └── dataverse-create-relationship (× 2)
dataverse-load-data
  └── dataverse-generate-sample-data
dataverse-query
```

The agent determines this chain from the `requires` declarations and the semantic content of the prompt — not from a hardcoded workflow

### When skills conflict

If two skills match the same intent (for example, a custom `aidevme-create-table` and the built-in `dataverse-create-table`), the agent uses recency and specificity to choose: more specific skills (higher match on description and triggers) take precedence over more general ones. You can also set explicit priority in the frontmatter:

```
priority: high  # Overrides built-in skills with the same intent
```

---

![Dataverse Python SDK architecture diagram showing DataverseClient, Azure Identity authentication, bulk operations with CreateMultiple, and Pandas DataFrame integration for data transformation](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-python-sdk-architecture-deep-dive.png?resize=1024%2C683&ssl=1)

One of the most important—and least obvious—design decisions in Dataverse Skills is its tool selection strategy. Unlike traditional development where the developer decides which API to call, agent-driven development requires encoding that decision-making logic into the skills themselves. The skills must teach the agent not just *how to use* the Dataverse Web API, Python SDK, and PAC CLI, but *when* each is the optimal choice.

This isn’t just about performance optimization. It’s about cost management (MCP calls consume Copilot credits), operational correctness (bulk operations require transactional integrity), and architectural compliance (ALM operations must use PAC CLI to generate audit-trail-compatible solution exports).

The tool selection logic in Dataverse Skills reflects real-world production learnings—specifically, where early adopters made expensive mistakes by using the wrong tool for the job. The guidance below isn’t theoretical; it’s battle-tested.

### Tool 1: Dataverse MCP Server

**Best for:**

-   Fast, read-only metadata queries (`list_tables`, `describe_table`)

-   Simple record reads (`read_query`)
-   Single-record create/update when transactional integrity is not critical

**Limitations:**

-   Charged per use (Copilot credits) for non-Copilot Studio clients

-   Not optimal for bulk operations
-   Limited to the tools exposed by the MCP server

### Tool 2: Dataverse Python SDK

**Best for:**

-   Bulk data operations (100+ records)

-   Operations requiring Pandas DataFrames for transformation
-   Data profiling and quality analysis

-   ETL pipelines that write back to Dataverse

Python

```
from PowerPlatform.Dataverse.client import DataverseClient
from azure.identity import AzureCliCredential

client = DataverseClient("https://yourorg.crm.dynamics.com", AzureCliCredential())

# Bulk create with native CreateMultiple (100x faster than looping)
records = [
    {"aidevme_firstname": f"Consultant {i}", "aidevme_specialization": "Power Platform"}
    for i in range(1, 51)
]
ids = client.records.create("aidevme_consultant", records)
print(f"Created {len(ids)} consultants")

# SQL query for analytical reads
results = client.query_sql(
    "SELECT TOP 20 aidevme_projectname, aidevme_status "
    "FROM aidevme_project "
    "WHERE aidevme_status = 1 "  # 1 = Active
    "ORDER BY nextwit_createdon DESC"
)
```

### Tool 3: PAC CLI

Best for:

-   Solution ALM (export, import, publish)

-   Environment management
-   Authentication lifecycle

-   Component registration (adding tables/columns to solutions)

Bash

```


# Solution export for ALM
pac solution export \
  --name ConsultingTracker \
  --path ./solutions/ConsultingTracker.zip \
  --managed false

# Publish all customizations
pac solution publish
```

### Decision matrix

The skills encode this decision logic explicitly:

| **Task** | **MCP** | **Python SDK** | **PAC CLI** |
| List tables | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Primary | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) |
| Read 10 records | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Primary | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) |
| Read 10,000 records | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Primary | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) |
| Create 1 record | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) |
| Create 500 records | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Primary | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) |
| Create a table schema | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) via Web API call |
| Add component to solution | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Primary |
| Export solution | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Primary |
| Authenticate | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Primary |

---

![MCP Server tool palette showing available Dataverse tools: list_tables, describe_table, read_query, create_record, update_record, search_knowledge, list_prompts, and execute_prompt](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-mcp-server-tools-toolkit.png?resize=1024%2C683&ssl=1)

## Deep Dive: The Dataverse Python SDK in Skills

The Python SDK (`PowerPlatform-Dataverse-Client`, currently v0.1.0b7) is the workhorse for the Operate phase. Understanding its capabilities helps you write better skills and better prompts.

### Authentication

The SDK uses Azure Identity providers — the same pattern as all modern Azure SDKs:

Python

```
from azure.identity import (
    AzureCliCredential,         # Development: uses 'az login' session
    InteractiveBrowserCredential, # Development: browser popup
    ClientSecretCredential,      # Production: service principal
    CertificateCredential,       # Production: certificate-based SPN
)
from PowerPlatform.Dataverse.client import DataverseClient

# For local development (preferred with Dataverse Skills)
credential = AzureCliCredential()

client = DataverseClient("https://yourorg.crm.dynamics.com", credential)
```

### CRUD operations

Python

```


# Create single record
ids = client.records.create("aidevme_project", {
    "aidevme_projectname": "Digital Transformation",
    "aidevme_status": 1,  # Active
    "aidevme_budget": 450000.00
})

# Create multiple records (uses CreateMultiple — much faster)
ids = client.records.create("aidevme_project", [
    {"aidevme_projectname": "Project Alpha", "aidevme_status": 1},
    {"aidevme_projectname": "Project Beta",  "aidevme_status": 2},
])

# Read with filter
for batch in client.records.get(
    "aidevme_project",
    filter="aidevme_status eq 1",
    select=["aidevme_projectname", "aidevme_budget"]
):
    for record in batch:
        print(record["aidevme_projectname"])

# Update
client.records.update("aidevme_project", record_id, {
    "aidevme_status": 3  # On Hold
})

# Delete
client.records.delete("aidevme_project", record_id)
```

### Pandas integration

For analytical use cases, the SDK wraps results in DataFrames:

Python

```
import pandas as pd

# Get all projects as a DataFrame
df = client.records.get_dataframe(
    "aidevme_project",
    select=["aidevme_projectname", "aidevme_status", "aidevme_budget"]
)

# Analyze
print(df.groupby("aidevme_status")["aidevme_budget"].sum())
print(df.describe())

# Write analysis results back to Dataverse
summary_records = df.groupby("aidevme_status").agg(
    total_projects=("aidevme_projectname", "count"),
    total_budget=("aidevme_budget", "sum")
).reset_index().to_dict("records")

client.records.create("aidevme_portfoliosummary", summary_records)
```

### Current limitations (preview)

-   General-purpose OData batching not fully supported

-   `DeleteMultiple` not yet available (use individual deletes or Python loops)
-   Limited retry policy — only network errors trigger automatic retry

-   No association operation support for relationships

---

![Terminal window showing Power Platform CLI commands for solution export, import, and publish, with ALM pipeline diagram showing deployment flow from dev to test to production environments](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-pac-cli-operations-alm-pipeline.png?resize=1024%2C683&ssl=1)

## Deep Dive: MCP Tools Available to Skills

When the Dataverse MCP server is connected, skills can call these built-in tools:

| **Tool** | **Description** | **Example use** |
| list\_tables | Lists all tables in the environment | Environment discovery, schema auditing |
| describe\_table | Returns schema for a specific table | Pre-build validation, column discovery |
| read\_query | Executes a read query (OData or natural language) | Fetching records for business questions |
| create\_record | Creates a single record | Quick single-record operations |
| update\_record | Updates a single record | Status updates, field corrections |
| search\_knowledge | Searches knowledge base content | RAG operations on Dataverse knowledge |
| list\_prompts | Lists reusable prompts in the environment | Discovering Business Skills |
| execute\_prompt | Executes a stored prompt | Running Business Skills from code |

### Calling MCP tools from a skill

Within a skill file, MCP tool calls are described in natural language — the agent translates them to actual API calls:

Markdown

```


## Steps

### 1. Verify table exists

Call MCP tool: `describe_table("aidevme_project")`

If the response is an error or empty, the table does not exist. 
Proceed to create it. Otherwise, report the existing schema to the user 
and ask whether to add columns, modify existing ones, or abort.

### 2. Query active records

Call MCP tool: `read_query` with filter:
"Show me all aidevme_project records where aidevme_status equals Active, 
ordered by creation date descending, limit 20"
```

---

![Custom skill authoring workflow showing transformation from empty skill template to completed organizational skill file with YAML frontmatter, Markdown instructions, and custom branding](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-writing-custom-skills-authoring.png?resize=1024%2C683&ssl=1)

The PAC CLI is called via bash commands within skills. Key patterns:

### Solution management

Bash

```


# Create a solution with publisher
pac solution create \
  --name ConsultingTracker \
  --publisher-name AiDevMe \
  --publisher-prefix aidevme \
  --version 1.0.0.0

# Export (unmanaged, for source control)
pac solution export \
  --name ConsultingTracker \
  --path ./solutions/ \
  --managed false

# Import to another environment
pac solution import \
  --path ./solutions/ConsultingTracker.zip \
  --activate-plugins true

# Publish all pending customizations
pac solution publish --async false
```

### Environment operations

Bash

```


# List environments
pac env list --filter "Dev"

# Copy environment (for testing)
pac admin copy \
  --source-url https://source.crm.dynamics.com \
  --target-url https://target.crm.dynamics.com
```

### Important PAC CLI note for skill authors

The skill documentation on the Dataverse Skills repository includes a critical warning:

**Never use `pac auth token`** — this command does not exist. Use Azure CLI instead:

Bash

```
az account get-access-token \
  --resource "https://yourorg.crm.dynamics.com/" \
  --tenant "your-tenant-id" \
  --query accessToken \
  -o tsv
```

This is the kind of tribal knowledge that makes skills valuable — encoding what *not* to do alongside what *to* do.

---

![Custom skill authoring workflow showing transformation from empty skill template to completed organizational skill file with YAML frontmatter, Markdown instructions, and custom branding](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-writing-custom-skills-authoring_original.png?resize=1024%2C683&ssl=1)

Creating a custom skill involves three steps: defining the metadata, writing the instruction body, and testing with your coding agent.

### Skill file structure template

All Dataverse skills use YAML frontmatter. Start with the required fields (name, description) and add optional fields as needed:

**Base format (required fields only):**

Markdown

```
---
name: {publisher}-{action}-{subject}
description: >
  One or two sentences describing what this skill does and when to use it.
  Use when: "trigger phrase 1", "trigger phrase 2", "natural language pattern".
  Do not use when: {anti-patterns that should use other skills}.
---

# Skill: {Title}

## Purpose

What does this skill do? When should an agent invoke it?

## Pre-conditions

1. What must be true before this skill can run?
2. What environment state is assumed?

## Steps

### Step 1: Validate inputs

What to check first. Include error conditions.

### Step 2: Main operation

The actual work. Include tool calls, code examples, API payloads.

### Step 3: Verify and report

How to confirm success. What to report to the user.

## Error handling

| Error | Cause | Resolution |
|-------|-------|------------|
| Error description | Why it happens | How to fix it |

## Examples

### Example 1: Basic usage

Input: "..."
Expected agent behavior: "..."
Expected output: "..."
```

**Extended format (with optional fields):**

Markdown

```
---
name: {publisher}-{action}-{subject}
description: >
  One or two sentences describing what this skill does and when to use it.
  Use when: "trigger phrase 1", "trigger phrase 2", "natural language pattern".
  Do not use when: {anti-patterns that should use other skills}.
version: 1.0.0
phase: connect | build | operate | custom
allowed-tools:
  - bash
  - file
  - web_fetch  # Only if needed
safety:
  - List explicit safety rules here
  - One rule per line
  - Be specific about what must be checked before proceeding
requires:
  - dataverse-connect  # Almost always required
  - list-other-prerequisites
priority: normal  # or high to override built-in skills
---

## Purpose

What does this skill do? When should an agent invoke it?

## Pre-conditions

1. What must be true before this skill can run?
2. What environment state is assumed?

## Steps

### Step 1: Validate inputs

What to check first. Include error conditions.

### Step 2: Main operation

The actual work. Include tool calls, code examples, API payloads.

### Step 3: Verify and report

How to confirm success. What to report to the user.

## Error handling

| Error | Cause | Resolution |
|-------|-------|------------|
| Error description | Why it happens | How to fix it |

## Examples

### Example 1: Basic usage

Input: "..."
Expected agent behavior: "..."
Expected output: "..."
```

### Naming conventions

Following the repository’s naming pattern:

Markdown

```
{publisher-prefix}-{verb}-{noun}

# Examples:
aidevme-create-environment
aidevme-export-solution-bundle
aidevme-dv-provision-dev-environment
aidevme-validate-publisher-prefix
```

---

![QA workflow diagram showing custom skill validation stages: syntax check, tool permission verification, dependency validation, agent execution test, and error handling verification with pass/fail indicators](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-testing-validation-qa-workflow.png?resize=1024%2C683&ssl=1)

## Testing and Validating Custom Skills

### Register your skill locally

For Claude Code, add your skill to the `.claude-plugin` directory in your repository:

```
your-project/
└── .claude-plugin/
    ├── marketplace.json
    └── skills/
        └── aidevme-create-environment.md
```

The `marketplace.json` file registers your skills:

JSON

```
{
  "name": "AiDevMe Power Platform Skills",
  "version": "1.0.0",
  "publisher": "aidevme",
  "skills": [
    {
      "name": "aidevme-create-environment",
      "path": "skills/aidevme-create-environment.md"
    }
  ]
}
```

For GitHub Copilot, add to `.github/plugins/`:

```
your-project/
└── .github/plugins/
    └── aidevme/
        └── skills/
            └── aidevme-create-environment.md
```

### Test with explicit skill invocation

During development, invoke skills explicitly to test them in isolation:

```


# Claude Code
/aidevme-create-environment Create a new developer sandbox environment 
named "Project Alpha Dev" with the Consulting Tracker solution installed.
```

### Debugging skill selection

If the agent is not selecting your skill when you expect it to:

1.  Check that the `description` contains the natural language patterns the user is likely to type
2.  Add explicit `trigger phrases` in the skill body
3.  Increase `priority` in the frontmatter if competing with built-in skills
4.  Verify the skill file is correctly registered in `marketplace.json`

---

## Real-World Custom Skill Examples

The following examples are from [Daniel Kerridge’s claude-code-power-platform-skills repository](https://github.com/DanielKerridge/claude-code-power-platform-skills) — a collection of production-ready skills for Power Platform development with Claude Code. These skills demonstrate how to encode complex domain knowledge into reusable, agent-executable instructions.

### Example 1: Dataverse Plugins Skill

This skill guides the agent through developing, registering, and deploying Dataverse plugins — C# server-side extensions that execute custom business logic in the Dataverse execution pipeline.

**Source:** [dataverse-plugins/SKILL.md](https://github.com/DanielKerridge/claude-code-power-platform-skills/tree/master/dataverse-plugins)

Markdown

```
---
name: dataverse-plugins
description: >
  Use when developing, registering, or deploying Dataverse plugins (C# server-side extensions).
  Covers the IPlugin interface, execution pipeline stages, entity images, common patterns
  (auto-numbering, cascading updates, validation), and registration/deployment.
  Triggers on: "plugin", "server-side logic", "business logic", "auto-number",
  "cascading update", "pre-operation", "post-operation", "plugin registration",
  "IPlugin", "execution pipeline", "plugin trace", "InvalidPluginExecutionException",
  "PreValidation", "PostOperation".
license: MIT
compatibility: "Dataverse SDK, .NET 4.6.2+, Plugin Registration Tool"
metadata:
  author: custom
  version: "1.0.0"
  platform: "Microsoft Power Platform / Dataverse"
---

# Dataverse Plugins Skill

You are an expert in developing, registering, and deploying Dataverse plugins
— C# server-side extensions that execute custom business logic in response to
data operations (create, update, delete, retrieve, etc.) in the Dataverse
execution pipeline.

## CRITICAL RULES

1. **Plugins run in a sandbox** by default. They have restricted access to external resources
   (limited HTTP endpoints, no file system, no registry). Plan accordingly.

2. **2-minute timeout** for synchronous plugins. Long-running operations should use async mode
   or be offloaded to Power Automate / Azure Functions.

3. **Throw `InvalidPluginExecutionException`** to show user-facing errors. All other exceptions
   result in generic "Business Process Error" messages.

4. **Never use static variables** for state. Plugin instances are cached and reused across
   requests. Use `IPluginExecutionContext.SharedVariables` for pipeline-scoped state.

5. **Always register entity images** when you need pre/post field values. Don't make extra
   Retrieve calls when an image would suffice.

6. **Test with Plugin Trace Log** enabled. Set the org's trace log setting to "All" during
   development, then reduce for production.

## Quick Reference

| Concept | Details |
|---|---|
| Interface | `Microsoft.Xrm.Sdk.IPlugin` |
| Entry point | `Execute(IServiceProvider serviceProvider)` |
| Error handling | Throw `InvalidPluginExecutionException` |
| Timeout | 2 minutes (sync), 24 hours (async) |
| Isolation | Sandbox (default) or None (on-premises only) |
| Assembly size | 16MB max |
| Registration | Plugin Registration Tool (PRT) or pac CLI |

## Resource Files

- `resources/plugin-anatomy.md` -- IPlugin interface, services, context, base class pattern

- `resources/execution-pipeline.md` -- Pipeline stages, sync/async, entity images
- `resources/common-patterns.md` -- Auto-numbering, validation, cascading updates, error handling

- `resources/registration-deployment.md` -- PRT, pac CLI, step registration, debugging
```

**Key features of this skill:**

-   **Critical rules section** — Encodes non-obvious constraints (sandbox limitations, timeout rules, error handling patterns) that prevent common mistakes

-   **Quick reference table** — Provides at-a-glance lookup for plugin fundamentals
-   **Resource files** — Breaks domain knowledge into focused sub-documents, keeping the main skill file concise while providing deep expertise when needed

-   **Comprehensive trigger phrases** — Ensures the skill activates on both technical terms (“IPlugin”, “PreValidation”) and natural language (“server-side logic”, “business logic”)

### Example 2: Dataverse Web Resources Skill

This skill teaches the agent to create, deploy, and manage Dataverse web resources — JavaScript, HTML, CSS, and other web content used to extend model-driven apps.

**Source:** [dataverse-web-resources/SKILL.md](https://github.com/DanielKerridge/claude-code-power-platform-skills/tree/master/dataverse-web-resources)

Markdown

```
---
name: dataverse-web-resources
description: >
  Use when creating, deploying, or managing Dataverse web resources for model-driven apps.
  Covers JavaScript form scripts (OnLoad, OnSave, OnChange events), HTML dashboard pages,
  CSS styling, image resources, navigation/side panes, ribbon/command bar customization,
  business process flow client API, and deployment via the Web API. Triggers on:
  "web resource", "javascript form", "form script", "html dashboard", "ribbon command", 
  "onload event", "onchange event", "onsave event", "formContext", "Xrm.WebApi", 
  "web resource deployment", "dashboard page", "form event handler", "side pane", 
  "command bar", "ribbon", "modal dialog", "navigation", "Xrm.App", "Xrm.Navigation", 
  "business process flow", "bpf", "stage change".
license: MIT
compatibility: "Dataverse Web API v9.2, Model-Driven Apps"
metadata:
  author: custom
  version: "1.0.0"
  platform: "Microsoft Power Platform / Dataverse"
---

# Dataverse Web Resources Skill

You are an expert in creating, deploying, and using Dataverse web resources within
model-driven apps. Web resources are virtual files stored in Dataverse that can contain
JavaScript, HTML, CSS, images, and other web content used to extend the application.

## CRITICAL RULES

1. **Always use a publisher prefix namespace** for web resource names (e.g., `cnt_/js/formscript.js`).
   The forward slash creates a virtual folder structure.

2. **JavaScript must use the namespace pattern.** Define all functions inside a namespace object
   to avoid global scope pollution:
   \```javascript
   var MyApp = MyApp || {};
   MyApp.FormScripts = { onLoad: function(executionContext) { ... } };
   \```

3. **Always pass `executionContext`** to form event handlers. Enable "Pass execution context
   as first parameter" when registering. Then: `var formContext = executionContext.getFormContext();`

4. **Content must be base64-encoded** when creating via the API. Use PowerShell's
   `[Convert]::ToBase64String()` or equivalent.

5. **Always publish after creating/updating** web resources. They remain in draft until published.

6. **5MB size limit** per web resource (configurable by org admin). Minify large JS/CSS.

7. **Always consult `resources/ux-decision-guide.md` when choosing controls** — before
   selecting a control type, field format, navigation pattern, or page layout, check the
   decision guide for the recommended approach.

8. **`Xrm` is NOT available in web resources loaded via MDA sitemap.** Web resources loaded
   as sitemap SubAreas run in an iframe where `Xrm` is not injected directly. Use this
   fallback chain: (1) `Xrm.Utility.getGlobalContext()`, (2) `parent.Xrm.Utility.getGlobalContext()`,
   (3) `WhoAmI` API call (`GET /api/data/v9.2/WhoAmI`) for user identity. Cache the result.

## Quick Reference

| Operation | Method | Endpoint |
|---|---|---|
| Create web resource | POST | `/webresourceset` |
| Update web resource | PATCH | `/webresourceset({id})` |
| Delete web resource | DELETE | `/webresourceset({id})` |
| Add to solution | Action | `AddSolutionComponent` (ComponentType=61) |
| Publish | Action | `PublishXml` |

## Xrm Client API Quick Reference

| API | Purpose | Target |
|---|---|---|
| `Xrm.App.sidePanes.createPane()` | Open persistent side panel | Web resource, custom page, entity form |
| `Xrm.Navigation.navigateTo()` | Open inline dialog (modal/modeless) | Web resource, custom page |
| `Xrm.Navigation.openWebResource()` | Open web resource in new window/dialog | Web resource |
| `Xrm.WebApi.createRecord()` | Create record from form JS | Dataverse table |
| `formContext.data.process.moveNext()` | Navigate BPF stages | Form process |
| `Xrm.Utility.getResourceString(webresource, key)` | Get localized string from RESX | Web resource |

## Resource Files

- `resources/types-reference.md` -- All 12 web resource types with Type IDs and use cases

- `resources/js-form-scripts.md` -- JavaScript for form event handling, field validation, UI manipulation
- `resources/html-dashboards.md` -- HTML pages for dashboards, charts, and KPI displays

- `resources/deployment.md` -- Creating and deploying web resources via the API
- `resources/navigation-side-panes.md` -- Side panes, dialogs, navigation APIs (Xrm.App, Xrm.Navigation)

- `resources/ribbon-command-bar.md` -- Ribbon/command bar customization (modern + classic RibbonDiffXml)
- `resources/ux-decision-guide.md` -- Decision trees for control, layout, and navigation pattern selection

- `resources/bpf-client-api.md` -- Business Process Flow JavaScript API, events, stage navigation
```

**Key features of this skill:**

-   **Platform-specific constraints** — Critical rules address web resource quirks that aren’t documented well elsewhere (namespace requirements, `Xrm` availability in sitemap SubAreas, base64 encoding)

-   **Dual quick reference tables** — Separates Web API operations from Client API patterns for faster lookup
-   **Extensive resource files** — 8 focused reference documents covering different web resource scenarios (form scripts, dashboards, navigation, BPF, ribbon customization)

-   **Rich trigger vocabulary** — 30+ trigger phrases covering both technical APIs (`Xrm.WebApi`, `formContext`) and natural language (“form script”, “side pane”, “command bar”)

**Why these examples matter:**

Both skills demonstrate **production-grade skill design** — they don’t just tell the agent what to do, they encode the *why* through critical rules, prevent common mistakes through safety guardrails, and provide quick-reference tables for efficient execution. The pattern of separating foundational rules (in the main skill) from detailed implementation patterns (in resource files) keeps skills maintainable while providing deep expertise when needed.

You can explore the complete skill collection at [github.com/DanielKerridge/claude-code-power-platform-skills](https://github.com/DanielKerridge/claude-code-power-platform-skills).

---

## Frequently Asked Questions

### Which skill format should I use — table or YAML frontmatter?

Both work. Use the **table format** if you’re contributing to the Microsoft repository or want maximum simplicity. Use **YAML frontmatter** when you need explicit tool restrictions (`allowed-tools`), dependency chains (`requires`), or priority control. For organizational skills that need security boundaries, YAML frontmatter is the better choice.

### Do skill files need to be valid Markdown?

Yes, but the bar is low. Standard Markdown rendering is expected, but agents primarily process the raw text. The most critical parts are the YAML frontmatter (which must be valid YAML) and the content structure (headings, code blocks). Minor Markdown formatting issues will not prevent the skill from working.

### Can I use Python in skill files?

Yes. Code blocks in any language are interpreted as instructions to the agent. If you include a Python code block, the agent will generate and execute that code (subject to the `allowed-tools` permission including `bash`). If `bash` is allowed, the agent can run Python scripts by writing them to a temp file and executing them.

### How long should a skill file be?

Best practice from the repository is to keep each skill focused on a single operation. If a skill file exceeds 200 lines, consider splitting it. The `requires` field handles dependencies — do not repeat shared logic across skills.

Yes. Commit the `.claude-plugin/` or `.github/plugins/` directory alongside your solution source in version control. All developers cloning the repository get the same skills. This is one of the most powerful aspects of the format.

---

## References & Further Reading

### Dataverse Skills Repository

-   [microsoft/Dataverse-skills on GitHub](https://github.com/microsoft/Dataverse-skills)

-   [Full skill catalog](https://github.com/microsoft/Dataverse-skills/tree/main/.github/plugins/dataverse/skills)
-   [AGENTS.md — contributor conventions](https://github.com/microsoft/Dataverse-skills/blob/main/AGENTS.md)

-   [CONTRIBUTING.md](https://github.com/microsoft/Dataverse-skills/blob/main/CONTRIBUTING.md)

### Python SDK Deep Dive

-   [Dataverse SDK for Python overview (Microsoft Learn)](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/sdk-python/overview)

-   [Build agentic flows with Dataverse SDK for Python](https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave2/data-platform/build-agentic-flows-dataverse-sdk-python)
-   [Python SDK API reference](https://learn.microsoft.com/en-us/python/api/powerplatform-dataverse-client/powerplatform.dataverse.client.dataverseclient)

-   [Analyze and automate business data with Python SDK](https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/dataverse-sdk-for-python)
-   [Python SDK examples on GitHub](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/examples/README.md)

### MCP Server Tools

-   [Connect to Dataverse with MCP](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp)

-   [List of tools available in Dataverse MCP Server](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp)

### PAC CLI Reference

-   [pac solution commands](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/solution)

-   [pac admin commands](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/admin)
-   [Use OAuth with Dataverse](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth)

### Third-Party Skills Ecosystems

-   [Dataverse Web API skill on LobeHub Skills Marketplace](https://lobehub.com/skills/danielkerridge-claude-code-power-platform-skills-dataverse-web-api)

-   [power-platform-skills DeepWiki](https://deepwiki.com/microsoft/power-platform-skills)
-   [DanielKerridge/claude-code-power-platform-skills: Power Platform skills for Claude Code — plan, build, deploy, and test Power Apps, Dataverse, plugins, PCF controls, and more.](https://github.com/DanielKerridge/claude-code-power-platform-skills)

### *Related*

[![Split-screen illustration showing developer transformation from traditional Power Platform development with multiple tools and context-switching to streamlined AI-assisted development with Dataverse Skills using natural language intent](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-intent-driven-development-transformation.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/from-scripts-to-intent-how-dataverse-skills-redefines-enterprise-development/ "From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development")

#### [From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development](https://aidevme.com/from-scripts-to-intent-how-dataverse-skills-redefines-enterprise-development/ "From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development")

Microsoft's Dataverse Skills represents a paradigm shift in Power Platform development—from manual tool orchestration to intent-driven AI coding. This open-source plugin for GitHub Copilot and Claude Code eliminates the developer tax of context-switching between PAC CLI, maker portal, and API documentation. Instead of writing scripts, developers describe their intent in…

April 3, 2026

In "AI & Copilot"

[![Power Apps MCP Server agent feed — AI agent extracting Dataverse records with human approval interface — AIDevMe 2026](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/02/power-apps-mcp-server-complete-guide-featured.png?fit=768%2C512&ssl=1&resize=350%2C200)](https://aidevme.com/power-apps-mcp-server-complete-guide/ "Power Apps MCP Server: Complete Guide to Every Feature (Public Preview 2026)")

#### [Power Apps MCP Server: Complete Guide to Every Feature (Public Preview 2026)](https://aidevme.com/power-apps-mcp-server-complete-guide/ "Power Apps MCP Server: Complete Guide to Every Feature (Public Preview 2026)")

The Power Apps MCP (Model Context Protocol) Server is now in public preview. It exposes three tools — invoke\_data\_entry, request\_assistance, and log\_for\_review — that let AI agents automate tasks inside model-driven apps with built-in human supervision via a redesigned agent feed. This guide covers every feature, technical detail, current limitation,…

February 21, 2026

In "AI & Copilot"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [Under the Hood: How Dataverse Skills Work and How to Write Your Own](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/)