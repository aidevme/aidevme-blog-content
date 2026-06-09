# Bluesky Thread — Article 70

> Bluesky limit: 300 characters per post. Format as a thread.

---

**Post 1 / 8**
You describe a task to GitHub Copilot Agent mode.
It modifies 12 files in directions you didn't intend.

The AI wasn't wrong. You just weren't aligned before it started.

Microsoft shipped the Plan agent in Visual Studio to fix this. 🧵

---

**Post 2 / 8**
The Plan agent runs *before* any code changes.

It scans your codebase read-only, asks clarifying questions, and drafts a step-by-step Markdown plan saved to `.copilot/plans/`.

You review it. Edit it. Approve it. Then — and only then — it implements.

---

**Post 3 / 8**
The plan is a real file you can:

→ Edit directly in the editor
→ Add constraints as inline comments
→ Commit to version control as a design decision record
→ Share with a colleague for sign-off before a single file changes

---

**Post 4 / 8**
Prompts that work well:

✅ Scope by layer, not by feature
✅ Reference existing patterns in your codebase
✅ State test coverage expectations upfront
✅ Explicitly name what should NOT be touched

The more you define the boundary, the tighter the plan.

---

**Post 5 / 8**
Real example: Dataverse plugin refactor.

Monolithic IPlugin.Execute → thin orchestrator plugin + testable AccountSyncService + Moq unit tests.

No live Dataverse needed in tests. Plan agent produced the structure. Implementation agent filled in the code.

---

**Post 6 / 8**
Over time, `.copilot/plans/` becomes a lightweight architectural decision log.

Add `status`, `author`, `pr` frontmatter to each plan file and you have a record of *why* the code is structured the way it is — without any extra tooling.

---

**Post 7 / 8**
Where it fits in the enterprise pipeline:

Plan agent → Agent mode → Solution Checker → Unit Tests / CI → PR Review → PAC CLI Deploy

It doesn't replace the downstream checks. It just makes the design right before they run.

---

**Post 8 / 8**
Full article — 5-phase workflow, before/after Dataverse plugin code, 4 prompt patterns, official docs links:

🔗 https://aidevme.com/think-before-you-build-github-copilots-plan-agent-in-visual-studio-structured-ai-assisted-development/

#GitHubCopilot #VisualStudio #PowerPlatform #Dataverse
