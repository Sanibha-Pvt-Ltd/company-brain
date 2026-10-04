---
type: app
category: universal-tv-remote
app: TV Remote
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:7]
---

# TV Remote — screenshot teardown

**Scope.** Screens-only review of `tvremoteapp.pdf` (PDF created 2026-10-03; 7 pages). Companion analysis PDF is secondary and was not used as evidence. App Store ID, listing, reviews and US pricing are unavailable. [UNKNOWN]

## Per-screen table

| Screen | What user sees | Visible ask | What it gives | Verbatim copy | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | App Tracking Transparency system prompt over a loading screen. | Allow or ask not to track. | Explains that tracking supports attribution (Facebook/Google ads). | “Allow ‘TV Remote’ to track your activity across other companies’ apps and websites?” | tracking permission | [OBSERVED] Permission comes before the app’s remote benefit is introduced. | `tvremoteapp.pdf`, p. 1 |
| 2 | Illustrated overview of phone as TV remote. | Continue. | Promises one app for smart TV control. | “TURN YOUR PHONE INTO A SMART TV CONTROLLER.” | benefit preview | [OBSERVED] | `tvremoteapp.pdf`, p. 2 |
| 3 | TV-search illustration with keyboard/touchpad. | Continue. | Promises faster TV searching and text input. | “MAKE TV SEARCHING A NO-BRAINER.” | benefit preview | [OBSERVED] | `tvremoteapp.pdf`, p. 3 |
| 4 | Customizable-control feature illustration. | Continue. | Promises quick customization. | “FULLY CUSTOMIZABLE, QUICK & EASY TO USE.” | benefit preview | [OBSERVED] Four promotional screens precede any device picker in this capture. | `tvremoteapp.pdf`, p. 4 |
| 5 | Premium feature screen. | Continue toward trial. | Lists full TV control and paid access. | “GET FULL ACCESS TO UNIVERSAL TV REMOTE.” | trial conversion | [OBSERVED] No connected TV or working control is shown first. | `tvremoteapp.pdf`, p. 5 |
| 6 | Apple in-app purchase sheet with three-day trial. | Confirm with side button or close. | Shows the native subscription confirmation and trial term. | “3-day free trial.” | payment | [OBSERVED] This is a purchase confirmation surface, not evidence that payment completed. | `tvremoteapp.pdf`, p. 6 |
| 7 | Plan-selection sheet titled “Choose your plan to Universal TV Remote.” | Select plan and start trial. | Presents trial/monthly/yearly choices. | “CHOOSE YOUR PLAN TO UNIVERSAL TV REMOTE.” | plan selection | [OBSERVED] The captured pages end without a TV selection or remote screen. | `tvremoteapp.pdf`, p. 7 |

## Eight screen lenses

1. **First win.** No device picker, paired state or working control appears in these seven pages. [OBSERVED] First win/taps and whether remote control is gated are [UNKNOWN].
2. **Ask ledger.** Tracking permission p. 1; four Continue actions on benefit cards p. 2–5; purchase confirmation p. 6; plan choice p. 7. This page order does not prove one uninterrupted tap path.
3. **Abstractions.** The cards name TV control, search, keyboard and customization. [OBSERVED] [INFERRED] Brand/device selection and pairing are the only necessary concepts before a first command.
4. **Feel-good moments.** The control/search illustrations make the product’s intended benefit easy to picture (pp. 2–4). [OBSERVED] They are promotional previews, not earned control success.
5. **Feel-bad moments.** ATT tracking permission opens before the app explains its core function (p. 1), followed by several promotion screens before connection. [OBSERVED] No delay/hidden close claim can be made.
6. **Paywall.** Premium screen p. 5, Apple purchase sheet p. 6, plan selector p. 7. The Apple sheet visibly offers a 3-day free trial then ₹999/week. [OBSERVED] INR is displayed; US pricing is unknown. PDF metadata creation date is 2026-10-03; screenshot capture date is unknown. No payment success or plan default is established.
7. **Repeat cost.** No remote screen or connected device appears; repeat action cost is [UNKNOWN].
8. **Feature map.** [INFERRED] Table stakes: TV picker, pairing state, power/navigation. Differentiator: keyboard and touchpad search (p. 3). Bloat risk: four feature cards and a premium ask before proving compatibility.

## Keep / Kill / Different

- **Keep.** [INFERRED] Keep the simple keyboard/touchpad explanation (p. 3).
- **Kill.** [INFERRED] Remove the ATT prompt and premium sequence from before TV selection (pp. 1–7).
- **Different.** [INFERRED] Show TV picker and connection requirements first, then let the user test one command before presenting optional text-entry tips or payment.

## Open questions and verification

- [UNKNOWN] Exact tap count/time to first control, whether the offer is a hard gate, exit/close timing, selected plan behavior, successful purchase, compatibility and command response.
- [UNKNOWN] US storefront, listing/reviews, App Store ID, repeat use and notification behavior.
- **Checked:** all 7 pages were visually inspected in the rendered contact sheet; the premium/payment pages p. 5–7 and tracking prompt p. 1 were re-opened as full-size renders. Price is India storefront, not a US estimate.
