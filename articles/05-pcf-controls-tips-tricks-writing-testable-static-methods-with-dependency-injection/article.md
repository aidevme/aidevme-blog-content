# PCF Tips & Tricks: Writing Testable Static Methods

Estimated reading time: 24 minutes

## Introduction: The Real-World Challenge

When building the Azure Maps Address Autocomplete PCF control, I encountered a common development challenge: determining when the control is running in different Power Platform environments. Specifically, I needed to detect two distinct modes: **Design Mode** (when users configure the control in the Power Apps maker portal at make.powerapps.com) and **Authoring Mode** (when developers edit forms or apps in the model-driven app designer). Initially, I implemented both detection methods as static utility functions in my [PcfContextService](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) class, thinking they would serve similar purposes with similar characteristics. However, when I started writing unit tests with Jest and JSDOM, I discovered a critical problem that changed my perspective on code design: one method was fully testable with comprehensive coverage, while the other was completely untestable.

**Why I Chose [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) as the Success Case:**

The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method demonstrates the **right way** to write testable code because it relies on **context parameters** passed into the method rather than accessing global browser state. The PCF framework provides [context.mode.isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) as an official (though undocumented) property that indicates whether the control is currently in the form designer or app designer editing experience in model-driven apps. I’ve read about detecting authoring mode and its practical [David Rivard](https://www.linkedin.com/in/davidrivard/)‘s article: [PCF Controls Tips & Tricks: How to Detect Authoring Mode](https://itmustbecode.com/pcf-controls-tips-tricks-how-to-detect-authoring-mode/). This method follows **dependency injection principles** where all required data comes from parameters, making it inherently mockable and testable. It produces **predictable, reproducible behavior** in any environment, whether running in production, development, or test scenarios. In contrast, `isInDesignMode()` depends on `globalThis.location.href` – a browser global object that JSDOM cannot reliably mock, making it inherently untestable in standard unit test environments without complex workarounds.

This article explores why these two seemingly similar methods have vastly different testability characteristics and demonstrates how dependency injection makes code both more testable and more maintainable. You’ll learn practical techniques for writing PCF control code that can be thoroughly tested, ensuring higher quality and fewer runtime bugs. By the end, you’ll understand how to design methods that embrace testability from the start rather than retrofitting tests onto poorly designed code.

## The Two Approaches: A Side-by-Side Comparison

## Method 1: `isInDesignMode()` – The Untestable Approach

### Implementation Details

The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method solves a similar problem to `isInDesignMode()` but with a fundamentally different architectural approach. Instead of checking browser URLs, it examines the [context.mode.isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) property provided by the PCF framework. This property is part of the (undocumented) PCF context API that indicates whether the control is currently in the authoring/editing experience within the form designer or app designer for model-driven apps. As I detailed in my article [How to Detect Authoring Mode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), the distinction is important: design mode refers to configuring controls in the Power Apps maker portal (the configuration experience), while authoring mode refers to the design-time editing experience when developers are actively building forms or customizing apps within model-driven apps. This detection is crucial for providing appropriate design-time experiences, such as displaying placeholder content or mock data while developers are building forms.

The implementation is remarkably simple and elegant. It first checks if the [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) parameter exists (defensive programming against null/undefined), then accesses the [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) property through a type assertion since this property isn’t included in the official TypeScript definitions. The explicit comparison to `true` ensures that only the boolean `true` value triggers the authoring mode detection, preventing truthy values like `1`, `"true"`, or `{}` from being mistakenly interpreted. If the context is missing or the property is `false` or `undefined`, the method safely returns `false`, providing a sensible default behavior. Understanding when and how to use this property can significantly improve the user experience for developers building with your controls.

The method exemplifies **pure function design**: given the same input (context object), it always produces the same output (boolean result). There are no side effects, no external state dependencies, and no hidden inputs. The function’s behavior is entirely determined by its parameters, making it predictable, debuggable, and most importantly, testable. You can call this function a thousand times with the same context object and get identical results every single time, which is exactly what unit tests require.

The method follows the **dependency injection pattern** perfectly. Instead of reaching out into the global environment to fetch the data it needs, all required data is injected through the [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) parameter. This inversion of control gives the caller (or test framework) complete authority over what data the function receives. In production, the PCF framework provides the real context object with live data. In tests, we provide a mock context object with controlled data. The function doesn’t know or care about the difference – it simply processes whatever context it receives. For more details on the practical applications and implementation patterns, refer to David Rivard’s comprehensive guide on [detecting authoring mode in PCF controls](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html).

### Why It Can’t Be Tested

The fundamental problem with testing `isInDesignMode()` is that it depends on browser global state that test environments cannot reliably control. When running Jest tests with JSDOM (JavaScript implementation of web standards), the `location` object exists but with severe limitations compared to real browsers. JSDOM’s `location` object is designed to be read-only in many scenarios to prevent tests from accidentally affecting each other or creating unpredictable state. While you can technically set `jsdom.reconfigure()` or use workarounds like `delete window.location` and recreate it, these approaches are fragile, error-prone, and create brittle tests that break with JSDOM version updates.

Even if we could successfully mock `globalThis.location.href`, we’d face another problem: our tests wouldn’t actually validate the real-world behavior of the method. The whole point of unit testing is to ensure code works correctly in isolation, but when we mock global state, we’re testing our mocks rather than the actual implementation. If the browser’s location API changes, or if JSDOM’s implementation diverges from real browsers, our passing tests might give us false confidence while the production code fails. This disconnect between test environment and production environment undermines the value of the tests.

Another critical issue is test isolation and parallelization. Modern test runners like Jest execute tests in parallel to improve performance, but when tests manipulate global state, they can interfere with each other in unpredictable ways. If one test sets `location.href` to “make.powerapps.com” and another sets it to “dynamics.com”, the execution order becomes critical, and tests might pass or fail non-deterministically. This is exactly the kind of flaky test behavior that erodes developer confidence in the test suite. Rather than helping catch bugs, these tests become maintenance burdens that developers eventually skip or disable.

### JSDOM Limitations with Global Objects

JSDOM is an excellent tool for testing DOM manipulation and React components, but it has inherent limitations when dealing with browser APIs that involve navigation, location, and window management. The JSDOM maintainers intentionally restrict certain operations to prevent tests from breaking out of their sandbox or creating security vulnerabilities. The `location` object, in particular, is heavily restricted because allowing arbitrary URL changes could cause tests to make real network requests, navigate away from the test page, or interact with the file system in unexpected ways.

When you try to set `window.location.href = "https://make.powerapps.com"` in JSDOM, one of several things might happen depending on the JSDOM version and configuration. In some versions, the assignment is silently ignored, and the location remains unchanged. In others, it throws a `TypeError` about setting a read-only property. In still others, it triggers JSDOM’s navigation simulation, which loads the URL (if it’s a data URI or file URI), potentially causing your test to hang or fail. This inconsistent behavior across versions makes it nearly impossible to write stable tests that work reliably across different development environments and CI/CD pipelines.

The workarounds for these limitations are complex and introduce their own problems. Some developers use `Object.defineProperty(window, 'location', { value: { href: 'test-url' }, writable: true })` to override the location object entirely, but this creates a fake location object that doesn’t behave like the real browser API. Others use libraries like [jest-location-mock](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) that intercept location access, but this adds another dependency and abstraction layer that can fail in subtle ways. The fundamental issue remains: you’re fighting against the testing framework’s design rather than writing naturally testable code.

Here’s what the skipped test looks like in our test file:

TypeScript

```
describe.skip('isInDesignMode (static)', () => {
  it('should return true for make.powerapps.com', () => {
    // Cannot reliably test due to JSDOM location.href limitations
    expect(true).toBe(true); // Placeholder
  });

  it('should return false for dynamics.com runtime', () => {
    // Cannot reliably test due to JSDOM location.href limitations
    expect(true).toBe(true); // Placeholder
  });
});
```

The [describe.skip](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) clearly indicates that these tests are not executable, leaving a gap in our test coverage that we must accept or work around through integration testing.

## Method 2: `isAuthoringMode()` – The Untestable Approach

### Implementation Details

The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method solves a similar problem to `isInDesignMode()` but with a fundamentally different architectural approach. Instead of checking browser URLs, it examines the [context.mode.isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) property provided by the PCF framework. This property is part of the (undocumented) PCF context API that indicates whether the control is currently being edited in Canvas App Studio, which is different from the maker portal where model-driven apps are configured. The distinction is important: design mode refers to configuring controls in the Power Apps maker portal, while authoring mode refers to actively editing a canvas app in the studio.

The implementation is remarkably simple and elegant. It first checks if the [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) parameter exists (defensive programming against null/undefined), then accesses the [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) property through a type assertion since this property isn’t included in the official TypeScript definitions. The explicit comparison to `true` ensures that only the boolean `true` value triggers the authoring mode detection, preventing truthy values like `1`, `"true"`, or `{}` from being mistakenly interpreted. If the context is missing or the property is `false` or `undefined`, the method safely returns `false`, providing a sensible default behavior.

This method exemplifies **pure function design**: given the same input (context object), it always produces the same output (boolean result). There are no side effects, no external state dependencies, and no hidden inputs. The function’s behavior is entirely determined by its parameters, making it predictable, debuggable, and most importantly, testable. You can call this function a thousand times with the same context object and get identical results every single time, which is exactly what unit tests require.

The method follows the **dependency injection pattern** perfectly. Instead of reaching out into the global environment to fetch the data it needs, all required data is injected through the [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) parameter. This inversion of control gives the caller (or test framework) complete authority over what data the function receives. In production, the PCF framework provides the real context object with live data. In tests, we provide a mock context object with controlled data. The function doesn’t know or care about the difference – it simply processes whatever context it receives.

### Why It Works Perfectly in Tests

Testing [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) is straightforward because we have complete control over the input data through the [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) parameter. In our test setup, we create a mock context object using a helper function that generates a properly structured PCF context with all required properties. We can then easily set the [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) property to any value we want to test: `true`, `false`, `undefined`, or even omit it entirely. Each test case is isolated, deterministic, and fast because there’s no global state to manage or reset between tests.

Here’s our test setup using a mock context:

TypeScript

```
describe('isAuthoringMode (static)', () => {
  it('should return true when context.mode.isAuthoringMode is true', () => {
    const mockContext = createMockContext({});
    (mockContext.mode as any).isAuthoringMode = true;

    const result = PcfContextService.isAuthoringMode(mockContext);

    expect(result).toBe(true);
  });

  it('should return false when context.mode.isAuthoringMode is false', () => {
    const mockContext = createMockContext({});
    (mockContext.mode as any).isAuthoringMode = false;

    const result = PcfContextService.isAuthoringMode(mockContext);

    expect(result).toBe(false);
  });
});
```

The test structure follows the **Arrange-Act-Assert** pattern clearly. In the Arrange phase, we create a mock context and set the [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) property to the desired test value. In the Act phase, we call the method with our prepared input. In the Assert phase, we verify that the output matches our expectations. This clear separation makes tests easy to read, understand, and maintain. Any developer can look at these tests and immediately understand what behavior is being verified without needing to understand complex mocking libraries or global state manipulation.

The tests run in milliseconds because they’re pure unit tests with no I/O, no network calls, no file system access, and no DOM manipulation. They can be executed hundreds of times during development without slowing down the feedback loop. When these tests fail, they fail for exactly one reason: the implementation logic changed. There are no false positives from environmental issues, timing problems, or state leakage between tests. This reliability is what makes test-driven development (TDD) practical and effective.

### Complete Test Coverage

We can achieve 100% branch coverage for [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) because every code path is testable. The method has multiple conditional branches: checking if context exists, checking if [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) is exactly `true`, and handling all other cases. Our test suite covers all these scenarios systematically, ensuring that the method behaves correctly under every possible input condition. This comprehensive coverage gives us confidence that the method will work correctly in production regardless of what values the PCF framework provides.

Here’s the complete test suite with all edge cases:

TypeScript

```
describe('isAuthoringMode (static)', () => {
  it('should return true when context.mode.isAuthoringMode is true', () => {
    const mockContext = createMockContext({});
    (mockContext.mode as any).isAuthoringMode = true;

    const result = PcfContextService.isAuthoringMode(mockContext);

    expect(result).toBe(true);
  });

  it('should return false when context.mode.isAuthoringMode is false', () => {
    const mockContext = createMockContext({});
    (mockContext.mode as any).isAuthoringMode = false;

    const result = PcfContextService.isAuthoringMode(mockContext);

    expect(result).toBe(false);
  });

  it('should return false when context.mode.isAuthoringMode is undefined', () => {
    const mockContext = createMockContext({});
    (mockContext.mode as any).isAuthoringMode = undefined;

    const result = PcfContextService.isAuthoringMode(mockContext);

    expect(result).toBe(false);
  });

  it('should return false when context is not provided', () => {
    const result = PcfContextService.isAuthoringMode();

    expect(result).toBe(false);
  });

  it('should return false when context is undefined', () => {
    const result = PcfContextService.isAuthoringMode(undefined);

    expect(result).toBe(false);
  });
});
```

These five test cases cover every possible scenario: the happy path where authoring mode is active, the normal runtime case where it’s explicitly `false`, the edge case where the property is `undefined`, and the defensive cases where no context is provided at all. When all five tests pass, we have mathematical certainty that the method will behave correctly for any input it might receive in production. This level of confidence is only possible when code is designed for testability from the start.

The test results from our actual test run confirm complete success:

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/01/pcf-controls-tips-tricks-writing-testable-static-methods-with-dependency-injection-test-result-1.png?resize=684%2C214&ssl=1)

