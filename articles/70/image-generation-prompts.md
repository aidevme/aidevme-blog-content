# Image Generation Prompts — Article 70
# Think Before You Build: GitHub Copilot's Plan Agent in Visual Studio — Structured AI-Assisted Development

---

## 1. Featured Image

**File name:** `github-copilot-plan-agent-visual-studio-featured.png`

**Alt text:** GitHub Copilot Plan agent in Visual Studio — structured AI-assisted development with a Markdown plan reviewed before code generation

**Description:** Featured image for the article introducing GitHub Copilot's Plan agent in Visual Studio. Should convey the idea of deliberate, structured AI planning — a blueprint being reviewed before construction begins. Displayed at 1200×628 (social/OG) and as the WordPress featured image at the top of the post.

**Generation prompt:**
Dark-background tech illustration. A large Markdown document floats in the center of the frame, its text rendered as clean glowing white lines — the visible structure resembles a numbered step list with section headings and file paths. A GitHub Copilot logo (the circular silhouette) hovers above-left of the document, casting a soft blue glow over it. A translucent approval checkmark overlays the bottom-right corner of the document, glowing green — suggesting human review and sign-off. In the background, faint code files and folder structures are visible but blurred, representing the codebase being scanned. A thin horizontal dividing line separates the upper "Plan" half from a lower "Implement" half, with the lower half slightly dimmer to suggest it hasn't started yet. Color palette: near-black (#0d1117), electric blue (#4361ee), soft teal (#00b4d8), approval green (#2ea043). Flat vector with soft glow halos. No readable text except stylised structural fragments.

---

## 2. The Problem With "Just Build It"

**File name:** `github-copilot-agent-mode-uncontrolled-changes.png`

**Alt text:** GitHub Copilot Agent mode modifying multiple files unpredictably — illustrating the problem of jumping straight to implementation without a plan

**Description:** Illustrates the core problem the article addresses: Agent mode diving straight into implementation and modifying many files in unpredictable directions. Used at the start of the problem statement section to make the pain point visually tangible before the solution is introduced.

**Generation prompt:**
Dark tech illustration conveying chaos and scope creep. A developer's IDE window shows twelve file tabs open simultaneously, each with a red-orange "modified" dot. Overlapping arrows in amber and red radiate outward from a central Copilot chat bubble, each arrow pointing to a different file — `ServiceLayer.cs`, `DI.cs`, `appsettings.json`, `WebhookController.cs`, etc. — all highlighted as being touched. A large red warning triangle sits at the top-right of the frame. The overall impression is of uncontrolled change spreading across a codebase. Background: near-black. Accent colors: amber (#f4a261), alert red (#e63946), muted white for file tabs. Flat vector style with sharp contrast between the chaos arrows and the calm dark background.

---

## 3. How the Plan Agent Works: Step by Step

**File name:** `github-copilot-plan-agent-five-phase-workflow.png`

**Alt text:** The five-phase workflow of GitHub Copilot's Plan agent — Describe, Scan, Draft, Edit, Implement

**Description:** Illustrates the complete five-phase pipeline of the Plan agent: Describe Intent → Scan Codebase (read-only) → Draft Plan → Edit Plan → Implement. Used at the start of the workflow section to give readers a single-glance mental model before each phase is explained.

**Generation prompt:**
Dark tech illustration. A horizontal five-step pipeline flows left to right across the center of the frame. Each step is a rounded pill or card connected by a glowing teal arrow. Step 1: a speech bubble icon labeled "Describe" (soft blue). Step 2: a magnifying glass over a folder tree labeled "Scan" (read-only, shown with a lock icon, soft purple). Step 3: a Markdown document icon labeled "Draft" (teal). Step 4: a pencil-on-document icon labeled "Edit" (amber). Step 5: a play-button / gear icon labeled "Implement" (electric blue). Each card glows with its own hue. The step numbers 1–5 appear as small circles above each card. Below the pipeline, a faint "no file changes" label sits under steps 1–4, and a "files modified" label appears under step 5, using a green checkmark. Background: near-black. Flat vector pipeline diagram style.

---

## 4. Phase 2 — Copilot Scans Your Codebase (Read-Only)

**File name:** `github-copilot-plan-agent-read-only-codebase-scan.png`

**Alt text:** GitHub Copilot Plan agent scanning a Power Platform solution in read-only mode — project structure, DI configuration, and interface definitions

**Description:** Illustrates the read-only codebase scanning phase where Copilot examines project structure, service registrations, interfaces, config files, and NuGet references — without making any changes. Used at the start of Phase 2 to reassure readers that nothing is modified during this phase.

