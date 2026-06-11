# Claude Fable 5 in GitHub Copilot — Technical Breakdown for Power Platform and Enterprise Teams

**WordPress SEO**
- **Focus keyphrase:** Claude Fable 5 GitHub Copilot
- **SEO title:** Claude Fable 5 in GitHub Copilot — Technical Breakdown for Power Platform and Enterprise Teams
- **Meta description:** Claude Fable 5 — Anthropic's first Mythos-class model — is now GA in GitHub Copilot. Technical specs, the Opus 4.8 fallback mechanism, 30-day retention, and what enterprise Power Platform teams need before enabling it.
- **Slug:** claude-fable-5-github-copilot-technical-breakdown
- **Excerpt:** Claude Fable 5 is Anthropic's first Mythos-class model and it's now generally available in GitHub Copilot. This breakdown covers the technical specs, the built-in Opus 4.8 fallback mechanism, the 30-day data retention requirement that breaks standard ZDR assumptions, and a practical enablement framework for Power Platform and enterprise teams operating under data governance constraints.

---

On June 9, GitHub announced that **Claude Fable 5** is generally available in GitHub Copilot. This isn't just another entry in the model picker. Fable 5 is the first model in Anthropic's new **Mythos class** — a capability tier that sits *above* Opus. It arrives with behaviors that change how you think about model selection in an enterprise context.

There are three things that make this release different from the usual "new model dropped" cycle:

1. **It's a genuinely different capability tier**, built for long-horizon autonomous work rather than chat-style completions.
2. **It ships with a built-in safeguard layer** that silently falls back to Claude Opus 4.8 on certain request types — behavior you've never had to reason about before.
3. **It's off by default in Copilot and requires 30-day data retention**, breaking the Zero Data Retention assumption most enterprise Copilot rollouts were approved under.

Data residency and retention questions surface in *every* architecture review for DACH and Benelux enterprise teams. That combination makes Fable 5 the first Copilot model where selection is a governance decision, not just a capability one.

Let's go through the technical detail, then the enablement framework.

---

## Table of Contents