All five tests pass consistently, every single time, with zero flakiness. This reliability is the hallmark of well-designed, testable code.

## The Core Difference: Global State vs. Dependency Injection

### What Makes Code Testable?

Code testability fundamentally depends on two characteristics: **determinism** and **isolation**. Deterministic code produces the same output for the same input every time, without being influenced by external factors like time, random numbers, global variables, or network state. Isolated code doesn’t depend on or affect other parts of the system, allowing it to be tested independently without complex setup or teardown procedures. When code violates either of these principles, testing becomes exponentially more difficult, often requiring elaborate mocking frameworks, test fixtures, or integration test environments.

The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method is deterministic because its output depends solely on the [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) parameter. If you call it with a context where [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) is `true`, it returns `true` – every single time, on every machine, in every environment. The `isInDesignMode()` method, however, is non-deterministic from a testing perspective because its output depends on `globalThis.location.href`, which changes based on where and how the test runs. The same code might return different results in a browser test versus a JSDOM test versus a headless Chrome test.

Isolation is equally important. The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method is perfectly isolated – it doesn’t read from or write to any shared state. You can call it a million times in parallel without any race conditions or interference between calls. The `isInDesignMode()` method violates isolation by reading from `globalThis`, a shared resource that all code in the JavaScript runtime can access. If multiple tests or production code paths try to manipulate `location.href` simultaneously, they interfere with each other unpredictably.

