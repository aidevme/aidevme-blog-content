# GitHub Copilot Code Reviews Are Now in Azure Repos — What It Actually Means for Teams That Aren't Migrating to GitHub

Microsoft quietly made a move last week that matters more than the announcement suggests.

On June 9, GitHub Copilot code reviews entered limited public preview inside Azure Repos pull requests. Not a roadmap item. Not a "coming soon." A sign-up form you can submit today.

For anyone building on Power Platform and Dataverse inside Azure DevOps — with no near-term plan to migrate — this closes a capability gap that has existed since GitHub Copilot code reviews first shipped on GitHub.com.

---

## Why This Announcement Has More Weight Than It Appears

The direction has been obvious for years: Microsoft ships AI-assisted developer tooling on GitHub first, and Azure Repos follows later (if at all). GitHub Copilot, Copilot Workspace, AI-assisted code review — all landed on GitHub well before Azure Repos saw any of it.

That creates a real problem for enterprise teams. Many organizations building Power Platform solutions are deeply rooted in Azure DevOps. Compliance policies, branching strategies baked into release pipelines, identity federations, ticketing integrations — migration to GitHub is a multi-year conversation at most enterprises, not a sprint. Telling those teams "migrate to GitHub to get AI features" is a non-starter.

This preview is Microsoft acknowledging that reality. They're bringing the capability to where those customers already are.

---

## What the Feature Actually Does

The experience is intentionally close to what exists on GitHub.com. Once enabled, a developer requests a Copilot review from the pull request's Reviewers section — the same UI element used to tag a human colleague. Copilot analyzes the changes and posts inline comments and suggestions asynchronously. When it's done, the status updates to "Review completed." The developer can apply suggestions directly, commit a revision, and request a fresh review.

There is no new interface to learn. No separate tool to open. If you've used Copilot code review on GitHub.com, the mental model transfers directly.

---

## Three Tiers of Control

Enabling the feature requires three toggles, which is the right design for enterprise rollout.

**Organization level** — an org admin enables Copilot Code Review in Organization Settings → Repositories. This is the master gate.

**Repository level** — once the org toggle is on, repo admins enable it per repository. You can target your core Dataverse plugin library and your PCF component repository without enabling it across every repository in a sprawling Azure DevOps organization.

**User level** — individual users enable "Copilot Code Review for Pull Requests" in their Preview Features panel.

This granularity is important. Start narrow, measure cost and coverage, then expand.

---

## Where This Fits in a Power Platform ALM Workflow

This is the practical question, and the answer depends heavily on which part of your Power Platform estate you're looking at.

**Dataverse plugins are the primary target.** Plugins are C#, they follow consistent patterns (IPlugin, execution context, service provider), and they contain a predictable set of common issues: missing null checks on retrieved entity attributes, sync vs. async registration mismatches, hardcoded GUIDs, missing try-catch around service calls. These are exactly the things that slip through when a reviewer is scanning twenty files at the end of a sprint. Copilot will catch them reliably.

**PCF controls in TypeScript and React are a strong second.** TypeScript is a language Copilot understands well. It will flag type assertion abuse, improper updateView lifecycle usage, missing destroy cleanup, and accessibility gaps — all common in PCF codebases that grow quickly under deadline pressure.

**Power Automate flows and canvas apps are not in scope.** This is the expectation to set clearly with your team before rollout. Copilot code review operates on code files. Power Automate flow JSON and canvas app YAML (even when unpacked via pac canvas unpack) are not yet in the picture. The declarative layer of Power Platform stays outside AI-assisted review for now.

The practical recommendation: enable it for your code-centric repositories immediately. Keep your broader solution lifecycle process unchanged.

---

## The Billing Model

Copilot code reviews consume tokens, converted to GitHub AI credits at 1 credit = $0.01 USD. Charges appear on the Azure subscription linked to your Azure DevOps organization and are visible in Azure Cost Management.

There is no fixed per-seat cost. The charge varies by pull request size and lines changed. For Power Platform teams — where plugin and PCF codebases tend to be compact — the per-review cost is likely low. But set up a cost alert before you scale it. You want telemetry from day one, not a surprise on the monthly statement.

---

## Preview Limits to Know Before You Start

The preview runs with deliberate guardrails:

- Repository size: 10 GB maximum
- Changed files per pull request: 100
- Pull request must be Active with no merge conflicts
- 1 review per merge commit
- 5 concurrent reviews per organization
- 2 concurrent reviews per user

For focused Power Platform feature branches, none of these are blockers. The 100-file limit becomes relevant if you're committing full unpacked solution exports — dozens of entity XML files can push that boundary. Consider whether your repository strategy separates code components from solution metadata, and adjust if needed.

---

## How to Get In

The preview uses selective onboarding. Submit your request at the sign-up form Microsoft linked in the announcement and wait for enablement confirmation. Microsoft indicated the preview will run for a couple of months before any broader availability decision.

I've submitted my request and am waiting for access. Once I can run it against a real Dataverse plugin codebase, I'll publish hands-on findings.

---

## The Broader Signal

This preview is worth reading as a statement about Azure Repos' future. AI tooling is arriving there, even if GitHub remains the first-class destination. Teams that have stayed on Azure DevOps for legitimate enterprise reasons are no longer being asked to choose between tooling parity and migration. That's a meaningful shift.

The full setup walkthrough, billing details, and Power Platform workflow breakdown are in the original article on AIDevMe:

https://aidevme.com/github-copilot-code-reviews-are-coming-to-azure-repos-what-it-means-for-power-platform-teams/

---

*If you're running Power Platform ALM on Azure DevOps and working through how AI-assisted tooling fits your workflow, I'd be glad to hear what you're seeing in real engagements.*
