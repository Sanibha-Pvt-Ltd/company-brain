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

**Scope.** Screens-only review of team capture `tvremote by kraftwerk.pdf` (PDF created 2026-10-03; 7 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | TV-brand picker with Continue. | Choose brand and continue. | No real-TV action outcome can be concluded from stills. | `“Please select your TV brand!”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `tvremote by kraftwerk.pdf`, pp. 1 |
| 2 | Connection progress overlay. | Wait for connection. | No real-TV action outcome can be concluded from stills. | `“We’re connecting to your TV. Please wait a moment.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `tvremote by kraftwerk.pdf`, pp. 2 |
| 3–4 | Feedback/rating request screen(s). | Give feedback; choices visible. | No real-TV action outcome can be concluded from stills. | `“App improvements.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `tvremote by kraftwerk.pdf`, pp. 3–4 |
| 5 | Device-found celebration and premium plan offer. | Trial toggle and plan selection. | No real-TV action outcome can be concluded from stills. | `“Device found.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `tvremote by kraftwerk.pdf`, pp. 5 |
| 6 | Trial reminder/benefit explainer. | Start free trial. | No real-TV action outcome can be concluded from stills. | `“3 Days Free No Risk.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `tvremote by kraftwerk.pdf`, pp. 6 |
| 7 | Remote-control home with TV backdrop and promotional branding. | Use controls; successful commands unverified. | No real-TV action outcome can be concluded from stills. | `“TV Remote.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `tvremote by kraftwerk.pdf`, pp. 7 |

## Eight screen lenses

1. **First win.** Brand picker p. 1, “Device found” paywall p. 5, remote p. 7. [OBSERVED] Device discovery appears successful in a screen, but no command response is shown.
2. **Ask ledger.** Choose brand p. 1; wait p. 2; feedback p. 3–4; trial/plan p. 5–6; remote p. 7.
3. **Abstractions.** Brand selection and device-found state are direct; weekly/annual trial plans and rating feedback are additional concepts. [OBSERVED] [INFERRED] Feedback is not part of the control job.
4. **Feel-good moments.** “Device found” p. 5 precedes the remote p. 7, an explicit reassurance state. [OBSERVED] It does not prove a command worked.
5. **Feel-bad moments.** Feedback ask follows connecting (p. 3–4) and precedes/overlaps the paid offer (p. 5). [OBSERVED] No trick/close timing proven.
6. **Paywall.** P. 5 shows free-trial toggle off and 3-day full access ₹0, yearly ₹76.90/week, and ₹999/week auto-renewable. P. 6 says 3 days free, then ₹999/week. [OBSERVED] India storefront, captured 2026-10-03. Confirm toggles and renewal terms in a hands-on run.
7. **Repeat cost.** Remote controls appear p. 7; connected TV and command response unknown. No repeat path captured.
8. **Feature map.** [INFERRED] Table stakes: brand selection, clear pairing state and core buttons. Differentiator: visible successful-discovery state. Bloat: mandatory feedback screen and premium interstitial before control is verified.

## Keep / Kill / Different

- **Keep.** [OBSERVED] Keep the short feature illustrations and persistent Skip affordance (pp. 2–5).
- **Kill.** Remove premium after five promotional screens but before a usable remote appears (p. 6). [INFERRED]
- **Different.** Move device discovery and a working power button ahead of feature education and the subscription. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 7 pages of `tvremote by kraftwerk.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