Good testable code also exhibits **low coupling** – it doesn’t depend on many external systems or libraries. The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method depends only on the structure of the PCF context object, which is defined by the framework contract. The `isInDesignMode()` method depends on the browser’s location API, the JSDOM implementation, and the assumption that maker portal URLs remain stable across Microsoft’s cloud environments. More dependencies mean more things that can break and more things you need to mock in tests.

Finally, testable code follows the **single responsibility principle**. Each function should do one thing and do it well. Both methods follow this principle reasonably well – they each answer a specific question about the runtime environment. However, `isInDesignMode()` mixes two responsibilities: determining the current URL (environment concern) and comparing it against a pattern list (business logic). These could be separated to improve testability, but that’s a topic for the refactoring section.

### The Dependency Injection Advantage

Dependency injection (DI) is a design pattern where a function or class receives its dependencies from external callers rather than creating or accessing them directly. This pattern is the cornerstone of testable code because it allows test code to inject mock dependencies while production code injects real dependencies. The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method uses DI perfectly: it receives the [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) dependency as a parameter, giving the caller complete control over what data the method processes.

The benefits of DI extend beyond testability. Code that uses DI is more flexible because you can swap implementations without changing the consuming code. For example, if Microsoft changes how [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) is detected in a future PCF framework version, we can create an adapter that provides the old interface while reading the new property, without changing every call site. This flexibility is impossible with the `isInDesignMode()` approach because the dependency on `globalThis.location` is hardcoded into the implementation.

