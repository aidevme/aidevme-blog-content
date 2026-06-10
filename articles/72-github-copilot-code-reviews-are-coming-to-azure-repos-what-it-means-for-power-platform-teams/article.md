# GitHub Copilot Code Reviews Are Coming to Azure Repos — What It Means for Power Platform Teams

**Published:** June 10, 2026  
**Tags:** GitHub Copilot, Azure DevOps, Azure Repos, ALM, Power Platform, Code Review

**URL:** https://aidevme.com/github-copilot-code-review-azure-repos-power-platform/

**WordPress SEO**
- **Focus keyphrase:** GitHub Copilot code review Azure Repos
- **SEO title:** GitHub Copilot Code Review for Azure Repos — Power Platform ALM Guide
- **Meta description:** GitHub Copilot code review is now in Azure Repos preview. Learn how to enable it, what it costs, and how it fits your Power Platform ALM workflow.
- **Slug:** github-copilot-code-review-azure-repos-power-platform
- **Excerpt:** GitHub Copilot code review is entering limited public preview inside Azure Repos pull requests. This guide covers three-tier setup, billing on your Azure subscription, preview limits, and how to integrate AI-assisted code review into Power Platform ALM workflows for Dataverse plugins and PCF controls.

---

Microsoft announced on June 9 that GitHub Copilot code reviews are entering a limited public preview directly inside Azure Repos pull requests. If your team is still on Azure DevOps and has no near-term migration plan to GitHub, this is worth paying attention to — not because it solves every ALM challenge Power Platform teams face, but because it closes a gap that has quietly frustrated developers for years.

Let me walk you through what was announced, what it actually means in practice, and how I see it fitting into a modern Power Platform ALM workflow.

---

## Table of Contents

