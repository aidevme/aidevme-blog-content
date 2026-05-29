# Image Generation Prompts — Article 37
# Entire.io Installation & Getting Started for Power Platform Developers

---

## 1. Featured Image

**File name:** `entire-io-installation-getting-started-featured.png`

**Alt text:** Entire.io CLI installation and setup process for Power Platform developers on macOS, Linux, and Windows

**Description:** Featured image for the article covering Entire.io installation and first-day setup. Should convey the idea of a developer configuring a new tool and connecting it to a Power Platform repository — the starting point of an Entire.io workflow. Displayed at 1200×628 (social/OG) and as the WordPress featured image at the top of the post.

**Generation prompt:**
Dark-background tech illustration. A terminal window centered in the frame shows a sequence of CLI commands being typed: `entire enable`, `entire login`, `entire status` — rendered as glowing white-on-dark text lines. Surrounding the terminal are three platform icons arranged in an arc: an Apple logo silhouette on the left, a Linux penguin outline in the centre-top, and a Windows logo silhouette on the right — all in soft muted tones. Below the terminal, a glowing teal progress bar or step-indicator shows three steps completing left to right. A faint Power Platform hexagon watermark sits behind the terminal. Color palette: near-black (#0d1117), teal (#00b4d8), electric blue (#4361ee), pale green for completed steps. Flat vector with soft glow halos around active elements. No visible readable text except stylised CLI fragments.

---

## 2. Prerequisites

**File name:** `entire-io-prerequisites-power-platform-dev-environment.png`

**Alt text:** Development environment prerequisites for Entire.io on a Power Platform project — Git, Node.js, .NET SDK, and PAC CLI

**Description:** Illustrates the prerequisite stack a Power Platform developer needs before installing Entire: Git, an AI coding agent, Node.js, .NET SDK, and PAC CLI. Used at the top of the Prerequisites section to give readers a quick visual inventory of what they need.

**Generation prompt:**
Dark tech illustration. A vertical stack of five tool icon tiles arranged like building blocks, each glowing with its own accent colour: a Git branch icon (orange), a Claude/Copilot chat bubble (blue), a Node.js hexagon (green), a .NET diamond logo (purple), a Power Platform diamond PAC CLI icon (teal). A faint checkmark appears next to each tile suggesting a readiness check. The background is deep navy. Each tile has a subtle drop shadow creating a layered card effect. Flat vector icon style. No readable text inside the tiles — only recognisable logo silhouettes.

---

## 3. Step 1: Install the Entire CLI

**File name:** `entire-io-cli-installation-macos-linux-windows.png`

**Alt text:** Entire.io CLI installation commands for macOS Homebrew, Linux curl, and Windows Scoop

**Description:** Illustrates the three installation paths for the Entire CLI: macOS with Homebrew, Linux with a curl script, and Windows with Scoop. Used at the start of the installation step to set the visual context before readers select their OS.

**Generation prompt:**
Dark-background tech illustration. Three terminal panels arranged side by side, each in a slightly different tinted window frame: left panel has an Apple silhouette above it showing `brew install entire` syntax; centre panel has a Linux penguin silhouette above showing `curl | bash`; right panel has a Windows logo above showing `scoop install entire`. Each panel glows with its own subtle accent (warm amber for macOS, cool green for Linux, azure for Windows). Below all three panels a single shared teal `entire version` output line appears, suggesting convergence after install. Background: near-black. Flat vector style. Terminal text is stylised/unreadable beyond the broad shape of commands.

---

## 4. Step 2: Log In to Entire

**File name:** `entire-io-login-authentication-browser-flow.png`

**Alt text:** Entire.io device authorization login flow — browser authentication connecting the CLI to the Entire.io account

**Description:** Illustrates the `entire login` device authorization flow: CLI triggers a browser window where the developer approves access, then the token is stored locally. Used at the start of Step 2 to make the one-time auth process feel simple and familiar before readers run the command.

**Generation prompt:**
Dark tech illustration. A two-step flow connected by a curved arrow. Left step: a terminal window showing `entire login` with a device code (e.g. `ABCD-1234`) displayed in glowing teal text below. Right step: a minimal browser window showing a clean approval screen — a large green checkmark button and a device code confirmation box. The curved arrow connecting terminal to browser has a small padlock icon at its midpoint suggesting secure authentication. Below both steps, a final terminal line reads `entire auth status → ✓ authenticated` in green. Background: near-black. Color palette: teal for CLI elements, soft green for the approval state, mid-blue for the browser chrome. Flat vector style.

---

## 5. Step 3: Enable Entire in Your Repository

**File name:** `entire-io-enable-repository-wizard-power-platform.png`

**Alt text:** The `entire enable` interactive wizard connecting Entire.io to a Power Platform solution repository

**Description:** Illustrates the `entire enable` setup wizard creating the `.entire/` folder, `settings.json`, and Git hooks inside a Power Platform repository. Used at the start of Step 3 to show what the command does structurally.

**Generation prompt:**
Dark tech illustration split in two halves. Left half: a terminal window showing an interactive wizard dialogue — numbered questions like "Which agent?" and "Push on git push?" rendered as glowing text. Right half: a folder tree diagram showing new files appearing — `.entire/settings.json`, `.git/hooks/`, `.claude/settings.json` — each file node illuminated as it is created, connected by thin glowing lines from the terminal on the left. A soft teal beam bridges the two halves suggesting the wizard writing the files. Background: deep navy. Flat vector style with subtle glow on newly created nodes.

---

## 6. Step 4: Add Multiple Agents (Optional)

**File name:** `entire-io-multiple-agents-configuration.png`

**Alt text:** Entire.io configured with multiple AI coding agents — Claude Code, GitHub Copilot CLI, and Cursor — in a single Power Platform repository

**Description:** Illustrates the ability to register multiple AI agents (Claude Code, Copilot CLI, Cursor, Codex) in the same repository so that every team member's agent of choice captures checkpoints. Used in Step 4 to show that Entire is not locked to a single tool.

**Generation prompt:**
Dark tech illustration. A central repository folder icon in teal sits at the middle of the frame. Four agent icons radiate outward from it connected by glowing lines: a Claude spiral logo (top-left, purple), a GitHub Copilot diamond (top-right, blue), a Cursor arrow icon (bottom-right, orange), and a Codex/OpenAI circle (bottom-left, soft white). Each line pulses with a directional glow flowing toward the repository — suggesting all agents feeding checkpoints into the same repo. A small hook/connector icon sits on each line close to the repo centre. Background: near-black. Color palette: teal for the central repo, each agent in its own accent colour. Flat vector spoke-and-hub diagram style.

---

## 7. Step 5: Power Platform Repository Structure with Entire - MISSING

**File name:** `entire-io-repository-structure-power-platform.png`

**Alt text:** Power Platform solution repository folder structure with Entire.io configuration files, plugin source, PCF controls, and pipeline YAML

**Description:** Shows the full recommended folder structure of a Power Platform code-first repository after Entire is enabled: solution source, plugin projects, PCF controls, Azure DevOps pipelines, and the `.entire/` config folder. Used in Step 5 to give developers a clear structural blueprint.

**Generation prompt:**
Dark tech illustration. A large, glowing directory tree diagram centered in the frame. Top-level folder is `my-solution-repo/` in teal. Children expand downward: `.entire/` (highlighted in electric blue with a checkpoint icon), `src/` (with sub-folders for `Plugins/`, `WebResources/`, `PCFControls/`), `pipelines/` (with a CI/CD icon), `MyApp.cdsproj`. Lines connecting folders are thin and glowing. The `.entire/` subtree is slightly brighter than the rest — it's the focus. A faint Power Platform diamond watermark sits behind the tree. Background: near-black. Flat vector diagram style, monospaced file names rendered as clean white text outlines — not meant to be precisely readable, just to convey structure.

---

## 8. Step 6: Team Configuration

**File name:** `entire-io-team-settings-json-configuration.png`

**Alt text:** Entire.io settings.json team configuration file showing redaction rules and session push options for a Power Platform project

**Description:** Illustrates the concept of shared team configuration via `settings.json` — redaction rules for Dataverse environment GUIDs, PII scrubbing, and session push settings. Used at the start of Step 6 to frame the configuration discussion visually.

**Generation prompt:**
Dark tech illustration. A glowing code-editor panel in the centre showing a JSON object structure — curly braces, key-value pairs, nested objects. Three specific lines are highlighted with soft accent glows: one for `push_sessions`, one for `redaction` (with a shield icon appearing next to it), one for `pii.enabled`. Above the panel a "team" icon (three overlapping silhouettes) with an upward arrow suggests this config is shared with the team via Git. A Git branch line runs along the bottom edge. Background: deep navy. Flat vector with subtle syntax-highlight colour coding on JSON elements.

---

## 9. Step 7: Choose Where to Store Checkpoints

**File name:** `entire-io-checkpoint-storage-same-vs-separate-repo.png`

**Alt text:** Decision diagram comparing Entire.io checkpoint storage in the same repository versus a separate private repository

**Description:** Illustrates the two approaches for checkpoint storage — same repo (default, zero config) versus separate repo (enterprise, independent access control) — as a forked decision diagram. Used at the start of Step 7 before readers choose their approach and before the configuration details of Option B.

**Generation prompt:**
Dark tech illustration. A forked-path decision diagram. At the top, a single teal `entire/checkpoints/v1` branch icon flows downward into a diamond decision node. Two paths diverge from the diamond. Left path (Option A — green accent): a single repository box containing both a code-bracket icon and a small branch/checkpoint capsule icon side by side — labelled "Same repo"; a zero-step badge sits on the arrow (zero config). Right path (Option B — amber/gold accent): two separate repository boxes — the left one has a code-bracket icon (solution code), the right one has a padlock icon (session records) — connected by a forking arrow with a small shield/governance badge at the split point. The green left path has a softer, simpler glow; the amber right path has a more structured, guarded feel. Background: near-black. Color palette: teal for the shared branch, green for Option A, amber for Option B. Flat vector diagram, no readable text labels.

---

## 10. Step 8: Checkpoint Remote for Enterprise Governance

**File name:** `entire-io-checkpoint-remote-enterprise-governance.png`

**Alt text:** Entire.io checkpoint remote configuration separating session transcripts from solution code in a separate private repository for enterprise governance

**Description:** Illustrates the enterprise pattern of routing checkpoint data to a separate private repository for independent access control. Used at the start of Step 7 to make the concept of split storage visually clear before the configuration details.

**Generation prompt:**
Dark tech illustration. Two repository boxes side by side, connected by diverging arrows from a central commit point. Left repository: labelled with a code-bracket icon — represents the solution code repo. Right repository: labelled with a lock icon and a checkpoint/capsule icon — represents the private session records repo. The arrow splitting them is labelled with a small shield/governance badge. Both repos have a subtle GitHub Octocat silhouette. Above the split-point, a single teal commit node with an `entire push` label initiates both flows. Color palette: near-black background, left repo in blue, right repo in teal/locked gold. Flat vector with clean directional arrows.

---

## 11. Step 9: GUI Git Client Configuration

**File name:** `entire-io-gui-git-client-configuration.png`

**Alt text:** Entire.io configured with GUI Git clients — Tower, GitKraken, and Sourcetree — using absolute binary paths for Git hook compatibility

**Description:** Illustrates the one extra configuration step needed for developers using GUI Git clients (Tower, GitKraken, Sourcetree), where the full binary path must be embedded in hooks because GUI apps don’t source the shell profile. Used in Step 8 to head off a common setup failure before it happens.

**Generation prompt:**
Dark tech illustration. A central Git hook icon (a small script/gear symbol) sits in the middle of the frame. Three GUI client logos radiate from it on the left side as stylised silhouettes: a tower/castle shape (Tower), a kraken tentacle shape (GitKraken), and a source-tree branch shape (Sourcetree). On the right side of the hook icon, a full file path string glows in teal — rendered as `/usr/local/bin/entire` — with a small warning triangle above it changing to a green checkmark after the path is resolved. A thin dashed line connects the GUI icons to the hook, and a solid line connects the hook to the resolved path. Background: near-black. Color palette: amber for the warning state, green for resolved, teal for the path text. Flat vector style.

---

## 12. Step 10: Your First AI-Assisted Session and Checkpoint

**File name:** `entire-io-first-checkpoint-ai-session-power-platform.png`

**Alt text:** First Entire.io checkpoint created from a Claude Code session writing a Dataverse plugin — linking the AI conversation to the Git commit

**Description:** Shows the moment a developer's first Entire checkpoint is created: an AI session in Claude Code producing a Dataverse plugin, followed by a commit, with Entire linking them as a checkpoint. Used in Step 9 to make the workflow feel tangible and real.

**Generation prompt:**
Dark tech illustration. Three connected panels in a left-to-right flow. Left panel: a chat interface with a developer prompt asking the AI to write a plugin, and a code response below — glowing blue conversation bubbles. Centre panel: a terminal showing `git commit -m "feat: Add plugin"` with the Entire confirmation prompt below ("Link this commit to session context? [Y]es"). Right panel: a Git graph node glowing teal with a checkpoint capsule icon attached — the session locked to the commit. Thin arrows connect all three panels. Background: near-black. Flat vector with a warm glow on the centre confirmation step as the focal point.

---

## 13. Verifying Your Setup

**File name:** `entire-io-verify-setup-checkpoint-list.png`

**Alt text:** Entire.io status, checkpoint list, and checkpoint explain commands verifying a successful installation in a Power Platform repository

**Description:** Shows the verification commands — `entire status`, `entire checkpoint list`, `entire checkpoint explain HEAD` — and their confirming outputs. Used in the Verifying Your Setup section to reassure readers that setup is complete and working.

**Generation prompt:**
Dark tech illustration. A tall terminal window with three stacked command+output blocks separated by subtle dividers. First block: `entire status` → a green success badge. Second block: `entire checkpoint list` → a short list of checkpoint entries, each a glowing capsule row. Third block: `entire checkpoint explain HEAD` → a compact summary card showing prompt, files changed, and a session snippet. A soft green glow pulses at the top of the terminal suggesting a healthy/confirmed state. Background: deep navy. Flat vector terminal UI style with clean monospaced layout.

---

## 13. Connecting to Entire.io Web Dashboard

**File name:** `entire-io-web-dashboard-power-platform-session-history.png`

**Alt text:** Entire.io web dashboard showing checkpoint history, session transcripts, and search across AI coding sessions for a Power Platform repository

**Description:** Illustrates the Entire.io web interface — checkpoint timeline, full session transcript view, and cross-session search. Used in the "Connecting to Entire.io" section to show the payoff of the setup work done in the preceding steps.

**Generation prompt:**
Dark tech illustration of a browser window (minimal chrome, no branding) showing a dashboard UI. Left sidebar: a list of checkpoint entries as glowing capsule rows with timestamps and short commit messages. Centre area: a selected session transcript showing alternating prompt/response blocks in a chat-like layout. Top-right: a search bar with a glowing cursor and a faint query suggestion. A Git branch timeline runs along the very bottom of the dashboard panel. Color palette: near-black UI background, teal accent on active/selected elements, pale blue for transcript text. Flat vector UI mockup style — not a real screenshot, clearly illustrative.

---

## 14. Installing Entire Skills

**File name:** `entire-io-skills-installation-power-platform-agents.png`

**Alt text:** Installing Entire Skills for Claude Code and GitHub Copilot CLI — reusable agent workflows for querying session history in Power Platform projects

**Description:** Illustrates the Entire Skills installation step: pluggable agent workflows (Search, Explain, What Happened, Session Handoff) that extend Claude Code and Copilot CLI with session-history awareness. Used in the Installing Entire Skills section to show what Skills add on top of basic checkpoint storage.

**Generation prompt:**
Dark tech illustration. A central puzzle-piece icon in teal sits at the middle of the frame — representing a skill/plugin. From the left, two agent logos (a Claude spiral and a Copilot diamond) send an arrow toward the puzzle piece. From the right of the puzzle piece, four labelled capability badges fan out as glowing pill shapes: “Search”, “Explain”, “What Happened”, “Handoff” — each in a slightly different accent colour. Below the whole composition, a faint terminal line shows a skill invocation command. Background: near-black. Color palette: teal for the skill piece, purple for Claude, blue for Copilot, varied pastels for capability badges. Flat vector style.

---

## 15. Troubleshooting Common Issues

**File name:** `entire-io-troubleshooting-common-issues-power-platform.png`

**Alt text:** Entire.io troubleshooting — entire doctor command diagnosing hook failures, missed sessions, and checkpoint push errors in a Power Platform repository

**Description:** Illustrates the `entire doctor` diagnostic command and the most common failure modes: hooks not firing, sessions not captured, and checkpoint branch not pushed. Used in the Troubleshooting section to reassure readers that problems are diagnosable and fixable with clear commands.

**Generation prompt:**
Dark tech illustration. A stethoscope icon in teal overlaps a terminal window — the visual metaphor for `entire doctor`. Inside the terminal, three rows each show a problem–fix pair: a red cross icon next to “Hooks not firing”, an amber warning icon next to “Session not captured”, and a blue info icon next to “Branch not pushed”. Each row has a right-pointing arrow leading to a small green resolved badge. Below the terminal a single command line glows: `entire doctor`. Background: near-black. Color palette: teal for the stethoscope and header, red/amber/blue for problem severity icons, green for resolved states. Flat vector style with clean row layout.

---

## 16. Environment Variables Reference

**File name:** `entire-io-environment-variables-reference.png`

**Alt text:** Entire.io environment variables — ENTIRE_ENABLED, ENTIRE_LOG_LEVEL, and ENTIRE_TELEMETRY_OPTOUT — for controlling CLI behaviour without modifying configuration files

**Description:** Illustrates the three key environment variables that control Entire’s runtime behaviour: disabling Entire globally, enabling debug logging for a session, and opting out of telemetry. Used in the Environment Variables Reference section to show that runtime overrides are a single shell variable away.

**Generation prompt:**
Dark tech illustration. Three environment variable rows arranged vertically, each in a clean pill-shaped card. First card: a power/off toggle icon next to `ENTIRE_ENABLED=false` in amber — suggesting temporary disable. Second card: a magnifying glass / bug icon next to `ENTIRE_LOG_LEVEL=debug` in teal — suggesting diagnostic mode. Third card: a no-tracking icon (circle with line) next to `ENTIRE_TELEMETRY_OPTOUT=1` in soft grey — suggesting privacy opt-out. Each card has a subtle left-border accent in its own colour. Background: near-black. To the left of all three cards, a small terminal prompt arrow suggests these are set inline before a command. Flat vector style.

---

## 17. Step 5: Repository Structure — Animated GIF

**File name:** `entire-io-power-platform-samples-folder-structure.gif`

**Alt text:** Animated folder tree reveal of the entire-io-power-platform-samples repository — showing src/, tests/, terraform/, and entire-config/ progressively expanding

**Description:** Animated GIF for Step 5. The full `entire-io-power-platform-samples` folder tree is printed instantly in a terminal-style window — taller than the viewport — and then the viewport automatically scrolls from top to bottom at a steady pace, letting readers read every line. Ends with a 2-second hold at the bottom, then loops back to the top.

**Animation spec (for terminalizer / asciinema2gif / custom renderer):**

Terminal window: 900×520 px (viewport), dark background `#0d1117`, monospace font (JetBrains Mono or Fira Code), font size 13px. The rendered tree is ~90 lines tall — approximately 2.5× the viewport height, so scrolling is necessary to see it all.

Color scheme:
- Root folder: `#00b4d8` (teal)
- `.entire/` subtree: `#4361ee` (electric blue) — highlight as Entire-owned files
- `.git/hooks/`: `#4361ee`
- `.claude/`: `#4361ee`
- `entire-config/`: `#4361ee`
- `terraform/`: `#f77f00` (orange)
- `src/`: `#06d6a0` (green)
- `tests/`: `#a8dadc` (pale blue)
- `.github/`: `#8d8d8d` (grey — secondary)
- File names: `#e6edf3` (near-white)
- Comments after `←`: `#6e7681` (muted grey)

**Full tree content (rendered in one pass before scroll begins):**

```
entire-io-power-platform-samples/
├── README.md                          ← Series overview, prerequisites, how to use
├── CONTRIBUTING.md                    ← How to run samples, submit issues, style guide
├── .gitignore
├── .entire/
│   ├── settings.json                  ← Entire enabled; sample redaction rules — commit this
│   ├── settings.local.json            ← Personal overrides — gitignored automatically
│   └── .gitignore                     ← Ensures local settings are not committed
├── .git/
│   └── hooks/                         ← post-commit, prepare-commit-msg, pre-push hooks installed
├── .claude/
│   └── settings.json                  ← Claude Code hook config (or equivalent for your agent)
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── bug_report.md
│   └── pull_request_template.md
├── entire-config/
│   ├── README.md
│   ├── settings.json.example
│   └── custom-redaction.json.example
├── terraform/
│   ├── README.md
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── terraform.tfvars.example
│   └── modules/
│       ├── function-app/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── outputs.tf
│       └── managed-identity/
│           ├── main.tf
│           ├── variables.tf
│           └── outputs.tf
└── src/
    ├── webresources/
    │   ├── package.json
    │   ├── tsconfig.json
    │   ├── webpack.config.js
    │   ├── shared/
    │   │   └── ClientApiUtils.ts
    │   ├── opportunity/
    │   │   └── FormScripts.ts
    │   └── account/
    │       └── FormScripts.ts
    ├── plugins/
    │   ├── Plugins.sln
    │   ├── Plugins.csproj
    │   ├── opportunity/
    │   │   └── OpportunityScoringPlugin.cs
    │   └── account/
    │       └── AccountValidationPlugin.cs
    ├── customapis/
    │   ├── CustomApis.sln
    │   ├── CustomApis.csproj
    │   └── quote/
    │       └── CalculateQuoteTotalHandler.cs
    ├── pcfs/
    │   └── AccountOpportunityGrid/
    │       ├── ControlManifest.Input.xml
    │       ├── index.ts
    │       └── css/
    │           └── AccountOpportunityGrid.css
    ├── codeapps/
    │   └── README.md
    └── azurefunctions/
        ├── DocumentGenerationFunction/
        │   ├── DocumentGenerationFunction.csproj
        │   ├── DocumentGenerationFunction.cs
        │   ├── host.json
        │   └── local.settings.json.example
        ├── ServiceBusProcessor/
        │   ├── ServiceBusProcessor.csproj
        │   └── ServiceBusTriggeredProcessor.cs
        └── custom-connector/
            └── openapi-definition.yaml

tests/
    ├── webresources/
    │   ├── package.json
    │   ├── jest.config.js
    │   ├── shared/
    │   │   └── ClientApiUtils.test.ts
    │   └── opportunity/
    │       └── FormScripts.test.ts
    ├── plugins/
    │   └── Plugins.Tests/
    │       ├── Plugins.Tests.csproj
    │       ├── opportunity/
    │       │   ├── OpportunityScoringPluginTests.cs
    │       │   └── Fakes/
    │       │       └── FakeOrganizationService.cs
    │       └── account/
    │           └── AccountValidationPluginTests.cs
    ├── customapis/
    │   └── CustomApis.Tests/
    │       ├── CustomApis.Tests.csproj
    │       └── quote/
    │           └── CalculateQuoteTotalHandlerTests.cs
    ├── pcfs/
    │   └── AccountOpportunityGrid.test/
    │       ├── index.test.ts
    │       ├── package.json
    │       └── jest.config.js
    └── azurefunctions/
        └── AzureFunctions.Tests/
            ├── AzureFunctions.Tests.csproj
            ├── DocumentGenerationFunctionTests.cs
            └── ServiceBusProcessorTests.cs
```

**Scroll animation:**

- Phase 1 — Render (0.0 s): Full tree is printed instantly (0 ms typing delay). Viewport shows top of tree.
- Phase 2 — Hold at top (0.5 s): Static, 500 ms.
- Phase 3 — Scroll down (1.0 s → 14.0 s): Smooth continuous scroll at ~55 px/s. Duration ~13 s to travel from top to bottom of the full tree. No pauses mid-scroll.
- Phase 4 — Hold at bottom (14.0 s): Static for 2 seconds showing the last lines of `tests/azurefunctions/`.
- Phase 5 — Loop: Jump-cut back to top (frame 1), repeat.

Total loop duration: ~16.5 seconds.

---

## 18. First-Day Checklist

**File name:** `entire-io-first-day-checklist-power-platform-team.png`

**Alt text:** First-day setup checklist for Entire.io on a Power Platform team — install, login, enable, configure, and verify

**Description:** Visual summary of the complete first-day setup checklist: install, login, enable, team config, redaction, skills, web dashboard. Used at the end of the article before the closing navigation links to leave readers with a clear sense of completion.

**Generation prompt:**
Dark tech illustration. A vertical checklist of eight items, each row containing a glowing checkbox (shown as checked / ticked) and a short icon+label: CLI install icon, login key icon, repository enable icon, team settings gear icon, redaction shield icon, skills puzzle icon, dashboard screen icon, and a final star/verified badge icon. The checkboxes glow from top to bottom in a completion gradient — teal at top transitioning to electric blue at the bottom — suggesting a sequence being completed. A faint "Day 1" banner in soft white arcs over the checklist. Background: near-black. Flat vector list-UI style with clean icon silhouettes.
