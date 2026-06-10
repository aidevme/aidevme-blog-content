# Substack Article — Article 72

*Canonical URL: https://aidevme.com/github-copilot-code-reviews-are-coming-to-azure-repos-what-it-means-for-power-platform-teams/*

---

# GitHub Copilot Code Review Is Coming to Azure Repos. Here's What That Actually Means.

You know the review cycle problem. A pull request sits in the queue because the one person who knows the plugin code is in meetings. Someone finally reviews it late in the sprint, finds three null reference issues and a hardcoded GUID, and now you're doing a hot-fix cycle that should have been caught three days ago.

AI-assisted code review has been available on GitHub.com for a while now. But if your team is running on Azure DevOps — and many Power Platform teams are, for reasons that don't have a quick answer — that feature has been out of reach.

On June 9, Microsoft announced that GitHub Copilot code review is entering limited public preview inside Azure Repos pull requests. I've already submitted my sign-up request. Once I'm in and have run it against a real Power Platform codebase, I'll write a detailed follow-up. This post is about the announcement itself — what it actually covers, what it costs, and how I see it fitting into a Power Platform ALM workflow.

---

## Why This Announcement Is More Significant Than It Looks

The direction has been clear for years: GitHub is where AI-assisted development tooling ships first. Azure Repos has increasingly felt like the "wait and see" platform. And yet enterprise migrations away from Azure DevOps are slow — compliance requirements, branching strategies baked into pipelines, identity federations, ticketing integrations. The organizations still running Power Platform ALM on Azure DevOps are not moving anytime soon, and Microsoft knows it.

This announcement is a direct acknowledgment of that reality. Rather than holding AI code review hostage to a migration decision, Microsoft is bringing it to where those teams already are. That is a meaningful commitment to Azure DevOps customers, and it's worth recognizing as one.

---

## How It Works

The feature is intentionally simple. A developer opens a pull request in Azure Repos, goes to the Reviewers section — the same place they'd request a human reviewer — and requests a Copilot review. Copilot analyzes the diff and posts inline comments and suggestions asynchronously. The developer can apply suggestions directly or take them back to the IDE. A new commit triggers a fresh review.

There is no new interface to learn. If you've used GitHub Copilot code review on GitHub.com, the mental model is identical.

Enabling it requires three layers: an org admin turns it on for the organization, a repo admin enables it per repository, and individual users activate it in the Preview Features panel. That three-tier model is the right call for a gradual enterprise rollout — you can start with one or two repos rather than flipping it on everywhere.

---

## The Preview Limits That Actually Matter

The preview comes with guardrails that are mostly reasonable. Repository size capped at 10 GB, 100 changed files per pull request, five concurrent reviews per organization, two per user. Pull requests must be Active with no merge conflicts.

For most Power Platform ALM workflows — plugin changes, PCF component updates, a custom API implementation — these limits aren't a practical problem. Where they could bite you is in large solution exports: if you're unpacking full solutions into source control (and you should be), a feature branch that touches dozens of entity XML files could approach the file limit. Worth checking before you roll this out on your solution repository.

---

## The Billing Question

Copilot code reviews consume tokens, converted to GitHub AI credits at $0.01 per credit. The charge lands on the Azure subscription linked to your Azure DevOps organization, visible in Azure Cost Management.

There's no fixed per-seat cost during preview — it's pay-per-use based on PR size. Microsoft's advice is to start with one or two repositories and monitor usage before broadening. That's sound. I'd add: set a cost management alert on this meter from day one, before you've established a baseline. For Power Platform teams with compact plugin and PCF codebases, the actual cost per review is likely to be low. But "likely low" and "instrumented" are different things.

---

## Where It Helps in a Power Platform ALM Workflow

The most valuable target for this feature is Dataverse plugin development. Plugins are C#, they follow well-understood patterns, and Copilot is well-positioned to catch the issues that slip through during a busy sprint review: missing null checks on retrieved entity attributes, sync vs. async plugin registration mismatches, hardcoded GUIDs, missing try-catch around service calls. These aren't architectural issues — they're the kind of things a good reviewer catches on a careful read, but doesn't always catch at the end of a long day.

PCF controls in React and TypeScript are another strong fit. TypeScript is a language Copilot understands deeply. It will catch type assertion abuse, improper `updateView` lifecycle usage, missing `destroy` cleanup, and accessibility gaps.

Power Automate flow JSON and canvas app YAML are a different story. Copilot code review won't touch the declarative layer of your Power Platform solutions until there's meaningful tooling support for reviewing those formats. Keep that expectation clear with your team — this is a code-first feature for now.

---

## A Preview, With Honest Caveats

This is still a preview. Selective onboarding, concurrency limits, and the billing model are all subject to change before broader availability. I've submitted my sign-up request and I'm waiting for access. Once I've run it against real plugin and PCF codebases, I'll publish a hands-on follow-up with concrete findings on what it catches and what it misses.

If you're running Power Platform ALM on Azure DevOps, the sign-up link is in the full article. The fact that this feature is reaching Azure Repos at all — while the Azure-to-GitHub migration conversation is still open at most enterprises — is itself a signal that Azure Repos is not being quietly wound down. That matters for the teams who've built their ALM on it.

[Read the full analysis →](https://aidevme.com/github-copilot-code-reviews-are-coming-to-azure-repos-what-it-means-for-power-platform-teams/)
