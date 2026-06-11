# Claude Fable 5 in GitHub Copilot — What Enterprise Teams Need to Know Before Enabling It

*The first Mythos-class model is now in the picker. It's more capable than anything Anthropic has shipped publicly. It's also the first model where the selection decision has real compliance implications.*

---

On June 9, GitHub announced that **Claude Fable 5** is generally available in GitHub Copilot. If you work in enterprise Power Platform development — or you're responsible for AI governance in your organisation — this one deserves more than a quick skim of the release notes.

Fable 5 is different from previous model additions in three specific ways, and each one has downstream consequences for how you use Copilot in client engagements.

## What Fable 5 actually is

Anthropic built Fable 5 on the same foundation as Claude Mythos — a capability tier above Opus, designed for long-horizon autonomous work. The original Mythos model never reached public release because Anthropic considered its cybersecurity capabilities too dangerous to release without controls. Fable 5 is the classifier-wrapped version that passed the bar for general availability.

The practical difference from Opus-tier models: Fable 5 is built to run for extended periods in an agent harness. It plans across stages, delegates to sub-agents, writes its own tests, and self-corrects. Anthropic describes it as built for work that would take a person hours, days, or weeks.

A few launch benchmarks that give this concrete shape:

- Stripe ran it against a 50-million-line Ruby codebase. It completed a migration in a single day that they estimated at two months of manual effort.
- On Cognition's FrontierCode evaluation, Fable 5 scored highest among frontier models at medium effort.
- GitHub's internal benchmarks show it completes equivalent agent work with fewer tool calls and lower token consumption than previous Opus-tier models.

That last point matters most for day-to-day use. Fewer tool calls means fewer failed agent runs and lower cost per completed task.

## The fallback mechanism — new behaviour you need to understand

Every previous model in Copilot either responds or refuses. Fable 5 introduces a third outcome.

Safety classifiers inspect each request. When they detect requests touching cybersecurity, biology and chemistry, or model distillation, they route the request to **Claude Opus 4.8** instead of letting Fable respond. Copilot notifies the user when this happens. Anthropic's data shows it triggers in under 5% of sessions.

For most Power Platform work, you'll never see it. But consider the edge cases: asking an agent to review authentication flows in a custom connector, or to analyse a security finding from a code scan. Those requests touch cybersecurity closely enough that a conservative classifier might catch them. The output won't be wrong — Opus 4.8 is highly capable — but you'll get a different model mid-session, and that switch happened without you choosing it.

On the API you can detect this: a classifier refusal returns `stop_reason: "refusal"` as a successful HTTP 200, and you aren't billed at Fable prices for it. In Copilot the routing is abstracted — it just happens. Worth knowing when a session behaves unexpectedly.

## The data retention requirement — read this before enabling

This is the part to send to your IT department.

Every other Claude model in GitHub Copilot — Opus 4.8, Sonnet 4.5, Haiku 4.5 — operates under Zero Data Retention. Anthropic doesn't store prompts or outputs. That assumption underpins most enterprise Copilot rollouts.

Claude Fable 5 is a **Covered Model**. It carries 30-day data retention on both first- and third-party surfaces, including Copilot. Anthropic retains prompts and outputs to run the safety classifiers. Anthropic deletes the data after 30 days and states it does not use retained data to train models or for any non-safety purpose.

The GitHub side of this:

- The Fable 5 policy is **off by default** for Copilot Business and Enterprise.
- Enabling it constitutes acknowledgement of the retention requirement.
- Leaving it off means the model stays unavailable — nothing else changes.

To be clear about what this is and isn't: it's not training-data collection. It's a bounded retention window that exists because the model is more capable. The classifiers are what made Mythos-class capabilities safe to release publicly at all.

But "not training data" doesn't resolve the compliance question. If your organisation's Copilot approval, client contracts, or DPA reviews assumed ZDR, enabling Fable 5 is a material change. It needs to go back through review — not as a formality, as an actual review.

## How to handle the enablement decision

Here's the framework I'd use for enterprise teams.

**Scope by repository, not by tenant.** Enable Fable 5 for repositories that contain your own IP: accelerators, internal tooling, community samples. Keep client-engagement repositories on ZDR models until the client's DPA explicitly covers the retention window. Agent-mode prompts routinely include source code, configuration, and architectural context. Whose code that is matters.

**Update your AI usage register.** If you operate under the EU AI Act or an internal governance framework, model-level data handling belongs in your documentation. "GitHub Copilot" is no longer a single line item — model selection now carries distinct data-handling properties. And Fable's US-only inference option doesn't solve EU residency requirements.

**Don't let the compliance discussion bury the capability discussion.** Some organisations will leave the policy off and quietly fall behind. A model that completes long-horizon work with fewer tool calls changes the economics of delegated development. For Power Platform teams — where an agent has to handle Dataverse metadata, solution layering, and ALM pipelines that generic models handle poorly — capability headroom translates directly into fewer failed agent runs. The right answer for most enterprises isn't "no." It's "yes, with scoped guardrails."

**Pilot with a measurable workload.** Pick one recurring, well-bounded task — scaffolding a Code App with Dataverse integration, or migrating classic workflows to Power Automate. Run it with Opus 4.8 and with Fable 5. Compare completion rate, intervention count, and billed cost. You'll have a defensible business case within a sprint.

---

I wrote the full technical breakdown on AIDevMe — specs table, fallback API mechanics, retention details, and the complete enablement framework.

**[Read the full article →](https://aidevme.com/claude-fable-5-in-github-copilot-technical-breakdown-for-power-platform-and-enterprise-teams/)**

---

*If you're working through AI governance questions like this in DACH or Benelux enterprise engagements, reply to this email — I'm always interested in what's coming up in real architecture reviews.*
