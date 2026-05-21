# Power Pages Authentication: A Complete Guide - Practical AI, Copilot & Modern Development Insights

Estimated reading time: 18 minutes

Microsoft Power Pages supports five authentication methods — local credentials, OpenID Connect (OIDC), SAML 2.0, OAuth 2.0 social login, and open/invitation-code registration. This guide explains how each one works, when to use it, how to configure it, and what security risks to watch out for before you go live.

## Table of contents

-   [Introduction — Why Authentication Matters in Power Pages](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-introduction-why-authentication-matters-in-power-pages)

-   [What Is Power Pages?](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-what-is-power-pages)
-   [How Power Pages Handles Identity](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-how-power-pages-handles-identity)

-   [Authentication Methods](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-authentication-methods)
    -   [Method 1 — Local Authentication (ASP.NET Identity](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-method-1-local-authentication-asp-net-identity)
    -   [Method 2 — OpenID Connect (OIDC)](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-method-2-openid-connect-oidc)
    -   [Method 3 — SAML 2.0](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-method-3-saml-2-0)
    -   [Method 4 — OAuth 2.0 Social Login](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-method-4-oauth-2-0-social-login)
    -   [Method 5 — Open Registration and Invitation Codes](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-method-5-open-registration-and-invitation-codes)
    -   [Side-by-Side Comparison of All Methods](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-side-by-side-comparison-of-all-methods)
-   [Security Best Practices for Power Pages Authentication](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-security-best-practices-for-power-pages-authentication)
    -   [1\. Always enforce HTTPS for session cookies](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#1-always-enforce-https-for-session-cookies)
    -   [2\. Disable local authentication unless explicitly required](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#2-disable-local-authentication-unless-explicitly-required)
    -   [3\. Override the implicit grant default in OIDC](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#3-override-the-implicit-grant-default-in-oidc)
    -   [4\. Always validate audience and issuer in OIDC](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#4-always-validate-audience-and-issuer-in-oidc)
    -   [5\. Disable open registration for any non-public portal](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#5-disable-open-registration-for-any-non-public-portal)
    -   [6\. Audit claims mapping configuration](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#6-audit-claims-mapping-configuration)
    -   [7\. Never enable demo mode in production](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#7-never-enable-demo-mode-in-production)
    -   [8\. Configure and test Single Logout](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#8-configure-and-test-single-logout)
    -   [9\. Avoid social providers for enterprise or regulated portals](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#9-avoid-social-providers-for-enterprise-or-regulated-portals)
    -   [10\. Manage duplicate contact records proactively](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#10-manage-duplicate-contact-records-proactively)
-   [Which Authentication Method Should You Choose?](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-which-authentication-method-should-you-choose)
    -   [Can I use multiple identity providers at the same time in Power Pages?](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-can-i-use-multiple-identity-providers-at-the-same-time-in-power-pages)
    -   [Can Power Pages work with Azure AD B2C?](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-can-power-pages-work-with-azure-ad-b2c)
    -   [What is the difference between OIDC and SAML 2.0 in Power Pages?](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-what-is-the-difference-between-oidc-and-saml-2-0-in-power-pages)
    -   [What happens when a user signs in with a social provider for the first time?](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-what-happens-when-a-user-signs-in-with-a-social-provider-for-the-first-time)
    -   [How do web roles get assigned to users in Power Pages?](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-how-do-web-roles-get-assigned-to-users-in-power-pages)
-   [References and Further Reading](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-references-and-further-reading)
    -   [Official Microsoft Documentation](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-official-microsoft-documentation)
    -   [Standards and Security References](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-standards-and-security-references)
    -   [Related Articles](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/#h-related-articles)

## Introduction — Why Authentication Matters in Power Pages

Building a portal on Microsoft Power Pages is fast and powerful. But the moment you add user-restricted content — customer dashboards, partner portals, employee self-service pages — you need to make a critical decision: **\*\*how will your users prove who they are?\*\***

Get this right and you get a seamless, secure experience that fits your existing identity infrastructure. Get it wrong and you open the door to account takeover, data leaks, regulatory non-compliance, and a painful re-architecture down the road.

Power Pages ships with five distinct authentication approaches, each with its own protocol, trust model, configuration overhead, and risk profile. In this guide we walk through all five — what they are, how they work step by step, when they are the right tool, and what you need to do to configure them securely.

Whether you are a developer wiring up your first portal, an architect designing an enterprise solution, or a security reviewer preparing for a go-live audit, this article has the depth you need.

---

## What Is Power Pages?

[Microsoft Power Pages](https://learn.microsoft.com/en-us/power-pages/) is a low-code platform for building externally facing business websites and portals. It sits within the Microsoft Power Platform ecosystem and is built on top of Microsoft Dataverse as its data layer.

Key characteristics relevant to authentication:

-   All authenticated portal users are stored as **Dataverse contact records**

-   Access to pages and data is controlled by **web roles** assigned to those contact records
-   The portal runtime is ASP.NET-based and uses **ASP.NET Identity** and **OWIN** middleware under the hood

-   Authentication state is maintained via a session cookie named **AspNet.Cookies**
-   Power Pages supports multiple identity providers simultaneously — users can be offered a choice at sign-in

Because everything flows through Dataverse contact records, the security of your authentication layer has a direct impact on the integrity of your CRM data. A compromised user account does not just grant portal access — it may also expose or corrupt Dataverse records tied to that contact.

---

## How Power Pages Handles Identity

Regardless of which authentication method you use, the end result is the same:

Markdown

```
[User authenticates] → [Identity verified] → [Contact record matched/created in Dataverse]
       → [Web roles retrieved] → [.AspNet.Cookies session issued] → [Portal access granted]
```

Power Pages uses a **claims-based identity model**. Once authentication succeeds, the identity provider (local or external) emits a set of claims — name, email, group memberships — that Power Pages maps to fields on the Dataverse contact record. This mapping is configurable through **registration claims mapping** and **login claims mapping** site settings.

**Important:** Every user must have a unique email address in Dataverse. If two contact records share the same email — including deactivated records — neither account can authenticate. This is a known denial-of-service vector that must be managed proactively.

---

![Power Pages portal window connected to five identity providers: local credentials, Entra ID (OIDC), SAML 2.0, social OAuth, and invitation code registration](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/power-pages-authentication-hero-banner.png?resize=1024%2C683&ssl=1)

## Authentication Methods

Power Pages supports five distinct approaches to user authentication. Each method uses a different protocol, trust model, and configuration approach. Understanding the differences is critical to choosing the right solution for your requirements.

#### The Five Authentication Approaches

**Method 1: Local Authentication (ASP.NET Identity)**  
Built-in username and password authentication stored directly in Dataverse contact records. No external identity provider required. Microsoft recommends migrating away from this approach for production enterprise portals.

**Method 2: OpenID Connect (OIDC)**  
Modern federated authentication protocol. Integrates with Azure AD B2C, Azure Entra ID (formerly Azure AD), and other OIDC-compliant providers. Recommended for customer-facing portals and B2C scenarios.

**Method 3: SAML 2.0**  
Enterprise-grade federated authentication. Used for integration with corporate identity systems like ADFS, Okta, Ping Identity, and other SAML 2.0-compliant providers. Best option for partner portals and B2B scenarios.

**Method 4: OAuth 2.0 Social Login**  
Allows users to sign in with their existing social media accounts (Microsoft personal, Google, LinkedIn, Facebook, Twitter/X). Suitable for consumer-facing portals and community sites where convenience is prioritized.

**Method 5: Open Registration and Invitation Codes**  
Self-service account creation with optional invitation codes. Not an authentication protocol itself, but a registration workflow that pairs with any of the above methods. Used for controlled onboarding scenarios.

---

![Local authentication with username and password in Power Pages — ASP.NET Identity login form with optional email two-factor authentication](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/power-pages-local-authentication.png?resize=1024%2C683&ssl=1)

### Method 1 — Local Authentication (ASP.NET Identity

Local authentication is the built-in, username-and-password credential store provided by ASP.NET Identity. Credentials are stored directly in Dataverse contact records. There is no external identity provider involved.

**Microsoft recommends migrating away from local authentication** to Azure AD B2C. Consider this method legacy. Use it only for low-risk, non-production, or transitional scenarios.

#### How It Works

1.  The user submits their email and password on the portal sign-in page.
2.  Power Pages retrieves the matching Dataverse contact record.
3.  ASP.NET Identity compares the submitted password against the stored PBKDF2 hash.
4.  If the account lockout threshold has not been exceeded (default: 5 failed attempts, 24-hour lockout), the login proceeds.
5.  If two-factor authentication is enabled for the account, an OTP is emailed to the user’s confirmed address.
6.  Upon successful authentication, Power Pages issues the `.AspNet.Cookies` session cookie.

#### When to Use It

-   Rapid prototyping and internal demos

-   Very low-sensitivity portals with no regulated data
-   Transitional phase while migrating to a federated identity provider

#### When Not to Use It

-   Any portal handling personal data, financial information, or health records

-   Any portal subject to regulatory requirements (GDPR, PSD2, HIPAA, ISO 27001)
-   Any scenario where phishing-resistant authentication is required

#### Key Configuration Settings

| **Setting** | **Default** | **Recommendation** |
| Authentication/Registration/LocalLoginEnabled | True | Disable for production enterprise portals |
| Authentication/Registration/TwoFactorEnabled | False | Enable if local auth is kept |
| Authentication/UserManager/PasswordValidator/RequireDigit | False | Set to True |
| Authentication/UserManager/PasswordValidator/RequireUppercase | False | Set to True |
| Authentication/UserManager/MaxFailedAccessAttemptsBeforeLockout | 5 | Consider reducing to 3 |
| Authentication/Registration/IsDemoMode | False | Must never be True in production |
| Authentication/ApplicationCookie/CookieSecure | SameAsRequest | Set to Always |

#### Top Security Risks

-   **Email-only 2FA** is not phishing-resistant and is vulnerable to email account compromise

-   **`IsDemoMode = True`** exposes OTP codes and password reset tokens directly in the UI — catastrophic if enabled in production
-   **Weak password policy defaults** — digit, uppercase, and special character requirements are all `False` out of the box

-   **`CookieSecure = SameAsRequest`** allows session cookies over HTTP on misconfigured infrastructure

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/power-pages-oidc-authentication.png?fit=1024%2C683&ssl=1)

### Method 2 — OpenID Connect (OIDC)

OpenID Connect is a modern identity layer built on top of OAuth 2.0. Power Pages supports OIDC for enterprise providers (Microsoft Entra ID, Entra External ID, Azure AD B2C) as well as any standards-compliant OIDC provider.

When properly configured, OIDC allows Power Pages to delegate all authentication — including MFA and Conditional Access enforcement — to a trusted external identity provider.

#### How It Works

1.  The user selects their OIDC identity provider on the sign-in page.
2.  Power Pages fetches the provider’s discovery document to obtain endpoints.
3.  Power Pages builds an authorization request and redirects the browser to the IdP’s authorize endpoint.
4.  The IdP authenticates the user (enforcing MFA, Conditional Access policies, etc.).
5.  The IdP issues an authorization code and redirects the browser back to the Power Pages reply URL.
6.  Power Pages exchanges the code for an `id_token` back-channel (server-to-server, not via the browser).
7.  Power Pages validates the `id_token` — checking signature, issuer, audience, nonce, and expiry.
8.  Claims from the token are mapped to a Dataverse contact record.
9.  Power Pages issues the `.AspNet.Cookies` session cookie.

#### Supported Identity Providers

-   Microsoft Entra ID (single tenant and multi-tenant)

-   Microsoft Entra External ID
-   Azure AD B2C (with custom policies)

-   Any OIDC-compliant provider (Okta, Auth0, Ping Identity, etc.)

#### Critical Configuration Warning

Power Pages defaults to the **implicit grant flow** (`response_type = code id_token`). This flow is deprecated under OAuth 2.0 Security Best Current Practice (RFC 9700) because it exposes tokens in the browser URL and history. **You must explicitly override this** to use the authorization code flow:

Markdown

```
response_type = code
response_mode = query
```

Additionally, **PKCE is not supported** in Power Pages OIDC as of 2026 — a known platform gap that should be formally noted in your security documentation.

#### Key Configuration Settings

| **Setting** | **Default** | **Recommendation** |
| response\_type | code id\_token | Change to code |
| response\_mode | form\_post | Change to query when using code flow |
| ValidateAudience | Off | Enable — explicit audience list |
| ValidateIssuers | Off | Enable — scoped issuer, no wildcards |
| Issuer filter | https://sts.windows.net/\*/ | Replace \* with your tenant ID |
| External logout | Off | Enable for federated sign-out |
| CookieSecure | SameAsRequest | Set to Always |

#### Top Security Risks

-   **Implicit grant as default** — tokens exposed in URL fragment and browser history

-   **No PKCE support** — authorization code interception is possible
-   **Audience/issuer validation not enforced by default** — accepts tokens from other apps or tenants

-   **Wildcard issuer filter** — accepts tokens from any Entra ID tenant unless scoped
-   **Claims mapping can overwrite sensitive contact fields** — audit your mapping configuration carefully

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/power-pages-saml2-authentication.png?fit=1024%2C683&ssl=1)

### Method 3 — SAML 2.0

SAML 2.0 (Security Assertion Markup Language) is a mature XML-based federation protocol widely used in enterprise environments. Power Pages acts as the Service Provider (SP); Entra ID or AD FS acts as the Identity Provider (IdP). SAML assertions are XML documents signed with the IdP’s private key — they never appear as readable tokens in the browser URL.

#### How It Works

1.  The user selects the SAML provider on the sign-in page.
2.  Power Pages (SP) builds a signed XML `AuthnRequest` and redirects the browser to the IdP’s SSO endpoint (the request is base64-encoded in the URL).
3.  The IdP validates the `AuthnRequest` signature and authenticates the user (with MFA and Conditional Access).
4.  The IdP issues a signed XML `SAMLResponse` containing the assertion with user attributes.
5.  The IdP sends the `SAMLResponse` back through the browser via an auto-submitting HTML form (HTTP POST binding).
6.  Power Pages receives the `SAMLResponse` and validates:
    -   Assertion signature (using IdP’s public certificate)
    -   Issuer (must match configured IdP entityID)
    -   Audience (must match SP entityID)
    -   `NotBefore` and `NotOnOrAfter` time conditions
    -   `InResponseTo` field (replay attack prevention)
7.  Attributes from the assertion are mapped to a Dataverse contact record.
8.  Power Pages issues the `.AspNet.Cookies` session cookie.
9.  **Single Logout (SLO):** When the user signs out, Power Pages can send a `LogoutRequest` to the IdP, ensuring the IdP session is also terminated.

#### Supported Identity Providers

-   Microsoft Entra ID

-   Microsoft AD FS (Active Directory Federation Services)
-   Any SAML 2.0-compliant IdP

#### Why SAML 2.0 Is the Recommended Choice for Enterprise

SAML 2.0 offers several advantages over OIDC for regulated enterprise portals:

-   **No tokens in the browser URL** — the `SAMLResponse` is POST-bound, not URL-bound

-   **Signed assertions** — every attribute claim is cryptographically bound to the IdP
-   **Mature SLO support** — federated sign-out is well-defined in the SAML spec

-   **Wide enterprise IdP support** — Entra ID and AD FS both have first-class SAML support
-   **No implicit grant problem** — the SAML protocol does not have an equivalent of OAuth’s implicit flow

#### Key Configuration Settings

| **Setting** | **Recommendation** |
| Signing certificate | Use a valid, non-expired X.509 certificate |
| WantAssertionsSigned | True — require signed assertions, not just signed response envelope |
| ValidateAudience | True — SP entityID must match exactly |
| ValidateIssuer | True — IdP entityID must match, no wildcards |
| SLO endpoint | Configure and test federated sign-out |
| Clock skew tolerance | ≤ 5 minutes to prevent time-based token replay |
| Attribute mapping | Map groups or roles claims to web roles |

#### Top Security Risks

-   **Contact mapping by email (default On)** — if the IdP can issue arbitrary email attributes, an attacker could hijack existing contact records

-   **SLO not enforced by default** — users may remain authenticated at the IdP after signing out of the portal

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/power-pages-oauth2-social-login.png?resize=1024%2C1024&ssl=1)

### Method 4 — OAuth 2.0 Social Login

Power Pages supports OAuth 2.0 social login with five consumer identity providers: Microsoft personal accounts, LinkedIn, Facebook, Google, and Twitter/X. Users authenticate with their existing social account — no separate portal password is needed.

**Not recommended for enterprise, regulated, or sensitive portals.** Social providers offer no enterprise MFA enforcement, no group/role claims for automatic web role assignment, and no compliance guarantees suitable for regulated industries.

#### How It Works

1.  The user selects a social provider (e.g. Google) on the sign-in page.
2.  Power Pages builds an OAuth 2.0 authorize URL and redirects the browser to the social provider.
3.  The user authenticates with their social account credentials.
4.  The social provider issues an authorization code and redirects back to the portal callback URL.
5.  Power Pages exchanges the code for an access token back-channel.
6.  Power Pages reads the minimal profile claims from the token (email, display name only — no groups or roles).
7.  Power Pages matches or creates a Dataverse contact record based on the email claim.
8.  Web roles must be assigned manually — there is no automatic provisioning from social token attributes.
9.  Power Pages issues the `.AspNet.Cookies` session cookie.

#### Supported Social Providers

| **Provider** | **Protocol** |
| Microsoft (personal) | OAuth 2.0 |
| Google | OAuth 2.0 |
| LinkedIn | OAuth 2.0 |
| Facebook | OAuth 2.0 |
| Twitter / X | OAuth 2.0 |

#### When to Use Social Login

-   Low-sensitivity public community portals

-   Consumer-facing portals where social identity is the primary user identifier
-   Portals where users are unlikely to have a corporate identity

#### When Not to Use Social Login

-   Any portal with regulated data (financial, health, legal)

-   Enterprise or partner portals requiring MFA enforcement
-   Any scenario where automatic web role provisioning from group membership is required

#### Top Security Risks

-   **No enterprise MFA enforcement** — social account security is entirely controlled by the end user

-   **Account takeover risk** — a compromised social account grants immediate portal access with no secondary check
-   **No group/role claims** — web roles must be assigned manually; there is no attribute-based access control

---

![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/03/power-pages-open-registration.png?fit=1024%2C683&ssl=1)

### Method 5 — Open Registration and Invitation Codes

Open registration is not a separate authentication protocol — it is a **user provisioning mode** that controls whether users can create their own Dataverse contact records. It works in combination with any of the authentication methods above.

Power Pages offers two registration modes:

**Open Sign-Up (`OpenRegistrationEnabled = True`, default)** Any anonymous internet user can register for an account. A Dataverse contact record is created immediately on registration. This is the least restrictive option and is unsuitable for most enterprise use cases.

**Invitation Code Registration (`InvitationEnabled = True`)** Administrators pre-provision contact records in Dataverse and distribute invitation codes by email. Users can only register by redeeming a valid code. This is the recommended registration path for any portal where user access must be controlled.

#### How Open Sign-Up Works

1.  The anonymous user visits `/register` and submits an email address and password.
2.  Power Pages validates input (password policy, CAPTCHA if enabled).
3.  A new Dataverse contact record is created with the email marked as unconfirmed.
4.  A confirmation email is sent with a verification link.
5.  The user clicks the link, confirms their email, and the account is activated.
6.  The user is signed in with a session cookie and any default web roles.

#### How Invitation Code Registration Works

1.  An administrator creates an invitation record in Dataverse linked to a pre-provisioned contact.
2.  The “Send Invitation” workflow emails the code and redemption link to the user.
3.  The user opens the link and submits the invitation code.
4.  Power Pages validates the code and activates the linked contact record.
5.  The user completes registration (sets a password or links an external identity).
6.  The user is signed in with the web roles pre-assigned to the contact.

#### Key Configuration Settings

| **Setting** | **Default** | **Recommendation** |
| Authentication/Registration/OpenRegistrationEnabled | True | False for enterprise portals |
| Authentication/Registration/InvitationEnabled | True | Acceptable for controlled onboarding |
| Authentication/Registration/CaptchaEnabled | False | True if any self-registration is permitted |
| Authentication/Registration/ResetPasswordRequiresConfirmedEmail | False | True |

#### Top Security Risks

-   **`OpenRegistrationEnabled = True` by default** — any internet user creates a Dataverse contact record and potentially gains portal access if web roles are misconfigured

-   **Duplicate email denial-of-service** — pre-registering an email address can block a legitimate user from ever authenticating
-   **Invitation code leakage** — codes distributed by email can be forwarded or leaked; no documented platform-level expiry enforcement

---

### Side-by-Side Comparison of All Methods

| **Criterion** | **Local Auth** | **OIDC** | **SAML 2.0** | **Social OAuth 2.0** | **Open Reg** |
| External IdP required | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No |
| Enterprise MFA enforcement | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) Email OTP only | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Conditional Access | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Conditional Access | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) None | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) None |
| Phishing-resistant | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Partial | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No |
| Tokens visible in browser | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Cookie only | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Yes (implicit default) | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) No (POST binding) | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Code in URL | N/A |
| Group / role claims | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) None | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) With config | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) Minimal | N/A |
| Single Logout (SLO) | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Optional | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Supported | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No | N/A |
| Regulatory compliance | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) With hardening | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Best option | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) No |
| Microsoft recommended | ![❌](https://s.w.org/images/core/emoji/17.0.2/svg/274c.svg) Deprecated | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) Yes | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Consumer only | ![⚠️](https://s.w.org/images/core/emoji/17.0.2/svg/26a0.svg) Public portals |
| Setup complexity | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) Low | ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) Medium | ![🟡](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e1.svg) Medium | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) Low | ![🟢](https://s.w.org/images/core/emoji/17.0.2/svg/1f7e2.svg) Low |
| Best for | Demos / dev | Customer portals (B2C) | Enterprise / partner | Consumer communities | Controlled onboarding |

---

## Security Best Practices for Power Pages Authentication

Regardless of which authentication method you choose, the following hardening steps apply to every Power Pages deployment:

### 1\. Always enforce HTTPS for session cookies

Set `Authentication/ApplicationCookie/CookieSecure = Always`. The default value `SameAsRequest` allows session cookies to transmit over HTTP on misconfigured or split-traffic infrastructure.

### 2\. Disable local authentication unless explicitly required

Set `Authentication/Registration/LocalLoginEnabled = False`. Microsoft itself recommends against local auth. If you must keep it, enforce strong passwords, enable 2FA, and require email confirmation for password resets.

### 3\. Override the implicit grant default in OIDC

Explicitly set `response_type = code` and `response_mode = query`. Never leave the default `code id_token` hybrid/implicit configuration in production.

### 4\. Always validate audience and issuer in OIDC

Enable `ValidateAudience` and `ValidateIssuers` with explicit, non-wildcard values. Replace `https://sts.windows.net/*/` with your specific tenant ID.

### 5\. Disable open registration for any non-public portal

Set `OpenRegistrationEnabled = False`. Use invitation codes or pre-provisioned contact records for controlled user onboarding.

### 6\. Audit claims mapping configuration

Review every registration and login claims mapping. Ensure no sensitive Dataverse contact fields (account numbers, role attributes, financial data fields) are writable from external token claims.

### 7\. Never enable demo mode in production

`IsDemoMode = True` exposes one-time codes and password reset tokens directly in the browser. Verify this setting is `False` in every environment, including staging.

### 8\. Configure and test Single Logout

Enable federated sign-out for OIDC and SAML 2.0. Test that signing out of the portal also terminates the IdP session — especially important for shared workstations in financial or healthcare environments.

### 9\. Avoid social providers for enterprise or regulated portals

Social login (Google, Facebook, LinkedIn, Twitter/X) provides no enterprise MFA enforcement, no group claims, and no compliance guarantees. Reserve social login for low-sensitivity consumer-facing portals only.

### 10\. Manage duplicate contact records proactively

A unique email is required per authenticated user. Implement a CRM data quality process to detect and merge duplicate contact records before they block user authentication.

## Which Authentication Method Should You Choose?

Here is a quick decision guide based on portal type and requirements:

**For enterprise or partner portals (B2B):** → Use **SAML 2.0** with Microsoft Entra ID or AD FS. Enable Conditional Access and MFA at the IdP. This is the lowest-risk, highest-compliance option available in Power Pages.

**For external customer portals (B2C):** → Use **OIDC with Azure AD B2C** or Microsoft Entra External ID. Override the implicit grant default to use authorization code flow. Configure B2C policies to enforce MFA and password complexity.

**For regulated industries (banking, healthcare, finance):** → Use **SAML 2.0** as the primary protocol. Formally document PKCE absence as a residual risk for any OIDC deployment. Disable local auth, social login, and open registration entirely.

**For public community or consumer portals:** → **Social login (OAuth 2.0)** is acceptable if the portal holds no sensitive data. Combine with open registration (invitation-code mode recommended). Implement CAPTCHA.

**For internal development or demos:** → **Local authentication** is acceptable for non-production environments. Ensure `IsDemoMode` is never set to `True` in any environment that connects to real data.

---

## Frequently Asked Questions

### Can I use multiple identity providers at the same time in Power Pages?

Yes. Power Pages allows you to configure multiple identity providers simultaneously. Users will see a sign-in page listing all available providers and can choose which one to use. Each provider is configured independently with its own claims mapping.

### Can Power Pages work with Azure AD B2C?

Yes. Azure AD B2C is one of the built-in OIDC providers with dedicated configuration support in Power Pages. B2C allows you to define custom user flows or policies for sign-up, sign-in, password reset, and profile editing, while also supporting social identity federation (Google, Facebook, etc.) through B2C itself — which is more controlled than direct social login in Power Pages.

### What is the difference between OIDC and SAML 2.0 in Power Pages?

Both are federated authentication protocols that delegate identity verification to an external provider. OIDC is a JSON/JWT-based protocol built on OAuth 2.0 — it is more modern and easier to configure for cloud-native scenarios. SAML 2.0 is an older XML-based protocol with stronger enterprise tooling, POST binding (no tokens in URLs), and mature SLO support. For regulated enterprise scenarios, SAML 2.0 is generally preferred. For cloud-native B2C portals, OIDC with Azure AD B2C is the more common choice.

### What happens when a user signs in with a social provider for the first time?

If open registration is enabled, Power Pages creates a new Dataverse contact record for the user using the email claim from the social token. If open registration is disabled, the user must have a pre-existing contact record with a matching email address — otherwise, sign-in fails. The social identity is then linked to that contact record.

### How do web roles get assigned to users in Power Pages?

Web roles can be assigned in several ways: manually by an administrator in the Dataverse portal management app; automatically via claims mapping if the token contains group or role claims (SAML 2.0 and OIDC); during invitation code redemption if the pre-provisioned contact record already has web roles assigned; or programmatically via Dataverse API or Power Automate workflows.

## References and Further Reading

### **Official Microsoft Documentation**

-   [Overview of authentication in Power Pages](https://learn.microsoft.com/en-us/power-pages/security/authentication/) — Microsoft Learn

-   [Set up an OpenID Connect provider](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-provider) — Microsoft Learn
-   [Configure a SAML 2.0 provider with Microsoft Entra ID](https://learn.microsoft.com/en-us/power-pages/security/authentication/saml2-settings-azure-ad) — Microsoft Learn

-   [Configure a SAML 2.0 provider with AD FS](https://learn.microsoft.com/en-us/power-pages/security/authentication/saml2-settings) — Microsoft Learn
-   [Configure the Azure AD B2C provider](https://learn.microsoft.com/en-us/power-apps/maker/portals/configure/configure-azure-ad-b2c-provider) — Microsoft Learn

-   [Local authentication, registration, and other settings](https://learn.microsoft.com/en-us/power-pages/security/authentication/set-authentication-identity) — Microsoft Learn
-   [Configure an OAuth 2.0 provider](https://learn.microsoft.com/en-us/power-pages/security/authentication/oauth2-provider) — Microsoft Learn

-   [Migrate identity providers to Azure AD B2C](https://learn.microsoft.com/en-us/power-pages/security/authentication/migrate-identity-providers) — Microsoft Learn
-   [Power Pages security overview](https://learn.microsoft.com/en-us/power-pages/security/power-pages-security) — Microsoft Learn

-   [Page permissions in Power Pages](https://learn.microsoft.com/en-us/power-pages/security/page-security) — Microsoft Learn
-   [Create web roles in Power Pages](https://learn.microsoft.com/en-us/power-pages/security/create-web-roles) — Microsoft Learn

### **Standards and Security References**

-   [OpenID Connect Core 1.0 Specification](https://openid.net/specs/openid-connect-core-1_0.html) — OpenID Foundation

-   [OAuth 2.0 Security Best Current Practice (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700) — IETF
-   [SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) — OASIS

-   [PKCE for OAuth Public Clients (RFC 7636)](https://datatracker.ietf.org/doc/html/rfc7636) — IETF
-   [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/) — Microsoft Learn

-   [Azure AD B2C documentation](https://learn.microsoft.com/en-us/azure/active-directory-b2c/) — Microsoft Learn

### **Related Articles**

-   [Power Pages security overview and best practices](https://learn.microsoft.com/en-us/power-pages/security/power-pages-security)

-   [Configuring site settings in Power Pages](https://learn.microsoft.com/en-us/power-pages/configure/configure-site-settings)
-   [Power Pages web roles and table permissions](https://learn.microsoft.com/en-us/power-pages/security/table-permissions)

-   [Microsoft Entra Conditional Access documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

### *Related*

[![](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/02/terraform-azure-power-platform-featured.png?fit=768%2C512&ssl=1&resize=350%2C200)](https://aidevme.com/terraform-azure-power-platform-developers/ "Terraform for Power Platform Developers: Provision Azure Resources &amp; Automate CI/CD")

#### [Terraform for Power Platform Developers: Provision Azure Resources & Automate CI/CD](https://aidevme.com/terraform-azure-power-platform-developers/ "Terraform for Power Platform Developers: Provision Azure Resources &amp; Automate CI/CD")

This guide shows Power Platform developers how to use Terraform to provision and manage Azure resources — Key Vault, Storage, Function Apps, API Management, and App Registrations — and integrate the full infrastructure lifecycle into GitHub Actions and Azure DevOps pipelines. All code samples are production-ready and environment-parameterized.

February 19, 2026

In "DevOps"

[![Comic-style illustration of a Power Platform developer using AI-assisted coding, showing human and AI collaboration in enterprise software development](https://i0.wp.com/aidevme.com/wp-content/uploads/2026/01/welcome-to-aidevme-feature.png?fit=1200%2C800&ssl=1&resize=350%2C200)](https://aidevme.com/welcome-to-ai-dev-me-power-platform-development-with-ai-tools/ "Welcome to AI Dev Me: Power Platform Development with AI Tools")

#### [Welcome to AI Dev Me: Power Platform Development with AI Tools](https://aidevme.com/welcome-to-ai-dev-me-power-platform-development-with-ai-tools/ "Welcome to AI Dev Me: Power Platform Development with AI Tools")

Where Microsoft Technology Meets Intelligent Coding I’m Zsolt Zombik, a senior Power Platform developer at ELCA Informatik AG, working at the intersection of Microsoft Power Platform and AI-assisted software development. This blog is not about shortcuts, hype, or “10x developer” promises. It is about building real, enterprise-grade Power Platform solutions—applications…

January 5, 2026

In "AI in Development"

---
> **Note:** This page contains 4 cross-origin iframe(s) that could not be accessed due to browser security policies. Some content may be missing. Links to these iframes have been preserved where possible.


---
Source: [Power Pages Authentication Methods: The Complete Guide (2026)](https://aidevme.com/power-pages-authentication-methods-the-complete-guide-2026/)