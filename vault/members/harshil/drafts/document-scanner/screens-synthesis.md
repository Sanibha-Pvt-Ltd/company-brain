---
type: category-screens
category: document-scanner
member: harshil
updated: 2026-10-05
status: draft
scope: screens-only
sources: [final_analysis.md, screenshots:34]
---

# Document scanner apps — synthesis (manual research, screenshot-checked)

Primary basis: Harshil's manual research `harshil-screenshots/scanning/final_analysis.md` (5 apps). Each claim was checked against 34 in-app screenshots (captured 2 Oct 2026). No App Store reviews, listings, downloads or revenue data were used — those sections are [UNKNOWN]. ₹ prices are India storefront; US prices [UNKNOWN].

App notes:
- [[members/harshil/apps/document-scanner/scanner-app]] — 15 screens
- [[members/harshil/apps/document-scanner/iscanner]] — 5 screens
- [[members/harshil/apps/document-scanner/adobe-acrobat]] — 9 screens
- [[members/harshil/apps/document-scanner/adobe-scan]] — 5 screens
- Tiny Scanner — **no screenshots**; manual notes only (below)

## Corrections to the manual notes (screenshots disagree)

| App | Manual said | Screenshots show |
|---|---|---|
| Adobe Acrobat | ~₹599/month | **₹349.00/month** (IMG_5316, 5321). Your handwritten notes (visible in Scanner App IMG_5335) also say 349 — typed version is a typo |
| iScanner | 7-day free trial, then ~₹599/week | ₹599/week shown with "Try it for free!" (no length, IMG_5344). The only stated trial is **3-Day Free Trial then ₹499/week** (IMG_5345–5346). No 7-day seen |
| iScanner | another price ~₹1,499/week | **₹1,499.00 per year** (= ₹28.57/week, "SAVE 94%") (IMG_5345–5346) |
| Adobe Scan | Plus ~₹499/month | Confirmed, plus a yearly option **₹1,999/yr** not in notes (IMG_5324) |
| iScanner | (not in notes) | Third offer: "56% OFF" ~~₹15,588~~ **₹6,900/year**, countdown, "This offer expires once dismissed", button "Miss This Offer" (IMG_5347) |

Not verifiable from screenshots (kept as manual-only): Scanner App ₹1,499/week; iScanner load time, 4-step onboarding, 1 free page, Fax/Invoice/AI tools, home layout; Adobe Scan free basic PDF and repeated nudges; all of Tiny Scanner.

## Cross-app table [OBSERVED unless marked]

| | Scanner App | iScanner | Adobe Acrobat | Adobe Scan | Tiny Scanner (manual only) |
|---|---|---|---|---|---|
| Account | None | None seen | Asked first screen, skippable (X) | **Required**, no skip seen | [UNKNOWN] |
| Asks before value | ATT + 5 carousel taps | Welcome + paywall(s) | Sign-in + paywall | Sign-in + paywall + camera/notifications | "5 clicks onboarding" |
| Paywall placement | After first scan | Right after welcome; 3 offers in session | Before first use (plan table) | After sign-in, before camera | "Nudging to buy pro" |
| Dismiss | X top-left | Small "Cancel" text | X | X | [UNKNOWN] |
| Trial | ₹49 for 7 days ("7-day access") | 3-day free | 7-day free | 7-day free | [UNKNOWN] |
| Renewal price | ₹999/week | ₹599/wk or ₹2,999/yr; ₹499/wk or ₹1,499/yr; ₹6,900/yr offer | ₹349/mo or ₹2,599/yr | Plus ₹499/mo or ₹1,999/yr; Premium ₹849/mo | "4$ and 49" (as written; unit/period unclear) |
| Free scan | Yes (limit [UNKNOWN]; "Remove Watermark" is Pro) | ~1 page (manual only) | "New scan" has no crown; "Create PDF" is premium | Basic scan free (manual only) | 1 page (manual) |
| Dark patterns seen | ATT first; "No commitment" next to auto-renew; 2 rating asks in 5 min | Countdown "expires once dismissed"; "Miss This Offer"; low-contrast Cancel; shifting prices | AI upsell on first file open | Sign-in wall; notifications bundled with camera | [UNKNOWN] |

## Patterns

1. **Weekly pricing is the indie norm; Adobe sells monthly/yearly.** Scanner App ₹999/week, iScanner ₹599 or ₹499/week vs Acrobat ₹349/month and Adobe Scan ₹499–849/month. Your note "aggressive for a one-time-use utility" holds on these numbers: Scanner App's one week (₹999) is more than Acrobat's ₹349 month [INFERRED from displayed prices].
2. **Scan-first beats account-first.** Scanner App gives a scan with no account and no paywall first; Adobe Scan blocks everything behind sign-in; Acrobat buries "New scan" in a + menu (IMG_5322).
3. **Indie apps lean on urgency and repeated offers; Adobe uses clear tables and plain trial terms.** iScanner showed 3 paywalls with different prices in 8 minutes (8:40–8:48). Adobe both show Free vs paid tables and "Billing begins when your free trial ends".
4. **Feature bloat around a simple job.** iScanner tiles include CVs, PPT, TXT, EDU bonus; Acrobat adds PDF Spaces, podcast, AI Assistant; Adobe Scan adds Ask AI. Scanner App stays closest to scan → PDF.

## What Sanibha would do [INFERRED — proposal, not evidence]

- **Our first minute:** open → camera (permission asked on tap) → auto-edge scan → PDF saved locally. No account, no ATT, no carousel.
- **Monetize honestly:** one paywall after the first scan, one price everywhere, real X, trial terms in plain words. No countdown, no "Miss This Offer".
- **Free tier stated up front** (e.g., N free exports) instead of discovering it through "Unlimited"/"Remove Watermark".
- **Refuse:** sign-in wall, bundled notification ask, AI/podcast/CV extras in the MVP.

## Open questions (need review mining / listing data / hands-on)
1. US prices for all 5 apps (all screens are ₹).
2. Tiny Scanner: needs screenshots; "4$ and 49" needs clarifying (price and period).
3. Scanner App ₹1,499/week and the trigger of "7-day trial is enabled".
4. Free limits: Scanner App's exact cap, iScanner's 1 page, Adobe Scan's free PDF export.
5. Ratings/download claims on onboarding (Scanner App "4.8, 3.5M", iScanner "130M+ users, 4.8") not checked against listings.

## What would change the call
- 1–2★ reviews showing users are fine with weekly pricing → weakens pattern 1.
- Adobe Scan's free tier turning out unlimited with no watermark → our free-tier edge shrinks.

## Next stage
Run `scripts/fetch-app.py` for these 5 apps to get `negatives.md` + `listing.json` (US), then stage A A6 failure mining and stage B market.
