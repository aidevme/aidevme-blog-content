# Image Generation Prompts — Article 60
# JavaScript vs TypeScript Web Resources in Model-Driven Apps: Complete Guide (2026)

---

## 1. Featured Image

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-hero.png`

**Alt text:** JavaScript vs TypeScript web resources in Model-Driven Apps — plain JS, Webpack, and esbuild comparison with Power Platform CLI deployment

**Description:** Featured image for the article comparing plain JavaScript, TypeScript + Webpack, and TypeScript + esbuild as approaches for Model-Driven App web resources. Should convey the idea of a developer choosing between code paradigms for Power Platform customization — technical, decisive, and modern. Displayed at 1200×628 (social/OG) and as the WordPress featured image at the top of the post.

**Generation prompt:**
Dark-background tech illustration. Three vertically divided panels side by side, each representing one approach. Left panel (warm amber tint): a single raw `.js` file icon with a lightning bolt below it — fast, direct, minimal. Centre panel (cool blue tint): a `webpack.config.js` file icon above a bundle output arrow, surrounded by small module block icons suggesting the bundler's dependency graph — structured and intricate. Right panel (vivid green tint): an esbuild rocket or lightning-bolt logo, with a sub-100ms build time badge glowing below it — blazing fast. All three panels are connected at the base by a single glowing Power Platform hexagon, implying they all target the same deployment destination. Above all panels, a faint Xrm API type definition ghost text floats as a watermark. Color palette: near-black (#0d1117) background, amber for JS panel, electric blue for Webpack panel, bright green for esbuild panel, teal for the shared Power Platform base. Flat vector style with panel dividers rendered as subtle glowing lines.

---

## 2. Why This Question Matters Now

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-why-this-question-matters-now.png`

**Alt text:** The evolution of Model-Driven App web resource development from plain JavaScript to TypeScript with modern build tooling

**Description:** Illustrates the evolution storyline: plain `.js` files from the Dynamics CRM era giving way to TypeScript with `@types/xrm`, modern bundlers, and IntelliSense. Positioned at the start of the "Why This Question Matters Now" section to immediately frame the historical shift.