DI also improves code documentation and readability. When you see a method signature like [isAuthoringMode(context?: ComponentFramework.Context)](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), you immediately understand that the method needs PCF context to do its work. The dependencies are explicit and visible in the signature. With `isInDesignMode()`, you have to read the implementation to discover that it depends on browser location – the dependency is hidden and implicit.

Here’s a comparison of how the two methods handle their dependencies:

TypeScript

```
//  Bad: Hidden dependency on global state
public static isInDesignMode(context?: ComponentFramework.Context<IInputs>): boolean {
  const currentUrl = globalThis.location.href; // Accessing global state
  return designModeUrls.some((url) => currentUrl.includes(url));
}

//  Good: Explicit dependency through parameter
public static isAuthoringMode(context?: ComponentFramework.Context<IInputs>): boolean {
  if (context && (context.mode as any).isAuthoringMode === true) {
    return true;
  }
  return false;
}
```

The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) method practices what’s called **pure function design**: no side effects, no hidden inputs or outputs, just a straightforward transformation of input to output. Pure functions are inherently testable because they’re predictable and isolated. They’re also easier to reason about, debug, and maintain because their behavior is transparent and self-contained.

DI doesn’t just help with unit testing – it also enables integration testing, contract testing, and behavior-driven development. When you can inject different implementations of a dependency, you can test how your code handles various scenarios: network failures, invalid data, boundary conditions, and exceptional cases. This comprehensive testing approach catches bugs that unit tests alone might miss, leading to more robust and reliable software.

