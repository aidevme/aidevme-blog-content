# PCF Webpack Plugins That Cut My Build Time in Half

Estimated reading time: 9 minutes

## Introduction

Let’s be honest – when you’re knee-deep in PCF development, the last thing you want to think about is webpack configuration. I totally get it. The default PCF CLI does a decent job, and you’ve got actual features to build. But here’s the thing: I’ve wasted too many hours debugging build issues and watching bloated bundles destroy load times to not share what I’ve learned about PCF webpack plugins.

In my last article, “[PCF Controls Tips & Tricks: How to Reduce Bundle Size and Improve](https://aidevme.com/pcf-controls-tips-tricks-pcf-webpack-plugins-optimize-build-performance/#) [Performance](https://aidevme.com/pcf-controls-tips-tricks-how-to-reduce-bundle-size-and-improve-performance/)“, I went deep on the bundle size nightmare – especially that Fluent UI icons disaster that probably cost me a few gray hairs. This time, I want to talk about the other webpack plugins that have actually made my life easier. Think of this as the “nice-to-have” tools that become “can’t-live-without” once you try them.

I’m not going to pretend these are earth-shattering discoveries. They’re just solid, battle-tested plugins that I wish someone had told me about when I started building PCF controls.

## Why Bother Customizing Your Webpack Config?

Look, the PCF CLI gives you a webpack config out of the box, and it works. But “works” and “works well” are two different things. Here’s what customizing my webpack setup has done for me:

-   **Saved me from shipping 4MB of unused icons** (true story – check my bundle size article)

-   **Cut my build times in half** by cleaning up properly
-   **Actually understood what was in my bundles** instead of crossing my fingers and hoping

-   **Stopped breaking production** with random asset issues
-   **Made my CI/CD pipeline actually useful** instead of just decorative

You don’t need all of these plugins on day one. Start with the ones that solve your current pain points, then add more as needed.

## The Plugins I Actually Use (And Why You Should Too)

### 1\. Bundle Analyzer – Your New Best Friend

**Plugin:** `webpack-bundle-analyzer`

If you only install one plugin from this list, make it this one. Seriously. I covered this extensively in my bundle size article, but it’s worth repeating: you cannot optimize what you cannot see.

**Heads up:** I did a deep dive on this in my “[How to Reduce Bundle Size and Improve Performance](https://aidevme.com/pcf-controls-tips-tricks-pcf-webpack-plugins-optimize-build-performance/#)” article, including the whole Fluent UI icons horror show. If you haven’t read that yet, stop right here and go check it out. I’ll wait.

**Installation:**

Bash

```
npm install --save-dev webpack-bundle-analyzer
```

**Configuration:**

JavaScript

```
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
      reportFilename: 'bundle-report.html'
    })
  ]
};
```

**Why I love it:**

-   Shows you exactly where your bundle size is going (spoiler: it’s usually icons or a dependency you forgot about)

-   Makes it painfully obvious when you’ve messed up an import
-   Great for explaining to your manager why you need time to optimize

-   The visual treemap is oddly satisfying when you get it right

**Pro tip:** I use `analyzerMode: 'static'` because it generates an HTML file you can share with your team or stick in your CI/CD artifacts. No one wants a dev server running just to look at a bundle report.

### 2\. Compression Plugin – Because Every Kilobyte Counts

**Plugin:** `compression-webpack-plugin`

After you’ve optimized your bundle (seriously, go read my bundle size article first), compression is the cherry on top. This pre-compresses your assets so they’re ready to serve smaller and faster.

**Installation:**

Bash

```
npm install --save-dev compression-webpack-plugin
```

**Configuration:**

JavaScript

```
const CompressionPlugin = require('compression-webpack-plugin');

module.exports = {
  plugins: [
    new CompressionPlugin({
      algorithm: 'gzip',
      test: /\.js$|\.css$/,
      threshold: 10240,
      minRatio: 0.8
    })
  ]
};
```

Why it matters:

-   Users on slow connections will thank you

-   Smaller payloads = happier Dataverse environments
-   It’s basically free performance once you set it up

-   I’ve seen 60-70% size reductions just from gzip alone

**My setup:** I only enable this for production builds. No point compressing during development when you’re rebuilding constantly.

### Clean Webpack Plugin – Stop the Madness

**Plugin:** `clean-webpack-plugin`

This one’s simple but saved my bacon more times than I can count. It just… cleans your output directory before each build. That’s it. But trust me, you need it.

**Installation:**

Bash

```
npm install --save-dev clean-webpack-plugin
```

**Configuration:**

JavaScript

```
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  plugins: [
    new CleanWebpackPlugin()
  ]
};
```

Why you need this:

-   Ever spent an hour debugging only to realize you were looking at an old build? Yeah, me too.

-   Prevents the “works on my machine” problems caused by stale files
-   Makes your builds deterministic (fancy word for “predictable”)

-   Your CI/CD will love you for it

**Story time:** I once shipped a bug to production because I had old compiled files hanging around. Never again.

### 4\. Copy Webpack Plugin – Because Assets Are a Pain

**Plugin:** `copy-webpack-plugin`

Managing static assets in PCF controls can be annoying. Images, fonts, config files – they all need to end up in the right place. This plugin handles all that for you.

**Installation:**

Bash

```
npm install --save-dev copy-webpack-plugin
```

**Configuration:**

JavaScript

```
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  plugins: [
    new CopyPlugin({
      patterns: [
        { from: 'src/assets', to: 'assets' },
        { from: 'src/img', to: 'img' }
      ]
    })
  ]
};
```

**Real-world use cases:**

-   Copying icon files or brand images

-   Moving configuration JSONs to the output
-   Handling fonts or other binary assets

-   Basically anything that webpack doesn’t naturally process

**My workflow:** I keep all static assets in a `src/assets` folder and let this plugin handle the rest. One less thing to think about.

## 5\. Terser Plugin – Minification Done Right

**Plugin:** `terser-webpack-plugin`

Webpack 5 includes Terser by default, but I customize it because the defaults aren’t aggressive enough for my taste. This works hand-in-hand with the optimization settings from my bundle size article.

**Installation:**

Bash

```
npm install --save-dev terser-webpack-plugin
```

**Configuration:**

JavaScript

```
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true,  // Bye-bye console.logs
            drop_debugger: true  // And debugger statements too
          },
          format: {
            comments: false  // No comments in production
          }
        },
        extractComments: false
      })
    ]
  }
};
```

**What this does:**

-   Removes all `console.log` statements from production (you do this, right?)

-   Strips out debugger statements you forgot to remove
-   Deletes comments to save a few more bytes

-   Makes your production bundle clean and minimal

**Important:** Make sure you’ve also got `usedExports: true` and `sideEffects: true` in your optimization config (covered in my bundle size article). These all work together to enable proper tree-shaking.

### 6\. Define Plugin – Environment Variables Made Easy

**Plugin:** Built-in `webpack.DefinePlugin`

This gem is built into webpack, so no installation needed. It lets you inject environment variables and constants at build time. Super useful for different configurations across environments.

**Configuration:**

JavaScript

```
const webpack = require('webpack');

module.exports = {
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'development'),
      'BUILD_VERSION': JSON.stringify('1.0.0'),
      'API_ENDPOINT': JSON.stringify(process.env.API_ENDPOINT || ''),
      'ENABLE_LOGGING': JSON.stringify(process.env.NODE_ENV !== 'production')
    })
  ]
};
```

How I use it:

-   Different API endpoints for dev/staging/prod

-   Feature flags for testing new functionality
-   Build version tracking

-   Conditional logging (verbose in dev, quiet in prod)

**Gotcha:** Notice the `JSON.stringify` everywhere? That’s not optional. DefinePlugin does a find-and-replace, so you need to stringify strings or they’ll break.

### 7\. ESLint Webpack Plugin – Catch Mistakes Early

**Plugin:** `eslint-webpack-plugin`

I used to run ESLint separately, then realize at deployment time that I’d broken something. This plugin integrates ESLint into your webpack build, so you catch issues immediately.

**Installation:**

Bash

```
npm install --save-dev eslint-webpack-plugin
```

**Configuration:**

JavaScript

```
const ESLintPlugin = require('eslint-webpack-plugin');

module.exports = {
  plugins: [
    new ESLintPlugin({
      extensions: ['ts', 'tsx'],
      fix: true,        // Auto-fix what it can
      cache: true,      // Much faster on subsequent builds
      failOnError: false  // I set to true in CI/CD only
    })
  ]
};
```

**Why I added this:**

-   Stops me from committing dumb mistakes

-   Enforces consistent code style across the team
-   Auto-fixes simple issues (missing semicolons, spacing, etc.)

-   Makes code reviews focus on logic instead of formatting

**Team tip:** Agree on ESLint rules before enabling this, or prepare for some… spirited discussions about tabs vs. spaces.

## Putting It All Together

Alright, so you’ve got all these plugins. Now what? Here’s my actual webpack config that combines everything from both articles:

JavaScript

```
const path = require('path');
const webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const CompressionPlugin = require('compression-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');
const ESLintPlugin = require('eslint-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production';
  const shouldAnalyze = process.env.ANALYZE === 'true';
  
  return {
    plugins: [
      // Always clean before building - trust me on this
      new CleanWebpackPlugin(),
      
      // Copy static assets
      new CopyPlugin({
        patterns: [
          { from: 'src/assets', to: 'assets' }
        ]
      }),
      
      // ESLint integration
      new ESLintPlugin({
        extensions: ['ts', 'tsx'],
        fix: true,
        cache: true,
        failOnError: isProduction  // Only fail builds in production
      }),
      
      // Environment variables
      new webpack.DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify(argv.mode),
        'ENABLE_LOGGING': JSON.stringify(!isProduction)
      }),
      
      // Bundle analyzer - only when requested
      // Run: ANALYZE=true npm run build
      ...(shouldAnalyze ? [
        new BundleAnalyzerPlugin({
          analyzerMode: 'static',
          openAnalyzer: false,
          reportFilename: 'bundle-report.html'
        })
      ] : []),
      
      // Compression - production only
      ...(isProduction ? [
        new CompressionPlugin({
          algorithm: 'gzip',
          test: /\.js$|\.css$/
        })
      ] : [])
    ],
    
    // This is the key optimization config from my bundle size article
    // These settings make the Fluent UI direct imports actually work
    optimization: {
      usedExports: true,    // Tree-shaking step 1
      sideEffects: true,    // Tree-shaking step 2
      minimize: isProduction,
      minimizer: [
        new TerserPlugin({
          terserOptions: {
            compress: {
              drop_console: isProduction,
              drop_debugger: isProduction
            },
            format: {
              comments: false
            }
          },
          extractComments: false
        })
      ],
      splitChunks: {
        chunks: 'all'  // Code splitting if needed
      }
    }
  };
};
```

How to Use This Config:

1.  Save this as `webpack.custom.config.js` in your PCF project root
2.  Update your `package.json` scripts:

JSON

```
{
  "scripts": {
    "build": "pcf-scripts build --webpack webpack.custom.config.js",
    "build:analyze": "cross-env ANALYZE=true npm run build",
    "start": "pcf-scripts start"
  }
}
```

3.  Install the cross-env package if you haven’t (makes environment variables work on Windows):

Bash

```
npm install --save-dev cross-env
```

4.  Run npm run build:analyze to see your bundle breakdown

## My Personal Workflow

Here’s how I actually use all this in my day-to-day PCF development:

### During Active Development:

-   Just use `npm start` with the default config – no point in running all plugins

-   Bundle analyzer is off – I’m not worried about size yet
-   ESLint catches my typos as I code

-   Clean plugin keeps my output folder sane

### **Before Committing:**

-   Run `npm run build` to make sure production build works

-   Check that ESLint didn’t find anything serious
-   Quick smoke test of the built control

### **Before Releasing:**

-   Run `npm run build:analyze` to check bundle size

-   Review the bundle report – any surprises?
-   Make sure compression is working (check file sizes)

-   Verify all console.logs are gone from production build

### In CI/CD:

-   Fail the build if ESLint errors are found

-   Auto-generate and archive the bundle report
-   Alert if bundle size exceeds our threshold (we use 500KB as our limit)

## Lessons I Learned the Hard Way

Let me save you some pain:

### 1\. Don’t Add Every Plugin

I went through a phase where I added every webpack plugin I could find. Bad idea. Each plugin:

-   Adds to your build time

-   Creates more configuration to maintain
-   Might conflict with others

-   Could break PCF’s expectations

Start minimal, add plugins as you need them.

### 2\. Production != Development

Your dev config and production config should be different. Don’t compress in dev. Don’t run the bundle analyzer every build. Do keep ESLint and cleaning though – those help during development.

### 3\. Bundle Size Budgets Are Your Friend

Set a maximum bundle size (I use 500KB for most controls) and enforce it in CI/CD. This catches bloat before it ships. I learned this after we accidentally shipped a 2MB control. Oops.

### 4.The Fluent UI Icons Thing Is Real

If you’re using Fluent UI and haven’t read my bundle size article, your bundles are probably 10x bigger than they need to be. Fix your imports first, then worry about plugins. Seriously.

### 5\. Test Your Builds

Changed webpack config? Test the actual built control, not just the dev version. I once broke production because a plugin messed with how resources were loaded. Users were… not happy.

## How to Know It’s Working

Here’s what I measure to know my optimizations are actually helping:

### **Bundle Size:**

-   Before all optimizations: ~4MB (yikes)

-   After fixing Fluent UI imports: ~400KB
-   After compression: ~120KB gzipped

### Build Time:

-   Development rebuild: <5 seconds

-   Production build: ~30 seconds
-   Bundle analyzer run: ~45 seconds

### Load Performance:

-   Initial load in model-driven app: <1 second

-   Subsequent loads: near instant (thanks caching!)

Your numbers will vary, but the point is: measure before and after. Celebrate wins. Fix losses.

### Common Issues and Fixes

Things I’ve broken and how I fixed them:

**“My bundle is still huge!”**

-   Did you actually fix your Fluent UI imports?

-   Check the bundle analyzer report – what’s taking space?
-   Make sure `usedExports` and `sideEffects` are enabled

**“Build fails with weird errors”**

-   Clean your `node_modules` and reinstall

-   Check for plugin version conflicts
-   Make sure you’re using webpack 5 (PCF CLI should handle this)

**“ESLint is failing on everything”**

-   Run `npx eslint --init` to set up proper config

-   Add `.eslintignore` for generated files
-   Consider disabling `failOnError` until you fix existing issues

**“Compression isn’t working”**

-   Are you checking the gzipped file size?

-   Make sure your hosting environment supports gzip
-   Check that `threshold` isn’t set too high

## What’s Next?

These plugins have made my PCF development way more productive, but they’re not the end of the story. Here’s what I’m exploring next:

-   **Webpack 5 Module Federation** for shared dependencies across controls

-   **Source map optimization** for better debugging without huge files
-   **Custom loaders** for specific PCF needs

-   **Bundle splitting strategies** for large controls

If there’s interest, I might write about these too. Let me know!

## Wrapping Up

Look, webpack configuration isn’t sexy. No one’s going to give you a high-five for setting up the clean plugin. But you know what is sexy? PCF controls that load in under a second. Builds that work consistently. Production deployments that don’t make you nervous.

These plugins, combined with the bundle size optimizations from my previous article, will get you there. Start with the bundle analyzer and clean plugin. Add compression for production. Customize from there based on your needs.

And please, for the love of all that’s holy, fix your Fluent UI icon imports if you haven’t already.

## Additional Resources

**Webpack Plugins:**

-   [webpack-bundle-analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer)

-   [compression-webpack-plugin](https://www.npmjs.com/package/compression-webpack-plugin)
-   [clean-webpack-plugin](https://www.npmjs.com/package/clean-webpack-plugin)

-   [copy-webpack-plugin](https://www.npmjs.com/package/copy-webpack-plugin)
-   [terser-webpack-plugin](https://www.npmjs.com/package/terser-webpack-plugin)

-   [eslint-webpack-plugin](https://www.npmjs.com/package/eslint-webpack-plugin)

**Highly Relevant Community Blogs**

-   [PCF Controls – Tree-Shaking For Better Bundle Size](https://itmustbecode.com/pcf-controls-tree-shaking-for-better-bundle-size/)

-   [Everything you need to know about Webpack’s Bundle-Analyzer](https://dev.to/mbarzeev/everything-you-need-to-know-about-webpacks-bundle-analyzer-g0l)
-   [How to use the webpack bundle analyzer](https://blog.jakoblind.no/webpack-bundle-analyzer/)

*Got questions? Found a plugin that’s even better? Hit me up in the comments. And if this helped you, share it with your fellow PCF developers – we’re all in this together!*

*This is part of my PCF Controls Tips & Tricks series. Subscribe/follow for more practical PCF development insights!*

---
> **Note:** This page contains 3 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [PCF Controls Tips & Tricks: Stop Fighting Webpack—Here’s What Actually Works](https://aidevme.com/pcf-controls-tips-tricks-pcf-webpack-plugins-optimize-build-performance/)