# Microsoft's AI Found 16 Windows CVEs — Including 4 Critical RCEs. Here's How the Agentic Pipeline Actually Works

**WordPress SEO**
- **URL:** https://aidevme.com/microsofts-ai-found-16-windows-cves-including-4-critical-rces-heres-how-the-agentic-pipeline-actually-works/
- **Focus keyphrase:** MDASH agentic security pipeline
- **SEO title:** Microsoft's AI Found 16 Windows CVEs — What Power Platform Solution Architects Need to Know
- **Meta description:** Microsoft's MDASH agentic scanning harness found 16 CVEs in Windows networking — 4 Critical RCEs on the infrastructure your Power Platform solutions run on. Here's what the pipeline does and what it means for your architecture reviews and client conversations.
- **Slug:** microsoft-mdash-agentic-security-system-power-platform-solution-architects
- **Excerpt:** Microsoft's MDASH agentic scanning harness found 16 CVEs in the Windows networking stack — including 4 Critical RCEs affecting tcpip.sys, IKEv2, DNS, and Netlogon. As a Power Platform Solution Architect, this is the infrastructure your solutions sit on. This post explains how the pipeline works, what the architectural lessons are, and how to use this in client governance and security conversations.

---

As a Power Platform Solution Architect, you don't patch Windows. You architect on top of it.

Azure, Dataverse, Power Pages, Power Automate — every one of those services runs on the Windows networking and authentication stack that Microsoft just announced its AI system scanned and found 16 vulnerabilities in. Four of them Critical remote code execution flaws. Most reachable with no credentials.

That's the context that makes Microsoft's May 12 announcement worth your time. Not because you need to understand kernel internals, but because:

- The platform you stake your client architectures on is being scanned by production AI at a depth that wasn't possible two years ago
- The security posture of that platform is now a talking point you can use in governance and architecture reviews
- The architectural principles behind how MDASH was built map directly to problems you solve in Dataverse and Power Platform design

Microsoft's new agentic scanning harness — codename **MDASH** (Microsoft Security multi-model agentic scanning harness) — found those 16 vulnerabilities in a single scan cycle and shipped them all to the same Patch Tuesday. That's not a research demo. That's an AI system closing the full loop: find, verify, patch, ship.

### Three Architectural Takeaways

Three things stand out from an architecture and governance perspective:

1. **The bugs made it to Patch Tuesday** — they passed triage, reproduction, and patch review. That's the bar most automated scanners never clear, and it's relevant to how you evaluate security tooling for your clients.
2. **The architecture is model-agnostic by design** — the value doesn't reset when a new model drops, which is exactly the kind of durable investment story you want to see in enterprise security tooling.
3. **88.45% on the CyberGym public benchmark** — highest on the leaderboard, using generally available models. The pipeline is doing most of the work, not the model.

Let's get into how it works — and then I'll translate the architectural lessons into what they mean for you.

---

## Table of Contents

