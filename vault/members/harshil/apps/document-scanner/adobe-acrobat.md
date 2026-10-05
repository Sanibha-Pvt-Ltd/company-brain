---
type: app
category: document-scanner
app: Adobe Acrobat Reader
app_store_id: "[UNKNOWN]"
member: harshil
updated: 2026-10-05
status: draft
scope: screens-only
sources: [final_analysis.md, screenshots:9]
reviews_analysed: 0
screens_analysed: 9
---

# Adobe Acrobat Reader — manual research checked against screenshots

Basis: Harshil's manual notes (`final_analysis.md`, section "Adobe Acrobat – PDF Suite"), checked against 9 screenshots in `harshil-screenshots/scanning/adobe acrobat/` (IMG_5314–5322, 8:16–8:20). Splash names the app "Adobe Acrobat Reader" (5314). ₹ = India storefront; US prices [UNKNOWN].

## Manual findings vs screenshots

| Manual finding | Screenshot check | Verdict |
|---|---|---|
| Very clean onboarding, no questions/permissions up front | Splash (5314) → sign-in (5315) → plan comparison (5316) → home (5317). No permission prompt captured | Confirmed [OBSERVED] |
| Sign-in on first screen, can be closed | "Welcome to Acrobat Reader", Sign in with Apple/Google/Facebook/Adobe, X top-right (5315) | Confirmed [OBSERVED] |
| Still nudges account creation | Profile icon on home (5317); no further sign-in screen captured | Partly; only first-screen ask seen |
| Creating PDFs requires payment | Create PDF, Edit PDF, Combine files carry crown badge (5317, 5322); "Convert this file to PDF" paywall (5321); plan table: "Convert documents or images to PDFs" Premium only (5316) | Confirmed [OBSERVED] |
| 7-day free trial | "Start 7-day free trial" (5316, 5321); banner "Try for 7 days" (5317) | Confirmed [OBSERVED] |
| ~₹2,599/year | "Yearly: ₹2,599.00 (₹216.58/mo)", "Save 38%" (5316, 5321) | Confirmed [OBSERVED] |
| **~₹599/month** | "Monthly: ₹349.00" (5316, 5321). Harshil's handwritten notes (visible in Scanner App IMG_5335) also say "Monthly 349" | **Corrected: ₹349/month** — ₹599 is a typo in the typed notes |
| Free: view, sign, podcast, read aloud | Plan table Free column: "Read PDFs, highlight, and comment", "Share files, collect feedback", "Fill and sign forms" (5316). Generate podcast tile and "New" badge, no crown (5317, 5322). Speaker icon in viewer toolbar (5318–5319) | View + sign confirmed; podcast/read-aloud shown without crown, but whether free to use is [UNKNOWN] |
| Simple UI but AI options exposed | Home: Create PDF Space, Generate podcast (5317); viewer: "Generative summary — Continue", "AI Assistant" button (5318–5319); + menu: Ask AI Assistant (5322) | Confirmed [OBSERVED] |

## Screen map

| # | File | Stage | What user sees | Ask / friction | Tag |
|---|---|---|---|---|---|
| 1 | 5314 | launch | Splash "Adobe Acrobat Reader" | — | [OBSERVED] |
| 2 | 5315 | account | 4 sign-in options, X | Account ask before value; skippable | [OBSERVED] |
| 3 | 5316 | paywall | Free vs Premium table; yearly ₹2,599 / monthly ₹349; "Start 7-day free trial"; X | Soft paywall before first use | [OBSERVED] |
| 4 | 5317 | home | "Unlock premium features… Try for 7 days" banner; tiles Create PDF👑, Edit PDF👑, Fill & Sign, Create PDF Space, Generate podcast; "Welcome" PDF 590 KB; "Connect cloud storage accounts" | Banner + cloud-connect card | [OBSERVED] |
| 5 | 5318 | upsell | Welcome PDF open, "Generative summary — Continue" bar + sheet "Full access to Generative summary — Summarize" | AI upsell on first file open | [OBSERVED] |
| 6 | 5319 | viewer | Welcome PDF, toolbar Draw/Text/Fill & Sign/Edit PDF👑/More tools, "AI Assistant" | — | [OBSERVED] |
| 7 | 5320 | home | Same as 5317 | — | [OBSERVED] |
| 8 | 5321 | paywall | "Convert this file to PDF", same prices | Gate on create | [OBSERVED] |
| 9 | 5322 | menu | Create PDF Space, Open File, **New scan**, Ask AI Assistant, Generate podcast (New), Edit PDF👑, Create PDF👑, Combine files👑 | "New scan" has no crown | [OBSERVED] |

## Lens measures
1. **First win:** Welcome PDF opened (5318) — preloaded sample, not user's doc. User scan result not captured.
2. **Ask ledger:** sign-in (nothing given) → plan table (nothing given) → home → AI upsell on first open → convert paywall.
3. **Abstractions:** PDF Spaces, Generative summary, AI Assistant, podcast — all invented beyond the scan job [INFERRED].
5. **Feel-bad:** Paywall shown before any use (5316); premium crowns on core "Create PDF".
6. **Paywall:** soft (X), 7-day trial, yearly pre-selected, clear billing copy ("Billing begins when your free trial ends… Cancel anytime in your Apple account").
8. **Feature map:** Acrobat is a PDF suite; scanning is one menu item (5322), not the core.

## Keep / Kill / Different
- **Keep:** clear Free vs Premium table (5316); honest trial billing copy.
- **Kill:** paywall before first use; gating "Create PDF" for a scan-to-PDF job.
- **Different:** scan-first home, not a menu entry [INFERRED].

## Open / unverified
- Whether a scan from "New scan" exports to PDF free. Whether podcast/read-aloud are free to run.
