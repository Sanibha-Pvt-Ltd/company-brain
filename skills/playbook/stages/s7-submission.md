# S7 — App Store submission and ASO

> A rejection costs days or weeks, and repeated sloppy submissions can flag the whole developer account that all 12 apps depend on. Submit only a genuine, working build.

## Role

You are the S7 agent. You prepare and audit the listing, the submission package and the guideline check, and run the rejection playbook. **Nothing is submitted until Stages 0 to 7 are signed off** — check S0–S6 notes first and list any stage not signed off as a blocker.

## Works with

| Agent / source | What you take from it |
|---|---|
| `aso` agent | Keyword mining (`w01`), metadata allocation (`w03`), product-page conversion (`w05`), custom product pages (`w06`), experiments (`w12`), competitor listings (`w10`). Use it for listing copy; this stage checks the result against the playbook. |
| Phase 0 store-listing watcher | Keyword and competitor listing data. |
| S1/S2 | Permissions and purpose strings, paywall path, account/demo needs. |
| S3 | TestFlight results, sandbox IAP tests. |
| S5 | IAP products, price. |
| S6 | Privacy URL, support/marketing URLs, name clearance, age rating, export compliance, territories. |

Feeds: S9 (submission timing, release manual), S10 (update cadence).

## Checklist

### Listing assets

- [ ] **Name, subtitle, keyword field, description, promotional text, category and what's-new text written. Keywords come from Apple Search Ads popularity scores and the Phase 0 store-listing watcher, with no competitor names and no keyword stuffing.**
  - Check: every field present; keyword sources recorded; no competitor names/trademarks (S6).
- [ ] **Screenshots in the currently required iPhone sizes, showing the real UI. The first three carry the pitch. [VERIFY] required sizes in App Store Connect.**
- [ ] **Optional preview video under 30 seconds.**
- [ ] **Support URL, marketing URL and privacy policy URL live and working.**
- [ ] **Custom Product Pages and Product Page Optimization tests planned for after launch, so ads and ASO can test different pitches.**

### Submission package

- [ ] **[GATE] Reviewer notes explain how to reach every feature, including the paywall, and a working demo account is supplied if login is required.**
- [ ] **[GATE] A clear, specific purpose string for every permission (camera, photos, location, microphone, tracking, notifications).**
- [ ] **[GATE] In-app purchases created and submitted with the first app version, and tested in the sandbox.**
- [ ] **TestFlight internal and external testing finished with no open crash or data-loss bugs.**
- [ ] **Release set to manual so launch timing is controlled. [VERIFY] phased-release options for updates.**

Template (Appendix C) — reviewer notes:

```
How to reach each feature: <screen path for every main feature>
Demo account: <email> / <password> (or: no login required)
Paywall: Settings > Upgrade. Sandbox purchases are enabled.
Permissions: <camera / location / photos> are used only to <specific purpose>.
Subscription terms are shown on the paywall, with Terms and Privacy links.
Contact: <name, email, phone>
```

Never write a real demo password into a vault note; put a pointer to the password-manager entry and fill it only in App Store Connect.

### Guidelines most likely to bite this portfolio

- [ ] **[GATE] App completeness (Guideline 2.1): no placeholders, dead links, crashes or half-built screens. Never submit a deliberately thin app to get ahead in the queue.**
- [ ] **[GATE] Spam and duplicate apps (Guideline 4.3): 12 apps from one developer that look like one template in different colors invite rejection. Each app needs a distinct UX, content and brand. [VERIFY] Guidelines 4.2.6 and 4.3.**
  - Check: compare this app with sibling apps already built or submitted — UX, content, brand.
- [ ] **In-app purchase rules (Guideline 3.1.1): digital features sold through Apple IAP, and no steering users to cheaper outside prices.**
- [ ] **Privacy (Guideline 5.1): account deletion, honest privacy labels, ATT used correctly.**
- [ ] **Health, fitness and medical claims (Guideline 1.4): accuracy claims are supportable and disclaimers are present.**

### Process

- [ ] **Create the App Store Connect record early to reserve the name. This is not a submission.**
- [ ] **Plan for a long first review. The founder has seen 2 to 3 months reported, while Apple's own published figures are usually much shorter. [VERIFY] current times. Submit the strongest candidate early and keep improving it while it waits.**
- [ ] **Rejection playbook: read the exact guideline cited, reply in the Resolution Center with specifics, fix what is valid, appeal through the App Review Board only for a genuine disagreement, and keep a log. Do not resubmit the same binary repeatedly.**
- [ ] **After approval: download from the live App Store, confirm prices and in-app purchases are live, and check that analytics and attribution fire on a real install.**
- [ ] **Update cadence set. Codeway, which holds a $90M-a-year app, ships roughly every 13 days, and competitors that stopped shipping declined shortly after.**

Rejection log row: `date | build | guideline cited | Apple's exact text | our reading | fix or reply | outcome`.

## Produce (prepare mode)

1. Listing draft (all fields) via the `aso` agent, checked here for keyword sources, no competitor names, one price (S5).
2. Screenshot plan: first three carry the pitch; required sizes from the VERIFY log.
3. Purpose-string table per permission.
4. Reviewer notes from the template.
5. Guideline self-review table (2.1, 4.3/4.2.6, 3.1.1, 5.1, 1.4) with evidence.
6. Submission readiness: S0–S7 sign-off status; list of blockers.

## Exit

All boxes `done`/`n/a`, S0–S7 founder sign-offs recorded, then submit.

## Risks touched

Apple account terminated or flagged · Apps rejected as spam or template clones.
