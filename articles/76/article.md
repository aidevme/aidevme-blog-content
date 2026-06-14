# Microsoft's AI Found 16 Windows CVEs — Including 4 Critical RCEs. Here's How the Agentic Pipeline Actually Works

**WordPress SEO**
- **Focus keyphrase:** Microsoft MDASH agentic security system Power Platform
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
- [Two Deep Dives: The Architectural Lessons Worth Stealing](#two-deep-dives-the-architectural-lessons-worth-stealing)
  - [CVE-2026-33827 — Trust Boundary Violation Across Concurrent Subsystems](#cve-2026-33827--trust-boundary-violation-across-concurrent-subsystems)
  - [CVE-2026-33824 — Shallow Copy Creates Implicit Shared Ownership](#cve-2026-33824--shallow-copy-creates-implicit-shared-ownership)
- [How Capable Is MDASH? Retrospective Benchmarks](#how-capable-is-mdash-retrospective-benchmarks)
  - [Recall on Historical MSRC Cases](#recall-on-historical-msrc-cases)
  - [CyberGym Public Benchmark](#cybergym-public-benchmark)
  - [Failure Analysis](#failure-analysis)
- [What This Means for You as a Power Platform Solution Architect](#what-this-means-for-you-as-a-power-platform-solution-architect)
- [Key Takeaways](#key-takeaways)

---

## What MDASH Actually Is

MDASH was built by Microsoft's **Autonomous Code Security (ACS)** team. A few members came from **Team Atlanta** — the group that won the $29.5 million DARPA AI Cyber Challenge by building an autonomous system that found and patched real bugs in complex open-source software. The DARPA challenge is worth knowing about because it required end-to-end proof, not just candidate flagging. You had to demonstrate the exploit, not just describe the vulnerability. That discipline is baked into MDASH's design.

As a Solution Architect, the constraint Microsoft faces with its own codebase is relevant to how you think about security scanning on your client environments:

- **Everything is proprietary.** Windows, Hyper-V, Azure, the driver ecosystem — none of it was ever in a model's training data. The AI can't rely on pattern matching. It has to reason about component-specific trust boundaries, ownership semantics, and concurrency models. Sound familiar? Dataverse has its own calling conventions, transaction boundaries, and plugin execution context that generic tools don't understand either.
- **False positives have a real cost.** Every finding has an owner and a triage queue. A tool that floods teams with noise doesn't get used. The same problem shows up in every enterprise security programme I've seen — alert fatigue kills adoption faster than anything else.
- **High-value targets raise the bar.** Windows and Azure serve billions of users. A single Critical CVE in tcpip.sys is a very bad day for a very large number of people. The acceptable false-positive rate is near zero.

All of that shapes why MDASH is built the way it is. It's not optimised to find the most candidates. It's optimised to find findings that survive being proven.

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

Here's the full list of 16 CVEs from the May 12 Patch Tuesday that MDASH found. As a Solution Architect, pay attention to the components column — `tcpip.sys`, `ikeext.dll`, `netlogon.dll`, `dnsapi.dll`, and `http.sys` are all part of the Windows infrastructure stack that Azure, Entra ID, and Power Platform run on.

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

10 kernel-mode, 6 usermode. Most are reachable from the network **with no credentials required**.

The ones most worth flagging in a client architecture review: the `dnsapi.dll` heap overflow (DNS is everywhere in hybrid environments), the `netlogon.dll` RCE (directly relevant to any AD-connected Power Platform tenant), and both `ikeext.dll` Critical findings (affects any environment using Always-On VPN, DirectAccess, or IPsec connection rules — common in enterprise Power Platform on-premises gateway configurations).

All of these were patched in May Patch Tuesday. But the fact that they were found this way is the news.

---

## Two Deep Dives: The Architectural Lessons Worth Stealing

Microsoft walked through two findings in detail because they illustrate *what multi-model agentic reasoning enables that a single-model harness doesn't*. As a Solution Architect, I'd read these less for the kernel mechanics and more for the design principles — both failures are patterns that appear in Power Platform solutions too.

### CVE-2026-33827 — Trust Boundary Violation Across Concurrent Subsystems

The bug is in the Windows IPv4 receive path. A component drops its reference to a shared object, then reuses the same pointer later. Meanwhile, three separate subsystems — all with legitimate reasons to clean up that object — can concurrently invalidate it. No lock is held. On a multi-processor system, the freed memory can be reclaimed and overwritten before the second access happens.

An attacker can trigger this remotely, with no credentials, using crafted IPv4 packets.

**The architectural lesson:** This is a cross-component ownership bug. One subsystem releases a resource; other subsystems don't know about the release; a third subsystem tries to use it later. The bug is invisible if you look at any single component in isolation. It only becomes visible when you reason about the full lifecycle of a shared object across all the things that touch it.

If you design Dataverse solutions with shared state — plugin chains passing entity references, Power Automate flows operating on the same record concurrently, or Code Apps calling multiple Dataverse APIs in parallel — you're working with the same class of problem. The ownership question (who's responsible for this object at this point in the flow?) is a design decision, not an implementation detail.

**Why single-model AI misses it:** The violation isn't visible in any one file. You need cross-file reasoning to see the inconsistency — specifically, the correct version of the same pattern exists elsewhere in the codebase. MDASH surfaces that comparison; single-model scanners don't.

### CVE-2026-33824 — Shallow Copy Creates Implicit Shared Ownership

This one is in IKEEXT, the Windows IPsec keying service. It's reachable over UDP/500 on any host acting as an IKEv2 responder — which includes environments using Always-On VPN, DirectAccess, or IPsec connection rules. Common in enterprise configurations with on-premises data gateways.

Two UDP packets. Deterministic trigger. Pre-authentication. Runs as LocalSystem.

The root cause: when IKEEXT copies a packet's context, it does a shallow copy of the struct. That copies the pointer to an attacker-supplied buffer but not the buffer itself. Now two parts of the system hold the same pointer and both think they own it. Both free it on teardown. That's a double-free, and in this context it leads to remote code execution as the highest-privilege process on the machine.

**The architectural lesson:** Shallow copy creates implicit shared ownership — and implicit shared ownership creates bugs. This pattern appears in enterprise solutions whenever objects, contexts, or references are passed between components without clearly defining who owns them and when they're released. In Power Platform terms: think about what happens when a plugin passes a service context to a helper class, or when a Code App shares a reference to an auth token across async operations. If ownership isn't explicit, you'll hit the same class of problem — just in managed code rather than C, so the symptoms look different (race conditions in async workflows, stale tokens, unexpected object state) but the design failure is identical.

**Why single-model AI misses it:** The bug spans six source files. The evidence that it's real — the correct pattern done right, one `memcpy` away from the broken one — only appears when you compare across all six. MDASH's agents are built for exactly this cross-file pattern comparison.

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

## What This Means for You as a Power Platform Solution Architect

Let me translate this into the three conversations where it actually matters.

**In client architecture reviews: the platform security story just got stronger.**

When clients ask about the security posture of Power Platform and Azure, most of the conversation centres on configuration — DLP policies, conditional access, network isolation, Managed Environments. That's all valid, but it's one layer. MDASH represents a different layer: Microsoft proactively scanning its own platform infrastructure with production AI at a depth that finds bugs offensive researchers missed for years. The `tcpip.sys` UAF and the IKEv2 RCE in this post were both patched in May. They weren't found by external researchers filing bug bounties. They were found by Microsoft's own system before anyone else could exploit them.

That's a meaningful security posture claim, and it's one you can use with clients who ask the right questions.

**In governance and security framework conversations: shared responsibility just shifted.**

The shared responsibility model for cloud platforms has always assumed Microsoft handles infrastructure-level security and you handle everything above it. MDASH is evidence that Microsoft's half of that contract is now operating at a materially higher level of rigor. That's relevant when you're doing ISO 27001 readiness work, Cyber Essentials Plus assessments, or enterprise security architecture reviews — particularly for clients in regulated industries who need to demonstrate due diligence about the platforms they run on.

The benchmark numbers (96% recall on five years of MSRC cases, 88.45% on CyberGym) give you something concrete to reference if anyone asks for evidence rather than marketing claims.

**In your own solution design: the architectural principles are directly applicable.**

The two CVE deep dives above aren't just Windows war stories. They're case studies in:

- **Shared ownership bugs** — what happens when two components both think they own a resource and neither explicitly transfers that ownership. This is a Dataverse plugin design problem, a Power Automate flow design problem, and a Code App async design problem.
- **Cross-component trust boundary violations** — what happens when a component acts on an object after another component has already released or invalidated it. This shows up in long-running plugin transactions, in gateway connectivity flows, and in any solution that passes context between service layers.

You don't need to write kernel code for these patterns to bite you. You need to design systems where ownership and lifecycle are explicit — not assumed.

**Should you sign up for the MDASH private preview?**

The honest answer: probably not immediately for most Power Platform practices. MDASH is currently targeting low-level platform and infrastructure code — C/C++ codebases, kernel components. It's not scanning your PCF controls or your Dataverse plugin assemblies yet.

What I *would* do is track it. The architectural pattern — multi-model agentic pipeline, specialised agents per stage, extensible proving plugins — is exactly what you'd want applied to managed code security scanning. If Microsoft extends MDASH to .NET and TypeScript targets, that becomes directly relevant to Power Platform development pipelines. [Sign up for the preview](https://aka.ms/AI-drivenScanningHarness) to stay ahead of where this goes.

---

## Key Takeaways

- **16 CVEs found in Windows networking infrastructure** in a single scan cycle — including components (`dnsapi.dll`, `netlogon.dll`, `ikeext.dll`, `http.sys`) directly relevant to enterprise Power Platform and Azure deployments.
- **MDASH closes the full loop**: find → validate → prove → patch → ship. That's the bar automated security tools almost never clear.
- **The five-stage pipeline** (Prepare → Scan → Validate → Dedupe → Prove) is the product. The model is just one input.
- **100+ specialised agents** across stages; multi-model ensemble uses disagreement as a credibility signal.
- **96% recall on 5 years of clfs.sys MSRC cases; 100% on tcpip.sys** — ground-truth retrospective evidence, not just benchmark numbers.
- **88.45% on CyberGym** — top of the public leaderboard, using generally available models.
- **For architecture reviews**: use this as evidence that Microsoft's infrastructure security posture operates at a materially higher level than configuration-layer controls alone.
- **For solution design**: the two CVE deep dives are case studies in shared ownership and cross-component trust boundary design — patterns that apply directly to Dataverse plugins, Power Automate flows, and Code Apps.
- **For tooling decisions**: MDASH targets C/C++ infrastructure code today. Track it for when it extends to .NET and TypeScript targets.
- **Private preview is open**: [https://aka.ms/AI-drivenScanningHarness](https://aka.ms/AI-drivenScanningHarness)

---

---

## References

- [Defense at AI speed: Microsoft's new multi-model agentic security system tops leading industry benchmark](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/) — Taesoo Kim, VP Agentic Security, Microsoft (May 12, 2026)
- [Sign up for the MDASH private preview](https://aka.ms/AI-drivenScanningHarness) — Microsoft Security
- [DARPA AI Cyber Challenge (AIxCC)](https://aicyberchallenge.com/) — DARPA
- [CyberGym benchmark leaderboard](https://cybergym-leaderboard.github.io/) — CyberGym
