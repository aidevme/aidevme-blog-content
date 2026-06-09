# Twitter / X Thread — Article 70

> Twitter/X limit: 280 characters per post. Format as a numbered thread.

---

**Post 1 / 9 — Hook**
You describe a task to GitHub Copilot Agent mode.

It modifies 12 files in the wrong direction.

The AI wasn't wrong. You just weren't aligned before it started.

Microsoft shipped the Plan agent in Visual Studio to fix this 🧵

#GitHubCopilot #VisualStudio

---

**Post 2 / 9 — What it is**
The Plan agent runs BEFORE any code changes.

→ Scans your codebase read-only
→ Asks clarifying questions
→ Drafts a Markdown plan in .copilot/plans/
→ Waits for your approval

Then — and only then — it implements.

---

**Post 3 / 9 — The plan file**
The plan is a real Markdown file you can:

✏️ Edit directly in the editor
💬 Add constraints as inline comments
📁 Commit to version control
👀 Share for team review before a single file changes

---

**Post 4 / 9 — Prompt tips**
Prompts that produce better plans:

✅ Scope by layer, not by feature
✅ Reference existing patterns in your codebase
✅ State test expectations upfront
✅ Explicitly name what should NOT be touched

The tighter the boundary, the better the plan.

---

**Post 5 / 9 — Real example**
Dataverse plugin refactor with the Plan agent:

Monolithic IPlugin.Execute
→ thin orchestrator plugin
→ testable AccountSyncService
→ Moq unit tests (no live Dataverse needed)

Plan agent designed it. Implementation agent built it. You approved both.

#PowerPlatform #Dataverse

---

**Post 6 / 9 — Decision log**
Over time, .copilot/plans/ becomes a lightweight architectural decision log.

Add status / author / pr frontmatter → you have a record of WHY the code is structured the way it is.

No extra tooling. Just Markdown in a committed folder.

---

**Post 7 / 9 — Pipeline fit**
Where it fits:

Plan agent → Agent mode → Solution Checker → Unit Tests / CI → PR Review → PAC CLI Deploy

It doesn't replace the downstream checks.
It makes the design right before they run.

---

**Post 8 / 9 — Bottom line**
5 minutes at the planning stage saves a much longer cleanup later.

Try it on your next multi-file refactoring task. Write a precise prompt, review the plan, push back, edit it, then implement.

---

**Post 9 / 9 — CTA**
Full article:
→ 5-phase workflow
→ Before/after Dataverse plugin code
→ 4 prompt patterns
→ Official docs links

🔗 https://aidevme.com/think-before-you-build-github-copilots-plan-agent-in-visual-studio-structured-ai-assisted-development/

#GitHubCopilot #VisualStudio #PowerPlatform #AgenticAI #DeveloperProductivity
