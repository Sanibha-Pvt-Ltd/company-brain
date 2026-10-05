---
type: app
category: document-scanner
app: Scanner App
app_store_id: "[UNKNOWN]"
member: harshil
updated: 2026-10-05
status: draft
scope: screens-only
sources: [final_analysis.md, screenshots:15]
reviews_analysed: 0
screens_analysed: 15
---

# Scanner App — manual research checked against screenshots

Basis: Harshil's manual notes (`harshil-screenshots/scanning/final_analysis.md`), checked against 15 in-app screenshots in `harshil-screenshots/scanning/Scanner App/` (IMG_5328–5342, captured 2 Oct 2026, 8:32–8:38 per status bar). Prices are ₹ as displayed (India storefront); US prices [UNKNOWN]. No reviews or listing data used. App name on screens: "Scanner App" / "Scanner"; version 3.1.8.0 (IMG_5339).

## Manual findings vs screenshots

| Manual finding | Screenshot check | Verdict |
|---|---|---|
| Onboarding requires multiple clicks | ATT prompt (5328) + 5-page carousel, each with Continue (5329–5333), then home (5334) | Confirmed: 1 system prompt + 5 Continue taps before home [OBSERVED] |
| No mandatory sign-in | No sign-in screen in any of the 15; Settings has no account/login row (5337–5339) | Confirmed [OBSERVED] |
| No immediate paywall | Home reached straight after carousel (5334); paywall (5336) appears after first doc exists (5335) | Confirmed, by filename/timestamp order [OBSERVED] |
| Some usage limits communicated | Pro list: "Unlimited Documents", "Remove Watermark" (5337); paywall: "Unlimited Scans" (5336). Exact free limit not shown | Partly: limit implied, number [UNKNOWN] |
| Free trial appears to start automatically when nudged | Screen "7-day trial is enabled" (5342, 8:38) with a toggle that is drawn in the off position. What triggered it is not captured | Screen exists [OBSERVED]; whether a trial actually started [UNKNOWN] |
| 7-day access for ₹49, then ~₹999/week | "7-Day Full Access ₹49 — Then ₹999/week"; footer "First 7 days at ₹49. Auto-renews at ₹999/week. No commitment." (5336) | Confirmed exactly [OBSERVED] |
| Another price ~₹1,499/week | Not in any screenshot | Manual-only, unverified |
| Pricing aggressive for a one-time utility | ₹999/week renewal shown (5336) | Opinion; price fact confirmed |
| Clean, simple UI; scan → PDF straightforward | Home: search, Recent, + button, tabs Home/Files/Tools/Account (5334, 5341); editor with filters Original/Photocopier/Auto/Lighten/Magic and Add/Edit PDF/Share/Text Recognition/More (5335) | Confirmed [OBSERVED] |
| Switching camera vs file upload feels smooth | Empty state copy: "Tap to scan from your camera, imported photos or files." (5334). Picker itself not captured | Copy confirmed; picker [UNKNOWN] |

## Screen map

| # | File | Stage | What user sees / verbatim copy | Ask / friction | Tag |
|---|---|---|---|---|---|
| 1 | 5328 | first-launch | ATT: "For a better personalized experience you can approve IDFA sharing." behind it "Preparing your workspace…" | Tracking ask before any value | [OBSERVED] |
| 2 | 5329 | onboarding 1/5 | "Welcome to Scanner App", "AI-powered scanner and PDF Editor", badge "4.8 3.5M total rating" | Social proof claim, not verified against listing | [OBSERVED] |
| 3 | 5330 | onboarding 2/5 | "Scan, Edit, and Share" — "Multipage scanning / Full PDF Editor / Export to PDF, JPG, DOC, and more" | Continue | [OBSERVED] |
| 4 | 5331 | onboarding 3/5 | "AI Scan Straightener" | Continue | [OBSERVED] |
| 5 | 5332 | onboarding 4/5 | "Go Paper-Free", "with #1 scanner app." | Unverified "#1" claim | [OBSERVED] |
| 6 | 5333 | onboarding 5/5 | "Top Rated by Scanner Users", 5★ testimonial "Jenny87" | Continue | [OBSERVED] |
| 7 | 5334 | core | Home empty: "You don't have any scans", PRO badge top-left | — | [OBSERVED] |
| 8 | 5335 | result | "Oct 2, Doc 1" scan in editor + native "Enjoying Scanner?" rating prompt | Rating ask right after first scan | [OBSERVED] |
| 9 | 5336 | paywall | "Unlimited Access", "Tap Continue for 7-day access ⚡", ₹49 then ₹999/week, X top-left, Restore | Soft (X visible). "No commitment" next to auto-renew | [OBSERVED] |
| 10–12 | 5337–5339 | settings | Pro card, Support, Copy User ID, App PIN, Get Pro, Restore, Start App With, Picture Quality HD, FAQ, Rate, Share, Contact, Privacy, Terms; v3.1.8.0 | "Get Pro" also in settings | [OBSERVED] |
| 13 | 5340 | result | "Oct 2, Doc 2" + custom sheet "Did Scanner App make things easier? 💙 … Review Us" | Second rating ask, custom pre-prompt | [OBSERVED] |
| 14 | 5341 | core | Home with 2 docs: Doc 2 5.83 MB, Doc 1 665.43 KB | — | [OBSERVED] |
| 15 | 5342 | upsell | "7-day trial is enabled" | Trigger unknown; toggle drawn off | [OBSERVED] |

## Lens measures

1. **First win:** first scan in editor (5335) — before paywall. Taps from launch: 1 ATT + 5 Continue + scan flow ([UNKNOWN] capture taps).
2. **Ask ledger:** tracking (nothing given yet) → 5 carousel taps (nothing given) → scan → rating prompt (just got 1 scan) → paywall → second rating prompt after Doc 2.
3. **Abstractions:** filter modes (Original/Photocopier/Auto/Lighten/Magic). Job needs at most one auto mode [INFERRED].
4. **Feel-good:** scan result appears free, saved to Recent with size.
5. **Feel-bad:** ATT before value; "No commitment" beside ₹999/week auto-renew; 2 rating asks in ~5 minutes (8:33, 8:37).
6. **Paywall:** soft, after first scan, ₹49 7-day paid intro then ₹999/week. Labelled "access", not "free trial", but later screen says "7-day trial is enabled".
7. **Repeat cost:** + button on every tab (5334, 5337). Retention hooks not seen.
8. **Feature map:** table stakes: scan, multipage, filters, share, OCR, PDF export. Differentiators claimed: "AI Scan Straightener". Bloat: [UNKNOWN] (Tools tab not captured).

## Keep / Kill / Different

- **Keep:** no sign-in; scan before paywall; simple 4-tab + big + layout.
- **Kill:** ATT on first launch (5328); "No commitment" copy beside auto-renew (5336); two rating asks in first session (5335, 5340).
- **Different:** show the free limit in plain words before scan 1, not via "Unlimited"/"Remove Watermark" on the paywall [INFERRED].

## Open / unverified
- ₹1,499/week price (manual only). Free scan limit. What triggers "7-day trial is enabled". Watermark on free export (implied by "Remove Watermark", not seen).
