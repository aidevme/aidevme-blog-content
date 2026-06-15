# I've built agents on Microsoft Graph. You probably have too. #

You know the experience: one user question, five API calls, and a context window full of message IDs and file record strings the agent didn't need and now has to reason through anyway.

Microsoft just shipped the fix for that. It's called Work IQ — and it goes GA on June 16.

Here's what changes:

𝗚𝗿𝗮𝗽𝗵 𝗿𝗲𝘁𝘂𝗿𝗻𝘀 𝗱𝗮𝘁𝗮. 𝗪𝗼𝗿𝗸 𝗜𝗤 𝗿𝗲𝘁𝘂𝗿𝗻𝘀 𝗰𝗼𝗻𝘁𝗲𝘅𝘁.

An agent asking "what's the status of Project Alpha?" doesn't get a list of emails to parse. It gets a synthesised answer grounded in everything that's happened across email, Teams, calendar, and files. Work IQ's internal LLMs do that pre-processing before the result ever reaches your agent.

The numbers:

→ 𝟮𝘅 𝗳𝗮𝘀𝘁𝗲𝗿 than traditional API calls
→ 𝟴𝟬% 𝗳𝗲𝘄𝗲𝗿 𝘁𝗼𝗸𝗲𝗻𝘀 in agent coding harnesses
→ 𝟭𝟬 𝗠𝗖𝗣 𝘁𝗼𝗼𝗹𝘀 instead of the hundreds of Graph endpoints

That 80% token reduction is the one that actually changes your economics. Your context window gets business context, not metadata. And 10 tools instead of hundreds means your agent makes decisions faster and fails less often — every tool in a context window is a decision point.

This isn't a new product. It's the intelligence layer already running underneath Microsoft Scout, Copilot Cowork, and M365 Copilot itself. It's now open to developers.

𝗧𝗵𝗲 𝗪𝗼𝗿𝗸𝘀𝗽𝗮𝗰𝗲𝘀 𝗱𝗼𝗺𝗮𝗶𝗻 𝗶𝘀 𝘁𝗵𝗲 𝗼𝗻𝗲 𝗜 𝗸𝗲𝗲𝗽 𝘁𝗵𝗶𝗻𝗸𝗶𝗻𝗴 𝗮𝗯𝗼𝘂𝘁.

Long-running enterprise agents have always had an awkward question: where does intermediate state live between steps, inside the tenant boundary, without adding a separate governed data store? Workspaces is the answer Microsoft is standardising on. Scout and Copilot Cowork both depend on it. Expect this to become the expected pattern in enterprise M365 agent architectures.

𝗬𝗼𝘂 𝗰𝗮𝗻 𝘀𝘁𝗮𝗿𝘁 𝘁𝗼𝗱𝗮𝘆:

```
npm install -g @microsoft/workiq
workiq ask -q "What meetings do I have tomorrow?"
```

The MCP server and CLI are in public preview now. Four plugins: standard queries, full read/write entity access, declarative agent scaffolding + eval, and productivity insights.

One thing nobody talks about enough: if you're currently building Graph API custom connectors for M365 data in Copilot Studio or Power Automate, you should genuinely compare that path against the `workiq-preview` plugin before you commit. The capabilities overlap significantly. The token economics don't.

---

What are you currently using for M365 context in your agent builds? Still on Graph, or already moving?

Link to the full breakdown👇

https://aidevme.com/work-iq-apis-microsoft-365-intelligence-layer-enterprise-agents/

#PowerPlatform #MicrosoftGraph #MCPServer #AIAgents #CopilotStudio #Microsoft365 #EnterpriseAI #AgentDevelopment #WorkIQ #Dataverse