**Generation prompt:**
Dark tech illustration. A large folder tree diagram fills the left half of the frame — showing a Power Platform solution structure with `Plugins/`, `Services/`, `appsettings.json`, and `.csproj` files. Scanning beams (thin horizontal lines) sweep across the tree from left to right, each illuminating a node in soft blue as the scan passes over it. A GitHub Copilot logo silhouette sits on the right side, its "eyes" or glow directed at the folder tree. Crucially, a large padlock icon overlays the bottom-left of the folder tree with a "read-only" label — emphasising no writes occur. Background: deep navy. Color palette: electric blue for scan beams, teal for highlighted nodes, soft white for folder tree structure. Flat vector style.

---

## 5. Phase 3 — The Plan Is Drafted

**File name:** `github-copilot-plan-agent-markdown-plan-output.png`

**Alt text:** GitHub Copilot Plan agent producing a Markdown implementation plan — goals, affected files, and numbered steps saved to the .copilot/plans/ folder

**Description:** Illustrates the output of the Plan agent's drafting phase: a rich Markdown document with sections for Goal, Affected Files, Steps, Out of Scope, and Open Questions — persisted to the `.copilot/plans/` folder. Used at the start of Phase 3 to give readers a concrete preview of what a plan looks like.

**Generation prompt:**
Dark tech illustration. A Markdown editor window dominates the center of the frame, displaying a structured document with glowing section headings: "# Plan", "## Goal", "## Affected Files", "## Steps", "## Out of Scope". The section headings glow in teal; bullet points and numbered steps are in soft white. A file path badge at the top of the window reads `.copilot/plans/plan-accountsync-refactor.md` in small type. A GitHub Copilot logo silhouette appears in the top-left corner with a subtle glow, suggesting it authored the document. A faint "Step 1 → Step 2 → Step 3" progression indicator runs along the bottom of the document. Background: near-black. Flat vector with a realistic code-editor aesthetic — rounded window chrome, a tab bar. Color palette: teal, electric blue, soft amber for emphasis.

---

## 6. Phase 4 — You Edit the Plan Directly

**File name:** `github-copilot-plan-agent-edit-markdown-plan.png`

**Alt text:** Developer editing a GitHub Copilot Markdown plan directly in the Visual Studio editor — adding constraints and modifying steps before implementation

**Description:** Illustrates the human-in-the-loop editing phase where the developer edits the generated Markdown plan like any other file — adding constraints, removing steps, changing file paths — before approving it for implementation. Used at the start of Phase 4 to emphasise developer control and the editing workflow.

