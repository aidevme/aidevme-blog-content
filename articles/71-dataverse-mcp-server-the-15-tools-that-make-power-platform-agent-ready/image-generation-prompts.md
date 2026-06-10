# Image Generation Prompts — Article 71
# Dataverse MCP Server: The 15 Tools That Make Power Platform Agent-Ready

---

## 1. Featured Image

**File name:** `dataverse-mcp-server-15-tools-power-platform-featured.png`

**Alt text:** Dataverse MCP server — 15 named tools giving AI agents grounded, auditable access to Power Platform data

**Description:** Featured image for the article introducing the Dataverse MCP server tool shape. Should convey the idea of a structured, trusted contract between an AI agent and an enterprise data platform — precision and governance rather than chaos. Displayed at 1200×628 (social/OG) and as the WordPress featured image at the top of the post.

**Generation prompt:**
Dark-background tech illustration. A large hexagonal hub glows in the center of the frame — inside it, a stylised Power Platform logo (abstract diamond shape) pulses in soft teal. From the hub, fifteen thin glowing connector lines radiate outward in a sunburst pattern, each terminating in a small rounded pill labeled with a tool name: `search`, `describe`, `read_query`, `create_record`, `delete_record`, etc. The pills are color-coded by risk tier: soft blue for read-only tools, amber for write tools, deep red-orange for the two destructive tools (`delete_record`, `delete_table`). A faint padlock icon overlays the hub, suggesting governance and access control. In the background, blurred code fragments and folder trees represent the live codebase being accessed. Color palette: near-black (#0d1117), teal (#00b4d8), electric blue (#4361ee), amber (#f4a261), alert red (#e63946). Flat vector with soft glow halos. No readable text except the stylised tool name pills.

---

## 2. The Grounding Problem, Solved Structurally

**File name:** `dataverse-mcp-server-agent-grounding-schema-discovery.png`

**Alt text:** AI agent calling Dataverse MCP search and describe tools to inspect live schema before generating code — solving the hallucination problem

**Description:** Illustrates the core grounding loop: an agent calling `search` and `describe` against the live Dataverse environment to orient itself before acting, contrasted with a ghost/faded agent on the left making confident but wrong assumptions. Used at the start of the grounding section to make the inspect-first pattern visually concrete.

**Generation prompt:**
Dark tech illustration. Split composition. Left half (labeled "Without MCP" in muted red): a stylised AI agent silhouette surrounded by faint ghost-text hallucinations — column names in red strikethrough, a FetchXML fragment with a warning icon, a table name that doesn't exist. The overall impression is of a confident agent working from fiction. Right half (labeled "With MCP" in teal): the same agent silhouette, now connected to a live database cylinder via two glowing call lines labeled `search` and `describe`. The returned schema blocks glow in clean white — real column names, real types, real relationships. A small green checkmark appears above the schema. A thin vertical dividing line separates the two halves. Background: near-black. Accent colors: teal and electric blue for the right side, muted red and amber for the left. Flat vector style.

---

## 3. Three Tiers of Risk, Three Tiers of Control

**File name:** `dataverse-mcp-server-tool-risk-tiers.png`

**Alt text:** Three risk tiers of Dataverse MCP server tools — read-only, write, and destructive — with color-coded access control visualization

**Description:** Illustrates the three-tier risk model for the 15 tools: read-only tools (blue), write tools (amber), and destructive tools (red) with explicit approval gates. Used at the start of the risk tiers section to give readers a single-glance mental model before each tier is analyzed.

**Generation prompt:**
Dark tech illustration. Three horizontal stacked bands fill the frame, each representing a risk tier. Top band (blue, labeled "Read-Only"): five rounded pill badges — `search`, `describe`, `read_query`, `search_data`, `file_download` — arranged in a row, glowing soft blue. A small eye icon appears at the left edge. Middle band (amber, labeled "Write"): seven pill badges — `create_record`, `update_record`, `create_table`, `update_table`, `upsert_skill`, `init_file_upload`, `commit_file_upload` — glowing amber. A small pencil icon at the left. Bottom band (deep red-orange, labeled "Destructive"): three pill badges — `delete_record`, `delete_table`, `delete_skill` — glowing red-orange. Each destructive pill has a small padlock icon attached, and a "⚠ Approval Required" label floats beside `delete_record` and `delete_table`. The bands are separated by thin glowing divider lines. Background: near-black. Flat vector style with clear visual weight hierarchy — blue lightest, red heaviest.

---

## 4. What the File Tools Actually Enable

**File name:** `dataverse-mcp-server-file-upload-download-workflow.png`

**Alt text:** Dataverse MCP server file handling workflow — SAS URL generation, direct Azure Blob transfer, and commit registration

**Description:** Illustrates the three-step file handling pattern: `init_file_upload` issues a SAS URL, the file transfers directly to Azure Blob storage, then `commit_file_upload` registers it in Dataverse. The MCP server is shown as an orchestrator, not a data carrier. Used in the file tools section to make the architectural split between protocol and data path visually clear.

**Generation prompt:**
Dark tech illustration. A horizontal three-step flow diagram across the center of the frame. Step 1 (left): a client/agent node sends a request arrow to a small MCP server node labeled "init_file_upload" — the server returns a glowing "SAS URL" token. Step 2 (center): a large curved arrow bypasses the MCP server entirely, going directly from the client to an Azure Blob storage cylinder — the arrow is labeled "direct transfer" in small teal text. Step 3 (right): another arrow goes from the client to the MCP server node labeled "commit_file_upload" — a small Dataverse logo receives a confirmation tick. The MCP server node is visually smaller than the storage cylinder, reinforcing that it orchestrates but doesn't carry bytes. A faint "No file bytes through MCP" annotation appears below the server node in muted text. Background: near-black. Color palette: teal for data flow arrows, electric blue for the MCP node, soft white for storage. Flat vector style.

---

## 5. Skills: The Self-Extending Agent

**File name:** `dataverse-mcp-server-skills-upsert-playbook-discovery.png`

**Alt text:** Dataverse Skills as discoverable agent playbooks — upsert_skill adding tribal knowledge to the environment, search surfacing it to other agents

**Description:** Illustrates the self-extending Skills loop: a developer upserts a skill into Dataverse, which then becomes discoverable by other agents via the `search` tool. Contrasts the "knowledge in Confluence pages" problem with the "knowledge in Dataverse as a skill" solution. Used in the Skills section to make the feedback loop concrete.

**Generation prompt:**
Dark tech illustration. A circular feedback loop dominates the frame. At the top: a developer avatar at a VS Code terminal sends an upward arrow labeled `upsert_skill` to a Dataverse cylinder in the center. Inside the cylinder, a small glowing document icon represents the stored skill playbook. At the bottom: two separate agent silhouettes send query arrows labeled `search` toward the same cylinder, and receive glowing document responses back — suggesting multiple agents independently discovering the same skill. A faint Confluence/wiki page icon on the far left is crossed out with a soft red X, contrasted with the teal Dataverse cylinder — representing the shift from implicit to explicit knowledge. Color palette: teal for the Dataverse cylinder and active flows, soft blue for agent silhouettes, amber for the developer. Background: near-black. Flat vector style with circular flow arrows.

---

## 6. Connecting from Claude Code, VS Code, and Copilot Studio

**File name:** `dataverse-mcp-server-client-allowlisting-admin-center.png`

**Alt text:** Power Platform admin center client allowlisting for Dataverse MCP server — enabling GitHub Copilot, Claude, and Copilot Studio per environment

**Description:** Illustrates the client allowlisting configuration: multiple AI clients (VS Code, Claude, Copilot Studio) attempting to connect to a Dataverse MCP endpoint, with the Power Platform admin center governing which clients are permitted per environment. Used in the connecting section to show the governance layer between clients and the endpoint.

**Generation prompt:**
Dark tech illustration. A vertical stack of three client logos on the left — a VS Code icon, a Claude silhouette, and a Copilot Studio icon — each connected by an arrow pointing right toward a central Dataverse MCP endpoint node (a teal hexagon). Between the clients and the endpoint, a tall vertical barrier labeled "Power Platform Admin Center" acts as a gate. The VS Code and Copilot Studio arrows pass through glowing green checkmark openings in the barrier. The Claude arrow hits a soft amber "pending" gate — suggesting it requires explicit activation. Below the barrier, a small "Managed Environment required" label glows in soft blue. The Dataverse endpoint node sits to the right of the barrier, with a faint OrgName URL fragment beneath it. Background: near-black. Color palette: teal for the endpoint, green for permitted clients, amber for pending, soft blue for labels. Flat vector with clean gate/barrier metaphor.

---

## 7. Writing Agent Instructions That Actually Work

**File name:** `dataverse-mcp-server-agent-instructions-structure.png`

**Alt text:** Structured Dataverse agent instructions showing Role, Objective, MCP tool selection, and Reasoning sections in a VS Code editor

**Description:** Illustrates the four-section structure of effective Dataverse agent instructions: Role, Objective, MCP tool selection, and Reasoning. Shows the instructions as a Markdown document open in a VS Code editor, with key phrases highlighted. Used at the start of the agent instructions section to give readers a visual anchor for the code sample that follows.

**Generation prompt:**
Dark tech illustration. A VS Code editor window dominates the frame, displaying a Markdown document with four clearly visible section headings glowing in teal: "## Role", "## Objective", "## MCP tool selection instructions", "## Reasoning instructions". Each heading has a two-line text preview beneath it in soft white monospace text. Two specific phrases are highlighted in amber as if selected: "list_tables" in the tool selection section, and "think out loud" in the reasoning section — emphasising the most important behavioral directives. A VS Code tab bar appears at the top showing a filename like `copilot-instructions.md`. A faint GitHub Copilot logo appears in the top-right corner of the editor window, suggesting the instructions are active. Background: near-black editor chrome. Color palette: teal for headings, amber for key phrases, soft white for body text. Flat vector with realistic editor chrome.

---

## 8. The Billing Dimension

**File name:** `dataverse-mcp-server-billing-copilot-credits-model.png`

**Alt text:** Dataverse MCP server billing model — Copilot Credits per tool call, with Dynamics 365 Premium and Microsoft 365 Copilot license exemptions

**Description:** Illustrates the two-track billing model: most tool calls consume Copilot Credits (with `search` at the Graph Grounding rate and all others at the basic rate), while Dynamics 365 Premium and Microsoft 365 Copilot licenses bypass billing entirely. Used in the billing section to make the cost model scannable at a glance.

**Generation prompt:**
Dark tech illustration. A horizontal split layout. Left side: a credit counter icon (coins or tokens) with two stacked rows — Row 1 shows the `search` tool pill with a higher credit rate label (Tenant Graph Grounding); Row 2 shows all other tool pills grouped together with a lower credit rate label (Text and Gen AI basic). Small downward arrows show credits being deducted per call. Right side (separated by a vertical glowing green dividing line): two license badge icons — a Dynamics 365 diamond logo and a Microsoft 365 Copilot logo — each with a large green "∅ No credits" badge beneath them, indicating exemption. A small asterisk footnote at the bottom reads "From Dec 15, 2025" in muted text. Background: near-black. Color palette: amber for credit consumption, green for exemption, teal for license badges. Flat vector style.

---

## 9. Security and Governance Analysis

**File name:** `dataverse-mcp-server-security-governance-layers.png`

**Alt text:** Dataverse MCP server security layers — Entra ID authentication, Dataverse RBAC, client allowlisting, and audit logging stacked as a governance model

**Description:** Illustrates the four security and governance layers that protect a Dataverse MCP deployment: Entra ID (identity), client allowlisting (client authorization), Dataverse security roles (data access), and audit logging (visibility). Used at the start of the security section to give readers a layered mental model before each layer is analyzed in depth.

**Generation prompt:**
Dark tech illustration. A tall vertical stack of four shield-shaped layers, each slightly larger than the one above — like nested defence rings. Layer 1 (outermost, darkest): labeled "Client Allowlisting" with a Power Platform admin center icon — only approved AI client logos appear on the permitted side. Layer 2: labeled "Entra ID Authentication" with a Microsoft Entra logo — a token/key icon and a Conditional Access symbol. Layer 3: labeled "Dataverse Security Roles" with a table-and-lock icon — RBAC rows suggesting granular privilege control. Layer 4 (innermost, brightest): labeled "Audit Log" with a log/scroll icon — a timeline of auditable events. A small red warning badge floats at the top-right of the stack labeled "Read ops not logged" — flagging the audit gap. Each layer glows with a progressively brighter teal hue toward the center. Background: near-black. Flat vector with nested shield motif.

---

## 10. What This Changes for Power Platform Architects

**File name:** `dataverse-mcp-server-architect-impact-three-shifts.png`

**Alt text:** Three architectural shifts from the Dataverse MCP server — deliberate agent design, shorter development loop, and platform-level governance enforcement

**Description:** Illustrates the three concrete architectural changes the article argues result from the MCP tool shape formalization: (1) agent integration as a deliberate design decision, (2) compressed development loop through live schema access, and (3) governance enforceable at the platform layer. Used in the architects section to summarize the key takeaways visually.

**Generation prompt:**
Dark tech illustration. Three vertical cards arranged side by side, each representing one architectural shift. Card 1 (left, blue): a blueprint/architecture diagram icon with the label "Design Deliberately" — suggesting intentional, structured agent permission design. Card 2 (center, teal): a circular dev loop arrow (write → deploy → test → debug) with a compression indicator showing the loop getting smaller — labeled "Shorter Dev Loop". Card 3 (right, electric blue): a platform stack with a shield icon at the base and "Platform Governance" label — suggesting enforcement at the infrastructure layer rather than just the prompt layer. Each card has a bold number (1, 2, 3) in the top-left corner and a thin glowing border matching its accent color. Below the three cards, a single line of text reads: "The 15 tools are the foundation." in soft white. Background: near-black with a subtle grid. Flat vector card-grid style.

---
