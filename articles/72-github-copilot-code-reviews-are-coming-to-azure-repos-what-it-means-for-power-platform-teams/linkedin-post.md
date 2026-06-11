GitHub Copilot code reviews just landed in Azure Repos — and this one is aimed squarely at teams that aren't migrating to GitHub anytime soon.

Microsoft announced a limited public preview on June 9. You request a Copilot review from the same Reviewers section you'd use to tag a colleague. It runs asynchronously, posts inline comments, and lets you apply suggestions directly. No new UI. No migration.

Here's what matters for Power Platform teams specifically:

𝗧𝗵𝗶𝘀 𝗳𝗶𝘁𝘀 𝘆𝗼𝘂𝗿 𝗰𝗼𝗱𝗲 𝗹𝗮𝘆𝗲𝗿, 𝗻𝗼𝘁 𝘆𝗼𝘂𝗿 𝗱𝗲𝗰𝗹𝗮𝗿𝗮𝘁𝗶𝘃𝗲 𝗹𝗮𝘆𝗲𝗿.
Dataverse plugins (C#) and PCF controls (TypeScript/React) — yes. Canvas app YAML and Power Automate flow JSON — not yet. Set the right expectation with your team before rollout.

𝗧𝗵𝗿𝗲𝗲-𝘁𝗶𝗲𝗿 𝗲𝗻𝗮𝗯𝗹𝗲𝗺𝗲𝗻𝘁 𝗴𝗶𝘃𝗲𝘀 𝘆𝗼𝘂 𝗰𝗼𝗻𝘁𝗿𝗼𝗹.
Org → Repo → User. You can enable it for your plugin library and PCF component repo without flipping it on across your entire Azure DevOps organization. That's the right default approach.

𝗕𝗶𝗹𝗹𝗶𝗻𝗴 𝗴𝗼𝗲𝘀 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗔𝘇𝘂𝗿𝗲 𝘀𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻.
1 AI credit = $0.01 USD, charged per review based on PR size. Not a fixed seat cost. Set up a cost alert before you scale it.

𝗣𝗿𝗲𝘃𝗶𝗲𝘄 𝗹𝗶𝗺𝗶𝘁𝘀 𝘁𝗼 𝗸𝗻𝗼𝘄:
→ 100 changed files per PR
→ 5 concurrent reviews per org
→ 10 GB max repo size

For most Power Platform codebases these aren't blockers — unless you're committing full unpacked solution exports with dozens of entity XML files.

I've submitted my sign-up request and I'm waiting for preview access. Once I can run it against a real Dataverse plugin codebase, I'll post hands-on findings.

For now, the setup guide, billing breakdown, and Power Platform-specific adoption notes are in the article — link in the comments 👇

https://aidevme.com/github-copilot-code-reviews-are-coming-to-azure-repos-what-it-means-for-power-platform-teams/

#GitHubCopilot #AzureDevOps #AzureRepos #PowerPlatform #ALM #Dataverse #PCFControls