**Generation prompt:**
Dark tech illustration. A code editor window on the left shows a Markdown plan file open for editing — a cursor is actively positioned mid-document near a comment block reading "<!-- CONSTRAINT: ... -->". On the right, a simplified Git commit panel shows the plan file staged for commit, with a small PR icon above suggesting the plan will be reviewed. A hand cursor icon (or stylised developer avatar silhouette) interacts with the document, emphasising human control. A pair of scissors / edit icon overlays the top of the plan document suggesting active modification. Background: near-black. Color palette: amber (#f4a261) for the cursor and active edit state, teal for the plan document header, electric blue for the Git/PR panel. Flat vector with editor window chrome.

---

## 7. Phase 5 — Implement

**File name:** `github-copilot-plan-agent-implement-approved-plan.png`

**Alt text:** GitHub Copilot Agent mode executing an approved Markdown plan — creating and modifying files step by step after human approval

**Description:** Illustrates the implementation phase where Agent mode executes the approved plan — showing files being created and modified step by step with visible progress. Used at the start of Phase 5 to make the transition from planning to execution visually distinct and to reinforce that human approval preceded this phase.

**Generation prompt:**
Dark tech illustration. A Markdown plan document on the left displays checked-off numbered steps — Step 1 ✓ (green), Step 2 ✓ (green), Step 3 (in progress, pulsing amber). An arrow flows rightward from the plan to a file explorer panel on the right, where new file nodes appear lit up in green: `AccountSyncService.cs`, `IAccountSyncService.cs`, `AccountSyncServiceTests.cs`. A progress bar runs horizontally below both panels, partially filled in teal, showing overall completion. A green "Approved" badge sits at the top-left of the plan document. The GitHub Copilot logo appears above the arrow — it is executing, not planning. Background: near-black. Color palette: teal for progress, green for completed items, amber for the active step. Flat vector style with subtle animation-suggestion effects.

---

## 8. Writing Better Prompts for the Plan Agent

**File name:** `github-copilot-plan-agent-prompt-patterns.png`

**Alt text:** Four prompt patterns for GitHub Copilot's Plan agent — scope by layer, reference existing patterns, specify test coverage, use constraints

**Description:** Illustrates the four prompt-writing patterns covered in the section: scope by layer, reference existing patterns, specify test coverage, and use constraints to protect sensitive areas. Used at the start of the section to give a quick visual summary of the four strategies.

**Generation prompt:**
Dark tech illustration. Four prompt-pattern cards arranged in a 2×2 grid. Each card has a bold number (1–4), a small icon, and a short label. Card 1: a stack of layers icon + "Scope by Layer" (blue). Card 2: a copy/reference icon + "Reference Existing Patterns" (teal). Card 3: a test-tube or checkmark icon + "Specify Test Coverage" (green). Card 4: a padlock icon + "Use Constraints" (amber). Each card is separated by a thin glowing border, and each icon pulses with its accent color. A faint chat bubble in the background suggests these are prompt strategies. Background: near-black with a subtle grid. Flat vector card-grid style.

---

## 9. A Real-World Scenario: Power Platform Plugin Refactor

**File name:** `github-copilot-plan-agent-dataverse-plugin-refactor.png`

**Alt text:** Before and after GitHub Copilot Plan agent refactoring a Dataverse plugin — monolithic Execute method extracted into a testable service class

**Description:** Illustrates the before-and-after transformation of a Dataverse plugin: a monolithic `IPlugin.Execute` method on the left versus a thin orchestrator plugin + testable `AccountSyncService` on the right. Used at the start of the scenario section to anchor the code examples with a clear architectural visual.

**Generation prompt:**
Dark tech illustration. A split-screen layout divided by a vertical glowing arrow pointing right. Left side (labeled "Before" in muted red): a single large `AccountSyncPlugin.cs` file icon, with a tall code block inside it suggesting 200+ lines — the block is dense and orange-tinted to convey complexity and risk. Right side (labeled "After" in green): three smaller file icons arranged vertically — `AccountSyncPlugin.cs` (small, thin), `AccountSyncService.cs` (medium), `AccountSyncServiceTests.cs` (medium, with a test-tube icon) — each glowing in teal or green. A Moq mock icon or test-beaker symbol appears next to the tests file. The arrow between the sides is labeled "Plan agent" in small teal text. Background: near-black. Flat vector style with clear size contrast between the monolithic before and modular after.

---

## 10. The Plan File as a Living Document

**File name:** `github-copilot-plan-agent-living-document-decision-log.png`

**Alt text:** The .copilot/plans/ folder as a team decision log — Markdown plan files with status frontmatter committed alongside code

**Description:** Illustrates the `.copilot/plans/` folder serving as a lightweight architectural decision log over time, with multiple committed plan files annotated with status, author, and PR references in YAML frontmatter. Used in the "Living Document" section to help readers visualise the long-term team value of persisting plans.

**Generation prompt:**
Dark tech illustration. A folder tree on the left shows `.copilot/plans/` expanded with four Markdown files listed below it — `plan-accountsync-refactor.md` (green checkmark: completed), `plan-jwt-auth-middleware.md` (green checkmark: completed), `plan-bulk-import-pipeline.md` (amber clock: in progress), `plan-power-pages-auth-redesign.md` (blue circle: under review). Each file icon has a subtle status badge. A zoomed tooltip panel floats to the right of one file, showing its YAML frontmatter: `status: completed`, `pr: #142`, `author: zsolt` — rendered as clean monospaced text. A faint Git branch diagram sits in the background, suggesting these files are committed to version control. Background: near-black. Color palette: teal for folder and file nodes, green/amber/blue for status badges. Flat vector style.

---

## 11. Where This Fits in Your Development Loop

**File name:** `github-copilot-plan-agent-development-pipeline.png`

**Alt text:** GitHub Copilot Plan agent positioned in the full enterprise development pipeline — from design through ALM deployment

**Description:** Illustrates the full development pipeline from the article's diagram section: Plan agent → Agent mode / Copilot → Solution Checker → Unit Tests / CI → PR Review → ALM pipeline / PAC CLI deploy. Used to give readers a high-level mental model of where planning fits relative to the full delivery pipeline.

**Generation prompt:**
Dark tech illustration. A vertical pipeline flows top to bottom through the center of the frame. Each stage is a pill-shaped node connected by a glowing teal line with a downward arrow. Stage 1: "Plan agent" — highlighted in bright teal with a document icon, indicating it is the focus of the article. Stage 2: "Agent mode / Copilot" — electric blue, gear icon. Stage 3: "Solution Checker" — purple, shield icon. Stage 4: "Unit Tests / CI" — green, test-tube icon. Stage 5: "PR Review" — amber, magnifying-glass icon. Stage 6: "PAC CLI Deploy" — soft blue, rocket/deploy icon. Stage 1 glows notably brighter than the others, drawing the eye. Faint Power Platform and GitHub logos appear as watermarks behind the pipeline. Background: near-black. Flat vector pipeline diagram.

---
