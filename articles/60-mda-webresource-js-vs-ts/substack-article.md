# JavaScript vs TypeScript Web Resources in Model-Driven Apps: Complete Guide (2026)

*Plain JavaScript is quick to ship. TypeScript bundled with Webpack or esbuild is built to scale. Here's everything you need to make an informed choice.*

---

If you've spent any time building Model-Driven App customisations, you've written a JavaScript web resource. For a long time that was the only option — drop a `.js` file into a solution, wire it to a form event, publish. It still works.

But the ecosystem has moved on. TypeScript is now the default for serious frontend work. `@types/xrm` gives you full IntelliSense for the entire Xrm client API. esbuild can bundle your TypeScript in under 100ms. And npm workspaces let a team of five developers each own their own form package without ever touching the same file.

The question isn't whether you *can* use TypeScript for web resources. The question is *when it makes sense* — and when plain JavaScript is still the faster path.

---

## What the guide covers

I implemented the same contact form logic in all three approaches — on `firstname` or `lastname` change, compose a greeting, fetch the related account name via `Xrm.WebApi`, and show a validation error if both fields are empty — so you can compare them directly:

**Approach 1: Plain JavaScript**
The classic `var aidevme = aidevme || {}` pattern. Zero build step, no toolchain, nothing to maintain. Still the right choice for one-off scripts and solo developers who need to ship fast.

**Approach 2: TypeScript + Webpack**
Full type safety, module system, rich plugin ecosystem. The right call when your team already uses Webpack or needs advanced bundling features. The cost: cold builds can hit 30 seconds, and `webpack.config.js` grows.

**Approach 3: TypeScript + esbuild**
Same type safety, a fraction of the configuration, and builds that complete in under 100ms. The better default for new projects — especially if you're already writing Code Apps or PCF controls in TypeScript, because the toolchain is nearly identical.

---

## The part most guides skip: multi-developer projects

A single-bundle approach breaks down the moment a second developer joins. Two people editing the same `index.ts` creates merge conflicts on logic that has nothing to do with each other.

The guide walks through an **npm workspace monorepo** where each form area and ribbon area is its own package — `@aidevme/contact-form`, `@aidevme/account-ribbon` — all consuming a shared internal `@aidevme/shared` package with typed WebApi service helpers and notification utilities. Full TypeScript IntelliSense across the repo, per-package CI builds that only rebuild what changed, and merge conflicts that are genuinely rare.

---

## And deployment

Five scenarios, with full YAML:

- Manual upload via the maker portal (for first-time setup)
- `pac webresource upload` for local developer iteration
- GitHub Actions with per-package path filtering
- GitHub Actions with environment promotion and reviewer approval gates
- Azure DevOps multi-stage pipelines with Power Platform Build Tools

Plus a decision guide on when to move from one to the next — and the signs that you've outgrown your current method.

---

## The key insight

These three approaches aren't competing. They're a natural progression.

You start with plain JavaScript. You add TypeScript + esbuild when the script grows beyond one file. You add workspaces when a second developer joins. You add CI/CD when you need test and production environments. Each step is incremental — you don't have to do it all at once.

---

**Read the full guide →**
[JavaScript vs TypeScript Web Resources in Model-Driven Apps: Complete Guide (2026)](https://aidevme.com/javascript-vs-typescript-web-resources-in-model-driven-apps-complete-guide/)

---

*If this was useful, forward it to a colleague who's still copy-pasting utility functions between web resource files. They'll thank you.*