- [What Claude Fable 5 Actually Is](#what-claude-fable-5-actually-is)
  - [Performance benchmarks at launch](#performance-benchmarks-at-launch)
- [The Technical Specs That Matter for Builders](#the-technical-specs-that-matter-for-builders)
- [The Fallback Mechanism — The Part That's Genuinely New](#the-fallback-mechanism--the-part-thats-genuinely-new)
  - [What this means for Power Platform teams](#what-this-means-for-power-platform-teams)
- [Where You'll Find It in Copilot](#where-youll-find-it-in-copilot)
- [The Data Retention Requirement — Read This Before Enabling](#the-data-retention-requirement--read-this-before-enabling)
  - [What the retention window actually means](#what-the-retention-window-actually-means)
- [My Take: How to Handle the Enablement Decision](#my-take-how-to-handle-the-enablement-decision)
  - [Treat It as a Scoped Rollout, Not a Tenant-Wide Switch](#treat-it-as-a-scoped-rollout-not-a-tenant-wide-switch)
  - [Put Model-Level Data Handling in Your AI Usage Register](#put-model-level-data-handling-in-your-ai-usage-register)
  - [Don't Let the Retention Discussion Bury the Capability Discussion](#dont-let-the-retention-discussion-bury-the-capability-discussion)
  - [Pilot with a Measurable Workload](#pilot-with-a-measurable-workload)
- [Key Takeaways](#key-takeaways)

---

## What Claude Fable 5 actually is

Anthropic launched Fable 5 on June 9, 2026, describing it as a Mythos-class model made safe for general use. The backstory matters for understanding the safeguards. Anthropic previewed **Claude Mythos** in April to a limited set of partners through Project Glasswing. Anthropic considered it too dangerous for open release. The model proved unusually good at finding and exploiting vulnerabilities across major operating systems and browsers.

Fable 5 is the *same underlying model* as the now-upgraded Claude Mythos 5, wrapped in a classifier layer. The two names exist purely to distinguish the safeguarded public model (Fable) from the unrestricted partner model (Mythos). Mythos 5 stays limited to vetted cyberdefense and biology partners; Fable 5 is what you and I get.

The headline characteristic of the Mythos class is **long-horizon, autonomous execution**. Fable 5 runs in an agent harness for extended periods. It plans across stages, delegates to sub-agents, writes its own tests, and self-corrects through verification loops. Anthropic frames it as built for work that would otherwise take a person hours, days, or weeks. The documentation explicitly describes it as capable of working "for days at a time." It also uses **vision to check its own coding output** against the original design or goal — relevant if you're having an agent implement a UI from a mockup. The longer and more complex the task, the larger Fable 5's lead over previous models.

### Performance benchmarks at launch

A few concrete data points from the launch that illustrate the capability jump:

- **Stripe** reported Fable 5 performed a codebase-wide migration in a 50-million-line Ruby codebase in a single day — work they estimated would have taken a team over two months by hand.
- On **Cognition's FrontierCode** evaluation (which tests production-grade coding quality, not just passing tests), Fable 5 scored highest among frontier models even at medium effort.
- GitHub's own internal benchmarks found Fable 5 completed equivalent autonomous coding work with *fewer tool calls and lower token consumption* than previous Opus-tier models.

That last point is the one that matters for day-to-day agent work. If you've run Copilot's coding agent against a Power Platform codebase — PCF controls, plugin assemblies, Code Apps, deployment pipelines — you know the ceiling is multi-step tasks spanning repository understanding, build validation, and iterative correction. Fewer tool calls to reach the same result means fewer failed agent runs and lower cost per completed task.

## The technical specs that matter for builders

Here are the hard numbers, pulled from Anthropic's API documentation rather than the launch hype.

| Spec | Value |
|---|---|
| API model ID | `claude-fable-5` |
| Context window | 1M tokens (default, standard pricing) |
| Max output | 128k tokens per request |
| Pricing | $10 / MTok input · $50 / MTok output |
| Batch pricing | $5 / MTok input · $25 / MTok output |
| Prompt caching | 90% discount on cached input tokens |
| Thinking mode | Adaptive only — cannot be disabled |
| Data retention | 30-day (Covered Model — no ZDR) |

A few of these have practical consequences worth calling out.

**The 1M-token context window is at standard pricing.** GitHub bills a 900k-token request at the same per-token rate as a 9k-token request — no long-context premium. For a Power Platform monorepo with solution metadata, multiple Code Apps, and pipeline definitions, that means you can put real architectural context in front of the model without a pricing cliff. And prompt caching carries a 90% discount on cached input tokens, so a stable context block (your solution structure, coding standards, schema) reused across an agent session gets cheap fast after the first call.

**US-only inference is available at 1.1x pricing** for input and output, for workloads that must run in the US. Note the direction here: this is US data residency, not EU. For DACH/Benelux clients with EU-residency requirements, US-only inference is the wrong lever — you'd be pinning data to the US, not Europe. Treat the residency story as unresolved for EU-regulated engagements until your platform (Copilot, Bedrock, Vertex, or Foundry) documents an EU option for this model.

**New tokenizer — budget for ~30% more tokens.** Fable 5 uses the tokenizer introduced with Opus 4.7. The same text produces roughly 30% more tokens than pre-4.7 models. If you're estimating cost by porting old token counts, you'll under-budget. Use the token counting API with `model: "claude-fable-5"` to measure accurately.

**Adaptive thinking is always on, and the API never returns the raw chain of thought.** You can't disable thinking; you steer depth through the `effort` parameter instead. The `thinking.display` field defaults to `"omitted"` — set it to `"summarized"` if you want readable reasoning summaries. If you've built tooling that parses raw reasoning tokens, that integration needs revisiting.

## The fallback mechanism — the part that's genuinely new

This is the behavior you've never had to design around before, and it deserves its own section.

Fable 5 ships with **safety classifiers** — separate AI systems that inspect requests and, when they detect certain categories, prevent Fable from responding. Instead of a flat refusal, the request **falls back to Claude Opus 4.8**, and Copilot notifies the user. The covered categories are cybersecurity (exploitation and offensive tasks), biology and chemistry, and model distillation attempts.

Anthropic's early data shows fallback triggers in **less than 5% of sessions** — for the other 95%+, you're getting full Fable 5 performance, effectively identical to Mythos 5. But "less than 5%" is an average, and the classifiers are deliberately tuned conservatively, so benign requests will sometimes be caught.

### What this means for Power Platform teams

Why does this matter for Power Platform work specifically? Most of what we do is nowhere near these categories. But consider the edge cases: a developer asking the agent to harden a Power Pages site against injection, to review authentication flows in a custom connector, or to analyze a security finding from a code scan. Those touch "cybersecurity" closely enough that a conservative classifier might route them to Opus 4.8 mid-session. The result won't be wrong — Opus 4.8 is highly capable — but it will be *different* from what the rest of your session produced, and the model behind your output changed without you choosing it.

On the API, this surfaces cleanly: a refused request returns `stop_reason: "refusal"` as a successful HTTP 200 (not an error), and reports which classifier declined it. You're **not billed at Fable prices** for a request refused before any output is generated. One nuance for those building directly on the Claude API: the reroute to Opus 4.8 isn't automatic. API customers configure it through the new Fallback API (the `fallbacks` parameter) or SDK middleware. In GitHub Copilot, the mechanics are abstracted and the routing just happens. The underlying behavior is the same — worth knowing when you're debugging why a particular run "felt like a different model."

## Where you'll find it in Copilot

Fable 5 is rolling out gradually to **Copilot Pro+, Max, Business, and Enterprise** plans. Once it reaches your tenant, the model picker shows Fable 5 across essentially the full surface area. In VS Code, that means chat, ask, edit, and agent modes. It also covers Visual Studio, Copilot CLI, the GitHub Copilot cloud agent and app, github.com, GitHub Mobile, JetBrains, Xcode, and Eclipse.

Two practical notes.

First, **billing in Copilot is usage-based at provider list pricing** — not the familiar premium-request multiplier. For an autonomous agent running long sessions, output tokens at $50/MTok accumulate fast. Budget owners should understand this before developers discover the model in the picker. Check GitHub's models and pricing reference for current numbers.

Second, **agent mode is where this model earns its price**. Using a Mythos-class model for single-turn chat completions is like renting a truck to deliver a letter. The economic case is in delegated, long-running tasks: a full solution refactor, a migration across plugin assemblies, a Code Apps scaffold with working Dataverse integration end to end.

## The data retention requirement — read this before enabling

Here's the section to forward to your IT department.

Every other Claude model in GitHub Copilot — Opus 4.8, Sonnet 4.5, Haiku 4.5 — operates under **Zero Data Retention (ZDR)**. Anthropic doesn't store prompts or outputs. This is the assumption that underpinned most enterprise Copilot rollouts.

Claude Fable 5 breaks that assumption deliberately. As a designated **Covered Model**, Fable 5 carries **30-day data retention** on both first- and third-party surfaces (including Copilot). Anthropic retains prompts and outputs to run the safety classifiers that detect misuse and reduce false positives. Anthropic deletes the data after 30 days, and states it **does not use retained data to train models** or for any non-safety purpose. They've also added privacy controls: logging all human access to the data and ensuring deletion in almost all cases.

The mechanics on the GitHub side:

- The Claude Fable 5 policy is **off by default** for Copilot Business and Enterprise.
- Enabling the policy **constitutes acknowledgement** of the retention requirement.
- Leaving it off keeps the model unavailable to your organization — everything else continues exactly as before.

### What the retention window actually means

I want to be precise about what this is and isn't. This is not training-data collection. It's a bounded, 30-day retention window that exists *because* the model is more capable. The classifiers watching for misuse are what made a Mythos-class model safe to release publicly.

But "not training data" doesn't make it a non-event for compliance. **Enabling Fable 5 is a material change** if your Copilot approval, client contracts, or DPA reviews assumed ZDR. Send it back through review. For regulated clients in our market — banking, insurance, public sector — assume this is a conversation, not a checkbox.

## My take: how to handle the enablement decision

Having sat on both sides of these reviews, here's the framework I'd use.

### Treat it as a scoped rollout, not a tenant-wide switch

The policy is org-level, but your *usage guidance* doesn't have to be uniform. Enable Fable 5 for repositories containing your own IP — internal tooling, accelerators, community samples. Keep client-engagement repositories on the ZDR models until the client's DPA explicitly covers the retention window. Agent-mode prompts routinely include source code, configuration, and architectural context. Whose code that is matters.

### Put model-level data handling in your AI usage register

Most DACH enterprises now operate under the EU AI Act or an internal AI governance framework. For those teams, the retention *and* residency characteristics of each model in your toolchain belong in your documentation. "GitHub Copilot" is no longer a single line item. Model selection now carries distinct data-handling properties, and Fable's US-only inference option doesn't solve EU residency.

### Don't let the retention discussion bury the capability discussion

Here's my opinionated bit: some organizations will reflexively leave the policy off and quietly fall behind. A model that completes long-horizon work with fewer tool calls and lower token consumption changes the economics of delegated development. For Power Platform teams specifically — where the agent has to juggle Dataverse metadata, solution layering, and ALM pipelines that generic models handle poorly — capability headroom translates directly into fewer failed agent runs. The right answer for most enterprises isn't "no," it's "yes, with scoped guardrails."

### Pilot with a measurable workload

Pick one recurring, well-bounded task — scaffolding a Code App with Dataverse integration, or migrating a set of classic workflows to Power Automate with documented mappings. Run it with Opus 4.8 and with Fable 5. Compare completion rate, intervention count, and actual billed cost. You'll have a defensible business case (or a defensible "not yet") within a sprint.

## Key takeaways

- **Claude Fable 5 is GA in GitHub Copilot** for Pro+, Max, Business, and Enterprise — the first Mythos-class model, positioned above Opus and built for long-running autonomous work.
- **The specs:** `claude-fable-5`, 1M-token context at standard pricing (90% prompt-cache discount), 128k max output, $10/$50 per MTok, adaptive-thinking-only, new tokenizer producing ~30% more tokens than pre-Opus-4.7 models.
- **A new fallback behavior:** safety classifiers route cybersecurity, bio/chem, and distillation requests to Opus 4.8 instead of refusing — triggering in under 5% of sessions, but worth understanding when a run behaves unexpectedly.
- **It's off by default and requires 30-day retention** — a break from the ZDR model every other Claude model in Copilot uses. Retained data is not used for training, but enabling it is a material compliance change.
- **For enterprise Power Platform teams**, treat enablement as a governance decision: scope by repository sensitivity, document model-level data handling, and pilot with a measurable workload before broad rollout.

[Internal link: Your Coding Agent Is Flying Blind in Dataverse — and how to fix it]
[Internal link: GitHub Copilot Code Reviews for Azure Repos — a Power Platform architect's guide]
[Internal link: GitHub Copilot CLI guide]

---

*Building Power Platform solutions in the DACH or Benelux region and working through AI governance questions like this one? Let's connect on [LinkedIn](https://www.linkedin.com/in/YOUR-PROFILE) — I share what I'm seeing in real enterprise engagements.*

*And if you want analysis like this in your inbox, subscribe to the **AIDevMe newsletter** for weekly Power Platform architecture insights → [aidevme.com](https://aidevme.com)*

---

## LinkedIn teaser (for your promo post)

Claude Fable 5 just landed in GitHub Copilot — Anthropic's first Mythos-class model, a full capability tier above Opus. But the spec sheet isn't the interesting part. It's off by default, it silently falls back to Opus 4.8 on certain requests, and enabling it means accepting 30-day data retention that breaks the ZDR assumption your Copilot rollout was probably approved under. I wrote up the technical breakdown and the governance checklist enterprise Power Platform teams need before flipping the switch.