## Real Test Results: Proof in Action

## Skipped Tests for `isInDesignMode()`

Our test suite for [PcfContextService](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) includes a section for `isInDesignMode()` that is entirely skipped using Jest’s [describe.skip()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) function. This skipped test block serves as documentation of the testing gap and a reminder of the technical debt we’ve accepted. Each placeholder test acknowledges what we *would* test if the method were testable: verifying that maker portal URLs return `true` and that runtime Dynamics 365 URLs return `false`. These tests exist in the codebase but never execute, contributing to our overall test coverage gap.

Here’s the actual code from our test file:

TypeScript

```
describe.skip('isInDesignMode (static)', () => {
  it('should return true for make.powerapps.com', () => {
    // Cannot reliably test due to JSDOM location.href limitations
    expect(true).toBe(true); // Placeholder
  });

  it('should return false for dynamics.com runtime', () => {
    // Cannot reliably test due to JSDOM location.href limitations
    expect(true).toBe(true); // Placeholder
  });
});
```

The comments clearly explain why these tests are skipped: JSDOM’s limitations make reliable testing impossible without complex, fragile workarounds. We could technically use `jsdom.reconfigure()` or `Object.defineProperty` hacks to mock `location.href`, but those approaches create brittle tests that break frequently and don’t accurately represent real browser behavior. The team decision was to skip these tests and rely on manual testing and integration tests to verify `isInDesignMode()` functionality.

This situation is frustrating for developers who value comprehensive test coverage. We’ve essentially given up on testing a critical piece of functionality that determines how the control behaves in different environments. If someone refactors `isInDesignMode()` and accidentally breaks it, our automated tests won’t catch the regression. We’ll only discover the problem when a user reports that the control displays incorrectly in the maker portal, by which point the code has already been deployed to production.

The skipped tests also affect our code coverage metrics. Most organizations have code coverage targets (e.g., “80% of code must be covered by tests”), and skipped tests create coverage gaps that require explanation and justification. Team leads and quality assurance managers rightfully question why certain code isn’t tested, and the answer “it’s not testable” often leads to deeper discussions about code quality and design patterns. These conversations are valuable but could be avoided entirely by writing testable code from the start.

### Five Passing Tests for [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)

In stark contrast to the skipped `isInDesignMode()` tests, the [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) test suite includes five fully functional, passing tests that execute on every test run. These tests provide comprehensive coverage of all code branches and edge cases, giving us confidence that the method works correctly under all possible conditions. The tests are fast, reliable, and require no special setup or teardown – they’re exactly what unit tests should be.

Here’s the output from our actual test run:

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/01/pcf-controls-tips-tricks-writing-testable-static-methods-with-dependency-injection-test-result-2.png?fit=674%2C366&ssl=1)

Notice that all five [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) tests complete in just 1-3 milliseconds each – this is the speed advantage of pure unit tests that don’t touch I/O or global state. These tests run so quickly that developers can execute the entire test suite dozens of times per hour during development without any productivity impact. The fast feedback loop encourages test-driven development and helps catch bugs immediately after they’re introduced.

