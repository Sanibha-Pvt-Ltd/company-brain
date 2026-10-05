---
type: app
category: document-scanner
app: iScanner
app_store_id: "[UNKNOWN]"
member: harshil
updated: 2026-10-05
status: draft
scope: screens-only
sources: [final_analysis.md, screenshots:5]
reviews_analysed: 0
screens_analysed: 5
---

# iScanner — manual research checked against screenshots

Basis: Harshil's manual notes (`final_analysis.md`), checked against 5 screenshots in `harshil-screenshots/scanning/iscanner/` (IMG_5343–5347, 2 Oct 2026, 8:39–8:48). Only 5 screens, so most feature and flow claims are manual-only. ₹ = India storefront; US prices [UNKNOWN].

## Manual findings vs screenshots

| Manual finding | Screenshot check | Verdict |
|---|---|---|
| Took time to load initially | Not capturable in stills | Manual-only |
| ~4-step onboarding | Only welcome screen captured (5343): "#1 Scanning App", "130M+ users worldwide", "4.8 App Store Rating", Continue | Steps between not captured [UNKNOWN] |
| Repeatedly nudged to paid plan | 3 different paywalls captured: 5344 (8:40), 5345/5346 (8:41), 5347 (8:48) | Confirmed [OBSERVED] |
| Close/cancel option camouflaged | "Cancel" is small plain text top-left on a photo (5344, 5347) and over a busy tile background (5345–5346); Continue is a large bright button | Supported [OBSERVED]; "intentional" is [INFERRED] |
| **7-day free trial, then ~₹599/week** | 5344: "Not sure yet? Try it for free!" (trial length not shown), "Weekly Access ₹599.00 per week", "Yearly Access Just ₹2,999.00 per year — ₹57.00 per week" (BEST OFFER). 5345/5346: "3-Day Free Trial then ₹499.00 per week", "No payment now" | **Corrected:** ₹599/week confirmed; "7-day" not seen anywhere — the only stated trial is **3 days, then ₹499/week** |
| **~₹1,499/week** | 5345/5346: "Yearly Plan Just ₹1,499.00 per year — ₹28.57 per week", badge "SAVE 94%" | **Corrected:** ₹1,499 is **per year**, not per week |
| (not in manual) | 5347: "An exclusive discount for you! This offer expires once dismissed." "56% OFF" ~~₹15,588.00~~ ₹6,900.00/year, countdown 00:00:2:55, "Get 56% Off Now" / "Miss This Offer" | New: countdown discount + confirm-shaming button [OBSERVED] |
| Features: scanner, fax, PDF edit, AI, invoice, file/gallery/camera import | Tile labels behind paywall (5345–5346): Add photos, Mark up docs, Sign docs, Recognize text, Convert to TXT, Create CVs, Convert to PPT, Correct docs, Share, Get EDU bonus, partial "…ress files", "…axes", "Sc… rooms". Paywall bullets: Unlimited scanning, File compressor, Advanced PDF editor | Broad toolset confirmed; Fax/Invoice/AI tiles not clearly visible (only partial "…axes") — manual-only |
| ~1 page free, then paywall | Not in screenshots | Manual-only |
| Direct Files/Gallery/Camera access; good navigation | Home screen not captured | Manual-only |

## Price spread captured (one session, 3 offers) [OBSERVED]

| Screen | Weekly | Yearly | Trial |
|---|---|---|---|
| 5344 | ₹599/week | ₹2,999/year | "Try it for free!" (length not shown) |
| 5345–5346 | ₹499/week after trial | ₹1,499/year | 3-Day Free Trial, "No payment now" |
| 5347 | — | ₹6,900/year ("56% OFF" from ₹15,588) | — |

The same session shows three different yearly prices (₹2,999, ₹1,499, ₹6,900). Why (A/B test, entry point, offer stage) is [UNKNOWN].

## Lens measures (only what 5 screens show)

1. **First win:** not captured [UNKNOWN].
2. **Ask ledger:** welcome → paywall (8:40) → paywall (8:41) → discount paywall (8:48). Asks between not captured.
5. **Feel-bad:** "This offer expires once dismissed" + countdown (false urgency); "Miss This Offer" (confirm-shaming); low-contrast Cancel; "SAVE 94%" anchor.
6. **Paywall:** soft (Cancel present on all), repeated, prices shift between screens.
8. **Feature map:** wide toolset (CV, PPT, TXT, compress, sign, OCR). Most is bloat for the scan job [INFERRED].

## Keep / Kill / Different
- **Keep:** one home grid of clear task tiles (per manual; tiles seen on 5345).
- **Kill:** countdown "expires once dismissed" offer, "Miss This Offer", low-contrast Cancel, multiple inconsistent prices.
- **Different:** one price, one trial length, same on every paywall [INFERRED].

## Open / unverified
- 7-day trial (not seen; screens say 3-day). Free-page limit. Fax/Invoice/AI tools. Onboarding step count. Home screen layout.
