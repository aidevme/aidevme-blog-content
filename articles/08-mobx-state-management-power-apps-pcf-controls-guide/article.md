# MobX for PCF Controls: Complete Guide (2025)

Estimated reading time: 7 minutes

If you’ve been building custom controls for Power Apps using the Component Framework (PCF), you know that managing state can get messy real fast. I’ve been there—juggling form values, validation rules, computed fields, and trying to keep everything in sync without pulling my hair out.

After building dozens of PCF controls over the past few years, I’ve learned that **choosing the right state management solution can make or break your development experience**. Today, I’m going to share everything I’ve learned about using MobX for PCF development, including when it shines and when you might want to consider alternatives.

**What you’ll learn in this guide:**

-   Why state management matters in PCF controls.

-   How MobX makes complex state simple (with real code examples).
-   When to use MobX vs modern alternatives like Zustand.

-   Building production-ready PCF controls with MobX.
-   Performance optimization tricks I wish I knew earlier

**Let’s dive in!**

## Table of contents

-   [Why State Management Matters in PCF Controls](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-why-state-management-matters-in-pcf-controls)

-   [What is MobX? (And Why I Love It)](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-what-is-mobx-and-why-i-love-it)
-   [Setting Up MobX in Your PCF Project](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-setting-up-mobx-in-your-pcf-project)

-   [Real-World Example: Building a Smart Contact Form](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-real-world-example-building-a-smart-contact-form)
    -   [The ViewModel](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-the-viewmodel)
    -   [The React Component](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-the-react-component)
    -   [Integrating with PCF](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-integrating-with-pcf)
-   [MobX vs Modern Alternatives (2026 Update)](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-mobx-vs-modern-alternatives-2026-update)
    -   [The Hybrid Approach (What I Actually Do)](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-the-hybrid-approach-what-i-actually-do)
-   [Best Practices I’ve Learned (The Hard Way)](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-best-practices-i-ve-learned-the-hard-way)

-   [Common Mistakes (So You Don’t Make Them)](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-common-mistakes-so-you-don-t-make-them)
-   [When NOT to Use MobX](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-when-not-to-use-mobx)

