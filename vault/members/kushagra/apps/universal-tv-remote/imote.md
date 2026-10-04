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
| 1 | App launch. | None visible. | No real-TV action outcome can be concluded from stills. | `“imote”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `remoteControl.pdf`, pp. 1 |
| 2 | Local-network permission prompt. | Allow or deny local network access. | No real-TV action outcome can be concluded from stills. | `“Allow ‘Remote Control’ to find devices on local networks?”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `remoteControl.pdf`, pp. 2 |
| 3–4 | Two-step pairing instructions: power TV on, confirm prompt/code. | Next and Go to search. | No real-TV action outcome can be concluded from stills. | `“Confirm the pairing.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `remoteControl.pdf`, pp. 3–4 |
| 5 | TV search with troubleshooting link. | Wait/search; open help. | No real-TV action outcome can be concluded from stills. | `“Searching for your TV…”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `remoteControl.pdf`, pp. 5 |
| 6–9 | Remote control variants (main pad, touchpad, number keypad) with persistent connect-to-TV CTA. | Use remote or connect TV; connection is not confirmed. | No real-TV action outcome can be concluded from stills. | `“Connect to your TV.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `remoteControl.pdf`, pp. 6–9 |
| 10–11 | Apps empty state and cast-photo/video tiles. | Connect TV or choose media. | No real-TV action outcome can be concluded from stills. | `“Oops! No TV found.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `remoteControl.pdf`, pp. 10–11 |
| 12–14 | Settings and ad banner surfaces. | Premium/restore, haptic/touch feedback, skin, device and support options. | No real-TV action outcome can be concluded from stills. | `“GO PRO.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `remoteControl.pdf`, pp. 12–14 |

## Eight screen lenses

1. **First win.** Pairing screen p. 5 searches; remote UI p. 6 appears with a “Connect to your TV” button. [OBSERVED] No connected TV/command result is proven.
2. **Ask ledger.** Local network permission p. 2; power-on/pairing steps p. 3–4; scan p. 5; repeated connect CTA p. 6–9; TV not found p. 10; premium offer p. 7.
3. **Abstractions.** Local network, pairing code, remote mode, touchpad, number pad, apps and casting are shown. [OBSERVED] [INFERRED] Remote mode variants are useful after pairing; empty app/cast tabs do not explain how to pair.
4. **Feel-good moments.** Pairing is taught with an illustration and two explicit steps p. 3–4. [OBSERVED] Helpful setup is the clearest good moment.
5. **Feel-bad moments.** Users are asked for local network access before pairing instructions (p. 2). Search can end at “Oops! No TV found” p. 10. [OBSERVED] No scary copy/close delay proven.
6. **Paywall.** Premium appears p. 7, “3-day free trial” then ₹499/week; annual access ₹1,999/year. [OBSERVED] India storefront, captured 2026-10-03. Full-resolution p. 7 checked; no claim about hard gate.
7. **Repeat cost.** Three control modes p. 6–9, but persistent connect CTA remains. [OBSERVED] No actual repeat command/path.
8. **Feature map.** [INFERRED] Table stakes: local-network explanation before prompt, pairing recovery and working controls. Differentiator: remote/touchpad/keypad modes. Bloat: ad banner and premium screen while unpaired.

## Keep / Kill / Different

- **Keep.** [OBSERVED] Keep the two illustrated pairing steps and connect CTA (pp. 3–6).
- **Kill.** Remove premium placement and ad clutter from the still-unpaired connection sequence (pp. 5–10). [INFERRED]
- **Different.** Explain local network before the OS permission, pair a TV, then test power/navigation before upsell. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 14 pages of `remoteControl.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
