# Dataverse Actions Power Apps Code Apps Guide - Practical AI, Copilot & Modern Development Insights

Estimated reading time: 17 minutes

I’ve been building Power Apps Code Apps for a while now, and the question that kept coming up was always the same: *how do I call actual server-side logic from here?* With the `@microsoft/power-apps` npm CLI hitting v1.1.1, that question finally has a clean answer. This guide walks through everything — discovering and scaffolding Dataverse actions, functions, and Power Automate flows, the generated TypeScript service classes, error handling, deployment, and the architectural decisions I’d make on a real project.

## Table of contents

-   [Introduction](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-introduction)

-   [What Are Dataverse Actions and Functions?](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-what-are-dataverse-actions-and-functions-0)
-   [Code Apps vs. Canvas Apps — Why This Matters](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-code-apps-vs-canvas-apps-why-this-matters-0)

-   [Prerequisites and Project Setup](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-prerequisites-and-project-setup-0)
    -   [What You Need](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#what-you-need)
    -   [Scaffolding a New Code App](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#scaffolding-a-new-code-app)
    -   [Verify the Setup](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-verify-the-setup)
-   [Discovering Dataverse Operations with find-dataverse-api](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-discovering-dataverse-operations-with-find-dataverse-api-0)
    -   [Basic Search](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#basic-search)
    -   [Searching for an Action](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-searching-for-an-action)
    -   [Getting JSON Output for Scripting](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-getting-json-output-for-scripting)
    -   [Tips for Effective Discovery](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#tips-for-effective-discovery)
-   [Adding Operations to Your Project with add-dataverse-api](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-adding-operations-to-your-project-with-add-dataverse-api-0)
    -   [What Happens Under the Hood](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#what-happens-under-the-hood)
    -   [Adding a Custom Action](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#adding-a-custom-action)
-   [The Generated File Structure Explained](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-the-generated-file-structure-explained-0)
    -   [The Generated Service Class](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#the-generated-service-class)
    -   [The  IOperationResult<T>  Contract](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#the-ioperationresultt-contract)
-   [Calling Dataverse Functions and Actions in Code](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-calling-dataverse-functions-and-actions-in-code-0)
    -   [Calling an Unbound Function: WhoAmI](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-calling-an-unbound-function-whoami)
    -   [Calling a Bound Action:  AddToQueue](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#calling-a-bound-action-addtoqueue)
    -   [Calling a Custom Action: aidevme\_SyncEnvironment](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#calling-a-custom-action-nextwit_syncenvironment)
    -   [Error Handling Pattern](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#error-handling-pattern)
    -   [React Component Integration Example](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#react-component-integration-example)
-   [Adding Power Automate Flows to Code Apps](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-adding-power-automate-flows-to-code-apps-0)
    -   [The Golden Rule: Power Apps Trigger Only](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#the-golden-rule-power-apps-trigger-only)
    -   [Step 1: List Available Flows](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-step-1-list-available-flows)
    -   [Step 2: Add the Flow](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-step-2-add-the-flow)
    -   [What  add-flow  Does](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#what-add-flow-does)
    -   [Generated Files Structure](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#generated-files-structure)
    -   [The power.config.json Entry](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-the-power-config-json-entry)
-   [Calling Flows from Your App — Typed and Cleanly](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-calling-flows-from-your-app-typed-and-cleanly-0)
    -   [Flow with Input Parameters](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#flow-with-input-parameters)
    -   [Flow without Input Parameters](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-flow-without-input-parameters)
    -   [The result Object Shape](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-the-result-object-shape)
    -   [React Component Pattern for Flow Invocation](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-react-component-pattern-for-flow-invocation)
-   [Updating and Removing Operations and Flows](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-updating-and-removing-operations-and-flows-0)
    -   [Updating an Operation](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#updating-an-operation)
    -   [Removing a Flow](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-removing-a-flow)
    -   [Removing a Dataverse Operation](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#removing-a-dataverse-operation)
-   [Building and Deploying](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-building-and-deploying-0)
    -   [CI/CD Considerations](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#cicd-considerations)
-   [Architectural Patterns: When to Use What](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-architectural-patterns-when-to-use-what-0)
    -   [Direct Dataverse Operations: Best When](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#direct-dataverse-operations-best-when)
    -   [Power Automate Flows: Best When](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#power-automate-flows-best-when)
    -   [Combining Both](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#combining-both)
-   [Troubleshooting Common Issues](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-troubleshooting-common-issues-0)
    -   [“No operations found” on  find-dataverse-api](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#no-operations-found-on-find-dataverse-api)
    -   [Stale generated files after renaming an operation](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#stale-generated-files-after-renaming-an-operation)
    -   [pac code add-data-source  skips your action schema](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#pac-code-add-data-source-skips-your-action-schema)
    -   [Flow not appearing in  list-flows](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#flow-not-appearing-in-list-flows)
    -   [add-flow  fails with an authorization error](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#add-flow-fails-with-an-authorization-error)
    -   [End users cannot invoke the flow at runtime](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#end-users-cannot-invoke-the-flow-at-runtime)
    -   [Can I call a Dataverse action from a Code App without using the CLI tooling?](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-can-i-call-a-dataverse-action-from-a-code-app-without-using-the-cli-tooling)
    -   [Can I add the same operation to multiple code apps?](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-can-i-add-the-same-operation-to-multiple-code-apps)
    -   [Are custom Dataverse actions (backed by plugins) supported?](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-are-custom-dataverse-actions-backed-by-plugins-supported)
    -   [What happens to the generated files when the Dataverse schema changes?](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-what-happens-to-the-generated-files-when-the-dataverse-schema-changes)
    -   [Can I use these features with the PAC CLI ( pac code ) instead of the npm CLI?](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-can-i-use-these-features-with-the-pac-cli-pac-code-instead-of-the-npm-cli)
-   [Key Takeaways](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-key-takeaways)

-   [Conclusion](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-conclusion)
-   [Further Reading](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/#h-further-reading)

## Introduction

Power Apps Code Apps have been quietly maturing into something genuinely exciting — and I say that as someone who’s spent a lot of time in both the Canvas App world and the pro-code TypeScript space. If you’ve already built your first code app — maybe populating a grid from a Dataverse table — you’ll know that the very next question is: **how do I call server-side logic?**

For a while, my honest answer was “write your own `fetch()` calls against the Web API and accept the pain.” It works, but it trades development speed for boilerplate: endpoint URLs written by hand, auth headers to manage, OData responses to decode, and all of it to maintain as the schema evolves. Not fun.

Version `1.1.1` of the `@microsoft/power-apps` npm package changes this completely. Two new CLI command families — `find-dataverse-api` / `add-dataverse-api` and `list-flows` / `add-flow` — let you scaffold **strongly-typed TypeScript service classes** for any Dataverse action, function, or solution-aware Power Automate flow in your environment. The generated code handles authentication, serialization, and OData wrapping transparently — you just call the method.

In this guide I’ll walk through the full workflow from a practitioner’s perspective: prerequisites, every CLI command with its flags, the generated file structure, how to consume the services, error handling patterns, deployment, and the architectural trade-offs I think about when deciding between direct Dataverse operations and Power Automate flows.

**Note:** All features described in this post are currently in **Preview**. Expect some rough edges and verify against the latest Microsoft Learn documentation before shipping to production.

---

![Diagram comparing Dataverse functions (HTTP GET, read-only) and Dataverse actions (HTTP POST, state-changing) with bound and unbound variants](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/dataverse-actions-vs-functions-explainer-1024x576.png?resize=1024%2C576&ssl=1)

## What Are Dataverse Actions and Functions?

Before diving into code, it is worth aligning on terminology — especially since Dataverse (and the underlying OData standard it is built on) distinguishes between two kinds of server-side operations:

**Functions** are **read-only** operations that don’t modify data. They are called via HTTP `GET` and always return a value. Classic examples:

-   `WhoAmI` — returns the calling user’s `UserId`, `BusinessUnitId`, and `OrganizationId`.

-   `RetrievePrincipalAccess` — returns the access rights a principal has to a record.
-   `GetTimeZoneCodeByLocalizedName` — returns a time zone code.

**Actions** are **state-changing** operations called via HTTP `POST`. They can have parameters and optionally return data. Examples:

-   `AddToQueue` — moves a record into a Dataverse queue.

-   `SendEmail` — sends an email from a Dynamics 365 email activity.
-   `GrantAccess` — grants sharing access to a record.

-   `QualifyLead` — converts a lead into an account, contact, and opportunity.

Both come in two variants:

| **Variant** | **Scope** | **Example** |
| **Unbound** | Environment-wide | `WhoAmI`, `SendEmail` |
| **Bound** | Scoped to a specific entity type | `AddToQueue` (bound to `mscrm.queue`) |

Bound operations always require the GUID of the target record as their first argument. As a result, the generated CLI code handles this distinction automatically.

Custom actions created in Dataverse (via the classic workflow designer or via code) also appear through this mechanism, which makes this feature particularly powerful for teams that have invested in server-side business logic.

---

![Architectural comparison showing Canvas Apps routing Dataverse calls through Power Automate flows versus Code Apps calling Dataverse operations directly in TypeScript](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/code-apps-vs-canvas-apps-comparison.png?resize=1024%2C576&ssl=1)

## Code Apps vs. Canvas Apps — Why This Matters

Canvas Apps let you call Power Automate flows via the `Power Apps` connector using Power Fx syntax. What they don’t give you is direct programmatic access to Dataverse Web API operations from the formula bar — you’re limited to the built-in `Dataverse` connector’s CRUD operations.

Code Apps flip this entirely: you write TypeScript, you control the HTTP lifecycle, and — with the CLI tooling — you get generated service classes that call any Dataverse operation with typed inputs and outputs. In my experience, Code Apps become the right call when:

-   You need to call **custom Dataverse actions** (plugin-backed server-side logic).

-   You need operations that aren’t exposed as standard connectors.
-   You want **fine-grained control** over request batching, error handling, and retries.

-   You’re building a **complex SPA** where Power Fx would become a bottleneck.

That said, Code Apps require a Node.js development workflow and TypeScript skills. If your team lives in Power Fx, Canvas Apps are still the better fit — and that’s okay.

---

![Developer workstation setup showing Node.js, npm CLI, VS Code, and Power Platform environment prerequisites for a Code Apps project](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/code-apps-project-setup-prerequisites.png?resize=1024%2C576&ssl=1)

### What You Need

-   A **Power Platform environment** with Code Apps enabled (check your admin centre).

-   **Node.js LTS** (v20+ recommended). Verify with `node -v`.
-   **Git** installed on your machine.

-   `@microsoft/power-apps` npm package at **version 1.1.1 or later**.
-   An **authenticated CLI session** — the CLI will prompt you to sign in interactively if needed.

-   **Access to the Dataverse environment** that contains the operations or flows you want to use.

**Important:** The npm-based CLI (`npx power-apps`) and the classic Power Platform CLI (`pac code`) are **two separate tools**. The actions, functions, and flow commands are only available in the npm CLI. Some `pac code` commands are being deprecated in a future release in favour of `npx power-apps`.

### Scaffolding a New Code App

If you don’t have a code app project yet, scaffold one from the official Vite template:

BashCopy

```


# Clone the template into a new folder
npx degit github:microsoft/PowerAppsCodeApps/templates/vite my-code-app
cd my-code-app

# Install dependencies and the Power Apps SDK
npm install
npm install @microsoft/power-apps

# Initialize the code app (interactive mode)
npx power-apps init

# Or pass options directly
npx power-apps init --displayName "My Business App" --environmentId <your-environment-id>
```

The `init` command authenticates you against your tenant, creates a `power.config.json` in the project root, and wires up the local dev server configuration.

### Verify the Setup

BashCopy

```


# Start the local dev server and verify the app loads
npx power-apps run
```

Open the **Local Play** URL in the same browser profile as your Power Platform tenant. Once you see the app skeleton, you are ready to add server-side integrations.

---

![Terminal output of npx power-apps find-dataverse-api command showing WhoAmI function discovery with parameters and return types](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/find-dataverse-api-command-discovery.png?resize=1024%2C576&ssl=1)

The first step is finding the exact name and signature of the operation you want to call. The `find-dataverse-api` command queries your environment’s Dataverse `$metadata` endpoint and returns matching operations.

### Basic Search

BashCopy

```
npx power-apps find-dataverse-api --search "WhoAmI" --environment-id <your-environment-id>
```

```
====================================================================================================
Dataverse Operations
====================================================================================================

  WhoAmI  (Function)
  Returns: mscrm.WhoAmIResponse

----------------------------------------------------------------------------------------------------
Total: 1 operation(s)
====================================================================================================
```

### Searching for an Action

BashCopy

```
npx power-apps find-dataverse-api --search "AddToQueue"
```

```
====================================================================================================
Dataverse Operations
====================================================================================================

  AddToQueue  (Action)
  Bound to: mscrm.queue
  Parameters:
    - Target: mscrm.crmbaseentity
    - SourceQueue?: mscrm.queue
    - QueueItemProperties?: mscrm.queueitem
  Returns: mscrm.AddToQueueResponse

----------------------------------------------------------------------------------------------------
Total: 1 operation(s)
====================================================================================================
```

**Notice:**

-   The **type** (Function vs. Action) appears in parentheses.

-   **Bound to** indicates the entity the action is scoped to; unbound operations omit this line.
-   Parameters marked with `?` are **optional**.

-   **Returns** shows the OData complex type of the response.

### Getting JSON Output for Scripting

BashCopy

```
npx power-apps find-dataverse-api --search "WhoAmI" --json
```

This returns the raw JSON representation — useful for automation scripts or when working with AI coding assistants that need machine-readable schema data.

JSONCopy

```
[
  {
    "name": "WhoAmI",
    "kind": "Function",
    "isBound": false,
    "parameters": [],
    "returnType": {
      "type": "mscrm.WhoAmIResponse",
      "nullable": false
    }
  }
]
```

Same for **AddToQueue**:

BashCopy

```
npx power-apps find-dataverse-api --search "AddToQueue" --json
```

This returns the raw JSON representation — useful for automation scripts or when working with AI coding assistants that need machine-readable schema data.

JSONCopy

```
[
  {
    "name": "AddToQueue",
    "kind": "Action",
    "isBound": true,
    "parameters": [
      {
        "name": "entity",
        "type": "mscrm.queue",
        "nullable": false
      },
      {
        "name": "Target",
        "type": "mscrm.crmbaseentity",
        "nullable": false
      },
      {
        "name": "SourceQueue",
        "type": "mscrm.queue",
        "nullable": true
      },
      {
        "name": "QueueItemProperties",
        "type": "mscrm.queueitem",
        "nullable": true
      }
    ],
    "returnType": {
      "type": "mscrm.AddToQueueResponse",
      "nullable": false
    }
  }
]
```

### Tips for Effective Discovery

-   The search is a **case-insensitive substring match** on the operation name. `"queue"` will match `AddToQueue`, `RemoveFromQueue`, etc.

-   If you are looking for **custom actions**, search for your publisher prefix, e.g., `"aidevme_"`.
-   Use shorter search terms when you are not sure of the exact name — `"Lead"` to find all lead-related actions.

---

![CLI command add-dataverse-api triggering TypeScript service class generation, showing the flow from Dataverse metadata to generated TypeScript files in VS Code](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/add-dataverse-api-code-generation.png?resize=1024%2C576&ssl=1)

## Adding Operations to Your Project with `add-dataverse-api`

Once you know the operation name, add it to your project:

BashCopy

```


# Using the full flag
npx power-apps add-dataverse-api --api-name WhoAmI

# Using the short alias
npx power-apps add-dataverse-api -n WhoAmI
```

On success:

```
Dataverse API 'WhoAmI' added successfully.
Hint: Run 'npx power-apps run' to test locally, or 'npx power-apps push' to deploy.
```

### What Happens Under the Hood

The command performs several steps automatically:

1.  **Fetches the operation definition** from your environment’s `$metadata`.
2.  **Writes a schema file** at `<schemaPath>/dataverse/WhoAmI.Schema.json` (overwritten on re-run).
3.  **Saves entity schemas** for any referenced parameter or return types (skips if they already exist — idempotent).
4.  **Updates `power.config.json`** — adds the `default.cds` database reference and, for bound operations, registers the binding entity in `dataSources`.
5.  **Regenerates `dataSourcesInfo.ts`** to include the new operation.
6.  **Generates TypeScript model and service classes** under `<codeGenPath>/generated/`.

### Adding a Custom Action

Custom actions created by your development team are discoverable and addable using the same command:

```


# Custom action with publisher prefix
npx power-apps add-dataverse-api -n aidevme_SyncEnvironment
```

The CLI resolves the full OData metadata for custom actions in exactly the same way as for built-in ones.

---

![VS Code file explorer showing the generated folder structure after add-dataverse-api — schemas, models, services, and dataSourcesInfo.ts](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/generated-file-structure-code-apps.png?resize=1024%2C576&ssl=1)

After running `add-dataverse-api`, the CLI creates or modifies these files:

```
project-root/
├── power.config.json                          ← Updated: default.cds reference added
├── schemas/
│   └── dataverse/
│       ├── WhoAmI.Schema.json                 ← Created: operation schema (do not edit)
│       └── <ReferencedEntity>.Schema.json     ← Created (if new): entity schema
├── src/
│   └── generated/
│       ├── models/
│       │   └── <EntityName>Model.ts           ← TypeScript entity model
│       ├── services/
│       │   └── WhoAmIService.ts               ← The service class you import
│       └── dataSourcesInfo.ts                 ← Regenerated: registry of all data sources
```

### The Generated Service Class

Here is what `WhoAmIService.ts` looks like conceptually:

TypeScriptCopy

```
//*!
 * Copyright (C) Microsoft Corporation. All rights reserved.
 * This file is autogenerated. Do not edit this file directly.
 */

import type { IOperationResult } from '@microsoft/power-apps/data';
import { dataSourcesInfo } from '../../../.power/schemas/appschemas/dataSourcesInfo';
import { getClient } from '@microsoft/power-apps/data';

export class WhoAmIService {
  private static readonly dataSourceName = 'whoami';

  private static readonly client = getClient(dataSourcesInfo);

  public static async WhoAmI(): Promise<IOperationResult<Record<string, unknown>>> {
    const result = await WhoAmIService.client.executeAsync<void, Record<string, unknown>>(
      {
        dataverseRequest: {
          action: 'customapi',
          parameters: {
            operationName: 'WhoAmI',
            tableName: WhoAmIService.dataSourceName,
          }
        },
      });
    return result;
  }
}
```

The key point: **you never write `fetch()` calls**, never construct OData URLs, and never manually add `Authorization` headers. In other words, the generated service encapsulates all of that.

### The `IOperationResult<T>` Contract

All generated service methods return `Promise<IOperationResult<T>>`. The shape is:

TypeScriptCopy

```
interface IOperationResult<T> {
  value: T;          // The typed return value
  // Additional OData metadata may be present
}
```

Operations that return nothing use `void` for `T`. Scalar returns (boolean, number) map to the corresponding TypeScript primitive. For complex types or entities, `T` is `Record<string, unknown>`.

---

![TypeScript React component calling WhoAmIService.WhoAmI() and receiving a typed result with UserId and BusinessUnitId](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/calling-dataverse-functions-actions-typescript.png?resize=1024%2C576&ssl=1)

## Calling Dataverse Functions and Actions in Code

### Calling an Unbound Function: `WhoAmI`

TypeScriptCopy

```
import { WhoAmIService } from './generated/services/WhoAmIService';

async function getCurrentUser() {
  try {
    const result = await WhoAmIService.WhoAmI();
    
    console.log('User ID:', result.value.UserId);
    console.log('Business Unit:', result.value.BusinessUnitId);
    console.log('Org ID:', result.value.OrganizationId);
    
    return result.value;
  } catch (error) {
    console.error('WhoAmI call failed:', error);
    throw error;
  }
}
```

### Calling a Bound Action: `AddToQueue`

For bound actions, the first argument is always the GUID of the target record (the entity the action is bound to):

TypeScriptCopy

```
import { AddToQueueService } from './generated/services/AddToQueueService';

async function moveActivityToQueue(
  destinationQueueId: string,
  activityRecord: Record<string, unknown>
) {
  try {
    const result = await AddToQueueService.AddToQueue(
      destinationQueueId,           // GUID of the destination queue (bound entity)
      activityRecord,               // Target: the activity to move
      undefined,                    // SourceQueue?: optional - omit if moving from no queue
      undefined                     // QueueItemProperties?: optional custom properties
    );
    
    console.log('Queue Item ID:', result.value.QueueItemId);
    return result.value.QueueItemId;
  } catch (error) {
    console.error('AddToQueue failed:', error);
    throw error;
  }
}

// Usage example
const emailRecord = {
  '@odata.type': 'Microsoft.Dynamics.CRM.email',
  activityid: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
};

await moveActivityToQueue('yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy', emailRecord);
```

### Calling a Custom Action: `aidevme_SyncEnvironment`

If your team has built a custom Dataverse action backed by a plugin, you call it identically:

TypeScriptCopy

```
import { aidevme_SyncEnvironmentService } from './generated/services/aidevme_SyncEnvironmentService';

async function syncEnvironment(environmentId: string) {
  const result = await aidevme_SyncEnvironmentService.aidevme_SyncEnvironment(
    environmentId,
    true   // forceRefresh parameter (example)
  );
  
  return result.value;
}
```

### Error Handling Pattern

Because these are async calls that cross the network, always handle errors explicitly:

TypeScriptCopy

```
import { WhoAmIService } from './generated/services/WhoAmIService';

async function safeWhoAmI() {
  try {
    const result = await WhoAmIService.WhoAmI();
    return { success: true, data: result.value };
  } catch (error: unknown) {
    const message = error instanceof Error ? error.message : 'Unknown error';
    console.error('[WhoAmI] Failed:', message);
    return { success: false, error: message };
  }
}
```

### React Component Integration Example

Here is a realistic pattern integrating a Dataverse call into a React component with loading and error states:

TypeScriptCopy

```
import React, { useEffect, useState } from 'react';
import { WhoAmIService } from './generated/services/WhoAmIService';

interface UserInfo {
  UserId: string;
  BusinessUnitId: string;
  OrganizationId: string;
}

export const UserInfoPanel: React.FC = () => {
  const [userInfo, setUserInfo] = useState<UserInfo | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadUser() {
      try {
        const result = await WhoAmIService.WhoAmI();
        setUserInfo(result.value);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load user');
      } finally {
        setLoading(false);
      }
    }
    loadUser();
  }, []);

  if (loading) return <div>Loading user info...</div>;
  if (error) return <div className="error">Error: {error}</div>;
  if (!userInfo) return null;

  return (
    <div className="user-info-panel">
      <h3>Current User</h3>
      <p><strong>User ID:</strong> {userInfo.UserId}</p>
      <p><strong>Business Unit:</strong> {userInfo.BusinessUnitId}</p>
    </div>
  );
};
```

---

![Power Automate flow with Power Apps trigger being scaffolded into a Code App using npx power-apps add-flow, generating typed TypeScript service class](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/add-flow-power-automate-code-apps.png?resize=1024%2C576&ssl=1)

## Adding Power Automate Flows to Code Apps

The flow integration follows a very similar pattern to Dataverse operations — and honestly, once I’d done it the first time, I found it even more satisfying because it makes the hand-off between pro-code and low-code teams so clean. There is one critical constraint you need to understand before you start, though.

### The Golden Rule: Power Apps Trigger Only

Only **Manual** flows using the **Power Apps trigger** are supported. Scheduled flows, automated flows, and instant flows with non-Power Apps triggers cannot be added to a code app and will not appear in `list-flows`.

This constraint exists because the Power Apps trigger is the only trigger type that generates an OpenAPI definition compatible with the code generation pipeline. The trigger also provides the mechanism for passing strongly-typed input parameters from the app into the flow.

Additionally, only **solution-aware** flows are available. If your flow lives outside a solution, add it to a solution first via Power Automate’s “Add to solution” feature.

### Step 1: List Available Flows

BashCopy

```


# List all solution-aware flows in your environment
npx power-apps list-flows

# Filter by name substring
npx power-apps list-flows --search approval
```

**Output:**

```
Name                    Status   Modified On   Flow ID
──────────────────────────────────────────────────────────────────────────────
Approval Workflow       Started  2026-01-15    a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
Send Notification       Started  2026-02-01    b1b1b1b1-cccc-dddd-eeee-f2f2f2f2f2f2

Total flows: 2
```

Copy the **Flow ID** of the flow you want to add.

### Step 2: Add the Flow

BashCopy

```
npx power-apps add-flow --flow-id a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
```

On success:

```
Flow added successfully.
```

### What `add-flow` Does

1.  **Downloads the flow’s OpenAPI definition** from Power Automate.
2.  **Generates typed TypeScript files**: a service class and a model file.
3.  **Writes the flow’s schema** to `schemas/logicflows/<FlowName>.Schema.json`.
4.  **Updates `power.config.json`** with the flow’s connection references and `workflowEntityId`.

### Generated Files Structure

```
project-root/
├── power.config.json                              ← Updated: flow connection references added
├── schemas/
│   └── logicflows/
│       └── ApprovalWorkflow.Schema.json           ← Flow's OpenAPI schema (do not edit)
├── src/
│   ├── services/
│   │   └── ApprovalWorkflowService.ts             ← The service class you import
│   └── models/
│       └── ApprovalWorkflowModel.ts               ← TypeScript types for inputs/outputs
```

### The `power.config.json` Entry

JSONCopy

```
"<uuid>": {
  "id": "/providers/microsoft.powerapps/apis/shared_logicflows",
  "displayName": "Logic flows",
  "dataSources": ["ApprovalWorkflow"],
  "workflowDetails": {
    "workflowEntityId": "<dataverse-entity-guid>",
    "workflowDisplayName": "Approval Workflow",
    "workflowName": "<flow-id>",
    "dependencies": {
      "shared_office365": "<dependency-uuid>"
    }
  }
}
```

Note the `dependencies` map — this is where connection references are tracked. The person running `add-flow` must have access to both the flow and all of its underlying connections (e.g., an Office 365 Outlook connection for a flow that sends email). If a connection is missing, the command fails with an authorization error.

---

![TypeScript code calling ApprovalWorkflowService.Run() with typed input parameters and handling the success/error result object](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/calling-flows-typed-typescript-code-apps.png?resize=1024%2C576&ssl=1)

## Calling Flows from Your App — Typed and Cleanly

The generated service class exposes a single `Run` static method. The signature varies based on whether the flow’s Power Apps trigger defines input parameters.

### Flow with Input Parameters

Design your flow’s Power Apps trigger to ask for inputs (use the “Ask in PowerApps” dynamic value in each step, or define trigger schema explicitly):

TypeScriptCopy

```
import { ApprovalWorkflowService } from './services/ApprovalWorkflowService';

async function requestApproval(requester: string, amount: number) {
  const result = await ApprovalWorkflowService.Run({
    requester,
    amount,
  });

  if (result.success) {
    console.log('Approval flow triggered. Response:', result.data);
    return result.data;
  } else {
    console.error('Approval flow failed:', result.error?.message);
    throw result.error;
  }
}
```

### Flow without Input Parameters

TypeScriptCopy

```
import { SendNotificationService } from './services/SendNotificationService';

async function triggerNotification() {
  const result = await SendNotificationService.Run();

  if (result.success) {
    console.log('Notification flow triggered successfully.');
  } else {
    console.error('Notification failed:', result.error?.message);
  }
}
```

### The `result` Object Shape

| **Property** | **Type** | **Description** |
| success | boolean | `true` if the flow was triggered without error |
| data | (varies) | Typed response payload from the flow’s `Respond to a PowerApp or flow` action, if configured |
| error | Error | undefined | Error details when `success` is `false` |

**Tip:** To get typed response data back from the flow, add a **“Respond to a PowerApp or flow”** action as the last step in your flow. Define the output fields there, and the code generator will include them in the TypeScript response type.

### React Component Pattern for Flow Invocation

TypeScriptCopy

```
import React, { useState } from 'react';
import { ApprovalWorkflowService } from './services/ApprovalWorkflowService';

export const ApprovalForm: React.FC = () => {
  const [requester, setRequester] = useState('');
  const [amount, setAmount] = useState(0);
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
  const [message, setMessage] = useState('');

  async function handleSubmit() {
    setStatus('loading');
    try {
      const result = await ApprovalWorkflowService.Run({ requester, amount });
      if (result.success) {
        setStatus('success');
        setMessage('Approval request submitted successfully!');
      } else {
        throw result.error;
      }
    } catch (err) {
      setStatus('error');
      setMessage(err instanceof Error ? err.message : 'Submission failed');
    }
  }

  return (
    <div className="approval-form">
      <input
        value={requester}
        onChange={e => setRequester(e.target.value)}
        placeholder="Your name"
      />
      <input
        type="number"
        value={amount}
        onChange={e => setAmount(Number(e.target.value))}
        placeholder="Amount (EUR)"
      />
      <button onClick={handleSubmit} disabled={status === 'loading'}>
        {status === 'loading' ? 'Submitting...' : 'Request Approval'}
      </button>
      {status === 'success' && <p className="success">{message}</p>}
      {status === 'error' && <p className="error">{message}</p>}
    </div>
  );
};
```

---

![CLI commands for re-running add-dataverse-api and add-flow to update schemas, and remove-flow to remove a flow from a Code App project](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/update-remove-operations-flows-code-apps.png?resize=1024%2C576&ssl=1)

## Updating and Removing Operations and Flows

### Updating an Operation

Both `add-dataverse-api` and `add-flow` are **idempotent**. Re-running them is the correct way to pick up schema changes:

BashCopy

```


# Pick up changes to WhoAmI (unlikely, but shows the pattern)
npx power-apps add-dataverse-api -n WhoAmI

# Pick up updated flow definition (new parameters, changed connections, etc.)
npx power-apps add-flow --flow-id a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
```

For flows, the command matches by `workflowEntityId` in `power.config.json`, so it reuses the existing UUID entry — no manual cleanup required.

**Important:** The app does **not** auto-detect flow definition changes. If a flow author adds a new parameter, you must manually re-run `add-flow` to regenerate the service class. Until you do, the old typed signature remains in your code.

### Removing a Flow

BashCopy

```


# Remove by data source name (as shown in power.config.json)
npx power-apps remove-flow --flow-name ApprovalWorkflow

# Remove by original flow ID
npx power-apps remove-flow --flow-id a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1
```

The command removes the flow from `power.config.json` and regenerates model services. However, it does **not** automatically delete the generated `.ts` files — remove those manually if you no longer need them.

### Removing a Dataverse Operation

There is currently no `remove-dataverse-api` command in the CLI. To remove an operation:

1.  Delete the generated service file (`src/generated/services/<ApiName>Service.ts`).
2.  Delete the schema file (`schemas/dataverse/<ApiName>.Schema.json`).
3.  Remove the `dataSources` entry from `power.config.json` manually.
4.  Re-run any import in your app code that referenced the removed service.

---

![CI/CD pipeline diagram showing npm run build, TypeScript compilation, Vite bundle, and npx power-apps push deploying to a Power Platform environment](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/code-apps-build-deploy-pipeline.png?resize=1024%2C576&ssl=1)

## Building and Deploying

Once your operations and flows are wired up and tested locally:

BashCopy

```


# Verify locally first
npx power-apps run

# Build the production bundle
npm run build    # runs: tsc -b && vite build

# Push to your Power Platform environment
npx power-apps push
```

The `push` command packages your compiled output and publishes a new version of the code app to your environment. On success, it returns the Power Apps URL where the live app can be played.

### CI/CD Considerations

For automated pipelines (GitHub Actions, Azure DevOps), use non-interactive authentication:

YAMLCopy

```


# .github/workflows/deploy.yml (conceptual)
- name: Authenticate and Deploy Code App
  run: |
    npx power-apps init --environmentId ${{ secrets.PP_ENV_ID }} --clientId ${{ secrets.SP_CLIENT_ID }} --clientSecret ${{ secrets.SP_CLIENT_SECRET }} --tenantId ${{ secrets.TENANT_ID }}
    npm run build
    npx power-apps push
```

Check the official Power Apps SDK npm package for the latest supported auth flags, as non-interactive authentication support was still evolving at the time of writing.

---

![Architecture diagram showing a Code App branching to direct Dataverse actions for low-latency synchronous calls and to Power Automate flows for async multi-connector orchestration](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/architectural-patterns-dataverse-vs-flows.png?resize=1024%2C576&ssl=1)

## Architectural Patterns: When to Use What

Now that you know *how* to call both Dataverse operations and Power Automate flows, the question becomes *which approach to use for a given piece of logic*. This is actually the decision I spend the most time on with clients — and the answer is usually less obvious than it looks.

### Direct Dataverse Operations: Best When

-   The logic is **already implemented as a Dataverse plugin** backing a custom action.

-   You need **low latency** — direct OData calls are faster than triggering a cloud flow.
-   The operation is **synchronous** and you need an immediate typed response.

-   You are calling standard platform operations (`WhoAmI`, `AddToQueue`, `QualifyLead`, etc.).

### Power Automate Flows: Best When

-   The logic involves **multiple connectors** (send email, update SharePoint, post to Teams).

-   You need **approval workflows** with human-in-the-loop steps.
-   The work is **long-running or asynchronous** and the flow runs in the background.

-   Business analysts or low-code developers own the logic and need to modify it without touching the app code.
-   You need **retry policies and run history** built in.

### Combining Both

A realistic enterprise pattern combines the two: a code app calls a Dataverse custom action (for fast, transactional work) and separately triggers a Power Automate flow (for downstream notifications and integrations) — both with full type safety from generated service classes.

```
Code App
  │
  ├── WhoAmIService.WhoAmI()                    → Dataverse Function (fast, sync)
  ├── aidevme_SyncEnvironmentService.Run()      → Custom Dataverse Action (plugin logic)
  └── ApprovalWorkflowService.Run({ ... })      → Power Automate Flow (async, multi-step)
```

---

![Troubleshooting guide visual showing common error scenarios — no operations found, flow not appearing in list-flows, add-flow authorization error, and end-user permission issues](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/05/troubleshooting-code-apps-dataverse-flows.png?resize=1024%2C576&ssl=1)

## Troubleshooting Common Issues

### “No operations found” on `find-dataverse-api`

The search is substring-based on the operation **name only**. Try:

-   A shorter or alternate term.

-   Check that your CLI session is authenticated against the correct environment.
-   Add `--json` to see the raw response and confirm the query is hitting the right endpoint.

### Stale generated files after renaming an operation

Rename or removal of a Dataverse custom action leaves orphaned files in `src/generated/`. Delete them manually and rerun `add-dataverse-api` if you want to regenerate.

### `pac code add-data-source` skips your action schema

This is expected. The `Microsoft.PowerApps/dataverseOperation` schema type generated by `add-dataverse-api` is not recognized by the PAC CLI and is silently skipped. This is not an error — the PAC CLI handles entity data sources while the npm CLI handles operation schemas. Use `npx power-apps push` for deployment.

### Flow not appearing in `list-flows`

-   Verify the flow has the **Power Apps trigger** (not scheduled, automated, or other).

-   Verify the flow is **in a solution**. Non-solution flows are invisible to the CLI.
-   Check that you are authenticated against the correct environment.

### `add-flow` fails with an authorization error

The person running `add-flow` must have access to the flow **and** to all underlying connections (e.g., Office 365 Outlook, SharePoint). Ask the flow owner to share access to the connections, or run the command as the flow owner.

### End users cannot invoke the flow at runtime

End users need sufficient Dataverse permissions. Assign the **App Opener** security role (or a custom role with equivalent privileges) to the users who need to run the app.

---

## Frequently Asked Questions

### Can I call a Dataverse action from a Code App without using the CLI tooling?

Yes, you can always write raw `fetch()` calls against the Dataverse Web API. The CLI tooling simply generates the boilerplate for you. The generated code calls the same Web API endpoints you would call manually. For one-off integrations, manual fetch calls are acceptable. For anything production-grade, the generated typed services save significant time and reduce error surface.

### Can I add the same operation to multiple code apps?

Yes. Each code app is an independent npm project. Run `add-dataverse-api` (or `add-flow`) in each project independently. The schema files and generated code are local to the project.

### Are custom Dataverse actions (backed by plugins) supported?

Yes. Custom actions are discoverable via `find-dataverse-api` using your publisher prefix (e.g., `--search "aidevme_"`). The CLI generates a service class for them identically to built-in actions. The only requirement is that the custom action is registered in the Dataverse environment your CLI session is authenticated against.

###  What happens to the generated files when the Dataverse schema changes?

Nothing happens automatically. You must re-run `add-dataverse-api -n <OperationName>` to regenerate. The command is idempotent and will overwrite the schema file and regenerated service class with the latest definition. This is by design — it keeps you in control of when schema updates are picked up.

### Can I use these features with the PAC CLI (`pac code`) instead of the npm CLI?

No. The `find-dataverse-api`, `add-dataverse-api`, `list-flows`, `add-flow`, and `remove-flow` commands are only available in the npm-based CLI (`npx power-apps`). The PAC CLI (`pac code`) does not support these commands and is being deprecated in favour of the npm CLI for code app development.

## Key Takeaways

-   **Two CLI commands do the heavy lifting:** `add-dataverse-api` for Dataverse operations and `add-flow` for Power Automate flows — both generate strongly-typed TypeScript service classes with zero manual REST wiring.

-   **Discover before you scaffold:** Always run `find-dataverse-api` (or `list-flows`) first to confirm the exact operation name, parameters, and return types before running the code generation command.
-   **Idempotent by design:** Re-running `add-dataverse-api` or `add-flow` is the correct way to pick up schema changes. The CLI safely overwrites schema files and regenerates service classes.

-   **Flows require a Power Apps trigger:** Only solution-aware flows with the Power Apps trigger are supported. Non-solution flows and all other trigger types are invisible to the CLI.
-   **Choose direct operations for speed, flows for orchestration:** Use Dataverse actions for synchronous, low-latency server logic backed by plugins. Use Power Automate flows when you need multi-connector orchestration, approvals, or long-running background processes.

-   **Still in Preview (May 2026):** The `add-dataverse-api` and `add-flow` features are in Preview. Validate against the latest Microsoft Learn documentation before deploying to production-critical environments.

---

## Conclusion

Power Apps Code Apps have crossed an important threshold — and I think this is one of those moments in the Power Platform that will look obvious in hindsight. They’re no longer limited to reading Dataverse tables and rendering UI. With the `add-dataverse-api` and `add-flow` CLI commands, you can integrate the full depth of your Dataverse environment — standard platform operations, custom plugin-backed actions, and multi-step Power Automate flows — into a TypeScript codebase with generated, strongly-typed service classes.

The developer experience feels a lot like what you’d get from an OpenAPI code generator or a GraphQL client. Declare what you want, let the tool generate the integration code, and get back to focusing on what actually matters: your application logic.

For enterprise Power Platform architects, the layering strategy this enables is genuinely clean: keep business logic in Dataverse plugins or Power Automate flows (where it belongs), and keep presentation and interaction logic in the Code App (where TypeScript excels). The CLI tooling bridges the two layers without you having to wire it together manually.

There are still rough edges — no `remove-dataverse-api` command, and you have to manually re-run `add-flow` when a flow changes. I’m confident those will get addressed as this moves from Preview to GA. The foundation is solid, and I’d already be using this on production-track projects.

---

## Further Reading

-   [Microsoft Learn: How to add a Dataverse action or function to your code app](https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/add-dataverse-action-function)

-   [Microsoft Learn: Add Power Automate flows to a code app (preview)](https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/add-flows)
-   [Microsoft Learn: Quickstart with npm CLI (preview)](https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/npm-quickstart)

-   [Use Web API actions — Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/use-web-api-actions)
-   [Use Web API functions — Microsoft Learn](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/use-web-api-functions)

-   [@microsoft/power-apps on npm](https://www.npmjs.com/package/@microsoft/power-apps)

### *Related*

[![Canvas Apps vs Code Apps decision point - visual representation of low-code meeting its architectural ceiling with pro-code path ahead](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/04/canvas-vs-code-apps-featured.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/power-apps-canvas-apps-vs-code-apps-when-low-code-hits-its-ceiling/ "Power Apps: Canvas Apps vs. Code Apps – When Low-Code Hits Its Ceiling")

#### [Power Apps: Canvas Apps vs. Code Apps – When Low-Code Hits Its Ceiling](https://aidevme.com/power-apps-canvas-apps-vs-code-apps-when-low-code-hits-its-ceiling/ "Power Apps: Canvas Apps vs. Code Apps – When Low-Code Hits Its Ceiling")

Most Power Platform architects reach for Canvas Apps by default — because they know them, and they work. This article will help you compare Canvas Apps vs Code Apps and understand the pros and cons of each. But there's a moment in every serious project where Canvas stops being an…

April 16, 2026

In "Canvas Apps"

[![Power Apps MCP Server agent feed — AI agent extracting Dataverse records with human approval interface — AIDevMe 2026](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/02/power-apps-mcp-server-complete-guide-featured.png?fit=768%2C512&ssl=1&resize=350%2C200)](https://aidevme.com/power-apps-mcp-server-complete-guide/ "Power Apps MCP Server: Complete Guide to Every Feature (Public Preview 2026)")

#### [Power Apps MCP Server: Complete Guide to Every Feature (Public Preview 2026)](https://aidevme.com/power-apps-mcp-server-complete-guide/ "Power Apps MCP Server: Complete Guide to Every Feature (Public Preview 2026)")

The Power Apps MCP (Model Context Protocol) Server is now in public preview. It exposes three tools — invoke\_data\_entry, request\_assistance, and log\_for\_review — that let AI agents automate tasks inside model-driven apps with built-in human supervision via a redesigned agent feed. This guide covers every feature, technical detail, current limitation,…

February 21, 2026

In "AI & Copilot"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [Dataverse Actions, Functions & Flows in Power Apps Code Apps: Complete Guide](https://aidevme.com/dataverse-actions-functions-flows-in-power-apps-code-apps-complete-guide/)