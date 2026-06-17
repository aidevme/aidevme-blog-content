Microsoft just shipped a new product category at Build 2026: Autopilot agents.

The first one is called Microsoft Scout — and it's meaningfully different from anything Copilot has done before.

Copilot Chat answers questions. Scout takes action. It runs on your desktop, reads and writes your files, executes shell commands, automates a browser with Playwright, queries your entire Microsoft 365 account — and keeps working in the background on a schedule while you're away.

Here's what makes it architecturally interesting:

𝟭. Every Scout agent has its own Entra identity.
Not a shared service account. Not user-delegated context. Its own governed identity with scoped credentials, redacted from logs, managed like a first-party Microsoft service. For anyone who has spent years managing Power Automate service accounts, this is the model we've been waiting for.

𝟮. It can work while you're not there.
Heartbeat mode runs a recurring prompt every 15–120 minutes. Automations trigger on a schedule or condition. Both run under a more restrictive permission policy than interactive sessions. The agent doesn't stop when you close the app.

𝟯. Shell access is tiered, not binary.
Three tiers: auto-approve (ls, git log, docker ps), prompt-before-run (npm install, git push, curl), and deny (rm -rf, format). Customisable. Transparent — Scout shows you the exact command before it runs.

𝟰. The data handling boundary matters.
LLM processing routes through GitHub Copilot — outside the M365 DPA boundary. Data residency, retention, eDiscovery: not covered for that processing path. If you're rolling Scout out in a regulated environment, this is the architecture review conversation to have before deployment, not after.

𝟱. Custom skills use the same ~/.copilot/skills/ pattern as GitHub Copilot.
Write a SKILL.md with your Dataverse conventions, pac CLI patterns, and ALM structure. Scout discovers it automatically at the start of every session. That's practical productivity for Power Platform developers right now.

Access is behind two admin gates (Frontier enrollment + Intune policy + attestation form), requires both M365 Copilot and GitHub Copilot Business/Enterprise licences, and burns GitHub Copilot AI Credits — not standard Copilot Credits. Sign-in fails silently if either gate is incomplete.

It's in Frontier private preview. Desktop only. Not GA. But the architecture decisions here — identity model, tiered permissions, data boundaries — are worth understanding now.

Full breakdown 👇

https://aidevme.com/microsoft-scout-autopilot-agent-complete-guide/

#MicrosoftScout #PowerPlatform #GitHubCopilot #AIAgents #EnterpriseAI #Dataverse #Microsoft365 #MicrosoftBuild