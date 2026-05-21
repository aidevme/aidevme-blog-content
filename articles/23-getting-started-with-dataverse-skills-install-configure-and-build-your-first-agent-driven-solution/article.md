# Getting Started with Dataverse Skills: A Guide - Practical AI, Copilot & Modern Development Insights

Estimated reading time: 12 minutes

Ready to build Power Platform solutions with AI? This comprehensive tutorial covers the complete Dataverse Skills installation process for both GitHub Copilot and Claude Code. Learn how to configure PAC CLI authentication, enable the Dataverse MCP server in Managed Environments, and build your first agent-driven solution from a single natural language prompt. Includes enterprise-tested authentication patterns, troubleshooting common errors, and a real-world project tracking system built entirely by AI. Perfect for Power Platform developers transitioning to intent-driven development workflows.

## Table of contents

-   [Introduction](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-introduction)

-   [Prerequisites Checklist](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-prerequisites-checklist)
    -   [Step 1: Install PAC CLI and Configure Authentication](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-step-1-install-pac-cli-and-configure-authentication)
    -   [Step 2: Enable the Dataverse MCP Server](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-step-2-enable-the-dataverse-mcp-server)
    -   [Step 3: Install Dataverse Skills in Claude Code](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-step-3-install-dataverse-skills-in-claude-code)
    -   [Step 4: Install Dataverse Skills in GitHub Copilot](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-step-4-install-dataverse-skills-in-github-copilot)
    -   [Step 5: Configure Python SDK Authentication](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-step-5-configure-python-sdk-authentication)
    -   [Step 6: Your First Intent-Driven Build](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-step-6-your-first-intent-driven-build)