The test descriptions are clear and specific, making it easy to understand what’s being verified: “should return true when context.mode.isAuthoringMode is true” leaves no ambiguity about the expected behavior. When one of these tests fails (which only happens when we intentionally change the implementation), the failure message immediately tells us what condition broke. We don’t have to dig through stack traces, debug complex mocking logic, or wonder if the test itself is flawed – the direct relationship between input and output makes debugging trivial.

These passing tests also serve as living documentation for the method’s behavior. New team members can read the tests to understand exactly how [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) should behave without studying the implementation code. The tests document the contract: given these inputs, expect these outputs. This documentation is always up-to-date because if the implementation changes without updating the tests, the tests fail. Unlike written documentation that becomes stale and outdated, executable tests must stay synchronized with the code they verify.

## Key Takeaways: Design Principles for Testable PCF Code

### Prefer Parameters Over Globals

The single most important lesson from this comparison is: **always prefer passing data through parameters rather than accessing global variables**. When you need information to make a decision, ask for it explicitly through your function signature instead of reaching into the global environment to fetch it. This principle applies to all global state: `window`, `document`, `localStorage`, `globalThis`, `process.env`, and singleton objects. Every global access makes your code harder to test, harder to reason about, and harder to reuse in different contexts.

The reflex to use globals is understandable – they’re convenient and require less typing than threading parameters through multiple function calls. However, this convenience comes at a steep cost in maintainability and testability. When you access `globalThis.location.href` directly, you create an implicit dependency that’s invisible in your function signature. Future maintainers (including yourself in six months) won’t know the function depends on the location unless they read every line of the implementation.

If you absolutely must work with global state, extract it at the boundaries of your system and pass it inward as parameters. For example, instead of reading `location.href` deep inside your business logic, read it once at the entry point (like a React component or PCF control’s `updateView()` method) and pass the URL down to methods that need it. This approach, called “pushing I/O to the edges,” keeps your core business logic pure and testable while isolating the global state access to a small, well-defined area.

Here’s a comparison showing the improvement:

TypeScript

```
//  Bad: Direct global access deep in business logic
function checkEnvironment(): string {
  const url = globalThis.location.href;
  if (url.includes('make.powerapps.com')) return 'design';
  return 'runtime';
}

//  Good: Global access at boundary, pass as parameter
function checkEnvironment(url: string): string {
  if (url.includes('make.powerapps.com')) return 'design';
  return 'runtime';
}

// In your React component or PCF control:
const environment = checkEnvironment(window.location.href);
```

This refactoring makes `checkEnvironment()` testable while keeping the same functionality. The global access still happens, but it’s isolated to the entry point where it’s expected and acceptable.

### Leverage PCF Context Properties

The PCF framework provides a rich [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) object filled with useful properties that tell you about the runtime environment, user settings, form state, and control configuration. Always prefer using these official (or undocumented but stable) context properties over implementing your own detection mechanisms. The framework maintainers at Microsoft have already solved common problems like environment detection, and their solutions are tested across millions of deployments in production environments worldwide.

The [context.mode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) object is particularly valuable for PCF control development. It includes properties like [isControlDisabled](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), [isVisible](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), [allocatedHeight](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), [allocatedWidth](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), and (unofficially) [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html). These properties give you authoritative information about the control’s state without needing to guess or infer from indirect signals. Using framework-provided properties also ensures your control stays compatible with future framework versions, as Microsoft is incentivized to maintain backward compatibility for properties that controls depend on.

When you discover undocumented properties like [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), document them clearly in your code with TSDoc comments explaining what they do and why you’re using them. Include type assertions (like [(context.mode as any).isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)) to acknowledge that the property isn’t officially typed, making it clear to reviewers and maintainers that you’re intentionally using an undocumented API. This transparency helps your team make informed decisions about the risk-reward tradeoff.

Here’s how we documented the [isAuthoringMode](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) usage:

TypeScript

```
/**
 * Determines if the control is currently running in authoring mode (Canvas App Studio).
 * 
 * @param context - The PCF context object
 * @returns True if in authoring mode, false otherwise
 * 
 * @remarks
 * This method uses the undocumented `context.mode.isAuthoringMode` property.
 * While not officially typed, it's been stable across PCF versions.
 */
public static isAuthoringMode(
  context?: ComponentFramework.Context<IInputs>
): boolean {
  if (context && (context.mode as any).isAuthoringMode === true) {
    return true;
  }
  return false;
}
```

