# Image Generation Prompts — Article 79
# Storybook MCP Server: The Complete Developer Guide to AI-Assisted UI Component Development

---

## 1. Featured Image

**File name:** `storybook-mcp-server-ai-component-library-featured.png`

**Alt text:** Storybook MCP Server — connecting an AI agent directly to a component library so it can query docs, generate stories, run accessibility tests, and self-heal

**Description:** Featured image for the article. Should convey the idea of an AI agent gaining direct access to a living component library — not guessing, but querying. Displayed at 1200×628 (social/OG) and as the WordPress featured image.

**Generation prompt:**
Dark-background tech illustration. A desktop UI frame on the left shows a stylised Storybook UI panel — a component explorer tree with items like Button, TextInput, Avatar, Header glowing softly in the sidebar. On the right, an AI agent chat interface shows a conversation in progress with tool call badges visible: `get-documentation`, `run-story-tests`, `preview-stories`. Between the two sides, a thick glowing bridge line labeled "MCP" in electric blue pulses with data flow indicators moving left to right. Below the bridge: three compact pill badges in teal, amber, and coral labeled "Docs", "Development", "Testing". Background: near-black (#0d1117). Color palette: electric blue (#00b4d8) for MCP bridge, teal (#4cc9f0) for docs, amber (#f4a430) for development, coral (#e05b5b) for testing. Flat vector with soft glow halos. No additional readable text beyond the tool names and labels.

---

## 2. What Is the Storybook MCP Server?

**File name:** `storybook-mcp-server-what-it-is-architecture.png`

**Alt text:** Storybook MCP Server architecture — exposing a component library to AI agents via the Model Context Protocol as queryable tools

**Description:** Illustrates the core concept: Storybook running as an MCP server, exposing component knowledge to any compliant AI agent. Used at the start of the "What Is" section.

**Generation prompt:**
Dark tech illustration. A hub-and-spoke diagram. Center: a large Storybook logo badge (stylised book icon) in amber, labeled "Storybook MCP Server" with a sub-label "localhost:6006/mcp". Radiating outward via thin connection lines: four agent badges arranged around it — Claude (purple), GitHub Copilot (blue with Octocat), Gemini (teal), OpenAI Codex (green). Each connection line is labeled "MCP" in small electric blue text. Below the center badge, three small downward-connected pills: "Docs tools", "Dev tools", "Testing tools". A small "React only (preview)" warning badge in amber sits in the bottom-right corner. Background: near-black. Flat vector hub-and-spoke layout. Clean, minimal.

---

## 3. The Two Approaches: Official Addon vs Community Package

**File name:** `storybook-mcp-official-vs-community-comparison.png`

**Alt text:** @storybook/addon-mcp vs storybook-mcp by mcpland — a comparison of the two approaches to connecting Storybook to AI agents via MCP

**Description:** Side-by-side comparison of the official addon and the community package across key dimensions. Used in the "Two Approaches" section.

**Generation prompt:**
Dark tech illustration. A clean two-column comparison layout. Left column header: "@storybook/addon-mcp" with the Storybook book icon in amber and a "Core Team" badge. Right column header: "storybook-mcp (mcpland)" with a community/person icon in teal and a "Community" badge. Eight comparison rows with a label on the far left and values in each column: "Maintainer", "How it runs", "Data source", "Framework support", "Custom tools", "Testing integration", "Story previews", "Requires Storybook". Checkmarks in coral-orange highlight the rows where the official addon has an advantage; teal checkmarks highlight rows where storybook-mcp has an advantage. Left column bordered in amber, right column bordered in teal. Background: near-black. Flat vector comparison table layout, alternating row shading.

---

## 4. The Official @storybook/addon-mcp: Architecture

**File name:** `storybook-addon-mcp-architecture-three-toolsets.png`

**Alt text:** @storybook/addon-mcp architecture — three toolsets (docs, development, testing) running inside the Storybook dev server

**Description:** Illustrates the addon's internal architecture: the five packages in the monorepo and how the three toolsets relate to the dev server. Used at the start of the architecture section.

**Generation prompt:**
Dark tech illustration. A layered architecture diagram. Top layer (amber, labeled "Storybook Dev Server"): a server icon with the Storybook badge. Inside it, three side-by-side boxes in distinct colors: teal box labeled "Docs Toolset" with icons for list, document, story; amber box labeled "Development Toolset" with icons for code editor, preview frame; coral box labeled "Testing Toolset" with icons for checkmark, accessibility symbol. Below the server, a thick downward arrow to a pale blue "MCP Endpoint" badge labeled "localhost:6006/mcp". Below that, a single agent icon labeled "AI Agent". On the right side of the diagram, a vertical list of five small package pills labeled "@storybook/mcp", "@storybook/addon-mcp", "@storybook/mcp-proxy", "@storybook/claude-code-plugin", "@storybook/codex-plugin" in soft grey. Background: near-black. Flat vector layered diagram.

---

## 5. How the Docs Toolset Works

**File name:** `storybook-mcp-docs-toolset-list-get-documentation.png`

**Alt text:** Storybook MCP docs toolset — list-all-documentation, get-documentation, and get-documentation-for-story give AI agents read access to component props and stories

**Description:** Illustrates how the three docs toolset tools work together to give an agent grounding in the component library before it writes any code. Used in the "Docs Toolset" subsection.

**Generation prompt:**
Dark tech illustration. A three-step sequential flow diagram. Step 1 (teal, magnifying glass icon): "list-all-documentation — agent discovers what components exist." A compact component index list is shown: Button, TextInput, Avatar, Header, Badge. Step 2 (electric blue, document icon): "get-documentation — agent reads props, stories, MDX docs for a target component." A condensed prop table is shown with columns Name, Type, Default. Step 3 (amber, story icon): "get-documentation-for-story — agent reads full story source for a specific variant." A small code snippet frame shows a Story definition. Thick right-pointing arrows connect all three steps. Background: near-black. Flat vector sequential flow layout.

---

## 6. How the Development Toolset Works

**File name:** `storybook-mcp-development-toolset-preview-stories.png`

**Alt text:** Storybook MCP development toolset — get-storybook-story-instructions and preview-stories let AI agents write consistent stories and see rendered previews in the chat

**Description:** Illustrates the two development toolset tools, with emphasis on the preview-stories inline rendering capability. Used in the "Development Toolset" subsection.

**Generation prompt:**
Dark tech illustration. A split two-panel layout. Left panel (amber, labeled "get-storybook-story-instructions"): a document/rulebook icon with a short list of conventions — "Use play functions for interactions", "Capture all variants", "Follow existing story patterns." An arrow from the agent icon reads "Ask before writing." Right panel (electric blue, labeled "preview-stories"): an AI chat bubble frame containing an embedded component preview box — a rendered Button component in three variants (primary, secondary, disabled) displayed inline inside the conversation. A small "MCP Apps" badge sits in the corner. Below the two panels, a caption: "Agents write consistent stories and see what they built." Background: near-black. Flat vector split layout.

---

## 7. How the Testing Toolset Works

**File name:** `storybook-mcp-testing-toolset-run-story-tests-accessibility.png`

**Alt text:** Storybook MCP testing toolset — run-story-tests lets AI agents execute interaction and accessibility tests and interpret failures to fix their own code

**Description:** Illustrates how the testing toolset connects to Storybook Test and returns structured results the agent can act on. Used in the "Testing Toolset" subsection.

**Generation prompt:**
Dark tech illustration. A test result flow diagram. An agent icon on the left sends a call: "run-story-tests → LoginForm stories." A test runner icon in the center processes the request. On the right, two result outputs split vertically: top half shows a green ✓ list (interaction tests passing), bottom half shows a red ✗ item labeled "Accessibility: contrast ratio 3.2 — minimum 4.5." Below the result box, a feedback arrow back to the agent icon labeled "Agent interprets failure and fixes." Below that, a re-run arrow and a second all-green result box. A small "@storybook/addon-a11y required" note in amber sits at the bottom. Background: near-black. Flat vector test flow diagram.

---

## 8. The Self-Healing Loop

**File name:** `storybook-mcp-self-healing-loop-generate-test-fix.png`

**Alt text:** Storybook MCP self-healing loop — AI agent generates UI, tests it, finds accessibility failures, fixes them using design system tokens, and re-tests automatically

**Description:** Illustrates the full self-healing cycle that results from combining all three toolsets. The centrepiece visual of the article. Used in the "Self-Healing Loop" subsection.

**Generation prompt:**
Dark tech illustration. A circular five-step loop diagram with a glowing continuous arrow forming the cycle. Step 1 (teal, code icon): "Generate component using documented props." Step 2 (amber, story icon): "Write stories with correct conventions." Step 3 (coral, test icon): "Run interaction + accessibility tests." Step 4 (red/warning, bug icon): "Tests fail — contrast issue found." Step 5 (green, fix icon): "Query theme tokens → fix value → re-run tests → pass." The loop arrow glows coral at the failure step and transitions to green at the fix step, then back to teal for the next cycle. In the center of the loop: a small "No manual intervention required" label in soft white. Background: near-black. Color palette: teal for generation, amber for authoring, coral for testing, red for failure, green for resolution. Flat vector circular loop.

---

## 9. Installing @storybook/addon-mcp: Step-by-Step

**File name:** `storybook-addon-mcp-installation-steps.png`

**Alt text:** Installing @storybook/addon-mcp — four steps: install the addon, connect your agent with mcp-add, configure AGENTS.md instructions, and test the connection

**Description:** A step-by-step visual guide to the installation process. Used at the start of the installation section.

**Generation prompt:**
Dark tech illustration. A vertical four-step numbered installation flow. Step 1 (electric blue, terminal icon): "npx storybook add @storybook/addon-mcp — MCP endpoint available at localhost:6006/mcp." Step 2 (teal, plug/connect icon): "npx mcp-add — register MCP server with your agent of choice." Step 3 (amber, document/rulebook icon): "Configure AGENTS.md — instructions for when and how to use MCP tools." Step 4 (green, checkmark icon): "Test: ask agent to list all documented components — verify connection." Each step is a rounded card connected by a downward arrow. Steps 1–2 have a terminal frame showing the command. Steps 3–4 have a document/chat frame. Background: near-black. Flat vector vertical installation flow.

---

## 10. Configuring VS Code Copilot with Storybook MCP

**File name:** `storybook-mcp-vscode-copilot-mcp-json-configuration.png`

**Alt text:** Configuring Storybook MCP with VS Code Copilot — add the HTTP server to .vscode/mcp.json and verify in the Copilot chat panel

**Description:** Illustrates the VS Code Copilot-specific configuration path using `.vscode/mcp.json`. Used in the "Configuring VS Code Copilot" section.

**Generation prompt:**
Dark tech illustration. A VS Code editor frame occupies most of the image. The file tree on the left shows `.vscode/mcp.json` highlighted. The editor pane shows a JSON configuration block with the server name "my-app-storybook", type "http", and URL "http://localhost:6006/mcp" — syntax-highlighted in the VS Code dark theme palette. On the right side, a narrow Copilot chat panel shows an MCP server status indicator — a green dot next to "my-app-storybook" labeled "Connected." A small annotation arrow from the JSON block points to the status dot. Below the editor, a caption: "Place in .vscode/ for project-scoped configuration." Background: near-black matching VS Code. Flat vector editor mockup.

---

## 11. Real-World Workflows: What This Looks Like in Practice

**File name:** `storybook-mcp-real-world-workflows-four-examples.png`

**Alt text:** Storybook MCP real-world workflows — building a login form, previewing dark mode, running targeted tests, and generating interaction tests

**Description:** A four-quadrant overview of the practical workflows covered in this section. Used as a section header image before the individual workflow breakdowns.

**Generation prompt:**
Dark tech illustration. A four-quadrant card layout, each quadrant a distinct workflow. Top-left (teal, form icon): "Build Login Form — agent queries TextInput and Button props, composes correctly, writes stories, passes a11y tests." Top-right (electric blue, moon/theme icon): "Dark Mode Preview — agent calls preview-stories with dark global, renders inline in chat." Bottom-left (coral, test results icon): "Run Targeted Tests — agent finds all stories for Header component, runs tests, returns summary." Bottom-right (amber, play-function icon): "Generate Interaction Tests — agent writes play() function that simulates user input and asserts outcome." Each quadrant has a thin border in its accent color and a small tool badge showing which MCP tool is called. Background: near-black. Flat vector four-quadrant layout.

---

## 12. Storybook Composition: Multi-Design-System Support

**File name:** `storybook-mcp-composition-multi-design-system.png`

**Alt text:** Storybook composition and MCP — the MCP server aggregates manifests from all composed Storybooks, giving agents access to the full component landscape

**Description:** Illustrates how Storybook composition extends MCP coverage to multiple design systems automatically. Used in the "Storybook Composition" section.

**Generation prompt:**
Dark tech illustration. A tree diagram. Top node (amber): "Host Application Storybook" with MCP server icon. Two branches downward: left branch to a teal node labeled "Shared Design System Storybook" with a component grid icon; right branch to an electric blue node labeled "Third-Party Component Library Storybook" with an external link icon. Both child nodes connect back up to the host node with dashed lines labeled "Composed". Below the host node, a downward arrow to an AI agent icon labeled "Agent sees all components from all composed Storybooks." Background: near-black. Flat vector tree diagram.

---

## 13. The Community Alternative: storybook-mcp by mcpland

**File name:** `storybook-mcp-community-mcpland-playwright-architecture.png`

**Alt text:** storybook-mcp by mcpland — a standalone MCP server using Playwright to extract prop information from any Storybook instance, including deployed and non-React ones

**Description:** Illustrates the community package's Playwright-based architecture and how it differs from the official addon. Used at the start of the community alternative section.

**Generation prompt:**
Dark tech illustration. A horizontal three-stage pipeline diagram. Stage 1 (teal, globe icon): "Any Storybook URL — local or deployed, any framework." Stage 2 (amber, Playwright browser icon — a stylised headless browser window): "Headless Chromium via Playwright — loads docs iframe, extracts props table HTML." Stage 3 (electric blue, tool/wrench icon): "MCP Tools returned to agent — getComponentList, getComponentsProps, custom tools." Thick right-pointing arrows connect the three stages. Below the pipeline, a "Community · MIT · Works with Vue / Angular / Web Components" badge in soft grey. A "vs Official Addon" annotation on the left side shows a small comparison note: "No dev server changes required — works on any deployed instance." Background: near-black. Flat vector pipeline diagram.

---

## 14. Custom Tools: Extending Beyond Props

**File name:** `storybook-mcp-custom-tools-icon-tokens-javascript-extraction.png`

**Alt text:** storybook-mcp custom tools — extending the MCP server with JavaScript extraction to expose icon libraries, color palettes, and design tokens to AI agents

**Description:** Illustrates the custom tools capability of storybook-mcp and what kinds of design system information it can expose beyond standard prop tables. Used in the "Custom Tools" subsection.

**Generation prompt:**
Dark tech illustration. A three-column card layout showing custom tool examples. Left card (coral, icon grid): "getIconList — Playwright navigates to /docs/icon--docs, executes JS, returns array of icon names." A small grid of icon placeholder squares fills the card. Center card (amber, color swatch grid): "getColorPalette — extracts color swatch names and hex values from design tokens page." A small grid of color swatch circles fills the card. Right card (electric blue, spacing ruler): "getSpacingScale — extracts spacing token values from design tokens docs." A small ruler with labeled increments fills the card. Below all three cards: a JSON code frame snippet showing the CUSTOM_TOOLS environment variable structure. Background: near-black. Flat vector card layout.

---

## 15. Current Limitations and Roadmap

**File name:** `storybook-mcp-limitations-roadmap-react-only-preview.png`

**Alt text:** Storybook MCP current limitations — React-only docs toolset, preview status, MCP Apps client support, and community package stability caveats

**Description:** Illustrates the key limitations and what is on the roadmap. Used in the "Current Limitations and Roadmap" section.

**Generation prompt:**
Dark tech illustration. A two-section layout. Top section (amber header, labeled "Current Limitations"): four warning cards in a 2×2 grid. Card 1 (amber): "React only — Vue, Angular, Svelte, Web Components pending." Card 2 (amber): "Preview status — API may change between releases." Card 3 (amber): "MCP Apps client support — not all clients support inline previews yet." Card 4 (amber): "Community package — Playwright adds install overhead, v0.5.1." Bottom section (teal header, labeled "Roadmap"): a horizontal timeline with three nodes — "React (now)" glowing, "Vue / Angular" greyed out, "Web Components / Svelte" greyed out with a question mark. Background: near-black. Flat vector two-section layout.

---
