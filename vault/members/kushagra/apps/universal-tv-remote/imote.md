---
type: app
category: universal-tv-remote
app: iMote / Remote Control
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:14]
---

# iMote / Remote Control — screenshot teardown

**Scope.** Screens-only review of team capture `remoteControl.pdf` (PDF created 2026-10-03; 14 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | App launch. | None visible. | [OBSERVED] App launch. | `“imote”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to none visible. Still images cannot establish timing, hard gating or action success. | `remoteControl.pdf`, pp. 1 |
| 2 | Local-network permission prompt. | Allow or deny local network access. | [OBSERVED] Local-network permission prompt. | `“Allow ‘Remote Control’ to find devices on local networks?”` (representative copy visible in this span) | permission cost | [INFERRED] Asks user to allow or deny local network access. Still images cannot establish timing, hard gating or action success. | `remoteControl.pdf`, pp. 2 |
| 3–4 | Two-step pairing instructions: power TV on, confirm prompt/code. | Next and Go to search. | [OBSERVED] Two-step pairing instructions: power TV on, confirm prompt/code. | `“Confirm the pairing.”` (representative copy visible in this span) | pairing progress | [INFERRED] Asks user to next and Go to search. Still images cannot establish timing, hard gating or action success. | `remoteControl.pdf`, pp. 3–4 |
| 5 | TV search with troubleshooting link. | Wait/search; open help. | [OBSERVED] TV search with troubleshooting link. | `“Searching for your TV…”` (representative copy visible in this span) | pairing progress | [INFERRED] Asks user to wait/search; open help. Still images cannot establish timing, hard gating or action success. | `remoteControl.pdf`, pp. 5 |
| 6 | Main remote screen with persistent connect-to-TV CTA. | Connect to TV. | Main directional and media controls are visible. | `“Connect to your TV.”` | core control | [OBSERVED] The CTA remains; pairing/command success is not shown. | `remoteControl.pdf`, p. 6 |
| 7 | Premium offer appears over TV imagery. | Trial/plan choice and Continue for Free. | 3-Day Full Access at ₹0; Yearly Access at ₹76.90 per week; ₹999.00/week auto-renewable is also shown. | `“Simplify your TV time.”` | trial conversion | [OBSERVED] Trial control appears enabled and 3-Day Full Access selected in this screenshot; live default behavior is unknown. INR displayed; US price unknown. | `remoteControl.pdf`, p. 7 |
| 8–9 | Touchpad and number keypad remote variants with persistent connect-to-TV CTA. | Connect to TV. | Two additional input modes are visible. | `“Connect to your TV.”` | control-mode discovery | [OBSERVED] No paired command is demonstrated. | `remoteControl.pdf`, pp. 8–9 |
| 10–11 | Apps empty state and cast-photo/video tiles. | Connect TV or choose media. | [OBSERVED] Apps empty state and cast-photo/video tiles. | `“Oops! No TV found.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to connect TV or choose media. Still images cannot establish timing, hard gating or action success. | `remoteControl.pdf`, pp. 10–11 |
| 12–14 | Settings and ad banner surfaces. | Premium/restore, haptic/touch feedback, skin, device and support options. | [OBSERVED] Settings and ad banner surfaces. | `“GO PRO.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to premium/restore, haptic/touch feedback, skin, device and support options. Still images cannot establish timing, hard gating or action success. | `remoteControl.pdf`, pp. 12–14 |

## Eight screen lenses

1. **First win.** Pairing screen p. 5 searches; remote UI p. 6 appears with a “Connect to your TV” button. [OBSERVED] No connected TV/command result is proven.
2. **Ask ledger.** Local network permission p. 2; power-on/pairing steps p. 3–4; scan p. 5; repeated connect CTA p. 6–9; TV not found p. 10; premium offer p. 7.
3. **Abstractions.** Local network, pairing code, remote mode, touchpad, number pad, apps and casting are shown. [OBSERVED] [INFERRED] Remote mode variants are useful after pairing; empty app/cast tabs do not explain how to pair.
4. **Feel-good moments.** Pairing is taught with an illustration and two explicit steps p. 3–4. [OBSERVED] Helpful setup is the clearest good moment.
5. **Feel-bad moments.** Users are asked for local network access before pairing instructions (p. 2). Search can end at “Oops! No TV found” p. 10. [OBSERVED] No scary copy/close delay proven.
6. **Paywall.** P. 7 shows “3-Day Full Access” at ₹0 selected, “Yearly Access” at ₹76.90/week and a ₹999.00/week auto-renewable line. [OBSERVED] INR displayed; US price unknown. Full-size page checked. The screenshot does not show the trial’s later renewal amount or prove the control is selected by default in the live flow.
7. **Repeat cost.** Three control modes p. 6–9, but persistent connect CTA remains. [OBSERVED] No actual repeat command/path.
8. **Feature map.** [INFERRED] Table stakes: local-network explanation before prompt, pairing recovery and working controls. Differentiator: remote/touchpad/keypad modes. Bloat: ad banner and premium screen while unpaired.

## Keep / Kill / Different

- **Keep.** [INFERRED] Keep the two illustrated pairing steps and connect CTA (pp. 3–6).
- **Kill.** Remove premium placement and ad clutter from the still-unpaired connection sequence (pp. 5–10). [INFERRED]
- **Different.** Explain local network before the OS permission, pair a TV, then test power/navigation before upsell. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 14 pages of `remoteControl.pdf` were visually inspected from rendered contact sheets. The offer page p. 7 was separately checked at full size. INR amounts are those visible in the supplied capture; screenshot capture date and US pricing are unknown.