**Generation prompt:**
Dark tech illustration. A horizontal timeline running left to right. On the far left, an older-style file icon labelled with a subtle "CRM" badge — muted, monochrome. Moving right, the timeline brightens progressively: a TypeScript logo (blue T icon) appears, then a `@types/xrm` type-definition ghost (showing an Xrm namespace autocomplete popup), then a Webpack gear and an esbuild bolt. The final right end of the timeline glows brightest — representing the modern era. A faint VS Code logo sits above the midpoint with an IntelliSense dropdown suggesting type-aware code. Color palette: near-black background, muted grey-to-teal gradient along the timeline, TypeScript blue (#3178c6), bright teal for the modern end. Flat vector with progressive glow intensity increasing left to right.

---

## 3. The Example We'll Use

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-contact-form-example-overview.png`

**Alt text:** Contact form example — name change handler, Xrm.WebApi account lookup, and form notification flow

**Description:** Shows the three-part business logic used as the running example throughout the article: the `firstname`/`lastname` change event, a `Xrm.WebApi` call to fetch the related Account, and a form notification banner. Positioned above the example definition to give readers a quick mental model before the code starts.

**Generation prompt:**
Dark tech illustration. A simplified Model-Driven App Contact form wireframe in the centre. Three numbered callout bubbles point to specific areas: (1) two text field outlines labelled "First Name" and "Last Name" with a small onChange event icon — an arrow looping back; (2) a cloud/API icon with an arrow pointing to an Account record chip, suggesting a WebApi lookup; (3) a horizontal notification banner at the top of the form glowing blue, representing the INFO notification. Thin connecting lines flow between the callouts in order. Color palette: dark background, form wireframe in dark slate, callout bubbles in electric blue for (1), teal for (2), soft green for (3). Flat vector UI-mockup style.

---

## 4. Approach 1: Plain JavaScript

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-approach-plain-javascript.png`

**Alt text:** Plain JavaScript web resource — single JS file uploaded directly to a Dynamics 365 Model-Driven App solution

**Description:** Illustrates the plain JavaScript approach: a single `.js` file, no build step, uploaded directly through the maker portal. Used at the top of the Plain JavaScript section. Should feel simple, direct, and uncluttered — matching the nature of the approach.

**Generation prompt:**
Dark tech illustration. A single large `aidevme_contact_form.js` file icon in the centre, rendered in warm amber with a JavaScript "JS" badge. A simple single-step arrow flows from the file icon to a Power Platform solution box (hexagonal icon, soft purple) — labelled only with an upload arrow icon, no intermediary steps. Below the solution box, a small Model-Driven App form outline appears, connected by a thin wiring line with an "OnLoad" event tag. The surrounding space is intentionally empty — conveying the zero-build-step simplicity. Color palette: near-black background, amber for the JS file icon, purple for Power Platform solution, white arrows. Flat vector, clean and uncluttered composition.

---

## 5. Approach 2: TypeScript + Webpack

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-approach-typescript-webpack.png`

**Alt text:** TypeScript and Webpack build pipeline for Model-Driven App web resources — ts-loader, bundling, and minified output

**Description:** Illustrates the TypeScript + Webpack workflow: multiple `.ts` source files fed through ts-loader into Webpack, producing a single minified `.js` bundle. Positions the bundler's dependency resolution and plugin pipeline as the key complexity. Used at the top of the TypeScript + Webpack section.

**Generation prompt:**
Dark tech illustration. A pipeline diagram flowing left to right. On the far left, three `.ts` file icons stacked vertically (index.ts, accountService.ts, notifications.ts) in TypeScript blue. An arrow labeled "ts-loader" (a small gear/cog icon) connects them to a central Webpack box (a stylised cube icon in dark blue). From the Webpack box, a narrowing funnel or compressor symbol flows right, then a single output file `aidevme_contact_form.js` glows in bright amber on the far right — minified/compressed as indicated by a small compression badge. Below the Webpack box, small plugin/module icons (representing optimization, source-map) float as satellites. Color palette: near-black background, TypeScript blue (#3178c6) for inputs, dark navy for Webpack, amber for output. Flat vector pipeline diagram style.

---

## 6. Approach 3: TypeScript + esbuild

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-approach-typescript-esbuild.png`

**Alt text:** TypeScript and esbuild build pipeline — sub-100ms bundling for Model-Driven App web resources

**Description:** Illustrates the esbuild approach: same TypeScript source files as Webpack but running through esbuild (written in Go) producing a bundle in under 100ms. Emphasises speed as the differentiator. Used at the top of the TypeScript + esbuild section.

**Generation prompt:**
Dark tech illustration. A pipeline diagram identical in structure to the Webpack image, but the central bundler element is now an esbuild lightning-bolt icon in bright green instead of the Webpack cube. A large prominent "< 100ms" badge with a stopwatch icon glows in vivid green above the pipeline — the speed is the hero. The input `.ts` files on the left are the same. The output `aidevme_contact_form.js` on the far right glows amber. A small separate `tsc --noEmit` step branches off below the esbuild box with a warning/type-check icon — signifying the separate typecheck concern. Color palette: near-black background, TypeScript blue for inputs, vivid green (#22c55e) for esbuild, amber for output. Flat vector pipeline diagram, same scale and layout feel as the Webpack image for easy comparison.

---

## 7. Side-by-Side Comparison

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-side-by-side-comparison-table.png`

**Alt text:** Side-by-side comparison of plain JavaScript, TypeScript + Webpack, and TypeScript + esbuild for Model-Driven App web resources

**Description:** A visual representation of the comparison table — three columns for each approach rated across key dimensions: type safety, build speed, config complexity, module system, and CI/CD friendliness. Used above or alongside the comparison table in the article.

**Generation prompt:**
Dark tech infographic illustration. Three vertical columns, each headed by a small approach badge: a JS icon (amber), a Webpack cube (blue), an esbuild bolt (green). Below each header, five horizontal attribute rows run across all three columns: "Type Safety", "Build Speed", "Config", "Modules", "CI/CD". Each cell contains a visual indicator — a filled circle (full), half-circle (partial), or empty circle (none) — in the column's accent color. For example: JS column has empty/grey circles for Type Safety and Modules, a green full circle for Config (none/simple), amber for CI/CD. Webpack has full blue circles for Type Safety, Modules, Source Maps, but a slow clock for Build Speed. esbuild has full green circles across most cells with a half-circle on Type Checking. The layout resembles a feature matrix card. Color palette: near-black background, amber for JS, blue for Webpack, green for esbuild. Flat vector infographic style, no readable text — only icons and visual indicators.

---

## 8. Multi-Developer Projects: Forms, Ribbons, and Shared Libraries

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-multi-developer-npm-workspaces-architecture.png`

**Alt text:** npm workspace monorepo architecture for multi-developer Model-Driven App web resource projects with shared TypeScript package

**Description:** Illustrates the npm workspace monorepo structure: a shared `@aidevme/shared` internal package at the centre, with form packages and ribbon packages as consumers, and separate output bundles for each. Used at the top of the multi-developer section to establish the architectural pattern before the code walkthrough.

**Generation prompt:**
Dark tech illustration. A hub-and-spoke architecture diagram. At the centre, a glowing teal package icon labelled `@aidevme/shared` — representing the shared internal library. Four spokes radiate outward: top-left leads to a `contact-form` package icon (form outline icon, blue); top-right leads to `account-form` (form icon, softer blue); bottom-left leads to `contact-ribbon` (ribbon/toolbar icon, purple); bottom-right leads to `account-ribbon` (ribbon icon, softer purple). Each spoke has a directional arrow flowing from shared to consumer. To the far right of each consumer, a small amber `dist/*.js` output file icon appears — showing the final built artifact. Above the diagram, a faint workspace root `package.json` label with a tree-root icon sits as the overarching container. Color palette: near-black background, teal for shared, blue for form packages, purple for ribbon packages, amber for output files. Flat vector hub-and-spoke diagram.

---

## 9. When to Choose What

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-when-to-choose-what-decision-guide.png`

**Alt text:** Decision guide for choosing plain JavaScript, TypeScript + Webpack, or TypeScript + esbuild for Power Platform web resources

**Description:** A visual decision tree or three-scenario card layout helping developers pick the right approach based on their context: project size, team size, toolchain preference. Used at the top of the "When to Choose What" section.

**Generation prompt:**
Dark tech illustration. Three tall decision-card panels arranged side by side with clear visual separation. Left card (amber): header icon is the JS badge; below it are three small scenario icons — a single developer silhouette, a clock (quick fix), a power-restriction symbol — suggesting "small, fast, solo". Centre card (blue): header is the Webpack cube; below it are scenario icons — multiple overlapping developer silhouettes (large team), a complex config file icon, a dynamic import arrow — suggesting "complex, team, feature-rich". Right card (green): header is the esbuild bolt; below it are scenario icons — a rocket/fast icon, a GitHub Actions workflow icon, a PCF/Code-App connection badge — suggesting "modern, CI/CD-first, TypeScript-familiar". Each card has a subtle glow around its header matching its accent color. Color palette: near-black background, amber left, electric blue centre, vivid green right. Flat vector card layout.

---

## 10. Deployment: Manual Upload via the Maker Portal

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-deployment-manual-upload-maker-portal.png`

**Alt text:** Manual upload of a JavaScript web resource through the Power Apps maker portal

**Description:** Illustrates the manual upload workflow: a built `.js` bundle file is uploaded through the Power Apps maker portal Web Resource editor, saved, and published. Used at the top of Scenario 1 to visualise the simplest deployment path.

**Generation prompt:**
Dark tech illustration. A minimal three-step vertical flow. Step 1: a terminal window showing `npm run build` with a file output arrow producing `dist/aidevme_contact_form.js` — glowing amber. Step 2: a simplified browser window frame showing the make.powerapps.com Web Resource editor — a "Choose file" button highlighted in teal, a file upload progress indicator, and a "Save" button. Step 3: a publish/rocket icon with a glowing green checkmark indicating successful publication. Connecting arrows flow downward between steps with a subtle "manual" stamp/badge on the arrow between steps 1 and 2 — emphasising the human click required. Color palette: near-black background, amber for the JS file, teal for the portal UI, green for the published state. Flat vector flow diagram.

---

## 11. Deployment: Power Platform CLI

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-deployment-pac-cli-local-workflow.png`

**Alt text:** Power Platform CLI pac webresource upload command for local developer web resource deployment workflow

**Description:** Illustrates the `pac` CLI inner-loop workflow: build → `pac webresource upload` → `pac solution publish`. Shows authentication profiles and the speed of the local developer loop. Used at the top of Scenario 2.

**Generation prompt:**
Dark tech illustration. A looping inner-dev-loop diagram arranged in a circular or arc shape. Starting at the top: a code-editor icon (VS Code style) with a TypeScript file open. Moving clockwise: a terminal showing `npm run build` producing a `.js` file. Next arc segment: a `pac webresource upload` terminal command glowing teal, with a small Dataverse diamond icon at the end of the upload arrow. Final arc segment: `pac solution publish` with a green checkmark and a Model-Driven App form wireframe illuminating. A small profile/auth badge (shield icon labelled "aidevme-dev") sits at the centre of the loop. The loop conveys speed with a subtle motion blur on the arrows. Color palette: near-black background, teal for pac commands, amber for the JS file, green for the publish step. Flat vector circular flow diagram.

---

## 12. Deployment: GitHub Actions CI/CD

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-deployment-github-actions-cicd.png`

**Alt text:** GitHub Actions CI/CD pipeline for automated TypeScript web resource deployment to Dataverse — typecheck, build, pac upload, publish

**Description:** Illustrates a GitHub Actions workflow: push to `main` triggers a pipeline that runs typecheck, build, `pac webresource upload`, and `pac solution publish`. Shows the automated, zero-touch deployment loop. Used at the top of Scenario 3.

**Generation prompt:**
Dark tech illustration. A horizontal pipeline diagram inside a faint GitHub Actions workflow container border (rounded rectangle, dark charcoal). Left trigger: a GitHub push/commit icon with a branch icon labelled "main" — glowing white. Pipeline stages flow left to right as connected boxes: (1) a typecheck `tsc` icon (TypeScript blue, shield/check badge); (2) a build `npm run build` box (amber, gear icon); (3) a `pac auth create` box (teal, padlock icon — the service principal secrets shown as three redacted dots); (4) a `pac webresource upload` box (teal, upload-arrow icon); (5) a `pac solution publish` box (green, checkmark icon). Above the pipeline, a GitHub Actions octocat silhouette is faintly visible. Color palette: near-black background, GitHub dark grey for the container, TypeScript blue, amber, teal, and green for the stages. Flat vector pipeline diagram.

---

## 13. Deployment: Azure DevOps Pipelines

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-deployment-azure-devops-pipelines.png`

**Alt text:** Azure DevOps multi-stage CI/CD pipeline for Power Platform web resource deployment with approval gates

**Description:** Illustrates an Azure DevOps multi-stage pipeline: a CI build stage producing an artifact, a Deploy Test stage with an optional approval gate, and a Deploy Production stage with a required manual approval gate. Used at the top of Scenario 4.

**Generation prompt:**
Dark tech illustration. A vertical multi-stage pipeline diagram with three distinct stages rendered as stacked horizontal slabs. Top slab (CI Build — blue): shows a Node.js icon, a typecheck badge, a build badge, and an artifact upload icon — all connected in a mini horizontal row. A small Azure DevOps logo badge sits in the top-left corner. Middle slab (Deploy Test — amber): shows a `pac` CLI icon, an upload arrow to a "Test" environment Dataverse icon (diamond, amber glow), and an optional approval badge (a soft dotted border around an "Approve" button — optional, not required). Bottom slab (Deploy Production — red/orange): identical to the Test slab but the approval badge is solid and bright — a padlock/required-reviewer icon glowing red. Connecting arrows between slabs flow downward. A "dependsOn" chain indicator connects the slabs on the right edge. Color palette: near-black background, blue for CI, amber for test, orange-red for production. Flat vector stage-diagram style.

---

## 14. Deployment: Managed vs Unmanaged Solutions

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-deployment-managed-vs-unmanaged-solutions.png`

**Alt text:** Power Platform managed vs unmanaged solution comparison — development with unmanaged, test and production with managed

**Description:** Illustrates the key distinction between unmanaged solutions (development environments, editable) and managed solutions (test/production, immutable, version-tracked). Shows the export → unpack → commit → pack → import ALM loop. Used at the top of Scenario 5.

**Generation prompt:**
Dark tech illustration. A horizontal environment progression diagram: three environment boxes labelled Dev, Test, and Production from left to right. The Dev box glows amber with an "unlocked padlock" icon and an editable-pencil badge — representing the unmanaged solution. The Test and Production boxes glow teal/purple with a "locked padlock" icon and a version-tag badge (v1.0.5) — representing managed solutions. Above the Dev box, a Git branch icon shows the export → unpack → commit cycle. A curved arrow between Dev and Test shows the CI pipeline packing and importing the managed solution. A second curved arrow between Test and Production shows the promotion flow with a required-approval badge at the midpoint. Color palette: near-black background, amber for Dev/unmanaged, teal for Test, purple for Production. Flat vector environment-flow diagram.

---

## 15. Deployment Scenario Decision Guide

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-deployment-scenario-decision-guide.png`

**Alt text:** Deployment scenario decision guide for Power Platform web resources — from manual portal upload to enterprise Azure DevOps pipelines

**Description:** A visual decision matrix or ladder diagram mapping team size and project maturity to the appropriate deployment scenario: manual upload, pac CLI, GitHub Actions, GitHub Environments with approvals, Azure DevOps pipelines, and managed solution ALM. Used at the top of the Deployment Scenario Decision Guide section, directly above the comparison table.

**Generation prompt:**
Dark tech infographic illustration. A vertical ladder or escalator diagram with six rungs, each representing a deployment scenario in increasing order of complexity. Bottom rung (grey, solo icon): "Manual upload — maker portal" with a browser/upload icon. Second rung (amber, single-person icon): "pac CLI local script" with a terminal icon and a pac command label. Third rung (green, two-person icon): "GitHub Actions per-package" with the GitHub Actions octocat badge and a PR merge arrow. Fourth rung (teal, small-team icon): "GitHub Actions + Environments + approvals" — same but with a padlock/approval badge added. Fifth rung (blue, mid-team icon): "Azure DevOps multi-stage pipeline" with an Azure DevOps spiral logo badge. Top rung (purple, enterprise building icon): "Managed solution ALM + version audit trail" with a shield/version-tag badge glowing bright. A vertical arrow on the left edge points upward labelled "Team size / complexity". Each rung glows progressively brighter from bottom to top. Color palette: near-black background, grey → amber → green → teal → blue → purple rung gradient. Flat vector ladder/escalator diagram.

---

## 16. Conclusion

**File name:** `javascript-vs-typescript-web-resources-model-driven-apps-conclusion-decision-summary.png`

**Alt text:** Summary decision paths for JavaScript vs TypeScript web resources in Model-Driven Apps — choose based on team size, project complexity, and CI/CD maturity

**Description:** A closing summary visual showing three converging paths — plain JS, TypeScript + Webpack, TypeScript + esbuild — all arriving at a well-deployed, production-ready Model-Driven App. Reinforces the article's core message that the right choice depends on context. Used at the top of the Conclusion section.

**Generation prompt:**
Dark tech illustration. Three paths (styled as glowing lanes or roads) converge from the left into a single destination on the right. Left lane (amber, narrow): a solo developer silhouette with a single `.js` icon — labelled by an amber glow. Centre lane (blue, wider): a team of two developer silhouettes, a Webpack cube, and a complex project icon. Right lane (green, medium): a team silhouette, an esbuild bolt, and a GitHub Actions workflow icon. All three lanes merge at a central convergence point — a bright glowing Power Platform diamond — representing a successful, production-deployed Model-Driven App web resource. A small "pac solution publish" label and version tag float above the convergence point. Color palette: near-black background, amber, blue, green lanes converging into a teal/purple Power Platform destination. Flat vector converging-lanes illustration.
