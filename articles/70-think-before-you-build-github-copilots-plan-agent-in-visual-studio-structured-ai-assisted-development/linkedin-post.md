# LinkedIn Post — Article 70

---

# How much time have you spent cleaning up after GitHub Copilot Agent mode this month? # 

Not because the AI was wrong. But because you were never properly aligned with it before it started touching files.

Microsoft shipped the **Plan agent** in Visual Studio in May 2026 — and it's a direct answer to that exact problem.

Instead of jumping straight to implementation, the Plan agent:

→ Scans your codebase in read-only mode
→ Asks targeted clarifying questions
→ Produces a step-by-step Markdown plan saved to `.copilot/plans/`
→ Waits for your approval before touching a single file

You review the plan. Edit it directly. Add constraints. Commit it to version control as a decision log. Then — and only then — you click Implement.

I wrote a complete guide covering:

✅ The 5-phase workflow (Describe → Scan → Draft → Edit → Implement)
✅ Prompt patterns that produce genuinely useful plans
✅ A real Dataverse plugin refactoring scenario with before/after code
✅ How `.copilot/plans/` becomes a lightweight architectural decision log for your team

👇 Drop a comment — what's your biggest frustration with agentic AI in a multi-file codebase? Curious whether this matches what others are running into.

🔗 https://aidevme.com/think-before-you-build-github-copilots-plan-agent-in-visual-studio-structured-ai-assisted-development/

---

#GitHubCopilot #VisualStudio #PowerPlatform #Dataverse #AgenticAI #DeveloperProductivity #EnterpriseDevlopment #AIAssistedDevelopment
