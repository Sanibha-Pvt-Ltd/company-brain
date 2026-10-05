---
type: app
category: document-scanner
app: Adobe Scan
app_store_id: "[UNKNOWN]"
member: harshil
updated: 2026-10-05
status: draft
scope: screens-only
sources: [final_analysis.md, screenshots:5]
reviews_analysed: 0
screens_analysed: 5
---

# Adobe Scan — manual research checked against screenshots

Basis: Harshil's manual notes (`final_analysis.md`), checked against 5 screenshots in `harshil-screenshots/scanning/adobe scan/` (IMG_5323–5327, 8:21–8:25). ₹ = India storefront; US prices [UNKNOWN].

## Manual findings vs screenshots

| Manual finding | Screenshot check | Verdict |
|---|---|---|
| Cannot use without sign-in | "Welcome to Adobe Scan", Sign in with Apple/Google/Facebook, "Already have an Adobe account? Sign in or sign up." No X or skip visible (5323) | Confirmed: no skip shown [OBSERVED] |
| After sign-in, paywall shown, skippable | "Upgrade your free plan" with X top-right (5324, 8:23) | Confirmed [OBSERVED] |
| ~3 clicks incl. camera + notification permissions | Pre-prompt: "Your scans will be processed in and saved to Adobe cloud storage. To get started, please provide permission to access your camera and to receive app notifications." OK (5325) | Confirmed; system prompts themselves not captured [OBSERVED] |
| Premium ~₹849/month | "PREMIUM ₹849.00/mo"; "Try Premium for 7 days, then ₹849.00/mo" (5324) | Confirmed [OBSERVED] |
| Plus ~₹499/month | "PLUS ₹499.00/mo or ₹1,999.00/yr" (5324) | Confirmed; yearly ₹1,999 added [OBSERVED] |
| 7-day free trial | "Start 7-day free trial"; "Only one free trial per product per customer." (5324) | Confirmed [OBSERVED] |
| Lands directly in scanning | Camera view with modes …teboard/Book/Document/ID card/Busine…, Scan / Ask AI toggle (5325, 5326) | Confirmed [OBSERVED] |
| Basic scan → PDF free | No completed scan captured; home empty "You don't have any scans" (5327) | Manual-only [UNKNOWN in screens] |
| Premium features: Edit Text, Magic Eraser, Cleanup | Plan table: Edit text in scans (Plus+Premium), Resize scans (both), Clean up scans (both), Magic eraser (Premium), capture modes Book/Business card/ID (Plus+Premium), high-speed scan, Export to Word/Excel/JPG, Extract pages (Premium) (5324) | Confirmed and extended [OBSERVED] |
| Repeated trial nudges | Only one paywall captured; camera top bar has camera icon with blue star badge (5325–5326) | One nudge seen; "repeated" manual-only |

## Screen map

| # | File | Stage | What user sees | Ask / friction | Tag |
|---|---|---|---|---|---|
| 1 | 5323 | account | Sign-in wall, no skip; "Adobe collects analytics to improve your experience." | Hard account gate before value | [OBSERVED] |
| 2 | 5324 | paywall | Plus vs Premium table, Premium pre-selected, 7-day trial, X | Soft | [OBSERVED] |
| 3 | 5325 | permission | Pre-prompt for camera + notifications together, cloud storage statement | Notification ask bundled with camera | [OBSERVED] |
| 4 | 5326 | core | Live camera, "Tap the screen when you're ready to scan. We'll find the borders, and take the photo for you." | Good guidance | [OBSERVED] |
| 5 | 5327 | home | "You don't have any scans", tabs Home/Files, big camera + | — | [OBSERVED] |

## Lens measures
1. **First win:** camera reached after sign-in + paywall + permissions (5326). Completed scan not captured.
2. **Ask ledger:** account (nothing given) → paywall (nothing given) → camera + notifications (nothing given) → scan.
3. **Abstractions:** Plus vs Premium tiers; capture modes; Ask AI.
5. **Feel-bad:** mandatory account; notification ask bundled with camera; scans saved to cloud (privacy cost).
6. **Paywall:** soft, 2 tiers, Premium pre-selected, clear trial terms.
7. **Repeat cost:** home has one big camera button (5327) — low.

## Keep / Kill / Different
- **Keep:** auto border detection + "we'll take the photo for you" guidance (5326); clear tier table (5324).
- **Kill:** sign-in wall (5323); notification permission bundled with camera (5325).
- **Different:** on-device, no account, camera on first tap [INFERRED].

## Open / unverified
- Free PDF export of a basic scan (manual says yes, not captured). Repeated nudges.
