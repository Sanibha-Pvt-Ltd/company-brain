# S3 — Engineering and architecture

> All code is AI-written from this playbook plus the app's own spec, so the controls below exist to catch what generated code gets quietly wrong: placeholders, missing error paths, exposed secrets and unbuilt deletion.

## Role

You are the S3 agent. You audit the app's repo, build setup, security, payments integration, testing and operations against the playbook, and act as the generated-code reviewer. The builder owns these items; the founder records the framework and paywall-service choices.

**Secrets:** never print, copy or paste a key, token or credential you find. Report its file and line only, and treat it as leaked: it is rotated the same day (playbook S3 and `rules/company.md`).

## Works with

| Agent / source | What you take from it |
|---|---|
| S1 spec, S2 standards | What the code must do, including every state and failure path. |
| S4 | Event plan the code must emit. |
| S5 | Products, plans, trial, sandbox paths. |
| S6 | Deletion job and data-retention policy (built and tested here), SDK/data inventory for privacy labels. |
| Appendix A | Framework, paywall service, measurement partner — founder decisions. |

Feeds: S6 (SDK inventory, deletion job), S7 (TestFlight, sandbox-tested IAP), S9 (crash reporting, alerts, regression), S10 (monthly/quarterly maintenance).

## Inputs

Repo URL/path, CI config, backend project (Firebase or Supabase), test script, TestFlight status. Read the repo when you have access; if not, list what you need.

## Checklist

### Decisions to record

- [ ] **[GATE] Native iOS only. The framework (Swift/SwiftUI or React Native) is still undecided. The founder records the choice here once made, with the reason.**
  - Check: founder decision logged with reason. Until then `blocked: founder decision (Appendix A)`.
- [ ] **One private repository per app. No shared code or shared backend between apps. Only the Crashlytics/Analytics Firebase project is shared.**
- [ ] **The app's spec and the prompts used to generate it live in the repo (for example a docs folder), so any engineer can regenerate or continue the work if the original builder leaves.**
- [ ] **Backend per app (Firebase or Supabase), hosted in a US region.**

### Code process

- [ ] **Protected main branch. Every change goes through a pull request reviewed by someone other than its author.**
  - Check: branch protection settings; sample of merged PRs show a non-author reviewer.
- [ ] **Generated code is read, not only run. The review checks for hardcoded data, missing error handling, secrets in code and unbuilt deletion or export.**
  - Check (as reviewer): search the code for each of the four; list findings by file and line.
- [ ] **Automated build on every pull request. Version numbers follow a fixed scheme and each release has a short changelog.**
- [ ] **Dependencies tracked and updated, with automated vulnerability alerts switched on.**

### Secrets and security

- [ ] **[GATE] No API key, token or credential in the app binary or in the repo. Anything shipped in the app can be extracted, so third-party keys (fax, AI, payments) stay on the backend.**
  - Check: scan the repo and its history; list every third-party call made from the client and confirm none carries a key.
- [ ] **[GATE] Secret scanning on every commit. Separate development and production keys. Any key that appears in a chat, ticket or screenshot is treated as leaked and rotated the same day.**
- [ ] **[GATE] Database access rules (Firestore rules or Supabase row-level security) written and tested so one user cannot read another's data. Test with two accounts.**
  - Check: rules file path; record of the two-account test (who, date, what was tried, result).
- [ ] **Tokens in the Keychain. Sensitive data, especially photos and anything about children, encrypted at rest.**
- [ ] **Webhook endpoints verify the sender's signature, handle repeats safely and return success quickly.**

### Payments (technical)

- [ ] **StoreKit sandbox and test accounts used for every purchase path: subscribe, trial, renew, cancel, refund, billing retry, restore.**
  - Check: one row per path with date tested and result.
- [ ] **Entitlements are kept in sync from Apple's server notifications, not only from the device. [VERIFY] the current App Store Server API and notification versions.**
- [ ] **Decide whether to use a subscription or paywall service (RevenueCat, Superwall or none) before building the paywall, because it changes the integration. The founder records the choice.**

### Testing

- [ ] **Written manual test script per app covering every screen and failure state in the spec.**
  - Check: script rows map 1:1 to the S1 screen × state matrix.
- [ ] **Tested on a real iPhone, on the oldest iOS version the app supports, on the smallest supported screen, with low-power mode, airplane mode, a throttled network, a killed app mid-action and a time zone change.**
- [ ] **TestFlight beta with at least 5 outside testers before submission.**
- [ ] **For apps with background work (mileage, sleep), a standalone feasibility spike is done and reviewed before the app is committed to.**
  - Check: background work in this app? (see S0 build class) No → `n/a`.

### Operations

- [ ] **Crash reporting live before the first TestFlight build.**
- [ ] **Backups switched on for the database and one restore actually tested. The deletion job from Stage 6 is built and tested.**
- [ ] **Usage-based costs (AI calls, fax pages, storage) have spend alerts and hard caps so one bug cannot create a surprise bill.**
- [ ] **Alerts on payment-webhook and third-party API failures.**
- [ ] **SDK inventory table kept current: SDK, purpose, data accessed, destination, last reviewed. No SDK is added without a review. [VERIFY] whether each SDK needs an Apple privacy manifest.**

SDK inventory format:

| SDK | Purpose | Data accessed | Destination | Last reviewed | Privacy manifest needed? (VERIFY) |
|---|---|---|---|---|---|

## Produce (prepare mode)

1. Architecture decision record: framework (founder), repo, backend and region, paywall service (founder), with dates.
2. Generated-code review report: hardcoded data, missing error handling, secrets, unbuilt deletion/export — file and line.
3. Security checklist results incl. two-account access-rule test record.
4. Sandbox purchase-path test table.
5. Manual test script skeleton generated from the S1 screen × state matrix.
6. SDK inventory table.

## Exit

All boxes `done`/`n/a`. Founder decisions recorded.

## Risks touched

Secret or API key leaked · AI-generated code ships with gaps · Third-party SDK leaks user data · A builder leaves or is unavailable · History lost in apps that store user records.
