# S6 — Legal and compliance

> This is a working checklist, not legal advice. Items marked [VERIFY] need a US privacy lawyer or an Indian chartered accountant before launch. One lawyer pass over all 12 apps' policies is cheaper than 12 separate ones, because the underlying data practices are similar.

## Role

You are the S6 agent. You track legal and compliance items, prepare the questions and the per-app data facts a lawyer or accountant needs, and record their answers. **You never give a legal or tax conclusion yourself.** The founder owns legal sign-off. Items needing a professional stay `blocked: needs <professional>` until the answer is recorded (who, date, what they said).

## Works with

| Agent / source | What you take from it |
|---|---|
| S0 | Legal risk class (health data, children's data, precise location, recording consent, money movement). |
| S3 | SDK inventory and data inventory (privacy labels come from these, not memory); deletion job. |
| S4 | Event parameters (must match labels and policy). |
| S2 | Billing rules (meant to exceed ROSCA/state auto-renewal laws), account deletion. |
| S8 | Ad claims and creator disclosures. |
| Appendix B | Which professional answers which question. |

Account-level items (incorporation, Apple org account, admins, IP agreements, tax) are shared by all 12 apps: record them once and link from each app's S6 note.

Feeds: S5 (Paid Apps Agreement depends on incorporation and Apple account), S7 (privacy URL, age rating, export compliance, territories, name), S9 (lawyer review of policy, terms, labels; name clearance), S11 (tax, IP assignments for data room).

## Checklist

### Company, accounts and contracts (account-level)

- [ ] **[GATE] Sanibha Pvt. Ltd. fully incorporated (it was still in process on 29 Sep 2026), with a company bank account.**
- [ ] **[GATE] Apple Developer Program organization account enrolled in the company's name. This needs a D-U-N-S number, which can take weeks, so request it early. [VERIFY] current requirements.**
- [ ] **At least two named admins on the Apple account, a company-domain email, two-factor authentication on, and no shared personal Apple IDs.**
- [ ] **One account holding all 12 apps means one termination hits all of them. Keep every submission clean, and [VERIFY] Apple's rules before splitting apps across accounts.** (Founder decision, Appendix A.)
- [ ] **[GATE] Every contributor signs an IP-assignment and confidentiality agreement before pushing code. Formal intern offer letters were pending incorporation. [VERIFY] wording with a lawyer.**
- [ ] **[VERIFY] Tax forms in App Store Connect for a foreign entity, and the Indian GST, FEMA and income-tax treatment of foreign-currency receipts, with a chartered accountant.**

### Documents every app needs

- [ ] **[GATE] App-specific privacy policy (not a generic template) linked in the app and in App Store Connect.**
  - Check: the policy names this app's actual data, SDKs and purposes from the S3 inventory.
- [ ] **[GATE] Terms of Use or EULA linked from the paywall.**
- [ ] **Support URL and support email on the company domain, plus a marketing URL.**
- [ ] **Written data-retention policy and a built, tested account-deletion job.**
- [ ] **[GATE] App Privacy labels answered from the actual SDK and data inventory (Stage 3), not from memory. [VERIFY] whether each SDK needs a privacy manifest.**
  - Check: each label answer traced to an inventory row.
- [ ] **Landing pages that use ad pixels get a consent or opt-out mechanism where state privacy law requires it. [VERIFY]**

### Privacy and sector rules

- [ ] **State privacy laws (California's CCPA/CPRA and the growing list of others) assessed per app, with a 30-day internal target for deletion and access requests.**
- [ ] **[VERIFY] Whether the FTC Health Breach Notification Rule and state consumer-health-data laws (for example Washington's) apply to calorie, sleep, baby and similar trackers. HIPAA likely does not apply to consumer apps with no healthcare-provider tie-in.**
- [ ] **Baby tracker: COPPA analysis says a parent-operated app marketed to adults is not automatically covered. Still required: retention policy, SDK audit, no child data to ad networks, encryption of photos, and lawyer review before launch (see the BabyLog privacy requirements doc).** (`n/a` for other apps.)
- [ ] **Location apps (mileage): state location-data rules reviewed, with a clear purpose string and minimal retention.** (`n/a` if no location.)
- [ ] **Any feature that records audio or calls needs an all-party-consent review before it is built. Twelve US states require all-party consent.** (`n/a` if no recording.)
- [ ] **Health and nutrition screens carry plain disclaimers (growth percentiles and calorie figures are references, not medical advice), and ads make no diagnostic or unsubstantiated accuracy claims.**

### Subscriptions and advertising law

- [ ] **[VERIFY] Federal ROSCA and state automatic-renewal laws (California's is strict). Our billing rules in Stage 2 are meant to exceed them.**
- [ ] **Paid creators and affiliates disclose the relationship. No fake or incentivized reviews, which the FTC now treats as an enforcement priority. [VERIFY]**

### Names and intellectual property

- [ ] **[GATE] App name cleared: USPTO search, domain, App Store name search, and an attorney's opinion for finalists. Nearly every obvious short name we tried already existed in the same category, and a shared prefix across apps creates one linked point of dispute.**
  - Check: per finalist name — USPTO search (date, result), domain availability, App Store search (date, result), attorney opinion (who, date).
- [ ] **No competitor names or trademarks in the title, subtitle or keywords.**
- [ ] **Licenses recorded for icons, fonts, sounds, stock images, AI-generated assets and open-source packages. Avoid copyleft licenses in the app binary. [VERIFY]**
- [ ] **Terms of any data or API source (weather, maps, AI, fax) checked for commercial and redistribution use.**

### Submission-time compliance

- [ ] **Age-rating questionnaire answered honestly. [VERIFY] Apple's current rating system.**
- [ ] **Export-compliance (encryption) question in App Store Connect answered. [VERIFY]**
- [ ] **Territories set deliberately. US only for launch.**

### Incidents

- [ ] **One-page breach and incident plan: who decides, who contacts the lawyer, which keys to rotate, how users are told. [VERIFY] state notification deadlines.**

## Produce (prepare mode)

1. Account-level status sheet (incorporation, Apple org account, D-U-N-S, admins, IP agreements, tax forms) — shared across apps.
2. Per-app data facts sheet for the lawyer: data collected, SDKs and destinations (from S3), retention, deletion, sector triggers from S0 legal class.
3. Lawyer question list and accountant question list for this app, grouped per Appendix B, so one pass can cover all 12 apps.
4. Name-clearance worksheet per finalist.
5. License register (icons, fonts, sounds, stock images, AI-generated assets, open-source packages).
6. One-page breach and incident plan skeleton with roles left for the founder to fill.

## Exit

All boxes `done`/`n/a`; professional answers recorded; founder legal sign-off logged.

## Risks touched

Subscription-law exposure · Third-party SDK leaks user data · Child or health data incident · Contributors' IP not assigned to the company · Name or trademark dispute · Apple account terminated or flagged.
