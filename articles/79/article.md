# Storybook MCP Server: The Complete Developer Guide to AI-Assisted UI Component Development

**WordPress SEO**
- **Focus keyphrase:** Storybook MCP Server
- **SEO title:** Storybook MCP Server: Complete Guide to AI-Assisted UI Development
- **Meta description:** Storybook's official MCP server connects AI agents directly to your component library — letting them query docs, generate stories, run accessibility tests, and self-heal. Here's everything developers need to know.
- **Slug:** storybook-mcp-server-complete-guide-ai-ui-development
- **Excerpt:** Storybook's official MCP server (@storybook/addon-mcp) turns your component library into a live knowledge source for AI agents. Agents can query component documentation, generate stories, run interaction and accessibility tests, and self-correct — all without you having to intervene. This guide covers the architecture, the three toolsets, installation step-by-step, and two alternative MCP approaches including the community-built storybook-mcp package.
- **Categories:** AI & Copilot, Model Context Protocol, Frontend Development
- **Tags:** Storybook, MCP Server, Model Context Protocol, AI Agents, UI Development, Component Library, Design System, GitHub Copilot, React, Frontend Development, Agentic AI, Accessibility Testing

---

I've been thinking about this for a while.

We spend months building design systems. We document every component in Storybook. We write stories, prop tables, usage guidelines, accessibility notes. We do the hard work of making the codebase self-explanatory — so that anyone joining the team can understand the `Button` is not just a `<button>`, it's a composed component with variants, sizes, and disabled states that all need testing.

Then we add an AI coding agent to the workflow. And the agent ignores all of it.

It generates a new button. Inline styles. A hardcoded hex value that doesn't match the palette. A different component name. It doesn't know your `TextInput` has a `type="password"` prop. It doesn't know your theme tokens exist. It doesn't know about anything you documented — because Storybook is running in a browser tab and your agent is running in a completely separate context.

I've watched this happen on multiple teams. The AI generates code fast, but it generates code that adds to the design debt rather than reducing it. You end up with a codebase that has two parallel component systems: the one your team built deliberately, and the one the AI invented.

The Storybook MCP server is the fix. It connects your running Storybook instance directly to any MCP-compatible AI agent — Claude, Gemini, GitHub Copilot, OpenAI Codex, and others — so the agent can query your component documentation, check prop definitions before using them, generate stories, run accessibility tests, and fix what it breaks. All without leaving the conversation.

It's not a workaround. It's the right architectural answer: give the agent the same knowledge source a new human developer would use.

This guide covers everything: what the Storybook MCP server is, how the three toolsets work, how to install it, how to configure your agent, and where the two main approaches (the official addon and the community `storybook-mcp` package) differ.

---

## Table of Contents

