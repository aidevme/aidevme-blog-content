# Image Generation Prompts — Article 72
# GitHub Copilot Code Reviews Are Coming to Azure Repos — What It Means for Power Platform Teams

---

## 1. Featured Image

**File name:** `github-copilot-code-review-azure-repos-featured.png`

**Alt text:** GitHub Copilot code review inside an Azure Repos pull request — AI reviewer posting inline comments alongside human reviewers

**Description:** Featured image for the article covering GitHub Copilot code review entering limited public preview for Azure Repos. Should convey the idea of AI-assisted peer review landing directly inside the Azure DevOps pull request experience — familiar workflow, new AI participant. Displayed at 1200×628 (social/OG) and as the WordPress featured image at the top of the post.

**Generation prompt:**
Dark-background tech illustration. A pull request diff view fills most of the frame — two columns of code, with line numbers in soft grey and changed lines highlighted in subtle green/red. On the right side of the PR, a reviewer panel shows two entries: a human avatar (faint silhouette, initials "SR") and directly below it a glowing GitHub Copilot logo — the Copilot entry is highlighted with a teal ring, suggesting it is the active reviewer. A single inline comment bubble floats over a changed line of code: the bubble has the Copilot logo and contains a short code suggestion in monospace. A faint Azure DevOps header bar runs across the top, with "Pull Requests" breadcrumb in muted white. No readable code content — code lines are impressionistic monospace fragments. Color palette: near-black (#0d1117), Azure blue (#0078d4), teal (#00b4d8), soft white for text, muted green/red for diff lines. Flat vector with subtle glow on the Copilot reviewer entry.

---

## 2. The Context: Why This Matters More Than It Looks

**File name:** `github-copilot-code-review-azure-repos-context-enterprise-migration.png`

**Alt text:** Enterprise organizations anchored to Azure DevOps while GitHub AI tooling advances — illustrating the migration drag that makes this announcement significant

**Description:** Illustrates the tension at the heart of the article's context: GitHub is where AI tooling ships first, but enterprise organizations are anchored to Azure DevOps by compliance, branching strategies, and integration dependencies. Used to frame why bringing Copilot code review to Azure Repos is a meaningful signal rather than a minor feature update.

**Generation prompt:**
Dark tech illustration. A horizontal tug-of-war composition. On the left: a cluster of Azure DevOps / enterprise elements — a compliance shield, a branching pipeline diagram, an identity federation icon, a ticketing integration icon — all grouped around a large "Azure DevOps" text badge in Azure blue. On the right: a cluster of GitHub AI elements — a GitHub Octocat outline, a Copilot sparkle icon, a code suggestion bubble — grouped around a "GitHub" badge in soft white. Between the two clusters, a thick glowing rope stretches taut, anchoring both sides. A small announcement ribbon banner floats above the center of the rope labeled "Preview Now Available" in teal — suggesting the rope has just relaxed slightly. Background: near-black. Color palette: Azure blue (#0078d4) for the left cluster, soft white and teal for the right, amber for the rope anchor points. Flat vector with subtle tension metaphor.

---

## 3. What Was Announced

**File name:** `github-copilot-code-review-azure-repos-pr-reviewers-panel.png`

**Alt text:** Developer requesting a Copilot code review from the Azure Repos pull request Reviewers section — same UX as requesting a human reviewer

**Description:** Illustrates the core UX of the announcement: a developer clicking "Request review" in a pull request's Reviewers panel and selecting GitHub Copilot alongside human teammates. The review then runs asynchronously and posts inline comments. Used to make the feature's simplicity and familiarity concrete for readers who haven't seen the preview yet.

**Generation prompt:**
Dark tech illustration. A zoomed-in Azure Repos pull request panel. The "Reviewers" section is in focus — showing two entries already added (two human avatar silhouettes with initials) and a third entry being added: a dropdown search box shows "GitHub Copilot" as the top autocomplete result, with the Copilot glowing teal logo to its left. A cursor arrow hovers over the Copilot entry. Below the reviewers panel, a status badge reads "Review completed" with a soft teal checkmark. A single inline comment thread is visible in the diff below — the thread starter is the Copilot logo with a short suggestion in monospace. The surrounding PR chrome (tabs, breadcrumbs) is Azure blue. Background: near-black. Color palette: Azure blue for chrome, teal for Copilot elements, soft white for text. Flat vector with realistic PR panel proportions.

---

## 4. Setup: Three Layers of Enablement

**File name:** `github-copilot-code-review-azure-repos-three-tier-setup.png`

**Alt text:** Three-tier enablement model for GitHub Copilot code review in Azure Repos — organization, repository, and user level settings

**Description:** Illustrates the three-level configuration model: organization admin enables the feature globally, repository admin enables it per repo, and individual users toggle it in Preview Features. Used to give readers a visual overview of the admin hierarchy before the step-by-step setup instructions.

**Generation prompt:**
Dark tech illustration. A top-down hierarchy of three nested rounded rectangles, each slightly smaller and centered inside the previous one — like a bullseye. Outermost rectangle (labeled "Organization" in Azure blue): an org administrator silhouette icon with a settings gear and a glowing toggle switch labeled "Enable Copilot Code Review." Middle rectangle (labeled "Repository" in teal): a repository folder icon and a list of two repository names — one with a green checkmark (enabled), one with a grey dash (not yet enabled). Innermost rectangle (labeled "User" in electric blue): a single user avatar and a "Preview Features" toggle in the on position. Thin connecting arrows flow downward between each layer, labeled "unlocks." Background: near-black. Color palette: Azure blue → teal → electric blue following the hierarchy depth. Flat vector nested-layer style.

---

## 5. Preview Limits Worth Knowing

**File name:** `github-copilot-code-review-azure-repos-preview-limits.png`

**Alt text:** GitHub Copilot code review preview constraints — repository size, file count, concurrency limits, and PR state requirements visualized

**Description:** Illustrates the seven preview constraints in a scannable visual format: repository size cap, files-per-PR limit, active PR state requirement, no-conflict requirement, one review per merge commit, and concurrency limits at org and user level. Used alongside the reference table to help readers quickly assess whether the preview will work for their scenario.

**Generation prompt:**
Dark tech illustration. A grid of seven constraint tiles arranged in two rows (4 top, 3 bottom), each tile a small rounded card on a near-black background. Each card shows: a small icon on the left (database cylinder, file stack, PR status badge, merge arrows, repeat arrow, organization nodes, user avatar), a bold constraint value in teal in the center (10 GB, 100 files, Active, No conflicts, 1 per commit, 5 orgs, 2 users), and a small grey label below (Repository size, Changed files, PR state, Merge status, Reviews/version, Concurrent/org, Concurrent/user). The cards have thin electric blue borders. One card — "Must be Active" — has a slightly brighter teal glow to indicate it's the most commonly hit gate. Background: near-black grid. Color palette: teal for values, soft white for labels, electric blue for borders. Flat vector card-grid style.

---

## 6. Billing: AI Credits on Your Azure Subscription

**File name:** `github-copilot-code-review-azure-repos-billing-ai-credits.png`

**Alt text:** GitHub Copilot code review billing — AI credits on Azure subscription at $0.01 per credit, visible in Azure Cost Management

**Description:** Illustrates the billing flow: code review activity generates token consumption, tokens convert to GitHub AI credits at $0.01 each, and the charge surfaces in Azure Cost Management under the linked Azure subscription. Used in the billing section to make the cost model concrete and flag the need for a cost alert.

**Generation prompt:**
Dark tech illustration. A three-step horizontal flow. Step 1 (left): a pull request diff icon with a "Review requested" arrow — representing the trigger event. Step 2 (center): a token counter spinning upward with a conversion label "1 credit = $0.01 USD" — a GitHub AI credit coin icon in amber. Step 3 (right): an Azure Cost Management dashboard fragment showing a new line item "GitHub AI Credits" with a small bar chart and a cost alert bell icon highlighted in teal — suggesting the monitoring setup. Thin connecting arrows labeled "consumes" and "billed to Azure subscription" flow between steps. A small "Preview — variable cost" label floats below the token counter in muted amber. Background: near-black. Color palette: teal for the flow arrows, amber for the credit coin, Azure blue for the Cost Management fragment. Flat vector style.

---

## 7. What This Means for Power Platform ALM Workflows

**File name:** `github-copilot-code-review-azure-repos-power-platform-alm.png`

**Alt text:** GitHub Copilot code review applied to Power Platform ALM — Dataverse plugins and PCF controls reviewed, Power Automate flows and canvas YAML outside scope

**Description:** Illustrates which parts of a Power Platform ALM workflow are in scope for Copilot code review (C# plugins, TypeScript PCF controls) and which are explicitly out of scope (Power Automate flow JSON, canvas app YAML). Used to set accurate expectations and prevent teams from expecting AI review coverage they won't get.

**Generation prompt:**
Dark tech illustration. A Power Platform solution stack as a vertical column of labeled layers. Top layers (glowing teal, labeled "In Scope"): a C# file icon labeled "Dataverse Plugins" with a Copilot review bubble beside it, and a TypeScript/React file icon labeled "PCF Controls" with another review bubble. Bottom layers (muted grey, labeled "Out of Scope"): a JSON flow diagram icon labeled "Power Automate Flows" with a soft X badge, and a canvas app YAML icon labeled "Canvas App Source" with a soft X badge. A vertical dotted dividing line labeled "AI Review Boundary" separates the two zones. A small annotation beside the out-of-scope layers reads "Declarative layer — not yet supported" in muted text. Background: near-black. Color palette: teal for in-scope layers, muted grey for out-of-scope, soft white for labels. Flat vector with clear zone separation.

---

## 8. How to Sign Up

**File name:** `github-copilot-code-review-azure-repos-preview-signup.png`

**Alt text:** GitHub Copilot code review Azure Repos preview sign-up — selective onboarding with telemetry monitoring before broader rollout

**Description:** Illustrates the preview sign-up process: an organization submits a request form, Microsoft reviews telemetry and onboards selectively, and approved organizations receive enablement confirmation. Used to make the sign-up path clear and frame the selective rollout as a quality gate rather than a barrier.

**Generation prompt:**
Dark tech illustration. A three-stage pipeline flowing left to right. Stage 1 (left): an organization admin avatar fills out a sign-up form — a simple web form with an "Organization Name" field and a "Submit" button glowing in teal. Stage 2 (center): a Microsoft review node — a shield/checkmark icon with a "Selective Onboarding" label and a soft amber "Reviewing" status badge, suggesting evaluation in progress. Stage 3 (right): an Azure DevOps repository panel with the Copilot code review toggle now illuminated green and an "Enabled" confirmation badge. Thin arrows labeled "Submit request" and "Enablement confirmed" connect the stages. A small "~2 months preview" timeline label floats below the pipeline. Background: near-black. Color palette: teal for the submit action, amber for the review stage, green for enablement. Flat vector pipeline style.

---

## 9. My Take

**File name:** `github-copilot-code-review-azure-repos-architect-recommendation.png`

**Alt text:** Power Platform architect recommendation — enable GitHub Copilot code review on plugin and PCF repositories, build into PR process for code-heavy components

**Description:** Illustrates the practical recommendation from the article's closing section: a Power Platform architect approving the rollout of Copilot code review on two specific repository types (plugins, PCF controls), with an explicit scope boundary around solution exports and declarative components. Used as a visual summary of the "My Take" section that readers can reference when making their own rollout decision.

**Generation prompt:**
Dark tech illustration. A decision card layout — a central architect avatar silhouette with a checkmark approval gesture. Two repository cards on the left are highlighted with green "Enable" badges: one labeled "Dataverse Plugins (C#)" and one labeled "PCF Controls (TypeScript/React)". Two repository cards on the right are marked with grey "Exclude for now" badges: one labeled "Solution Exports (XML)" and one labeled "Canvas App YAML". Thin lines connect the architect avatar to each card, with green lines to the left cards and grey dashed lines to the right. A single recommendation sentence appears below the architect: "Catch issues that slow review cycles. Keep architectural review human." in soft white italic. Background: near-black. Color palette: teal for the architect node, green for recommended repos, grey for excluded, soft white for text. Flat vector with balanced left/right layout.

---
