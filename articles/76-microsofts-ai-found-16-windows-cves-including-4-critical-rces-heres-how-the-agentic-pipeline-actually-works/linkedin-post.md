Microsoft's AI just found 16 Windows CVEs — including 4 Critical RCEs — and shipped them all to the same Patch Tuesday. That's not a research demo. That's a production AI closing the full loop: find, verify, patch, ship.

The system is called MDASH (Microsoft Security multi-model agentic scanning harness). Here's what makes it worth understanding for anyone building on Azure, Dataverse, or Power Platform:

𝟭. The bugs are real and on your infrastructure.
4 Critical RCEs — in tcpip.sys, IKEv2, DNS, and Netlogon. Most reachable with no credentials. This is the networking and authentication stack your Power Platform solutions run on. All patched in May 2026 Patch Tuesday.

𝟮. The architecture is why it works — not the model.
MDASH runs a five-stage pipeline: Prepare → Scan (100+ specialised agents) → Validate (debater agents argue against every finding) → Dedupe → Prove (dynamic triggering, not flagging). A finding that can't be demonstrated doesn't make the cut.

𝟯. Multi-model disagreement is used as a signal.
A SOTA heavy reasoner, a distilled cost-effective debater, and a second SOTA counterpoint run in parallel. When two models diverge on a finding, that divergence is used explicitly to weight credibility. It's not a problem to resolve — it's information.

𝟰. The recall numbers are hard to ignore.
→ 96% recall on 28 clfs.sys MSRC cases over five years
→ 100% recall on 7 tcpip.sys MSRC cases over five years
→ 88.45% on the CyberGym public benchmark — top of the leaderboard, 5 points ahead of the next entry, with generally available models

𝟱. The architecture is model-agnostic by design.
When a new model lands, one configuration change A/B tests it against the current panel. Scan plugins, proving agents, scope configurations — none of it needs rebuilding. The value carries forward.

The architectural lesson here applies well beyond security tooling: the pipeline is the product. A model handed a single function missed both the tcpip.sys race condition (cross-file reference tracking) and the six-file ikeext.dll double-free (cross-file pattern comparison). The system around the model is what caught them.

I wrote the full breakdown — pipeline stages, both CVE deep dives, the complete 16-CVE table, benchmark details, and what this means for evaluating AI security tooling in enterprise architecture reviews.

Link in the comments 👇

https://aidevme.com/microsofts-ai-found-16-windows-cves-including-4-critical-rces-heres-how-the-agentic-pipeline-actually-works/

#MicrosoftSecurity #PowerPlatform #Azure #AIAgents #CyberSecurity #Dataverse #EnterpriseAI #PatchTuesday