- [What Is the Storybook MCP Server?](#what-is-the-storybook-mcp-server)
- [The Two Approaches: Official Addon vs Community Package](#the-two-approaches-official-addon-vs-community-package)
- [The Official @storybook/addon-mcp: Architecture](#the-official-storybookaddon-mcp-architecture)
  - [How the Docs Toolset Works](#how-the-docs-toolset-works)
  - [How the Development Toolset Works](#how-the-development-toolset-works)
  - [How the Testing Toolset Works](#how-the-testing-toolset-works)
  - [The Self-Healing Loop](#the-self-healing-loop)
- [Installing @storybook/addon-mcp: Step-by-Step](#installing-storybookaddon-mcp-step-by-step)
  - [Step 1: Install the Addon](#step-1-install-the-addon)
  - [Step 2: Connect Your Agent](#step-2-connect-your-agent)
  - [Step 3: Configure Agent Instructions](#step-3-configure-agent-instructions)
  - [Step 4: Test the Connection](#step-4-test-the-connection)
- [Configuring VS Code Copilot with Storybook MCP](#configuring-vs-code-copilot-with-storybook-mcp)
- [Real-World Workflows: What This Looks Like in Practice](#real-world-workflows-what-this-looks-like-in-practice)
  - [Workflow 1: Building a Login Form](#workflow-1-building-a-login-form)
  - [Workflow 2: Previewing a Component in Dark Mode](#workflow-2-previewing-a-component-in-dark-mode)
  - [Workflow 3: Running Tests Against Specific Stories](#workflow-3-running-tests-against-specific-stories)
  - [Workflow 4: Generating Interaction Tests](#workflow-4-generating-interaction-tests)
- [Storybook Composition: Multi-Design-System Support](#storybook-composition-multi-design-system-support)
- [The Community Alternative: storybook-mcp by mcpland](#the-community-alternative-storybook-mcp-by-mcpland)
  - [Built-In Tools](#built-in-tools)
  - [Custom Tools: Extending Beyond Props](#custom-tools-extending-beyond-props)
  - [How It Works Under the Hood](#how-it-works-under-the-hood)
  - [When to Use storybook-mcp Instead](#when-to-use-storybook-mcp-instead)
- [Current Limitations and Roadmap](#current-limitations-and-roadmap)
- [Key Takeaways](#key-takeaways)
- [References](#references)

---

## What Is the Storybook MCP Server?

The Storybook MCP Server is a [Model Context Protocol](https://modelcontextprotocol.io/) server that exposes your Storybook component library to AI agents as a set of queryable tools. Instead of the agent guessing what components you have, it can ask. Instead of hallucinating prop names, it can look them up. Instead of writing tests manually after generating code, it can run them and respond to what fails.

MCP — the Model Context Protocol — is an open standard originally developed by Anthropic and now widely adopted across the AI tool ecosystem. It defines a structured way for AI agents to discover and call external tools, making Storybook's capabilities available to any compliant agent without vendor-specific integrations.

The official implementation is `@storybook/addon-mcp`, published and maintained by the Storybook core team. When you run Storybook's dev server with this addon installed, the MCP server becomes available at `http://localhost:6006/mcp` (port may vary). Any agent you point at that URL gains access to three toolsets: **docs**, **development**, and **testing**.

There is also a community-built alternative — `storybook-mcp` by mcpland — which takes a different architectural approach using headless browser automation. Both are covered in detail below.

> **Current Status:** Storybook's AI capabilities, including the MCP server, are in **preview** and currently support **React projects only**. The Storybook team plans to expand to Vue, Angular, Web Components, and Svelte after stabilising the React experience. The API may change between releases.

---

## The Two Approaches: Official Addon vs Community Package

Before going deeper, it is worth understanding the landscape. There are two meaningfully different approaches to connecting Storybook to an AI agent via MCP:

| | **@storybook/addon-mcp** | **storybook-mcp (mcpland)** |
|---|---|---|
| **Maintainer** | Storybook core team | Community (mcpland) |
| **How it runs** | Embedded in Storybook dev server | Standalone via `npx` |
| **Data source** | Storybook manifests (compiled) | `index.json` + Playwright automation |
| **Framework support** | React only (preview) | Any Storybook instance |
| **Custom tools** | No | Yes (JavaScript extraction) |
| **Testing integration** | Full (Storybook Test) | None |
| **Story previews in agent** | Yes (MCP Apps-capable clients) | No |
| **Requires Storybook running** | Yes | Yes (URL-based) |

The right choice depends on your situation. If you are on React, using an active dev server, and want agent-driven story generation and testing, the official addon is the correct path. If you need to connect to any deployed Storybook — including non-React ones or published design system docs — the community package is the more flexible option.

---

## The Official @storybook/addon-mcp: Architecture

The addon is part of a larger monorepo (`storybookjs/addon-mcp`) that ships five packages:

- **`@storybook/mcp`** — Standalone MCP library for serving Storybook component knowledge, usable independently
- **`@storybook/addon-mcp`** — The Storybook addon, which runs an MCP server within your dev server and includes everything from `@storybook/mcp`
- **`@storybook/mcp-proxy`** — A stable proxy package for agent integrations
- **`@storybook/claude-code-plugin`** — Claude Code plugin that configures Storybook MCP automatically
- **`@storybook/codex-plugin`** — OpenAI Codex plugin equivalent

The addon exposes three toolsets to the agent, each solving a distinct part of the UI development workflow.

### How the Docs Toolset Works

The docs toolset is the foundation. It gives the agent read access to your component library — what components exist, what props they accept, and what stories demonstrate their usage.

It relies on **Storybook manifests** — structured data that Storybook compiles from your component stories and TypeScript definitions. The manifest captures your prop types, default values, required flags, and story examples in a form the agent can consume without rendering anything.

The toolset provides three tools:

**`list-all-documentation`**
Returns an index of all components and unattached docs entries in your Storybook. This is the starting point — the agent calls this first to understand what is available before deciding which components to use.

**`get-documentation`**
Returns detailed documentation for a specific component: its props, the first three stories, an index of remaining stories, and any additional MDX documentation you have written. This is what prevents the agent from guessing at your API surface.

**`get-documentation-for-story`**
Returns the full story source and associated documentation for a specific story. The agent calls this when `get-documentation` alone is not enough to understand a component's usage — for example, when a story demonstrates a complex interaction pattern or a prop combination that is not obvious from the type definition alone.

> The docs toolset is **React-only** in the current preview because it depends on the manifest format, which is currently limited to React projects.

### How the Development Toolset Works

The development toolset handles authoring. Once the agent has used the docs toolset to understand what components are available, the development toolset helps it write stories and preview rendered output.

**`get-storybook-story-instructions`**
Returns Storybook's current conventions for writing stories — which props to capture, how to write interaction tests using play functions, and what patterns the project expects. This keeps the agent's generated stories consistent with your existing codebase rather than inventing a different style for each generation.

**`preview-stories`**
This is the most visually interesting capability. If your agent client supports [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview), this tool returns rendered story previews directly in the chat interface. You can see the component output without leaving the conversation. If the client does not support MCP Apps, it returns links to the stories in Storybook instead.

### How the Testing Toolset Works

The testing toolset requires [Storybook Test](https://storybook.js.org/docs/writing-tests) to be configured in your project. When it is, the agent gains the ability to run your tests programmatically and interpret the results.

**`run-story-tests`**
Runs tests for specific stories and returns results, including any accessibility issues if you have `@storybook/addon-a11y` configured. The tool also instructs the agent on how to interpret results and resolve issues — it does not just return a pass/fail, it returns enough context for the agent to understand what went wrong and why.

### The Self-Healing Loop

The real power of combining all three toolsets is what the Storybook team calls the **self-healing loop**. Here is what it looks like in practice:

```
Agent generates UI component
    → Uses docs toolset to ensure correct prop usage
    → Uses development toolset to write stories
    → Uses testing toolset to run interaction and accessibility tests
    → Tests fail: accessibility contrast issue found
    → Agent uses docs toolset to query your theme tokens
    → Agent fixes the component with the correct theme value
    → Agent re-runs tests to confirm the fix
    → Tests pass
```

No manual intervention required. The agent catches its own mistakes, references your actual design system to fix them, and validates the fix before presenting the result to you.

I want to be honest about this: the self-healing loop works, but it is not magic. It works because the agent has grounding — real prop definitions, real theme values, real test output. Without that grounding, agents fix accessibility errors by guessing. With it, they fix them correctly. The loop is only as strong as the documentation you have already written in Storybook. If your stories are thin and your MDX docs are empty, the agent will still hallucinate — just less often. Investing in your Storybook documentation is now directly investing in the quality of your AI-generated UI.

---

## Installing @storybook/addon-mcp: Step-by-Step

### Step 1: Install the Addon

Run this command in your project root:

```bash
npx storybook add @storybook/addon-mcp
```

This installs the package and registers it in your Storybook configuration. When you next run your Storybook dev server, the MCP endpoint becomes available:

```
http://localhost:6006/mcp
```

You can verify it is working by opening that URL in a browser — you will see a page listing the available tools and a link to the manifest debugger.

### Step 2: Connect Your Agent

Use `mcp-add` to register the MCP server with your agent:

```bash
npx mcp-add --type http --url "http://localhost:6006/mcp" --scope project
```

`mcp-add` is an open-source CLI that handles the configuration differences between agents (VS Code Copilot, Claude Code, Gemini CLI, Codex, etc.) behind a single command. You will be prompted for a name — choose something descriptive and unique. For example: `my-app-sb-mcp`. This is the name you will reference in your agent instructions.

You can also configure agents manually using their native configuration files. See the sections below for the VS Code Copilot-specific approach.

### Step 3: Configure Agent Instructions

Add Storybook-specific instructions to your `AGENTS.md` (or `CLAUDE.md` for Claude Code). These instructions tell the agent when and how to use the MCP tools. Replace `your-project-sb-mcp` with the name you chose:

```markdown
When working on UI components, always use the `your-project-sb-mcp`
MCP tools to access Storybook's component and documentation knowledge
before answering or taking any action.

- **CRITICAL: Never hallucinate component properties!**
  Before using ANY property on a component from the design system
  (including common-sounding ones), you MUST use the MCP tools to
  check if the property is actually documented for that component.

- Query `list-all-documentation` to get a list of all components
- Query `get-documentation` for that component to see all available
  properties and examples
- Only use properties that are explicitly documented or shown in
  example stories
- If a property is not documented, do not assume it based on naming
  conventions. Check back with the user.
- Use `get-storybook-story-instructions` before creating or updating
  stories to ensure you follow current conventions
- Check your work by running `run-story-tests`

Remember: A story name might not reflect the property name correctly,
so always verify properties through documentation or example stories
before using them.
```

The last point matters more than it appears. Story names like "Primary Button" do not map to a `primary` prop. Without this instruction, agents frequently infer prop names from story display names and get it wrong.

### Step 4: Test the Connection

With Storybook running, try a prompt like:

```
List all documented components
```

You should see the agent call the `list-all-documentation` tool and return a list of components from your Storybook. If it does, the connection is working.

---

## Configuring VS Code Copilot with Storybook MCP

For VS Code Copilot users, you can configure the MCP server directly in your `.vscode/mcp.json` file instead of using `mcp-add`:

```json
{
  "servers": {
    "my-app-storybook": {
      "type": "http",
      "url": "http://localhost:6006/mcp"
    }
  }
}
```

Scope this to the project by placing it in `.vscode/` rather than user settings. Once the file is saved, open a Copilot chat session — the MCP server should appear as an available tool provider. You can verify it is active by checking the MCP server status in the chat panel.

If you are using the Insiders build of VS Code, you can also work with the `preview-stories` tool's rendered output directly in the chat interface, provided the `chat.mcp.apps.enabled` setting is turned on.

---

## Real-World Workflows: What This Looks Like in Practice

### Workflow 1: Building a Login Form

**Prompt:** Build a login form

1. The agent calls `list-all-documentation` to survey available components
2. It identifies `TextInput` and `Button` as candidates
3. It calls `get-documentation` on `TextInput`, discovering the `type="password"` prop for the password field
4. It calls `get-documentation` on `Button` to verify the correct variant prop for a primary submit action
5. It generates a `LoginForm` component that composes both
6. It calls `get-storybook-story-instructions` to confirm story conventions
7. It writes stories for the login form's empty, filled, loading, and error states
8. It runs `run-story-tests` and discovers a contrast issue on the submit button
9. It calls `get-documentation` on your theme tokens, finds the correct accessible colour, and updates the component
10. It re-runs tests — all pass

The output you receive is a component that uses your existing design system correctly, has working stories, and has passed accessibility checks.

### Workflow 2: Previewing a Component in Dark Mode

**Prompt:** Show me the Button in dark mode

The agent calls `preview-stories` with the default Button story and the dark mode global applied. If your client supports MCP Apps, the rendered preview appears directly in the chat. If not, it returns the direct Storybook URL with the correct globals query string set.

### Workflow 3: Running Tests Against Specific Stories

**Prompt:** Run tests for all the stories that contain the Header component

1. The agent uses file search to identify which components import `Header`
2. It locates all story files for those components
3. It calls `run-story-tests` on each set of stories in sequence
4. It returns a summary of results, calling out any failures with enough context to act on them

### Workflow 4: Generating Interaction Tests

**Prompt:** Write a story to test the login form submit action

The agent calls `get-storybook-story-instructions` first to understand the expected pattern for [play functions](https://storybook.js.org/docs/writing-stories/play-function) in this project. It then generates a story with a `play` function that simulates a user filling in the form fields using `userEvent`, clicks the submit button, and asserts the expected outcome — such as a success message appearing or a callback being called.

---

## Storybook Composition: Multi-Design-System Support

If your project uses [Storybook composition](https://storybook.js.org/docs/sharing/storybook-composition) to embed multiple Storybooks — for example, a host application that composes a shared design system Storybook — the MCP server handles this automatically.

When a composed Storybook has its own manifests, the MCP server includes that content in its responses without any additional configuration. The agent can discover and reference components from all composed Storybooks simultaneously through the same `list-all-documentation` and `get-documentation` calls.

This is particularly useful for organisations that maintain a centralised design system Storybook that individual product teams compose into their own instances. Agents working in any product team's repo gain access to the full component knowledge from the shared design system.

---

## The Community Alternative: storybook-mcp by mcpland

The `storybook-mcp` package (published on npm as `storybook-mcp`) is a community-built MCP server that takes a fundamentally different approach. Rather than running inside your Storybook dev server and reading compiled manifests, it runs as a standalone process, fetches your Storybook's `index.json` file over HTTP, and uses Playwright to extract prop information from rendered documentation pages.

This architecture means it works with **any Storybook instance** — not just React, not just locally running ones. You can point it at a deployed design system Storybook and connect an agent to it without any changes to the Storybook project itself.

Configure it in your MCP settings file:

```json
{
  "mcpServers": {
    "storybook": {
      "command": "npx",
      "args": ["-y", "storybook-mcp@latest"],
      "env": {
        "STORYBOOK_URL": "https://your-storybook-domain.com/index.json"
      }
    }
  }
}
```

The `STORYBOOK_URL` environment variable points to the `index.json` file (or `stories.json` for older Storybook v3 instances) that every Storybook automatically generates.

On first run, the package installs Chromium in the background using Playwright. If you want to pre-install it ahead of time to avoid the delay on the first tool call:

```bash
npx -y storybook-mcp@latest install-browser
```

### Built-In Tools

**`getComponentList`**
Fetches `index.json` from the configured Storybook URL and returns all components marked as `docs` type entries. This gives the agent a catalogue of what is available without launching a browser.

**`getComponentsProps`**
For a given array of component names, the server constructs the iframe documentation URL for each, loads it in a headless Chromium instance via Playwright, and extracts the props table HTML. It returns structured prop information including:

- Property names
- Types
- Default values
- Descriptions
- Required/optional status

Example call:

```json
{
  "tool": "getComponentsProps",
  "parameters": {
    "componentNames": ["Button", "TextInput", "Avatar"]
  }
}
```

### Custom Tools: Extending Beyond Props

The `storybook-mcp` package supports a `CUSTOM_TOOLS` environment variable that accepts a JSON array of tool definitions. Each custom tool can navigate to any URL in your Storybook and execute arbitrary JavaScript to extract information from the rendered page.

Custom tool structure:

```typescript
interface CustomTool {
  name: string;        // Unique tool name visible to the agent
  description: string; // Description the agent uses to decide when to call it
  parameters: object;  // Input parameters schema (optional)
  page: string;        // URL to navigate to
  handler: string;     // JavaScript code to execute on the page
}
```

Real-world example — extracting an icon list from a Storybook icon documentation page:

```json
[
  {
    "name": "getIconList",
    "description": "Get all available icons from the Icon page",
    "parameters": {},
    "page": "https://your-storybook.com/?path=/docs/icon--docs",
    "handler": "Array.from(document.querySelectorAll('.icon-name')).map(i => i.textContent)"
  },
  {
    "name": "getColorPalette",
    "description": "Extract color palette from design tokens",
    "parameters": {},
    "page": "https://your-storybook.com/?path=/docs/design-tokens--colors",
    "handler": "Array.from(document.querySelectorAll('.color-swatch')).map(el => ({ name: el.getAttribute('data-color-name'), value: el.style.backgroundColor }))"
  }
]
```

This makes the agent aware of resources that are not captured in standard prop tables — icon libraries, colour tokens, spacing scales, typography scales, or any other design system documentation that lives in a Storybook docs page.

For a deployed third-party design system example, Adobe's Spectrum Web Components Storybook:

```json
{
  "mcpServers": {
    "storybook-mcp": {
      "command": "npx",
      "args": ["-y", "storybook-mcp@latest"],
      "env": {
        "STORYBOOK_URL": "https://opensource.adobe.com/spectrum-web-components/storybook/index.json",
        "CUSTOM_TOOLS": "[{\"name\":\"getIconList\",\"description\":\"Get All Icons\",\"parameters\":{},\"page\":\"https://opensource.adobe.com/spectrum-web-components/storybook/iframe.html?viewMode=docs&id=icons--docs&globals=\",\"handler\":\"Array.from(document.querySelector('icons-demo').shadowRoot.querySelectorAll('.icon')).map(i => i.textContent)\"}]"
      }
    }
  }
}
```

### How It Works Under the Hood

The extraction pipeline for `getComponentsProps`:

1. `index.json` is fetched from the configured `STORYBOOK_URL`
2. Entries with type `docs` are extracted as the component catalogue
3. For a prop information request, the server finds the target component's documentation ID in the index
4. It constructs the iframe URL: `?viewMode=docs&id={componentId}`
5. Playwright loads that URL in a headless Chromium instance
6. The HTML of the props table is extracted and returned

This approach works even for Storybooks that generate props tables dynamically (for example, from TypeScript declarations compiled at runtime), because it reads the rendered output rather than static manifests.

### When to Use storybook-mcp Instead

Choose `storybook-mcp` over `@storybook/addon-mcp` when:

- Your Storybook uses a non-React framework (Vue, Angular, Web Components, Svelte)
- You want to connect to a deployed/published Storybook rather than a local dev server
- You need to extract design tokens, icon lists, or other information that is not captured in prop tables
- You are working with a third-party design system where you cannot modify the Storybook configuration
- You need the MCP server to be available without requiring the Storybook dev server to be running locally

Choose `@storybook/addon-mcp` when:

- Your project is React
- You want agent-driven story generation and automatic test runs
- You want visual story previews inside the agent chat (with a supporting client)
- You want to keep the MCP configuration part of the Storybook project itself

---

## Current Limitations and Roadmap

**Framework support:** The official addon's docs toolset is React-only — and this is the limitation that matters most. The majority of enterprise design systems I see are not pure React. They use Angular, Web Components, or Vue. For those teams, the official addon's docs toolset simply does not exist yet. The roadmap mentions Vue, Angular, Web Components, and Svelte, but there is no committed timeline. If your stack is not React, the community `storybook-mcp` package is not a fallback — it is currently your only option for docs-level agent grounding.

**Preview status:** The feature is in preview, and I would treat that label seriously. The API has already changed between early versions. If you are setting this up for a team, pin your Storybook version and build the MCP configuration into your project conventions before colleagues start depending on it. Do not assume the `AGENTS.md` instructions you write today will work unchanged after a major Storybook upgrade.

**Client support for MCP Apps:** The `preview-stories` tool's ability to render visual output inline depends on the agent client supporting [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview#client-support). This is a newer MCP extension and not all clients support it yet. VS Code Copilot supports it in Insiders builds with the feature flag enabled. Claude Code and other clients are on different release schedules.

**Storybook Test requirement:** The testing toolset requires `@storybook/test` to already be configured. The MCP server does not configure testing for you — it exposes existing test infrastructure to the agent.

**Community package stability:** `storybook-mcp` by mcpland is community-maintained (MIT licensed, three contributors, version 0.5.1 as of June 2026). It is not an official Storybook project. The Playwright dependency adds installation overhead and means the first run can be slow while Chromium downloads.

---

## Key Takeaways

- **Storybook's MCP server eliminates the component hallucination problem.** By giving agents read access to your actual component documentation, prop types, and stories, it prevents the most common form of AI-assisted frontend code debt.

- **The official `@storybook/addon-mcp` provides three toolsets** — docs, development, and testing — that together create a self-healing loop: generate, test, fix, re-test.

- **The self-healing loop is the headline capability.** Agents can catch accessibility and interaction failures in their own generated code, fix them using your design system's actual values, and confirm the fix passes tests — with no manual intervention.

- **Storybook composition extends coverage.** If you compose multiple Storybooks, the MCP server automatically aggregates manifests from all of them, giving the agent access to your full component landscape.

- **The community `storybook-mcp` package is the better choice for non-React or deployed Storybooks.** Its Playwright-based extraction works on any Storybook instance and its custom tools feature unlocks design tokens, icon catalogues, and other documentation that does not appear in prop tables.

- **The `AGENTS.md` instruction quality is load-bearing.** The quality of agent behaviour with these tools depends heavily on the instructions you provide. Explicit instructions not to guess properties and to always use `get-documentation` before using a component are the difference between the system working as intended and the agent treating the tools as optional.

- **React-only for now, but expanding.** The official addon's docs toolset requires React. Vue, Angular, Web Components, and Svelte support is planned.

- **My honest recommendation: set this up today, even if it is imperfect.** The alternative — doing nothing — means your agents keep generating shadow component systems that erode your design work. An imperfect MCP connection with thin documentation is still better than no connection at all. Start with the official addon if you are on React. Start with `storybook-mcp` if you are not. Improve your Storybook docs as you go. The feedback loop from watching an agent correctly reuse a component you documented is a better motivator than any internal documentation initiative.

---

## Over to You

I'm curious where you are with this. Are you already using AI agents for UI development, and have you hit the component hallucination problem? Or does your team not have a Storybook at all — in which case, is this the nudge to finally set one up?

Drop a comment below: **are you connecting your design system to your AI agent yet — and if not, what's stopping you?**

---

## References

- [Storybook MCP Server — Official Documentation](https://storybook.js.org/docs/ai/mcp/overview)
- [storybookjs/addon-mcp — GitHub Repository](https://github.com/storybookjs/addon-mcp)
- [storybook-mcp by mcpland — GitHub Repository](https://github.com/mcpland/storybook-mcp)
- [Storybook MCP Server — MCP Servers Directory](https://mcpservers.org/servers/github-com-storybookjs-addon-mcp)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Storybook AI Best Practices](https://storybook.js.org/docs/ai/best-practices)
- [Storybook Manifests](https://storybook.js.org/docs/ai/manifests)
- [Storybook MCP API Reference](https://storybook.js.org/docs/ai/mcp/api)
- [mcp-add CLI](https://github.com/paoloricciuti/mcp-add)
- [Storybook Composition](https://storybook.js.org/docs/sharing/storybook-composition)
