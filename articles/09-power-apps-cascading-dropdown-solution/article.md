# Power Apps Cascading Dropdowns: Complete PCF Control Guide

Estimated reading time: 7 minutes

## Introduction: Solving the Cascading Dropdown Challenge

After implementing cascading dropdown solutions across dozens of Dynamics 365 projects, I noticed a recurring pattern: every organization struggled with the same problems. Custom JavaScript solutions broke easily, business rules couldn’t filter option sets, and third-party tools were expensive and inflexible.

**DependentChoice** is our answer to this challenge—a production-ready PCF control that brings intelligent, configuration-driven cascading dropdowns to Power Apps and Dynamics 365. Built with React, TypeScript, and Fluent UI, it’s designed to be both powerful and maintainable.

## The Problem with Traditional Cascading Dropdown Approaches

Building cascading dropdowns in Power Apps typically means dealing with one of these imperfect solutions:

### Traditional Approaches and Their Limitations

**Business Rules**  
Platform-native but limited—can show/hide fields but can’t filter option set values. Users still see all 195 countries regardless of the selected continent.

**Custom JavaScript**  
Provides full control but creates maintenance headaches. Every option set change requires code updates, testing, and deployment. Form-specific implementations are difficult to reuse.

**Third-Party Solutions**  
Feature-rich but expensive, with vendor lock-in and compatibility concerns during platform updates.

After implementing these approaches across multiple projects, the need for a reusable, maintainable solution became clear.

## The Solution: Configuration Over Code

The key insight was separating the pattern from the data. The logic of cascading dropdowns never changes—only the relationships between values change. By moving these relationships into JSON configuration, we could:

-   Enable non-developers to manage dependencies.

-   Eliminate code deployment for relationship changes.
-   Create a truly reusable solution.

-   Reduce maintenance overhead significantly

This became the foundation of **DependentChoice**: a PCF control configured entirely through JSON, with zero code required for typical use cases.

## Technical Architecture

### Technology Stack

**The control is built on enterprise-grade technologies:**

-   **React 16.14**: PCF platform requirement, using modern hooks and functional components.

-   **Fluent UI v9**: Microsoft’s design system for consistent, accessible UI.
-   **TypeScript 5.8**: Full type safety and improved developer experience.