-   [Wrapping Up](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/#h-wrapping-up)

## Why State Management Matters in PCF Controls

Let me tell you a story.

A few years ago, I was building a complex configurator control for a manufacturing client. It had dropdown menus, checkboxes, calculated prices, validation rules—you name it. I thought I could just use React’s `useState` and call it a day.

**Big mistake.**

Within a week, my component file was 800 lines of tangled logic. Every time I changed one field, I had to manually update five others. Bugs were popping up faster than I could squash them. Sound familiar?

### The PCF State Management Challenge

PCF controls have unique challenges:

-   M**ultiple data sources**: Form inputs, datasets, context parameters.

-   **Complex validation**: Business rules, dependent fields, async validation.
-   **Performance**: Re-rendering only what’s necessary.

-   **Testability**: Keeping business logic separate from UI.
-   **Cross-platform**: Same code for Model-Driven and Canvas apps

This is where proper state management becomes your best friend.

## What is MobX? (And Why I Love It)

**MobX** is like having an intelligent assistant that watches your data and automatically updates your UI when things change. No manual wiring. No boilerplate. Just pure magic (okay, it’s actually science, but it *feels* like magic).

### The Core Philosophy

MobX follows one simple principle:

> Anything that can be derived from the application state, should be. Automatically.

What does this mean in practice? Let me show you with a simple example:

TypeScript

```
// Traditional React approach
const [firstName, setFirstName] = useState('');
const [lastName, setLastName] = useState('');
const [fullName, setFullName] = useState('');

// Every time either name changes, you need to update fullName
useEffect(() => {
  setFullName(`${firstName} ${lastName}`.trim());
}, [firstName, lastName]);

// MobX approach
class UserViewModel {
  firstName = '';
  lastName = '';
  
  constructor() {
    makeAutoObservable(this);
  }
  
  get fullName() {
    return `${this.firstName} ${this.lastName}`.trim();
  }
}
```

See the difference? With MobX, `fullName` is **automatically computed**. No manual synchronization. No `useEffect` hooks. It just works.

**Why MobX is Perfect for PCF**

After building PCF controls with plain React hooks, here’s why MobX became my go-to:

**1\. MVVM Pattern Support**  
PCF development benefits hugely from the Model-View-ViewModel pattern. MobX’s class-based approach fits this perfectly.

**2\. Automatic Reactivity**  
Computed values update automatically. No need to manually track dependencies.

**3\. Less Boilerplate**  
Compared to Redux, MobX saves you from writing actions, reducers, and selectors.

**4\. Great for Complex Forms**  
When you have fields that depend on each other, MobX’s reactive model is a lifesaver.

**5\. Object-Oriented Friendly**  
If you come from a C#/.NET background (common in Power Platform development), MobX feels natural.

## Setting Up MobX in Your PCF Project

Alright, let’s get our hands dirty! Here’s how to add MobX to your PCF project.

### Prerequisites

Before we start, make sure you have:

-   Node.js installed (v16+ recommended).

-   Power Apps CLI (`pac` CLI) installed.
-   [Visual Studio Code](https://code.visualstudio.com/) (or your favorite editor).

-   Basic knowledge of React and TypeScript

**Step 1: Create Your PCF Project**

Bash

```


# Create a new PCF control
pac pcf init --namespace YourNamespace --name SmartContactForm --template field --framework React

# Navigate into the project
cd SmartContactForm
```

**Step 2: Install MobX**

Bash

```


# Install MobX and React bindings
npm install mobx mobx-react-lite --save

# Install types (if needed)
npm install @types/react --save-dev
```

**Step 3: Configure TypeScript (Optional)**

If you want to use decorators (optional with modern MobX), update your `tsconfig.json`:

JSON

```
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "useDefineForClassFields": false
  }
}
```

**Pro tip:** Modern MobX (v6+) doesn’t require decorators. You can use `makeAutoObservable` instead, which I prefer because it’s simpler.

**Step 4: Verify Your Setup**

Run the build to make sure everything’s working:

Bash

```
npm run build
```

If you see no errors, you’re golden!

Okay, theory is great, but let’s build something real. We’re going to create a contact form with:

-   First name and last name fields.

-   Email and phone fields.
-   Conditional validation (email required if preferred contact is email).

-   Real-time full name display.
-   Country/state cascading dropdowns

This is the kind of complex form where MobX really shines.

### The ViewModel

First, let’s create our MobX ViewModel. This is where all the business logic lives:

TypeScript

```
// ContactFormViewModel.ts
import { makeAutoObservable, reaction } from 'mobx';
import { IInputs, IOutputs } from './generated/ManifestTypes';

export class ContactFormViewModel {
  // Observable state
  firstName: string = '';
  lastName: string = '';
  email: string = '';
  phone: string = '';
  country: string = 'US';
  state: string = '';
  preferredContact: 'email' | 'phone' = 'email';
  
  // Validation errors
  errors: Map<string, string> = new Map();
  
  // Available states for selected country
  availableStates: string[] = [];
  
  // Submitting flag
  isSubmitting: boolean = false;

  constructor(
    private context: ComponentFramework.Context<IInputs>,
    private notifyOutputChanged: () => void
  ) {
    // Make everything observable (this is the magic!)
    makeAutoObservable(this, {
      context: false,
      notifyOutputChanged: false
    });

    // React to country changes
    reaction(
      () => this.country,
      (country) => {
        this.loadStatesForCountry(country);
        this.state = ''; // Reset state when country changes
      }
    );

    // React to preferred contact changes
    reaction(
      () => this.preferredContact,
      () => this.validatePreferredContact()
    );
  }

  // Computed value - automatically updates!
  get fullName(): string {
    return `${this.firstName} ${this.lastName}`.trim();
  }

  // Another computed value
  get isValid(): boolean {
    return this.errors.size === 0;
  }

  get canSubmit(): boolean {
    return this.isValid && 
           this.firstName.length > 0 && 
           this.lastName.length > 0 &&
           !this.isSubmitting;
  }

  // Action to update field
  setField<K extends keyof this>(field: K, value: this[K]): void {
    this[field] = value;
    this.validate();
  }

  // Validation logic
  validate(): void {
    this.errors.clear();

    // Required fields
    if (!this.firstName) {
      this.errors.set('firstName', 'First name is required');
    }

    if (!this.lastName) {
      this.errors.set('lastName', 'Last name is required');
    }

    // Email validation
    if (this.preferredContact === 'email' || this.email.length > 0) {
      if (!this.email) {
        this.errors.set('email', 'Email is required');
      } else if (!this.isValidEmail(this.email)) {
        this.errors.set('email', 'Please enter a valid email');
      }
    }

    // Phone validation
    if (this.preferredContact === 'phone') {
      if (!this.phone) {
        this.errors.set('phone', 'Phone is required when it\'s your preferred contact');
      }
    }

    // State validation
    if (this.availableStates.length > 0 && !this.state) {
      this.errors.set('state', 'Please select a state');
    }
  }

  validatePreferredContact(): void {
    // This runs automatically when preferredContact changes!
    if (this.preferredContact === 'email') {
      if (!this.email) {
        this.errors.set('email', 'Email required for email contact');
      }
      this.errors.delete('phone');
    } else {
      if (!this.phone) {
        this.errors.set('phone', 'Phone required for phone contact');
      }
      this.errors.delete('email');
    }
  }

  private isValidEmail(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  async loadStatesForCountry(country: string): Promise<void> {
    // In real app, fetch from Dataverse
    const statesMap: Record<string, string[]> = {
      'US': ['CA', 'NY', 'TX', 'FL', 'WA'],
      'CA': ['ON', 'BC', 'QC', 'AB'],
      'UK': ['England', 'Scotland', 'Wales']
    };
    
    this.availableStates = statesMap[country] || [];
  }

  // Update from PCF context
  updateFromContext(context: ComponentFramework.Context<IInputs>): void {
    // Update from external changes
    const inputFirstName = context.parameters.firstName?.raw || '';
    const inputLastName = context.parameters.lastName?.raw || '';
    
    if (inputFirstName !== this.firstName) {
      this.firstName = inputFirstName;
    }
    
    if (inputLastName !== this.lastName) {
      this.lastName = inputLastName;
    }
  }

  // Get outputs for PCF
  getOutputs(): IOutputs {
    return {
      fullName: this.fullName,
      firstName: this.firstName,
      lastName: this.lastName,
      email: this.email,
      phone: this.phone,
      country: this.country,
      state: this.state
    };
  }

  // Submit handler
  async submit(): Promise<void> {
    this.validate();
    
    if (!this.isValid) {
      return;
    }

    this.isSubmitting = true;
    
    try {
      // Your submit logic here
      console.log('Submitting:', this.getOutputs());
      
      // Notify PCF that outputs changed
      this.notifyOutputChanged();
    } finally {
      this.isSubmitting = false;
    }
  }
}
```

**Let me break down what’s happening here:**

1.  **`makeAutoObservable(this)`** – This one line makes all properties observable and all methods actions. Magic!
2.  **Computed values** (`get fullName()`) – These update automatically when their dependencies change.
3.  **Reactions** – The `reaction()` calls set up automatic side effects when specific values change.
4.  **Validation** – Centralized in one place, easy to test.

### The React Component

**Now let’s create the UI that uses this ViewModel:**

TypeScript

```
// ContactFormComponent.tsx
import React from 'react';
import { observer } from 'mobx-react-lite';
import { ContactFormViewModel } from './ContactFormViewModel';
import './ContactForm.css';

interface ContactFormProps {
  viewModel: ContactFormViewModel;
}

export const ContactFormComponent = observer((props: ContactFormProps) => {
  const vm = props.viewModel; // Shorthand for cleaner code

  return (
    <div className="contact-form">
      <h2>Contact Information</h2>
      
      {/* Name Section */}
      <div className="form-section">
        <div className="form-row">
          <div className="form-field">
            <label>First Name *</label>
            <input
              type="text"
              value={vm.firstName}
              onChange={(e) => vm.setField('firstName', e.target.value)}
              className={vm.errors.has('firstName') ? 'error' : ''}
              placeholder="Enter first name"
            />
            {vm.errors.has('firstName') && (
              <span className="error-message">{vm.errors.get('firstName')}</span>
            )}
          </div>

          <div className="form-field">
            <label>Last Name *</label>
            <input
              type="text"
              value={vm.lastName}
              onChange={(e) => vm.setField('lastName', e.target.value)}
              className={vm.errors.has('lastName') ? 'error' : ''}
              placeholder="Enter last name"
            />
            {vm.errors.has('lastName') && (
              <span className="error-message">{vm.errors.get('lastName')}</span>
            )}
          </div>
        </div>

        {/* Full Name Display (auto-computed!) */}
        {vm.fullName && (
          <div className="full-name-display">
            <strong>Full Name:</strong> {vm.fullName}
          </div>
        )}
      </div>

      {/* Preferred Contact */}
      <div className="form-section">
        <div className="form-field">
          <label>Preferred Contact Method *</label>
          <select
            value={vm.preferredContact}
            onChange={(e) => vm.setField('preferredContact', e.target.value as 'email' | 'phone')}
          >
            <option value="email">Email</option>
            <option value="phone">Phone</option>
          </select>
        </div>
      </div>

      {/* Conditional Email Field */}
      {(vm.preferredContact === 'email' || vm.email.length > 0) && (
        <div className="form-section">
          <div className="form-field">
            <label>Email *</label>
            <input
              type="email"
              value={vm.email}
              onChange={(e) => vm.setField('email', e.target.value)}
              className={vm.errors.has('email') ? 'error' : ''}
              placeholder="your.email@example.com"
            />
            {vm.errors.has('email') && (
              <span className="error-message">{vm.errors.get('email')}</span>
            )}
          </div>
        </div>
      )}

      {/* Conditional Phone Field */}
      {vm.preferredContact === 'phone' && (
        <div className="form-section">
          <div className="form-field">
            <label>Phone *</label>
            <input
              type="tel"
              value={vm.phone}
              onChange={(e) => vm.setField('phone', e.target.value)}
              className={vm.errors.has('phone') ? 'error' : ''}
              placeholder="(555) 123-4567"
            />
            {vm.errors.has('phone') && (
              <span className="error-message">{vm.errors.get('phone')}</span>
            )}
          </div>
        </div>
      )}

      {/* Location Section */}
      <div className="form-section">
        <h3>Location</h3>
        
        <div className="form-row">
          <div className="form-field">
            <label>Country</label>
            <select
              value={vm.country}
              onChange={(e) => vm.setField('country', e.target.value)}
            >
              <option value="US">United States</option>
              <option value="CA">Canada</option>
              <option value="UK">United Kingdom</option>
            </select>
          </div>

          {vm.availableStates.length > 0 && (
            <div className="form-field">
              <label>State/Province *</label>
              <select
                value={vm.state}
                onChange={(e) => vm.setField('state', e.target.value)}
                className={vm.errors.has('state') ? 'error' : ''}
              >
                <option value="">Select...</option>
                {vm.availableStates.map(state => (
                  <option key={state} value={state}>{state}</option>
                ))}
              </select>
              {vm.errors.has('state') && (
                <span className="error-message">{vm.errors.get('state')}</span>
              )}
            </div>
          )}
        </div>
      </div>

      {/* Submit Button */}
      <div className="form-actions">
        <button
          onClick={() => vm.submit()}
          disabled={!vm.canSubmit}
          className={`submit-button ${vm.canSubmit ? 'enabled' : 'disabled'}`}
        >
          {vm.isSubmitting ? 'Submitting...' : 'Submit'}
        </button>
      </div>

      {/* Validation Summary */}
      {!vm.isValid && (
        <div className="validation-summary">
          <strong>Please fix the following errors:</strong>
          <ul>
            {Array.from(vm.errors.values()).map((error, index) => (
              <li key={index}>{error}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
});
```

**The magic of `observer`:**  
Notice that single `observer` wrapper? That’s what makes this component automatically re-render when any observable value changes. No `useEffect`, no manual subscriptions. Beautiful!

### Integrating with PCF

**Finally, let’s wire this up to the PCF framework:**

TypeScript

```
// index.ts
import { IInputs, IOutputs } from './generated/ManifestTypes';
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { ContactFormViewModel } from './ContactFormViewModel';
import { ContactFormComponent } from './ContactFormComponent';

export class SmartContactForm implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  private container: HTMLDivElement;
  private viewModel: ContactFormViewModel;
  private notifyOutputChanged: () => void;

  constructor() {}

  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ): void {
    this.container = container;
    this.notifyOutputChanged = notifyOutputChanged;
    
    // Create the ViewModel
    this.viewModel = new ContactFormViewModel(
      context,
      notifyOutputChanged
    );
    
    // Initial render
    this.renderComponent();
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    // Update ViewModel from context
    this.viewModel.updateFromContext(context);
  }

  private renderComponent(): void {
    ReactDOM.render(
      React.createElement(ContactFormComponent, {
        viewModel: this.viewModel
      }),
      this.container
    );
  }

  public getOutputs(): IOutputs {
    return this.viewModel.getOutputs();
  }

  public destroy(): void {
    ReactDOM.unmountComponentAtNode(this.container);
  }
}
```

**And that’s it!** You now have a fully functional, smart contact form with MobX state management.

## MobX vs Modern Alternatives (2026 Update)

Now, I know what you’re thinking: *“Is MobX still relevant in 2026?”*

Great question! Let me give you the honest answer.

MobX is **definitely not dead**. It’s mature, stable, and actively maintained. But the JavaScript ecosystem has evolved, and you have more choices now. Let me break down when to use what.

### MobX vs Zustand

[**Zustand**](https://zustand-demo.pmnd.rs/) is the new kid on the block everyone’s talking about. It’s tiny (~1KB) and super simple.

**Use MobX when:**

-   You have complex business logic with lots of interdependent fields.

-   You want automatic computed values (not function calls).
-   You prefer class-based ViewModels (MVVM pattern).

-   You’re coming from C#/.NET background

**Use Zustand when:**

-   Your control is relatively simple.

-   You want minimal bundle size.
-   You prefer functional programming.

-   You’re prototyping quickly

**Real talk:** For simple counters or toggles, Zustand wins. For complex forms with validation, MobX is still my pick.

**Quick Comparison**

| **Feature** | **MobX** | **Zustand** | **My Take** |
| **Bundle Size** | ~16KB | ~1KB | Zustand wins, but 15KB isn’t a dealbreaker |
| **Learning Curve** | Moderate | Super Easy | Zustand is easier to learn |
| **Auto Computed** | Yes | No (must call functions) | MobX wins for complex logic |
| **MVVM Support** | Excellent | Possible but awkward | MobX wins for architecture |
| **Boilerplate** | Low | Minimal | Both are good |

### The Hybrid Approach (What I Actually Do)

Here’s my secret: **I use both!**

-   **MobX** for complex PCF controls with business logic.

-   **Zustand** for simple UI state (modals, tabs, etc.).
-   **TanStack Query** for all server/API data

## Best Practices I’ve Learned (The Hard Way)

After building PCF controls with MobX, here are the lessons I wish someone had taught me:

**1\. Keep ViewModels Pure**

![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) **Bad:**

TypeScript

```
class BadViewModel {
  value = 0;
  
  increment() {
    this.value++;
    document.getElementById('counter').focus(); // DON'T DO THIS!
  }
}
```

![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) **Good:**

TypeScript

```
class GoodViewModel {
  value = 0;
  
  increment() {
    this.value++;
    // Let the component handle DOM interactions
  }
}
```

**2\. Use `runInAction` for Async Updates**

![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) **Bad:**

TypeScript

```
async loadData() {
  const data = await fetchData();
  this.data = data; // MobX will warn about this!
}
```

![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) **Good:**

TypeScript

```
async loadData() {
  const data = await fetchData();
  runInAction(() => {
    this.data = data; // Safe!
  });
}
```

**3\. Don’t Make Everything Observable**

TypeScript

```
constructor() {
  makeAutoObservable(this, {
    context: false,        // PCF context doesn't need to be observable
    helper: false,         // Helper classes don't need to be observable
    computedValue: computed // Be explicit about computed
  });
}
```

**4\. Test Your ViewModels**

The beauty of ViewModels is they’re easy to test:

TypeScript

```
describe('ContactFormViewModel', () => {
  let vm: ContactFormViewModel;
  
  beforeEach(() => {
    vm = new ContactFormViewModel(mockContext, jest.fn());
  });

  test('computes full name correctly', () => {
    vm.firstName = 'John';
    vm.lastName = 'Doe';
    expect(vm.fullName).toBe('John Doe');
  });

  test('validates required fields', () => {
    vm.validate();
    expect(vm.errors.has('firstName')).toBe(true);
  });
});
```

**5\. Use Reactions Wisely**

Reactions are powerful, but don’t go crazy:

TypeScript

```
//  Good: React to specific changes
reaction(
  () => this.country,
  (country) => this.loadStates(country)
);

//  Bad: Too many reactions can be hard to debug
reaction(() => this.field1, () => { /* ... */ });
reaction(() => this.field2, () => { /* ... */ });
reaction(() => this.field3, () => { /* ... */ });
// ... etc
```

## Common Mistakes (So You Don’t Make Them)

**Mistake #1: Forgetting `observer`**

TypeScript

```
//  This won't react to changes!
export const MyComponent = (props) => {
  return <div>{props.viewModel.value}</div>;
};

//  This will!
export const MyComponent = observer((props) => {
  return <div>{props.viewModel.value}</div>;
});
```

**Mistake #2: Mutating Arrays Directly**

TypeScript

```
//  Might not trigger reactions
this.items.push(newItem);

//  Always works
this.items = [...this.items, newItem];
```

**Mistake #3: Over-engineering Simple State**

TypeScript

```
//  Overkill for a simple toggle
class ModalViewModel {
  isOpen = false;
  constructor() { makeAutoObservable(this); }
  toggle() { this.isOpen = !this.isOpen; }
}

//  Just use React hooks for simple state
const [isOpen, setIsOpen] = useState(false);
```

## When NOT to Use MobX

Look, I love MobX, but it’s not always the right choice. Here’s when to skip it:

**Don’t use MobX if:**

-   Your control is super simple (just a formatted text field).

-   Your team is unfamiliar with OOP patterns.
-   Bundle size is critical (<5KB requirement).

-   You’re just toggling a modal open/closed

**DO use MobX if:**

-   Complex forms with validation.

-   Interdependent calculated fields.
-   You want MVVM architecture.

-   Performance optimization is needed (large datasets)

## Wrapping Up

**Here’s what we covered:**

-   Why state management matters in PCF development.

-   How MobX makes complex state simple.
-   Building a real production-ready contact form.

-   MobX vs modern alternatives (Zustand, etc.).
-   Best practices and common mistakes

**My Final Recommendation**

If you’re building a **complex PCF control** with business logic, validation, and computed values—**MobX is still an excellent choice in 2025**. It’s mature, well-documented, and makes your code cleaner.

For **simple controls**, consider Zustand or even just React hooks.

And remember: **The best state management solution is the one that makes your code easier to understand and maintain.** Don’t get caught up in hype—choose what works for your specific needs.

**What’s Next?**

**Now that you understand MobX for PCF, here are some next steps:**

-   **Build something!** The best way to learn is by doing.

-   Check out the [official MobX docs](https://mobx.js.org/).
-   Explore [PCF Gallery](https://pcf.gallery/) for inspiration.

-   Join the [Power Platform Community](https://powerusers.microsoft.com/)

### Resources & Links

**Official Documentation:**

-   [MobX Official Docs](https://mobx.js.org/) – Comprehensive MobX guide

-   [Power Apps PCF Docs](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview) – Microsoft’s official PCF documentation.
-   [pcf-react Library](https://github.com/scottdurow/pcf-react) – MVVM helpers for PCF

**Community Resources:**

-   [PCF Gallery](https://pcf.gallery/) – Browse community PCF controls.

-   [Dynamics PCF Lady](https://dianabirkelbach.wordpress.com/)
-   [Power Platform Community](https://powerusers.microsoft.com/t5/Power-Apps-Component/bd-p/pa_component_framework)[.](https://stackoverflow.com/questions/tagged/powerapps-component-framework)

-   [Stack Overflow – PCF Tag](https://stackoverflow.com/questions/tagged/powerapps-component-framework)

## Questions? Let’s Chat!

**Have questions about MobX, PCF, or Power Platform development? Drop a comment below**.

*Happy coding, and may your state always be reactive!*

### *Related*

---
> **Note:** This page contains 3 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [MobX State Management for Power Apps PCF Controls: Your Complete Guide 2026](https://aidevme.com/mobx-state-management-power-apps-pcf-controls-guide/)