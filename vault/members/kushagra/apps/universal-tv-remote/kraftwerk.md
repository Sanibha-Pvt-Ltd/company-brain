---
type: app
category: universal-tv-remote
app: TV Remote by Kraftwerk
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:7]
---

# TV Remote by Kraftwerk — screenshot teardown

**Scope.** Screens-only review of team capture `tvremote by kraftwerk.pdf` (PDF created 2026-10-03; 7 pages). Pages are grouped only where adjacent screenshots show the same flow; every page is indexed. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews, App Store ID and US pricing are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | TV-device picker with “Searching for device…” and a blank result list. | Wait for scan; “Select device to connect.” | Explains discovery is in progress; no device result is shown. | `“Select a device to connect.”` | pairing progress | [INFERRED] Asking the user to wait without a result; capture cannot establish scan duration. | `tvremote by kraftwerk.pdf`, p. 1 |
| 2–5 | Four onboarding cards explain remote basics, familiar buttons, touchpad/keyboard navigation, and device compatibility. | Continue through each card; Skip is visible. | Promises ease of control, app navigation and compatibility. | `“Your TV Remote, Now on iPhone.”` | feature preview | [INFERRED] Four promotional screens occur before the next captured device scan. | `tvremote by kraftwerk.pdf`, p. 2–5 |
| 6 | Premium screen: touchpad benefit, annual plan selected, weekly alternative, 3-day trials on both plans. | Choose plan and Continue; close X and Restore Purchases visible. | Discloses an annual ₹3,499.00 plan or ₹299.00/week, each with a 3-day free trial. | `“Get Access to All Features.”` | trial conversion | [OBSERVED] India storefront. Trial toggle/default behavior cannot be established from the still. | `tvremote by kraftwerk.pdf`, p. 6 |
| 7 | Return to “Select a device to connect” search state. | Wait/scan again. | The screenshot does not show a found TV or working command. | `“Select a device to connect.”` | pairing retry | [OBSERVED] The capture ends at search, so onboarding and offer did not establish connection. | `tvremote by kraftwerk.pdf`, p. 7 |

## Eight screen lenses

1. **First win.** No TV list item or remote command is captured. First working control and taps to reach it are [UNKNOWN]; the last page is still searching (p. 7).
2. **Ask ledger.** Search/wait p. 1; four Continue/Skip onboarding cards p. 2–5; plan choice/payment CTA p. 6; another search p. 7. The PDF is an ordered capture, not proof of one tap path.
3. **Abstractions.** Touchpad, keyboard and “all features” are introduced before any pairing result. [OBSERVED] [INFERRED] Brand/device picker and pairing status are essential; the other controls can be explained when available.
4. **Feel-good moments.** The onboarding cards preview keyboard/touchpad benefits (pp. 2–5). [OBSERVED] These are promises, not earned success.
5. **Feel-bad moments.** The user sees a waiting search at both ends (pp. 1, 7), with four product-benefit cards and a paywall between. [OBSERVED] Stills do not establish the scan’s true duration or whether the user can bypass.
6. **Paywall.** P. 6: ₹3,499/year and ₹299/week; both display a 3-day free trial; annual is selected in the screenshot and a close X is visible. [OBSERVED] India storefront, 2026-10-03. Payment and trial default in the live flow [UNKNOWN].
7. **Repeat cost.** No connected remote is shown, so repeat tap cost and command result are [UNKNOWN].
8. **Feature map.** [INFERRED] Table stakes: discovery, retry/help and power/navigation. Differentiator: keyboard/touchpad (p. 3–4 preview). Bloat: four benefit cards before a found-device state.

## Keep / Kill / Different

- **Keep.** [OBSERVED] Keep the Skip control and the clear visual previews for keyboard/touchpad (pp. 2–5).
- **Kill.** [INFERRED] The four-card carousel plus premium offer before a discoverable TV/usable remote (pp. 1–7).
- **Different.** [INFERRED] Start on the TV picker, show discovered devices with retry/manual help, then test power/navigation. Explain touchpad/keyboard on demand and show the plan only after one command works.

## Open questions and verification

- [UNKNOWN] Exact launch-to-command taps/time; stills do not prove page order is a tap path, successful pairing, command response, repeat usage, trial selection in action, checkout, or hidden/delayed close behavior.
- [UNKNOWN] App Store ID, current US prices, listing/reviews, actual TV compatibility and whether all TV brands require the same local-network setup.
- **Checked:** all 7 pages of `tvremote by kraftwerk.pdf` were visually inspected in rendered contact sheets. Offer details are transcribed from a full-size rendering of the cited page; amounts are India storefront, captured 2026-10-03.