- [The Context: Why This Matters More Than It Looks](#the-context-why-this-matters-more-than-it-looks)
- [What Was Announced](#what-was-announced)
- [Setup: Three Layers of Enablement](#setup-three-layers-of-enablement)
- [Preview Limits Worth Knowing](#preview-limits-worth-knowing)
- [Billing: AI Credits on Your Azure Subscription](#billing-ai-credits-on-your-azure-subscription)
- [What This Means for Power Platform ALM Workflows](#what-this-means-for-power-platform-alm-workflows)
- [How to Sign Up](#how-to-sign-up)
- [My Take](#my-take)
- [Resources](#resources)
- [References](#references)

---

## The Context: Why This Matters More Than It Looks

Microsoft has been steering customers toward GitHub for a while. The direction is no secret — GitHub is where AI-assisted development tooling gets shipped first, and Azure Repos has increasingly felt like the "wait and see" option. But enterprise migrations are slow. Compliance requirements, branching strategies baked into release pipelines, identity federations, ticketing integrations — all of these create real drag. Many organizations building on Power Platform and Dataverse are still firmly on Azure DevOps, running Power Platform Build Tools pipelines, and they are not moving anytime soon.

This announcement is a direct acknowledgment of that reality: GitHub Copilot code review is now coming to Azure Repos, not just as a future promise, but as a preview you can sign up for today.

---

## What Was Announced

The feature brings GitHub Copilot's code review capability into Azure Repos pull requests. Once enabled, a developer can explicitly request a Copilot review directly from the pull request's Reviewers section, the same place you'd request a human colleague. Copilot then analyzes the changes and posts inline comments and suggestions, just as a human reviewer would.

The review runs asynchronously. Depending on repository and pull request size, it takes a moment to complete, after which the status changes to "Review completed." From there, the developer can apply Copilot's suggested changes directly, or take them back to the IDE and commit a revision. After a new commit lands, a fresh Copilot review can be requested again.

It's intentionally simple. There is no new interface to learn. If you've used GitHub Copilot code review on GitHub.com, you already understand the mental model.

---

## Setup: Three Layers of Enablement

Getting the feature running requires enabling it at three levels, which makes sense for enterprise rollout — you want control over where AI-assisted tooling is active.

### Organization Level

An organization administrator goes to Organization Settings → Repositories and enables Copilot Code Review for the organization. This is the gate that allows the feature to exist at all.

### Repository Level

Once the organization toggle is on, individual repository administrators can enable the feature per repository via Project → Repositories → Manage Repositories. This is the right granularity. You probably don't want this running across every repository in a sprawling Azure DevOps organization on day one.

### User Level

Finally, individual users (or an org admin on their behalf) turn on "Copilot Code Review for Pull Requests" in the Preview Features panel. Users control their own experience.

This three-tier model is thoughtful. It means your Platform team can enable the feature for selected repos — say, your core Dataverse plugin library or your PCF component repository — without flipping it on everywhere at once.

---

## Preview Limits Worth Knowing

The preview comes with guardrails that reflect a cautious rollout rather than a production-ready feature. The key ones to be aware of:

<figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr><td><strong>Constraint</strong></td><td><strong>Limit</strong></td></tr><tr><td>Repository size</td><td>10 GB max</td></tr><tr><td>Changed files per pull request</td><td>100 files</td></tr><tr><td>Pull request state</td><td>Must be Active</td></tr><tr><td>Merge status</td><td>Must have no conflicts</td></tr><tr><td>Reviews per PR version</td><td>1 per merge commit</td></tr><tr><td>Concurrent reviews per org</td><td>5</td></tr><tr><td>Concurrent reviews per user</td><td>2</td></tr></tbody></table></figure>

For most Power Platform ALM workflows — where pull requests typically touch a solution export diff, a small set of plugin files, or a PCF component — these limits are not a practical blocker. The 100-file limit is generous enough for a focused feature branch. Where it could become an issue is in large solution exports that include dozens of unpacked entity XML files. If you're unpacking full solutions into source control (as you should be), be mindful of that boundary.

---

## Billing: AI Credits on Your Azure Subscription

This is the part organizations will need to communicate clearly to finance teams. Copilot code reviews consume tokens, and those tokens are converted to GitHub AI credits at a rate of 1 credit = $0.01 USD. The charges appear on the Azure subscription linked to your Azure DevOps organization, visible in Azure Cost Management.

There is no fixed per-seat cost during preview. The cost varies based on pull request size and number of lines changed. Microsoft's advice — start with one or two repositories and monitor daily usage before broader rollout — is sound. It also means you should add a cost management alert for this new meter from day one.

For Power Platform teams, the actual cost per review is likely to be low, since plugin and PCF codebases tend to be compact compared to large application repositories. But instrument it before you scale it.

---

## What This Means for Power Platform ALM Workflows

If you're running Power Platform ALM on Azure DevOps — solution unpacking, automated build and deploy pipelines with Power Platform Build Tools, managed solution promotion across environments — here is how I see this fitting in.

### Dataverse Plugin Development

Dataverse plugin development is the most obvious target for this feature. Plugins are C#, they follow consistent patterns (IPlugin, execution context, service provider), and Copilot is well-positioned to catch common issues: missing null checks on retrieved entity attributes, sync vs. async plugin registration mismatches, hardcoded organization-specific GUIDs, missing try-catch around service calls. These are exactly the kinds of things that slip through when a reviewer is scanning twenty files in a PR at the end of a sprint.

### PCF Controls

PCF controls built in React and TypeScript are another strong fit. TypeScript is one of the languages Copilot understands deeply. It will catch type assertion abuse, improper use of `updateView` lifecycle, missing `destroy` cleanup, and accessibility gaps — all common in PCF codebases that grow quickly under deadline pressure.

### Power Automate Cloud Flows

Power Automate Cloud Flows and canvas app YAML are a different story. Until there is meaningful AI-assisted review of Power Automate flow JSON or canvas app source (unpacked via pac canvas unpack), Copilot code review will not touch the declarative layer of your Power Platform solutions. Keep that expectation clear with your team.

### Custom APIs and Dataverse Actions

Custom APIs and Dataverse Actions defined as code components (function/action implementations) are in scope to the extent they surface in C# or TypeScript files. The Dataverse metadata layer itself remains outside AI code review.

In short: adopt this for your code-centric repositories now. Keep the broader solution lifecycle process as-is.

---

## How to Sign Up

The preview is accessed through a sign-up form — Microsoft is onboarding organizations selectively and monitoring telemetry before broader availability. If you want in, [submit your request here](https://nam.dcv.ms/VeDNq3VRhX) and wait for enablement confirmation.

Microsoft indicated the preview will run for a couple of months before any broader availability decision. That is enough runway to test it properly on a real-world codebase.

---

## My Take

This is a pragmatic move by Microsoft, and I think it's the right one. Rather than telling Azure Repos customers "migrate to GitHub to get AI features," they're bringing a meaningful capability to where those customers already are. The feature itself is not experimental — GitHub Copilot code reviews have been live on GitHub.com, and the engine is proven. Bringing it into the Azure Repos pull request UI is largely a surface-area question, and that surface now exists.

For Power Platform architects managing enterprise ALM, my recommendation is clear: sign up for the preview, enable it on your plugin or PCF repository, and build it into your PR process for code-heavy components. It won't replace architectural review or domain knowledge, but it will catch a class of issues that slow down review cycles and create regression risk.

The fact that this is showing up now — while the Azure-to-GitHub migration conversation is still open at most enterprises — is itself a signal. Azure Repos is not being abandoned. AI tooling will increasingly reach it, even if GitHub remains the first-class destination.

---

## Resources

- [Official announcement — Azure DevOps Blog](https://devblogs.microsoft.com/devops/copilot-code-reviews-for-azure-repos/)
- [Sign up for the limited public preview](https://nam.dcv.ms/VeDNq3VRhX)
- [Power Platform Build Tools for Azure DevOps](https://learn.microsoft.com/en-us/power-platform/alm/devops-build-tools)
- [pac solution unpack — Power Platform CLI](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/solution)

---

## References

- Varga, Z. (2026, June 10). *GitHub Copilot Code Reviews Are Coming to Azure Repos — What It Means for Power Platform Teams*. AIDevMe. https://aidevme.com/github-copilot-code-review-azure-repos-power-platform/
- Microsoft. (2026, June 9). *Copilot Code Reviews for Azure Repos*. Azure DevOps Blog. https://devblogs.microsoft.com/devops/copilot-code-reviews-for-azure-repos/

---

*Have thoughts on how you're using AI-assisted code review in your Power Platform ALM pipeline? I'd love to hear from you — reach out on LinkedIn or drop a comment below.*