- [What MDASH Actually Is](#what-mdash-actually-is)
- [The Five-Stage Pipeline](#the-five-stage-pipeline)
  - [Prepare](#prepare)
  - [Scan](#scan)
  - [Validate](#validate)
  - [Dedupe](#dedupe)
  - [Prove](#prove)
- [The Three Properties That Make It Work in Practice](#the-three-properties-that-make-it-work-in-practice)
- [What It Found: The May 2026 Patch Tuesday Cohort](#what-it-found-the-may-2026-patch-tuesday-cohort)
- [Two Deep Dives: The Bugs Single-Model Systems Miss](#two-deep-dives-the-bugs-single-model-systems-miss)
  - [CVE-2026-33827 — Remote Unauthenticated UAF in tcpip.sys via SSRR](#cve-2026-33827--remote-unauthenticated-uaf-in-tcpipsys-via-ssrr)
  - [CVE-2026-33824 — IKEv2 SA_INIT Double-Free → LocalSystem RCE](#cve-2026-33824--ikev2-sa_init-double-free--localsystem-rce)
- [How Capable Is MDASH? Retrospective Benchmarks](#how-capable-is-mdash-retrospective-benchmarks)
  - [Recall on Historical MSRC Cases](#recall-on-historical-msrc-cases)
  - [CyberGym Public Benchmark](#cybergym-public-benchmark)
  - [Failure Analysis](#failure-analysis)
- [What This Means for Enterprise Defenders](#what-this-means-for-enterprise-defenders)
- [Key Takeaways](#key-takeaways)

---

## What MDASH Actually Is

MDASH was built by Microsoft's **Autonomous Code Security (ACS)** team. A few members came from **Team Atlanta** — the group that won the $29.5 million DARPA AI Cyber Challenge by building an autonomous system that found and patched real bugs in complex open-source software. That origin story matters, because the DARPA challenge didn't let you just flag candidates. You had to prove them with working exploits. That end-to-end thinking is baked into how MDASH was designed.

Now, you might be thinking: "okay, but scanning open-source code is different from scanning Windows." You're right, and Microsoft is upfront about why their codebase is an unusually hard target:

- **It's all private.** Windows, Hyper-V, Azure, the device-driver ecosystem — none of it was ever in a model's training data. A model can't pattern-match its way through kernel calling conventions or IRP lock invariants. It has to actually reason.
- **Noise has a real cost.** Every finding has an owner, a triage queue, and a Patch Tuesday to land on. If your tool generates false positives in tier-one components, you've just made life worse for the people who actually ship Windows.
- **The targets are worth attacking.** A single hard bug in Windows can affect billions of devices. Which means the bar for what counts as "useful" is genuinely high.

All of that explains why MDASH isn't optimised to find the most candidates. It's optimised to find findings that survive being proven.

---

## The Five-Stage Pipeline

Think of MDASH as a pipeline: you put a codebase in one end and get validated, proven findings out the other. There's no single step where "the AI reads the code and finds bugs." It's staged, and each stage has a specific job.

### Prepare

Before any agent touches the code, MDASH ingests the source target, builds language-aware indices, and maps the attack surface by analysing past commits. Domain context enters the system here — not through the model's weights, but through structured tooling that understands what the code does before any scanning starts.

### Scan

More than **100 specialised auditor agents** run over candidate code paths. Each one was built from deep research into past CVEs and their patches, so they're not generic "find a bug" agents — they know what specific classes of vulnerability look like in this kind of code. They work independently, and their findings get ensembled into a single report.

### Validate

This is the stage that separates real findings from noise, and it's where MDASH does something most scanners skip entirely. A second cohort of agents — the *debaters* — argue against each finding. They try to prove it's not reachable, not exploitable, not real. If the auditor flagged something and the debater can't knock it down, the finding's credibility goes up. That disagreement signal is used explicitly.

### Dedupe

Semantically equivalent findings get collapsed. Patch-based grouping is the primary mechanism — if two findings trace back to the same root cause, they show up in triage as one item, not ten.

### Prove

This is where MDASH either proves a finding or drops it. The prove stage constructs actual triggering inputs and validates them dynamically. For C/C++ code, that means ASan integration. If a finding can't be demonstrated, it doesn't make the cut.

The **CLFS proving plugin** is a good example of how this extensibility works. It knows the on-disk container layout, the block-validation sequence, and the in-memory state machine for the Common Log File System — enough to construct triggering log files for candidate findings. The model doesn't need to know any of this. The plugin embeds it, the model uses it, and the result is bugs that ship to Patch Tuesday rather than bugs that sit in a backlog.

---

## The Three Properties That Make It Work in Practice

### 1. An ensemble of diverse models

No single model is best at every stage — and MDASH doesn't pretend otherwise. It runs a configurable panel: a SOTA model as the heavy reasoner, a distilled model as a cost-effective debater for high-volume passes, and a second separate SOTA model as an independent counterpoint. The key insight is that disagreement between models isn't a problem to resolve — it's a signal. When two models diverge on a finding, that divergence tells you something about how credible the finding actually is.

### 2. Specialised agents

An auditor thinks differently to a debater, which thinks differently to a prover. Each stage has its own role, its own prompt regime, its own tools, its own stop criteria. MDASH doesn't try to cram everything into one agent or one prompt. That might sound obvious, but most AI coding tools still do exactly that.

### 3. Model-agnostic architecture

This is the one that matters most long-term. When a new model lands, swapping it in is one configuration flip. When a model improves, everything the team already built — scan plugins, scope configurations, proving agents — carries over. The value doesn't reset. Compare that to a system built around a specific model: the moment a better one ships, you're rebuilding from scratch.

---

## What It Found: The May 2026 Patch Tuesday Cohort

Here's the full list of 16 CVEs from the May 12 Patch Tuesday that MDASH found. Scan the severity column.

| Component | Description | CVE | Severity | Type |
|---|---|---|---|---|
| tcpip.sys | Remote unauth SSRR IPv4 packets causing UAF | CVE-2026-33827 | **Critical** | Remote Code Execution |
| ikeext.dll | Unauth IKEv2 SA_INIT double-free → LocalSystem RCE | CVE-2026-33824 | **Critical** | Remote Code Execution |
| netlogon.dll | Unauthenticated CLDAP User= filter stack overflow | CVE-2026-41089 | **Critical** | Remote Code Execution |
| dnsapi.dll | Crafted UDP DNS response triggers heap OOB | CVE-2026-41096 | **Critical** | Remote Code Execution |
| tcpip.sys | NULL deref via crafted IPv6 extension headers | CVE-2026-40413 | Important | Denial of Service |
| tcpip.sys | Kernel DoS via ESP SA refcount underflow | CVE-2026-40405 | Important | Denial of Service |
| tcpip.sys | Use-after-free in Ipv4pReassembleDatagram → info disclosure | CVE-2026-40406 | Important | Information Disclosure |
| tcpip.sys | IPsec cross-SA fragment splicing via reassembly | CVE-2026-35422 | Important | Security Feature Bypass |
| tcpip.sys | Unauthenticated local WFP RPC disables name cache | CVE-2026-32209 | Important | Security Feature Bypass |
| ikeext.dll | Memory leak | CVE-2026-35424 | Important | Denial of Service |
| telnet.exe | OOB read in FProcessSB via malformed TO_AUTH | CVE-2026-35423 | Important | Information Disclosure |
| tcpip.sys | IPv6+TCP MDL-split packet triggers NULL deref | CVE-2026-40414 | Important | Denial of Service |
| tcpip.sys | ICMPv6 packet triggers NdisGetDataBuffer NULL deref | CVE-2026-40401 | Important | Denial of Service |
| tcpip.sys | Pre-auth remote UAF via SA double-decrement | CVE-2026-40415 | Important | Remote Code Execution |
| http.sys | Unauth remote QUIC control-stream OOB read | CVE-2026-33096 | Important | Denial of Service |
| tcpip.sys | Kernel stack buffer overflow via RPC blob | CVE-2026-40399 | Important | Elevation of Privilege |

10 kernel-mode. 6 usermode. Most are reachable from the network **with no credentials required**.

This isn't a list of edge-case theoretical findings. This is the kind of bug density an experienced offensive security researcher produces after spending months focused on a single component — except MDASH did it across the entire Windows network stack in one scan cycle.

---

## Two Deep Dives: The Bugs Single-Model Systems Miss

Microsoft walked through two findings in detail and explicitly called them out as the type of bug the multi-model pipeline catches that a single-model harness doesn't. Both are worth reading carefully, because they show you exactly where the architectural difference shows up in practice.

### CVE-2026-33827 — Remote Unauthenticated UAF in tcpip.sys via SSRR

The bug is in `Ipv4pReceiveRoutingHeader`, the Windows IPv4 receive path. The function drops its sole owned reference to a `Path` object, then later reuses the same pointer when handling Strict Source and Record Route (SSRR) processing. Classic use-after-free setup.

But here's what makes it hard to catch: the timing window is real, and it involves multiple independent subsystems. The path-cache scavenger, explicit flush routines, and interface state-driven garbage collection can all concurrently remove the object and drop the final reference. None of them are synchronised with the receive-side execution window in this function. No lock is held. On an SMP system, the freed object can be reclaimed and overwritten before the subsequent dereference — a race-driven UAF with actual exploitation feasibility.

An attacker can trigger this with crafted IPv4 packets carrying the SSRR option. No credentials, no special setup.

**So why did single-model systems miss it?** The lifetime violation isn't locally visible in any single function. The release and reuse are separated by non-trivial control flow — alternate branches, multiple validation checks, early-drop conditions. Without tracking reference ownership across all of that, the model just sees two independent operations. And the decisive signal — the correct version of the same pattern elsewhere in the codebase — only becomes visible when you're doing cross-file reasoning. A single-shot analysis misses the connection entirely.

### CVE-2026-33824 — IKEv2 SA_INIT Double-Free → LocalSystem RCE

This one is in IKEEXT, the Windows component that handles IKE and AuthIP keying for IPsec. It's reachable over UDP/500 on any host acting as an IKEv2 responder — think RRAS VPN, DirectAccess, Always-On VPN, or any machine with an inbound IPsec connection security rule.

Two UDP packets. No race. No special timing. Deterministic.

The root cause is a shallow copy problem. When IKEEXT reinjects a reassembled IKEv2 fragment through its receive pipeline, it copies the packet's receive context with a flat `memcpy`. That copies the struct bytes but not the heap allocations the struct points to. One of those allocations is the attacker-supplied security-realm identifier. After the copy, both the queued context and the live Main Mode SA hold the same pointer — and both think they own it. On teardown, both free it. Double-free of a fixed-size heap chunk. IKEEXT runs as LocalSystem inside `svchost.exe`. That's pre-auth RCE into one of the highest-privilege contexts on the machine.

#### Why Single-Model Systems Missed It

The bug spans **six source files**: the bad `memcpy` in `ike_A.c`, the alias origin in `ike_B.c`, the wrong free in `ike_C.c`, the right pattern *and* the second free in `ike_D.c`, the remote population in `ike_E.c`, and the UAF read site in `ike_F.c`. No single-file analysis connects all of that. The strongest evidence that the bug is real is the correct version of the same pattern immediately after the `memcpy` in `ike_D.c` — but you only see that by comparing across files. MDASH's specialised auditor agents are built to surface exactly that kind of cross-file pattern comparison, and the debate stage forces each finding to hold up under scrutiny before it moves forward.

---

## How Capable Is MDASH? Retrospective Benchmarks

The Patch Tuesday results are forward-looking. The retrospective benchmarks are where you get ground truth — can it rediscover bugs that real attackers found and that real engineers already patched?

### Recall on Historical MSRC Cases

The team ran MDASH against pre-patch snapshots of two heavily reviewed Windows components and measured re-discovery of confirmed historical bugs:

- **clfs.sys**: 96% recall across 28 MSRC cases over five years
- **tcpip.sys**: 100% recall across 7 MSRC cases over five years

Think about what the MSRC case database actually represents. These are the bugs real attackers exploited, the ones that triggered emergency patches, the ones defenders had to react to under pressure. A system that rediscovers 96% of a five-year MSRC backlog in a heavily reviewed kernel component isn't finding theoretical weaknesses. It's finding the bugs that mattered.

Microsoft is honest about the limits here. These are retrospective recall numbers on a finite case count. They tell you the system would have been useful if it had existed at the time. They don't guarantee the same rate on the *next* 38 CLFS bugs. Fair caveat.

### CyberGym Public Benchmark

On the public **CyberGym benchmark** — 1,507 real-world vulnerability reproduction tasks across 188 OSS-Fuzz projects — MDASH scored **88.45%**. That's the top result on the leaderboard, roughly **five points ahead of the next entry at 83.1%**.

What makes that number meaningful isn't just the ranking. It's that it was achieved with generally available models. No special fine-tune. No proprietary model. The agentic system around the model is doing the heavy lifting — which is exactly the architectural claim Microsoft is making.

### Failure Analysis

The remaining ~12% that MDASH missed breaks down into two patterns, and Microsoft published the breakdown:

1. **Wrong code area targeting** — 82% of these came from tasks with vague descriptions that lacked function or file identifiers. Better scan input = better results. This is a solvable problem.
2. **Harness format mismatch** — the agent built correct reproductions using libFuzzer-style inputs, but the benchmark expected honggfuzz format. Sound finds, wrong format. Also solvable.

Neither failure pattern points to a fundamental model limitation. Both point to tooling and input quality issues.

---

## What This Means for Enterprise Defenders

Let me give you the honest takeaway.

AI vulnerability discovery has crossed from "interesting research project" into "this is how we ship Patch Tuesday now." That's the real significance of the May 12 announcement — not the benchmark score, not the CVE count, but the fact that the full loop closed: AI found bugs, teams verified them, patches shipped. At scale. In production.

Here's what I think the MDASH architecture teaches us, regardless of whether you're ever going to use MDASH specifically:

### The Model Isn't the Product. The Pipeline Is.

The bugs MDASH found — the tcpip.sys race, the six-file ikeext.dll alias chain — are invisible to a model handed a single function. They become visible when you have a system that can sequence cross-file comparison, multi-step reachability analysis, debate between agents, and end-to-end proof construction. If you've been evaluating AI security tools based on "which model does it use," you've been asking the wrong question.

### Validation Is Where Most of the Work Actually Lives

A tool that flags candidate bugs without proving them just creates a triage backlog. The reason the Patch Tuesday cohort exists is that MDASH didn't stop at flagging. It debated, deduped, and proved. Validation isn't a checkbox at the end of the pipeline. It's its own sub-system, and it's where most of the day-to-day engineering effort goes.

### Model-Agnostic Architecture Is a Competitive Advantage

The model market is going to keep moving. Any security tool whose core value is locked to a specific model is a tool that needs to be rebuilt every six months. MDASH's architecture carries investment forward — scan plugins, scope configurations, proving agents — across model generations. That's what durable value looks like.

When you're evaluating any AI security tooling, the question worth asking is: *what does this system do with the model, and what survives when the next model arrives?*

MDASH is currently in limited private preview. [Sign up here](https://aka.ms/AI-drivenScanningHarness) if you want early access.

---

## Key Takeaways

- **MDASH found 16 CVEs in the Windows networking stack** in a single Patch Tuesday cycle, including 4 Critical RCEs reachable with no authentication.
- **The five-stage pipeline** (Prepare → Scan → Validate → Dedupe → Prove) is what separates findings that survive triage from ones that don't.
- **100+ specialised agents** work independently across each stage; their results are ensembled.
- **The multi-model ensemble** uses disagreement between models as an explicit confidence signal, not just as a performance hedge.
- **On StorageDrive** (a private test driver with 21 injected vulnerabilities), MDASH found all 21 with zero false positives.
- **Retrospective recall**: 96% on 28 clfs.sys MSRC cases over five years; 100% on 7 tcpip.sys cases.
- **CyberGym benchmark**: 88.45% — top of the public leaderboard, five points ahead of the next entry, using generally available models.
- **The architecture is model-agnostic**: when a new model lands, one configuration change A/B tests it against the current panel. Customer investment carries forward.
- **Limited private preview is open**: [https://aka.ms/AI-drivenScanningHarness](https://aka.ms/AI-drivenScanningHarness)

---

---

## References

- [Defense at AI speed: Microsoft's new multi-model agentic security system tops leading industry benchmark](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/) — Taesoo Kim, VP Agentic Security, Microsoft (May 12, 2026)
- [Sign up for the MDASH private preview](https://aka.ms/AI-drivenScanningHarness) — Microsoft Security
- [DARPA AI Cyber Challenge (AIxCC)](https://aicyberchallenge.com/) — DARPA
- [CyberGym benchmark leaderboard](https://cybergym-leaderboard.github.io/) — CyberGym
