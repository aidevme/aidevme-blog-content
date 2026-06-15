# Microsoft's AI Found 16 Windows CVEs — Including 4 Critical RCEs. Here's How the Agentic Pipeline Actually Works

*Microsoft didn't just announce a research demo. It shipped a full AI security loop to Patch Tuesday — and the architecture behind it maps directly to problems Power Platform teams solve every day.*

---

On May 12, Microsoft announced that its new agentic scanning harness — **MDASH** (Microsoft Security multi-model agentic scanning harness) — found 16 vulnerabilities in the Windows networking stack in a single scan cycle. Four of them are Critical remote code execution flaws, most reachable with no credentials.

If you're a Power Platform Solution Architect, this is the infrastructure your solutions run on: Azure, Dataverse, Power Pages, Power Automate — all of it sitting on the Windows networking and authentication stack that MDASH just scanned. And all 16 findings made it to Patch Tuesday. That's the full loop: AI found them, teams verified them, patches shipped.

That bar — closing the loop, not just flagging candidates — is what makes this worth your time.

## What MDASH actually does

MDASH was built by Microsoft's Autonomous Code Security team, partly by members of Team Atlanta, which won the $29.5M DARPA AI Cyber Challenge by building an autonomous system that had to prove bugs with working exploits, not just flag them. That end-to-end discipline is baked into how MDASH works.

The pipeline has five stages: **Prepare** (ingest, index, map attack surface), **Scan** (100+ specialised auditor agents working independently), **Validate** (a separate cohort of debater agents argues against every finding), **Dedupe** (semantically equivalent findings are collapsed), and **Prove** (each finding is dynamically validated — if it can't be demonstrated, it doesn't ship).

Nothing reaches Patch Tuesday unless it passes the prove stage.

## The two bugs that show you why multi-model matters

Microsoft walked through two findings in detail, and both show exactly why the multi-model architecture catches things a single-model system misses.

**CVE-2026-33827** is a remote unauthenticated use-after-free in `tcpip.sys`. The lifetime violation isn't visible in any single function — the release and reuse are separated by non-trivial control flow, and the decisive signal only appears when you're doing cross-file comparison against the correct version of the same pattern elsewhere in the codebase. A single-shot analysis can't see it.

**CVE-2026-33824** spans six source files in IKEEXT — a shallow copy in `ike_A.c` creates an aliased pointer, a wrong free in `ike_C.c` frees it, a second free in `ike_D.c` double-frees it. Two UDP packets, no race, no credentials. Pre-auth RCE into LocalSystem. The strongest evidence that the bug is real is a correct version of the pattern sitting immediately after the bad `memcpy` in `ike_D.c` — but only visible through cross-file comparison.

## The three architectural properties that make it work

**1. An ensemble of diverse models.** MDASH doesn't try to pick the best model — it runs a configurable panel and treats disagreement between models as an explicit confidence signal, not a problem to resolve.

**2. Specialised agents.** Auditors, debaters, and provers each have their own role, prompt regime, tools, and stop criteria. Nothing is crammed into a single agent or prompt.

**3. Model-agnostic architecture.** When a new model lands, swapping it in is one configuration flip. Scan plugins, scope configurations, proving agents — all of it carries forward. The value doesn't reset.

## The benchmark numbers

- **96% recall** on 28 historical MSRC cases for `clfs.sys` over five years
- **100% recall** on 7 historical MSRC cases for `tcpip.sys` over five years
- **88.45% on the CyberGym public benchmark** — top of the leaderboard, five points ahead of the next entry, using generally available models

The MSRC recall numbers tell you this would have caught the bugs that real attackers exploited. The CyberGym number tells you the pipeline is doing the heavy lifting, not the model.

---

I wrote the full breakdown on AIDevMe — the complete five-stage pipeline, both CVE deep dives, the full 16-CVE table with severity and type, the benchmark details, and what the architecture means for how you evaluate AI security tooling in client governance conversations.

**[Read the full article →](https://aidevme.com/microsofts-ai-found-16-windows-cves-including-4-critical-rces-heres-how-the-agentic-pipeline-actually-works/)**

---

*If questions like this come up in your architecture reviews or client governance conversations, reply to this email — I'm always interested in what's landing in real engagements.*
