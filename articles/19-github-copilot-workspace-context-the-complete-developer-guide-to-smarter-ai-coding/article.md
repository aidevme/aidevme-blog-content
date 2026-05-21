# GitHub Copilot Workspace Context Explained - Practical AI, Copilot & Modern Development Insights

Estimated reading time: 15 minutes

If you have ever typed `@workspace how does authentication work?` into Copilot Chat and got a blank stare back, this article is for you. Understanding how Copilot actually reads your codebase — and how to control what it sees — is the single biggest lever for getting useful AI responses in a real project.

This guide goes deep on workspace context: how indexing works, when to use `#codebase` vs `@workspace`, how to write `copilot-instructions.md`, and practical prompt patterns for everyday tasks.

## Table of contents

-   [What Is Workspace Context — and Why Should You Care?](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-what-is-workspace-context-and-why-should-you-care)

-   [How Copilot Indexes Your Codebase](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-how-copilot-indexes-your-codebase)
-   [Index Types: Remote, Local, and Basic](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-index-types-remote-local-and-basic)
    -   [Remote Index (GitHub / Azure DevOps)](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-remote-index-github-azure-devops)
    -   [Local Index](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-local-index)
    -   [Basic Index](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-basic-index)
-   [codebase vs @workspace — Stop Confusing Them](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-codebase-vs-workspace-stop-confusing-them)
    -   [@workspace](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-workspace)
    -   [#codebase](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-codebase)
    -   [Which one should you use?](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-which-one-should-you-use)
-   [Practical Prompt Patterns That Work](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-practical-prompt-patterns-that-work)
    -   [Pattern 1: Name the thing you’re looking for](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-pattern-1-name-the-thing-you-re-looking-for)
    -   [Pattern 2: Cross-file tracing](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-pattern-2-cross-file-tracing)
    -   [Pattern 3: “Show me an example” prompts](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-pattern-3-show-me-an-example-prompts)
    -   [Pattern 4: “Where is X handled?”](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-pattern-4-where-is-x-handled)
    -   [Pattern 5: Combined context](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-pattern-5-combined-context)
    -   [Pattern 6: “How do I add X following our pattern?”](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-pattern-6-how-do-i-add-x-following-our-pattern)
    -   [Prompts That Don’t Work Well](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-prompts-that-don-t-work-well)
-   [Custom Instructions: copilot-instructions.md](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-custom-instructions-copilot-instructions-md)
    -   [What NOT to put in copilot-instructions.md](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-what-not-to-put-in-copilot-instructions-md)
-   [Path-Specific Instructions with .instructions.md](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-path-specific-instructions-with-instructions-md)

-   [Multi-Repository Workspaces](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-multi-repository-workspaces)
-   [What Copilot Cannot See — and How to Fix It](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-what-copilot-cannot-see-and-how-to-fix-it)

-   [Troubleshooting Workspace Context](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-troubleshooting-workspace-context)
    -   [Copilot gives generic answers, not project-specific ones](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-copilot-gives-generic-answers-not-project-specific-ones)
    -   [Copilot ignores your copilot-instructions.md](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-copilot-ignores-your-copilot-instructions-md)
    -   [Local index fails to build or stays stuck](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-local-index-fails-to-build-or-stays-stuck)
    -   [Copilot retrieves the wrong files](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-copilot-retrieves-the-wrong-files)
    -   [Copilot doesn’t know about code you just wrote](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-copilot-doesn-t-know-about-code-you-just-wrote)
    -   [Verify your index is being used](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-verify-your-index-is-being-used)
    -   [Does Copilot use my code to train its models?](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-does-copilot-use-my-code-to-train-its-models)
    -   [Which branch does the remote index use?](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-which-branch-does-the-remote-index-use)
    -   [Is the remote index shared across my team?](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-is-the-remote-index-shared-across-my-team)
    -   [Can I disable codebase indexing?](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-can-i-disable-codebase-indexing)
    -   [“github.copilot.codebase”: “off”](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-github-copilot-codebase-off)
-   [Summary](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-summary)

-   [References](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/#h-references)

## What Is Workspace Context — and Why Should You Care?

When you ask Copilot a question in chat, it doesn’t just look at the file you have open. With workspace context enabled, Copilot can search your entire project — across files, folders, symbols, and function signatures — to assemble an answer grounded in your actual code.

This is what makes questions like these actually useful:

-   *“Where is the JWT token being validated?”*

-   *“Show me all places that call the `sendEmail` helper.”*
-   *“How do I add a new route following the existing pattern?”*

Without workspace context, Copilot is essentially blindfolded. It guesses based on the current file and generic training data. With workspace context, it reasons across the full project structure, just like a developer who has read the whole codebase.

---

## How Copilot Indexes Your Codebase

Copilot doesn’t scan your files on every prompt. It builds and maintains an **index** — a searchable representation of your code — and queries it when it needs to answer workspace-level questions.

When you submit a prompt, Copilot follows roughly these steps:

1.  **Intent detection** — Does this question need codebase context? A question like “fix this null check” doesn’t. “Where is the DB connection pool configured?” does.
2.  **Index query** — Copilot searches the index using one or more strategies in parallel and picks the fastest relevant result:
    -   GitHub’s remote code search
    -   Local semantic (vector) search — finds code by *meaning*, not just keywords
    -   Text-based file name and content search
    -   VS Code IntelliSense — resolves symbols, function signatures, type hierarchies
3.  **Context assembly** — Relevant snippets are collected and inserted into the prompt context window. If there’s too much, only the most relevant parts are kept.
4.  **Answer generation** — The model generates a response grounded in your actual code.

GITHUB COPILOT — CONTEXT RETRIEVAL PIPELINE Developer types prompt Intent detection Needs codebase context? No Answer from current file \+ training data Yes Index query Run strategies in parallel GitHub remote Code search Local semantic Vector search Text-based File/content search VS Code IntelliSense Symbols & signatures Context assembly Top relevant snippets selected Fits context window? Yes No All snippets included Only most relevant snippets kept Answer generated grounded in your code

**Practical takeaway:** If Copilot gives a wrong answer, it’s often because the wrong snippets were retrieved. Better prompt phrasing (see section 5) improves retrieval, not just generation.

---

## Index Types: Remote, Local, and Basic

Copilot uses different index types depending on your setup. Knowing which one you have matters because it directly affects quality.

GITHUB COPILOT — INDEX SELECTION PIPELINE Your Repository Hosted on GitHub or Azure DevOps? Yes Remote Index ⭐ Best quality Shared across team Auto-updated on push No File count? < 750 files 750–2500 \> 2500 Local Index Auto-built Good semantic quality Stored on your machine Local Index Run ‘Build local workspace index’ once manually Basic Index Keyword-based only Lower accuracy Fast + Accurate codebase answers Works for simple queries Upgrade recommended

### Remote Index (GitHub / Azure DevOps)

The best option. GitHub automatically builds and maintains a semantic index of your repository. It’s based on the **committed state of your default branch** (usually `main`).

**How to check your index status:** Click the Copilot icon in the VS Code Status Bar → you’ll see the index type and its current state.

**How to trigger indexing manually:**

Markdown

```
Ctrl+Shift+P → "Build Remote Workspace Index"
```

**Key facts:**

-   Index builds in seconds for most repos (up to 60 seconds for very large ones).

-   Rebuilds automatically after pushes.
-   Shared across all teammates with repo access.

-   **Does NOT include uncommitted local changes** — but VS Code detects modified files and layers them on top in real time

Push frequently. The remote index is only as fresh as your last push.

---

### Local Index

Used when you don’t have a GitHub or Azure DevOps remote. Stored on your machine.

| **File count** | **Behavior** |
| < 750 files | Auto-built |
| 750–2500 files | Run `Build local workspace index` manually (once) |
| 2500 files | Falls back to Basic index |

---

### Basic Index

The fallback for large local repos. Uses simpler keyword-based algorithms. Works for many queries but struggles with semantic questions like “show me examples of how errors are handled.” If accuracy matters, upgrade to a remote index.

---

## codebase vs @workspace — Stop Confusing Them

This trips up almost every developer the first time. Here’s the practical difference:

GITHUB COPILOT CONTEXT MECHANISMS #codebase vs @workspace @workspace — Chat Participant Your prompt Handed off entirely to @workspace agent Codebase search only Answer LIMITATIONS ❌ Cannot use other tools ❌ Cannot combine sources ✅ Focused codebase expert USE FOR: pure codebase questions #codebase — Tool / Context Variable Your prompt Language model stays in control orchestrates all tool calls Calls #codebase tool Calls other tools #terminalLastCommand #file, web search… Combined answer CAPABILITIES ✅ Multiple tool calls per prompt ✅ Mix with any context source ✅ Agentic multi-step search ⭐ RECOMMENDED DEFAULT VS KEY INSIGHT Both search your codebase — but #codebase lets the model combine results with terminal output, open files, and other tools. @workspace handles the entire prompt alone, with no tool mixing. WHEN TO USE @workspace → Pure “explain this codebase” questions → You want a codebase-only expert agent → Simple one-shot lookup questions → Familiar, older workflow you trust Only one participant per chat prompt WHEN TO USE #codebase → Combining codebase + terminal errors → Agentic multi-step investigations → Mixing with open file context → Most everyday coding questions ✦ Use this in almost all cases

### @workspace

`@workspace` is a **chat participant**. When you use it, the entire prompt is handed off to a specialized agent that focuses exclusively on codebase questions. The base language model steps back — it can’t invoke other tools or combine results with other sources.

Markdown

```
@workspace how is the payment service initialized?
```

### #codebase

`#codebase` is a **tool** (a context variable). The model can call it multiple times, mix it with other tools, and combine it with other context like terminal output, open files, or web search results.

Markdown

```
Based on #codebase and the error in #terminalLastCommand, 
why is the AuthService throwing a NullReferenceException?
```

### Which one should you use?

**Use `#codebase` in almost all cases.** It’s more flexible, can be combined with other context, and the model can invoke it multiple times during agentic searches.

Use `@workspace` only when you want to force a pure codebase question without any other tool involvement, or if you’re used to the older pattern and it works for you.

You don’t always need either. In Agent and Ask modes, Copilot automatically triggers a codebase search when your prompt implies one. Explicit `#codebase` is useful when your question is ambiguous.

---

## Practical Prompt Patterns That Work

The quality of Copilot’s answer is heavily influenced by how you phrase the question. Here are patterns that consistently produce better results.

### Pattern 1: Name the thing you’re looking for

**Weak:**

Markdown

```
how does this work
```

**Strong:**

Markdown

```
#codebase how does the TokenRefreshMiddleware intercept expired JWT tokens?
```

Use the actual class names, function names, or file names from your project. These terms appear in the index and dramatically improve retrieval.

---

### Pattern 2: Cross-file tracing

Markdown

```
#codebase show me the full call chain from the CreateOrderController 
action to the database write in OrderRepository
```

This works well for tracing data flow, finding where a side effect is triggered, or understanding a complex async pipeline.

---

### Pattern 3: “Show me an example” prompts

Markdown

```
#codebase show me two or three existing examples of how we 
implement repository classes in this project so I can follow the pattern
```

This leverages Copilot’s retrieval strength — finding real examples from your codebase rather than generating generic boilerplate.

---

### Pattern 4: “Where is X handled?”

Markdown

```
#codebase where is global exception handling configured 
and what HTTP status codes do we return?
```

Great for onboarding to a new codebase or finding the right place to make a change.

---

### Pattern 5: Combined context

Markdown

```
#codebase #terminalLastCommand 
The build is failing. Based on our project structure, 
what is the most likely cause and which file should I check first?
```

Combining `#codebase` with terminal output, selected code, or open files gives Copilot a much richer picture.

---

### Pattern 6: “How do I add X following our pattern?”

Markdown

```
#codebase I need to add a new REST endpoint for exporting invoices as PDF.
Show me how an existing endpoint is structured end-to-end, 
then generate the new one following the same pattern.
```

This is one of the most powerful use cases — forcing Copilot to learn your conventions before generating new code.

---

### Prompts That Don’t Work Well

Avoid these — Copilot’s workspace search isn’t designed for exhaustive analysis:

-   `#codebase how many times is this function called across the project?` — Use VS Code’s “Find All References” instead

-   `#codebase fix all the TypeScript errors in the project` — Too broad, will miss most of them
-   `#codebase what is the test coverage percentage?` — Use your coverage tool

---

## Custom Instructions: copilot-instructions.md

This is the most underused feature for teams. A `copilot-instructions.md` file tells Copilot about your project before any question is asked — your stack, conventions, naming rules, and team preferences.

**Create the file**

Bash

```
mkdir -p .github
touch .github/copilot-instructions.md
```

**Example for a TypeScript + Node.js API project**

Markdown

```


# Project: InvoicingAPI

## Stack
- Node.js 20, TypeScript 5, Express 4

- Prisma ORM, PostgreSQL
- Jest for testing, Supertest for API tests

- Deployed to Azure Container Apps

## Conventions
- Use `async/await`, never raw Promise chains

- All controllers are thin — business logic lives in services
- Services receive dependencies via constructor injection

- Never use `any` in TypeScript — use `unknown` and narrow properly
- Errors are wrapped in `AppError` with an `httpStatus` code

## File Structure
- Controllers: `src/controllers/`

- Services: `src/services/`
- Repositories: `src/repositories/`

- DTOs: `src/dtos/`
- Middleware: `src/middleware/`

## Testing
- Unit tests live next to source files: `MyService.test.ts`

- Integration tests are in `tests/integration/`
- Always mock the repository layer in unit tests
```

### What NOT to put in copilot-instructions.md

Based on Microsoft’s guidance, these don’t work well:

-   Instructions to reference external style guides in other repos.

-   Instructions to “always answer in a friendly tone”.
-   Instructions to “always use detailed explanations”

**Keep it factual and structural. What is the stack? What are the naming conventions? Where do things live?**

Copilot code review only reads the first 4,000 characters of the file. Keep it focused. Chat and agent modes have higher limits.

---

## Path-Specific Instructions with .instructions.md

For larger projects, a single global file isn’t enough. You can create zone-specific instruction files that Copilot applies only when working on matching files.

**The Full .github Instructions Folder Layout**

**Location**

Markdown

```
.github/instructions/
  testing.instructions.md
  frontend.instructions.md
  migrations.instructions.md
```

**Example: Testing conventions**

Markdown

```
---
applyTo: "**/__tests__/**/*.ts,**/*.test.ts,**/*.spec.ts"
---

## Testing Guidelines

- Use Jest with ts-jest

- Use `@faker-js/faker` for test data generation — never hardcode GUIDs
- Mock external HTTP calls with `msw` (Mock Service Worker)

- Assert on user-visible outcomes, not implementation details
- Every test file must have a `describe` block named after the module under test
```

**Example: Database migrations**

Markdown

```
---
applyTo: "src/migrations/**/*.ts"
---

## Migration Rules

- Never modify an existing migration — always create a new one

- All migrations must be reversible — include both `up()` and `down()` methods
- Column names use snake_case

- Always add an index for foreign keys
```

These files are version-controlled and shared with your team automatically — the whole team gets the same Copilot behavior.

---

## Multi-Repository Workspaces

If your application spans multiple repos (common in microservice architectures), Copilot can only index what’s in your open VS Code workspace. If you open only the `auth-service` repo, Copilot doesn’t know anything about `order-service`.

**The Fix: Use a .code-workspace file**

Create a workspace definition file that opens all required repos together:

JSON

```
{
  "folders": [
    { "path": "../auth-service" },
    { "path": "../order-service" },
    { "path": "../shared-lib" }
  ],
  "settings": {}
}
```

Save this as `my-app.code-workspace` in a shared “developer experience” repo. Team members open it with **File → Open Workspace from File**.

**Index limits for multi-repo**

The local index limit is 2,500 files **across the entire workspace**. For multi-repo setups this adds up fast. Prefer remote indexing via GitHub for any serious multi-service project.

---

## What Copilot Cannot See — and How to Fix It

Knowing the blind spots helps you compensate.

| **Situation** | **What Copilot misses** | **Workaround** |
| Uncommitted changes | New files not yet pushed | The active editor content is included in real-time — open the relevant files |
| Files in `.gitignore` | `node_modules`, build output, secrets | This is intentional. Open the file directly if you need Copilot to reference it |
| Binary files | Images, PDFs, compiled DLLs | Not indexed. Describe them in text comments or docs |
| 2,500 files (local) | Files beyond the limit | Use remote indexing (GitHub/Azure DevOps) |
| Private GitHub Enterprise Server | Remote index not available | Use local index + keep file count manageable |

---

## Troubleshooting Workspace Context

Most workspace context problems fall into one of five categories: the index isn’t built, the index is stale, the prompt doesn’t trigger retrieval, the instructions file isn’t being loaded, or Copilot is pulling the wrong files. Work through each scenario below systematically before assuming something is broken.

The Full .github Instructions Folder Layout

### Copilot gives generic answers, not project-specific ones

This is the most common complaint. It usually means Copilot either couldn’t find relevant code in the index, or the codebase search wasn’t triggered at all.

**Diagnosis steps:**

1.  Click the Copilot icon in the VS Code Status Bar → check index type and state. If it shows “Building” or “Not indexed”, wait for it to complete or trigger it manually.
2.  If using a local index, run `Build local workspace index` from the Command Palette. If the command is grayed out, your project exceeds 2,500 files and you need a remote index.
3.  If using a remote index, check when you last pushed. The remote index reflects the committed state — if your key changes are still local, Copilot won’t see them. Push first, then ask again.
4.  Rephrase your prompt using actual names from your code — class names, method names, file names. Vague prompts like “how does this service work” produce vague answers because the retrieval step finds nothing specific to latch onto.
5.  Add `#codebase` explicitly to your prompt to force a codebase search even if Copilot’s intent detection doesn’t trigger one automatically.

**Quick test:** Ask `#codebase what is the entry point of this application?` and expand the References panel. If you see files listed there, the index is working. If the panel is empty, the index is the problem.

---

### Copilot ignores your copilot-instructions.md

Instructions files are silently ignored when they’re in the wrong location or when the setting is disabled — Copilot won’t warn you.

**Diagnosis steps:**

1.  Confirm the exact path: the file must be at `.github/copilot-instructions.md` in the **workspace root**, not in a subfolder or the repo root of a nested project.
2.  Open VS Code Settings (`Ctrl+,`) and search for `instruction files`. Confirm that **Code Generation: Use Instruction Files** is checked. It’s enabled by default but can be accidentally turned off.
3.  Right-click inside the Chat view → **Diagnostics**. This opens a panel that lists every loaded instruction file and any loading errors. If your file doesn’t appear here, it’s not being loaded regardless of what you type.
4.  Check file size. Copilot code review only reads the first **4,000 characters** of `copilot-instructions.md`. If your instructions are longer, anything past that limit is silently ignored during code review. Chat and agent modes have higher limits but keeping the file concise is still best practice.
5.  Avoid instructions that reference external resources, ask Copilot to adopt a persona, or specify response style. These types of instructions are documented by Microsoft as unreliable. Stick to factual content: stack, conventions, folder structure, naming rules.

**After any change to the file**, you don’t need to restart VS Code — the updated instructions are picked up on the next chat request.

---

### Local index fails to build or stays stuck

**Diagnosis steps:**

1.  Check your indexable file count. Open the Command Palette and run `Build local workspace index`. If it doesn’t appear or is unavailable, you’ve exceeded the 2,500 file limit and must use a remote index instead.
2.  Check your `.gitignore`. The most common cause of hitting the file limit unexpectedly is `node_modules`, `dist`, `.next`, `__pycache__`, or other generated directories not being excluded. Add them to `.gitignore` and the index file count drops immediately.
3.  Check the `files.exclude` setting in VS Code. Any pattern listed there is also excluded from the index. If you’re intentionally excluding large folders, this helps keep the count manageable.
4.  If the index shows as “Building” for more than a few minutes on a large local repo, close and reopen VS Code. The indexing process runs in the background and can stall after a branch switch that changes many files simultaneously.
5.  Switching git branches invalidates parts of the index. After a large branch switch, allow a minute for the index to catch up before querying it.

---

### Copilot retrieves the wrong files

Sometimes the index works fine but Copilot pulls in irrelevant code — a common symptom when your project has many files with similar names or patterns.

**Diagnosis steps:**

1.  Expand the **References** panel below any Copilot response to see exactly which files were retrieved. If you see the wrong files, the retrieval query needs to be more specific.
2.  Use the actual symbol names in your prompt. Semantic search finds code by meaning, but including the precise function or class name makes retrieval much more targeted.
3.  Open the relevant files in your editor before asking. Currently open and visible files are always included in context, which anchors Copilot’s search around the right area of the codebase.
4.  If you’re in a multi-root workspace and Copilot consistently pulls from the wrong repo, check which folders are included in your `.code-workspace` file and whether the target repo is actually open.

---

### Copilot doesn’t know about code you just wrote

This happens because the remote index reflects committed code, not your local working copy.

**Diagnosis steps:**

1.  For brand-new files, open them in the editor. Currently open file content is always passed to Copilot in real time, regardless of index state.
2.  For changes across multiple files, commit and push to GitHub. The remote index updates automatically within seconds to a minute after a push.
3.  If you’re on a feature branch, remember that the remote index is built from the default branch only. Code that exists only on your branch is visible to Copilot only through open editor files and the hybrid local file tracking — not through full codebase search.

---

### Verify your index is being used

After asking a codebase question, expand the **References** section below the Copilot response. You’ll see which files were pulled into context, with clickable links to each one. This is your primary debugging tool.

-   **Files listed** → index is working, retrieval happened.

-   **No files listed** → codebase search was not triggered; add `#codebase` explicitly or rephrase the prompt.
-   **Wrong files listed** → retrieval happened but pulled the wrong code; use more specific terms or open the target files in the editor first**.**

-   **Instructions file listed** → your `copilot-instructions.md` was loaded and applied to this request

---

## Frequently Asked Questions

### Does Copilot use my code to train its models?

No. Your indexed codebase is not used for model training. The index is used only to provide context for your own chat sessions.

### Which branch does the remote index use?

The default branch (`main` or `master`). Feature branches are not separately indexed.

### Is the remote index shared across my team?

Yes. The remote index is per-repository and shared by everyone with access. Your local editor state (open files, unsaved changes) remains private.

### Can I disable codebase indexing?

Yes. Add this to your VS Code `settings.json`:

JSON

```
"github.copilot.codebase": "off"
```

### “github.copilot.codebase”: “off”

It falls back to a local index. The local index works without GitHub but has the 2,500-file limit and lower accuracy than the remote semantic index.

---

## Summary

Getting the most out of GitHub Copilot isn’t about typing better prompts — it’s about giving Copilot the right foundation to work from. Workspace context is that foundation.

The single highest-impact action you can take right now is to **host your code on GitHub and sign in with your GitHub account in VS Code**. This unlocks the remote semantic index, which is faster, more accurate, and shared automatically across your team — no configuration required. Everything else in this guide builds on top of that.

The second biggest win is a `copilot-instructions.md` file. Most developers skip this entirely. A well-written file means Copilot understands your stack, your naming conventions, and your folder structure before you type a single prompt. For teams, this is the equivalent of a codebase onboarding doc that Copilot reads on every request.

For day-to-day usage, the shift from `@workspace` to `#codebase` is worth making. It’s more flexible, works inside agentic workflows, and can be combined with other context variables like `#terminalLastCommand` or open files. And remember — in Agent and Ask modes, you often don’t need either. Copilot detects workspace intent automatically.

Finally, when something isn’t working — wrong answers, generic responses, instructions being ignored — the **References panel** and the **Diagnostics view** are your two debugging tools. Check them before assuming Copilot is broken. Nine times out of ten, the index just needs a push or the instructions file is in the wrong location.

**Here’s the full quick-reference checklist:**

| **Feature** | **What to do** |
| Enable best indexing | Use a GitHub-hosted repo + sign in with GitHub in VS Code |
| Check index status | Click the Copilot status bar icon |
| Trigger manual indexing | `Ctrl+Shift+P → Build Remote Workspace Index` |
| Ask workspace questions | Use `#codebase` in your prompt |
| Set project conventions | Create `.github/copilot-instructions.md` |
| Set zone-specific rules | Create `.github/instructions/*.instructions.md` |
| Multi-repo setup | Use a `.code-workspace` file |
| Debug missing context | Right-click Chat view → Diagnostics |

---

## References

-   [VS Code — Make chat an expert in your workspace](https://code.visualstudio.com/docs/copilot/reference/workspace-context)

-   [VS Code — Use custom instructions in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
-   [GitHub Docs — Indexing repositories for GitHub Copilot Chat](https://docs.github.com/copilot/concepts/indexing-repositories-for-copilot-chat)

-   [GitHub Docs — Adding custom instructions for GitHub Copilot](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
-   [GitHub Changelog — Instant semantic code search indexing now generally available](https://github.blog/changelog/2025-03-12-instant-semantic-code-search-indexing-now-generally-available-for-github-copilot/)

-   [GitHub Copilot Trust Center — Security & Privacy](https://resources.github.com/copilot-trust-center/)
-   [Microsoft Learn — How Copilot Chat uses context (Visual Studio)](https://learn.microsoft.com/visualstudio/ide/copilot-context-overview)

-   [GitHub Community — #codebase vs @workspace discussion](https://github.com/orgs/community/discussions/114471)
-   [GitHub Community — Optimizing Copilot for multi-repository teams](https://github.com/orgs/community/discussions/175497)

-   [github/awesome-copilot — Community-contributed instructions and customizations](https://github.com/github/awesome-copilot)

### *Related*

[![GitHub Copilot Agentic Memory vs Stateless AI](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/02/github-copilot-agentic-memory-what-it-is-how-it-works-featured.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/ "GitHub Copilot Agentic Memory: What It Is, How It Works?")

#### [GitHub Copilot Agentic Memory: What It Is, How It Works?](https://aidevme.com/github-copilot-agentic-memory-what-it-is-how-it-works/ "GitHub Copilot Agentic Memory: What It Is, How It Works?")

GitHub Copilot just launched a persistent, repository-scoped agentic memory system in public preview. Instead of starting from scratch every session, Copilot now learns your codebase conventions over time and shares that knowledge across the coding agent, code review, and CLI. In this article, we explore how it works under the…

February 24, 2026

In "AI & Copilot"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [GitHub Copilot Workspace Context: The Complete Developer Guide to Smarter AI Coding](https://aidevme.com/github-copilot-workspace-context-the-complete-developer-guide-to-smarter-ai-coding/)