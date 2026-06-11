# Claude Fable 5 Is in GitHub Copilot — And It's the First Model Where the Selection Decision Has Compliance Implications

GitHub added Claude Fable 5 to Copilot on June 9. Most announcements like this get a brief read, a mental note, and then everyone moves on. This one is worth a closer look — not because the capability story is bigger than usual (though it is), but because for the first time, which model you pick in Copilot carries data governance consequences.

Here's what's actually happening and why it matters for teams running Copilot in enterprise environments.

---

## Fable 5 is a different kind of model

Anthropic has been building toward a capability tier above Opus for a while. They called it Mythos. When they previewed the original Mythos model in April through Project Glasswing, they didn't release it publicly — they considered its cybersecurity capabilities too dangerous without controls in place. It was unusually effective at finding and exploiting vulnerabilities.

Fable 5 is Mythos with a classifier layer on top. Same underlying model. Different access boundary. The name "Fable" distinguishes the safeguarded public version from "Mythos," which remains restricted to vetted cyberdefense and biology partners.

The headline capability is long-horizon autonomous execution. This isn't a better chat model — it's a model designed to run in an agent harness for extended periods, planning across stages, delegating to sub-agents, writing its own tests, and self-correcting. Anthropic describes it as built for work that would take a person hours, days, or weeks.

Some launch benchmarks that give this shape:

- Stripe ran it against a 50-million-line Ruby codebase. It completed a migration in a day that they estimated at two months of manual work.
- On Cognition's FrontierCode evaluation — which measures production-grade coding quality, not just test-passing — Fable 5 scored highest among frontier models at medium effort.
- GitHub's internal benchmarks show it completes equivalent agent work with fewer tool calls and lower token consumption than previous Opus-tier models.

That last point is the most practical one. Fewer tool calls means fewer failed agent runs and lower cost per completed task. For anyone who has run Copilot's agent against a complex codebase — Power Platform solutions, PCF controls, Dataverse plugins — the ceiling has always been multi-step work falling apart mid-session. Fable 5 raises that ceiling.

---

## There's a new behaviour you haven't had to think about before

Every previous model in Copilot either responds or refuses. Fable 5 introduces a third outcome: a classifier-triggered fallback.

Safety classifiers inspect each request before Fable responds. When they detect requests in certain categories — cybersecurity exploitation, biology and chemistry, model distillation — they route the request to **Claude Opus 4.8** instead. Copilot notifies the user when this happens. Anthropic reports it triggers in under 5% of sessions.

For typical development work, you'll never notice it. The edge cases that matter: asking an agent to review authentication flows in a custom connector, to harden a web application against injection, or to analyse output from a security scanner. Those requests touch "cybersecurity" closely enough that a conservative classifier might catch them.

The result won't be wrong — Opus 4.8 is highly capable. But you'll get a different model for that request than for the rest of your session, and that switch happened without you choosing it. In agent mode, where consistency across a long-running task matters, this is worth understanding.

On the API, you can detect it: a classifier refusal returns `stop_reason: "refusal"` as a successful HTTP 200. You aren't billed at Fable prices for refused requests. In Copilot, the routing is abstracted — it just happens silently.

---

## The part to send to your IT department

Every other Claude model in GitHub Copilot operates under Zero Data Retention. Anthropic doesn't store prompts or outputs. That assumption underpins most enterprise Copilot rollouts — it's usually the answer to the first data governance question in any procurement or DPA review.

Fable 5 is a **Covered Model**. It carries 30-day data retention on all surfaces where it runs, including Copilot. Anthropic retains prompts and outputs to operate the safety classifiers. After 30 days, Anthropic deletes the data. Anthropic states it does not use retained data to train models or for any non-safety purpose. They've added access logging and deletion controls on top of that.

On the GitHub side:

- The Fable 5 policy is **off by default** for Copilot Business and Enterprise.
- Enabling it constitutes acknowledgement of the retention requirement.
- Leaving it off means the model stays unavailable — nothing else in your Copilot configuration changes.

The important distinction: this is not a training-data story. It's a bounded, 30-day window that exists because the classifiers need to run on retained data to improve their accuracy over time. The classifiers are the mechanism that made a Mythos-class model safe to release publicly. The retention and the capability are connected.

That said, "not training data" doesn't resolve the compliance question. If your organisation's Copilot approval, your client contracts, or your DPA reviews rested on a ZDR assumption for AI coding tools, enabling Fable 5 is a material change. It needs an actual review — not a rubber stamp.

---

## A practical framework for enterprise teams

The organisations that will get this right are the ones that treat model selection as a configuration decision with governance consequences, not just a capability upgrade.

**Scope by repository, not by tenant.** The policy is org-level, but your usage guidance doesn't have to be uniform. Enable Fable 5 for repositories containing your own IP: accelerators, internal tooling, community samples. Keep client-engagement repositories on ZDR models until the client's DPA covers the retention window. Agent-mode prompts routinely include source code, configuration, and architectural context. Whose code that is matters.

**Update your AI toolchain documentation.** If you operate under the EU AI Act or an internal AI governance framework, model-level data handling belongs in your register. "GitHub Copilot" is no longer a single line item. Model selection now carries distinct retention and residency properties. For DACH and Benelux teams specifically: Fable's US-only inference option at 1.1× pricing pins data to the US. It doesn't help with EU residency requirements.

**Don't let the governance discussion become an excuse to do nothing.** Some organisations will leave the policy off indefinitely and quietly fall behind. A model that completes long-horizon work with fewer tool calls changes the economics of delegated development. For Power Platform teams — where an agent has to navigate Dataverse metadata, solution layering, and ALM pipelines that generic models handle poorly — that headroom translates directly into better agent outcomes. The right answer for most enterprises isn't "no." It's "yes, scoped appropriately."

**Run a measurable pilot before broad rollout.** Pick one recurring task with a clear definition of done — scaffolding a Code App with Dataverse integration, or migrating a set of classic workflows to Power Automate with documented mappings. Run it with Opus 4.8. Run it with Fable 5. Compare completion rate, how many times you had to intervene, and actual billed cost. You'll have a defensible business case or a defensible "not yet" within a sprint.

---

## The short version

Fable 5 is a genuinely capable model that earns its place in agent workflows. It's also the first model in Copilot's picker where selecting it requires a governance conversation, not just a capability evaluation. The two things are connected: the retention requirement exists *because* the model is more capable, and the safeguards are what made it releasable.

Enable it thoughtfully. Scope it to the right repositories. Document the data-handling properties. Pilot it on a measurable workload. That's the framework.

---

*I published the full technical breakdown — spec table, fallback API mechanics, and the complete enablement framework — on AIDevMe. If you're working through AI governance questions in enterprise Power Platform engagements, that's where to start.*

https://aidevme.com/claude-fable-5-in-github-copilot-technical-breakdown-for-power-platform-and-enterprise-teams/