The context object also provides methods for calling Web API, navigation, user settings retrieval, and resource string localization. Familiarize yourself with all the capabilities of [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) to avoid reinventing functionality that the framework already provides.

###  Make Dependencies Explicit

Every function has inputs and outputs. Explicit inputs come through parameters; implicit inputs come from global state, instance variables, or closures. Explicit outputs come through return values; implicit outputs go to global state, instance variables, or side effects. Testable code maximizes explicit inputs and outputs while minimizing implicit ones. When you look at a function signature, you should be able to understand what data it needs (parameters) and what data it produces (return type) without reading the implementation.

The [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) signature clearly communicates its contract: [(context?: ComponentFramework.Context): boolean](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html). This tells readers: “Give me an optional PCF context, and I’ll give you a boolean answer.” There are no hidden inputs or outputs. The `isInDesignMode()` signature lies: [(context?: ComponentFramework.Context): boolean](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) suggests it uses the context parameter, but it actually ignores it and reads from `globalThis` instead. This mismatch between signature and implementation violates the principle of least surprise.

Making dependencies explicit has benefits beyond testability. It improves code review because reviewers can see exactly what data flows into and out of each function. It enables better static analysis because tools can trace data dependencies through the codebase. It facilitates refactoring because you can change a function’s implementation without affecting callers as long as you maintain the same explicit contract. And it improves debugging because you can inspect exactly what inputs led to specific outputs without worrying about hidden state.

When designing functions, ask yourself: “What data does this function absolutely need to do its job?” Then ensure that all required data comes through parameters. If you find yourself accessing global state, ask: “Could this be passed as a parameter instead?” More often than not, the answer is yes, and making that change will immediately improve your code’s testability and quality.

## Refactoring `isInDesignMode()` for Testability (Optional Improvement)

While we’ve accepted that the current `isInDesignMode()` implementation isn’t testable, we don’t have to live with this limitation forever. The method can be refactored to follow the same dependency injection pattern as [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), making it fully testable without sacrificing its production functionality. The key insight is to separate the URL-fetching concern (inherently tied to global state) from the URL-checking logic (pure business logic that’s perfectly testable).

Here’s a refactored version that accepts the URL as an optional parameter:

TypeScript

```
/**
 * Determines if the control is running in design mode (Power Apps maker portal).
 * 
 * @param url - Optional URL to check; defaults to current browser location
 * @param context - The PCF context (unused but kept for API consistency)
 * @returns True if running in a maker portal, false otherwise
 */
public static isInDesignMode(
  url?: string,
  context?: ComponentFramework.Context<IInputs>
): boolean {
  const designModeUrls = [
    "make.powerapps.com",
    "make.gov.powerapps.us",
    "make.high.powerapps.us",
    "make.apps.appsplatform.us",
    "localhost",
  ];
  
  const currentUrl = url ?? globalThis.location.href;
  return designModeUrls.some((designUrl) => currentUrl.includes(designUrl));
}
```

This refactored version maintains backward compatibility – existing code that calls `isInDesignMode()` or [isInDesignMode(context)](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) continues working exactly as before because the first parameter defaults to `globalThis.location.href`. However, test code can now inject specific URLs to verify the detection logic without touching global state. This is a win-win solution that preserves production behavior while enabling comprehensive testing.

Here’s how the tests would look with this refactored version:

TypeScript

```
describe('isInDesignMode (static)', () => {
  it('should return true for make.powerapps.com', () => {
    const result = PcfContextService.isInDesignMode('https://make.powerapps.com/environments/12345');
    expect(result).toBe(true);
  });

  it('should return true for GCC environment', () => {
    const result = PcfContextService.isInDesignMode('https://make.gov.powerapps.us/environments/12345');
    expect(result).toBe(true);
  });

  it('should return false for dynamics.com runtime', () => {
    const result = PcfContextService.isInDesignMode('https://org.crm.dynamics.com/main.aspx');
    expect(result).toBe(false);
  });

  it('should default to globalThis.location.href when URL not provided', () => {
    // This test would still be skipped or use integration testing
    // because it depends on global state
  });
});
```

