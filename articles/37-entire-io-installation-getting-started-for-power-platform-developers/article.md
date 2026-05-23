# Entire.io Installation & Getting Started for Power Platform Developers

*Part 2 of 9 in the [Entire.io for Power Platform](https://aidevme.com/entire-io-for-power-platform-developers-why-ai-coding-sessions-need-a-system-of-record/) series · ← [Part 1: Why AI Coding Sessions Need a System of Record](https://aidevme.com/entire-io-for-power-platform-developers-why-ai-coding-sessions-need-a-system-of-record/) · [Part 3: Form Scripts & Web Resources →](https://aidevme.com/entire-io-for-power-platform-javascript-typescript-development-form-scripts-and-web-resources/)*

## Prerequisites

Before installing Entire, ensure the following are in place on your development machine:

- **Git** — installed and configured with your identity (`git config --global user.name` / `user.email`)
- **At least one AI coding agent** — Claude Code, GitHub Copilot CLI, Cursor, Codex, Gemini CLI, or OpenCode
- **OS** — macOS, Linux, or Windows
- **Node.js / npm** — required for some agent CLIs; already present in most Power Platform dev environments
- **.NET SDK** — required if working on Dataverse plugins (C#)
- **Power Platform CLI (`pac`)** — recommended; used for `pac solution unpack`, `pac pcf init`, and related workflows
- **Optional: GitHub CLI (`gh`)** — if you want Entire to auto-create a private GitHub repository during first-time setup

---

## Step 1: Install the Entire CLI

Entire ships two channels: **stable** (recommended) and **nightly** (pre-release).

### macOS (Homebrew)

```bash
# Stable
brew tap entireio/tap
brew install --cask entire

# Nightly (for latest features)
brew tap entireio/tap
brew install --cask entire@nightly
```

### Linux

```bash
# Stable
curl -fsSL https://entire.io/install.sh | bash

# Nightly
curl -fsSL https://entire.io/install.sh | bash -s -- --channel nightly
```

### Windows (Scoop)

```powershell
scoop bucket add entire https://github.com/entireio/scoop-bucket.git
scoop install entire/cli
```

### Verify Installation

```bash
entire version
# Output: Entire CLI v1.x.x (abc1234) Go version: go1.21.0 OS/Arch: darwin/arm64
```

---

## Step 2: Log In to Entire

Authenticate with your Entire account to enable web dashboard access and cloud search:

```bash
entire login
```

This opens a device authorization flow in your browser. After approving, your token is stored locally. Verify:

```bash
entire auth status
```

---

## Step 3: Enable Entire in Your Power Platform Repository

Navigate to the root of your Power Platform solution repository — where your `.git` folder lives and where `pac solution unpack` has placed the solution folder structure — and run:

```bash
cd my-solution-repo
entire enable
```

The interactive setup wizard will ask:

1. **Which agent to set up hooks for** — choose the one you use (Claude Code is default)
2. **Whether to enable telemetry** — anonymous usage analytics; opt in or out per your policy
3. **Whether to push checkpoint data automatically on git push** — recommended: yes

For non-interactive / CI environments:

```bash
entire enable --yes --agent claude-code
```

### What `entire enable` Creates

```
my-solution-repo/
├── .entire/
│   ├── settings.json        # Shared project settings — commit this
│   ├── settings.local.json  # Personal overrides — gitignored automatically
│   └── .gitignore           # Ensures local settings are not committed
├── .git/
│   └── hooks/               # post-commit, prepare-commit-msg, pre-push hooks installed
└── .claude/
    └── settings.json        # Claude Code hook config (or equivalent for your agent)
```

> **Important for teams:** Commit `.entire/settings.json` and `.entire/.gitignore` to your repository so all team members share the same Entire configuration. Each developer runs `entire enable` locally to install the Git hooks on their machine.

---

## Step 4: Add Multiple Agents (Optional)

Mixed-agent teams are common, not the exception. According to the [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/ai), 25.5% of development teams report that tool adoption is uneven — different developers reach for different tools independently before any org-wide decision is made. In practice, Power Platform teams typically end up with multiple agents for three reasons:

- **Enterprise licensing vs. personal choice.** Most organisations already have GitHub Copilot through a Microsoft 365 E5 or GitHub Enterprise agreement. Developers then independently adopt Claude Code, Cursor, or Gemini CLI. Copilot becomes the org standard; everything else runs in parallel.
- **IDE-native vs. terminal-native workflows.** Copilot CLI and Cursor live inside the editor as inline autocomplete and chat sidebars. Claude Code and Codex are terminal-native — better suited for long agentic sessions that span the whole repository. Teams routinely use both: one for active in-editor work, another for complex multi-file sessions.
- **Developer autonomy.** On a five-person team, all five may have formed preferences before any standardisation happened. Registering all agents in Entire is a practical middle ground: individual tool choice is preserved, but session history remains unified.

Register each agent your team uses:

```bash
entire agent add copilot-cli
entire agent add cursor
entire agent add codex
entire agent add gemini
entire agent add factoryai-droid
entire agent add opencode
entire agent add pi
```

List what's configured:

```bash
entire agent list
```

Each agent installs its hooks independently. The agents supported by Entire and their current capture capabilities are:

| Agent | `--agent` flag | Subagent capture | Token tracking | Rewind/Resume |
|---|---|---|---|---|
| Claude Code | `claude-code` | ✅ Full | ✅ | ✅ |
| Codex | `codex` | ❌ Not yet | ✅ | ✅ |
| Copilot CLI | `copilot-cli` | ✅ | Post-session | ✅ |
| Cursor | `cursor` | ✅ | ✅ | ❌ |
| Factory Droid | `factoryai-droid` | ✅ via hooks | ✅ | ✅ |
| Gemini CLI | `gemini` | ✅ | Limited | ✅ |
| OpenCode | `opencode` | ✅ | ✅ | ✅ |
| Pi *(Preview)* | `pi` | ✅ | ✅ | ✅ |

Source: [docs.entire.io/agents](https://docs.entire.io/agents)

The capability differences matter when choosing which agent to use for complex, multi-step sessions where you need full transcript fidelity and rewind support. For quick edits and inline completions, any agent works equally well with Entire.

---

## Step 5: Typical Power Platform Repository Structure with Entire

A mature Power Platform code-first repository with Entire enabled looks like this:

```
my-solution-repo/
├── .entire/
│   ├── settings.json           # Shared Entire config
│   ├── .gitignore
│   └── redactors/              # Optional: custom redaction rule packs
│       └── pp-internal.yaml
├── src/
│   ├── MyCompany.MyApp/        # Unpacked solution (pac solution unpack)
│   │   ├── Plugins/
│   │   ├── WebResources/
│   │   └── Other/
│   ├── MyApp.Plugins/          # C# Dataverse plugin project
│   │   ├── MyApp.Plugins.csproj
│   │   └── *.cs
│   ├── MyApp.PCFControls/      # PCF TypeScript projects
│   │   └── MyControl/
│   │       ├── index.ts
│   │       └── ControlManifest.Input.xml
│   └── MyApp.Tests/            # NUnit / Moq unit tests
├── pipelines/                   # Azure DevOps YAML pipeline definitions
├── MyApp.cdsproj               # Solution build driver (dotnet build)
├── .claude/
│   └── settings.json           # Claude Code hook config (auto-created)
└── .gitignore
```

---

## Step 6: Team Configuration — `settings.json`

Edit `.entire/settings.json` to configure team-wide behavior:

```json
{
  "enabled": true,
  "log_level": "info",
  "telemetry": true,
  "strategy_options": {
    "push_sessions": true,
    "summarize": {
      "enabled": true
    }
  },
  "redaction": {
    "custom_redactions": {
      "env_guid": "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
      "connection_ref": "new_[a-zA-Z]{2,}_[a-zA-Z0-9_]{5,}",
      "sp_client_secret": "(?i)(clientsecret|client_secret)[\"']?\\s*[:=]\\s*[\"']?[A-Za-z0-9+/=.~_-]{20,}"
    },
    "pii": {
      "enabled": true,
      "email": true,
      "phone": true
    }
  }
}
```

**Key settings for Power Platform projects:**

| Setting | Recommendation |
|---|---|
| `push_sessions: true` | Always push checkpoint data alongside code |
| `summarize.enabled: true` | Auto-generate AI summaries at commit time — very useful for complex plugin sessions |
| Custom redaction for env GUIDs | Prevents Dataverse environment GUIDs from appearing in session transcripts |
| PII redaction enabled | Appropriate for solutions that process customer or employee data through Dataverse |

### Personal Overrides (`.entire/settings.local.json`)

Each developer can override settings locally without affecting the team:

```json
{
  "log_level": "debug",
  "telemetry": false
}
```

This file is gitignored automatically.

---

## Step 7: Checkpoint Remote (Enterprise / Governance)

For enterprise teams where session transcripts should be kept separate from the solution code repository — for security, governance, or access control reasons — configure a checkpoint remote:

```bash
entire enable --checkpoint-remote github:myorg/pp-session-records
```

Or in `settings.json`:

```json
{
  "strategy_options": {
    "checkpoint_remote": {
      "provider": "github",
      "repo": "myorg/pp-session-records"
    }
  }
}
```

This pushes the `entire/checkpoints/v1` branch to a separate private repository. Your solution code stays in its normal repository. Access to session transcripts is independently controlled.

> **Fork detection:** Entire automatically skips checkpoint pushes when the push remote owner differs from the checkpoint remote owner — preventing contributors from accidentally pushing to an organization's private session repository.

---

## Step 8: GUI Git Client Configuration

If your team uses Tower, GitKraken, Sourcetree, or similar GUI Git clients, the Entire hooks need the full binary path because GUI clients don't source your shell profile:

```bash
entire configure --absolute-git-hook-path
```

This embeds the full path to the `entire` binary in the installed Git hooks.

---

## Step 9: Your First AI-Assisted Session and Checkpoint

With Entire configured, start a normal agent session in your repository:

```bash
# Example with Claude Code
claude

# Example with GitHub Copilot CLI
copilot
```

Give the agent a task relevant to your Power Platform work:

```
Create a new Dataverse plugin class for the account entity's pre-operation create 
message that validates the account name is not empty and sets the account number 
prefix to "ACC-" followed by today's date.
```

When the agent finishes, commit as normal:

```bash
git add .
git commit -m "feat: Add account pre-create validation plugin"
```

Entire detects the session and may prompt:

```
Entire: Active Claude Code session detected
  Last prompt: Create a new Dataverse plugin class for the account entity...

Link this commit to session context? [Y]es / [n]o / [a]lways:
```

Press Enter (or `y`). Your first checkpoint is created.

---

## Verifying Your Setup

```bash
# Check Entire status in the repository
entire status

# List checkpoints on the current branch
entire checkpoint list

# View the checkpoint you just created
entire checkpoint explain HEAD
```

The `explain` output shows the full session: prompt, transcript, tool calls, and file changes.

---

## Connecting to Entire.io (Web Dashboard)

To browse your checkpoints visually:

1. Log in at [entire.io](https://entire.io)
2. Connect your repository (GitHub integration)
3. Entire.io reads from the `entire/checkpoints/v1` branch that was pushed with your code

The dashboard shows checkpoint history, full session transcripts, search across all sessions, and the `Entire-Attribution` breakdown per commit.

---

## Installing Entire Skills

Entire Skills are reusable agent workflows for querying session history — Search, Explain, What Happened, Session Handoff, and more. Install them following the [Skills tutorial](https://docs.entire.io/skills/tutorial) for your agent.

Once installed, use them through your normal agent interface:

```
# Through Claude Code after Skills are installed:
> Search for all sessions where we wrote pre-operation plugins
> Explain why this form script uses async OnSave handlers  
> Package a handoff for my current PCF control session
```

---

## Troubleshooting Common Issues

**Hooks not firing on commit**

```bash
entire doctor
# Scan for stuck or misconfigured sessions

entire doctor logs --tail 50
# Show recent operational logs
```

**Session not captured for a session that already happened**

If Entire wasn't enabled when a session started, attach it manually:

```bash
# Get the session ID from your agent's history
entire session attach <session-id> --agent claude-code --force
```

**Checkpoint branch not pushed**

```bash
# Push manually
git push origin entire/checkpoints/v1

# Or re-push with the pre-push hook:
git push
```

**GUI client not triggering hooks**

```bash
entire configure --absolute-git-hook-path
```

**Check overall status**

```bash
entire status --detailed
```

---

## Environment Variables Reference

| Variable | Purpose |
|---|---|
| `ENTIRE_ENABLED=false` | Disable Entire globally without removing hooks |
| `ENTIRE_LOG_LEVEL=debug` | Enable debug logging for a session (`ENTIRE_LOG_LEVEL=debug claude`) |
| `ENTIRE_TELEMETRY_OPTOUT=1` | Opt out of telemetry globally |

---

## Summary: First-Day Checklist for a Power Platform Team

- [ ] Install Entire CLI on each developer machine
- [ ] Run `entire login` on each machine
- [ ] Run `entire enable --agent <name>` in the solution repository root
- [ ] Commit `.entire/settings.json` and `.entire/.gitignore`
- [ ] Configure custom redaction rules for environment GUIDs and connection references
- [ ] Enable PII redaction if the solution processes customer data
- [ ] Configure checkpoint remote if session transcripts need separate governance
- [ ] Run `entire configure --absolute-git-hook-path` for developers using GUI Git clients
- [ ] Install Entire Skills for the agents your team uses
- [ ] Install [Dataverse Skills](https://github.com/microsoft/Dataverse-skills): `/plugin install dataverse@awesome-copilot` (Copilot CLI) or `/plugin install dataverse@claude-plugins-official` (Claude Code) — natural-language Dataverse schema, data, and solution lifecycle operations
- [ ] Install [Power Platform Skills](https://github.com/microsoft/power-platform-skills): `curl -fsSL https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js | node` — adds Power Pages, Model Apps, Code Apps, and Canvas Apps build agents
- [ ] Connect the repository to Entire.io for web dashboard access
- [ ] Run a test session and verify the first checkpoint appears in `entire checkpoint list`

---

*← [Part 1: Why AI Coding Sessions Need a System of Record](https://aidevme.com/entire-io-for-power-platform-developers-why-ai-coding-sessions-need-a-system-of-record/) · [Part 3: Form Scripts & Web Resources →](https://aidevme.com/entire-io-for-power-platform-javascript-typescript-development-form-scripts-and-web-resources/)*

*Documentation: [docs.entire.io](https://docs.entire.io) · Quickstart: [docs.entire.io/quickstart](https://docs.entire.io/quickstart)*