-   [Understanding What Happened Under the Hood](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-understanding-what-happened-under-the-hood)
    -   [Which tools were used and when](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#which-tools-were-used-and-when)
    -   [The skill files at work](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#the-skill-files-at-work)
-   [Common Errors and How to Fix Them](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-common-errors-and-how-to-fix-them)
    -   [Error: “MCP client not allowed in this environment”](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-error-mcp-client-not-allowed-in-this-environment)
    -   [Error: “pac: command not found”](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#error-pac-command-not-found)
    -   [Error: “No active auth profile” in Claude Code](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#error-no-active-auth-profile-in-claude-code)
    -   [Error: Python SDK bulk create fails with 400](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#error-python-sdk-bulk-create-fails-with-400)
    -   [Error: “Table not found in solution”](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#error-table-not-found-in-solution)
-   [Next Steps](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-next-steps)
    -   [Do I need both Claude Code and GitHub Copilot installed?](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-do-i-need-both-claude-code-and-github-copilot-installed)
    -   [Does the agent modify production environments?](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-does-the-agent-modify-production-environments)
    -   [Can I use Dataverse Skills with a trial Power Platform environment?](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-can-i-use-dataverse-skills-with-a-trial-power-platform-environment)
    -   [Can multiple developers share the same Dataverse Skills plugin configuration?](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-can-multiple-developers-share-the-same-dataverse-skills-plugin-configuration)
    -   [What happens if I run the build prompt twice?](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-what-happens-if-i-run-the-build-prompt-twice)
-   [References & Further Reading](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#h-references-amp-further-reading)
    -   [Dataverse Skills](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#dataverse-skills)
    -   [MCP Configuration](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#mcp-configuration)
    -   [PAC CLI](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#pac-cli)
    -   [Python SDK](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#python-sdk)
    -   [Claude Code](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/#claude-code)

## Introduction

In Part 1 of this series – [From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development](https://aidevme.com/from-scripts-to-intent-how-dataverse-skills-redefines-enterprise-development/), we examined the paradigm shift from manual tool orchestration to intent-driven development. The theoretical foundation matters, but enterprise adoption requires practical proof. This article bridges that gap with a production-grade installation guide that accounts for real-world enterprise constraints: Managed Environment policies, authentication complexity, and multi-agent toolchain integration.

The setup process we’re about to walk through reflects lessons learned from early adopter organizations across consulting firms, ISVs, and enterprise CoE teams. I’ve distilled dozens of installation attempts—successful and failed—into the critical path you see here. This isn’t just “how to install”—it’s “how to install correctly the first time in an enterprise context.”

By the end of this article, you will have:

-   The Dataverse MCP server enabled and configured according to enterprise security best practices

-   The Dataverse Skills plugin installed in your preferred coding agent with proper authentication lifecycle management
-   A working Dataverse solution built entirely from natural language—proving the end-to-end workflow

-   Understanding of where this fits in your broader Power Platform governance framework

---

![Prerequisites checklist infographic showing six required components: Managed Environment, PAC CLI, Node.js 18+, Python 3.10+, Azure CLI, and choice of GitHub Copilot or Claude Code with dependency connections](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-prerequisites-checklist-infographic.png?resize=1024%2C683&ssl=1)

## Prerequisites Checklist

Before you start, ensure you have the following:

| **Requirement** | **How to verify** | **Install link** |
| Power Platform environment (Managed) | Admin center → Environments | [Power Platform admin center](https://admin.powerplatform.microsoft.com/) |
| PAC CLI installed | `pac` | [aka.ms/PowerAppsCLI](https://aka.ms/PowerAppsCLI) |
| Node.js 18 or later | `node --version` | [nodejs.org](https://nodejs.org/) |
| Python 3.10 or later | `python --version` | [python.org](https://python.org/) |
| Azure CLI (recommended) | `az --version` | [aka.ms/installazurecliwindows](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) |
| Claude Code CLI **or** GitHub Copilot (VS Code or CLI) | `claude --version / Copilot extension` | See agent sections below |

**Enterprise Reality Check — Managed Environments:** The Dataverse MCP server requires a Managed Environment. This is not a technical limitation—it’s a deliberate architectural decision by Microsoft. Managed Environments provide the governance boundary necessary for agent access: DLP enforcement, usage telemetry, and IP firewall controls. If your developer environment is not managed (common in legacy tenant setups), you have two paths forward: (1) Request environment conversion to Managed status through your Power Platform admin team, or (2) Use the Python SDK and PAC CLI portions of Dataverse Skills exclusively, accepting that MCP-based natural language queries won’t work. In practice, most organizations pursuing Dataverse Skills adoption take path #1—the governance benefits of Managed Environments extend far beyond just agent access.

---

### Step 1: Install PAC CLI and Configure Authentication

#### 1.1 Install PAC CLI

The recommended installation methods:

**Option 1: MSI Installer (Windows – Most Reliable)**

Markdown

```


# Download and run the installer from:


# https://aka.ms/PowerAppsCLI
```

**Option 2: winget (Windows)**

Bash

```
winget install Microsoft.PowerApps.CLI
```

Verify the installation:

Bash

```
pac


# Microsoft PowerPlatform CLI


# Version: 2.2.1+g666525f (.NET Framework 4.8.9325.0)
```

#### 1.2 Authenticate with your tenant

Bash

```
pac auth create --name MyDev
```

This opens a browser window for interactive Azure AD authentication. After sign-in, you will see confirmation of the authentication profile.

**Professional Context:** PAC CLI authentication uses the same OAuth 2.0 device code flow as Azure CLI—a pattern familiar to infrastructure engineers but sometimes new to Power Platform developers coming from maker portal backgrounds. Understanding this flow matters for troubleshooting: if authentication fails, the issue is usually at the Entra ID conditional access policy level, not with PAC CLI itself. Work with your identity team to ensure the “Microsoft PowerApps Checker” enterprise app has the necessary grant permissions in your tenant.

For automation scenarios (CI/CD, service principals):

Bash

```
pac auth create \
  --name MyDev-SPN \
  --applicationId <your-app-id> \
  --clientSecret <your-secret> \
  --tenant <your-tenant-id>
```

#### 1.3 Select your target environment

Bash

```


# List available environments
pac org list

# Select by name or URL
pac org select --environment "Your Dev Environment"

# Verify
pac org who
```

The `pac org who` command is your equivalent of a Dataverse `WhoAmI` request — it confirms which user and environment are active.

#### 1.4 Authenticate with Azure CLI (recommended alongside PAC CLI)

Dataverse Skills’ Connect phase can use Azure CLI as an alternative authentication path, and the Python SDK uses Azure Identity providers. Having Azure CLI authenticated avoids additional prompts:

Bash

```
az login
az account set --subscription "<your-subscription-id>"
```

---

### Step 2: Enable the Dataverse MCP Server

The Dataverse MCP server represents Microsoft’s strategic bet on the Model Context Protocol as the standard for agent-to-data connectivity. Enabled by default for Copilot Studio (Microsoft’s own agent platform), the MCP server requires explicit enablement for third-party clients like GitHub Copilot and Claude Code. This is governance by design, not accident—every external client connection point is a potential security boundary that needs conscious approval.

From an enterprise architecture perspective, this approval gating aligns with zero-trust principles: assume no client has access until explicitly granted, with the approval authority resting with environment admins rather than individual developers.

#### 2.1 Enable in Power Platform Admin Center

1.  Go to [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com/)
2.  Select **Manage → Environments**
3.  Select your target environment
4.  Go to **Settings → Product → Features**
5.  Scroll to **Dataverse Model Context Protocol**
6.  Ensure **Allow MCP clients to interact with Dataverse MCP server** is **On** ![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-enable-model-context-protocol-01.png?resize=1024%2C504&ssl=1)
7.  Click **Advanced Settings**
8.  Enable the specific clients you need: ![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-enable-model-context-protocol-02.png?resize=1024%2C179&ssl=1)
    -   `Microsoft GitHub Copilot` — for VS Code / Copilot CLI
    -   `Dataverse CLI` (App ID: `0c412cc3-0dd6-449b-987f-05b053db9457`) — for Claude Code and other non-Microsoft clients via local proxy

#### 2.2 Find your MCP server URL

Your Dataverse MCP server URL follows this format:

```
https://{your-org-name}.crm.dynamics.com/api/mcp
```

You can find your organization URL in:

-   Power Apps maker portal → Settings (gear icon) → Session details → Instance URL

-   PAC CLI: `pac org who` outputs the environment URL

**Preview endpoint:** There is also a preview endpoint at `/api/mcp_preview` with early-access features. The stable endpoint `/api/mcp` is recommended for general use.

---

### Step 3: Install Dataverse Skills in Claude Code

#### 3.1 Install Claude Code

If you do not have Claude Code installed:

Bash

```
npm install -g @anthropic-ai/claude-code
```

Verify:

Bash

```
claude --version
```

#### 3.2 Install the Dataverse Skills plugin

The automated installer handles prerequisites and registers the plugin:

Bash

```


# Clone the repository
git clone https://github.com/microsoft/Dataverse-skills.git
cd Dataverse-skills

# Run the installer
./install.sh    # macOS/Linux


# or
.\install.ps1   # Windows PowerShell
```

Alternatively, for one-command installation via the marketplace (once available):

Bash

```
claude plugin install microsoft/dataverse-skills
```

#### 3.3 Verify installation

Open Claude Code in your project directory and test the connection:

Bash

```
claude
> Connect to my Dataverse environment and list available solutions
```

Claude Code will invoke the Connect phase skills automatically: discover your PAC CLI auth profiles, select the active environment, and list solutions via the MCP server.

#### 3.4 Claude Code with direct MCP connection (non-proxy)

For direct connection to the Dataverse MCP server (without the local proxy), you need to register an Entra app with `mcp.tools` permissions on the Dynamics CRM API, then configure Claude Code with the MCP URL:

Add to your Claude Code MCP configuration (`~/.claude/mcp_config.json`):

JSON

```
{
  "mcpServers": {
    "DataverseMcp": {
      "type": "http",
      "url": "https://yourorg.crm.dynamics.com/api/mcp"
    }
  }
}
```

---

### Step 4: Install Dataverse Skills in GitHub Copilot

#### 4.1 Prerequisites for GitHub Copilot

-   Visual Studio Code with the GitHub Copilot extension, or

-   GitHub Copilot CLI (`gh copilot`)

#### 4.2 Clone Dataverse Skills Repository

Clone the official Microsoft repository to access the plugin files:

Bash

```


# Clone to a temporary location
git clone https://github.com/microsoft/Dataverse-skills.git /tmp/Dataverse-skills

# Or on Windows:
git clone https://github.com/microsoft/Dataverse-skills.git C:\temp\Dataverse-skills
```

#### 4.3 Copy Plugin Files to Your Repository

Copy the `.github/plugins/dataverse/` directory to your working repository:

Bash

```


# From your project root
cp -r /tmp/Dataverse-skills/.github/plugins/dataverse .github/plugins/

# Windows PowerShell:
Copy-Item -Recurse C:\temp\Dataverse-skills\.github\plugins\dataverse .github\plugins\
```

Your repository structure should now look like:

```
your-repo/
├── .env                                    # Created in Step 2.5
├── .gitignore                              # Add .env to this
├── .vscode/
│   └── mcp.json                           # Will create in next step
├── .github/
│   └── plugins/
│       └── dataverse/                     # Copied from microsoft/Dataverse-skills
│           ├── skills/
│           │   ├── dv-connect/
│           │   ├── dv-solution/
│           │   ├── dv-metadata/
│           │   ├── dv-python-sdk/
│           │   └── dv-overview/
│           ├── scripts/
│           │   └── auth.py               # Uses .env for config
│           └── .github/plugin/
│               └── plugin.json
└── [your code]
```

#### 4.4 Add the Dataverse MCP server in VS Code

1.  Open VS Code
2.  Press `Ctrl+Shift+P` → type `MCP: Add Server` → press Enter
3.  Select **HTTP or Server Sent Events**
4.  Paste your MCP URL: `https://yourorg.crm.dynamics.com/api/mcp`
5.  Press Enter

This generates the MCP server configuration in VS Code’s settings.

#### 4.5 Install via the Awesome Copilot marketplace

The Awesome Copilot marketplace provides a Dataverse plugin that includes an `mcp-configure` skill for interactive setup:

Bash

```


# Add the Awesome Copilot marketplace
copilot plugin marketplace add github/awesome-copilot
```

Then in a Copilot chat session, use the skill:

```
/dataverse:mcp-configure
```

The skill walks you through environment discovery and endpoint selection.

#### 4.6 Configure MCP for Copilot CLI

Edit your Copilot CLI MCP configuration file:

JSON

```
// Global: ~/.copilot/mcp-config.json
// Project: .mcp/copilot/mcp.json
{
  "mcpServers": {
    "DataverseMcp": {
      "type": "http",
      "url": "https://yourorg.crm.dynamics.com/api/mcp"
    }
  }
}
```

#### 4.7 Install Dataverse Skills for Copilot

From the Dataverse Skills repository:

Bash

```


# The install script detects your coding agent<br>./install.sh
```

The installer registers the marketplace with any detected AI coding assistants.

#### 4.8 Verify Python SDK Authentication

Before proceeding, test that the Python SDK can authenticate:

Bash

```
python .github/plugins/dataverse/scripts/auth.py
```

If you see an access token printed (long string starting with `eyJ...`), authentication is working. If you see a device code prompt, complete the browser authentication – this saves the token for future use.

#### 4.9 Commit Plugin Configuration

Bash

```
git add .github/plugins/dataverse .vscode/mcp.json .gitignore
git commit -m "Add Dataverse Skills plugin and MCP configuration"
```

**Why commit these files?**

-   `.github/plugins/` → GitHub Copilot automatically discovers and loads skills from this location

-   `.vscode/mcp.json` → VS Code’s MCP client uses this configuration
-   `.gitignore` → Prevents accidental commit of `.env` with secrets

**Important:** Do NOT commit `.env` – it contains secrets. Verify it’s in `.gitignore`.

#### 4.10 Verify GitHub Copilot Recognizes the Skills

Open VS Code in your repository and start a Copilot Chat session:

```
@workspace What Dataverse skills are available?
```

GitHub Copilot should list the five skills:

-   `dv-connect` – Authentication and environment discovery

-   `dv-solution` – Solution lifecycle management
-   `dv-metadata` – Table/column/relationship creation

-   `dv-python-sdk` – Data operations and bulk loading
-   `dv-overview` – Overview of all capabilities

#### 4.11 Test MCP Connection

In Copilot Chat, test the MCP connection:

If successful, Copilot will:

1.  Read your PAC CLI authentication profile
2.  Connect to the MCP server at the URL in `.vscode/mcp.json`
3.  List tables from your environment

**Common Issues:**

-   “MCP client not allowed” → Enable GitHub Copilot in Power Platform Admin Center

-   “No active auth profile” → Run `pac auth create` and `pac org select`
-   “Connection refused” → Verify MCP URL in `.vscode/mcp.json` matches your environment

### Step 5: Configure Python SDK Authentication

The Dataverse Skills plugin uses the Python SDK for metadata operations and data loading. This step is **critical** – without it, the “operate” phase (loading sample data, running queries) will fail with authentication errors.

#### 5.1 Install Python SDK Dependencies

**Option 1: Global Installation**

Bash

```
pip install PowerPlatform-Dataverse-Client azure-identity python-dotenv
```

**Option 2: Virtual Environment (Recommended)**

Bash

```


# Create virtual environment
python -m venv .venv

# Activate it


# Windows:
.venv\Scripts\activate


# macOS/Linux:
source .venv/bin/activate

# Install packages
pip install PowerPlatform-Dataverse-Client azure-identity python-dotenv
```

#### 5.2 Create `.env` File

The `auth.py` script in the Dataverse Skills plugin requires a `.env` file at your repository root:

Bash

```


# Create .env in your project root
touch .env  # macOS/Linux


# or
New-Item .env  # Windows PowerShell
```

Add the following content:

Markdown

```
DATAVERSE_URL=https://yourorg.crm17.dynamics.com
TENANT_ID=common

# Optional: Service Principal for non-interactive authentication


# CLIENT_ID=<your-app-registration-client-id>


# CLIENT_SECRET=<your-app-registration-secret>
```

 **Important**: Add `.env` to your `.gitignore` to avoid committing secrets:

Bash

```
echo ".env" >> .gitignore
```

#### 5.3 Authentication Options

**Option A: Interactive Device Code Flow (Default)**

Without `CLIENT_ID` and `CLIENT_SECRET`, the SDK uses interactive device code authentication:

Bash

```


# Test authentication (after installing plugin in Step 4)
python .github/plugins/dataverse/scripts/auth.py
```

On first run, you’ll see:

Markdown

```
To sign in, visit https://login.microsoft.com/device and enter code: ABC123XYZ
(Waiting for you to complete the login in your browser...)
```

After authentication, the token is cached in your OS credential store (Windows Credential Manager, macOS Keychain, Linux libsecret). Subsequent runs will use silent refresh.

**Option B: Service Principal (Automated/CI/CD)**

For automation scenarios, create an Azure App Registration:

1.  **Azure Portal** → **Azure Active Directory** → **App registrations** → **New registration**
2.  Name: “Dataverse CLI” (or any name)
3.  Copy the **Application (client) ID** → This is your `CLIENT_ID`
4.  Go to **Certificates & secrets** → **New client secret** → Copy the **Value** → This is your `CLIENT_SECRET`
5.  Go to **API permissions** → **Add permission** → **Dynamics CRM** → **Delegated permissions** → Add `user_impersonation`
6.  Click **Grant admin consent**

Add to your `.env`:

Markdown

```
CLIENT_ID=<your-app-id>
CLIENT_SECRET=<your-secret>
```

With service principal configured, authentication is fully non-interactive – no browser prompts.

### Step 6: Your First Intent-Driven Build

With everything configured, let’s build a real Dataverse solution from a single prompt.

**The prompt**

Open your coding agent (Claude Code or GitHub Copilot agent mode) in your working directory and type:

Markdown

```
I need a simple project tracking system for a consulting firm. 
Create tables for Projects, Clients, Consultants, and Assignments 
(with a many-to-many between Projects and Consultants). 
Add a status choice column to Projects with values: 
Proposal, Active, On Hold, Completed. 
Use the publisher prefix 'aidevme'. 
Create everything in a solution called 'ConsultingTracker', 
load 10 realistic sample records per table, 
and show me all active projects with their assigned consultants.
```

**What the agent does (observable steps)**

**Connect phase:**

Bash

```
> Checking PAC CLI authentication...
> Active profile: MyDev → https://yourorg.crm.dynamics.com<br>> Registering Dataverse MCP server...
> MCP connection established. 23 tables available.
```

**Build phase:**

Bash

```
> Creating solution 'ConsultingTracker' (publisher: aievme)...
> Creating table: aidevme_Project<br>>   + Text column: aidevme_projectname + Choice column: aidevme_status (Proposal | Active | On Hold | Completed) + Currency column: aidevme_budget
> Creating table: aidevme_Client
> Creating table: aidevme_Consultant
> Creating table: aidevme_Assignment (Activity table, M:N junction)
> Creating relationship: aidevme_project_consultant (M:N)
> Adding all components to ConsultingTracker solution...
```

**Operate phase:**

Bash

```
> Generating sample data script (Python)...<br>> Creating 10 Client records...
> Creating 10 Consultant records...
> Creating 10 Project records...
> Creating Assignment relationships...
> Running query: Active projects with assigned consultants...
```

**Result:**

Bash

```
Active Projects and Assigned Consultants:<br><br>Project: "Digital Transformation – Stadtwerke Basel" Status: Active | Budget: CHF 450,000 Consultants: Klaus Weber (Senior Architect), Petra Müller (Developer) Project: "CRM Migration – Schweizer Bank AG" Status: Active | Budget: CHF 280,000 Consultants: Andreas Huber (Solution Architect) [... 3 more active projects]
```

The entire operation — from empty environment to queryable data — in a single prompt.

---

![Dual-panel diagram showing tool selection logic mapping different operations (environment discovery, solution creation, data generation) to appropriate tools (PAC CLI, Web API, MCP, Python SDK) alongside skill file directory structure with connect, build, and operate folders](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-tool-selection-logic-and-file-structure.png?resize=993%2C1024&ssl=1)

## Understanding What Happened Under the Hood

The agent just built a complete Dataverse solution from a single natural language prompt—but understanding *how* it made those decisions matters for production use. This section dissects the tool selection logic, revealing which operations triggered PAC CLI versus Web API versus MCP calls, and why those choices optimize for both correctness and performance. Transparency into agent decision-making transforms this from “magic” into predictable, governable infrastructure.

### Which tools were used and when

The agent selected tools based on the operation type:

| **Operation** | **Tool used** | **Why** |
| Environment discovery | PAC CLI (`pac org list`) | Authoritative source for environment metadata |
| Solution creation | PAC CLI (`pac solution create`) | Native ALM operation |
| Table/column creation | Dataverse Web API (OData) | Full schema control, supports all column types |
| MCP registration | `@microsoft/dataverse` npm package | Local proxy for Claude Code connectivity |
| Metadata reads during build | Dataverse MCP (`describe_table`) | Fastest path for read-only schema queries |
| Sample data generation | Dataverse Python SDK | Bulk operations (`CreateMultiple`) for efficiency |
| Analytical query | Dataverse MCP (`read_query`) | Natural language to OData translation |

### The skill files at work

You can inspect exactly which skills the agent loaded by examining the repository:

```
Dataverse-skills/
└── .github/plugins/dataverse/skills/
    ├── connect/
    │   ├── authenticate.md
    │   └── mcp-register.md
    ├── build/
    │   ├── create-solution.md
    │   ├── create-table.md
    │   ├── create-column.md
    │   └── create-relationship.md
    └── operate/
        ├── load-data.md
        └── query.md
```

Each file contains structured instructions that the agent interprets, including safety checks (for example, the build skills warn against creating tables with the same logical name as system tables).

---

![Troubleshooting flowchart displaying five common Dataverse Skills errors (MCP client not allowed, PAC CLI not found, no auth profile, Python SDK 400, table not in solution) with visual diagnostic paths leading to specific solutions and fix commands](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-common-errors-troubleshooting-flowchart.png?resize=842%2C1024&ssl=1)

## Common Errors and How to Fix Them

Even with careful setup, enterprise environments introduce variables that can cause installation issues. Here are the five most common errors encountered during Dataverse Skills installation, with diagnostic steps and verified fixes from production deployments.

### Error: “MCP client not allowed in this environment”

**Cause:** The MCP client (GitHub Copilot or Dataverse CLI) has not been enabled in the Power Platform Admin Center.

**Fix:** Follow Step 2.1 above. Enable the specific client app ID for your environment.

### Error: “pac: command not found”

**Cause:** PAC CLI is not on your PATH, or only installed via the VS Code extension.

**Fix:** Install via .NET tool (`dotnet tool install`) or add the extension’s bin directory to your system PATH.

### Error: “No active auth profile” in Claude Code

**Cause:** The Dataverse Skills Connect phase could not find a valid PAC CLI authentication profile.

**Fix:**

Bash

```
pac auth create --name DevProfile
pac org select --environment "Your Environment Name"
pac org who  # Verify the active context
```

### Error: Python SDK bulk create fails with 400

**Cause:** Likely missing alternate key configuration for upsert operations, or incorrect column logical names (remember the publisher prefix).

**Fix:** Verify column logical names match your publisher prefix:

Bash

```


# Wrong — missing publisher prefix<br>client.records.create("project", [{"name": "Test"}])<br><br># Correct<br>client.records.create("aiddevme_project", [{"aidevme_projectname": "Test"}])
```

### Error: “Table not found in solution”

**Cause:** The build skill created the table but failed to add it to the solution before the operate phase ran.

**Fix:** Manually add the table to the solution:

Bash

```
pac solution add-solution-component \
  --solutionUniqueName ConsultingTracker \
  --component aidevme_project \
  --componentType 1
```

---

![Learning path roadmap showing completed installation phase with 100% progress, two branching paths for Part 3 technical deep dive and Part 4 enterprise architecture, plus three experimental prompts for custom views, CSV import, and data profiling](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-learning-path-next-steps-roadmap.png?resize=683%2C1024&ssl=1)

## Next Steps

Completing this installation represents more than technical setup—you’ve established the foundation for intent-driven development in your Power Platform practice. The workflow you just proved end-to-end (natural language to deployed solution) scales to production scenarios with the right governance patterns. Here’s how to build on this foundation both immediately and strategically.

You now have a working Dataverse Skills setup. In the next articles in this series, we go deeper:

-   **Part 3** — The technical internals: [how skill Markdown files work, tool selection logic, and how to write your own custom skills](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/)

-   **Part 4** — Enterprise architecture view: [Managed Environments, MCP billing, ALM pipelines, and governance considerations](https://aidevme.com/dataverse-skills-for-enterprise-architects-governance-alm-mcp-billing-and-production-readiness/)

To experiment further right now, try these prompts:

Bash

```
Add a view showing projects by status 
Add a public view to the aidevme_Project table that groups projects by status and shows project name, client, total budget, and assigned consultant count.
Import from CSV Import the attached projects.csv file into the aidevme_Project table, mapping the 'project_title' column to aidevme_projectname and 'state' to the aidevme_status choice column. 
Profile data quality Profile the data quality of all tables in the ConsultingTracker solution and report on null percentages and value distributions.
```

---

## Frequently Asked Questions

### Do I need both Claude Code and GitHub Copilot installed?

No. Dataverse Skills works with either agent. Install whichever you use. The plugin covers both agents with the same skill files.

### Does the agent modify production environments?

The agent uses whichever authentication profile and environment are active in your PAC CLI context. Always verify `pac org who` before running prompts. It is strongly recommended to use dedicated development environments, not production.

### Can I use Dataverse Skills with a trial Power Platform environment?

Yes for the PAC CLI and Python SDK portions. The MCP server requires a Managed Environment, which trial environments typically are not. Check your environment type in the admin center.

Yes. The plugin files live in the repository (`.claude-plugin/` and `.github/plugins/` directories). Commit the configuration alongside your solution source. Each developer authenticates independently via their own PAC CLI profiles.

### What happens if I run the build prompt twice?

The build skills include safety checks that detect existing tables and columns. They will warn you before creating duplicates. If a component already exists with the correct schema, the skill skips creation. This makes the prompts largely idempotent.

---

## References & Further Reading

### Dataverse Skills

-   [Dataverse Skills GitHub Repository](https://github.com/microsoft/Dataverse-skills)

-   [Getting Started Guide](https://github.com/microsoft/Dataverse-skills#getting-started)
-   [Full Skill Catalog](https://github.com/microsoft/Dataverse-skills/tree/main/.github/plugins/dataverse/skills)

-   [Contributing Guide](https://github.com/microsoft/Dataverse-skills/blob/main/CONTRIBUTING.md)

### MCP Configuration

-   [Connect to Dataverse with MCP (Microsoft Learn)](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp)

-   [Configure the Dataverse MCP server](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp-disable)
-   [Connect Dataverse MCP with GitHub Copilot in VS Code](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp-vscode)

-   [Connect to Dataverse MCP from non-Microsoft clients](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp-other-clients)

### PAC CLI

-   [Power Platform CLI introduction](https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction)

-   [pac auth command reference](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/auth)
-   [pac solution command reference](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/solution)

### Python SDK

-   [Dataverse SDK for Python overview](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/sdk-python/overview)

-   [PowerPlatform-Dataverse-Client on PyPI](https://pypi.org/project/PowerPlatform-Dataverse-Client/)
-   [Python SDK GitHub Repository](https://github.com/microsoft/PowerPlatform-DataverseClient-Python)

### Claude Code

-   [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code/overview)

-   [Claude Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

---

*Previous: [Part 1 — From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development](https://aidevme.com/from-scripts-to-intent-how-dataverse-skills-redefines-enterprise-development/)*  
*Next: [Part 3 — Under the Hood: Skill Markdown Format, Tool Selection Logic, and Writing Your Own Skills](https://file+.vscode-resource.vscode-cdn.net/c%3A/aidevme/aidevme-blog/draft-articles/dataverse-skills/article-02.md#)*

### *Related*

[![Split-screen illustration showing developer transformation from traditional Power Platform development with multiple tools and context-switching to streamlined AI-assisted development with Dataverse Skills using natural language intent](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-intent-driven-development-transformation.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/from-scripts-to-intent-how-dataverse-skills-redefines-enterprise-development/ "From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development")

#### [From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development](https://aidevme.com/from-scripts-to-intent-how-dataverse-skills-redefines-enterprise-development/ "From Scripts to Intent: How Dataverse Skills Redefines Enterprise Development")

Microsoft's Dataverse Skills represents a paradigm shift in Power Platform development—from manual tool orchestration to intent-driven AI coding. This open-source plugin for GitHub Copilot and Claude Code eliminates the developer tax of context-switching between PAC CLI, maker portal, and API documentation. Instead of writing scripts, developers describe their intent in…

April 3, 2026

In "AI & Copilot"

[![Dataverse Skills internal architecture diagram showing AI agent connected to three tools: Python SDK, PAC CLI, and MCP Server with YAML code snippets and data flow visualization](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/dataverse-skills-part-03-under-the-hood-architecture-featured.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/ "Under the Hood: How Dataverse Skills Work and How to Write Your Own")

#### [Under the Hood: How Dataverse Skills Work and How to Write Your Own](https://aidevme.com/under-the-hood-how-dataverse-skills-work-and-how-to-write-your-own/ "Under the Hood: How Dataverse Skills Work and How to Write Your Own")

Understand the engineering decisions behind Dataverse Skills and learn to build your own custom skills for organizational patterns. This advanced guide dissects both skill file formats (Microsoft's table format and extended YAML frontmatter), explains how AI agents select and chain skills, and reveals the three-tool strategy (MCP Server, Python SDK,…

April 10, 2026

In "AI & Copilot"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [Getting Started with Dataverse Skills: Install, Configure, and Build Your First Agent-Driven Solution](https://aidevme.com/getting-started-with-dataverse-skills-install-configure-and-build-your-first-agent-driven-solution/)