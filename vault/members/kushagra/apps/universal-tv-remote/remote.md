---
type: app
category: universal-tv-remote
app: TV Remote (screenshot capture name remote.pdf)
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:6]
---

# TV Remote (screenshot capture name remote.pdf) — screenshot teardown

**Scope.** Screens-only review of team capture `remote.pdf` (PDF created 2026-10-03; 6 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1 | Remote layout with TV not connected. | Connect TV. | [OBSERVED] Remote layout with TV not connected. | `“TV is not connected.”` (representative copy visible in this span) | pairing progress | [INFERRED] Asks user to connect TV. Still images cannot establish timing, hard gating or action success. | `remote.pdf`, pp. 1 |
| 2 | Apps tab empty state. | Connect TV. | [OBSERVED] Apps tab empty state. | `“Not connected.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to connect TV. Still images cannot establish timing, hard gating or action success. | `remote.pdf`, pp. 2 |
| 3 | Settings with premium unlock, haptics, touchpad lock, mobile power, forgotten devices and FAQ. | Unlock premium or connect/manage a TV. | [OBSERVED] Settings with premium unlock, haptics, touchpad lock, mobile power, forgotten devices and FAQ. | `“Unlock Premium.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to unlock premium or connect/manage a TV. Still images cannot establish timing, hard gating or action success. | `remote.pdf`, pp. 3 |
| 4 | Premium feature/paywall screen. | Continue trial/paid access. | [OBSERVED] Premium feature/paywall screen. | `“GET PRO ACCESS.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to continue trial/paid access. Still images cannot establish timing, hard gating or action success. | `remote.pdf`, pp. 4 |
| 5–6 | Connection scan/search followed by another paywall. | Wait/search; troubleshoot link, then premium CTA. | [OBSERVED] Connection scan/search followed by another paywall. | `“Connect to your TV.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to wait/search; troubleshoot link, then premium CTA. Still images cannot establish timing, hard gating or action success. | `remote.pdf`, pp. 5–6 |

## Eight screen lenses

1. **First win.** Remote screen p. 1 itself says TV is not connected; Apps is empty p. 2. [OBSERVED] No successful control shown; first win/taps unknown.
2. **Ask ledger.** Connect prompt from remote/apps p. 1–2; premium offer p. 3–4; connection scan p. 5; repeated premium p. 6.
3. **Abstractions.** Touchpad, mobile power, forgotten devices, app list and “premium” are shown. [OBSERVED] [INFERRED] Pairing status and core controls are needed; touchpad unlock creates a feature distinction.
4. **Feel-good moments.** The dark remote layout groups arrows, OK, channel, home and media controls on one screen p. 1. [OBSERVED] No confirmation feedback shown.
5. **Feel-bad moments.** Premium is reached from Settings p. 3 and repeated at p. 4/6 while TV remains disconnected. [OBSERVED] The resulting price/gate is not clearly legible in contact sheets and is [UNKNOWN] here.
6. **Paywall.** P. 4 shows “YEARLY ACCESS Just ₹1,999 per year” (₹38.33/week) and a “3-DAY FREE TRIAL then ₹499.00 per week” option. [OBSERVED] INR is displayed; US pricing is unknown. PDF metadata creation date is 2026-10-03; screenshot capture date is unknown. P. 6 repeats the offer. Close timing/hard gate remain unknown.
7. **Repeat cost.** Connection search p. 5 and controls p. 1; no paired session. [OBSERVED] Repeat cost unknown.
8. **Feature map.** [INFERRED] Table stakes: discover, pair, control. Differentiator: touchpad and mobile power. Bloat risk: upsell controls before establishing that this TV can pair.

## Keep / Kill / Different

- **Keep.** [INFERRED] Keep the standard arrow/OK/home/volume remote layout (p. 1).
- **Kill.** Remove the premium prompt reached from settings while no TV is connected (pp. 3–6). [INFERRED]
- **Different.** Put a clear TV picker and troubleshooting path first; offer touchpad premium after a successful basic command. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 6 pages of `remote.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
