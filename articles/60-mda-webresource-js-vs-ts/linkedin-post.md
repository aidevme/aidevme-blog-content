**Still writing Model-Driven App web resources in plain JavaScript?**

You're not wrong. But you might be making your future self's life harder than it needs to be.

I just published a complete guide comparing three approaches — plain JS, TypeScript + Webpack, and TypeScript + esbuild — using the same real example implemented in all three. Same form, same Xrm API calls, same deployment target.

Here's what the guide covers:

🔧 When plain JavaScript is still the right call (it genuinely is, for solo one-off scripts)
⚡ Why esbuild is the better default for new TypeScript projects — sub-100ms builds, minimal config
📦 How to structure a multi-developer workspace with npm workspaces so two devs never touch the same file
🚀 Every deployment scenario from manual portal upload to multi-stage Azure DevOps pipelines with approval gates
🔒 Why managed solutions in test and production aren't optional if you care about rollback and audit trails

The biggest insight for me writing this: the three approaches aren't really competing. They form a natural progression. You start with plain JS, add TypeScript + esbuild once the script grows, then add workspaces when a second developer joins, then add CI/CD when you hit test and production. Each step is incremental — you don't have to do it all at once.

Drop a comment if you're using a different bundler setup or have strong opinions on Webpack vs esbuild for enterprise Power Platform projects — I'd love to hear what's working in practice.

🔗 Link in comments

#PowerPlatform #Dynamics365 #TypeScript #ModelDrivenApps #PowerApps #DevOps #GitHub