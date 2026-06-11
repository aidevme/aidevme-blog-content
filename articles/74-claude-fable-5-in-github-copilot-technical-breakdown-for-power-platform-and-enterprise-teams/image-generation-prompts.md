# Image Generation Prompts — Article 74
# Claude Fable 5 in GitHub Copilot — Technical Breakdown for Power Platform and Enterprise Teams

---

## 1. Featured Image

**File name:** `claude-fable-5-github-copilot-power-platform-featured.png`

**Alt text:** Claude Fable 5 in GitHub Copilot — Anthropic's first Mythos-class model now available for enterprise Power Platform teams

**Description:** Featured image for the article covering Claude Fable 5's GA release in GitHub Copilot. Should convey the idea of a genuinely new capability tier — above Opus, built for long-horizon autonomous work — landing in a familiar enterprise toolchain. Displayed at 1200×628 (social/OG) and as the WordPress featured image at the top of the post.

**Generation prompt:**
Dark-background tech illustration. A large glowing diamond shape dominates the center frame — styled after the Anthropic/Claude brand color (warm coral/orange gradient), labeled "Fable 5" in clean sans-serif. Above the diamond, a faint crown or tier badge labeled "Mythos Class" in gold, signifying a capability above Opus. The diamond is partially overlaid with the GitHub Copilot glowing circle logo (teal), suggesting the model is now embedded in Copilot. Below the composition, a faint Power Platform abstract grid pattern (hexagons or diamonds in Azure blue) represents the enterprise deployment target. Thin arcing lines radiate outward from the central diamond — suggesting long-horizon autonomous reach. Color palette: near-black (#0d1117), warm coral-orange (#e07b54) for the Claude diamond, teal (#00b4d8) for the Copilot overlay, gold (#f4c430) for the Mythos badge. Flat vector with soft glow halos. No readable text except the stylised "Fable 5" and "Mythos Class" labels.

---

## 2. What Claude Fable 5 Actually Is

**File name:** `claude-fable-5-mythos-class-capability-tier.png`

**Alt text:** Claude capability tier diagram — Fable 5 sits above Opus in the new Mythos class, with safety classifier layer distinguishing it from the unrestricted Mythos partner model

**Description:** Illustrates the capability tier structure and the Fable/Mythos naming split: Mythos is the unrestricted partner model, Fable 5 is the same model with safety classifiers added for public use. Used at the start of the "What it actually is" section to give readers an immediate mental model of where Fable 5 sits in the Claude lineup.

**Generation prompt:**
Dark tech illustration. A vertical capability ladder with four labeled rungs, bottom to top: "Haiku" (soft grey, small), "Sonnet" (soft blue, medium), "Opus" (electric blue, larger), "Fable 5 / Mythos" (coral-orange glow, largest — the top rung). The Fable 5 rung is split into two adjacent tiles: left tile labeled "Fable 5 — Public" with a small shield/classifier icon; right tile labeled "Mythos 5 — Partner only" with a small lock icon. A thin bracket labeled "Mythos class" spans both tiles. A faint dashed line labeled "Project Glasswing" floats above the right tile, referencing the restricted preview. Below the ladder, a small label reads "Long-horizon autonomous execution" as the capability description. Background: near-black. Color palette: coral-orange (#e07b54) for the top rung, electric blue for Opus, soft blue for Sonnet, grey for Haiku. Flat vector ladder style.

---

## 3. The Technical Specs That Matter for Builders

**File name:** `claude-fable-5-technical-specs-context-window-pricing.png`

**Alt text:** Claude Fable 5 technical specs — 1M token context window, 128k max output, adaptive thinking, 30-day data retention, and pricing at $10/$50 per MTok

**Description:** Illustrates the key technical specification cards for Fable 5: context window, max output, pricing, prompt caching discount, thinking mode, and data retention. Used alongside the reference table in the specs section to make the most important numbers scannable at a glance, particularly the retention flag.

**Generation prompt:**
Dark tech illustration. A grid of six specification tiles arranged in two rows (3 top, 3 bottom), each a small rounded card. Card 1: a token counter icon with "1M tokens" in large coral text, labeled "Context window." Card 2: an output arrow icon with "128k tokens" in electric blue, labeled "Max output." Card 3: a price tag icon with "$10 / $50 MTok" in amber, labeled "Input / Output pricing." Card 4: a cache cylinder with "90% off" in teal, labeled "Prompt caching." Card 5: a brain/thinking icon with "Always on" in soft white, labeled "Adaptive thinking." Card 6: a clock/calendar icon with "30 days" in warm red, labeled "Data retention" — this card has a subtle warning glow to flag its governance significance. All cards have thin electric blue borders on near-black backgrounds. Flat vector card-grid style. No additional text.

---

## 4. The Fallback Mechanism — The Part That's Genuinely New

**File name:** `claude-fable-5-fallback-opus-safety-classifier.png`

**Alt text:** Claude Fable 5 safety classifier fallback — requests triggering cybersecurity or bio/chem classifiers are silently routed to Opus 4.8 rather than refused

**Description:** Illustrates the two-path request routing introduced with Fable 5: most requests go directly to Fable 5 (>95%), while a small category of requests hits the safety classifiers and routes to Opus 4.8 instead. Used in the fallback mechanism section to make the routing behavior visually concrete for developers building agent workflows.

**Generation prompt:**
Dark tech illustration. A request node on the left (a chat bubble or API request icon) sends an arrow to a central classifier node — a small shield labeled "Safety Classifiers." From the classifier, two paths diverge. The wide path (labeled ">95% of requests" in teal) curves right to a large Fable 5 diamond node glowing in coral-orange — labeled "Claude Fable 5." The narrow path (labeled "<5% of requests — cybersecurity, bio/chem, distillation" in amber) curves downward to a smaller Opus 4.8 node in electric blue — labeled "Claude Opus 4.8." A small annotation beside the narrow path reads "stop_reason: 'refusal' — HTTP 200, no charge." The Opus node has a small notification badge: "User informed of routing." Background: near-black. Color palette: coral-orange for Fable, electric blue for Opus, teal for the main path, amber for the fallback path. Flat vector split-path diagram.

---

## 5. Where You'll Find It in Copilot

**File name:** `claude-fable-5-github-copilot-surfaces-agent-mode.png`

**Alt text:** Claude Fable 5 available across GitHub Copilot surfaces — VS Code, GitHub.com, CLI, mobile, and JetBrains — with agent mode as the primary value surface

**Description:** Illustrates the breadth of GitHub Copilot surfaces where Fable 5 is available (VS Code, Visual Studio, GitHub.com, CLI, Mobile, JetBrains) and highlights agent mode as the context where the model's long-horizon capability actually delivers its value. Used in the "Where you'll find it" section to orient readers on availability and steer toward the right use case.

**Generation prompt:**
Dark tech illustration. A central GitHub Copilot glowing circle logo (teal) in the middle. Six surface icons radiate outward from the center in a spoke pattern — each a small rounded badge: VS Code icon, Visual Studio icon, GitHub.com browser icon, CLI terminal icon, mobile phone outline, JetBrains logo. Each badge is connected to the center by a thin teal line. One spoke — labeled "Agent Mode" — is visually emphasized: the line is thicker, the badge glows brighter, and a small tag beside it reads "Long-horizon tasks — primary value surface." The other spokes are slightly muted by comparison. A faint "Pro+ · Max · Business · Enterprise" label arcs below the composition. Background: near-black. Color palette: teal for active spokes, electric blue for surface badges, coral-orange highlight on the Agent Mode badge. Flat vector hub-and-spoke style.

---

## 6. The Data Retention Requirement — Read This Before Enabling

**File name:** `claude-fable-5-data-retention-zdr-compliance-governance.png`

**Alt text:** Claude Fable 5 breaks Zero Data Retention — 30-day retention required for safety classifiers, off by default in Copilot Business and Enterprise, compliance review needed

**Description:** Illustrates the ZDR break introduced by Fable 5: all other Claude models in Copilot operate under ZDR (no retention), while Fable 5 requires 30-day retention for its safety classifier system. Used in the data retention section to make the compliance gap visually stark, particularly for enterprise readers who approved Copilot under ZDR assumptions.

**Generation prompt:**
Dark tech illustration. A split layout with two columns. Left column (labeled "All other Claude models in Copilot" in soft blue): a model list (Opus 4.8, Sonnet 4.5, Haiku 4.5) each with a large green "ZDR" shield icon and "No retention" label beneath. Right column (labeled "Claude Fable 5" in coral-orange): the Fable 5 diamond icon with an amber clock badge labeled "30 days" and a warning tag reading "Covered Model — retention required." Below the Fable 5 column, two bullet annotations in soft white: "Not used for training" (green checkmark) and "Safety classifier use only" (green checkmark). At the bottom of the composition, a horizontal red banner reads "Off by default — enabling = compliance review" to flag the governance action required. A thin vertical divider separates the two columns. Background: near-black. Color palette: green for ZDR, amber and coral for the Fable retention column, red for the compliance banner. Flat vector comparison layout.

---

## 7. My Take: How to Handle the Enablement Decision

**File name:** `claude-fable-5-enterprise-enablement-governance-framework.png`

**Alt text:** Enterprise enablement framework for Claude Fable 5 — scoped rollout by repository sensitivity, AI usage register, piloting with measurable workloads

**Description:** Illustrates the four-step governance framework for enabling Fable 5 in an enterprise context: scope by repository, document in the AI usage register, keep capability and retention discussions separate, and pilot before broad rollout. Used in the "My Take" section as a visual summary of the recommended decision process.

**Generation prompt:**
Dark tech illustration. A vertical four-step checklist card layout, each step a rounded row with a large step number on the left and an action label on the right. Step 1 (electric blue): a repository fork icon labeled "Scope by repository — own IP first, client repos last." Step 2 (teal): a document/register icon labeled "Add to AI usage register — retention + residency per model." Step 3 (soft white): a balance scale icon labeled "Keep retention and capability discussions separate." Step 4 (coral-orange): a measuring gauge icon labeled "Pilot with a measurable workload — one sprint, compare Opus vs Fable." Each row has a thin left border in its accent color. Below the four steps, a small footer reads "Governance decision — not a capability gating." Background: near-black. Flat vector checklist style with clean left-right layout.

---

## 8. Key Takeaways

**File name:** `claude-fable-5-github-copilot-key-takeaways-enterprise.png`

**Alt text:** Claude Fable 5 key takeaways — Mythos-class model in Copilot, 30-day retention, fallback behavior, and enterprise enablement checklist for Power Platform teams

**Description:** Illustrates the five key takeaways from the article as a compact summary card — GA in Copilot, technical specs, fallback routing, retention break, and enterprise governance recommendation. Used at the end of the article as a visual recap readers can screenshot and share.

**Generation prompt:**
Dark tech illustration. A single tall summary card on near-black, with a coral-orange header bar reading "Claude Fable 5 — What You Need to Know." Below the header, five numbered rows, each a single-line takeaway with a small icon to the left: (1) Copilot logo + "GA in Copilot Pro+, Max, Business, Enterprise — Mythos class." (2) Token counter + "1M context · 128k output · $10/$50 MTok · 90% cache discount." (3) Shield + "Safety classifiers → Opus 4.8 fallback on <5% of requests." (4) Clock + "30-day retention — ZDR break — off by default." (5) Checklist + "Scope by repo, document, pilot before broad rollout." Each row alternates between very dark grey and near-black backgrounds for readability. The card has a thin coral-orange border and a small "aidevme.com" watermark in the bottom-right corner. Color palette: coral-orange for header and icons, soft white for text. Flat vector summary-card style.

---