-   **Webpack 5 + Terser**: Production build with 83.7% size reduction (849 KiB → 138 KiB.
-   **WebAPI Integration**: Direct metadata retrieval with intelligent caching

### Core Services Architecture

**DependentChoice follows a clean service-oriented architecture with three main components:**

#### 1\. PcfContextService

Wraps the PCF context and provides:

-   Theme detection (including GCC/DoD cloud support).

-   Form factor detection (desktop/tablet/phone).
-   Environment detection (design mode vs. runtime).

-   Security context (field-level permissions) Metadata retrieval helpers

TypeScript

```
// Automatic theme adaptation
const theme = pcfContextService.getTheme();
return (
  <FluentProvider theme={theme}>
    {/* Components automatically adapt to user's theme */}
  </FluentProvider>
);
```

#### 2\. DependencyMappingService

**Manages parent-child relationships through JSON configuration:**

-   Validates configuration structure.

-   Provides O(1) lookup for dependent values.
-   Handles multi-select parent scenarios.

-   Returns null for “show all” behavior

TypeScript

```
// Check if a dependent value is allowed
const isAllowed = mappingService.isAllowed(
  parentValue: 1,
  dependentValue: 101
); // true/false
```

#### 3\. MetadataService

**Handles all Dataverse metadata operations:**

-   Entity metadata retrieval.

-   Attribute metadata retrieval.
-   Option set metadata with caching (5-minute TTL).

-   Global option set support Reduces API calls by 90%+

TypeScript

```
// Cached metadata retrieval
const optionSet = await metadataService
  .getOptionSetMetadata('account', 'industrycode');
```

## Configuration Philosophy: JSON Over Code

DependentChoice uses a zero-code configuration approach through simple JSON:

JSON

```
{
  "mappings": [
    {
      "parentValue": 1,
      "dependentValues": [101, 102, 103]
    },
    {
      "parentValue": 2,
      "dependentValues": [201, 202, 203]
    }
  ]
}
```

This JSON structure provides:

-   Management by non-developers.

-   Storage in configuration fields (no code deployment).
-   Automatic validation with helpful error messages.

-   Version control and testing support.
-   Dynamic configuration at runtime

### Real-World Example: Geographic Hierarchy

Here’s a practical implementation of a three-level geographic hierarchy:

**Scenario**: Account form with *Continent → Country → City*

### Step 1: Create the Fields

Bash

```
Continent (Choice):
- 1: North America

- 2: Europe  
- 3: Asia

Country (Choice):
- 101: United States

- 102: Canada
- 103: Mexico

- 201: United Kingdom
- 202: France

- 203: Germany
- 301: Japan

- 302: China
- 303: India

City (Choice):
- 10101: New York

- 10102: Los Angeles
- 10201: Toronto

- 10202: Vancouver
... (and so on)
```

### Step 2: Configure Continent → Country

JSON

```
{
  "mappings": [
    {
      "parentValue": 1,
      "dependentValues": [101, 102, 103]
    },
    {
      "parentValue": 2,
      "dependentValues": [201, 202, 203]
    },
    {
      "parentValue": 3,
      "dependentValues": [301, 302, 303]
    }
  ]
}
```

### Step 3: Configure Country → City

Add another **DependentChoice** control with Country as parent and City as dependent:

JSON

```
{
  "mappings": [
    {
      "parentValue": 101,
      "dependentValues": [10101, 10102, 10103, 10104]
    },
    {
      "parentValue": 102,
      "dependentValues": [10201, 10202, 10203]
    }
    // ... additional mappings
  ]
}
```

**Result**: Users select a continent, see only relevant countries, then see only cities in the selected country. If they change the continent, the country and city selections automatically clear.

When new countries or cities are added, simply update the JSON configuration—no code deployment required.

## Performance Optimization: Bundle Size Reduction

Optimizing the bundle size was critical for production deployment. Here’s the optimization journey:

### Optimization Results

**Initial State** (Development Build):

-   Bundle size: 849 KiB.

-   Unminified code with source maps.
-   Development React libraries.

-   Full console logging

**Final State** (Production Build):

-   Bundle size: 138 KiB.

-   **83.7% reduction**.
-   Minified and optimized.

-   Power Apps Checker compliant

**Key Optimizations**

The production build configuration in `pcfconfig.json` enabled automatic Terser minification:

JSON

```
"buildMode": "production"
```

**This activated multiple optimizations:**

-   **Variable mangling**: Long names converted to single characters.

-   **Whitespace removal**: All formatting stripped.
-   **Dead code elimination**: Unused imports removed.

-   **Tree shaking**: Only used exports included.
-   **Function inlining**: Small functions merged.

-   **Module concatenation**: Scope hoisting

See more about bundle size reduction: [PCF Controls Tips & Tricks: How to Reduce Bundle Size and Improve Performance](https://aidevme.com/pcf-controls-tips-tricks-how-to-reduce-bundle-size-and-improve-performance/)

**Power Apps Checker Compliance**

The production build ensures:

-   No `eval()` usage.

-   Minified output under 200 KB threshold.
-   No security vulnerabilities.

-   Compatible with all Power Apps environments

## Built-in Configuration Validation

**DependentChoice** includes comprehensive validation to prevent configuration errors:

### Validation Checks

-   **Invalid JSON syntax** → Line number and syntax error details.

-   **Missing “mappings” array** → Expected structure shown.
-   **Non-numeric values** → Data type requirements explained.

-   **Duplicate parent values** → Conflict location identified.
-   **Invalid array structures** → Correct format provided

### User-Friendly Error Messages

When validation fails, users see detailed feedback:

Bash

```
 Configuration Error

Your configuration has validation errors:

- Line 3: "parentValue" must be a number (found: "1" as string)

- Line 8: Duplicate parentValue 1 found at index 2

Expected format:
{
  "mappings": [
    { "parentValue": 1, "dependentValues": [11, 12] }
  ]
}

Need help? Check the documentation: [link]
```

This validation system enables non-developers to configure the control independently while preventing common mistakes.

### Performance Characteristics

**Production Metrics**

-   **Initial Load**: <200ms (including metadata retrieval).

-   **Filter Operation**: <50ms (instant user feedback).
-   **Metadata Cache TTL**: 5 minutes (configurable).

-   **Memory Footprint**: ~2MB (React + Fluent UI).
-   **Bundle Size**: 138 KiB (minified + gzipped)

**Scalability Testing**

**Successfully tested with:**

-   100+ option values per field.

-   10+ dependency mappings.
-   10 concurrent controls on a single form.

-   Multi-select parent scenarios

## Development Lessons Learned

### Successful Approaches

1.  **TypeScript First**: Type safety caught bugs during compilation rather than runtime.
2.  **Service Architecture**: Clean separation of concerns enabled easier testing and maintenance.
3.  **JSON Configuration**: Enabled non-developer management of dependencies.
4.  **Production Build Configuration**: 83.7% size reduction was essential for deployment.
5.  **Automated Documentation**: CI/CD pipeline keeps wiki synchronized with code

### Technical Challenges Addressed

1.  **React 16 Requirement**: PCF platform locked to older React version, required modern patterns within constraints.
2.  **Fluent UI Compatibility**: Careful version selection for React 16 compatibility.
3.  **Bundle Optimization**: Production webpack configuration was critical for size reduction.
4.  **Multi-Select Parents**: Complex logic for handling array parent values.
5.  **Metadata Caching**: Balanced performance optimization with data freshness (5-minute TTL)

### Best Practices

1.  Validate all configuration before runtime execution.
2.  Implement aggressive metadata caching with appropriate TTL.
3.  Clear dependent field values automatically when parent changes.
4.  Use TypeScript for all development work Test with large datasets (100+ values) early in development.
5.  Support multi-select scenarios from initial design Implement internationalization from project start (18 languages included)

## Open Source Contribution

DependentChoice is fully open source under the MIT license, enabling:

-   Community bug detection and rapid fixes.

-   Diverse feature requests from real-world use cases.
-   Contributor-provided language translations (18 languages).

-   Enterprise source code review and security audits.
-   Collaborative improvement from global developers

**Repository**: [github.com/aidevme/dependent-choice](https://github.com/aidevme/dependent-choice)

### Contributing

-   Report bugs via [GitHub Issues](https://github.com/aidevme/dependent-choice/issues).

-   Suggest features in [Discussions](https://github.com/aidevme/dependent-choice/discussions).
-   Submit pull requests following contribution guidelines.

-   Improve documentation via wiki edits.
-   Add language translations for international support

## Getting Started: Your First Implementation in 10 Minutes

**Ready to stop fighting with cascading dropdowns? Here’s how to get started:**

### Step 1: Download and Install (2 minutes)

1.  Go to [GitHub releases](https://github.com/aidevme/dependent-choice/releases).
2.  Download the latest solution (currently v1.0.0.14).
3.  Import into your Dynamics 365 or Power Apps environment.
4.  Wait for the import to complete

### Step 2: Add to Your Form (3 minutes)

-   Open your form in the form designer.

-   Select the field you want to make dependent (e.g., “Country”).
-   Click “Components” in the ribbon Choose “DependentChoice” from the list.

-   In the properties panel, bind the “Parent Choice” to your parent field (e.g., “Continent”)

### Step 3: Configure the Mappings (5 minutes)

1.  In the “Configuration JSON” property, paste your mappings:
2.  Save and publish your form
3.  Test it out!

JSON

```
{
  "mappings": [
    {
      "parentValue": 1,
      "dependentValues": [101, 102, 103]
    },
    {
      "parentValue": 2,
      "dependentValues": [201, 202, 203]
    }
  ]
}
```

### What Happens Now

-   User selects parent value → Dependent dropdown filters instantly.

-   User changes parent value → Dependent value clears automatically.
-   User sees only relevant options → No scrolling through irrelevant choices.

-   Configuration updates require no code deployment

## Conclusion

DependentChoice demonstrates how the Power Apps Component Framework can extend platform capabilities while maintaining native user experience. By applying modern development practices—TypeScript, React, service architecture, and automated CI/CD—we’ve created a production-ready control that solves a common business challenge efficiently.

## Quick Reference Links

-   **GitHub Repository**: [aidevme/dependent-choice](https://github.com/aidevme/dependent-choice)

-   Latest Release: [Releases · aidevme/dependent-choice](https://github.com/aidevme/dependent-choice/releases/tag/v1.0.17)
-   Full Documentation: [AIDevMe Dependent Choice Wiki](https://github.com/aidevme/dependent-choice/wiki)

-   Community Support: [AIDevMe Dependent Choice Discussion](https://github.com/aidevme/dependent-choice/discussions)
-   Issue Tracking: [AIDevMe Dependent Choice Issues](https://github.com/aidevme/dependent-choice/issues)

---

*Found this helpful? Star the repository on GitHub and share your implementation story in the discussions.*

---

## Frequently Asked Questions

### Can I use this with custom tables and custom choices?

Absolutely. It works with any choice field (option set), whether standard or custom.

### How do I handle scenarios where I want “All” as an option?

Don’t include a mapping for that parent value. The control will show all options when no mapping exists.

### *Related*

---
> **Note:** This page contains 3 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [How I Built a Smart Cascading Dropdown Solution That Transformed Our Power Apps Forms](https://aidevme.com/power-apps-cascading-dropdown-solution/)