Three of the four tests are now fully executable and testable. Only the default parameter behavior test remains challenging, but we’ve isolated the untestable global access to a single edge case rather than having the entire method untestable. This is a massive improvement in test coverage and confidence.

The refactoring demonstrates an important principle: you can often make code testable through incremental improvements rather than complete rewrites. By adding a single optional parameter with a sensible default, we transformed an untestable method into a mostly testable one. This technique applies broadly across PCF development and web development in general – whenever you see global state access, ask yourself: “Could this be an optional parameter with a default value?” If yes, you’ve found an easy path to better testability.

## Conclusion: Write Code That Can Be Tested

The journey from untestable to testable code isn’t about learning complex testing frameworks or mocking libraries – it’s about making better design decisions at the moment you write each function. When you sit down to implement a method like `isInDesignMode()` or [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html), you face a choice: reach for global state (easy now, painful later) or design for dependency injection (slightly more thought upfront, smooth sailing forever). The extra 30 seconds of thought about “how would I test this?” pays dividends for months and years afterward.

Testable code isn’t just about passing automated tests – it’s about writing code that’s easier to understand, maintain, debug, and evolve. When you write functions that accept all their dependencies as parameters and produce outputs solely through return values, you create code that’s modular, reusable, and resilient to change. These functions work equally well in production, tests, debugging sessions, and interactive development environments because they don’t depend on hidden state or environmental factors.

The contrast between `isInDesignMode()` and [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) illustrates a broader principle that applies throughout software engineering: **design choices have long-term consequences**. Choosing to read from `globalThis.location.href` seemed harmless when writing `isInDesignMode()`, but it created technical debt that we’re still paying months later through skipped tests and coverage gaps. Choosing to read from the injected [context](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) parameter in [isAuthoringMode()](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) created an asset that keeps delivering value through reliable, fast tests that catch bugs before they reach production.

As you continue developing PCF controls, make testability a first-class concern alongside functionality and performance. Before writing a function, ask: “How would I test this?” If the answer involves complex mocking, global state manipulation, or environmental dependencies, reconsider your design. Can you accept dependencies through parameters? Can you extract pure logic from impure I/O? Can you push side effects to the boundaries of your system? The answers to these questions will guide you toward better, more testable code.

Remember that the goal isn’t 100% test coverage for its own sake – some code legitimately can’t or shouldn’t be unit tested (like UI rendering logic that requires visual verification). The goal is to design the majority of your business logic as pure, testable functions that can be verified automatically. When you achieve this, you gain confidence in your code, velocity in your development, and peace of mind in your deployments. That’s the real value of writing testable code.

## Resources and Further Reading

For developers who want to deepen their understanding of testable code design and PCF development best practices, here are valuable resources that expand on the concepts discussed in this article:

**Official Microsoft Documentation:**

-   [PCF Controls Tips & Tricks: How to Detect Authoring Mode](https://itmustbecode.com/pcf-controls-tips-tricks-how-to-detect-authoring-mode/) – Detailed guide on detecting and leveraging authoring mode in PCF controls for better design-time experiences

-   [Power Apps Component Framework API Reference](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Official documentation for the PCF context object and framework APIs
-   [Test your code components](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Microsoft’s guidance on testing PCF controls

**Testing Best Practices:**

-   [Jest Documentation](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Official Jest testing framework documentation, including guides on mocking and test design

-   [Testing Library Guiding Principles](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Philosophy and principles for writing maintainable tests that focus on behavior over implementation
-   [JSDOM](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Documentation for the JavaScript implementation of web standards used in Jest, including its limitations

**Design Patterns and Principles:**

-   [Dependency Injection Principles](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Martin Fowler’s comprehensive guide to dependency injection patterns

-   [Pure Functions](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Understanding pure functions and their role in testable code
-   [SOLID Principles](vscode-file://vscode-app/c:/Users/zomz/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) – Foundational object-oriented design principles that improve code quality and testability

*Have questions or tips of your own? Share your experiences in the comment below.*

---
> **Note:** This page contains 3 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [PCF Controls Tips & Tricks: Writing Testable Static Methods with Dependency Injection](https://aidevme.com/pcf-controls-tips-tricks-writing-testable-static-methods-with-dependency-injection/)